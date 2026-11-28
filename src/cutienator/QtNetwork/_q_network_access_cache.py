"""
QNetworkAccessCache binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qnetworkaccesscache_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QNetworkAccessCache to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaObject, QTimerEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QTimerEvent = WAIT['QTimerEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QNetworkAccessCache(QObject):
  """
  The cute side of Qt's QNetworkAccessCache: a plain Python object standing
  in front of one C++ QNetworkAccessCache.

  It is built on the cute 'QObject', as Qt's QNetworkAccessCache is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QNetworkAccessCache that has a ritual and that
  Python can call so far, 3 names in all: 'metaObject', 'hasEntry',
  'timerEvent'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QNetworkAccessCache::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QNetworkAccessCache::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QNetworkAccessCache::~QNetworkAccessCache()': the destructor:
    Python never removes a C++ QNetworkAccessCache.

  What has no ritual
  ------------------

  11 of the 17 functions Qt declares: 8 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 2 not a gap;
  1 leans on 'QNetworkAccessCache.

  What to expect
  --------------

  - The C++ QNetworkAccessCache is created at the first use, not by
    'QNetworkAccessCache(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QNetworkAccessCache.
  - Qt tells when it has removed the C++ QNetworkAccessCache. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QNetworkAccessCache that has no cute function yet,
    'addEntry', 'clear', 'linkEntry', 'releaseEntry', 'removeEntry',
    'requestEntryNow', 'unlinkEntry', 'updateTimer', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QNetworkAccessCache, each a class in here
  #  as in C++.

  class CacheableObject(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QNetworkAccessCache::CacheableObject: a plain
    Python object standing in front of one C++
    QNetworkAccessCache::CacheableObject.

    What exists
    -----------

    Every function of Qt's QNetworkAccessCache::CacheableObject that has a
    ritual and that Python can call so far, 2 names in all: 'dispose',
    'cacheKey'. It can be made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QNetworkAccessCache::CacheableObject::~CacheableObject()': the
      destructor: Python never removes a C++
      QNetworkAccessCache::CacheableObject.

    What to expect
    --------------

    - The C++ QNetworkAccessCache::CacheableObject is created at the first
      use, not by 'QNetworkAccessCache::CacheableObject(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - Python never removes the C++ QNetworkAccessCache::CacheableObject.
    """

    #  The enums Qt writes inside QNetworkAccessCache::CacheableObject, each
    #  a class in here as in C++, and the names Qt has for the combinations
    #  of its flags enums.

    class Option(CuteFlags, scoped=True):
      """
      The flags enum 'QNetworkAccessCache::CacheableObject::Option' of Qt,
      with the 2 names Qt gives in it. Qt names the type of its combinations
      'QNetworkAccessCache::CacheableObject::Options'. C++ keeps these names
      inside the enum, so the class that holds the enum does not have them.
      """

      Expires = 0x1
      Shareable = 0x2

    Options = Option

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QNetworkAccessCache::CacheableObject'

    #  A C++ QNetworkAccessCache::CacheableObject Python makes is of a C++
    #  class of ours, in which Python can take functions over. This ritual
    #  hands one over; see 'CuteMixin._takeOver'.
    __take_ritual__ = 'ritual_take_QNetworkAccessCache_CacheableObject'

    #  The functions Qt calls itself that
    #  QNetworkAccessCache::CacheableObject is the first to declare. A class
    #  of a program built on it can write one anew, and Qt then calls that.
    #  For each name: the key C++ knows the function by, what it gives, and
    #  what it takes.
    __virtual_functions__ = {
        'dispose': (
            ('_ZN19QNetworkAccessCache15CacheableObject7disposeEv',
             ('nothing', 'nothing', ''),
             ()),
        ),
    }

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def cacheKey(self) -> QByteArray:
      """
      Calls Qt's 'QByteArray QNetworkAccessCache::CacheableObject::cacheKey()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qnetworkaccesscache-cacheableobject.html

      Returns
      -------

      QByteArray
        A new cute QByteArray around the copy Qt gave back. Python owns it.
      """
      #  QByteArray QNetworkAccessCache::CacheableObject::cacheKey() const
      address = self.uglySide.call(
          'ritual_ZNK19QNetworkAccessCache15CacheableObject8cacheKeyEv',
      )
      from ..QtCore import QByteArray
      return QByteArray._cuteOwning(address)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(Options)
    def __init__(self, options: Options) -> None:
      """
      Notes what was given, for Qt's
      'QNetworkAccessCache::CacheableObject::CacheableObject(Options
      options)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qnetworkaccesscache-cacheableobject.html

      Parameters
      ----------

      options : Options
        Passed on as its number.
      """
      #  QNetworkAccessCache::CacheableObject::CacheableObject(Options
      #      options)
      self._noteCreation(
          QNetworkAccessCache.CacheableObject, lambda: Rituals.call(
              'ritual_ZN19QNetworkAccessCache15CacheableObjectC1E6QFlagsINS'
              '0_6OptionEE',
              options.value,
          ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def dispose(self) -> None:
      """
      Calls Qt's 'void QNetworkAccessCache::CacheableObject::dispose()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qnetworkaccesscache-cacheableobject.html#dispose
      """
      #  void QNetworkAccessCache::CacheableObject::dispose()
      self.uglySide.call(
          'ritual_ZN19QNetworkAccessCache15CacheableObject7disposeEv',
      )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNetworkAccessCache'

  #  A C++ QNetworkAccessCache Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QNetworkAccessCache'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QNetworkAccessCache::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccesscache.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QNetworkAccessCache::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QNetworkAccessCache10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(QByteArray)
  def hasEntry(self, key: QByteArray) -> bool:
    """
    Calls Qt's 'bool QNetworkAccessCache::hasEntry(const QByteArray &key)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkaccesscache.html#hasEntry

    Parameters
    ----------

    key : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  bool QNetworkAccessCache::hasEntry(const QByteArray &key) const
    return self.uglySide.call(
        'ritual_ZNK19QNetworkAccessCache8hasEntryERK10QByteArray',
        self._valueOf(key),
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

  @overload(QTimerEvent)
  @overload(NoneType)
  def timerEvent(self, a0: Optional[QTimerEvent]) -> None:
    """
    Calls Qt's 'void QNetworkAccessCache::timerEvent(QTimerEvent *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccesscache.html#timerEvent

    Parameters
    ----------

    a0 : Optional[QTimerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QNetworkAccessCache::timerEvent(QTimerEvent *a0)
    self.uglySide.call(
        'ritual_ZN19QNetworkAccessCache10timerEventEP11QTimerEvent',
        self._addressOf(a0),
    )

  @staticmethod
  def addEntry(*__, **_) -> Never:
    """
    Qt's 'void QNetworkAccessCache::addEntry(const QByteArray &key,
    CacheableObject *entry, std::optional<qint64>
    connectionCacheExpiryTimeoutSeconds)': Qt's library has no name for it,
    and its code in Qt's source does not compile apart from its file:
    allocation of incomplete type 'Node'.
    """
    raise NotImplementedError(
        "'QNetworkAccessCache.addEntry' has no cute function yet. Qt's "
        "'void QNetworkAccessCache::addEntry(const QByteArray &key, "
        "CacheableObject *entry, std::optional<qint64> "
        "connectionCacheExpiryTimeoutSeconds)': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: allocation of incomplete type 'Node'.")

  @staticmethod
  def clear(*__, **_) -> Never:
    """
    Qt's 'void QNetworkAccessCache::clear()': Qt's library has no name for
    it, and its code in Qt's source does not compile apart from its file:
    member access into incomplete type 'QNetworkAccessCache::Node'.
    """
    raise NotImplementedError(
        "'QNetworkAccessCache.clear' has no cute function yet. Qt's 'void "
        "QNetworkAccessCache::clear()': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "member access into incomplete type 'QNetworkAccessCache::Node'.")

  @staticmethod
  def linkEntry(*__, **_) -> Never:
    """
    Qt's 'void QNetworkAccessCache::linkEntry(const QByteArray &key)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: member access into incomplete type 'Node'.
    """
    raise NotImplementedError(
        "'QNetworkAccessCache.linkEntry' has no cute function yet. Qt's "
        "'void QNetworkAccessCache::linkEntry(const QByteArray &key)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: member access into incomplete type "
        "'Node'.")

  @staticmethod
  def releaseEntry(*__, **_) -> Never:
    """
    Qt's 'void QNetworkAccessCache::releaseEntry(const QByteArray &key)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: member access into incomplete type 'Node'.
    """
    raise NotImplementedError(
        "'QNetworkAccessCache.releaseEntry' has no cute function yet. Qt's "
        "'void QNetworkAccessCache::releaseEntry(const QByteArray &key)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: member access into incomplete "
        "type 'Node'.")

  @staticmethod
  def removeEntry(*__, **_) -> Never:
    """
    Qt's 'void QNetworkAccessCache::removeEntry(const QByteArray &key)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: member access into incomplete type 'Node'.
    """
    raise NotImplementedError(
        "'QNetworkAccessCache.removeEntry' has no cute function yet. Qt's "
        "'void QNetworkAccessCache::removeEntry(const QByteArray &key)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: member access into incomplete "
        "type 'Node'.")

  @staticmethod
  def requestEntryNow(*__, **_) -> Never:
    """
    Qt's 'CacheableObject *QNetworkAccessCache::requestEntryNow(const
    QByteArray &key)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: member access into
    incomplete type 'Node'.
    """
    raise NotImplementedError(
        "'QNetworkAccessCache.requestEntryNow' has no cute function yet. "
        "Qt's 'CacheableObject *QNetworkAccessCache::requestEntryNow(const "
        "QByteArray &key)': Qt's library has no name for it, and its code "
        "in Qt's source does not compile apart from its file: member access "
        "into incomplete type 'Node'.")

  @staticmethod
  def unlinkEntry(*__, **_) -> Never:
    """
    Qt's 'bool QNetworkAccessCache::unlinkEntry(const QByteArray &key)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: member access into incomplete type 'Node'.
    """
    raise NotImplementedError(
        "'QNetworkAccessCache.unlinkEntry' has no cute function yet. Qt's "
        "'bool QNetworkAccessCache::unlinkEntry(const QByteArray &key)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: member access into incomplete "
        "type 'Node'.")

  @staticmethod
  def updateTimer(*__, **_) -> Never:
    """
    Qt's 'void QNetworkAccessCache::updateTimer()': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    member access into incomplete type 'Node'.
    """
    raise NotImplementedError(
        "'QNetworkAccessCache.updateTimer' has no cute function yet. Qt's "
        "'void QNetworkAccessCache::updateTimer()': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: member access into incomplete type 'Node'.")
