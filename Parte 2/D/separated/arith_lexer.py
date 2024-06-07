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

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Ignorar espaços e tabulações
t_ignore = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Construir o lexer
lexer = lex.lex()
