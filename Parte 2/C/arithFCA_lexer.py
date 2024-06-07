import ply.lex as lex

tokens = [
    'NUMBER',
    'IDENTIFIER',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'LPAREN', 'RPAREN',
    'COMMA', 'SEMICOLON',
    'ASSIGN', 'STRING',
    'FUNCAO', 'FIM',
    'COLON', 'EQUALS', 'SEMI',
    'ESCREVER', 'ENTRADA', 'ALEATORIO'
]

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_ASSIGN = r'='
t_COMMA = r','
t_STRING = r'\"([^\\\n]|(\\.))*?\"'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMI = r';'
t_COLON = r':'

t_ignore = ' \t'

def t_FUNCAO(t):
    r'FUNCAO'
    return t

def t_FIM(t):
    r'FIM'
    return t

def t_ESCREVER(t):
    r'ESCREVER'
    return t

def t_ENTRADA(t):
    r'ENTRADA'
    return t

def t_ALEATORIO(t):
    r'ALEATORIO'
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()
