"""
QDateTimePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qdatetime_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QDateTimePrivate to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute
from ..occult import Rituals
from . import QSharedData

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QDateTimePrivate(QSharedData):
  """
  The cute side of Qt's QDateTimePrivate: a plain Python object standing in
  front of one C++ QDateTimePrivate.

  It is built on the cute 'QSharedData', as Qt's QDateTimePrivate is built on
  Qt's QSharedData, and has everything that class has.

  C++ hands a QDateTimePrivate around as a copy, so every C++
  QDateTimePrivate behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QDateTimePrivate yet. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDateTimePrivate::~QDateTimePrivate()': the destructor: Python
    removes its C++ QDateTimePrivate by it, and has no other use for it.

  What has no ritual
  ------------------

  5 of the 6 functions Qt declares: 5 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QDateTimePrivate is created at the first use, not by
    'QDateTimePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDateTimePrivate back gives a copy the ritual made
    for Python, in a new cute QDateTimePrivate.
  - Each name of Qt's QDateTimePrivate that has no cute function yet,
    'create', 'expressUtcAsLocal', 'localNameAtMillis', 'localStateAtMillis',
    'zoneStateAtMillis', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  #  The enums Qt writes inside QDateTimePrivate, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class DaylightStatus(CuteNum):
    """
    The enum 'QDateTimePrivate::DaylightStatus' of Qt, with the 3 names Qt
    gives in it.
    """

    UnknownDaylightTime = Kee[int](-1)
    StandardTime = Kee[int](0)
    DaylightTime = Kee[int](1)

  class Spec(CuteNum):
    """
    The enum 'QDateTimePrivate::Spec' of Qt, with the 6 names Qt gives in it.
    """

    LocalUnknown = Kee[int](-1)
    LocalStandard = Kee[int](0)
    LocalDST = Kee[int](1)
    UTC = Kee[int](2)
    OffsetFromUTC = Kee[int](3)
    TimeZone = Kee[int](4)

  class StatusFlag(CuteFlags):
    """
    The flags enum 'QDateTimePrivate::StatusFlag' of Qt, with the 9 names Qt
    gives in it. Qt names the type of its combinations
    'QDateTimePrivate::StatusFlags'.
    """

    ShortData = 0x1
    ValidDate = 0x2
    ValidTime = 0x4
    ValidDateTime = 0x8
    TimeSpecMask = 0x30
    SetToStandardTime = 0x40
    SetToDaylightTime = 0x80
    ValidityMask = 0xe
    DaylightMask = 0xc0

  StatusFlags = StatusFlag

  class TransitionOption(CuteFlags):
    """
    The flags enum 'QDateTimePrivate::TransitionOption' of Qt, with the 7
    names Qt gives in it. Qt names the type of its combinations
    'QDateTimePrivate::TransitionOptions'.
    """

    GapUseBefore = 0x2
    GapUseAfter = 0x4
    FoldUseBefore = 0x20
    FoldUseAfter = 0x40
    FlipForReverseDst = 0x400
    GapMask = 0x6
    FoldMask = 0x60

  TransitionOptions = TransitionOption

  #  The classes Qt writes inside QDateTimePrivate, each a class in here as
  #  in C++.

  class ZoneState(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QDateTimePrivate::ZoneState: a plain Python object
    standing in front of one C++ QDateTimePrivate::ZoneState.

    C++ hands a QDateTimePrivate::ZoneState around as a copy, so every C++
    QDateTimePrivate::ZoneState behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QDateTimePrivate::ZoneState yet. It can be made from
    Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QDateTimePrivate::ZoneState::ZoneState(qint64 w, int o,
      DaylightStatus d, bool v)': names the enum
      'QDateTimePrivate::DaylightStatus', whose class cannot be named here.
    - Qt's 'QDateTimePrivate::ZoneState::~ZoneState()': the destructor:
      Python removes its C++ QDateTimePrivate::ZoneState by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QDateTimePrivate::ZoneState is created at the first use, not by
      'QDateTimePrivate::ZoneState(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QDateTimePrivate::ZoneState back gives a copy the
      ritual made for Python, in a new cute QDateTimePrivate::ZoneState.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QDateTimePrivate::ZoneState'

    #  Qt's '~QDateTimePrivate::ZoneState()'. Naming it makes this a value
    #  class: Python owns every C++ QDateTimePrivate::ZoneState behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN16QDateTimePrivate9ZoneStateD1Ev'

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

    @overload(int)
    def __init__(self, local: int) -> None:
      """
      Notes what was given, for Qt's
      'QDateTimePrivate::ZoneState::ZoneState(qint64 local)', which is called
      at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qdatetimeprivate-zonestate.html#ZoneState

      Parameters
      ----------

      local : int
        Passed on as it is.
      """
      #  QDateTimePrivate::ZoneState::ZoneState(qint64 local)
      self._noteCreation(QDateTimePrivate.ZoneState, lambda: Rituals.call(
          'ritual_ZN16QDateTimePrivate9ZoneStateC1Ex', local,
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
  __qt_class__ = 'QDateTimePrivate'

  #  Qt's '~QDateTimePrivate()'. Naming it makes this a value class: Python
  #  owns every C++ QDateTimePrivate behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QDateTimePrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
  def create(*__, **_) -> Never:
    """
    Qt's 'QDateTime::Data QDateTimePrivate::create(QDate toDate, QTime
    toTime, const QTimeZone &timeZone, QDateTime::TransitionResolution
    resolve)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: no matching function for call to
    'setDateTime'.
    """
    raise NotImplementedError(
        "'QDateTimePrivate.create' has no cute function yet. Qt's "
        "'QDateTime::Data QDateTimePrivate::create(QDate toDate, QTime "
        "toTime, const QTimeZone &timeZone, QDateTime::TransitionResolution "
        "resolve)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: no matching function "
        "for call to 'setDateTime'.")

  @staticmethod
  def expressUtcAsLocal(*__, **_) -> Never:
    """
    Qt's 'ZoneState QDateTimePrivate::expressUtcAsLocal(qint64 utcMSecs)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier
    'MSECS_PER_SEC'; did you mean
    'QtPrivate::DateTimeConstants::MSECS_PER_SEC'?.
    """
    raise NotImplementedError(
        "'QDateTimePrivate.expressUtcAsLocal' has no cute function yet. "
        "Qt's 'ZoneState QDateTimePrivate::expressUtcAsLocal(qint64 "
        "utcMSecs)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'MSECS_PER_SEC'; did you mean "
        "'QtPrivate::DateTimeConstants::MSECS_PER_SEC'?.")

  @staticmethod
  def localNameAtMillis(*__, **_) -> Never:
    """
    Qt's 'QString QDateTimePrivate::localNameAtMillis(qint64 millis,
    DaylightStatus dst)': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: use of undeclared
    identifier 'toTransitionOptions'; did you mean 'TransitionOptions'?.
    """
    raise NotImplementedError(
        "'QDateTimePrivate.localNameAtMillis' has no cute function yet. "
        "Qt's 'QString QDateTimePrivate::localNameAtMillis(qint64 millis, "
        "DaylightStatus dst)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'toTransitionOptions'; did you mean "
        "'TransitionOptions'?.")

  @staticmethod
  def localStateAtMillis(*__, **_) -> Never:
    """
    Qt's 'ZoneState QDateTimePrivate::localStateAtMillis(qint64 millis,
    TransitionOptions resolve)': Qt's library has no name for it, and its
    code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'MSECS_PER_DAY'; did you mean
    'QtPrivate::DateTimeConstants::MSECS_PER_DAY'?.
    """
    raise NotImplementedError(
        "'QDateTimePrivate.localStateAtMillis' has no cute function yet. "
        "Qt's 'ZoneState QDateTimePrivate::localStateAtMillis(qint64 "
        "millis, TransitionOptions resolve)': Qt's library has no name for "
        "it, and its code in Qt's source does not compile apart from its "
        "file: use of undeclared identifier 'MSECS_PER_DAY'; did you mean "
        "'QtPrivate::DateTimeConstants::MSECS_PER_DAY'?.")

  @staticmethod
  def zoneStateAtMillis(*__, **_) -> Never:
    """
    Qt's 'ZoneState QDateTimePrivate::zoneStateAtMillis(const QTimeZone
    &zone, qint64 millis, TransitionOptions resolve)': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: member access into incomplete type 'const QTimeZonePrivate'.
    """
    raise NotImplementedError(
        "'QDateTimePrivate.zoneStateAtMillis' has no cute function yet. "
        "Qt's 'ZoneState QDateTimePrivate::zoneStateAtMillis(const "
        "QTimeZone &zone, qint64 millis, TransitionOptions resolve)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: member access into incomplete type "
        "'const QTimeZonePrivate'.")
