"""
QSvgCssValues stands for the namespace 'QSvgCssValues' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.NamespaceGenerator from the records of Qt 6.12.0.
#  Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class QSvgCssValues:
  """
  The namespace 'QSvgCssValues' of Qt, which holds no objects. It holds the 2
  enums Qt writes in it, each under its name, and the 0 names Qt has for the
  combinations of a flags enum, each holding the class of that enum. It is
  never made into an object.
  """

  class EasingFunction(CuteNum, scoped=True):
    """
    The enum 'QSvgCssValues::EasingFunction' of Qt, with the 7 names Qt gives
    in it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Ease = Kee[int](0)
    EaseIn = Kee[int](1)
    EaseOut = Kee[int](2)
    EaseInOut = Kee[int](3)
    CubicBezier = Kee[int](4)
    Linear = Kee[int](5)
    Steps = Kee[int](6)

  class StepPosition(CuteNum, scoped=True):
    """
    The enum 'QSvgCssValues::StepPosition' of Qt, with the 6 names Qt gives
    in it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    JumpStart = Kee[int](0)
    JumpEnd = Kee[int](1)
    JumpNone = Kee[int](2)
    JumpBoth = Kee[int](3)
    Start = Kee[int](0)
    End = Kee[int](1)
