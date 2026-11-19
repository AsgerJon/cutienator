"""
Format stands for the enum 'QImage::Format' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of QtGui/qimage.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class Format(CuteNum):
  """
  The enum 'QImage::Format' of Qt, with the 38 names Qt gives in it.
  """

  Format_Invalid = Kee[int](0)
  Format_Mono = Kee[int](1)
  Format_MonoLSB = Kee[int](2)
  Format_Indexed8 = Kee[int](3)
  Format_RGB32 = Kee[int](4)
  Format_ARGB32 = Kee[int](5)
  Format_ARGB32_Premultiplied = Kee[int](6)
  Format_RGB16 = Kee[int](7)
  Format_ARGB8565_Premultiplied = Kee[int](8)
  Format_RGB666 = Kee[int](9)
  Format_ARGB6666_Premultiplied = Kee[int](10)
  Format_RGB555 = Kee[int](11)
  Format_ARGB8555_Premultiplied = Kee[int](12)
  Format_RGB888 = Kee[int](13)
  Format_RGB444 = Kee[int](14)
  Format_ARGB4444_Premultiplied = Kee[int](15)
  Format_RGBX8888 = Kee[int](16)
  Format_RGBA8888 = Kee[int](17)
  Format_RGBA8888_Premultiplied = Kee[int](18)
  Format_BGR30 = Kee[int](19)
  Format_A2BGR30_Premultiplied = Kee[int](20)
  Format_RGB30 = Kee[int](21)
  Format_A2RGB30_Premultiplied = Kee[int](22)
  Format_Alpha8 = Kee[int](23)
  Format_Grayscale8 = Kee[int](24)
  Format_RGBX64 = Kee[int](25)
  Format_RGBA64 = Kee[int](26)
  Format_RGBA64_Premultiplied = Kee[int](27)
  Format_Grayscale16 = Kee[int](28)
  Format_BGR888 = Kee[int](29)
  Format_RGBX16FPx4 = Kee[int](30)
  Format_RGBA16FPx4 = Kee[int](31)
  Format_RGBA16FPx4_Premultiplied = Kee[int](32)
  Format_RGBX32FPx4 = Kee[int](33)
  Format_RGBA32FPx4 = Kee[int](34)
  Format_RGBA32FPx4_Premultiplied = Kee[int](35)
  Format_CMYK8888 = Kee[int](36)
  NImageFormats = Kee[int](37)
