"""
TokenType stands for the enum 'QXmlStreamReader::TokenType' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qxmlstream.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class TokenType(CuteNum):
  """
  The enum 'QXmlStreamReader::TokenType' of Qt, with the 11 names Qt gives in
  it.
  """

  NoToken = Kee[int](0)
  Invalid = Kee[int](1)
  StartDocument = Kee[int](2)
  EndDocument = Kee[int](3)
  StartElement = Kee[int](4)
  EndElement = Kee[int](5)
  Characters = Kee[int](6)
  Comment = Kee[int](7)
  DTD = Kee[int](8)
  EntityReference = Kee[int](9)
  ProcessingInstruction = Kee[int](10)
