"""
QFutureWatcherBasePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qfuturewatcher_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QFutureWatcherBasePrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QFutureCallOutInterface, QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QFutureCallOutEvent, QFutureWatcherBase
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QFutureCallOutEvent = WAIT['QFutureCallOutEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QFutureWatcherBasePrivate(QObjectPrivate, QFutureCallOutInterface):
  """
  The cute side of Qt's QFutureWatcherBasePrivate: a plain Python object
  standing in front of one C++ QFutureWatcherBasePrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QFutureWatcherBasePrivate
  is built on Qt's QObjectPrivate, and has everything that class has. It is
  built on the cute 'QFutureCallOutInterface' as well, as Qt's
  QFutureWatcherBasePrivate is built on Qt's QFutureCallOutInterface too, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QFutureWatcherBasePrivate that has a ritual and that
  Python can call so far, 3 names in all: 'q_func',
  'callOutInterfaceDisconnected', 'sendCallOutEvent'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QFutureWatcherBase *QFutureWatcherBasePrivate::q_func()
    const': takes in Python what 'QFutureWatcherBase
    *QFutureWatcherBasePrivate::q_func()' takes.
  - Qt's 'void QFutureWatcherBasePrivate::postCallOutEvent(const
    QFutureCallOutEvent &callOutEvent)': takes a type Python has no way to
    hand over yet.

  What has no ritual
  ------------------

  1 of the 6 functions Qt declares: 1 leans on 'non-virtual thunk to
  QFutureWatcherBasePrivate.

  What to expect
  --------------

  - The C++ QFutureWatcherBasePrivate is created at the first use, not by
    'QFutureWatcherBasePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QFutureWatcherBasePrivate.
  - Each name of Qt's QFutureWatcherBasePrivate that has no cute function
    yet, '__init__', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QFutureWatcherBasePrivate'

  #  Qt's QFutureWatcherBasePrivate is built on more than one class. The part
  #  of a C++ QFutureWatcherBasePrivate that belongs to a class after the
  #  first begins somewhere inside the object, and the ritual named for that
  #  class gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QFutureCallOutInterface':
          'ritual_cast_QFutureWatcherBasePrivate_QFutureCallOutInterface',
  }

  #  A C++ QFutureWatcherBasePrivate Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QFutureWatcherBasePrivate'

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
    Qt's 'QFutureWatcherBasePrivate::QFutureWatcherBasePrivate()': leans on
    'non-virtual thunk to
    QFutureWatcherBasePrivate::postCallOutEvent(QFutureCallOutEvent const&)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QFutureWatcherBasePrivate.__init__' has no cute function yet. "
        "Qt's 'QFutureWatcherBasePrivate::QFutureWatcherBasePrivate()': "
        "leans on 'non-virtual thunk to "
        "QFutureWatcherBasePrivate::postCallOutEvent(QFutureCallOutEvent "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

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

  def q_func(self) -> Optional[QFutureWatcherBase]:
    """
    Calls Qt's 'QFutureWatcherBase *QFutureWatcherBasePrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfuturewatcherbaseprivate.html#q_func

    Returns
    -------

    Optional[QFutureWatcherBase]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QFutureWatcherBase *QFutureWatcherBasePrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN25QFutureWatcherBasePrivate6q_funcEv',
    )
    from . import QFutureWatcherBase
    return QFutureWatcherBase._cuteAt(address)

  def callOutInterfaceDisconnected(self) -> None:
    """
    Calls Qt's 'void
    QFutureWatcherBasePrivate::callOutInterfaceDisconnected()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfuturewatcherbaseprivate.html
    """
    #  void QFutureWatcherBasePrivate::callOutInterfaceDisconnected()
    ritual = (
        'ritual_ZN25QFutureWatcherBasePrivate28callOutInterfaceDisconnected'
        'Ev')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QFutureWatcherBasePrivate28callOutInterfaceDiscon'
          'nectedEv')
    self.uglySide.call(ritual)

  @overload(QFutureCallOutEvent)
  @overload(NoneType)
  def sendCallOutEvent(self, event: Optional[QFutureCallOutEvent]) -> None:
    """
    Calls Qt's 'void
    QFutureWatcherBasePrivate::sendCallOutEvent(QFutureCallOutEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfuturewatcherbaseprivate.html#sendCallOutEvent

    Parameters
    ----------

    event : Optional[QFutureCallOutEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QFutureWatcherBasePrivate::sendCallOutEvent(QFutureCallOutEvent
    #      *event)
    self.uglySide.call(
        'ritual_ZN25QFutureWatcherBasePrivate16sendCallOutEventEP19QFutureC'
        'allOutEvent',
        self._addressOf(event),
    )
