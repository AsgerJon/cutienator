"""
QtSvg stands for the namespace 'QtSvg' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.NamespaceGenerator from the records of Qt 6.12.0.
#  Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteFlags, CuteNum


class QtSvg:
  """
  The namespace 'QtSvg' of Qt, which holds no objects. It holds the 4 enums
  Qt writes in it, each under its name, and the 1 names Qt has for the
  combinations of a flags enum, each holding the class of that enum. It is
  never made into an object.
  """

  class AnimatorType(CuteNum, scoped=True):
    """
    The enum 'QtSvg::AnimatorType' of Qt, with the 2 names Qt gives in it.
    C++ keeps these names inside the enum, so the class that holds the enum
    does not have them.
    """

    Controlled = Kee[int](0)
    Automatic = Kee[int](1)

  class OffsetRotateType(CuteNum, scoped=True):
    """
    The enum 'QtSvg::OffsetRotateType' of Qt, with the 5 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Auto = Kee[int](0)
    Angle = Kee[int](1)
    AutoAngle = Kee[int](2)
    Reverse = Kee[int](3)
    ReverseAngle = Kee[int](4)

  class Option(CuteFlags, number='unsigned int'):
    """
    The flags enum 'QtSvg::Option' of Qt, with the 6 names Qt gives in it. Qt
    names the type of its combinations 'QtSvg::Options'.
    """

    NoOption = 0x0
    Tiny12FeaturesOnly = 0x1
    AssumeTrustedSource = 0x2
    DisableSMILAnimations = 0x10
    DisableCSSAnimations = 0x20
    DisableAnimations = 0xf0

  Options = Option

  class UnitTypes(CuteNum, scoped=True):
    """
    The enum 'QtSvg::UnitTypes' of Qt, with the 3 names Qt gives in it. C++
    keeps these names inside the enum, so the class that holds the enum does
    not have them.
    """

    unknown = Kee[int](0)
    objectBoundingBox = Kee[int](1)
    userSpaceOnUse = Kee[int](2)
