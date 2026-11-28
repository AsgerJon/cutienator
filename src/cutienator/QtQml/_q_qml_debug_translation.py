"""
QQmlDebugTranslation stands for the namespace 'QQmlDebugTranslation' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.NamespaceGenerator from the records of Qt 6.12.0.
#  Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class QQmlDebugTranslation:
  """
  The namespace 'QQmlDebugTranslation' of Qt, which holds no objects. It
  holds the 2 enums Qt writes in it, each under its name, and the 0 names Qt
  has for the combinations of a flags enum, each holding the class of that
  enum. It is never made into an object.
  """

  class Reply(CuteNum, scoped=True):
    """
    The enum 'QQmlDebugTranslation::Reply' of Qt, with the 7 names Qt gives
    in it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    LanguageChanged = Kee[int](101)
    StateList = Kee[int](102)
    StateChanged = Kee[int](103)
    TranslationIssues = Kee[int](104)
    TranslatableTextOccurrences = Kee[int](105)
    MissingTranslations = Kee[int](106)
    TextElided = Kee[int](107)

  class Request(CuteNum, scoped=True):
    """
    The enum 'QQmlDebugTranslation::Request' of Qt, with the 8 names Qt gives
    in it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    ChangeLanguage = Kee[int](1)
    StateList = Kee[int](2)
    ChangeState = Kee[int](3)
    TranslationIssues = Kee[int](4)
    TranslatableTextOccurrences = Kee[int](5)
    WatchTextElides = Kee[int](6)
    DisableWatchTextElides = Kee[int](7)
    MissingTranslations = Kee[int](8)
