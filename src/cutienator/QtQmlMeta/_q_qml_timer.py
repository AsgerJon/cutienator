"""
QQmlTimer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlMeta/6.12.0/QtQmlMeta/private/qqmltimer_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQmlTimer to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..QtQml import QQmlParserStatus

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlTimer(QObject, QQmlParserStatus):
  """
  The cute side of Qt's QQmlTimer: a plain Python object standing in front of
  one C++ QQmlTimer.

  It is built on the cute 'QObject', as Qt's QQmlTimer is built on Qt's
  QObject, and has everything that class has. It is built on the cute
  'QQmlParserStatus' as well, as Qt's QQmlTimer is built on Qt's
  QQmlParserStatus too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlTimer that has a ritual and that Python can call
  so far, 23 names in all: 'metaObject', 'tr', 'setInterval', 'interval',
  'isRunning', 'setRunning', 'isRepeating', 'setRepeating',
  'triggeredOnStart', 'setTriggeredOnStart', 'classBegin',
  'componentComplete', 'event', 'start', 'stop', 'restart', 'triggered',
  'runningChanged', 'intervalChanged', 'repeatChanged',
  'triggeredOnStartChanged', 'update', 'ticked'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlTimer::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQmlTimer::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQmlTimerPrivate *QQmlTimer::d_func()': gives 'QQmlTimerPrivate',
    which has no cute class yet.
  - Qt's 'const QQmlTimerPrivate *QQmlTimer::d_func() const': gives
    'QQmlTimerPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 30 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQmlTimer is created at the first use, not by 'QQmlTimer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlTimer.
  - Qt tells when it has removed the C++ QQmlTimer. Every call on the cute
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
    Calls Qt's 'QString QQmlTimer::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltimer.html#tr

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
    #  QString QQmlTimer::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN9QQmlTimer2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlTimer'

  #  Qt's QQmlTimer is built on more than one class. The part of a C++
  #  QQmlTimer that belongs to a class after the first begins somewhere
  #  inside the object, and the ritual named for that class gives where; see
  #  'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlParserStatus': 'ritual_cast_QQmlTimer_QQmlParserStatus',
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
    Calls Qt's 'const QMetaObject *QQmlTimer::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltimer.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlTimer::metaObject() const
    address = self.uglySide.call('ritual_ZNK9QQmlTimer10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def interval(self) -> int:
    """
    Calls Qt's 'int QQmlTimer::interval() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltimer.html#interval
    """
    #  int QQmlTimer::interval() const
    return self.uglySide.call('ritual_ZNK9QQmlTimer8intervalEv')

  def isRunning(self) -> bool:
    """
    Calls Qt's 'bool QQmlTimer::isRunning() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltimer.html#isRunning
    """
    #  bool QQmlTimer::isRunning() const
    return self.uglySide.call('ritual_ZNK9QQmlTimer9isRunningEv')

  def isRepeating(self) -> bool:
    """
    Calls Qt's 'bool QQmlTimer::isRepeating() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltimer.html#isRepeating
    """
    #  bool QQmlTimer::isRepeating() const
    return self.uglySide.call('ritual_ZNK9QQmlTimer11isRepeatingEv')

  def triggeredOnStart(self) -> bool:
    """
    Calls Qt's 'bool QQmlTimer::triggeredOnStart() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltimer.html#triggeredOnStart
    """
    #  bool QQmlTimer::triggeredOnStart() const
    return self.uglySide.call('ritual_ZNK9QQmlTimer16triggeredOnStartEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setInterval(self, interval: int) -> None:
    """
    Calls Qt's 'void QQmlTimer::setInterval(int interval)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltimer.html#setInterval

    Parameters
    ----------

    interval : int
      Passed on as it is.
    """
    #  void QQmlTimer::setInterval(int interval)
    self.uglySide.call('ritual_ZN9QQmlTimer11setIntervalEi', interval)

  @overload(bool)
  def setRunning(self, running: bool) -> None:
    """
    Calls Qt's 'void QQmlTimer::setRunning(bool running)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltimer.html#setRunning

    Parameters
    ----------

    running : bool
      Passed on as it is.
    """
    #  void QQmlTimer::setRunning(bool running)
    self.uglySide.call('ritual_ZN9QQmlTimer10setRunningEb', running)

  @overload(bool)
  def setRepeating(self, repeating: bool) -> None:
    """
    Calls Qt's 'void QQmlTimer::setRepeating(bool repeating)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltimer.html#setRepeating

    Parameters
    ----------

    repeating : bool
      Passed on as it is.
    """
    #  void QQmlTimer::setRepeating(bool repeating)
    self.uglySide.call('ritual_ZN9QQmlTimer12setRepeatingEb', repeating)

  @overload(bool)
  def setTriggeredOnStart(self, triggeredOnStart: bool) -> None:
    """
    Calls Qt's 'void QQmlTimer::setTriggeredOnStart(bool triggeredOnStart)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltimer.html#setTriggeredOnStart

    Parameters
    ----------

    triggeredOnStart : bool
      Passed on as it is.
    """
    #  void QQmlTimer::setTriggeredOnStart(bool triggeredOnStart)
    self.uglySide.call(
        'ritual_ZN9QQmlTimer19setTriggeredOnStartEb', triggeredOnStart,
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QQmlTimer::QQmlTimer(QObject *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmltimer.html#QQmlTimer

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlTimer::QQmlTimer(QObject *parent)
    self._noteCreation(QQmlTimer, lambda: Rituals.call(
        'ritual_ZN9QQmlTimerC1EP7QObject',
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

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QQmlTimer::classBegin()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltimer.html#classBegin
    """
    #  void QQmlTimer::classBegin()
    ritual = 'ritual_ZN9QQmlTimer10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9QQmlTimer10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQmlTimer::componentComplete()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltimer.html#componentComplete
    """
    #  void QQmlTimer::componentComplete()
    ritual = 'ritual_ZN9QQmlTimer17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9QQmlTimer17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(QEvent)
  @overload(NoneType)
  def event(self, a0: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QQmlTimer::event(QEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltimer.html#event

    Parameters
    ----------

    a0 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlTimer::event(QEvent *a0)
    ritual = 'ritual_ZN9QQmlTimer5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9QQmlTimer5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(a0))

  def start(self) -> None:
    """
    Calls Qt's 'void QQmlTimer::start()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltimer.html#start
    """
    #  void QQmlTimer::start()
    self.uglySide.call('ritual_ZN9QQmlTimer5startEv')

  def stop(self) -> None:
    """
    Calls Qt's 'void QQmlTimer::stop()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltimer.html#stop
    """
    #  void QQmlTimer::stop()
    self.uglySide.call('ritual_ZN9QQmlTimer4stopEv')

  def restart(self) -> None:
    """
    Calls Qt's 'void QQmlTimer::restart()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltimer.html#restart
    """
    #  void QQmlTimer::restart()
    self.uglySide.call('ritual_ZN9QQmlTimer7restartEv')

  def triggered(self) -> None:
    """
    Calls Qt's 'void QQmlTimer::triggered()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltimer.html#triggered
    """
    #  void QQmlTimer::triggered()
    self.uglySide.call('ritual_ZN9QQmlTimer9triggeredEv')

  def runningChanged(self) -> None:
    """
    Calls Qt's 'void QQmlTimer::runningChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltimer.html#runningChanged
    """
    #  void QQmlTimer::runningChanged()
    self.uglySide.call('ritual_ZN9QQmlTimer14runningChangedEv')

  def intervalChanged(self) -> None:
    """
    Calls Qt's 'void QQmlTimer::intervalChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltimer.html#intervalChanged
    """
    #  void QQmlTimer::intervalChanged()
    self.uglySide.call('ritual_ZN9QQmlTimer15intervalChangedEv')

  def repeatChanged(self) -> None:
    """
    Calls Qt's 'void QQmlTimer::repeatChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltimer.html#repeatChanged
    """
    #  void QQmlTimer::repeatChanged()
    self.uglySide.call('ritual_ZN9QQmlTimer13repeatChangedEv')

  def triggeredOnStartChanged(self) -> None:
    """
    Calls Qt's 'void QQmlTimer::triggeredOnStartChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltimer.html#triggeredOnStartChanged
    """
    #  void QQmlTimer::triggeredOnStartChanged()
    self.uglySide.call('ritual_ZN9QQmlTimer23triggeredOnStartChangedEv')

  def update(self) -> None:
    """
    Calls Qt's 'void QQmlTimer::update()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltimer.html#update
    """
    #  void QQmlTimer::update()
    self.uglySide.call('ritual_ZN9QQmlTimer6updateEv')

  def ticked(self) -> None:
    """
    Calls Qt's 'void QQmlTimer::ticked()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltimer.html#ticked
    """
    #  void QQmlTimer::ticked()
    self.uglySide.call('ritual_ZN9QQmlTimer6tickedEv')
