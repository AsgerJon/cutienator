"""
MetaInformation stands for the enum 'QTextDocument::MetaInformation' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qtextdocument.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class MetaInformation(CuteNum):
  """
  The enum 'QTextDocument::MetaInformation' of Qt, with the 4 names Qt gives
  in it.
  """

  DocumentTitle = Kee[int](0)
  DocumentUrl = Kee[int](1)
  CssMedia = Kee[int](2)
  FrontMatter = Kee[int](3)
