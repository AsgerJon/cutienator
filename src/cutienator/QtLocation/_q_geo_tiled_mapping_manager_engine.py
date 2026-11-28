"""
QGeoTiledMappingManagerEngine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qgeotiledmappingmanagerengine_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QGeoTiledMappingManagerEngine to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QAbstractGeoTileCache, QGeoMappingManagerEngine

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaObject, QSize
  from . import QGeoMap, QGeoTileFetcher, QGeoTileSpec, QGeoTiledMap
  from . import QGeoTiledMappingManagerEnginePrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QGeoTileFetcher = WAIT['QGeoTileFetcher']
  QGeoTileSpec = WAIT['QGeoTileSpec']
  QGeoTiledMap = WAIT['QGeoTiledMap']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGeoTiledMappingManagerEngine(QGeoMappingManagerEngine):
  """
  The cute side of Qt's QGeoTiledMappingManagerEngine: a plain Python object
  standing in front of one C++ QGeoTiledMappingManagerEngine.

  It is built on the cute 'QGeoMappingManagerEngine', as Qt's
  QGeoTiledMappingManagerEngine is built on Qt's QGeoMappingManagerEngine,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGeoTiledMappingManagerEngine that has a ritual and
  that Python can call so far, 19 names in all: 'metaObject', 'tr',
  'tileFetcher', 'createMap', 'releaseMap', 'tileSize', 'tileVersion',
  'tileCache', 'cacheHint', 'engineTileFinished', 'engineTileError',
  'tileError', 'tileVersionChanged', 'setTileFetcher', 'setTileSize',
  'setTileVersion', 'setCacheHint', 'setTileCache', 'd_func'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QGeoTiledMappingManagerEngine::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QGeoTiledMappingManagerEngine::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QGeoTiledMappingManagerEngine::~QGeoTiledMappingManagerEngine()':
    the destructor: Python never removes a C++ QGeoTiledMappingManagerEngine.
  - Qt's 'void QGeoTiledMappingManagerEngine::updateTileRequests(QGeoTiledMap
    *map, const QSet<QGeoTileSpec> &tilesAdded, const QSet<QGeoTileSpec>
    &tilesRemoved)': takes a type Python has no way to hand over yet.
  - Qt's 'QSharedPointer<QGeoTileTexture>
    QGeoTiledMappingManagerEngine::getTileTexture(const QGeoTileSpec &spec)':
    gives a type Python has no way to take yet.
  - Qt's 'const QGeoTiledMappingManagerEnginePrivate
    *QGeoTiledMappingManagerEngine::d_func() const': takes in Python what
    'QGeoTiledMappingManagerEnginePrivate
    *QGeoTiledMappingManagerEngine::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 30 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QGeoTiledMappingManagerEngine is created at the first use, not by
    'QGeoTiledMappingManagerEngine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGeoTiledMappingManagerEngine.
  - Qt tells when it has removed the C++ QGeoTiledMappingManagerEngine. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QGeoTiledMappingManagerEngine that has no cute function
    yet, 'getTileTexture', 'updateTileRequests', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QGeoTiledMappingManagerEngine::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeotiledmappingmanagerengine.html#tr

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
    #  QString QGeoTiledMappingManagerEngine::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN29QGeoTiledMappingManagerEngine2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoTiledMappingManagerEngine'

  #  A C++ QGeoTiledMappingManagerEngine Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGeoTiledMappingManagerEngine'

  #  The functions Qt calls itself that QGeoTiledMappingManagerEngine is the
  #  first to declare and that cannot be handed to Python yet, each as Qt
  #  declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'updateTileRequests': (
          'void '
          'QGeoTiledMappingManagerEngine::updateTileRequests(QGeoTiledMap '
          '*, const QSet<QGeoTileSpec> &, const QSet<QGeoTileSpec> &)',
      ),
      'getTileTexture': (
          'QSharedPointer<QGeoTileTexture> '
          'QGeoTiledMappingManagerEngine::getTileTexture(const '
          'QGeoTileSpec &)',
      ),
  }

  #  The functions Qt calls itself that QGeoTiledMappingManagerEngine is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'engineTileFinished': (
          ('_ZN29QGeoTiledMappingManagerEngine18engineTileFinishedERK12QGeo'
           'TileSpecRK10QByteArrayRK7QString',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtLocation:QGeoTileSpec'),
               ('address', 'value', 'QtCore:QByteArray'),
               ('address', 'text', ''),
           )),
      ),
      'engineTileError': (
          ('_ZN29QGeoTiledMappingManagerEngine15engineTileErrorERK12QGeoTil'
           'eSpecRK7QString',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtLocation:QGeoTileSpec'),
               ('address', 'text', ''),
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
    Calls Qt's 'const QMetaObject
    *QGeoTiledMappingManagerEngine::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeotiledmappingmanagerengine.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QGeoTiledMappingManagerEngine::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK29QGeoTiledMappingManagerEngine10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def tileSize(self) -> QSize:
    """
    Calls Qt's 'QSize QGeoTiledMappingManagerEngine::tileSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeotiledmappingmanagerengine.html#tileSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QGeoTiledMappingManagerEngine::tileSize() const
    address = self.uglySide.call(
        'ritual_ZNK29QGeoTiledMappingManagerEngine8tileSizeEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def tileVersion(self) -> int:
    """
    Calls Qt's 'int QGeoTiledMappingManagerEngine::tileVersion() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeotiledmappingmanagerengine.html#tileVersion
    """
    #  int QGeoTiledMappingManagerEngine::tileVersion() const
    return self.uglySide.call(
        'ritual_ZNK29QGeoTiledMappingManagerEngine11tileVersionEv',
    )

  def cacheHint(self) -> QAbstractGeoTileCache.CacheAreas:
    """
    Calls Qt's 'QAbstractGeoTileCache::CacheAreas
    QGeoTiledMappingManagerEngine::cacheHint() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeotiledmappingmanagerengine.html#cacheHint

    Returns
    -------

    QAbstractGeoTileCache.CacheAreas
      The value standing for the combination Qt gave back.
    """
    #  QAbstractGeoTileCache::CacheAreas
    #      QGeoTiledMappingManagerEngine::cacheHint() const
    return QAbstractGeoTileCache.CacheAreas(self.uglySide.call(
        'ritual_ZNK29QGeoTiledMappingManagerEngine9cacheHintEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QGeoTileFetcher)
  @overload(NoneType)
  def setTileFetcher(self, fetcher: Optional[QGeoTileFetcher]) -> None:
    """
    Calls Qt's 'void
    QGeoTiledMappingManagerEngine::setTileFetcher(QGeoTileFetcher *fetcher)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeotiledmappingmanagerengine.html#setTileFetcher

    Parameters
    ----------

    fetcher : Optional[QGeoTileFetcher]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGeoTiledMappingManagerEngine::setTileFetcher(QGeoTileFetcher
    #      *fetcher)
    self.uglySide.call(
        'ritual_ZN29QGeoTiledMappingManagerEngine14setTileFetcherEP15QGeoTi'
        'leFetcher',
        self._addressOf(fetcher),
    )

  @overload(QSize)
  def setTileSize(self, tileSize: QSize) -> None:
    """
    Calls Qt's 'void QGeoTiledMappingManagerEngine::setTileSize(const QSize
    &tileSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeotiledmappingmanagerengine.html#setTileSize

    Parameters
    ----------

    tileSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QGeoTiledMappingManagerEngine::setTileSize(const QSize &tileSize)
    self.uglySide.call(
        'ritual_ZN29QGeoTiledMappingManagerEngine11setTileSizeERK5QSize',
        self._valueOf(tileSize),
    )

  @overload(int)
  def setTileVersion(self, version: int) -> None:
    """
    Calls Qt's 'void QGeoTiledMappingManagerEngine::setTileVersion(int
    version)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeotiledmappingmanagerengine.html#setTileVersion

    Parameters
    ----------

    version : int
      Passed on as it is.
    """
    #  void QGeoTiledMappingManagerEngine::setTileVersion(int version)
    self.uglySide.call(
        'ritual_ZN29QGeoTiledMappingManagerEngine14setTileVersionEi',
        version,
    )

  @overload(QAbstractGeoTileCache.CacheAreas)
  def setCacheHint(
      self,
      cacheHint: QAbstractGeoTileCache.CacheAreas,
  ) -> None:
    """
    Calls Qt's 'void
    QGeoTiledMappingManagerEngine::setCacheHint(QAbstractGeoTileCache::
    CacheAreas cacheHint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeotiledmappingmanagerengine.html#setCacheHint

    Parameters
    ----------

    cacheHint : QAbstractGeoTileCache.CacheAreas
      Passed on as its number.
    """
    #  void QGeoTiledMappingManagerEngine::setCacheHint(
    #      QAbstractGeoTileCache::CacheAreas cacheHint)
    self.uglySide.call(
        'ritual_ZN29QGeoTiledMappingManagerEngine12setCacheHintE6QFlagsIN21'
        'QAbstractGeoTileCache9CacheAreaEE',
        cacheHint.value,
    )

  @overload(QAbstractGeoTileCache)
  @overload(NoneType)
  def setTileCache(self, cache: Optional[QAbstractGeoTileCache]) -> None:
    """
    Calls Qt's 'void
    QGeoTiledMappingManagerEngine::setTileCache(QAbstractGeoTileCache
    *cache)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeotiledmappingmanagerengine.html#setTileCache

    Parameters
    ----------

    cache : Optional[QAbstractGeoTileCache]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGeoTiledMappingManagerEngine::setTileCache(QAbstractGeoTileCache
    #      *cache)
    self.uglySide.call(
        'ritual_ZN29QGeoTiledMappingManagerEngine12setTileCacheEP21QAbstrac'
        'tGeoTileCache',
        self._addressOf(cache),
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
    'QGeoTiledMappingManagerEngine::QGeoTiledMappingManagerEngine(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeotiledmappingmanagerengine.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QGeoTiledMappingManagerEngine::QGeoTiledMappingManagerEngine(QObject
    #      *parent)
    self._noteCreation(QGeoTiledMappingManagerEngine, lambda: Rituals.call(
        'ritual_ZN29QGeoTiledMappingManagerEngineC1EP7QObject',
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

  def tileFetcher(self) -> Optional[QGeoTileFetcher]:
    """
    Calls Qt's 'QGeoTileFetcher
    *QGeoTiledMappingManagerEngine::tileFetcher()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeotiledmappingmanagerengine.html#tileFetcher

    Returns
    -------

    Optional[QGeoTileFetcher]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGeoTileFetcher *QGeoTiledMappingManagerEngine::tileFetcher()
    address = self.uglySide.call(
        'ritual_ZN29QGeoTiledMappingManagerEngine11tileFetcherEv',
    )
    from . import QGeoTileFetcher
    return QGeoTileFetcher._cuteAt(address)

  def createMap(self) -> Optional[QGeoMap]:
    """
    Calls Qt's 'QGeoMap *QGeoTiledMappingManagerEngine::createMap()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeotiledmappingmanagerengine.html#createMap

    Returns
    -------

    Optional[QGeoMap]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGeoMap *QGeoTiledMappingManagerEngine::createMap()
    ritual = 'ritual_ZN29QGeoTiledMappingManagerEngine9createMapEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN29QGeoTiledMappingManagerEngine9createMapEv'
    address = self.uglySide.call(ritual)
    from . import QGeoMap
    return QGeoMap._cuteAt(address)

  @overload(QGeoTiledMap)
  @overload(NoneType)
  def releaseMap(self, map: Optional[QGeoTiledMap]) -> None:
    """
    Calls Qt's 'void QGeoTiledMappingManagerEngine::releaseMap(QGeoTiledMap
    *map)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeotiledmappingmanagerengine.html#releaseMap

    Parameters
    ----------

    map : Optional[QGeoTiledMap]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGeoTiledMappingManagerEngine::releaseMap(QGeoTiledMap *map)
    self.uglySide.call(
        'ritual_ZN29QGeoTiledMappingManagerEngine10releaseMapEP12QGeoTiledM'
        'ap',
        self._addressOf(map),
    )

  def tileCache(self) -> Optional[QAbstractGeoTileCache]:
    """
    Calls Qt's 'QAbstractGeoTileCache
    *QGeoTiledMappingManagerEngine::tileCache()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeotiledmappingmanagerengine.html#tileCache

    Returns
    -------

    Optional[QAbstractGeoTileCache]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractGeoTileCache *QGeoTiledMappingManagerEngine::tileCache()
    address = self.uglySide.call(
        'ritual_ZN29QGeoTiledMappingManagerEngine9tileCacheEv',
    )
    return QAbstractGeoTileCache._cuteAt(address)

  @overload(QGeoTileSpec, QByteArray, str)
  def engineTileFinished(
      self,
      spec: QGeoTileSpec,
      bytes: QByteArray,
      format: str,
  ) -> None:
    """
    Calls Qt's 'void QGeoTiledMappingManagerEngine::engineTileFinished(const
    QGeoTileSpec &spec, const QByteArray &bytes, const QString &format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeotiledmappingmanagerengine.html

    Parameters
    ----------

    spec : QGeoTileSpec
      Passed on as a value: Qt reads the C++ QGeoTileSpec, which stays
      Python's own.

    bytes : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    format : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QGeoTiledMappingManagerEngine::engineTileFinished(const
    #      QGeoTileSpec &spec, const QByteArray &bytes, const QString
    #      &format)
    ritual = (
        'ritual_ZN29QGeoTiledMappingManagerEngine18engineTileFinishedERK12Q'
        'GeoTileSpecRK10QByteArrayRK7QString')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN29QGeoTiledMappingManagerEngine18engineTileFinished'
          'ERK12QGeoTileSpecRK10QByteArrayRK7QString')
    self.uglySide.call(
        ritual, self._valueOf(spec), self._valueOf(bytes), format,
    )

  @overload(QGeoTileSpec, str)
  def engineTileError(self, spec: QGeoTileSpec, errorString: str) -> None:
    """
    Calls Qt's 'void QGeoTiledMappingManagerEngine::engineTileError(const
    QGeoTileSpec &spec, const QString &errorString)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeotiledmappingmanagerengine.html#engineTileError

    Parameters
    ----------

    spec : QGeoTileSpec
      Passed on as a value: Qt reads the C++ QGeoTileSpec, which stays
      Python's own.

    errorString : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QGeoTiledMappingManagerEngine::engineTileError(const QGeoTileSpec
    #      &spec, const QString &errorString)
    ritual = (
        'ritual_ZN29QGeoTiledMappingManagerEngine15engineTileErrorERK12QGeo'
        'TileSpecRK7QString')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN29QGeoTiledMappingManagerEngine15engineTileErrorERK'
          '12QGeoTileSpecRK7QString')
    self.uglySide.call(ritual, self._valueOf(spec), errorString)

  @overload(QGeoTileSpec, str)
  def tileError(self, spec: QGeoTileSpec, errorString: str) -> None:
    """
    Calls Qt's 'void QGeoTiledMappingManagerEngine::tileError(const
    QGeoTileSpec &spec, const QString &errorString)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeotiledmappingmanagerengine.html#tileError

    Parameters
    ----------

    spec : QGeoTileSpec
      Passed on as a value: Qt reads the C++ QGeoTileSpec, which stays
      Python's own.

    errorString : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QGeoTiledMappingManagerEngine::tileError(const QGeoTileSpec
    #      &spec, const QString &errorString)
    self.uglySide.call(
        'ritual_ZN29QGeoTiledMappingManagerEngine9tileErrorERK12QGeoTileSpe'
        'cRK7QString',
        self._valueOf(spec), errorString,
    )

  def tileVersionChanged(self) -> None:
    """
    Calls Qt's 'void QGeoTiledMappingManagerEngine::tileVersionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeotiledmappingmanagerengine.html
    """
    #  void QGeoTiledMappingManagerEngine::tileVersionChanged()
    self.uglySide.call(
        'ritual_ZN29QGeoTiledMappingManagerEngine18tileVersionChangedEv',
    )

  def d_func(self) -> Optional[QGeoTiledMappingManagerEnginePrivate]:
    """
    Calls Qt's 'QGeoTiledMappingManagerEnginePrivate
    *QGeoTiledMappingManagerEngine::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeotiledmappingmanagerengine.html#d_func

    Returns
    -------

    Optional[QGeoTiledMappingManagerEnginePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGeoTiledMappingManagerEnginePrivate
    #      *QGeoTiledMappingManagerEngine::d_func()
    address = self.uglySide.call(
        'ritual_ZN29QGeoTiledMappingManagerEngine6d_funcEv',
    )
    from . import QGeoTiledMappingManagerEnginePrivate
    return QGeoTiledMappingManagerEnginePrivate._cuteAt(address)

  @staticmethod
  def getTileTexture(*__, **_) -> Never:
    """
    Qt's 'QSharedPointer<QGeoTileTexture>
    QGeoTiledMappingManagerEngine::getTileTexture(const QGeoTileSpec &spec)':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QGeoTiledMappingManagerEngine.getTileTexture' has no cute "
        "function yet. Qt's 'QSharedPointer<QGeoTileTexture> "
        "QGeoTiledMappingManagerEngine::getTileTexture(const QGeoTileSpec "
        "&spec)': gives a type Python has no way to take yet.")

  @staticmethod
  def updateTileRequests(*__, **_) -> Never:
    """
    Qt's 'void QGeoTiledMappingManagerEngine::updateTileRequests(QGeoTiledMap
    *map, const QSet<QGeoTileSpec> &tilesAdded, const QSet<QGeoTileSpec>
    &tilesRemoved)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QGeoTiledMappingManagerEngine.updateTileRequests' has no cute "
        "function yet. Qt's 'void "
        "QGeoTiledMappingManagerEngine::updateTileRequests(QGeoTiledMap "
        "*map, const QSet<QGeoTileSpec> &tilesAdded, const "
        "QSet<QGeoTileSpec> &tilesRemoved)': takes a type Python has no way "
        "to hand over yet.")
