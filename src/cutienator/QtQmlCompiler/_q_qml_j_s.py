"""
QQmlJS stands for the namespace 'QQmlJS' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.NamespaceGenerator from the records of Qt 6.12.0.
#  Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class QQmlJS:
  """
  The namespace 'QQmlJS' of Qt, which holds no objects. It holds the 2 enums
  Qt writes in it, each under its name, and the 0 names Qt has for the
  combinations of a flags enum, each holding the class of that enum. It is
  never made into an object.
  """

  class CodegenResult(CuteNum, scoped=True):
    """
    The enum 'QQmlJS::CodegenResult' of Qt, with the 3 names Qt gives in it.
    C++ keeps these names inside the enum, so the class that holds the enum
    does not have them.
    """

    Success = Kee[int](0)
    Skip = Kee[int](1)
    Failure = Kee[int](2)

  class PrecedenceValues(CuteNum, scoped=True):
    """
    The enum 'QQmlJS::PrecedenceValues' of Qt, with the 3 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    InlineComponent = Kee[int](0)
    Default = Kee[int](1)
    ImplicitImport = Kee[int](127)
