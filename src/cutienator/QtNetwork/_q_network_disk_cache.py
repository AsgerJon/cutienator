"""
QNetworkDiskCache binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/qnetworkdiskcache.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QAbstractNetworkCache

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QIODevice, QMetaObject, QUrl
  from . import QNetworkCacheMetaData, QNetworkDiskCachePrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QIODevice = WAIT['QIODevice']
  QNetworkCacheMetaData = WAIT['QNetworkCacheMetaData']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QNetworkDiskCache(QAbstractNetworkCache):
  """
  The cute side of Qt's QNetworkDiskCache: a plain Python object standing in
  front of one C++ QNetworkDiskCache.

  It is built on the cute 'QAbstractNetworkCache', as Qt's QNetworkDiskCache
  is built on Qt's QAbstractNetworkCache, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QNetworkDiskCache that has a ritual and that Python
  can call so far, 17 names in all: 'metaObject', 'tr', 'cacheDirectory',
  'setCacheDirectory', 'maximumCacheSize', 'setMaximumCacheSize',
  'cacheSize', 'metaData', 'updateMetaData', 'data', 'remove', 'prepare',
  'insert', 'fileMetaData', 'clear', 'expire', 'd_func'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QNetworkDiskCache::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QNetworkDiskCache::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QNetworkDiskCache::~QNetworkDiskCache()': the destructor: Python
    never removes a C++ QNetworkDiskCache.
  - Qt's 'const QNetworkDiskCachePrivate *QNetworkDiskCache::d_func() const':
    takes in Python what 'QNetworkDiskCachePrivate
    *QNetworkDiskCache::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 26 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QNetworkDiskCache is created at the first use, not by
    'QNetworkDiskCache(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QNetworkDiskCache.
  - Qt tells when it has removed the C++ QNetworkDiskCache. Every call on the
    cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QNetworkDiskCache::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkdiskcache.html#tr

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
    #  QString QNetworkDiskCache::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QNetworkDiskCache2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNetworkDiskCache'

  #  A C++ QNetworkDiskCache Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QNetworkDiskCache'

  #  The functions Qt calls itself that QNetworkDiskCache is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'expire': (
          ('_ZN17QNetworkDiskCache6expireEv',
           ('long long', 'number', ''),
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
    Calls Qt's 'const QMetaObject *QNetworkDiskCache::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkdiskcache.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QNetworkDiskCache::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QNetworkDiskCache10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def cacheDirectory(self) -> str:
    """
    Calls Qt's 'QString QNetworkDiskCache::cacheDirectory() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkdiskcache.html#cacheDirectory

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QNetworkDiskCache::cacheDirectory() const
    return self.uglySide.call(
        'ritual_ZNK17QNetworkDiskCache14cacheDirectoryEv',
    )

  def maximumCacheSize(self) -> int:
    """
    Calls Qt's 'qint64 QNetworkDiskCache::maximumCacheSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkdiskcache.html#maximumCacheSize
    """
    #  qint64 QNetworkDiskCache::maximumCacheSize() const
    return self.uglySide.call(
        'ritual_ZNK17QNetworkDiskCache16maximumCacheSizeEv',
    )

  def cacheSize(self) -> int:
    """
    Calls Qt's 'qint64 QNetworkDiskCache::cacheSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkdiskcache.html#cacheSize
    """
    #  qint64 QNetworkDiskCache::cacheSize() const
    ritual = 'ritual_ZNK17QNetworkDiskCache9cacheSizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QNetworkDiskCache9cacheSizeEv'
    return self.uglySide.call(ritual)

  @overload(str)
  def fileMetaData(self, fileName: str) -> QNetworkCacheMetaData:
    """
    Calls Qt's 'QNetworkCacheMetaData QNetworkDiskCache::fileMetaData(const
    QString &fileName) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkdiskcache.html#fileMetaData

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QNetworkCacheMetaData
      A new cute QNetworkCacheMetaData around the copy Qt gave back. Python
      owns it.
    """
    #  QNetworkCacheMetaData QNetworkDiskCache::fileMetaData(const QString
    #      &fileName) const
    address = self.uglySide.call(
        'ritual_ZNK17QNetworkDiskCache12fileMetaDataERK7QString', fileName,
    )
    from . import QNetworkCacheMetaData
    return QNetworkCacheMetaData._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setCacheDirectory(self, cacheDir: str) -> None:
    """
    Calls Qt's 'void QNetworkDiskCache::setCacheDirectory(const QString
    &cacheDir)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkdiskcache.html#setCacheDirectory

    Parameters
    ----------

    cacheDir : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QNetworkDiskCache::setCacheDirectory(const QString &cacheDir)
    self.uglySide.call(
        'ritual_ZN17QNetworkDiskCache17setCacheDirectoryERK7QString',
        cacheDir,
    )

  @overload(int)
  def setMaximumCacheSize(self, size: int) -> None:
    """
    Calls Qt's 'void QNetworkDiskCache::setMaximumCacheSize(qint64 size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkdiskcache.html#setMaximumCacheSize

    Parameters
    ----------

    size : int
      Passed on as it is.
    """
    #  void QNetworkDiskCache::setMaximumCacheSize(qint64 size)
    self.uglySide.call(
        'ritual_ZN17QNetworkDiskCache19setMaximumCacheSizeEx', size,
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
    'QNetworkDiskCache::QNetworkDiskCache(QObject *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkdiskcache.html#QNetworkDiskCache

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QNetworkDiskCache::QNetworkDiskCache(QObject *parent)
    self._noteCreation(QNetworkDiskCache, lambda: Rituals.call(
        'ritual_ZN17QNetworkDiskCacheC1EP7QObject',
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

  @overload(QUrl)
  def metaData(self, url: QUrl) -> QNetworkCacheMetaData:
    """
    Calls Qt's 'QNetworkCacheMetaData QNetworkDiskCache::metaData(const QUrl
    &url)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkdiskcache.html#metaData

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    Returns
    -------

    QNetworkCacheMetaData
      A new cute QNetworkCacheMetaData around the copy Qt gave back. Python
      owns it.
    """
    #  QNetworkCacheMetaData QNetworkDiskCache::metaData(const QUrl &url)
    ritual = 'ritual_ZN17QNetworkDiskCache8metaDataERK4QUrl'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QNetworkDiskCache8metaDataERK4QUrl'
    address = self.uglySide.call(ritual, self._valueOf(url))
    from . import QNetworkCacheMetaData
    return QNetworkCacheMetaData._cuteOwning(address)

  @overload(QNetworkCacheMetaData)
  def updateMetaData(self, metaData: QNetworkCacheMetaData) -> None:
    """
    Calls Qt's 'void QNetworkDiskCache::updateMetaData(const
    QNetworkCacheMetaData &metaData)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkdiskcache.html#updateMetaData

    Parameters
    ----------

    metaData : QNetworkCacheMetaData
      Passed on as a value: Qt reads the C++ QNetworkCacheMetaData, which
      stays Python's own.
    """
    #  void QNetworkDiskCache::updateMetaData(const QNetworkCacheMetaData
    #      &metaData)
    ritual = (
        'ritual_ZN17QNetworkDiskCache14updateMetaDataERK21QNetworkCacheMeta'
        'Data')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QNetworkDiskCache14updateMetaDataERK21QNetworkCac'
          'heMetaData')
    self.uglySide.call(ritual, self._valueOf(metaData))

  @overload(QUrl)
  def data(self, url: QUrl) -> Optional[QIODevice]:
    """
    Calls Qt's 'QIODevice *QNetworkDiskCache::data(const QUrl &url)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkdiskcache.html#data

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    Returns
    -------

    Optional[QIODevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIODevice *QNetworkDiskCache::data(const QUrl &url)
    ritual = 'ritual_ZN17QNetworkDiskCache4dataERK4QUrl'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QNetworkDiskCache4dataERK4QUrl'
    address = self.uglySide.call(ritual, self._valueOf(url))
    from ..QtCore import QIODevice
    return QIODevice._cuteAt(address)

  @overload(QUrl)
  def remove(self, url: QUrl) -> bool:
    """
    Calls Qt's 'bool QNetworkDiskCache::remove(const QUrl &url)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkdiskcache.html#remove

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  bool QNetworkDiskCache::remove(const QUrl &url)
    ritual = 'ritual_ZN17QNetworkDiskCache6removeERK4QUrl'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QNetworkDiskCache6removeERK4QUrl'
    return self.uglySide.call(ritual, self._valueOf(url))

  @overload(QNetworkCacheMetaData)
  def prepare(self, metaData: QNetworkCacheMetaData) -> Optional[QIODevice]:
    """
    Calls Qt's 'QIODevice *QNetworkDiskCache::prepare(const
    QNetworkCacheMetaData &metaData)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkdiskcache.html#prepare

    Parameters
    ----------

    metaData : QNetworkCacheMetaData
      Passed on as a value: Qt reads the C++ QNetworkCacheMetaData, which
      stays Python's own.

    Returns
    -------

    Optional[QIODevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIODevice *QNetworkDiskCache::prepare(const QNetworkCacheMetaData
    #      &metaData)
    ritual = 'ritual_ZN17QNetworkDiskCache7prepareERK21QNetworkCacheMetaData'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QNetworkDiskCache7prepareERK21QNetworkCacheMetaDa'
          'ta')
    address = self.uglySide.call(ritual, self._valueOf(metaData))
    from ..QtCore import QIODevice
    return QIODevice._cuteAt(address)

  @overload(QIODevice)
  @overload(NoneType)
  def insert(self, device: Optional[QIODevice]) -> None:
    """
    Calls Qt's 'void QNetworkDiskCache::insert(QIODevice *device)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkdiskcache.html#insert

    Parameters
    ----------

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QNetworkDiskCache::insert(QIODevice *device)
    ritual = 'ritual_ZN17QNetworkDiskCache6insertEP9QIODevice'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QNetworkDiskCache6insertEP9QIODevice'
    self.uglySide.call(ritual, self._addressOf(device))

  def clear(self) -> None:
    """
    Calls Qt's 'void QNetworkDiskCache::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkdiskcache.html#clear
    """
    #  void QNetworkDiskCache::clear()
    ritual = 'ritual_ZN17QNetworkDiskCache5clearEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QNetworkDiskCache5clearEv'
    self.uglySide.call(ritual)

  def expire(self) -> int:
    """
    Calls Qt's 'qint64 QNetworkDiskCache::expire()'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkdiskcache.html#expire
    """
    #  qint64 QNetworkDiskCache::expire()
    ritual = 'ritual_ZN17QNetworkDiskCache6expireEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QNetworkDiskCache6expireEv'
    return self.uglySide.call(ritual)

  def d_func(self) -> Optional[QNetworkDiskCachePrivate]:
    """
    Calls Qt's 'QNetworkDiskCachePrivate *QNetworkDiskCache::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkdiskcache.html#d_func

    Returns
    -------

    Optional[QNetworkDiskCachePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkDiskCachePrivate *QNetworkDiskCache::d_func()
    address = self.uglySide.call('ritual_ZN17QNetworkDiskCache6d_funcEv')
    from . import QNetworkDiskCachePrivate
    return QNetworkDiskCachePrivate._cuteAt(address)
