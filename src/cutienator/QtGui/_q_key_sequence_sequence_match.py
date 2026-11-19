"""
SequenceMatch stands for the enum 'QKeySequence::SequenceMatch' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qkeysequence.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class SequenceMatch(CuteNum):
  """
  The enum 'QKeySequence::SequenceMatch' of Qt, with the 3 names Qt gives in
  it.
  """

  NoMatch = Kee[int](0)
  PartialMatch = Kee[int](1)
  ExactMatch = Kee[int](2)
