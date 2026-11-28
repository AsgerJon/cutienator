"""
QUnicodeTools stands for the namespace 'QUnicodeTools' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.NamespaceGenerator from the records of Qt 6.12.0.
#  Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class QUnicodeTools:
  """
  The namespace 'QUnicodeTools' of Qt, which holds no objects. It holds the 1
  enums Qt writes in it, each under its name, and the 1 names Qt has for the
  combinations of a flags enum, each holding the class of that enum. It is
  never made into an object.
  """

  class CharAttributeOption(CuteFlags):
    """
    The flags enum 'QUnicodeTools::CharAttributeOption' of Qt, with the 7
    names Qt gives in it. Qt names the type of its combinations
    'QUnicodeTools::CharAttributeOptions'.
    """

    GraphemeBreaks = 0x1
    WordBreaks = 0x2
    SentenceBreaks = 0x4
    LineBreaks = 0x8
    WhiteSpaces = 0x10
    HangulLineBreakTailoring = 0x20
    DontClearAttributes = 0x1000

  CharAttributeOptions = CharAttributeOption
