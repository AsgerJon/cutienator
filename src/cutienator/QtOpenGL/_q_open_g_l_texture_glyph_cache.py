"""
QOpenGLTextureGlyphCache binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpenGL/6.12.0/QtOpenGL/private/qopengltextureglyphcache_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QOpenGLTextureGlyphCache to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..occult import Rituals
from ..QtGui import QFontEngine, QImageTextureGlyphCache, QTextureGlyphCache

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtGui import QColor, QFixedPoint, QOpenGLContextGroup, QTransform
  from . import QOpenGL2PaintEngineExPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QFixedPoint = WAIT['QFixedPoint']
  QOpenGL2PaintEngineExPrivate = WAIT['QOpenGL2PaintEngineExPrivate']
  QTransform = WAIT['QTransform']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QOpenGLTextureGlyphCache(QImageTextureGlyphCache):
  """
  The cute side of Qt's QOpenGLTextureGlyphCache: a plain Python object
  standing in front of one C++ QOpenGLTextureGlyphCache.

  It is built on the cute 'QImageTextureGlyphCache', as Qt's
  QOpenGLTextureGlyphCache is built on Qt's QImageTextureGlyphCache, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QOpenGLTextureGlyphCache that has a ritual and that
  Python can call so far, 17 names in all: 'createTextureData',
  'resizeTextureData', 'fillTexture', 'glyphPadding', 'maxTextureWidth',
  'maxTextureHeight', 'texture', 'width', 'height', 'setPaintEnginePrivate',
  'contextGroup', 'serialNumber', 'filterMode', 'setFilterMode', 'clear',
  'paintEnginePrivate', 'setupVertexAttribs'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpenGLTextureGlyphCache::~QOpenGLTextureGlyphCache()': the
    destructor: Python never removes a C++ QOpenGLTextureGlyphCache.

  What to expect
  --------------

  - The C++ QOpenGLTextureGlyphCache is created at the first use, not by
    'QOpenGLTextureGlyphCache(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QOpenGLTextureGlyphCache.
  """

  #  The enums Qt writes inside QOpenGLTextureGlyphCache, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class FilterMode(CuteNum):
    """
    The enum 'QOpenGLTextureGlyphCache::FilterMode' of Qt, with the 2 names
    Qt gives in it.
    """

    Nearest = Kee[int](0)
    Linear = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpenGLTextureGlyphCache'

  #  A C++ QOpenGLTextureGlyphCache Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QOpenGLTextureGlyphCache'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def glyphPadding(self) -> int:
    """
    Calls Qt's 'int QOpenGLTextureGlyphCache::glyphPadding() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltextureglyphcache.html#glyphPadding
    """
    #  int QOpenGLTextureGlyphCache::glyphPadding() const
    ritual = 'ritual_ZNK24QOpenGLTextureGlyphCache12glyphPaddingEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK24QOpenGLTextureGlyphCache12glyphPaddingEv'
    return self.uglySide.call(ritual)

  def maxTextureWidth(self) -> int:
    """
    Calls Qt's 'int QOpenGLTextureGlyphCache::maxTextureWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltextureglyphcache.html#maxTextureWidth
    """
    #  int QOpenGLTextureGlyphCache::maxTextureWidth() const
    ritual = 'ritual_ZNK24QOpenGLTextureGlyphCache15maxTextureWidthEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK24QOpenGLTextureGlyphCache15maxTextureWidthEv'
    return self.uglySide.call(ritual)

  def maxTextureHeight(self) -> int:
    """
    Calls Qt's 'int QOpenGLTextureGlyphCache::maxTextureHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltextureglyphcache.html#maxTextureHeight
    """
    #  int QOpenGLTextureGlyphCache::maxTextureHeight() const
    ritual = 'ritual_ZNK24QOpenGLTextureGlyphCache16maxTextureHeightEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK24QOpenGLTextureGlyphCache16maxTextureHeightEv'
    return self.uglySide.call(ritual)

  def texture(self) -> int:
    """
    Calls Qt's 'GLuint QOpenGLTextureGlyphCache::texture() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltextureglyphcache.html#texture
    """
    #  GLuint QOpenGLTextureGlyphCache::texture() const
    return self.uglySide.call(
        'ritual_ZNK24QOpenGLTextureGlyphCache7textureEv',
    )

  def width(self) -> int:
    """
    Calls Qt's 'int QOpenGLTextureGlyphCache::width() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltextureglyphcache.html#width
    """
    #  int QOpenGLTextureGlyphCache::width() const
    return self.uglySide.call('ritual_ZNK24QOpenGLTextureGlyphCache5widthEv')

  def height(self) -> int:
    """
    Calls Qt's 'int QOpenGLTextureGlyphCache::height() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltextureglyphcache.html#height
    """
    #  int QOpenGLTextureGlyphCache::height() const
    return self.uglySide.call(
        'ritual_ZNK24QOpenGLTextureGlyphCache6heightEv',
    )

  def contextGroup(self) -> Optional[QOpenGLContextGroup]:
    """
    Calls Qt's 'const QOpenGLContextGroup
    *QOpenGLTextureGlyphCache::contextGroup() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltextureglyphcache.html#contextGroup

    Returns
    -------

    Optional[QOpenGLContextGroup]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QOpenGLContextGroup *QOpenGLTextureGlyphCache::contextGroup()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK24QOpenGLTextureGlyphCache12contextGroupEv',
    )
    from ..QtGui import QOpenGLContextGroup
    return QOpenGLContextGroup._cuteAt(address)

  def serialNumber(self) -> int:
    """
    Calls Qt's 'int QOpenGLTextureGlyphCache::serialNumber() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltextureglyphcache.html#serialNumber
    """
    #  int QOpenGLTextureGlyphCache::serialNumber() const
    return self.uglySide.call(
        'ritual_ZNK24QOpenGLTextureGlyphCache12serialNumberEv',
    )

  def filterMode(self) -> FilterMode:
    """
    Calls Qt's 'FilterMode QOpenGLTextureGlyphCache::filterMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltextureglyphcache.html#filterMode

    Returns
    -------

    FilterMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'FilterMode(number)'
      gives.
    """
    #  FilterMode QOpenGLTextureGlyphCache::filterMode() const
    return QOpenGLTextureGlyphCache.FilterMode(self.uglySide.call(
        'ritual_ZNK24QOpenGLTextureGlyphCache10filterModeEv',
    ))

  def paintEnginePrivate(self) -> Optional[QOpenGL2PaintEngineExPrivate]:
    """
    Calls Qt's 'QOpenGL2PaintEngineExPrivate
    *QOpenGLTextureGlyphCache::paintEnginePrivate() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltextureglyphcache.html#paintEnginePrivate

    Returns
    -------

    Optional[QOpenGL2PaintEngineExPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOpenGL2PaintEngineExPrivate
    #      *QOpenGLTextureGlyphCache::paintEnginePrivate() const
    address = self.uglySide.call(
        'ritual_ZNK24QOpenGLTextureGlyphCache18paintEnginePrivateEv',
    )
    from . import QOpenGL2PaintEngineExPrivate
    return QOpenGL2PaintEngineExPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QOpenGL2PaintEngineExPrivate)
  @overload(NoneType)
  def setPaintEnginePrivate(
      self,
      p: Optional[QOpenGL2PaintEngineExPrivate],
  ) -> None:
    """
    Calls Qt's 'void QOpenGLTextureGlyphCache::setPaintEnginePrivate(
    QOpenGL2PaintEngineExPrivate *p)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltextureglyphcache.html

    Parameters
    ----------

    p : Optional[QOpenGL2PaintEngineExPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QOpenGLTextureGlyphCache::setPaintEnginePrivate(
    #      QOpenGL2PaintEngineExPrivate *p)
    self.uglySide.call(
        'ritual_ZN24QOpenGLTextureGlyphCache21setPaintEnginePrivateEP28QOpe'
        'nGL2PaintEngineExPrivate',
        self._addressOf(p),
    )

  @overload(FilterMode)
  def setFilterMode(self, m: FilterMode) -> None:
    """
    Calls Qt's 'void QOpenGLTextureGlyphCache::setFilterMode(FilterMode m)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltextureglyphcache.html#setFilterMode

    Parameters
    ----------

    m : FilterMode
      Passed on as its number.
    """
    #  void QOpenGLTextureGlyphCache::setFilterMode(FilterMode m)
    self.uglySide.call(
        'ritual_ZN24QOpenGLTextureGlyphCache13setFilterModeENS_10FilterMode'
        'E',
        m.value,
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

  @overload(QFontEngine.GlyphFormat, QTransform)
  @overload(QFontEngine.GlyphFormat, QTransform, QColor)
  def __init__(
      self,
      glyphFormat: QFontEngine.GlyphFormat,
      matrix: QTransform,
      color: Optional[QColor] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QOpenGLTextureGlyphCache::QOpenGLTextureGlyphCache(QFontEngine::
    GlyphFormat glyphFormat, const QTransform &matrix, const QColor &color)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltextureglyphcache.html

    Parameters
    ----------

    glyphFormat : QFontEngine.GlyphFormat
      Passed on as its number.

    matrix : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.

    color : Optional[QColor]
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own. May be left out, as in Qt: a new 'QColor()' is then passed on.
    """
    #  QOpenGLTextureGlyphCache::QOpenGLTextureGlyphCache(QFontEngine::
    #      GlyphFormat glyphFormat, const QTransform &matrix, const QColor
    #      &color)
    if color is None:
      from ..QtGui import QColor
      color = QColor()
    self._noteCreation(QOpenGLTextureGlyphCache, lambda: Rituals.call(
        'ritual_ZN24QOpenGLTextureGlyphCacheC1EN11QFontEngine11GlyphFormatE'
        'RK10QTransformRK6QColor',
        glyphFormat.value, self._valueOf(matrix), self._valueOf(color),
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
    Calls Qt's 'void QOpenGLTextureGlyphCache::createTextureData(int width,
    int height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltextureglyphcache.html#createTextureData

    Parameters
    ----------

    width : int
      Passed on as it is.

    height : int
      Passed on as it is.
    """
    #  void QOpenGLTextureGlyphCache::createTextureData(int width, int
    #      height)
    ritual = 'ritual_ZN24QOpenGLTextureGlyphCache17createTextureDataEii'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QOpenGLTextureGlyphCache17createTextureDataEii')
    self.uglySide.call(ritual, width, height)

  @overload(int, int)
  def resizeTextureData(self, width: int, height: int) -> None:
    """
    Calls Qt's 'void QOpenGLTextureGlyphCache::resizeTextureData(int width,
    int height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltextureglyphcache.html#resizeTextureData

    Parameters
    ----------

    width : int
      Passed on as it is.

    height : int
      Passed on as it is.
    """
    #  void QOpenGLTextureGlyphCache::resizeTextureData(int width, int
    #      height)
    ritual = 'ritual_ZN24QOpenGLTextureGlyphCache17resizeTextureDataEii'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QOpenGLTextureGlyphCache17resizeTextureDataEii')
    self.uglySide.call(ritual, width, height)

  @overload(QTextureGlyphCache.Coord, int, QFixedPoint)
  def fillTexture(
      self,
      c: QTextureGlyphCache.Coord,
      glyph: int,
      subPixelPosition: QFixedPoint,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLTextureGlyphCache::fillTexture(const Coord &c,
    glyph_t glyph, const QFixedPoint &subPixelPosition)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltextureglyphcache.html#fillTexture

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
    #  void QOpenGLTextureGlyphCache::fillTexture(const Coord &c, glyph_t
    #      glyph, const QFixedPoint &subPixelPosition)
    ritual = (
        'ritual_ZN24QOpenGLTextureGlyphCache11fillTextureERKN18QTextureGlyp'
        'hCache5CoordEjRK11QFixedPoint')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QOpenGLTextureGlyphCache11fillTextureERKN18QTextu'
          'reGlyphCache5CoordEjRK11QFixedPoint')
    self.uglySide.call(
        ritual, self._valueOf(c), glyph, self._valueOf(subPixelPosition),
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QOpenGLTextureGlyphCache::clear()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltextureglyphcache.html#clear
    """
    #  void QOpenGLTextureGlyphCache::clear()
    self.uglySide.call('ritual_ZN24QOpenGLTextureGlyphCache5clearEv')

  def setupVertexAttribs(self) -> None:
    """
    Calls Qt's 'void QOpenGLTextureGlyphCache::setupVertexAttribs()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltextureglyphcache.html#setupVertexAttribs
    """
    #  void QOpenGLTextureGlyphCache::setupVertexAttribs()
    self.uglySide.call(
        'ritual_ZN24QOpenGLTextureGlyphCache18setupVertexAttribsEv',
    )
