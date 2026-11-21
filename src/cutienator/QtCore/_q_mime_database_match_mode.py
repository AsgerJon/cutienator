"""
MatchMode stands for the enum 'QMimeDatabase::MatchMode' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qmimedatabase.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class MatchMode(CuteNum):
  """
  The enum 'QMimeDatabase::MatchMode' of Qt, with the 3 names Qt gives in it.
  """

  MatchDefault = Kee[int](0)
  MatchExtension = Kee[int](1)
  MatchContent = Kee[int](2)
