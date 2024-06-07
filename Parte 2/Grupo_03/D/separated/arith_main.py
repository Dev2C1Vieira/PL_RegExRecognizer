import sys
import arith_grammar04

if len(sys.argv) != 2:
    print("Usage: %s filename" % sys.argv[0])
    sys.exit(1)

filename = sys.argv[1]
with open(filename, 'r') as file:
    data = file.read()

arith_grammar04.parser.parse(data)
