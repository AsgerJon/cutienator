"""
Qt3DExtras::QConeGeometry binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DExtras/qconegeometry.h, Qt 6.12.0. Changes made here are lost.
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


class QConeGeometry(Qt3DCore.QGeometry):
  """
  The cute side of Qt's Qt3DExtras::QConeGeometry: a plain Python object
  standing in front of one C++ Qt3DExtras::QConeGeometry.

  It is built on the cute 'Qt3DCore::QGeometry', as Qt's
  Qt3DExtras::QConeGeometry is built on Qt's Qt3DCore::QGeometry, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DExtras::QConeGeometry that has a ritual and that
  Python can call so far, 30 names in all: 'metaObject', 'tr',
  'updateVertices', 'updateIndices', 'hasTopEndcap', 'hasBottomEndcap',
  'topRadius', 'bottomRadius', 'rings', 'slices', 'length',
  'positionAttribute', 'normalAttribute', 'texCoordAttribute',
  'indexAttribute', 'setHasTopEndcap', 'setHasBottomEndcap', 'setTopRadius',
  'setBottomRadius', 'setRings', 'setSlices', 'setLength',
  'hasTopEndcapChanged', 'hasBottomEndcapChanged', 'topRadiusChanged',
  'bottomRadiusChanged', 'ringsChanged', 'slicesChanged', 'lengthChanged',
  'd_func'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DExtras::QConeGeometry::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int Qt3DExtras::QConeGeometry::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DExtras::QConeGeometry::~QConeGeometry()': the destructor:
    Python never removes a C++ Qt3DExtras::QConeGeometry.
  - Qt's 'Qt3DExtras::QConeGeometry::QConeGeometry(QConeGeometryPrivate &dd,
    QNode *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'const QConeGeometryPrivate *Qt3DExtras::QConeGeometry::d_func()
    const': takes in Python what 'QConeGeometryPrivate
    *Qt3DExtras::QConeGeometry::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 38 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DExtras::QConeGeometry is created at the first use, not by
    'Qt3DExtras::QConeGeometry(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DExtras::QConeGeometry.
  - Qt tells when it has removed the C++ Qt3DExtras::QConeGeometry. Every
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
    Calls Qt's 'QString Qt3DExtras::QConeGeometry::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dextras-qconegeometry.html#tr

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
    #  QString Qt3DExtras::QConeGeometry::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN10Qt3DExtras13QConeGeometry2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DExtras::QConeGeometry'

  #  A C++ Qt3DExtras::QConeGeometry Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DExtras_QConeGeometry'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DExtras::QConeGeometry::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconegeometry.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DExtras::QConeGeometry::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras13QConeGeometry10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def hasTopEndcap(self) -> bool:
    """
    Calls Qt's 'bool Qt3DExtras::QConeGeometry::hasTopEndcap() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconegeometry.html#hasTopEndcap
    """
    #  bool Qt3DExtras::QConeGeometry::hasTopEndcap() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras13QConeGeometry12hasTopEndcapEv',
    )

  def hasBottomEndcap(self) -> bool:
    """
    Calls Qt's 'bool Qt3DExtras::QConeGeometry::hasBottomEndcap() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconegeometry.html#hasBottomEndcap
    """
    #  bool Qt3DExtras::QConeGeometry::hasBottomEndcap() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras13QConeGeometry15hasBottomEndcapEv',
    )

  def topRadius(self) -> float:
    """
    Calls Qt's 'float Qt3DExtras::QConeGeometry::topRadius() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconegeometry.html#topRadius
    """
    #  float Qt3DExtras::QConeGeometry::topRadius() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras13QConeGeometry9topRadiusEv',
    )

  def bottomRadius(self) -> float:
    """
    Calls Qt's 'float Qt3DExtras::QConeGeometry::bottomRadius() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconegeometry.html#bottomRadius
    """
    #  float Qt3DExtras::QConeGeometry::bottomRadius() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras13QConeGeometry12bottomRadiusEv',
    )

  def rings(self) -> int:
    """
    Calls Qt's 'int Qt3DExtras::QConeGeometry::rings() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconegeometry.html#rings
    """
    #  int Qt3DExtras::QConeGeometry::rings() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras13QConeGeometry5ringsEv',
    )

  def slices(self) -> int:
    """
    Calls Qt's 'int Qt3DExtras::QConeGeometry::slices() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconegeometry.html#slices
    """
    #  int Qt3DExtras::QConeGeometry::slices() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras13QConeGeometry6slicesEv',
    )

  def length(self) -> float:
    """
    Calls Qt's 'float Qt3DExtras::QConeGeometry::length() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconegeometry.html#length
    """
    #  float Qt3DExtras::QConeGeometry::length() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras13QConeGeometry6lengthEv',
    )

  def positionAttribute(self) -> Optional[Qt3DCore.QAttribute]:
    """
    Calls Qt's 'Qt3DCore::QAttribute
    *Qt3DExtras::QConeGeometry::positionAttribute() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconegeometry.html#positionAttribute

    Returns
    -------

    Optional[Qt3DCore.QAttribute]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DCore::QAttribute *Qt3DExtras::QConeGeometry::positionAttribute()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras13QConeGeometry17positionAttributeEv',
    )
    return Qt3DCore.QAttribute._cuteAt(address)

  def normalAttribute(self) -> Optional[Qt3DCore.QAttribute]:
    """
    Calls Qt's 'Qt3DCore::QAttribute
    *Qt3DExtras::QConeGeometry::normalAttribute() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconegeometry.html#normalAttribute

    Returns
    -------

    Optional[Qt3DCore.QAttribute]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DCore::QAttribute *Qt3DExtras::QConeGeometry::normalAttribute()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras13QConeGeometry15normalAttributeEv',
    )
    return Qt3DCore.QAttribute._cuteAt(address)

  def texCoordAttribute(self) -> Optional[Qt3DCore.QAttribute]:
    """
    Calls Qt's 'Qt3DCore::QAttribute
    *Qt3DExtras::QConeGeometry::texCoordAttribute() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconegeometry.html#texCoordAttribute

    Returns
    -------

    Optional[Qt3DCore.QAttribute]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DCore::QAttribute *Qt3DExtras::QConeGeometry::texCoordAttribute()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras13QConeGeometry17texCoordAttributeEv',
    )
    return Qt3DCore.QAttribute._cuteAt(address)

  def indexAttribute(self) -> Optional[Qt3DCore.QAttribute]:
    """
    Calls Qt's 'Qt3DCore::QAttribute
    *Qt3DExtras::QConeGeometry::indexAttribute() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconegeometry.html#indexAttribute

    Returns
    -------

    Optional[Qt3DCore.QAttribute]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DCore::QAttribute *Qt3DExtras::QConeGeometry::indexAttribute()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras13QConeGeometry14indexAttributeEv',
    )
    return Qt3DCore.QAttribute._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setHasTopEndcap(self, hasTopEndcap: bool) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QConeGeometry::setHasTopEndcap(bool
    hasTopEndcap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconegeometry.html#setHasTopEndcap

    Parameters
    ----------

    hasTopEndcap : bool
      Passed on as it is.
    """
    #  void Qt3DExtras::QConeGeometry::setHasTopEndcap(bool hasTopEndcap)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras13QConeGeometry15setHasTopEndcapEb',
        hasTopEndcap,
    )

  @overload(bool)
  def setHasBottomEndcap(self, hasBottomEndcap: bool) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QConeGeometry::setHasBottomEndcap(bool
    hasBottomEndcap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconegeometry.html#setHasBottomEndcap

    Parameters
    ----------

    hasBottomEndcap : bool
      Passed on as it is.
    """
    #  void Qt3DExtras::QConeGeometry::setHasBottomEndcap(bool
    #      hasBottomEndcap)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras13QConeGeometry18setHasBottomEndcapEb',
        hasBottomEndcap,
    )

  @overload(float)
  def setTopRadius(self, topRadius: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QConeGeometry::setTopRadius(float
    topRadius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconegeometry.html#setTopRadius

    Parameters
    ----------

    topRadius : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QConeGeometry::setTopRadius(float topRadius)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras13QConeGeometry12setTopRadiusEf', topRadius,
    )

  @overload(float)
  def setBottomRadius(self, bottomRadius: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QConeGeometry::setBottomRadius(float
    bottomRadius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconegeometry.html#setBottomRadius

    Parameters
    ----------

    bottomRadius : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QConeGeometry::setBottomRadius(float bottomRadius)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras13QConeGeometry15setBottomRadiusEf',
        bottomRadius,
    )

  @overload(int)
  def setRings(self, rings: int) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QConeGeometry::setRings(int rings)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconegeometry.html#setRings

    Parameters
    ----------

    rings : int
      Passed on as it is.
    """
    #  void Qt3DExtras::QConeGeometry::setRings(int rings)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras13QConeGeometry8setRingsEi', rings,
    )

  @overload(int)
  def setSlices(self, slices: int) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QConeGeometry::setSlices(int slices)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconegeometry.html#setSlices

    Parameters
    ----------

    slices : int
      Passed on as it is.
    """
    #  void Qt3DExtras::QConeGeometry::setSlices(int slices)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras13QConeGeometry9setSlicesEi', slices,
    )

  @overload(float)
  def setLength(self, length: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QConeGeometry::setLength(float length)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconegeometry.html#setLength

    Parameters
    ----------

    length : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QConeGeometry::setLength(float length)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras13QConeGeometry9setLengthEf', length,
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
    'Qt3DExtras::QConeGeometry::QConeGeometry(QNode *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconegeometry.html#QConeGeometry

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DExtras::QConeGeometry::QConeGeometry(QNode *parent)
    self._noteCreation(QConeGeometry, lambda: Rituals.call(
        'ritual_ZN10Qt3DExtras13QConeGeometryC1EPN8Qt3DCore5QNodeE',
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
    Calls Qt's 'void Qt3DExtras::QConeGeometry::updateVertices()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconegeometry.html#updateVertices
    """
    #  void Qt3DExtras::QConeGeometry::updateVertices()
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras13QConeGeometry14updateVerticesEv',
    )

  def updateIndices(self) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QConeGeometry::updateIndices()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconegeometry.html#updateIndices
    """
    #  void Qt3DExtras::QConeGeometry::updateIndices()
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras13QConeGeometry13updateIndicesEv',
    )

  @overload(bool)
  def hasTopEndcapChanged(self, hasTopEndcap: bool) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QConeGeometry::hasTopEndcapChanged(bool
    hasTopEndcap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconegeometry.html#hasTopEndcapChanged

    Parameters
    ----------

    hasTopEndcap : bool
      Passed on as it is.
    """
    #  void Qt3DExtras::QConeGeometry::hasTopEndcapChanged(bool hasTopEndcap)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras13QConeGeometry19hasTopEndcapChangedEb',
        hasTopEndcap,
    )

  @overload(bool)
  def hasBottomEndcapChanged(self, hasBottomEndcap: bool) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QConeGeometry::hasBottomEndcapChanged(bool
    hasBottomEndcap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconegeometry.html

    Parameters
    ----------

    hasBottomEndcap : bool
      Passed on as it is.
    """
    #  void Qt3DExtras::QConeGeometry::hasBottomEndcapChanged(bool
    #      hasBottomEndcap)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras13QConeGeometry22hasBottomEndcapChangedEb',
        hasBottomEndcap,
    )

  @overload(float)
  def topRadiusChanged(self, topRadius: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QConeGeometry::topRadiusChanged(float
    topRadius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconegeometry.html#topRadiusChanged

    Parameters
    ----------

    topRadius : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QConeGeometry::topRadiusChanged(float topRadius)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras13QConeGeometry16topRadiusChangedEf',
        topRadius,
    )

  @overload(float)
  def bottomRadiusChanged(self, bottomRadius: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QConeGeometry::bottomRadiusChanged(float
    bottomRadius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconegeometry.html#bottomRadiusChanged

    Parameters
    ----------

    bottomRadius : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QConeGeometry::bottomRadiusChanged(float
    #      bottomRadius)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras13QConeGeometry19bottomRadiusChangedEf',
        bottomRadius,
    )

  @overload(int)
  def ringsChanged(self, rings: int) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QConeGeometry::ringsChanged(int rings)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconegeometry.html#ringsChanged

    Parameters
    ----------

    rings : int
      Passed on as it is.
    """
    #  void Qt3DExtras::QConeGeometry::ringsChanged(int rings)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras13QConeGeometry12ringsChangedEi', rings,
    )

  @overload(int)
  def slicesChanged(self, slices: int) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QConeGeometry::slicesChanged(int slices)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconegeometry.html#slicesChanged

    Parameters
    ----------

    slices : int
      Passed on as it is.
    """
    #  void Qt3DExtras::QConeGeometry::slicesChanged(int slices)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras13QConeGeometry13slicesChangedEi', slices,
    )

  @overload(float)
  def lengthChanged(self, length: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QConeGeometry::lengthChanged(float length)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconegeometry.html#lengthChanged

    Parameters
    ----------

    length : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QConeGeometry::lengthChanged(float length)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras13QConeGeometry13lengthChangedEf', length,
    )

  def d_func(self) -> Optional[Qt3DExtras.QConeGeometryPrivate]:
    """
    Calls Qt's 'QConeGeometryPrivate *Qt3DExtras::QConeGeometry::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconegeometry.html#d_func

    Returns
    -------

    Optional[Qt3DExtras.QConeGeometryPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QConeGeometryPrivate *Qt3DExtras::QConeGeometry::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DExtras13QConeGeometry6d_funcEv',
    )
    return Qt3DExtras.QConeGeometryPrivate._cuteAt(address)
