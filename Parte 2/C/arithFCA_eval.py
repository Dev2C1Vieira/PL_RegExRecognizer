import random
import re

def perform_operation(operation, left, right):
    if operation == '+':
        return left + right
    elif operation == '-':
        return left - right
    elif operation == '*':
        return left * right
    elif operation == '/':
        if right == 0:
            raise ValueError("Division by zero")
        return left // right  # Assuming integer division for simplicity

def call_function(name, args, variables, functions):
    if name not in functions:
        raise ValueError(f"Function '{name}' not defined.")
    params, body = functions[name]
    local_vars = {param: arg for param, arg in zip(params, args)}
    print(f"Debug: Function '{name}', Params: {params}, Args: {args}, Local Vars: {local_vars}")
    return evaluate(body, {**variables, **local_vars}, functions)

def evaluate(node, variables, functions):
    if isinstance(node, tuple):
        op = node[0]
        if op == 'binop':
            operation = node[1]
            left = evaluate(node[2], variables, functions)
            right = evaluate(node[3], variables, functions)
            if left is None or right is None:
                print(f"Debug: Operation '{operation}' - Left: {left}, Right: {right}")
                raise TypeError("Operands cannot be None")
            return perform_operation(operation, left, right)
        elif op == 'concat':
            return str(evaluate(node[1], variables, functions)) + str(evaluate(node[2], variables, functions))
        elif op == 'assign':
            value = evaluate(node[2], variables, functions)
            variables[node[1]] = value
            return value
        elif op == 'escrever':
             value = evaluate(node[1], variables, functions)
             print(value)
             return value
        elif op == 'entrada':
            return int(input("Enter a number: "))
        elif op == 'aleatorio':
            if len(node) == 2:
                max_value = evaluate(node[1], variables, functions)
                return random.randint(0, max_value)
            return random.randint(0, 100)
        elif op == 'num':
            return node[1]
        elif op == 'string':
            return node[1]
        elif op == 'func_call':
            func_name = node[1]
            args = [evaluate(arg, variables, functions) for arg in node[2]]
            print(f"Debug: Calling function '{func_name}' with args {args}")
            return call_function(func_name, args, variables, functions)
    else:
        value = variables.get(node, 'Variable not found')
        print(f"Debug: Accessing variable '{node}' with value {value}")
        return value

def interpolate_string(string, variables):
    """Interpolate variables within a string."""
    def replace_var(match):
        var_name = match.group(1)
        return str(variables.get(var_name, f'#{var_name}'))
    return re.sub(r'#{(\w+[\?\!]*)}', replace_var, string)
