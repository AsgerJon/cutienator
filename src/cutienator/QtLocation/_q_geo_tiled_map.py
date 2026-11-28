"""
QGeoTiledMap binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qgeotiledmap_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QGeoTiledMap to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QGeoMap

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtQuick import QQuickWindow, QSGNode
  from . import QAbstractGeoTileCache, QGeoTileRequestManager, QGeoTileSpec
  from . import QGeoTiledMapPrivate, QGeoTiledMappingManagerEngine
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGeoTileSpec = WAIT['QGeoTileSpec']
  QGeoTiledMappingManagerEngine = WAIT['QGeoTiledMappingManagerEngine']
  QQuickWindow = WAIT['QQuickWindow']
  QSGNode = WAIT['QSGNode']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGeoTiledMap(QGeoMap):
  """
  The cute side of Qt's QGeoTiledMap: a plain Python object standing in front
  of one C++ QGeoTiledMap.

  It is built on the cute 'QGeoMap', as Qt's QGeoTiledMap is built on Qt's
  QGeoMap, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGeoTiledMap that has a ritual and that Python can
  call so far, 14 names in all: 'metaObject', 'tr', 'd_func', 'tileCache',
  'requestManager', 'updateTile', 'setPrefetchStyle', 'prefetchData',
  'clearData', 'capabilities', 'setCopyrightVisible', 'clearScene',
  'updateSceneGraph', 'handleTileVersionChanged'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QGeoTiledMap::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QGeoTiledMap::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'const QGeoTiledMapPrivate *QGeoTiledMap::d_func() const': takes in
    Python what 'QGeoTiledMapPrivate *QGeoTiledMap::d_func()' takes.
  - Qt's 'QGeoTiledMap::~QGeoTiledMap()': the destructor: Python never
    removes a C++ QGeoTiledMap.
  - Qt's 'void QGeoTiledMap::evaluateCopyrights(const QSet<QGeoTileSpec>
    &visibleTiles)': takes a type Python has no way to hand over yet.
  - Qt's 'QGeoTiledMap::QGeoTiledMap(QGeoTiledMapPrivate &dd,
    QGeoTiledMappingManagerEngine *engine, QObject *parent)': takes a type
    Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 25 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QGeoTiledMap is created at the first use, not by
    'QGeoTiledMap(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGeoTiledMap.
  - Qt tells when it has removed the C++ QGeoTiledMap. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QGeoTiledMap that has no cute function yet,
    'evaluateCopyrights', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  #  The enums Qt writes inside QGeoTiledMap, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class PrefetchStyle(CuteNum):
    """
    The enum 'QGeoTiledMap::PrefetchStyle' of Qt, with the 3 names Qt gives
    in it.
    """

    NoPrefetching = Kee[int](0)
    PrefetchNeighbourLayer = Kee[int](1)
    PrefetchTwoNeighbourLayers = Kee[int](2)

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
    Calls Qt's 'QString QGeoTiledMap::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeotiledmap.html#tr

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
    #  QString QGeoTiledMap::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN12QGeoTiledMap2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoTiledMap'

  #  A C++ QGeoTiledMap Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGeoTiledMap'

  #  The functions Qt calls itself that QGeoTiledMap is the first to declare
  #  and that cannot be handed to Python yet, each as Qt declares it. A class
  #  of a program that writes one of them anew is refused, since Qt would
  #  never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'evaluateCopyrights': (
          'void QGeoTiledMap::evaluateCopyrights(const QSet<QGeoTileSpec> '
          '&)',
      ),
  }

  #  The functions Qt calls itself that QGeoTiledMap is the first to declare.
  #  A class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'clearScene': (
          ('_ZN12QGeoTiledMap10clearSceneEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QGeoTiledMap::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeotiledmap.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QGeoTiledMap::metaObject() const
    address = self.uglySide.call('ritual_ZNK12QGeoTiledMap10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def capabilities(self) -> QGeoMap.Capabilities:
    """
    Calls Qt's 'Capabilities QGeoTiledMap::capabilities() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeotiledmap.html#capabilities

    Returns
    -------

    QGeoMap.Capabilities
      The value standing for the combination Qt gave back.
    """
    #  Capabilities QGeoTiledMap::capabilities() const
    ritual = 'ritual_ZNK12QGeoTiledMap12capabilitiesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12QGeoTiledMap12capabilitiesEv'
    return QGeoMap.Capabilities(self.uglySide.call(ritual))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(PrefetchStyle)
  def setPrefetchStyle(self, style: PrefetchStyle) -> None:
    """
    Calls Qt's 'void QGeoTiledMap::setPrefetchStyle(PrefetchStyle style)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeotiledmap.html#setPrefetchStyle

    Parameters
    ----------

    style : PrefetchStyle
      Passed on as its number.
    """
    #  void QGeoTiledMap::setPrefetchStyle(PrefetchStyle style)
    self.uglySide.call(
        'ritual_ZN12QGeoTiledMap16setPrefetchStyleENS_13PrefetchStyleE',
        style.value,
    )

  @overload(bool)
  def setCopyrightVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void QGeoTiledMap::setCopyrightVisible(bool visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeotiledmap.html#setCopyrightVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QGeoTiledMap::setCopyrightVisible(bool visible)
    ritual = 'ritual_ZN12QGeoTiledMap19setCopyrightVisibleEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QGeoTiledMap19setCopyrightVisibleEb'
    self.uglySide.call(ritual, visible)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QGeoTiledMappingManagerEngine, QObject)
  @overload(QGeoTiledMappingManagerEngine, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      engine: Optional[QGeoTiledMappingManagerEngine],
      parent: Optional[QObject],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QGeoTiledMap::QGeoTiledMap(QGeoTiledMappingManagerEngine *engine,
    QObject *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qgeotiledmap.html#QGeoTiledMap

    Parameters
    ----------

    engine : Optional[QGeoTiledMappingManagerEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QGeoTiledMap::QGeoTiledMap(QGeoTiledMappingManagerEngine *engine,
    #      QObject *parent)
    self._noteCreation(QGeoTiledMap, lambda: Rituals.call(
        'ritual_ZN12QGeoTiledMapC1EP29QGeoTiledMappingManagerEngineP7QObjec'
        't',
        self._addressOf(engine), self._addressOf(parent, 'QObject'),
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

  def d_func(self) -> Optional[QGeoTiledMapPrivate]:
    """
    Calls Qt's 'QGeoTiledMapPrivate *QGeoTiledMap::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qgeotiledmap.html#d_func

    Returns
    -------

    Optional[QGeoTiledMapPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGeoTiledMapPrivate *QGeoTiledMap::d_func()
    address = self.uglySide.call('ritual_ZN12QGeoTiledMap6d_funcEv')
    from . import QGeoTiledMapPrivate
    return QGeoTiledMapPrivate._cuteAt(address)

  def tileCache(self) -> Optional[QAbstractGeoTileCache]:
    """
    Calls Qt's 'QAbstractGeoTileCache *QGeoTiledMap::tileCache()'.

    Qt's own words: https://doc.qt.io/qt-6/qgeotiledmap.html#tileCache

    Returns
    -------

    Optional[QAbstractGeoTileCache]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractGeoTileCache *QGeoTiledMap::tileCache()
    address = self.uglySide.call('ritual_ZN12QGeoTiledMap9tileCacheEv')
    from . import QAbstractGeoTileCache
    return QAbstractGeoTileCache._cuteAt(address)

  def requestManager(self) -> Optional[QGeoTileRequestManager]:
    """
    Calls Qt's 'QGeoTileRequestManager *QGeoTiledMap::requestManager()'.

    Qt's own words: https://doc.qt.io/qt-6/qgeotiledmap.html#requestManager

    Returns
    -------

    Optional[QGeoTileRequestManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGeoTileRequestManager *QGeoTiledMap::requestManager()
    address = self.uglySide.call('ritual_ZN12QGeoTiledMap14requestManagerEv')
    from . import QGeoTileRequestManager
    return QGeoTileRequestManager._cuteAt(address)

  @overload(QGeoTileSpec)
  def updateTile(self, spec: QGeoTileSpec) -> None:
    """
    Calls Qt's 'void QGeoTiledMap::updateTile(const QGeoTileSpec &spec)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeotiledmap.html#updateTile

    Parameters
    ----------

    spec : QGeoTileSpec
      Passed on as a value: Qt reads the C++ QGeoTileSpec, which stays
      Python's own.
    """
    #  void QGeoTiledMap::updateTile(const QGeoTileSpec &spec)
    self.uglySide.call(
        'ritual_ZN12QGeoTiledMap10updateTileERK12QGeoTileSpec',
        self._valueOf(spec),
    )

  def prefetchData(self) -> None:
    """
    Calls Qt's 'void QGeoTiledMap::prefetchData()'.

    Qt's own words: https://doc.qt.io/qt-6/qgeotiledmap.html#prefetchData
    """
    #  void QGeoTiledMap::prefetchData()
    ritual = 'ritual_ZN12QGeoTiledMap12prefetchDataEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QGeoTiledMap12prefetchDataEv'
    self.uglySide.call(ritual)

  def clearData(self) -> None:
    """
    Calls Qt's 'void QGeoTiledMap::clearData()'.

    Qt's own words: https://doc.qt.io/qt-6/qgeotiledmap.html#clearData
    """
    #  void QGeoTiledMap::clearData()
    ritual = 'ritual_ZN12QGeoTiledMap9clearDataEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QGeoTiledMap9clearDataEv'
    self.uglySide.call(ritual)

  @overload(int)
  def clearScene(self, mapId: int) -> None:
    """
    Calls Qt's 'void QGeoTiledMap::clearScene(int mapId)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeotiledmap.html#clearScene

    Parameters
    ----------

    mapId : int
      Passed on as it is.
    """
    #  void QGeoTiledMap::clearScene(int mapId)
    ritual = 'ritual_ZN12QGeoTiledMap10clearSceneEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QGeoTiledMap10clearSceneEi'
    self.uglySide.call(ritual, mapId)

  @overload(QSGNode, QQuickWindow)
  @overload(QSGNode, NoneType)
  @overload(NoneType, QQuickWindow)
  @overload(NoneType, NoneType)
  def updateSceneGraph(
      self,
      a0: Optional[QSGNode],
      window: Optional[QQuickWindow],
  ) -> Optional[QSGNode]:
    """
    Calls Qt's 'QSGNode *QGeoTiledMap::updateSceneGraph(QSGNode *a0,
    QQuickWindow *window)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeotiledmap.html#updateSceneGraph

    Parameters
    ----------

    a0 : Optional[QSGNode]
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
    #  QSGNode *QGeoTiledMap::updateSceneGraph(QSGNode *a0, QQuickWindow
    #      *window)
    ritual = (
        'ritual_ZN12QGeoTiledMap16updateSceneGraphEP7QSGNodeP12QQuickWindow')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN12QGeoTiledMap16updateSceneGraphEP7QSGNodeP12QQuick'
          'Window')
    address = self.uglySide.call(
        ritual, self._addressOf(a0, 'QSGNode'), self._addressOf(window),
    )
    from ..QtQuick import QSGNode
    return QSGNode._cuteAt(address)

  def handleTileVersionChanged(self) -> None:
    """
    Calls Qt's 'void QGeoTiledMap::handleTileVersionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeotiledmap.html#handleTileVersionChanged
    """
    #  void QGeoTiledMap::handleTileVersionChanged()
    self.uglySide.call('ritual_ZN12QGeoTiledMap24handleTileVersionChangedEv')

  @staticmethod
  def evaluateCopyrights(*__, **_) -> Never:
    """
    Qt's 'void QGeoTiledMap::evaluateCopyrights(const QSet<QGeoTileSpec>
    &visibleTiles)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QGeoTiledMap.evaluateCopyrights' has no cute function yet. Qt's "
        "'void QGeoTiledMap::evaluateCopyrights(const QSet<QGeoTileSpec> "
        "&visibleTiles)': takes a type Python has no way to hand over yet.")
