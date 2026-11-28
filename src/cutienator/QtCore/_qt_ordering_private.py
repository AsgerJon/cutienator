"""
QtOrderingPrivate stands for the namespace 'QtOrderingPrivate' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.NamespaceGenerator from the records of Qt 6.12.0.
#  Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class QtOrderingPrivate:
  """
  The namespace 'QtOrderingPrivate' of Qt, which holds no objects. It holds
  the 1 enums Qt writes in it, each under its name, and the 1 names Qt has
  for the combinations of a flags enum, each holding the class of that enum.
  It is never made into an object.
  """

  class QtOrderingType(CuteFlags, scoped=True):
    """
    The flags enum 'QtOrderingPrivate::QtOrderingType' of Qt, with the 6
    names Qt gives in it. Qt names the type of its combinations
    'QtOrderingPrivate::QtOrderingTypeFlag'. C++ keeps these names inside the
    enum, so the class that holds the enum does not have them.
    """

    QtOrder = 0x0
    StdOrder = 0x1
    Partial = 0x0
    Weak = 0x20
    Strong = 0x40
    StrengthMask = 0x60

  QtOrderingTypeFlag = QtOrderingType
