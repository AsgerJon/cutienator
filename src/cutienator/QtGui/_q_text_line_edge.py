"""
Edge stands for the enum 'QTextLine::Edge' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qtextlayout.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class Edge(CuteNum):
  """
  The enum 'QTextLine::Edge' of Qt, with the 2 names Qt gives in it.
  """

  Leading = Kee[int](0)
  Trailing = Kee[int](1)
