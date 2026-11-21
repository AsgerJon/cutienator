"""
QTimer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtCore/qtimer.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from . import Qt, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTimer(QObject):
  """
  The cute side of Qt's QTimer: a plain Python object standing in front of
  one C++ QTimer.

  It is built on the cute 'QObject', as Qt's QTimer is built on Qt's QObject,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QTimer that has a ritual and that Python can call so
  far, 15 names in all: 'metaObject', 'tr', 'isActive', 'timerId', 'id',
  'setInterval', 'interval', 'remainingTime', 'setTimerType', 'timerType',
  'setSingleShot', 'isSingleShot', 'singleShot', 'start', 'stop'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTimer::~QTimer()': the destructor: Python never removes a C++
    QTimer.

  What has no ritual
  ------------------

  33 of the 52 functions Qt declares: 12 takes or gives a type that cannot be
  passed yet; 11 private; 6 a template; 2 forbidden; 1 a signal; 1 protected.

  What to expect
  --------------

  - The C++ QTimer is created at the first use, not by 'QTimer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTimer.
  - Qt tells when it has removed the C++ QTimer. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QTimer::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qtimer.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTimer::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN6QTimer2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(int, QObject, str)
  @overload(int, QObject, NoneType)
  @overload(int, NoneType, str)
  @overload(int, NoneType, NoneType)
  def singleShot(
      msec: int,
      receiver: Optional[QObject],
      member: Optional[str],
  ) -> None:
    """
    Calls Qt's 'void QTimer::singleShot(int msec, const QObject *receiver,
    const char *member)'.

    Qt's own words: https://doc.qt.io/qt-6/qtimer.html#singleShot

    Parameters
    ----------

    msec : int
      Passed on as it is.

    receiver : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    member : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  void QTimer::singleShot(int msec, const QObject *receiver, const char
    #      *member)
    Rituals.call(
        'ritual_ZN6QTimer10singleShotEiPK7QObjectPKc',
        msec, CuteMixin._addressOf(receiver), CuteMixin._bytesOf(member),
    )

  @staticmethod
  @overload(int, Qt.TimerType, QObject, str)
  @overload(int, Qt.TimerType, QObject, NoneType)
  @overload(int, Qt.TimerType, NoneType, str)
  @overload(int, Qt.TimerType, NoneType, NoneType)
  def singleShot(
      msec: int,
      timerType: Qt.TimerType,
      receiver: Optional[QObject],
      member: Optional[str],
  ) -> None:
    """
    Calls Qt's 'void QTimer::singleShot(int msec, Qt::TimerType timerType,
    const QObject *receiver, const char *member)'.

    Qt's own words: https://doc.qt.io/qt-6/qtimer.html#singleShot

    Parameters
    ----------

    msec : int
      Passed on as it is.

    timerType : Qt.TimerType
      Passed on as its number.

    receiver : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    member : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  void QTimer::singleShot(int msec, Qt::TimerType timerType, const
    #      QObject *receiver, const char *member)
    Rituals.call(
        'ritual_ZN6QTimer10singleShotEiN2Qt9TimerTypeEPK7QObjectPKc',
        msec, timerType.value, CuteMixin._addressOf(receiver),
        CuteMixin._bytesOf(member),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTimer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QTimer::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtimer.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QTimer::metaObject() const
    address = self.uglySide.call('ritual_ZNK6QTimer10metaObjectEv')
    from . import QMetaObject
    return QMetaObject._cuteAt(address)

  def isActive(self) -> bool:
    """
    Calls Qt's 'bool QTimer::isActive() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtimer.html#isActive
    """
    #  bool QTimer::isActive() const
    return self.uglySide.call('ritual_ZNK6QTimer8isActiveEv')

  def timerId(self) -> int:
    """
    Calls Qt's 'int QTimer::timerId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtimer.html#timerId
    """
    #  int QTimer::timerId() const
    return self.uglySide.call('ritual_ZNK6QTimer7timerIdEv')

  def id(self) -> Qt.TimerId:
    """
    Calls Qt's 'Qt::TimerId QTimer::id() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtimer.html#id

    Returns
    -------

    Qt.TimerId
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.TimerId(number)'
      gives.
    """
    #  Qt::TimerId QTimer::id() const
    return Qt.TimerId(self.uglySide.call('ritual_ZNK6QTimer2idEv'))

  def interval(self) -> int:
    """
    Calls Qt's 'int QTimer::interval() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtimer.html#interval
    """
    #  int QTimer::interval() const
    return self.uglySide.call('ritual_ZNK6QTimer8intervalEv')

  def remainingTime(self) -> int:
    """
    Calls Qt's 'int QTimer::remainingTime() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtimer.html#remainingTime
    """
    #  int QTimer::remainingTime() const
    return self.uglySide.call('ritual_ZNK6QTimer13remainingTimeEv')

  def timerType(self) -> Qt.TimerType:
    """
    Calls Qt's 'Qt::TimerType QTimer::timerType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtimer.html#timerType

    Returns
    -------

    Qt.TimerType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.TimerType(number)'
      gives.
    """
    #  Qt::TimerType QTimer::timerType() const
    return Qt.TimerType(self.uglySide.call('ritual_ZNK6QTimer9timerTypeEv'))

  def isSingleShot(self) -> bool:
    """
    Calls Qt's 'bool QTimer::isSingleShot() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtimer.html#isSingleShot
    """
    #  bool QTimer::isSingleShot() const
    return self.uglySide.call('ritual_ZNK6QTimer12isSingleShotEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setInterval(self, msec: int) -> None:
    """
    Calls Qt's 'void QTimer::setInterval(int msec)'.

    Qt's own words: https://doc.qt.io/qt-6/qtimer.html#setInterval

    Parameters
    ----------

    msec : int
      Passed on as it is.
    """
    #  void QTimer::setInterval(int msec)
    self.uglySide.call('ritual_ZN6QTimer11setIntervalEi', msec)

  @overload(Qt.TimerType)
  def setTimerType(self, atype: Qt.TimerType) -> None:
    """
    Calls Qt's 'void QTimer::setTimerType(Qt::TimerType atype)'.

    Qt's own words: https://doc.qt.io/qt-6/qtimer.html#setTimerType

    Parameters
    ----------

    atype : Qt.TimerType
      Passed on as its number.
    """
    #  void QTimer::setTimerType(Qt::TimerType atype)
    self.uglySide.call(
        'ritual_ZN6QTimer12setTimerTypeEN2Qt9TimerTypeE', atype.value,
    )

  @overload(bool)
  def setSingleShot(self, singleShot: bool) -> None:
    """
    Calls Qt's 'void QTimer::setSingleShot(bool singleShot)'.

    Qt's own words: https://doc.qt.io/qt-6/qtimer.html#setSingleShot

    Parameters
    ----------

    singleShot : bool
      Passed on as it is.
    """
    #  void QTimer::setSingleShot(bool singleShot)
    self.uglySide.call('ritual_ZN6QTimer13setSingleShotEb', singleShot)

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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QTimer::QTimer(QObject *parent)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtimer.html#QTimer

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QTimer::QTimer(QObject *parent)
    self._noteCreation(QTimer, lambda: Rituals.call(
        'ritual_ZN6QTimerC1EP7QObject', self._addressOf(parent),
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

  @overload(int)
  def start(self, msec: int) -> None:
    """
    Calls Qt's 'void QTimer::start(int msec)'.

    Qt's own words: https://doc.qt.io/qt-6/qtimer.html#start

    Parameters
    ----------

    msec : int
      Passed on as it is.
    """
    #  void QTimer::start(int msec)
    self.uglySide.call('ritual_ZN6QTimer5startEi', msec)

  @overload()
  def start(self) -> None:
    """
    Calls Qt's 'void QTimer::start()'.

    Qt's own words: https://doc.qt.io/qt-6/qtimer.html#start
    """
    #  void QTimer::start()
    self.uglySide.call('ritual_ZN6QTimer5startEv')

  def stop(self) -> None:
    """
    Calls Qt's 'void QTimer::stop()'.

    Qt's own words: https://doc.qt.io/qt-6/qtimer.html#stop
    """
    #  void QTimer::stop()
    self.uglySide.call('ritual_ZN6QTimer4stopEv')
