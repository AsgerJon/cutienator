"""
BytecodeGenerator stands in for the class 'QV4::Moth::BytecodeGenerator' of
Qt, which has no cute class yet.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4bytecodegenerator_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QV4::Moth::BytecodeGenerator to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from ..cute import UnsupportedMeta


class BytecodeGenerator(metaclass=UnsupportedMeta):
  """
  Qt's class 'QV4::Moth::BytecodeGenerator' of QtQml: writing its cute class
  raised LookupError: The dependency tree has no class named
  'BytecodeGenerator'.
  """

  #  The class of Qt this class stands in for.
  __qt_class__ = 'QV4::Moth::BytecodeGenerator'
