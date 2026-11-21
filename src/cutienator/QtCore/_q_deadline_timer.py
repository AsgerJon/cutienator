"""
QDeadlineTimer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qdeadlinetimer.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from . import Qt, QDeadlineTimerForeverConstant


class QDeadlineTimer(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDeadlineTimer: a plain Python object standing in
  front of one C++ QDeadlineTimer.

  C++ hands a QDeadlineTimer around as a copy, so every C++ QDeadlineTimer
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDeadlineTimer that has a ritual and that Python can
  call so far, 14 names in all: 'isForever', 'hasExpired', 'timerType',
  'setTimerType', 'remainingTime', 'remainingTimeNSecs', 'setRemainingTime',
  'setPreciseRemainingTime', 'deadline', 'deadlineNSecs', 'setDeadline',
  'setPreciseDeadline', 'addNSecs', 'current'. It can be made from Python, in
  4 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDeadlineTimer::~QDeadlineTimer()': the destructor: Python removes
    its C++ QDeadlineTimer by it, and has no other use for it.

  What has no ritual
  ------------------

  12 of the 31 functions Qt declares: 7 a template; 4 takes or gives a type
  that cannot be passed yet; 1 private.

  What to expect
  --------------

  - The C++ QDeadlineTimer is created at the first use, not by
    'QDeadlineTimer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDeadlineTimer back gives a copy the ritual made for
    Python, in a new cute QDeadlineTimer.
  """

  #  The enums Qt writes inside QDeadlineTimer, and the names Qt has for the
  #  combinations of its flags enums.
  ForeverConstant = QDeadlineTimerForeverConstant

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(THIS, int)
  def addNSecs(dt: QDeadlineTimer, nsecs: int) -> QDeadlineTimer:
    """
    Calls Qt's 'QDeadlineTimer QDeadlineTimer::addNSecs(QDeadlineTimer dt,
    qint64 nsecs)'.

    Qt's own words: https://doc.qt.io/qt-6/qdeadlinetimer.html#addNSecs

    Parameters
    ----------

    dt : QDeadlineTimer
      Passed on as a value: Qt reads the C++ QDeadlineTimer, which stays
      Python's own.

    nsecs : int
      Passed on as it is.

    Returns
    -------

    QDeadlineTimer
      A new cute QDeadlineTimer around the copy Qt gave back. Python owns it.
    """
    #  QDeadlineTimer QDeadlineTimer::addNSecs(QDeadlineTimer dt, qint64
    #      nsecs)
    address = Rituals.call(
        'ritual_ZN14QDeadlineTimer8addNSecsES_x',
        CuteMixin._valueOf(dt), nsecs,
    )
    return QDeadlineTimer._cuteOwning(address)

  @staticmethod
  @overload()
  @overload(Qt.TimerType)
  def current(
      timerType: Qt.TimerType = Qt.TimerType.CoarseTimer,
  ) -> QDeadlineTimer:
    """
    Calls Qt's 'QDeadlineTimer QDeadlineTimer::current(Qt::TimerType
    timerType)'.

    Qt's own words: https://doc.qt.io/qt-6/qdeadlinetimer.html#current

    Parameters
    ----------

    timerType : Qt.TimerType
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.TimerType.CoarseTimer.

    Returns
    -------

    QDeadlineTimer
      A new cute QDeadlineTimer around the copy Qt gave back. Python owns it.
    """
    #  QDeadlineTimer QDeadlineTimer::current(Qt::TimerType timerType)
    address = Rituals.call(
        'ritual_ZN14QDeadlineTimer7currentEN2Qt9TimerTypeE', timerType.value,
    )
    return QDeadlineTimer._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDeadlineTimer'

  #  Qt's '~QDeadlineTimer()'. Naming it makes this a value class: Python
  #  owns every C++ QDeadlineTimer behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN14QDeadlineTimerD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isForever(self) -> bool:
    """
    Calls Qt's 'bool QDeadlineTimer::isForever() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdeadlinetimer.html#isForever
    """
    #  bool QDeadlineTimer::isForever() const
    return self.uglySide.call('ritual_ZNK14QDeadlineTimer9isForeverEv')

  def hasExpired(self) -> bool:
    """
    Calls Qt's 'bool QDeadlineTimer::hasExpired() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdeadlinetimer.html#hasExpired
    """
    #  bool QDeadlineTimer::hasExpired() const
    return self.uglySide.call('ritual_ZNK14QDeadlineTimer10hasExpiredEv')

  def timerType(self) -> Qt.TimerType:
    """
    Calls Qt's 'Qt::TimerType QDeadlineTimer::timerType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdeadlinetimer.html#timerType

    Returns
    -------

    Qt.TimerType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.TimerType(number)'
      gives.
    """
    #  Qt::TimerType QDeadlineTimer::timerType() const
    return Qt.TimerType(self.uglySide.call(
        'ritual_ZNK14QDeadlineTimer9timerTypeEv',
    ))

  def remainingTime(self) -> int:
    """
    Calls Qt's 'qint64 QDeadlineTimer::remainingTime() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdeadlinetimer.html#remainingTime
    """
    #  qint64 QDeadlineTimer::remainingTime() const
    return self.uglySide.call('ritual_ZNK14QDeadlineTimer13remainingTimeEv')

  def remainingTimeNSecs(self) -> int:
    """
    Calls Qt's 'qint64 QDeadlineTimer::remainingTimeNSecs() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeadlinetimer.html#remainingTimeNSecs
    """
    #  qint64 QDeadlineTimer::remainingTimeNSecs() const
    return self.uglySide.call(
        'ritual_ZNK14QDeadlineTimer18remainingTimeNSecsEv',
    )

  def deadline(self) -> int:
    """
    Calls Qt's 'qint64 QDeadlineTimer::deadline() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdeadlinetimer.html#deadline
    """
    #  qint64 QDeadlineTimer::deadline() const
    return self.uglySide.call('ritual_ZNK14QDeadlineTimer8deadlineEv')

  def deadlineNSecs(self) -> int:
    """
    Calls Qt's 'qint64 QDeadlineTimer::deadlineNSecs() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdeadlinetimer.html#deadlineNSecs
    """
    #  qint64 QDeadlineTimer::deadlineNSecs() const
    return self.uglySide.call('ritual_ZNK14QDeadlineTimer13deadlineNSecsEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Qt.TimerType)
  def setTimerType(self, type: Qt.TimerType) -> None:
    """
    Calls Qt's 'void QDeadlineTimer::setTimerType(Qt::TimerType type)'.

    Qt's own words: https://doc.qt.io/qt-6/qdeadlinetimer.html#setTimerType

    Parameters
    ----------

    type : Qt.TimerType
      Passed on as its number.
    """
    #  void QDeadlineTimer::setTimerType(Qt::TimerType type)
    self.uglySide.call(
        'ritual_ZN14QDeadlineTimer12setTimerTypeEN2Qt9TimerTypeE',
        type.value,
    )

  @overload(int)
  @overload(int, Qt.TimerType)
  def setRemainingTime(
      self,
      msecs: int,
      type: Qt.TimerType = Qt.TimerType.CoarseTimer,
  ) -> None:
    """
    Calls Qt's 'void QDeadlineTimer::setRemainingTime(qint64 msecs,
    Qt::TimerType type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeadlinetimer.html#setRemainingTime

    Parameters
    ----------

    msecs : int
      Passed on as it is.

    type : Qt.TimerType
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.TimerType.CoarseTimer.
    """
    #  void QDeadlineTimer::setRemainingTime(qint64 msecs, Qt::TimerType
    #      type)
    self.uglySide.call(
        'ritual_ZN14QDeadlineTimer16setRemainingTimeExN2Qt9TimerTypeE',
        msecs, type.value,
    )

  @overload(int)
  @overload(int, int)
  @overload(int, int, Qt.TimerType)
  def setPreciseRemainingTime(
      self,
      secs: int,
      nsecs: int = 0,
      type: Qt.TimerType = Qt.TimerType.CoarseTimer,
  ) -> None:
    """
    Calls Qt's 'void QDeadlineTimer::setPreciseRemainingTime(qint64 secs,
    qint64 nsecs, Qt::TimerType type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeadlinetimer.html#setPreciseRemainingTime

    Parameters
    ----------

    secs : int
      Passed on as it is.

    nsecs : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    type : Qt.TimerType
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.TimerType.CoarseTimer.
    """
    #  void QDeadlineTimer::setPreciseRemainingTime(qint64 secs, qint64
    #      nsecs, Qt::TimerType type)
    self.uglySide.call(
        'ritual_ZN14QDeadlineTimer23setPreciseRemainingTimeExxN2Qt9TimerTyp'
        'eE',
        secs, nsecs, type.value,
    )

  @overload(int)
  @overload(int, Qt.TimerType)
  def setDeadline(
      self,
      msecs: int,
      timerType: Qt.TimerType = Qt.TimerType.CoarseTimer,
  ) -> None:
    """
    Calls Qt's 'void QDeadlineTimer::setDeadline(qint64 msecs, Qt::TimerType
    timerType)'.

    Qt's own words: https://doc.qt.io/qt-6/qdeadlinetimer.html#setDeadline

    Parameters
    ----------

    msecs : int
      Passed on as it is.

    timerType : Qt.TimerType
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.TimerType.CoarseTimer.
    """
    #  void QDeadlineTimer::setDeadline(qint64 msecs, Qt::TimerType
    #      timerType)
    self.uglySide.call(
        'ritual_ZN14QDeadlineTimer11setDeadlineExN2Qt9TimerTypeE',
        msecs, timerType.value,
    )

  @overload(int)
  @overload(int, int)
  @overload(int, int, Qt.TimerType)
  def setPreciseDeadline(
      self,
      secs: int,
      nsecs: int = 0,
      type: Qt.TimerType = Qt.TimerType.CoarseTimer,
  ) -> None:
    """
    Calls Qt's 'void QDeadlineTimer::setPreciseDeadline(qint64 secs, qint64
    nsecs, Qt::TimerType type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeadlinetimer.html#setPreciseDeadline

    Parameters
    ----------

    secs : int
      Passed on as it is.

    nsecs : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    type : Qt.TimerType
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.TimerType.CoarseTimer.
    """
    #  void QDeadlineTimer::setPreciseDeadline(qint64 secs, qint64 nsecs,
    #      Qt::TimerType type)
    self.uglySide.call(
        'ritual_ZN14QDeadlineTimer18setPreciseDeadlineExxN2Qt9TimerTypeE',
        secs, nsecs, type.value,
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QDeadlineTimer::QDeadlineTimer()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdeadlinetimer.html#QDeadlineTimer
    """
    #  QDeadlineTimer::QDeadlineTimer()
    self._noteCreation(QDeadlineTimer, lambda: Rituals.call(
        'ritual_ZN14QDeadlineTimerC1Ev',
    ))

  @overload(Qt.TimerType)
  def __init__(self, type_: Qt.TimerType) -> None:
    """
    Notes what was given, for Qt's
    'QDeadlineTimer::QDeadlineTimer(Qt::TimerType type_)', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdeadlinetimer.html#QDeadlineTimer

    Parameters
    ----------

    type_ : Qt.TimerType
      Passed on as its number.
    """
    #  QDeadlineTimer::QDeadlineTimer(Qt::TimerType type_)
    self._noteCreation(QDeadlineTimer, lambda: Rituals.call(
        'ritual_ZN14QDeadlineTimerC1EN2Qt9TimerTypeE', type_.value,
    ))

  @overload(ForeverConstant)
  @overload(ForeverConstant, Qt.TimerType)
  def __init__(
      self,
      a0: ForeverConstant,
      type_: Qt.TimerType = Qt.TimerType.CoarseTimer,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QDeadlineTimer::QDeadlineTimer(ForeverConstant a0, Qt::TimerType
    type_)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdeadlinetimer.html#QDeadlineTimer

    Parameters
    ----------

    a0 : ForeverConstant
      Passed on as its number.

    type_ : Qt.TimerType
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.TimerType.CoarseTimer.
    """
    #  QDeadlineTimer::QDeadlineTimer(ForeverConstant a0, Qt::TimerType
    #      type_)
    self._noteCreation(QDeadlineTimer, lambda: Rituals.call(
        'ritual_ZN14QDeadlineTimerC1ENS_15ForeverConstantEN2Qt9TimerTypeE',
        a0.value, type_.value,
    ))

  @overload(int)
  @overload(int, Qt.TimerType)
  def __init__(
      self,
      msecs: int,
      type: Qt.TimerType = Qt.TimerType.CoarseTimer,
  ) -> None:
    """
    Notes what was given, for Qt's 'QDeadlineTimer::QDeadlineTimer(qint64
    msecs, Qt::TimerType type)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdeadlinetimer.html#QDeadlineTimer

    Parameters
    ----------

    msecs : int
      Passed on as it is.

    type : Qt.TimerType
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.TimerType.CoarseTimer.
    """
    #  QDeadlineTimer::QDeadlineTimer(qint64 msecs, Qt::TimerType type)
    self._noteCreation(QDeadlineTimer, lambda: Rituals.call(
        'ritual_ZN14QDeadlineTimerC1ExN2Qt9TimerTypeE', msecs, type.value,
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
