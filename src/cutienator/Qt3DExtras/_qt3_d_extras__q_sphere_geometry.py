"""
Qt3DExtras::QSphereGeometry binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DExtras/qspheregeometry.h, Qt 6.12.0. Changes made here are lost.
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


class QSphereGeometry(Qt3DCore.QGeometry):
  """
  The cute side of Qt's Qt3DExtras::QSphereGeometry: a plain Python object
  standing in front of one C++ Qt3DExtras::QSphereGeometry.

  It is built on the cute 'Qt3DCore::QGeometry', as Qt's
  Qt3DExtras::QSphereGeometry is built on Qt's Qt3DCore::QGeometry, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DExtras::QSphereGeometry that has a ritual and
  that Python can call so far, 22 names in all: 'metaObject', 'tr',
  'updateVertices', 'updateIndices', 'generateTangents', 'rings', 'slices',
  'radius', 'positionAttribute', 'normalAttribute', 'texCoordAttribute',
  'tangentAttribute', 'indexAttribute', 'setRings', 'setSlices', 'setRadius',
  'setGenerateTangents', 'radiusChanged', 'ringsChanged', 'slicesChanged',
  'generateTangentsChanged', 'd_func'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DExtras::QSphereGeometry::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int Qt3DExtras::QSphereGeometry::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DExtras::QSphereGeometry::~QSphereGeometry()': the destructor:
    Python never removes a C++ Qt3DExtras::QSphereGeometry.
  - Qt's 'Qt3DExtras::QSphereGeometry::QSphereGeometry(QSphereGeometryPrivate
    &dd, QNode *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'const QSphereGeometryPrivate *Qt3DExtras::QSphereGeometry::d_func()
    const': takes in Python what 'QSphereGeometryPrivate
    *Qt3DExtras::QSphereGeometry::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 30 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DExtras::QSphereGeometry is created at the first use, not by
    'Qt3DExtras::QSphereGeometry(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DExtras::QSphereGeometry.
  - Qt tells when it has removed the C++ Qt3DExtras::QSphereGeometry. Every
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
    Calls Qt's 'QString Qt3DExtras::QSphereGeometry::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dextras-qspheregeometry.html#tr

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
    #  QString Qt3DExtras::QSphereGeometry::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN10Qt3DExtras15QSphereGeometry2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DExtras::QSphereGeometry'

  #  A C++ Qt3DExtras::QSphereGeometry Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DExtras_QSphereGeometry'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DExtras::QSphereGeometry::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qspheregeometry.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DExtras::QSphereGeometry::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras15QSphereGeometry10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def generateTangents(self) -> bool:
    """
    Calls Qt's 'bool Qt3DExtras::QSphereGeometry::generateTangents() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qspheregeometry.html#generateTangents
    """
    #  bool Qt3DExtras::QSphereGeometry::generateTangents() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras15QSphereGeometry16generateTangentsEv',
    )

  def rings(self) -> int:
    """
    Calls Qt's 'int Qt3DExtras::QSphereGeometry::rings() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qspheregeometry.html#rings
    """
    #  int Qt3DExtras::QSphereGeometry::rings() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras15QSphereGeometry5ringsEv',
    )

  def slices(self) -> int:
    """
    Calls Qt's 'int Qt3DExtras::QSphereGeometry::slices() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qspheregeometry.html#slices
    """
    #  int Qt3DExtras::QSphereGeometry::slices() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras15QSphereGeometry6slicesEv',
    )

  def radius(self) -> float:
    """
    Calls Qt's 'float Qt3DExtras::QSphereGeometry::radius() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qspheregeometry.html#radius
    """
    #  float Qt3DExtras::QSphereGeometry::radius() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras15QSphereGeometry6radiusEv',
    )

  def positionAttribute(self) -> Optional[Qt3DCore.QAttribute]:
    """
    Calls Qt's 'Qt3DCore::QAttribute
    *Qt3DExtras::QSphereGeometry::positionAttribute() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qspheregeometry.html#positionAttribute

    Returns
    -------

    Optional[Qt3DCore.QAttribute]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DCore::QAttribute *Qt3DExtras::QSphereGeometry::positionAttribute()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras15QSphereGeometry17positionAttributeEv',
    )
    return Qt3DCore.QAttribute._cuteAt(address)

  def normalAttribute(self) -> Optional[Qt3DCore.QAttribute]:
    """
    Calls Qt's 'Qt3DCore::QAttribute
    *Qt3DExtras::QSphereGeometry::normalAttribute() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qspheregeometry.html#normalAttribute

    Returns
    -------

    Optional[Qt3DCore.QAttribute]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DCore::QAttribute *Qt3DExtras::QSphereGeometry::normalAttribute()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras15QSphereGeometry15normalAttributeEv',
    )
    return Qt3DCore.QAttribute._cuteAt(address)

  def texCoordAttribute(self) -> Optional[Qt3DCore.QAttribute]:
    """
    Calls Qt's 'Qt3DCore::QAttribute
    *Qt3DExtras::QSphereGeometry::texCoordAttribute() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qspheregeometry.html#texCoordAttribute

    Returns
    -------

    Optional[Qt3DCore.QAttribute]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DCore::QAttribute *Qt3DExtras::QSphereGeometry::texCoordAttribute()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras15QSphereGeometry17texCoordAttributeEv',
    )
    return Qt3DCore.QAttribute._cuteAt(address)

  def tangentAttribute(self) -> Optional[Qt3DCore.QAttribute]:
    """
    Calls Qt's 'Qt3DCore::QAttribute
    *Qt3DExtras::QSphereGeometry::tangentAttribute() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qspheregeometry.html#tangentAttribute

    Returns
    -------

    Optional[Qt3DCore.QAttribute]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DCore::QAttribute *Qt3DExtras::QSphereGeometry::tangentAttribute()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras15QSphereGeometry16tangentAttributeEv',
    )
    return Qt3DCore.QAttribute._cuteAt(address)

  def indexAttribute(self) -> Optional[Qt3DCore.QAttribute]:
    """
    Calls Qt's 'Qt3DCore::QAttribute
    *Qt3DExtras::QSphereGeometry::indexAttribute() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qspheregeometry.html#indexAttribute

    Returns
    -------

    Optional[Qt3DCore.QAttribute]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DCore::QAttribute *Qt3DExtras::QSphereGeometry::indexAttribute()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras15QSphereGeometry14indexAttributeEv',
    )
    return Qt3DCore.QAttribute._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setRings(self, rings: int) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QSphereGeometry::setRings(int rings)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qspheregeometry.html#setRings

    Parameters
    ----------

    rings : int
      Passed on as it is.
    """
    #  void Qt3DExtras::QSphereGeometry::setRings(int rings)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras15QSphereGeometry8setRingsEi', rings,
    )

  @overload(int)
  def setSlices(self, slices: int) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QSphereGeometry::setSlices(int slices)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qspheregeometry.html#setSlices

    Parameters
    ----------

    slices : int
      Passed on as it is.
    """
    #  void Qt3DExtras::QSphereGeometry::setSlices(int slices)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras15QSphereGeometry9setSlicesEi', slices,
    )

  @overload(float)
  def setRadius(self, radius: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QSphereGeometry::setRadius(float radius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qspheregeometry.html#setRadius

    Parameters
    ----------

    radius : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QSphereGeometry::setRadius(float radius)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras15QSphereGeometry9setRadiusEf', radius,
    )

  @overload(bool)
  def setGenerateTangents(self, gen: bool) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QSphereGeometry::setGenerateTangents(bool
    gen)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qspheregeometry.html

    Parameters
    ----------

    gen : bool
      Passed on as it is.
    """
    #  void Qt3DExtras::QSphereGeometry::setGenerateTangents(bool gen)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras15QSphereGeometry19setGenerateTangentsEb', gen,
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
    'Qt3DExtras::QSphereGeometry::QSphereGeometry(QNode *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qspheregeometry.html#QSphereGeometry

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DExtras::QSphereGeometry::QSphereGeometry(QNode *parent)
    self._noteCreation(QSphereGeometry, lambda: Rituals.call(
        'ritual_ZN10Qt3DExtras15QSphereGeometryC1EPN8Qt3DCore5QNodeE',
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
    Calls Qt's 'void Qt3DExtras::QSphereGeometry::updateVertices()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qspheregeometry.html#updateVertices
    """
    #  void Qt3DExtras::QSphereGeometry::updateVertices()
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras15QSphereGeometry14updateVerticesEv',
    )

  def updateIndices(self) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QSphereGeometry::updateIndices()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qspheregeometry.html#updateIndices
    """
    #  void Qt3DExtras::QSphereGeometry::updateIndices()
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras15QSphereGeometry13updateIndicesEv',
    )

  @overload(float)
  def radiusChanged(self, radius: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QSphereGeometry::radiusChanged(float
    radius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qspheregeometry.html#radiusChanged

    Parameters
    ----------

    radius : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QSphereGeometry::radiusChanged(float radius)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras15QSphereGeometry13radiusChangedEf', radius,
    )

  @overload(int)
  def ringsChanged(self, rings: int) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QSphereGeometry::ringsChanged(int rings)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qspheregeometry.html#ringsChanged

    Parameters
    ----------

    rings : int
      Passed on as it is.
    """
    #  void Qt3DExtras::QSphereGeometry::ringsChanged(int rings)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras15QSphereGeometry12ringsChangedEi', rings,
    )

  @overload(int)
  def slicesChanged(self, slices: int) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QSphereGeometry::slicesChanged(int slices)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qspheregeometry.html#slicesChanged

    Parameters
    ----------

    slices : int
      Passed on as it is.
    """
    #  void Qt3DExtras::QSphereGeometry::slicesChanged(int slices)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras15QSphereGeometry13slicesChangedEi', slices,
    )

  @overload(bool)
  def generateTangentsChanged(self, generateTangents: bool) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QSphereGeometry::generateTangentsChanged(bool
    generateTangents)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qspheregeometry.html

    Parameters
    ----------

    generateTangents : bool
      Passed on as it is.
    """
    #  void Qt3DExtras::QSphereGeometry::generateTangentsChanged(bool
    #      generateTangents)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras15QSphereGeometry23generateTangentsChangedEb',
        generateTangents,
    )

  def d_func(self) -> Optional[Qt3DExtras.QSphereGeometryPrivate]:
    """
    Calls Qt's 'QSphereGeometryPrivate
    *Qt3DExtras::QSphereGeometry::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qspheregeometry.html#d_func

    Returns
    -------

    Optional[Qt3DExtras.QSphereGeometryPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSphereGeometryPrivate *Qt3DExtras::QSphereGeometry::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DExtras15QSphereGeometry6d_funcEv',
    )
    return Qt3DExtras.QSphereGeometryPrivate._cuteAt(address)
