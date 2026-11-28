"""
QCRhiColorGlyphCache binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcrhicolorglyphcache_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QCRhiColorGlyphCache to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QRect, QSize
  from ..QtGui import QRhi, QRhiResourceUpdateBatch, QRhiTexture
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRhi = WAIT['QRhi']
  QRhiResourceUpdateBatch = WAIT['QRhiResourceUpdateBatch']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCRhiColorGlyphCache(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCRhiColorGlyphCache: a plain Python object standing
  in front of one C++ QCRhiColorGlyphCache.

  C++ hands a QCRhiColorGlyphCache around as a copy, so every C++
  QCRhiColorGlyphCache behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QCRhiColorGlyphCache that has a ritual and that
  Python can call so far, 8 names in all: 'commitResourceUpdate',
  'optimizeAfterRendering', 'texture', 'isEmpty', 'ensureAtlas', 'growAtlas',
  'useTextureResizeWorkaround', 'evictUntilAllocated'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCRhiColorGlyphCache::~QCRhiColorGlyphCache()': the destructor:
    Python removes its C++ QCRhiColorGlyphCache by it, and has no other use
    for it.
  - Qt's 'void QCRhiColorGlyphCache::addGlyphRun(QPointF glyphPos, const
    QGlyphRun &run, QColor color, const QTransform &transform, float
    devicePixelRatio, QCRhiDistanceFieldGlyphCache::VertexList *verts,
    QCRhiDistanceFieldGlyphCache::IndexList *indices)': names
    'QCRhiDistanceFieldGlyphCache::VertexList', which has no cute class yet.
  - Qt's 'void QCRhiColorGlyphCache::referenceGlyph(const GlyphKey &key,
    GlyphData &gd)': takes a type Python has no way to hand over yet.
  - Qt's 'void QCRhiColorGlyphCache::releaseGlyphs(const QSet<GlyphKey>
    &glyphs)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  1 of the 14 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QCRhiColorGlyphCache is created at the first use, not by
    'QCRhiColorGlyphCache(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCRhiColorGlyphCache back gives a copy the ritual
    made for Python, in a new cute QCRhiColorGlyphCache.
  - Each name of Qt's QCRhiColorGlyphCache that has no cute function yet,
    'addGlyphRun', 'ensureGlyph', 'referenceGlyph', 'releaseGlyphs', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCRhiColorGlyphCache'

  #  Qt's '~QCRhiColorGlyphCache()'. Naming it makes this a value class:
  #  Python owns every C++ QCRhiColorGlyphCache behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QCRhiColorGlyphCacheD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def texture(self) -> Optional[QRhiTexture]:
    """
    Calls Qt's 'QRhiTexture *QCRhiColorGlyphCache::texture() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcrhicolorglyphcache.html#texture

    Returns
    -------

    Optional[QRhiTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiTexture *QCRhiColorGlyphCache::texture() const
    address = self.uglySide.call(
        'ritual_ZNK20QCRhiColorGlyphCache7textureEv',
    )
    from ..QtGui import QRhiTexture
    return QRhiTexture._cuteAt(address)

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QCRhiColorGlyphCache::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcrhicolorglyphcache.html#isEmpty
    """
    #  bool QCRhiColorGlyphCache::isEmpty() const
    return self.uglySide.call('ritual_ZNK20QCRhiColorGlyphCache7isEmptyEv')

  def useTextureResizeWorkaround(self) -> bool:
    """
    Calls Qt's 'bool QCRhiColorGlyphCache::useTextureResizeWorkaround()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcrhicolorglyphcache.html
    """
    #  bool QCRhiColorGlyphCache::useTextureResizeWorkaround() const
    return self.uglySide.call(
        'ritual_ZNK20QCRhiColorGlyphCache26useTextureResizeWorkaroundEv',
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

  @overload(QRhi)
  @overload(NoneType)
  def __init__(self, rhi: Optional[QRhi]) -> None:
    """
    Notes what was given, for Qt's
    'QCRhiColorGlyphCache::QCRhiColorGlyphCache(QRhi *rhi)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcrhicolorglyphcache.html#QCRhiColorGlyphCache

    Parameters
    ----------

    rhi : Optional[QRhi]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QCRhiColorGlyphCache::QCRhiColorGlyphCache(QRhi *rhi)
    self._noteCreation(QCRhiColorGlyphCache, lambda: Rituals.call(
        'ritual_ZN20QCRhiColorGlyphCacheC1EP4QRhi', self._addressOf(rhi),
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

  @overload(QRhiResourceUpdateBatch)
  @overload(NoneType)
  def commitResourceUpdate(
      self,
      batch: Optional[QRhiResourceUpdateBatch],
  ) -> None:
    """
    Calls Qt's 'void
    QCRhiColorGlyphCache::commitResourceUpdate(QRhiResourceUpdateBatch
    *batch)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcrhicolorglyphcache.html#commitResourceUpdate

    Parameters
    ----------

    batch : Optional[QRhiResourceUpdateBatch]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void
    #      QCRhiColorGlyphCache::commitResourceUpdate(QRhiResourceUpdateBatch
    #      *batch)
    self.uglySide.call(
        'ritual_ZN20QCRhiColorGlyphCache20commitResourceUpdateEP23QRhiResou'
        'rceUpdateBatch',
        self._addressOf(batch),
    )

  def optimizeAfterRendering(self) -> None:
    """
    Calls Qt's 'void QCRhiColorGlyphCache::optimizeAfterRendering()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcrhicolorglyphcache.html#optimizeAfterRendering
    """
    #  void QCRhiColorGlyphCache::optimizeAfterRendering()
    self.uglySide.call(
        'ritual_ZN20QCRhiColorGlyphCache22optimizeAfterRenderingEv',
    )

  def ensureAtlas(self) -> None:
    """
    Calls Qt's 'void QCRhiColorGlyphCache::ensureAtlas()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcrhicolorglyphcache.html#ensureAtlas
    """
    #  void QCRhiColorGlyphCache::ensureAtlas()
    self.uglySide.call('ritual_ZN20QCRhiColorGlyphCache11ensureAtlasEv')

  @overload(int)
  def growAtlas(self, requiredSize: int) -> None:
    """
    Calls Qt's 'void QCRhiColorGlyphCache::growAtlas(int requiredSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcrhicolorglyphcache.html#growAtlas

    Parameters
    ----------

    requiredSize : int
      Passed on as it is.
    """
    #  void QCRhiColorGlyphCache::growAtlas(int requiredSize)
    self.uglySide.call(
        'ritual_ZN20QCRhiColorGlyphCache9growAtlasEi', requiredSize,
    )

  @overload(QSize)
  def evictUntilAllocated(self, allocSize: QSize) -> QRect:
    """
    Calls Qt's 'QRect QCRhiColorGlyphCache::evictUntilAllocated(const QSize
    &allocSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcrhicolorglyphcache.html#evictUntilAllocated

    Parameters
    ----------

    allocSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QCRhiColorGlyphCache::evictUntilAllocated(const QSize
    #      &allocSize)
    address = self.uglySide.call(
        'ritual_ZN20QCRhiColorGlyphCache19evictUntilAllocatedERK5QSize',
        self._valueOf(allocSize),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @staticmethod
  def addGlyphRun(*__, **_) -> Never:
    """
    Qt's 'void QCRhiColorGlyphCache::addGlyphRun(QPointF glyphPos, const
    QGlyphRun &run, QColor color, const QTransform &transform, float
    devicePixelRatio, QCRhiDistanceFieldGlyphCache::VertexList *verts,
    QCRhiDistanceFieldGlyphCache::IndexList *indices)': names
    'QCRhiDistanceFieldGlyphCache::VertexList', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QCRhiColorGlyphCache.addGlyphRun' has no cute function yet. Qt's "
        "'void QCRhiColorGlyphCache::addGlyphRun(QPointF glyphPos, const "
        "QGlyphRun &run, QColor color, const QTransform &transform, float "
        "devicePixelRatio, QCRhiDistanceFieldGlyphCache::VertexList *verts, "
        "QCRhiDistanceFieldGlyphCache::IndexList *indices)': names "
        "'QCRhiDistanceFieldGlyphCache::VertexList', which has no cute "
        "class yet.")

  @staticmethod
  def ensureGlyph(*__, **_) -> Never:
    """
    Qt's 'const GlyphData &QCRhiColorGlyphCache::ensureGlyph(const GlyphKey
    &key, QFontEngine *fe, QColor color, const QTransform &rasterTransform)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier
    'QC_COLOR_GLYPH_PADDING'.
    """
    raise NotImplementedError(
        "'QCRhiColorGlyphCache.ensureGlyph' has no cute function yet. Qt's "
        "'const GlyphData &QCRhiColorGlyphCache::ensureGlyph(const GlyphKey "
        "&key, QFontEngine *fe, QColor color, const QTransform "
        "&rasterTransform)': Qt's library has no name for it, and its code "
        "in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'QC_COLOR_GLYPH_PADDING'.")

  @staticmethod
  def referenceGlyph(*__, **_) -> Never:
    """
    Qt's 'void QCRhiColorGlyphCache::referenceGlyph(const GlyphKey &key,
    GlyphData &gd)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QCRhiColorGlyphCache.referenceGlyph' has no cute function yet. "
        "Qt's 'void QCRhiColorGlyphCache::referenceGlyph(const GlyphKey "
        "&key, GlyphData &gd)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def releaseGlyphs(*__, **_) -> Never:
    """
    Qt's 'void QCRhiColorGlyphCache::releaseGlyphs(const QSet<GlyphKey>
    &glyphs)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QCRhiColorGlyphCache.releaseGlyphs' has no cute function yet. "
        "Qt's 'void QCRhiColorGlyphCache::releaseGlyphs(const "
        "QSet<GlyphKey> &glyphs)': takes a type Python has no way to hand "
        "over yet.")
