
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'LPAREN MINUS NUMBER PLUS RPAREN TIMESexpression : expression PLUS expression\n                  | expression MINUS expression\n                  | expression TIMES expressionexpression : LPAREN expression RPARENexpression : NUMBER'
    
_lr_action_items = {'LPAREN':([0,2,4,5,6,],[2,2,2,2,2,]),'NUMBER':([0,2,4,5,6,],[3,3,3,3,3,]),'$end':([1,3,8,9,10,11,],[0,-5,-1,-2,-3,-4,]),'PLUS':([1,3,7,8,9,10,11,],[4,-5,4,4,4,4,-4,]),'MINUS':([1,3,7,8,9,10,11,],[5,-5,5,5,5,5,-4,]),'TIMES':([1,3,7,8,9,10,11,],[6,-5,6,6,6,6,-4,]),'RPAREN':([3,7,8,9,10,11,],[-5,11,-1,-2,-3,-4,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,2,4,5,6,],[1,7,8,9,10,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','parser.py',7),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','parser.py',8),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','parser.py',9),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','parser.py',18),
  ('expression -> NUMBER','expression',1,'p_expression_number','parser.py',22),
]