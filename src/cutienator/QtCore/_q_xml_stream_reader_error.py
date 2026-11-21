"""
Error stands for the enum 'QXmlStreamReader::Error' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qxmlstream.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class Error(CuteNum):
  """
  The enum 'QXmlStreamReader::Error' of Qt, with the 5 names Qt gives in it.
  """

  NoError = Kee[int](0)
  UnexpectedElementError = Kee[int](1)
  CustomError = Kee[int](2)
  NotWellFormedError = Kee[int](3)
  PrematureEndOfDocumentError = Kee[int](4)
