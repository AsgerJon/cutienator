"""
StyleOptionVersion stands for the enum
'QStyleOptionHeader::StyleOptionVersion' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qstyleoption.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class StyleOptionVersion(CuteNum):
  """
  The enum 'QStyleOptionHeader::StyleOptionVersion' of Qt, with the 1 names
  Qt gives in it.
  """

  Version = Kee[int](1)
