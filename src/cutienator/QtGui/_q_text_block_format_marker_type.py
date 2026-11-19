"""
MarkerType stands for the enum 'QTextBlockFormat::MarkerType' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qtextformat.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class MarkerType(CuteNum, scoped=True):
  """
  The enum 'QTextBlockFormat::MarkerType' of Qt, with the 3 names Qt gives in
  it. C++ keeps these names inside the enum, so the class that holds the enum
  does not have them.
  """

  NoMarker = Kee[int](0)
  Unchecked = Kee[int](1)
  Checked = Kee[int](2)
