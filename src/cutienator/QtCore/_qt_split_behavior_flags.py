"""
SplitBehaviorFlags stands for the flags enum 'Qt::SplitBehaviorFlags' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qnamespace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class SplitBehaviorFlags(CuteFlags):
  """
  The flags enum 'Qt::SplitBehaviorFlags' of Qt, with the 2 names Qt gives in
  it. Qt names the type of its combinations 'Qt::SplitBehavior'.
  """

  KeepEmptyParts = 0x0
  SkipEmptyParts = 0x1
