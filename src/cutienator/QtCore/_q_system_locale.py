"""
QSystemLocale binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qlocale_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QSystemLocale to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QLocale, QVariant


class QSystemLocale(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSystemLocale: a plain Python object standing in
  front of one C++ QSystemLocale.

  What exists
  -----------

  Every function of Qt's QSystemLocale that has a ritual and that Python can
  call so far, 2 names in all: 'fallbackLocale', 'fallbackLocaleIndex'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSystemLocale::~QSystemLocale()': the destructor: Python never
    removes a C++ QSystemLocale.
  - Qt's 'QVariant QSystemLocale::query(QueryType type, QVariant &&in)
    const': takes a type Python has no way to hand over yet.
  - Qt's 'const QSharedDataPointer<QLocalePrivate>
    QSystemLocale::localeData(const QLocale &locale) const': gives a type
    Python has no way to take yet.

  What has no ritual
  ------------------

  4 of the 10 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QSystemLocale is created at the first use, not by
    'QSystemLocale(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSystemLocale.
  - Each name of Qt's QSystemLocale that has no cute function yet,
    'localeData', 'query', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QSystemLocale, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class QueryType(CuteNum):
    """
    The enum 'QSystemLocale::QueryType' of Qt, with the 48 names Qt gives in
    it.
    """

    LanguageId = Kee[int](0)
    TerritoryId = Kee[int](1)
    DecimalPoint = Kee[int](2)
    Grouping = Kee[int](3)
    GroupSeparator = Kee[int](4)
    ZeroDigit = Kee[int](5)
    NegativeSign = Kee[int](6)
    DateFormatLong = Kee[int](7)
    DateFormatShort = Kee[int](8)
    TimeFormatLong = Kee[int](9)
    TimeFormatShort = Kee[int](10)
    DayNameLong = Kee[int](11)
    DayNameShort = Kee[int](12)
    DayNameNarrow = Kee[int](13)
    MonthNameLong = Kee[int](14)
    MonthNameShort = Kee[int](15)
    MonthNameNarrow = Kee[int](16)
    DateToStringLong = Kee[int](17)
    DateToStringShort = Kee[int](18)
    TimeToStringLong = Kee[int](19)
    TimeToStringShort = Kee[int](20)
    DateTimeFormatLong = Kee[int](21)
    DateTimeFormatShort = Kee[int](22)
    DateTimeToStringLong = Kee[int](23)
    DateTimeToStringShort = Kee[int](24)
    MeasurementSystem = Kee[int](25)
    PositiveSign = Kee[int](26)
    AMText = Kee[int](27)
    PMText = Kee[int](28)
    FirstDayOfWeek = Kee[int](29)
    Weekdays = Kee[int](30)
    CurrencySymbol = Kee[int](31)
    CurrencyToString = Kee[int](32)
    Collation = Kee[int](33)
    UILanguages = Kee[int](34)
    StringToStandardQuotation = Kee[int](35)
    StringToAlternateQuotation = Kee[int](36)
    ScriptId = Kee[int](37)
    ListToSeparatedString = Kee[int](38)
    LocaleChanged = Kee[int](39)
    NativeLanguageName = Kee[int](40)
    NativeTerritoryName = Kee[int](41)
    StandaloneMonthNameLong = Kee[int](42)
    StandaloneMonthNameShort = Kee[int](43)
    StandaloneMonthNameNarrow = Kee[int](44)
    StandaloneDayNameLong = Kee[int](45)
    StandaloneDayNameShort = Kee[int](46)
    StandaloneDayNameNarrow = Kee[int](47)

  #  The classes Qt writes inside QSystemLocale, each a class in here as in
  #  C++.

  class CurrencyToStringArgument(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSystemLocale::CurrencyToStringArgument: a plain
    Python object standing in front of one C++
    QSystemLocale::CurrencyToStringArgument.

    C++ hands a QSystemLocale::CurrencyToStringArgument around as a copy, so
    every C++ QSystemLocale::CurrencyToStringArgument behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QSystemLocale::CurrencyToStringArgument yet. It can
    be made from Python, in 2 ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's
      'QSystemLocale::CurrencyToStringArgument::~CurrencyToStringArgument()':
      the destructor: Python removes its C++
      QSystemLocale::CurrencyToStringArgument by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QSystemLocale::CurrencyToStringArgument is created at the first
      use, not by 'QSystemLocale::CurrencyToStringArgument(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSystemLocale::CurrencyToStringArgument back gives
      a copy the ritual made for Python, in a new cute
      QSystemLocale::CurrencyToStringArgument.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QVariant = WAIT['QVariant']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSystemLocale::CurrencyToStringArgument'

    #  Qt's '~QSystemLocale::CurrencyToStringArgument()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QSystemLocale::CurrencyToStringArgument behind a cute one, and removes
    #  it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN13QSystemLocale24CurrencyToStringArgumentD1Ev')

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
      'QSystemLocale::CurrencyToStringArgument::CurrencyToStringArgument()',
      which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qsystemlocale-currencytostringargument.html
      """
      #  QSystemLocale::CurrencyToStringArgument::CurrencyToStringArgument()
      self._noteCreation(
          QSystemLocale.CurrencyToStringArgument, lambda: Rituals.call(
              'ritual_ZN13QSystemLocale24CurrencyToStringArgumentC1Ev',
          ))

    @overload(QVariant, str)
    def __init__(self, v: QVariant, s: str) -> None:
      """
      Notes what was given, for Qt's
      'QSystemLocale::CurrencyToStringArgument::CurrencyToStringArgument(
      const QVariant &v, const QString &s)', which is called at the first
      use.

      Qt's own words:
      https://doc.qt.io/qt-6/qsystemlocale-currencytostringargument.html

      Parameters
      ----------

      v : QVariant
        Passed on as a value: Qt reads the C++ QVariant, which stays Python's
        own.

      s : str
        Passed on as it is: a QString is made of it for the call.
      """
      #  QSystemLocale::CurrencyToStringArgument::
      #      CurrencyToStringArgument(const QVariant &v, const QString &s)
      self._noteCreation(
          QSystemLocale.CurrencyToStringArgument, lambda: Rituals.call(
              'ritual_ZN13QSystemLocale24CurrencyToStringArgumentC1ERK8QVar'
              'iantRK7QString',
              self._valueOf(v), s,
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
  __qt_class__ = 'QSystemLocale'

  #  A C++ QSystemLocale Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSystemLocale'

  #  The functions Qt calls itself that QSystemLocale is the first to declare
  #  and that cannot be handed to Python yet, each as Qt declares it. A class
  #  of a program that writes one of them anew is refused, since Qt would
  #  never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'query': (
          'QVariant QSystemLocale::query(QueryType, QVariant &&) const',
      ),
  }

  #  The functions Qt calls itself that QSystemLocale is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'fallbackLocale': (
          ('_ZNK13QSystemLocale14fallbackLocaleEv',
           ('address', 'value', 'QtCore:QLocale'),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def fallbackLocale(self) -> QLocale:
    """
    Calls Qt's 'QLocale QSystemLocale::fallbackLocale() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsystemlocale.html#fallbackLocale

    Returns
    -------

    QLocale
      A new cute QLocale around the copy Qt gave back. Python owns it.
    """
    #  QLocale QSystemLocale::fallbackLocale() const
    ritual = 'ritual_ZNK13QSystemLocale14fallbackLocaleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QSystemLocale14fallbackLocaleEv'
    address = self.uglySide.call(ritual)
    from . import QLocale
    return QLocale._cuteOwning(address)

  def fallbackLocaleIndex(self) -> int:
    """
    Calls Qt's 'qsizetype QSystemLocale::fallbackLocaleIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsystemlocale.html#fallbackLocaleIndex
    """
    #  qsizetype QSystemLocale::fallbackLocaleIndex() const
    return self.uglySide.call(
        'ritual_ZNK13QSystemLocale19fallbackLocaleIndexEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QSystemLocale::QSystemLocale()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsystemlocale.html#QSystemLocale
    """
    #  QSystemLocale::QSystemLocale()
    self._noteCreation(QSystemLocale, lambda: Rituals.call(
        'ritual_ZN13QSystemLocaleC1Ev',
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

  @staticmethod
  def localeData(*__, **_) -> Never:
    """
    Qt's 'const QSharedDataPointer<QLocalePrivate>
    QSystemLocale::localeData(const QLocale &locale) const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSystemLocale.localeData' has no cute function yet. Qt's 'const "
        "QSharedDataPointer<QLocalePrivate> QSystemLocale::localeData(const "
        "QLocale &locale) const': gives a type Python has no way to take "
        "yet.")

  @staticmethod
  def query(*__, **_) -> Never:
    """
    Qt's 'QVariant QSystemLocale::query(QueryType type, QVariant &&in)
    const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSystemLocale.query' has no cute function yet. Qt's 'QVariant "
        "QSystemLocale::query(QueryType type, QVariant &&in) const': takes "
        "a type Python has no way to hand over yet.")
