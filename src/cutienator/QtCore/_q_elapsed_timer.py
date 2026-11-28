"""
QElapsedTimer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qelapsedtimer.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QElapsedTimer(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QElapsedTimer: a plain Python object standing in
  front of one C++ QElapsedTimer.

  C++ hands a QElapsedTimer around as a copy, so every C++ QElapsedTimer
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QElapsedTimer that has a ritual and that Python can
  call so far, 18 names in all: 'clockType', 'isMonotonic', 'start',
  'restart', 'invalidate', 'isValid', 'nsecsElapsed', 'elapsed',
  'hasExpired', 'msecsSinceReference', 'msecsTo', 'secsTo', '__lt__',
  '__eq__', '__ne__', '__gt__', '__le__', '__ge__'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Duration QElapsedTimer::durationElapsed() const': gives a type
    Python has no way to take yet.
  - Qt's 'Duration QElapsedTimer::durationTo(const QElapsedTimer &other)
    const': gives a type Python has no way to take yet.
  - Qt's 'QElapsedTimer::~QElapsedTimer()': the destructor: Python removes
    its C++ QElapsedTimer by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QElapsedTimer is created at the first use, not by
    'QElapsedTimer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QElapsedTimer back gives a copy the ritual made for
    Python, in a new cute QElapsedTimer.
  - Each name of Qt's QElapsedTimer that has no cute function yet,
    'durationElapsed', 'durationTo', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QElapsedTimer, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class ClockType(CuteNum):
    """
    The enum 'QElapsedTimer::ClockType' of Qt, with the 5 names Qt gives in
    it.
    """

    SystemTime = Kee[int](0)
    MonotonicClock = Kee[int](1)
    TickCounter = Kee[int](2)
    MachAbsoluteTime = Kee[int](3)
    PerformanceCounter = Kee[int](4)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def clockType() -> ClockType:
    """
    Calls Qt's 'ClockType QElapsedTimer::clockType()'.

    Qt's own words: https://doc.qt.io/qt-6/qelapsedtimer.html#clockType

    Returns
    -------

    ClockType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ClockType(number)' gives.
    """
    #  ClockType QElapsedTimer::clockType()
    return QElapsedTimer.ClockType(Rituals.call(
        'ritual_ZN13QElapsedTimer9clockTypeEv',
    ))

  @staticmethod
  def isMonotonic() -> bool:
    """
    Calls Qt's 'bool QElapsedTimer::isMonotonic()'.

    Qt's own words: https://doc.qt.io/qt-6/qelapsedtimer.html#isMonotonic
    """
    #  bool QElapsedTimer::isMonotonic()
    return Rituals.call('ritual_ZN13QElapsedTimer11isMonotonicEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QElapsedTimer'

  #  Qt's '~QElapsedTimer()'. Naming it makes this a value class: Python owns
  #  every C++ QElapsedTimer behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN13QElapsedTimerD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QElapsedTimer::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qelapsedtimer.html#isValid
    """
    #  bool QElapsedTimer::isValid() const
    return self.uglySide.call('ritual_ZNK13QElapsedTimer7isValidEv')

  def nsecsElapsed(self) -> int:
    """
    Calls Qt's 'qint64 QElapsedTimer::nsecsElapsed() const'.

    Qt's own words: https://doc.qt.io/qt-6/qelapsedtimer.html#nsecsElapsed
    """
    #  qint64 QElapsedTimer::nsecsElapsed() const
    return self.uglySide.call('ritual_ZNK13QElapsedTimer12nsecsElapsedEv')

  def elapsed(self) -> int:
    """
    Calls Qt's 'qint64 QElapsedTimer::elapsed() const'.

    Qt's own words: https://doc.qt.io/qt-6/qelapsedtimer.html#elapsed
    """
    #  qint64 QElapsedTimer::elapsed() const
    return self.uglySide.call('ritual_ZNK13QElapsedTimer7elapsedEv')

  @overload(int)
  def hasExpired(self, timeout: int) -> bool:
    """
    Calls Qt's 'bool QElapsedTimer::hasExpired(qint64 timeout) const'.

    Qt's own words: https://doc.qt.io/qt-6/qelapsedtimer.html#hasExpired

    Parameters
    ----------

    timeout : int
      Passed on as it is.
    """
    #  bool QElapsedTimer::hasExpired(qint64 timeout) const
    return self.uglySide.call(
        'ritual_ZNK13QElapsedTimer10hasExpiredEx', timeout,
    )

  def msecsSinceReference(self) -> int:
    """
    Calls Qt's 'qint64 QElapsedTimer::msecsSinceReference() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qelapsedtimer.html#msecsSinceReference
    """
    #  qint64 QElapsedTimer::msecsSinceReference() const
    return self.uglySide.call(
        'ritual_ZNK13QElapsedTimer19msecsSinceReferenceEv',
    )

  @overload(THIS)
  def msecsTo(self, other: QElapsedTimer) -> int:
    """
    Calls Qt's 'qint64 QElapsedTimer::msecsTo(const QElapsedTimer &other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qelapsedtimer.html#msecsTo

    Parameters
    ----------

    other : QElapsedTimer
      Passed on as a value: Qt reads the C++ QElapsedTimer, which stays
      Python's own.
    """
    #  qint64 QElapsedTimer::msecsTo(const QElapsedTimer &other) const
    return self.uglySide.call(
        'ritual_ZNK13QElapsedTimer7msecsToERKS_', self._valueOf(other),
    )

  @overload(THIS)
  def secsTo(self, other: QElapsedTimer) -> int:
    """
    Calls Qt's 'qint64 QElapsedTimer::secsTo(const QElapsedTimer &other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qelapsedtimer.html#secsTo

    Parameters
    ----------

    other : QElapsedTimer
      Passed on as a value: Qt reads the C++ QElapsedTimer, which stays
      Python's own.
    """
    #  qint64 QElapsedTimer::secsTo(const QElapsedTimer &other) const
    return self.uglySide.call(
        'ritual_ZNK13QElapsedTimer6secsToERKS_', self._valueOf(other),
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

  @overload(THIS)
  def __lt__(self, rhs: QElapsedTimer) -> bool:
    """
    Calls Qt's 'bool operator<(const QElapsedTimer &lhs, const QElapsedTimer
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qelapsedtimer.html#operator<

    Parameters
    ----------

    rhs : QElapsedTimer
      Passed on as a value: Qt reads the C++ QElapsedTimer, which stays
      Python's own.
    """
    #  bool operator<(const QElapsedTimer &lhs, const QElapsedTimer &rhs)
    return Rituals.call(
        'ritual_ZltRK13QElapsedTimerS1_',
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
  def __eq__(self, rhs: QElapsedTimer) -> bool:
    """
    Calls Qt's 'bool operator==(const QElapsedTimer &lhs, const QElapsedTimer
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qelapsedtimer.html#operator==

    Parameters
    ----------

    rhs : QElapsedTimer
      Passed on as a value: Qt reads the C++ QElapsedTimer, which stays
      Python's own.
    """
    #  bool operator==(const QElapsedTimer &lhs, const QElapsedTimer &rhs)
    return Rituals.call(
        'ritual_ZeqRK13QElapsedTimerS1_',
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
  def __ne__(self, rhs: QElapsedTimer) -> bool:
    """
    Calls Qt's 'bool operator!=(const QElapsedTimer &lhs, const QElapsedTimer
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qelapsedtimer.html#operator!=

    Parameters
    ----------

    rhs : QElapsedTimer
      Passed on as a value: Qt reads the C++ QElapsedTimer, which stays
      Python's own.
    """
    #  bool operator!=(const QElapsedTimer &lhs, const QElapsedTimer &rhs)
    return Rituals.call(
        'ritual_ZneRK13QElapsedTimerS1_',
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
  def __gt__(self, rhs: QElapsedTimer) -> bool:
    """
    Calls Qt's 'bool operator>(const QElapsedTimer &lhs, const QElapsedTimer
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qelapsedtimer.html#operator>

    Parameters
    ----------

    rhs : QElapsedTimer
      Passed on as a value: Qt reads the C++ QElapsedTimer, which stays
      Python's own.
    """
    #  bool operator>(const QElapsedTimer &lhs, const QElapsedTimer &rhs)
    return Rituals.call(
        'ritual_ZgtRK13QElapsedTimerS1_',
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
  def __le__(self, rhs: QElapsedTimer) -> bool:
    """
    Calls Qt's 'bool operator<=(const QElapsedTimer &lhs, const QElapsedTimer
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qelapsedtimer.html#operator<=

    Parameters
    ----------

    rhs : QElapsedTimer
      Passed on as a value: Qt reads the C++ QElapsedTimer, which stays
      Python's own.
    """
    #  bool operator<=(const QElapsedTimer &lhs, const QElapsedTimer &rhs)
    return Rituals.call(
        'ritual_ZleRK13QElapsedTimerS1_',
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
  def __ge__(self, rhs: QElapsedTimer) -> bool:
    """
    Calls Qt's 'bool operator>=(const QElapsedTimer &lhs, const QElapsedTimer
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qelapsedtimer.html#operator>=

    Parameters
    ----------

    rhs : QElapsedTimer
      Passed on as a value: Qt reads the C++ QElapsedTimer, which stays
      Python's own.
    """
    #  bool operator>=(const QElapsedTimer &lhs, const QElapsedTimer &rhs)
    return Rituals.call(
        'ritual_ZgeRK13QElapsedTimerS1_',
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
    Notes what was given, for Qt's 'QElapsedTimer::QElapsedTimer()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qelapsedtimer.html#QElapsedTimer
    """
    #  QElapsedTimer::QElapsedTimer()
    self._noteCreation(QElapsedTimer, lambda: Rituals.call(
        'ritual_ZN13QElapsedTimerC1Ev',
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

  def start(self) -> None:
    """
    Calls Qt's 'void QElapsedTimer::start()'.

    Qt's own words: https://doc.qt.io/qt-6/qelapsedtimer.html#start
    """
    #  void QElapsedTimer::start()
    self.uglySide.call('ritual_ZN13QElapsedTimer5startEv')

  def restart(self) -> int:
    """
    Calls Qt's 'qint64 QElapsedTimer::restart()'.

    Qt's own words: https://doc.qt.io/qt-6/qelapsedtimer.html#restart
    """
    #  qint64 QElapsedTimer::restart()
    return self.uglySide.call('ritual_ZN13QElapsedTimer7restartEv')

  def invalidate(self) -> None:
    """
    Calls Qt's 'void QElapsedTimer::invalidate()'.

    Qt's own words: https://doc.qt.io/qt-6/qelapsedtimer.html#invalidate
    """
    #  void QElapsedTimer::invalidate()
    self.uglySide.call('ritual_ZN13QElapsedTimer10invalidateEv')

  @staticmethod
  def durationElapsed(*__, **_) -> Never:
    """
    Qt's 'Duration QElapsedTimer::durationElapsed() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QElapsedTimer.durationElapsed' has no cute function yet. Qt's "
        "'Duration QElapsedTimer::durationElapsed() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def durationTo(*__, **_) -> Never:
    """
    Qt's 'Duration QElapsedTimer::durationTo(const QElapsedTimer &other)
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QElapsedTimer.durationTo' has no cute function yet. Qt's "
        "'Duration QElapsedTimer::durationTo(const QElapsedTimer &other) "
        "const': gives a type Python has no way to take yet.")
