"""
QPanGesturePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qgesture_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QPanGesturePrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from . import QGesturePrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QPanGesture


class QPanGesturePrivate(QGesturePrivate):
  """
  The cute side of Qt's QPanGesturePrivate: a plain Python object standing in
  front of one C++ QPanGesturePrivate.

  It is built on the cute 'QGesturePrivate', as Qt's QPanGesturePrivate is
  built on Qt's QGesturePrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPanGesturePrivate that has a ritual and that Python
  can call so far, 5 names in all: 'q_func', 'horizontalVelocity',
  'setHorizontalVelocity', 'verticalVelocity', 'setVerticalVelocity'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QPanGesture *QPanGesturePrivate::q_func() const': takes in
    Python what 'QPanGesture *QPanGesturePrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ QPanGesturePrivate is created at the first use, not by
    'QPanGesturePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPanGesturePrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPanGesturePrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def horizontalVelocity(self) -> float:
    """
    Calls Qt's 'qreal QPanGesturePrivate::horizontalVelocity() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpangestureprivate.html#horizontalVelocity
    """
    #  qreal QPanGesturePrivate::horizontalVelocity() const
    return self.uglySide.call(
        'ritual_ZNK18QPanGesturePrivate18horizontalVelocityEv',
    )

  def verticalVelocity(self) -> float:
    """
    Calls Qt's 'qreal QPanGesturePrivate::verticalVelocity() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpangestureprivate.html#verticalVelocity
    """
    #  qreal QPanGesturePrivate::verticalVelocity() const
    return self.uglySide.call(
        'ritual_ZNK18QPanGesturePrivate16verticalVelocityEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setHorizontalVelocity(self, value: float) -> None:
    """
    Calls Qt's 'void QPanGesturePrivate::setHorizontalVelocity(qreal value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpangestureprivate.html#setHorizontalVelocity

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void QPanGesturePrivate::setHorizontalVelocity(qreal value)
    self.uglySide.call(
        'ritual_ZN18QPanGesturePrivate21setHorizontalVelocityEd', value,
    )

  @overload(float)
  def setVerticalVelocity(self, value: float) -> None:
    """
    Calls Qt's 'void QPanGesturePrivate::setVerticalVelocity(qreal value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpangestureprivate.html#setVerticalVelocity

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void QPanGesturePrivate::setVerticalVelocity(qreal value)
    self.uglySide.call(
        'ritual_ZN18QPanGesturePrivate19setVerticalVelocityEd', value,
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
    'QPanGesturePrivate::QPanGesturePrivate()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpangestureprivate.html#QPanGesturePrivate
    """
    #  QPanGesturePrivate::QPanGesturePrivate()
    self._noteCreation(QPanGesturePrivate, lambda: Rituals.call(
        'ritual_ZN18QPanGesturePrivateC1Ev',
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

  def q_func(self) -> Optional[QPanGesture]:
    """
    Calls Qt's 'QPanGesture *QPanGesturePrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qpangestureprivate.html#q_func

    Returns
    -------

    Optional[QPanGesture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPanGesture *QPanGesturePrivate::q_func()
    address = self.uglySide.call('ritual_ZN18QPanGesturePrivate6q_funcEv')
    from . import QPanGesture
    return QPanGesture._cuteAt(address)
