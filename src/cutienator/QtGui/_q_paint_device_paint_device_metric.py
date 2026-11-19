"""
PaintDeviceMetric stands for the enum 'QPaintDevice::PaintDeviceMetric' of
Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qpaintdevice.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class PaintDeviceMetric(CuteNum):
  """
  The enum 'QPaintDevice::PaintDeviceMetric' of Qt, with the 14 names Qt
  gives in it.
  """

  PdmWidth = Kee[int](1)
  PdmHeight = Kee[int](2)
  PdmWidthMM = Kee[int](3)
  PdmHeightMM = Kee[int](4)
  PdmNumColors = Kee[int](5)
  PdmDepth = Kee[int](6)
  PdmDpiX = Kee[int](7)
  PdmDpiY = Kee[int](8)
  PdmPhysicalDpiX = Kee[int](9)
  PdmPhysicalDpiY = Kee[int](10)
  PdmDevicePixelRatio = Kee[int](11)
  PdmDevicePixelRatioScaled = Kee[int](12)
  PdmDevicePixelRatioF_EncodedA = Kee[int](13)
  PdmDevicePixelRatioF_EncodedB = Kee[int](14)
