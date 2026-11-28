"""
QNativeSocketEngine stands in for the class 'QNativeSocketEngine' of Qt,
which has no cute class yet.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qnativesocketengine_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QNativeSocketEngine to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from ..cute import UnsupportedMeta


class QNativeSocketEngine(metaclass=UnsupportedMeta):
  """
  Qt's class 'QNativeSocketEngine' of QtNetwork: writing its cute class
  raised RuntimeError: The compiler refuses the ritual file of
  'QNativeSocketEngine' as it would be written, for what no code taken from
  Qt's source is to blame: line 175: expected 'while' in do/while loop; line
  434: unknown type name 'CuteQNativeSocketEngineCall0'; line 869: expected
  '}'
  """

  #  The class of Qt this class stands in for.
  __qt_class__ = 'QNativeSocketEngine'
