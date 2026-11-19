"""
SortFlag stands for the flags enum 'QDir::SortFlag' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of QtCore/qdir.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class SortFlag(CuteFlags):
  """
  The flags enum 'QDir::SortFlag' of Qt, with the 12 names Qt gives in it. Qt
  names the type of its combinations 'QDir::SortFlags'.
  """

  Name = 0x0
  Time = 0x1
  Size = 0x2
  Unsorted = 0x3
  SortByMask = 0x3
  DirsFirst = 0x4
  Reversed = 0x8
  IgnoreCase = 0x10
  DirsLast = 0x20
  LocaleAware = 0x40
  Type = 0x80
  NoSort = -1
