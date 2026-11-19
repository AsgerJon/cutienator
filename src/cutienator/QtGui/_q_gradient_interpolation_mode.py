"""
InterpolationMode stands for the enum 'QGradient::InterpolationMode' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of QtGui/qbrush.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class InterpolationMode(CuteNum):
  """
  The enum 'QGradient::InterpolationMode' of Qt, with the 2 names Qt gives in
  it.
  """

  ColorInterpolation = Kee[int](0)
  ComponentInterpolation = Kee[int](1)
