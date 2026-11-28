"""
QAbstractGeoTileCache binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qabstractgeotilecache_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QAbstractGeoTileCache to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaObject
  from . import QGeoTileSpec
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QGeoTileSpec = WAIT['QGeoTileSpec']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractGeoTileCache(QObject):
  """
  The cute side of Qt's QAbstractGeoTileCache: a plain Python object standing
  in front of one C++ QAbstractGeoTileCache.

  It is built on the cute 'QObject', as Qt's QAbstractGeoTileCache is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstractGeoTileCache that has a ritual and that
  Python can call so far, 26 names in all: 'metaObject', 'tr',
  'setMaxDiskUsage', 'maxDiskUsage', 'diskUsage', 'setMaxMemoryUsage',
  'maxMemoryUsage', 'memoryUsage', 'setMinTextureUsage',
  'setExtraTextureUsage', 'maxTextureUsage', 'minTextureUsage',
  'textureUsage', 'clearAll', 'setCostStrategyDisk', 'costStrategyDisk',
  'setCostStrategyMemory', 'costStrategyMemory', 'setCostStrategyTexture',
  'costStrategyTexture', 'insert', 'handleError', 'init',
  'baseCacheDirectory', 'baseLocationCacheDirectory', 'printStats'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QAbstractGeoTileCache::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QAbstractGeoTileCache::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QAbstractGeoTileCache::~QAbstractGeoTileCache()': the destructor:
    Python never removes a C++ QAbstractGeoTileCache.
  - Qt's 'QSharedPointer<QGeoTileTexture> QAbstractGeoTileCache::get(const
    QGeoTileSpec &spec)': gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  3 of the 33 functions Qt declares: 2 not a gap; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ QAbstractGeoTileCache is created at the first use, not by
    'QAbstractGeoTileCache(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractGeoTileCache.
  - Qt tells when it has removed the C++ QAbstractGeoTileCache. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QAbstractGeoTileCache that has no cute function yet,
    '__init__', 'get', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  #  The enums Qt writes inside QAbstractGeoTileCache, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class CacheArea(CuteFlags):
    """
    The flags enum 'QAbstractGeoTileCache::CacheArea' of Qt, with the 3 names
    Qt gives in it. Qt names the type of its combinations
    'QAbstractGeoTileCache::CacheAreas'.
    """

    DiskCache = 0x1
    MemoryCache = 0x2
    AllCaches = 0xff

  CacheAreas = CacheArea

  class CostStrategy(CuteNum):
    """
    The enum 'QAbstractGeoTileCache::CostStrategy' of Qt, with the 2 names Qt
    gives in it.
    """

    Unitary = Kee[int](0)
    ByteSize = Kee[int](1)

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
    Calls Qt's 'QString QAbstractGeoTileCache::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractgeotilecache.html#tr

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
    #  QString QAbstractGeoTileCache::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QAbstractGeoTileCache2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def baseCacheDirectory() -> str:
    """
    Calls Qt's 'QString QAbstractGeoTileCache::baseCacheDirectory()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractgeotilecache.html#baseCacheDirectory

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAbstractGeoTileCache::baseCacheDirectory()
    return Rituals.call(
        'ritual_ZN21QAbstractGeoTileCache18baseCacheDirectoryEv',
    )

  @staticmethod
  def baseLocationCacheDirectory() -> str:
    """
    Calls Qt's 'QString QAbstractGeoTileCache::baseLocationCacheDirectory()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractgeotilecache.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAbstractGeoTileCache::baseLocationCacheDirectory()
    return Rituals.call(
        'ritual_ZN21QAbstractGeoTileCache26baseLocationCacheDirectoryEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractGeoTileCache'

  #  A C++ QAbstractGeoTileCache Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAbstractGeoTileCache'

  #  The functions Qt calls itself that QAbstractGeoTileCache is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'get': (
          'QSharedPointer<QGeoTileTexture> '
          'QAbstractGeoTileCache::get(const QGeoTileSpec &)',
      ),
  }

  #  The functions Qt calls itself that QAbstractGeoTileCache is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'setMaxDiskUsage': (
          ('_ZN21QAbstractGeoTileCache15setMaxDiskUsageEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'maxDiskUsage': (
          ('_ZNK21QAbstractGeoTileCache12maxDiskUsageEv',
           ('int', 'number', ''),
           ()),
      ),
      'diskUsage': (
          ('_ZNK21QAbstractGeoTileCache9diskUsageEv',
           ('int', 'number', ''),
           ()),
      ),
      'setMaxMemoryUsage': (
          ('_ZN21QAbstractGeoTileCache17setMaxMemoryUsageEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'maxMemoryUsage': (
          ('_ZNK21QAbstractGeoTileCache14maxMemoryUsageEv',
           ('int', 'number', ''),
           ()),
      ),
      'memoryUsage': (
          ('_ZNK21QAbstractGeoTileCache11memoryUsageEv',
           ('int', 'number', ''),
           ()),
      ),
      'setMinTextureUsage': (
          ('_ZN21QAbstractGeoTileCache18setMinTextureUsageEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'setExtraTextureUsage': (
          ('_ZN21QAbstractGeoTileCache20setExtraTextureUsageEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'maxTextureUsage': (
          ('_ZNK21QAbstractGeoTileCache15maxTextureUsageEv',
           ('int', 'number', ''),
           ()),
      ),
      'minTextureUsage': (
          ('_ZNK21QAbstractGeoTileCache15minTextureUsageEv',
           ('int', 'number', ''),
           ()),
      ),
      'textureUsage': (
          ('_ZNK21QAbstractGeoTileCache12textureUsageEv',
           ('int', 'number', ''),
           ()),
      ),
      'clearAll': (
          ('_ZN21QAbstractGeoTileCache8clearAllEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'setCostStrategyDisk': (
          ('_ZN21QAbstractGeoTileCache19setCostStrategyDiskENS_12CostStrate'
           'gyE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum',
                'QtLocation:QAbstractGeoTileCache.CostStrategy'),
           )),
      ),
      'costStrategyDisk': (
          ('_ZNK21QAbstractGeoTileCache16costStrategyDiskEv',
           ('int', 'enum', 'QtLocation:QAbstractGeoTileCache.CostStrategy'),
           ()),
      ),
      'setCostStrategyMemory': (
          ('_ZN21QAbstractGeoTileCache21setCostStrategyMemoryENS_12CostStra'
           'tegyE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum',
                'QtLocation:QAbstractGeoTileCache.CostStrategy'),
           )),
      ),
      'costStrategyMemory': (
          ('_ZNK21QAbstractGeoTileCache18costStrategyMemoryEv',
           ('int', 'enum', 'QtLocation:QAbstractGeoTileCache.CostStrategy'),
           ()),
      ),
      'setCostStrategyTexture': (
          ('_ZN21QAbstractGeoTileCache22setCostStrategyTextureENS_12CostStr'
           'ategyE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum',
                'QtLocation:QAbstractGeoTileCache.CostStrategy'),
           )),
      ),
      'costStrategyTexture': (
          ('_ZNK21QAbstractGeoTileCache19costStrategyTextureEv',
           ('int', 'enum', 'QtLocation:QAbstractGeoTileCache.CostStrategy'),
           ()),
      ),
      'insert': (
          ('_ZN21QAbstractGeoTileCache6insertERK12QGeoTileSpecRK10QByteArra'
           'yRK7QString6QFlagsINS_9CacheAreaEE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtLocation:QGeoTileSpec'),
               ('address', 'value', 'QtCore:QByteArray'),
               ('address', 'text', ''),
               ('int', 'flags',
                'QtLocation:QAbstractGeoTileCache.CacheArea'),
           )),
      ),
      'handleError': (
          ('_ZN21QAbstractGeoTileCache11handleErrorERK12QGeoTileSpecRK7QStr'
           'ing',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtLocation:QGeoTileSpec'),
               ('address', 'text', ''),
           )),
      ),
      'init': (
          ('_ZN21QAbstractGeoTileCache4initEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'printStats': (
          ('_ZN21QAbstractGeoTileCache10printStatsEv',
           ('nothing', 'nothing', ''),
           ()),
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
    Calls Qt's 'const QMetaObject *QAbstractGeoTileCache::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractgeotilecache.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QAbstractGeoTileCache::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QAbstractGeoTileCache10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def maxDiskUsage(self) -> int:
    """
    Calls Qt's 'int QAbstractGeoTileCache::maxDiskUsage() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractgeotilecache.html#maxDiskUsage
    """
    #  int QAbstractGeoTileCache::maxDiskUsage() const
    ritual = 'ritual_ZNK21QAbstractGeoTileCache12maxDiskUsageEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QAbstractGeoTileCache12maxDiskUsageEv'
    return self.uglySide.call(ritual)

  def diskUsage(self) -> int:
    """
    Calls Qt's 'int QAbstractGeoTileCache::diskUsage() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractgeotilecache.html#diskUsage
    """
    #  int QAbstractGeoTileCache::diskUsage() const
    ritual = 'ritual_ZNK21QAbstractGeoTileCache9diskUsageEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QAbstractGeoTileCache9diskUsageEv'
    return self.uglySide.call(ritual)

  def maxMemoryUsage(self) -> int:
    """
    Calls Qt's 'int QAbstractGeoTileCache::maxMemoryUsage() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractgeotilecache.html#maxMemoryUsage
    """
    #  int QAbstractGeoTileCache::maxMemoryUsage() const
    ritual = 'ritual_ZNK21QAbstractGeoTileCache14maxMemoryUsageEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QAbstractGeoTileCache14maxMemoryUsageEv'
    return self.uglySide.call(ritual)

  def memoryUsage(self) -> int:
    """
    Calls Qt's 'int QAbstractGeoTileCache::memoryUsage() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractgeotilecache.html#memoryUsage
    """
    #  int QAbstractGeoTileCache::memoryUsage() const
    ritual = 'ritual_ZNK21QAbstractGeoTileCache11memoryUsageEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QAbstractGeoTileCache11memoryUsageEv'
    return self.uglySide.call(ritual)

  def maxTextureUsage(self) -> int:
    """
    Calls Qt's 'int QAbstractGeoTileCache::maxTextureUsage() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractgeotilecache.html#maxTextureUsage
    """
    #  int QAbstractGeoTileCache::maxTextureUsage() const
    return self.uglySide.call(
        'ritual_ZNK21QAbstractGeoTileCache15maxTextureUsageEv',
    )

  def minTextureUsage(self) -> int:
    """
    Calls Qt's 'int QAbstractGeoTileCache::minTextureUsage() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractgeotilecache.html#minTextureUsage
    """
    #  int QAbstractGeoTileCache::minTextureUsage() const
    return self.uglySide.call(
        'ritual_ZNK21QAbstractGeoTileCache15minTextureUsageEv',
    )

  def textureUsage(self) -> int:
    """
    Calls Qt's 'int QAbstractGeoTileCache::textureUsage() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractgeotilecache.html#textureUsage
    """
    #  int QAbstractGeoTileCache::textureUsage() const
    return self.uglySide.call(
        'ritual_ZNK21QAbstractGeoTileCache12textureUsageEv',
    )

  def costStrategyDisk(self) -> CostStrategy:
    """
    Calls Qt's 'CostStrategy QAbstractGeoTileCache::costStrategyDisk()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractgeotilecache.html#costStrategyDisk

    Returns
    -------

    CostStrategy
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'CostStrategy(number)'
      gives.
    """
    #  CostStrategy QAbstractGeoTileCache::costStrategyDisk() const
    return QAbstractGeoTileCache.CostStrategy(self.uglySide.call(
        'ritual_ZNK21QAbstractGeoTileCache16costStrategyDiskEv',
    ))

  def costStrategyMemory(self) -> CostStrategy:
    """
    Calls Qt's 'CostStrategy QAbstractGeoTileCache::costStrategyMemory()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractgeotilecache.html#costStrategyMemory

    Returns
    -------

    CostStrategy
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'CostStrategy(number)'
      gives.
    """
    #  CostStrategy QAbstractGeoTileCache::costStrategyMemory() const
    return QAbstractGeoTileCache.CostStrategy(self.uglySide.call(
        'ritual_ZNK21QAbstractGeoTileCache18costStrategyMemoryEv',
    ))

  def costStrategyTexture(self) -> CostStrategy:
    """
    Calls Qt's 'CostStrategy QAbstractGeoTileCache::costStrategyTexture()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractgeotilecache.html#costStrategyTexture

    Returns
    -------

    CostStrategy
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'CostStrategy(number)'
      gives.
    """
    #  CostStrategy QAbstractGeoTileCache::costStrategyTexture() const
    return QAbstractGeoTileCache.CostStrategy(self.uglySide.call(
        'ritual_ZNK21QAbstractGeoTileCache19costStrategyTextureEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setMaxDiskUsage(self, diskUsage: int) -> None:
    """
    Calls Qt's 'void QAbstractGeoTileCache::setMaxDiskUsage(int diskUsage)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractgeotilecache.html#setMaxDiskUsage

    Parameters
    ----------

    diskUsage : int
      Passed on as it is.
    """
    #  void QAbstractGeoTileCache::setMaxDiskUsage(int diskUsage)
    ritual = 'ritual_ZN21QAbstractGeoTileCache15setMaxDiskUsageEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QAbstractGeoTileCache15setMaxDiskUsageEi'
    self.uglySide.call(ritual, diskUsage)

  @overload(int)
  def setMaxMemoryUsage(self, memoryUsage: int) -> None:
    """
    Calls Qt's 'void QAbstractGeoTileCache::setMaxMemoryUsage(int
    memoryUsage)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractgeotilecache.html#setMaxMemoryUsage

    Parameters
    ----------

    memoryUsage : int
      Passed on as it is.
    """
    #  void QAbstractGeoTileCache::setMaxMemoryUsage(int memoryUsage)
    ritual = 'ritual_ZN21QAbstractGeoTileCache17setMaxMemoryUsageEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QAbstractGeoTileCache17setMaxMemoryUsageEi'
    self.uglySide.call(ritual, memoryUsage)

  @overload(int)
  def setMinTextureUsage(self, textureUsage: int) -> None:
    """
    Calls Qt's 'void QAbstractGeoTileCache::setMinTextureUsage(int
    textureUsage)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractgeotilecache.html#setMinTextureUsage

    Parameters
    ----------

    textureUsage : int
      Passed on as it is.
    """
    #  void QAbstractGeoTileCache::setMinTextureUsage(int textureUsage)
    self.uglySide.call(
        'ritual_ZN21QAbstractGeoTileCache18setMinTextureUsageEi',
        textureUsage,
    )

  @overload(int)
  def setExtraTextureUsage(self, textureUsage: int) -> None:
    """
    Calls Qt's 'void QAbstractGeoTileCache::setExtraTextureUsage(int
    textureUsage)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractgeotilecache.html#setExtraTextureUsage

    Parameters
    ----------

    textureUsage : int
      Passed on as it is.
    """
    #  void QAbstractGeoTileCache::setExtraTextureUsage(int textureUsage)
    self.uglySide.call(
        'ritual_ZN21QAbstractGeoTileCache20setExtraTextureUsageEi',
        textureUsage,
    )

  @overload(CostStrategy)
  def setCostStrategyDisk(self, costStrategy: CostStrategy) -> None:
    """
    Calls Qt's 'void QAbstractGeoTileCache::setCostStrategyDisk(CostStrategy
    costStrategy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractgeotilecache.html#setCostStrategyDisk

    Parameters
    ----------

    costStrategy : CostStrategy
      Passed on as its number.
    """
    #  void QAbstractGeoTileCache::setCostStrategyDisk(CostStrategy
    #      costStrategy)
    self.uglySide.call(
        'ritual_ZN21QAbstractGeoTileCache19setCostStrategyDiskENS_12CostStr'
        'ategyE',
        costStrategy.value,
    )

  @overload(CostStrategy)
  def setCostStrategyMemory(self, costStrategy: CostStrategy) -> None:
    """
    Calls Qt's 'void
    QAbstractGeoTileCache::setCostStrategyMemory(CostStrategy costStrategy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractgeotilecache.html#setCostStrategyMemory

    Parameters
    ----------

    costStrategy : CostStrategy
      Passed on as its number.
    """
    #  void QAbstractGeoTileCache::setCostStrategyMemory(CostStrategy
    #      costStrategy)
    self.uglySide.call(
        'ritual_ZN21QAbstractGeoTileCache21setCostStrategyMemoryENS_12CostS'
        'trategyE',
        costStrategy.value,
    )

  @overload(CostStrategy)
  def setCostStrategyTexture(self, costStrategy: CostStrategy) -> None:
    """
    Calls Qt's 'void
    QAbstractGeoTileCache::setCostStrategyTexture(CostStrategy
    costStrategy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractgeotilecache.html#setCostStrategyTexture

    Parameters
    ----------

    costStrategy : CostStrategy
      Passed on as its number.
    """
    #  void QAbstractGeoTileCache::setCostStrategyTexture(CostStrategy
    #      costStrategy)
    self.uglySide.call(
        'ritual_ZN21QAbstractGeoTileCache22setCostStrategyTextureENS_12Cost'
        'StrategyE',
        costStrategy.value,
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QAbstractGeoTileCache::QAbstractGeoTileCache(QObject *parent)': the
    class is abstract, so C++ cannot make one, and the C++ class of ours does
    not fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'QAbstractGeoTileCache.__init__' has no cute function yet. Qt's "
        "'QAbstractGeoTileCache::QAbstractGeoTileCache(QObject *parent)': "
        "the class is abstract, so C++ cannot make one, and the C++ class "
        "of ours does not fill in every function it leaves open.")

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
    Calls Qt's 'void QAbstractGeoTileCache::clearAll()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractgeotilecache.html#clearAll
    """
    #  void QAbstractGeoTileCache::clearAll()
    self.uglySide.call('ritual_ZN21QAbstractGeoTileCache8clearAllEv')

  @overload(QGeoTileSpec, QByteArray, str)
  @overload(QGeoTileSpec, QByteArray, str, CacheAreas)
  def insert(
      self,
      spec: QGeoTileSpec,
      bytes: QByteArray,
      format: str,
      areas: CacheAreas = CacheAreas.AllCaches,
  ) -> None:
    """
    Calls Qt's 'void QAbstractGeoTileCache::insert(const QGeoTileSpec &spec,
    const QByteArray &bytes, const QString &format,
    QAbstractGeoTileCache::CacheAreas areas)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractgeotilecache.html#insert

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

    areas : CacheAreas
      Passed on as its number. May be left out, as in Qt: it is then
      CacheAreas.AllCaches.
    """
    #  void QAbstractGeoTileCache::insert(const QGeoTileSpec &spec, const
    #      QByteArray &bytes, const QString &format,
    #      QAbstractGeoTileCache::CacheAreas areas)
    self.uglySide.call(
        'ritual_ZN21QAbstractGeoTileCache6insertERK12QGeoTileSpecRK10QByteA'
        'rrayRK7QString6QFlagsINS_9CacheAreaEE',
        self._valueOf(spec), self._valueOf(bytes), format, areas.value,
    )

  @overload(QGeoTileSpec, str)
  def handleError(self, spec: QGeoTileSpec, errorString: str) -> None:
    """
    Calls Qt's 'void QAbstractGeoTileCache::handleError(const QGeoTileSpec
    &spec, const QString &errorString)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractgeotilecache.html#handleError

    Parameters
    ----------

    spec : QGeoTileSpec
      Passed on as a value: Qt reads the C++ QGeoTileSpec, which stays
      Python's own.

    errorString : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAbstractGeoTileCache::handleError(const QGeoTileSpec &spec,
    #      const QString &errorString)
    ritual = (
        'ritual_ZN21QAbstractGeoTileCache11handleErrorERK12QGeoTileSpecRK7Q'
        'String')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QAbstractGeoTileCache11handleErrorERK12QGeoTileSp'
          'ecRK7QString')
    self.uglySide.call(ritual, self._valueOf(spec), errorString)

  def init(self) -> None:
    """
    Calls Qt's 'void QAbstractGeoTileCache::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractgeotilecache.html#init
    """
    #  void QAbstractGeoTileCache::init()
    self.uglySide.call('ritual_ZN21QAbstractGeoTileCache4initEv')

  def printStats(self) -> None:
    """
    Calls Qt's 'void QAbstractGeoTileCache::printStats()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractgeotilecache.html#printStats
    """
    #  void QAbstractGeoTileCache::printStats()
    self.uglySide.call('ritual_ZN21QAbstractGeoTileCache10printStatsEv')

  @staticmethod
  def get(*__, **_) -> Never:
    """
    Qt's 'QSharedPointer<QGeoTileTexture> QAbstractGeoTileCache::get(const
    QGeoTileSpec &spec)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QAbstractGeoTileCache.get' has no cute function yet. Qt's "
        "'QSharedPointer<QGeoTileTexture> QAbstractGeoTileCache::get(const "
        "QGeoTileSpec &spec)': gives a type Python has no way to take yet.")
