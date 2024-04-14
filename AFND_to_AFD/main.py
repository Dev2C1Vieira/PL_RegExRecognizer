import sys
import json

def generate_afnd(expression_tree):
    Q = []
    V = []
    delta = {}
    
    def add_transition(state_from, symbol, state_to):
        if state_from not in delta:
            delta[state_from] = {}
        if symbol not in delta[state_from]:
            delta[state_from][symbol] = []
        delta[state_from][symbol].append(state_to)
    
    def explore_tree(node, current_state):
        nonlocal Q
        nonlocal V
        
        if "simb" in node:
            V.append(node["simb"])
            next_state = "q" + str(len(Q))
            Q.append(next_state)
            add_transition(current_state, node["simb"], next_state)
            return next_state
        
        if node["op"] == "alt":
            next_state = "q" + str(len(Q))
            Q.append(next_state)
            add_transition(current_state, "", next_state)
            next_state_1 = explore_tree(node["args"][0], next_state)
            next_state_2 = explore_tree(node["args"][1], next_state)
            add_transition(next_state, "", next_state_1)
            add_transition(next_state, "", next_state_2)
            return next_state
        
        if node["op"] == "seq":
            next_state = current_state
            for arg in node["args"]:
                next_state = explore_tree(arg, next_state)
            return next_state
        
        if node["op"] == "kle":
            next_state = "q" + str(len(Q))
            Q.append(next_state)
            add_transition(current_state, "", next_state)
            next_state_1 = explore_tree(node["args"][0], next_state)
            add_transition(next_state_1, "", next_state)
            return next_state
    
    q0 = "q0"
    F = ["q" + str(len(Q))]
    Q.append(q0)
    explore_tree(expression_tree, q0)
    
    return {
        "Q": Q,
        "V": V,
        "q0": q0,
        "F": F,
        "delta": delta
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
