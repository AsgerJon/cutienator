"""
QOpenGLTextureCache binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpenGL/6.12.0/QtOpenGL/private/qopengltexturecache_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QOpenGLTextureCache to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, MetaCute, WAIT
from ..occult import Rituals
from ..QtGui import QOpenGLSharedResource
from . import QOpenGLTextureUploader

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtGui import QImage, QOpenGLContext, QPixmap
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QImage = WAIT['QImage']
  QOpenGLContext = WAIT['QOpenGLContext']
  QPixmap = WAIT['QPixmap']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QOpenGLTextureCache(QOpenGLSharedResource):
  """
  The cute side of Qt's QOpenGLTextureCache: a plain Python object standing
  in front of one C++ QOpenGLTextureCache.

  It is built on the cute 'QOpenGLSharedResource', as Qt's
  QOpenGLTextureCache is built on Qt's QOpenGLSharedResource, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QOpenGLTextureCache that has a ritual and that
  Python can call so far, 5 names in all: 'cacheForContext', 'bindTexture',
  'invalidate', 'invalidateResource', 'freeResource'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpenGLTextureCache::~QOpenGLTextureCache()': the destructor:
    Python never removes a C++ QOpenGLTextureCache.

  What to expect
  --------------

  - The C++ QOpenGLTextureCache is created at the first use, not by
    'QOpenGLTextureCache(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QOpenGLTextureCache.
  """

  #  The enums Qt writes inside QOpenGLTextureCache, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class BindResultFlag(CuteFlags, number='unsigned char', scoped=True):
    """
    The flags enum 'QOpenGLTextureCache::BindResultFlag' of Qt, with the 1
    names Qt gives in it. Qt names the type of its combinations
    'QOpenGLTextureCache::BindResultFlags'. C++ keeps these names inside the
    enum, so the class that holds the enum does not have them.
    """

    NewTexture = 0x1

  BindResultFlags = BindResultFlag

  #  The classes Qt writes inside QOpenGLTextureCache, each a class in here
  #  as in C++.

  class BindResult(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QOpenGLTextureCache::BindResult: a plain Python
    object standing in front of one C++ QOpenGLTextureCache::BindResult.

    C++ hands a QOpenGLTextureCache::BindResult around as a copy, so every
    C++ QOpenGLTextureCache::BindResult behind a cute one is Python's own: it
    is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QOpenGLTextureCache::BindResult yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QOpenGLTextureCache::BindResult::~BindResult()': the destructor:
      Python removes its C++ QOpenGLTextureCache::BindResult by it, and has
      no other use for it.

    What to expect
    --------------

    - The C++ QOpenGLTextureCache::BindResult is created at the first use,
      not by 'QOpenGLTextureCache::BindResult(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QOpenGLTextureCache::BindResult back gives a copy
      the ritual made for Python, in a new cute
      QOpenGLTextureCache::BindResult.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QOpenGLTextureCache::BindResult'

    #  Qt's '~QOpenGLTextureCache::BindResult()'. Naming it makes this a
    #  value class: Python owns every C++ QOpenGLTextureCache::BindResult
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN19QOpenGLTextureCache10BindResultD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QOpenGLContext)
  @overload(NoneType)
  def cacheForContext(
      context: Optional[QOpenGLContext],
  ) -> Optional[QOpenGLTextureCache]:
    """
    Calls Qt's 'QOpenGLTextureCache
    *QOpenGLTextureCache::cacheForContext(QOpenGLContext *context)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexturecache.html#cacheForContext

    Parameters
    ----------

    context : Optional[QOpenGLContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QOpenGLTextureCache]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOpenGLTextureCache
    #      *QOpenGLTextureCache::cacheForContext(QOpenGLContext *context)
    address = Rituals.call(
        'ritual_ZN19QOpenGLTextureCache15cacheForContextEP14QOpenGLContext',
        CuteMixin._addressOf(context),
    )
    return QOpenGLTextureCache._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpenGLTextureCache'

  #  A C++ QOpenGLTextureCache Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QOpenGLTextureCache'

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

  @overload(QOpenGLContext)
  @overload(NoneType)
  def __init__(self, a0: Optional[QOpenGLContext]) -> None:
    """
    Notes what was given, for Qt's
    'QOpenGLTextureCache::QOpenGLTextureCache(QOpenGLContext *a0)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexturecache.html#QOpenGLTextureCache

    Parameters
    ----------

    a0 : Optional[QOpenGLContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QOpenGLTextureCache::QOpenGLTextureCache(QOpenGLContext *a0)
    self._noteCreation(QOpenGLTextureCache, lambda: Rituals.call(
        'ritual_ZN19QOpenGLTextureCacheC1EP14QOpenGLContext',
        self._addressOf(a0),
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

  @overload(QOpenGLContext, QPixmap)
  @overload(NoneType, QPixmap)
  @overload(QOpenGLContext, QPixmap, QOpenGLTextureUploader.BindOptions)
  @overload(NoneType, QPixmap, QOpenGLTextureUploader.BindOptions)
  def bindTexture(
      self,
      context: Optional[QOpenGLContext],
      pixmap: QPixmap,
      options: QOpenGLTextureUploader.BindOptions = (
          QOpenGLTextureUploader.BindOptions.PremultipliedAlphaBindOption),
  ) -> BindResult:
    """
    Calls Qt's 'BindResult QOpenGLTextureCache::bindTexture(QOpenGLContext
    *context, const QPixmap &pixmap, QOpenGLTextureUploader::BindOptions
    options)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexturecache.html#bindTexture

    Parameters
    ----------

    context : Optional[QOpenGLContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pixmap : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.

    options : QOpenGLTextureUploader.BindOptions
      Passed on as its number. May be left out, as in Qt: it is then
      QOpenGLTextureUploader.BindOptions.PremultipliedAlphaBindOption.

    Returns
    -------

    BindResult
      A new cute QOpenGLTextureCache::BindResult around the copy Qt gave
      back. Python owns it.
    """
    #  BindResult QOpenGLTextureCache::bindTexture(QOpenGLContext *context,
    #      const QPixmap &pixmap, QOpenGLTextureUploader::BindOptions
    #      options)
    address = self.uglySide.call(
        'ritual_ZN19QOpenGLTextureCache11bindTextureEP14QOpenGLContextRK7QP'
        'ixmap6QFlagsIN22QOpenGLTextureUploader10BindOptionEE',
        self._addressOf(context), self._valueOf(pixmap), options.value,
    )
    return QOpenGLTextureCache.BindResult._cuteOwning(address)

  @overload(QOpenGLContext, QImage)
  @overload(NoneType, QImage)
  @overload(QOpenGLContext, QImage, QOpenGLTextureUploader.BindOptions)
  @overload(NoneType, QImage, QOpenGLTextureUploader.BindOptions)
  def bindTexture(
      self,
      context: Optional[QOpenGLContext],
      image: QImage,
      options: QOpenGLTextureUploader.BindOptions = (
          QOpenGLTextureUploader.BindOptions.PremultipliedAlphaBindOption),
  ) -> BindResult:
    """
    Calls Qt's 'BindResult QOpenGLTextureCache::bindTexture(QOpenGLContext
    *context, const QImage &image, QOpenGLTextureUploader::BindOptions
    options)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexturecache.html#bindTexture

    Parameters
    ----------

    context : Optional[QOpenGLContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.

    options : QOpenGLTextureUploader.BindOptions
      Passed on as its number. May be left out, as in Qt: it is then
      QOpenGLTextureUploader.BindOptions.PremultipliedAlphaBindOption.

    Returns
    -------

    BindResult
      A new cute QOpenGLTextureCache::BindResult around the copy Qt gave
      back. Python owns it.
    """
    #  BindResult QOpenGLTextureCache::bindTexture(QOpenGLContext *context,
    #      const QImage &image, QOpenGLTextureUploader::BindOptions options)
    address = self.uglySide.call(
        'ritual_ZN19QOpenGLTextureCache11bindTextureEP14QOpenGLContextRK6QI'
        'mage6QFlagsIN22QOpenGLTextureUploader10BindOptionEE',
        self._addressOf(context), self._valueOf(image), options.value,
    )
    return QOpenGLTextureCache.BindResult._cuteOwning(address)

  @overload(QOpenGLContext, int, QImage, QOpenGLTextureUploader.BindOptions)
  @overload(NoneType, int, QImage, QOpenGLTextureUploader.BindOptions)
  def bindTexture(
      self,
      context: Optional[QOpenGLContext],
      key: int,
      image: QImage,
      options: QOpenGLTextureUploader.BindOptions,
  ) -> BindResult:
    """
    Calls Qt's 'BindResult QOpenGLTextureCache::bindTexture(QOpenGLContext
    *context, qint64 key, const QImage &image,
    QOpenGLTextureUploader::BindOptions options)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexturecache.html#bindTexture

    Parameters
    ----------

    context : Optional[QOpenGLContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    key : int
      Passed on as it is.

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.

    options : QOpenGLTextureUploader.BindOptions
      Passed on as its number.

    Returns
    -------

    BindResult
      A new cute QOpenGLTextureCache::BindResult around the copy Qt gave
      back. Python owns it.
    """
    #  BindResult QOpenGLTextureCache::bindTexture(QOpenGLContext *context,
    #      qint64 key, const QImage &image,
    #      QOpenGLTextureUploader::BindOptions options)
    address = self.uglySide.call(
        'ritual_ZN19QOpenGLTextureCache11bindTextureEP14QOpenGLContextxRK6Q'
        'Image6QFlagsIN22QOpenGLTextureUploader10BindOptionEE',
        self._addressOf(context), key, self._valueOf(image), options.value,
    )
    return QOpenGLTextureCache.BindResult._cuteOwning(address)

  @overload(int)
  def invalidate(self, key: int) -> None:
    """
    Calls Qt's 'void QOpenGLTextureCache::invalidate(qint64 key)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexturecache.html#invalidate

    Parameters
    ----------

    key : int
      Passed on as it is.
    """
    #  void QOpenGLTextureCache::invalidate(qint64 key)
    self.uglySide.call('ritual_ZN19QOpenGLTextureCache10invalidateEx', key)

  def invalidateResource(self) -> None:
    """
    Calls Qt's 'void QOpenGLTextureCache::invalidateResource()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexturecache.html#invalidateResource
    """
    #  void QOpenGLTextureCache::invalidateResource()
    ritual = 'ritual_ZN19QOpenGLTextureCache18invalidateResourceEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QOpenGLTextureCache18invalidateResourceEv'
    self.uglySide.call(ritual)

  @overload(QOpenGLContext)
  @overload(NoneType)
  def freeResource(self, ctx: Optional[QOpenGLContext]) -> None:
    """
    Calls Qt's 'void QOpenGLTextureCache::freeResource(QOpenGLContext *ctx)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexturecache.html#freeResource

    Parameters
    ----------

    ctx : Optional[QOpenGLContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QOpenGLTextureCache::freeResource(QOpenGLContext *ctx)
    ritual = 'ritual_ZN19QOpenGLTextureCache12freeResourceEP14QOpenGLContext'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QOpenGLTextureCache12freeResourceEP14QOpenGLConte'
          'xt')
    self.uglySide.call(ritual, self._addressOf(ctx))
