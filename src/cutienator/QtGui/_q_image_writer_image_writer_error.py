"""
ImageWriterError stands for the enum 'QImageWriter::ImageWriterError' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qimagewriter.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class ImageWriterError(CuteNum):
  """
  The enum 'QImageWriter::ImageWriterError' of Qt, with the 4 names Qt gives
  in it.
  """

  UnknownError = Kee[int](0)
  DeviceError = Kee[int](1)
  UnsupportedFormatError = Kee[int](2)
  InvalidImageError = Kee[int](3)
