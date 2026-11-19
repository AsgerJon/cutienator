"""
PdfVersion stands for the enum 'QPagedPaintDevice::PdfVersion' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qpagedpaintdevice.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class PdfVersion(CuteNum):
  """
  The enum 'QPagedPaintDevice::PdfVersion' of Qt, with the 4 names Qt gives
  in it.
  """

  PdfVersion_1_4 = Kee[int](0)
  PdfVersion_A1b = Kee[int](1)
  PdfVersion_1_6 = Kee[int](2)
  PdfVersion_X4 = Kee[int](3)
