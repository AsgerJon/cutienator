"""
QQuickGeoCoordinateAnimationPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPositioningQuick/6.12.0/QtPositioningQuick/private/qquickgeocoordinateanimation_p_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickGeoCoordinateAnimationPrivate to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from ..QtQuick import QQuickPropertyAnimationPrivate
from . import QQuickGeoCoordinateAnimation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional


class QQuickGeoCoordinateAnimationPrivate(QQuickPropertyAnimationPrivate):
  """
  The cute side of Qt's QQuickGeoCoordinateAnimationPrivate: a plain Python
  object standing in front of one C++ QQuickGeoCoordinateAnimationPrivate.

  It is built on the cute 'QQuickPropertyAnimationPrivate', as Qt's
  QQuickGeoCoordinateAnimationPrivate is built on Qt's
  QQuickPropertyAnimationPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickGeoCoordinateAnimationPrivate that has a
  ritual and that Python can call so far, 4 names in all: 'q_func',
  'setDirection', 'directionChanged', '_qt_property_m_direction_offset'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickGeoCoordinateAnimation
    *QQuickGeoCoordinateAnimationPrivate::q_func() const': takes in Python
    what 'QQuickGeoCoordinateAnimation
    *QQuickGeoCoordinateAnimationPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ QQuickGeoCoordinateAnimationPrivate is created at the first use,
    not by 'QQuickGeoCoordinateAnimationPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickGeoCoordinateAnimationPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def _qt_property_m_direction_offset() -> int:
    """
    Calls Qt's 'size_t
    QQuickGeoCoordinateAnimationPrivate::_qt_property_m_direction_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgeocoordinateanimationprivate.html
    """
    #  size_t QQuickGeoCoordinateAnimationPrivate::
    #      _qt_property_m_direction_offset()
    return Rituals.call(
        'ritual_ZN35QQuickGeoCoordinateAnimationPrivate31_qt_property_m_dir'
        'ection_offsetEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickGeoCoordinateAnimationPrivate'

  #  A C++ QQuickGeoCoordinateAnimationPrivate Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickGeoCoordinateAnimationPrivate'

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

  @overload(QQuickGeoCoordinateAnimation.Direction)
  def setDirection(
      self,
      direction: QQuickGeoCoordinateAnimation.Direction,
  ) -> None:
    """
    Calls Qt's 'void QQuickGeoCoordinateAnimationPrivate::setDirection(
    QQuickGeoCoordinateAnimation::Direction direction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgeocoordinateanimationprivate.html

    Parameters
    ----------

    direction : QQuickGeoCoordinateAnimation.Direction
      Passed on as its number.
    """
    #  void QQuickGeoCoordinateAnimationPrivate::setDirection(
    #      QQuickGeoCoordinateAnimation::Direction direction)
    self.uglySide.call(
        'ritual_ZN35QQuickGeoCoordinateAnimationPrivate12setDirectionEN28QQ'
        'uickGeoCoordinateAnimation9DirectionE',
        direction.value,
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

  def q_func(self) -> Optional[QQuickGeoCoordinateAnimation]:
    """
    Calls Qt's 'QQuickGeoCoordinateAnimation
    *QQuickGeoCoordinateAnimationPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgeocoordinateanimationprivate.html#q_func

    Returns
    -------

    Optional[QQuickGeoCoordinateAnimation]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickGeoCoordinateAnimation
    #      *QQuickGeoCoordinateAnimationPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN35QQuickGeoCoordinateAnimationPrivate6q_funcEv',
    )
    return QQuickGeoCoordinateAnimation._cuteAt(address)

  def directionChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuickGeoCoordinateAnimationPrivate::directionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgeocoordinateanimationprivate.html
    """
    #  void QQuickGeoCoordinateAnimationPrivate::directionChanged()
    self.uglySide.call(
        'ritual_ZN35QQuickGeoCoordinateAnimationPrivate16directionChangedEv',
    )
