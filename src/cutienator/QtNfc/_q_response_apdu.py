"""
QResponseApdu stands in for the class 'QResponseApdu' of Qt, which has no
cute class yet.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNfc/6.12.0/QtNfc/private/qapduutils_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QResponseApdu to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from ..cute import UnsupportedMeta


class QResponseApdu(metaclass=UnsupportedMeta):
  """
  Qt's class 'QResponseApdu' of QtNfc: writing its cute class raised
  RuntimeError: The compiler refuses the ritual file of 'QResponseApdu' as it
  would be written, for what no code taken from Qt's source is to blame: line
  6: division by zero in preprocessor expression
  """

  #  The class of Qt this class stands in for.
  __qt_class__ = 'QResponseApdu'
