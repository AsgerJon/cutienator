"""
QPlatformSharedGraphicsCache binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/qpa/qplatformsharedgraphicscache.h, Qt 6.12.0. Changes
#  made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPlatformSharedGraphicsCache(QObject):
  """
  The cute side of Qt's QPlatformSharedGraphicsCache: a plain Python object
  standing in front of one C++ QPlatformSharedGraphicsCache.

  It is built on the cute 'QObject', as Qt's QPlatformSharedGraphicsCache is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPlatformSharedGraphicsCache that has a ritual and
  that Python can call so far, 6 names in all: 'metaObject', 'tr',
  'beginRequestBatch', 'ensureCacheInitialized', 'endRequestBatch',
  'requestBatchStarted'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPlatformSharedGraphicsCache::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QPlatformSharedGraphicsCache::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QPlatformSharedGraphicsCache::requestItems(const QByteArray
    &cacheId, const QList<quint32> &itemIds)': takes a type Python has no way
    to hand over yet.
  - Qt's 'void QPlatformSharedGraphicsCache::insertItems(const QByteArray
    &cacheId, const QList<quint32> &itemIds, const QList<QImage> &items)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void QPlatformSharedGraphicsCache::releaseItems(const QByteArray
    &cacheId, const QList<quint32> &itemIds)': takes a type Python has no way
    to hand over yet.
  - Qt's 'uint QPlatformSharedGraphicsCache::textureIdForBuffer(void
    *bufferId)': names 'void', which has no cute class yet.
  - Qt's 'void QPlatformSharedGraphicsCache::referenceBuffer(void
    *bufferId)': names 'void', which has no cute class yet.
  - Qt's 'bool QPlatformSharedGraphicsCache::dereferenceBuffer(void
    *bufferId)': names 'void', which has no cute class yet.
  - Qt's 'QSize QPlatformSharedGraphicsCache::sizeOfBuffer(void *bufferId)':
    names 'void', which has no cute class yet.
  - Qt's 'void *QPlatformSharedGraphicsCache::eglImageForBuffer(void
    *bufferId)': names 'void', which has no cute class yet.
  - Qt's 'void QPlatformSharedGraphicsCache::itemsMissing(const QByteArray
    &cacheId, const QList<quint32> &itemIds)': takes a type Python has no way
    to hand over yet.
  - Qt's 'void QPlatformSharedGraphicsCache::itemsAvailable(const QByteArray
    &cacheId, void *bufferId, const QList<quint32> &itemIds, const
    QList<QPoint> &positionsInBuffer)': names 'void', which has no cute class
    yet.
  - Qt's 'void QPlatformSharedGraphicsCache::itemsInvalidated(const
    QByteArray &cacheId, const QList<quint32> &itemIds)': takes a type Python
    has no way to hand over yet.
  - Qt's 'void QPlatformSharedGraphicsCache::itemsUpdated(const QByteArray
    &cacheId, void *bufferId, const QList<quint32> &itemIds, const
    QList<QPoint> &positionsInBuffer)': names 'void', which has no cute class
    yet.

  What has no ritual
  ------------------

  3 of the 23 functions Qt declares: 2 not a gap; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ QPlatformSharedGraphicsCache is created at the first use, not by
    'QPlatformSharedGraphicsCache(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPlatformSharedGraphicsCache.
  - Qt tells when it has removed the C++ QPlatformSharedGraphicsCache. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QPlatformSharedGraphicsCache that has no cute function
    yet, '__init__', 'dereferenceBuffer', 'eglImageForBuffer', 'insertItems',
    'itemsAvailable', 'itemsInvalidated', 'itemsMissing', 'itemsUpdated',
    'referenceBuffer', 'releaseItems', 'requestItems', 'sizeOfBuffer',
    'textureIdForBuffer', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  #  The enums Qt writes inside QPlatformSharedGraphicsCache, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class BufferType(CuteNum):
    """
    The enum 'QPlatformSharedGraphicsCache::BufferType' of Qt, with the 1
    names Qt gives in it.
    """

    OpenGLTexture = Kee[int](0)

  class PixelFormat(CuteNum):
    """
    The enum 'QPlatformSharedGraphicsCache::PixelFormat' of Qt, with the 1
    names Qt gives in it.
    """

    Alpha8 = Kee[int](0)

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
    Calls Qt's 'QString QPlatformSharedGraphicsCache::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformsharedgraphicscache.html#tr

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
    #  QString QPlatformSharedGraphicsCache::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN28QPlatformSharedGraphicsCache2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlatformSharedGraphicsCache'

  #  A C++ QPlatformSharedGraphicsCache Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPlatformSharedGraphicsCache'

  #  The functions Qt calls itself that QPlatformSharedGraphicsCache is the
  #  first to declare and that cannot be handed to Python yet, each as Qt
  #  declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'requestItems': (
          'void QPlatformSharedGraphicsCache::requestItems(const '
          'QByteArray &, const QList<quint32> &)',
      ),
      'insertItems': (
          'void QPlatformSharedGraphicsCache::insertItems(const QByteArray '
          '&, const QList<quint32> &, const QList<QImage> &)',
      ),
      'releaseItems': (
          'void QPlatformSharedGraphicsCache::releaseItems(const '
          'QByteArray &, const QList<quint32> &)',
      ),
      'textureIdForBuffer': (
          'uint QPlatformSharedGraphicsCache::textureIdForBuffer(void *)',
      ),
      'referenceBuffer': (
          'void QPlatformSharedGraphicsCache::referenceBuffer(void *)',
      ),
      'dereferenceBuffer': (
          'bool QPlatformSharedGraphicsCache::dereferenceBuffer(void *)',
      ),
      'sizeOfBuffer': (
          'QSize QPlatformSharedGraphicsCache::sizeOfBuffer(void *)',
      ),
      'eglImageForBuffer': (
          'void *QPlatformSharedGraphicsCache::eglImageForBuffer(void *)',
      ),
  }

  #  The functions Qt calls itself that QPlatformSharedGraphicsCache is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'beginRequestBatch': (
          ('_ZN28QPlatformSharedGraphicsCache17beginRequestBatchEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'ensureCacheInitialized': (
          ('_ZN28QPlatformSharedGraphicsCache22ensureCacheInitializedERK10Q'
           'ByteArrayNS_10BufferTypeENS_11PixelFormatE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QByteArray'),
               ('int', 'enum',
                'QtGui:QPlatformSharedGraphicsCache.BufferType'),
               ('int', 'enum',
                'QtGui:QPlatformSharedGraphicsCache.PixelFormat'),
           )),
      ),
      'endRequestBatch': (
          ('_ZN28QPlatformSharedGraphicsCache15endRequestBatchEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'requestBatchStarted': (
          ('_ZNK28QPlatformSharedGraphicsCache19requestBatchStartedEv',
           ('bool', 'number', ''),
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
    Calls Qt's 'const QMetaObject *QPlatformSharedGraphicsCache::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformsharedgraphicscache.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPlatformSharedGraphicsCache::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK28QPlatformSharedGraphicsCache10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def requestBatchStarted(self) -> bool:
    """
    Calls Qt's 'bool QPlatformSharedGraphicsCache::requestBatchStarted()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformsharedgraphicscache.html
    """
    #  bool QPlatformSharedGraphicsCache::requestBatchStarted() const
    return self.uglySide.call(
        'ritual_ZNK28QPlatformSharedGraphicsCache19requestBatchStartedEv',
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QPlatformSharedGraphicsCache::QPlatformSharedGraphicsCache(QObject
    *parent)': the class is abstract, so C++ cannot make one, and the C++
    class of ours does not fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'QPlatformSharedGraphicsCache.__init__' has no cute function yet. "
        "Qt's "
        "'QPlatformSharedGraphicsCache::QPlatformSharedGraphicsCache(QObject"
        " *parent)': the class is abstract, so C++ cannot make one, and the "
        "C++ class of ours does not fill in every function it leaves open.")

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

  def beginRequestBatch(self) -> None:
    """
    Calls Qt's 'void QPlatformSharedGraphicsCache::beginRequestBatch()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformsharedgraphicscache.html
    """
    #  void QPlatformSharedGraphicsCache::beginRequestBatch()
    self.uglySide.call(
        'ritual_ZN28QPlatformSharedGraphicsCache17beginRequestBatchEv',
    )

  @overload(QByteArray, BufferType, PixelFormat)
  def ensureCacheInitialized(
      self,
      cacheId: QByteArray,
      bufferType: BufferType,
      pixelFormat: PixelFormat,
  ) -> None:
    """
    Calls Qt's 'void
    QPlatformSharedGraphicsCache::ensureCacheInitialized(const QByteArray
    &cacheId, BufferType bufferType, PixelFormat pixelFormat)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformsharedgraphicscache.html

    Parameters
    ----------

    cacheId : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    bufferType : BufferType
      Passed on as its number.

    pixelFormat : PixelFormat
      Passed on as its number.
    """
    #  void QPlatformSharedGraphicsCache::ensureCacheInitialized(const
    #      QByteArray &cacheId, BufferType bufferType, PixelFormat
    #      pixelFormat)
    self.uglySide.call(
        'ritual_ZN28QPlatformSharedGraphicsCache22ensureCacheInitializedERK'
        '10QByteArrayNS_10BufferTypeENS_11PixelFormatE',
        self._valueOf(cacheId), bufferType.value, pixelFormat.value,
    )

  def endRequestBatch(self) -> None:
    """
    Calls Qt's 'void QPlatformSharedGraphicsCache::endRequestBatch()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformsharedgraphicscache.html#endRequestBatch
    """
    #  void QPlatformSharedGraphicsCache::endRequestBatch()
    self.uglySide.call(
        'ritual_ZN28QPlatformSharedGraphicsCache15endRequestBatchEv',
    )

  @staticmethod
  def dereferenceBuffer(*__, **_) -> Never:
    """
    Qt's 'bool QPlatformSharedGraphicsCache::dereferenceBuffer(void
    *bufferId)': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QPlatformSharedGraphicsCache.dereferenceBuffer' has no cute "
        "function yet. Qt's 'bool "
        "QPlatformSharedGraphicsCache::dereferenceBuffer(void *bufferId)': "
        "names 'void', which has no cute class yet.")

  @staticmethod
  def eglImageForBuffer(*__, **_) -> Never:
    """
    Qt's 'void *QPlatformSharedGraphicsCache::eglImageForBuffer(void
    *bufferId)': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QPlatformSharedGraphicsCache.eglImageForBuffer' has no cute "
        "function yet. Qt's 'void "
        "*QPlatformSharedGraphicsCache::eglImageForBuffer(void *bufferId)': "
        "names 'void', which has no cute class yet.")

  @staticmethod
  def insertItems(*__, **_) -> Never:
    """
    Qt's 'void QPlatformSharedGraphicsCache::insertItems(const QByteArray
    &cacheId, const QList<quint32> &itemIds, const QList<QImage> &items)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QPlatformSharedGraphicsCache.insertItems' has no cute function "
        "yet. Qt's 'void QPlatformSharedGraphicsCache::insertItems(const "
        "QByteArray &cacheId, const QList<quint32> &itemIds, const "
        "QList<QImage> &items)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def itemsAvailable(*__, **_) -> Never:
    """
    Qt's 'void QPlatformSharedGraphicsCache::itemsAvailable(const QByteArray
    &cacheId, void *bufferId, const QList<quint32> &itemIds, const
    QList<QPoint> &positionsInBuffer)': names 'void', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QPlatformSharedGraphicsCache.itemsAvailable' has no cute function "
        "yet. Qt's 'void QPlatformSharedGraphicsCache::itemsAvailable(const "
        "QByteArray &cacheId, void *bufferId, const QList<quint32> "
        "&itemIds, const QList<QPoint> &positionsInBuffer)': names 'void', "
        "which has no cute class yet.")

  @staticmethod
  def itemsInvalidated(*__, **_) -> Never:
    """
    Qt's 'void QPlatformSharedGraphicsCache::itemsInvalidated(const
    QByteArray &cacheId, const QList<quint32> &itemIds)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QPlatformSharedGraphicsCache.itemsInvalidated' has no cute "
        "function yet. Qt's 'void "
        "QPlatformSharedGraphicsCache::itemsInvalidated(const QByteArray "
        "&cacheId, const QList<quint32> &itemIds)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def itemsMissing(*__, **_) -> Never:
    """
    Qt's 'void QPlatformSharedGraphicsCache::itemsMissing(const QByteArray
    &cacheId, const QList<quint32> &itemIds)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'QPlatformSharedGraphicsCache.itemsMissing' has no cute function "
        "yet. Qt's 'void QPlatformSharedGraphicsCache::itemsMissing(const "
        "QByteArray &cacheId, const QList<quint32> &itemIds)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def itemsUpdated(*__, **_) -> Never:
    """
    Qt's 'void QPlatformSharedGraphicsCache::itemsUpdated(const QByteArray
    &cacheId, void *bufferId, const QList<quint32> &itemIds, const
    QList<QPoint> &positionsInBuffer)': names 'void', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QPlatformSharedGraphicsCache.itemsUpdated' has no cute function "
        "yet. Qt's 'void QPlatformSharedGraphicsCache::itemsUpdated(const "
        "QByteArray &cacheId, void *bufferId, const QList<quint32> "
        "&itemIds, const QList<QPoint> &positionsInBuffer)': names 'void', "
        "which has no cute class yet.")

  @staticmethod
  def referenceBuffer(*__, **_) -> Never:
    """
    Qt's 'void QPlatformSharedGraphicsCache::referenceBuffer(void
    *bufferId)': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QPlatformSharedGraphicsCache.referenceBuffer' has no cute "
        "function yet. Qt's 'void "
        "QPlatformSharedGraphicsCache::referenceBuffer(void *bufferId)': "
        "names 'void', which has no cute class yet.")

  @staticmethod
  def releaseItems(*__, **_) -> Never:
    """
    Qt's 'void QPlatformSharedGraphicsCache::releaseItems(const QByteArray
    &cacheId, const QList<quint32> &itemIds)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'QPlatformSharedGraphicsCache.releaseItems' has no cute function "
        "yet. Qt's 'void QPlatformSharedGraphicsCache::releaseItems(const "
        "QByteArray &cacheId, const QList<quint32> &itemIds)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def requestItems(*__, **_) -> Never:
    """
    Qt's 'void QPlatformSharedGraphicsCache::requestItems(const QByteArray
    &cacheId, const QList<quint32> &itemIds)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'QPlatformSharedGraphicsCache.requestItems' has no cute function "
        "yet. Qt's 'void QPlatformSharedGraphicsCache::requestItems(const "
        "QByteArray &cacheId, const QList<quint32> &itemIds)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def sizeOfBuffer(*__, **_) -> Never:
    """
    Qt's 'QSize QPlatformSharedGraphicsCache::sizeOfBuffer(void *bufferId)':
    names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QPlatformSharedGraphicsCache.sizeOfBuffer' has no cute function "
        "yet. Qt's 'QSize QPlatformSharedGraphicsCache::sizeOfBuffer(void "
        "*bufferId)': names 'void', which has no cute class yet.")

  @staticmethod
  def textureIdForBuffer(*__, **_) -> Never:
    """
    Qt's 'uint QPlatformSharedGraphicsCache::textureIdForBuffer(void
    *bufferId)': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QPlatformSharedGraphicsCache.textureIdForBuffer' has no cute "
        "function yet. Qt's 'uint "
        "QPlatformSharedGraphicsCache::textureIdForBuffer(void *bufferId)': "
        "names 'void', which has no cute class yet.")
