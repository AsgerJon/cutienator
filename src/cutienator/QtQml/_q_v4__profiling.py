"""
Profiling stands for the namespace 'QV4::Profiling' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.NamespaceGenerator from the records of Qt 6.12.0.
#  Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class Profiling:
  """
  The namespace 'QV4::Profiling' of Qt, which holds no objects. It holds the
  2 enums Qt writes in it, each under its name, and the 0 names Qt has for
  the combinations of a flags enum, each holding the class of that enum. It
  is never made into an object.
  """

  class Features(CuteNum):
    """
    The enum 'QV4::Profiling::Features' of Qt, with the 2 names Qt gives in
    it.
    """

    FeatureFunctionCall = Kee[int](0)
    FeatureMemoryAllocation = Kee[int](1)

  class MemoryType(CuteNum):
    """
    The enum 'QV4::Profiling::MemoryType' of Qt, with the 3 names Qt gives in
    it.
    """

    HeapPage = Kee[int](0)
    LargeItem = Kee[int](1)
    RegularItem = Kee[int](2)
