"""
QImageTextureGlyphCache binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qtextureglyphcache_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QImageTextureGlyphCache to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QFontEngine, QTextureGlyphCache

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QColor, QFixedPoint, QImage, QTransform
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QFixedPoint = WAIT['QFixedPoint']
  QTransform = WAIT['QTransform']


class QImageTextureGlyphCache(QTextureGlyphCache):
  """
  The cute side of Qt's QImageTextureGlyphCache: a plain Python object
  standing in front of one C++ QImageTextureGlyphCache.

  It is built on the cute 'QTextureGlyphCache', as Qt's
  QImageTextureGlyphCache is built on Qt's QTextureGlyphCache, and has
  everything that class has.

  C++ hands a QImageTextureGlyphCache around as a copy, so every C++
  QImageTextureGlyphCache behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QImageTextureGlyphCache that has a ritual and that
  Python can call so far, 4 names in all: 'createTextureData',
  'resizeTextureData', 'fillTexture', 'image'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QImageTextureGlyphCache::~QImageTextureGlyphCache()': the
    destructor: Python removes its C++ QImageTextureGlyphCache by it, and has
    no other use for it.

  What to expect
  --------------

  - The C++ QImageTextureGlyphCache is created at the first use, not by
    'QImageTextureGlyphCache(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QImageTextureGlyphCache back gives a copy the ritual
    made for Python, in a new cute QImageTextureGlyphCache.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QImageTextureGlyphCache'

  #  A C++ QImageTextureGlyphCache Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QImageTextureGlyphCache'

  #  Qt's '~QImageTextureGlyphCache()'. Naming it makes this a value class:
  #  Python owns every C++ QImageTextureGlyphCache behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN23QImageTextureGlyphCacheD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def image(self) -> QImage:
    """
    Calls Qt's 'const QImage &QImageTextureGlyphCache::image() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimagetextureglyphcache.html#image

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  const QImage &QImageTextureGlyphCache::image() const
    address = self.uglySide.call(
        'ritual_ZNK23QImageTextureGlyphCache5imageEv',
    )
    from . import QImage
    return QImage._cuteOwning(address)

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

  @overload(QFontEngine.GlyphFormat, QTransform)
  @overload(QFontEngine.GlyphFormat, QTransform, QColor)
  def __init__(
      self,
      format: QFontEngine.GlyphFormat,
      matrix: QTransform,
      color: Optional[QColor] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QImageTextureGlyphCache::QImageTextureGlyphCache(QFontEngine::
    GlyphFormat format, const QTransform &matrix, const QColor &color)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qimagetextureglyphcache.html

    Parameters
    ----------

    format : QFontEngine.GlyphFormat
      Passed on as its number.

    matrix : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.

    color : Optional[QColor]
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own. May be left out, as in Qt: a new 'QColor()' is then passed on.
    """
    #  QImageTextureGlyphCache::QImageTextureGlyphCache(QFontEngine::
    #      GlyphFormat format, const QTransform &matrix, const QColor &color)
    if color is None:
      from . import QColor
      color = QColor()
    self._noteCreation(QImageTextureGlyphCache, lambda: Rituals.call(
        'ritual_ZN23QImageTextureGlyphCacheC1EN11QFontEngine11GlyphFormatER'
        'K10QTransformRK6QColor',
        format.value, self._valueOf(matrix), self._valueOf(color),
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

  @overload(int, int)
  def createTextureData(self, width: int, height: int) -> None:
    """
    Calls Qt's 'void QImageTextureGlyphCache::createTextureData(int width,
    int height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qimagetextureglyphcache.html#createTextureData

    Parameters
    ----------

    width : int
      Passed on as it is.

    height : int
      Passed on as it is.
    """
    #  void QImageTextureGlyphCache::createTextureData(int width, int height)
    ritual = 'ritual_ZN23QImageTextureGlyphCache17createTextureDataEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QImageTextureGlyphCache17createTextureDataEii'
    self.uglySide.call(ritual, width, height)

  @overload(int, int)
  def resizeTextureData(self, width: int, height: int) -> None:
    """
    Calls Qt's 'void QImageTextureGlyphCache::resizeTextureData(int width,
    int height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qimagetextureglyphcache.html#resizeTextureData

    Parameters
    ----------

    width : int
      Passed on as it is.

    height : int
      Passed on as it is.
    """
    #  void QImageTextureGlyphCache::resizeTextureData(int width, int height)
    ritual = 'ritual_ZN23QImageTextureGlyphCache17resizeTextureDataEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QImageTextureGlyphCache17resizeTextureDataEii'
    self.uglySide.call(ritual, width, height)

  @overload(QTextureGlyphCache.Coord, int, QFixedPoint)
  def fillTexture(
      self,
      c: QTextureGlyphCache.Coord,
      glyph: int,
      subPixelPosition: QFixedPoint,
  ) -> None:
    """
    Calls Qt's 'void QImageTextureGlyphCache::fillTexture(const Coord &c,
    glyph_t glyph, const QFixedPoint &subPixelPosition)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qimagetextureglyphcache.html#fillTexture

    Parameters
    ----------

    c : QTextureGlyphCache.Coord
      Passed on as a value: Qt reads the C++ QTextureGlyphCache::Coord, which
      stays Python's own.

    glyph : int
      Passed on as it is.

    subPixelPosition : QFixedPoint
      Passed on as a value: Qt reads the C++ QFixedPoint, which stays
      Python's own.
    """
    #  void QImageTextureGlyphCache::fillTexture(const Coord &c, glyph_t
    #      glyph, const QFixedPoint &subPixelPosition)
    ritual = (
        'ritual_ZN23QImageTextureGlyphCache11fillTextureERKN18QTextureGlyph'
        'Cache5CoordEjRK11QFixedPoint')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QImageTextureGlyphCache11fillTextureERKN18QTextur'
          'eGlyphCache5CoordEjRK11QFixedPoint')
    self.uglySide.call(
        ritual, self._valueOf(c), glyph, self._valueOf(subPixelPosition),
    )
