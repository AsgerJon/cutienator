"""
ResourceType stands for the enum 'QTextDocument::ResourceType' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qtextdocument.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class ResourceType(CuteNum):
  """
  The enum 'QTextDocument::ResourceType' of Qt, with the 6 names Qt gives in
  it.
  """

  UnknownResource = Kee[int](0)
  HtmlResource = Kee[int](1)
  ImageResource = Kee[int](2)
  StyleSheetResource = Kee[int](3)
  MarkdownResource = Kee[int](4)
  UserResource = Kee[int](100)
