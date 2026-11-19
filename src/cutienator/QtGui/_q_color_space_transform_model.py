"""
TransformModel stands for the enum 'QColorSpace::TransformModel' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qcolorspace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class TransformModel(CuteNum, scoped=True):
  """
  The enum 'QColorSpace::TransformModel' of Qt, with the 2 names Qt gives in
  it. C++ keeps these names inside the enum, so the class that holds the enum
  does not have them.
  """

  ThreeComponentMatrix = Kee[int](0)
  ElementListProcessing = Kee[int](1)
