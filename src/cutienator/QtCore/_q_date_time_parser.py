"""
QDateTimeParser binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qdatetimeparser_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QDateTimeParser to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from . import QMetaType

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QCalendar, QDate, QDateTime, QLocale, QTime, QTimeZone
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCalendar = WAIT['QCalendar']
  QDate = WAIT['QDate']
  QDateTime = WAIT['QDateTime']
  QLocale = WAIT['QLocale']
  QTime = WAIT['QTime']
  QTimeZone = WAIT['QTimeZone']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDateTimeParser(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDateTimeParser: a plain Python object standing in
  front of one C++ QDateTimeParser.

  C++ hands a QDateTimeParser around as a copy, so every C++ QDateTimeParser
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDateTimeParser that has a ritual and that Python
  can call so far, 25 names in all: 'parse', 'fromString', 'parseFormat',
  'fieldInfo', 'setDefaultLocale', 'displayText', 'setCalendar',
  'sectionMaxSize', 'sectionText', 'scanString', 'potentialValue',
  'baseDate', 'sectionSize', 'sectionPos', 'sectionNode', 'sectionType',
  'getDigit', 'absoluteMax', 'absoluteMin', 'skipToNextSection', 'stateName',
  'getMinimum', 'getMaximum', 'cursorPosition', 'locale'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDateTimeParser::~QDateTimeParser()': the destructor: Python
    removes its C++ QDateTimeParser by it, and has no other use for it.
  - Qt's 'ParsedSection QDateTimeParser::parseSection(const QDateTime
    &currentValue, int sectionIndex, int offset) const': gives a type Python
    has no way to take yet.
  - Qt's 'int QDateTimeParser::findMonth(QStringView str, int monthstart, int
    sectionIndex, int year, QString *monthName, int *used) const': takes a
    number to change where it is.
  - Qt's 'int QDateTimeParser::findDay(QStringView str, int intDaystart, int
    sectionIndex, QString *dayName, int *used) const': takes a number to
    change where it is.
  - Qt's 'ParsedSection QDateTimeParser::findUtcOffset(QStringView str, int
    mode) const': gives a type Python has no way to take yet.
  - Qt's 'ParsedSection QDateTimeParser::findTimeZoneName(QStringView str,
    const QDateTime &when) const': gives a type Python has no way to take
    yet.
  - Qt's 'ParsedSection QDateTimeParser::findTimeZone(QStringView str, const
    QDateTime &when, int maxVal, int minVal, int mode) const': gives a type
    Python has no way to take yet.
  - Qt's 'AmPmFinder QDateTimeParser::findAmPm(QString &str, int index, int
    *used) const': takes a type Python has no way to hand over yet.
  - Qt's 'bool QDateTimeParser::potentialValue(const QString &str, int min,
    int max, int index, const QDateTime &currentValue, int insert) const':
    takes in Python what 'bool QDateTimeParser::potentialValue(QStringView
    str, int min, int max, int index, const QDateTime &currentValue, int
    insert) const' takes.
  - Qt's 'QString QDateTimeParser::getAmPmText(AmPm ap, Case cs) const':
    names the enum 'QDateTimeParser::Case', whose class cannot be named here.
  - Qt's 'bool QDateTimeParser::setDigit(QDateTime &t, int index, int newval)
    const': takes a type Python has no way to hand over yet.
  - Qt's 'bool QDateTimeParser::skipToNextSection(int section, const
    QDateTime &current, const QString &sectionText) const': takes in Python
    what 'bool QDateTimeParser::skipToNextSection(int section, const
    QDateTime &current, QStringView sectionText) const' takes.

  What to expect
  --------------

  - The C++ QDateTimeParser is created at the first use, not by
    'QDateTimeParser(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDateTimeParser back gives a copy the ritual made for
    Python, in a new cute QDateTimeParser.
  - Each name of Qt's QDateTimeParser that has no cute function yet,
    'findAmPm', 'findDay', 'findMonth', 'findTimeZone', 'findTimeZoneName',
    'findUtcOffset', 'getAmPmText', 'parseSection', 'setDigit', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QDateTimeParser, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class AmPm(CuteNum):
    """
    The enum 'QDateTimeParser::AmPm' of Qt, with the 2 names Qt gives in it.
    """

    AmText = Kee[int](0)
    PmText = Kee[int](1)

  class Context(CuteNum):
    """
    The enum 'QDateTimeParser::Context' of Qt, with the 2 names Qt gives in
    it.
    """

    FromString = Kee[int](0)
    DateTimeEdit = Kee[int](1)

  class FieldInfoFlag(CuteFlags):
    """
    The flags enum 'QDateTimeParser::FieldInfoFlag' of Qt, with the 4 names
    Qt gives in it. Qt names the type of its combinations
    'QDateTimeParser::FieldInfo'.
    """

    Numeric = 0x1
    FixedWidth = 0x2
    AllowPartial = 0x4
    Fraction = 0x8

  FieldInfo = FieldInfoFlag

  class Section(CuteFlags):
    """
    The flags enum 'QDateTimeParser::Section' of Qt, with the 24 names Qt
    gives in it. Qt names the type of its combinations
    'QDateTimeParser::Sections'.
    """

    NoSection = 0x0
    AmPmSection = 0x1
    MSecSection = 0x2
    SecondSection = 0x4
    MinuteSection = 0x8
    Hour12Section = 0x10
    Hour24Section = 0x20
    TimeZoneSection = 0x40
    HourSectionMask = 0x30
    TimeSectionMask = 0x7f
    DaySection = 0x100
    MonthSection = 0x200
    YearSection = 0x400
    YearSection2Digits = 0x800
    YearSectionMask = 0xc00
    DayOfWeekSectionShort = 0x1000
    DayOfWeekSectionLong = 0x2000
    DayOfWeekSectionMask = 0x3000
    DaySectionMask = 0x3100
    DateSectionMask = 0x3f00
    Internal = 0x10000
    FirstSection = 0x30000
    LastSection = 0x50000
    CalendarPopupSection = 0x90000

  Sections = Section

  class State(CuteNum):
    """
    The enum 'QDateTimeParser::State' of Qt, with the 3 names Qt gives in it.
    """

    Invalid = Kee[int](0)
    Intermediate = Kee[int](1)
    Acceptable = Kee[int](2)

  #  The classes Qt writes inside QDateTimeParser, each a class in here as in
  #  C++.

  class SectionNode(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QDateTimeParser::SectionNode: a plain Python object
    standing in front of one C++ QDateTimeParser::SectionNode.

    C++ hands a QDateTimeParser::SectionNode around as a copy, so every C++
    QDateTimeParser::SectionNode behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QDateTimeParser::SectionNode that has a ritual and
    that Python can call so far, 3 names in all: 'name', 'format',
    'maxChange'. None can be made from Python: one comes out of a function of
    another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QDateTimeParser::SectionNode::SectionNode(Section tp, int ps, int
      ct, int zs)': names the enum 'QDateTimeParser::Section', whose class
      cannot be named here.
    - Qt's 'QString QDateTimeParser::SectionNode::name(Section s)': names the
      enum 'QDateTimeParser::Section', whose class cannot be named here.
    - Qt's 'QDateTimeParser::SectionNode::~SectionNode()': the destructor:
      Python removes its C++ QDateTimeParser::SectionNode by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QDateTimeParser::SectionNode is created at the first use, not
      by 'QDateTimeParser::SectionNode(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QDateTimeParser::SectionNode back gives a copy the
      ritual made for Python, in a new cute QDateTimeParser::SectionNode.
    - Each name of Qt's QDateTimeParser::SectionNode that has no cute
      function yet, '__init__', holds a function that raises
      'NotImplementedError', and its docstring says why.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QDateTimeParser::SectionNode'

    #  Qt's '~QDateTimeParser::SectionNode()'. Naming it makes this a value
    #  class: Python owns every C++ QDateTimeParser::SectionNode behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN15QDateTimeParser11SectionNodeD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def name(self) -> str:
      """
      Calls Qt's 'QString QDateTimeParser::SectionNode::name() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qdatetimeparser-sectionnode.html#name

      Returns
      -------

      str
        The text Qt gave back.
      """
      #  QString QDateTimeParser::SectionNode::name() const
      return self.uglySide.call(
          'ritual_ZNK15QDateTimeParser11SectionNode4nameEv',
      )

    def format(self) -> str:
      """
      Calls Qt's 'QString QDateTimeParser::SectionNode::format() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qdatetimeparser-sectionnode.html#format

      Returns
      -------

      str
        The text Qt gave back.
      """
      #  QString QDateTimeParser::SectionNode::format() const
      return self.uglySide.call(
          'ritual_ZNK15QDateTimeParser11SectionNode6formatEv',
      )

    def maxChange(self) -> int:
      """
      Calls Qt's 'int QDateTimeParser::SectionNode::maxChange() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qdatetimeparser-sectionnode.html#maxChange
      """
      #  int QDateTimeParser::SectionNode::maxChange() const
      return self.uglySide.call(
          'ritual_ZNK15QDateTimeParser11SectionNode9maxChangeEv',
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    def __init__(*__, **_) -> Never:
      """
      Qt's 'QDateTimeParser::SectionNode::SectionNode(Section tp, int ps, int
      ct, int zs)': names the enum 'QDateTimeParser::Section', whose class
      cannot be named here.
      """
      raise NotImplementedError(
          "'QDateTimeParser.SectionNode.__init__' has no cute function yet. "
          "Qt's 'QDateTimeParser::SectionNode::SectionNode(Section tp, int "
          "ps, int ct, int zs)': names the enum 'QDateTimeParser::Section', "
          "whose class cannot be named here.")

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  class StateNode(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QDateTimeParser::StateNode: a plain Python object
    standing in front of one C++ QDateTimeParser::StateNode.

    C++ hands a QDateTimeParser::StateNode around as a copy, so every C++
    QDateTimeParser::StateNode behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QDateTimeParser::StateNode yet. It can be made from
    Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QDateTimeParser::StateNode::StateNode(const QDateTime &val, State
      ok, int pad, bool bad)': names the enum 'QDateTimeParser::State', whose
      class cannot be named here.
    - Qt's 'QDateTimeParser::StateNode::~StateNode()': the destructor: Python
      removes its C++ QDateTimeParser::StateNode by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QDateTimeParser::StateNode is created at the first use, not by
      'QDateTimeParser::StateNode(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QDateTimeParser::StateNode back gives a copy the
      ritual made for Python, in a new cute QDateTimeParser::StateNode.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QDateTimeParser::StateNode'

    #  Qt's '~QDateTimeParser::StateNode()'. Naming it makes this a value
    #  class: Python owns every C++ QDateTimeParser::StateNode behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN15QDateTimeParser9StateNodeD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'QDateTimeParser::StateNode::StateNode()', which is called at the first
      use.

      Qt's own words:
      https://doc.qt.io/qt-6/qdatetimeparser-statenode.html#StateNode
      """
      #  QDateTimeParser::StateNode::StateNode()
      self._noteCreation(QDateTimeParser.StateNode, lambda: Rituals.call(
          'ritual_ZN15QDateTimeParser9StateNodeC1Ev',
      ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDateTimeParser'

  #  A C++ QDateTimeParser Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDateTimeParser'

  #  The functions Qt calls itself that QDateTimeParser is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'displayText': (
          ('_ZNK15QDateTimeParser11displayTextEv',
           ('address', 'text', ''),
           ()),
      ),
      'getMinimum': (
          ('_ZNK15QDateTimeParser10getMinimumERK9QTimeZone',
           ('address', 'value', 'QtCore:QDateTime'),
           (
               ('address', 'value', 'QtCore:QTimeZone'),
           )),
      ),
      'getMaximum': (
          ('_ZNK15QDateTimeParser10getMaximumERK9QTimeZone',
           ('address', 'value', 'QtCore:QDateTime'),
           (
               ('address', 'value', 'QtCore:QTimeZone'),
           )),
      ),
      'cursorPosition': (
          ('_ZNK15QDateTimeParser14cursorPositionEv',
           ('int', 'number', ''),
           ()),
      ),
      'locale': (
          ('_ZNK15QDateTimeParser6localeEv',
           ('address', 'value', 'QtCore:QLocale'),
           ()),
      ),
  }

  #  Qt's '~QDateTimeParser()'. Naming it makes this a value class: Python
  #  owns every C++ QDateTimeParser behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QDateTimeParserD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str, int, QDateTime, bool)
  def parse(
      self,
      input: str,
      position: int,
      defaultValue: QDateTime,
      fixup: bool,
  ) -> StateNode:
    """
    Calls Qt's 'StateNode QDateTimeParser::parse(const QString &input, int
    position, const QDateTime &defaultValue, bool fixup) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeparser.html#parse

    Parameters
    ----------

    input : str
      Passed on as it is: a QString is made of it for the call.

    position : int
      Passed on as it is.

    defaultValue : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.

    fixup : bool
      Passed on as it is.

    Returns
    -------

    StateNode
      A new cute QDateTimeParser::StateNode around the copy Qt gave back.
      Python owns it.
    """
    #  StateNode QDateTimeParser::parse(const QString &input, int position,
    #      const QDateTime &defaultValue, bool fixup) const
    address = self._callAs(
        'QDateTimeParser',
        'ritual_ZNK15QDateTimeParser5parseERK7QStringiRK9QDateTimeb',
        input, position, self._valueOf(defaultValue), fixup,
    )
    return QDateTimeParser.StateNode._cuteOwning(address)

  @overload(str, QDate, QTime)
  @overload(str, QDate, NoneType)
  @overload(str, NoneType, QTime)
  @overload(str, NoneType, NoneType)
  @overload(str, QDate, QTime, int)
  @overload(str, QDate, NoneType, int)
  @overload(str, NoneType, QTime, int)
  @overload(str, NoneType, NoneType, int)
  def fromString(
      self,
      text: str,
      date: Optional[QDate],
      time: Optional[QTime],
      baseYear: int = 1900,
  ) -> bool:
    """
    Calls Qt's 'bool QDateTimeParser::fromString(const QString &text, QDate
    *date, QTime *time, int baseYear) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeparser.html#fromString

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    date : Optional[QDate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    time : Optional[QTime]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    baseYear : int
      Passed on as it is. May be left out, as in Qt: it is then 1900.
    """
    #  bool QDateTimeParser::fromString(const QString &text, QDate *date,
    #      QTime *time, int baseYear) const
    return self._callAs(
        'QDateTimeParser',
        'ritual_ZNK15QDateTimeParser10fromStringERK7QStringP5QDateP5QTimei',
        text, self._addressOf(date), self._addressOf(time), baseYear,
    )

  @overload(str, QDateTime, int)
  @overload(str, NoneType, int)
  def fromString(
      self,
      text: str,
      datetime: Optional[QDateTime],
      baseYear: int,
  ) -> bool:
    """
    Calls Qt's 'bool QDateTimeParser::fromString(const QString &text,
    QDateTime *datetime, int baseYear) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeparser.html#fromString

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    datetime : Optional[QDateTime]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    baseYear : int
      Passed on as it is.
    """
    #  bool QDateTimeParser::fromString(const QString &text, QDateTime
    #      *datetime, int baseYear) const
    return self._callAs(
        'QDateTimeParser',
        'ritual_ZNK15QDateTimeParser10fromStringERK7QStringP9QDateTimei',
        text, self._addressOf(datetime), baseYear,
    )

  @overload(int)
  def fieldInfo(self, index: int) -> FieldInfo:
    """
    Calls Qt's 'FieldInfo QDateTimeParser::fieldInfo(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeparser.html#fieldInfo

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    FieldInfo
      The value standing for the combination Qt gave back.
    """
    #  FieldInfo QDateTimeParser::fieldInfo(int index) const
    return QDateTimeParser.FieldInfo(self._callAs(
        'QDateTimeParser', 'ritual_ZNK15QDateTimeParser9fieldInfoEi', index,
    ))

  def displayText(self) -> str:
    """
    Calls Qt's 'QString QDateTimeParser::displayText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeparser.html#displayText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDateTimeParser::displayText() const
    ritual = 'ritual_ZNK15QDateTimeParser11displayTextEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QDateTimeParser11displayTextEv'
    return self._callAs('QDateTimeParser', ritual)

  @overload(Section, int)
  def sectionMaxSize(self, s: Section, count: int) -> int:
    """
    Calls Qt's 'int QDateTimeParser::sectionMaxSize(Section s, int count)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetimeparser.html#sectionMaxSize

    Parameters
    ----------

    s : Section
      Passed on as its number.

    count : int
      Passed on as it is.
    """
    #  int QDateTimeParser::sectionMaxSize(Section s, int count) const
    return self._callAs(
        'QDateTimeParser',
        'ritual_ZNK15QDateTimeParser14sectionMaxSizeENS_7SectionEi',
        s.value, count,
    )

  @overload(int)
  def sectionMaxSize(self, index: int) -> int:
    """
    Calls Qt's 'int QDateTimeParser::sectionMaxSize(int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetimeparser.html#sectionMaxSize

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  int QDateTimeParser::sectionMaxSize(int index) const
    return self._callAs(
        'QDateTimeParser', 'ritual_ZNK15QDateTimeParser14sectionMaxSizeEi',
        index,
    )

  @overload(str, int, int)
  def sectionText(self, text: str, sectionIndex: int, index: int) -> str:
    """
    Calls Qt's 'QString QDateTimeParser::sectionText(const QString &text, int
    sectionIndex, int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeparser.html#sectionText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    sectionIndex : int
      Passed on as it is.

    index : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDateTimeParser::sectionText(const QString &text, int
    #      sectionIndex, int index) const
    return self._callAs(
        'QDateTimeParser',
        'ritual_ZNK15QDateTimeParser11sectionTextERK7QStringii',
        text, sectionIndex, index,
    )

  @overload(int)
  def sectionText(self, sectionIndex: int) -> str:
    """
    Calls Qt's 'QString QDateTimeParser::sectionText(int sectionIndex)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeparser.html#sectionText

    Parameters
    ----------

    sectionIndex : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDateTimeParser::sectionText(int sectionIndex) const
    return self._callAs(
        'QDateTimeParser', 'ritual_ZNK15QDateTimeParser11sectionTextEi',
        sectionIndex,
    )

  @overload(QDateTime, bool)
  def scanString(self, defaultValue: QDateTime, fixup: bool) -> StateNode:
    """
    Calls Qt's 'StateNode QDateTimeParser::scanString(const QDateTime
    &defaultValue, bool fixup) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeparser.html#scanString

    Parameters
    ----------

    defaultValue : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.

    fixup : bool
      Passed on as it is.

    Returns
    -------

    StateNode
      A new cute QDateTimeParser::StateNode around the copy Qt gave back.
      Python owns it.
    """
    #  StateNode QDateTimeParser::scanString(const QDateTime &defaultValue,
    #      bool fixup) const
    address = self._callAs(
        'QDateTimeParser',
        'ritual_ZNK15QDateTimeParser10scanStringERK9QDateTimeb',
        self._valueOf(defaultValue), fixup,
    )
    return QDateTimeParser.StateNode._cuteOwning(address)

  @overload(str, int, int, int, QDateTime, int)
  def potentialValue(
      self,
      str: str,
      min: int,
      max: int,
      index: int,
      currentValue: QDateTime,
      insert: int,
  ) -> bool:
    """
    Calls Qt's 'bool QDateTimeParser::potentialValue(QStringView str, int
    min, int max, int index, const QDateTime &currentValue, int insert)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetimeparser.html#potentialValue

    Parameters
    ----------

    str : str
      Passed on as it is: a QString is made of it for the call.

    min : int
      Passed on as it is.

    max : int
      Passed on as it is.

    index : int
      Passed on as it is.

    currentValue : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.

    insert : int
      Passed on as it is.
    """
    #  bool QDateTimeParser::potentialValue(QStringView str, int min, int
    #      max, int index, const QDateTime &currentValue, int insert) const
    return self._callAs(
        'QDateTimeParser',
        'ritual_ZNK15QDateTimeParser14potentialValueE11QStringViewiiiRK9QDa'
        'teTimei',
        str, min, max, index, self._valueOf(currentValue), insert,
    )

  @overload(QTimeZone)
  def baseDate(self, zone: QTimeZone) -> QDateTime:
    """
    Calls Qt's 'QDateTime QDateTimeParser::baseDate(const QTimeZone &zone)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeparser.html#baseDate

    Parameters
    ----------

    zone : QTimeZone
      Passed on as a value: Qt reads the C++ QTimeZone, which stays Python's
      own.

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QDateTimeParser::baseDate(const QTimeZone &zone) const
    address = self._callAs(
        'QDateTimeParser',
        'ritual_ZNK15QDateTimeParser8baseDateERK9QTimeZone',
        self._valueOf(zone),
    )
    from . import QDateTime
    return QDateTime._cuteOwning(address)

  @overload(int)
  def sectionSize(self, index: int) -> int:
    """
    Calls Qt's 'int QDateTimeParser::sectionSize(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeparser.html#sectionSize

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  int QDateTimeParser::sectionSize(int index) const
    return self._callAs(
        'QDateTimeParser', 'ritual_ZNK15QDateTimeParser11sectionSizeEi',
        index,
    )

  @overload(int)
  def sectionPos(self, index: int) -> int:
    """
    Calls Qt's 'int QDateTimeParser::sectionPos(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeparser.html#sectionPos

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  int QDateTimeParser::sectionPos(int index) const
    return self._callAs(
        'QDateTimeParser', 'ritual_ZNK15QDateTimeParser10sectionPosEi',
        index,
    )

  @overload(SectionNode)
  def sectionPos(self, sn: SectionNode) -> int:
    """
    Calls Qt's 'int QDateTimeParser::sectionPos(SectionNode sn) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeparser.html#sectionPos

    Parameters
    ----------

    sn : SectionNode
      Passed on as a value: Qt reads the C++ QDateTimeParser::SectionNode,
      which stays Python's own.
    """
    #  int QDateTimeParser::sectionPos(SectionNode sn) const
    return self._callAs(
        'QDateTimeParser',
        'ritual_ZNK15QDateTimeParser10sectionPosENS_11SectionNodeE',
        self._valueOf(sn),
    )

  @overload(int)
  def sectionNode(self, index: int) -> SectionNode:
    """
    Calls Qt's 'const SectionNode &QDateTimeParser::sectionNode(int index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeparser.html#sectionNode

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    SectionNode
      A new cute QDateTimeParser::SectionNode around the copy Qt gave back.
      Python owns it.
    """
    #  const SectionNode &QDateTimeParser::sectionNode(int index) const
    address = self._callAs(
        'QDateTimeParser', 'ritual_ZNK15QDateTimeParser11sectionNodeEi',
        index,
    )
    return QDateTimeParser.SectionNode._cuteOwning(address)

  @overload(int)
  def sectionType(self, index: int) -> Section:
    """
    Calls Qt's 'Section QDateTimeParser::sectionType(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeparser.html#sectionType

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Section
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Section(number)' gives.
    """
    #  Section QDateTimeParser::sectionType(int index) const
    return QDateTimeParser.Section(self._callAs(
        'QDateTimeParser', 'ritual_ZNK15QDateTimeParser11sectionTypeEi',
        index,
    ))

  @overload(QDateTime, int)
  def getDigit(self, dt: QDateTime, index: int) -> int:
    """
    Calls Qt's 'int QDateTimeParser::getDigit(const QDateTime &dt, int index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeparser.html#getDigit

    Parameters
    ----------

    dt : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.

    index : int
      Passed on as it is.
    """
    #  int QDateTimeParser::getDigit(const QDateTime &dt, int index) const
    return self._callAs(
        'QDateTimeParser',
        'ritual_ZNK15QDateTimeParser8getDigitERK9QDateTimei',
        self._valueOf(dt), index,
    )

  @overload(int)
  @overload(int, QDateTime)
  def absoluteMax(
      self,
      index: int,
      value: Optional[QDateTime] = None,
  ) -> int:
    """
    Calls Qt's 'int QDateTimeParser::absoluteMax(int index, const QDateTime
    &value) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeparser.html#absoluteMax

    Parameters
    ----------

    index : int
      Passed on as it is.

    value : Optional[QDateTime]
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own. May be left out, as in Qt: a new 'QDateTime()' is then passed on.
    """
    #  int QDateTimeParser::absoluteMax(int index, const QDateTime &value)
    #      const
    if value is None:
      from . import QDateTime
      value = QDateTime()
    return self._callAs(
        'QDateTimeParser',
        'ritual_ZNK15QDateTimeParser11absoluteMaxEiRK9QDateTime',
        index, self._valueOf(value),
    )

  @overload(int)
  def absoluteMin(self, index: int) -> int:
    """
    Calls Qt's 'int QDateTimeParser::absoluteMin(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeparser.html#absoluteMin

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  int QDateTimeParser::absoluteMin(int index) const
    return self._callAs(
        'QDateTimeParser', 'ritual_ZNK15QDateTimeParser11absoluteMinEi',
        index,
    )

  @overload(int, QDateTime, str)
  def skipToNextSection(
      self,
      section: int,
      current: QDateTime,
      sectionText: str,
  ) -> bool:
    """
    Calls Qt's 'bool QDateTimeParser::skipToNextSection(int section, const
    QDateTime &current, QStringView sectionText) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetimeparser.html#skipToNextSection

    Parameters
    ----------

    section : int
      Passed on as it is.

    current : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.

    sectionText : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QDateTimeParser::skipToNextSection(int section, const QDateTime
    #      &current, QStringView sectionText) const
    return self._callAs(
        'QDateTimeParser',
        'ritual_ZNK15QDateTimeParser17skipToNextSectionEiRK9QDateTime11QStr'
        'ingView',
        section, self._valueOf(current), sectionText,
    )

  @overload(State)
  def stateName(self, s: State) -> str:
    """
    Calls Qt's 'QString QDateTimeParser::stateName(State s) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeparser.html#stateName

    Parameters
    ----------

    s : State
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDateTimeParser::stateName(State s) const
    return self._callAs(
        'QDateTimeParser',
        'ritual_ZNK15QDateTimeParser9stateNameENS_5StateE',
        s.value,
    )

  @overload(QTimeZone)
  def getMinimum(self, zone: QTimeZone) -> QDateTime:
    """
    Calls Qt's 'QDateTime QDateTimeParser::getMinimum(const QTimeZone &zone)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeparser.html#getMinimum

    Parameters
    ----------

    zone : QTimeZone
      Passed on as a value: Qt reads the C++ QTimeZone, which stays Python's
      own.

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QDateTimeParser::getMinimum(const QTimeZone &zone) const
    ritual = 'ritual_ZNK15QDateTimeParser10getMinimumERK9QTimeZone'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QDateTimeParser10getMinimumERK9QTimeZone'
    address = self._callAs('QDateTimeParser', ritual, self._valueOf(zone))
    from . import QDateTime
    return QDateTime._cuteOwning(address)

  @overload(QTimeZone)
  def getMaximum(self, zone: QTimeZone) -> QDateTime:
    """
    Calls Qt's 'QDateTime QDateTimeParser::getMaximum(const QTimeZone &zone)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeparser.html#getMaximum

    Parameters
    ----------

    zone : QTimeZone
      Passed on as a value: Qt reads the C++ QTimeZone, which stays Python's
      own.

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QDateTimeParser::getMaximum(const QTimeZone &zone) const
    ritual = 'ritual_ZNK15QDateTimeParser10getMaximumERK9QTimeZone'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QDateTimeParser10getMaximumERK9QTimeZone'
    address = self._callAs('QDateTimeParser', ritual, self._valueOf(zone))
    from . import QDateTime
    return QDateTime._cuteOwning(address)

  def cursorPosition(self) -> int:
    """
    Calls Qt's 'int QDateTimeParser::cursorPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetimeparser.html#cursorPosition
    """
    #  int QDateTimeParser::cursorPosition() const
    ritual = 'ritual_ZNK15QDateTimeParser14cursorPositionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QDateTimeParser14cursorPositionEv'
    return self._callAs('QDateTimeParser', ritual)

  def locale(self) -> QLocale:
    """
    Calls Qt's 'QLocale QDateTimeParser::locale() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeparser.html#locale

    Returns
    -------

    QLocale
      A new cute QLocale around the copy Qt gave back. Python owns it.
    """
    #  QLocale QDateTimeParser::locale() const
    ritual = 'ritual_ZNK15QDateTimeParser6localeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QDateTimeParser6localeEv'
    address = self._callAs('QDateTimeParser', ritual)
    from . import QLocale
    return QLocale._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QLocale)
  def setDefaultLocale(self, loc: QLocale) -> None:
    """
    Calls Qt's 'void QDateTimeParser::setDefaultLocale(const QLocale &loc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetimeparser.html#setDefaultLocale

    Parameters
    ----------

    loc : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.
    """
    #  void QDateTimeParser::setDefaultLocale(const QLocale &loc)
    self._callAs(
        'QDateTimeParser',
        'ritual_ZN15QDateTimeParser16setDefaultLocaleERK7QLocale',
        self._valueOf(loc),
    )

  @overload(QCalendar)
  def setCalendar(self, calendar: QCalendar) -> None:
    """
    Calls Qt's 'void QDateTimeParser::setCalendar(QCalendar calendar)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeparser.html#setCalendar

    Parameters
    ----------

    calendar : QCalendar
      Passed on as a value: Qt reads the C++ QCalendar, which stays Python's
      own.
    """
    #  void QDateTimeParser::setCalendar(QCalendar calendar)
    self._callAs(
        'QDateTimeParser',
        'ritual_ZN15QDateTimeParser11setCalendarE9QCalendar',
        self._valueOf(calendar),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QMetaType.Type, Context)
  @overload(QMetaType.Type, Context, QCalendar)
  def __init__(
      self,
      t: QMetaType.Type,
      ctx: Context,
      cal: Optional[QCalendar] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QDateTimeParser::QDateTimeParser(QMetaType::Type t, Context ctx,
    QCalendar cal)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetimeparser.html#QDateTimeParser

    Parameters
    ----------

    t : QMetaType.Type
      Passed on as its number.

    ctx : Context
      Passed on as its number.

    cal : Optional[QCalendar]
      Passed on as a value: Qt reads the C++ QCalendar, which stays Python's
      own. May be left out, as in Qt: a new 'QCalendar()' is then passed on.
    """
    #  QDateTimeParser::QDateTimeParser(QMetaType::Type t, Context ctx,
    #      QCalendar cal)
    if cal is None:
      from . import QCalendar
      cal = QCalendar()
    self._noteCreation(QDateTimeParser, lambda: Rituals.call(
        'ritual_ZN15QDateTimeParserC1EN9QMetaType4TypeENS_7ContextE9QCalend'
        'ar',
        t.value, ctx.value, self._valueOf(cal),
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def parseFormat(self, format: str) -> bool:
    """
    Calls Qt's 'bool QDateTimeParser::parseFormat(QStringView format)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeparser.html#parseFormat

    Parameters
    ----------

    format : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QDateTimeParser::parseFormat(QStringView format)
    return self._callAs(
        'QDateTimeParser',
        'ritual_ZN15QDateTimeParser11parseFormatE11QStringView',
        format,
    )

  @staticmethod
  def findAmPm(*__, **_) -> Never:
    """
    Qt's 'AmPmFinder QDateTimeParser::findAmPm(QString &str, int index, int
    *used) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QDateTimeParser.findAmPm' has no cute function yet. Qt's "
        "'AmPmFinder QDateTimeParser::findAmPm(QString &str, int index, int "
        "*used) const': takes a type Python has no way to hand over yet.")

  @staticmethod
  def findDay(*__, **_) -> Never:
    """
    Qt's 'int QDateTimeParser::findDay(QStringView str, int intDaystart, int
    sectionIndex, QString *dayName, int *used) const': takes a number to
    change where it is.
    """
    raise NotImplementedError(
        "'QDateTimeParser.findDay' has no cute function yet. Qt's 'int "
        "QDateTimeParser::findDay(QStringView str, int intDaystart, int "
        "sectionIndex, QString *dayName, int *used) const': takes a number "
        "to change where it is.")

  @staticmethod
  def findMonth(*__, **_) -> Never:
    """
    Qt's 'int QDateTimeParser::findMonth(QStringView str, int monthstart, int
    sectionIndex, int year, QString *monthName, int *used) const': takes a
    number to change where it is.
    """
    raise NotImplementedError(
        "'QDateTimeParser.findMonth' has no cute function yet. Qt's 'int "
        "QDateTimeParser::findMonth(QStringView str, int monthstart, int "
        "sectionIndex, int year, QString *monthName, int *used) const': "
        "takes a number to change where it is.")

  @staticmethod
  def findTimeZone(*__, **_) -> Never:
    """
    Qt's 'ParsedSection QDateTimeParser::findTimeZone(QStringView str, const
    QDateTime &when, int maxVal, int minVal, int mode) const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QDateTimeParser.findTimeZone' has no cute function yet. Qt's "
        "'ParsedSection QDateTimeParser::findTimeZone(QStringView str, "
        "const QDateTime &when, int maxVal, int minVal, int mode) const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def findTimeZoneName(*__, **_) -> Never:
    """
    Qt's 'ParsedSection QDateTimeParser::findTimeZoneName(QStringView str,
    const QDateTime &when) const': gives a type Python has no way to take
    yet.
    """
    raise NotImplementedError(
        "'QDateTimeParser.findTimeZoneName' has no cute function yet. Qt's "
        "'ParsedSection QDateTimeParser::findTimeZoneName(QStringView str, "
        "const QDateTime &when) const': gives a type Python has no way to "
        "take yet.")

  @staticmethod
  def findUtcOffset(*__, **_) -> Never:
    """
    Qt's 'ParsedSection QDateTimeParser::findUtcOffset(QStringView str, int
    mode) const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QDateTimeParser.findUtcOffset' has no cute function yet. Qt's "
        "'ParsedSection QDateTimeParser::findUtcOffset(QStringView str, int "
        "mode) const': gives a type Python has no way to take yet.")

  @staticmethod
  def getAmPmText(*__, **_) -> Never:
    """
    Qt's 'QString QDateTimeParser::getAmPmText(AmPm ap, Case cs) const':
    names the enum 'QDateTimeParser::Case', whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QDateTimeParser.getAmPmText' has no cute function yet. Qt's "
        "'QString QDateTimeParser::getAmPmText(AmPm ap, Case cs) const': "
        "names the enum 'QDateTimeParser::Case', whose class cannot be "
        "named here.")

  @staticmethod
  def parseSection(*__, **_) -> Never:
    """
    Qt's 'ParsedSection QDateTimeParser::parseSection(const QDateTime
    &currentValue, int sectionIndex, int offset) const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QDateTimeParser.parseSection' has no cute function yet. Qt's "
        "'ParsedSection QDateTimeParser::parseSection(const QDateTime "
        "&currentValue, int sectionIndex, int offset) const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def setDigit(*__, **_) -> Never:
    """
    Qt's 'bool QDateTimeParser::setDigit(QDateTime &t, int index, int newval)
    const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QDateTimeParser.setDigit' has no cute function yet. Qt's 'bool "
        "QDateTimeParser::setDigit(QDateTime &t, int index, int newval) "
        "const': takes a type Python has no way to hand over yet.")
