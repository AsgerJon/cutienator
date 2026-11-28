"""
QOpenGL2PaintEngineExPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpenGL/6.12.0/QtOpenGL/private/qopenglpaintengine_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QOpenGL2PaintEngineExPrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..QtGui import QPaintEngineExPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QRect
  from ..QtGui import QBrush
  from . import QOpenGLRect
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBrush = WAIT['QBrush']
  QOpenGLRect = WAIT['QOpenGLRect']
  QRect = WAIT['QRect']


class QOpenGL2PaintEngineExPrivate(QPaintEngineExPrivate):
  """
  The cute side of Qt's QOpenGL2PaintEngineExPrivate: a plain Python object
  standing in front of one C++ QOpenGL2PaintEngineExPrivate.

  It is built on the cute 'QPaintEngineExPrivate', as Qt's
  QOpenGL2PaintEngineExPrivate is built on Qt's QPaintEngineExPrivate, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QOpenGL2PaintEngineExPrivate that has a ritual and
  that Python can call so far, 15 names in all: 'updateMatrix',
  'updateCompositionMode', 'activateTextureUnit', 'resetGLState',
  'composite', 'setBrush', 'useSimpleShader', 'clearClip',
  'resetClipIfNeeded', 'updateClipScissorTest', 'setScissor',
  'regenerateClip', 'systemStateChanged', 'setVertexAttribArrayEnabled',
  'syncGlState'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpenGL2PaintEngineEx *QOpenGL2PaintEngineExPrivate::q_func()':
    gives 'QOpenGL2PaintEngineEx', which has no cute class yet.
  - Qt's 'const QOpenGL2PaintEngineEx *QOpenGL2PaintEngineExPrivate::q_func()
    const': gives 'QOpenGL2PaintEngineEx', which has no cute class yet.
  - Qt's 'QOpenGL2PaintEngineExPrivate::QOpenGL2PaintEngineExPrivate(
    QOpenGL2PaintEngineEx *q_ptr)': names 'QOpenGL2PaintEngineEx', which has
    no cute class yet.
  - Qt's 'QOpenGL2PaintEngineExPrivate::~QOpenGL2PaintEngineExPrivate()': the
    destructor: Python never removes a C++ QOpenGL2PaintEngineExPrivate.
  - Qt's 'void QOpenGL2PaintEngineExPrivate::uploadData(unsigned int
    arrayIndex, const GLfloat *data, GLuint count)': names 'GLfloat', which
    has no cute class yet.
  - Qt's 'bool QOpenGL2PaintEngineExPrivate::uploadIndexData(const void
    *data, GLenum indexValueType, GLuint count)': names 'void', which has no
    cute class yet.
  - Qt's 'void QOpenGL2PaintEngineExPrivate::drawVertexArrays(const float
    *data, int *stops, int stopCount, GLenum primitive)': names 'float',
    which has no cute class yet.
  - Qt's 'void
    QOpenGL2PaintEngineExPrivate::drawVertexArrays(QOpenGL2PEXVertexArray
    &vertexArray, GLenum primitive)': takes a type Python has no way to hand
    over yet.
  - Qt's 'void QOpenGL2PaintEngineExPrivate::fillStencilWithVertexArray(const
    float *data, int count, int *stops, int stopCount, const QOpenGLRect
    &bounds, StencilFillMode mode)': names 'float', which has no cute class
    yet.
  - Qt's 'void QOpenGL2PaintEngineExPrivate::fillStencilWithVertexArray(
    QOpenGL2PEXVertexArray &vertexArray, bool useWindingFill)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void QOpenGL2PaintEngineExPrivate::transferMode(EngineMode
    newMode)': names the enum 'EngineMode', whose class cannot be named here.
  - Qt's 'GLuint QOpenGL2PaintEngineExPrivate::location(const
    QOpenGLEngineShaderManager::Uniform uniform)': takes a type Python has no
    way to hand over yet.
  - Qt's 'void QOpenGL2PaintEngineExPrivate::writeClip(const QVectorPath
    &path, uint value)': takes a type Python has no way to hand over yet.
  - Qt's 'QOpenGLEngineShaderManager
    *QOpenGL2PaintEngineExPrivate::shaderManagerForEngine(
    QOpenGL2PaintEngineEx *engine)': names 'QOpenGL2PaintEngineEx', which has
    no cute class yet.
  - Qt's 'QOpenGL2PaintEngineExPrivate
    *QOpenGL2PaintEngineExPrivate::getData(QOpenGL2PaintEngineEx *engine)':
    names 'QOpenGL2PaintEngineEx', which has no cute class yet.

  What has no ritual
  ------------------

  12 of the 42 functions Qt declares: 6 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 3 leans on
  'QOpenGL2PaintEngineExPrivate; 2 a template; 1 cannot be called and cannot
  be called through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QOpenGL2PaintEngineExPrivate is created at the first use, not by
    'QOpenGL2PaintEngineExPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QOpenGL2PaintEngineExPrivate.
  - Each name of Qt's QOpenGL2PaintEngineExPrivate that has no cute function
    yet, '__init__', 'bindTexture', 'cleanupVectorPath', 'drawCachedGlyphs',
    'drawPixmapFragments', 'drawTexture', 'drawVertexArrays', 'fill',
    'fillStencilWithVertexArray', 'getData', 'location',
    'prepareForCachedGlyphDraw', 'prepareForDraw', 'shaderManagerForEngine',
    'stroke', 'transferMode', 'updateBrushTexture', 'updateBrushUniforms',
    'updateTexture', 'uploadData', 'uploadIndexData', 'writeClip', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QOpenGL2PaintEngineExPrivate, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class StencilFillMode(CuteNum):
    """
    The enum 'QOpenGL2PaintEngineExPrivate::StencilFillMode' of Qt, with the
    3 names Qt gives in it.
    """

    OddEvenFillMode = Kee[int](0)
    WindingFillMode = Kee[int](1)
    TriStripStrokeFillMode = Kee[int](2)

  class TextureUpdateMode(CuteNum):
    """
    The enum 'QOpenGL2PaintEngineExPrivate::TextureUpdateMode' of Qt, with
    the 2 names Qt gives in it.
    """

    UpdateIfNeeded = Kee[int](0)
    ForceUpdate = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpenGL2PaintEngineExPrivate'

  #  A C++ QOpenGL2PaintEngineExPrivate Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QOpenGL2PaintEngineExPrivate'

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

  @overload(QBrush)
  def setBrush(self, brush: QBrush) -> None:
    """
    Calls Qt's 'void QOpenGL2PaintEngineExPrivate::setBrush(const QBrush
    &brush)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengl2paintengineexprivate.html#setBrush

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void QOpenGL2PaintEngineExPrivate::setBrush(const QBrush &brush)
    self.uglySide.call(
        'ritual_ZN28QOpenGL2PaintEngineExPrivate8setBrushERK6QBrush',
        self._valueOf(brush),
    )

  @overload(QRect)
  def setScissor(self, rect: QRect) -> None:
    """
    Calls Qt's 'void QOpenGL2PaintEngineExPrivate::setScissor(const QRect
    &rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengl2paintengineexprivate.html#setScissor

    Parameters
    ----------

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QOpenGL2PaintEngineExPrivate::setScissor(const QRect &rect)
    self.uglySide.call(
        'ritual_ZN28QOpenGL2PaintEngineExPrivate10setScissorERK5QRect',
        self._valueOf(rect),
    )

  @overload(int)
  @overload(int, bool)
  def setVertexAttribArrayEnabled(
      self,
      arrayIndex: int,
      enabled: bool = True,
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGL2PaintEngineExPrivate::setVertexAttribArrayEnabled(int arrayIndex,
    bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengl2paintengineexprivate.html

    Parameters
    ----------

    arrayIndex : int
      Passed on as it is.

    enabled : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QOpenGL2PaintEngineExPrivate::setVertexAttribArrayEnabled(int
    #      arrayIndex, bool enabled)
    self.uglySide.call(
        'ritual_ZN28QOpenGL2PaintEngineExPrivate27setVertexAttribArrayEnabl'
        'edEib',
        arrayIndex, enabled,
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
    Qt's 'QOpenGL2PaintEngineExPrivate::QOpenGL2PaintEngineExPrivate(
    QOpenGL2PaintEngineEx *q_ptr)': names 'QOpenGL2PaintEngineEx', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGL2PaintEngineExPrivate.__init__' has no cute function yet. "
        "Qt's "
        "'QOpenGL2PaintEngineExPrivate::QOpenGL2PaintEngineExPrivate(QOpenGL"
        "2PaintEngineEx *q_ptr)': names 'QOpenGL2PaintEngineEx', which has "
        "no cute class yet.")

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

  def updateMatrix(self) -> None:
    """
    Calls Qt's 'void QOpenGL2PaintEngineExPrivate::updateMatrix()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengl2paintengineexprivate.html#updateMatrix
    """
    #  void QOpenGL2PaintEngineExPrivate::updateMatrix()
    self.uglySide.call(
        'ritual_ZN28QOpenGL2PaintEngineExPrivate12updateMatrixEv',
    )

  def updateCompositionMode(self) -> None:
    """
    Calls Qt's 'void QOpenGL2PaintEngineExPrivate::updateCompositionMode()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengl2paintengineexprivate.html
    """
    #  void QOpenGL2PaintEngineExPrivate::updateCompositionMode()
    self.uglySide.call(
        'ritual_ZN28QOpenGL2PaintEngineExPrivate21updateCompositionModeEv',
    )

  @overload(int)
  def activateTextureUnit(self, textureUnit: int) -> None:
    """
    Calls Qt's 'void QOpenGL2PaintEngineExPrivate::activateTextureUnit(GLenum
    textureUnit)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengl2paintengineexprivate.html

    Parameters
    ----------

    textureUnit : int
      Passed on as it is.
    """
    #  void QOpenGL2PaintEngineExPrivate::activateTextureUnit(GLenum
    #      textureUnit)
    self.uglySide.call(
        'ritual_ZN28QOpenGL2PaintEngineExPrivate19activateTextureUnitEj',
        textureUnit,
    )

  def resetGLState(self) -> None:
    """
    Calls Qt's 'void QOpenGL2PaintEngineExPrivate::resetGLState()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengl2paintengineexprivate.html#resetGLState
    """
    #  void QOpenGL2PaintEngineExPrivate::resetGLState()
    self.uglySide.call(
        'ritual_ZN28QOpenGL2PaintEngineExPrivate12resetGLStateEv',
    )

  @overload(QOpenGLRect)
  def composite(self, boundingRect: QOpenGLRect) -> None:
    """
    Calls Qt's 'void QOpenGL2PaintEngineExPrivate::composite(const
    QOpenGLRect &boundingRect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengl2paintengineexprivate.html#composite

    Parameters
    ----------

    boundingRect : QOpenGLRect
      Passed on as a value: Qt reads the C++ QOpenGLRect, which stays
      Python's own.
    """
    #  void QOpenGL2PaintEngineExPrivate::composite(const QOpenGLRect
    #      &boundingRect)
    self.uglySide.call(
        'ritual_ZN28QOpenGL2PaintEngineExPrivate9compositeERK11QOpenGLRect',
        self._valueOf(boundingRect),
    )

  def useSimpleShader(self) -> None:
    """
    Calls Qt's 'void QOpenGL2PaintEngineExPrivate::useSimpleShader()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengl2paintengineexprivate.html#useSimpleShader
    """
    #  void QOpenGL2PaintEngineExPrivate::useSimpleShader()
    self.uglySide.call(
        'ritual_ZN28QOpenGL2PaintEngineExPrivate15useSimpleShaderEv',
    )

  @overload(int)
  def clearClip(self, value: int) -> None:
    """
    Calls Qt's 'void QOpenGL2PaintEngineExPrivate::clearClip(uint value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengl2paintengineexprivate.html#clearClip

    Parameters
    ----------

    value : int
      Passed on as it is.
    """
    #  void QOpenGL2PaintEngineExPrivate::clearClip(uint value)
    self.uglySide.call(
        'ritual_ZN28QOpenGL2PaintEngineExPrivate9clearClipEj', value,
    )

  def resetClipIfNeeded(self) -> None:
    """
    Calls Qt's 'void QOpenGL2PaintEngineExPrivate::resetClipIfNeeded()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengl2paintengineexprivate.html
    """
    #  void QOpenGL2PaintEngineExPrivate::resetClipIfNeeded()
    self.uglySide.call(
        'ritual_ZN28QOpenGL2PaintEngineExPrivate17resetClipIfNeededEv',
    )

  def updateClipScissorTest(self) -> None:
    """
    Calls Qt's 'void QOpenGL2PaintEngineExPrivate::updateClipScissorTest()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengl2paintengineexprivate.html
    """
    #  void QOpenGL2PaintEngineExPrivate::updateClipScissorTest()
    self.uglySide.call(
        'ritual_ZN28QOpenGL2PaintEngineExPrivate21updateClipScissorTestEv',
    )

  def regenerateClip(self) -> None:
    """
    Calls Qt's 'void QOpenGL2PaintEngineExPrivate::regenerateClip()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengl2paintengineexprivate.html#regenerateClip
    """
    #  void QOpenGL2PaintEngineExPrivate::regenerateClip()
    self.uglySide.call(
        'ritual_ZN28QOpenGL2PaintEngineExPrivate14regenerateClipEv',
    )

  def systemStateChanged(self) -> None:
    """
    Calls Qt's 'void QOpenGL2PaintEngineExPrivate::systemStateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengl2paintengineexprivate.html
    """
    #  void QOpenGL2PaintEngineExPrivate::systemStateChanged()
    ritual = 'ritual_ZN28QOpenGL2PaintEngineExPrivate18systemStateChangedEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QOpenGL2PaintEngineExPrivate18systemStateChangedE'
          'v')
    self.uglySide.call(ritual)

  def syncGlState(self) -> None:
    """
    Calls Qt's 'void QOpenGL2PaintEngineExPrivate::syncGlState()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengl2paintengineexprivate.html#syncGlState
    """
    #  void QOpenGL2PaintEngineExPrivate::syncGlState()
    self.uglySide.call(
        'ritual_ZN28QOpenGL2PaintEngineExPrivate11syncGlStateEv',
    )

  @staticmethod
  def bindTexture(*__, **_) -> Never:
    """
    Qt's 'QOpenGL2PaintEngineExPrivate::bindTexture': a template: a pattern
    and no single function.
    """
    raise NotImplementedError(
        "'QOpenGL2PaintEngineExPrivate.bindTexture' has no cute function "
        "yet. Qt's 'QOpenGL2PaintEngineExPrivate::bindTexture': a template: "
        "a pattern and no single function.")

  @staticmethod
  def cleanupVectorPath(*__, **_) -> Never:
    """
    Qt's 'void QOpenGL2PaintEngineExPrivate::cleanupVectorPath(QPaintEngineEx
    *engine, void *data)': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: unknown type name
    'QOpenGL2PEVectorPathCache'.
    """
    raise NotImplementedError(
        "'QOpenGL2PaintEngineExPrivate.cleanupVectorPath' has no cute "
        "function yet. Qt's 'void "
        "QOpenGL2PaintEngineExPrivate::cleanupVectorPath(QPaintEngineEx "
        "*engine, void *data)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: unknown "
        "type name 'QOpenGL2PEVectorPathCache'.")

  @staticmethod
  def drawCachedGlyphs(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGL2PaintEngineExPrivate::drawCachedGlyphs(QFontEngine::GlyphFormat
    glyphFormat, QStaticTextItem *staticTextItem)': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    no member named 'glyphFormat' in 'QStaticTextUserData'.
    """
    raise NotImplementedError(
        "'QOpenGL2PaintEngineExPrivate.drawCachedGlyphs' has no cute "
        "function yet. Qt's 'void "
        "QOpenGL2PaintEngineExPrivate::drawCachedGlyphs(QFontEngine::GlyphFo"
        "rmat glyphFormat, QStaticTextItem *staticTextItem)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: no member named 'glyphFormat' in "
        "'QStaticTextUserData'.")

  @staticmethod
  def drawPixmapFragments(*__, **_) -> Never:
    """
    Qt's 'void QOpenGL2PaintEngineExPrivate::drawPixmapFragments(const
    QPainter::PixmapFragment *fragments, int fragmentCount, const QPixmap
    &pixmap, QPainter::PixmapFragmentHints hints)': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    use of undeclared identifier 'qt_premultiplyColor'.
    """
    raise NotImplementedError(
        "'QOpenGL2PaintEngineExPrivate.drawPixmapFragments' has no cute "
        "function yet. Qt's 'void "
        "QOpenGL2PaintEngineExPrivate::drawPixmapFragments(const "
        "QPainter::PixmapFragment *fragments, int fragmentCount, const "
        "QPixmap &pixmap, QPainter::PixmapFragmentHints hints)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'qt_premultiplyColor'.")

  @staticmethod
  def drawTexture(*__, **_) -> Never:
    """
    Qt's 'void QOpenGL2PaintEngineExPrivate::drawTexture(const QOpenGLRect
    &dest, const QOpenGLRect &src, const QSize &textureSize, bool opaque,
    bool pattern)': cannot be called and cannot be called through the
    meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QOpenGL2PaintEngineExPrivate.drawTexture' has no cute function "
        "yet. Qt's 'void QOpenGL2PaintEngineExPrivate::drawTexture(const "
        "QOpenGLRect &dest, const QOpenGLRect &src, const QSize "
        "&textureSize, bool opaque, bool pattern)': cannot be called and "
        "cannot be called through the meta-object and cannot be copied: no "
        "header file has its code, Qt's source does not mark it or its "
        "class for use from outside Qt or writes it 'inline' or nowhere, "
        "and it is no signal, slot or invokable function giving back "
        "nothing, of a class built on QObject, and Qt's source has no code "
        "for it that could be told from the rest.")

  @staticmethod
  def drawVertexArrays(*__, **_) -> Never:
    """
    - Qt's 'void QOpenGL2PaintEngineExPrivate::drawVertexArrays(const float
      *data, int *stops, int stopCount, GLenum primitive)': names 'float',
      which has no cute class yet.
    - Qt's 'void
      QOpenGL2PaintEngineExPrivate::drawVertexArrays(QOpenGL2PEXVertexArray
      &vertexArray, GLenum primitive)': takes a type Python has no way to
      hand over yet.
    """
    raise NotImplementedError(
        "'QOpenGL2PaintEngineExPrivate.drawVertexArrays' has no cute "
        "function yet. Qt's 'void "
        "QOpenGL2PaintEngineExPrivate::drawVertexArrays(const float *data, "
        "int *stops, int stopCount, GLenum primitive)': names 'float', "
        "which has no cute class yet. Qt's 'void "
        "QOpenGL2PaintEngineExPrivate::drawVertexArrays(QOpenGL2PEXVertexArr"
        "ay &vertexArray, GLenum primitive)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def fill(*__, **_) -> Never:
    """
    Qt's 'void QOpenGL2PaintEngineExPrivate::fill(const QVectorPath &path)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier
    'QOpenGL2PEVectorPathCache'.
    """
    raise NotImplementedError(
        "'QOpenGL2PaintEngineExPrivate.fill' has no cute function yet. Qt's "
        "'void QOpenGL2PaintEngineExPrivate::fill(const QVectorPath "
        "&path)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'QOpenGL2PEVectorPathCache'.")

  @staticmethod
  def fillStencilWithVertexArray(*__, **_) -> Never:
    """
    - Qt's 'void
      QOpenGL2PaintEngineExPrivate::fillStencilWithVertexArray(const float
      *data, int count, int *stops, int stopCount, const QOpenGLRect &bounds,
      StencilFillMode mode)': names 'float', which has no cute class yet.
    - Qt's 'void QOpenGL2PaintEngineExPrivate::fillStencilWithVertexArray(
      QOpenGL2PEXVertexArray &vertexArray, bool useWindingFill)': takes a
      type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QOpenGL2PaintEngineExPrivate.fillStencilWithVertexArray' has no "
        "cute function yet. Qt's 'void "
        "QOpenGL2PaintEngineExPrivate::fillStencilWithVertexArray(const "
        "float *data, int count, int *stops, int stopCount, const "
        "QOpenGLRect &bounds, StencilFillMode mode)': names 'float', which "
        "has no cute class yet. Qt's 'void "
        "QOpenGL2PaintEngineExPrivate::fillStencilWithVertexArray(QOpenGL2PE"
        "XVertexArray &vertexArray, bool useWindingFill)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def getData(*__, **_) -> Never:
    """
    Qt's 'QOpenGL2PaintEngineExPrivate
    *QOpenGL2PaintEngineExPrivate::getData(QOpenGL2PaintEngineEx *engine)':
    names 'QOpenGL2PaintEngineEx', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGL2PaintEngineExPrivate.getData' has no cute function yet. "
        "Qt's 'QOpenGL2PaintEngineExPrivate "
        "*QOpenGL2PaintEngineExPrivate::getData(QOpenGL2PaintEngineEx "
        "*engine)': names 'QOpenGL2PaintEngineEx', which has no cute class "
        "yet.")

  @staticmethod
  def location(*__, **_) -> Never:
    """
    Qt's 'GLuint QOpenGL2PaintEngineExPrivate::location(const
    QOpenGLEngineShaderManager::Uniform uniform)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QOpenGL2PaintEngineExPrivate.location' has no cute function yet. "
        "Qt's 'GLuint QOpenGL2PaintEngineExPrivate::location(const "
        "QOpenGLEngineShaderManager::Uniform uniform)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def prepareForCachedGlyphDraw(*__, **_) -> Never:
    """
    Qt's 'bool QOpenGL2PaintEngineExPrivate::prepareForCachedGlyphDraw(const
    QFontEngineGlyphCache &cache)': leans on
    'QOpenGL2PaintEngineExPrivate::updateBrushTexture()', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QOpenGL2PaintEngineExPrivate.prepareForCachedGlyphDraw' has no "
        "cute function yet. Qt's 'bool "
        "QOpenGL2PaintEngineExPrivate::prepareForCachedGlyphDraw(const "
        "QFontEngineGlyphCache &cache)': leans on "
        "'QOpenGL2PaintEngineExPrivate::updateBrushTexture()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def prepareForDraw(*__, **_) -> Never:
    """
    Qt's 'bool QOpenGL2PaintEngineExPrivate::prepareForDraw(bool
    srcPixelsAreOpaque)': leans on
    'QOpenGL2PaintEngineExPrivate::updateBrushTexture()', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QOpenGL2PaintEngineExPrivate.prepareForDraw' has no cute function "
        "yet. Qt's 'bool QOpenGL2PaintEngineExPrivate::prepareForDraw(bool "
        "srcPixelsAreOpaque)': leans on "
        "'QOpenGL2PaintEngineExPrivate::updateBrushTexture()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def shaderManagerForEngine(*__, **_) -> Never:
    """
    Qt's 'QOpenGLEngineShaderManager
    *QOpenGL2PaintEngineExPrivate::shaderManagerForEngine(
    QOpenGL2PaintEngineEx *engine)': names 'QOpenGL2PaintEngineEx', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGL2PaintEngineExPrivate.shaderManagerForEngine' has no cute "
        "function yet. Qt's 'QOpenGLEngineShaderManager "
        "*QOpenGL2PaintEngineExPrivate::shaderManagerForEngine(QOpenGL2Paint"
        "EngineEx *engine)': names 'QOpenGL2PaintEngineEx', which has no "
        "cute class yet.")

  @staticmethod
  def stroke(*__, **_) -> Never:
    """
    Qt's 'void QOpenGL2PaintEngineExPrivate::stroke(const QVectorPath &path,
    const QPen &pen)': leans on
    'QOpenGL2PaintEngineExPrivate::updateBrushTexture()', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QOpenGL2PaintEngineExPrivate.stroke' has no cute function yet. "
        "Qt's 'void QOpenGL2PaintEngineExPrivate::stroke(const QVectorPath "
        "&path, const QPen &pen)': leans on "
        "'QOpenGL2PaintEngineExPrivate::updateBrushTexture()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def transferMode(*__, **_) -> Never:
    """
    Qt's 'void QOpenGL2PaintEngineExPrivate::transferMode(EngineMode
    newMode)': names the enum 'EngineMode', whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QOpenGL2PaintEngineExPrivate.transferMode' has no cute function "
        "yet. Qt's 'void "
        "QOpenGL2PaintEngineExPrivate::transferMode(EngineMode newMode)': "
        "names the enum 'EngineMode', whose class cannot be named here.")

  @staticmethod
  def updateBrushTexture(*__, **_) -> Never:
    """
    Qt's 'void QOpenGL2PaintEngineExPrivate::updateBrushTexture()': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'qt_imageForBrush'.
    """
    raise NotImplementedError(
        "'QOpenGL2PaintEngineExPrivate.updateBrushTexture' has no cute "
        "function yet. Qt's 'void "
        "QOpenGL2PaintEngineExPrivate::updateBrushTexture()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier "
        "'qt_imageForBrush'.")

  @staticmethod
  def updateBrushUniforms(*__, **_) -> Never:
    """
    Qt's 'void QOpenGL2PaintEngineExPrivate::updateBrushUniforms()': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'qt_premultiplyColor'.
    """
    raise NotImplementedError(
        "'QOpenGL2PaintEngineExPrivate.updateBrushUniforms' has no cute "
        "function yet. Qt's 'void "
        "QOpenGL2PaintEngineExPrivate::updateBrushUniforms()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier "
        "'qt_premultiplyColor'.")

  @staticmethod
  def updateTexture(*__, **_) -> Never:
    """
    Qt's 'QOpenGL2PaintEngineExPrivate::updateTexture': a template: a pattern
    and no single function.
    """
    raise NotImplementedError(
        "'QOpenGL2PaintEngineExPrivate.updateTexture' has no cute function "
        "yet. Qt's 'QOpenGL2PaintEngineExPrivate::updateTexture': a "
        "template: a pattern and no single function.")

  @staticmethod
  def uploadData(*__, **_) -> Never:
    """
    Qt's 'void QOpenGL2PaintEngineExPrivate::uploadData(unsigned int
    arrayIndex, const GLfloat *data, GLuint count)': names 'GLfloat', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGL2PaintEngineExPrivate.uploadData' has no cute function "
        "yet. Qt's 'void QOpenGL2PaintEngineExPrivate::uploadData(unsigned "
        "int arrayIndex, const GLfloat *data, GLuint count)': names "
        "'GLfloat', which has no cute class yet.")

  @staticmethod
  def uploadIndexData(*__, **_) -> Never:
    """
    Qt's 'bool QOpenGL2PaintEngineExPrivate::uploadIndexData(const void
    *data, GLenum indexValueType, GLuint count)': names 'void', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGL2PaintEngineExPrivate.uploadIndexData' has no cute "
        "function yet. Qt's 'bool "
        "QOpenGL2PaintEngineExPrivate::uploadIndexData(const void *data, "
        "GLenum indexValueType, GLuint count)': names 'void', which has no "
        "cute class yet.")

  @staticmethod
  def writeClip(*__, **_) -> Never:
    """
    Qt's 'void QOpenGL2PaintEngineExPrivate::writeClip(const QVectorPath
    &path, uint value)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QOpenGL2PaintEngineExPrivate.writeClip' has no cute function yet. "
        "Qt's 'void QOpenGL2PaintEngineExPrivate::writeClip(const "
        "QVectorPath &path, uint value)': takes a type Python has no way to "
        "hand over yet.")
