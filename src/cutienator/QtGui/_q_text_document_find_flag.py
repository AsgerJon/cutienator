"""
FindFlag stands for the flags enum 'QTextDocument::FindFlag' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qtextdocument.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class FindFlag(CuteFlags):
  """
  The flags enum 'QTextDocument::FindFlag' of Qt, with the 3 names Qt gives
  in it. Qt names the type of its combinations 'QTextDocument::FindFlags'.
  """

  FindBackward = 0x1
  FindCaseSensitively = 0x2
  FindWholeWords = 0x4
