"""
Mode stands for the enum 'QClipboard::Mode' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qclipboard.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class Mode(CuteNum):
  """
  The enum 'QClipboard::Mode' of Qt, with the 4 names Qt gives in it.
  """

  Clipboard = Kee[int](0)
  Selection = Kee[int](1)
  FindBuffer = Kee[int](2)
  LastMode = Kee[int](2)
