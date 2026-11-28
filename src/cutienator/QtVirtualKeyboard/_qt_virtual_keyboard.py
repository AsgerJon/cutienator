"""
QtVirtualKeyboard stands for the namespace 'QtVirtualKeyboard' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.NamespaceGenerator from the records of Qt 6.12.0.
#  Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteFlags, CuteNum


class QtVirtualKeyboard:
  """
  The namespace 'QtVirtualKeyboard' of Qt, which holds no objects. It holds
  the 3 enums Qt writes in it, each under its name, and the 1 names Qt has
  for the combinations of a flags enum, each holding the class of that enum.
  It is never made into an object.
  """

  class KeyType(CuteNum, scoped=True):
    """
    The enum 'QtVirtualKeyboard::KeyType' of Qt, with the 15 names Qt gives
    in it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    BaseKey = Kee[int](0)
    BackspaceKey = Kee[int](1)
    ChangeLanguageKey = Kee[int](2)
    EnterKey = Kee[int](3)
    FillerKey = Kee[int](4)
    HandwritingModeKey = Kee[int](5)
    HideKeyboardKey = Kee[int](6)
    InputModeKey = Kee[int](7)
    Key = Kee[int](8)
    ModeKey = Kee[int](9)
    NumberKey = Kee[int](10)
    ShiftKey = Kee[int](11)
    SpaceKey = Kee[int](12)
    SymbolModeKey = Kee[int](13)
    FlickKey = Kee[int](14)

  class KeyboardFunction(CuteNum, scoped=True):
    """
    The enum 'QtVirtualKeyboard::KeyboardFunction' of Qt, with the 3 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    HideInputPanel = Kee[int](0)
    ChangeLanguage = Kee[int](1)
    ToggleHandwritingMode = Kee[int](2)

  class KeyboardFunctionKey(CuteFlags, number='unsigned int', scoped=True):
    """
    The flags enum 'QtVirtualKeyboard::KeyboardFunctionKey' of Qt, with the 4
    names Qt gives in it. Qt names the type of its combinations
    'QtVirtualKeyboard::KeyboardFunctionKeys'. C++ keeps these names inside
    the enum, so the class that holds the enum does not have them.
    """

    NULL = 0x0
    Hide = 0x1
    Language = 0x2
    All = 0xffffffff

  KeyboardFunctionKeys = KeyboardFunctionKey
