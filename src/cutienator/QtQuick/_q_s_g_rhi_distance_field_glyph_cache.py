"""
QSGRhiDistanceFieldGlyphCache binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgrhidistancefieldglyphcache_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QSGRhiDistanceFieldGlyphCache to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QSGDistanceFieldGlyphCache

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtGui import QDistanceField, QRawFont, QRhiResourceUpdateBatch
  from . import QSGDefaultRenderContext
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDistanceField = WAIT['QDistanceField']
  QRawFont = WAIT['QRawFont']
  QRhiResourceUpdateBatch = WAIT['QRhiResourceUpdateBatch']
  QSGDefaultRenderContext = WAIT['QSGDefaultRenderContext']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGRhiDistanceFieldGlyphCache(QSGDistanceFieldGlyphCache):
  """
  The cute side of Qt's QSGRhiDistanceFieldGlyphCache: a plain Python object
  standing in front of one C++ QSGRhiDistanceFieldGlyphCache.

  It is built on the cute 'QSGDistanceFieldGlyphCache', as Qt's
  QSGRhiDistanceFieldGlyphCache is built on Qt's QSGDistanceFieldGlyphCache,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGRhiDistanceFieldGlyphCache that has a ritual and
  that Python can call so far, 11 names in all: 'storeGlyphs',
  'useTextureResizeWorkaround', 'createFullSizeTextures', 'isActive',
  'maxTextureSize', 'setMaxTextureCount', 'maxTextureCount',
  'commitResourceUpdates', 'eightBitFormatIsAlphaSwizzled',
  'screenSpaceDerivativesSupported', 'loadPregeneratedCache'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSGRhiDistanceFieldGlyphCache::~QSGRhiDistanceFieldGlyphCache()':
    the destructor: Python never removes a C++ QSGRhiDistanceFieldGlyphCache.
  - Qt's 'void QSGRhiDistanceFieldGlyphCache::requestGlyphs(const
    QSet<glyph_t> &glyphs)': takes a type Python has no way to hand over yet.
  - Qt's 'void QSGRhiDistanceFieldGlyphCache::referenceGlyphs(const
    QSet<glyph_t> &glyphs)': takes a type Python has no way to hand over yet.
  - Qt's 'void QSGRhiDistanceFieldGlyphCache::releaseGlyphs(const
    QSet<glyph_t> &glyphs)': takes a type Python has no way to hand over yet.
  - Qt's 'void QSGRhiDistanceFieldGlyphCache::createTexture(TextureInfo
    *texInfo, int width, int height, const void *pixels)': names
    'QSGRhiDistanceFieldGlyphCache::TextureInfo', which has no cute class
    yet.
  - Qt's 'void QSGRhiDistanceFieldGlyphCache::createTexture(TextureInfo
    *texInfo, int width, int height)': names
    'QSGRhiDistanceFieldGlyphCache::TextureInfo', which has no cute class
    yet.
  - Qt's 'void QSGRhiDistanceFieldGlyphCache::resizeTexture(TextureInfo
    *texInfo, int width, int height)': names
    'QSGRhiDistanceFieldGlyphCache::TextureInfo', which has no cute class
    yet.
  - Qt's 'TextureInfo *QSGRhiDistanceFieldGlyphCache::textureInfo(int
    index)': gives 'QSGRhiDistanceFieldGlyphCache::TextureInfo', which has no
    cute class yet.

  What to expect
  --------------

  - The C++ QSGRhiDistanceFieldGlyphCache is created at the first use, not by
    'QSGRhiDistanceFieldGlyphCache(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGRhiDistanceFieldGlyphCache.
  - Each name of Qt's QSGRhiDistanceFieldGlyphCache that has no cute function
    yet, 'createTexture', 'resizeTexture', 'textureInfo', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGRhiDistanceFieldGlyphCache'

  #  A C++ QSGRhiDistanceFieldGlyphCache Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGRhiDistanceFieldGlyphCache'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def useTextureResizeWorkaround(self) -> bool:
    """
    Calls Qt's 'bool
    QSGRhiDistanceFieldGlyphCache::useTextureResizeWorkaround() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhidistancefieldglyphcache.html
    """
    #  bool QSGRhiDistanceFieldGlyphCache::useTextureResizeWorkaround() const
    return self.uglySide.call(
        'ritual_ZNK29QSGRhiDistanceFieldGlyphCache26useTextureResizeWorkaro'
        'undEv',
    )

  def createFullSizeTextures(self) -> bool:
    """
    Calls Qt's 'bool QSGRhiDistanceFieldGlyphCache::createFullSizeTextures()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhidistancefieldglyphcache.html
    """
    #  bool QSGRhiDistanceFieldGlyphCache::createFullSizeTextures() const
    return self.uglySide.call(
        'ritual_ZNK29QSGRhiDistanceFieldGlyphCache22createFullSizeTexturesE'
        'v',
    )

  def isActive(self) -> bool:
    """
    Calls Qt's 'bool QSGRhiDistanceFieldGlyphCache::isActive() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhidistancefieldglyphcache.html#isActive
    """
    #  bool QSGRhiDistanceFieldGlyphCache::isActive() const
    ritual = 'ritual_ZNK29QSGRhiDistanceFieldGlyphCache8isActiveEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK29QSGRhiDistanceFieldGlyphCache8isActiveEv'
    return self.uglySide.call(ritual)

  def maxTextureSize(self) -> int:
    """
    Calls Qt's 'int QSGRhiDistanceFieldGlyphCache::maxTextureSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhidistancefieldglyphcache.html#maxTextureSize
    """
    #  int QSGRhiDistanceFieldGlyphCache::maxTextureSize() const
    return self.uglySide.call(
        'ritual_ZNK29QSGRhiDistanceFieldGlyphCache14maxTextureSizeEv',
    )

  def maxTextureCount(self) -> int:
    """
    Calls Qt's 'int QSGRhiDistanceFieldGlyphCache::maxTextureCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhidistancefieldglyphcache.html#maxTextureCount
    """
    #  int QSGRhiDistanceFieldGlyphCache::maxTextureCount() const
    return self.uglySide.call(
        'ritual_ZNK29QSGRhiDistanceFieldGlyphCache15maxTextureCountEv',
    )

  def eightBitFormatIsAlphaSwizzled(self) -> bool:
    """
    Calls Qt's 'bool
    QSGRhiDistanceFieldGlyphCache::eightBitFormatIsAlphaSwizzled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhidistancefieldglyphcache.html
    """
    #  bool QSGRhiDistanceFieldGlyphCache::eightBitFormatIsAlphaSwizzled()
    #      const
    ritual = (
        'ritual_ZNK29QSGRhiDistanceFieldGlyphCache29eightBitFormatIsAlphaSw'
        'izzledEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK29QSGRhiDistanceFieldGlyphCache29eightBitFormatIsA'
          'lphaSwizzledEv')
    return self.uglySide.call(ritual)

  def screenSpaceDerivativesSupported(self) -> bool:
    """
    Calls Qt's 'bool
    QSGRhiDistanceFieldGlyphCache::screenSpaceDerivativesSupported() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhidistancefieldglyphcache.html
    """
    #  bool QSGRhiDistanceFieldGlyphCache::screenSpaceDerivativesSupported()
    #      const
    ritual = (
        'ritual_ZNK29QSGRhiDistanceFieldGlyphCache31screenSpaceDerivativesS'
        'upportedEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK29QSGRhiDistanceFieldGlyphCache31screenSpaceDeriva'
          'tivesSupportedEv')
    return self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setMaxTextureCount(self, max: int) -> None:
    """
    Calls Qt's 'void QSGRhiDistanceFieldGlyphCache::setMaxTextureCount(int
    max)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhidistancefieldglyphcache.html

    Parameters
    ----------

    max : int
      Passed on as it is.
    """
    #  void QSGRhiDistanceFieldGlyphCache::setMaxTextureCount(int max)
    self.uglySide.call(
        'ritual_ZN29QSGRhiDistanceFieldGlyphCache18setMaxTextureCountEi',
        max,
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

  @overload(QSGDefaultRenderContext, QRawFont, int)
  @overload(NoneType, QRawFont, int)
  def __init__(
      self,
      rc: Optional[QSGDefaultRenderContext],
      font: QRawFont,
      renderTypeQuality: int,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QSGRhiDistanceFieldGlyphCache::QSGRhiDistanceFieldGlyphCache(
    QSGDefaultRenderContext *rc, const QRawFont &font, int
    renderTypeQuality)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhidistancefieldglyphcache.html

    Parameters
    ----------

    rc : Optional[QSGDefaultRenderContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    font : QRawFont
      Passed on as a value: Qt reads the C++ QRawFont, which stays Python's
      own.

    renderTypeQuality : int
      Passed on as it is.
    """
    #  QSGRhiDistanceFieldGlyphCache::QSGRhiDistanceFieldGlyphCache(
    #      QSGDefaultRenderContext *rc, const QRawFont &font, int
    #      renderTypeQuality)
    self._noteCreation(QSGRhiDistanceFieldGlyphCache, lambda: Rituals.call(
        'ritual_ZN29QSGRhiDistanceFieldGlyphCacheC1EP23QSGDefaultRenderCont'
        'extRK8QRawFonti',
        self._addressOf(rc), self._valueOf(font), renderTypeQuality,
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

  @overload(QList[QDistanceField])
  def storeGlyphs(self, glyphs: QList[QDistanceField]) -> None:
    """
    Calls Qt's 'void QSGRhiDistanceFieldGlyphCache::storeGlyphs(const
    QList<QDistanceField> &glyphs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhidistancefieldglyphcache.html#storeGlyphs

    Parameters
    ----------

    glyphs : QList[QDistanceField]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QSGRhiDistanceFieldGlyphCache::storeGlyphs(const
    #      QList<QDistanceField> &glyphs)
    self.uglySide.call(
        'ritual_ZN29QSGRhiDistanceFieldGlyphCache11storeGlyphsERK5QListI14Q'
        'DistanceFieldE',
        self._valueOf(glyphs),
    )

  @overload(QRhiResourceUpdateBatch)
  @overload(NoneType)
  def commitResourceUpdates(
      self,
      mergeInto: Optional[QRhiResourceUpdateBatch],
  ) -> None:
    """
    Calls Qt's 'void QSGRhiDistanceFieldGlyphCache::commitResourceUpdates(
    QRhiResourceUpdateBatch *mergeInto)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhidistancefieldglyphcache.html

    Parameters
    ----------

    mergeInto : Optional[QRhiResourceUpdateBatch]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGRhiDistanceFieldGlyphCache::commitResourceUpdates(
    #      QRhiResourceUpdateBatch *mergeInto)
    self.uglySide.call(
        'ritual_ZN29QSGRhiDistanceFieldGlyphCache21commitResourceUpdatesEP2'
        '3QRhiResourceUpdateBatch',
        self._addressOf(mergeInto),
    )

  @overload(QRawFont)
  def loadPregeneratedCache(self, font: QRawFont) -> bool:
    """
    Calls Qt's 'bool
    QSGRhiDistanceFieldGlyphCache::loadPregeneratedCache(const QRawFont
    &font)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhidistancefieldglyphcache.html

    Parameters
    ----------

    font : QRawFont
      Passed on as a value: Qt reads the C++ QRawFont, which stays Python's
      own.
    """
    #  bool QSGRhiDistanceFieldGlyphCache::loadPregeneratedCache(const
    #      QRawFont &font)
    return self.uglySide.call(
        'ritual_ZN29QSGRhiDistanceFieldGlyphCache21loadPregeneratedCacheERK'
        '8QRawFont',
        self._valueOf(font),
    )

  @staticmethod
  def createTexture(*__, **_) -> Never:
    """
    - Qt's 'void QSGRhiDistanceFieldGlyphCache::createTexture(TextureInfo
      *texInfo, int width, int height, const void *pixels)': names
      'QSGRhiDistanceFieldGlyphCache::TextureInfo', which has no cute class
      yet.
    - Qt's 'void QSGRhiDistanceFieldGlyphCache::createTexture(TextureInfo
      *texInfo, int width, int height)': names
      'QSGRhiDistanceFieldGlyphCache::TextureInfo', which has no cute class
      yet.
    """
    raise NotImplementedError(
        "'QSGRhiDistanceFieldGlyphCache.createTexture' has no cute function "
        "yet. Qt's 'void "
        "QSGRhiDistanceFieldGlyphCache::createTexture(TextureInfo *texInfo, "
        "int width, int height, const void *pixels)': names "
        "'QSGRhiDistanceFieldGlyphCache::TextureInfo', which has no cute "
        "class yet. Qt's 'void "
        "QSGRhiDistanceFieldGlyphCache::createTexture(TextureInfo *texInfo, "
        "int width, int height)': names "
        "'QSGRhiDistanceFieldGlyphCache::TextureInfo', which has no cute "
        "class yet.")

  @staticmethod
  def resizeTexture(*__, **_) -> Never:
    """
    Qt's 'void QSGRhiDistanceFieldGlyphCache::resizeTexture(TextureInfo
    *texInfo, int width, int height)': names
    'QSGRhiDistanceFieldGlyphCache::TextureInfo', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QSGRhiDistanceFieldGlyphCache.resizeTexture' has no cute function "
        "yet. Qt's 'void "
        "QSGRhiDistanceFieldGlyphCache::resizeTexture(TextureInfo *texInfo, "
        "int width, int height)': names "
        "'QSGRhiDistanceFieldGlyphCache::TextureInfo', which has no cute "
        "class yet.")

  @staticmethod
  def textureInfo(*__, **_) -> Never:
    """
    Qt's 'TextureInfo *QSGRhiDistanceFieldGlyphCache::textureInfo(int
    index)': gives 'QSGRhiDistanceFieldGlyphCache::TextureInfo', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QSGRhiDistanceFieldGlyphCache.textureInfo' has no cute function "
        "yet. Qt's 'TextureInfo "
        "*QSGRhiDistanceFieldGlyphCache::textureInfo(int index)': gives "
        "'QSGRhiDistanceFieldGlyphCache::TextureInfo', which has no cute "
        "class yet.")
