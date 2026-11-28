"""
QEventDispatcherUNIX binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qeventdispatcher_unix_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QEventDispatcherUNIX to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import Qt, QAbstractEventDispatcherV2, QEventLoop, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QEventDispatcherUNIXPrivate, QMetaObject, QSocketNotifier
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSocketNotifier = WAIT['QSocketNotifier']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QEventDispatcherUNIX(QAbstractEventDispatcherV2):
  """
  The cute side of Qt's QEventDispatcherUNIX: a plain Python object standing
  in front of one C++ QEventDispatcherUNIX.

  It is built on the cute 'QAbstractEventDispatcherV2', as Qt's
  QEventDispatcherUNIX is built on Qt's QAbstractEventDispatcherV2, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QEventDispatcherUNIX that has a ritual and that
  Python can call so far, 10 names in all: 'metaObject', 'tr', 'd_func',
  'processEvents', 'registerSocketNotifier', 'unregisterSocketNotifier',
  'unregisterTimer', 'unregisterTimers', 'wakeUp', 'interrupt'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QEventDispatcherUNIX::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QEventDispatcherUNIX::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'const QEventDispatcherUNIXPrivate *QEventDispatcherUNIX::d_func()
    const': takes in Python what 'QEventDispatcherUNIXPrivate
    *QEventDispatcherUNIX::d_func()' takes.
  - Qt's 'QEventDispatcherUNIX::~QEventDispatcherUNIX()': the destructor:
    Python never removes a C++ QEventDispatcherUNIX.
  - Qt's 'void QEventDispatcherUNIX::registerTimer(Qt::TimerId timerId,
    Duration interval, Qt::TimerType timerType, QObject *object)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QList<TimerInfoV2> QEventDispatcherUNIX::timersForObject(QObject
    *object) const': gives a type Python has no way to take yet.
  - Qt's 'Duration QEventDispatcherUNIX::remainingTime(Qt::TimerId timerId)
    const': gives a type Python has no way to take yet.
  - Qt's
    'QEventDispatcherUNIX::QEventDispatcherUNIX(QEventDispatcherUNIXPrivate
    &dd, QObject *parent)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 21 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QEventDispatcherUNIX is created at the first use, not by
    'QEventDispatcherUNIX(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QEventDispatcherUNIX.
  - Qt tells when it has removed the C++ QEventDispatcherUNIX. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QEventDispatcherUNIX::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qeventdispatcherunix.html#tr

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
    #  QString QEventDispatcherUNIX::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QEventDispatcherUNIX2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QEventDispatcherUNIX'

  #  A C++ QEventDispatcherUNIX Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QEventDispatcherUNIX'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QEventDispatcherUNIX::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qeventdispatcherunix.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QEventDispatcherUNIX::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QEventDispatcherUNIX10metaObjectEv',
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

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QEventDispatcherUNIX::QEventDispatcherUNIX(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qeventdispatcherunix.html#QEventDispatcherUNIX

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QEventDispatcherUNIX::QEventDispatcherUNIX(QObject *parent)
    self._noteCreation(QEventDispatcherUNIX, lambda: Rituals.call(
        'ritual_ZN20QEventDispatcherUNIXC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  def d_func(self) -> Optional[QEventDispatcherUNIXPrivate]:
    """
    Calls Qt's 'QEventDispatcherUNIXPrivate *QEventDispatcherUNIX::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qeventdispatcherunix.html#d_func

    Returns
    -------

    Optional[QEventDispatcherUNIXPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QEventDispatcherUNIXPrivate *QEventDispatcherUNIX::d_func()
    address = self.uglySide.call('ritual_ZN20QEventDispatcherUNIX6d_funcEv')
    from . import QEventDispatcherUNIXPrivate
    return QEventDispatcherUNIXPrivate._cuteAt(address)

  @overload(QEventLoop.ProcessEventsFlags)
  def processEvents(self, flags: QEventLoop.ProcessEventsFlags) -> bool:
    """
    Calls Qt's 'bool
    QEventDispatcherUNIX::processEvents(QEventLoop::ProcessEventsFlags
    flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qeventdispatcherunix.html#processEvents

    Parameters
    ----------

    flags : QEventLoop.ProcessEventsFlags
      Passed on as its number.
    """
    #  bool
    #      QEventDispatcherUNIX::processEvents(QEventLoop::ProcessEventsFlags
    #      flags)
    ritual = (
        'ritual_ZN20QEventDispatcherUNIX13processEventsE6QFlagsIN10QEventLo'
        'op17ProcessEventsFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QEventDispatcherUNIX13processEventsE6QFlagsIN10QE'
          'ventLoop17ProcessEventsFlagEE')
    return self.uglySide.call(ritual, flags.value)

  @overload(QSocketNotifier)
  @overload(NoneType)
  def registerSocketNotifier(
      self,
      notifier: Optional[QSocketNotifier],
  ) -> None:
    """
    Calls Qt's 'void
    QEventDispatcherUNIX::registerSocketNotifier(QSocketNotifier *notifier)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qeventdispatcherunix.html#registerSocketNotifier

    Parameters
    ----------

    notifier : Optional[QSocketNotifier]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QEventDispatcherUNIX::registerSocketNotifier(QSocketNotifier
    #      *notifier)
    self.uglySide.call(
        'ritual_ZN20QEventDispatcherUNIX22registerSocketNotifierEP15QSocket'
        'Notifier',
        self._addressOf(notifier),
    )

  @overload(QSocketNotifier)
  @overload(NoneType)
  def unregisterSocketNotifier(
      self,
      notifier: Optional[QSocketNotifier],
  ) -> None:
    """
    Calls Qt's 'void
    QEventDispatcherUNIX::unregisterSocketNotifier(QSocketNotifier
    *notifier)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qeventdispatcherunix.html#unregisterSocketNotifier

    Parameters
    ----------

    notifier : Optional[QSocketNotifier]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QEventDispatcherUNIX::unregisterSocketNotifier(QSocketNotifier
    #      *notifier)
    self.uglySide.call(
        'ritual_ZN20QEventDispatcherUNIX24unregisterSocketNotifierEP15QSock'
        'etNotifier',
        self._addressOf(notifier),
    )

  @overload(Qt.TimerId)
  def unregisterTimer(self, timerId: Qt.TimerId) -> bool:
    """
    Calls Qt's 'bool QEventDispatcherUNIX::unregisterTimer(Qt::TimerId
    timerId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qeventdispatcherunix.html#unregisterTimer

    Parameters
    ----------

    timerId : Qt.TimerId
      Passed on as its number.
    """
    #  bool QEventDispatcherUNIX::unregisterTimer(Qt::TimerId timerId)
    return self.uglySide.call(
        'ritual_ZN20QEventDispatcherUNIX15unregisterTimerEN2Qt7TimerIdE',
        timerId.value,
    )

  @overload(QObject)
  @overload(NoneType)
  def unregisterTimers(self, object: Optional[QObject]) -> bool:
    """
    Calls Qt's 'bool QEventDispatcherUNIX::unregisterTimers(QObject
    *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qeventdispatcherunix.html#unregisterTimers

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QEventDispatcherUNIX::unregisterTimers(QObject *object)
    return self.uglySide.call(
        'ritual_ZN20QEventDispatcherUNIX16unregisterTimersEP7QObject',
        self._addressOf(object, 'QObject'),
    )

  def wakeUp(self) -> None:
    """
    Calls Qt's 'void QEventDispatcherUNIX::wakeUp()'.

    Qt's own words: https://doc.qt.io/qt-6/qeventdispatcherunix.html#wakeUp
    """
    #  void QEventDispatcherUNIX::wakeUp()
    ritual = 'ritual_ZN20QEventDispatcherUNIX6wakeUpEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QEventDispatcherUNIX6wakeUpEv'
    self.uglySide.call(ritual)

  def interrupt(self) -> None:
    """
    Calls Qt's 'void QEventDispatcherUNIX::interrupt()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qeventdispatcherunix.html#interrupt
    """
    #  void QEventDispatcherUNIX::interrupt()
    self.uglySide.call('ritual_ZN20QEventDispatcherUNIX9interruptEv')
