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
from . import Qt, QAbstractEventDispatcher, QEventLoop

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QDeadlineTimer, QMetaObject
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
  that Python can call so far, 4 names in all: 'metaObject', 'tr',
  'unregisterTimer', 'processEventsWithDeadline'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAbstractEventDispatcherV2::~QAbstractEventDispatcherV2()': the
    destructor: Python never removes a C++ QAbstractEventDispatcherV2.

  What has no ritual
  ------------------

  15 of the 20 functions Qt declares: 7 private; 5 takes or gives a type that
  cannot be passed yet; 1 a template; 1 the class is abstract, so C++ cannot
  make one; 1 protected.

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
  #  first to declare and that cannot be handed to Python yet, each as Qt
  #  declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'processEventsWithDeadline': (
          'bool '
          'QAbstractEventDispatcherV2::processEventsWithDeadline(QEventLoop'
          '::ProcessEventsFlags, QDeadlineTimer)',
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
    return self.uglySide.call(
        'ritual_ZN26QAbstractEventDispatcherV225processEventsWithDeadlineE6'
        'QFlagsIN10QEventLoop17ProcessEventsFlagEE14QDeadlineTimer',
        flags.value, self._valueOf(deadline),
    )
