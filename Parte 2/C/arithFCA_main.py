import sys
from arithFCA_lexer import lexer
from arithFCA_grammar import parser

if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        with open(filename, 'r') as file:
          for line in file:
            if line.strip():  # Skip empty lines
              result = parser.parse(line, lexer=lexer)
              print(result)
    else:
        while True:
         try:
             s = input('FCA > ')
         except EOFError:
            break
         if not s: continue
         result = parser.parse(s, lexer=lexer)
