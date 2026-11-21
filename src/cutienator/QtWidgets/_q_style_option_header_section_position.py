"""
SectionPosition stands for the enum 'QStyleOptionHeader::SectionPosition' of
Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qstyleoption.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class SectionPosition(CuteNum):
  """
  The enum 'QStyleOptionHeader::SectionPosition' of Qt, with the 4 names Qt
  gives in it.
  """

  Beginning = Kee[int](0)
  Middle = Kee[int](1)
  End = Kee[int](2)
  OnlyOneSection = Kee[int](3)
