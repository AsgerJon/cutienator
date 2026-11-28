"""
QGeoTiledMapScene binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qgeotiledmapscene_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QGeoTiledMapScene to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QRectF, QSize
  from ..QtQuick import QQuickWindow, QSGNode
  from . import QGeoCameraData, QGeoTiledMapScenePrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGeoCameraData = WAIT['QGeoCameraData']
  QQuickWindow = WAIT['QQuickWindow']
  QRectF = WAIT['QRectF']
  QSGNode = WAIT['QSGNode']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGeoTiledMapScene(QObject):
  """
  The cute side of Qt's QGeoTiledMapScene: a plain Python object standing in
  front of one C++ QGeoTiledMapScene.

  It is built on the cute 'QObject', as Qt's QGeoTiledMapScene is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGeoTiledMapScene that has a ritual and that Python
  can call so far, 10 names in all: 'metaObject', 'tr', 'd_func',
  'setScreenSize', 'setTileSize', 'setCameraData', 'setVisibleArea',
  'updateSceneGraph', 'clearTexturedTiles', 'updateSceneParameters'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QGeoTiledMapScene::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QGeoTiledMapScene::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'const QGeoTiledMapScenePrivate *QGeoTiledMapScene::d_func() const':
    takes in Python what 'QGeoTiledMapScenePrivate
    *QGeoTiledMapScene::d_func()' takes.
  - Qt's 'QGeoTiledMapScene::~QGeoTiledMapScene()': the destructor: Python
    never removes a C++ QGeoTiledMapScene.
  - Qt's 'void QGeoTiledMapScene::setVisibleTiles(const QSet<QGeoTileSpec>
    &tiles)': takes a type Python has no way to hand over yet.
  - Qt's 'const QSet<QGeoTileSpec> &QGeoTiledMapScene::visibleTiles() const':
    gives a type Python has no way to take yet.
  - Qt's 'void QGeoTiledMapScene::addTile(const QGeoTileSpec &spec,
    QSharedPointer<QGeoTileTexture> texture)': takes a type Python has no way
    to hand over yet.
  - Qt's 'QSet<QGeoTileSpec> QGeoTiledMapScene::texturedTiles()': gives a
    type Python has no way to take yet.
  - Qt's 'void QGeoTiledMapScene::newTilesVisible(const QSet<QGeoTileSpec>
    &newTiles)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 24 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QGeoTiledMapScene is created at the first use, not by
    'QGeoTiledMapScene(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGeoTiledMapScene.
  - Qt tells when it has removed the C++ QGeoTiledMapScene. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QGeoTiledMapScene that has no cute function yet,
    'addTile', 'newTilesVisible', 'setVisibleTiles', 'texturedTiles',
    'visibleTiles', holds a function that raises 'NotImplementedError', and
    its docstring says why.
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
    Calls Qt's 'QString QGeoTiledMapScene::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeotiledmapscene.html#tr

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
    #  QString QGeoTiledMapScene::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QGeoTiledMapScene2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoTiledMapScene'

  #  A C++ QGeoTiledMapScene Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGeoTiledMapScene'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QGeoTiledMapScene::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeotiledmapscene.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QGeoTiledMapScene::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QGeoTiledMapScene10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSize)
  def setScreenSize(self, size: QSize) -> None:
    """
    Calls Qt's 'void QGeoTiledMapScene::setScreenSize(const QSize &size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeotiledmapscene.html#setScreenSize

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QGeoTiledMapScene::setScreenSize(const QSize &size)
    self.uglySide.call(
        'ritual_ZN17QGeoTiledMapScene13setScreenSizeERK5QSize',
        self._valueOf(size),
    )

  @overload(int)
  def setTileSize(self, tileSize: int) -> None:
    """
    Calls Qt's 'void QGeoTiledMapScene::setTileSize(int tileSize)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeotiledmapscene.html#setTileSize

    Parameters
    ----------

    tileSize : int
      Passed on as it is.
    """
    #  void QGeoTiledMapScene::setTileSize(int tileSize)
    self.uglySide.call(
        'ritual_ZN17QGeoTiledMapScene11setTileSizeEi', tileSize,
    )

  @overload(QGeoCameraData)
  def setCameraData(self, cameraData: QGeoCameraData) -> None:
    """
    Calls Qt's 'void QGeoTiledMapScene::setCameraData(const QGeoCameraData
    &cameraData)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeotiledmapscene.html#setCameraData

    Parameters
    ----------

    cameraData : QGeoCameraData
      Passed on as a value: Qt reads the C++ QGeoCameraData, which stays
      Python's own.
    """
    #  void QGeoTiledMapScene::setCameraData(const QGeoCameraData
    #      &cameraData)
    self.uglySide.call(
        'ritual_ZN17QGeoTiledMapScene13setCameraDataERK14QGeoCameraData',
        self._valueOf(cameraData),
    )

  @overload(QRectF)
  def setVisibleArea(self, visibleArea: QRectF) -> None:
    """
    Calls Qt's 'void QGeoTiledMapScene::setVisibleArea(const QRectF
    &visibleArea)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeotiledmapscene.html#setVisibleArea

    Parameters
    ----------

    visibleArea : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QGeoTiledMapScene::setVisibleArea(const QRectF &visibleArea)
    self.uglySide.call(
        'ritual_ZN17QGeoTiledMapScene14setVisibleAreaERK6QRectF',
        self._valueOf(visibleArea),
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QGeoTiledMapScene::QGeoTiledMapScene(QObject *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeotiledmapscene.html#QGeoTiledMapScene

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QGeoTiledMapScene::QGeoTiledMapScene(QObject *parent)
    self._noteCreation(QGeoTiledMapScene, lambda: Rituals.call(
        'ritual_ZN17QGeoTiledMapSceneC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  def d_func(self) -> Optional[QGeoTiledMapScenePrivate]:
    """
    Calls Qt's 'QGeoTiledMapScenePrivate *QGeoTiledMapScene::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qgeotiledmapscene.html#d_func

    Returns
    -------

    Optional[QGeoTiledMapScenePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGeoTiledMapScenePrivate *QGeoTiledMapScene::d_func()
    address = self.uglySide.call('ritual_ZN17QGeoTiledMapScene6d_funcEv')
    from . import QGeoTiledMapScenePrivate
    return QGeoTiledMapScenePrivate._cuteAt(address)

  @overload(QSGNode, QQuickWindow)
  @overload(QSGNode, NoneType)
  @overload(NoneType, QQuickWindow)
  @overload(NoneType, NoneType)
  def updateSceneGraph(
      self,
      oldNode: Optional[QSGNode],
      window: Optional[QQuickWindow],
  ) -> Optional[QSGNode]:
    """
    Calls Qt's 'QSGNode *QGeoTiledMapScene::updateSceneGraph(QSGNode
    *oldNode, QQuickWindow *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeotiledmapscene.html#updateSceneGraph

    Parameters
    ----------

    oldNode : Optional[QSGNode]
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
    #  QSGNode *QGeoTiledMapScene::updateSceneGraph(QSGNode *oldNode,
    #      QQuickWindow *window)
    address = self.uglySide.call(
        'ritual_ZN17QGeoTiledMapScene16updateSceneGraphEP7QSGNodeP12QQuickW'
        'indow',
        self._addressOf(oldNode, 'QSGNode'), self._addressOf(window),
    )
    from ..QtQuick import QSGNode
    return QSGNode._cuteAt(address)

  def clearTexturedTiles(self) -> None:
    """
    Calls Qt's 'void QGeoTiledMapScene::clearTexturedTiles()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeotiledmapscene.html#clearTexturedTiles
    """
    #  void QGeoTiledMapScene::clearTexturedTiles()
    self.uglySide.call('ritual_ZN17QGeoTiledMapScene18clearTexturedTilesEv')

  def updateSceneParameters(self) -> None:
    """
    Calls Qt's 'void QGeoTiledMapScene::updateSceneParameters()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeotiledmapscene.html#updateSceneParameters
    """
    #  void QGeoTiledMapScene::updateSceneParameters()
    self.uglySide.call(
        'ritual_ZN17QGeoTiledMapScene21updateSceneParametersEv',
    )

  @staticmethod
  def addTile(*__, **_) -> Never:
    """
    Qt's 'void QGeoTiledMapScene::addTile(const QGeoTileSpec &spec,
    QSharedPointer<QGeoTileTexture> texture)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'QGeoTiledMapScene.addTile' has no cute function yet. Qt's 'void "
        "QGeoTiledMapScene::addTile(const QGeoTileSpec &spec, "
        "QSharedPointer<QGeoTileTexture> texture)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def newTilesVisible(*__, **_) -> Never:
    """
    Qt's 'void QGeoTiledMapScene::newTilesVisible(const QSet<QGeoTileSpec>
    &newTiles)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QGeoTiledMapScene.newTilesVisible' has no cute function yet. Qt's "
        "'void QGeoTiledMapScene::newTilesVisible(const QSet<QGeoTileSpec> "
        "&newTiles)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def setVisibleTiles(*__, **_) -> Never:
    """
    Qt's 'void QGeoTiledMapScene::setVisibleTiles(const QSet<QGeoTileSpec>
    &tiles)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QGeoTiledMapScene.setVisibleTiles' has no cute function yet. Qt's "
        "'void QGeoTiledMapScene::setVisibleTiles(const QSet<QGeoTileSpec> "
        "&tiles)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def texturedTiles(*__, **_) -> Never:
    """
    Qt's 'QSet<QGeoTileSpec> QGeoTiledMapScene::texturedTiles()': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QGeoTiledMapScene.texturedTiles' has no cute function yet. Qt's "
        "'QSet<QGeoTileSpec> QGeoTiledMapScene::texturedTiles()': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def visibleTiles(*__, **_) -> Never:
    """
    Qt's 'const QSet<QGeoTileSpec> &QGeoTiledMapScene::visibleTiles() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QGeoTiledMapScene.visibleTiles' has no cute function yet. Qt's "
        "'const QSet<QGeoTileSpec> &QGeoTiledMapScene::visibleTiles() "
        "const': gives a type Python has no way to take yet.")
