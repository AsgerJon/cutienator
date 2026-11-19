"""
FontPropertiesInheritanceBehavior stands for the enum
'QTextCharFormat::FontPropertiesInheritanceBehavior' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qtextformat.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class FontPropertiesInheritanceBehavior(CuteNum):
  """
  The enum 'QTextCharFormat::FontPropertiesInheritanceBehavior' of Qt, with
  the 2 names Qt gives in it.
  """

  FontPropertiesSpecifiedOnly = Kee[int](0)
  FontPropertiesAll = Kee[int](1)
