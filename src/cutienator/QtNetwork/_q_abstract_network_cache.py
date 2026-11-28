"""
QAbstractNetworkCache binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/qabstractnetworkcache.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QIODevice, QMetaObject, QUrl
  from . import QAbstractNetworkCachePrivate, QNetworkCacheMetaData
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


class QAbstractNetworkCache(QObject):
  """
  The cute side of Qt's QAbstractNetworkCache: a plain Python object standing
  in front of one C++ QAbstractNetworkCache.

  It is built on the cute 'QObject', as Qt's QAbstractNetworkCache is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstractNetworkCache that has a ritual and that
  Python can call so far, 11 names in all: 'metaObject', 'tr', 'metaData',
  'updateMetaData', 'data', 'remove', 'cacheSize', 'prepare', 'insert',
  'clear', 'd_func'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QAbstractNetworkCache::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QAbstractNetworkCache::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QAbstractNetworkCache::~QAbstractNetworkCache()': the destructor:
    Python never removes a C++ QAbstractNetworkCache.
  - Qt's 'QAbstractNetworkCache::QAbstractNetworkCache(
    QAbstractNetworkCachePrivate &dd, QObject *parent)': takes a type Python
    has no way to hand over yet.
  - Qt's 'const QAbstractNetworkCachePrivate *QAbstractNetworkCache::d_func()
    const': takes in Python what 'QAbstractNetworkCachePrivate
    *QAbstractNetworkCache::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 21 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QAbstractNetworkCache is created at the first use, not by
    'QAbstractNetworkCache(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractNetworkCache.
  - Qt tells when it has removed the C++ QAbstractNetworkCache. Every call on
    the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QAbstractNetworkCache::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractnetworkcache.html#tr

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
    #  QString QAbstractNetworkCache::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QAbstractNetworkCache2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractNetworkCache'

  #  A C++ QAbstractNetworkCache Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAbstractNetworkCache'

  #  The functions Qt calls itself that QAbstractNetworkCache is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'metaData': (
          ('_ZN21QAbstractNetworkCache8metaDataERK4QUrl',
           ('address', 'value', 'QtNetwork:QNetworkCacheMetaData'),
           (
               ('address', 'value', 'QtCore:QUrl'),
           )),
      ),
      'updateMetaData': (
          ('_ZN21QAbstractNetworkCache14updateMetaDataERK21QNetworkCacheMet'
           'aData',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtNetwork:QNetworkCacheMetaData'),
           )),
      ),
      'data': (
          ('_ZN21QAbstractNetworkCache4dataERK4QUrl',
           ('address', 'address', 'QtCore:QIODevice'),
           (
               ('address', 'value', 'QtCore:QUrl'),
           )),
      ),
      'remove': (
          ('_ZN21QAbstractNetworkCache6removeERK4QUrl',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtCore:QUrl'),
           )),
      ),
      'cacheSize': (
          ('_ZNK21QAbstractNetworkCache9cacheSizeEv',
           ('long long', 'number', ''),
           ()),
      ),
      'prepare': (
          ('_ZN21QAbstractNetworkCache7prepareERK21QNetworkCacheMetaData',
           ('address', 'address', 'QtCore:QIODevice'),
           (
               ('address', 'value', 'QtNetwork:QNetworkCacheMetaData'),
           )),
      ),
      'insert': (
          ('_ZN21QAbstractNetworkCache6insertEP9QIODevice',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QIODevice'),
           )),
      ),
      'clear': (
          ('_ZN21QAbstractNetworkCache5clearEv',
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
    Calls Qt's 'const QMetaObject *QAbstractNetworkCache::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractnetworkcache.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QAbstractNetworkCache::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QAbstractNetworkCache10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def cacheSize(self) -> int:
    """
    Calls Qt's 'qint64 QAbstractNetworkCache::cacheSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractnetworkcache.html#cacheSize
    """
    #  qint64 QAbstractNetworkCache::cacheSize() const
    return self.uglySide.call(
        'ritual_ZNK21QAbstractNetworkCache9cacheSizeEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    'QAbstractNetworkCache::QAbstractNetworkCache(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractnetworkcache.html#QAbstractNetworkCache

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QAbstractNetworkCache::QAbstractNetworkCache(QObject *parent)
    self._noteCreation(QAbstractNetworkCache, lambda: Rituals.call(
        'ritual_ZN21QAbstractNetworkCacheC1EP7QObject',
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
    Calls Qt's 'QNetworkCacheMetaData QAbstractNetworkCache::metaData(const
    QUrl &url)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractnetworkcache.html#metaData

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
    #  QNetworkCacheMetaData QAbstractNetworkCache::metaData(const QUrl &url)
    address = self.uglySide.call(
        'ritual_ZN21QAbstractNetworkCache8metaDataERK4QUrl',
        self._valueOf(url),
    )
    from . import QNetworkCacheMetaData
    return QNetworkCacheMetaData._cuteOwning(address)

  @overload(QNetworkCacheMetaData)
  def updateMetaData(self, metaData: QNetworkCacheMetaData) -> None:
    """
    Calls Qt's 'void QAbstractNetworkCache::updateMetaData(const
    QNetworkCacheMetaData &metaData)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractnetworkcache.html#updateMetaData

    Parameters
    ----------

    metaData : QNetworkCacheMetaData
      Passed on as a value: Qt reads the C++ QNetworkCacheMetaData, which
      stays Python's own.
    """
    #  void QAbstractNetworkCache::updateMetaData(const QNetworkCacheMetaData
    #      &metaData)
    self.uglySide.call(
        'ritual_ZN21QAbstractNetworkCache14updateMetaDataERK21QNetworkCache'
        'MetaData',
        self._valueOf(metaData),
    )

  @overload(QUrl)
  def data(self, url: QUrl) -> Optional[QIODevice]:
    """
    Calls Qt's 'QIODevice *QAbstractNetworkCache::data(const QUrl &url)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractnetworkcache.html#data

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
    #  QIODevice *QAbstractNetworkCache::data(const QUrl &url)
    address = self.uglySide.call(
        'ritual_ZN21QAbstractNetworkCache4dataERK4QUrl', self._valueOf(url),
    )
    from ..QtCore import QIODevice
    return QIODevice._cuteAt(address)

  @overload(QUrl)
  def remove(self, url: QUrl) -> bool:
    """
    Calls Qt's 'bool QAbstractNetworkCache::remove(const QUrl &url)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractnetworkcache.html#remove

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  bool QAbstractNetworkCache::remove(const QUrl &url)
    return self.uglySide.call(
        'ritual_ZN21QAbstractNetworkCache6removeERK4QUrl',
        self._valueOf(url),
    )

  @overload(QNetworkCacheMetaData)
  def prepare(self, metaData: QNetworkCacheMetaData) -> Optional[QIODevice]:
    """
    Calls Qt's 'QIODevice *QAbstractNetworkCache::prepare(const
    QNetworkCacheMetaData &metaData)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractnetworkcache.html#prepare

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
    #  QIODevice *QAbstractNetworkCache::prepare(const QNetworkCacheMetaData
    #      &metaData)
    address = self.uglySide.call(
        'ritual_ZN21QAbstractNetworkCache7prepareERK21QNetworkCacheMetaData',
        self._valueOf(metaData),
    )
    from ..QtCore import QIODevice
    return QIODevice._cuteAt(address)

  @overload(QIODevice)
  @overload(NoneType)
  def insert(self, device: Optional[QIODevice]) -> None:
    """
    Calls Qt's 'void QAbstractNetworkCache::insert(QIODevice *device)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractnetworkcache.html#insert

    Parameters
    ----------

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractNetworkCache::insert(QIODevice *device)
    self.uglySide.call(
        'ritual_ZN21QAbstractNetworkCache6insertEP9QIODevice',
        self._addressOf(device),
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QAbstractNetworkCache::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractnetworkcache.html#clear
    """
    #  void QAbstractNetworkCache::clear()
    self.uglySide.call('ritual_ZN21QAbstractNetworkCache5clearEv')

  def d_func(self) -> Optional[QAbstractNetworkCachePrivate]:
    """
    Calls Qt's 'QAbstractNetworkCachePrivate
    *QAbstractNetworkCache::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractnetworkcache.html#d_func

    Returns
    -------

    Optional[QAbstractNetworkCachePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractNetworkCachePrivate *QAbstractNetworkCache::d_func()
    address = self.uglySide.call('ritual_ZN21QAbstractNetworkCache6d_funcEv')
    from . import QAbstractNetworkCachePrivate
    return QAbstractNetworkCachePrivate._cuteAt(address)
