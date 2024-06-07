import ply.lex as lex
import ply.yacc as yacc

# Léxico
tokens = (
    'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'EQUALS',
    'STRING', 'IDENTIFIER', 'COMMA', 'LPAREN', 'RPAREN', 'ESCREVER', 'SEMI'
)

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r'='
t_COMMA = r','
t_STRING = r'\"([^\\\n]|(\\.))*?\"'
t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z_0-9]*'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMI = r';'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ESCREVER(t):
    r'ESCREVER'
    return t

t_ignore = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

# Sintaxe
def p_statement_expr(p):
    'statement : expression SEMI'
    print(p[1])

def p_statement_assign(p):
    'statement : IDENTIFIER EQUALS expression SEMI'
    names[p[1]] = p[3]

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    if p[2] == '+': p[0] = p[1] + p[3]
    elif p[2] == '-': p[0] = p[1] - p[3]
    elif p[2] == '*': p[0] = p[1] * p[3]
    elif p[2] == '/': p[0] = p[1] / p[3]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_expression_string(p):
    'expression : STRING'
    p[0] = str(p[1][1:-1])

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_identifier(p):
    'expression : IDENTIFIER'
    p[0] = names.get(p[1], None)

def p_expression_command(p):
    '''statement : ESCREVER LPAREN expression RPAREN SEMI
                 | ESCREVER LPAREN expression COMMA expression RPAREN SEMI'''
    if len(p) == 6:
        print(p[3])
    elif len(p) == 8:
        print(p[3], p[5])

def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()

# Adicionar suporte para variáveis e funções
names = {}

while True:
    try:
        s = input('FCA > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s, lexer=lexer)