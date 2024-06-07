import json
import sys
from collections import deque
from graphviz import Digraph, ExecutableNotFound


class AFNDtoAFD:
    def __init__(self, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            self.afnd = json.load(f)

        self.Q = []
        self.V = self.afnd["V"]
        self.delta = {}
        self.q0 = None
        self.F = []

        if filename.endswith('.json'):
            self.load_afd_from_json(filename)
        else:
            print("Erro: O arquivo fornecido não é um arquivo JSON.")
            sys.exit(1)

    def calcular_fecho_epsilon(self, estado):
        fecho = set([estado])
        fila = deque([estado])

        while fila:
            estado_atual = fila.popleft()
            transicoes = self.afnd["delta"].get(estado_atual, {}).get("", [])
            for prox_estado in transicoes:
                if prox_estado not in fecho:
                    fecho.add(prox_estado)
                    fila.append(prox_estado)

        return fecho

    def calcular_transicoes(self, estados):
        transicoes = {}
        for simbolo in self.V:
            proximos_estados = set()
            for estado in estados:
                transicoes_estado = self.afnd["delta"].get(estado, {}).get(simbolo, [])
                proximos_estados.update(transicoes_estado)
            fecho_prox_estados = set()
            for estado in proximos_estados:
                fecho_prox_estados.update(self.calcular_fecho_epsilon(estado))
            if fecho_prox_estados:
                transicoes[simbolo] = fecho_prox_estados
        return transicoes

    def converter(self):
        fecho_q0 = tuple(sorted(self.calcular_fecho_epsilon(self.afnd["q0"])))
        self.Q.append(fecho_q0)
        fila = deque([fecho_q0])

        while fila:
            estados = fila.popleft()
            transicoes = self.calcular_transicoes(estados)

            if estados not in self.delta:
                self.delta[estados] = transicoes

                for proximos_estados in transicoes.values():
                    if proximos_estados and tuple(sorted(proximos_estados)) not in self.Q:
                        self.Q.append(tuple(sorted(proximos_estados)))
                        fila.append(tuple(sorted(proximos_estados)))

        for estado in self.Q:
            for estado_final in self.afnd["F"]:
                if estado_final in estado:
                    self.F.append(estado)
                    break

        self.q0 = fecho_q0

        delta_converted = {}
        for key, value in self.delta.items():
            new_key = ','.join(map(str, key))
            new_value = {k: list(map(str, v)) for k, v in value.items()}
            delta_converted[new_key] = new_value

        afd = {
            "Q": [sorted(map(str, q)) for q in self.Q],
            "V": self.V,
            "delta": delta_converted,
            "q0": list(map(str, self.q0)),
            "F": [sorted(map(str, f)) for f in self.F]
        }

        return afd

    def load_afd_from_json(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            afd_definition = json.load(file)

        required_keys = ["Q", "V", "delta", "q0", "F"]

        for key in required_keys:
            if key not in afd_definition:
                print(f"Erro: Chave '{key}' ausente na definição do autômato.")
                sys.exit(1)

        self.states = afd_definition["Q"]
        self.alphabet = afd_definition["V"]
        self.transitions = afd_definition["delta"]
        self.initial_state = afd_definition["q0"]
        self.final_states = afd_definition["F"]

        # Realizar mais validações conforme necessário
        print("Autômato carregado com sucesso a partir do arquivo JSON.")

    def generate_graphviz(self, output_file):
        dot = Digraph()

        for state in self.states:
            if state in self.final_states:
                dot.node(state, shape='doublecircle')
            else:
                dot.node(state)

        dot.node('initial', shape='point')
        dot.edge('initial', self.initial_state)

        for origin, transitions in self.transitions.items():
            for symbol, destinations in transitions.items():
                for destination in destinations:
                    if symbol != "Ɛ":
                        dot.edge(origin, destination, label=symbol)
                    else:
                        dot.edge(origin, destination, label="ε")

        try:
            # Salvando o arquivo .dot na pasta 'digraph'
            dot.render(f"digraph/afd/{output_file}", format='dot', cleanup=True)
            print(f"Graphviz representation generated: digraph/{output_file}.dot")

            # Salvando o arquivo .png na pasta 'digraph'
            dot.render(f"digraph/afd/{output_file}", format='png', cleanup=True)
            print(f"Graphviz representation generated: digraph/{output_file}.png")
        except ExecutableNotFound:
            print("Graphviz executável 'dot' não encontrado. Por favor, verifique se o Graphviz está instalado corretamente e adicionado ao seu PATH.")


def main():
    if len(sys.argv) < 3:
        print("Uso: python afnd_main.py <filename.json> [-graphviz | -output <filename.json>]")
        return

    nome_arquivo = sys.argv[1]
    operacao = sys.argv[2]

    try:
        conversor = AFNDtoAFD(nome_arquivo)

        if operacao == "-graphviz":
            conversor.generate_graphviz("grafo_afd_teste")
            print("Ficheiro Graphviz gerado com sucesso.")
        elif operacao == "-output":
            afd = conversor.converter()
            if len(sys.argv) < 4:
                print("Uso: python afnd_main.py <filename.json> -output <filename.json>")
                return
            nome_saida = sys.argv[3]
            with open(nome_saida, 'w') as f:
                json.dump(afd, f, indent=4)
                print(f"AFD salvo em {nome_saida}")
        else:
            print("Operação inválida. Por favor, use -graphviz ou -output")
    except ValueError as e:
        print(f"Erro ao converter AFND para AFD: {e}")

if __name__ == "__main__":
    main()
