import json
import sys
from graphviz import Digraph
from graphviz import ExecutableNotFound

class AFD:
    
    def __init__(self, filename):
        if filename.endswith('.json'):
            self.load_afd_from_json(filename)
        else:
            print("Erro: O arquivo fornecido não é um arquivo JSON.")
            sys.exit(1)
                   
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
            for symbol, destination in transitions.items():
                if symbol != "Ɛ":
                    dot.edge(origin, destination, label=symbol)
                else:
                    dot.edge(origin, destination, label="ε")
        
        try:
            # Salvando o arquivo .dot na pasta 'digraph'
            dot.render(f"digraph/{output_file}", format='dot', cleanup=True)
            print(f"Graphviz representation generated: digraph/{output_file}.dot")
            
            # Salvando o arquivo .png na pasta 'digraph'
            dot.render(f"digraph/{output_file}", format='png', cleanup=True)
            print(f"Graphviz representation generated: digraph/{output_file}.png")
        except ExecutableNotFound:
            print("Graphviz executável 'dot' não encontrado. Por favor, verifique se o Graphviz está instalado corretamente e adicionado ao seu PATH.")
    
    def recognize_word(self, word):
        current_states = [self.initial_state]
        path = [self.initial_state]
        error_message = ""
        
        for symbol in word:
            if symbol not in self.alphabet:
                error_message = f"Símbolo '{symbol}' não pertence ao alfabeto da linguagem"
                return False, path, error_message
            
            next_states = []
            for state in current_states:
                next_state = self.transitions.get(state, {}).get(symbol)
                if next_state:
                    next_states.append(next_state)
            
            if not next_states:
                error_message = f"Transição inválida de '{current_states}' para '{next_states}' com o símbolo '{symbol}'"
                return False, path, error_message
            
            path.append(symbol)
            path.extend(next_states)
            current_states = next_states
        
        if any(state in self.final_states for state in current_states):
            return True, path, "Palavra reconhecida."
        else:
            error_message = f"Nenhum dos estados {current_states} é final"
            return False, path, error_message

def main():
    if len(sys.argv) < 3:
        print("Usage: python afd.py <filename.json> [-graphviz | -rec <word>]")
        return

    filename = sys.argv[1]
    operation = sys.argv[2]

    afd = AFD(filename)

    if operation == "-graphviz":
        afd.generate_graphviz("graph")
        print("Graphviz file generated successfully.")
    elif operation == "-rec":
        if len(sys.argv) < 4:
            print("Usage: python afd.py <filename.json> -rec <word>")
            return
        word = sys.argv[3]
        recognized, path, message = afd.recognize_word(word)
        if recognized:
            print(f"'{word}' é reconhecida")
            print(f"[caminho {'->'.join(path)}]")
        else:
            print(f"'{word}' não é reconhecida")
            print(f"[{message}]")
    else:
        print("Invalid operation. Please use -graphviz or -rec")

if __name__ == "__main__":
    main()