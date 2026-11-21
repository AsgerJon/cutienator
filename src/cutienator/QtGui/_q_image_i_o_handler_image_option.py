"""
ImageOption stands for the enum 'QImageIOHandler::ImageOption' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qimageiohandler.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class ImageOption(CuteNum):
  """
  The enum 'QImageIOHandler::ImageOption' of Qt, with the 19 names Qt gives
  in it.
  """

  Size = Kee[int](0)
  ClipRect = Kee[int](1)
  Description = Kee[int](2)
  ScaledClipRect = Kee[int](3)
  ScaledSize = Kee[int](4)
  CompressionRatio = Kee[int](5)
  Gamma = Kee[int](6)
  Quality = Kee[int](7)
  Name = Kee[int](8)
  SubType = Kee[int](9)
  IncrementalReading = Kee[int](10)
  Endianness = Kee[int](11)
  Animation = Kee[int](12)
  BackgroundColor = Kee[int](13)
  ImageFormat = Kee[int](14)
  SupportedSubTypes = Kee[int](15)
  OptimizedWrite = Kee[int](16)
  ProgressiveScanWrite = Kee[int](17)
  ImageTransformation = Kee[int](18)
