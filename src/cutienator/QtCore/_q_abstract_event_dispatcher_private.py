"""
QAbstractEventDispatcherPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qabstracteventdispatcher_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QAbstractEventDispatcherPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import Qt, QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QAbstractEventDispatcher
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractEventDispatcher = WAIT['QAbstractEventDispatcher']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractEventDispatcherPrivate(QObjectPrivate):
  """
  The cute side of Qt's QAbstractEventDispatcherPrivate: a plain Python
  object standing in front of one C++ QAbstractEventDispatcherPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's
  QAbstractEventDispatcherPrivate is built on Qt's QObjectPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstractEventDispatcherPrivate that has a ritual
  and that Python can call so far, 4 names in all: 'q_func',
  'allocateTimerId', 'releaseTimerId', 'get'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QAbstractEventDispatcher
    *QAbstractEventDispatcherPrivate::q_func() const': takes in Python what
    'QAbstractEventDispatcher *QAbstractEventDispatcherPrivate::q_func()'
    takes.
  - Qt's
    'QAbstractEventDispatcherPrivate::~QAbstractEventDispatcherPrivate()':
    the destructor: Python never removes a C++
    QAbstractEventDispatcherPrivate.
  - Qt's 'const QAbstractEventDispatcherPrivate
    *QAbstractEventDispatcherPrivate::get(const QAbstractEventDispatcher
    *o)': takes in Python what 'QAbstractEventDispatcherPrivate
    *QAbstractEventDispatcherPrivate::get(QAbstractEventDispatcher *o)'
    takes.

  What to expect
  --------------

  - The C++ QAbstractEventDispatcherPrivate is created at the first use, not
    by 'QAbstractEventDispatcherPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractEventDispatcherPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def allocateTimerId() -> Qt.TimerId:
    """
    Calls Qt's 'Qt::TimerId
    QAbstractEventDispatcherPrivate::allocateTimerId()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracteventdispatcherprivate.html

    Returns
    -------

    Qt.TimerId
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.TimerId(number)'
      gives.
    """
    #  Qt::TimerId QAbstractEventDispatcherPrivate::allocateTimerId()
    return Qt.TimerId(Rituals.call(
        'ritual_ZN31QAbstractEventDispatcherPrivate15allocateTimerIdEv',
    ))

  @staticmethod
  @overload(int)
  def releaseTimerId(id: int) -> None:
    """
    Calls Qt's 'void QAbstractEventDispatcherPrivate::releaseTimerId(int
    id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracteventdispatcherprivate.html

    Parameters
    ----------

    id : int
      Passed on as it is.
    """
    #  void QAbstractEventDispatcherPrivate::releaseTimerId(int id)
    Rituals.call(
        'ritual_ZN31QAbstractEventDispatcherPrivate14releaseTimerIdEi', id,
    )

  @staticmethod
  @overload(Qt.TimerId)
  def releaseTimerId(id: Qt.TimerId) -> None:
    """
    Calls Qt's 'void
    QAbstractEventDispatcherPrivate::releaseTimerId(Qt::TimerId id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracteventdispatcherprivate.html

    Parameters
    ----------

    id : Qt.TimerId
      Passed on as its number.
    """
    #  void QAbstractEventDispatcherPrivate::releaseTimerId(Qt::TimerId id)
    Rituals.call(
        'ritual_ZN31QAbstractEventDispatcherPrivate14releaseTimerIdEN2Qt7Ti'
        'merIdE',
        id.value,
    )

  @staticmethod
  @overload(QAbstractEventDispatcher)
  @overload(NoneType)
  def get(
      o: Optional[QAbstractEventDispatcher],
  ) -> Optional[QAbstractEventDispatcherPrivate]:
    """
    Calls Qt's 'QAbstractEventDispatcherPrivate
    *QAbstractEventDispatcherPrivate::get(QAbstractEventDispatcher *o)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracteventdispatcherprivate.html#get

    Parameters
    ----------

    o : Optional[QAbstractEventDispatcher]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QAbstractEventDispatcherPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractEventDispatcherPrivate
    #      *QAbstractEventDispatcherPrivate::get(QAbstractEventDispatcher *o)
    address = Rituals.call(
        'ritual_ZN31QAbstractEventDispatcherPrivate3getEP24QAbstractEventDi'
        'spatcher',
        CuteMixin._addressOf(o),
    )
    return QAbstractEventDispatcherPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractEventDispatcherPrivate'

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QAbstractEventDispatcherPrivate::QAbstractEventDispatcherPrivate()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracteventdispatcherprivate.html
    """
    #  QAbstractEventDispatcherPrivate::QAbstractEventDispatcherPrivate()
    self._noteCreation(QAbstractEventDispatcherPrivate, lambda: Rituals.call(
        'ritual_ZN31QAbstractEventDispatcherPrivateC1Ev',
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

  def q_func(self) -> Optional[QAbstractEventDispatcher]:
    """
    Calls Qt's 'QAbstractEventDispatcher
    *QAbstractEventDispatcherPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracteventdispatcherprivate.html#q_func

    Returns
    -------

    Optional[QAbstractEventDispatcher]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractEventDispatcher *QAbstractEventDispatcherPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN31QAbstractEventDispatcherPrivate6q_funcEv',
    )
    from . import QAbstractEventDispatcher
    return QAbstractEventDispatcher._cuteAt(address)
