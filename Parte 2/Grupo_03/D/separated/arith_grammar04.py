import ply.yacc as yacc
from arith_lexer import tokens

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

def p_expression_name(p):
    'expression : IDENTIFIER'
    try:
        p[0] = names[p[1]]
    except LookupError:
        print(f"Undefined name '{p[1]}'")
        p[0] = 0

def p_expression_list(p):
    '''expression : LBRACKET list_elements RBRACKET'''
    p[0] = p[2]

def p_list_elements(p):
    '''list_elements : list_elements COMMA expression
                     | expression
                     | empty'''
    if len(p) == 2 and p[1] is not None:
        p[0] = [p[1]]
    elif len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = []

def p_empty(p):
    'empty :'
    pass

def p_statement_list(p):
    '''statement_list : statement_list statement
                      | statement'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_statement_write(p):
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

parser = yacc.yacc()
