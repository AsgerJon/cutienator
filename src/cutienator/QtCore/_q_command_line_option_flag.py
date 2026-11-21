"""
Flag stands for the flags enum 'QCommandLineOption::Flag' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qcommandlineoption.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class Flag(CuteFlags):
  """
  The flags enum 'QCommandLineOption::Flag' of Qt, with the 3 names Qt gives
  in it. Qt names the type of its combinations 'QCommandLineOption::Flags'.
  """

  HiddenFromHelp = 0x1
  ShortOptionStyle = 0x2
  IgnoreOptionsAfter = 0x4
