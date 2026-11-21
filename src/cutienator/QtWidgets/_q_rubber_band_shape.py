"""
Shape stands for the enum 'QRubberBand::Shape' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qrubberband.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class Shape(CuteNum):
  """
  The enum 'QRubberBand::Shape' of Qt, with the 2 names Qt gives in it.
  """

  Line = Kee[int](0)
  Rectangle = Kee[int](1)
