
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVIDEALEATORIO ASSIGN ASSIGN COLON COMMA DIVIDE ENTRADA EQUALS ESCREVER FIM FUNCAO IDENTIFIER LPAREN MINUS NUMBER PLUS RPAREN SEMI SEMICOLON STRING TIMESstatement : IDENTIFIER ASSIGN expression SEMIstatement : expressionstatement : ESCREVER LPAREN expression RPARENexpression : expression PLUS expression\n                  | expression MINUS expression\n                  | expression TIMES expression\n                  | expression DIVIDE expressionexpression : IDENTIFIER LPAREN args RPARENexpression : LPAREN expression RPARENexpression : NUMBERexpression : STRINGexpression : IDENTIFIERstatement : FUNCAO IDENTIFIER LPAREN params RPAREN COLON expression SEMIstatement : FUNCAO IDENTIFIER LPAREN params RPAREN COLON statements FIMparams : IDENTIFIER\n              | IDENTIFIER COMMA params\n              | emptyargs : expression\n            | expression COMMA argsstatements : statement\n                  | statement statementsempty :'
    
_lr_action_items = {'IDENTIFIER':([0,2,3,5,6,7,8,9,10,11,12,13,14,15,17,22,23,24,25,27,28,29,30,31,32,37,40,41,42,44,45,46,],[2,-12,-2,17,18,-10,-11,17,17,17,17,17,17,17,-12,-4,-5,-6,-7,-9,33,-1,-8,17,-3,33,41,-12,-2,2,-13,-14,]),'ESCREVER':([0,2,3,7,8,17,22,23,24,25,27,29,30,32,40,41,42,44,45,46,],[4,-12,-2,-10,-11,-12,-4,-5,-6,-7,-9,-1,-8,-3,4,-12,-2,4,-13,-14,]),'FUNCAO':([0,2,3,7,8,17,22,23,24,25,27,29,30,32,40,41,42,44,45,46,],[6,-12,-2,-10,-11,-12,-4,-5,-6,-7,-9,-1,-8,-3,6,-12,-2,6,-13,-14,]),'LPAREN':([0,2,3,4,5,7,8,9,10,11,12,13,14,15,17,18,22,23,24,25,27,29,30,31,32,40,41,42,44,45,46,],[5,10,-2,15,5,-10,-11,5,5,5,5,5,5,5,10,28,-4,-5,-6,-7,-9,-1,-8,5,-3,5,10,-2,5,-13,-14,]),'NUMBER':([0,2,3,5,7,8,9,10,11,12,13,14,15,17,22,23,24,25,27,29,30,31,32,40,41,42,44,45,46,],[7,-12,-2,7,-10,-11,7,7,7,7,7,7,7,-12,-4,-5,-6,-7,-9,-1,-8,7,-3,7,-12,-2,7,-13,-14,]),'STRING':([0,2,3,5,7,8,9,10,11,12,13,14,15,17,22,23,24,25,27,29,30,31,32,40,41,42,44,45,46,],[8,-12,-2,8,-10,-11,8,8,8,8,8,8,8,-12,-4,-5,-6,-7,-9,-1,-8,8,-3,8,-12,-2,8,-13,-14,]),'$end':([1,2,3,7,8,17,22,23,24,25,27,29,30,32,45,46,],[0,-12,-2,-10,-11,-12,-4,-5,-6,-7,-9,-1,-8,-3,-13,-14,]),'ASSIGN':([2,41,],[9,9,]),'PLUS':([2,3,7,8,16,17,19,21,22,23,24,25,26,27,30,41,42,],[-12,11,-10,-11,11,-12,11,11,-4,-5,-6,-7,11,-9,-8,-12,11,]),'MINUS':([2,3,7,8,16,17,19,21,22,23,24,25,26,27,30,41,42,],[-12,12,-10,-11,12,-12,12,12,-4,-5,-6,-7,12,-9,-8,-12,12,]),'TIMES':([2,3,7,8,16,17,19,21,22,23,24,25,26,27,30,41,42,],[-12,13,-10,-11,13,-12,13,13,13,13,-6,-7,13,-9,-8,-12,13,]),'DIVIDE':([2,3,7,8,16,17,19,21,22,23,24,25,26,27,30,41,42,],[-12,14,-10,-11,14,-12,14,14,14,14,-6,-7,14,-9,-8,-12,14,]),'FIM':([2,3,7,8,17,22,23,24,25,27,29,30,32,41,42,43,44,45,46,47,],[-12,-2,-10,-11,-12,-4,-5,-6,-7,-9,-1,-8,-3,-12,-2,46,-20,-13,-14,-21,]),'RPAREN':([7,8,16,17,20,21,22,23,24,25,26,27,28,30,33,34,35,36,37,39,],[-10,-11,27,-12,30,-18,-4,-5,-6,-7,32,-9,-22,-8,-15,38,-17,-19,-22,-16,]),'SEMI':([7,8,17,19,22,23,24,25,27,30,41,42,],[-10,-11,-12,29,-4,-5,-6,-7,-9,-8,-12,45,]),'COMMA':([7,8,17,21,22,23,24,25,27,30,33,],[-10,-11,-12,31,-4,-5,-6,-7,-9,-8,37,]),'COLON':([38,],[40,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,40,44,],[1,44,44,]),'expression':([0,5,9,10,11,12,13,14,15,31,40,44,],[3,16,19,21,22,23,24,25,26,21,42,3,]),'args':([10,31,],[20,36,]),'params':([28,37,],[34,39,]),'empty':([28,37,],[35,35,]),'statements':([40,44,],[43,47,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> IDENTIFIER ASSIGN expression SEMI','statement',4,'p_statement_assign','arithFCA_grammar.py',16),
  ('statement -> expression','statement',1,'p_statement_expr','arithFCA_grammar.py',20),
  ('statement -> ESCREVER LPAREN expression RPAREN','statement',4,'p_statement_escrever','arithFCA_grammar.py',24),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','arithFCA_grammar.py',28),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','arithFCA_grammar.py',29),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','arithFCA_grammar.py',30),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','arithFCA_grammar.py',31),
  ('expression -> IDENTIFIER LPAREN args RPAREN','expression',4,'p_expression_function_call','arithFCA_grammar.py',35),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','arithFCA_grammar.py',39),
  ('expression -> NUMBER','expression',1,'p_expression_number','arithFCA_grammar.py',43),
  ('expression -> STRING','expression',1,'p_expression_string','arithFCA_grammar.py',47),
  ('expression -> IDENTIFIER','expression',1,'p_expression_name','arithFCA_grammar.py',51),
  ('statement -> FUNCAO IDENTIFIER LPAREN params RPAREN COLON expression SEMI','statement',8,'p_function_declaration_one_line','arithFCA_grammar.py',55),
  ('statement -> FUNCAO IDENTIFIER LPAREN params RPAREN COLON statements FIM','statement',8,'p_function_declaration_multi_line','arithFCA_grammar.py',60),
  ('params -> IDENTIFIER','params',1,'p_params','arithFCA_grammar.py',74),
  ('params -> IDENTIFIER COMMA params','params',3,'p_params','arithFCA_grammar.py',75),
  ('params -> empty','params',1,'p_params','arithFCA_grammar.py',76),
  ('args -> expression','args',1,'p_args','arithFCA_grammar.py',85),
  ('args -> expression COMMA args','args',3,'p_args','arithFCA_grammar.py',86),
  ('statements -> statement','statements',1,'p_statements','arithFCA_grammar.py',93),
  ('statements -> statement statements','statements',2,'p_statements','arithFCA_grammar.py',94),
  ('empty -> <empty>','empty',0,'p_empty','arithFCA_grammar.py',101),
]