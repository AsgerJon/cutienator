"""
QOpenGL2GradientCache binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpenGL/6.12.0/QtOpenGL/private/qopenglgradientcache_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QOpenGL2GradientCache to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtGui import QOpenGLSharedResource

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtGui import QGradient, QOpenGLContext, QRgba64
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGradient = WAIT['QGradient']
  QOpenGLContext = WAIT['QOpenGLContext']
  QRgba64 = WAIT['QRgba64']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QOpenGL2GradientCache(QOpenGLSharedResource):
  """
  The cute side of Qt's QOpenGL2GradientCache: a plain Python object standing
  in front of one C++ QOpenGL2GradientCache.

  It is built on the cute 'QOpenGLSharedResource', as Qt's
  QOpenGL2GradientCache is built on Qt's QOpenGLSharedResource, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QOpenGL2GradientCache that has a ritual and that
  Python can call so far, 8 names in all: 'getBuffer', 'paletteSize',
  'invalidateResource', 'freeResource', 'maxCacheSize',
  'generateGradientColorTable', 'addCacheElement', 'cleanCache'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpenGL2GradientCache::~QOpenGL2GradientCache()': the destructor:
    Python never removes a C++ QOpenGL2GradientCache.
  - Qt's 'void QOpenGL2GradientCache::generateGradientColorTable(const
    QGradient &gradient, uint *colorTable, int size, qreal opacity) const':
    takes a number to change where it is.

  What has no ritual
  ------------------

  1 of the 12 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QOpenGL2GradientCache is created at the first use, not by
    'QOpenGL2GradientCache(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QOpenGL2GradientCache.
  - Each name of Qt's QOpenGL2GradientCache that has no cute function yet,
    'cacheForContext', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpenGL2GradientCache'

  #  A C++ QOpenGL2GradientCache Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QOpenGL2GradientCache'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def paletteSize(self) -> int:
    """
    Calls Qt's 'int QOpenGL2GradientCache::paletteSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengl2gradientcache.html#paletteSize
    """
    #  int QOpenGL2GradientCache::paletteSize() const
    return self.uglySide.call(
        'ritual_ZNK21QOpenGL2GradientCache11paletteSizeEv',
    )

  def maxCacheSize(self) -> int:
    """
    Calls Qt's 'int QOpenGL2GradientCache::maxCacheSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengl2gradientcache.html#maxCacheSize
    """
    #  int QOpenGL2GradientCache::maxCacheSize() const
    return self.uglySide.call(
        'ritual_ZNK21QOpenGL2GradientCache12maxCacheSizeEv',
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

  @overload(QOpenGLContext)
  @overload(NoneType)
  def __init__(self, a0: Optional[QOpenGLContext]) -> None:
    """
    Notes what was given, for Qt's
    'QOpenGL2GradientCache::QOpenGL2GradientCache(QOpenGLContext *a0)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengl2gradientcache.html#QOpenGL2GradientCache

    Parameters
    ----------

    a0 : Optional[QOpenGLContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QOpenGL2GradientCache::QOpenGL2GradientCache(QOpenGLContext *a0)
    self._noteCreation(QOpenGL2GradientCache, lambda: Rituals.call(
        'ritual_ZN21QOpenGL2GradientCacheC1EP14QOpenGLContext',
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

  @overload(QGradient, float)
  def getBuffer(self, gradient: QGradient, opacity: float) -> int:
    """
    Calls Qt's 'GLuint QOpenGL2GradientCache::getBuffer(const QGradient
    &gradient, qreal opacity)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengl2gradientcache.html#getBuffer

    Parameters
    ----------

    gradient : QGradient
      Passed on as a value: Qt reads the C++ QGradient, which stays Python's
      own.

    opacity : float
      Passed on as it is.
    """
    #  GLuint QOpenGL2GradientCache::getBuffer(const QGradient &gradient,
    #      qreal opacity)
    return self.uglySide.call(
        'ritual_ZN21QOpenGL2GradientCache9getBufferERK9QGradientd',
        self._valueOf(gradient), opacity,
    )

  def invalidateResource(self) -> None:
    """
    Calls Qt's 'void QOpenGL2GradientCache::invalidateResource()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengl2gradientcache.html#invalidateResource
    """
    #  void QOpenGL2GradientCache::invalidateResource()
    ritual = 'ritual_ZN21QOpenGL2GradientCache18invalidateResourceEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QOpenGL2GradientCache18invalidateResourceEv'
    self.uglySide.call(ritual)

  @overload(QOpenGLContext)
  @overload(NoneType)
  def freeResource(self, ctx: Optional[QOpenGLContext]) -> None:
    """
    Calls Qt's 'void QOpenGL2GradientCache::freeResource(QOpenGLContext
    *ctx)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengl2gradientcache.html#freeResource

    Parameters
    ----------

    ctx : Optional[QOpenGLContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QOpenGL2GradientCache::freeResource(QOpenGLContext *ctx)
    ritual = (
        'ritual_ZN21QOpenGL2GradientCache12freeResourceEP14QOpenGLContext')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QOpenGL2GradientCache12freeResourceEP14QOpenGLCon'
          'text')
    self.uglySide.call(ritual, self._addressOf(ctx))

  @overload(QGradient, QRgba64, int, float)
  @overload(QGradient, NoneType, int, float)
  def generateGradientColorTable(
      self,
      gradient: QGradient,
      colorTable: Optional[QRgba64],
      size: int,
      opacity: float,
  ) -> None:
    """
    Calls Qt's 'void QOpenGL2GradientCache::generateGradientColorTable(const
    QGradient &gradient, QRgba64 *colorTable, int size, qreal opacity)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengl2gradientcache.html

    Parameters
    ----------

    gradient : QGradient
      Passed on as a value: Qt reads the C++ QGradient, which stays Python's
      own.

    colorTable : Optional[QRgba64]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    size : int
      Passed on as it is.

    opacity : float
      Passed on as it is.
    """
    #  void QOpenGL2GradientCache::generateGradientColorTable(const QGradient
    #      &gradient, QRgba64 *colorTable, int size, qreal opacity) const
    self.uglySide.call(
        'ritual_ZNK21QOpenGL2GradientCache26generateGradientColorTableERK9Q'
        'GradientP7QRgba64id',
        self._valueOf(gradient), self._addressOf(colorTable), size, opacity,
    )

  @overload(int, QGradient, float)
  def addCacheElement(
      self,
      hash_val: int,
      gradient: QGradient,
      opacity: float,
  ) -> int:
    """
    Calls Qt's 'GLuint QOpenGL2GradientCache::addCacheElement(quint64
    hash_val, const QGradient &gradient, qreal opacity)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengl2gradientcache.html#addCacheElement

    Parameters
    ----------

    hash_val : int
      Passed on as it is.

    gradient : QGradient
      Passed on as a value: Qt reads the C++ QGradient, which stays Python's
      own.

    opacity : float
      Passed on as it is.
    """
    #  GLuint QOpenGL2GradientCache::addCacheElement(quint64 hash_val, const
    #      QGradient &gradient, qreal opacity)
    return self.uglySide.call(
        'ritual_ZN21QOpenGL2GradientCache15addCacheElementEyRK9QGradientd',
        hash_val, self._valueOf(gradient), opacity,
    )

  def cleanCache(self) -> None:
    """
    Calls Qt's 'void QOpenGL2GradientCache::cleanCache()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengl2gradientcache.html#cleanCache
    """
    #  void QOpenGL2GradientCache::cleanCache()
    self.uglySide.call('ritual_ZN21QOpenGL2GradientCache10cleanCacheEv')

  @staticmethod
  def cacheForContext(*__, **_) -> Never:
    """
    Qt's 'QOpenGL2GradientCache
    *QOpenGL2GradientCache::cacheForContext(QOpenGLContext *context)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'qt_gradient_caches'.
    """
    raise NotImplementedError(
        "'QOpenGL2GradientCache.cacheForContext' has no cute function yet. "
        "Qt's 'QOpenGL2GradientCache "
        "*QOpenGL2GradientCache::cacheForContext(QOpenGLContext *context)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'qt_gradient_caches'.")
