"""
QGeoCameraTiles binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qgeocameratiles_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QGeoCameraTiles to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QRectF, QSize
  from . import QGeoCameraData, QGeoMapType
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGeoCameraData = WAIT['QGeoCameraData']
  QGeoMapType = WAIT['QGeoMapType']
  QRectF = WAIT['QRectF']
  QSize = WAIT['QSize']


class QGeoCameraTiles(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QGeoCameraTiles: a plain Python object standing in
  front of one C++ QGeoCameraTiles.

  What exists
  -----------

  Every function of Qt's QGeoCameraTiles that has a ritual and that Python
  can call so far, 11 names in all: 'setCameraData', 'cameraData',
  'setVisibleArea', 'setScreenSize', 'setTileSize', 'tileSize',
  'setViewExpansion', 'setPluginString', 'setMapType', 'activeMapType',
  'setMapVersion'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGeoCameraTiles::~QGeoCameraTiles()': the destructor: Python never
    removes a C++ QGeoCameraTiles.
  - Qt's 'const QSet<QGeoTileSpec> &QGeoCameraTiles::createTiles()': gives a
    type Python has no way to take yet.

  What has no ritual
  ------------------

  2 of the 16 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QGeoCameraTiles is created at the first use, not by
    'QGeoCameraTiles(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGeoCameraTiles.
  - Each name of Qt's QGeoCameraTiles that has no cute function yet,
    'createTiles', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoCameraTiles'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def cameraData(self) -> QGeoCameraData:
    """
    Calls Qt's 'QGeoCameraData QGeoCameraTiles::cameraData() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocameratiles.html#cameraData

    Returns
    -------

    QGeoCameraData
      A new cute QGeoCameraData around the copy Qt gave back. Python owns it.
    """
    #  QGeoCameraData QGeoCameraTiles::cameraData() const
    address = self.uglySide.call('ritual_ZNK15QGeoCameraTiles10cameraDataEv')
    from . import QGeoCameraData
    return QGeoCameraData._cuteOwning(address)

  def tileSize(self) -> int:
    """
    Calls Qt's 'int QGeoCameraTiles::tileSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocameratiles.html#tileSize
    """
    #  int QGeoCameraTiles::tileSize() const
    return self.uglySide.call('ritual_ZNK15QGeoCameraTiles8tileSizeEv')

  def activeMapType(self) -> QGeoMapType:
    """
    Calls Qt's 'QGeoMapType QGeoCameraTiles::activeMapType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocameratiles.html#activeMapType

    Returns
    -------

    QGeoMapType
      A new cute QGeoMapType around the copy Qt gave back. Python owns it.
    """
    #  QGeoMapType QGeoCameraTiles::activeMapType() const
    address = self.uglySide.call(
        'ritual_ZNK15QGeoCameraTiles13activeMapTypeEv',
    )
    from . import QGeoMapType
    return QGeoMapType._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QGeoCameraData)
  def setCameraData(self, camera: QGeoCameraData) -> None:
    """
    Calls Qt's 'void QGeoCameraTiles::setCameraData(const QGeoCameraData
    &camera)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocameratiles.html#setCameraData

    Parameters
    ----------

    camera : QGeoCameraData
      Passed on as a value: Qt reads the C++ QGeoCameraData, which stays
      Python's own.
    """
    #  void QGeoCameraTiles::setCameraData(const QGeoCameraData &camera)
    self.uglySide.call(
        'ritual_ZN15QGeoCameraTiles13setCameraDataERK14QGeoCameraData',
        self._valueOf(camera),
    )

  @overload(QRectF)
  def setVisibleArea(self, visibleArea: QRectF) -> None:
    """
    Calls Qt's 'void QGeoCameraTiles::setVisibleArea(const QRectF
    &visibleArea)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocameratiles.html#setVisibleArea

    Parameters
    ----------

    visibleArea : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QGeoCameraTiles::setVisibleArea(const QRectF &visibleArea)
    self.uglySide.call(
        'ritual_ZN15QGeoCameraTiles14setVisibleAreaERK6QRectF',
        self._valueOf(visibleArea),
    )

  @overload(QSize)
  def setScreenSize(self, size: QSize) -> None:
    """
    Calls Qt's 'void QGeoCameraTiles::setScreenSize(const QSize &size)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocameratiles.html#setScreenSize

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QGeoCameraTiles::setScreenSize(const QSize &size)
    self.uglySide.call(
        'ritual_ZN15QGeoCameraTiles13setScreenSizeERK5QSize',
        self._valueOf(size),
    )

  @overload(int)
  def setTileSize(self, tileSize: int) -> None:
    """
    Calls Qt's 'void QGeoCameraTiles::setTileSize(int tileSize)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocameratiles.html#setTileSize

    Parameters
    ----------

    tileSize : int
      Passed on as it is.
    """
    #  void QGeoCameraTiles::setTileSize(int tileSize)
    self.uglySide.call('ritual_ZN15QGeoCameraTiles11setTileSizeEi', tileSize)

  @overload(float)
  def setViewExpansion(self, viewExpansion: float) -> None:
    """
    Calls Qt's 'void QGeoCameraTiles::setViewExpansion(double
    viewExpansion)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocameratiles.html#setViewExpansion

    Parameters
    ----------

    viewExpansion : float
      Passed on as it is.
    """
    #  void QGeoCameraTiles::setViewExpansion(double viewExpansion)
    self.uglySide.call(
        'ritual_ZN15QGeoCameraTiles16setViewExpansionEd', viewExpansion,
    )

  @overload(str)
  def setPluginString(self, pluginString: str) -> None:
    """
    Calls Qt's 'void QGeoCameraTiles::setPluginString(const QString
    &pluginString)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocameratiles.html#setPluginString

    Parameters
    ----------

    pluginString : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QGeoCameraTiles::setPluginString(const QString &pluginString)
    self.uglySide.call(
        'ritual_ZN15QGeoCameraTiles15setPluginStringERK7QString',
        pluginString,
    )

  @overload(QGeoMapType)
  def setMapType(self, mapType: QGeoMapType) -> None:
    """
    Calls Qt's 'void QGeoCameraTiles::setMapType(const QGeoMapType
    &mapType)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocameratiles.html#setMapType

    Parameters
    ----------

    mapType : QGeoMapType
      Passed on as a value: Qt reads the C++ QGeoMapType, which stays
      Python's own.
    """
    #  void QGeoCameraTiles::setMapType(const QGeoMapType &mapType)
    self.uglySide.call(
        'ritual_ZN15QGeoCameraTiles10setMapTypeERK11QGeoMapType',
        self._valueOf(mapType),
    )

  @overload(int)
  def setMapVersion(self, mapVersion: int) -> None:
    """
    Calls Qt's 'void QGeoCameraTiles::setMapVersion(int mapVersion)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocameratiles.html#setMapVersion

    Parameters
    ----------

    mapVersion : int
      Passed on as it is.
    """
    #  void QGeoCameraTiles::setMapVersion(int mapVersion)
    self.uglySide.call(
        'ritual_ZN15QGeoCameraTiles13setMapVersionEi', mapVersion,
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
    Notes what was given, for Qt's 'QGeoCameraTiles::QGeoCameraTiles()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocameratiles.html#QGeoCameraTiles
    """
    #  QGeoCameraTiles::QGeoCameraTiles()
    self._noteCreation(QGeoCameraTiles, lambda: Rituals.call(
        'ritual_ZN15QGeoCameraTilesC1Ev',
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
  def createTiles(*__, **_) -> Never:
    """
    Qt's 'const QSet<QGeoTileSpec> &QGeoCameraTiles::createTiles()': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QGeoCameraTiles.createTiles' has no cute function yet. Qt's "
        "'const QSet<QGeoTileSpec> &QGeoCameraTiles::createTiles()': gives "
        "a type Python has no way to take yet.")
