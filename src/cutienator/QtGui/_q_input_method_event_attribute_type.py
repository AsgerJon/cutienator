"""
AttributeType stands for the enum 'QInputMethodEvent::AttributeType' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of QtGui/qevent.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class AttributeType(CuteNum):
  """
  The enum 'QInputMethodEvent::AttributeType' of Qt, with the 6 names Qt
  gives in it.
  """

  TextFormat = Kee[int](0)
  Cursor = Kee[int](1)
  Language = Kee[int](2)
  Ruby = Kee[int](3)
  Selection = Kee[int](4)
  MimeData = Kee[int](5)
