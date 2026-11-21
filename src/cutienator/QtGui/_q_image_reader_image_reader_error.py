"""
ImageReaderError stands for the enum 'QImageReader::ImageReaderError' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qimagereader.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class ImageReaderError(CuteNum):
  """
  The enum 'QImageReader::ImageReaderError' of Qt, with the 5 names Qt gives
  in it.
  """

  UnknownError = Kee[int](0)
  FileNotFoundError = Kee[int](1)
  DeviceError = Kee[int](2)
  UnsupportedFormatError = Kee[int](3)
  InvalidDataError = Kee[int](4)
