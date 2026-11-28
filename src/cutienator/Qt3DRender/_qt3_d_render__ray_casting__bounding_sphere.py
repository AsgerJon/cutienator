"""
Qt3DRender::RayCasting::BoundingSphere binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/boundingsphere_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DRender::RayCasting::BoundingSphere to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtGui import QVector3D


class BoundingSphere(Qt3DRender.RayCasting.QBoundingVolume):
  """
  The cute side of Qt's Qt3DRender::RayCasting::BoundingSphere: a plain
  Python object standing in front of one C++
  Qt3DRender::RayCasting::BoundingSphere.

  It is built on the cute 'Qt3DRender::RayCasting::QBoundingVolume', as Qt's
  Qt3DRender::RayCasting::BoundingSphere is built on Qt's
  Qt3DRender::RayCasting::QBoundingVolume, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::RayCasting::BoundingSphere that has a
  ritual and that Python can call so far, 2 names in all: 'center', 'radius'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DRender::RayCasting::BoundingSphere::~BoundingSphere()': the
    destructor: Python never removes a C++
    Qt3DRender::RayCasting::BoundingSphere.

  What to expect
  --------------

  - The C++ Qt3DRender::RayCasting::BoundingSphere is created at the first
    use, not by 'Qt3DRender::RayCasting::BoundingSphere(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::RayCasting::BoundingSphere.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::RayCasting::BoundingSphere'

  #  A C++ Qt3DRender::RayCasting::BoundingSphere Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_RayCasting_BoundingSphere'

  #  The functions Qt calls itself that
  #  Qt3DRender::RayCasting::BoundingSphere is the first to declare. A class
  #  of a program built on it can write one anew, and Qt then calls that. For
  #  each name: the key C++ knows the function by, what it gives, and what it
  #  takes.
  __virtual_functions__ = {
      'center': (
          ('_ZNK10Qt3DRender10RayCasting14BoundingSphere6centerEv',
           ('address', 'value', 'QtGui:QVector3D'),
           ()),
      ),
      'radius': (
          ('_ZNK10Qt3DRender10RayCasting14BoundingSphere6radiusEv',
           ('float', 'number', ''),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def center(self) -> QVector3D:
    """
    Calls Qt's 'Vector3D Qt3DRender::RayCasting::BoundingSphere::center()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-raycasting-boundingsphere.html#center

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  Vector3D Qt3DRender::RayCasting::BoundingSphere::center() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender10RayCasting14BoundingSphere6centerEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def radius(self) -> float:
    """
    Calls Qt's 'float Qt3DRender::RayCasting::BoundingSphere::radius()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-raycasting-boundingsphere.html#radius
    """
    #  float Qt3DRender::RayCasting::BoundingSphere::radius() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender10RayCasting14BoundingSphere6radiusEv',
    )

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
    'Qt3DRender::RayCasting::BoundingSphere::BoundingSphere()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-raycasting-boundingsphere.html
    """
    #  Qt3DRender::RayCasting::BoundingSphere::BoundingSphere()
    self._noteCreation(BoundingSphere, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender10RayCasting14BoundingSphereC1Ev',
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
