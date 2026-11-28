"""
QSGRhiTextureGlyphCache binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgrhitextureglyphcache_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QSGRhiTextureGlyphCache to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtGui import QFontEngine, QImageTextureGlyphCache, QRhiTexture
from ..QtGui import QTextureGlyphCache

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtGui import QColor, QFixedPoint, QImage, QRhiResourceUpdateBatch
  from ..QtGui import QTransform
  from . import QSGDefaultRenderContext
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QFixedPoint = WAIT['QFixedPoint']
  QImage = WAIT['QImage']
  QRhiResourceUpdateBatch = WAIT['QRhiResourceUpdateBatch']
  QSGDefaultRenderContext = WAIT['QSGDefaultRenderContext']
  QTransform = WAIT['QTransform']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGRhiTextureGlyphCache(QImageTextureGlyphCache):
  """
  The cute side of Qt's QSGRhiTextureGlyphCache: a plain Python object
  standing in front of one C++ QSGRhiTextureGlyphCache.

  It is built on the cute 'QImageTextureGlyphCache', as Qt's
  QSGRhiTextureGlyphCache is built on Qt's QImageTextureGlyphCache, and has
  everything that class has.

  C++ hands a QSGRhiTextureGlyphCache around as a copy, so every C++
  QSGRhiTextureGlyphCache behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSGRhiTextureGlyphCache that has a ritual and that
  Python can call so far, 15 names in all: 'createTextureData',
  'resizeTextureData', 'beginFillTexture', 'fillTexture', 'endFillTexture',
  'glyphPadding', 'maxTextureWidth', 'maxTextureHeight', 'texture',
  'commitResourceUpdates', 'width', 'height',
  'eightBitFormatIsAlphaSwizzled', 'prepareGlyphImage', 'createEmptyTexture'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSGRhiTextureGlyphCache::~QSGRhiTextureGlyphCache()': the
    destructor: Python removes its C++ QSGRhiTextureGlyphCache by it, and has
    no other use for it.

  What to expect
  --------------

  - The C++ QSGRhiTextureGlyphCache is created at the first use, not by
    'QSGRhiTextureGlyphCache(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSGRhiTextureGlyphCache back gives a copy the ritual
    made for Python, in a new cute QSGRhiTextureGlyphCache.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGRhiTextureGlyphCache'

  #  A C++ QSGRhiTextureGlyphCache Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGRhiTextureGlyphCache'

  #  Qt's '~QSGRhiTextureGlyphCache()'. Naming it makes this a value class:
  #  Python owns every C++ QSGRhiTextureGlyphCache behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN23QSGRhiTextureGlyphCacheD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def glyphPadding(self) -> int:
    """
    Calls Qt's 'int QSGRhiTextureGlyphCache::glyphPadding() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhitextureglyphcache.html#glyphPadding
    """
    #  int QSGRhiTextureGlyphCache::glyphPadding() const
    ritual = 'ritual_ZNK23QSGRhiTextureGlyphCache12glyphPaddingEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK23QSGRhiTextureGlyphCache12glyphPaddingEv'
    return self.uglySide.call(ritual)

  def maxTextureWidth(self) -> int:
    """
    Calls Qt's 'int QSGRhiTextureGlyphCache::maxTextureWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhitextureglyphcache.html#maxTextureWidth
    """
    #  int QSGRhiTextureGlyphCache::maxTextureWidth() const
    ritual = 'ritual_ZNK23QSGRhiTextureGlyphCache15maxTextureWidthEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK23QSGRhiTextureGlyphCache15maxTextureWidthEv'
    return self.uglySide.call(ritual)

  def maxTextureHeight(self) -> int:
    """
    Calls Qt's 'int QSGRhiTextureGlyphCache::maxTextureHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhitextureglyphcache.html#maxTextureHeight
    """
    #  int QSGRhiTextureGlyphCache::maxTextureHeight() const
    ritual = 'ritual_ZNK23QSGRhiTextureGlyphCache16maxTextureHeightEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK23QSGRhiTextureGlyphCache16maxTextureHeightEv'
    return self.uglySide.call(ritual)

  def texture(self) -> Optional[QRhiTexture]:
    """
    Calls Qt's 'QRhiTexture *QSGRhiTextureGlyphCache::texture() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhitextureglyphcache.html#texture

    Returns
    -------

    Optional[QRhiTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiTexture *QSGRhiTextureGlyphCache::texture() const
    address = self.uglySide.call(
        'ritual_ZNK23QSGRhiTextureGlyphCache7textureEv',
    )
    return QRhiTexture._cuteAt(address)

  def width(self) -> int:
    """
    Calls Qt's 'int QSGRhiTextureGlyphCache::width() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrhitextureglyphcache.html#width
    """
    #  int QSGRhiTextureGlyphCache::width() const
    return self.uglySide.call('ritual_ZNK23QSGRhiTextureGlyphCache5widthEv')

  def height(self) -> int:
    """
    Calls Qt's 'int QSGRhiTextureGlyphCache::height() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhitextureglyphcache.html#height
    """
    #  int QSGRhiTextureGlyphCache::height() const
    return self.uglySide.call('ritual_ZNK23QSGRhiTextureGlyphCache6heightEv')

  def eightBitFormatIsAlphaSwizzled(self) -> bool:
    """
    Calls Qt's 'bool QSGRhiTextureGlyphCache::eightBitFormatIsAlphaSwizzled()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhitextureglyphcache.html
    """
    #  bool QSGRhiTextureGlyphCache::eightBitFormatIsAlphaSwizzled() const
    return self.uglySide.call(
        'ritual_ZNK23QSGRhiTextureGlyphCache29eightBitFormatIsAlphaSwizzled'
        'Ev',
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

  @overload(QSGDefaultRenderContext, QFontEngine.GlyphFormat, QTransform)
  @overload(NoneType, QFontEngine.GlyphFormat, QTransform)
  @overload(
      QSGDefaultRenderContext, QFontEngine.GlyphFormat, QTransform, QColor,
  )
  @overload(NoneType, QFontEngine.GlyphFormat, QTransform, QColor)
  def __init__(
      self,
      rc: Optional[QSGDefaultRenderContext],
      format: QFontEngine.GlyphFormat,
      matrix: QTransform,
      color: Optional[QColor] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QSGRhiTextureGlyphCache::QSGRhiTextureGlyphCache(QSGDefaultRenderContext
    *rc, QFontEngine::GlyphFormat format, const QTransform &matrix, const
    QColor &color)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhitextureglyphcache.html

    Parameters
    ----------

    rc : Optional[QSGDefaultRenderContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    format : QFontEngine.GlyphFormat
      Passed on as its number.

    matrix : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.

    color : Optional[QColor]
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own. May be left out, as in Qt: a new 'QColor()' is then passed on.
    """
    #  QSGRhiTextureGlyphCache::QSGRhiTextureGlyphCache(
    #      QSGDefaultRenderContext *rc, QFontEngine::GlyphFormat format,
    #      const QTransform &matrix, const QColor &color)
    if color is None:
      from ..QtGui import QColor
      color = QColor()
    self._noteCreation(QSGRhiTextureGlyphCache, lambda: Rituals.call(
        'ritual_ZN23QSGRhiTextureGlyphCacheC1EP23QSGDefaultRenderContextN11'
        'QFontEngine11GlyphFormatERK10QTransformRK6QColor',
        self._addressOf(rc), format.value, self._valueOf(matrix),
        self._valueOf(color),
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
    Calls Qt's 'void QSGRhiTextureGlyphCache::createTextureData(int width,
    int height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhitextureglyphcache.html#createTextureData

    Parameters
    ----------

    width : int
      Passed on as it is.

    height : int
      Passed on as it is.
    """
    #  void QSGRhiTextureGlyphCache::createTextureData(int width, int height)
    ritual = 'ritual_ZN23QSGRhiTextureGlyphCache17createTextureDataEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QSGRhiTextureGlyphCache17createTextureDataEii'
    self.uglySide.call(ritual, width, height)

  @overload(int, int)
  def resizeTextureData(self, width: int, height: int) -> None:
    """
    Calls Qt's 'void QSGRhiTextureGlyphCache::resizeTextureData(int width,
    int height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhitextureglyphcache.html#resizeTextureData

    Parameters
    ----------

    width : int
      Passed on as it is.

    height : int
      Passed on as it is.
    """
    #  void QSGRhiTextureGlyphCache::resizeTextureData(int width, int height)
    ritual = 'ritual_ZN23QSGRhiTextureGlyphCache17resizeTextureDataEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QSGRhiTextureGlyphCache17resizeTextureDataEii'
    self.uglySide.call(ritual, width, height)

  def beginFillTexture(self) -> None:
    """
    Calls Qt's 'void QSGRhiTextureGlyphCache::beginFillTexture()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhitextureglyphcache.html#beginFillTexture
    """
    #  void QSGRhiTextureGlyphCache::beginFillTexture()
    ritual = 'ritual_ZN23QSGRhiTextureGlyphCache16beginFillTextureEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QSGRhiTextureGlyphCache16beginFillTextureEv'
    self.uglySide.call(ritual)

  @overload(QTextureGlyphCache.Coord, int, QFixedPoint)
  def fillTexture(
      self,
      c: QTextureGlyphCache.Coord,
      glyph: int,
      subPixelPosition: QFixedPoint,
  ) -> None:
    """
    Calls Qt's 'void QSGRhiTextureGlyphCache::fillTexture(const Coord &c,
    glyph_t glyph, const QFixedPoint &subPixelPosition)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhitextureglyphcache.html#fillTexture

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
    #  void QSGRhiTextureGlyphCache::fillTexture(const Coord &c, glyph_t
    #      glyph, const QFixedPoint &subPixelPosition)
    ritual = (
        'ritual_ZN23QSGRhiTextureGlyphCache11fillTextureERKN18QTextureGlyph'
        'Cache5CoordEjRK11QFixedPoint')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QSGRhiTextureGlyphCache11fillTextureERKN18QTextur'
          'eGlyphCache5CoordEjRK11QFixedPoint')
    self.uglySide.call(
        ritual, self._valueOf(c), glyph, self._valueOf(subPixelPosition),
    )

  def endFillTexture(self) -> None:
    """
    Calls Qt's 'void QSGRhiTextureGlyphCache::endFillTexture()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhitextureglyphcache.html#endFillTexture
    """
    #  void QSGRhiTextureGlyphCache::endFillTexture()
    ritual = 'ritual_ZN23QSGRhiTextureGlyphCache14endFillTextureEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QSGRhiTextureGlyphCache14endFillTextureEv'
    self.uglySide.call(ritual)

  @overload(QRhiResourceUpdateBatch)
  @overload(NoneType)
  def commitResourceUpdates(
      self,
      mergeInto: Optional[QRhiResourceUpdateBatch],
  ) -> None:
    """
    Calls Qt's 'void
    QSGRhiTextureGlyphCache::commitResourceUpdates(QRhiResourceUpdateBatch
    *mergeInto)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhitextureglyphcache.html#commitResourceUpdates

    Parameters
    ----------

    mergeInto : Optional[QRhiResourceUpdateBatch]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGRhiTextureGlyphCache::commitResourceUpdates(
    #      QRhiResourceUpdateBatch *mergeInto)
    self.uglySide.call(
        'ritual_ZN23QSGRhiTextureGlyphCache21commitResourceUpdatesEP23QRhiR'
        'esourceUpdateBatch',
        self._addressOf(mergeInto),
    )

  @overload(QImage)
  @overload(NoneType)
  def prepareGlyphImage(self, img: Optional[QImage]) -> None:
    """
    Calls Qt's 'void QSGRhiTextureGlyphCache::prepareGlyphImage(QImage
    *img)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhitextureglyphcache.html#prepareGlyphImage

    Parameters
    ----------

    img : Optional[QImage]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGRhiTextureGlyphCache::prepareGlyphImage(QImage *img)
    self.uglySide.call(
        'ritual_ZN23QSGRhiTextureGlyphCache17prepareGlyphImageEP6QImage',
        self._addressOf(img),
    )

  @overload(QRhiTexture.Format)
  def createEmptyTexture(
      self,
      format: QRhiTexture.Format,
  ) -> Optional[QRhiTexture]:
    """
    Calls Qt's 'QRhiTexture
    *QSGRhiTextureGlyphCache::createEmptyTexture(QRhiTexture::Format
    format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhitextureglyphcache.html#createEmptyTexture

    Parameters
    ----------

    format : QRhiTexture.Format
      Passed on as its number.

    Returns
    -------

    Optional[QRhiTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiTexture
    #      *QSGRhiTextureGlyphCache::createEmptyTexture(QRhiTexture::Format
    #      format)
    address = self.uglySide.call(
        'ritual_ZN23QSGRhiTextureGlyphCache18createEmptyTextureEN11QRhiText'
        'ure6FormatE',
        format.value,
    )
    return QRhiTexture._cuteAt(address)
