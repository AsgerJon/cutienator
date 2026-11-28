"""
QSGDistanceFieldTextMaterial binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgdistancefieldglyphnode_p_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QSGDistanceFieldTextMaterial to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QSGDistanceFieldGlyphCache, QSGMaterial, QSGRendererInterface

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QSize
  from ..QtGui import QColor, QVector4D
  from . import QSGMaterialShader, QSGMaterialType, QSGTexture
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGDistanceFieldTextMaterial(QSGMaterial):
  """
  The cute side of Qt's QSGDistanceFieldTextMaterial: a plain Python object
  standing in front of one C++ QSGDistanceFieldTextMaterial.

  It is built on the cute 'QSGMaterial', as Qt's QSGDistanceFieldTextMaterial
  is built on Qt's QSGMaterial, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGDistanceFieldTextMaterial that has a ritual and
  that Python can call so far, 15 names in all: 'type', 'createShader',
  'compare', 'setColor', 'color', 'setGlyphCache', 'glyphCache',
  'setTexture', 'texture', 'setFontScale', 'fontScale', 'textureSize',
  'updateTextureSize', 'updateTextureSizeAndWrapper', 'wrapperTexture'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSGDistanceFieldTextMaterial::~QSGDistanceFieldTextMaterial()': the
    destructor: Python never removes a C++ QSGDistanceFieldTextMaterial.

  What to expect
  --------------

  - The C++ QSGDistanceFieldTextMaterial is created at the first use, not by
    'QSGDistanceFieldTextMaterial(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGDistanceFieldTextMaterial.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGDistanceFieldTextMaterial'

  #  A C++ QSGDistanceFieldTextMaterial Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGDistanceFieldTextMaterial'

  #  The functions Qt calls itself that QSGDistanceFieldTextMaterial is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'setColor': (
          ('_ZN28QSGDistanceFieldTextMaterial8setColorERK6QColor',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtGui:QColor'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> Optional[QSGMaterialType]:
    """
    Calls Qt's 'QSGMaterialType *QSGDistanceFieldTextMaterial::type() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdistancefieldtextmaterial.html#type

    Returns
    -------

    Optional[QSGMaterialType]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGMaterialType *QSGDistanceFieldTextMaterial::type() const
    ritual = 'ritual_ZNK28QSGDistanceFieldTextMaterial4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK28QSGDistanceFieldTextMaterial4typeEv'
    address = self.uglySide.call(ritual)
    from . import QSGMaterialType
    return QSGMaterialType._cuteAt(address)

  @overload(QSGRendererInterface.RenderMode)
  def createShader(
      self,
      renderMode: QSGRendererInterface.RenderMode,
  ) -> Optional[QSGMaterialShader]:
    """
    Calls Qt's 'QSGMaterialShader
    *QSGDistanceFieldTextMaterial::createShader(QSGRendererInterface::
    RenderMode renderMode) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdistancefieldtextmaterial.html#createShader

    Parameters
    ----------

    renderMode : QSGRendererInterface.RenderMode
      Passed on as its number.

    Returns
    -------

    Optional[QSGMaterialShader]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGMaterialShader *QSGDistanceFieldTextMaterial::createShader(
    #      QSGRendererInterface::RenderMode renderMode) const
    ritual = (
        'ritual_ZNK28QSGDistanceFieldTextMaterial12createShaderEN20QSGRende'
        'rerInterface10RenderModeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK28QSGDistanceFieldTextMaterial12createShaderEN20QS'
          'GRendererInterface10RenderModeE')
    address = self.uglySide.call(ritual, renderMode.value)
    from . import QSGMaterialShader
    return QSGMaterialShader._cuteAt(address)

  @overload(QSGMaterial)
  @overload(NoneType)
  def compare(self, other: Optional[QSGMaterial]) -> int:
    """
    Calls Qt's 'int QSGDistanceFieldTextMaterial::compare(const QSGMaterial
    *other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdistancefieldtextmaterial.html#compare

    Parameters
    ----------

    other : Optional[QSGMaterial]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QSGDistanceFieldTextMaterial::compare(const QSGMaterial *other)
    #      const
    ritual = (
        'ritual_ZNK28QSGDistanceFieldTextMaterial7compareEPK11QSGMaterial')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK28QSGDistanceFieldTextMaterial7compareEPK11QSGMate'
          'rial')
    return self.uglySide.call(ritual, self._addressOf(other))

  def color(self) -> QVector4D:
    """
    Calls Qt's 'const QVector4D &QSGDistanceFieldTextMaterial::color()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdistancefieldtextmaterial.html#color

    Returns
    -------

    QVector4D
      A new cute QVector4D around the copy Qt gave back. Python owns it.
    """
    #  const QVector4D &QSGDistanceFieldTextMaterial::color() const
    address = self.uglySide.call(
        'ritual_ZNK28QSGDistanceFieldTextMaterial5colorEv',
    )
    from ..QtGui import QVector4D
    return QVector4D._cuteOwning(address)

  def glyphCache(self) -> Optional[QSGDistanceFieldGlyphCache]:
    """
    Calls Qt's 'QSGDistanceFieldGlyphCache
    *QSGDistanceFieldTextMaterial::glyphCache() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdistancefieldtextmaterial.html#glyphCache

    Returns
    -------

    Optional[QSGDistanceFieldGlyphCache]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGDistanceFieldGlyphCache *QSGDistanceFieldTextMaterial::glyphCache()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK28QSGDistanceFieldTextMaterial10glyphCacheEv',
    )
    return QSGDistanceFieldGlyphCache._cuteAt(address)

  def texture(self) -> Optional[QSGDistanceFieldGlyphCache.Texture]:
    """
    Calls Qt's 'const QSGDistanceFieldGlyphCache::Texture
    *QSGDistanceFieldTextMaterial::texture() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdistancefieldtextmaterial.html#texture

    Returns
    -------

    Optional[QSGDistanceFieldGlyphCache.Texture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QSGDistanceFieldGlyphCache::Texture
    #      *QSGDistanceFieldTextMaterial::texture() const
    address = self.uglySide.call(
        'ritual_ZNK28QSGDistanceFieldTextMaterial7textureEv',
    )
    return QSGDistanceFieldGlyphCache.Texture._cuteAt(address)

  def fontScale(self) -> float:
    """
    Calls Qt's 'qreal QSGDistanceFieldTextMaterial::fontScale() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdistancefieldtextmaterial.html#fontScale
    """
    #  qreal QSGDistanceFieldTextMaterial::fontScale() const
    return self.uglySide.call(
        'ritual_ZNK28QSGDistanceFieldTextMaterial9fontScaleEv',
    )

  def textureSize(self) -> QSize:
    """
    Calls Qt's 'QSize QSGDistanceFieldTextMaterial::textureSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdistancefieldtextmaterial.html#textureSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QSGDistanceFieldTextMaterial::textureSize() const
    address = self.uglySide.call(
        'ritual_ZNK28QSGDistanceFieldTextMaterial11textureSizeEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def wrapperTexture(self) -> Optional[QSGTexture]:
    """
    Calls Qt's 'QSGTexture *QSGDistanceFieldTextMaterial::wrapperTexture()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdistancefieldtextmaterial.html#wrapperTexture

    Returns
    -------

    Optional[QSGTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGTexture *QSGDistanceFieldTextMaterial::wrapperTexture() const
    address = self.uglySide.call(
        'ritual_ZNK28QSGDistanceFieldTextMaterial14wrapperTextureEv',
    )
    from . import QSGTexture
    return QSGTexture._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QColor)
  def setColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QSGDistanceFieldTextMaterial::setColor(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdistancefieldtextmaterial.html#setColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QSGDistanceFieldTextMaterial::setColor(const QColor &color)
    ritual = 'ritual_ZN28QSGDistanceFieldTextMaterial8setColorERK6QColor'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QSGDistanceFieldTextMaterial8setColorERK6QColor')
    self.uglySide.call(ritual, self._valueOf(color))

  @overload(QSGDistanceFieldGlyphCache)
  @overload(NoneType)
  def setGlyphCache(self, a: Optional[QSGDistanceFieldGlyphCache]) -> None:
    """
    Calls Qt's 'void
    QSGDistanceFieldTextMaterial::setGlyphCache(QSGDistanceFieldGlyphCache
    *a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdistancefieldtextmaterial.html#setGlyphCache

    Parameters
    ----------

    a : Optional[QSGDistanceFieldGlyphCache]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGDistanceFieldTextMaterial::setGlyphCache(
    #      QSGDistanceFieldGlyphCache *a)
    self.uglySide.call(
        'ritual_ZN28QSGDistanceFieldTextMaterial13setGlyphCacheEP26QSGDista'
        'nceFieldGlyphCache',
        self._addressOf(a),
    )

  @overload(QSGDistanceFieldGlyphCache.Texture)
  @overload(NoneType)
  def setTexture(
      self,
      tex: Optional[QSGDistanceFieldGlyphCache.Texture],
  ) -> None:
    """
    Calls Qt's 'void QSGDistanceFieldTextMaterial::setTexture(const
    QSGDistanceFieldGlyphCache::Texture *tex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdistancefieldtextmaterial.html#setTexture

    Parameters
    ----------

    tex : Optional[QSGDistanceFieldGlyphCache.Texture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGDistanceFieldTextMaterial::setTexture(const
    #      QSGDistanceFieldGlyphCache::Texture *tex)
    self.uglySide.call(
        'ritual_ZN28QSGDistanceFieldTextMaterial10setTextureEPKN26QSGDistan'
        'ceFieldGlyphCache7TextureE',
        self._addressOf(tex),
    )

  @overload(float)
  def setFontScale(self, fontScale: float) -> None:
    """
    Calls Qt's 'void QSGDistanceFieldTextMaterial::setFontScale(qreal
    fontScale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdistancefieldtextmaterial.html#setFontScale

    Parameters
    ----------

    fontScale : float
      Passed on as it is.
    """
    #  void QSGDistanceFieldTextMaterial::setFontScale(qreal fontScale)
    self.uglySide.call(
        'ritual_ZN28QSGDistanceFieldTextMaterial12setFontScaleEd', fontScale,
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QSGDistanceFieldTextMaterial::QSGDistanceFieldTextMaterial()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdistancefieldtextmaterial.html
    """
    #  QSGDistanceFieldTextMaterial::QSGDistanceFieldTextMaterial()
    self._noteCreation(QSGDistanceFieldTextMaterial, lambda: Rituals.call(
        'ritual_ZN28QSGDistanceFieldTextMaterialC1Ev',
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

  def updateTextureSize(self) -> bool:
    """
    Calls Qt's 'bool QSGDistanceFieldTextMaterial::updateTextureSize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdistancefieldtextmaterial.html
    """
    #  bool QSGDistanceFieldTextMaterial::updateTextureSize()
    return self.uglySide.call(
        'ritual_ZN28QSGDistanceFieldTextMaterial17updateTextureSizeEv',
    )

  def updateTextureSizeAndWrapper(self) -> bool:
    """
    Calls Qt's 'bool
    QSGDistanceFieldTextMaterial::updateTextureSizeAndWrapper()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdistancefieldtextmaterial.html
    """
    #  bool QSGDistanceFieldTextMaterial::updateTextureSizeAndWrapper()
    return self.uglySide.call(
        'ritual_ZN28QSGDistanceFieldTextMaterial27updateTextureSizeAndWrapp'
        'erEv',
    )
