"""
QSwipeGesturePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qgesture_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QSwipeGesturePrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum
from ..occult import Rituals
from . import QGesturePrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QSwipeGesture


class QSwipeGesturePrivate(QGesturePrivate):
  """
  The cute side of Qt's QSwipeGesturePrivate: a plain Python object standing
  in front of one C++ QSwipeGesturePrivate.

  It is built on the cute 'QGesturePrivate', as Qt's QSwipeGesturePrivate is
  built on Qt's QGesturePrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSwipeGesturePrivate that has a ritual and that
  Python can call so far, 3 names in all: 'q_func', 'velocity',
  'setVelocity'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QSwipeGesture *QSwipeGesturePrivate::q_func() const': takes
    in Python what 'QSwipeGesture *QSwipeGesturePrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ QSwipeGesturePrivate is created at the first use, not by
    'QSwipeGesturePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSwipeGesturePrivate.
  """

  #  The enums Qt writes inside QSwipeGesturePrivate, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class State(CuteNum):
    """
    The enum 'QSwipeGesturePrivate::State' of Qt, with the 3 names Qt gives
    in it.
    """

    NoGesture = Kee[int](0)
    Started = Kee[int](1)
    ThreePointsReached = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSwipeGesturePrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def velocity(self) -> float:
    """
    Calls Qt's 'qreal QSwipeGesturePrivate::velocity() const'.

    Qt's own words: https://doc.qt.io/qt-6/qswipegestureprivate.html#velocity
    """
    #  qreal QSwipeGesturePrivate::velocity() const
    return self.uglySide.call('ritual_ZNK20QSwipeGesturePrivate8velocityEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setVelocity(self, value: float) -> None:
    """
    Calls Qt's 'void QSwipeGesturePrivate::setVelocity(qreal value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qswipegestureprivate.html#setVelocity

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void QSwipeGesturePrivate::setVelocity(qreal value)
    self.uglySide.call(
        'ritual_ZN20QSwipeGesturePrivate11setVelocityEd', value,
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
    'QSwipeGesturePrivate::QSwipeGesturePrivate()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qswipegestureprivate.html#QSwipeGesturePrivate
    """
    #  QSwipeGesturePrivate::QSwipeGesturePrivate()
    self._noteCreation(QSwipeGesturePrivate, lambda: Rituals.call(
        'ritual_ZN20QSwipeGesturePrivateC1Ev',
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

  def q_func(self) -> Optional[QSwipeGesture]:
    """
    Calls Qt's 'QSwipeGesture *QSwipeGesturePrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qswipegestureprivate.html#q_func

    Returns
    -------

    Optional[QSwipeGesture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSwipeGesture *QSwipeGesturePrivate::q_func()
    address = self.uglySide.call('ritual_ZN20QSwipeGesturePrivate6q_funcEv')
    from . import QSwipeGesture
    return QSwipeGesture._cuteAt(address)
