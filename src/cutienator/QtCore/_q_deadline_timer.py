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
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals
from . import Qt

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


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
  call so far, 26 names in all: 'isForever', 'hasExpired', 'timerType',
  'setTimerType', 'remainingTime', 'remainingTimeNSecs', 'setRemainingTime',
  'setPreciseRemainingTime', 'deadline', 'deadlineNSecs', 'setDeadline',
  'setPreciseDeadline', 'addNSecs', 'current', '__add__', '__radd__',
  '__sub__', '__iadd__', '__isub__', '__eq__', '__ne__', '__lt__', '__gt__',
  '__le__', '__ge__', 'rawRemainingTimeNSecs'. It can be made from Python, in
  4 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QDeadlineTimer::swap(QDeadlineTimer &other)': takes a type
    Python has no way to hand over yet.
  - Qt's 'std::chrono::nanoseconds QDeadlineTimer::remainingTimeAsDuration()
    const': gives a type Python has no way to take yet.
  - Qt's 'QDeadlineTimer::~QDeadlineTimer()': the destructor: Python removes
    its C++ QDeadlineTimer by it, and has no other use for it.

  What has no ritual
  ------------------

  7 of the 41 functions Qt declares: 7 a template.

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
  - Each name of Qt's QDeadlineTimer that has no cute function yet,
    'remainingTimeAsDuration', 'swap', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QDeadlineTimer, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class ForeverConstant(CuteNum, scoped=True):
    """
    The enum 'QDeadlineTimer::ForeverConstant' of Qt, with the 1 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Forever = Kee[int](0)

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

  def rawRemainingTimeNSecs(self) -> int:
    """
    Calls Qt's 'qint64 QDeadlineTimer::rawRemainingTimeNSecs() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeadlinetimer.html#rawRemainingTimeNSecs
    """
    #  qint64 QDeadlineTimer::rawRemainingTimeNSecs() const
    return self.uglySide.call(
        'ritual_ZNK14QDeadlineTimer21rawRemainingTimeNSecsEv',
    )

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

  @overload(int)
  def __add__(self, msecs: int) -> QDeadlineTimer:
    """
    Calls Qt's 'QDeadlineTimer operator+(QDeadlineTimer dt, qint64 msecs)'.

    Qt's own words: https://doc.qt.io/qt-6/qdeadlinetimer.html#operator+

    Parameters
    ----------

    msecs : int
      Passed on as it is.

    Returns
    -------

    QDeadlineTimer
      A new cute QDeadlineTimer around the copy Qt gave back. Python owns it.
    """
    #  QDeadlineTimer operator+(QDeadlineTimer dt, qint64 msecs)
    address = Rituals.call(
        'ritual_Zpl14QDeadlineTimerx', CuteMixin._valueOf(self), msecs,
    )
    return QDeadlineTimer._cuteOwning(address)

  @overload.fallback
  def __add__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(int)
  def __radd__(self, msecs: int) -> QDeadlineTimer:
    """
    Calls Qt's 'QDeadlineTimer operator+(qint64 msecs, QDeadlineTimer dt)'.

    Qt's own words: https://doc.qt.io/qt-6/qdeadlinetimer.html#operator+

    Parameters
    ----------

    msecs : int
      Passed on as it is.

    Returns
    -------

    QDeadlineTimer
      A new cute QDeadlineTimer around the copy Qt gave back. Python owns it.
    """
    #  QDeadlineTimer operator+(qint64 msecs, QDeadlineTimer dt)
    address = Rituals.call(
        'ritual_Zplx14QDeadlineTimer', msecs, CuteMixin._valueOf(self),
    )
    return QDeadlineTimer._cuteOwning(address)

  @overload.fallback
  def __radd__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(int)
  def __sub__(self, msecs: int) -> QDeadlineTimer:
    """
    Calls Qt's 'QDeadlineTimer operator-(QDeadlineTimer dt, qint64 msecs)'.

    Qt's own words: https://doc.qt.io/qt-6/qdeadlinetimer.html#operator-

    Parameters
    ----------

    msecs : int
      Passed on as it is.

    Returns
    -------

    QDeadlineTimer
      A new cute QDeadlineTimer around the copy Qt gave back. Python owns it.
    """
    #  QDeadlineTimer operator-(QDeadlineTimer dt, qint64 msecs)
    address = Rituals.call(
        'ritual_Zmi14QDeadlineTimerx', CuteMixin._valueOf(self), msecs,
    )
    return QDeadlineTimer._cuteOwning(address)

  @overload(THIS)
  def __sub__(self, dt2: QDeadlineTimer) -> int:
    """
    Calls Qt's 'qint64 operator-(QDeadlineTimer dt1, QDeadlineTimer dt2)'.

    Qt's own words: https://doc.qt.io/qt-6/qdeadlinetimer.html#operator-

    Parameters
    ----------

    dt2 : QDeadlineTimer
      Passed on as a value: Qt reads the C++ QDeadlineTimer, which stays
      Python's own.
    """
    #  qint64 operator-(QDeadlineTimer dt1, QDeadlineTimer dt2)
    return Rituals.call(
        'ritual_Zmi14QDeadlineTimerS_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(dt2),
    )

  @overload.fallback
  def __sub__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(int)
  def __iadd__(self, msecs: int) -> QDeadlineTimer:
    """
    Calls Qt's 'QDeadlineTimer &QDeadlineTimer::operator+=(qint64 msecs)'.

    Qt's own words: https://doc.qt.io/qt-6/qdeadlinetimer.html#operator+=

    Parameters
    ----------

    msecs : int
      Passed on as it is.
    """
    #  QDeadlineTimer &QDeadlineTimer::operator+=(qint64 msecs)
    self.uglySide.call('ritual_ZN14QDeadlineTimerpLEx', msecs)
    return self

  @overload.fallback
  def __iadd__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(int)
  def __isub__(self, msecs: int) -> QDeadlineTimer:
    """
    Calls Qt's 'QDeadlineTimer &QDeadlineTimer::operator-=(qint64 msecs)'.

    Qt's own words: https://doc.qt.io/qt-6/qdeadlinetimer.html#operator-=

    Parameters
    ----------

    msecs : int
      Passed on as it is.
    """
    #  QDeadlineTimer &QDeadlineTimer::operator-=(qint64 msecs)
    self.uglySide.call('ritual_ZN14QDeadlineTimermIEx', msecs)
    return self

  @overload.fallback
  def __isub__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __eq__(self, rhs: QDeadlineTimer) -> bool:
    """
    Calls Qt's 'bool operator==(const QDeadlineTimer &lhs, const
    QDeadlineTimer &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qdeadlinetimer.html#operator==

    Parameters
    ----------

    rhs : QDeadlineTimer
      Passed on as a value: Qt reads the C++ QDeadlineTimer, which stays
      Python's own.
    """
    #  bool operator==(const QDeadlineTimer &lhs, const QDeadlineTimer &rhs)
    return Rituals.call(
        'ritual_ZeqRK14QDeadlineTimerS1_',
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
  def __ne__(self, rhs: QDeadlineTimer) -> bool:
    """
    Calls Qt's 'bool operator!=(const QDeadlineTimer &lhs, const
    QDeadlineTimer &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qdeadlinetimer.html#operator!=

    Parameters
    ----------

    rhs : QDeadlineTimer
      Passed on as a value: Qt reads the C++ QDeadlineTimer, which stays
      Python's own.
    """
    #  bool operator!=(const QDeadlineTimer &lhs, const QDeadlineTimer &rhs)
    return Rituals.call(
        'ritual_ZneRK14QDeadlineTimerS1_',
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

  @overload(THIS)
  def __lt__(self, rhs: QDeadlineTimer) -> bool:
    """
    Calls Qt's 'bool operator<(const QDeadlineTimer &lhs, const
    QDeadlineTimer &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qdeadlinetimer.html#operator<

    Parameters
    ----------

    rhs : QDeadlineTimer
      Passed on as a value: Qt reads the C++ QDeadlineTimer, which stays
      Python's own.
    """
    #  bool operator<(const QDeadlineTimer &lhs, const QDeadlineTimer &rhs)
    return Rituals.call(
        'ritual_ZltRK14QDeadlineTimerS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __lt__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __gt__(self, rhs: QDeadlineTimer) -> bool:
    """
    Calls Qt's 'bool operator>(const QDeadlineTimer &lhs, const
    QDeadlineTimer &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qdeadlinetimer.html#operator>

    Parameters
    ----------

    rhs : QDeadlineTimer
      Passed on as a value: Qt reads the C++ QDeadlineTimer, which stays
      Python's own.
    """
    #  bool operator>(const QDeadlineTimer &lhs, const QDeadlineTimer &rhs)
    return Rituals.call(
        'ritual_ZgtRK14QDeadlineTimerS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __gt__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __le__(self, rhs: QDeadlineTimer) -> bool:
    """
    Calls Qt's 'bool operator<=(const QDeadlineTimer &lhs, const
    QDeadlineTimer &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qdeadlinetimer.html#operator<=

    Parameters
    ----------

    rhs : QDeadlineTimer
      Passed on as a value: Qt reads the C++ QDeadlineTimer, which stays
      Python's own.
    """
    #  bool operator<=(const QDeadlineTimer &lhs, const QDeadlineTimer &rhs)
    return Rituals.call(
        'ritual_ZleRK14QDeadlineTimerS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __le__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ge__(self, rhs: QDeadlineTimer) -> bool:
    """
    Calls Qt's 'bool operator>=(const QDeadlineTimer &lhs, const
    QDeadlineTimer &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qdeadlinetimer.html#operator>=

    Parameters
    ----------

    rhs : QDeadlineTimer
      Passed on as a value: Qt reads the C++ QDeadlineTimer, which stays
      Python's own.
    """
    #  bool operator>=(const QDeadlineTimer &lhs, const QDeadlineTimer &rhs)
    return Rituals.call(
        'ritual_ZgeRK14QDeadlineTimerS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ge__(self, *args: object) -> object:
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

  @staticmethod
  def remainingTimeAsDuration(*__, **_) -> Never:
    """
    Qt's 'std::chrono::nanoseconds QDeadlineTimer::remainingTimeAsDuration()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QDeadlineTimer.remainingTimeAsDuration' has no cute function yet. "
        "Qt's 'std::chrono::nanoseconds "
        "QDeadlineTimer::remainingTimeAsDuration() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QDeadlineTimer::swap(QDeadlineTimer &other)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QDeadlineTimer.swap' has no cute function yet. Qt's 'void "
        "QDeadlineTimer::swap(QDeadlineTimer &other)': takes a type Python "
        "has no way to hand over yet.")
