"""
ParsingMode stands for the enum 'QUrl::ParsingMode' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of QtCore/qurl.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class ParsingMode(CuteNum):
  """
  The enum 'QUrl::ParsingMode' of Qt, with the 3 names Qt gives in it.
  """

  TolerantMode = Kee[int](0)
  StrictMode = Kee[int](1)
  DecodedMode = Kee[int](2)
