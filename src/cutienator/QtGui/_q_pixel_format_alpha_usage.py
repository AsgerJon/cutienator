"""
AlphaUsage stands for the enum 'QPixelFormat::AlphaUsage' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qpixelformat.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class AlphaUsage(CuteNum):
  """
  The enum 'QPixelFormat::AlphaUsage' of Qt, with the 2 names Qt gives in it.
  """

  UsesAlpha = Kee[int](0)
  IgnoresAlpha = Kee[int](1)
