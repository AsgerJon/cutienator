"""
QEventDispatcherGlib binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qeventdispatcher_glib_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QEventDispatcherGlib to be private: it declares the class in a
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

  from . import QEventDispatcherGlibPrivate, QMetaObject, QSocketNotifier
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSocketNotifier = WAIT['QSocketNotifier']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QEventDispatcherGlib(QAbstractEventDispatcherV2):
  """
  The cute side of Qt's QEventDispatcherGlib: a plain Python object standing
  in front of one C++ QEventDispatcherGlib.

  It is built on the cute 'QAbstractEventDispatcherV2', as Qt's
  QEventDispatcherGlib is built on Qt's QAbstractEventDispatcherV2, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QEventDispatcherGlib that has a ritual and that
  Python can call so far, 11 names in all: 'metaObject', 'tr', 'd_func',
  'processEvents', 'registerSocketNotifier', 'unregisterSocketNotifier',
  'unregisterTimer', 'unregisterTimers', 'wakeUp', 'interrupt',
  'versionSupported'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QEventDispatcherGlib::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QEventDispatcherGlib::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'const QEventDispatcherGlibPrivate *QEventDispatcherGlib::d_func()
    const': takes in Python what 'QEventDispatcherGlibPrivate
    *QEventDispatcherGlib::d_func()' takes.
  - Qt's 'QEventDispatcherGlib::QEventDispatcherGlib(GMainContext *context,
    QObject *parent)': names 'GMainContext', which has no cute class yet.
  - Qt's 'QEventDispatcherGlib::~QEventDispatcherGlib()': the destructor:
    Python never removes a C++ QEventDispatcherGlib.
  - Qt's 'void QEventDispatcherGlib::registerTimer(Qt::TimerId timerId,
    Duration interval, Qt::TimerType timerType, QObject *object)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QList<TimerInfoV2> QEventDispatcherGlib::timersForObject(QObject
    *object) const': gives a type Python has no way to take yet.
  - Qt's 'Duration QEventDispatcherGlib::remainingTime(Qt::TimerId timerId)
    const': gives a type Python has no way to take yet.
  - Qt's
    'QEventDispatcherGlib::QEventDispatcherGlib(QEventDispatcherGlibPrivate
    &dd, QObject *parent)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 23 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QEventDispatcherGlib is created at the first use, not by
    'QEventDispatcherGlib(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QEventDispatcherGlib.
  - Qt tells when it has removed the C++ QEventDispatcherGlib. Every call on
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
    Calls Qt's 'QString QEventDispatcherGlib::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qeventdispatcherglib.html#tr

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
    #  QString QEventDispatcherGlib::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QEventDispatcherGlib2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def versionSupported() -> bool:
    """
    Calls Qt's 'bool QEventDispatcherGlib::versionSupported()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qeventdispatcherglib.html#versionSupported
    """
    #  bool QEventDispatcherGlib::versionSupported()
    return Rituals.call(
        'ritual_ZN20QEventDispatcherGlib16versionSupportedEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QEventDispatcherGlib'

  #  A C++ QEventDispatcherGlib Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QEventDispatcherGlib'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QEventDispatcherGlib::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qeventdispatcherglib.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QEventDispatcherGlib::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QEventDispatcherGlib10metaObjectEv',
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
    'QEventDispatcherGlib::QEventDispatcherGlib(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qeventdispatcherglib.html#QEventDispatcherGlib

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QEventDispatcherGlib::QEventDispatcherGlib(QObject *parent)
    self._noteCreation(QEventDispatcherGlib, lambda: Rituals.call(
        'ritual_ZN20QEventDispatcherGlibC1EP7QObject',
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

  def d_func(self) -> Optional[QEventDispatcherGlibPrivate]:
    """
    Calls Qt's 'QEventDispatcherGlibPrivate *QEventDispatcherGlib::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qeventdispatcherglib.html#d_func

    Returns
    -------

    Optional[QEventDispatcherGlibPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QEventDispatcherGlibPrivate *QEventDispatcherGlib::d_func()
    address = self.uglySide.call('ritual_ZN20QEventDispatcherGlib6d_funcEv')
    from . import QEventDispatcherGlibPrivate
    return QEventDispatcherGlibPrivate._cuteAt(address)

  @overload(QEventLoop.ProcessEventsFlags)
  def processEvents(self, flags: QEventLoop.ProcessEventsFlags) -> bool:
    """
    Calls Qt's 'bool
    QEventDispatcherGlib::processEvents(QEventLoop::ProcessEventsFlags
    flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qeventdispatcherglib.html#processEvents

    Parameters
    ----------

    flags : QEventLoop.ProcessEventsFlags
      Passed on as its number.
    """
    #  bool
    #      QEventDispatcherGlib::processEvents(QEventLoop::ProcessEventsFlags
    #      flags)
    ritual = (
        'ritual_ZN20QEventDispatcherGlib13processEventsE6QFlagsIN10QEventLo'
        'op17ProcessEventsFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QEventDispatcherGlib13processEventsE6QFlagsIN10QE'
          'ventLoop17ProcessEventsFlagEE')
    return self.uglySide.call(ritual, flags.value)

  @overload(QSocketNotifier)
  @overload(NoneType)
  def registerSocketNotifier(
      self,
      socketNotifier: Optional[QSocketNotifier],
  ) -> None:
    """
    Calls Qt's 'void
    QEventDispatcherGlib::registerSocketNotifier(QSocketNotifier
    *socketNotifier)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qeventdispatcherglib.html#registerSocketNotifier

    Parameters
    ----------

    socketNotifier : Optional[QSocketNotifier]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QEventDispatcherGlib::registerSocketNotifier(QSocketNotifier
    #      *socketNotifier)
    self.uglySide.call(
        'ritual_ZN20QEventDispatcherGlib22registerSocketNotifierEP15QSocket'
        'Notifier',
        self._addressOf(socketNotifier),
    )

  @overload(QSocketNotifier)
  @overload(NoneType)
  def unregisterSocketNotifier(
      self,
      socketNotifier: Optional[QSocketNotifier],
  ) -> None:
    """
    Calls Qt's 'void
    QEventDispatcherGlib::unregisterSocketNotifier(QSocketNotifier
    *socketNotifier)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qeventdispatcherglib.html#unregisterSocketNotifier

    Parameters
    ----------

    socketNotifier : Optional[QSocketNotifier]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QEventDispatcherGlib::unregisterSocketNotifier(QSocketNotifier
    #      *socketNotifier)
    self.uglySide.call(
        'ritual_ZN20QEventDispatcherGlib24unregisterSocketNotifierEP15QSock'
        'etNotifier',
        self._addressOf(socketNotifier),
    )

  @overload(Qt.TimerId)
  def unregisterTimer(self, timerId: Qt.TimerId) -> bool:
    """
    Calls Qt's 'bool QEventDispatcherGlib::unregisterTimer(Qt::TimerId
    timerId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qeventdispatcherglib.html#unregisterTimer

    Parameters
    ----------

    timerId : Qt.TimerId
      Passed on as its number.
    """
    #  bool QEventDispatcherGlib::unregisterTimer(Qt::TimerId timerId)
    return self.uglySide.call(
        'ritual_ZN20QEventDispatcherGlib15unregisterTimerEN2Qt7TimerIdE',
        timerId.value,
    )

  @overload(QObject)
  @overload(NoneType)
  def unregisterTimers(self, object: Optional[QObject]) -> bool:
    """
    Calls Qt's 'bool QEventDispatcherGlib::unregisterTimers(QObject
    *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qeventdispatcherglib.html#unregisterTimers

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QEventDispatcherGlib::unregisterTimers(QObject *object)
    return self.uglySide.call(
        'ritual_ZN20QEventDispatcherGlib16unregisterTimersEP7QObject',
        self._addressOf(object, 'QObject'),
    )

  def wakeUp(self) -> None:
    """
    Calls Qt's 'void QEventDispatcherGlib::wakeUp()'.

    Qt's own words: https://doc.qt.io/qt-6/qeventdispatcherglib.html#wakeUp
    """
    #  void QEventDispatcherGlib::wakeUp()
    self.uglySide.call('ritual_ZN20QEventDispatcherGlib6wakeUpEv')

  def interrupt(self) -> None:
    """
    Calls Qt's 'void QEventDispatcherGlib::interrupt()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qeventdispatcherglib.html#interrupt
    """
    #  void QEventDispatcherGlib::interrupt()
    self.uglySide.call('ritual_ZN20QEventDispatcherGlib9interruptEv')
