import sys
import json

def generate_afnd(expression_tree):
    Q = []
    V = set()  # Usando um conjunto para garantir que os símbolos sejam únicos
    delta = {}
    final_states = set()  # Usando um conjunto para garantir que os estados finais sejam únicos
    
    def add_transition(state_from, symbol, state_to):
        if state_from not in delta:
            delta[state_from] = {}
        if symbol not in delta[state_from]:
            delta[state_from][symbol] = []
        delta[state_from][symbol].append(state_to)
    
    def explore_tree(node, current_state):
        nonlocal Q
        nonlocal final_states

        if "simb" in node:
            symbol = node["simb"]
            V.add(symbol)  # Adiciona o símbolo ao conjunto V
            next_state = "q" + str(len(Q))
            Q.append(next_state)
            add_transition(current_state, symbol, next_state)
            return next_state

        if "op" in node and node["op"] == "alt":
            epsilon_states = []
            has_final_state = False
            for arg in node["args"]:
                if "epsilon" in arg:
                    epsilon_state = "q" + str(len(Q))
                    Q.append(epsilon_state)
                    epsilon_states.append(epsilon_state)
                else:
                    next_state = explore_tree(arg, current_state)
                    if next_state in final_states:
                        has_final_state = True
            if epsilon_states or has_final_state:
                for epsilon_state in epsilon_states:
                    add_transition(current_state, "", epsilon_state)
            return current_state

        if "op" in node and node["op"] == "seq":
            next_state = current_state
            for arg in node["args"]:
                next_state = explore_tree(arg, next_state)
            return next_state

        if "op" in node and node["op"] == "kle":
            next_state = explore_tree(node["args"][0], current_state)
            add_transition(next_state, "", current_state)
            return current_state
        
    q0 = "q0"
    Q.append(q0)
    final_state = explore_tree(expression_tree, q0)
    final_states.add(final_state)  # Adiciona o estado final encontrado ao conjunto F
    
    return {
        "V": list(V),  # Convertendo o conjunto V de volta para uma lista
        "Q": Q,
        "delta": delta,
        "q0": q0,
        "F": list(final_states)  # Convertendo o conjunto de estados finais F de volta para uma lista
    }

def main(input_file, output_file):
    with open(input_file, 'r') as f:
        expression_tree = json.load(f)
    
    afnd = generate_afnd(expression_tree)
    
    with open(output_file, 'w') as f:
        json.dump(afnd, f, indent=4)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py input_file output_file")
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    main(input_file, output_file)