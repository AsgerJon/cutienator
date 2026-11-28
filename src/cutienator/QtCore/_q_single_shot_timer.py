"""
QSingleShotTimer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qsingleshottimer_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QSingleShotTimer to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QMetaObject, QTimerEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QTimerEvent = WAIT['QTimerEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSingleShotTimer(QObject):
  """
  The cute side of Qt's QSingleShotTimer: a plain Python object standing in
  front of one C++ QSingleShotTimer.

  It is built on the cute 'QObject', as Qt's QSingleShotTimer is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSingleShotTimer that has a ritual and that Python
  can call so far, 3 names in all: 'metaObject', 'timeout', 'timerEvent'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QSingleShotTimer::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QSingleShotTimer::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QSingleShotTimer::~QSingleShotTimer()': the destructor: Python
    never removes a C++ QSingleShotTimer.
  - Qt's 'void QSingleShotTimer::startTimerForReceiver(Duration interval,
    Qt::TimerType timerType, const QObject *receiver)': takes a type Python
    has no way to hand over yet.

  What has no ritual
  ------------------

  6 of the 13 functions Qt declares: 4 leans on 'QSingleShotTimer; 2 not a
  gap.

  What to expect
  --------------

  - The C++ QSingleShotTimer is created at the first use, not by
    'QSingleShotTimer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSingleShotTimer.
  - Qt tells when it has removed the C++ QSingleShotTimer. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QSingleShotTimer that has no cute function yet,
    '__init__', 'startTimerForReceiver', 'timerFinished', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSingleShotTimer'

  #  A C++ QSingleShotTimer Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSingleShotTimer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QSingleShotTimer::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsingleshottimer.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSingleShotTimer::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QSingleShotTimer10metaObjectEv',
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
    - Qt's 'QSingleShotTimer::QSingleShotTimer(Duration interval,
      Qt::TimerType timerType, const QObject *r, const char *member)': leans
      on 'QSingleShotTimer::qt_metacall(QMetaObject::Call, int, void**)',
      which Qt's source does not mark for use from outside Qt and has no code
      for that could be taken.
    - Qt's 'QSingleShotTimer::QSingleShotTimer(Duration interval,
      Qt::TimerType timerType, const QObject *r, QtPrivate::QSlotObjectBase
      *slotObj)': leans on 'QSingleShotTimer::qt_metacall(QMetaObject::Call,
      int, void**)', which Qt's source does not mark for use from outside Qt
      and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QSingleShotTimer.__init__' has no cute function yet. Qt's "
        "'QSingleShotTimer::QSingleShotTimer(Duration interval, "
        "Qt::TimerType timerType, const QObject *r, const char *member)': "
        "leans on 'QSingleShotTimer::qt_metacall(QMetaObject::Call, int, "
        "void**)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken. Qt's "
        "'QSingleShotTimer::QSingleShotTimer(Duration interval, "
        "Qt::TimerType timerType, const QObject *r, "
        "QtPrivate::QSlotObjectBase *slotObj)': leans on "
        "'QSingleShotTimer::qt_metacall(QMetaObject::Call, int, void**)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

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

  def timeout(self) -> None:
    """
    Calls Qt's 'void QSingleShotTimer::timeout()'.

    Qt's own words: https://doc.qt.io/qt-6/qsingleshottimer.html#timeout
    """
    #  void QSingleShotTimer::timeout()
    self.uglySide.call('ritual_ZN16QSingleShotTimer7timeoutEv')

  @overload(QTimerEvent)
  @overload(NoneType)
  def timerEvent(self, a0: Optional[QTimerEvent]) -> None:
    """
    Calls Qt's 'void QSingleShotTimer::timerEvent(QTimerEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsingleshottimer.html#timerEvent

    Parameters
    ----------

    a0 : Optional[QTimerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSingleShotTimer::timerEvent(QTimerEvent *a0)
    self.uglySide.call(
        'ritual_ZN16QSingleShotTimer10timerEventEP11QTimerEvent',
        self._addressOf(a0),
    )

  @staticmethod
  def startTimerForReceiver(*__, **_) -> Never:
    """
    Qt's 'void QSingleShotTimer::startTimerForReceiver(Duration interval,
    Qt::TimerType timerType, const QObject *receiver)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSingleShotTimer.startTimerForReceiver' has no cute function yet. "
        "Qt's 'void QSingleShotTimer::startTimerForReceiver(Duration "
        "interval, Qt::TimerType timerType, const QObject *receiver)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def timerFinished(*__, **_) -> Never:
    """
    Qt's 'void QSingleShotTimer::timerFinished()': leans on
    'QSingleShotTimer::timeout()', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QSingleShotTimer.timerFinished' has no cute function yet. Qt's "
        "'void QSingleShotTimer::timerFinished()': leans on "
        "'QSingleShotTimer::timeout()', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")
