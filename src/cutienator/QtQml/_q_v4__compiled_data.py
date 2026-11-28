"""
CompiledData stands for the namespace 'QV4::CompiledData' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.NamespaceGenerator from the records of Qt 6.12.0.
#  Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class CompiledData:
  """
  The namespace 'QV4::CompiledData' of Qt, which holds no objects. It holds
  the 2 enums Qt writes in it, each under its name, and the 0 names Qt has
  for the combinations of a flags enum, each holding the class of that enum.
  It is never made into an object.
  """

  class CommonType(CuteNum, scoped=True):
    """
    The enum 'QV4::CompiledData::CommonType' of Qt, with the 15 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Void = Kee[int](0)
    Var = Kee[int](1)
    Int = Kee[int](2)
    Bool = Kee[int](3)
    Real = Kee[int](4)
    String = Kee[int](5)
    Url = Kee[int](6)
    DateTime = Kee[int](7)
    RegExp = Kee[int](8)
    Time = Kee[int](9)
    Date = Kee[int](10)
    Rect = Kee[int](11)
    Point = Kee[int](12)
    Size = Kee[int](13)
    Invalid = Kee[int](14)

  class NamedBuiltin(CuteNum, scoped=True):
    """
    The enum 'QV4::CompiledData::NamedBuiltin' of Qt, with the 9 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Void = Kee[int](0)
    Var = Kee[int](1)
    Int = Kee[int](2)
    Bool = Kee[int](3)
    Real = Kee[int](4)
    String = Kee[int](5)
    Url = Kee[int](6)
    DateTime = Kee[int](7)
    RegExp = Kee[int](8)
