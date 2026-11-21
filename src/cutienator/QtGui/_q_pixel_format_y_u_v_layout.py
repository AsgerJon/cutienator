"""
YUVLayout stands for the enum 'QPixelFormat::YUVLayout' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qpixelformat.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class YUVLayout(CuteNum):
  """
  The enum 'QPixelFormat::YUVLayout' of Qt, with the 16 names Qt gives in it.
  """

  YUV444 = Kee[int](0)
  YUV422 = Kee[int](1)
  YUV411 = Kee[int](2)
  YUV420P = Kee[int](3)
  YUV420SP = Kee[int](4)
  YV12 = Kee[int](5)
  UYVY = Kee[int](6)
  YUYV = Kee[int](7)
  NV12 = Kee[int](8)
  NV21 = Kee[int](9)
  IMC1 = Kee[int](10)
  IMC2 = Kee[int](11)
  IMC3 = Kee[int](12)
  IMC4 = Kee[int](13)
  Y8 = Kee[int](14)
  Y16 = Kee[int](15)
