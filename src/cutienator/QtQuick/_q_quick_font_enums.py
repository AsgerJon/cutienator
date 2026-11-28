"""
QQuickFontEnums stands for the namespace 'QQuickFontEnums' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.NamespaceGenerator from the records of Qt 6.12.0.
#  Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class QQuickFontEnums:
  """
  The namespace 'QQuickFontEnums' of Qt, which holds no objects. It holds the
  4 enums Qt writes in it, each under its name, and the 0 names Qt has for
  the combinations of a flags enum, each holding the class of that enum. It
  is never made into an object.
  """

  class Capitalization(CuteNum):
    """
    The enum 'QQuickFontEnums::Capitalization' of Qt, with the 5 names Qt
    gives in it.
    """

    MixedCase = Kee[int](0)
    AllUppercase = Kee[int](1)
    AllLowercase = Kee[int](2)
    SmallCaps = Kee[int](3)
    Capitalize = Kee[int](4)

  class FontWeight(CuteNum):
    """
    The enum 'QQuickFontEnums::FontWeight' of Qt, with the 9 names Qt gives
    in it.
    """

    Thin = Kee[int](100)
    ExtraLight = Kee[int](200)
    Light = Kee[int](300)
    Normal = Kee[int](400)
    Medium = Kee[int](500)
    DemiBold = Kee[int](600)
    Bold = Kee[int](700)
    ExtraBold = Kee[int](800)
    Black = Kee[int](900)

  class HintingPreference(CuteNum):
    """
    The enum 'QQuickFontEnums::HintingPreference' of Qt, with the 4 names Qt
    gives in it.
    """

    PreferDefaultHinting = Kee[int](0)
    PreferNoHinting = Kee[int](1)
    PreferVerticalHinting = Kee[int](2)
    PreferFullHinting = Kee[int](3)

  class Style(CuteNum):
    """
    The enum 'QQuickFontEnums::Style' of Qt, with the 3 names Qt gives in it.
    """

    StyleNormal = Kee[int](0)
    StyleItalic = Kee[int](1)
    StyleOblique = Kee[int](2)
