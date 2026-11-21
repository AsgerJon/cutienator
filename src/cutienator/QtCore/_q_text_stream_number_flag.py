"""
NumberFlag stands for the flags enum 'QTextStream::NumberFlag' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qtextstream.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class NumberFlag(CuteFlags):
  """
  The flags enum 'QTextStream::NumberFlag' of Qt, with the 5 names Qt gives
  in it. Qt names the type of its combinations 'QTextStream::NumberFlags'.
  """

  ShowBase = 0x1
  ForcePoint = 0x2
  ForceSign = 0x4
  UppercaseBase = 0x8
  UppercaseDigits = 0x10
