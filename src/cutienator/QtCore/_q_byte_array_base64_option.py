"""
Base64Option stands for the flags enum 'QByteArray::Base64Option' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qbytearray.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class Base64Option(CuteFlags):
  """
  The flags enum 'QByteArray::Base64Option' of Qt, with the 6 names Qt gives
  in it. Qt names the type of its combinations 'QByteArray::Base64Options'.
  """

  Base64Encoding = 0x0
  Base64UrlEncoding = 0x1
  KeepTrailingEquals = 0x0
  OmitTrailingEquals = 0x2
  IgnoreBase64DecodingErrors = 0x0
  AbortOnBase64DecodingErrors = 0x4
