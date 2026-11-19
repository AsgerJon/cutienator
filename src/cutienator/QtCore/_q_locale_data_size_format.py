"""
DataSizeFormat stands for the flags enum 'QLocale::DataSizeFormat' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qlocale.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class DataSizeFormat(CuteFlags):
  """
  The flags enum 'QLocale::DataSizeFormat' of Qt, with the 5 names Qt gives
  in it. Qt names the type of its combinations 'QLocale::DataSizeFormats'.
  """

  DataSizeBase1000 = 0x1
  DataSizeSIQuantifiers = 0x2
  DataSizeIecFormat = 0x0
  DataSizeTraditionalFormat = 0x2
  DataSizeSIFormat = 0x3
