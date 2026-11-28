"""
QAbstractEventDispatcherV2 binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qabstracteventdispatcher.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import Qt, QAbstractEventDispatcher, QEventLoop, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QAbstractEventDispatcherPrivate, QDeadlineTimer, QMetaObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDeadlineTimer = WAIT['QDeadlineTimer']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractEventDispatcherV2(QAbstractEventDispatcher):
  """
  The cute side of Qt's QAbstractEventDispatcherV2: a plain Python object
  standing in front of one C++ QAbstractEventDispatcherV2.

  It is built on the cute 'QAbstractEventDispatcher', as Qt's
  QAbstractEventDispatcherV2 is built on Qt's QAbstractEventDispatcher, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstractEventDispatcherV2 that has a ritual and
  that Python can call so far, 7 names in all: 'metaObject', 'tr', 'd_func',
  'unregisterTimer', 'processEventsWithDeadline', 'registerTimer',
  'remainingTime'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QAbstractEventDispatcherV2::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QAbstractEventDispatcherV2::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'const QAbstractEventDispatcherPrivate
    *QAbstractEventDispatcherV2::d_func() const': takes in Python what
    'QAbstractEventDispatcherPrivate *QAbstractEventDispatcherV2::d_func()'
    takes.
  - Qt's 'QAbstractEventDispatcherV2::~QAbstractEventDispatcherV2()': the
    destructor: Python never removes a C++ QAbstractEventDispatcherV2.
  - Qt's 'void QAbstractEventDispatcherV2::registerTimer(Qt::TimerId timerId,
    Duration interval, Qt::TimerType timerType, QObject *object)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QList<TimerInfoV2>
    QAbstractEventDispatcherV2::timersForObject(QObject *object) const':
    gives a type Python has no way to take yet.
  - Qt's 'Duration QAbstractEventDispatcherV2::remainingTime(Qt::TimerId
    timerId) const': gives a type Python has no way to take yet.
  - Qt's 'QList<TimerInfo>
    QAbstractEventDispatcherV2::registeredTimers(QObject *object) const':
    gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  4 of the 20 functions Qt declares: 2 not a gap; 2 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ QAbstractEventDispatcherV2 is created at the first use, not by
    'QAbstractEventDispatcherV2(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractEventDispatcherV2.
  - Qt tells when it has removed the C++ QAbstractEventDispatcherV2. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QAbstractEventDispatcherV2 that has no cute function
    yet, '__init__', holds a function that raises 'NotImplementedError', and
    its docstring says why.
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
    Calls Qt's 'QString QAbstractEventDispatcherV2::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstracteventdispatcherv2.html#tr

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
    #  QString QAbstractEventDispatcherV2::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN26QAbstractEventDispatcherV22trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractEventDispatcherV2'

  #  A C++ QAbstractEventDispatcherV2 Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAbstractEventDispatcherV2'

  #  The functions Qt calls itself that QAbstractEventDispatcherV2 is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'processEventsWithDeadline': (
          ('_ZN26QAbstractEventDispatcherV225processEventsWithDeadlineE6QFl'
           'agsIN10QEventLoop17ProcessEventsFlagEE14QDeadlineTimer',
           ('bool', 'number', ''),
           (
               ('int', 'flags', 'QtCore:QEventLoop.ProcessEventsFlag'),
               ('address', 'value', 'QtCore:QDeadlineTimer'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QAbstractEventDispatcherV2::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracteventdispatcherv2.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QAbstractEventDispatcherV2::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK26QAbstractEventDispatcherV210metaObjectEv',
    )
    from . import QMetaObject
    return QMetaObject._cuteAt(address)

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    - Qt's 'QAbstractEventDispatcherV2::QAbstractEventDispatcherV2(QObject
      *parent)': the class is abstract, so C++ cannot make one, and the C++
      class of ours does not fill in every function it leaves open.
    - Qt's 'QAbstractEventDispatcherV2::QAbstractEventDispatcherV2(
      QAbstractEventDispatcherPrivate &a0, QObject *parent)': the class is
      abstract, so C++ cannot make one, and the C++ class of ours does not
      fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'QAbstractEventDispatcherV2.__init__' has no cute function yet. "
        "Qt's "
        "'QAbstractEventDispatcherV2::QAbstractEventDispatcherV2(QObject "
        "*parent)': the class is abstract, so C++ cannot make one, and the "
        "C++ class of ours does not fill in every function it leaves open. "
        "Qt's "
        "'QAbstractEventDispatcherV2::QAbstractEventDispatcherV2(QAbstractEv"
        "entDispatcherPrivate &a0, QObject *parent)': the class is "
        "abstract, so C++ cannot make one, and the C++ class of ours does "
        "not fill in every function it leaves open.")

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

  def d_func(self) -> Optional[QAbstractEventDispatcherPrivate]:
    """
    Calls Qt's 'QAbstractEventDispatcherPrivate
    *QAbstractEventDispatcherV2::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracteventdispatcherv2.html#d_func

    Returns
    -------

    Optional[QAbstractEventDispatcherPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractEventDispatcherPrivate *QAbstractEventDispatcherV2::d_func()
    address = self.uglySide.call(
        'ritual_ZN26QAbstractEventDispatcherV26d_funcEv',
    )
    from . import QAbstractEventDispatcherPrivate
    return QAbstractEventDispatcherPrivate._cuteAt(address)

  @overload(Qt.TimerId)
  def unregisterTimer(self, timerId: Qt.TimerId) -> bool:
    """
    Calls Qt's 'bool QAbstractEventDispatcherV2::unregisterTimer(Qt::TimerId
    timerId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracteventdispatcherv2.html#unregisterTimer

    Parameters
    ----------

    timerId : Qt.TimerId
      Passed on as its number.
    """
    #  bool QAbstractEventDispatcherV2::unregisterTimer(Qt::TimerId timerId)
    return self.uglySide.call(
        'ritual_ZN26QAbstractEventDispatcherV215unregisterTimerEN2Qt7TimerI'
        'dE',
        timerId.value,
    )

  @overload(int)
  def unregisterTimer(self, timerId: int) -> bool:
    """
    Calls Qt's 'bool QAbstractEventDispatcherV2::unregisterTimer(int
    timerId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracteventdispatcherv2.html#unregisterTimer

    Parameters
    ----------

    timerId : int
      Passed on as it is.
    """
    #  bool QAbstractEventDispatcherV2::unregisterTimer(int timerId)
    return self.uglySide.call(
        'ritual_ZN26QAbstractEventDispatcherV215unregisterTimerEi', timerId,
    )

  @overload(QEventLoop.ProcessEventsFlags, QDeadlineTimer)
  def processEventsWithDeadline(
      self,
      flags: QEventLoop.ProcessEventsFlags,
      deadline: QDeadlineTimer,
  ) -> bool:
    """
    Calls Qt's 'bool
    QAbstractEventDispatcherV2::processEventsWithDeadline(QEventLoop::
    ProcessEventsFlags flags, QDeadlineTimer deadline)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracteventdispatcherv2.html

    Parameters
    ----------

    flags : QEventLoop.ProcessEventsFlags
      Passed on as its number.

    deadline : QDeadlineTimer
      Passed on as a value: Qt reads the C++ QDeadlineTimer, which stays
      Python's own.
    """
    #  bool QAbstractEventDispatcherV2::processEventsWithDeadline(
    #      QEventLoop::ProcessEventsFlags flags, QDeadlineTimer deadline)
    ritual = (
        'ritual_ZN26QAbstractEventDispatcherV225processEventsWithDeadlineE6'
        'QFlagsIN10QEventLoop17ProcessEventsFlagEE14QDeadlineTimer')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN26QAbstractEventDispatcherV225processEventsWithDead'
          'lineE6QFlagsIN10QEventLoop17ProcessEventsFlagEE14QDeadlineTimer')
    return self.uglySide.call(ritual, flags.value, self._valueOf(deadline))

  @overload(int, int, Qt.TimerType, QObject)
  @overload(int, int, Qt.TimerType, NoneType)
  def registerTimer(
      self,
      timerId: int,
      interval: int,
      timerType: Qt.TimerType,
      object: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void QAbstractEventDispatcherV2::registerTimer(int timerId,
    qint64 interval, Qt::TimerType timerType, QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracteventdispatcherv2.html#registerTimer

    Parameters
    ----------

    timerId : int
      Passed on as it is.

    interval : int
      Passed on as it is.

    timerType : Qt.TimerType
      Passed on as its number.

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractEventDispatcherV2::registerTimer(int timerId, qint64
    #      interval, Qt::TimerType timerType, QObject *object)
    self.uglySide.call(
        'ritual_ZN26QAbstractEventDispatcherV213registerTimerEixN2Qt9TimerT'
        'ypeEP7QObject',
        timerId, interval, timerType.value, self._addressOf(object,
        'QObject'),
    )

  @overload(int)
  def remainingTime(self, timerId: int) -> int:
    """
    Calls Qt's 'int QAbstractEventDispatcherV2::remainingTime(int timerId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracteventdispatcherv2.html#remainingTime

    Parameters
    ----------

    timerId : int
      Passed on as it is.
    """
    #  int QAbstractEventDispatcherV2::remainingTime(int timerId)
    return self.uglySide.call(
        'ritual_ZN26QAbstractEventDispatcherV213remainingTimeEi', timerId,
    )
