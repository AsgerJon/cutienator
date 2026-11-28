"""
QtTemporalPattern stands for the namespace 'QtTemporalPattern' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.NamespaceGenerator from the records of Qt 6.12.0.
#  Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteFlags, CuteNum


class QtTemporalPattern:
  """
  The namespace 'QtTemporalPattern' of Qt, which holds no objects. It holds
  the 4 enums Qt writes in it, each under its name, and the 2 names Qt has
  for the combinations of a flags enum, each holding the class of that enum.
  It is never made into an object.
  """

  class DateTimePart(CuteFlags, scoped=True):
    """
    The flags enum 'QtTemporalPattern::DateTimePart' of Qt, with the 4 names
    Qt gives in it. Qt names the type of its combinations
    'QtTemporalPattern::DateTimeParts'. C++ keeps these names inside the
    enum, so the class that holds the enum does not have them.
    """

    NULL = 0x0
    Date = 0x1
    Time = 0x2
    Zone = 0x4

  DateTimeParts = DateTimePart

  class SupportType(CuteNum, scoped=True):
    """
    The enum 'QtTemporalPattern::SupportType' of Qt, with the 4 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Partial = Kee[int](-1)
    NULL = Kee[int](0)
    Clear = Kee[int](1)
    HasStrays = Kee[int](2)

  class TemporalFieldCategory(CuteNum, scoped=True):
    """
    The enum 'QtTemporalPattern::TemporalFieldCategory' of Qt, with the 14
    names Qt gives in it. C++ keeps these names inside the enum, so the class
    that holds the enum does not have them.
    """

    Literal = Kee[int](0)
    TimeZone = Kee[int](4)
    Second = Kee[int](20)
    SecondFraction = Kee[int](21)
    Minute = Kee[int](24)
    HourMod12 = Kee[int](30)
    Hour = Kee[int](31)
    PeriodInDay = Kee[int](33)
    DayOfWeek = Kee[int](64)
    DayOfMonth = Kee[int](65)
    Month = Kee[int](80)
    YearWithinCentury = Kee[int](92)
    Year = Kee[int](93)
    EndCategories = Kee[int](94)

  class TemporalFieldFlag(CuteFlags, number='unsigned int', scoped=True):
    """
    The flags enum 'QtTemporalPattern::TemporalFieldFlag' of Qt, with the 25
    names Qt gives in it. Qt names the type of its combinations
    'QtTemporalPattern::TemporalFieldFlags'. C++ keeps these names inside the
    enum, so the class that holds the enum does not have them.
    """

    Numeric = 0x1
    Verbal = 0x2
    Standalone = 0x4
    Narrow = 0x10
    Abbreviated = 0x20
    Short = 0x40
    Wide = 0x80
    ZeroPad = 0x100
    SpacePad = 0x200
    FlexSpace = 0x400
    StrictSpace = 0x800
    LowerCase = 0x1000
    UpperCase = 0x2000
    IgnoreCase = 0x4000
    RoundFraction = 0x10000
    YearSignIso8601 = 0x80000
    LocalizedZone = 0x100000
    Iso8601 = 0x200000
    AcceptUtcPrefix = 0x400000
    NeedNoUtcPrefix = 0x800000
    AllowZSuffix = 0x1000000
    GenericTime = 0x2000000
    StandardTime = 0x4000000
    DaylightSavingTime = 0x8000000
    LocalTimeName = 0x80000000

  TemporalFieldFlags = TemporalFieldFlag
