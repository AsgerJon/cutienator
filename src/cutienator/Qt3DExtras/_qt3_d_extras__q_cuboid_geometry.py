"""
Qt3DExtras::QCuboidGeometry binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DExtras/qcuboidgeometry.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DExtras

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QSize
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCuboidGeometry(Qt3DCore.QGeometry):
  """
  The cute side of Qt's Qt3DExtras::QCuboidGeometry: a plain Python object
  standing in front of one C++ Qt3DExtras::QCuboidGeometry.

  It is built on the cute 'Qt3DCore::QGeometry', as Qt's
  Qt3DExtras::QCuboidGeometry is built on Qt's Qt3DCore::QGeometry, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DExtras::QCuboidGeometry that has a ritual and
  that Python can call so far, 28 names in all: 'metaObject', 'tr',
  'updateIndices', 'updateVertices', 'xExtent', 'yExtent', 'zExtent',
  'yzMeshResolution', 'xyMeshResolution', 'xzMeshResolution',
  'positionAttribute', 'normalAttribute', 'texCoordAttribute',
  'tangentAttribute', 'indexAttribute', 'setXExtent', 'setYExtent',
  'setZExtent', 'setYZMeshResolution', 'setXZMeshResolution',
  'setXYMeshResolution', 'xExtentChanged', 'yExtentChanged',
  'zExtentChanged', 'yzMeshResolutionChanged', 'xzMeshResolutionChanged',
  'xyMeshResolutionChanged', 'd_func'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DExtras::QCuboidGeometry::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int Qt3DExtras::QCuboidGeometry::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DExtras::QCuboidGeometry::~QCuboidGeometry()': the destructor:
    Python never removes a C++ Qt3DExtras::QCuboidGeometry.
  - Qt's 'Qt3DExtras::QCuboidGeometry::QCuboidGeometry(QCuboidGeometryPrivate
    &dd, QNode *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'const QCuboidGeometryPrivate *Qt3DExtras::QCuboidGeometry::d_func()
    const': takes in Python what 'QCuboidGeometryPrivate
    *Qt3DExtras::QCuboidGeometry::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 36 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DExtras::QCuboidGeometry is created at the first use, not by
    'Qt3DExtras::QCuboidGeometry(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DExtras::QCuboidGeometry.
  - Qt tells when it has removed the C++ Qt3DExtras::QCuboidGeometry. Every
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
    Calls Qt's 'QString Qt3DExtras::QCuboidGeometry::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dextras-qcuboidgeometry.html#tr

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
    #  QString Qt3DExtras::QCuboidGeometry::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN10Qt3DExtras15QCuboidGeometry2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DExtras::QCuboidGeometry'

  #  A C++ Qt3DExtras::QCuboidGeometry Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DExtras_QCuboidGeometry'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DExtras::QCuboidGeometry::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qcuboidgeometry.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DExtras::QCuboidGeometry::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras15QCuboidGeometry10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def xExtent(self) -> float:
    """
    Calls Qt's 'float Qt3DExtras::QCuboidGeometry::xExtent() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qcuboidgeometry.html#xExtent
    """
    #  float Qt3DExtras::QCuboidGeometry::xExtent() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras15QCuboidGeometry7xExtentEv',
    )

  def yExtent(self) -> float:
    """
    Calls Qt's 'float Qt3DExtras::QCuboidGeometry::yExtent() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qcuboidgeometry.html#yExtent
    """
    #  float Qt3DExtras::QCuboidGeometry::yExtent() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras15QCuboidGeometry7yExtentEv',
    )

  def zExtent(self) -> float:
    """
    Calls Qt's 'float Qt3DExtras::QCuboidGeometry::zExtent() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qcuboidgeometry.html#zExtent
    """
    #  float Qt3DExtras::QCuboidGeometry::zExtent() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras15QCuboidGeometry7zExtentEv',
    )

  def yzMeshResolution(self) -> QSize:
    """
    Calls Qt's 'QSize Qt3DExtras::QCuboidGeometry::yzMeshResolution() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qcuboidgeometry.html#yzMeshResolution

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize Qt3DExtras::QCuboidGeometry::yzMeshResolution() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras15QCuboidGeometry16yzMeshResolutionEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def xyMeshResolution(self) -> QSize:
    """
    Calls Qt's 'QSize Qt3DExtras::QCuboidGeometry::xyMeshResolution() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qcuboidgeometry.html#xyMeshResolution

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize Qt3DExtras::QCuboidGeometry::xyMeshResolution() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras15QCuboidGeometry16xyMeshResolutionEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def xzMeshResolution(self) -> QSize:
    """
    Calls Qt's 'QSize Qt3DExtras::QCuboidGeometry::xzMeshResolution() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qcuboidgeometry.html#xzMeshResolution

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize Qt3DExtras::QCuboidGeometry::xzMeshResolution() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras15QCuboidGeometry16xzMeshResolutionEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def positionAttribute(self) -> Optional[Qt3DCore.QAttribute]:
    """
    Calls Qt's 'Qt3DCore::QAttribute
    *Qt3DExtras::QCuboidGeometry::positionAttribute() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qcuboidgeometry.html#positionAttribute

    Returns
    -------

    Optional[Qt3DCore.QAttribute]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DCore::QAttribute *Qt3DExtras::QCuboidGeometry::positionAttribute()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras15QCuboidGeometry17positionAttributeEv',
    )
    return Qt3DCore.QAttribute._cuteAt(address)

  def normalAttribute(self) -> Optional[Qt3DCore.QAttribute]:
    """
    Calls Qt's 'Qt3DCore::QAttribute
    *Qt3DExtras::QCuboidGeometry::normalAttribute() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qcuboidgeometry.html#normalAttribute

    Returns
    -------

    Optional[Qt3DCore.QAttribute]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DCore::QAttribute *Qt3DExtras::QCuboidGeometry::normalAttribute()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras15QCuboidGeometry15normalAttributeEv',
    )
    return Qt3DCore.QAttribute._cuteAt(address)

  def texCoordAttribute(self) -> Optional[Qt3DCore.QAttribute]:
    """
    Calls Qt's 'Qt3DCore::QAttribute
    *Qt3DExtras::QCuboidGeometry::texCoordAttribute() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qcuboidgeometry.html#texCoordAttribute

    Returns
    -------

    Optional[Qt3DCore.QAttribute]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DCore::QAttribute *Qt3DExtras::QCuboidGeometry::texCoordAttribute()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras15QCuboidGeometry17texCoordAttributeEv',
    )
    return Qt3DCore.QAttribute._cuteAt(address)

  def tangentAttribute(self) -> Optional[Qt3DCore.QAttribute]:
    """
    Calls Qt's 'Qt3DCore::QAttribute
    *Qt3DExtras::QCuboidGeometry::tangentAttribute() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qcuboidgeometry.html#tangentAttribute

    Returns
    -------

    Optional[Qt3DCore.QAttribute]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DCore::QAttribute *Qt3DExtras::QCuboidGeometry::tangentAttribute()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras15QCuboidGeometry16tangentAttributeEv',
    )
    return Qt3DCore.QAttribute._cuteAt(address)

  def indexAttribute(self) -> Optional[Qt3DCore.QAttribute]:
    """
    Calls Qt's 'Qt3DCore::QAttribute
    *Qt3DExtras::QCuboidGeometry::indexAttribute() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qcuboidgeometry.html#indexAttribute

    Returns
    -------

    Optional[Qt3DCore.QAttribute]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DCore::QAttribute *Qt3DExtras::QCuboidGeometry::indexAttribute()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras15QCuboidGeometry14indexAttributeEv',
    )
    return Qt3DCore.QAttribute._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setXExtent(self, xExtent: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QCuboidGeometry::setXExtent(float xExtent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qcuboidgeometry.html#setXExtent

    Parameters
    ----------

    xExtent : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QCuboidGeometry::setXExtent(float xExtent)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras15QCuboidGeometry10setXExtentEf', xExtent,
    )

  @overload(float)
  def setYExtent(self, yExtent: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QCuboidGeometry::setYExtent(float yExtent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qcuboidgeometry.html#setYExtent

    Parameters
    ----------

    yExtent : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QCuboidGeometry::setYExtent(float yExtent)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras15QCuboidGeometry10setYExtentEf', yExtent,
    )

  @overload(float)
  def setZExtent(self, zExtent: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QCuboidGeometry::setZExtent(float zExtent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qcuboidgeometry.html#setZExtent

    Parameters
    ----------

    zExtent : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QCuboidGeometry::setZExtent(float zExtent)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras15QCuboidGeometry10setZExtentEf', zExtent,
    )

  @overload(QSize)
  def setYZMeshResolution(self, resolution: QSize) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QCuboidGeometry::setYZMeshResolution(const
    QSize &resolution)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qcuboidgeometry.html

    Parameters
    ----------

    resolution : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void Qt3DExtras::QCuboidGeometry::setYZMeshResolution(const QSize
    #      &resolution)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras15QCuboidGeometry19setYZMeshResolutionERK5QSi'
        'ze',
        self._valueOf(resolution),
    )

  @overload(QSize)
  def setXZMeshResolution(self, resolution: QSize) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QCuboidGeometry::setXZMeshResolution(const
    QSize &resolution)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qcuboidgeometry.html

    Parameters
    ----------

    resolution : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void Qt3DExtras::QCuboidGeometry::setXZMeshResolution(const QSize
    #      &resolution)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras15QCuboidGeometry19setXZMeshResolutionERK5QSi'
        'ze',
        self._valueOf(resolution),
    )

  @overload(QSize)
  def setXYMeshResolution(self, resolution: QSize) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QCuboidGeometry::setXYMeshResolution(const
    QSize &resolution)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qcuboidgeometry.html

    Parameters
    ----------

    resolution : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void Qt3DExtras::QCuboidGeometry::setXYMeshResolution(const QSize
    #      &resolution)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras15QCuboidGeometry19setXYMeshResolutionERK5QSi'
        'ze',
        self._valueOf(resolution),
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
    'Qt3DExtras::QCuboidGeometry::QCuboidGeometry(QNode *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qcuboidgeometry.html#QCuboidGeometry

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DExtras::QCuboidGeometry::QCuboidGeometry(QNode *parent)
    self._noteCreation(QCuboidGeometry, lambda: Rituals.call(
        'ritual_ZN10Qt3DExtras15QCuboidGeometryC1EPN8Qt3DCore5QNodeE',
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

  def updateIndices(self) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QCuboidGeometry::updateIndices()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qcuboidgeometry.html#updateIndices
    """
    #  void Qt3DExtras::QCuboidGeometry::updateIndices()
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras15QCuboidGeometry13updateIndicesEv',
    )

  def updateVertices(self) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QCuboidGeometry::updateVertices()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qcuboidgeometry.html#updateVertices
    """
    #  void Qt3DExtras::QCuboidGeometry::updateVertices()
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras15QCuboidGeometry14updateVerticesEv',
    )

  @overload(float)
  def xExtentChanged(self, xExtent: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QCuboidGeometry::xExtentChanged(float
    xExtent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qcuboidgeometry.html#xExtentChanged

    Parameters
    ----------

    xExtent : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QCuboidGeometry::xExtentChanged(float xExtent)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras15QCuboidGeometry14xExtentChangedEf', xExtent,
    )

  @overload(float)
  def yExtentChanged(self, yExtent: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QCuboidGeometry::yExtentChanged(float
    yExtent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qcuboidgeometry.html#yExtentChanged

    Parameters
    ----------

    yExtent : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QCuboidGeometry::yExtentChanged(float yExtent)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras15QCuboidGeometry14yExtentChangedEf', yExtent,
    )

  @overload(float)
  def zExtentChanged(self, zExtent: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QCuboidGeometry::zExtentChanged(float
    zExtent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qcuboidgeometry.html#zExtentChanged

    Parameters
    ----------

    zExtent : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QCuboidGeometry::zExtentChanged(float zExtent)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras15QCuboidGeometry14zExtentChangedEf', zExtent,
    )

  @overload(QSize)
  def yzMeshResolutionChanged(self, yzMeshResolution: QSize) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QCuboidGeometry::yzMeshResolutionChanged(const QSize
    &yzMeshResolution)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qcuboidgeometry.html

    Parameters
    ----------

    yzMeshResolution : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void Qt3DExtras::QCuboidGeometry::yzMeshResolutionChanged(const QSize
    #      &yzMeshResolution)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras15QCuboidGeometry23yzMeshResolutionChangedERK'
        '5QSize',
        self._valueOf(yzMeshResolution),
    )

  @overload(QSize)
  def xzMeshResolutionChanged(self, xzMeshResolution: QSize) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QCuboidGeometry::xzMeshResolutionChanged(const QSize
    &xzMeshResolution)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qcuboidgeometry.html

    Parameters
    ----------

    xzMeshResolution : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void Qt3DExtras::QCuboidGeometry::xzMeshResolutionChanged(const QSize
    #      &xzMeshResolution)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras15QCuboidGeometry23xzMeshResolutionChangedERK'
        '5QSize',
        self._valueOf(xzMeshResolution),
    )

  @overload(QSize)
  def xyMeshResolutionChanged(self, xyMeshResolution: QSize) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QCuboidGeometry::xyMeshResolutionChanged(const QSize
    &xyMeshResolution)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qcuboidgeometry.html

    Parameters
    ----------

    xyMeshResolution : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void Qt3DExtras::QCuboidGeometry::xyMeshResolutionChanged(const QSize
    #      &xyMeshResolution)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras15QCuboidGeometry23xyMeshResolutionChangedERK'
        '5QSize',
        self._valueOf(xyMeshResolution),
    )

  def d_func(self) -> Optional[Qt3DExtras.QCuboidGeometryPrivate]:
    """
    Calls Qt's 'QCuboidGeometryPrivate
    *Qt3DExtras::QCuboidGeometry::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qcuboidgeometry.html#d_func

    Returns
    -------

    Optional[Qt3DExtras.QCuboidGeometryPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCuboidGeometryPrivate *Qt3DExtras::QCuboidGeometry::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DExtras15QCuboidGeometry6d_funcEv',
    )
    return Qt3DExtras.QCuboidGeometryPrivate._cuteAt(address)
