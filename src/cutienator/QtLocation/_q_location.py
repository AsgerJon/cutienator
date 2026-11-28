"""
QLocation stands for the namespace 'QLocation' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.NamespaceGenerator from the records of Qt 6.12.0.
#  Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteFlags, CuteNum


class QLocation:
  """
  The namespace 'QLocation' of Qt, which holds no objects. It holds the 2
  enums Qt writes in it, each under its name, and the 1 names Qt has for the
  combinations of a flags enum, each holding the class of that enum. It is
  never made into an object.
  """

  class ReferenceSurface(CuteNum, scoped=True):
    """
    The enum 'QLocation::ReferenceSurface' of Qt, with the 2 names Qt gives
    in it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Map = Kee[int](0)
    Globe = Kee[int](1)

  class Visibility(CuteFlags):
    """
    The flags enum 'QLocation::Visibility' of Qt, with the 4 names Qt gives
    in it. Qt names the type of its combinations
    'QLocation::VisibilityScope'.
    """

    UnspecifiedVisibility = 0x0
    DeviceVisibility = 0x1
    PrivateVisibility = 0x2
    PublicVisibility = 0x4

  VisibilityScope = Visibility
