"""
QtPrivate stands for the namespace 'QtPrivate' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.NamespaceGenerator from the records of Qt 6.12.0.
#  Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class QtPrivate:
  """
  The namespace 'QtPrivate' of Qt, which holds no objects. It holds the 6
  enums Qt writes in it, each under its name, and the 0 names Qt has for the
  combinations of a flags enum, each holding the class of that enum. It is
  never made into an object.
  """

  class LegacyUncomparable(CuteNum, scoped=True):
    """
    The enum 'QtPrivate::LegacyUncomparable' of Qt, with the 1 names Qt gives
    in it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Unordered = Kee[int](-127)

  class Operation(CuteNum, scoped=True):
    """
    The enum 'QtPrivate::Operation' of Qt, with the 10 names Qt gives in it.
    C++ keeps these names inside the enum, so the class that holds the enum
    does not have them.
    """

    Open = Kee[int](0)
    Close = Kee[int](1)
    Read = Kee[int](2)
    Write = Kee[int](3)
    VectoredRead = Kee[int](4)
    VectoredWrite = Kee[int](5)
    Flush = Kee[int](6)
    Stat = Kee[int](7)
    Cancel = Kee[int](8)
    NumOperations = Kee[int](9)

  class Ordering(CuteNum, scoped=True):
    """
    The enum 'QtPrivate::Ordering' of Qt, with the 4 names Qt gives in it.
    C++ keeps these names inside the enum, so the class that holds the enum
    does not have them.
    """

    Equal = Kee[int](0)
    Equivalent = Kee[int](0)
    Less = Kee[int](-1)
    Greater = Kee[int](1)

  class SynthesizedAccessFunction(CuteNum, scoped=True):
    """
    The enum 'QtPrivate::SynthesizedAccessFunction' of Qt, with the 2 names
    Qt gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    IterableSize = Kee[int](0)
    SequenceAt = Kee[int](1)

  class Uncomparable(CuteNum, scoped=True):
    """
    The enum 'QtPrivate::Uncomparable' of Qt, with the 1 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Unordered = Kee[int](2)

  class WakeMode(CuteNum, scoped=True):
    """
    The enum 'QtPrivate::WakeMode' of Qt, with the 2 names Qt gives in it.
    C++ keeps these names inside the enum, so the class that holds the enum
    does not have them.
    """

    One = Kee[int](1)
    All = Kee[int](-1)
