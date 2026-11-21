"""
AlphaPremultiplied stands for the enum 'QPixelFormat::AlphaPremultiplied' of
Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qpixelformat.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class AlphaPremultiplied(CuteNum):
  """
  The enum 'QPixelFormat::AlphaPremultiplied' of Qt, with the 2 names Qt
  gives in it.
  """

  NotPremultiplied = Kee[int](0)
  Premultiplied = Kee[int](1)
