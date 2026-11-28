"""
QDBusUtil stands for the namespace 'QDBusUtil' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.NamespaceGenerator from the records of Qt 6.12.0.
#  Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class QDBusUtil:
  """
  The namespace 'QDBusUtil' of Qt, which holds no objects. It holds the 1
  enums Qt writes in it, each under its name, and the 0 names Qt has for the
  combinations of a flags enum, each holding the class of that enum. It is
  never made into an object.
  """

  class AllowEmptyFlag(CuteNum):
    """
    The enum 'QDBusUtil::AllowEmptyFlag' of Qt, with the 2 names Qt gives in
    it.
    """

    EmptyAllowed = Kee[int](0)
    EmptyNotAllowed = Kee[int](1)
