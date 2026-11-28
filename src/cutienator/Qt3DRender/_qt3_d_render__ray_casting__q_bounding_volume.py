"""
Qt3DRender::RayCasting::QBoundingVolume binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/qboundingvolume_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DRender::RayCasting::QBoundingVolume to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QBoundingVolume(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DRender::RayCasting::QBoundingVolume: a plain
  Python object standing in front of one C++
  Qt3DRender::RayCasting::QBoundingVolume.

  What exists
  -----------

  Every function of Qt's Qt3DRender::RayCasting::QBoundingVolume that has a
  ritual and that Python can call so far, 2 names in all: 'id', 'type'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DRender::RayCasting::QBoundingVolume::~QBoundingVolume()': the
    destructor: Python never removes a C++
    Qt3DRender::RayCasting::QBoundingVolume.
  - Qt's 'bool Qt3DRender::RayCasting::QBoundingVolume::intersects(const
    QRay3D &ray, Vector3D *q, Vector3D *uvw) const': names 'Vector3D', which
    has no cute class yet.

  What to expect
  --------------

  - The C++ Qt3DRender::RayCasting::QBoundingVolume is created at the first
    use, not by 'Qt3DRender::RayCasting::QBoundingVolume(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::RayCasting::QBoundingVolume.
  - Each name of Qt's Qt3DRender::RayCasting::QBoundingVolume that has no
    cute function yet, 'intersects', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside Qt3DRender::RayCasting::QBoundingVolume, each
  #  a class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class Type(CuteNum):
    """
    The enum 'Qt3DRender::RayCasting::QBoundingVolume::Type' of Qt, with the
    2 names Qt gives in it.
    """

    Sphere = Kee[int](0)
    Triangle = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::RayCasting::QBoundingVolume'

  #  A C++ Qt3DRender::RayCasting::QBoundingVolume Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_RayCasting_QBoundingVolume'

  #  The functions Qt calls itself that
  #  Qt3DRender::RayCasting::QBoundingVolume is the first to declare and that
  #  cannot be handed to Python yet, each as Qt declares it. A class of a
  #  program that writes one of them anew is refused, since Qt would never
  #  call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'intersects': (
          'bool Qt3DRender::RayCasting::QBoundingVolume::intersects(const '
          'QRay3D &, Vector3D *, Vector3D *) const',
      ),
  }

  #  The functions Qt calls itself that
  #  Qt3DRender::RayCasting::QBoundingVolume is the first to declare. A class
  #  of a program built on it can write one anew, and Qt then calls that. For
  #  each name: the key C++ knows the function by, what it gives, and what it
  #  takes.
  __virtual_functions__ = {
      'id': (
          ('_ZNK10Qt3DRender10RayCasting15QBoundingVolume2idEv',
           ('address', 'value', 'Qt3DCore:Qt3DCore.QNodeId'),
           ()),
      ),
      'type': (
          ('_ZNK10Qt3DRender10RayCasting15QBoundingVolume4typeEv',
           ('int', 'enum',
            'Qt3DRender:Qt3DRender.RayCasting.QBoundingVolume.Type'),
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

  def id(self) -> Qt3DCore.QNodeId:
    """
    Calls Qt's 'Qt3DCore::QNodeId
    Qt3DRender::RayCasting::QBoundingVolume::id() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-raycasting-qboundingvolume.html#id

    Returns
    -------

    Qt3DCore.QNodeId
      A new cute Qt3DCore::QNodeId around the copy Qt gave back. Python owns
      it.
    """
    #  Qt3DCore::QNodeId Qt3DRender::RayCasting::QBoundingVolume::id() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender10RayCasting15QBoundingVolume2idEv',
    )
    return Qt3DCore.QNodeId._cuteOwning(address)

  def type(self) -> Type:
    """
    Calls Qt's 'Type Qt3DRender::RayCasting::QBoundingVolume::type() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-raycasting-qboundingvolume.html#type

    Returns
    -------

    Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Type(number)' gives.
    """
    #  Type Qt3DRender::RayCasting::QBoundingVolume::type() const
    return QBoundingVolume.Type(self.uglySide.call(
        'ritual_ZNK10Qt3DRender10RayCasting15QBoundingVolume4typeEv',
    ))

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
    'Qt3DRender::RayCasting::QBoundingVolume::QBoundingVolume()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-raycasting-qboundingvolume.html
    """
    #  Qt3DRender::RayCasting::QBoundingVolume::QBoundingVolume()
    self._noteCreation(QBoundingVolume, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender10RayCasting15QBoundingVolumeC1Ev',
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

  @staticmethod
  def intersects(*__, **_) -> Never:
    """
    Qt's 'bool Qt3DRender::RayCasting::QBoundingVolume::intersects(const
    QRay3D &ray, Vector3D *q, Vector3D *uvw) const': names 'Vector3D', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.RayCasting.QBoundingVolume.intersects' has no cute "
        "function yet. Qt's 'bool "
        "Qt3DRender::RayCasting::QBoundingVolume::intersects(const QRay3D "
        "&ray, Vector3D *q, Vector3D *uvw) const': names 'Vector3D', which "
        "has no cute class yet.")
