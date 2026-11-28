"""
OverrideSemantics stands for the namespace 'OverrideSemantics' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.NamespaceGenerator from the records of Qt 6.12.0.
#  Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class OverrideSemantics:
  """
  The namespace 'OverrideSemantics' of Qt, which holds no objects. It holds
  the 2 enums Qt writes in it, each under its name, and the 0 names Qt has
  for the combinations of a flags enum, each holding the class of that enum.
  It is never made into an object.
  """

  class CheckMode(CuteNum, scoped=True):
    """
    The enum 'OverrideSemantics::CheckMode' of Qt, with the 2 names Qt gives
    in it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Minimal = Kee[int](0)
    Full = Kee[int](1)

  class Status(CuteNum, scoped=True):
    """
    The enum 'OverrideSemantics::Status' of Qt, with the 9 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Valid = Kee[int](0)
    NoOverride = Kee[int](1)
    MissingBase = Kee[int](2)
    OverridingFinal = Kee[int](3)
    OverridingNonVirtual = Kee[int](4)
    OverridingNonVirtualError = Kee[int](5)
    MissingOverrideOrFinalSpecifier = Kee[int](6)
    InvokabilityMismatch = Kee[int](7)
    Unknown = Kee[int](8)
