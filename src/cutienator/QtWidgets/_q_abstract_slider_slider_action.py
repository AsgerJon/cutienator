"""
SliderAction stands for the enum 'QAbstractSlider::SliderAction' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qabstractslider.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class SliderAction(CuteNum):
  """
  The enum 'QAbstractSlider::SliderAction' of Qt, with the 8 names Qt gives
  in it.
  """

  SliderNoAction = Kee[int](0)
  SliderSingleStepAdd = Kee[int](1)
  SliderSingleStepSub = Kee[int](2)
  SliderPageStepAdd = Kee[int](3)
  SliderPageStepSub = Kee[int](4)
  SliderToMinimum = Kee[int](5)
  SliderToMaximum = Kee[int](6)
  SliderMove = Kee[int](7)
