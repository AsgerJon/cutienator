"""
QOpenGLExtraFunctions binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qopenglextrafunctions.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QOpenGLFunctions

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QOpenGLContext, QOpenGLExtraFunctionsPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QOpenGLContext = WAIT['QOpenGLContext']
  QOpenGLExtraFunctionsPrivate = WAIT['QOpenGLExtraFunctionsPrivate']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QOpenGLExtraFunctions(QOpenGLFunctions):
  """
  The cute side of Qt's QOpenGLExtraFunctions: a plain Python object standing
  in front of one C++ QOpenGLExtraFunctions.

  It is built on the cute 'QOpenGLFunctions', as Qt's QOpenGLExtraFunctions
  is built on Qt's QOpenGLFunctions, and has everything that class has.

  C++ hands a QOpenGLExtraFunctions around as a copy, so every C++
  QOpenGLExtraFunctions behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QOpenGLExtraFunctions that has a ritual and that
  Python can call so far, 75 names in all: 'd_func', 'glReadBuffer',
  'glCopyTexSubImage3D', 'glBeginQuery', 'glEndQuery', 'glBlitFramebuffer',
  'glRenderbufferStorageMultisample', 'glFramebufferTextureLayer',
  'glBindVertexArray', 'glBeginTransformFeedback', 'glEndTransformFeedback',
  'glBindBufferBase', 'glVertexAttribI4i', 'glVertexAttribI4ui',
  'glUniform1ui', 'glUniform2ui', 'glUniform3ui', 'glUniform4ui',
  'glClearBufferfi', 'glUniformBlockBinding', 'glDrawArraysInstanced',
  'glBindSampler', 'glSamplerParameteri', 'glSamplerParameterf',
  'glVertexAttribDivisor', 'glBindTransformFeedback',
  'glPauseTransformFeedback', 'glResumeTransformFeedback',
  'glProgramParameteri', 'glTexStorage2D', 'glTexStorage3D',
  'glDispatchCompute', 'glFramebufferParameteri', 'glUseProgramStages',
  'glActiveShaderProgram', 'glBindProgramPipeline', 'glProgramUniform1i',
  'glProgramUniform2i', 'glProgramUniform3i', 'glProgramUniform4i',
  'glProgramUniform1ui', 'glProgramUniform2ui', 'glProgramUniform3ui',
  'glProgramUniform4ui', 'glProgramUniform1f', 'glProgramUniform2f',
  'glProgramUniform3f', 'glProgramUniform4f', 'glValidateProgramPipeline',
  'glBindImageTexture', 'glMemoryBarrier', 'glMemoryBarrierByRegion',
  'glTexStorage2DMultisample', 'glSampleMaski', 'glVertexAttribFormat',
  'glVertexAttribIFormat', 'glVertexAttribBinding', 'glVertexBindingDivisor',
  'glBlendBarrier', 'glCopyImageSubData', 'glPopDebugGroup', 'glEnablei',
  'glDisablei', 'glBlendEquationi', 'glBlendEquationSeparatei',
  'glBlendFunci', 'glBlendFuncSeparatei', 'glColorMaski',
  'glFramebufferTexture', 'glPrimitiveBoundingBox', 'glMinSampleShading',
  'glPatchParameteri', 'glTexBuffer', 'glTexStorage3DMultisample',
  'isInitialized'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QOpenGLExtraFunctionsPrivate *QOpenGLExtraFunctions::d_func()
    const': takes in Python what 'QOpenGLExtraFunctionsPrivate
    *QOpenGLExtraFunctions::d_func()' takes.
  - Qt's 'QOpenGLExtraFunctions::~QOpenGLExtraFunctions()': the destructor:
    Python removes its C++ QOpenGLExtraFunctions by it, and has no other use
    for it.

  What has no ritual
  ------------------

  143 of the 222 functions Qt declares: 137 takes or gives a type that cannot
  be passed yet; 6 takes or gives a number that is not equally wide on every
  system.

  What to expect
  --------------

  - The C++ QOpenGLExtraFunctions is created at the first use, not by
    'QOpenGLExtraFunctions(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpenGLExtraFunctions back gives a copy the ritual
    made for Python, in a new cute QOpenGLExtraFunctions.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QOpenGLExtraFunctionsPrivate)
  @overload(NoneType)
  def isInitialized(d: Optional[QOpenGLExtraFunctionsPrivate]) -> bool:
    """
    Calls Qt's 'bool QOpenGLExtraFunctions::isInitialized(const
    QOpenGLExtraFunctionsPrivate *d)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html#isInitialized

    Parameters
    ----------

    d : Optional[QOpenGLExtraFunctionsPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QOpenGLExtraFunctions::isInitialized(const
    #      QOpenGLExtraFunctionsPrivate *d)
    return Rituals.call(
        'ritual_ZN21QOpenGLExtraFunctions13isInitializedEPK28QOpenGLExtraFu'
        'nctionsPrivate',
        CuteMixin._addressOf(d),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpenGLExtraFunctions'

  #  Qt's '~QOpenGLExtraFunctions()'. Naming it makes this a value class:
  #  Python owns every C++ QOpenGLExtraFunctions behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN21QOpenGLExtraFunctionsD1Ev'

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
    'QOpenGLExtraFunctions::QOpenGLExtraFunctions()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html#QOpenGLExtraFunctions
    """
    #  QOpenGLExtraFunctions::QOpenGLExtraFunctions()
    self._noteCreation(QOpenGLExtraFunctions, lambda: Rituals.call(
        'ritual_ZN21QOpenGLExtraFunctionsC1Ev',
    ))

  @overload(QOpenGLContext)
  @overload(NoneType)
  def __init__(self, context: Optional[QOpenGLContext]) -> None:
    """
    Notes what was given, for Qt's
    'QOpenGLExtraFunctions::QOpenGLExtraFunctions(QOpenGLContext *context)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html#QOpenGLExtraFunctions

    Parameters
    ----------

    context : Optional[QOpenGLContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QOpenGLExtraFunctions::QOpenGLExtraFunctions(QOpenGLContext *context)
    self._noteCreation(QOpenGLExtraFunctions, lambda: Rituals.call(
        'ritual_ZN21QOpenGLExtraFunctionsC1EP14QOpenGLContext',
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

  def d_func(self) -> Optional[QOpenGLExtraFunctionsPrivate]:
    """
    Calls Qt's 'QOpenGLExtraFunctionsPrivate
    *QOpenGLExtraFunctions::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglextrafunctions.html#d_func

    Returns
    -------

    Optional[QOpenGLExtraFunctionsPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOpenGLExtraFunctionsPrivate *QOpenGLExtraFunctions::d_func()
    address = self.uglySide.call('ritual_ZN21QOpenGLExtraFunctions6d_funcEv')
    from . import QOpenGLExtraFunctionsPrivate
    return QOpenGLExtraFunctionsPrivate._cuteAt(address)

  @overload(int)
  def glReadBuffer(self, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLExtraFunctions::glReadBuffer(GLenum mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html#glReadBuffer

    Parameters
    ----------

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLExtraFunctions::glReadBuffer(GLenum mode)
    self.uglySide.call(
        'ritual_ZN21QOpenGLExtraFunctions12glReadBufferEj', mode,
    )

  @overload(int, int, int, int, int, int, int, int, int)
  def glCopyTexSubImage3D(
      self,
      target: int,
      level: int,
      xoffset: int,
      yoffset: int,
      zoffset: int,
      x: int,
      y: int,
      width: int,
      height: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLExtraFunctions::glCopyTexSubImage3D(GLenum
    target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLint
    x, GLint y, GLsizei width, GLsizei height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html#glCopyTexSubImage3D

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

    zoffset : int
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
    #  void QOpenGLExtraFunctions::glCopyTexSubImage3D(GLenum target, GLint
    #      level, GLint xoffset, GLint yoffset, GLint zoffset, GLint x, GLint
    #      y, GLsizei width, GLsizei height)
    self.uglySide.call(
        'ritual_ZN21QOpenGLExtraFunctions19glCopyTexSubImage3DEjiiiiiiii',
        target, level, xoffset, yoffset, zoffset, x, y, width, height,
    )

  @overload(int, int)
  def glBeginQuery(self, target: int, id: int) -> None:
    """
    Calls Qt's 'void QOpenGLExtraFunctions::glBeginQuery(GLenum target,
    GLuint id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html#glBeginQuery

    Parameters
    ----------

    target : int
      Passed on as it is.

    id : int
      Passed on as it is.
    """
    #  void QOpenGLExtraFunctions::glBeginQuery(GLenum target, GLuint id)
    self.uglySide.call(
        'ritual_ZN21QOpenGLExtraFunctions12glBeginQueryEjj', target, id,
    )

  @overload(int)
  def glEndQuery(self, target: int) -> None:
    """
    Calls Qt's 'void QOpenGLExtraFunctions::glEndQuery(GLenum target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html#glEndQuery

    Parameters
    ----------

    target : int
      Passed on as it is.
    """
    #  void QOpenGLExtraFunctions::glEndQuery(GLenum target)
    self.uglySide.call(
        'ritual_ZN21QOpenGLExtraFunctions10glEndQueryEj', target,
    )

  @overload(int, int, int, int, int, int, int, int, int, int)
  def glBlitFramebuffer(
      self,
      srcX0: int,
      srcY0: int,
      srcX1: int,
      srcY1: int,
      dstX0: int,
      dstY0: int,
      dstX1: int,
      dstY1: int,
      mask: int,
      filter: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLExtraFunctions::glBlitFramebuffer(GLint srcX0,
    GLint srcY0, GLint srcX1, GLint srcY1, GLint dstX0, GLint dstY0, GLint
    dstX1, GLint dstY1, GLbitfield mask, GLenum filter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html#glBlitFramebuffer

    Parameters
    ----------

    srcX0 : int
      Passed on as it is.

    srcY0 : int
      Passed on as it is.

    srcX1 : int
      Passed on as it is.

    srcY1 : int
      Passed on as it is.

    dstX0 : int
      Passed on as it is.

    dstY0 : int
      Passed on as it is.

    dstX1 : int
      Passed on as it is.

    dstY1 : int
      Passed on as it is.

    mask : int
      Passed on as it is.

    filter : int
      Passed on as it is.
    """
    #  void QOpenGLExtraFunctions::glBlitFramebuffer(GLint srcX0, GLint
    #      srcY0, GLint srcX1, GLint srcY1, GLint dstX0, GLint dstY0, GLint
    #      dstX1, GLint dstY1, GLbitfield mask, GLenum filter)
    self.uglySide.call(
        'ritual_ZN21QOpenGLExtraFunctions17glBlitFramebufferEiiiiiiiijj',
        srcX0, srcY0, srcX1, srcY1, dstX0, dstY0, dstX1, dstY1, mask, filter,
    )

  @overload(int, int, int, int, int)
  def glRenderbufferStorageMultisample(
      self,
      target: int,
      samples: int,
      internalformat: int,
      width: int,
      height: int,
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLExtraFunctions::glRenderbufferStorageMultisample(GLenum target,
    GLsizei samples, GLenum internalformat, GLsizei width, GLsizei height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html

    Parameters
    ----------

    target : int
      Passed on as it is.

    samples : int
      Passed on as it is.

    internalformat : int
      Passed on as it is.

    width : int
      Passed on as it is.

    height : int
      Passed on as it is.
    """
    #  void QOpenGLExtraFunctions::glRenderbufferStorageMultisample(GLenum
    #      target, GLsizei samples, GLenum internalformat, GLsizei width,
    #      GLsizei height)
    self.uglySide.call(
        'ritual_ZN21QOpenGLExtraFunctions32glRenderbufferStorageMultisample'
        'Ejijii',
        target, samples, internalformat, width, height,
    )

  @overload(int, int, int, int, int)
  def glFramebufferTextureLayer(
      self,
      target: int,
      attachment: int,
      texture: int,
      level: int,
      layer: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLExtraFunctions::glFramebufferTextureLayer(GLenum
    target, GLenum attachment, GLuint texture, GLint level, GLint layer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html

    Parameters
    ----------

    target : int
      Passed on as it is.

    attachment : int
      Passed on as it is.

    texture : int
      Passed on as it is.

    level : int
      Passed on as it is.

    layer : int
      Passed on as it is.
    """
    #  void QOpenGLExtraFunctions::glFramebufferTextureLayer(GLenum target,
    #      GLenum attachment, GLuint texture, GLint level, GLint layer)
    self.uglySide.call(
        'ritual_ZN21QOpenGLExtraFunctions25glFramebufferTextureLayerEjjjii',
        target, attachment, texture, level, layer,
    )

  @overload(int)
  def glBindVertexArray(self, array: int) -> None:
    """
    Calls Qt's 'void QOpenGLExtraFunctions::glBindVertexArray(GLuint array)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html#glBindVertexArray

    Parameters
    ----------

    array : int
      Passed on as it is.
    """
    #  void QOpenGLExtraFunctions::glBindVertexArray(GLuint array)
    self.uglySide.call(
        'ritual_ZN21QOpenGLExtraFunctions17glBindVertexArrayEj', array,
    )

  @overload(int)
  def glBeginTransformFeedback(self, primitiveMode: int) -> None:
    """
    Calls Qt's 'void QOpenGLExtraFunctions::glBeginTransformFeedback(GLenum
    primitiveMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html

    Parameters
    ----------

    primitiveMode : int
      Passed on as it is.
    """
    #  void QOpenGLExtraFunctions::glBeginTransformFeedback(GLenum
    #      primitiveMode)
    self.uglySide.call(
        'ritual_ZN21QOpenGLExtraFunctions24glBeginTransformFeedbackEj',
        primitiveMode,
    )

  def glEndTransformFeedback(self) -> None:
    """
    Calls Qt's 'void QOpenGLExtraFunctions::glEndTransformFeedback()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html#glEndTransformFeedback
    """
    #  void QOpenGLExtraFunctions::glEndTransformFeedback()
    self.uglySide.call(
        'ritual_ZN21QOpenGLExtraFunctions22glEndTransformFeedbackEv',
    )

  @overload(int, int, int)
  def glBindBufferBase(self, target: int, index: int, buffer: int) -> None:
    """
    Calls Qt's 'void QOpenGLExtraFunctions::glBindBufferBase(GLenum target,
    GLuint index, GLuint buffer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html#glBindBufferBase

    Parameters
    ----------

    target : int
      Passed on as it is.

    index : int
      Passed on as it is.

    buffer : int
      Passed on as it is.
    """
    #  void QOpenGLExtraFunctions::glBindBufferBase(GLenum target, GLuint
    #      index, GLuint buffer)
    self.uglySide.call(
        'ritual_ZN21QOpenGLExtraFunctions16glBindBufferBaseEjjj',
        target, index, buffer,
    )

  @overload(int, int, int, int, int)
  def glVertexAttribI4i(
      self,
      index: int,
      x: int,
      y: int,
      z: int,
      w: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLExtraFunctions::glVertexAttribI4i(GLuint index,
    GLint x, GLint y, GLint z, GLint w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html#glVertexAttribI4i

    Parameters
    ----------

    index : int
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
    #  void QOpenGLExtraFunctions::glVertexAttribI4i(GLuint index, GLint x,
    #      GLint y, GLint z, GLint w)
    self.uglySide.call(
        'ritual_ZN21QOpenGLExtraFunctions17glVertexAttribI4iEjiiii',
        index, x, y, z, w,
    )

  @overload(int, int, int, int, int)
  def glVertexAttribI4ui(
      self,
      index: int,
      x: int,
      y: int,
      z: int,
      w: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLExtraFunctions::glVertexAttribI4ui(GLuint index,
    GLuint x, GLuint y, GLuint z, GLuint w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html#glVertexAttribI4ui

    Parameters
    ----------

    index : int
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
    #  void QOpenGLExtraFunctions::glVertexAttribI4ui(GLuint index, GLuint x,
    #      GLuint y, GLuint z, GLuint w)
    self.uglySide.call(
        'ritual_ZN21QOpenGLExtraFunctions18glVertexAttribI4uiEjjjjj',
        index, x, y, z, w,
    )

  @overload(int, int)
  def glUniform1ui(self, location: int, v0: int) -> None:
    """
    Calls Qt's 'void QOpenGLExtraFunctions::glUniform1ui(GLint location,
    GLuint v0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html#glUniform1ui

    Parameters
    ----------

    location : int
      Passed on as it is.

    v0 : int
      Passed on as it is.
    """
    #  void QOpenGLExtraFunctions::glUniform1ui(GLint location, GLuint v0)
    self.uglySide.call(
        'ritual_ZN21QOpenGLExtraFunctions12glUniform1uiEij', location, v0,
    )

  @overload(int, int, int)
  def glUniform2ui(self, location: int, v0: int, v1: int) -> None:
    """
    Calls Qt's 'void QOpenGLExtraFunctions::glUniform2ui(GLint location,
    GLuint v0, GLuint v1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html#glUniform2ui

    Parameters
    ----------

    location : int
      Passed on as it is.

    v0 : int
      Passed on as it is.

    v1 : int
      Passed on as it is.
    """
    #  void QOpenGLExtraFunctions::glUniform2ui(GLint location, GLuint v0,
    #      GLuint v1)
    self.uglySide.call(
        'ritual_ZN21QOpenGLExtraFunctions12glUniform2uiEijj',
        location, v0, v1,
    )

  @overload(int, int, int, int)
  def glUniform3ui(self, location: int, v0: int, v1: int, v2: int) -> None:
    """
    Calls Qt's 'void QOpenGLExtraFunctions::glUniform3ui(GLint location,
    GLuint v0, GLuint v1, GLuint v2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html#glUniform3ui

    Parameters
    ----------

    location : int
      Passed on as it is.

    v0 : int
      Passed on as it is.

    v1 : int
      Passed on as it is.

    v2 : int
      Passed on as it is.
    """
    #  void QOpenGLExtraFunctions::glUniform3ui(GLint location, GLuint v0,
    #      GLuint v1, GLuint v2)
    self.uglySide.call(
        'ritual_ZN21QOpenGLExtraFunctions12glUniform3uiEijjj',
        location, v0, v1, v2,
    )

  @overload(int, int, int, int, int)
  def glUniform4ui(
      self,
      location: int,
      v0: int,
      v1: int,
      v2: int,
      v3: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLExtraFunctions::glUniform4ui(GLint location,
    GLuint v0, GLuint v1, GLuint v2, GLuint v3)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html#glUniform4ui

    Parameters
    ----------

    location : int
      Passed on as it is.

    v0 : int
      Passed on as it is.

    v1 : int
      Passed on as it is.

    v2 : int
      Passed on as it is.

    v3 : int
      Passed on as it is.
    """
    #  void QOpenGLExtraFunctions::glUniform4ui(GLint location, GLuint v0,
    #      GLuint v1, GLuint v2, GLuint v3)
    self.uglySide.call(
        'ritual_ZN21QOpenGLExtraFunctions12glUniform4uiEijjjj',
        location, v0, v1, v2, v3,
    )

  @overload(int, int, float, int)
  def glClearBufferfi(
      self,
      buffer: int,
      drawbuffer: int,
      depth: float,
      stencil: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLExtraFunctions::glClearBufferfi(GLenum buffer,
    GLint drawbuffer, GLfloat depth, GLint stencil)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html#glClearBufferfi

    Parameters
    ----------

    buffer : int
      Passed on as it is.

    drawbuffer : int
      Passed on as it is.

    depth : float
      Passed on as it is.

    stencil : int
      Passed on as it is.
    """
    #  void QOpenGLExtraFunctions::glClearBufferfi(GLenum buffer, GLint
    #      drawbuffer, GLfloat depth, GLint stencil)
    self.uglySide.call(
        'ritual_ZN21QOpenGLExtraFunctions15glClearBufferfiEjifi',
        buffer, drawbuffer, depth, stencil,
    )

  @overload(int, int, int)
  def glUniformBlockBinding(
      self,
      program: int,
      uniformBlockIndex: int,
      uniformBlockBinding: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLExtraFunctions::glUniformBlockBinding(GLuint
    program, GLuint uniformBlockIndex, GLuint uniformBlockBinding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html#glUniformBlockBinding

    Parameters
    ----------

    program : int
      Passed on as it is.

    uniformBlockIndex : int
      Passed on as it is.

    uniformBlockBinding : int
      Passed on as it is.
    """
    #  void QOpenGLExtraFunctions::glUniformBlockBinding(GLuint program,
    #      GLuint uniformBlockIndex, GLuint uniformBlockBinding)
    self.uglySide.call(
        'ritual_ZN21QOpenGLExtraFunctions21glUniformBlockBindingEjjj',
        program, uniformBlockIndex, uniformBlockBinding,
    )

  @overload(int, int, int, int)
  def glDrawArraysInstanced(
      self,
      mode: int,
      first: int,
      count: int,
      instancecount: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLExtraFunctions::glDrawArraysInstanced(GLenum
    mode, GLint first, GLsizei count, GLsizei instancecount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html#glDrawArraysInstanced

    Parameters
    ----------

    mode : int
      Passed on as it is.

    first : int
      Passed on as it is.

    count : int
      Passed on as it is.

    instancecount : int
      Passed on as it is.
    """
    #  void QOpenGLExtraFunctions::glDrawArraysInstanced(GLenum mode, GLint
    #      first, GLsizei count, GLsizei instancecount)
    self.uglySide.call(
        'ritual_ZN21QOpenGLExtraFunctions21glDrawArraysInstancedEjiii',
        mode, first, count, instancecount,
    )

  @overload(int, int)
  def glBindSampler(self, unit: int, sampler: int) -> None:
    """
    Calls Qt's 'void QOpenGLExtraFunctions::glBindSampler(GLuint unit, GLuint
    sampler)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html#glBindSampler

    Parameters
    ----------

    unit : int
      Passed on as it is.

    sampler : int
      Passed on as it is.
    """
    #  void QOpenGLExtraFunctions::glBindSampler(GLuint unit, GLuint sampler)
    self.uglySide.call(
        'ritual_ZN21QOpenGLExtraFunctions13glBindSamplerEjj', unit, sampler,
    )

  @overload(int, int, int)
  def glSamplerParameteri(
      self,
      sampler: int,
      pname: int,
      param: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLExtraFunctions::glSamplerParameteri(GLuint
    sampler, GLenum pname, GLint param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html#glSamplerParameteri

    Parameters
    ----------

    sampler : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    param : int
      Passed on as it is.
    """
    #  void QOpenGLExtraFunctions::glSamplerParameteri(GLuint sampler, GLenum
    #      pname, GLint param)
    self.uglySide.call(
        'ritual_ZN21QOpenGLExtraFunctions19glSamplerParameteriEjji',
        sampler, pname, param,
    )

  @overload(int, int, float)
  def glSamplerParameterf(
      self,
      sampler: int,
      pname: int,
      param: float,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLExtraFunctions::glSamplerParameterf(GLuint
    sampler, GLenum pname, GLfloat param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html#glSamplerParameterf

    Parameters
    ----------

    sampler : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    param : float
      Passed on as it is.
    """
    #  void QOpenGLExtraFunctions::glSamplerParameterf(GLuint sampler, GLenum
    #      pname, GLfloat param)
    self.uglySide.call(
        'ritual_ZN21QOpenGLExtraFunctions19glSamplerParameterfEjjf',
        sampler, pname, param,
    )

  @overload(int, int)
  def glVertexAttribDivisor(self, index: int, divisor: int) -> None:
    """
    Calls Qt's 'void QOpenGLExtraFunctions::glVertexAttribDivisor(GLuint
    index, GLuint divisor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html#glVertexAttribDivisor

    Parameters
    ----------

    index : int
      Passed on as it is.

    divisor : int
      Passed on as it is.
    """
    #  void QOpenGLExtraFunctions::glVertexAttribDivisor(GLuint index, GLuint
    #      divisor)
    self.uglySide.call(
        'ritual_ZN21QOpenGLExtraFunctions21glVertexAttribDivisorEjj',
        index, divisor,
    )

  @overload(int, int)
  def glBindTransformFeedback(self, target: int, id: int) -> None:
    """
    Calls Qt's 'void QOpenGLExtraFunctions::glBindTransformFeedback(GLenum
    target, GLuint id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html#glBindTransformFeedback

    Parameters
    ----------

    target : int
      Passed on as it is.

    id : int
      Passed on as it is.
    """
    #  void QOpenGLExtraFunctions::glBindTransformFeedback(GLenum target,
    #      GLuint id)
    self.uglySide.call(
        'ritual_ZN21QOpenGLExtraFunctions23glBindTransformFeedbackEjj',
        target, id,
    )

  def glPauseTransformFeedback(self) -> None:
    """
    Calls Qt's 'void QOpenGLExtraFunctions::glPauseTransformFeedback()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html
    """
    #  void QOpenGLExtraFunctions::glPauseTransformFeedback()
    self.uglySide.call(
        'ritual_ZN21QOpenGLExtraFunctions24glPauseTransformFeedbackEv',
    )

  def glResumeTransformFeedback(self) -> None:
    """
    Calls Qt's 'void QOpenGLExtraFunctions::glResumeTransformFeedback()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html
    """
    #  void QOpenGLExtraFunctions::glResumeTransformFeedback()
    self.uglySide.call(
        'ritual_ZN21QOpenGLExtraFunctions25glResumeTransformFeedbackEv',
    )

  @overload(int, int, int)
  def glProgramParameteri(
      self,
      program: int,
      pname: int,
      value: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLExtraFunctions::glProgramParameteri(GLuint
    program, GLenum pname, GLint value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html#glProgramParameteri

    Parameters
    ----------

    program : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    value : int
      Passed on as it is.
    """
    #  void QOpenGLExtraFunctions::glProgramParameteri(GLuint program, GLenum
    #      pname, GLint value)
    self.uglySide.call(
        'ritual_ZN21QOpenGLExtraFunctions19glProgramParameteriEjji',
        program, pname, value,
    )

  @overload(int, int, int, int, int)
  def glTexStorage2D(
      self,
      target: int,
      levels: int,
      internalformat: int,
      width: int,
      height: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLExtraFunctions::glTexStorage2D(GLenum target,
    GLsizei levels, GLenum internalformat, GLsizei width, GLsizei height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html#glTexStorage2D

    Parameters
    ----------

    target : int
      Passed on as it is.

    levels : int
      Passed on as it is.

    internalformat : int
      Passed on as it is.

    width : int
      Passed on as it is.

    height : int
      Passed on as it is.
    """
    #  void QOpenGLExtraFunctions::glTexStorage2D(GLenum target, GLsizei
    #      levels, GLenum internalformat, GLsizei width, GLsizei height)
    self.uglySide.call(
        'ritual_ZN21QOpenGLExtraFunctions14glTexStorage2DEjijii',
        target, levels, internalformat, width, height,
    )

  @overload(int, int, int, int, int, int)
  def glTexStorage3D(
      self,
      target: int,
      levels: int,
      internalformat: int,
      width: int,
      height: int,
      depth: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLExtraFunctions::glTexStorage3D(GLenum target,
    GLsizei levels, GLenum internalformat, GLsizei width, GLsizei height,
    GLsizei depth)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html#glTexStorage3D

    Parameters
    ----------

    target : int
      Passed on as it is.

    levels : int
      Passed on as it is.

    internalformat : int
      Passed on as it is.

    width : int
      Passed on as it is.

    height : int
      Passed on as it is.

    depth : int
      Passed on as it is.
    """
    #  void QOpenGLExtraFunctions::glTexStorage3D(GLenum target, GLsizei
    #      levels, GLenum internalformat, GLsizei width, GLsizei height,
    #      GLsizei depth)
    self.uglySide.call(
        'ritual_ZN21QOpenGLExtraFunctions14glTexStorage3DEjijiii',
        target, levels, internalformat, width, height, depth,
    )

  @overload(int, int, int)
  def glDispatchCompute(
      self,
      num_groups_x: int,
      num_groups_y: int,
      num_groups_z: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLExtraFunctions::glDispatchCompute(GLuint
    num_groups_x, GLuint num_groups_y, GLuint num_groups_z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html#glDispatchCompute

    Parameters
    ----------

    num_groups_x : int
      Passed on as it is.

    num_groups_y : int
      Passed on as it is.

    num_groups_z : int
      Passed on as it is.
    """
    #  void QOpenGLExtraFunctions::glDispatchCompute(GLuint num_groups_x,
    #      GLuint num_groups_y, GLuint num_groups_z)
    self.uglySide.call(
        'ritual_ZN21QOpenGLExtraFunctions17glDispatchComputeEjjj',
        num_groups_x, num_groups_y, num_groups_z,
    )

  @overload(int, int, int)
  def glFramebufferParameteri(
      self,
      target: int,
      pname: int,
      param: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLExtraFunctions::glFramebufferParameteri(GLenum
    target, GLenum pname, GLint param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html#glFramebufferParameteri

    Parameters
    ----------

    target : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    param : int
      Passed on as it is.
    """
    #  void QOpenGLExtraFunctions::glFramebufferParameteri(GLenum target,
    #      GLenum pname, GLint param)
    self.uglySide.call(
        'ritual_ZN21QOpenGLExtraFunctions23glFramebufferParameteriEjji',
        target, pname, param,
    )

  @overload(int, int, int)
  def glUseProgramStages(
      self,
      pipeline: int,
      stages: int,
      program: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLExtraFunctions::glUseProgramStages(GLuint
    pipeline, GLbitfield stages, GLuint program)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html#glUseProgramStages

    Parameters
    ----------

    pipeline : int
      Passed on as it is.

    stages : int
      Passed on as it is.

    program : int
      Passed on as it is.
    """
    #  void QOpenGLExtraFunctions::glUseProgramStages(GLuint pipeline,
    #      GLbitfield stages, GLuint program)
    self.uglySide.call(
        'ritual_ZN21QOpenGLExtraFunctions18glUseProgramStagesEjjj',
        pipeline, stages, program,
    )

  @overload(int, int)
  def glActiveShaderProgram(self, pipeline: int, program: int) -> None:
    """
    Calls Qt's 'void QOpenGLExtraFunctions::glActiveShaderProgram(GLuint
    pipeline, GLuint program)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html#glActiveShaderProgram

    Parameters
    ----------

    pipeline : int
      Passed on as it is.

    program : int
      Passed on as it is.
    """
    #  void QOpenGLExtraFunctions::glActiveShaderProgram(GLuint pipeline,
    #      GLuint program)
    self.uglySide.call(
        'ritual_ZN21QOpenGLExtraFunctions21glActiveShaderProgramEjj',
        pipeline, program,
    )

  @overload(int)
  def glBindProgramPipeline(self, pipeline: int) -> None:
    """
    Calls Qt's 'void QOpenGLExtraFunctions::glBindProgramPipeline(GLuint
    pipeline)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html#glBindProgramPipeline

    Parameters
    ----------

    pipeline : int
      Passed on as it is.
    """
    #  void QOpenGLExtraFunctions::glBindProgramPipeline(GLuint pipeline)
    self.uglySide.call(
        'ritual_ZN21QOpenGLExtraFunctions21glBindProgramPipelineEj',
        pipeline,
    )

  @overload(int, int, int)
  def glProgramUniform1i(self, program: int, location: int, v0: int) -> None:
    """
    Calls Qt's 'void QOpenGLExtraFunctions::glProgramUniform1i(GLuint
    program, GLint location, GLint v0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html#glProgramUniform1i

    Parameters
    ----------

    program : int
      Passed on as it is.

    location : int
      Passed on as it is.

    v0 : int
      Passed on as it is.
    """
    #  void QOpenGLExtraFunctions::glProgramUniform1i(GLuint program, GLint
    #      location, GLint v0)
    self.uglySide.call(
        'ritual_ZN21QOpenGLExtraFunctions18glProgramUniform1iEjii',
        program, location, v0,
    )

  @overload(int, int, int, int)
  def glProgramUniform2i(
      self,
      program: int,
      location: int,
      v0: int,
      v1: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLExtraFunctions::glProgramUniform2i(GLuint
    program, GLint location, GLint v0, GLint v1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html#glProgramUniform2i

    Parameters
    ----------

    program : int
      Passed on as it is.

    location : int
      Passed on as it is.

    v0 : int
      Passed on as it is.

    v1 : int
      Passed on as it is.
    """
    #  void QOpenGLExtraFunctions::glProgramUniform2i(GLuint program, GLint
    #      location, GLint v0, GLint v1)
    self.uglySide.call(
        'ritual_ZN21QOpenGLExtraFunctions18glProgramUniform2iEjiii',
        program, location, v0, v1,
    )

  @overload(int, int, int, int, int)
  def glProgramUniform3i(
      self,
      program: int,
      location: int,
      v0: int,
      v1: int,
      v2: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLExtraFunctions::glProgramUniform3i(GLuint
    program, GLint location, GLint v0, GLint v1, GLint v2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html#glProgramUniform3i

    Parameters
    ----------

    program : int
      Passed on as it is.

    location : int
      Passed on as it is.

    v0 : int
      Passed on as it is.

    v1 : int
      Passed on as it is.

    v2 : int
      Passed on as it is.
    """
    #  void QOpenGLExtraFunctions::glProgramUniform3i(GLuint program, GLint
    #      location, GLint v0, GLint v1, GLint v2)
    self.uglySide.call(
        'ritual_ZN21QOpenGLExtraFunctions18glProgramUniform3iEjiiii',
        program, location, v0, v1, v2,
    )

  @overload(int, int, int, int, int, int)
  def glProgramUniform4i(
      self,
      program: int,
      location: int,
      v0: int,
      v1: int,
      v2: int,
      v3: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLExtraFunctions::glProgramUniform4i(GLuint
    program, GLint location, GLint v0, GLint v1, GLint v2, GLint v3)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html#glProgramUniform4i

    Parameters
    ----------

    program : int
      Passed on as it is.

    location : int
      Passed on as it is.

    v0 : int
      Passed on as it is.

    v1 : int
      Passed on as it is.

    v2 : int
      Passed on as it is.

    v3 : int
      Passed on as it is.
    """
    #  void QOpenGLExtraFunctions::glProgramUniform4i(GLuint program, GLint
    #      location, GLint v0, GLint v1, GLint v2, GLint v3)
    self.uglySide.call(
        'ritual_ZN21QOpenGLExtraFunctions18glProgramUniform4iEjiiiii',
        program, location, v0, v1, v2, v3,
    )

  @overload(int, int, int)
  def glProgramUniform1ui(
      self,
      program: int,
      location: int,
      v0: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLExtraFunctions::glProgramUniform1ui(GLuint
    program, GLint location, GLuint v0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html#glProgramUniform1ui

    Parameters
    ----------

    program : int
      Passed on as it is.

    location : int
      Passed on as it is.

    v0 : int
      Passed on as it is.
    """
    #  void QOpenGLExtraFunctions::glProgramUniform1ui(GLuint program, GLint
    #      location, GLuint v0)
    self.uglySide.call(
        'ritual_ZN21QOpenGLExtraFunctions19glProgramUniform1uiEjij',
        program, location, v0,
    )

  @overload(int, int, int, int)
  def glProgramUniform2ui(
      self,
      program: int,
      location: int,
      v0: int,
      v1: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLExtraFunctions::glProgramUniform2ui(GLuint
    program, GLint location, GLuint v0, GLuint v1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html#glProgramUniform2ui

    Parameters
    ----------

    program : int
      Passed on as it is.

    location : int
      Passed on as it is.

    v0 : int
      Passed on as it is.

    v1 : int
      Passed on as it is.
    """
    #  void QOpenGLExtraFunctions::glProgramUniform2ui(GLuint program, GLint
    #      location, GLuint v0, GLuint v1)
    self.uglySide.call(
        'ritual_ZN21QOpenGLExtraFunctions19glProgramUniform2uiEjijj',
        program, location, v0, v1,
    )

  @overload(int, int, int, int, int)
  def glProgramUniform3ui(
      self,
      program: int,
      location: int,
      v0: int,
      v1: int,
      v2: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLExtraFunctions::glProgramUniform3ui(GLuint
    program, GLint location, GLuint v0, GLuint v1, GLuint v2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html#glProgramUniform3ui

    Parameters
    ----------

    program : int
      Passed on as it is.

    location : int
      Passed on as it is.

    v0 : int
      Passed on as it is.

    v1 : int
      Passed on as it is.

    v2 : int
      Passed on as it is.
    """
    #  void QOpenGLExtraFunctions::glProgramUniform3ui(GLuint program, GLint
    #      location, GLuint v0, GLuint v1, GLuint v2)
    self.uglySide.call(
        'ritual_ZN21QOpenGLExtraFunctions19glProgramUniform3uiEjijjj',
        program, location, v0, v1, v2,
    )

  @overload(int, int, int, int, int, int)
  def glProgramUniform4ui(
      self,
      program: int,
      location: int,
      v0: int,
      v1: int,
      v2: int,
      v3: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLExtraFunctions::glProgramUniform4ui(GLuint
    program, GLint location, GLuint v0, GLuint v1, GLuint v2, GLuint v3)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html#glProgramUniform4ui

    Parameters
    ----------

    program : int
      Passed on as it is.

    location : int
      Passed on as it is.

    v0 : int
      Passed on as it is.

    v1 : int
      Passed on as it is.

    v2 : int
      Passed on as it is.

    v3 : int
      Passed on as it is.
    """
    #  void QOpenGLExtraFunctions::glProgramUniform4ui(GLuint program, GLint
    #      location, GLuint v0, GLuint v1, GLuint v2, GLuint v3)
    self.uglySide.call(
        'ritual_ZN21QOpenGLExtraFunctions19glProgramUniform4uiEjijjjj',
        program, location, v0, v1, v2, v3,
    )

  @overload(int, int, float)
  def glProgramUniform1f(
      self,
      program: int,
      location: int,
      v0: float,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLExtraFunctions::glProgramUniform1f(GLuint
    program, GLint location, GLfloat v0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html#glProgramUniform1f

    Parameters
    ----------

    program : int
      Passed on as it is.

    location : int
      Passed on as it is.

    v0 : float
      Passed on as it is.
    """
    #  void QOpenGLExtraFunctions::glProgramUniform1f(GLuint program, GLint
    #      location, GLfloat v0)
    self.uglySide.call(
        'ritual_ZN21QOpenGLExtraFunctions18glProgramUniform1fEjif',
        program, location, v0,
    )

  @overload(int, int, float, float)
  def glProgramUniform2f(
      self,
      program: int,
      location: int,
      v0: float,
      v1: float,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLExtraFunctions::glProgramUniform2f(GLuint
    program, GLint location, GLfloat v0, GLfloat v1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html#glProgramUniform2f

    Parameters
    ----------

    program : int
      Passed on as it is.

    location : int
      Passed on as it is.

    v0 : float
      Passed on as it is.

    v1 : float
      Passed on as it is.
    """
    #  void QOpenGLExtraFunctions::glProgramUniform2f(GLuint program, GLint
    #      location, GLfloat v0, GLfloat v1)
    self.uglySide.call(
        'ritual_ZN21QOpenGLExtraFunctions18glProgramUniform2fEjiff',
        program, location, v0, v1,
    )

  @overload(int, int, float, float, float)
  def glProgramUniform3f(
      self,
      program: int,
      location: int,
      v0: float,
      v1: float,
      v2: float,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLExtraFunctions::glProgramUniform3f(GLuint
    program, GLint location, GLfloat v0, GLfloat v1, GLfloat v2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html#glProgramUniform3f

    Parameters
    ----------

    program : int
      Passed on as it is.

    location : int
      Passed on as it is.

    v0 : float
      Passed on as it is.

    v1 : float
      Passed on as it is.

    v2 : float
      Passed on as it is.
    """
    #  void QOpenGLExtraFunctions::glProgramUniform3f(GLuint program, GLint
    #      location, GLfloat v0, GLfloat v1, GLfloat v2)
    self.uglySide.call(
        'ritual_ZN21QOpenGLExtraFunctions18glProgramUniform3fEjifff',
        program, location, v0, v1, v2,
    )

  @overload(int, int, float, float, float, float)
  def glProgramUniform4f(
      self,
      program: int,
      location: int,
      v0: float,
      v1: float,
      v2: float,
      v3: float,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLExtraFunctions::glProgramUniform4f(GLuint
    program, GLint location, GLfloat v0, GLfloat v1, GLfloat v2, GLfloat
    v3)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html#glProgramUniform4f

    Parameters
    ----------

    program : int
      Passed on as it is.

    location : int
      Passed on as it is.

    v0 : float
      Passed on as it is.

    v1 : float
      Passed on as it is.

    v2 : float
      Passed on as it is.

    v3 : float
      Passed on as it is.
    """
    #  void QOpenGLExtraFunctions::glProgramUniform4f(GLuint program, GLint
    #      location, GLfloat v0, GLfloat v1, GLfloat v2, GLfloat v3)
    self.uglySide.call(
        'ritual_ZN21QOpenGLExtraFunctions18glProgramUniform4fEjiffff',
        program, location, v0, v1, v2, v3,
    )

  @overload(int)
  def glValidateProgramPipeline(self, pipeline: int) -> None:
    """
    Calls Qt's 'void QOpenGLExtraFunctions::glValidateProgramPipeline(GLuint
    pipeline)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html

    Parameters
    ----------

    pipeline : int
      Passed on as it is.
    """
    #  void QOpenGLExtraFunctions::glValidateProgramPipeline(GLuint pipeline)
    self.uglySide.call(
        'ritual_ZN21QOpenGLExtraFunctions25glValidateProgramPipelineEj',
        pipeline,
    )

  @overload(int, int, int, int, int, int, int)
  def glBindImageTexture(
      self,
      unit: int,
      texture: int,
      level: int,
      layered: int,
      layer: int,
      access: int,
      format: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLExtraFunctions::glBindImageTexture(GLuint unit,
    GLuint texture, GLint level, GLboolean layered, GLint layer, GLenum
    access, GLenum format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html#glBindImageTexture

    Parameters
    ----------

    unit : int
      Passed on as it is.

    texture : int
      Passed on as it is.

    level : int
      Passed on as it is.

    layered : int
      Passed on as it is.

    layer : int
      Passed on as it is.

    access : int
      Passed on as it is.

    format : int
      Passed on as it is.
    """
    #  void QOpenGLExtraFunctions::glBindImageTexture(GLuint unit, GLuint
    #      texture, GLint level, GLboolean layered, GLint layer, GLenum
    #      access, GLenum format)
    self.uglySide.call(
        'ritual_ZN21QOpenGLExtraFunctions18glBindImageTextureEjjihijj',
        unit, texture, level, layered, layer, access, format,
    )

  @overload(int)
  def glMemoryBarrier(self, barriers: int) -> None:
    """
    Calls Qt's 'void QOpenGLExtraFunctions::glMemoryBarrier(GLbitfield
    barriers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html#glMemoryBarrier

    Parameters
    ----------

    barriers : int
      Passed on as it is.
    """
    #  void QOpenGLExtraFunctions::glMemoryBarrier(GLbitfield barriers)
    self.uglySide.call(
        'ritual_ZN21QOpenGLExtraFunctions15glMemoryBarrierEj', barriers,
    )

  @overload(int)
  def glMemoryBarrierByRegion(self, barriers: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLExtraFunctions::glMemoryBarrierByRegion(GLbitfield barriers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html#glMemoryBarrierByRegion

    Parameters
    ----------

    barriers : int
      Passed on as it is.
    """
    #  void QOpenGLExtraFunctions::glMemoryBarrierByRegion(GLbitfield
    #      barriers)
    self.uglySide.call(
        'ritual_ZN21QOpenGLExtraFunctions23glMemoryBarrierByRegionEj',
        barriers,
    )

  @overload(int, int, int, int, int, int)
  def glTexStorage2DMultisample(
      self,
      target: int,
      samples: int,
      internalformat: int,
      width: int,
      height: int,
      fixedsamplelocations: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLExtraFunctions::glTexStorage2DMultisample(GLenum
    target, GLsizei samples, GLenum internalformat, GLsizei width, GLsizei
    height, GLboolean fixedsamplelocations)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html

    Parameters
    ----------

    target : int
      Passed on as it is.

    samples : int
      Passed on as it is.

    internalformat : int
      Passed on as it is.

    width : int
      Passed on as it is.

    height : int
      Passed on as it is.

    fixedsamplelocations : int
      Passed on as it is.
    """
    #  void QOpenGLExtraFunctions::glTexStorage2DMultisample(GLenum target,
    #      GLsizei samples, GLenum internalformat, GLsizei width, GLsizei
    #      height, GLboolean fixedsamplelocations)
    self.uglySide.call(
        'ritual_ZN21QOpenGLExtraFunctions25glTexStorage2DMultisampleEjijiih',
        target, samples, internalformat, width, height, fixedsamplelocations,
    )

  @overload(int, int)
  def glSampleMaski(self, maskNumber: int, mask: int) -> None:
    """
    Calls Qt's 'void QOpenGLExtraFunctions::glSampleMaski(GLuint maskNumber,
    GLbitfield mask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html#glSampleMaski

    Parameters
    ----------

    maskNumber : int
      Passed on as it is.

    mask : int
      Passed on as it is.
    """
    #  void QOpenGLExtraFunctions::glSampleMaski(GLuint maskNumber,
    #      GLbitfield mask)
    self.uglySide.call(
        'ritual_ZN21QOpenGLExtraFunctions13glSampleMaskiEjj',
        maskNumber, mask,
    )

  @overload(int, int, int, int, int)
  def glVertexAttribFormat(
      self,
      attribindex: int,
      size: int,
      type: int,
      normalized: int,
      relativeoffset: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLExtraFunctions::glVertexAttribFormat(GLuint
    attribindex, GLint size, GLenum type, GLboolean normalized, GLuint
    relativeoffset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html#glVertexAttribFormat

    Parameters
    ----------

    attribindex : int
      Passed on as it is.

    size : int
      Passed on as it is.

    type : int
      Passed on as it is.

    normalized : int
      Passed on as it is.

    relativeoffset : int
      Passed on as it is.
    """
    #  void QOpenGLExtraFunctions::glVertexAttribFormat(GLuint attribindex,
    #      GLint size, GLenum type, GLboolean normalized, GLuint
    #      relativeoffset)
    self.uglySide.call(
        'ritual_ZN21QOpenGLExtraFunctions20glVertexAttribFormatEjijhj',
        attribindex, size, type, normalized, relativeoffset,
    )

  @overload(int, int, int, int)
  def glVertexAttribIFormat(
      self,
      attribindex: int,
      size: int,
      type: int,
      relativeoffset: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLExtraFunctions::glVertexAttribIFormat(GLuint
    attribindex, GLint size, GLenum type, GLuint relativeoffset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html#glVertexAttribIFormat

    Parameters
    ----------

    attribindex : int
      Passed on as it is.

    size : int
      Passed on as it is.

    type : int
      Passed on as it is.

    relativeoffset : int
      Passed on as it is.
    """
    #  void QOpenGLExtraFunctions::glVertexAttribIFormat(GLuint attribindex,
    #      GLint size, GLenum type, GLuint relativeoffset)
    self.uglySide.call(
        'ritual_ZN21QOpenGLExtraFunctions21glVertexAttribIFormatEjijj',
        attribindex, size, type, relativeoffset,
    )

  @overload(int, int)
  def glVertexAttribBinding(
      self,
      attribindex: int,
      bindingindex: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLExtraFunctions::glVertexAttribBinding(GLuint
    attribindex, GLuint bindingindex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html#glVertexAttribBinding

    Parameters
    ----------

    attribindex : int
      Passed on as it is.

    bindingindex : int
      Passed on as it is.
    """
    #  void QOpenGLExtraFunctions::glVertexAttribBinding(GLuint attribindex,
    #      GLuint bindingindex)
    self.uglySide.call(
        'ritual_ZN21QOpenGLExtraFunctions21glVertexAttribBindingEjj',
        attribindex, bindingindex,
    )

  @overload(int, int)
  def glVertexBindingDivisor(self, bindingindex: int, divisor: int) -> None:
    """
    Calls Qt's 'void QOpenGLExtraFunctions::glVertexBindingDivisor(GLuint
    bindingindex, GLuint divisor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html#glVertexBindingDivisor

    Parameters
    ----------

    bindingindex : int
      Passed on as it is.

    divisor : int
      Passed on as it is.
    """
    #  void QOpenGLExtraFunctions::glVertexBindingDivisor(GLuint
    #      bindingindex, GLuint divisor)
    self.uglySide.call(
        'ritual_ZN21QOpenGLExtraFunctions22glVertexBindingDivisorEjj',
        bindingindex, divisor,
    )

  def glBlendBarrier(self) -> None:
    """
    Calls Qt's 'void QOpenGLExtraFunctions::glBlendBarrier()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html#glBlendBarrier
    """
    #  void QOpenGLExtraFunctions::glBlendBarrier()
    self.uglySide.call('ritual_ZN21QOpenGLExtraFunctions14glBlendBarrierEv')

  @overload(
      int, int, int, int, int, int, int, int, int, int, int, int, int, int,
      int,
  )
  def glCopyImageSubData(
      self,
      srcName: int,
      srcTarget: int,
      srcLevel: int,
      srcX: int,
      srcY: int,
      srcZ: int,
      dstName: int,
      dstTarget: int,
      dstLevel: int,
      dstX: int,
      dstY: int,
      dstZ: int,
      srcWidth: int,
      srcHeight: int,
      srcDepth: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLExtraFunctions::glCopyImageSubData(GLuint
    srcName, GLenum srcTarget, GLint srcLevel, GLint srcX, GLint srcY, GLint
    srcZ, GLuint dstName, GLenum dstTarget, GLint dstLevel, GLint dstX, GLint
    dstY, GLint dstZ, GLsizei srcWidth, GLsizei srcHeight, GLsizei
    srcDepth)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html#glCopyImageSubData

    Parameters
    ----------

    srcName : int
      Passed on as it is.

    srcTarget : int
      Passed on as it is.

    srcLevel : int
      Passed on as it is.

    srcX : int
      Passed on as it is.

    srcY : int
      Passed on as it is.

    srcZ : int
      Passed on as it is.

    dstName : int
      Passed on as it is.

    dstTarget : int
      Passed on as it is.

    dstLevel : int
      Passed on as it is.

    dstX : int
      Passed on as it is.

    dstY : int
      Passed on as it is.

    dstZ : int
      Passed on as it is.

    srcWidth : int
      Passed on as it is.

    srcHeight : int
      Passed on as it is.

    srcDepth : int
      Passed on as it is.
    """
    #  void QOpenGLExtraFunctions::glCopyImageSubData(GLuint srcName, GLenum
    #      srcTarget, GLint srcLevel, GLint srcX, GLint srcY, GLint srcZ,
    #      GLuint dstName, GLenum dstTarget, GLint dstLevel, GLint dstX,
    #      GLint dstY, GLint dstZ, GLsizei srcWidth, GLsizei srcHeight,
    #      GLsizei srcDepth)
    self.uglySide.call(
        'ritual_ZN21QOpenGLExtraFunctions18glCopyImageSubDataEjjiiiijjiiiii'
        'ii',
        srcName, srcTarget, srcLevel, srcX, srcY, srcZ, dstName, dstTarget,
        dstLevel, dstX, dstY, dstZ, srcWidth, srcHeight, srcDepth,
    )

  def glPopDebugGroup(self) -> None:
    """
    Calls Qt's 'void QOpenGLExtraFunctions::glPopDebugGroup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html#glPopDebugGroup
    """
    #  void QOpenGLExtraFunctions::glPopDebugGroup()
    self.uglySide.call('ritual_ZN21QOpenGLExtraFunctions15glPopDebugGroupEv')

  @overload(int, int)
  def glEnablei(self, target: int, index: int) -> None:
    """
    Calls Qt's 'void QOpenGLExtraFunctions::glEnablei(GLenum target, GLuint
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html#glEnablei

    Parameters
    ----------

    target : int
      Passed on as it is.

    index : int
      Passed on as it is.
    """
    #  void QOpenGLExtraFunctions::glEnablei(GLenum target, GLuint index)
    self.uglySide.call(
        'ritual_ZN21QOpenGLExtraFunctions9glEnableiEjj', target, index,
    )

  @overload(int, int)
  def glDisablei(self, target: int, index: int) -> None:
    """
    Calls Qt's 'void QOpenGLExtraFunctions::glDisablei(GLenum target, GLuint
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html#glDisablei

    Parameters
    ----------

    target : int
      Passed on as it is.

    index : int
      Passed on as it is.
    """
    #  void QOpenGLExtraFunctions::glDisablei(GLenum target, GLuint index)
    self.uglySide.call(
        'ritual_ZN21QOpenGLExtraFunctions10glDisableiEjj', target, index,
    )

  @overload(int, int)
  def glBlendEquationi(self, buf: int, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLExtraFunctions::glBlendEquationi(GLuint buf,
    GLenum mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html#glBlendEquationi

    Parameters
    ----------

    buf : int
      Passed on as it is.

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLExtraFunctions::glBlendEquationi(GLuint buf, GLenum mode)
    self.uglySide.call(
        'ritual_ZN21QOpenGLExtraFunctions16glBlendEquationiEjj', buf, mode,
    )

  @overload(int, int, int)
  def glBlendEquationSeparatei(
      self,
      buf: int,
      modeRGB: int,
      modeAlpha: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLExtraFunctions::glBlendEquationSeparatei(GLuint
    buf, GLenum modeRGB, GLenum modeAlpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html

    Parameters
    ----------

    buf : int
      Passed on as it is.

    modeRGB : int
      Passed on as it is.

    modeAlpha : int
      Passed on as it is.
    """
    #  void QOpenGLExtraFunctions::glBlendEquationSeparatei(GLuint buf,
    #      GLenum modeRGB, GLenum modeAlpha)
    self.uglySide.call(
        'ritual_ZN21QOpenGLExtraFunctions24glBlendEquationSeparateiEjjj',
        buf, modeRGB, modeAlpha,
    )

  @overload(int, int, int)
  def glBlendFunci(self, buf: int, src: int, dst: int) -> None:
    """
    Calls Qt's 'void QOpenGLExtraFunctions::glBlendFunci(GLuint buf, GLenum
    src, GLenum dst)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html#glBlendFunci

    Parameters
    ----------

    buf : int
      Passed on as it is.

    src : int
      Passed on as it is.

    dst : int
      Passed on as it is.
    """
    #  void QOpenGLExtraFunctions::glBlendFunci(GLuint buf, GLenum src,
    #      GLenum dst)
    self.uglySide.call(
        'ritual_ZN21QOpenGLExtraFunctions12glBlendFunciEjjj', buf, src, dst,
    )

  @overload(int, int, int, int, int)
  def glBlendFuncSeparatei(
      self,
      buf: int,
      srcRGB: int,
      dstRGB: int,
      srcAlpha: int,
      dstAlpha: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLExtraFunctions::glBlendFuncSeparatei(GLuint buf,
    GLenum srcRGB, GLenum dstRGB, GLenum srcAlpha, GLenum dstAlpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html#glBlendFuncSeparatei

    Parameters
    ----------

    buf : int
      Passed on as it is.

    srcRGB : int
      Passed on as it is.

    dstRGB : int
      Passed on as it is.

    srcAlpha : int
      Passed on as it is.

    dstAlpha : int
      Passed on as it is.
    """
    #  void QOpenGLExtraFunctions::glBlendFuncSeparatei(GLuint buf, GLenum
    #      srcRGB, GLenum dstRGB, GLenum srcAlpha, GLenum dstAlpha)
    self.uglySide.call(
        'ritual_ZN21QOpenGLExtraFunctions20glBlendFuncSeparateiEjjjjj',
        buf, srcRGB, dstRGB, srcAlpha, dstAlpha,
    )

  @overload(int, int, int, int, int)
  def glColorMaski(self, index: int, r: int, g: int, b: int, a: int) -> None:
    """
    Calls Qt's 'void QOpenGLExtraFunctions::glColorMaski(GLuint index,
    GLboolean r, GLboolean g, GLboolean b, GLboolean a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html#glColorMaski

    Parameters
    ----------

    index : int
      Passed on as it is.

    r : int
      Passed on as it is.

    g : int
      Passed on as it is.

    b : int
      Passed on as it is.

    a : int
      Passed on as it is.
    """
    #  void QOpenGLExtraFunctions::glColorMaski(GLuint index, GLboolean r,
    #      GLboolean g, GLboolean b, GLboolean a)
    self.uglySide.call(
        'ritual_ZN21QOpenGLExtraFunctions12glColorMaskiEjhhhh',
        index, r, g, b, a,
    )

  @overload(int, int, int, int)
  def glFramebufferTexture(
      self,
      target: int,
      attachment: int,
      texture: int,
      level: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLExtraFunctions::glFramebufferTexture(GLenum
    target, GLenum attachment, GLuint texture, GLint level)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html#glFramebufferTexture

    Parameters
    ----------

    target : int
      Passed on as it is.

    attachment : int
      Passed on as it is.

    texture : int
      Passed on as it is.

    level : int
      Passed on as it is.
    """
    #  void QOpenGLExtraFunctions::glFramebufferTexture(GLenum target, GLenum
    #      attachment, GLuint texture, GLint level)
    self.uglySide.call(
        'ritual_ZN21QOpenGLExtraFunctions20glFramebufferTextureEjjji',
        target, attachment, texture, level,
    )

  @overload(float, float, float, float, float, float, float, float)
  def glPrimitiveBoundingBox(
      self,
      minX: float,
      minY: float,
      minZ: float,
      minW: float,
      maxX: float,
      maxY: float,
      maxZ: float,
      maxW: float,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLExtraFunctions::glPrimitiveBoundingBox(GLfloat
    minX, GLfloat minY, GLfloat minZ, GLfloat minW, GLfloat maxX, GLfloat
    maxY, GLfloat maxZ, GLfloat maxW)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html#glPrimitiveBoundingBox

    Parameters
    ----------

    minX : float
      Passed on as it is.

    minY : float
      Passed on as it is.

    minZ : float
      Passed on as it is.

    minW : float
      Passed on as it is.

    maxX : float
      Passed on as it is.

    maxY : float
      Passed on as it is.

    maxZ : float
      Passed on as it is.

    maxW : float
      Passed on as it is.
    """
    #  void QOpenGLExtraFunctions::glPrimitiveBoundingBox(GLfloat minX,
    #      GLfloat minY, GLfloat minZ, GLfloat minW, GLfloat maxX, GLfloat
    #      maxY, GLfloat maxZ, GLfloat maxW)
    self.uglySide.call(
        'ritual_ZN21QOpenGLExtraFunctions22glPrimitiveBoundingBoxEffffffff',
        minX, minY, minZ, minW, maxX, maxY, maxZ, maxW,
    )

  @overload(float)
  def glMinSampleShading(self, value: float) -> None:
    """
    Calls Qt's 'void QOpenGLExtraFunctions::glMinSampleShading(GLfloat
    value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html#glMinSampleShading

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void QOpenGLExtraFunctions::glMinSampleShading(GLfloat value)
    self.uglySide.call(
        'ritual_ZN21QOpenGLExtraFunctions18glMinSampleShadingEf', value,
    )

  @overload(int, int)
  def glPatchParameteri(self, pname: int, value: int) -> None:
    """
    Calls Qt's 'void QOpenGLExtraFunctions::glPatchParameteri(GLenum pname,
    GLint value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html#glPatchParameteri

    Parameters
    ----------

    pname : int
      Passed on as it is.

    value : int
      Passed on as it is.
    """
    #  void QOpenGLExtraFunctions::glPatchParameteri(GLenum pname, GLint
    #      value)
    self.uglySide.call(
        'ritual_ZN21QOpenGLExtraFunctions17glPatchParameteriEji',
        pname, value,
    )

  @overload(int, int, int)
  def glTexBuffer(
      self,
      target: int,
      internalformat: int,
      buffer: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLExtraFunctions::glTexBuffer(GLenum target, GLenum
    internalformat, GLuint buffer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html#glTexBuffer

    Parameters
    ----------

    target : int
      Passed on as it is.

    internalformat : int
      Passed on as it is.

    buffer : int
      Passed on as it is.
    """
    #  void QOpenGLExtraFunctions::glTexBuffer(GLenum target, GLenum
    #      internalformat, GLuint buffer)
    self.uglySide.call(
        'ritual_ZN21QOpenGLExtraFunctions11glTexBufferEjjj',
        target, internalformat, buffer,
    )

  @overload(int, int, int, int, int, int, int)
  def glTexStorage3DMultisample(
      self,
      target: int,
      samples: int,
      internalformat: int,
      width: int,
      height: int,
      depth: int,
      fixedsamplelocations: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLExtraFunctions::glTexStorage3DMultisample(GLenum
    target, GLsizei samples, GLenum internalformat, GLsizei width, GLsizei
    height, GLsizei depth, GLboolean fixedsamplelocations)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextrafunctions.html

    Parameters
    ----------

    target : int
      Passed on as it is.

    samples : int
      Passed on as it is.

    internalformat : int
      Passed on as it is.

    width : int
      Passed on as it is.

    height : int
      Passed on as it is.

    depth : int
      Passed on as it is.

    fixedsamplelocations : int
      Passed on as it is.
    """
    #  void QOpenGLExtraFunctions::glTexStorage3DMultisample(GLenum target,
    #      GLsizei samples, GLenum internalformat, GLsizei width, GLsizei
    #      height, GLsizei depth, GLboolean fixedsamplelocations)
    self.uglySide.call(
        'ritual_ZN21QOpenGLExtraFunctions25glTexStorage3DMultisampleEjijiii'
        'h',
        target, samples, internalformat, width, height, depth,
        fixedsamplelocations,
    )
