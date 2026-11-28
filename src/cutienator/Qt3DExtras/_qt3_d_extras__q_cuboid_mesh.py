"""
Qt3DExtras::QCuboidMesh binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DExtras/qcuboidmesh.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from ..Qt3DRender import Qt3DRender

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


class QCuboidMesh(Qt3DRender.QGeometryRenderer):
  """
  The cute side of Qt's Qt3DExtras::QCuboidMesh: a plain Python object
  standing in front of one C++ Qt3DExtras::QCuboidMesh.

  It is built on the cute 'Qt3DRender::QGeometryRenderer', as Qt's
  Qt3DExtras::QCuboidMesh is built on Qt's Qt3DRender::QGeometryRenderer, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DExtras::QCuboidMesh that has a ritual and that
  Python can call so far, 20 names in all: 'metaObject', 'tr', 'xExtent',
  'yExtent', 'zExtent', 'yzMeshResolution', 'xzMeshResolution',
  'xyMeshResolution', 'setXExtent', 'setYExtent', 'setZExtent',
  'setYZMeshResolution', 'setXZMeshResolution', 'setXYMeshResolution',
  'xExtentChanged', 'yExtentChanged', 'zExtentChanged',
  'yzMeshResolutionChanged', 'xzMeshResolutionChanged',
  'xyMeshResolutionChanged'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DExtras::QCuboidMesh::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int Qt3DExtras::QCuboidMesh::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DExtras::QCuboidMesh::~QCuboidMesh()': the destructor: Python
    never removes a C++ Qt3DExtras::QCuboidMesh.

  What has no ritual
  ------------------

  10 of the 34 functions Qt declares: 10 not a gap.

  What to expect
  --------------

  - The C++ Qt3DExtras::QCuboidMesh is created at the first use, not by
    'Qt3DExtras::QCuboidMesh(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DExtras::QCuboidMesh.
  - Qt tells when it has removed the C++ Qt3DExtras::QCuboidMesh. Every call
    on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString Qt3DExtras::QCuboidMesh::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dextras-qcuboidmesh.html#tr

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
    #  QString Qt3DExtras::QCuboidMesh::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN10Qt3DExtras11QCuboidMesh2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DExtras::QCuboidMesh'

  #  A C++ Qt3DExtras::QCuboidMesh Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DExtras_QCuboidMesh'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DExtras::QCuboidMesh::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qcuboidmesh.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DExtras::QCuboidMesh::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras11QCuboidMesh10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def xExtent(self) -> float:
    """
    Calls Qt's 'float Qt3DExtras::QCuboidMesh::xExtent() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qcuboidmesh.html#xExtent
    """
    #  float Qt3DExtras::QCuboidMesh::xExtent() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras11QCuboidMesh7xExtentEv',
    )

  def yExtent(self) -> float:
    """
    Calls Qt's 'float Qt3DExtras::QCuboidMesh::yExtent() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qcuboidmesh.html#yExtent
    """
    #  float Qt3DExtras::QCuboidMesh::yExtent() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras11QCuboidMesh7yExtentEv',
    )

  def zExtent(self) -> float:
    """
    Calls Qt's 'float Qt3DExtras::QCuboidMesh::zExtent() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qcuboidmesh.html#zExtent
    """
    #  float Qt3DExtras::QCuboidMesh::zExtent() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras11QCuboidMesh7zExtentEv',
    )

  def yzMeshResolution(self) -> QSize:
    """
    Calls Qt's 'QSize Qt3DExtras::QCuboidMesh::yzMeshResolution() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qcuboidmesh.html#yzMeshResolution

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize Qt3DExtras::QCuboidMesh::yzMeshResolution() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras11QCuboidMesh16yzMeshResolutionEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def xzMeshResolution(self) -> QSize:
    """
    Calls Qt's 'QSize Qt3DExtras::QCuboidMesh::xzMeshResolution() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qcuboidmesh.html#xzMeshResolution

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize Qt3DExtras::QCuboidMesh::xzMeshResolution() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras11QCuboidMesh16xzMeshResolutionEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def xyMeshResolution(self) -> QSize:
    """
    Calls Qt's 'QSize Qt3DExtras::QCuboidMesh::xyMeshResolution() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qcuboidmesh.html#xyMeshResolution

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize Qt3DExtras::QCuboidMesh::xyMeshResolution() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras11QCuboidMesh16xyMeshResolutionEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setXExtent(self, xExtent: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QCuboidMesh::setXExtent(float xExtent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qcuboidmesh.html#setXExtent

    Parameters
    ----------

    xExtent : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QCuboidMesh::setXExtent(float xExtent)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras11QCuboidMesh10setXExtentEf', xExtent,
    )

  @overload(float)
  def setYExtent(self, yExtent: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QCuboidMesh::setYExtent(float yExtent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qcuboidmesh.html#setYExtent

    Parameters
    ----------

    yExtent : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QCuboidMesh::setYExtent(float yExtent)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras11QCuboidMesh10setYExtentEf', yExtent,
    )

  @overload(float)
  def setZExtent(self, zExtent: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QCuboidMesh::setZExtent(float zExtent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qcuboidmesh.html#setZExtent

    Parameters
    ----------

    zExtent : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QCuboidMesh::setZExtent(float zExtent)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras11QCuboidMesh10setZExtentEf', zExtent,
    )

  @overload(QSize)
  def setYZMeshResolution(self, resolution: QSize) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QCuboidMesh::setYZMeshResolution(const QSize
    &resolution)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qcuboidmesh.html#setYZMeshResolution

    Parameters
    ----------

    resolution : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void Qt3DExtras::QCuboidMesh::setYZMeshResolution(const QSize
    #      &resolution)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras11QCuboidMesh19setYZMeshResolutionERK5QSize',
        self._valueOf(resolution),
    )

  @overload(QSize)
  def setXZMeshResolution(self, resolution: QSize) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QCuboidMesh::setXZMeshResolution(const QSize
    &resolution)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qcuboidmesh.html#setXZMeshResolution

    Parameters
    ----------

    resolution : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void Qt3DExtras::QCuboidMesh::setXZMeshResolution(const QSize
    #      &resolution)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras11QCuboidMesh19setXZMeshResolutionERK5QSize',
        self._valueOf(resolution),
    )

  @overload(QSize)
  def setXYMeshResolution(self, resolution: QSize) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QCuboidMesh::setXYMeshResolution(const QSize
    &resolution)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qcuboidmesh.html#setXYMeshResolution

    Parameters
    ----------

    resolution : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void Qt3DExtras::QCuboidMesh::setXYMeshResolution(const QSize
    #      &resolution)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras11QCuboidMesh19setXYMeshResolutionERK5QSize',
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
    'Qt3DExtras::QCuboidMesh::QCuboidMesh(Qt3DCore::QNode *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qcuboidmesh.html#QCuboidMesh

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DExtras::QCuboidMesh::QCuboidMesh(Qt3DCore::QNode *parent)
    self._noteCreation(QCuboidMesh, lambda: Rituals.call(
        'ritual_ZN10Qt3DExtras11QCuboidMeshC1EPN8Qt3DCore5QNodeE',
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

  @overload(float)
  def xExtentChanged(self, xExtent: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QCuboidMesh::xExtentChanged(float xExtent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qcuboidmesh.html#xExtentChanged

    Parameters
    ----------

    xExtent : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QCuboidMesh::xExtentChanged(float xExtent)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras11QCuboidMesh14xExtentChangedEf', xExtent,
    )

  @overload(float)
  def yExtentChanged(self, yExtent: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QCuboidMesh::yExtentChanged(float yExtent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qcuboidmesh.html#yExtentChanged

    Parameters
    ----------

    yExtent : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QCuboidMesh::yExtentChanged(float yExtent)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras11QCuboidMesh14yExtentChangedEf', yExtent,
    )

  @overload(float)
  def zExtentChanged(self, zExtent: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QCuboidMesh::zExtentChanged(float zExtent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qcuboidmesh.html#zExtentChanged

    Parameters
    ----------

    zExtent : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QCuboidMesh::zExtentChanged(float zExtent)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras11QCuboidMesh14zExtentChangedEf', zExtent,
    )

  @overload(QSize)
  def yzMeshResolutionChanged(self, yzMeshResolution: QSize) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QCuboidMesh::yzMeshResolutionChanged(const
    QSize &yzMeshResolution)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qcuboidmesh.html

    Parameters
    ----------

    yzMeshResolution : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void Qt3DExtras::QCuboidMesh::yzMeshResolutionChanged(const QSize
    #      &yzMeshResolution)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras11QCuboidMesh23yzMeshResolutionChangedERK5QSi'
        'ze',
        self._valueOf(yzMeshResolution),
    )

  @overload(QSize)
  def xzMeshResolutionChanged(self, xzMeshResolution: QSize) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QCuboidMesh::xzMeshResolutionChanged(const
    QSize &xzMeshResolution)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qcuboidmesh.html

    Parameters
    ----------

    xzMeshResolution : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void Qt3DExtras::QCuboidMesh::xzMeshResolutionChanged(const QSize
    #      &xzMeshResolution)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras11QCuboidMesh23xzMeshResolutionChangedERK5QSi'
        'ze',
        self._valueOf(xzMeshResolution),
    )

  @overload(QSize)
  def xyMeshResolutionChanged(self, xyMeshResolution: QSize) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QCuboidMesh::xyMeshResolutionChanged(const
    QSize &xyMeshResolution)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qcuboidmesh.html

    Parameters
    ----------

    xyMeshResolution : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void Qt3DExtras::QCuboidMesh::xyMeshResolutionChanged(const QSize
    #      &xyMeshResolution)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras11QCuboidMesh23xyMeshResolutionChangedERK5QSi'
        'ze',
        self._valueOf(xyMeshResolution),
    )
