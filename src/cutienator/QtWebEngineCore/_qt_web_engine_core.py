"""
QtWebEngineCore stands for the namespace 'QtWebEngineCore' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.NamespaceGenerator from the records of Qt 6.12.0.
#  Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class QtWebEngineCore:
  """
  The namespace 'QtWebEngineCore' of Qt, which holds no objects. It holds the
  1 enums Qt writes in it, each under its name, and the 0 names Qt has for
  the combinations of a flags enum, each holding the class of that enum. It
  is never made into an object.
  """

  class ReferrerPolicy(CuteNum, scoped=True):
    """
    The enum 'QtWebEngineCore::ReferrerPolicy' of Qt, with the 10 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Always = Kee[int](0)
    Default = Kee[int](1)
    NoReferrerWhenDowngrade = Kee[int](2)
    Never = Kee[int](3)
    Origin = Kee[int](4)
    OriginWhenCrossOrigin = Kee[int](5)
    NoReferrerWhenDowngradeOriginWhenCrossOrigin = Kee[int](6)
    SameOrigin = Kee[int](7)
    StrictOrigin = Kee[int](8)
    Last = Kee[int](8)
