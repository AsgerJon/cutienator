"""
QSampleCache binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/private/qsamplecache_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QSampleCache to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QThreadPool

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSampleCache(QObject):
  """
  The cute side of Qt's QSampleCache: a plain Python object standing in front
  of one C++ QSampleCache.

  It is built on the cute 'QObject', as Qt's QSampleCache is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSampleCache that has a ritual and that Python can
  call so far, 2 names in all: 'instance', 'threadPool'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSampleCache::~QSampleCache()': the destructor: Python never
    removes a C++ QSampleCache.
  - Qt's 'QFuture<SharedSamplePtr> QSampleCache::requestSampleFuture(const
    QUrl &a0, std::optional<int> targetSampleRate,
    std::optional<SampleSourceType> forceSourceType)': takes a type Python
    has no way to hand over yet.
  - Qt's 'bool QSampleCache::isCached(const QUrl &url, std::optional<int>
    targetSampleRate) const': takes a type Python has no way to hand over
    yet.
  - Qt's 'SampleLoadResult QSampleCache::loadSample(QSpan<const char> a0)':
    takes a type Python has no way to hand over yet.
  - Qt's 'SampleLoadResult
    QSampleCache::loadSampleViaDecoder(std::variant<QUrl, QByteArray> a0)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QFuture<SampleLoadResult>
    QSampleCache::loadSampleAsyncViaDecoder(QByteArray a0)': gives a type
    Python has no way to take yet.
  - Qt's 'void QSampleCache::removeUnreferencedSample(const QUrl &a0,
    std::optional<SampleRate> targetSampleRate)': takes a type Python has no
    way to hand over yet.
  - Qt's 'SampleLoadResult QSampleCache::loadSample(const QUrl &a0,
    std::optional<SampleSourceType> a1)': takes a type Python has no way to
    hand over yet.
  - Qt's 'QFuture<SampleLoadResult> QSampleCache::loadSampleAsync(const QUrl
    &a0, std::optional<SampleSourceType> a1)': takes a type Python has no way
    to hand over yet.

  What has no ritual
  ------------------

  1 of the 13 functions Qt declares: 1 not a gap.

  What to expect
  --------------

  - The C++ QSampleCache is created at the first use, not by
    'QSampleCache(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSampleCache.
  - Qt tells when it has removed the C++ QSampleCache. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QSampleCache that has no cute function yet, 'isCached',
    'loadSample', 'loadSampleAsync', 'loadSampleAsyncViaDecoder',
    'loadSampleViaDecoder', 'removeUnreferencedSample',
    'requestSampleFuture', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QSampleCache, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class SampleSourceType(CuteNum, scoped=True):
    """
    The enum 'QSampleCache::SampleSourceType' of Qt, with the 3 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    File = Kee[int](0)
    NetworkManager = Kee[int](1)
    AudioDecoder = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def instance() -> Optional[QSampleCache]:
    """
    Calls Qt's 'QSampleCache *QSampleCache::instance()'.

    Qt's own words: https://doc.qt.io/qt-6/qsamplecache.html#instance

    Returns
    -------

    Optional[QSampleCache]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSampleCache *QSampleCache::instance()
    address = Rituals.call('ritual_ZN12QSampleCache8instanceEv')
    return QSampleCache._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSampleCache'

  #  A C++ QSampleCache Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSampleCache'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    Notes what was given, for Qt's 'QSampleCache::QSampleCache(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsamplecache.html#QSampleCache

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QSampleCache::QSampleCache(QObject *parent)
    self._noteCreation(QSampleCache, lambda: Rituals.call(
        'ritual_ZN12QSampleCacheC1EP7QObject',
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

  def threadPool(self) -> Optional[QThreadPool]:
    """
    Calls Qt's 'QThreadPool *QSampleCache::threadPool()'.

    Qt's own words: https://doc.qt.io/qt-6/qsamplecache.html#threadPool

    Returns
    -------

    Optional[QThreadPool]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QThreadPool *QSampleCache::threadPool()
    address = self.uglySide.call('ritual_ZN12QSampleCache10threadPoolEv')
    from ..QtCore import QThreadPool
    return QThreadPool._cuteAt(address)

  @staticmethod
  def isCached(*__, **_) -> Never:
    """
    Qt's 'bool QSampleCache::isCached(const QUrl &url, std::optional<int>
    targetSampleRate) const': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QSampleCache.isCached' has no cute function yet. Qt's 'bool "
        "QSampleCache::isCached(const QUrl &url, std::optional<int> "
        "targetSampleRate) const': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def loadSample(*__, **_) -> Never:
    """
    - Qt's 'SampleLoadResult QSampleCache::loadSample(QSpan<const char> a0)':
      takes a type Python has no way to hand over yet.
    - Qt's 'SampleLoadResult QSampleCache::loadSample(const QUrl &a0,
      std::optional<SampleSourceType> a1)': takes a type Python has no way to
      hand over yet.
    """
    raise NotImplementedError(
        "'QSampleCache.loadSample' has no cute function yet. Qt's "
        "'SampleLoadResult QSampleCache::loadSample(QSpan<const char> a0)': "
        "takes a type Python has no way to hand over yet. Qt's "
        "'SampleLoadResult QSampleCache::loadSample(const QUrl &a0, "
        "std::optional<SampleSourceType> a1)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def loadSampleAsync(*__, **_) -> Never:
    """
    Qt's 'QFuture<SampleLoadResult> QSampleCache::loadSampleAsync(const QUrl
    &a0, std::optional<SampleSourceType> a1)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'QSampleCache.loadSampleAsync' has no cute function yet. Qt's "
        "'QFuture<SampleLoadResult> QSampleCache::loadSampleAsync(const "
        "QUrl &a0, std::optional<SampleSourceType> a1)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def loadSampleAsyncViaDecoder(*__, **_) -> Never:
    """
    Qt's 'QFuture<SampleLoadResult>
    QSampleCache::loadSampleAsyncViaDecoder(QByteArray a0)': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSampleCache.loadSampleAsyncViaDecoder' has no cute function yet. "
        "Qt's 'QFuture<SampleLoadResult> "
        "QSampleCache::loadSampleAsyncViaDecoder(QByteArray a0)': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def loadSampleViaDecoder(*__, **_) -> Never:
    """
    Qt's 'SampleLoadResult
    QSampleCache::loadSampleViaDecoder(std::variant<QUrl, QByteArray> a0)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSampleCache.loadSampleViaDecoder' has no cute function yet. Qt's "
        "'SampleLoadResult "
        "QSampleCache::loadSampleViaDecoder(std::variant<QUrl, QByteArray> "
        "a0)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def removeUnreferencedSample(*__, **_) -> Never:
    """
    Qt's 'void QSampleCache::removeUnreferencedSample(const QUrl &a0,
    std::optional<SampleRate> targetSampleRate)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QSampleCache.removeUnreferencedSample' has no cute function yet. "
        "Qt's 'void QSampleCache::removeUnreferencedSample(const QUrl &a0, "
        "std::optional<SampleRate> targetSampleRate)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def requestSampleFuture(*__, **_) -> Never:
    """
    Qt's 'QFuture<SharedSamplePtr> QSampleCache::requestSampleFuture(const
    QUrl &a0, std::optional<int> targetSampleRate,
    std::optional<SampleSourceType> forceSourceType)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSampleCache.requestSampleFuture' has no cute function yet. Qt's "
        "'QFuture<SharedSamplePtr> QSampleCache::requestSampleFuture(const "
        "QUrl &a0, std::optional<int> targetSampleRate, "
        "std::optional<SampleSourceType> forceSourceType)': takes a type "
        "Python has no way to hand over yet.")
