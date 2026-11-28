"""
QSql stands for the namespace 'QSql' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.NamespaceGenerator from the records of Qt 6.12.0.
#  Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteFlags, CuteNum


class QSql:
  """
  The namespace 'QSql' of Qt, which holds no objects. It holds the 4 enums Qt
  writes in it, each under its name, and the 1 names Qt has for the
  combinations of a flags enum, each holding the class of that enum. It is
  never made into an object.
  """

  class Location(CuteNum):
    """The enum 'QSql::Location' of Qt, with the 2 names Qt gives in it."""

    BeforeFirstRow = Kee[int](-1)
    AfterLastRow = Kee[int](-2)

  class NumericalPrecisionPolicy(CuteNum):
    """
    The enum 'QSql::NumericalPrecisionPolicy' of Qt, with the 4 names Qt
    gives in it.
    """

    LowPrecisionInt32 = Kee[int](1)
    LowPrecisionInt64 = Kee[int](2)
    LowPrecisionDouble = Kee[int](4)
    HighPrecision = Kee[int](0)

  class ParamTypeFlag(CuteFlags):
    """
    The flags enum 'QSql::ParamTypeFlag' of Qt, with the 4 names Qt gives in
    it. Qt names the type of its combinations 'QSql::ParamType'.
    """

    In = 0x1
    Out = 0x2
    InOut = 0x3
    Binary = 0x4

  ParamType = ParamTypeFlag

  class TableType(CuteNum):
    """The enum 'QSql::TableType' of Qt, with the 4 names Qt gives in it."""

    Tables = Kee[int](1)
    SystemTables = Kee[int](2)
    Views = Kee[int](4)
    AllTables = Kee[int](255)
