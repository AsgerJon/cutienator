"""
Qt3DExtras::QCylinderGeometry binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DExtras/qcylindergeometry.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DExtras

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCylinderGeometry(Qt3DCore.QGeometry):
  """
  The cute side of Qt's Qt3DExtras::QCylinderGeometry: a plain Python object
  standing in front of one C++ Qt3DExtras::QCylinderGeometry.

  It is built on the cute 'Qt3DCore::QGeometry', as Qt's
  Qt3DExtras::QCylinderGeometry is built on Qt's Qt3DCore::QGeometry, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DExtras::QCylinderGeometry that has a ritual and
  that Python can call so far, 21 names in all: 'metaObject', 'tr',
  'updateVertices', 'updateIndices', 'rings', 'slices', 'radius', 'length',
  'positionAttribute', 'normalAttribute', 'texCoordAttribute',
  'indexAttribute', 'setRings', 'setSlices', 'setRadius', 'setLength',
  'radiusChanged', 'ringsChanged', 'slicesChanged', 'lengthChanged',
  'd_func'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DExtras::QCylinderGeometry::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int Qt3DExtras::QCylinderGeometry::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DExtras::QCylinderGeometry::~QCylinderGeometry()': the
    destructor: Python never removes a C++ Qt3DExtras::QCylinderGeometry.
  - Qt's 'Qt3DExtras::QCylinderGeometry::QCylinderGeometry(
    QCylinderGeometryPrivate &dd, QNode *parent)': takes a type Python has no
    way to hand over yet.
  - Qt's 'const QCylinderGeometryPrivate
    *Qt3DExtras::QCylinderGeometry::d_func() const': takes in Python what
    'QCylinderGeometryPrivate *Qt3DExtras::QCylinderGeometry::d_func()'
    takes.

  What has no ritual
  ------------------

  2 of the 29 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DExtras::QCylinderGeometry is created at the first use, not by
    'Qt3DExtras::QCylinderGeometry(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DExtras::QCylinderGeometry.
  - Qt tells when it has removed the C++ Qt3DExtras::QCylinderGeometry. Every
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
    Calls Qt's 'QString Qt3DExtras::QCylinderGeometry::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qcylindergeometry.html#tr

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
    #  QString Qt3DExtras::QCylinderGeometry::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN10Qt3DExtras17QCylinderGeometry2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DExtras::QCylinderGeometry'

  #  A C++ Qt3DExtras::QCylinderGeometry Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DExtras_QCylinderGeometry'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *Qt3DExtras::QCylinderGeometry::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qcylindergeometry.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DExtras::QCylinderGeometry::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras17QCylinderGeometry10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def rings(self) -> int:
    """
    Calls Qt's 'int Qt3DExtras::QCylinderGeometry::rings() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qcylindergeometry.html#rings
    """
    #  int Qt3DExtras::QCylinderGeometry::rings() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras17QCylinderGeometry5ringsEv',
    )

  def slices(self) -> int:
    """
    Calls Qt's 'int Qt3DExtras::QCylinderGeometry::slices() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qcylindergeometry.html#slices
    """
    #  int Qt3DExtras::QCylinderGeometry::slices() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras17QCylinderGeometry6slicesEv',
    )

  def radius(self) -> float:
    """
    Calls Qt's 'float Qt3DExtras::QCylinderGeometry::radius() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qcylindergeometry.html#radius
    """
    #  float Qt3DExtras::QCylinderGeometry::radius() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras17QCylinderGeometry6radiusEv',
    )

  def length(self) -> float:
    """
    Calls Qt's 'float Qt3DExtras::QCylinderGeometry::length() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qcylindergeometry.html#length
    """
    #  float Qt3DExtras::QCylinderGeometry::length() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras17QCylinderGeometry6lengthEv',
    )

  def positionAttribute(self) -> Optional[Qt3DCore.QAttribute]:
    """
    Calls Qt's 'Qt3DCore::QAttribute
    *Qt3DExtras::QCylinderGeometry::positionAttribute() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qcylindergeometry.html

    Returns
    -------

    Optional[Qt3DCore.QAttribute]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DCore::QAttribute
    #      *Qt3DExtras::QCylinderGeometry::positionAttribute() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras17QCylinderGeometry17positionAttributeEv',
    )
    return Qt3DCore.QAttribute._cuteAt(address)

  def normalAttribute(self) -> Optional[Qt3DCore.QAttribute]:
    """
    Calls Qt's 'Qt3DCore::QAttribute
    *Qt3DExtras::QCylinderGeometry::normalAttribute() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qcylindergeometry.html#normalAttribute

    Returns
    -------

    Optional[Qt3DCore.QAttribute]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DCore::QAttribute *Qt3DExtras::QCylinderGeometry::normalAttribute()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras17QCylinderGeometry15normalAttributeEv',
    )
    return Qt3DCore.QAttribute._cuteAt(address)

  def texCoordAttribute(self) -> Optional[Qt3DCore.QAttribute]:
    """
    Calls Qt's 'Qt3DCore::QAttribute
    *Qt3DExtras::QCylinderGeometry::texCoordAttribute() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qcylindergeometry.html

    Returns
    -------

    Optional[Qt3DCore.QAttribute]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DCore::QAttribute
    #      *Qt3DExtras::QCylinderGeometry::texCoordAttribute() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras17QCylinderGeometry17texCoordAttributeEv',
    )
    return Qt3DCore.QAttribute._cuteAt(address)

  def indexAttribute(self) -> Optional[Qt3DCore.QAttribute]:
    """
    Calls Qt's 'Qt3DCore::QAttribute
    *Qt3DExtras::QCylinderGeometry::indexAttribute() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qcylindergeometry.html#indexAttribute

    Returns
    -------

    Optional[Qt3DCore.QAttribute]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DCore::QAttribute *Qt3DExtras::QCylinderGeometry::indexAttribute()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras17QCylinderGeometry14indexAttributeEv',
    )
    return Qt3DCore.QAttribute._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setRings(self, rings: int) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QCylinderGeometry::setRings(int rings)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qcylindergeometry.html#setRings

    Parameters
    ----------

    rings : int
      Passed on as it is.
    """
    #  void Qt3DExtras::QCylinderGeometry::setRings(int rings)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras17QCylinderGeometry8setRingsEi', rings,
    )

  @overload(int)
  def setSlices(self, slices: int) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QCylinderGeometry::setSlices(int slices)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qcylindergeometry.html#setSlices

    Parameters
    ----------

    slices : int
      Passed on as it is.
    """
    #  void Qt3DExtras::QCylinderGeometry::setSlices(int slices)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras17QCylinderGeometry9setSlicesEi', slices,
    )

  @overload(float)
  def setRadius(self, radius: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QCylinderGeometry::setRadius(float radius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qcylindergeometry.html#setRadius

    Parameters
    ----------

    radius : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QCylinderGeometry::setRadius(float radius)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras17QCylinderGeometry9setRadiusEf', radius,
    )

  @overload(float)
  def setLength(self, length: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QCylinderGeometry::setLength(float length)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qcylindergeometry.html#setLength

    Parameters
    ----------

    length : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QCylinderGeometry::setLength(float length)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras17QCylinderGeometry9setLengthEf', length,
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
  @overload(Qt3DCore.QNode)
  @overload(NoneType)
  def __init__(self, parent: Optional[Qt3DCore.QNode] = None) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DExtras::QCylinderGeometry::QCylinderGeometry(QNode *parent)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qcylindergeometry.html

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DExtras::QCylinderGeometry::QCylinderGeometry(QNode *parent)
    self._noteCreation(QCylinderGeometry, lambda: Rituals.call(
        'ritual_ZN10Qt3DExtras17QCylinderGeometryC1EPN8Qt3DCore5QNodeE',
        self._addressOf(parent),
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

  def updateVertices(self) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QCylinderGeometry::updateVertices()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qcylindergeometry.html#updateVertices
    """
    #  void Qt3DExtras::QCylinderGeometry::updateVertices()
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras17QCylinderGeometry14updateVerticesEv',
    )

  def updateIndices(self) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QCylinderGeometry::updateIndices()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qcylindergeometry.html#updateIndices
    """
    #  void Qt3DExtras::QCylinderGeometry::updateIndices()
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras17QCylinderGeometry13updateIndicesEv',
    )

  @overload(float)
  def radiusChanged(self, radius: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QCylinderGeometry::radiusChanged(float
    radius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qcylindergeometry.html#radiusChanged

    Parameters
    ----------

    radius : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QCylinderGeometry::radiusChanged(float radius)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras17QCylinderGeometry13radiusChangedEf', radius,
    )

  @overload(int)
  def ringsChanged(self, rings: int) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QCylinderGeometry::ringsChanged(int rings)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qcylindergeometry.html#ringsChanged

    Parameters
    ----------

    rings : int
      Passed on as it is.
    """
    #  void Qt3DExtras::QCylinderGeometry::ringsChanged(int rings)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras17QCylinderGeometry12ringsChangedEi', rings,
    )

  @overload(int)
  def slicesChanged(self, slices: int) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QCylinderGeometry::slicesChanged(int
    slices)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qcylindergeometry.html#slicesChanged

    Parameters
    ----------

    slices : int
      Passed on as it is.
    """
    #  void Qt3DExtras::QCylinderGeometry::slicesChanged(int slices)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras17QCylinderGeometry13slicesChangedEi', slices,
    )

  @overload(float)
  def lengthChanged(self, length: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QCylinderGeometry::lengthChanged(float
    length)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qcylindergeometry.html#lengthChanged

    Parameters
    ----------

    length : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QCylinderGeometry::lengthChanged(float length)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras17QCylinderGeometry13lengthChangedEf', length,
    )

  def d_func(self) -> Optional[Qt3DExtras.QCylinderGeometryPrivate]:
    """
    Calls Qt's 'QCylinderGeometryPrivate
    *Qt3DExtras::QCylinderGeometry::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qcylindergeometry.html#d_func

    Returns
    -------

    Optional[Qt3DExtras.QCylinderGeometryPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCylinderGeometryPrivate *Qt3DExtras::QCylinderGeometry::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DExtras17QCylinderGeometry6d_funcEv',
    )
    return Qt3DExtras.QCylinderGeometryPrivate._cuteAt(address)
