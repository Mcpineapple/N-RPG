import accesmodule

"""
Importe le parser, et imprime les appels renvoyes a la lecture du protitype du
VNMD.
"""
import os
import sys

from nrpg.parser import Parser

position_script = os.path.join(os.path.dirname(__file__), '..', 'vnmd',
        'prototype.vnmd')
parser = Parser(pos)

a = ""
while a != "fin":
    a = parser.suivant()
    print(a)
