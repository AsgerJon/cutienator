"""
QTimeZone binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qtimezone.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from . import Qt, QLocale

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QByteArray, QByteArrayView, QDateTime, QDebug
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QByteArrayView = WAIT['QByteArrayView']
  QDateTime = WAIT['QDateTime']
  QDebug = WAIT['QDebug']


class QTimeZone(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QTimeZone: a plain Python object standing in front of
  one C++ QTimeZone.

  C++ hands a QTimeZone around as a copy, so every C++ QTimeZone behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QTimeZone that has a ritual and that Python can call
  so far, 30 names in all: 'isValid', 'fromSecondsAheadOfUtc', 'timeSpec',
  'fixedSecondsAheadOfUtc', 'isUtcOrFixedOffset', 'asBackendZone',
  'hasAlternativeName', 'id', 'country', 'comment', 'displayName',
  'abbreviation', 'offsetFromUtc', 'standardTimeOffset',
  'daylightTimeOffset', 'hasDaylightTime', 'isDaylightTime', 'offsetData',
  'hasTransitions', 'nextTransition', 'previousTransition',
  'systemTimeZoneId', 'systemTimeZone', 'utc', 'isTimeZoneIdAvailable',
  'ianaIdToWindowsId', 'windowsIdToDefaultIanaId', '__eq__', '__ne__',
  '__rlshift__'. It can be made from Python, in 5 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTimeZone::~QTimeZone()': the destructor: Python removes its C++
    QTimeZone by it, and has no other use for it.

  What has no ritual
  ------------------

  18 of the 56 functions Qt declares: 15 takes or gives a type that cannot be
  passed yet; 2 private; 1 forbidden.

  What to expect
  --------------

  - The C++ QTimeZone is created at the first use, not by 'QTimeZone(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QTimeZone back gives a copy the ritual made for
    Python, in a new cute QTimeZone.
  """

  #  The enums Qt writes inside QTimeZone, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class Initialization(CuteNum):
    """
    The enum 'QTimeZone::Initialization' of Qt, with the 2 names Qt gives in
    it.
    """

    LocalTime = Kee[int](0)
    UTC = Kee[int](1)

  class NameType(CuteNum):
    """
    The enum 'QTimeZone::NameType' of Qt, with the 4 names Qt gives in it.
    """

    DefaultName = Kee[int](0)
    LongName = Kee[int](1)
    ShortName = Kee[int](2)
    OffsetName = Kee[int](3)

  class TimeType(CuteNum):
    """
    The enum 'QTimeZone::TimeType' of Qt, with the 3 names Qt gives in it.
    """

    StandardTime = Kee[int](0)
    DaylightTime = Kee[int](1)
    GenericTime = Kee[int](2)

  #  The classes Qt writes inside QTimeZone, each a class in here as in C++.

  class OffsetData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QTimeZone::OffsetData: a plain Python object
    standing in front of one C++ QTimeZone::OffsetData.

    C++ hands a QTimeZone::OffsetData around as a copy, so every C++
    QTimeZone::OffsetData behind a cute one is Python's own: it is removed,
    by the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QTimeZone::OffsetData yet. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QTimeZone::OffsetData::~OffsetData()': the destructor: Python
      removes its C++ QTimeZone::OffsetData by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QTimeZone::OffsetData is created at the first use, not by
      'QTimeZone::OffsetData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QTimeZone::OffsetData back gives a copy the ritual
      made for Python, in a new cute QTimeZone::OffsetData.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QTimeZone::OffsetData'

    #  Qt's '~QTimeZone::OffsetData()'. Naming it makes this a value class:
    #  Python owns every C++ QTimeZone::OffsetData behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN9QTimeZone10OffsetDataD1Ev'

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

  @staticmethod
  @overload(int)
  def fromSecondsAheadOfUtc(offset: int) -> QTimeZone:
    """
    Calls Qt's 'QTimeZone QTimeZone::fromSecondsAheadOfUtc(int offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtimezone.html#fromSecondsAheadOfUtc

    Parameters
    ----------

    offset : int
      Passed on as it is.

    Returns
    -------

    QTimeZone
      A new cute QTimeZone around the copy Qt gave back. Python owns it.
    """
    #  QTimeZone QTimeZone::fromSecondsAheadOfUtc(int offset)
    address = Rituals.call(
        'ritual_ZN9QTimeZone21fromSecondsAheadOfUtcEi', offset,
    )
    return QTimeZone._cuteOwning(address)

  @staticmethod
  @overload(Qt.TimeSpec)
  def isUtcOrFixedOffset(spec: Qt.TimeSpec) -> bool:
    """
    Calls Qt's 'bool QTimeZone::isUtcOrFixedOffset(Qt::TimeSpec spec)'.

    Qt's own words: https://doc.qt.io/qt-6/qtimezone.html#isUtcOrFixedOffset

    Parameters
    ----------

    spec : Qt.TimeSpec
      Passed on as its number.
    """
    #  bool QTimeZone::isUtcOrFixedOffset(Qt::TimeSpec spec)
    return Rituals.call(
        'ritual_ZN9QTimeZone18isUtcOrFixedOffsetEN2Qt8TimeSpecE', spec.value,
    )

  @overload()
  def isUtcOrFixedOffset(self) -> bool:
    """
    Calls Qt's 'bool QTimeZone::isUtcOrFixedOffset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtimezone.html#isUtcOrFixedOffset
    """
    #  bool QTimeZone::isUtcOrFixedOffset() const
    return self.uglySide.call('ritual_ZNK9QTimeZone18isUtcOrFixedOffsetEv')

  @staticmethod
  def systemTimeZoneId() -> QByteArray:
    """
    Calls Qt's 'QByteArray QTimeZone::systemTimeZoneId()'.

    Qt's own words: https://doc.qt.io/qt-6/qtimezone.html#systemTimeZoneId

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QTimeZone::systemTimeZoneId()
    address = Rituals.call('ritual_ZN9QTimeZone16systemTimeZoneIdEv')
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  @staticmethod
  def systemTimeZone() -> QTimeZone:
    """
    Calls Qt's 'QTimeZone QTimeZone::systemTimeZone()'.

    Qt's own words: https://doc.qt.io/qt-6/qtimezone.html#systemTimeZone

    Returns
    -------

    QTimeZone
      A new cute QTimeZone around the copy Qt gave back. Python owns it.
    """
    #  QTimeZone QTimeZone::systemTimeZone()
    address = Rituals.call('ritual_ZN9QTimeZone14systemTimeZoneEv')
    return QTimeZone._cuteOwning(address)

  @staticmethod
  def utc() -> QTimeZone:
    """
    Calls Qt's 'QTimeZone QTimeZone::utc()'.

    Qt's own words: https://doc.qt.io/qt-6/qtimezone.html#utc

    Returns
    -------

    QTimeZone
      A new cute QTimeZone around the copy Qt gave back. Python owns it.
    """
    #  QTimeZone QTimeZone::utc()
    address = Rituals.call('ritual_ZN9QTimeZone3utcEv')
    return QTimeZone._cuteOwning(address)

  @staticmethod
  @overload(QByteArrayView)
  def isTimeZoneIdAvailable(ianaId: QByteArrayView) -> bool:
    """
    Calls Qt's 'bool QTimeZone::isTimeZoneIdAvailable(QByteArrayView
    ianaId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtimezone.html#isTimeZoneIdAvailable

    Parameters
    ----------

    ianaId : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.
    """
    #  bool QTimeZone::isTimeZoneIdAvailable(QByteArrayView ianaId)
    return Rituals.call(
        'ritual_ZN9QTimeZone21isTimeZoneIdAvailableE14QByteArrayView',
        CuteMixin._valueOf(ianaId),
    )

  @staticmethod
  @overload(QByteArray)
  def ianaIdToWindowsId(ianaId: QByteArray) -> QByteArray:
    """
    Calls Qt's 'QByteArray QTimeZone::ianaIdToWindowsId(const QByteArray
    &ianaId)'.

    Qt's own words: https://doc.qt.io/qt-6/qtimezone.html#ianaIdToWindowsId

    Parameters
    ----------

    ianaId : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QTimeZone::ianaIdToWindowsId(const QByteArray &ianaId)
    address = Rituals.call(
        'ritual_ZN9QTimeZone17ianaIdToWindowsIdERK10QByteArray',
        CuteMixin._valueOf(ianaId),
    )
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  @staticmethod
  @overload(QByteArray)
  def windowsIdToDefaultIanaId(windowsId: QByteArray) -> QByteArray:
    """
    Calls Qt's 'QByteArray QTimeZone::windowsIdToDefaultIanaId(const
    QByteArray &windowsId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtimezone.html#windowsIdToDefaultIanaId

    Parameters
    ----------

    windowsId : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QTimeZone::windowsIdToDefaultIanaId(const QByteArray
    #      &windowsId)
    address = Rituals.call(
        'ritual_ZN9QTimeZone24windowsIdToDefaultIanaIdERK10QByteArray',
        CuteMixin._valueOf(windowsId),
    )
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTimeZone'

  #  Qt's '~QTimeZone()'. Naming it makes this a value class: Python owns
  #  every C++ QTimeZone behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN9QTimeZoneD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QTimeZone::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtimezone.html#isValid
    """
    #  bool QTimeZone::isValid() const
    return self.uglySide.call('ritual_ZNK9QTimeZone7isValidEv')

  def timeSpec(self) -> Qt.TimeSpec:
    """
    Calls Qt's 'Qt::TimeSpec QTimeZone::timeSpec() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtimezone.html#timeSpec

    Returns
    -------

    Qt.TimeSpec
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.TimeSpec(number)'
      gives.
    """
    #  Qt::TimeSpec QTimeZone::timeSpec() const
    return Qt.TimeSpec(self.uglySide.call('ritual_ZNK9QTimeZone8timeSpecEv'))

  def fixedSecondsAheadOfUtc(self) -> int:
    """
    Calls Qt's 'int QTimeZone::fixedSecondsAheadOfUtc() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtimezone.html#fixedSecondsAheadOfUtc
    """
    #  int QTimeZone::fixedSecondsAheadOfUtc() const
    return self.uglySide.call(
        'ritual_ZNK9QTimeZone22fixedSecondsAheadOfUtcEv',
    )

  def asBackendZone(self) -> QTimeZone:
    """
    Calls Qt's 'QTimeZone QTimeZone::asBackendZone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtimezone.html#asBackendZone

    Returns
    -------

    QTimeZone
      A new cute QTimeZone around the copy Qt gave back. Python owns it.
    """
    #  QTimeZone QTimeZone::asBackendZone() const
    address = self.uglySide.call('ritual_ZNK9QTimeZone13asBackendZoneEv')
    return QTimeZone._cuteOwning(address)

  @overload(QByteArrayView)
  def hasAlternativeName(self, alias: QByteArrayView) -> bool:
    """
    Calls Qt's 'bool QTimeZone::hasAlternativeName(QByteArrayView alias)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtimezone.html#hasAlternativeName

    Parameters
    ----------

    alias : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.
    """
    #  bool QTimeZone::hasAlternativeName(QByteArrayView alias) const
    return self.uglySide.call(
        'ritual_ZNK9QTimeZone18hasAlternativeNameE14QByteArrayView',
        self._valueOf(alias),
    )

  def id(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QTimeZone::id() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtimezone.html#id

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QTimeZone::id() const
    address = self.uglySide.call('ritual_ZNK9QTimeZone2idEv')
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  def country(self) -> QLocale.Country:
    """
    Calls Qt's 'QLocale::Country QTimeZone::country() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtimezone.html#country

    Returns
    -------

    QLocale.Country
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QLocale.Country(number)'
      gives.
    """
    #  QLocale::Country QTimeZone::country() const
    return QLocale.Country(self.uglySide.call(
        'ritual_ZNK9QTimeZone7countryEv',
    ))

  def comment(self) -> str:
    """
    Calls Qt's 'QString QTimeZone::comment() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtimezone.html#comment

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTimeZone::comment() const
    return self.uglySide.call('ritual_ZNK9QTimeZone7commentEv')

  @overload(QDateTime)
  @overload(QDateTime, NameType)
  @overload(QDateTime, NameType, QLocale)
  def displayName(
      self,
      atDateTime: QDateTime,
      nameType: NameType = NameType.DefaultName,
      locale: Optional[QLocale] = None,
  ) -> str:
    """
    Calls Qt's 'QString QTimeZone::displayName(const QDateTime &atDateTime,
    NameType nameType, const QLocale &locale) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtimezone.html#displayName

    Parameters
    ----------

    atDateTime : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.

    nameType : NameType
      Passed on as its number. May be left out, as in Qt: it is then
      NameType.DefaultName.

    locale : Optional[QLocale]
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own. May be left out, as in Qt: a new 'QLocale()' is then passed on.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTimeZone::displayName(const QDateTime &atDateTime, NameType
    #      nameType, const QLocale &locale) const
    if locale is None:
      locale = QLocale()
    return self.uglySide.call(
        'ritual_ZNK9QTimeZone11displayNameERK9QDateTimeNS_8NameTypeERK7QLoc'
        'ale',
        self._valueOf(atDateTime), nameType.value, self._valueOf(locale),
    )

  @overload(TimeType)
  @overload(TimeType, NameType)
  @overload(TimeType, NameType, QLocale)
  def displayName(
      self,
      timeType: TimeType,
      nameType: NameType = NameType.DefaultName,
      locale: Optional[QLocale] = None,
  ) -> str:
    """
    Calls Qt's 'QString QTimeZone::displayName(TimeType timeType, NameType
    nameType, const QLocale &locale) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtimezone.html#displayName

    Parameters
    ----------

    timeType : TimeType
      Passed on as its number.

    nameType : NameType
      Passed on as its number. May be left out, as in Qt: it is then
      NameType.DefaultName.

    locale : Optional[QLocale]
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own. May be left out, as in Qt: a new 'QLocale()' is then passed on.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTimeZone::displayName(TimeType timeType, NameType nameType,
    #      const QLocale &locale) const
    if locale is None:
      locale = QLocale()
    return self.uglySide.call(
        'ritual_ZNK9QTimeZone11displayNameENS_8TimeTypeENS_8NameTypeERK7QLo'
        'cale',
        timeType.value, nameType.value, self._valueOf(locale),
    )

  @overload(QDateTime)
  def abbreviation(self, atDateTime: QDateTime) -> str:
    """
    Calls Qt's 'QString QTimeZone::abbreviation(const QDateTime &atDateTime)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtimezone.html#abbreviation

    Parameters
    ----------

    atDateTime : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTimeZone::abbreviation(const QDateTime &atDateTime) const
    return self.uglySide.call(
        'ritual_ZNK9QTimeZone12abbreviationERK9QDateTime',
        self._valueOf(atDateTime),
    )

  @overload(QDateTime)
  def offsetFromUtc(self, atDateTime: QDateTime) -> int:
    """
    Calls Qt's 'int QTimeZone::offsetFromUtc(const QDateTime &atDateTime)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtimezone.html#offsetFromUtc

    Parameters
    ----------

    atDateTime : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.
    """
    #  int QTimeZone::offsetFromUtc(const QDateTime &atDateTime) const
    return self.uglySide.call(
        'ritual_ZNK9QTimeZone13offsetFromUtcERK9QDateTime',
        self._valueOf(atDateTime),
    )

  @overload(QDateTime)
  def standardTimeOffset(self, atDateTime: QDateTime) -> int:
    """
    Calls Qt's 'int QTimeZone::standardTimeOffset(const QDateTime
    &atDateTime) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtimezone.html#standardTimeOffset

    Parameters
    ----------

    atDateTime : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.
    """
    #  int QTimeZone::standardTimeOffset(const QDateTime &atDateTime) const
    return self.uglySide.call(
        'ritual_ZNK9QTimeZone18standardTimeOffsetERK9QDateTime',
        self._valueOf(atDateTime),
    )

  @overload(QDateTime)
  def daylightTimeOffset(self, atDateTime: QDateTime) -> int:
    """
    Calls Qt's 'int QTimeZone::daylightTimeOffset(const QDateTime
    &atDateTime) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtimezone.html#daylightTimeOffset

    Parameters
    ----------

    atDateTime : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.
    """
    #  int QTimeZone::daylightTimeOffset(const QDateTime &atDateTime) const
    return self.uglySide.call(
        'ritual_ZNK9QTimeZone18daylightTimeOffsetERK9QDateTime',
        self._valueOf(atDateTime),
    )

  def hasDaylightTime(self) -> bool:
    """
    Calls Qt's 'bool QTimeZone::hasDaylightTime() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtimezone.html#hasDaylightTime
    """
    #  bool QTimeZone::hasDaylightTime() const
    return self.uglySide.call('ritual_ZNK9QTimeZone15hasDaylightTimeEv')

  @overload(QDateTime)
  def isDaylightTime(self, atDateTime: QDateTime) -> bool:
    """
    Calls Qt's 'bool QTimeZone::isDaylightTime(const QDateTime &atDateTime)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtimezone.html#isDaylightTime

    Parameters
    ----------

    atDateTime : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.
    """
    #  bool QTimeZone::isDaylightTime(const QDateTime &atDateTime) const
    return self.uglySide.call(
        'ritual_ZNK9QTimeZone14isDaylightTimeERK9QDateTime',
        self._valueOf(atDateTime),
    )

  @overload(QDateTime)
  def offsetData(self, forDateTime: QDateTime) -> OffsetData:
    """
    Calls Qt's 'OffsetData QTimeZone::offsetData(const QDateTime
    &forDateTime) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtimezone.html#offsetData

    Parameters
    ----------

    forDateTime : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.

    Returns
    -------

    OffsetData
      A new cute QTimeZone::OffsetData around the copy Qt gave back. Python
      owns it.
    """
    #  OffsetData QTimeZone::offsetData(const QDateTime &forDateTime) const
    address = self.uglySide.call(
        'ritual_ZNK9QTimeZone10offsetDataERK9QDateTime',
        self._valueOf(forDateTime),
    )
    return QTimeZone.OffsetData._cuteOwning(address)

  def hasTransitions(self) -> bool:
    """
    Calls Qt's 'bool QTimeZone::hasTransitions() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtimezone.html#hasTransitions
    """
    #  bool QTimeZone::hasTransitions() const
    return self.uglySide.call('ritual_ZNK9QTimeZone14hasTransitionsEv')

  @overload(QDateTime)
  def nextTransition(self, afterDateTime: QDateTime) -> OffsetData:
    """
    Calls Qt's 'OffsetData QTimeZone::nextTransition(const QDateTime
    &afterDateTime) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtimezone.html#nextTransition

    Parameters
    ----------

    afterDateTime : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.

    Returns
    -------

    OffsetData
      A new cute QTimeZone::OffsetData around the copy Qt gave back. Python
      owns it.
    """
    #  OffsetData QTimeZone::nextTransition(const QDateTime &afterDateTime)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK9QTimeZone14nextTransitionERK9QDateTime',
        self._valueOf(afterDateTime),
    )
    return QTimeZone.OffsetData._cuteOwning(address)

  @overload(QDateTime)
  def previousTransition(self, beforeDateTime: QDateTime) -> OffsetData:
    """
    Calls Qt's 'OffsetData QTimeZone::previousTransition(const QDateTime
    &beforeDateTime) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtimezone.html#previousTransition

    Parameters
    ----------

    beforeDateTime : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.

    Returns
    -------

    OffsetData
      A new cute QTimeZone::OffsetData around the copy Qt gave back. Python
      owns it.
    """
    #  OffsetData QTimeZone::previousTransition(const QDateTime
    #      &beforeDateTime) const
    address = self.uglySide.call(
        'ritual_ZNK9QTimeZone18previousTransitionERK9QDateTime',
        self._valueOf(beforeDateTime),
    )
    return QTimeZone.OffsetData._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QTimeZone) -> bool:
    """
    Calls Qt's 'bool operator==(const QTimeZone &lhs, const QTimeZone &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qtimezone.html#operator==

    Parameters
    ----------

    rhs : QTimeZone
      Passed on as a value: Qt reads the C++ QTimeZone, which stays Python's
      own.
    """
    #  bool operator==(const QTimeZone &lhs, const QTimeZone &rhs)
    return Rituals.call(
        'ritual_ZeqRK9QTimeZoneS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, rhs: QTimeZone) -> bool:
    """
    Calls Qt's 'bool operator!=(const QTimeZone &lhs, const QTimeZone &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qtimezone.html#operator!=

    Parameters
    ----------

    rhs : QTimeZone
      Passed on as a value: Qt reads the C++ QTimeZone, which stays Python's
      own.
    """
    #  bool operator!=(const QTimeZone &lhs, const QTimeZone &rhs)
    return Rituals.call(
        'ritual_ZneRK9QTimeZoneS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(QDebug)
  def __rlshift__(self, dbg: QDebug) -> QDebug:
    """
    Calls Qt's 'QDebug operator<<(QDebug dbg, const QTimeZone &tz)'.

    Qt's own words: https://doc.qt.io/qt-6/qtimezone.html#operator<<

    Parameters
    ----------

    dbg : QDebug
      Passed on as a value: Qt reads the C++ QDebug, which stays Python's
      own.

    Returns
    -------

    QDebug
      A new cute QDebug around the copy Qt gave back. Python owns it.
    """
    #  QDebug operator<<(QDebug dbg, const QTimeZone &tz)
    address = Rituals.call(
        'ritual_Zls6QDebugRK9QTimeZone',
        CuteMixin._valueOf(dbg), CuteMixin._valueOf(self),
    )
    from . import QDebug
    return QDebug._cuteOwning(address)

  @overload.fallback
  def __rlshift__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QTimeZone::QTimeZone()', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtimezone.html#QTimeZone
    """
    #  QTimeZone::QTimeZone()
    self._noteCreation(QTimeZone, lambda: Rituals.call(
        'ritual_ZN9QTimeZoneC1Ev',
    ))

  @overload(Initialization)
  def __init__(self, spec: Initialization) -> None:
    """
    Notes what was given, for Qt's 'QTimeZone::QTimeZone(Initialization
    spec)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtimezone.html#QTimeZone

    Parameters
    ----------

    spec : Initialization
      Passed on as its number.
    """
    #  QTimeZone::QTimeZone(Initialization spec)
    self._noteCreation(QTimeZone, lambda: Rituals.call(
        'ritual_ZN9QTimeZoneC1ENS_14InitializationE', spec.value,
    ))

  @overload(int)
  def __init__(self, offsetSeconds: int) -> None:
    """
    Notes what was given, for Qt's 'QTimeZone::QTimeZone(int offsetSeconds)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtimezone.html#QTimeZone

    Parameters
    ----------

    offsetSeconds : int
      Passed on as it is.
    """
    #  QTimeZone::QTimeZone(int offsetSeconds)
    self._noteCreation(QTimeZone, lambda: Rituals.call(
        'ritual_ZN9QTimeZoneC1Ei', offsetSeconds,
    ))

  @overload(QByteArray)
  def __init__(self, ianaId: QByteArray) -> None:
    """
    Notes what was given, for Qt's 'QTimeZone::QTimeZone(const QByteArray
    &ianaId)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtimezone.html#QTimeZone

    Parameters
    ----------

    ianaId : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  QTimeZone::QTimeZone(const QByteArray &ianaId)
    self._noteCreation(QTimeZone, lambda: Rituals.call(
        'ritual_ZN9QTimeZoneC1ERK10QByteArray', self._valueOf(ianaId),
    ))

  @overload(THIS)
  def __init__(self, other: QTimeZone) -> None:
    """
    Notes what was given, for Qt's 'QTimeZone::QTimeZone(const QTimeZone
    &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtimezone.html#QTimeZone

    Parameters
    ----------

    other : QTimeZone
      Passed on as a value: Qt reads the C++ QTimeZone, which stays Python's
      own.
    """
    #  QTimeZone::QTimeZone(const QTimeZone &other)
    self._noteCreation(QTimeZone, lambda: Rituals.call(
        'ritual_ZN9QTimeZoneC1ERKS_', self._valueOf(other),
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
