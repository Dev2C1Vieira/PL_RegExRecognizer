import ply.yacc as yacc
from arithFCA_lexer import tokens
from arithFCA_eval import evaluate

# Regras de precedência
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)

# Dicionário de nomes
names = {}
functions = {}

def p_statement_assign(p):
    'statement : IDENTIFIER ASSIGN expression SEMI'
    names[p[1]] = p[3]

def p_statement_expr(p):
    'statement : expression'
    print(p[1])

def p_statement_escrever(p):
    'statement : ESCREVER LPAREN expression RPAREN'
    evaluate(('escrever', p[3]), names, functions)

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    p[0] = ('binop', p[2], p[1], p[3])

def p_expression_function_call(p):
    'expression : IDENTIFIER LPAREN args RPAREN'
    p[0] = ('func_call', p[1], p[3])

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = ('num', p[1])

def p_expression_string(p):
    'expression : STRING'
    p[0] = ('string', p[1])

def p_expression_name(p):
    'expression : IDENTIFIER'
    p[0] = ('id', p[1])

def p_function_declaration_one_line(p):
    'statement : FUNCAO IDENTIFIER LPAREN params RPAREN COLON expression SEMI'
    # Armazenando o corpo da função diretamente como uma expressão a ser avaliada
    functions[p[2]] = (p[4], p[7])  # params, expression

def p_function_declaration_multi_line(p):
    'statement : FUNCAO IDENTIFIER LPAREN params RPAREN COLON statements FIM'
    functions[p[2]] = ('multi_line', p[4], p[7])

def call_function(name, args, variables, functions):
    if name not in functions:
        raise ValueError(f"Function '{name}' not defined.")
    params, body = functions[name]
    local_vars = {param: arg for param, arg in zip(params, args)}
    if None in local_vars.values():  # Debugging to check if any local variable is None
        print(f"Debug: Local variables for function '{name}' contain None: {local_vars}")
    return evaluate(body, {**variables, **local_vars}, functions)


def p_params(p):
    '''params : IDENTIFIER
              | IDENTIFIER COMMA params
              | empty'''
    if len(p) == 2:
        p[0] = [p[1]]
    elif len(p) == 4:
        p[0] = [p[1]] + p[3]
    else:
        p[0] = []

def p_args(p):
    '''args : expression
            | expression COMMA args'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

def p_statements(p):
    '''statements : statement
                  | statement statements'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[2]

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    print(f"Erro de sintaxe em '{p.value}'")

parser = yacc.yacc()
