"""
QGeoTiledMapPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qgeotiledmap_p_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QGeoTiledMapPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QGeoMapPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QRectF, QSize
  from ..QtQuick import QQuickWindow, QSGNode
  from . import QGeoCameraCapabilities, QGeoCameraData, QGeoMapType
  from . import QGeoTileSpec, QGeoTiledMap, QGeoTiledMappingManagerEngine
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGeoCameraCapabilities = WAIT['QGeoCameraCapabilities']
  QGeoCameraData = WAIT['QGeoCameraData']
  QGeoMapType = WAIT['QGeoMapType']
  QGeoTileSpec = WAIT['QGeoTileSpec']
  QGeoTiledMappingManagerEngine = WAIT['QGeoTiledMappingManagerEngine']
  QQuickWindow = WAIT['QQuickWindow']
  QRectF = WAIT['QRectF']
  QSGNode = WAIT['QSGNode']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGeoTiledMapPrivate(QGeoMapPrivate):
  """
  The cute side of Qt's QGeoTiledMapPrivate: a plain Python object standing
  in front of one C++ QGeoTiledMapPrivate.

  It is built on the cute 'QGeoMapPrivate', as Qt's QGeoTiledMapPrivate is
  built on Qt's QGeoMapPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGeoTiledMapPrivate that has a ritual and that
  Python can call so far, 14 names in all: 'q_func', 'updateSceneGraph',
  'updateTile', 'prefetchTiles', 'activeMapType',
  'onCameraCapabilitiesChanged', 'changeViewportSize', 'changeCameraData',
  'changeActiveMapType', 'changeTileVersion', 'clearScene', 'updateScene',
  'setVisibleArea', 'visibleArea'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QGeoTiledMap *QGeoTiledMapPrivate::q_func() const': takes in
    Python what 'QGeoTiledMap *QGeoTiledMapPrivate::q_func()' takes.
  - Qt's 'QGeoTiledMapPrivate::~QGeoTiledMapPrivate()': the destructor:
    Python never removes a C++ QGeoTiledMapPrivate.

  What has no ritual
  ------------------

  2 of the 19 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QGeoTiledMapPrivate is created at the first use, not by
    'QGeoTiledMapPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGeoTiledMapPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoTiledMapPrivate'

  #  A C++ QGeoTiledMapPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGeoTiledMapPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def activeMapType(self) -> QGeoMapType:
    """
    Calls Qt's 'QGeoMapType QGeoTiledMapPrivate::activeMapType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeotiledmapprivate.html#activeMapType

    Returns
    -------

    QGeoMapType
      A new cute QGeoMapType around the copy Qt gave back. Python owns it.
    """
    #  QGeoMapType QGeoTiledMapPrivate::activeMapType() const
    address = self.uglySide.call(
        'ritual_ZNK19QGeoTiledMapPrivate13activeMapTypeEv',
    )
    from . import QGeoMapType
    return QGeoMapType._cuteOwning(address)

  def visibleArea(self) -> QRectF:
    """
    Calls Qt's 'QRectF QGeoTiledMapPrivate::visibleArea() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeotiledmapprivate.html#visibleArea

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QGeoTiledMapPrivate::visibleArea() const
    ritual = 'ritual_ZNK19QGeoTiledMapPrivate11visibleAreaEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QGeoTiledMapPrivate11visibleAreaEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRectF)
  def setVisibleArea(self, visibleArea: QRectF) -> None:
    """
    Calls Qt's 'void QGeoTiledMapPrivate::setVisibleArea(const QRectF
    &visibleArea)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeotiledmapprivate.html#setVisibleArea

    Parameters
    ----------

    visibleArea : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QGeoTiledMapPrivate::setVisibleArea(const QRectF &visibleArea)
    ritual = 'ritual_ZN19QGeoTiledMapPrivate14setVisibleAreaERK6QRectF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QGeoTiledMapPrivate14setVisibleAreaERK6QRectF'
    self.uglySide.call(ritual, self._valueOf(visibleArea))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QGeoTiledMappingManagerEngine)
  @overload(NoneType)
  def __init__(
      self,
      engine: Optional[QGeoTiledMappingManagerEngine],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QGeoTiledMapPrivate::QGeoTiledMapPrivate(QGeoTiledMappingManagerEngine
    *engine)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeotiledmapprivate.html#QGeoTiledMapPrivate

    Parameters
    ----------

    engine : Optional[QGeoTiledMappingManagerEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QGeoTiledMapPrivate::QGeoTiledMapPrivate(QGeoTiledMappingManagerEngine
    #      *engine)
    self._noteCreation(QGeoTiledMapPrivate, lambda: Rituals.call(
        'ritual_ZN19QGeoTiledMapPrivateC1EP29QGeoTiledMappingManagerEngine',
        self._addressOf(engine),
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

  def q_func(self) -> Optional[QGeoTiledMap]:
    """
    Calls Qt's 'QGeoTiledMap *QGeoTiledMapPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qgeotiledmapprivate.html#q_func

    Returns
    -------

    Optional[QGeoTiledMap]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGeoTiledMap *QGeoTiledMapPrivate::q_func()
    address = self.uglySide.call('ritual_ZN19QGeoTiledMapPrivate6q_funcEv')
    from . import QGeoTiledMap
    return QGeoTiledMap._cuteAt(address)

  @overload(QSGNode, QQuickWindow)
  @overload(QSGNode, NoneType)
  @overload(NoneType, QQuickWindow)
  @overload(NoneType, NoneType)
  def updateSceneGraph(
      self,
      node: Optional[QSGNode],
      window: Optional[QQuickWindow],
  ) -> Optional[QSGNode]:
    """
    Calls Qt's 'QSGNode *QGeoTiledMapPrivate::updateSceneGraph(QSGNode *node,
    QQuickWindow *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeotiledmapprivate.html#updateSceneGraph

    Parameters
    ----------

    node : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSGNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGNode *QGeoTiledMapPrivate::updateSceneGraph(QSGNode *node,
    #      QQuickWindow *window)
    address = self.uglySide.call(
        'ritual_ZN19QGeoTiledMapPrivate16updateSceneGraphEP7QSGNodeP12QQuic'
        'kWindow',
        self._addressOf(node, 'QSGNode'), self._addressOf(window),
    )
    from ..QtQuick import QSGNode
    return QSGNode._cuteAt(address)

  @overload(QGeoTileSpec)
  def updateTile(self, spec: QGeoTileSpec) -> None:
    """
    Calls Qt's 'void QGeoTiledMapPrivate::updateTile(const QGeoTileSpec
    &spec)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeotiledmapprivate.html#updateTile

    Parameters
    ----------

    spec : QGeoTileSpec
      Passed on as a value: Qt reads the C++ QGeoTileSpec, which stays
      Python's own.
    """
    #  void QGeoTiledMapPrivate::updateTile(const QGeoTileSpec &spec)
    self.uglySide.call(
        'ritual_ZN19QGeoTiledMapPrivate10updateTileERK12QGeoTileSpec',
        self._valueOf(spec),
    )

  def prefetchTiles(self) -> None:
    """
    Calls Qt's 'void QGeoTiledMapPrivate::prefetchTiles()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeotiledmapprivate.html#prefetchTiles
    """
    #  void QGeoTiledMapPrivate::prefetchTiles()
    self.uglySide.call('ritual_ZN19QGeoTiledMapPrivate13prefetchTilesEv')

  @overload(QGeoCameraCapabilities)
  def onCameraCapabilitiesChanged(
      self,
      oldCameraCapabilities: QGeoCameraCapabilities,
  ) -> None:
    """
    Calls Qt's 'void QGeoTiledMapPrivate::onCameraCapabilitiesChanged(const
    QGeoCameraCapabilities &oldCameraCapabilities)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeotiledmapprivate.html

    Parameters
    ----------

    oldCameraCapabilities : QGeoCameraCapabilities
      Passed on as a value: Qt reads the C++ QGeoCameraCapabilities, which
      stays Python's own.
    """
    #  void QGeoTiledMapPrivate::onCameraCapabilitiesChanged(const
    #      QGeoCameraCapabilities &oldCameraCapabilities)
    self.uglySide.call(
        'ritual_ZN19QGeoTiledMapPrivate27onCameraCapabilitiesChangedERK22QG'
        'eoCameraCapabilities',
        self._valueOf(oldCameraCapabilities),
    )

  @overload(QSize)
  def changeViewportSize(self, size: QSize) -> None:
    """
    Calls Qt's 'void QGeoTiledMapPrivate::changeViewportSize(const QSize
    &size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeotiledmapprivate.html#changeViewportSize

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QGeoTiledMapPrivate::changeViewportSize(const QSize &size)
    ritual = 'ritual_ZN19QGeoTiledMapPrivate18changeViewportSizeERK5QSize'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QGeoTiledMapPrivate18changeViewportSizeERK5QSize')
    self.uglySide.call(ritual, self._valueOf(size))

  @overload(QGeoCameraData)
  def changeCameraData(self, cameraData: QGeoCameraData) -> None:
    """
    Calls Qt's 'void QGeoTiledMapPrivate::changeCameraData(const
    QGeoCameraData &cameraData)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeotiledmapprivate.html#changeCameraData

    Parameters
    ----------

    cameraData : QGeoCameraData
      Passed on as a value: Qt reads the C++ QGeoCameraData, which stays
      Python's own.
    """
    #  void QGeoTiledMapPrivate::changeCameraData(const QGeoCameraData
    #      &cameraData)
    ritual = (
        'ritual_ZN19QGeoTiledMapPrivate16changeCameraDataERK14QGeoCameraDat'
        'a')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QGeoTiledMapPrivate16changeCameraDataERK14QGeoCam'
          'eraData')
    self.uglySide.call(ritual, self._valueOf(cameraData))

  @overload(QGeoMapType)
  def changeActiveMapType(self, mapType: QGeoMapType) -> None:
    """
    Calls Qt's 'void QGeoTiledMapPrivate::changeActiveMapType(const
    QGeoMapType &mapType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeotiledmapprivate.html#changeActiveMapType

    Parameters
    ----------

    mapType : QGeoMapType
      Passed on as a value: Qt reads the C++ QGeoMapType, which stays
      Python's own.
    """
    #  void QGeoTiledMapPrivate::changeActiveMapType(const QGeoMapType
    #      &mapType)
    ritual = (
        'ritual_ZN19QGeoTiledMapPrivate19changeActiveMapTypeERK11QGeoMapTyp'
        'e')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QGeoTiledMapPrivate19changeActiveMapTypeERK11QGeo'
          'MapType')
    self.uglySide.call(ritual, self._valueOf(mapType))

  @overload(int)
  def changeTileVersion(self, version: int) -> None:
    """
    Calls Qt's 'void QGeoTiledMapPrivate::changeTileVersion(int version)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeotiledmapprivate.html#changeTileVersion

    Parameters
    ----------

    version : int
      Passed on as it is.
    """
    #  void QGeoTiledMapPrivate::changeTileVersion(int version)
    self.uglySide.call(
        'ritual_ZN19QGeoTiledMapPrivate17changeTileVersionEi', version,
    )

  def clearScene(self) -> None:
    """
    Calls Qt's 'void QGeoTiledMapPrivate::clearScene()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeotiledmapprivate.html#clearScene
    """
    #  void QGeoTiledMapPrivate::clearScene()
    self.uglySide.call('ritual_ZN19QGeoTiledMapPrivate10clearSceneEv')

  def updateScene(self) -> None:
    """
    Calls Qt's 'void QGeoTiledMapPrivate::updateScene()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeotiledmapprivate.html#updateScene
    """
    #  void QGeoTiledMapPrivate::updateScene()
    self.uglySide.call('ritual_ZN19QGeoTiledMapPrivate11updateSceneEv')
