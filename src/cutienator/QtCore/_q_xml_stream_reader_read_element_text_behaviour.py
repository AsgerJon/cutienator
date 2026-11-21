"""
ReadElementTextBehaviour stands for the enum
'QXmlStreamReader::ReadElementTextBehaviour' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qxmlstream.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class ReadElementTextBehaviour(CuteNum):
  """
  The enum 'QXmlStreamReader::ReadElementTextBehaviour' of Qt, with the 3
  names Qt gives in it.
  """

  ErrorOnUnexpectedElement = Kee[int](0)
  IncludeChildElements = Kee[int](1)
  SkipChildElements = Kee[int](2)
