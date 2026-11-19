"""
MarkdownFeature stands for the flags enum 'QTextDocument::MarkdownFeature' of
Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qtextdocument.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class MarkdownFeature(CuteFlags):
  """
  The flags enum 'QTextDocument::MarkdownFeature' of Qt, with the 3 names Qt
  gives in it. Qt names the type of its combinations
  'QTextDocument::MarkdownFeatures'.
  """

  MarkdownNoHTML = 0x60
  MarkdownDialectCommonMark = 0x0
  MarkdownDialectGitHub = 0x104f0c
