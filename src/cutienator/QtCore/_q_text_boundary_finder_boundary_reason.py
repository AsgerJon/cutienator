"""
BoundaryReason stands for the flags enum
'QTextBoundaryFinder::BoundaryReason' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qtextboundaryfinder.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class BoundaryReason(CuteFlags):
  """
  The flags enum 'QTextBoundaryFinder::BoundaryReason' of Qt, with the 6
  names Qt gives in it. Qt names the type of its combinations
  'QTextBoundaryFinder::BoundaryReasons'.
  """

  NotAtBoundary = 0x0
  BreakOpportunity = 0x1f
  StartOfItem = 0x20
  EndOfItem = 0x40
  MandatoryBreak = 0x80
  SoftHyphen = 0x100
