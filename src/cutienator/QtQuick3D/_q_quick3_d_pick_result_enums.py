"""
QQuick3DPickResultEnums stands for the namespace 'QQuick3DPickResultEnums' of
Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.NamespaceGenerator from the records of Qt 6.12.0.
#  Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class QQuick3DPickResultEnums:
  """
  The namespace 'QQuick3DPickResultEnums' of Qt, which holds no objects. It
  holds the 1 enums Qt writes in it, each under its name, and the 0 names Qt
  has for the combinations of a flags enum, each holding the class of that
  enum. It is never made into an object.
  """

  class HitType(CuteNum):
    """
    The enum 'QQuick3DPickResultEnums::HitType' of Qt, with the 3 names Qt
    gives in it.
    """

    Null = Kee[int](0)
    Model = Kee[int](1)
    Item = Kee[int](2)
