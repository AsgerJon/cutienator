"""
QEventDispatcherUNIXPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qeventdispatcher_unix_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QEventDispatcherUNIXPrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QAbstractEventDispatcherPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QEventDispatcherUNIX, QSocketNotifier
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSocketNotifier = WAIT['QSocketNotifier']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QEventDispatcherUNIXPrivate(QAbstractEventDispatcherPrivate):
  """
  The cute side of Qt's QEventDispatcherUNIXPrivate: a plain Python object
  standing in front of one C++ QEventDispatcherUNIXPrivate.

  It is built on the cute 'QAbstractEventDispatcherPrivate', as Qt's
  QEventDispatcherUNIXPrivate is built on Qt's
  QAbstractEventDispatcherPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QEventDispatcherUNIXPrivate that has a ritual and
  that Python can call so far, 5 names in all: 'q_func', 'activateTimers',
  'markPendingSocketNotifiers', 'activateSocketNotifiers',
  'setSocketNotifierPending'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QEventDispatcherUNIX *QEventDispatcherUNIXPrivate::q_func()
    const': takes in Python what 'QEventDispatcherUNIX
    *QEventDispatcherUNIXPrivate::q_func()' takes.
  - Qt's 'QEventDispatcherUNIXPrivate::~QEventDispatcherUNIXPrivate()': the
    destructor: Python never removes a C++ QEventDispatcherUNIXPrivate.

  What to expect
  --------------

  - The C++ QEventDispatcherUNIXPrivate is created at the first use, not by
    'QEventDispatcherUNIXPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QEventDispatcherUNIXPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QEventDispatcherUNIXPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSocketNotifier)
  @overload(NoneType)
  def setSocketNotifierPending(
      self,
      notifier: Optional[QSocketNotifier],
  ) -> None:
    """
    Calls Qt's 'void
    QEventDispatcherUNIXPrivate::setSocketNotifierPending(QSocketNotifier
    *notifier)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qeventdispatcherunixprivate.html

    Parameters
    ----------

    notifier : Optional[QSocketNotifier]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QEventDispatcherUNIXPrivate::setSocketNotifierPending(
    #      QSocketNotifier *notifier)
    self.uglySide.call(
        'ritual_ZN27QEventDispatcherUNIXPrivate24setSocketNotifierPendingEP'
        '15QSocketNotifier',
        self._addressOf(notifier),
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
    Notes what was given, for Qt's
    'QEventDispatcherUNIXPrivate::QEventDispatcherUNIXPrivate()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qeventdispatcherunixprivate.html
    """
    #  QEventDispatcherUNIXPrivate::QEventDispatcherUNIXPrivate()
    self._noteCreation(QEventDispatcherUNIXPrivate, lambda: Rituals.call(
        'ritual_ZN27QEventDispatcherUNIXPrivateC1Ev',
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

  def q_func(self) -> Optional[QEventDispatcherUNIX]:
    """
    Calls Qt's 'QEventDispatcherUNIX *QEventDispatcherUNIXPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qeventdispatcherunixprivate.html#q_func

    Returns
    -------

    Optional[QEventDispatcherUNIX]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QEventDispatcherUNIX *QEventDispatcherUNIXPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN27QEventDispatcherUNIXPrivate6q_funcEv',
    )
    from . import QEventDispatcherUNIX
    return QEventDispatcherUNIX._cuteAt(address)

  def activateTimers(self) -> int:
    """
    Calls Qt's 'int QEventDispatcherUNIXPrivate::activateTimers()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qeventdispatcherunixprivate.html#activateTimers
    """
    #  int QEventDispatcherUNIXPrivate::activateTimers()
    return self.uglySide.call(
        'ritual_ZN27QEventDispatcherUNIXPrivate14activateTimersEv',
    )

  def markPendingSocketNotifiers(self) -> None:
    """
    Calls Qt's 'void
    QEventDispatcherUNIXPrivate::markPendingSocketNotifiers()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qeventdispatcherunixprivate.html
    """
    #  void QEventDispatcherUNIXPrivate::markPendingSocketNotifiers()
    self.uglySide.call(
        'ritual_ZN27QEventDispatcherUNIXPrivate26markPendingSocketNotifiers'
        'Ev',
    )

  def activateSocketNotifiers(self) -> int:
    """
    Calls Qt's 'int QEventDispatcherUNIXPrivate::activateSocketNotifiers()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qeventdispatcherunixprivate.html
    """
    #  int QEventDispatcherUNIXPrivate::activateSocketNotifiers()
    return self.uglySide.call(
        'ritual_ZN27QEventDispatcherUNIXPrivate23activateSocketNotifiersEv',
    )
