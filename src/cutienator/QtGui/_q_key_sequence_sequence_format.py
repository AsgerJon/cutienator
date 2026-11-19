"""
SequenceFormat stands for the enum 'QKeySequence::SequenceFormat' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qkeysequence.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class SequenceFormat(CuteNum):
  """
  The enum 'QKeySequence::SequenceFormat' of Qt, with the 2 names Qt gives in
  it.
  """

  NativeText = Kee[int](0)
  PortableText = Kee[int](1)
