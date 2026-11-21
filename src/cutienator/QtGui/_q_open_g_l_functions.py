"""
QOpenGLFunctions binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qopenglfunctions.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QOpenGLContext
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QOpenGLContext = WAIT['QOpenGLContext']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QOpenGLFunctions(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpenGLFunctions: a plain Python object standing in
  front of one C++ QOpenGLFunctions.

  C++ hands a QOpenGLFunctions around as a copy, so every C++
  QOpenGLFunctions behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QOpenGLFunctions that has a ritual and that Python
  can call so far, 73 names in all: 'openGLFeatures', 'hasOpenGLFeature',
  'initializeOpenGLFunctions', 'glBindTexture', 'glBlendFunc', 'glClear',
  'glClearColor', 'glClearStencil', 'glColorMask', 'glCopyTexImage2D',
  'glCopyTexSubImage2D', 'glCullFace', 'glDepthFunc', 'glDepthMask',
  'glDisable', 'glDrawArrays', 'glEnable', 'glFinish', 'glFlush',
  'glFrontFace', 'glHint', 'glLineWidth', 'glPixelStorei', 'glPolygonOffset',
  'glScissor', 'glStencilFunc', 'glStencilMask', 'glStencilOp',
  'glTexParameterf', 'glTexParameteri', 'glViewport', 'glActiveTexture',
  'glAttachShader', 'glBindAttribLocation', 'glBindBuffer',
  'glBindFramebuffer', 'glBindRenderbuffer', 'glBlendColor',
  'glBlendEquation', 'glBlendEquationSeparate', 'glBlendFuncSeparate',
  'glClearDepthf', 'glCompileShader', 'glDeleteProgram', 'glDeleteShader',
  'glDepthRangef', 'glDetachShader', 'glDisableVertexAttribArray',
  'glEnableVertexAttribArray', 'glFramebufferRenderbuffer',
  'glFramebufferTexture2D', 'glGenerateMipmap', 'glLinkProgram',
  'glReleaseShaderCompiler', 'glRenderbufferStorage', 'glSampleCoverage',
  'glStencilFuncSeparate', 'glStencilMaskSeparate', 'glStencilOpSeparate',
  'glUniform1f', 'glUniform1i', 'glUniform2f', 'glUniform2i', 'glUniform3f',
  'glUniform3i', 'glUniform4f', 'glUniform4i', 'glUseProgram',
  'glValidateProgram', 'glVertexAttrib1f', 'glVertexAttrib2f',
  'glVertexAttrib3f', 'glVertexAttrib4f'. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpenGLFunctions::~QOpenGLFunctions()': the destructor: Python
    removes its C++ QOpenGLFunctions by it, and has no other use for it.

  What has no ritual
  ------------------

  73 of the 149 functions Qt declares: 72 takes or gives a type that cannot
  be passed yet; 1 protected.

  What to expect
  --------------

  - The C++ QOpenGLFunctions is created at the first use, not by
    'QOpenGLFunctions(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpenGLFunctions back gives a copy the ritual made
    for Python, in a new cute QOpenGLFunctions.
  """

  #  The enums Qt writes inside QOpenGLFunctions, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class OpenGLFeature(CuteFlags):
    """
    The flags enum 'QOpenGLFunctions::OpenGLFeature' of Qt, with the 18 names
    Qt gives in it. Qt names the type of its combinations
    'QOpenGLFunctions::OpenGLFeatures'.
    """

    Multitexture = 0x1
    Shaders = 0x2
    Buffers = 0x4
    Framebuffers = 0x8
    BlendColor = 0x10
    BlendEquation = 0x20
    BlendEquationSeparate = 0x40
    BlendFuncSeparate = 0x80
    BlendSubtract = 0x100
    CompressedTextures = 0x200
    Multisample = 0x400
    StencilSeparate = 0x800
    NPOTTextures = 0x1000
    NPOTTextureRepeat = 0x2000
    FixedFunctionPipeline = 0x4000
    TextureRGFormats = 0x8000
    MultipleRenderTargets = 0x10000
    BlendEquationAdvanced = 0x20000

  OpenGLFeatures = OpenGLFeature

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpenGLFunctions'

  #  Qt's '~QOpenGLFunctions()'. Naming it makes this a value class: Python
  #  owns every C++ QOpenGLFunctions behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QOpenGLFunctionsD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def openGLFeatures(self) -> OpenGLFeatures:
    """
    Calls Qt's 'QOpenGLFunctions::OpenGLFeatures
    QOpenGLFunctions::openGLFeatures() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions.html#openGLFeatures

    Returns
    -------

    OpenGLFeatures
      The value standing for the combination Qt gave back.
    """
    #  QOpenGLFunctions::OpenGLFeatures QOpenGLFunctions::openGLFeatures()
    #      const
    return QOpenGLFunctions.OpenGLFeatures(self.uglySide.call(
        'ritual_ZNK16QOpenGLFunctions14openGLFeaturesEv',
    ))

  @overload(OpenGLFeature)
  def hasOpenGLFeature(self, feature: OpenGLFeature) -> bool:
    """
    Calls Qt's 'bool
    QOpenGLFunctions::hasOpenGLFeature(QOpenGLFunctions::OpenGLFeature
    feature) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions.html#hasOpenGLFeature

    Parameters
    ----------

    feature : OpenGLFeature
      Passed on as its number.
    """
    #  bool
    #      QOpenGLFunctions::hasOpenGLFeature(QOpenGLFunctions::OpenGLFeature
    #      feature) const
    return self.uglySide.call(
        'ritual_ZNK16QOpenGLFunctions16hasOpenGLFeatureENS_13OpenGLFeatureE',
        feature.value,
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QOpenGLFunctions::QOpenGLFunctions()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions.html#QOpenGLFunctions
    """
    #  QOpenGLFunctions::QOpenGLFunctions()
    self._noteCreation(QOpenGLFunctions, lambda: Rituals.call(
        'ritual_ZN16QOpenGLFunctionsC1Ev',
    ))

  @overload(QOpenGLContext)
  @overload(NoneType)
  def __init__(self, context: Optional[QOpenGLContext]) -> None:
    """
    Notes what was given, for Qt's
    'QOpenGLFunctions::QOpenGLFunctions(QOpenGLContext *context)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions.html#QOpenGLFunctions

    Parameters
    ----------

    context : Optional[QOpenGLContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QOpenGLFunctions::QOpenGLFunctions(QOpenGLContext *context)
    self._noteCreation(QOpenGLFunctions, lambda: Rituals.call(
        'ritual_ZN16QOpenGLFunctionsC1EP14QOpenGLContext',
        self._addressOf(context),
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

  def initializeOpenGLFunctions(self) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions::initializeOpenGLFunctions()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions.html#initializeOpenGLFunctions
    """
    #  void QOpenGLFunctions::initializeOpenGLFunctions()
    self.uglySide.call(
        'ritual_ZN16QOpenGLFunctions25initializeOpenGLFunctionsEv',
    )

  @overload(int, int)
  def glBindTexture(self, target: int, texture: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions::glBindTexture(GLenum target, GLuint
    texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions.html#glBindTexture

    Parameters
    ----------

    target : int
      Passed on as it is.

    texture : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions::glBindTexture(GLenum target, GLuint texture)
    self.uglySide.call(
        'ritual_ZN16QOpenGLFunctions13glBindTextureEjj', target, texture,
    )

  @overload(int, int)
  def glBlendFunc(self, sfactor: int, dfactor: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions::glBlendFunc(GLenum sfactor, GLenum
    dfactor)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions.html#glBlendFunc

    Parameters
    ----------

    sfactor : int
      Passed on as it is.

    dfactor : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions::glBlendFunc(GLenum sfactor, GLenum dfactor)
    self.uglySide.call(
        'ritual_ZN16QOpenGLFunctions11glBlendFuncEjj', sfactor, dfactor,
    )

  @overload(int)
  def glClear(self, mask: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions::glClear(GLbitfield mask)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions.html#glClear

    Parameters
    ----------

    mask : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions::glClear(GLbitfield mask)
    self.uglySide.call('ritual_ZN16QOpenGLFunctions7glClearEj', mask)

  @overload(float, float, float, float)
  def glClearColor(
      self,
      red: float,
      green: float,
      blue: float,
      alpha: float,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions::glClearColor(GLclampf red, GLclampf
    green, GLclampf blue, GLclampf alpha)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions.html#glClearColor

    Parameters
    ----------

    red : float
      Passed on as it is.

    green : float
      Passed on as it is.

    blue : float
      Passed on as it is.

    alpha : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions::glClearColor(GLclampf red, GLclampf green,
    #      GLclampf blue, GLclampf alpha)
    self.uglySide.call(
        'ritual_ZN16QOpenGLFunctions12glClearColorEffff',
        red, green, blue, alpha,
    )

  @overload(int)
  def glClearStencil(self, s: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions::glClearStencil(GLint s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions.html#glClearStencil

    Parameters
    ----------

    s : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions::glClearStencil(GLint s)
    self.uglySide.call('ritual_ZN16QOpenGLFunctions14glClearStencilEi', s)

  @overload(int, int, int, int)
  def glColorMask(self, red: int, green: int, blue: int, alpha: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions::glColorMask(GLboolean red, GLboolean
    green, GLboolean blue, GLboolean alpha)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions.html#glColorMask

    Parameters
    ----------

    red : int
      Passed on as it is.

    green : int
      Passed on as it is.

    blue : int
      Passed on as it is.

    alpha : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions::glColorMask(GLboolean red, GLboolean green,
    #      GLboolean blue, GLboolean alpha)
    self.uglySide.call(
        'ritual_ZN16QOpenGLFunctions11glColorMaskEhhhh',
        red, green, blue, alpha,
    )

  @overload(int, int, int, int, int, int, int, int)
  def glCopyTexImage2D(
      self,
      target: int,
      level: int,
      internalformat: int,
      x: int,
      y: int,
      width: int,
      height: int,
      border: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions::glCopyTexImage2D(GLenum target, GLint
    level, GLenum internalformat, GLint x, GLint y, GLsizei width, GLsizei
    height, GLint border)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions.html#glCopyTexImage2D

    Parameters
    ----------

    target : int
      Passed on as it is.

    level : int
      Passed on as it is.

    internalformat : int
      Passed on as it is.

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    width : int
      Passed on as it is.

    height : int
      Passed on as it is.

    border : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions::glCopyTexImage2D(GLenum target, GLint level,
    #      GLenum internalformat, GLint x, GLint y, GLsizei width, GLsizei
    #      height, GLint border)
    self.uglySide.call(
        'ritual_ZN16QOpenGLFunctions16glCopyTexImage2DEjijiiiii',
        target, level, internalformat, x, y, width, height, border,
    )

  @overload(int, int, int, int, int, int, int, int)
  def glCopyTexSubImage2D(
      self,
      target: int,
      level: int,
      xoffset: int,
      yoffset: int,
      x: int,
      y: int,
      width: int,
      height: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions::glCopyTexSubImage2D(GLenum target,
    GLint level, GLint xoffset, GLint yoffset, GLint x, GLint y, GLsizei
    width, GLsizei height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions.html#glCopyTexSubImage2D

    Parameters
    ----------

    target : int
      Passed on as it is.

    level : int
      Passed on as it is.

    xoffset : int
      Passed on as it is.

    yoffset : int
      Passed on as it is.

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    width : int
      Passed on as it is.

    height : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions::glCopyTexSubImage2D(GLenum target, GLint level,
    #      GLint xoffset, GLint yoffset, GLint x, GLint y, GLsizei width,
    #      GLsizei height)
    self.uglySide.call(
        'ritual_ZN16QOpenGLFunctions19glCopyTexSubImage2DEjiiiiiii',
        target, level, xoffset, yoffset, x, y, width, height,
    )

  @overload(int)
  def glCullFace(self, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions::glCullFace(GLenum mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions.html#glCullFace

    Parameters
    ----------

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions::glCullFace(GLenum mode)
    self.uglySide.call('ritual_ZN16QOpenGLFunctions10glCullFaceEj', mode)

  @overload(int)
  def glDepthFunc(self, func: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions::glDepthFunc(GLenum func)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions.html#glDepthFunc

    Parameters
    ----------

    func : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions::glDepthFunc(GLenum func)
    self.uglySide.call('ritual_ZN16QOpenGLFunctions11glDepthFuncEj', func)

  @overload(int)
  def glDepthMask(self, flag: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions::glDepthMask(GLboolean flag)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions.html#glDepthMask

    Parameters
    ----------

    flag : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions::glDepthMask(GLboolean flag)
    self.uglySide.call('ritual_ZN16QOpenGLFunctions11glDepthMaskEh', flag)

  @overload(int)
  def glDisable(self, cap: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions::glDisable(GLenum cap)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions.html#glDisable

    Parameters
    ----------

    cap : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions::glDisable(GLenum cap)
    self.uglySide.call('ritual_ZN16QOpenGLFunctions9glDisableEj', cap)

  @overload(int, int, int)
  def glDrawArrays(self, mode: int, first: int, count: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions::glDrawArrays(GLenum mode, GLint first,
    GLsizei count)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions.html#glDrawArrays

    Parameters
    ----------

    mode : int
      Passed on as it is.

    first : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions::glDrawArrays(GLenum mode, GLint first, GLsizei
    #      count)
    self.uglySide.call(
        'ritual_ZN16QOpenGLFunctions12glDrawArraysEjii', mode, first, count,
    )

  @overload(int)
  def glEnable(self, cap: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions::glEnable(GLenum cap)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions.html#glEnable

    Parameters
    ----------

    cap : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions::glEnable(GLenum cap)
    self.uglySide.call('ritual_ZN16QOpenGLFunctions8glEnableEj', cap)

  def glFinish(self) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions::glFinish()'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions.html#glFinish
    """
    #  void QOpenGLFunctions::glFinish()
    self.uglySide.call('ritual_ZN16QOpenGLFunctions8glFinishEv')

  def glFlush(self) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions::glFlush()'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions.html#glFlush
    """
    #  void QOpenGLFunctions::glFlush()
    self.uglySide.call('ritual_ZN16QOpenGLFunctions7glFlushEv')

  @overload(int)
  def glFrontFace(self, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions::glFrontFace(GLenum mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions.html#glFrontFace

    Parameters
    ----------

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions::glFrontFace(GLenum mode)
    self.uglySide.call('ritual_ZN16QOpenGLFunctions11glFrontFaceEj', mode)

  @overload(int, int)
  def glHint(self, target: int, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions::glHint(GLenum target, GLenum mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions.html#glHint

    Parameters
    ----------

    target : int
      Passed on as it is.

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions::glHint(GLenum target, GLenum mode)
    self.uglySide.call('ritual_ZN16QOpenGLFunctions6glHintEjj', target, mode)

  @overload(float)
  def glLineWidth(self, width: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions::glLineWidth(GLfloat width)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions.html#glLineWidth

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions::glLineWidth(GLfloat width)
    self.uglySide.call('ritual_ZN16QOpenGLFunctions11glLineWidthEf', width)

  @overload(int, int)
  def glPixelStorei(self, pname: int, param: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions::glPixelStorei(GLenum pname, GLint
    param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions.html#glPixelStorei

    Parameters
    ----------

    pname : int
      Passed on as it is.

    param : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions::glPixelStorei(GLenum pname, GLint param)
    self.uglySide.call(
        'ritual_ZN16QOpenGLFunctions13glPixelStoreiEji', pname, param,
    )

  @overload(float, float)
  def glPolygonOffset(self, factor: float, units: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions::glPolygonOffset(GLfloat factor,
    GLfloat units)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions.html#glPolygonOffset

    Parameters
    ----------

    factor : float
      Passed on as it is.

    units : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions::glPolygonOffset(GLfloat factor, GLfloat units)
    self.uglySide.call(
        'ritual_ZN16QOpenGLFunctions15glPolygonOffsetEff', factor, units,
    )

  @overload(int, int, int, int)
  def glScissor(self, x: int, y: int, width: int, height: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions::glScissor(GLint x, GLint y, GLsizei
    width, GLsizei height)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions.html#glScissor

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    width : int
      Passed on as it is.

    height : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions::glScissor(GLint x, GLint y, GLsizei width,
    #      GLsizei height)
    self.uglySide.call(
        'ritual_ZN16QOpenGLFunctions9glScissorEiiii', x, y, width, height,
    )

  @overload(int, int, int)
  def glStencilFunc(self, func: int, ref: int, mask: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions::glStencilFunc(GLenum func, GLint ref,
    GLuint mask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions.html#glStencilFunc

    Parameters
    ----------

    func : int
      Passed on as it is.

    ref : int
      Passed on as it is.

    mask : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions::glStencilFunc(GLenum func, GLint ref, GLuint
    #      mask)
    self.uglySide.call(
        'ritual_ZN16QOpenGLFunctions13glStencilFuncEjij', func, ref, mask,
    )

  @overload(int)
  def glStencilMask(self, mask: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions::glStencilMask(GLuint mask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions.html#glStencilMask

    Parameters
    ----------

    mask : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions::glStencilMask(GLuint mask)
    self.uglySide.call('ritual_ZN16QOpenGLFunctions13glStencilMaskEj', mask)

  @overload(int, int, int)
  def glStencilOp(self, fail: int, zfail: int, zpass: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions::glStencilOp(GLenum fail, GLenum zfail,
    GLenum zpass)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions.html#glStencilOp

    Parameters
    ----------

    fail : int
      Passed on as it is.

    zfail : int
      Passed on as it is.

    zpass : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions::glStencilOp(GLenum fail, GLenum zfail, GLenum
    #      zpass)
    self.uglySide.call(
        'ritual_ZN16QOpenGLFunctions11glStencilOpEjjj', fail, zfail, zpass,
    )

  @overload(int, int, float)
  def glTexParameterf(self, target: int, pname: int, param: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions::glTexParameterf(GLenum target, GLenum
    pname, GLfloat param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions.html#glTexParameterf

    Parameters
    ----------

    target : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    param : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions::glTexParameterf(GLenum target, GLenum pname,
    #      GLfloat param)
    self.uglySide.call(
        'ritual_ZN16QOpenGLFunctions15glTexParameterfEjjf',
        target, pname, param,
    )

  @overload(int, int, int)
  def glTexParameteri(self, target: int, pname: int, param: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions::glTexParameteri(GLenum target, GLenum
    pname, GLint param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions.html#glTexParameteri

    Parameters
    ----------

    target : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    param : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions::glTexParameteri(GLenum target, GLenum pname,
    #      GLint param)
    self.uglySide.call(
        'ritual_ZN16QOpenGLFunctions15glTexParameteriEjji',
        target, pname, param,
    )

  @overload(int, int, int, int)
  def glViewport(self, x: int, y: int, width: int, height: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions::glViewport(GLint x, GLint y, GLsizei
    width, GLsizei height)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions.html#glViewport

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    width : int
      Passed on as it is.

    height : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions::glViewport(GLint x, GLint y, GLsizei width,
    #      GLsizei height)
    self.uglySide.call(
        'ritual_ZN16QOpenGLFunctions10glViewportEiiii', x, y, width, height,
    )

  @overload(int)
  def glActiveTexture(self, texture: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions::glActiveTexture(GLenum texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions.html#glActiveTexture

    Parameters
    ----------

    texture : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions::glActiveTexture(GLenum texture)
    self.uglySide.call(
        'ritual_ZN16QOpenGLFunctions15glActiveTextureEj', texture,
    )

  @overload(int, int)
  def glAttachShader(self, program: int, shader: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions::glAttachShader(GLuint program, GLuint
    shader)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions.html#glAttachShader

    Parameters
    ----------

    program : int
      Passed on as it is.

    shader : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions::glAttachShader(GLuint program, GLuint shader)
    self.uglySide.call(
        'ritual_ZN16QOpenGLFunctions14glAttachShaderEjj', program, shader,
    )

  @overload(int, int, str)
  @overload(int, int, NoneType)
  def glBindAttribLocation(
      self,
      program: int,
      index: int,
      name: Optional[str],
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions::glBindAttribLocation(GLuint program,
    GLuint index, const char *name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions.html#glBindAttribLocation

    Parameters
    ----------

    program : int
      Passed on as it is.

    index : int
      Passed on as it is.

    name : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  void QOpenGLFunctions::glBindAttribLocation(GLuint program, GLuint
    #      index, const char *name)
    self.uglySide.call(
        'ritual_ZN16QOpenGLFunctions20glBindAttribLocationEjjPKc',
        program, index, self._bytesOf(name),
    )

  @overload(int, int)
  def glBindBuffer(self, target: int, buffer: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions::glBindBuffer(GLenum target, GLuint
    buffer)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions.html#glBindBuffer

    Parameters
    ----------

    target : int
      Passed on as it is.

    buffer : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions::glBindBuffer(GLenum target, GLuint buffer)
    self.uglySide.call(
        'ritual_ZN16QOpenGLFunctions12glBindBufferEjj', target, buffer,
    )

  @overload(int, int)
  def glBindFramebuffer(self, target: int, framebuffer: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions::glBindFramebuffer(GLenum target,
    GLuint framebuffer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions.html#glBindFramebuffer

    Parameters
    ----------

    target : int
      Passed on as it is.

    framebuffer : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions::glBindFramebuffer(GLenum target, GLuint
    #      framebuffer)
    self.uglySide.call(
        'ritual_ZN16QOpenGLFunctions17glBindFramebufferEjj',
        target, framebuffer,
    )

  @overload(int, int)
  def glBindRenderbuffer(self, target: int, renderbuffer: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions::glBindRenderbuffer(GLenum target,
    GLuint renderbuffer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions.html#glBindRenderbuffer

    Parameters
    ----------

    target : int
      Passed on as it is.

    renderbuffer : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions::glBindRenderbuffer(GLenum target, GLuint
    #      renderbuffer)
    self.uglySide.call(
        'ritual_ZN16QOpenGLFunctions18glBindRenderbufferEjj',
        target, renderbuffer,
    )

  @overload(float, float, float, float)
  def glBlendColor(
      self,
      red: float,
      green: float,
      blue: float,
      alpha: float,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions::glBlendColor(GLclampf red, GLclampf
    green, GLclampf blue, GLclampf alpha)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions.html#glBlendColor

    Parameters
    ----------

    red : float
      Passed on as it is.

    green : float
      Passed on as it is.

    blue : float
      Passed on as it is.

    alpha : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions::glBlendColor(GLclampf red, GLclampf green,
    #      GLclampf blue, GLclampf alpha)
    self.uglySide.call(
        'ritual_ZN16QOpenGLFunctions12glBlendColorEffff',
        red, green, blue, alpha,
    )

  @overload(int)
  def glBlendEquation(self, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions::glBlendEquation(GLenum mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions.html#glBlendEquation

    Parameters
    ----------

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions::glBlendEquation(GLenum mode)
    self.uglySide.call(
        'ritual_ZN16QOpenGLFunctions15glBlendEquationEj', mode,
    )

  @overload(int, int)
  def glBlendEquationSeparate(self, modeRGB: int, modeAlpha: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions::glBlendEquationSeparate(GLenum
    modeRGB, GLenum modeAlpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions.html#glBlendEquationSeparate

    Parameters
    ----------

    modeRGB : int
      Passed on as it is.

    modeAlpha : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions::glBlendEquationSeparate(GLenum modeRGB, GLenum
    #      modeAlpha)
    self.uglySide.call(
        'ritual_ZN16QOpenGLFunctions23glBlendEquationSeparateEjj',
        modeRGB, modeAlpha,
    )

  @overload(int, int, int, int)
  def glBlendFuncSeparate(
      self,
      srcRGB: int,
      dstRGB: int,
      srcAlpha: int,
      dstAlpha: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions::glBlendFuncSeparate(GLenum srcRGB,
    GLenum dstRGB, GLenum srcAlpha, GLenum dstAlpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions.html#glBlendFuncSeparate

    Parameters
    ----------

    srcRGB : int
      Passed on as it is.

    dstRGB : int
      Passed on as it is.

    srcAlpha : int
      Passed on as it is.

    dstAlpha : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions::glBlendFuncSeparate(GLenum srcRGB, GLenum
    #      dstRGB, GLenum srcAlpha, GLenum dstAlpha)
    self.uglySide.call(
        'ritual_ZN16QOpenGLFunctions19glBlendFuncSeparateEjjjj',
        srcRGB, dstRGB, srcAlpha, dstAlpha,
    )

  @overload(float)
  def glClearDepthf(self, depth: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions::glClearDepthf(GLclampf depth)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions.html#glClearDepthf

    Parameters
    ----------

    depth : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions::glClearDepthf(GLclampf depth)
    self.uglySide.call('ritual_ZN16QOpenGLFunctions13glClearDepthfEf', depth)

  @overload(int)
  def glCompileShader(self, shader: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions::glCompileShader(GLuint shader)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions.html#glCompileShader

    Parameters
    ----------

    shader : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions::glCompileShader(GLuint shader)
    self.uglySide.call(
        'ritual_ZN16QOpenGLFunctions15glCompileShaderEj', shader,
    )

  @overload(int)
  def glDeleteProgram(self, program: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions::glDeleteProgram(GLuint program)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions.html#glDeleteProgram

    Parameters
    ----------

    program : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions::glDeleteProgram(GLuint program)
    self.uglySide.call(
        'ritual_ZN16QOpenGLFunctions15glDeleteProgramEj', program,
    )

  @overload(int)
  def glDeleteShader(self, shader: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions::glDeleteShader(GLuint shader)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions.html#glDeleteShader

    Parameters
    ----------

    shader : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions::glDeleteShader(GLuint shader)
    self.uglySide.call(
        'ritual_ZN16QOpenGLFunctions14glDeleteShaderEj', shader,
    )

  @overload(float, float)
  def glDepthRangef(self, zNear: float, zFar: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions::glDepthRangef(GLclampf zNear, GLclampf
    zFar)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions.html#glDepthRangef

    Parameters
    ----------

    zNear : float
      Passed on as it is.

    zFar : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions::glDepthRangef(GLclampf zNear, GLclampf zFar)
    self.uglySide.call(
        'ritual_ZN16QOpenGLFunctions13glDepthRangefEff', zNear, zFar,
    )

  @overload(int, int)
  def glDetachShader(self, program: int, shader: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions::glDetachShader(GLuint program, GLuint
    shader)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions.html#glDetachShader

    Parameters
    ----------

    program : int
      Passed on as it is.

    shader : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions::glDetachShader(GLuint program, GLuint shader)
    self.uglySide.call(
        'ritual_ZN16QOpenGLFunctions14glDetachShaderEjj', program, shader,
    )

  @overload(int)
  def glDisableVertexAttribArray(self, index: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions::glDisableVertexAttribArray(GLuint
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions.html#glDisableVertexAttribArray

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions::glDisableVertexAttribArray(GLuint index)
    self.uglySide.call(
        'ritual_ZN16QOpenGLFunctions26glDisableVertexAttribArrayEj', index,
    )

  @overload(int)
  def glEnableVertexAttribArray(self, index: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions::glEnableVertexAttribArray(GLuint
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions.html#glEnableVertexAttribArray

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions::glEnableVertexAttribArray(GLuint index)
    self.uglySide.call(
        'ritual_ZN16QOpenGLFunctions25glEnableVertexAttribArrayEj', index,
    )

  @overload(int, int, int, int)
  def glFramebufferRenderbuffer(
      self,
      target: int,
      attachment: int,
      renderbuffertarget: int,
      renderbuffer: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions::glFramebufferRenderbuffer(GLenum
    target, GLenum attachment, GLenum renderbuffertarget, GLuint
    renderbuffer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions.html#glFramebufferRenderbuffer

    Parameters
    ----------

    target : int
      Passed on as it is.

    attachment : int
      Passed on as it is.

    renderbuffertarget : int
      Passed on as it is.

    renderbuffer : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions::glFramebufferRenderbuffer(GLenum target, GLenum
    #      attachment, GLenum renderbuffertarget, GLuint renderbuffer)
    self.uglySide.call(
        'ritual_ZN16QOpenGLFunctions25glFramebufferRenderbufferEjjjj',
        target, attachment, renderbuffertarget, renderbuffer,
    )

  @overload(int, int, int, int, int)
  def glFramebufferTexture2D(
      self,
      target: int,
      attachment: int,
      textarget: int,
      texture: int,
      level: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions::glFramebufferTexture2D(GLenum target,
    GLenum attachment, GLenum textarget, GLuint texture, GLint level)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions.html#glFramebufferTexture2D

    Parameters
    ----------

    target : int
      Passed on as it is.

    attachment : int
      Passed on as it is.

    textarget : int
      Passed on as it is.

    texture : int
      Passed on as it is.

    level : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions::glFramebufferTexture2D(GLenum target, GLenum
    #      attachment, GLenum textarget, GLuint texture, GLint level)
    self.uglySide.call(
        'ritual_ZN16QOpenGLFunctions22glFramebufferTexture2DEjjjji',
        target, attachment, textarget, texture, level,
    )

  @overload(int)
  def glGenerateMipmap(self, target: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions::glGenerateMipmap(GLenum target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions.html#glGenerateMipmap

    Parameters
    ----------

    target : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions::glGenerateMipmap(GLenum target)
    self.uglySide.call(
        'ritual_ZN16QOpenGLFunctions16glGenerateMipmapEj', target,
    )

  @overload(int)
  def glLinkProgram(self, program: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions::glLinkProgram(GLuint program)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions.html#glLinkProgram

    Parameters
    ----------

    program : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions::glLinkProgram(GLuint program)
    self.uglySide.call(
        'ritual_ZN16QOpenGLFunctions13glLinkProgramEj', program,
    )

  def glReleaseShaderCompiler(self) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions::glReleaseShaderCompiler()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions.html#glReleaseShaderCompiler
    """
    #  void QOpenGLFunctions::glReleaseShaderCompiler()
    self.uglySide.call(
        'ritual_ZN16QOpenGLFunctions23glReleaseShaderCompilerEv',
    )

  @overload(int, int, int, int)
  def glRenderbufferStorage(
      self,
      target: int,
      internalformat: int,
      width: int,
      height: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions::glRenderbufferStorage(GLenum target,
    GLenum internalformat, GLsizei width, GLsizei height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions.html#glRenderbufferStorage

    Parameters
    ----------

    target : int
      Passed on as it is.

    internalformat : int
      Passed on as it is.

    width : int
      Passed on as it is.

    height : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions::glRenderbufferStorage(GLenum target, GLenum
    #      internalformat, GLsizei width, GLsizei height)
    self.uglySide.call(
        'ritual_ZN16QOpenGLFunctions21glRenderbufferStorageEjjii',
        target, internalformat, width, height,
    )

  @overload(float, int)
  def glSampleCoverage(self, value: float, invert: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions::glSampleCoverage(GLclampf value,
    GLboolean invert)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions.html#glSampleCoverage

    Parameters
    ----------

    value : float
      Passed on as it is.

    invert : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions::glSampleCoverage(GLclampf value, GLboolean
    #      invert)
    self.uglySide.call(
        'ritual_ZN16QOpenGLFunctions16glSampleCoverageEfh', value, invert,
    )

  @overload(int, int, int, int)
  def glStencilFuncSeparate(
      self,
      face: int,
      func: int,
      ref: int,
      mask: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions::glStencilFuncSeparate(GLenum face,
    GLenum func, GLint ref, GLuint mask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions.html#glStencilFuncSeparate

    Parameters
    ----------

    face : int
      Passed on as it is.

    func : int
      Passed on as it is.

    ref : int
      Passed on as it is.

    mask : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions::glStencilFuncSeparate(GLenum face, GLenum func,
    #      GLint ref, GLuint mask)
    self.uglySide.call(
        'ritual_ZN16QOpenGLFunctions21glStencilFuncSeparateEjjij',
        face, func, ref, mask,
    )

  @overload(int, int)
  def glStencilMaskSeparate(self, face: int, mask: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions::glStencilMaskSeparate(GLenum face,
    GLuint mask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions.html#glStencilMaskSeparate

    Parameters
    ----------

    face : int
      Passed on as it is.

    mask : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions::glStencilMaskSeparate(GLenum face, GLuint mask)
    self.uglySide.call(
        'ritual_ZN16QOpenGLFunctions21glStencilMaskSeparateEjj', face, mask,
    )

  @overload(int, int, int, int)
  def glStencilOpSeparate(
      self,
      face: int,
      fail: int,
      zfail: int,
      zpass: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions::glStencilOpSeparate(GLenum face,
    GLenum fail, GLenum zfail, GLenum zpass)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions.html#glStencilOpSeparate

    Parameters
    ----------

    face : int
      Passed on as it is.

    fail : int
      Passed on as it is.

    zfail : int
      Passed on as it is.

    zpass : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions::glStencilOpSeparate(GLenum face, GLenum fail,
    #      GLenum zfail, GLenum zpass)
    self.uglySide.call(
        'ritual_ZN16QOpenGLFunctions19glStencilOpSeparateEjjjj',
        face, fail, zfail, zpass,
    )

  @overload(int, float)
  def glUniform1f(self, location: int, x: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions::glUniform1f(GLint location, GLfloat
    x)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions.html#glUniform1f

    Parameters
    ----------

    location : int
      Passed on as it is.

    x : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions::glUniform1f(GLint location, GLfloat x)
    self.uglySide.call(
        'ritual_ZN16QOpenGLFunctions11glUniform1fEif', location, x,
    )

  @overload(int, int)
  def glUniform1i(self, location: int, x: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions::glUniform1i(GLint location, GLint x)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions.html#glUniform1i

    Parameters
    ----------

    location : int
      Passed on as it is.

    x : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions::glUniform1i(GLint location, GLint x)
    self.uglySide.call(
        'ritual_ZN16QOpenGLFunctions11glUniform1iEii', location, x,
    )

  @overload(int, float, float)
  def glUniform2f(self, location: int, x: float, y: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions::glUniform2f(GLint location, GLfloat x,
    GLfloat y)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions.html#glUniform2f

    Parameters
    ----------

    location : int
      Passed on as it is.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions::glUniform2f(GLint location, GLfloat x, GLfloat
    #      y)
    self.uglySide.call(
        'ritual_ZN16QOpenGLFunctions11glUniform2fEiff', location, x, y,
    )

  @overload(int, int, int)
  def glUniform2i(self, location: int, x: int, y: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions::glUniform2i(GLint location, GLint x,
    GLint y)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions.html#glUniform2i

    Parameters
    ----------

    location : int
      Passed on as it is.

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions::glUniform2i(GLint location, GLint x, GLint y)
    self.uglySide.call(
        'ritual_ZN16QOpenGLFunctions11glUniform2iEiii', location, x, y,
    )

  @overload(int, float, float, float)
  def glUniform3f(self, location: int, x: float, y: float, z: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions::glUniform3f(GLint location, GLfloat x,
    GLfloat y, GLfloat z)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions.html#glUniform3f

    Parameters
    ----------

    location : int
      Passed on as it is.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions::glUniform3f(GLint location, GLfloat x, GLfloat
    #      y, GLfloat z)
    self.uglySide.call(
        'ritual_ZN16QOpenGLFunctions11glUniform3fEifff', location, x, y, z,
    )

  @overload(int, int, int, int)
  def glUniform3i(self, location: int, x: int, y: int, z: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions::glUniform3i(GLint location, GLint x,
    GLint y, GLint z)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions.html#glUniform3i

    Parameters
    ----------

    location : int
      Passed on as it is.

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    z : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions::glUniform3i(GLint location, GLint x, GLint y,
    #      GLint z)
    self.uglySide.call(
        'ritual_ZN16QOpenGLFunctions11glUniform3iEiiii', location, x, y, z,
    )

  @overload(int, float, float, float, float)
  def glUniform4f(
      self,
      location: int,
      x: float,
      y: float,
      z: float,
      w: float,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions::glUniform4f(GLint location, GLfloat x,
    GLfloat y, GLfloat z, GLfloat w)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions.html#glUniform4f

    Parameters
    ----------

    location : int
      Passed on as it is.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.

    w : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions::glUniform4f(GLint location, GLfloat x, GLfloat
    #      y, GLfloat z, GLfloat w)
    self.uglySide.call(
        'ritual_ZN16QOpenGLFunctions11glUniform4fEiffff',
        location, x, y, z, w,
    )

  @overload(int, int, int, int, int)
  def glUniform4i(
      self,
      location: int,
      x: int,
      y: int,
      z: int,
      w: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions::glUniform4i(GLint location, GLint x,
    GLint y, GLint z, GLint w)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions.html#glUniform4i

    Parameters
    ----------

    location : int
      Passed on as it is.

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    z : int
      Passed on as it is.

    w : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions::glUniform4i(GLint location, GLint x, GLint y,
    #      GLint z, GLint w)
    self.uglySide.call(
        'ritual_ZN16QOpenGLFunctions11glUniform4iEiiiii',
        location, x, y, z, w,
    )

  @overload(int)
  def glUseProgram(self, program: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions::glUseProgram(GLuint program)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions.html#glUseProgram

    Parameters
    ----------

    program : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions::glUseProgram(GLuint program)
    self.uglySide.call(
        'ritual_ZN16QOpenGLFunctions12glUseProgramEj', program,
    )

  @overload(int)
  def glValidateProgram(self, program: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions::glValidateProgram(GLuint program)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions.html#glValidateProgram

    Parameters
    ----------

    program : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions::glValidateProgram(GLuint program)
    self.uglySide.call(
        'ritual_ZN16QOpenGLFunctions17glValidateProgramEj', program,
    )

  @overload(int, float)
  def glVertexAttrib1f(self, indx: int, x: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions::glVertexAttrib1f(GLuint indx, GLfloat
    x)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions.html#glVertexAttrib1f

    Parameters
    ----------

    indx : int
      Passed on as it is.

    x : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions::glVertexAttrib1f(GLuint indx, GLfloat x)
    self.uglySide.call(
        'ritual_ZN16QOpenGLFunctions16glVertexAttrib1fEjf', indx, x,
    )

  @overload(int, float, float)
  def glVertexAttrib2f(self, indx: int, x: float, y: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions::glVertexAttrib2f(GLuint indx, GLfloat
    x, GLfloat y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions.html#glVertexAttrib2f

    Parameters
    ----------

    indx : int
      Passed on as it is.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions::glVertexAttrib2f(GLuint indx, GLfloat x,
    #      GLfloat y)
    self.uglySide.call(
        'ritual_ZN16QOpenGLFunctions16glVertexAttrib2fEjff', indx, x, y,
    )

  @overload(int, float, float, float)
  def glVertexAttrib3f(
      self,
      indx: int,
      x: float,
      y: float,
      z: float,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions::glVertexAttrib3f(GLuint indx, GLfloat
    x, GLfloat y, GLfloat z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions.html#glVertexAttrib3f

    Parameters
    ----------

    indx : int
      Passed on as it is.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions::glVertexAttrib3f(GLuint indx, GLfloat x,
    #      GLfloat y, GLfloat z)
    self.uglySide.call(
        'ritual_ZN16QOpenGLFunctions16glVertexAttrib3fEjfff', indx, x, y, z,
    )

  @overload(int, float, float, float, float)
  def glVertexAttrib4f(
      self,
      indx: int,
      x: float,
      y: float,
      z: float,
      w: float,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions::glVertexAttrib4f(GLuint indx, GLfloat
    x, GLfloat y, GLfloat z, GLfloat w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions.html#glVertexAttrib4f

    Parameters
    ----------

    indx : int
      Passed on as it is.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.

    w : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions::glVertexAttrib4f(GLuint indx, GLfloat x,
    #      GLfloat y, GLfloat z, GLfloat w)
    self.uglySide.call(
        'ritual_ZN16QOpenGLFunctions16glVertexAttrib4fEjffff',
        indx, x, y, z, w,
    )
