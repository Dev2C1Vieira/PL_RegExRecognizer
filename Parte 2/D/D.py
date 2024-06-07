import ply.lex as lex
import ply.yacc as yacc
import functools

# Lista de tokens
tokens = (
    'FLOAT', 'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'EQUALS',
    'STRING', 'IDENTIFIER', 'COMMA', 'LPAREN', 'RPAREN', 
    'LBRACKET', 'RBRACKET', 'ESCREVER', 'SEMI', 'MAP', 'FOLD', 
    'COLON', 'FUNCAO', 'FIM'
)

# Regras de expressões regulares para tokens simples
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r'='
t_COMMA = r','
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_SEMI = r';'
t_COLON = r':'
t_STRING = r'\"([^\\\n]|(\\.))*?\"'
t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z_0-9]*'
t_MAP = r'map'
t_FOLD = r'fold'
t_FUNCAO = r'FUNCAO'
t_FIM = r'FIM'

# Regras de expressões regulares com ações
def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ESCREVER(t):
    r'ESCREVER'
    return t

# Ignorar espaços e tabulações
t_ignore = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Construir o lexer
lexer = lex.lex()

# Dicionário para armazenar nomes de variáveis e funções
names = {}

def p_statement_assign(p):
    'statement : IDENTIFIER EQUALS expression SEMI'
    names[p[1]] = p[3]

def p_statement_expr(p):
    'statement : expression SEMI'
    print(p[1])

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    if p[1] is None or p[3] is None:
        raise TypeError("Unsupported operand type(s) for binary operation")
    if p[2] == '+': p[0] = p[1] + p[3]
    elif p[2] == '-': p[0] = p[1] - p[3]
    elif p[2] == '*': p[0] = p[1] * p[3]
    elif p[2] == '/': p[0] = p[1] / p[3]

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_number(p):
    '''expression : NUMBER
                  | FLOAT'''
    p[0] = p[1]

def p_expression_string(p):
    'expression : STRING'
    p[0] = p[1]

def p_expression_name(p):
    'expression : IDENTIFIER'
    try:
        p[0] = names[p[1]]
    except LookupError:
        print(f"Undefined name '{p[1]}'")
        p[0] = 0

def p_expression_list(p):
    'expression : LBRACKET expression_list RBRACKET'
    p[0] = p[2]

def p_expression_list_empty(p):
    'expression : LBRACKET RBRACKET'
    p[0] = []

def p_expression_list_multiple(p):
    'expression_list : expression_list COMMA expression'
    p[0] = p[1] + [p[3]]

def p_expression_list_single(p):
    'expression_list : expression'
    p[0] = [p[1]]

def p_expression_function_call(p):
    '''expression : IDENTIFIER LPAREN expression RPAREN
                  | IDENTIFIER LPAREN expression COMMA expression RPAREN'''
    if len(p) == 5:
        p[0] = (p[1], p[3])
    elif len(p) == 7:
        p[0] = (p[1], p[3], p[5])

def p_expression_map(p):
    'expression : MAP LPAREN expression RPAREN'
    func = names.get(p[3])
    if func:
        p[0] = list(map(func, p[3]))
    else:
        raise NameError(f"Function '{p[3]}' not defined")

def p_expression_fold(p):
    'expression : FOLD LPAREN expression COMMA expression RPAREN'
    func = names.get(p[3])
    if func:
        p[0] = functools.reduce(func, p[5], p[7])
    else:
        raise NameError(f"Function '{p[3]}' not defined")

def p_function_definition(p):
    '''statement : FUNCAO IDENTIFIER LPAREN params RPAREN COLON expression SEMI
                 | FUNCAO IDENTIFIER LPAREN params RPAREN COLON statement_list FIM'''
    if len(p) == 8:
        def func(*args):
            local_vars = {p[4][i]: args[i] for i in range(len(args))}
            return eval(p[7], {"__builtins__": None}, local_vars)
        names[p[2]] = func
    else:
        def func(*args):
            local_vars = {p[4][i]: args[i] for i in range(len(args))}
            for stmt in p[7]:
                eval(stmt, {"__builtins__": None}, local_vars)
        names[p[2]] = func

def p_params(p):
    '''params : params COMMA IDENTIFIER
              | IDENTIFIER
              | empty'''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    elif len(p) == 2 and p[1]:
        p[0] = [p[1]]
    else:
        p[0] = []

def p_statement_list(p):
    '''statement_list : statement_list statement
                      | statement'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_expression_command(p):
    '''statement : ESCREVER LPAREN expression RPAREN SEMI
                 | ESCREVER LPAREN expression COMMA expression RPAREN SEMI'''
    if len(p) == 6:
        print(p[3])
    elif len(p) == 8:
        print(p[3], p[5])

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at EOF")

def p_empty(p):
    'empty :'
    pass

parser = yacc.yacc()

# Loop de leitura de entrada
while True:
    try:
        s = input('FCA > ')
    except EOFError:
        break
    if not s: continue
    try:
        result = parser.parse(s, lexer=lexer)
    except Exception as e:
        print(e)
