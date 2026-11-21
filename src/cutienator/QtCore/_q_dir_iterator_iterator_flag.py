"""
IteratorFlag stands for the flags enum 'QDirIterator::IteratorFlag' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qdiriterator.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class IteratorFlag(CuteFlags):
  """
  The flags enum 'QDirIterator::IteratorFlag' of Qt, with the 3 names Qt
  gives in it. Qt names the type of its combinations
  'QDirIterator::IteratorFlags'.
  """

  NoIteratorFlags = 0x0
  FollowSymlinks = 0x1
  Subdirectories = 0x2
