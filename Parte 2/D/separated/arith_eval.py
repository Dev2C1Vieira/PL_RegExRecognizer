def evaluate(node):
    if isinstance(node, int):
        return node
    elif isinstance(node, list):
        return [evaluate(n) for n in node]
    elif isinstance(node, tuple):
        if node[0] == 'write':
            result = evaluate(node[1])
            print(result)
            return result
        elif node[0] == 'assign':
            variables[node[1]] = evaluate(node[2])
            return variables[node[1]]
        elif node[0] == 'var':
            return variables.get(node[1], 0)
        elif node[0] == 'program':
            for stmt in node[1]:
                evaluate(stmt)
    return None

variables = {}
