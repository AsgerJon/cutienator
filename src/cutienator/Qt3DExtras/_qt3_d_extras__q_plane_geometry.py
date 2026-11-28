"""
Qt3DExtras::QPlaneGeometry binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DExtras/qplanegeometry.h, Qt 6.12.0. Changes made here are lost.
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


class QPlaneGeometry(Qt3DCore.QGeometry):
  """
  The cute side of Qt's Qt3DExtras::QPlaneGeometry: a plain Python object
  standing in front of one C++ Qt3DExtras::QPlaneGeometry.

  It is built on the cute 'Qt3DCore::QGeometry', as Qt's
  Qt3DExtras::QPlaneGeometry is built on Qt's Qt3DCore::QGeometry, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DExtras::QPlaneGeometry that has a ritual and
  that Python can call so far, 22 names in all: 'metaObject', 'tr',
  'updateVertices', 'updateIndices', 'resolution', 'width', 'height',
  'mirrored', 'positionAttribute', 'normalAttribute', 'texCoordAttribute',
  'tangentAttribute', 'indexAttribute', 'setResolution', 'setWidth',
  'setHeight', 'setMirrored', 'resolutionChanged', 'widthChanged',
  'heightChanged', 'mirroredChanged', 'd_func'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DExtras::QPlaneGeometry::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int Qt3DExtras::QPlaneGeometry::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DExtras::QPlaneGeometry::~QPlaneGeometry()': the destructor:
    Python never removes a C++ Qt3DExtras::QPlaneGeometry.
  - Qt's 'Qt3DExtras::QPlaneGeometry::QPlaneGeometry(QPlaneGeometryPrivate
    &dd, QNode *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'const QPlaneGeometryPrivate *Qt3DExtras::QPlaneGeometry::d_func()
    const': takes in Python what 'QPlaneGeometryPrivate
    *Qt3DExtras::QPlaneGeometry::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 30 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DExtras::QPlaneGeometry is created at the first use, not by
    'Qt3DExtras::QPlaneGeometry(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DExtras::QPlaneGeometry.
  - Qt tells when it has removed the C++ Qt3DExtras::QPlaneGeometry. Every
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
    Calls Qt's 'QString Qt3DExtras::QPlaneGeometry::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dextras-qplanegeometry.html#tr

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
    #  QString Qt3DExtras::QPlaneGeometry::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN10Qt3DExtras14QPlaneGeometry2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DExtras::QPlaneGeometry'

  #  A C++ Qt3DExtras::QPlaneGeometry Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DExtras_QPlaneGeometry'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DExtras::QPlaneGeometry::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qplanegeometry.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DExtras::QPlaneGeometry::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras14QPlaneGeometry10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def resolution(self) -> QSize:
    """
    Calls Qt's 'QSize Qt3DExtras::QPlaneGeometry::resolution() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qplanegeometry.html#resolution

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize Qt3DExtras::QPlaneGeometry::resolution() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras14QPlaneGeometry10resolutionEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def width(self) -> float:
    """
    Calls Qt's 'float Qt3DExtras::QPlaneGeometry::width() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qplanegeometry.html#width
    """
    #  float Qt3DExtras::QPlaneGeometry::width() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras14QPlaneGeometry5widthEv',
    )

  def height(self) -> float:
    """
    Calls Qt's 'float Qt3DExtras::QPlaneGeometry::height() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qplanegeometry.html#height
    """
    #  float Qt3DExtras::QPlaneGeometry::height() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras14QPlaneGeometry6heightEv',
    )

  def mirrored(self) -> bool:
    """
    Calls Qt's 'bool Qt3DExtras::QPlaneGeometry::mirrored() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qplanegeometry.html#mirrored
    """
    #  bool Qt3DExtras::QPlaneGeometry::mirrored() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras14QPlaneGeometry8mirroredEv',
    )

  def positionAttribute(self) -> Optional[Qt3DCore.QAttribute]:
    """
    Calls Qt's 'Qt3DCore::QAttribute
    *Qt3DExtras::QPlaneGeometry::positionAttribute() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qplanegeometry.html#positionAttribute

    Returns
    -------

    Optional[Qt3DCore.QAttribute]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DCore::QAttribute *Qt3DExtras::QPlaneGeometry::positionAttribute()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras14QPlaneGeometry17positionAttributeEv',
    )
    return Qt3DCore.QAttribute._cuteAt(address)

  def normalAttribute(self) -> Optional[Qt3DCore.QAttribute]:
    """
    Calls Qt's 'Qt3DCore::QAttribute
    *Qt3DExtras::QPlaneGeometry::normalAttribute() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qplanegeometry.html#normalAttribute

    Returns
    -------

    Optional[Qt3DCore.QAttribute]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DCore::QAttribute *Qt3DExtras::QPlaneGeometry::normalAttribute()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras14QPlaneGeometry15normalAttributeEv',
    )
    return Qt3DCore.QAttribute._cuteAt(address)

  def texCoordAttribute(self) -> Optional[Qt3DCore.QAttribute]:
    """
    Calls Qt's 'Qt3DCore::QAttribute
    *Qt3DExtras::QPlaneGeometry::texCoordAttribute() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qplanegeometry.html#texCoordAttribute

    Returns
    -------

    Optional[Qt3DCore.QAttribute]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DCore::QAttribute *Qt3DExtras::QPlaneGeometry::texCoordAttribute()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras14QPlaneGeometry17texCoordAttributeEv',
    )
    return Qt3DCore.QAttribute._cuteAt(address)

  def tangentAttribute(self) -> Optional[Qt3DCore.QAttribute]:
    """
    Calls Qt's 'Qt3DCore::QAttribute
    *Qt3DExtras::QPlaneGeometry::tangentAttribute() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qplanegeometry.html#tangentAttribute

    Returns
    -------

    Optional[Qt3DCore.QAttribute]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DCore::QAttribute *Qt3DExtras::QPlaneGeometry::tangentAttribute()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras14QPlaneGeometry16tangentAttributeEv',
    )
    return Qt3DCore.QAttribute._cuteAt(address)

  def indexAttribute(self) -> Optional[Qt3DCore.QAttribute]:
    """
    Calls Qt's 'Qt3DCore::QAttribute
    *Qt3DExtras::QPlaneGeometry::indexAttribute() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qplanegeometry.html#indexAttribute

    Returns
    -------

    Optional[Qt3DCore.QAttribute]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DCore::QAttribute *Qt3DExtras::QPlaneGeometry::indexAttribute()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras14QPlaneGeometry14indexAttributeEv',
    )
    return Qt3DCore.QAttribute._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSize)
  def setResolution(self, resolution: QSize) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QPlaneGeometry::setResolution(const QSize
    &resolution)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qplanegeometry.html#setResolution

    Parameters
    ----------

    resolution : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void Qt3DExtras::QPlaneGeometry::setResolution(const QSize
    #      &resolution)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras14QPlaneGeometry13setResolutionERK5QSize',
        self._valueOf(resolution),
    )

  @overload(float)
  def setWidth(self, width: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QPlaneGeometry::setWidth(float width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qplanegeometry.html#setWidth

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QPlaneGeometry::setWidth(float width)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras14QPlaneGeometry8setWidthEf', width,
    )

  @overload(float)
  def setHeight(self, height: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QPlaneGeometry::setHeight(float height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qplanegeometry.html#setHeight

    Parameters
    ----------

    height : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QPlaneGeometry::setHeight(float height)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras14QPlaneGeometry9setHeightEf', height,
    )

  @overload(bool)
  def setMirrored(self, mirrored: bool) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QPlaneGeometry::setMirrored(bool mirrored)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qplanegeometry.html#setMirrored

    Parameters
    ----------

    mirrored : bool
      Passed on as it is.
    """
    #  void Qt3DExtras::QPlaneGeometry::setMirrored(bool mirrored)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras14QPlaneGeometry11setMirroredEb', mirrored,
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
    'Qt3DExtras::QPlaneGeometry::QPlaneGeometry(QNode *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qplanegeometry.html#QPlaneGeometry

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DExtras::QPlaneGeometry::QPlaneGeometry(QNode *parent)
    self._noteCreation(QPlaneGeometry, lambda: Rituals.call(
        'ritual_ZN10Qt3DExtras14QPlaneGeometryC1EPN8Qt3DCore5QNodeE',
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
    Calls Qt's 'void Qt3DExtras::QPlaneGeometry::updateVertices()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qplanegeometry.html#updateVertices
    """
    #  void Qt3DExtras::QPlaneGeometry::updateVertices()
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras14QPlaneGeometry14updateVerticesEv',
    )

  def updateIndices(self) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QPlaneGeometry::updateIndices()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qplanegeometry.html#updateIndices
    """
    #  void Qt3DExtras::QPlaneGeometry::updateIndices()
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras14QPlaneGeometry13updateIndicesEv',
    )

  @overload(QSize)
  def resolutionChanged(self, resolution: QSize) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QPlaneGeometry::resolutionChanged(const
    QSize &resolution)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qplanegeometry.html#resolutionChanged

    Parameters
    ----------

    resolution : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void Qt3DExtras::QPlaneGeometry::resolutionChanged(const QSize
    #      &resolution)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras14QPlaneGeometry17resolutionChangedERK5QSize',
        self._valueOf(resolution),
    )

  @overload(float)
  def widthChanged(self, width: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QPlaneGeometry::widthChanged(float width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qplanegeometry.html#widthChanged

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QPlaneGeometry::widthChanged(float width)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras14QPlaneGeometry12widthChangedEf', width,
    )

  @overload(float)
  def heightChanged(self, height: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QPlaneGeometry::heightChanged(float
    height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qplanegeometry.html#heightChanged

    Parameters
    ----------

    height : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QPlaneGeometry::heightChanged(float height)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras14QPlaneGeometry13heightChangedEf', height,
    )

  @overload(bool)
  def mirroredChanged(self, mirrored: bool) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QPlaneGeometry::mirroredChanged(bool
    mirrored)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qplanegeometry.html#mirroredChanged

    Parameters
    ----------

    mirrored : bool
      Passed on as it is.
    """
    #  void Qt3DExtras::QPlaneGeometry::mirroredChanged(bool mirrored)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras14QPlaneGeometry15mirroredChangedEb', mirrored,
    )

  def d_func(self) -> Optional[Qt3DExtras.QPlaneGeometryPrivate]:
    """
    Calls Qt's 'QPlaneGeometryPrivate *Qt3DExtras::QPlaneGeometry::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qplanegeometry.html#d_func

    Returns
    -------

    Optional[Qt3DExtras.QPlaneGeometryPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlaneGeometryPrivate *Qt3DExtras::QPlaneGeometry::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DExtras14QPlaneGeometry6d_funcEv',
    )
    return Qt3DExtras.QPlaneGeometryPrivate._cuteAt(address)
