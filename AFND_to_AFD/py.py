import json
import sys
from collections import defaultdict

class Automato:
    def __init__(self, estados, alfabeto, transicoes, estado_inicial, estados_finais):
        self.estados = estados
        self.alfabeto = alfabeto
        self.transicoes = transicoes
        self.estado_inicial = estado_inicial
        self.estados_finais = estados_finais

    def transitar(self, estado, simbolo):
        if (estado, simbolo) in self.transicoes:
            return self.transicoes[(estado, simbolo)]
        else:
            return []

    def gerar_afd(self):
        novos_estados = [self.estado_inicial]
        novas_transicoes = defaultdict(dict)
        novos_estados_finais = []

        for estado in novos_estados:
            for simbolo in self.alfabeto:
                proximos_estados = set()
                for estado_atual in estado:
                    proximos_estados.update(self.transitar(estado_atual, simbolo))
                proximos_estados = tuple(sorted(proximos_estados))
                chave_estado = ",".join(str(est) for est in estado)  # Convertendo a chave para uma string
                print("Chave do estado:", chave_estado)
                print("Próximos estados:", proximos_estados)
                novas_transicoes[chave_estado][simbolo] = proximos_estados
                if proximos_estados not in novos_estados:
                    novos_estados.append(proximos_estados)

        for estado in novos_estados:
            for estado_final in self.estados_finais:
                if any(est in estado_final for est in estado):
                    novos_estados_finais.append(estado)

        return Automato(novos_estados, self.alfabeto, novas_transicoes, self.estado_inicial, novos_estados_finais)

def main():
    if len(sys.argv) != 3:
        print("Usage: python afnd_main.py <afnd_file> <afd_output_file>")
        sys.exit(1)

    afnd_file = sys.argv[1]
    afd_output_file = sys.argv[2]

    # Lendo o arquivo JSON
    with open(afnd_file, "r") as arquivo:
        afnd = json.load(arquivo)

    estados = afnd["Q"]
    alfabeto = afnd["V"]
    transicoes = defaultdict(dict)

    for origem, trans in afnd["delta"].items():
        for simbolo, destino in trans.items():
            transicoes[(origem, simbolo)] = destino

    estado_inicial = afnd["q0"]
    estados_finais = afnd["F"]

    # Criando o objeto do autômato
    automato = Automato(estados, alfabeto, transicoes, estado_inicial, estados_finais)

    # Convertendo para AFD
    afd = automato.gerar_afd()

    # Escrevendo o AFD no arquivo JSON
    with open(afd_output_file, "w") as output_file:
        json.dump({
            "Q": afd.estados,
            "V": afd.alfabeto,
            "delta": afd.transicoes,
            "q0": afd.estado_inicial,
            "F": afd.estados_finais
        }, output_file)

if __name__ == "__main__":
    main()