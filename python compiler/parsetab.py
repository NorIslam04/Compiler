
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVIDEDIVIDE LPAREN MINUS NUMBER PLUS RPAREN TIMESexpression : expression PLUS term\n                  | expression MINUS term\n                  | termterm : term TIMES factor\n            | term DIVIDE factor\n            | factorfactor : NUMBER\n              | LPAREN expression RPARENexpression : LPAREN expression RPARENexpression : NUMBER'
    
_lr_action_items = {'LPAREN':([0,3,6,7,8,9,13,],[3,3,13,13,13,13,3,]),'NUMBER':([0,3,6,7,8,9,13,],[4,4,12,12,12,12,4,]),'$end':([1,2,4,5,11,12,14,15,16,17,19,],[0,-3,-7,-6,-1,-7,-2,-4,-5,-8,-8,]),'PLUS':([1,2,4,5,10,11,12,14,15,16,17,18,19,],[6,-3,-7,-6,6,-1,-7,-2,-4,-5,-8,6,-8,]),'MINUS':([1,2,4,5,10,11,12,14,15,16,17,18,19,],[7,-3,-7,-6,7,-1,-7,-2,-4,-5,-8,7,-8,]),'RPAREN':([2,4,5,10,11,12,14,15,16,17,18,19,],[-3,-7,-6,17,-1,-7,-2,-4,-5,-8,19,-8,]),'TIMES':([2,4,5,11,12,14,15,16,17,19,],[8,-7,-6,8,-7,8,-4,-5,-8,-8,]),'DIVIDE':([2,4,5,11,12,14,15,16,17,19,],[9,-7,-6,9,-7,9,-4,-5,-8,-8,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,3,13,],[1,10,18,]),'term':([0,3,6,7,13,],[2,2,11,14,2,]),'factor':([0,3,6,7,8,9,13,],[5,5,5,5,15,16,5,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> expression PLUS term','expression',3,'p_expression_binop','parser.py',12),
  ('expression -> expression MINUS term','expression',3,'p_expression_binop','parser.py',13),
  ('expression -> term','expression',1,'p_expression_binop','parser.py',14),
  ('term -> term TIMES factor','term',3,'p_term','parser.py',24),
  ('term -> term DIVIDE factor','term',3,'p_term','parser.py',25),
  ('term -> factor','term',1,'p_term','parser.py',26),
  ('factor -> NUMBER','factor',1,'p_factor','parser.py',36),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor','parser.py',37),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','parser.py',44),
  ('expression -> NUMBER','expression',1,'p_expression_number','parser.py',48),
]
