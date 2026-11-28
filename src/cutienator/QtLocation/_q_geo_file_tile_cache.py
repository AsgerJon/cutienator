"""
QGeoFileTileCache binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qgeofiletilecache_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QGeoFileTileCache to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QAbstractGeoTileCache

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaObject
  from . import QGeoCachedTileDisk, QGeoTileSpec
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QGeoCachedTileDisk = WAIT['QGeoCachedTileDisk']
  QGeoTileSpec = WAIT['QGeoTileSpec']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGeoFileTileCache(QAbstractGeoTileCache):
  """
  The cute side of Qt's QGeoFileTileCache: a plain Python object standing in
  front of one C++ QGeoFileTileCache.

  It is built on the cute 'QAbstractGeoTileCache', as Qt's QGeoFileTileCache
  is built on Qt's QAbstractGeoTileCache, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGeoFileTileCache that has a ritual and that Python
  can call so far, 34 names in all: 'metaObject', 'tr', 'setMaxDiskUsage',
  'maxDiskUsage', 'diskUsage', 'setMaxMemoryUsage', 'maxMemoryUsage',
  'memoryUsage', 'setMinTextureUsage', 'setExtraTextureUsage',
  'maxTextureUsage', 'minTextureUsage', 'textureUsage', 'clearAll',
  'clearMapId', 'setCostStrategyDisk', 'costStrategyDisk',
  'setCostStrategyMemory', 'costStrategyMemory', 'setCostStrategyTexture',
  'costStrategyTexture', 'evictFromDiskCache', 'insert',
  'tileSpecToFilenameDefault', 'filenameToTileSpecDefault', 'init',
  'printStats', 'loadTiles', 'directory', 'addToDiskCache',
  'addToMemoryCache', 'isTileBogus', 'tileSpecToFilename',
  'filenameToTileSpec'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QGeoFileTileCache::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QGeoFileTileCache::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QGeoFileTileCache::~QGeoFileTileCache()': the destructor: Python
    never removes a C++ QGeoFileTileCache.
  - Qt's 'QSharedPointer<QGeoTileTexture> QGeoFileTileCache::get(const
    QGeoTileSpec &spec)': gives a type Python has no way to take yet.
  - Qt's 'void QGeoFileTileCache::evictFromMemoryCache(QGeoCachedTileMemory
    *tm)': names 'QGeoCachedTileMemory', which has no cute class yet.
  - Qt's 'QSharedPointer<QGeoCachedTileDisk>
    QGeoFileTileCache::addToDiskCache(const QGeoTileSpec &spec, const QString
    &filename)': gives a type Python has no way to take yet.
  - Qt's 'QSharedPointer<QGeoTileTexture>
    QGeoFileTileCache::addToTextureCache(const QGeoTileSpec &spec, const
    QImage &image)': gives a type Python has no way to take yet.
  - Qt's 'QSharedPointer<QGeoTileTexture>
    QGeoFileTileCache::getFromMemory(const QGeoTileSpec &spec)': gives a type
    Python has no way to take yet.
  - Qt's 'QSharedPointer<QGeoTileTexture>
    QGeoFileTileCache::getFromDisk(const QGeoTileSpec &spec)': gives a type
    Python has no way to take yet.

  What has no ritual
  ------------------

  2 of the 46 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QGeoFileTileCache is created at the first use, not by
    'QGeoFileTileCache(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGeoFileTileCache.
  - Qt tells when it has removed the C++ QGeoFileTileCache. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QGeoFileTileCache that has no cute function yet,
    'addToTextureCache', 'evictFromMemoryCache', 'getFromDisk',
    'getFromMemory', holds a function that raises 'NotImplementedError', and
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
    Calls Qt's 'QString QGeoFileTileCache::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeofiletilecache.html#tr

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
    #  QString QGeoFileTileCache::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QGeoFileTileCache2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QGeoCachedTileDisk)
  @overload(NoneType)
  def evictFromDiskCache(td: Optional[QGeoCachedTileDisk]) -> None:
    """
    Calls Qt's 'void QGeoFileTileCache::evictFromDiskCache(QGeoCachedTileDisk
    *td)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeofiletilecache.html#evictFromDiskCache

    Parameters
    ----------

    td : Optional[QGeoCachedTileDisk]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGeoFileTileCache::evictFromDiskCache(QGeoCachedTileDisk *td)
    Rituals.call(
        'ritual_ZN17QGeoFileTileCache18evictFromDiskCacheEP18QGeoCachedTile'
        'Disk',
        CuteMixin._addressOf(td),
    )

  @staticmethod
  @overload(QGeoTileSpec, str, str)
  def tileSpecToFilenameDefault(
      spec: QGeoTileSpec,
      format: str,
      directory: str,
  ) -> str:
    """
    Calls Qt's 'QString QGeoFileTileCache::tileSpecToFilenameDefault(const
    QGeoTileSpec &spec, const QString &format, const QString &directory)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeofiletilecache.html#tileSpecToFilenameDefault

    Parameters
    ----------

    spec : QGeoTileSpec
      Passed on as a value: Qt reads the C++ QGeoTileSpec, which stays
      Python's own.

    format : str
      Passed on as it is: a QString is made of it for the call.

    directory : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGeoFileTileCache::tileSpecToFilenameDefault(const
    #      QGeoTileSpec &spec, const QString &format, const QString
    #      &directory)
    return Rituals.call(
        'ritual_ZN17QGeoFileTileCache25tileSpecToFilenameDefaultERK12QGeoTi'
        'leSpecRK7QStringS5_',
        CuteMixin._valueOf(spec), format, directory,
    )

  @staticmethod
  @overload(str)
  def filenameToTileSpecDefault(filename: str) -> QGeoTileSpec:
    """
    Calls Qt's 'QGeoTileSpec
    QGeoFileTileCache::filenameToTileSpecDefault(const QString &filename)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeofiletilecache.html#filenameToTileSpecDefault

    Parameters
    ----------

    filename : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QGeoTileSpec
      A new cute QGeoTileSpec around the copy Qt gave back. Python owns it.
    """
    #  QGeoTileSpec QGeoFileTileCache::filenameToTileSpecDefault(const
    #      QString &filename)
    address = Rituals.call(
        'ritual_ZN17QGeoFileTileCache25filenameToTileSpecDefaultERK7QString',
        filename,
    )
    from . import QGeoTileSpec
    return QGeoTileSpec._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoFileTileCache'

  #  A C++ QGeoFileTileCache Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGeoFileTileCache'

  #  The functions Qt calls itself that QGeoFileTileCache is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'isTileBogus': (
          ('_ZNK17QGeoFileTileCache11isTileBogusERK10QByteArray',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtCore:QByteArray'),
           )),
      ),
      'tileSpecToFilename': (
          ('_ZNK17QGeoFileTileCache18tileSpecToFilenameERK12QGeoTileSpecRK7'
           'QStringS5_',
           ('address', 'text', ''),
           (
               ('address', 'value', 'QtLocation:QGeoTileSpec'),
               ('address', 'text', ''),
               ('address', 'text', ''),
           )),
      ),
      'filenameToTileSpec': (
          ('_ZNK17QGeoFileTileCache18filenameToTileSpecERK7QString',
           ('address', 'value', 'QtLocation:QGeoTileSpec'),
           (
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
    Calls Qt's 'const QMetaObject *QGeoFileTileCache::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeofiletilecache.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QGeoFileTileCache::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QGeoFileTileCache10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def maxDiskUsage(self) -> int:
    """
    Calls Qt's 'int QGeoFileTileCache::maxDiskUsage() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeofiletilecache.html#maxDiskUsage
    """
    #  int QGeoFileTileCache::maxDiskUsage() const
    ritual = 'ritual_ZNK17QGeoFileTileCache12maxDiskUsageEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QGeoFileTileCache12maxDiskUsageEv'
    return self.uglySide.call(ritual)

  def diskUsage(self) -> int:
    """
    Calls Qt's 'int QGeoFileTileCache::diskUsage() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeofiletilecache.html#diskUsage
    """
    #  int QGeoFileTileCache::diskUsage() const
    ritual = 'ritual_ZNK17QGeoFileTileCache9diskUsageEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QGeoFileTileCache9diskUsageEv'
    return self.uglySide.call(ritual)

  def maxMemoryUsage(self) -> int:
    """
    Calls Qt's 'int QGeoFileTileCache::maxMemoryUsage() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeofiletilecache.html#maxMemoryUsage
    """
    #  int QGeoFileTileCache::maxMemoryUsage() const
    ritual = 'ritual_ZNK17QGeoFileTileCache14maxMemoryUsageEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QGeoFileTileCache14maxMemoryUsageEv'
    return self.uglySide.call(ritual)

  def memoryUsage(self) -> int:
    """
    Calls Qt's 'int QGeoFileTileCache::memoryUsage() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeofiletilecache.html#memoryUsage
    """
    #  int QGeoFileTileCache::memoryUsage() const
    ritual = 'ritual_ZNK17QGeoFileTileCache11memoryUsageEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QGeoFileTileCache11memoryUsageEv'
    return self.uglySide.call(ritual)

  def maxTextureUsage(self) -> int:
    """
    Calls Qt's 'int QGeoFileTileCache::maxTextureUsage() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeofiletilecache.html#maxTextureUsage
    """
    #  int QGeoFileTileCache::maxTextureUsage() const
    ritual = 'ritual_ZNK17QGeoFileTileCache15maxTextureUsageEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QGeoFileTileCache15maxTextureUsageEv'
    return self.uglySide.call(ritual)

  def minTextureUsage(self) -> int:
    """
    Calls Qt's 'int QGeoFileTileCache::minTextureUsage() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeofiletilecache.html#minTextureUsage
    """
    #  int QGeoFileTileCache::minTextureUsage() const
    ritual = 'ritual_ZNK17QGeoFileTileCache15minTextureUsageEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QGeoFileTileCache15minTextureUsageEv'
    return self.uglySide.call(ritual)

  def textureUsage(self) -> int:
    """
    Calls Qt's 'int QGeoFileTileCache::textureUsage() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeofiletilecache.html#textureUsage
    """
    #  int QGeoFileTileCache::textureUsage() const
    ritual = 'ritual_ZNK17QGeoFileTileCache12textureUsageEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QGeoFileTileCache12textureUsageEv'
    return self.uglySide.call(ritual)

  def costStrategyDisk(self) -> QAbstractGeoTileCache.CostStrategy:
    """
    Calls Qt's 'CostStrategy QGeoFileTileCache::costStrategyDisk() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeofiletilecache.html#costStrategyDisk

    Returns
    -------

    QAbstractGeoTileCache.CostStrategy
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QAbstractGeoTileCache.CostStrategy(number)' gives.
    """
    #  CostStrategy QGeoFileTileCache::costStrategyDisk() const
    ritual = 'ritual_ZNK17QGeoFileTileCache16costStrategyDiskEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QGeoFileTileCache16costStrategyDiskEv'
    return QAbstractGeoTileCache.CostStrategy(self.uglySide.call(ritual))

  def costStrategyMemory(self) -> QAbstractGeoTileCache.CostStrategy:
    """
    Calls Qt's 'CostStrategy QGeoFileTileCache::costStrategyMemory() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeofiletilecache.html#costStrategyMemory

    Returns
    -------

    QAbstractGeoTileCache.CostStrategy
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QAbstractGeoTileCache.CostStrategy(number)' gives.
    """
    #  CostStrategy QGeoFileTileCache::costStrategyMemory() const
    ritual = 'ritual_ZNK17QGeoFileTileCache18costStrategyMemoryEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QGeoFileTileCache18costStrategyMemoryEv'
    return QAbstractGeoTileCache.CostStrategy(self.uglySide.call(ritual))

  def costStrategyTexture(self) -> QAbstractGeoTileCache.CostStrategy:
    """
    Calls Qt's 'CostStrategy QGeoFileTileCache::costStrategyTexture() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeofiletilecache.html#costStrategyTexture

    Returns
    -------

    QAbstractGeoTileCache.CostStrategy
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QAbstractGeoTileCache.CostStrategy(number)' gives.
    """
    #  CostStrategy QGeoFileTileCache::costStrategyTexture() const
    ritual = 'ritual_ZNK17QGeoFileTileCache19costStrategyTextureEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QGeoFileTileCache19costStrategyTextureEv'
    return QAbstractGeoTileCache.CostStrategy(self.uglySide.call(ritual))

  def directory(self) -> str:
    """
    Calls Qt's 'QString QGeoFileTileCache::directory() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeofiletilecache.html#directory

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGeoFileTileCache::directory() const
    return self.uglySide.call('ritual_ZNK17QGeoFileTileCache9directoryEv')

  @overload(QByteArray)
  def isTileBogus(self, bytes: QByteArray) -> bool:
    """
    Calls Qt's 'bool QGeoFileTileCache::isTileBogus(const QByteArray &bytes)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeofiletilecache.html#isTileBogus

    Parameters
    ----------

    bytes : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  bool QGeoFileTileCache::isTileBogus(const QByteArray &bytes) const
    ritual = 'ritual_ZNK17QGeoFileTileCache11isTileBogusERK10QByteArray'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK17QGeoFileTileCache11isTileBogusERK10QByteArray')
    return self.uglySide.call(ritual, self._valueOf(bytes))

  @overload(QGeoTileSpec, str, str)
  def tileSpecToFilename(
      self,
      spec: QGeoTileSpec,
      format: str,
      directory: str,
  ) -> str:
    """
    Calls Qt's 'QString QGeoFileTileCache::tileSpecToFilename(const
    QGeoTileSpec &spec, const QString &format, const QString &directory)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeofiletilecache.html#tileSpecToFilename

    Parameters
    ----------

    spec : QGeoTileSpec
      Passed on as a value: Qt reads the C++ QGeoTileSpec, which stays
      Python's own.

    format : str
      Passed on as it is: a QString is made of it for the call.

    directory : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGeoFileTileCache::tileSpecToFilename(const QGeoTileSpec
    #      &spec, const QString &format, const QString &directory) const
    ritual = (
        'ritual_ZNK17QGeoFileTileCache18tileSpecToFilenameERK12QGeoTileSpec'
        'RK7QStringS5_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK17QGeoFileTileCache18tileSpecToFilenameERK12QGeoTi'
          'leSpecRK7QStringS5_')
    return self.uglySide.call(ritual, self._valueOf(spec), format, directory)

  @overload(str)
  def filenameToTileSpec(self, filename: str) -> QGeoTileSpec:
    """
    Calls Qt's 'QGeoTileSpec QGeoFileTileCache::filenameToTileSpec(const
    QString &filename) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeofiletilecache.html#filenameToTileSpec

    Parameters
    ----------

    filename : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QGeoTileSpec
      A new cute QGeoTileSpec around the copy Qt gave back. Python owns it.
    """
    #  QGeoTileSpec QGeoFileTileCache::filenameToTileSpec(const QString
    #      &filename) const
    ritual = 'ritual_ZNK17QGeoFileTileCache18filenameToTileSpecERK7QString'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK17QGeoFileTileCache18filenameToTileSpecERK7QString')
    address = self.uglySide.call(ritual, filename)
    from . import QGeoTileSpec
    return QGeoTileSpec._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setMaxDiskUsage(self, diskUsage: int) -> None:
    """
    Calls Qt's 'void QGeoFileTileCache::setMaxDiskUsage(int diskUsage)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeofiletilecache.html#setMaxDiskUsage

    Parameters
    ----------

    diskUsage : int
      Passed on as it is.
    """
    #  void QGeoFileTileCache::setMaxDiskUsage(int diskUsage)
    ritual = 'ritual_ZN17QGeoFileTileCache15setMaxDiskUsageEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QGeoFileTileCache15setMaxDiskUsageEi'
    self.uglySide.call(ritual, diskUsage)

  @overload(int)
  def setMaxMemoryUsage(self, memoryUsage: int) -> None:
    """
    Calls Qt's 'void QGeoFileTileCache::setMaxMemoryUsage(int memoryUsage)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeofiletilecache.html#setMaxMemoryUsage

    Parameters
    ----------

    memoryUsage : int
      Passed on as it is.
    """
    #  void QGeoFileTileCache::setMaxMemoryUsage(int memoryUsage)
    ritual = 'ritual_ZN17QGeoFileTileCache17setMaxMemoryUsageEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QGeoFileTileCache17setMaxMemoryUsageEi'
    self.uglySide.call(ritual, memoryUsage)

  @overload(int)
  def setMinTextureUsage(self, textureUsage: int) -> None:
    """
    Calls Qt's 'void QGeoFileTileCache::setMinTextureUsage(int
    textureUsage)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeofiletilecache.html#setMinTextureUsage

    Parameters
    ----------

    textureUsage : int
      Passed on as it is.
    """
    #  void QGeoFileTileCache::setMinTextureUsage(int textureUsage)
    ritual = 'ritual_ZN17QGeoFileTileCache18setMinTextureUsageEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QGeoFileTileCache18setMinTextureUsageEi'
    self.uglySide.call(ritual, textureUsage)

  @overload(int)
  def setExtraTextureUsage(self, textureUsage: int) -> None:
    """
    Calls Qt's 'void QGeoFileTileCache::setExtraTextureUsage(int
    textureUsage)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeofiletilecache.html#setExtraTextureUsage

    Parameters
    ----------

    textureUsage : int
      Passed on as it is.
    """
    #  void QGeoFileTileCache::setExtraTextureUsage(int textureUsage)
    ritual = 'ritual_ZN17QGeoFileTileCache20setExtraTextureUsageEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QGeoFileTileCache20setExtraTextureUsageEi'
    self.uglySide.call(ritual, textureUsage)

  @overload(QAbstractGeoTileCache.CostStrategy)
  def setCostStrategyDisk(
      self,
      costStrategy: QAbstractGeoTileCache.CostStrategy,
  ) -> None:
    """
    Calls Qt's 'void QGeoFileTileCache::setCostStrategyDisk(CostStrategy
    costStrategy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeofiletilecache.html#setCostStrategyDisk

    Parameters
    ----------

    costStrategy : QAbstractGeoTileCache.CostStrategy
      Passed on as its number.
    """
    #  void QGeoFileTileCache::setCostStrategyDisk(CostStrategy costStrategy)
    ritual = (
        'ritual_ZN17QGeoFileTileCache19setCostStrategyDiskEN21QAbstractGeoT'
        'ileCache12CostStrategyE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QGeoFileTileCache19setCostStrategyDiskEN21QAbstra'
          'ctGeoTileCache12CostStrategyE')
    self.uglySide.call(ritual, costStrategy.value)

  @overload(QAbstractGeoTileCache.CostStrategy)
  def setCostStrategyMemory(
      self,
      costStrategy: QAbstractGeoTileCache.CostStrategy,
  ) -> None:
    """
    Calls Qt's 'void QGeoFileTileCache::setCostStrategyMemory(CostStrategy
    costStrategy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeofiletilecache.html#setCostStrategyMemory

    Parameters
    ----------

    costStrategy : QAbstractGeoTileCache.CostStrategy
      Passed on as its number.
    """
    #  void QGeoFileTileCache::setCostStrategyMemory(CostStrategy
    #      costStrategy)
    ritual = (
        'ritual_ZN17QGeoFileTileCache21setCostStrategyMemoryEN21QAbstractGe'
        'oTileCache12CostStrategyE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QGeoFileTileCache21setCostStrategyMemoryEN21QAbst'
          'ractGeoTileCache12CostStrategyE')
    self.uglySide.call(ritual, costStrategy.value)

  @overload(QAbstractGeoTileCache.CostStrategy)
  def setCostStrategyTexture(
      self,
      costStrategy: QAbstractGeoTileCache.CostStrategy,
  ) -> None:
    """
    Calls Qt's 'void QGeoFileTileCache::setCostStrategyTexture(CostStrategy
    costStrategy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeofiletilecache.html#setCostStrategyTexture

    Parameters
    ----------

    costStrategy : QAbstractGeoTileCache.CostStrategy
      Passed on as its number.
    """
    #  void QGeoFileTileCache::setCostStrategyTexture(CostStrategy
    #      costStrategy)
    ritual = (
        'ritual_ZN17QGeoFileTileCache22setCostStrategyTextureEN21QAbstractG'
        'eoTileCache12CostStrategyE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QGeoFileTileCache22setCostStrategyTextureEN21QAbs'
          'tractGeoTileCache12CostStrategyE')
    self.uglySide.call(ritual, costStrategy.value)

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
  @overload(str)
  @overload(str, QObject)
  @overload(str, NoneType)
  def __init__(
      self,
      directory: str = '',
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QGeoFileTileCache::QGeoFileTileCache(const QString &directory, QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeofiletilecache.html#QGeoFileTileCache

    Parameters
    ----------

    directory : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QGeoFileTileCache::QGeoFileTileCache(const QString &directory, QObject
    #      *parent)
    self._noteCreation(QGeoFileTileCache, lambda: Rituals.call(
        'ritual_ZN17QGeoFileTileCacheC1ERK7QStringP7QObject',
        directory, self._addressOf(parent, 'QObject'),
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

  def clearAll(self) -> None:
    """
    Calls Qt's 'void QGeoFileTileCache::clearAll()'.

    Qt's own words: https://doc.qt.io/qt-6/qgeofiletilecache.html#clearAll
    """
    #  void QGeoFileTileCache::clearAll()
    ritual = 'ritual_ZN17QGeoFileTileCache8clearAllEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QGeoFileTileCache8clearAllEv'
    self.uglySide.call(ritual)

  @overload(int)
  def clearMapId(self, mapId: int) -> None:
    """
    Calls Qt's 'void QGeoFileTileCache::clearMapId(int mapId)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeofiletilecache.html#clearMapId

    Parameters
    ----------

    mapId : int
      Passed on as it is.
    """
    #  void QGeoFileTileCache::clearMapId(int mapId)
    self.uglySide.call('ritual_ZN17QGeoFileTileCache10clearMapIdEi', mapId)

  @overload(QGeoTileSpec, QByteArray, str)
  @overload(QGeoTileSpec, QByteArray, str, QAbstractGeoTileCache.CacheAreas)
  def insert(
      self,
      spec: QGeoTileSpec,
      bytes: QByteArray,
      format: str,
      areas: QAbstractGeoTileCache.CacheAreas = (
          QAbstractGeoTileCache.CacheAreas.AllCaches),
  ) -> None:
    """
    Calls Qt's 'void QGeoFileTileCache::insert(const QGeoTileSpec &spec,
    const QByteArray &bytes, const QString &format,
    QAbstractGeoTileCache::CacheAreas areas)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeofiletilecache.html#insert

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

    areas : QAbstractGeoTileCache.CacheAreas
      Passed on as its number. May be left out, as in Qt: it is then
      QAbstractGeoTileCache.CacheAreas.AllCaches.
    """
    #  void QGeoFileTileCache::insert(const QGeoTileSpec &spec, const
    #      QByteArray &bytes, const QString &format,
    #      QAbstractGeoTileCache::CacheAreas areas)
    ritual = (
        'ritual_ZN17QGeoFileTileCache6insertERK12QGeoTileSpecRK10QByteArray'
        'RK7QString6QFlagsIN21QAbstractGeoTileCache9CacheAreaEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QGeoFileTileCache6insertERK12QGeoTileSpecRK10QByt'
          'eArrayRK7QString6QFlagsIN21QAbstractGeoTileCache9CacheAreaEE')
    self.uglySide.call(
        ritual,
        self._valueOf(spec), self._valueOf(bytes), format, areas.value,
    )

  def init(self) -> None:
    """
    Calls Qt's 'void QGeoFileTileCache::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qgeofiletilecache.html#init
    """
    #  void QGeoFileTileCache::init()
    ritual = 'ritual_ZN17QGeoFileTileCache4initEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QGeoFileTileCache4initEv'
    self.uglySide.call(ritual)

  def printStats(self) -> None:
    """
    Calls Qt's 'void QGeoFileTileCache::printStats()'.

    Qt's own words: https://doc.qt.io/qt-6/qgeofiletilecache.html#printStats
    """
    #  void QGeoFileTileCache::printStats()
    ritual = 'ritual_ZN17QGeoFileTileCache10printStatsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QGeoFileTileCache10printStatsEv'
    self.uglySide.call(ritual)

  def loadTiles(self) -> None:
    """
    Calls Qt's 'void QGeoFileTileCache::loadTiles()'.

    Qt's own words: https://doc.qt.io/qt-6/qgeofiletilecache.html#loadTiles
    """
    #  void QGeoFileTileCache::loadTiles()
    self.uglySide.call('ritual_ZN17QGeoFileTileCache9loadTilesEv')

  @overload(QGeoTileSpec, str, QByteArray)
  def addToDiskCache(
      self,
      spec: QGeoTileSpec,
      filename: str,
      bytes: QByteArray,
  ) -> bool:
    """
    Calls Qt's 'bool QGeoFileTileCache::addToDiskCache(const QGeoTileSpec
    &spec, const QString &filename, const QByteArray &bytes)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeofiletilecache.html#addToDiskCache

    Parameters
    ----------

    spec : QGeoTileSpec
      Passed on as a value: Qt reads the C++ QGeoTileSpec, which stays
      Python's own.

    filename : str
      Passed on as it is: a QString is made of it for the call.

    bytes : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  bool QGeoFileTileCache::addToDiskCache(const QGeoTileSpec &spec, const
    #      QString &filename, const QByteArray &bytes)
    return self.uglySide.call(
        'ritual_ZN17QGeoFileTileCache14addToDiskCacheERK12QGeoTileSpecRK7QS'
        'tringRK10QByteArray',
        self._valueOf(spec), filename, self._valueOf(bytes),
    )

  @overload(QGeoTileSpec, QByteArray, str)
  def addToMemoryCache(
      self,
      spec: QGeoTileSpec,
      bytes: QByteArray,
      format: str,
  ) -> None:
    """
    Calls Qt's 'void QGeoFileTileCache::addToMemoryCache(const QGeoTileSpec
    &spec, const QByteArray &bytes, const QString &format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeofiletilecache.html#addToMemoryCache

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
    #  void QGeoFileTileCache::addToMemoryCache(const QGeoTileSpec &spec,
    #      const QByteArray &bytes, const QString &format)
    self.uglySide.call(
        'ritual_ZN17QGeoFileTileCache16addToMemoryCacheERK12QGeoTileSpecRK1'
        '0QByteArrayRK7QString',
        self._valueOf(spec), self._valueOf(bytes), format,
    )

  @staticmethod
  def addToTextureCache(*__, **_) -> Never:
    """
    Qt's 'QSharedPointer<QGeoTileTexture>
    QGeoFileTileCache::addToTextureCache(const QGeoTileSpec &spec, const
    QImage &image)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QGeoFileTileCache.addToTextureCache' has no cute function yet. "
        "Qt's 'QSharedPointer<QGeoTileTexture> "
        "QGeoFileTileCache::addToTextureCache(const QGeoTileSpec &spec, "
        "const QImage &image)': gives a type Python has no way to take yet.")

  @staticmethod
  def evictFromMemoryCache(*__, **_) -> Never:
    """
    Qt's 'void QGeoFileTileCache::evictFromMemoryCache(QGeoCachedTileMemory
    *tm)': names 'QGeoCachedTileMemory', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QGeoFileTileCache.evictFromMemoryCache' has no cute function yet. "
        "Qt's 'void "
        "QGeoFileTileCache::evictFromMemoryCache(QGeoCachedTileMemory "
        "*tm)': names 'QGeoCachedTileMemory', which has no cute class yet.")

  @staticmethod
  def getFromDisk(*__, **_) -> Never:
    """
    Qt's 'QSharedPointer<QGeoTileTexture>
    QGeoFileTileCache::getFromDisk(const QGeoTileSpec &spec)': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QGeoFileTileCache.getFromDisk' has no cute function yet. Qt's "
        "'QSharedPointer<QGeoTileTexture> "
        "QGeoFileTileCache::getFromDisk(const QGeoTileSpec &spec)': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def getFromMemory(*__, **_) -> Never:
    """
    Qt's 'QSharedPointer<QGeoTileTexture>
    QGeoFileTileCache::getFromMemory(const QGeoTileSpec &spec)': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QGeoFileTileCache.getFromMemory' has no cute function yet. Qt's "
        "'QSharedPointer<QGeoTileTexture> "
        "QGeoFileTileCache::getFromMemory(const QGeoTileSpec &spec)': gives "
        "a type Python has no way to take yet.")
