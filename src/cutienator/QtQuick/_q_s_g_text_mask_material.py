"""
QSGTextMaskMaterial binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgdefaultglyphnode_p_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QSGTextMaskMaterial to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtGui import QFontEngine
from . import QSGMaterial, QSGRendererInterface

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtGui import QColor, QTextureGlyphCache, QVector4D
  from . import QSGMaterialShader, QSGMaterialType, QSGRhiTextureGlyphCache
  from . import QSGTexture
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QVector4D = WAIT['QVector4D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGTextMaskMaterial(QSGMaterial):
  """
  The cute side of Qt's QSGTextMaskMaterial: a plain Python object standing
  in front of one C++ QSGTextMaskMaterial.

  It is built on the cute 'QSGMaterial', as Qt's QSGTextMaskMaterial is built
  on Qt's QSGMaterial, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGTextMaskMaterial that has a ritual and that
  Python can call so far, 11 names in all: 'type', 'createShader', 'compare',
  'setColor', 'color', 'texture', 'ensureUpToDate', 'glyphCache',
  'rhiGlyphCache', 'init', 'updateCache'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSGTextMaskMaterial::~QSGTextMaskMaterial()': the destructor:
    Python never removes a C++ QSGTextMaskMaterial.
  - Qt's 'void QSGTextMaskMaterial::populate(const QPointF &position, const
    QList<quint32> &glyphIndexes, const QList<QPointF> &glyphPositions,
    QSGGeometry *geometry, QRectF *boundingRect, QPointF *baseLine, const
    QMargins &margins)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  1 of the 15 functions Qt declares: 1 leans on 'QSGTextMaskMaterial.

  What to expect
  --------------

  - The C++ QSGTextMaskMaterial is created at the first use, not by
    'QSGTextMaskMaterial(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGTextMaskMaterial.
  - Each name of Qt's QSGTextMaskMaterial that has no cute function yet,
    '__init__', 'populate', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGTextMaskMaterial'

  #  A C++ QSGTextMaskMaterial Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGTextMaskMaterial'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> Optional[QSGMaterialType]:
    """
    Calls Qt's 'QSGMaterialType *QSGTextMaskMaterial::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgtextmaskmaterial.html#type

    Returns
    -------

    Optional[QSGMaterialType]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGMaterialType *QSGTextMaskMaterial::type() const
    ritual = 'ritual_ZNK19QSGTextMaskMaterial4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QSGTextMaskMaterial4typeEv'
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
    *QSGTextMaskMaterial::createShader(QSGRendererInterface::RenderMode
    renderMode) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgtextmaskmaterial.html#createShader

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
    #  QSGMaterialShader
    #      *QSGTextMaskMaterial::createShader(QSGRendererInterface::
    #      RenderMode renderMode) const
    address = self.uglySide.call(
        'ritual_ZNK19QSGTextMaskMaterial12createShaderEN20QSGRendererInterf'
        'ace10RenderModeE',
        renderMode.value,
    )
    from . import QSGMaterialShader
    return QSGMaterialShader._cuteAt(address)

  @overload(QSGMaterial)
  @overload(NoneType)
  def compare(self, other: Optional[QSGMaterial]) -> int:
    """
    Calls Qt's 'int QSGTextMaskMaterial::compare(const QSGMaterial *other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgtextmaskmaterial.html#compare

    Parameters
    ----------

    other : Optional[QSGMaterial]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QSGTextMaskMaterial::compare(const QSGMaterial *other) const
    ritual = 'ritual_ZNK19QSGTextMaskMaterial7compareEPK11QSGMaterial'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QSGTextMaskMaterial7compareEPK11QSGMaterial'
    return self.uglySide.call(ritual, self._addressOf(other))

  def color(self) -> QVector4D:
    """
    Calls Qt's 'const QVector4D &QSGTextMaskMaterial::color() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgtextmaskmaterial.html#color

    Returns
    -------

    QVector4D
      A new cute QVector4D around the copy Qt gave back. Python owns it.
    """
    #  const QVector4D &QSGTextMaskMaterial::color() const
    address = self.uglySide.call('ritual_ZNK19QSGTextMaskMaterial5colorEv')
    from ..QtGui import QVector4D
    return QVector4D._cuteOwning(address)

  def texture(self) -> Optional[QSGTexture]:
    """
    Calls Qt's 'QSGTexture *QSGTextMaskMaterial::texture() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgtextmaskmaterial.html#texture

    Returns
    -------

    Optional[QSGTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGTexture *QSGTextMaskMaterial::texture() const
    address = self.uglySide.call('ritual_ZNK19QSGTextMaskMaterial7textureEv')
    from . import QSGTexture
    return QSGTexture._cuteAt(address)

  def glyphCache(self) -> Optional[QTextureGlyphCache]:
    """
    Calls Qt's 'QTextureGlyphCache *QSGTextMaskMaterial::glyphCache() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgtextmaskmaterial.html#glyphCache

    Returns
    -------

    Optional[QTextureGlyphCache]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextureGlyphCache *QSGTextMaskMaterial::glyphCache() const
    address = self.uglySide.call(
        'ritual_ZNK19QSGTextMaskMaterial10glyphCacheEv',
    )
    from ..QtGui import QTextureGlyphCache
    return QTextureGlyphCache._cuteAt(address)

  def rhiGlyphCache(self) -> Optional[QSGRhiTextureGlyphCache]:
    """
    Calls Qt's 'QSGRhiTextureGlyphCache *QSGTextMaskMaterial::rhiGlyphCache()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgtextmaskmaterial.html#rhiGlyphCache

    Returns
    -------

    Optional[QSGRhiTextureGlyphCache]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGRhiTextureGlyphCache *QSGTextMaskMaterial::rhiGlyphCache() const
    address = self.uglySide.call(
        'ritual_ZNK19QSGTextMaskMaterial13rhiGlyphCacheEv',
    )
    from . import QSGRhiTextureGlyphCache
    return QSGRhiTextureGlyphCache._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QColor)
  def setColor(self, c: QColor) -> None:
    """
    Calls Qt's 'void QSGTextMaskMaterial::setColor(const QColor &c)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgtextmaskmaterial.html#setColor

    Parameters
    ----------

    c : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QSGTextMaskMaterial::setColor(const QColor &c)
    self.uglySide.call(
        'ritual_ZN19QSGTextMaskMaterial8setColorERK6QColor',
        self._valueOf(c),
    )

  @overload(QVector4D)
  def setColor(self, color: QVector4D) -> None:
    """
    Calls Qt's 'void QSGTextMaskMaterial::setColor(const QVector4D &color)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgtextmaskmaterial.html#setColor

    Parameters
    ----------

    color : QVector4D
      Passed on as a value: Qt reads the C++ QVector4D, which stays Python's
      own.
    """
    #  void QSGTextMaskMaterial::setColor(const QVector4D &color)
    self.uglySide.call(
        'ritual_ZN19QSGTextMaskMaterial8setColorERK9QVector4D',
        self._valueOf(color),
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QSGTextMaskMaterial::QSGTextMaskMaterial(QSGRenderContext *rc,
    const QVector4D &color, const QRawFont &font, QFontEngine::GlyphFormat
    glyphFormat)': leans on
    'QSGTextMaskMaterial::createShader(QSGRendererInterface::RenderMode)
    const', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QSGTextMaskMaterial.__init__' has no cute function yet. Qt's "
        "'QSGTextMaskMaterial::QSGTextMaskMaterial(QSGRenderContext *rc, "
        "const QVector4D &color, const QRawFont &font, "
        "QFontEngine::GlyphFormat glyphFormat)': leans on "
        "'QSGTextMaskMaterial::createShader(QSGRendererInterface::RenderMode"
        ") const', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

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

  def ensureUpToDate(self) -> bool:
    """
    Calls Qt's 'bool QSGTextMaskMaterial::ensureUpToDate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgtextmaskmaterial.html#ensureUpToDate
    """
    #  bool QSGTextMaskMaterial::ensureUpToDate()
    return self.uglySide.call(
        'ritual_ZN19QSGTextMaskMaterial14ensureUpToDateEv',
    )

  @overload(QFontEngine.GlyphFormat)
  def init(self, glyphFormat: QFontEngine.GlyphFormat) -> None:
    """
    Calls Qt's 'void QSGTextMaskMaterial::init(QFontEngine::GlyphFormat
    glyphFormat)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgtextmaskmaterial.html#init

    Parameters
    ----------

    glyphFormat : QFontEngine.GlyphFormat
      Passed on as its number.
    """
    #  void QSGTextMaskMaterial::init(QFontEngine::GlyphFormat glyphFormat)
    self.uglySide.call(
        'ritual_ZN19QSGTextMaskMaterial4initEN11QFontEngine11GlyphFormatE',
        glyphFormat.value,
    )

  @overload(QFontEngine.GlyphFormat)
  def updateCache(self, glyphFormat: QFontEngine.GlyphFormat) -> None:
    """
    Calls Qt's 'void
    QSGTextMaskMaterial::updateCache(QFontEngine::GlyphFormat glyphFormat)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgtextmaskmaterial.html#updateCache

    Parameters
    ----------

    glyphFormat : QFontEngine.GlyphFormat
      Passed on as its number.
    """
    #  void QSGTextMaskMaterial::updateCache(QFontEngine::GlyphFormat
    #      glyphFormat)
    self.uglySide.call(
        'ritual_ZN19QSGTextMaskMaterial11updateCacheEN11QFontEngine11GlyphF'
        'ormatE',
        glyphFormat.value,
    )

  @staticmethod
  def populate(*__, **_) -> Never:
    """
    Qt's 'void QSGTextMaskMaterial::populate(const QPointF &position, const
    QList<quint32> &glyphIndexes, const QList<QPointF> &glyphPositions,
    QSGGeometry *geometry, QRectF *boundingRect, QPointF *baseLine, const
    QMargins &margins)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSGTextMaskMaterial.populate' has no cute function yet. Qt's "
        "'void QSGTextMaskMaterial::populate(const QPointF &position, const "
        "QList<quint32> &glyphIndexes, const QList<QPointF> "
        "&glyphPositions, QSGGeometry *geometry, QRectF *boundingRect, "
        "QPointF *baseLine, const QMargins &margins)': takes a type Python "
        "has no way to hand over yet.")
