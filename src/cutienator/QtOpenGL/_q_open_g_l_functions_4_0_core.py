"""
QOpenGLFunctions_4_0_Core binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpenGL/qopenglfunctions_4_0_core.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QAbstractOpenGLFunctions

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtGui import QOpenGLContext
  from . import QOpenGLVersionProfile
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QOpenGLContext = WAIT['QOpenGLContext']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QOpenGLFunctions_4_0_Core(QAbstractOpenGLFunctions):
  """
  The cute side of Qt's QOpenGLFunctions_4_0_Core: a plain Python object
  standing in front of one C++ QOpenGLFunctions_4_0_Core.

  It is built on the cute 'QAbstractOpenGLFunctions', as Qt's
  QOpenGLFunctions_4_0_Core is built on Qt's QAbstractOpenGLFunctions, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QOpenGLFunctions_4_0_Core that has a ritual and that
  Python can call so far, 155 names in all: 'initializeOpenGLFunctions',
  'glViewport', 'glDepthRange', 'glIsEnabled', 'glGetError', 'glReadBuffer',
  'glPixelStorei', 'glPixelStoref', 'glDepthFunc', 'glStencilOp',
  'glStencilFunc', 'glLogicOp', 'glBlendFunc', 'glFlush', 'glFinish',
  'glEnable', 'glDisable', 'glDepthMask', 'glColorMask', 'glStencilMask',
  'glClearDepth', 'glClearStencil', 'glClearColor', 'glClear',
  'glDrawBuffer', 'glTexParameteri', 'glTexParameterf', 'glScissor',
  'glPolygonMode', 'glPointSize', 'glLineWidth', 'glHint', 'glFrontFace',
  'glCullFace', 'glIsTexture', 'glBindTexture', 'glCopyTexSubImage2D',
  'glCopyTexSubImage1D', 'glCopyTexImage2D', 'glCopyTexImage1D',
  'glPolygonOffset', 'glDrawArrays', 'glCopyTexSubImage3D',
  'glBlendEquation', 'glBlendColor', 'glSampleCoverage', 'glActiveTexture',
  'glPointParameteri', 'glPointParameterf', 'glBlendFuncSeparate',
  'glUnmapBuffer', 'glIsBuffer', 'glBindBuffer', 'glEndQuery',
  'glBeginQuery', 'glIsQuery', 'glValidateProgram', 'glUniform4i',
  'glUniform3i', 'glUniform2i', 'glUniform1i', 'glUniform4f', 'glUniform3f',
  'glUniform2f', 'glUniform1f', 'glUseProgram', 'glLinkProgram',
  'glIsShader', 'glIsProgram', 'glEnableVertexAttribArray',
  'glDisableVertexAttribArray', 'glDetachShader', 'glDeleteShader',
  'glDeleteProgram', 'glCreateShader', 'glCreateProgram', 'glCompileShader',
  'glAttachShader', 'glStencilMaskSeparate', 'glStencilFuncSeparate',
  'glStencilOpSeparate', 'glBlendEquationSeparate', 'glIsVertexArray',
  'glBindVertexArray', 'glFlushMappedBufferRange',
  'glFramebufferTextureLayer', 'glRenderbufferStorageMultisample',
  'glBlitFramebuffer', 'glGenerateMipmap', 'glFramebufferRenderbuffer',
  'glFramebufferTexture3D', 'glFramebufferTexture2D',
  'glFramebufferTexture1D', 'glCheckFramebufferStatus', 'glBindFramebuffer',
  'glIsFramebuffer', 'glRenderbufferStorage', 'glBindRenderbuffer',
  'glIsRenderbuffer', 'glClearBufferfi', 'glUniform4ui', 'glUniform3ui',
  'glUniform2ui', 'glUniform1ui', 'glEndConditionalRender',
  'glBeginConditionalRender', 'glClampColor', 'glBindBufferBase',
  'glBindBufferRange', 'glEndTransformFeedback', 'glBeginTransformFeedback',
  'glIsEnabledi', 'glDisablei', 'glEnablei', 'glColorMaski',
  'glCopyBufferSubData', 'glUniformBlockBinding', 'glPrimitiveRestartIndex',
  'glTexBuffer', 'glDrawArraysInstanced', 'glSampleMaski',
  'glTexImage3DMultisample', 'glTexImage2DMultisample', 'glProvokingVertex',
  'glFramebufferTexture', 'glVertexAttribP4ui', 'glVertexAttribP3ui',
  'glVertexAttribP2ui', 'glVertexAttribP1ui', 'glQueryCounter',
  'glSamplerParameterf', 'glSamplerParameteri', 'glBindSampler',
  'glIsSampler', 'glVertexAttribDivisor', 'glEndQueryIndexed',
  'glBeginQueryIndexed', 'glDrawTransformFeedbackStream',
  'glDrawTransformFeedback', 'glResumeTransformFeedback',
  'glPauseTransformFeedback', 'glIsTransformFeedback',
  'glBindTransformFeedback', 'glPatchParameteri', 'glUniform4d',
  'glUniform3d', 'glUniform2d', 'glUniform1d', 'glBlendFuncSeparatei',
  'glBlendFunci', 'glBlendEquationSeparatei', 'glBlendEquationi',
  'glMinSampleShading', 'isContextCompatible', 'versionProfile'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpenGLFunctions_4_0_Core::~QOpenGLFunctions_4_0_Core()': the
    destructor: Python never removes a C++ QOpenGLFunctions_4_0_Core.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glGetTexLevelParameteriv(GLenum
    target, GLint level, GLenum pname, GLint *params)': takes a number to
    change where it is.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glGetTexLevelParameterfv(GLenum
    target, GLint level, GLenum pname, GLfloat *params)': takes a number to
    change where it is.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glGetTexParameteriv(GLenum target,
    GLenum pname, GLint *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glGetTexParameterfv(GLenum target,
    GLenum pname, GLfloat *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glGetTexImage(GLenum target, GLint
    level, GLenum format, GLenum type, GLvoid *pixels)': names 'GLvoid',
    which has no cute class yet.
  - Qt's 'const GLubyte *QOpenGLFunctions_4_0_Core::glGetString(GLenum
    name)': gives 'unsigned char', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glGetIntegerv(GLenum pname, GLint
    *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glGetFloatv(GLenum pname, GLfloat
    *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glGetDoublev(GLenum pname, GLdouble
    *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glGetBooleanv(GLenum pname,
    GLboolean *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glReadPixels(GLint x, GLint y,
    GLsizei width, GLsizei height, GLenum format, GLenum type, GLvoid
    *pixels)': names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glTexImage2D(GLenum target, GLint
    level, GLint internalformat, GLsizei width, GLsizei height, GLint border,
    GLenum format, GLenum type, const GLvoid *pixels)': names 'GLvoid', which
    has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glTexImage1D(GLenum target, GLint
    level, GLint internalformat, GLsizei width, GLint border, GLenum format,
    GLenum type, const GLvoid *pixels)': names 'GLvoid', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glTexParameteriv(GLenum target,
    GLenum pname, const GLint *params)': names 'GLint', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glTexParameterfv(GLenum target,
    GLenum pname, const GLfloat *params)': names 'GLfloat', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glGenTextures(GLsizei n, GLuint
    *textures)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glDeleteTextures(GLsizei n, const
    GLuint *textures)': names 'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glTexSubImage2D(GLenum target,
    GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height,
    GLenum format, GLenum type, const GLvoid *pixels)': names 'GLvoid', which
    has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glTexSubImage1D(GLenum target,
    GLint level, GLint xoffset, GLsizei width, GLenum format, GLenum type,
    const GLvoid *pixels)': names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glDrawElements(GLenum mode, GLsizei
    count, GLenum type, const GLvoid *indices)': names 'GLvoid', which has no
    cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glTexSubImage3D(GLenum target,
    GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width,
    GLsizei height, GLsizei depth, GLenum format, GLenum type, const GLvoid
    *pixels)': names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glTexImage3D(GLenum target, GLint
    level, GLint internalformat, GLsizei width, GLsizei height, GLsizei
    depth, GLint border, GLenum format, GLenum type, const GLvoid *pixels)':
    names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glDrawRangeElements(GLenum mode,
    GLuint start, GLuint end, GLsizei count, GLenum type, const GLvoid
    *indices)': names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glGetCompressedTexImage(GLenum
    target, GLint level, GLvoid *img)': names 'GLvoid', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glCompressedTexSubImage1D(GLenum
    target, GLint level, GLint xoffset, GLsizei width, GLenum format, GLsizei
    imageSize, const GLvoid *data)': names 'GLvoid', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glCompressedTexSubImage2D(GLenum
    target, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei
    height, GLenum format, GLsizei imageSize, const GLvoid *data)': names
    'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glCompressedTexSubImage3D(GLenum
    target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei
    width, GLsizei height, GLsizei depth, GLenum format, GLsizei imageSize,
    const GLvoid *data)': names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glCompressedTexImage1D(GLenum
    target, GLint level, GLenum internalformat, GLsizei width, GLint border,
    GLsizei imageSize, const GLvoid *data)': names 'GLvoid', which has no
    cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glCompressedTexImage2D(GLenum
    target, GLint level, GLenum internalformat, GLsizei width, GLsizei
    height, GLint border, GLsizei imageSize, const GLvoid *data)': names
    'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glCompressedTexImage3D(GLenum
    target, GLint level, GLenum internalformat, GLsizei width, GLsizei
    height, GLsizei depth, GLint border, GLsizei imageSize, const GLvoid
    *data)': names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glPointParameteriv(GLenum pname,
    const GLint *params)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glPointParameterfv(GLenum pname,
    const GLfloat *params)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glMultiDrawElements(GLenum mode,
    const GLsizei *count, GLenum type, const GLvoid *const *indices, GLsizei
    drawcount)': names 'GLsizei', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glMultiDrawArrays(GLenum mode,
    const GLint *first, const GLsizei *count, GLsizei drawcount)': names
    'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glGetBufferPointerv(GLenum target,
    GLenum pname, GLvoid **params)': takes a type Python has no way to hand
    over yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glGetBufferParameteriv(GLenum
    target, GLenum pname, GLint *params)': takes a number to change where it
    is.
  - Qt's 'GLvoid *QOpenGLFunctions_4_0_Core::glMapBuffer(GLenum target,
    GLenum access)': gives 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glGetBufferSubData(GLenum target,
    GLintptr offset, GLsizeiptr size, GLvoid *data)': names 'GLvoid', which
    has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glBufferSubData(GLenum target,
    GLintptr offset, GLsizeiptr size, const GLvoid *data)': names 'GLvoid',
    which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glBufferData(GLenum target,
    GLsizeiptr size, const GLvoid *data, GLenum usage)': names 'GLvoid',
    which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glGenBuffers(GLsizei n, GLuint
    *buffers)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glDeleteBuffers(GLsizei n, const
    GLuint *buffers)': names 'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glGetQueryObjectuiv(GLuint id,
    GLenum pname, GLuint *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glGetQueryObjectiv(GLuint id,
    GLenum pname, GLint *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glGetQueryiv(GLenum target, GLenum
    pname, GLint *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glDeleteQueries(GLsizei n, const
    GLuint *ids)': names 'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glGenQueries(GLsizei n, GLuint
    *ids)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glVertexAttribPointer(GLuint index,
    GLint size, GLenum type, GLboolean normalized, GLsizei stride, const
    GLvoid *pointer)': names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glUniformMatrix4fv(GLint location,
    GLsizei count, GLboolean transpose, const GLfloat *value)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glUniformMatrix3fv(GLint location,
    GLsizei count, GLboolean transpose, const GLfloat *value)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glUniformMatrix2fv(GLint location,
    GLsizei count, GLboolean transpose, const GLfloat *value)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glUniform4iv(GLint location,
    GLsizei count, const GLint *value)': names 'GLint', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glUniform3iv(GLint location,
    GLsizei count, const GLint *value)': names 'GLint', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glUniform2iv(GLint location,
    GLsizei count, const GLint *value)': names 'GLint', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glUniform1iv(GLint location,
    GLsizei count, const GLint *value)': names 'GLint', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glUniform4fv(GLint location,
    GLsizei count, const GLfloat *value)': names 'GLfloat', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glUniform3fv(GLint location,
    GLsizei count, const GLfloat *value)': names 'GLfloat', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glUniform2fv(GLint location,
    GLsizei count, const GLfloat *value)': names 'GLfloat', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glUniform1fv(GLint location,
    GLsizei count, const GLfloat *value)': names 'GLfloat', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glShaderSource(GLuint shader,
    GLsizei count, const GLchar *const *string, const GLint *length)': names
    'GLchar *const', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glGetVertexAttribPointerv(GLuint
    index, GLenum pname, GLvoid **pointer)': takes a type Python has no way
    to hand over yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glGetVertexAttribiv(GLuint index,
    GLenum pname, GLint *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glGetVertexAttribfv(GLuint index,
    GLenum pname, GLfloat *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glGetVertexAttribdv(GLuint index,
    GLenum pname, GLdouble *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glGetUniformiv(GLuint program,
    GLint location, GLint *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glGetUniformfv(GLuint program,
    GLint location, GLfloat *params)': takes a number to change where it is.
  - Qt's 'GLint QOpenGLFunctions_4_0_Core::glGetUniformLocation(GLuint
    program, const GLchar *name)': names 'GLchar', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glGetShaderSource(GLuint shader,
    GLsizei bufSize, GLsizei *length, GLchar *source)': takes a number to
    change where it is.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glGetShaderInfoLog(GLuint shader,
    GLsizei bufSize, GLsizei *length, GLchar *infoLog)': takes a number to
    change where it is.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glGetShaderiv(GLuint shader, GLenum
    pname, GLint *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glGetProgramInfoLog(GLuint program,
    GLsizei bufSize, GLsizei *length, GLchar *infoLog)': takes a number to
    change where it is.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glGetProgramiv(GLuint program,
    GLenum pname, GLint *params)': takes a number to change where it is.
  - Qt's 'GLint QOpenGLFunctions_4_0_Core::glGetAttribLocation(GLuint
    program, const GLchar *name)': names 'GLchar', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glGetAttachedShaders(GLuint
    program, GLsizei maxCount, GLsizei *count, GLuint *obj)': takes a number
    to change where it is.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glGetActiveUniform(GLuint program,
    GLuint index, GLsizei bufSize, GLsizei *length, GLint *size, GLenum
    *type, GLchar *name)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glGetActiveAttrib(GLuint program,
    GLuint index, GLsizei bufSize, GLsizei *length, GLint *size, GLenum
    *type, GLchar *name)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glBindAttribLocation(GLuint
    program, GLuint index, const GLchar *name)': names 'GLchar', which has no
    cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glDrawBuffers(GLsizei n, const
    GLenum *bufs)': names 'GLenum', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glUniformMatrix4x3fv(GLint
    location, GLsizei count, GLboolean transpose, const GLfloat *value)':
    names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glUniformMatrix3x4fv(GLint
    location, GLsizei count, GLboolean transpose, const GLfloat *value)':
    names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glUniformMatrix4x2fv(GLint
    location, GLsizei count, GLboolean transpose, const GLfloat *value)':
    names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glUniformMatrix2x4fv(GLint
    location, GLsizei count, GLboolean transpose, const GLfloat *value)':
    names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glUniformMatrix3x2fv(GLint
    location, GLsizei count, GLboolean transpose, const GLfloat *value)':
    names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glUniformMatrix2x3fv(GLint
    location, GLsizei count, GLboolean transpose, const GLfloat *value)':
    names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glGenVertexArrays(GLsizei n, GLuint
    *arrays)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glDeleteVertexArrays(GLsizei n,
    const GLuint *arrays)': names 'GLuint', which has no cute class yet.
  - Qt's 'GLvoid *QOpenGLFunctions_4_0_Core::glMapBufferRange(GLenum target,
    GLintptr offset, GLsizeiptr length, GLbitfield access)': gives 'GLvoid',
    which has no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_0_Core::glGetFramebufferAttachmentParameteriv(GLenum
    target, GLenum attachment, GLenum pname, GLint *params)': takes a number
    to change where it is.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glGenFramebuffers(GLsizei n, GLuint
    *framebuffers)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glDeleteFramebuffers(GLsizei n,
    const GLuint *framebuffers)': names 'GLuint', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glGetRenderbufferParameteriv(GLenum
    target, GLenum pname, GLint *params)': takes a number to change where it
    is.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glGenRenderbuffers(GLsizei n,
    GLuint *renderbuffers)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glDeleteRenderbuffers(GLsizei n,
    const GLuint *renderbuffers)': names 'GLuint', which has no cute class
    yet.
  - Qt's 'const GLubyte *QOpenGLFunctions_4_0_Core::glGetStringi(GLenum name,
    GLuint index)': gives 'unsigned char', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glClearBufferfv(GLenum buffer,
    GLint drawbuffer, const GLfloat *value)': names 'GLfloat', which has no
    cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glClearBufferuiv(GLenum buffer,
    GLint drawbuffer, const GLuint *value)': names 'GLuint', which has no
    cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glClearBufferiv(GLenum buffer,
    GLint drawbuffer, const GLint *value)': names 'GLint', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glGetTexParameterIuiv(GLenum
    target, GLenum pname, GLuint *params)': takes a number to change where it
    is.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glGetTexParameterIiv(GLenum target,
    GLenum pname, GLint *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glTexParameterIuiv(GLenum target,
    GLenum pname, const GLuint *params)': names 'GLuint', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glTexParameterIiv(GLenum target,
    GLenum pname, const GLint *params)': names 'GLint', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glUniform4uiv(GLint location,
    GLsizei count, const GLuint *value)': names 'GLuint', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glUniform3uiv(GLint location,
    GLsizei count, const GLuint *value)': names 'GLuint', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glUniform2uiv(GLint location,
    GLsizei count, const GLuint *value)': names 'GLuint', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glUniform1uiv(GLint location,
    GLsizei count, const GLuint *value)': names 'GLuint', which has no cute
    class yet.
  - Qt's 'GLint QOpenGLFunctions_4_0_Core::glGetFragDataLocation(GLuint
    program, const GLchar *name)': names 'GLchar', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glBindFragDataLocation(GLuint
    program, GLuint color, const GLchar *name)': names 'GLchar', which has no
    cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glGetUniformuiv(GLuint program,
    GLint location, GLuint *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glGetVertexAttribIuiv(GLuint index,
    GLenum pname, GLuint *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glGetVertexAttribIiv(GLuint index,
    GLenum pname, GLint *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glVertexAttribIPointer(GLuint
    index, GLint size, GLenum type, GLsizei stride, const GLvoid *pointer)':
    names 'GLvoid', which has no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_0_Core::glGetTransformFeedbackVarying(GLuint program,
    GLuint index, GLsizei bufSize, GLsizei *length, GLsizei *size, GLenum
    *type, GLchar *name)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glTransformFeedbackVaryings(GLuint
    program, GLsizei count, const GLchar *const *varyings, GLenum
    bufferMode)': names 'GLchar *const', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glGetIntegeri_v(GLenum target,
    GLuint index, GLint *data)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glGetBooleani_v(GLenum target,
    GLuint index, GLboolean *data)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glGetActiveUniformBlockName(GLuint
    program, GLuint uniformBlockIndex, GLsizei bufSize, GLsizei *length,
    GLchar *uniformBlockName)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glGetActiveUniformBlockiv(GLuint
    program, GLuint uniformBlockIndex, GLenum pname, GLint *params)': takes a
    number to change where it is.
  - Qt's 'GLuint QOpenGLFunctions_4_0_Core::glGetUniformBlockIndex(GLuint
    program, const GLchar *uniformBlockName)': names 'GLchar', which has no
    cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glGetActiveUniformName(GLuint
    program, GLuint uniformIndex, GLsizei bufSize, GLsizei *length, GLchar
    *uniformName)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glGetActiveUniformsiv(GLuint
    program, GLsizei uniformCount, const GLuint *uniformIndices, GLenum
    pname, GLint *params)': names 'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glGetUniformIndices(GLuint program,
    GLsizei uniformCount, const GLchar *const *uniformNames, GLuint
    *uniformIndices)': names 'GLchar *const', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glDrawElementsInstanced(GLenum
    mode, GLsizei count, GLenum type, const GLvoid *indices, GLsizei
    instancecount)': names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glGetMultisamplefv(GLenum pname,
    GLuint index, GLfloat *val)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glGetSynciv(GLsync sync, GLenum
    pname, GLsizei bufSize, GLsizei *length, GLint *values)': names 'struct
    __GLsync', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glGetInteger64v(GLenum pname,
    GLint64 *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glWaitSync(GLsync sync, GLbitfield
    flags, GLuint64 timeout)': names 'struct __GLsync', which has no cute
    class yet.
  - Qt's 'GLenum QOpenGLFunctions_4_0_Core::glClientWaitSync(GLsync sync,
    GLbitfield flags, GLuint64 timeout)': names 'struct __GLsync', which has
    no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glDeleteSync(GLsync sync)': names
    'struct __GLsync', which has no cute class yet.
  - Qt's 'GLboolean QOpenGLFunctions_4_0_Core::glIsSync(GLsync sync)': names
    'struct __GLsync', which has no cute class yet.
  - Qt's 'GLsync QOpenGLFunctions_4_0_Core::glFenceSync(GLenum condition,
    GLbitfield flags)': gives a type Python has no way to take yet.
  - Qt's 'void
    QOpenGLFunctions_4_0_Core::glMultiDrawElementsBaseVertex(GLenum mode,
    const GLsizei *count, GLenum type, const GLvoid *const *indices, GLsizei
    drawcount, const GLint *basevertex)': names 'GLsizei', which has no cute
    class yet.
  - Qt's 'void
    QOpenGLFunctions_4_0_Core::glDrawElementsInstancedBaseVertex(GLenum mode,
    GLsizei count, GLenum type, const GLvoid *indices, GLsizei instancecount,
    GLint basevertex)': names 'GLvoid', which has no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_0_Core::glDrawRangeElementsBaseVertex(GLenum mode,
    GLuint start, GLuint end, GLsizei count, GLenum type, const GLvoid
    *indices, GLint basevertex)': names 'GLvoid', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glDrawElementsBaseVertex(GLenum
    mode, GLsizei count, GLenum type, const GLvoid *indices, GLint
    basevertex)': names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glGetBufferParameteri64v(GLenum
    target, GLenum pname, GLint64 *params)': takes a number to change where
    it is.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glGetInteger64i_v(GLenum target,
    GLuint index, GLint64 *data)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glVertexAttribP4uiv(GLuint index,
    GLenum type, GLboolean normalized, const GLuint *value)': names 'GLuint',
    which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glVertexAttribP3uiv(GLuint index,
    GLenum type, GLboolean normalized, const GLuint *value)': names 'GLuint',
    which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glVertexAttribP2uiv(GLuint index,
    GLenum type, GLboolean normalized, const GLuint *value)': names 'GLuint',
    which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glVertexAttribP1uiv(GLuint index,
    GLenum type, GLboolean normalized, const GLuint *value)': names 'GLuint',
    which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glGetQueryObjectui64v(GLuint id,
    GLenum pname, GLuint64 *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glGetQueryObjecti64v(GLuint id,
    GLenum pname, GLint64 *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glGetSamplerParameterIuiv(GLuint
    sampler, GLenum pname, GLuint *params)': takes a number to change where
    it is.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glGetSamplerParameterfv(GLuint
    sampler, GLenum pname, GLfloat *params)': takes a number to change where
    it is.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glGetSamplerParameterIiv(GLuint
    sampler, GLenum pname, GLint *params)': takes a number to change where it
    is.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glGetSamplerParameteriv(GLuint
    sampler, GLenum pname, GLint *params)': takes a number to change where it
    is.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glSamplerParameterIuiv(GLuint
    sampler, GLenum pname, const GLuint *param)': names 'GLuint', which has
    no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glSamplerParameterIiv(GLuint
    sampler, GLenum pname, const GLint *param)': names 'GLint', which has no
    cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glSamplerParameterfv(GLuint
    sampler, GLenum pname, const GLfloat *param)': names 'GLfloat', which has
    no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glSamplerParameteriv(GLuint
    sampler, GLenum pname, const GLint *param)': names 'GLint', which has no
    cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glDeleteSamplers(GLsizei count,
    const GLuint *samplers)': names 'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glGenSamplers(GLsizei count, GLuint
    *samplers)': takes a number to change where it is.
  - Qt's 'GLint QOpenGLFunctions_4_0_Core::glGetFragDataIndex(GLuint program,
    const GLchar *name)': names 'GLchar', which has no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_0_Core::glBindFragDataLocationIndexed(GLuint program,
    GLuint colorNumber, GLuint index, const GLchar *name)': names 'GLchar',
    which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glGetQueryIndexediv(GLenum target,
    GLuint index, GLenum pname, GLint *params)': takes a number to change
    where it is.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glGenTransformFeedbacks(GLsizei n,
    GLuint *ids)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glDeleteTransformFeedbacks(GLsizei
    n, const GLuint *ids)': names 'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glPatchParameterfv(GLenum pname,
    const GLfloat *values)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glGetProgramStageiv(GLuint program,
    GLenum shadertype, GLenum pname, GLint *values)': takes a number to
    change where it is.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glGetUniformSubroutineuiv(GLenum
    shadertype, GLint location, GLuint *params)': takes a number to change
    where it is.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glUniformSubroutinesuiv(GLenum
    shadertype, GLsizei count, const GLuint *indices)': names 'GLuint', which
    has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glGetActiveSubroutineName(GLuint
    program, GLenum shadertype, GLuint index, GLsizei bufsize, GLsizei
    *length, GLchar *name)': takes a number to change where it is.
  - Qt's 'void
    QOpenGLFunctions_4_0_Core::glGetActiveSubroutineUniformName(GLuint
    program, GLenum shadertype, GLuint index, GLsizei bufsize, GLsizei
    *length, GLchar *name)': takes a number to change where it is.
  - Qt's 'void
    QOpenGLFunctions_4_0_Core::glGetActiveSubroutineUniformiv(GLuint program,
    GLenum shadertype, GLuint index, GLenum pname, GLint *values)': takes a
    number to change where it is.
  - Qt's 'GLuint QOpenGLFunctions_4_0_Core::glGetSubroutineIndex(GLuint
    program, GLenum shadertype, const GLchar *name)': names 'GLchar', which
    has no cute class yet.
  - Qt's 'GLint
    QOpenGLFunctions_4_0_Core::glGetSubroutineUniformLocation(GLuint program,
    GLenum shadertype, const GLchar *name)': names 'GLchar', which has no
    cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glGetUniformdv(GLuint program,
    GLint location, GLdouble *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glUniformMatrix4x3dv(GLint
    location, GLsizei count, GLboolean transpose, const GLdouble *value)':
    names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glUniformMatrix4x2dv(GLint
    location, GLsizei count, GLboolean transpose, const GLdouble *value)':
    names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glUniformMatrix3x4dv(GLint
    location, GLsizei count, GLboolean transpose, const GLdouble *value)':
    names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glUniformMatrix3x2dv(GLint
    location, GLsizei count, GLboolean transpose, const GLdouble *value)':
    names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glUniformMatrix2x4dv(GLint
    location, GLsizei count, GLboolean transpose, const GLdouble *value)':
    names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glUniformMatrix2x3dv(GLint
    location, GLsizei count, GLboolean transpose, const GLdouble *value)':
    names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glUniformMatrix4dv(GLint location,
    GLsizei count, GLboolean transpose, const GLdouble *value)': names
    'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glUniformMatrix3dv(GLint location,
    GLsizei count, GLboolean transpose, const GLdouble *value)': names
    'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glUniformMatrix2dv(GLint location,
    GLsizei count, GLboolean transpose, const GLdouble *value)': names
    'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glUniform4dv(GLint location,
    GLsizei count, const GLdouble *value)': names 'GLdouble', which has no
    cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glUniform3dv(GLint location,
    GLsizei count, const GLdouble *value)': names 'GLdouble', which has no
    cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glUniform2dv(GLint location,
    GLsizei count, const GLdouble *value)': names 'GLdouble', which has no
    cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glUniform1dv(GLint location,
    GLsizei count, const GLdouble *value)': names 'GLdouble', which has no
    cute class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glDrawElementsIndirect(GLenum mode,
    GLenum type, const GLvoid *indirect)': names 'GLvoid', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_4_0_Core::glDrawArraysIndirect(GLenum mode,
    const GLvoid *indirect)': names 'GLvoid', which has no cute class yet.

  What to expect
  --------------

  - The C++ QOpenGLFunctions_4_0_Core is created at the first use, not by
    'QOpenGLFunctions_4_0_Core(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QOpenGLFunctions_4_0_Core.
  - Each name of Qt's QOpenGLFunctions_4_0_Core that has no cute function
    yet, 'glBindAttribLocation', 'glBindFragDataLocation',
    'glBindFragDataLocationIndexed', 'glBufferData', 'glBufferSubData',
    'glClearBufferfv', 'glClearBufferiv', 'glClearBufferuiv',
    'glClientWaitSync', 'glCompressedTexImage1D', 'glCompressedTexImage2D',
    'glCompressedTexImage3D', 'glCompressedTexSubImage1D',
    'glCompressedTexSubImage2D', 'glCompressedTexSubImage3D',
    'glDeleteBuffers', 'glDeleteFramebuffers', 'glDeleteQueries',
    'glDeleteRenderbuffers', 'glDeleteSamplers', 'glDeleteSync',
    'glDeleteTextures', 'glDeleteTransformFeedbacks', 'glDeleteVertexArrays',
    'glDrawArraysIndirect', 'glDrawBuffers', 'glDrawElements',
    'glDrawElementsBaseVertex', 'glDrawElementsIndirect',
    'glDrawElementsInstanced', 'glDrawElementsInstancedBaseVertex',
    'glDrawRangeElements', 'glDrawRangeElementsBaseVertex', 'glFenceSync',
    'glGenBuffers', 'glGenFramebuffers', 'glGenQueries',
    'glGenRenderbuffers', 'glGenSamplers', 'glGenTextures',
    'glGenTransformFeedbacks', 'glGenVertexArrays', 'glGetActiveAttrib',
    'glGetActiveSubroutineName', 'glGetActiveSubroutineUniformName',
    'glGetActiveSubroutineUniformiv', 'glGetActiveUniform',
    'glGetActiveUniformBlockName', 'glGetActiveUniformBlockiv',
    'glGetActiveUniformName', 'glGetActiveUniformsiv',
    'glGetAttachedShaders', 'glGetAttribLocation', 'glGetBooleani_v',
    'glGetBooleanv', 'glGetBufferParameteri64v', 'glGetBufferParameteriv',
    'glGetBufferPointerv', 'glGetBufferSubData', 'glGetCompressedTexImage',
    'glGetDoublev', 'glGetFloatv', 'glGetFragDataIndex',
    'glGetFragDataLocation', 'glGetFramebufferAttachmentParameteriv',
    'glGetInteger64i_v', 'glGetInteger64v', 'glGetIntegeri_v',
    'glGetIntegerv', 'glGetMultisamplefv', 'glGetProgramInfoLog',
    'glGetProgramStageiv', 'glGetProgramiv', 'glGetQueryIndexediv',
    'glGetQueryObjecti64v', 'glGetQueryObjectiv', 'glGetQueryObjectui64v',
    'glGetQueryObjectuiv', 'glGetQueryiv', 'glGetRenderbufferParameteriv',
    'glGetSamplerParameterIiv', 'glGetSamplerParameterIuiv',
    'glGetSamplerParameterfv', 'glGetSamplerParameteriv',
    'glGetShaderInfoLog', 'glGetShaderSource', 'glGetShaderiv',
    'glGetString', 'glGetStringi', 'glGetSubroutineIndex',
    'glGetSubroutineUniformLocation', 'glGetSynciv', 'glGetTexImage',
    'glGetTexLevelParameterfv', 'glGetTexLevelParameteriv',
    'glGetTexParameterIiv', 'glGetTexParameterIuiv', 'glGetTexParameterfv',
    'glGetTexParameteriv', 'glGetTransformFeedbackVarying',
    'glGetUniformBlockIndex', 'glGetUniformIndices', 'glGetUniformLocation',
    'glGetUniformSubroutineuiv', 'glGetUniformdv', 'glGetUniformfv',
    'glGetUniformiv', 'glGetUniformuiv', 'glGetVertexAttribIiv',
    'glGetVertexAttribIuiv', 'glGetVertexAttribPointerv',
    'glGetVertexAttribdv', 'glGetVertexAttribfv', 'glGetVertexAttribiv',
    'glIsSync', 'glMapBuffer', 'glMapBufferRange', 'glMultiDrawArrays',
    'glMultiDrawElements', 'glMultiDrawElementsBaseVertex',
    'glPatchParameterfv', 'glPointParameterfv', 'glPointParameteriv',
    'glReadPixels', 'glSamplerParameterIiv', 'glSamplerParameterIuiv',
    'glSamplerParameterfv', 'glSamplerParameteriv', 'glShaderSource',
    'glTexImage1D', 'glTexImage2D', 'glTexImage3D', 'glTexParameterIiv',
    'glTexParameterIuiv', 'glTexParameterfv', 'glTexParameteriv',
    'glTexSubImage1D', 'glTexSubImage2D', 'glTexSubImage3D',
    'glTransformFeedbackVaryings', 'glUniform1dv', 'glUniform1fv',
    'glUniform1iv', 'glUniform1uiv', 'glUniform2dv', 'glUniform2fv',
    'glUniform2iv', 'glUniform2uiv', 'glUniform3dv', 'glUniform3fv',
    'glUniform3iv', 'glUniform3uiv', 'glUniform4dv', 'glUniform4fv',
    'glUniform4iv', 'glUniform4uiv', 'glUniformMatrix2dv',
    'glUniformMatrix2fv', 'glUniformMatrix2x3dv', 'glUniformMatrix2x3fv',
    'glUniformMatrix2x4dv', 'glUniformMatrix2x4fv', 'glUniformMatrix3dv',
    'glUniformMatrix3fv', 'glUniformMatrix3x2dv', 'glUniformMatrix3x2fv',
    'glUniformMatrix3x4dv', 'glUniformMatrix3x4fv', 'glUniformMatrix4dv',
    'glUniformMatrix4fv', 'glUniformMatrix4x2dv', 'glUniformMatrix4x2fv',
    'glUniformMatrix4x3dv', 'glUniformMatrix4x3fv',
    'glUniformSubroutinesuiv', 'glVertexAttribIPointer',
    'glVertexAttribP1uiv', 'glVertexAttribP2uiv', 'glVertexAttribP3uiv',
    'glVertexAttribP4uiv', 'glVertexAttribPointer', 'glWaitSync', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QOpenGLContext)
  @overload(NoneType)
  def isContextCompatible(context: Optional[QOpenGLContext]) -> bool:
    """
    Calls Qt's 'bool
    QOpenGLFunctions_4_0_Core::isContextCompatible(QOpenGLContext *context)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#isContextCompatible

    Parameters
    ----------

    context : Optional[QOpenGLContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QOpenGLFunctions_4_0_Core::isContextCompatible(QOpenGLContext
    #      *context)
    return Rituals.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core19isContextCompatibleEP14QOpen'
        'GLContext',
        CuteMixin._addressOf(context),
    )

  @staticmethod
  def versionProfile() -> QOpenGLVersionProfile:
    """
    Calls Qt's 'QOpenGLVersionProfile
    QOpenGLFunctions_4_0_Core::versionProfile()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#versionProfile

    Returns
    -------

    QOpenGLVersionProfile
      A new cute QOpenGLVersionProfile around the copy Qt gave back. Python
      owns it.
    """
    #  QOpenGLVersionProfile QOpenGLFunctions_4_0_Core::versionProfile()
    address = Rituals.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core14versionProfileEv',
    )
    from . import QOpenGLVersionProfile
    return QOpenGLVersionProfile._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpenGLFunctions_4_0_Core'

  #  A C++ QOpenGLFunctions_4_0_Core Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QOpenGLFunctions_4_0_Core'

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
    'QOpenGLFunctions_4_0_Core::QOpenGLFunctions_4_0_Core()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html
    """
    #  QOpenGLFunctions_4_0_Core::QOpenGLFunctions_4_0_Core()
    self._noteCreation(QOpenGLFunctions_4_0_Core, lambda: Rituals.call(
        'ritual_ZN25QOpenGLFunctions_4_0_CoreC1Ev',
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

  def initializeOpenGLFunctions(self) -> bool:
    """
    Calls Qt's 'bool QOpenGLFunctions_4_0_Core::initializeOpenGLFunctions()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html
    """
    #  bool QOpenGLFunctions_4_0_Core::initializeOpenGLFunctions()
    ritual = (
        'ritual_ZN25QOpenGLFunctions_4_0_Core25initializeOpenGLFunctionsEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QOpenGLFunctions_4_0_Core25initializeOpenGLFuncti'
          'onsEv')
    return self.uglySide.call(ritual)

  @overload(int, int, int, int)
  def glViewport(self, x: int, y: int, width: int, height: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glViewport(GLint x, GLint y,
    GLsizei width, GLsizei height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glViewport

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
    #  void QOpenGLFunctions_4_0_Core::glViewport(GLint x, GLint y, GLsizei
    #      width, GLsizei height)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core10glViewportEiiii',
        x, y, width, height,
    )

  @overload(float, float)
  def glDepthRange(self, nearVal: float, farVal: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glDepthRange(GLdouble
    nearVal, GLdouble farVal)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glDepthRange

    Parameters
    ----------

    nearVal : float
      Passed on as it is.

    farVal : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glDepthRange(GLdouble nearVal,
    #      GLdouble farVal)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core12glDepthRangeEdd',
        nearVal, farVal,
    )

  @overload(int)
  def glIsEnabled(self, cap: int) -> int:
    """
    Calls Qt's 'GLboolean QOpenGLFunctions_4_0_Core::glIsEnabled(GLenum
    cap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glIsEnabled

    Parameters
    ----------

    cap : int
      Passed on as it is.
    """
    #  GLboolean QOpenGLFunctions_4_0_Core::glIsEnabled(GLenum cap)
    return self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core11glIsEnabledEj', cap,
    )

  def glGetError(self) -> int:
    """
    Calls Qt's 'GLenum QOpenGLFunctions_4_0_Core::glGetError()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glGetError
    """
    #  GLenum QOpenGLFunctions_4_0_Core::glGetError()
    return self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core10glGetErrorEv',
    )

  @overload(int)
  def glReadBuffer(self, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glReadBuffer(GLenum mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glReadBuffer

    Parameters
    ----------

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glReadBuffer(GLenum mode)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core12glReadBufferEj', mode,
    )

  @overload(int, int)
  def glPixelStorei(self, pname: int, param: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glPixelStorei(GLenum pname,
    GLint param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glPixelStorei

    Parameters
    ----------

    pname : int
      Passed on as it is.

    param : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glPixelStorei(GLenum pname, GLint
    #      param)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core13glPixelStoreiEji',
        pname, param,
    )

  @overload(int, float)
  def glPixelStoref(self, pname: int, param: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glPixelStoref(GLenum pname,
    GLfloat param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glPixelStoref

    Parameters
    ----------

    pname : int
      Passed on as it is.

    param : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glPixelStoref(GLenum pname, GLfloat
    #      param)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core13glPixelStorefEjf',
        pname, param,
    )

  @overload(int)
  def glDepthFunc(self, func: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glDepthFunc(GLenum func)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glDepthFunc

    Parameters
    ----------

    func : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glDepthFunc(GLenum func)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core11glDepthFuncEj', func,
    )

  @overload(int, int, int)
  def glStencilOp(self, fail: int, zfail: int, zpass: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glStencilOp(GLenum fail,
    GLenum zfail, GLenum zpass)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glStencilOp

    Parameters
    ----------

    fail : int
      Passed on as it is.

    zfail : int
      Passed on as it is.

    zpass : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glStencilOp(GLenum fail, GLenum zfail,
    #      GLenum zpass)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core11glStencilOpEjjj',
        fail, zfail, zpass,
    )

  @overload(int, int, int)
  def glStencilFunc(self, func: int, ref: int, mask: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glStencilFunc(GLenum func,
    GLint ref, GLuint mask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glStencilFunc

    Parameters
    ----------

    func : int
      Passed on as it is.

    ref : int
      Passed on as it is.

    mask : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glStencilFunc(GLenum func, GLint ref,
    #      GLuint mask)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core13glStencilFuncEjij',
        func, ref, mask,
    )

  @overload(int)
  def glLogicOp(self, opcode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glLogicOp(GLenum opcode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glLogicOp

    Parameters
    ----------

    opcode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glLogicOp(GLenum opcode)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core9glLogicOpEj', opcode,
    )

  @overload(int, int)
  def glBlendFunc(self, sfactor: int, dfactor: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glBlendFunc(GLenum sfactor,
    GLenum dfactor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glBlendFunc

    Parameters
    ----------

    sfactor : int
      Passed on as it is.

    dfactor : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glBlendFunc(GLenum sfactor, GLenum
    #      dfactor)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core11glBlendFuncEjj',
        sfactor, dfactor,
    )

  def glFlush(self) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glFlush()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glFlush
    """
    #  void QOpenGLFunctions_4_0_Core::glFlush()
    self.uglySide.call('ritual_ZN25QOpenGLFunctions_4_0_Core7glFlushEv')

  def glFinish(self) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glFinish()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glFinish
    """
    #  void QOpenGLFunctions_4_0_Core::glFinish()
    self.uglySide.call('ritual_ZN25QOpenGLFunctions_4_0_Core8glFinishEv')

  @overload(int)
  def glEnable(self, cap: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glEnable(GLenum cap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glEnable

    Parameters
    ----------

    cap : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glEnable(GLenum cap)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core8glEnableEj', cap,
    )

  @overload(int)
  def glDisable(self, cap: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glDisable(GLenum cap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glDisable

    Parameters
    ----------

    cap : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glDisable(GLenum cap)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core9glDisableEj', cap,
    )

  @overload(int)
  def glDepthMask(self, flag: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glDepthMask(GLboolean flag)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glDepthMask

    Parameters
    ----------

    flag : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glDepthMask(GLboolean flag)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core11glDepthMaskEh', flag,
    )

  @overload(int, int, int, int)
  def glColorMask(self, red: int, green: int, blue: int, alpha: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glColorMask(GLboolean red,
    GLboolean green, GLboolean blue, GLboolean alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glColorMask

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
    #  void QOpenGLFunctions_4_0_Core::glColorMask(GLboolean red, GLboolean
    #      green, GLboolean blue, GLboolean alpha)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core11glColorMaskEhhhh',
        red, green, blue, alpha,
    )

  @overload(int)
  def glStencilMask(self, mask: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glStencilMask(GLuint mask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glStencilMask

    Parameters
    ----------

    mask : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glStencilMask(GLuint mask)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core13glStencilMaskEj', mask,
    )

  @overload(float)
  def glClearDepth(self, depth: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glClearDepth(GLdouble
    depth)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glClearDepth

    Parameters
    ----------

    depth : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glClearDepth(GLdouble depth)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core12glClearDepthEd', depth,
    )

  @overload(int)
  def glClearStencil(self, s: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glClearStencil(GLint s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glClearStencil

    Parameters
    ----------

    s : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glClearStencil(GLint s)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core14glClearStencilEi', s,
    )

  @overload(float, float, float, float)
  def glClearColor(
      self,
      red: float,
      green: float,
      blue: float,
      alpha: float,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glClearColor(GLfloat red,
    GLfloat green, GLfloat blue, GLfloat alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glClearColor

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
    #  void QOpenGLFunctions_4_0_Core::glClearColor(GLfloat red, GLfloat
    #      green, GLfloat blue, GLfloat alpha)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core12glClearColorEffff',
        red, green, blue, alpha,
    )

  @overload(int)
  def glClear(self, mask: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glClear(GLbitfield mask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glClear

    Parameters
    ----------

    mask : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glClear(GLbitfield mask)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core7glClearEj', mask,
    )

  @overload(int)
  def glDrawBuffer(self, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glDrawBuffer(GLenum mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glDrawBuffer

    Parameters
    ----------

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glDrawBuffer(GLenum mode)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core12glDrawBufferEj', mode,
    )

  @overload(int, int, int)
  def glTexParameteri(self, target: int, pname: int, param: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glTexParameteri(GLenum
    target, GLenum pname, GLint param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glTexParameteri

    Parameters
    ----------

    target : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    param : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glTexParameteri(GLenum target, GLenum
    #      pname, GLint param)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core15glTexParameteriEjji',
        target, pname, param,
    )

  @overload(int, int, float)
  def glTexParameterf(self, target: int, pname: int, param: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glTexParameterf(GLenum
    target, GLenum pname, GLfloat param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glTexParameterf

    Parameters
    ----------

    target : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    param : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glTexParameterf(GLenum target, GLenum
    #      pname, GLfloat param)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core15glTexParameterfEjjf',
        target, pname, param,
    )

  @overload(int, int, int, int)
  def glScissor(self, x: int, y: int, width: int, height: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glScissor(GLint x, GLint y,
    GLsizei width, GLsizei height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glScissor

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
    #  void QOpenGLFunctions_4_0_Core::glScissor(GLint x, GLint y, GLsizei
    #      width, GLsizei height)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core9glScissorEiiii',
        x, y, width, height,
    )

  @overload(int, int)
  def glPolygonMode(self, face: int, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glPolygonMode(GLenum face,
    GLenum mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glPolygonMode

    Parameters
    ----------

    face : int
      Passed on as it is.

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glPolygonMode(GLenum face, GLenum
    #      mode)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core13glPolygonModeEjj', face, mode,
    )

  @overload(float)
  def glPointSize(self, size: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glPointSize(GLfloat size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glPointSize

    Parameters
    ----------

    size : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glPointSize(GLfloat size)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core11glPointSizeEf', size,
    )

  @overload(float)
  def glLineWidth(self, width: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glLineWidth(GLfloat width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glLineWidth

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glLineWidth(GLfloat width)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core11glLineWidthEf', width,
    )

  @overload(int, int)
  def glHint(self, target: int, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glHint(GLenum target, GLenum
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glHint

    Parameters
    ----------

    target : int
      Passed on as it is.

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glHint(GLenum target, GLenum mode)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core6glHintEjj', target, mode,
    )

  @overload(int)
  def glFrontFace(self, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glFrontFace(GLenum mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glFrontFace

    Parameters
    ----------

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glFrontFace(GLenum mode)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core11glFrontFaceEj', mode,
    )

  @overload(int)
  def glCullFace(self, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glCullFace(GLenum mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glCullFace

    Parameters
    ----------

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glCullFace(GLenum mode)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core10glCullFaceEj', mode,
    )

  @overload(int)
  def glIsTexture(self, texture: int) -> int:
    """
    Calls Qt's 'GLboolean QOpenGLFunctions_4_0_Core::glIsTexture(GLuint
    texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glIsTexture

    Parameters
    ----------

    texture : int
      Passed on as it is.
    """
    #  GLboolean QOpenGLFunctions_4_0_Core::glIsTexture(GLuint texture)
    return self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core11glIsTextureEj', texture,
    )

  @overload(int, int)
  def glBindTexture(self, target: int, texture: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glBindTexture(GLenum target,
    GLuint texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glBindTexture

    Parameters
    ----------

    target : int
      Passed on as it is.

    texture : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glBindTexture(GLenum target, GLuint
    #      texture)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core13glBindTextureEjj',
        target, texture,
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
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glCopyTexSubImage2D(GLenum
    target, GLint level, GLint xoffset, GLint yoffset, GLint x, GLint y,
    GLsizei width, GLsizei height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glCopyTexSubImage2D

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
    #  void QOpenGLFunctions_4_0_Core::glCopyTexSubImage2D(GLenum target,
    #      GLint level, GLint xoffset, GLint yoffset, GLint x, GLint y,
    #      GLsizei width, GLsizei height)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core19glCopyTexSubImage2DEjiiiiiii',
        target, level, xoffset, yoffset, x, y, width, height,
    )

  @overload(int, int, int, int, int, int)
  def glCopyTexSubImage1D(
      self,
      target: int,
      level: int,
      xoffset: int,
      x: int,
      y: int,
      width: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glCopyTexSubImage1D(GLenum
    target, GLint level, GLint xoffset, GLint x, GLint y, GLsizei width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glCopyTexSubImage1D

    Parameters
    ----------

    target : int
      Passed on as it is.

    level : int
      Passed on as it is.

    xoffset : int
      Passed on as it is.

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    width : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glCopyTexSubImage1D(GLenum target,
    #      GLint level, GLint xoffset, GLint x, GLint y, GLsizei width)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core19glCopyTexSubImage1DEjiiiii',
        target, level, xoffset, x, y, width,
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
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glCopyTexImage2D(GLenum
    target, GLint level, GLenum internalformat, GLint x, GLint y, GLsizei
    width, GLsizei height, GLint border)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glCopyTexImage2D

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
    #  void QOpenGLFunctions_4_0_Core::glCopyTexImage2D(GLenum target, GLint
    #      level, GLenum internalformat, GLint x, GLint y, GLsizei width,
    #      GLsizei height, GLint border)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core16glCopyTexImage2DEjijiiiii',
        target, level, internalformat, x, y, width, height, border,
    )

  @overload(int, int, int, int, int, int, int)
  def glCopyTexImage1D(
      self,
      target: int,
      level: int,
      internalformat: int,
      x: int,
      y: int,
      width: int,
      border: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glCopyTexImage1D(GLenum
    target, GLint level, GLenum internalformat, GLint x, GLint y, GLsizei
    width, GLint border)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glCopyTexImage1D

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

    border : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glCopyTexImage1D(GLenum target, GLint
    #      level, GLenum internalformat, GLint x, GLint y, GLsizei width,
    #      GLint border)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core16glCopyTexImage1DEjijiiii',
        target, level, internalformat, x, y, width, border,
    )

  @overload(float, float)
  def glPolygonOffset(self, factor: float, units: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glPolygonOffset(GLfloat
    factor, GLfloat units)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glPolygonOffset

    Parameters
    ----------

    factor : float
      Passed on as it is.

    units : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glPolygonOffset(GLfloat factor,
    #      GLfloat units)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core15glPolygonOffsetEff',
        factor, units,
    )

  @overload(int, int, int)
  def glDrawArrays(self, mode: int, first: int, count: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glDrawArrays(GLenum mode,
    GLint first, GLsizei count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glDrawArrays

    Parameters
    ----------

    mode : int
      Passed on as it is.

    first : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glDrawArrays(GLenum mode, GLint first,
    #      GLsizei count)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core12glDrawArraysEjii',
        mode, first, count,
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
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glCopyTexSubImage3D(GLenum
    target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLint
    x, GLint y, GLsizei width, GLsizei height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glCopyTexSubImage3D

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
    #  void QOpenGLFunctions_4_0_Core::glCopyTexSubImage3D(GLenum target,
    #      GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLint x,
    #      GLint y, GLsizei width, GLsizei height)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core19glCopyTexSubImage3DEjiiiiiii'
        'i',
        target, level, xoffset, yoffset, zoffset, x, y, width, height,
    )

  @overload(int)
  def glBlendEquation(self, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glBlendEquation(GLenum
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glBlendEquation

    Parameters
    ----------

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glBlendEquation(GLenum mode)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core15glBlendEquationEj', mode,
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
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glBlendColor(GLfloat red,
    GLfloat green, GLfloat blue, GLfloat alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glBlendColor

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
    #  void QOpenGLFunctions_4_0_Core::glBlendColor(GLfloat red, GLfloat
    #      green, GLfloat blue, GLfloat alpha)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core12glBlendColorEffff',
        red, green, blue, alpha,
    )

  @overload(float, int)
  def glSampleCoverage(self, value: float, invert: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glSampleCoverage(GLfloat
    value, GLboolean invert)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glSampleCoverage

    Parameters
    ----------

    value : float
      Passed on as it is.

    invert : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glSampleCoverage(GLfloat value,
    #      GLboolean invert)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core16glSampleCoverageEfh',
        value, invert,
    )

  @overload(int)
  def glActiveTexture(self, texture: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glActiveTexture(GLenum
    texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glActiveTexture

    Parameters
    ----------

    texture : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glActiveTexture(GLenum texture)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core15glActiveTextureEj', texture,
    )

  @overload(int, int)
  def glPointParameteri(self, pname: int, param: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glPointParameteri(GLenum
    pname, GLint param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glPointParameteri

    Parameters
    ----------

    pname : int
      Passed on as it is.

    param : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glPointParameteri(GLenum pname, GLint
    #      param)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core17glPointParameteriEji',
        pname, param,
    )

  @overload(int, float)
  def glPointParameterf(self, pname: int, param: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glPointParameterf(GLenum
    pname, GLfloat param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glPointParameterf

    Parameters
    ----------

    pname : int
      Passed on as it is.

    param : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glPointParameterf(GLenum pname,
    #      GLfloat param)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core17glPointParameterfEjf',
        pname, param,
    )

  @overload(int, int, int, int)
  def glBlendFuncSeparate(
      self,
      sfactorRGB: int,
      dfactorRGB: int,
      sfactorAlpha: int,
      dfactorAlpha: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glBlendFuncSeparate(GLenum
    sfactorRGB, GLenum dfactorRGB, GLenum sfactorAlpha, GLenum
    dfactorAlpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glBlendFuncSeparate

    Parameters
    ----------

    sfactorRGB : int
      Passed on as it is.

    dfactorRGB : int
      Passed on as it is.

    sfactorAlpha : int
      Passed on as it is.

    dfactorAlpha : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glBlendFuncSeparate(GLenum sfactorRGB,
    #      GLenum dfactorRGB, GLenum sfactorAlpha, GLenum dfactorAlpha)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core19glBlendFuncSeparateEjjjj',
        sfactorRGB, dfactorRGB, sfactorAlpha, dfactorAlpha,
    )

  @overload(int)
  def glUnmapBuffer(self, target: int) -> int:
    """
    Calls Qt's 'GLboolean QOpenGLFunctions_4_0_Core::glUnmapBuffer(GLenum
    target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glUnmapBuffer

    Parameters
    ----------

    target : int
      Passed on as it is.
    """
    #  GLboolean QOpenGLFunctions_4_0_Core::glUnmapBuffer(GLenum target)
    return self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core13glUnmapBufferEj', target,
    )

  @overload(int)
  def glIsBuffer(self, buffer: int) -> int:
    """
    Calls Qt's 'GLboolean QOpenGLFunctions_4_0_Core::glIsBuffer(GLuint
    buffer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glIsBuffer

    Parameters
    ----------

    buffer : int
      Passed on as it is.
    """
    #  GLboolean QOpenGLFunctions_4_0_Core::glIsBuffer(GLuint buffer)
    return self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core10glIsBufferEj', buffer,
    )

  @overload(int, int)
  def glBindBuffer(self, target: int, buffer: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glBindBuffer(GLenum target,
    GLuint buffer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glBindBuffer

    Parameters
    ----------

    target : int
      Passed on as it is.

    buffer : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glBindBuffer(GLenum target, GLuint
    #      buffer)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core12glBindBufferEjj',
        target, buffer,
    )

  @overload(int)
  def glEndQuery(self, target: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glEndQuery(GLenum target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glEndQuery

    Parameters
    ----------

    target : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glEndQuery(GLenum target)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core10glEndQueryEj', target,
    )

  @overload(int, int)
  def glBeginQuery(self, target: int, id: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glBeginQuery(GLenum target,
    GLuint id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glBeginQuery

    Parameters
    ----------

    target : int
      Passed on as it is.

    id : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glBeginQuery(GLenum target, GLuint id)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core12glBeginQueryEjj', target, id,
    )

  @overload(int)
  def glIsQuery(self, id: int) -> int:
    """
    Calls Qt's 'GLboolean QOpenGLFunctions_4_0_Core::glIsQuery(GLuint id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glIsQuery

    Parameters
    ----------

    id : int
      Passed on as it is.
    """
    #  GLboolean QOpenGLFunctions_4_0_Core::glIsQuery(GLuint id)
    return self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core9glIsQueryEj', id,
    )

  @overload(int)
  def glValidateProgram(self, program: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glValidateProgram(GLuint
    program)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glValidateProgram

    Parameters
    ----------

    program : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glValidateProgram(GLuint program)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core17glValidateProgramEj', program,
    )

  @overload(int, int, int, int, int)
  def glUniform4i(
      self,
      location: int,
      v0: int,
      v1: int,
      v2: int,
      v3: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glUniform4i(GLint location,
    GLint v0, GLint v1, GLint v2, GLint v3)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glUniform4i

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
    #  void QOpenGLFunctions_4_0_Core::glUniform4i(GLint location, GLint v0,
    #      GLint v1, GLint v2, GLint v3)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core11glUniform4iEiiiii',
        location, v0, v1, v2, v3,
    )

  @overload(int, int, int, int)
  def glUniform3i(self, location: int, v0: int, v1: int, v2: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glUniform3i(GLint location,
    GLint v0, GLint v1, GLint v2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glUniform3i

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
    #  void QOpenGLFunctions_4_0_Core::glUniform3i(GLint location, GLint v0,
    #      GLint v1, GLint v2)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core11glUniform3iEiiii',
        location, v0, v1, v2,
    )

  @overload(int, int, int)
  def glUniform2i(self, location: int, v0: int, v1: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glUniform2i(GLint location,
    GLint v0, GLint v1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glUniform2i

    Parameters
    ----------

    location : int
      Passed on as it is.

    v0 : int
      Passed on as it is.

    v1 : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glUniform2i(GLint location, GLint v0,
    #      GLint v1)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core11glUniform2iEiii',
        location, v0, v1,
    )

  @overload(int, int)
  def glUniform1i(self, location: int, v0: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glUniform1i(GLint location,
    GLint v0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glUniform1i

    Parameters
    ----------

    location : int
      Passed on as it is.

    v0 : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glUniform1i(GLint location, GLint v0)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core11glUniform1iEii', location, v0,
    )

  @overload(int, float, float, float, float)
  def glUniform4f(
      self,
      location: int,
      v0: float,
      v1: float,
      v2: float,
      v3: float,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glUniform4f(GLint location,
    GLfloat v0, GLfloat v1, GLfloat v2, GLfloat v3)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glUniform4f

    Parameters
    ----------

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
    #  void QOpenGLFunctions_4_0_Core::glUniform4f(GLint location, GLfloat
    #      v0, GLfloat v1, GLfloat v2, GLfloat v3)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core11glUniform4fEiffff',
        location, v0, v1, v2, v3,
    )

  @overload(int, float, float, float)
  def glUniform3f(
      self,
      location: int,
      v0: float,
      v1: float,
      v2: float,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glUniform3f(GLint location,
    GLfloat v0, GLfloat v1, GLfloat v2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glUniform3f

    Parameters
    ----------

    location : int
      Passed on as it is.

    v0 : float
      Passed on as it is.

    v1 : float
      Passed on as it is.

    v2 : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glUniform3f(GLint location, GLfloat
    #      v0, GLfloat v1, GLfloat v2)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core11glUniform3fEifff',
        location, v0, v1, v2,
    )

  @overload(int, float, float)
  def glUniform2f(self, location: int, v0: float, v1: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glUniform2f(GLint location,
    GLfloat v0, GLfloat v1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glUniform2f

    Parameters
    ----------

    location : int
      Passed on as it is.

    v0 : float
      Passed on as it is.

    v1 : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glUniform2f(GLint location, GLfloat
    #      v0, GLfloat v1)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core11glUniform2fEiff',
        location, v0, v1,
    )

  @overload(int, float)
  def glUniform1f(self, location: int, v0: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glUniform1f(GLint location,
    GLfloat v0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glUniform1f

    Parameters
    ----------

    location : int
      Passed on as it is.

    v0 : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glUniform1f(GLint location, GLfloat
    #      v0)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core11glUniform1fEif', location, v0,
    )

  @overload(int)
  def glUseProgram(self, program: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glUseProgram(GLuint
    program)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glUseProgram

    Parameters
    ----------

    program : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glUseProgram(GLuint program)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core12glUseProgramEj', program,
    )

  @overload(int)
  def glLinkProgram(self, program: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glLinkProgram(GLuint
    program)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glLinkProgram

    Parameters
    ----------

    program : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glLinkProgram(GLuint program)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core13glLinkProgramEj', program,
    )

  @overload(int)
  def glIsShader(self, shader: int) -> int:
    """
    Calls Qt's 'GLboolean QOpenGLFunctions_4_0_Core::glIsShader(GLuint
    shader)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glIsShader

    Parameters
    ----------

    shader : int
      Passed on as it is.
    """
    #  GLboolean QOpenGLFunctions_4_0_Core::glIsShader(GLuint shader)
    return self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core10glIsShaderEj', shader,
    )

  @overload(int)
  def glIsProgram(self, program: int) -> int:
    """
    Calls Qt's 'GLboolean QOpenGLFunctions_4_0_Core::glIsProgram(GLuint
    program)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glIsProgram

    Parameters
    ----------

    program : int
      Passed on as it is.
    """
    #  GLboolean QOpenGLFunctions_4_0_Core::glIsProgram(GLuint program)
    return self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core11glIsProgramEj', program,
    )

  @overload(int)
  def glEnableVertexAttribArray(self, index: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_0_Core::glEnableVertexAttribArray(GLuint index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glEnableVertexAttribArray(GLuint
    #      index)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core25glEnableVertexAttribArrayEj',
        index,
    )

  @overload(int)
  def glDisableVertexAttribArray(self, index: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_0_Core::glDisableVertexAttribArray(GLuint index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glDisableVertexAttribArray(GLuint
    #      index)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core26glDisableVertexAttribArrayEj',
        index,
    )

  @overload(int, int)
  def glDetachShader(self, program: int, shader: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glDetachShader(GLuint
    program, GLuint shader)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glDetachShader

    Parameters
    ----------

    program : int
      Passed on as it is.

    shader : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glDetachShader(GLuint program, GLuint
    #      shader)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core14glDetachShaderEjj',
        program, shader,
    )

  @overload(int)
  def glDeleteShader(self, shader: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glDeleteShader(GLuint
    shader)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glDeleteShader

    Parameters
    ----------

    shader : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glDeleteShader(GLuint shader)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core14glDeleteShaderEj', shader,
    )

  @overload(int)
  def glDeleteProgram(self, program: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glDeleteProgram(GLuint
    program)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glDeleteProgram

    Parameters
    ----------

    program : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glDeleteProgram(GLuint program)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core15glDeleteProgramEj', program,
    )

  @overload(int)
  def glCreateShader(self, type: int) -> int:
    """
    Calls Qt's 'GLuint QOpenGLFunctions_4_0_Core::glCreateShader(GLenum
    type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glCreateShader

    Parameters
    ----------

    type : int
      Passed on as it is.
    """
    #  GLuint QOpenGLFunctions_4_0_Core::glCreateShader(GLenum type)
    return self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core14glCreateShaderEj', type,
    )

  def glCreateProgram(self) -> int:
    """
    Calls Qt's 'GLuint QOpenGLFunctions_4_0_Core::glCreateProgram()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glCreateProgram
    """
    #  GLuint QOpenGLFunctions_4_0_Core::glCreateProgram()
    return self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core15glCreateProgramEv',
    )

  @overload(int)
  def glCompileShader(self, shader: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glCompileShader(GLuint
    shader)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glCompileShader

    Parameters
    ----------

    shader : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glCompileShader(GLuint shader)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core15glCompileShaderEj', shader,
    )

  @overload(int, int)
  def glAttachShader(self, program: int, shader: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glAttachShader(GLuint
    program, GLuint shader)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glAttachShader

    Parameters
    ----------

    program : int
      Passed on as it is.

    shader : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glAttachShader(GLuint program, GLuint
    #      shader)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core14glAttachShaderEjj',
        program, shader,
    )

  @overload(int, int)
  def glStencilMaskSeparate(self, face: int, mask: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glStencilMaskSeparate(GLenum
    face, GLuint mask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html

    Parameters
    ----------

    face : int
      Passed on as it is.

    mask : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glStencilMaskSeparate(GLenum face,
    #      GLuint mask)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core21glStencilMaskSeparateEjj',
        face, mask,
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
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glStencilFuncSeparate(GLenum
    face, GLenum func, GLint ref, GLuint mask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html

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
    #  void QOpenGLFunctions_4_0_Core::glStencilFuncSeparate(GLenum face,
    #      GLenum func, GLint ref, GLuint mask)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core21glStencilFuncSeparateEjjij',
        face, func, ref, mask,
    )

  @overload(int, int, int, int)
  def glStencilOpSeparate(
      self,
      face: int,
      sfail: int,
      dpfail: int,
      dppass: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glStencilOpSeparate(GLenum
    face, GLenum sfail, GLenum dpfail, GLenum dppass)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glStencilOpSeparate

    Parameters
    ----------

    face : int
      Passed on as it is.

    sfail : int
      Passed on as it is.

    dpfail : int
      Passed on as it is.

    dppass : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glStencilOpSeparate(GLenum face,
    #      GLenum sfail, GLenum dpfail, GLenum dppass)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core19glStencilOpSeparateEjjjj',
        face, sfail, dpfail, dppass,
    )

  @overload(int, int)
  def glBlendEquationSeparate(self, modeRGB: int, modeAlpha: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_0_Core::glBlendEquationSeparate(GLenum modeRGB, GLenum
    modeAlpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html

    Parameters
    ----------

    modeRGB : int
      Passed on as it is.

    modeAlpha : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glBlendEquationSeparate(GLenum
    #      modeRGB, GLenum modeAlpha)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core23glBlendEquationSeparateEjj',
        modeRGB, modeAlpha,
    )

  @overload(int)
  def glIsVertexArray(self, array: int) -> int:
    """
    Calls Qt's 'GLboolean QOpenGLFunctions_4_0_Core::glIsVertexArray(GLuint
    array)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glIsVertexArray

    Parameters
    ----------

    array : int
      Passed on as it is.
    """
    #  GLboolean QOpenGLFunctions_4_0_Core::glIsVertexArray(GLuint array)
    return self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core15glIsVertexArrayEj', array,
    )

  @overload(int)
  def glBindVertexArray(self, array: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glBindVertexArray(GLuint
    array)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glBindVertexArray

    Parameters
    ----------

    array : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glBindVertexArray(GLuint array)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core17glBindVertexArrayEj', array,
    )

  @overload(int, int, int)
  def glFlushMappedBufferRange(
      self,
      target: int,
      offset: int,
      length: int,
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_0_Core::glFlushMappedBufferRange(GLenum target,
    GLintptr offset, GLsizeiptr length)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html

    Parameters
    ----------

    target : int
      Passed on as it is.

    offset : int
      Passed on as it is.

    length : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glFlushMappedBufferRange(GLenum
    #      target, GLintptr offset, GLsizeiptr length)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core24glFlushMappedBufferRangeEjll',
        target, offset, length,
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
    Calls Qt's 'void
    QOpenGLFunctions_4_0_Core::glFramebufferTextureLayer(GLenum target,
    GLenum attachment, GLuint texture, GLint level, GLint layer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html

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
    #  void QOpenGLFunctions_4_0_Core::glFramebufferTextureLayer(GLenum
    #      target, GLenum attachment, GLuint texture, GLint level, GLint
    #      layer)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core25glFramebufferTextureLayerEjj'
        'jii',
        target, attachment, texture, level, layer,
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
    QOpenGLFunctions_4_0_Core::glRenderbufferStorageMultisample(GLenum
    target, GLsizei samples, GLenum internalformat, GLsizei width, GLsizei
    height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html

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
    #  void
    #      QOpenGLFunctions_4_0_Core::glRenderbufferStorageMultisample(GLenum
    #      target, GLsizei samples, GLenum internalformat, GLsizei width,
    #      GLsizei height)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core32glRenderbufferStorageMultisa'
        'mpleEjijii',
        target, samples, internalformat, width, height,
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
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glBlitFramebuffer(GLint
    srcX0, GLint srcY0, GLint srcX1, GLint srcY1, GLint dstX0, GLint dstY0,
    GLint dstX1, GLint dstY1, GLbitfield mask, GLenum filter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glBlitFramebuffer

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
    #  void QOpenGLFunctions_4_0_Core::glBlitFramebuffer(GLint srcX0, GLint
    #      srcY0, GLint srcX1, GLint srcY1, GLint dstX0, GLint dstY0, GLint
    #      dstX1, GLint dstY1, GLbitfield mask, GLenum filter)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core17glBlitFramebufferEiiiiiiiijj',
        srcX0, srcY0, srcX1, srcY1, dstX0, dstY0, dstX1, dstY1, mask, filter,
    )

  @overload(int)
  def glGenerateMipmap(self, target: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glGenerateMipmap(GLenum
    target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glGenerateMipmap

    Parameters
    ----------

    target : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glGenerateMipmap(GLenum target)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core16glGenerateMipmapEj', target,
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
    Calls Qt's 'void
    QOpenGLFunctions_4_0_Core::glFramebufferRenderbuffer(GLenum target,
    GLenum attachment, GLenum renderbuffertarget, GLuint renderbuffer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html

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
    #  void QOpenGLFunctions_4_0_Core::glFramebufferRenderbuffer(GLenum
    #      target, GLenum attachment, GLenum renderbuffertarget, GLuint
    #      renderbuffer)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core25glFramebufferRenderbufferEjj'
        'jj',
        target, attachment, renderbuffertarget, renderbuffer,
    )

  @overload(int, int, int, int, int, int)
  def glFramebufferTexture3D(
      self,
      target: int,
      attachment: int,
      textarget: int,
      texture: int,
      level: int,
      zoffset: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glFramebufferTexture3D(GLenum
    target, GLenum attachment, GLenum textarget, GLuint texture, GLint level,
    GLint zoffset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html

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

    zoffset : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glFramebufferTexture3D(GLenum target,
    #      GLenum attachment, GLenum textarget, GLuint texture, GLint level,
    #      GLint zoffset)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core22glFramebufferTexture3DEjjjji'
        'i',
        target, attachment, textarget, texture, level, zoffset,
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
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glFramebufferTexture2D(GLenum
    target, GLenum attachment, GLenum textarget, GLuint texture, GLint
    level)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html

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
    #  void QOpenGLFunctions_4_0_Core::glFramebufferTexture2D(GLenum target,
    #      GLenum attachment, GLenum textarget, GLuint texture, GLint level)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core22glFramebufferTexture2DEjjjji',
        target, attachment, textarget, texture, level,
    )

  @overload(int, int, int, int, int)
  def glFramebufferTexture1D(
      self,
      target: int,
      attachment: int,
      textarget: int,
      texture: int,
      level: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glFramebufferTexture1D(GLenum
    target, GLenum attachment, GLenum textarget, GLuint texture, GLint
    level)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html

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
    #  void QOpenGLFunctions_4_0_Core::glFramebufferTexture1D(GLenum target,
    #      GLenum attachment, GLenum textarget, GLuint texture, GLint level)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core22glFramebufferTexture1DEjjjji',
        target, attachment, textarget, texture, level,
    )

  @overload(int)
  def glCheckFramebufferStatus(self, target: int) -> int:
    """
    Calls Qt's 'GLenum
    QOpenGLFunctions_4_0_Core::glCheckFramebufferStatus(GLenum target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html

    Parameters
    ----------

    target : int
      Passed on as it is.
    """
    #  GLenum QOpenGLFunctions_4_0_Core::glCheckFramebufferStatus(GLenum
    #      target)
    return self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core24glCheckFramebufferStatusEj',
        target,
    )

  @overload(int, int)
  def glBindFramebuffer(self, target: int, framebuffer: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glBindFramebuffer(GLenum
    target, GLuint framebuffer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glBindFramebuffer

    Parameters
    ----------

    target : int
      Passed on as it is.

    framebuffer : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glBindFramebuffer(GLenum target,
    #      GLuint framebuffer)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core17glBindFramebufferEjj',
        target, framebuffer,
    )

  @overload(int)
  def glIsFramebuffer(self, framebuffer: int) -> int:
    """
    Calls Qt's 'GLboolean QOpenGLFunctions_4_0_Core::glIsFramebuffer(GLuint
    framebuffer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glIsFramebuffer

    Parameters
    ----------

    framebuffer : int
      Passed on as it is.
    """
    #  GLboolean QOpenGLFunctions_4_0_Core::glIsFramebuffer(GLuint
    #      framebuffer)
    return self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core15glIsFramebufferEj',
        framebuffer,
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
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glRenderbufferStorage(GLenum
    target, GLenum internalformat, GLsizei width, GLsizei height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html

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
    #  void QOpenGLFunctions_4_0_Core::glRenderbufferStorage(GLenum target,
    #      GLenum internalformat, GLsizei width, GLsizei height)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core21glRenderbufferStorageEjjii',
        target, internalformat, width, height,
    )

  @overload(int, int)
  def glBindRenderbuffer(self, target: int, renderbuffer: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glBindRenderbuffer(GLenum
    target, GLuint renderbuffer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glBindRenderbuffer

    Parameters
    ----------

    target : int
      Passed on as it is.

    renderbuffer : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glBindRenderbuffer(GLenum target,
    #      GLuint renderbuffer)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core18glBindRenderbufferEjj',
        target, renderbuffer,
    )

  @overload(int)
  def glIsRenderbuffer(self, renderbuffer: int) -> int:
    """
    Calls Qt's 'GLboolean QOpenGLFunctions_4_0_Core::glIsRenderbuffer(GLuint
    renderbuffer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glIsRenderbuffer

    Parameters
    ----------

    renderbuffer : int
      Passed on as it is.
    """
    #  GLboolean QOpenGLFunctions_4_0_Core::glIsRenderbuffer(GLuint
    #      renderbuffer)
    return self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core16glIsRenderbufferEj',
        renderbuffer,
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
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glClearBufferfi(GLenum
    buffer, GLint drawbuffer, GLfloat depth, GLint stencil)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glClearBufferfi

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
    #  void QOpenGLFunctions_4_0_Core::glClearBufferfi(GLenum buffer, GLint
    #      drawbuffer, GLfloat depth, GLint stencil)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core15glClearBufferfiEjifi',
        buffer, drawbuffer, depth, stencil,
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
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glUniform4ui(GLint location,
    GLuint v0, GLuint v1, GLuint v2, GLuint v3)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glUniform4ui

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
    #  void QOpenGLFunctions_4_0_Core::glUniform4ui(GLint location, GLuint
    #      v0, GLuint v1, GLuint v2, GLuint v3)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core12glUniform4uiEijjjj',
        location, v0, v1, v2, v3,
    )

  @overload(int, int, int, int)
  def glUniform3ui(self, location: int, v0: int, v1: int, v2: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glUniform3ui(GLint location,
    GLuint v0, GLuint v1, GLuint v2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glUniform3ui

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
    #  void QOpenGLFunctions_4_0_Core::glUniform3ui(GLint location, GLuint
    #      v0, GLuint v1, GLuint v2)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core12glUniform3uiEijjj',
        location, v0, v1, v2,
    )

  @overload(int, int, int)
  def glUniform2ui(self, location: int, v0: int, v1: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glUniform2ui(GLint location,
    GLuint v0, GLuint v1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glUniform2ui

    Parameters
    ----------

    location : int
      Passed on as it is.

    v0 : int
      Passed on as it is.

    v1 : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glUniform2ui(GLint location, GLuint
    #      v0, GLuint v1)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core12glUniform2uiEijj',
        location, v0, v1,
    )

  @overload(int, int)
  def glUniform1ui(self, location: int, v0: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glUniform1ui(GLint location,
    GLuint v0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glUniform1ui

    Parameters
    ----------

    location : int
      Passed on as it is.

    v0 : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glUniform1ui(GLint location, GLuint
    #      v0)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core12glUniform1uiEij',
        location, v0,
    )

  def glEndConditionalRender(self) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glEndConditionalRender()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html
    """
    #  void QOpenGLFunctions_4_0_Core::glEndConditionalRender()
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core22glEndConditionalRenderEv',
    )

  @overload(int, int)
  def glBeginConditionalRender(self, id: int, mode: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_0_Core::glBeginConditionalRender(GLuint id, GLenum
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html

    Parameters
    ----------

    id : int
      Passed on as it is.

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glBeginConditionalRender(GLuint id,
    #      GLenum mode)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core24glBeginConditionalRenderEjj',
        id, mode,
    )

  @overload(int, int)
  def glClampColor(self, target: int, clamp: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glClampColor(GLenum target,
    GLenum clamp)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glClampColor

    Parameters
    ----------

    target : int
      Passed on as it is.

    clamp : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glClampColor(GLenum target, GLenum
    #      clamp)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core12glClampColorEjj',
        target, clamp,
    )

  @overload(int, int, int)
  def glBindBufferBase(self, target: int, index: int, buffer: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glBindBufferBase(GLenum
    target, GLuint index, GLuint buffer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glBindBufferBase

    Parameters
    ----------

    target : int
      Passed on as it is.

    index : int
      Passed on as it is.

    buffer : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glBindBufferBase(GLenum target, GLuint
    #      index, GLuint buffer)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core16glBindBufferBaseEjjj',
        target, index, buffer,
    )

  @overload(int, int, int, int, int)
  def glBindBufferRange(
      self,
      target: int,
      index: int,
      buffer: int,
      offset: int,
      size: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glBindBufferRange(GLenum
    target, GLuint index, GLuint buffer, GLintptr offset, GLsizeiptr size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glBindBufferRange

    Parameters
    ----------

    target : int
      Passed on as it is.

    index : int
      Passed on as it is.

    buffer : int
      Passed on as it is.

    offset : int
      Passed on as it is.

    size : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glBindBufferRange(GLenum target,
    #      GLuint index, GLuint buffer, GLintptr offset, GLsizeiptr size)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core17glBindBufferRangeEjjjll',
        target, index, buffer, offset, size,
    )

  def glEndTransformFeedback(self) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glEndTransformFeedback()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html
    """
    #  void QOpenGLFunctions_4_0_Core::glEndTransformFeedback()
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core22glEndTransformFeedbackEv',
    )

  @overload(int)
  def glBeginTransformFeedback(self, primitiveMode: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_0_Core::glBeginTransformFeedback(GLenum
    primitiveMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html

    Parameters
    ----------

    primitiveMode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glBeginTransformFeedback(GLenum
    #      primitiveMode)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core24glBeginTransformFeedbackEj',
        primitiveMode,
    )

  @overload(int, int)
  def glIsEnabledi(self, target: int, index: int) -> int:
    """
    Calls Qt's 'GLboolean QOpenGLFunctions_4_0_Core::glIsEnabledi(GLenum
    target, GLuint index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glIsEnabledi

    Parameters
    ----------

    target : int
      Passed on as it is.

    index : int
      Passed on as it is.
    """
    #  GLboolean QOpenGLFunctions_4_0_Core::glIsEnabledi(GLenum target,
    #      GLuint index)
    return self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core12glIsEnablediEjj',
        target, index,
    )

  @overload(int, int)
  def glDisablei(self, target: int, index: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glDisablei(GLenum target,
    GLuint index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glDisablei

    Parameters
    ----------

    target : int
      Passed on as it is.

    index : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glDisablei(GLenum target, GLuint
    #      index)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core10glDisableiEjj', target, index,
    )

  @overload(int, int)
  def glEnablei(self, target: int, index: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glEnablei(GLenum target,
    GLuint index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glEnablei

    Parameters
    ----------

    target : int
      Passed on as it is.

    index : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glEnablei(GLenum target, GLuint index)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core9glEnableiEjj', target, index,
    )

  @overload(int, int, int, int, int)
  def glColorMaski(self, index: int, r: int, g: int, b: int, a: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glColorMaski(GLuint index,
    GLboolean r, GLboolean g, GLboolean b, GLboolean a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glColorMaski

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
    #  void QOpenGLFunctions_4_0_Core::glColorMaski(GLuint index, GLboolean
    #      r, GLboolean g, GLboolean b, GLboolean a)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core12glColorMaskiEjhhhh',
        index, r, g, b, a,
    )

  @overload(int, int, int, int, int)
  def glCopyBufferSubData(
      self,
      readTarget: int,
      writeTarget: int,
      readOffset: int,
      writeOffset: int,
      size: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glCopyBufferSubData(GLenum
    readTarget, GLenum writeTarget, GLintptr readOffset, GLintptr
    writeOffset, GLsizeiptr size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glCopyBufferSubData

    Parameters
    ----------

    readTarget : int
      Passed on as it is.

    writeTarget : int
      Passed on as it is.

    readOffset : int
      Passed on as it is.

    writeOffset : int
      Passed on as it is.

    size : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glCopyBufferSubData(GLenum readTarget,
    #      GLenum writeTarget, GLintptr readOffset, GLintptr writeOffset,
    #      GLsizeiptr size)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core19glCopyBufferSubDataEjjlll',
        readTarget, writeTarget, readOffset, writeOffset, size,
    )

  @overload(int, int, int)
  def glUniformBlockBinding(
      self,
      program: int,
      uniformBlockIndex: int,
      uniformBlockBinding: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glUniformBlockBinding(GLuint
    program, GLuint uniformBlockIndex, GLuint uniformBlockBinding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html

    Parameters
    ----------

    program : int
      Passed on as it is.

    uniformBlockIndex : int
      Passed on as it is.

    uniformBlockBinding : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glUniformBlockBinding(GLuint program,
    #      GLuint uniformBlockIndex, GLuint uniformBlockBinding)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core21glUniformBlockBindingEjjj',
        program, uniformBlockIndex, uniformBlockBinding,
    )

  @overload(int)
  def glPrimitiveRestartIndex(self, index: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_0_Core::glPrimitiveRestartIndex(GLuint index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glPrimitiveRestartIndex(GLuint index)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core23glPrimitiveRestartIndexEj',
        index,
    )

  @overload(int, int, int)
  def glTexBuffer(
      self,
      target: int,
      internalformat: int,
      buffer: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glTexBuffer(GLenum target,
    GLenum internalformat, GLuint buffer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glTexBuffer

    Parameters
    ----------

    target : int
      Passed on as it is.

    internalformat : int
      Passed on as it is.

    buffer : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glTexBuffer(GLenum target, GLenum
    #      internalformat, GLuint buffer)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core11glTexBufferEjjj',
        target, internalformat, buffer,
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
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glDrawArraysInstanced(GLenum
    mode, GLint first, GLsizei count, GLsizei instancecount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html

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
    #  void QOpenGLFunctions_4_0_Core::glDrawArraysInstanced(GLenum mode,
    #      GLint first, GLsizei count, GLsizei instancecount)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core21glDrawArraysInstancedEjiii',
        mode, first, count, instancecount,
    )

  @overload(int, int)
  def glSampleMaski(self, index: int, mask: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glSampleMaski(GLuint index,
    GLbitfield mask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glSampleMaski

    Parameters
    ----------

    index : int
      Passed on as it is.

    mask : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glSampleMaski(GLuint index, GLbitfield
    #      mask)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core13glSampleMaskiEjj',
        index, mask,
    )

  @overload(int, int, int, int, int, int, int)
  def glTexImage3DMultisample(
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
    Calls Qt's 'void
    QOpenGLFunctions_4_0_Core::glTexImage3DMultisample(GLenum target, GLsizei
    samples, GLint internalformat, GLsizei width, GLsizei height, GLsizei
    depth, GLboolean fixedsamplelocations)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html

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
    #  void QOpenGLFunctions_4_0_Core::glTexImage3DMultisample(GLenum target,
    #      GLsizei samples, GLint internalformat, GLsizei width, GLsizei
    #      height, GLsizei depth, GLboolean fixedsamplelocations)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core23glTexImage3DMultisampleEjiii'
        'iih',
        target, samples, internalformat, width, height, depth,
        fixedsamplelocations,
    )

  @overload(int, int, int, int, int, int)
  def glTexImage2DMultisample(
      self,
      target: int,
      samples: int,
      internalformat: int,
      width: int,
      height: int,
      fixedsamplelocations: int,
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_0_Core::glTexImage2DMultisample(GLenum target, GLsizei
    samples, GLint internalformat, GLsizei width, GLsizei height, GLboolean
    fixedsamplelocations)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html

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
    #  void QOpenGLFunctions_4_0_Core::glTexImage2DMultisample(GLenum target,
    #      GLsizei samples, GLint internalformat, GLsizei width, GLsizei
    #      height, GLboolean fixedsamplelocations)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core23glTexImage2DMultisampleEjiii'
        'ih',
        target, samples, internalformat, width, height, fixedsamplelocations,
    )

  @overload(int)
  def glProvokingVertex(self, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glProvokingVertex(GLenum
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glProvokingVertex

    Parameters
    ----------

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glProvokingVertex(GLenum mode)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core17glProvokingVertexEj', mode,
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
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glFramebufferTexture(GLenum
    target, GLenum attachment, GLuint texture, GLint level)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html

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
    #  void QOpenGLFunctions_4_0_Core::glFramebufferTexture(GLenum target,
    #      GLenum attachment, GLuint texture, GLint level)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core20glFramebufferTextureEjjji',
        target, attachment, texture, level,
    )

  @overload(int, int, int, int)
  def glVertexAttribP4ui(
      self,
      index: int,
      type: int,
      normalized: int,
      value: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glVertexAttribP4ui(GLuint
    index, GLenum type, GLboolean normalized, GLuint value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glVertexAttribP4ui

    Parameters
    ----------

    index : int
      Passed on as it is.

    type : int
      Passed on as it is.

    normalized : int
      Passed on as it is.

    value : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glVertexAttribP4ui(GLuint index,
    #      GLenum type, GLboolean normalized, GLuint value)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core18glVertexAttribP4uiEjjhj',
        index, type, normalized, value,
    )

  @overload(int, int, int, int)
  def glVertexAttribP3ui(
      self,
      index: int,
      type: int,
      normalized: int,
      value: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glVertexAttribP3ui(GLuint
    index, GLenum type, GLboolean normalized, GLuint value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glVertexAttribP3ui

    Parameters
    ----------

    index : int
      Passed on as it is.

    type : int
      Passed on as it is.

    normalized : int
      Passed on as it is.

    value : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glVertexAttribP3ui(GLuint index,
    #      GLenum type, GLboolean normalized, GLuint value)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core18glVertexAttribP3uiEjjhj',
        index, type, normalized, value,
    )

  @overload(int, int, int, int)
  def glVertexAttribP2ui(
      self,
      index: int,
      type: int,
      normalized: int,
      value: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glVertexAttribP2ui(GLuint
    index, GLenum type, GLboolean normalized, GLuint value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glVertexAttribP2ui

    Parameters
    ----------

    index : int
      Passed on as it is.

    type : int
      Passed on as it is.

    normalized : int
      Passed on as it is.

    value : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glVertexAttribP2ui(GLuint index,
    #      GLenum type, GLboolean normalized, GLuint value)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core18glVertexAttribP2uiEjjhj',
        index, type, normalized, value,
    )

  @overload(int, int, int, int)
  def glVertexAttribP1ui(
      self,
      index: int,
      type: int,
      normalized: int,
      value: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glVertexAttribP1ui(GLuint
    index, GLenum type, GLboolean normalized, GLuint value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glVertexAttribP1ui

    Parameters
    ----------

    index : int
      Passed on as it is.

    type : int
      Passed on as it is.

    normalized : int
      Passed on as it is.

    value : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glVertexAttribP1ui(GLuint index,
    #      GLenum type, GLboolean normalized, GLuint value)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core18glVertexAttribP1uiEjjhj',
        index, type, normalized, value,
    )

  @overload(int, int)
  def glQueryCounter(self, id: int, target: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glQueryCounter(GLuint id,
    GLenum target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glQueryCounter

    Parameters
    ----------

    id : int
      Passed on as it is.

    target : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glQueryCounter(GLuint id, GLenum
    #      target)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core14glQueryCounterEjj',
        id, target,
    )

  @overload(int, int, float)
  def glSamplerParameterf(
      self,
      sampler: int,
      pname: int,
      param: float,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glSamplerParameterf(GLuint
    sampler, GLenum pname, GLfloat param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glSamplerParameterf

    Parameters
    ----------

    sampler : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    param : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glSamplerParameterf(GLuint sampler,
    #      GLenum pname, GLfloat param)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core19glSamplerParameterfEjjf',
        sampler, pname, param,
    )

  @overload(int, int, int)
  def glSamplerParameteri(
      self,
      sampler: int,
      pname: int,
      param: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glSamplerParameteri(GLuint
    sampler, GLenum pname, GLint param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glSamplerParameteri

    Parameters
    ----------

    sampler : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    param : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glSamplerParameteri(GLuint sampler,
    #      GLenum pname, GLint param)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core19glSamplerParameteriEjji',
        sampler, pname, param,
    )

  @overload(int, int)
  def glBindSampler(self, unit: int, sampler: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glBindSampler(GLuint unit,
    GLuint sampler)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glBindSampler

    Parameters
    ----------

    unit : int
      Passed on as it is.

    sampler : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glBindSampler(GLuint unit, GLuint
    #      sampler)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core13glBindSamplerEjj',
        unit, sampler,
    )

  @overload(int)
  def glIsSampler(self, sampler: int) -> int:
    """
    Calls Qt's 'GLboolean QOpenGLFunctions_4_0_Core::glIsSampler(GLuint
    sampler)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glIsSampler

    Parameters
    ----------

    sampler : int
      Passed on as it is.
    """
    #  GLboolean QOpenGLFunctions_4_0_Core::glIsSampler(GLuint sampler)
    return self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core11glIsSamplerEj', sampler,
    )

  @overload(int, int)
  def glVertexAttribDivisor(self, index: int, divisor: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glVertexAttribDivisor(GLuint
    index, GLuint divisor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html

    Parameters
    ----------

    index : int
      Passed on as it is.

    divisor : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glVertexAttribDivisor(GLuint index,
    #      GLuint divisor)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core21glVertexAttribDivisorEjj',
        index, divisor,
    )

  @overload(int, int)
  def glEndQueryIndexed(self, target: int, index: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glEndQueryIndexed(GLenum
    target, GLuint index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glEndQueryIndexed

    Parameters
    ----------

    target : int
      Passed on as it is.

    index : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glEndQueryIndexed(GLenum target,
    #      GLuint index)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core17glEndQueryIndexedEjj',
        target, index,
    )

  @overload(int, int, int)
  def glBeginQueryIndexed(self, target: int, index: int, id: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glBeginQueryIndexed(GLenum
    target, GLuint index, GLuint id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glBeginQueryIndexed

    Parameters
    ----------

    target : int
      Passed on as it is.

    index : int
      Passed on as it is.

    id : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glBeginQueryIndexed(GLenum target,
    #      GLuint index, GLuint id)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core19glBeginQueryIndexedEjjj',
        target, index, id,
    )

  @overload(int, int, int)
  def glDrawTransformFeedbackStream(
      self,
      mode: int,
      id: int,
      stream: int,
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_0_Core::glDrawTransformFeedbackStream(GLenum mode,
    GLuint id, GLuint stream)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html

    Parameters
    ----------

    mode : int
      Passed on as it is.

    id : int
      Passed on as it is.

    stream : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glDrawTransformFeedbackStream(GLenum
    #      mode, GLuint id, GLuint stream)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core29glDrawTransformFeedbackStrea'
        'mEjjj',
        mode, id, stream,
    )

  @overload(int, int)
  def glDrawTransformFeedback(self, mode: int, id: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_0_Core::glDrawTransformFeedback(GLenum mode, GLuint
    id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html

    Parameters
    ----------

    mode : int
      Passed on as it is.

    id : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glDrawTransformFeedback(GLenum mode,
    #      GLuint id)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core23glDrawTransformFeedbackEjj',
        mode, id,
    )

  def glResumeTransformFeedback(self) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glResumeTransformFeedback()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html
    """
    #  void QOpenGLFunctions_4_0_Core::glResumeTransformFeedback()
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core25glResumeTransformFeedbackEv',
    )

  def glPauseTransformFeedback(self) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glPauseTransformFeedback()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html
    """
    #  void QOpenGLFunctions_4_0_Core::glPauseTransformFeedback()
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core24glPauseTransformFeedbackEv',
    )

  @overload(int)
  def glIsTransformFeedback(self, id: int) -> int:
    """
    Calls Qt's 'GLboolean
    QOpenGLFunctions_4_0_Core::glIsTransformFeedback(GLuint id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html

    Parameters
    ----------

    id : int
      Passed on as it is.
    """
    #  GLboolean QOpenGLFunctions_4_0_Core::glIsTransformFeedback(GLuint id)
    return self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core21glIsTransformFeedbackEj', id,
    )

  @overload(int, int)
  def glBindTransformFeedback(self, target: int, id: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_0_Core::glBindTransformFeedback(GLenum target, GLuint
    id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html

    Parameters
    ----------

    target : int
      Passed on as it is.

    id : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glBindTransformFeedback(GLenum target,
    #      GLuint id)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core23glBindTransformFeedbackEjj',
        target, id,
    )

  @overload(int, int)
  def glPatchParameteri(self, pname: int, value: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glPatchParameteri(GLenum
    pname, GLint value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glPatchParameteri

    Parameters
    ----------

    pname : int
      Passed on as it is.

    value : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glPatchParameteri(GLenum pname, GLint
    #      value)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core17glPatchParameteriEji',
        pname, value,
    )

  @overload(int, float, float, float, float)
  def glUniform4d(
      self,
      location: int,
      x: float,
      y: float,
      z: float,
      w: float,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glUniform4d(GLint location,
    GLdouble x, GLdouble y, GLdouble z, GLdouble w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glUniform4d

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
    #  void QOpenGLFunctions_4_0_Core::glUniform4d(GLint location, GLdouble
    #      x, GLdouble y, GLdouble z, GLdouble w)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core11glUniform4dEidddd',
        location, x, y, z, w,
    )

  @overload(int, float, float, float)
  def glUniform3d(self, location: int, x: float, y: float, z: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glUniform3d(GLint location,
    GLdouble x, GLdouble y, GLdouble z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glUniform3d

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
    #  void QOpenGLFunctions_4_0_Core::glUniform3d(GLint location, GLdouble
    #      x, GLdouble y, GLdouble z)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core11glUniform3dEiddd',
        location, x, y, z,
    )

  @overload(int, float, float)
  def glUniform2d(self, location: int, x: float, y: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glUniform2d(GLint location,
    GLdouble x, GLdouble y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glUniform2d

    Parameters
    ----------

    location : int
      Passed on as it is.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glUniform2d(GLint location, GLdouble
    #      x, GLdouble y)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core11glUniform2dEidd',
        location, x, y,
    )

  @overload(int, float)
  def glUniform1d(self, location: int, x: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glUniform1d(GLint location,
    GLdouble x)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glUniform1d

    Parameters
    ----------

    location : int
      Passed on as it is.

    x : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glUniform1d(GLint location, GLdouble
    #      x)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core11glUniform1dEid', location, x,
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
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glBlendFuncSeparatei(GLuint
    buf, GLenum srcRGB, GLenum dstRGB, GLenum srcAlpha, GLenum dstAlpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html

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
    #  void QOpenGLFunctions_4_0_Core::glBlendFuncSeparatei(GLuint buf,
    #      GLenum srcRGB, GLenum dstRGB, GLenum srcAlpha, GLenum dstAlpha)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core20glBlendFuncSeparateiEjjjjj',
        buf, srcRGB, dstRGB, srcAlpha, dstAlpha,
    )

  @overload(int, int, int)
  def glBlendFunci(self, buf: int, src: int, dst: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glBlendFunci(GLuint buf,
    GLenum src, GLenum dst)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glBlendFunci

    Parameters
    ----------

    buf : int
      Passed on as it is.

    src : int
      Passed on as it is.

    dst : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glBlendFunci(GLuint buf, GLenum src,
    #      GLenum dst)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core12glBlendFunciEjjj',
        buf, src, dst,
    )

  @overload(int, int, int)
  def glBlendEquationSeparatei(
      self,
      buf: int,
      modeRGB: int,
      modeAlpha: int,
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_0_Core::glBlendEquationSeparatei(GLuint buf, GLenum
    modeRGB, GLenum modeAlpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html

    Parameters
    ----------

    buf : int
      Passed on as it is.

    modeRGB : int
      Passed on as it is.

    modeAlpha : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glBlendEquationSeparatei(GLuint buf,
    #      GLenum modeRGB, GLenum modeAlpha)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core24glBlendEquationSeparateiEjjj',
        buf, modeRGB, modeAlpha,
    )

  @overload(int, int)
  def glBlendEquationi(self, buf: int, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glBlendEquationi(GLuint buf,
    GLenum mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glBlendEquationi

    Parameters
    ----------

    buf : int
      Passed on as it is.

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glBlendEquationi(GLuint buf, GLenum
    #      mode)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core16glBlendEquationiEjj',
        buf, mode,
    )

  @overload(float)
  def glMinSampleShading(self, value: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_0_Core::glMinSampleShading(GLfloat
    value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_0_core.html#glMinSampleShading

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_0_Core::glMinSampleShading(GLfloat value)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_0_Core18glMinSampleShadingEf', value,
    )

  @staticmethod
  def glBindAttribLocation(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glBindAttribLocation(GLuint
    program, GLuint index, const GLchar *name)': names 'GLchar', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glBindAttribLocation' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glBindAttribLocation(GLuint program, "
        "GLuint index, const GLchar *name)': names 'GLchar', which has no "
        "cute class yet.")

  @staticmethod
  def glBindFragDataLocation(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glBindFragDataLocation(GLuint
    program, GLuint color, const GLchar *name)': names 'GLchar', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glBindFragDataLocation' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glBindFragDataLocation(GLuint program, "
        "GLuint color, const GLchar *name)': names 'GLchar', which has no "
        "cute class yet.")

  @staticmethod
  def glBindFragDataLocationIndexed(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_0_Core::glBindFragDataLocationIndexed(GLuint program,
    GLuint colorNumber, GLuint index, const GLchar *name)': names 'GLchar',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glBindFragDataLocationIndexed' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glBindFragDataLocationIndexed(GLuint "
        "program, GLuint colorNumber, GLuint index, const GLchar *name)': "
        "names 'GLchar', which has no cute class yet.")

  @staticmethod
  def glBufferData(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glBufferData(GLenum target,
    GLsizeiptr size, const GLvoid *data, GLenum usage)': names 'GLvoid',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glBufferData' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_4_0_Core::glBufferData(GLenum target, "
        "GLsizeiptr size, const GLvoid *data, GLenum usage)': names "
        "'GLvoid', which has no cute class yet.")

  @staticmethod
  def glBufferSubData(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glBufferSubData(GLenum target,
    GLintptr offset, GLsizeiptr size, const GLvoid *data)': names 'GLvoid',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glBufferSubData' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_0_Core::glBufferSubData(GLenum "
        "target, GLintptr offset, GLsizeiptr size, const GLvoid *data)': "
        "names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glClearBufferfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glClearBufferfv(GLenum buffer,
    GLint drawbuffer, const GLfloat *value)': names 'GLfloat', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glClearBufferfv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_0_Core::glClearBufferfv(GLenum "
        "buffer, GLint drawbuffer, const GLfloat *value)': names 'GLfloat', "
        "which has no cute class yet.")

  @staticmethod
  def glClearBufferiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glClearBufferiv(GLenum buffer,
    GLint drawbuffer, const GLint *value)': names 'GLint', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glClearBufferiv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_0_Core::glClearBufferiv(GLenum "
        "buffer, GLint drawbuffer, const GLint *value)': names 'GLint', "
        "which has no cute class yet.")

  @staticmethod
  def glClearBufferuiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glClearBufferuiv(GLenum buffer,
    GLint drawbuffer, const GLuint *value)': names 'GLuint', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glClearBufferuiv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_0_Core::glClearBufferuiv(GLenum "
        "buffer, GLint drawbuffer, const GLuint *value)': names 'GLuint', "
        "which has no cute class yet.")

  @staticmethod
  def glClientWaitSync(*__, **_) -> Never:
    """
    Qt's 'GLenum QOpenGLFunctions_4_0_Core::glClientWaitSync(GLsync sync,
    GLbitfield flags, GLuint64 timeout)': names 'struct __GLsync', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glClientWaitSync' has no cute function "
        "yet. Qt's 'GLenum "
        "QOpenGLFunctions_4_0_Core::glClientWaitSync(GLsync sync, "
        "GLbitfield flags, GLuint64 timeout)': names 'struct __GLsync', "
        "which has no cute class yet.")

  @staticmethod
  def glCompressedTexImage1D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glCompressedTexImage1D(GLenum
    target, GLint level, GLenum internalformat, GLsizei width, GLint border,
    GLsizei imageSize, const GLvoid *data)': names 'GLvoid', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glCompressedTexImage1D' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glCompressedTexImage1D(GLenum target, "
        "GLint level, GLenum internalformat, GLsizei width, GLint border, "
        "GLsizei imageSize, const GLvoid *data)': names 'GLvoid', which has "
        "no cute class yet.")

  @staticmethod
  def glCompressedTexImage2D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glCompressedTexImage2D(GLenum
    target, GLint level, GLenum internalformat, GLsizei width, GLsizei
    height, GLint border, GLsizei imageSize, const GLvoid *data)': names
    'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glCompressedTexImage2D' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glCompressedTexImage2D(GLenum target, "
        "GLint level, GLenum internalformat, GLsizei width, GLsizei height, "
        "GLint border, GLsizei imageSize, const GLvoid *data)': names "
        "'GLvoid', which has no cute class yet.")

  @staticmethod
  def glCompressedTexImage3D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glCompressedTexImage3D(GLenum
    target, GLint level, GLenum internalformat, GLsizei width, GLsizei
    height, GLsizei depth, GLint border, GLsizei imageSize, const GLvoid
    *data)': names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glCompressedTexImage3D' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glCompressedTexImage3D(GLenum target, "
        "GLint level, GLenum internalformat, GLsizei width, GLsizei height, "
        "GLsizei depth, GLint border, GLsizei imageSize, const GLvoid "
        "*data)': names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glCompressedTexSubImage1D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glCompressedTexSubImage1D(GLenum
    target, GLint level, GLint xoffset, GLsizei width, GLenum format, GLsizei
    imageSize, const GLvoid *data)': names 'GLvoid', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glCompressedTexSubImage1D' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glCompressedTexSubImage1D(GLenum "
        "target, GLint level, GLint xoffset, GLsizei width, GLenum format, "
        "GLsizei imageSize, const GLvoid *data)': names 'GLvoid', which has "
        "no cute class yet.")

  @staticmethod
  def glCompressedTexSubImage2D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glCompressedTexSubImage2D(GLenum
    target, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei
    height, GLenum format, GLsizei imageSize, const GLvoid *data)': names
    'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glCompressedTexSubImage2D' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glCompressedTexSubImage2D(GLenum "
        "target, GLint level, GLint xoffset, GLint yoffset, GLsizei width, "
        "GLsizei height, GLenum format, GLsizei imageSize, const GLvoid "
        "*data)': names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glCompressedTexSubImage3D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glCompressedTexSubImage3D(GLenum
    target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei
    width, GLsizei height, GLsizei depth, GLenum format, GLsizei imageSize,
    const GLvoid *data)': names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glCompressedTexSubImage3D' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glCompressedTexSubImage3D(GLenum "
        "target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, "
        "GLsizei width, GLsizei height, GLsizei depth, GLenum format, "
        "GLsizei imageSize, const GLvoid *data)': names 'GLvoid', which has "
        "no cute class yet.")

  @staticmethod
  def glDeleteBuffers(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glDeleteBuffers(GLsizei n, const
    GLuint *buffers)': names 'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glDeleteBuffers' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_0_Core::glDeleteBuffers(GLsizei "
        "n, const GLuint *buffers)': names 'GLuint', which has no cute "
        "class yet.")

  @staticmethod
  def glDeleteFramebuffers(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glDeleteFramebuffers(GLsizei n,
    const GLuint *framebuffers)': names 'GLuint', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glDeleteFramebuffers' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glDeleteFramebuffers(GLsizei n, const "
        "GLuint *framebuffers)': names 'GLuint', which has no cute class "
        "yet.")

  @staticmethod
  def glDeleteQueries(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glDeleteQueries(GLsizei n, const
    GLuint *ids)': names 'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glDeleteQueries' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_0_Core::glDeleteQueries(GLsizei "
        "n, const GLuint *ids)': names 'GLuint', which has no cute class "
        "yet.")

  @staticmethod
  def glDeleteRenderbuffers(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glDeleteRenderbuffers(GLsizei n,
    const GLuint *renderbuffers)': names 'GLuint', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glDeleteRenderbuffers' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glDeleteRenderbuffers(GLsizei n, const "
        "GLuint *renderbuffers)': names 'GLuint', which has no cute class "
        "yet.")

  @staticmethod
  def glDeleteSamplers(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glDeleteSamplers(GLsizei count,
    const GLuint *samplers)': names 'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glDeleteSamplers' has no cute function "
        "yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glDeleteSamplers(GLsizei count, const "
        "GLuint *samplers)': names 'GLuint', which has no cute class yet.")

  @staticmethod
  def glDeleteSync(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glDeleteSync(GLsync sync)': names
    'struct __GLsync', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glDeleteSync' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_4_0_Core::glDeleteSync(GLsync sync)': "
        "names 'struct __GLsync', which has no cute class yet.")

  @staticmethod
  def glDeleteTextures(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glDeleteTextures(GLsizei n, const
    GLuint *textures)': names 'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glDeleteTextures' has no cute function "
        "yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glDeleteTextures(GLsizei n, const "
        "GLuint *textures)': names 'GLuint', which has no cute class yet.")

  @staticmethod
  def glDeleteTransformFeedbacks(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glDeleteTransformFeedbacks(GLsizei
    n, const GLuint *ids)': names 'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glDeleteTransformFeedbacks' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glDeleteTransformFeedbacks(GLsizei n, "
        "const GLuint *ids)': names 'GLuint', which has no cute class yet.")

  @staticmethod
  def glDeleteVertexArrays(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glDeleteVertexArrays(GLsizei n,
    const GLuint *arrays)': names 'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glDeleteVertexArrays' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glDeleteVertexArrays(GLsizei n, const "
        "GLuint *arrays)': names 'GLuint', which has no cute class yet.")

  @staticmethod
  def glDrawArraysIndirect(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glDrawArraysIndirect(GLenum mode,
    const GLvoid *indirect)': names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glDrawArraysIndirect' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glDrawArraysIndirect(GLenum mode, const "
        "GLvoid *indirect)': names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glDrawBuffers(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glDrawBuffers(GLsizei n, const
    GLenum *bufs)': names 'GLenum', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glDrawBuffers' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_0_Core::glDrawBuffers(GLsizei "
        "n, const GLenum *bufs)': names 'GLenum', which has no cute class "
        "yet.")

  @staticmethod
  def glDrawElements(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glDrawElements(GLenum mode, GLsizei
    count, GLenum type, const GLvoid *indices)': names 'GLvoid', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glDrawElements' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_0_Core::glDrawElements(GLenum "
        "mode, GLsizei count, GLenum type, const GLvoid *indices)': names "
        "'GLvoid', which has no cute class yet.")

  @staticmethod
  def glDrawElementsBaseVertex(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glDrawElementsBaseVertex(GLenum
    mode, GLsizei count, GLenum type, const GLvoid *indices, GLint
    basevertex)': names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glDrawElementsBaseVertex' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glDrawElementsBaseVertex(GLenum mode, "
        "GLsizei count, GLenum type, const GLvoid *indices, GLint "
        "basevertex)': names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glDrawElementsIndirect(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glDrawElementsIndirect(GLenum mode,
    GLenum type, const GLvoid *indirect)': names 'GLvoid', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glDrawElementsIndirect' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glDrawElementsIndirect(GLenum mode, "
        "GLenum type, const GLvoid *indirect)': names 'GLvoid', which has "
        "no cute class yet.")

  @staticmethod
  def glDrawElementsInstanced(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glDrawElementsInstanced(GLenum
    mode, GLsizei count, GLenum type, const GLvoid *indices, GLsizei
    instancecount)': names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glDrawElementsInstanced' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glDrawElementsInstanced(GLenum mode, "
        "GLsizei count, GLenum type, const GLvoid *indices, GLsizei "
        "instancecount)': names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glDrawElementsInstancedBaseVertex(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_0_Core::glDrawElementsInstancedBaseVertex(GLenum mode,
    GLsizei count, GLenum type, const GLvoid *indices, GLsizei instancecount,
    GLint basevertex)': names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glDrawElementsInstancedBaseVertex' has "
        "no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glDrawElementsInstancedBaseVertex(GLenum"
        " mode, GLsizei count, GLenum type, const GLvoid *indices, GLsizei "
        "instancecount, GLint basevertex)': names 'GLvoid', which has no "
        "cute class yet.")

  @staticmethod
  def glDrawRangeElements(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glDrawRangeElements(GLenum mode,
    GLuint start, GLuint end, GLsizei count, GLenum type, const GLvoid
    *indices)': names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glDrawRangeElements' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glDrawRangeElements(GLenum mode, GLuint "
        "start, GLuint end, GLsizei count, GLenum type, const GLvoid "
        "*indices)': names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glDrawRangeElementsBaseVertex(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_0_Core::glDrawRangeElementsBaseVertex(GLenum mode,
    GLuint start, GLuint end, GLsizei count, GLenum type, const GLvoid
    *indices, GLint basevertex)': names 'GLvoid', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glDrawRangeElementsBaseVertex' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glDrawRangeElementsBaseVertex(GLenum "
        "mode, GLuint start, GLuint end, GLsizei count, GLenum type, const "
        "GLvoid *indices, GLint basevertex)': names 'GLvoid', which has no "
        "cute class yet.")

  @staticmethod
  def glFenceSync(*__, **_) -> Never:
    """
    Qt's 'GLsync QOpenGLFunctions_4_0_Core::glFenceSync(GLenum condition,
    GLbitfield flags)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glFenceSync' has no cute function yet. "
        "Qt's 'GLsync QOpenGLFunctions_4_0_Core::glFenceSync(GLenum "
        "condition, GLbitfield flags)': gives a type Python has no way to "
        "take yet.")

  @staticmethod
  def glGenBuffers(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glGenBuffers(GLsizei n, GLuint
    *buffers)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGenBuffers' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_4_0_Core::glGenBuffers(GLsizei n, "
        "GLuint *buffers)': takes a number to change where it is.")

  @staticmethod
  def glGenFramebuffers(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glGenFramebuffers(GLsizei n, GLuint
    *framebuffers)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGenFramebuffers' has no cute function "
        "yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glGenFramebuffers(GLsizei n, GLuint "
        "*framebuffers)': takes a number to change where it is.")

  @staticmethod
  def glGenQueries(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glGenQueries(GLsizei n, GLuint
    *ids)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGenQueries' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_4_0_Core::glGenQueries(GLsizei n, "
        "GLuint *ids)': takes a number to change where it is.")

  @staticmethod
  def glGenRenderbuffers(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glGenRenderbuffers(GLsizei n,
    GLuint *renderbuffers)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGenRenderbuffers' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glGenRenderbuffers(GLsizei n, GLuint "
        "*renderbuffers)': takes a number to change where it is.")

  @staticmethod
  def glGenSamplers(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glGenSamplers(GLsizei count, GLuint
    *samplers)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGenSamplers' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_0_Core::glGenSamplers(GLsizei "
        "count, GLuint *samplers)': takes a number to change where it is.")

  @staticmethod
  def glGenTextures(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glGenTextures(GLsizei n, GLuint
    *textures)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGenTextures' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_0_Core::glGenTextures(GLsizei "
        "n, GLuint *textures)': takes a number to change where it is.")

  @staticmethod
  def glGenTransformFeedbacks(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glGenTransformFeedbacks(GLsizei n,
    GLuint *ids)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGenTransformFeedbacks' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glGenTransformFeedbacks(GLsizei n, "
        "GLuint *ids)': takes a number to change where it is.")

  @staticmethod
  def glGenVertexArrays(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glGenVertexArrays(GLsizei n, GLuint
    *arrays)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGenVertexArrays' has no cute function "
        "yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glGenVertexArrays(GLsizei n, GLuint "
        "*arrays)': takes a number to change where it is.")

  @staticmethod
  def glGetActiveAttrib(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glGetActiveAttrib(GLuint program,
    GLuint index, GLsizei bufSize, GLsizei *length, GLint *size, GLenum
    *type, GLchar *name)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGetActiveAttrib' has no cute function "
        "yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glGetActiveAttrib(GLuint program, "
        "GLuint index, GLsizei bufSize, GLsizei *length, GLint *size, "
        "GLenum *type, GLchar *name)': takes a number to change where it is."
    )

  @staticmethod
  def glGetActiveSubroutineName(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glGetActiveSubroutineName(GLuint
    program, GLenum shadertype, GLuint index, GLsizei bufsize, GLsizei
    *length, GLchar *name)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGetActiveSubroutineName' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glGetActiveSubroutineName(GLuint "
        "program, GLenum shadertype, GLuint index, GLsizei bufsize, GLsizei "
        "*length, GLchar *name)': takes a number to change where it is.")

  @staticmethod
  def glGetActiveSubroutineUniformName(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_0_Core::glGetActiveSubroutineUniformName(GLuint
    program, GLenum shadertype, GLuint index, GLsizei bufsize, GLsizei
    *length, GLchar *name)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGetActiveSubroutineUniformName' has "
        "no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glGetActiveSubroutineUniformName(GLuint "
        "program, GLenum shadertype, GLuint index, GLsizei bufsize, GLsizei "
        "*length, GLchar *name)': takes a number to change where it is.")

  @staticmethod
  def glGetActiveSubroutineUniformiv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_0_Core::glGetActiveSubroutineUniformiv(GLuint program,
    GLenum shadertype, GLuint index, GLenum pname, GLint *values)': takes a
    number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGetActiveSubroutineUniformiv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glGetActiveSubroutineUniformiv(GLuint "
        "program, GLenum shadertype, GLuint index, GLenum pname, GLint "
        "*values)': takes a number to change where it is.")

  @staticmethod
  def glGetActiveUniform(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glGetActiveUniform(GLuint program,
    GLuint index, GLsizei bufSize, GLsizei *length, GLint *size, GLenum
    *type, GLchar *name)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGetActiveUniform' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glGetActiveUniform(GLuint program, "
        "GLuint index, GLsizei bufSize, GLsizei *length, GLint *size, "
        "GLenum *type, GLchar *name)': takes a number to change where it is."
    )

  @staticmethod
  def glGetActiveUniformBlockName(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glGetActiveUniformBlockName(GLuint
    program, GLuint uniformBlockIndex, GLsizei bufSize, GLsizei *length,
    GLchar *uniformBlockName)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGetActiveUniformBlockName' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glGetActiveUniformBlockName(GLuint "
        "program, GLuint uniformBlockIndex, GLsizei bufSize, GLsizei "
        "*length, GLchar *uniformBlockName)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetActiveUniformBlockiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glGetActiveUniformBlockiv(GLuint
    program, GLuint uniformBlockIndex, GLenum pname, GLint *params)': takes a
    number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGetActiveUniformBlockiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glGetActiveUniformBlockiv(GLuint "
        "program, GLuint uniformBlockIndex, GLenum pname, GLint *params)': "
        "takes a number to change where it is.")

  @staticmethod
  def glGetActiveUniformName(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glGetActiveUniformName(GLuint
    program, GLuint uniformIndex, GLsizei bufSize, GLsizei *length, GLchar
    *uniformName)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGetActiveUniformName' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glGetActiveUniformName(GLuint program, "
        "GLuint uniformIndex, GLsizei bufSize, GLsizei *length, GLchar "
        "*uniformName)': takes a number to change where it is.")

  @staticmethod
  def glGetActiveUniformsiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glGetActiveUniformsiv(GLuint
    program, GLsizei uniformCount, const GLuint *uniformIndices, GLenum
    pname, GLint *params)': names 'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGetActiveUniformsiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glGetActiveUniformsiv(GLuint program, "
        "GLsizei uniformCount, const GLuint *uniformIndices, GLenum pname, "
        "GLint *params)': names 'GLuint', which has no cute class yet.")

  @staticmethod
  def glGetAttachedShaders(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glGetAttachedShaders(GLuint
    program, GLsizei maxCount, GLsizei *count, GLuint *obj)': takes a number
    to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGetAttachedShaders' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glGetAttachedShaders(GLuint program, "
        "GLsizei maxCount, GLsizei *count, GLuint *obj)': takes a number to "
        "change where it is.")

  @staticmethod
  def glGetAttribLocation(*__, **_) -> Never:
    """
    Qt's 'GLint QOpenGLFunctions_4_0_Core::glGetAttribLocation(GLuint
    program, const GLchar *name)': names 'GLchar', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGetAttribLocation' has no cute "
        "function yet. Qt's 'GLint "
        "QOpenGLFunctions_4_0_Core::glGetAttribLocation(GLuint program, "
        "const GLchar *name)': names 'GLchar', which has no cute class yet.")

  @staticmethod
  def glGetBooleani_v(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glGetBooleani_v(GLenum target,
    GLuint index, GLboolean *data)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGetBooleani_v' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_0_Core::glGetBooleani_v(GLenum "
        "target, GLuint index, GLboolean *data)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetBooleanv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glGetBooleanv(GLenum pname,
    GLboolean *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGetBooleanv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_0_Core::glGetBooleanv(GLenum "
        "pname, GLboolean *params)': takes a number to change where it is.")

  @staticmethod
  def glGetBufferParameteri64v(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glGetBufferParameteri64v(GLenum
    target, GLenum pname, GLint64 *params)': takes a number to change where
    it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGetBufferParameteri64v' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glGetBufferParameteri64v(GLenum target, "
        "GLenum pname, GLint64 *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetBufferParameteriv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glGetBufferParameteriv(GLenum
    target, GLenum pname, GLint *params)': takes a number to change where it
    is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGetBufferParameteriv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glGetBufferParameteriv(GLenum target, "
        "GLenum pname, GLint *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetBufferPointerv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glGetBufferPointerv(GLenum target,
    GLenum pname, GLvoid **params)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGetBufferPointerv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glGetBufferPointerv(GLenum target, "
        "GLenum pname, GLvoid **params)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def glGetBufferSubData(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glGetBufferSubData(GLenum target,
    GLintptr offset, GLsizeiptr size, GLvoid *data)': names 'GLvoid', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGetBufferSubData' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glGetBufferSubData(GLenum target, "
        "GLintptr offset, GLsizeiptr size, GLvoid *data)': names 'GLvoid', "
        "which has no cute class yet.")

  @staticmethod
  def glGetCompressedTexImage(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glGetCompressedTexImage(GLenum
    target, GLint level, GLvoid *img)': names 'GLvoid', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGetCompressedTexImage' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glGetCompressedTexImage(GLenum target, "
        "GLint level, GLvoid *img)': names 'GLvoid', which has no cute "
        "class yet.")

  @staticmethod
  def glGetDoublev(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glGetDoublev(GLenum pname, GLdouble
    *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGetDoublev' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_4_0_Core::glGetDoublev(GLenum pname, "
        "GLdouble *params)': takes a number to change where it is.")

  @staticmethod
  def glGetFloatv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glGetFloatv(GLenum pname, GLfloat
    *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGetFloatv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_4_0_Core::glGetFloatv(GLenum pname, "
        "GLfloat *params)': takes a number to change where it is.")

  @staticmethod
  def glGetFragDataIndex(*__, **_) -> Never:
    """
    Qt's 'GLint QOpenGLFunctions_4_0_Core::glGetFragDataIndex(GLuint program,
    const GLchar *name)': names 'GLchar', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGetFragDataIndex' has no cute "
        "function yet. Qt's 'GLint "
        "QOpenGLFunctions_4_0_Core::glGetFragDataIndex(GLuint program, "
        "const GLchar *name)': names 'GLchar', which has no cute class yet.")

  @staticmethod
  def glGetFragDataLocation(*__, **_) -> Never:
    """
    Qt's 'GLint QOpenGLFunctions_4_0_Core::glGetFragDataLocation(GLuint
    program, const GLchar *name)': names 'GLchar', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGetFragDataLocation' has no cute "
        "function yet. Qt's 'GLint "
        "QOpenGLFunctions_4_0_Core::glGetFragDataLocation(GLuint program, "
        "const GLchar *name)': names 'GLchar', which has no cute class yet.")

  @staticmethod
  def glGetFramebufferAttachmentParameteriv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_0_Core::glGetFramebufferAttachmentParameteriv(GLenum
    target, GLenum attachment, GLenum pname, GLint *params)': takes a number
    to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGetFramebufferAttachmentParameteriv' "
        "has no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glGetFramebufferAttachmentParameteriv(GL"
        "enum target, GLenum attachment, GLenum pname, GLint *params)': "
        "takes a number to change where it is.")

  @staticmethod
  def glGetInteger64i_v(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glGetInteger64i_v(GLenum target,
    GLuint index, GLint64 *data)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGetInteger64i_v' has no cute function "
        "yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glGetInteger64i_v(GLenum target, GLuint "
        "index, GLint64 *data)': takes a number to change where it is.")

  @staticmethod
  def glGetInteger64v(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glGetInteger64v(GLenum pname,
    GLint64 *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGetInteger64v' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_0_Core::glGetInteger64v(GLenum "
        "pname, GLint64 *params)': takes a number to change where it is.")

  @staticmethod
  def glGetIntegeri_v(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glGetIntegeri_v(GLenum target,
    GLuint index, GLint *data)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGetIntegeri_v' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_0_Core::glGetIntegeri_v(GLenum "
        "target, GLuint index, GLint *data)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetIntegerv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glGetIntegerv(GLenum pname, GLint
    *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGetIntegerv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_0_Core::glGetIntegerv(GLenum "
        "pname, GLint *params)': takes a number to change where it is.")

  @staticmethod
  def glGetMultisamplefv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glGetMultisamplefv(GLenum pname,
    GLuint index, GLfloat *val)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGetMultisamplefv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glGetMultisamplefv(GLenum pname, GLuint "
        "index, GLfloat *val)': takes a number to change where it is.")

  @staticmethod
  def glGetProgramInfoLog(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glGetProgramInfoLog(GLuint program,
    GLsizei bufSize, GLsizei *length, GLchar *infoLog)': takes a number to
    change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGetProgramInfoLog' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glGetProgramInfoLog(GLuint program, "
        "GLsizei bufSize, GLsizei *length, GLchar *infoLog)': takes a "
        "number to change where it is.")

  @staticmethod
  def glGetProgramStageiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glGetProgramStageiv(GLuint program,
    GLenum shadertype, GLenum pname, GLint *values)': takes a number to
    change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGetProgramStageiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glGetProgramStageiv(GLuint program, "
        "GLenum shadertype, GLenum pname, GLint *values)': takes a number "
        "to change where it is.")

  @staticmethod
  def glGetProgramiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glGetProgramiv(GLuint program,
    GLenum pname, GLint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGetProgramiv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_0_Core::glGetProgramiv(GLuint "
        "program, GLenum pname, GLint *params)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetQueryIndexediv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glGetQueryIndexediv(GLenum target,
    GLuint index, GLenum pname, GLint *params)': takes a number to change
    where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGetQueryIndexediv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glGetQueryIndexediv(GLenum target, "
        "GLuint index, GLenum pname, GLint *params)': takes a number to "
        "change where it is.")

  @staticmethod
  def glGetQueryObjecti64v(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glGetQueryObjecti64v(GLuint id,
    GLenum pname, GLint64 *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGetQueryObjecti64v' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glGetQueryObjecti64v(GLuint id, GLenum "
        "pname, GLint64 *params)': takes a number to change where it is.")

  @staticmethod
  def glGetQueryObjectiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glGetQueryObjectiv(GLuint id,
    GLenum pname, GLint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGetQueryObjectiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glGetQueryObjectiv(GLuint id, GLenum "
        "pname, GLint *params)': takes a number to change where it is.")

  @staticmethod
  def glGetQueryObjectui64v(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glGetQueryObjectui64v(GLuint id,
    GLenum pname, GLuint64 *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGetQueryObjectui64v' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glGetQueryObjectui64v(GLuint id, GLenum "
        "pname, GLuint64 *params)': takes a number to change where it is.")

  @staticmethod
  def glGetQueryObjectuiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glGetQueryObjectuiv(GLuint id,
    GLenum pname, GLuint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGetQueryObjectuiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glGetQueryObjectuiv(GLuint id, GLenum "
        "pname, GLuint *params)': takes a number to change where it is.")

  @staticmethod
  def glGetQueryiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glGetQueryiv(GLenum target, GLenum
    pname, GLint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGetQueryiv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_4_0_Core::glGetQueryiv(GLenum target, "
        "GLenum pname, GLint *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetRenderbufferParameteriv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glGetRenderbufferParameteriv(GLenum
    target, GLenum pname, GLint *params)': takes a number to change where it
    is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGetRenderbufferParameteriv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glGetRenderbufferParameteriv(GLenum "
        "target, GLenum pname, GLint *params)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetSamplerParameterIiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glGetSamplerParameterIiv(GLuint
    sampler, GLenum pname, GLint *params)': takes a number to change where it
    is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGetSamplerParameterIiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glGetSamplerParameterIiv(GLuint "
        "sampler, GLenum pname, GLint *params)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetSamplerParameterIuiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glGetSamplerParameterIuiv(GLuint
    sampler, GLenum pname, GLuint *params)': takes a number to change where
    it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGetSamplerParameterIuiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glGetSamplerParameterIuiv(GLuint "
        "sampler, GLenum pname, GLuint *params)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetSamplerParameterfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glGetSamplerParameterfv(GLuint
    sampler, GLenum pname, GLfloat *params)': takes a number to change where
    it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGetSamplerParameterfv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glGetSamplerParameterfv(GLuint sampler, "
        "GLenum pname, GLfloat *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetSamplerParameteriv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glGetSamplerParameteriv(GLuint
    sampler, GLenum pname, GLint *params)': takes a number to change where it
    is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGetSamplerParameteriv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glGetSamplerParameteriv(GLuint sampler, "
        "GLenum pname, GLint *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetShaderInfoLog(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glGetShaderInfoLog(GLuint shader,
    GLsizei bufSize, GLsizei *length, GLchar *infoLog)': takes a number to
    change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGetShaderInfoLog' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glGetShaderInfoLog(GLuint shader, "
        "GLsizei bufSize, GLsizei *length, GLchar *infoLog)': takes a "
        "number to change where it is.")

  @staticmethod
  def glGetShaderSource(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glGetShaderSource(GLuint shader,
    GLsizei bufSize, GLsizei *length, GLchar *source)': takes a number to
    change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGetShaderSource' has no cute function "
        "yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glGetShaderSource(GLuint shader, "
        "GLsizei bufSize, GLsizei *length, GLchar *source)': takes a number "
        "to change where it is.")

  @staticmethod
  def glGetShaderiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glGetShaderiv(GLuint shader, GLenum
    pname, GLint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGetShaderiv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_0_Core::glGetShaderiv(GLuint "
        "shader, GLenum pname, GLint *params)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetString(*__, **_) -> Never:
    """
    Qt's 'const GLubyte *QOpenGLFunctions_4_0_Core::glGetString(GLenum
    name)': gives 'unsigned char', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGetString' has no cute function yet. "
        "Qt's 'const GLubyte *QOpenGLFunctions_4_0_Core::glGetString(GLenum "
        "name)': gives 'unsigned char', which has no cute class yet.")

  @staticmethod
  def glGetStringi(*__, **_) -> Never:
    """
    Qt's 'const GLubyte *QOpenGLFunctions_4_0_Core::glGetStringi(GLenum name,
    GLuint index)': gives 'unsigned char', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGetStringi' has no cute function yet. "
        "Qt's 'const GLubyte "
        "*QOpenGLFunctions_4_0_Core::glGetStringi(GLenum name, GLuint "
        "index)': gives 'unsigned char', which has no cute class yet.")

  @staticmethod
  def glGetSubroutineIndex(*__, **_) -> Never:
    """
    Qt's 'GLuint QOpenGLFunctions_4_0_Core::glGetSubroutineIndex(GLuint
    program, GLenum shadertype, const GLchar *name)': names 'GLchar', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGetSubroutineIndex' has no cute "
        "function yet. Qt's 'GLuint "
        "QOpenGLFunctions_4_0_Core::glGetSubroutineIndex(GLuint program, "
        "GLenum shadertype, const GLchar *name)': names 'GLchar', which has "
        "no cute class yet.")

  @staticmethod
  def glGetSubroutineUniformLocation(*__, **_) -> Never:
    """
    Qt's 'GLint
    QOpenGLFunctions_4_0_Core::glGetSubroutineUniformLocation(GLuint program,
    GLenum shadertype, const GLchar *name)': names 'GLchar', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGetSubroutineUniformLocation' has no "
        "cute function yet. Qt's 'GLint "
        "QOpenGLFunctions_4_0_Core::glGetSubroutineUniformLocation(GLuint "
        "program, GLenum shadertype, const GLchar *name)': names 'GLchar', "
        "which has no cute class yet.")

  @staticmethod
  def glGetSynciv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glGetSynciv(GLsync sync, GLenum
    pname, GLsizei bufSize, GLsizei *length, GLint *values)': names 'struct
    __GLsync', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGetSynciv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_4_0_Core::glGetSynciv(GLsync sync, "
        "GLenum pname, GLsizei bufSize, GLsizei *length, GLint *values)': "
        "names 'struct __GLsync', which has no cute class yet.")

  @staticmethod
  def glGetTexImage(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glGetTexImage(GLenum target, GLint
    level, GLenum format, GLenum type, GLvoid *pixels)': names 'GLvoid',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGetTexImage' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_0_Core::glGetTexImage(GLenum "
        "target, GLint level, GLenum format, GLenum type, GLvoid *pixels)': "
        "names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glGetTexLevelParameterfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glGetTexLevelParameterfv(GLenum
    target, GLint level, GLenum pname, GLfloat *params)': takes a number to
    change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGetTexLevelParameterfv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glGetTexLevelParameterfv(GLenum target, "
        "GLint level, GLenum pname, GLfloat *params)': takes a number to "
        "change where it is.")

  @staticmethod
  def glGetTexLevelParameteriv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glGetTexLevelParameteriv(GLenum
    target, GLint level, GLenum pname, GLint *params)': takes a number to
    change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGetTexLevelParameteriv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glGetTexLevelParameteriv(GLenum target, "
        "GLint level, GLenum pname, GLint *params)': takes a number to "
        "change where it is.")

  @staticmethod
  def glGetTexParameterIiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glGetTexParameterIiv(GLenum target,
    GLenum pname, GLint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGetTexParameterIiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glGetTexParameterIiv(GLenum target, "
        "GLenum pname, GLint *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetTexParameterIuiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glGetTexParameterIuiv(GLenum
    target, GLenum pname, GLuint *params)': takes a number to change where it
    is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGetTexParameterIuiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glGetTexParameterIuiv(GLenum target, "
        "GLenum pname, GLuint *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetTexParameterfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glGetTexParameterfv(GLenum target,
    GLenum pname, GLfloat *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGetTexParameterfv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glGetTexParameterfv(GLenum target, "
        "GLenum pname, GLfloat *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetTexParameteriv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glGetTexParameteriv(GLenum target,
    GLenum pname, GLint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGetTexParameteriv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glGetTexParameteriv(GLenum target, "
        "GLenum pname, GLint *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetTransformFeedbackVarying(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_0_Core::glGetTransformFeedbackVarying(GLuint program,
    GLuint index, GLsizei bufSize, GLsizei *length, GLsizei *size, GLenum
    *type, GLchar *name)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGetTransformFeedbackVarying' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glGetTransformFeedbackVarying(GLuint "
        "program, GLuint index, GLsizei bufSize, GLsizei *length, GLsizei "
        "*size, GLenum *type, GLchar *name)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetUniformBlockIndex(*__, **_) -> Never:
    """
    Qt's 'GLuint QOpenGLFunctions_4_0_Core::glGetUniformBlockIndex(GLuint
    program, const GLchar *uniformBlockName)': names 'GLchar', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGetUniformBlockIndex' has no cute "
        "function yet. Qt's 'GLuint "
        "QOpenGLFunctions_4_0_Core::glGetUniformBlockIndex(GLuint program, "
        "const GLchar *uniformBlockName)': names 'GLchar', which has no "
        "cute class yet.")

  @staticmethod
  def glGetUniformIndices(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glGetUniformIndices(GLuint program,
    GLsizei uniformCount, const GLchar *const *uniformNames, GLuint
    *uniformIndices)': names 'GLchar *const', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGetUniformIndices' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glGetUniformIndices(GLuint program, "
        "GLsizei uniformCount, const GLchar *const *uniformNames, GLuint "
        "*uniformIndices)': names 'GLchar *const', which has no cute class "
        "yet.")

  @staticmethod
  def glGetUniformLocation(*__, **_) -> Never:
    """
    Qt's 'GLint QOpenGLFunctions_4_0_Core::glGetUniformLocation(GLuint
    program, const GLchar *name)': names 'GLchar', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGetUniformLocation' has no cute "
        "function yet. Qt's 'GLint "
        "QOpenGLFunctions_4_0_Core::glGetUniformLocation(GLuint program, "
        "const GLchar *name)': names 'GLchar', which has no cute class yet.")

  @staticmethod
  def glGetUniformSubroutineuiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glGetUniformSubroutineuiv(GLenum
    shadertype, GLint location, GLuint *params)': takes a number to change
    where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGetUniformSubroutineuiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glGetUniformSubroutineuiv(GLenum "
        "shadertype, GLint location, GLuint *params)': takes a number to "
        "change where it is.")

  @staticmethod
  def glGetUniformdv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glGetUniformdv(GLuint program,
    GLint location, GLdouble *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGetUniformdv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_0_Core::glGetUniformdv(GLuint "
        "program, GLint location, GLdouble *params)': takes a number to "
        "change where it is.")

  @staticmethod
  def glGetUniformfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glGetUniformfv(GLuint program,
    GLint location, GLfloat *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGetUniformfv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_0_Core::glGetUniformfv(GLuint "
        "program, GLint location, GLfloat *params)': takes a number to "
        "change where it is.")

  @staticmethod
  def glGetUniformiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glGetUniformiv(GLuint program,
    GLint location, GLint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGetUniformiv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_0_Core::glGetUniformiv(GLuint "
        "program, GLint location, GLint *params)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetUniformuiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glGetUniformuiv(GLuint program,
    GLint location, GLuint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGetUniformuiv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_0_Core::glGetUniformuiv(GLuint "
        "program, GLint location, GLuint *params)': takes a number to "
        "change where it is.")

  @staticmethod
  def glGetVertexAttribIiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glGetVertexAttribIiv(GLuint index,
    GLenum pname, GLint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGetVertexAttribIiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glGetVertexAttribIiv(GLuint index, "
        "GLenum pname, GLint *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetVertexAttribIuiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glGetVertexAttribIuiv(GLuint index,
    GLenum pname, GLuint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGetVertexAttribIuiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glGetVertexAttribIuiv(GLuint index, "
        "GLenum pname, GLuint *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetVertexAttribPointerv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glGetVertexAttribPointerv(GLuint
    index, GLenum pname, GLvoid **pointer)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGetVertexAttribPointerv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glGetVertexAttribPointerv(GLuint index, "
        "GLenum pname, GLvoid **pointer)': takes a type Python has no way "
        "to hand over yet.")

  @staticmethod
  def glGetVertexAttribdv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glGetVertexAttribdv(GLuint index,
    GLenum pname, GLdouble *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGetVertexAttribdv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glGetVertexAttribdv(GLuint index, "
        "GLenum pname, GLdouble *params)': takes a number to change where "
        "it is.")

  @staticmethod
  def glGetVertexAttribfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glGetVertexAttribfv(GLuint index,
    GLenum pname, GLfloat *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGetVertexAttribfv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glGetVertexAttribfv(GLuint index, "
        "GLenum pname, GLfloat *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetVertexAttribiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glGetVertexAttribiv(GLuint index,
    GLenum pname, GLint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glGetVertexAttribiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glGetVertexAttribiv(GLuint index, "
        "GLenum pname, GLint *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glIsSync(*__, **_) -> Never:
    """
    Qt's 'GLboolean QOpenGLFunctions_4_0_Core::glIsSync(GLsync sync)': names
    'struct __GLsync', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glIsSync' has no cute function yet. "
        "Qt's 'GLboolean QOpenGLFunctions_4_0_Core::glIsSync(GLsync sync)': "
        "names 'struct __GLsync', which has no cute class yet.")

  @staticmethod
  def glMapBuffer(*__, **_) -> Never:
    """
    Qt's 'GLvoid *QOpenGLFunctions_4_0_Core::glMapBuffer(GLenum target,
    GLenum access)': gives 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glMapBuffer' has no cute function yet. "
        "Qt's 'GLvoid *QOpenGLFunctions_4_0_Core::glMapBuffer(GLenum "
        "target, GLenum access)': gives 'GLvoid', which has no cute class "
        "yet.")

  @staticmethod
  def glMapBufferRange(*__, **_) -> Never:
    """
    Qt's 'GLvoid *QOpenGLFunctions_4_0_Core::glMapBufferRange(GLenum target,
    GLintptr offset, GLsizeiptr length, GLbitfield access)': gives 'GLvoid',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glMapBufferRange' has no cute function "
        "yet. Qt's 'GLvoid "
        "*QOpenGLFunctions_4_0_Core::glMapBufferRange(GLenum target, "
        "GLintptr offset, GLsizeiptr length, GLbitfield access)': gives "
        "'GLvoid', which has no cute class yet.")

  @staticmethod
  def glMultiDrawArrays(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glMultiDrawArrays(GLenum mode,
    const GLint *first, const GLsizei *count, GLsizei drawcount)': names
    'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glMultiDrawArrays' has no cute function "
        "yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glMultiDrawArrays(GLenum mode, const "
        "GLint *first, const GLsizei *count, GLsizei drawcount)': names "
        "'GLint', which has no cute class yet.")

  @staticmethod
  def glMultiDrawElements(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glMultiDrawElements(GLenum mode,
    const GLsizei *count, GLenum type, const GLvoid *const *indices, GLsizei
    drawcount)': names 'GLsizei', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glMultiDrawElements' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glMultiDrawElements(GLenum mode, const "
        "GLsizei *count, GLenum type, const GLvoid *const *indices, GLsizei "
        "drawcount)': names 'GLsizei', which has no cute class yet.")

  @staticmethod
  def glMultiDrawElementsBaseVertex(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_0_Core::glMultiDrawElementsBaseVertex(GLenum mode,
    const GLsizei *count, GLenum type, const GLvoid *const *indices, GLsizei
    drawcount, const GLint *basevertex)': names 'GLsizei', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glMultiDrawElementsBaseVertex' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glMultiDrawElementsBaseVertex(GLenum "
        "mode, const GLsizei *count, GLenum type, const GLvoid *const "
        "*indices, GLsizei drawcount, const GLint *basevertex)': names "
        "'GLsizei', which has no cute class yet.")

  @staticmethod
  def glPatchParameterfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glPatchParameterfv(GLenum pname,
    const GLfloat *values)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glPatchParameterfv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glPatchParameterfv(GLenum pname, const "
        "GLfloat *values)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glPointParameterfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glPointParameterfv(GLenum pname,
    const GLfloat *params)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glPointParameterfv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glPointParameterfv(GLenum pname, const "
        "GLfloat *params)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glPointParameteriv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glPointParameteriv(GLenum pname,
    const GLint *params)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glPointParameteriv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glPointParameteriv(GLenum pname, const "
        "GLint *params)': names 'GLint', which has no cute class yet.")

  @staticmethod
  def glReadPixels(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glReadPixels(GLint x, GLint y,
    GLsizei width, GLsizei height, GLenum format, GLenum type, GLvoid
    *pixels)': names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glReadPixels' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_4_0_Core::glReadPixels(GLint x, GLint "
        "y, GLsizei width, GLsizei height, GLenum format, GLenum type, "
        "GLvoid *pixels)': names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glSamplerParameterIiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glSamplerParameterIiv(GLuint
    sampler, GLenum pname, const GLint *param)': names 'GLint', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glSamplerParameterIiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glSamplerParameterIiv(GLuint sampler, "
        "GLenum pname, const GLint *param)': names 'GLint', which has no "
        "cute class yet.")

  @staticmethod
  def glSamplerParameterIuiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glSamplerParameterIuiv(GLuint
    sampler, GLenum pname, const GLuint *param)': names 'GLuint', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glSamplerParameterIuiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glSamplerParameterIuiv(GLuint sampler, "
        "GLenum pname, const GLuint *param)': names 'GLuint', which has no "
        "cute class yet.")

  @staticmethod
  def glSamplerParameterfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glSamplerParameterfv(GLuint
    sampler, GLenum pname, const GLfloat *param)': names 'GLfloat', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glSamplerParameterfv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glSamplerParameterfv(GLuint sampler, "
        "GLenum pname, const GLfloat *param)': names 'GLfloat', which has "
        "no cute class yet.")

  @staticmethod
  def glSamplerParameteriv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glSamplerParameteriv(GLuint
    sampler, GLenum pname, const GLint *param)': names 'GLint', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glSamplerParameteriv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glSamplerParameteriv(GLuint sampler, "
        "GLenum pname, const GLint *param)': names 'GLint', which has no "
        "cute class yet.")

  @staticmethod
  def glShaderSource(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glShaderSource(GLuint shader,
    GLsizei count, const GLchar *const *string, const GLint *length)': names
    'GLchar *const', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glShaderSource' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_0_Core::glShaderSource(GLuint "
        "shader, GLsizei count, const GLchar *const *string, const GLint "
        "*length)': names 'GLchar *const', which has no cute class yet.")

  @staticmethod
  def glTexImage1D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glTexImage1D(GLenum target, GLint
    level, GLint internalformat, GLsizei width, GLint border, GLenum format,
    GLenum type, const GLvoid *pixels)': names 'GLvoid', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glTexImage1D' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_4_0_Core::glTexImage1D(GLenum target, "
        "GLint level, GLint internalformat, GLsizei width, GLint border, "
        "GLenum format, GLenum type, const GLvoid *pixels)': names "
        "'GLvoid', which has no cute class yet.")

  @staticmethod
  def glTexImage2D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glTexImage2D(GLenum target, GLint
    level, GLint internalformat, GLsizei width, GLsizei height, GLint border,
    GLenum format, GLenum type, const GLvoid *pixels)': names 'GLvoid', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glTexImage2D' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_4_0_Core::glTexImage2D(GLenum target, "
        "GLint level, GLint internalformat, GLsizei width, GLsizei height, "
        "GLint border, GLenum format, GLenum type, const GLvoid *pixels)': "
        "names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glTexImage3D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glTexImage3D(GLenum target, GLint
    level, GLint internalformat, GLsizei width, GLsizei height, GLsizei
    depth, GLint border, GLenum format, GLenum type, const GLvoid *pixels)':
    names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glTexImage3D' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_4_0_Core::glTexImage3D(GLenum target, "
        "GLint level, GLint internalformat, GLsizei width, GLsizei height, "
        "GLsizei depth, GLint border, GLenum format, GLenum type, const "
        "GLvoid *pixels)': names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glTexParameterIiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glTexParameterIiv(GLenum target,
    GLenum pname, const GLint *params)': names 'GLint', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glTexParameterIiv' has no cute function "
        "yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glTexParameterIiv(GLenum target, GLenum "
        "pname, const GLint *params)': names 'GLint', which has no cute "
        "class yet.")

  @staticmethod
  def glTexParameterIuiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glTexParameterIuiv(GLenum target,
    GLenum pname, const GLuint *params)': names 'GLuint', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glTexParameterIuiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glTexParameterIuiv(GLenum target, "
        "GLenum pname, const GLuint *params)': names 'GLuint', which has no "
        "cute class yet.")

  @staticmethod
  def glTexParameterfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glTexParameterfv(GLenum target,
    GLenum pname, const GLfloat *params)': names 'GLfloat', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glTexParameterfv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_0_Core::glTexParameterfv(GLenum "
        "target, GLenum pname, const GLfloat *params)': names 'GLfloat', "
        "which has no cute class yet.")

  @staticmethod
  def glTexParameteriv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glTexParameteriv(GLenum target,
    GLenum pname, const GLint *params)': names 'GLint', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glTexParameteriv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_0_Core::glTexParameteriv(GLenum "
        "target, GLenum pname, const GLint *params)': names 'GLint', which "
        "has no cute class yet.")

  @staticmethod
  def glTexSubImage1D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glTexSubImage1D(GLenum target,
    GLint level, GLint xoffset, GLsizei width, GLenum format, GLenum type,
    const GLvoid *pixels)': names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glTexSubImage1D' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_0_Core::glTexSubImage1D(GLenum "
        "target, GLint level, GLint xoffset, GLsizei width, GLenum format, "
        "GLenum type, const GLvoid *pixels)': names 'GLvoid', which has no "
        "cute class yet.")

  @staticmethod
  def glTexSubImage2D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glTexSubImage2D(GLenum target,
    GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height,
    GLenum format, GLenum type, const GLvoid *pixels)': names 'GLvoid', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glTexSubImage2D' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_0_Core::glTexSubImage2D(GLenum "
        "target, GLint level, GLint xoffset, GLint yoffset, GLsizei width, "
        "GLsizei height, GLenum format, GLenum type, const GLvoid "
        "*pixels)': names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glTexSubImage3D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glTexSubImage3D(GLenum target,
    GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width,
    GLsizei height, GLsizei depth, GLenum format, GLenum type, const GLvoid
    *pixels)': names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glTexSubImage3D' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_0_Core::glTexSubImage3D(GLenum "
        "target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, "
        "GLsizei width, GLsizei height, GLsizei depth, GLenum format, "
        "GLenum type, const GLvoid *pixels)': names 'GLvoid', which has no "
        "cute class yet.")

  @staticmethod
  def glTransformFeedbackVaryings(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glTransformFeedbackVaryings(GLuint
    program, GLsizei count, const GLchar *const *varyings, GLenum
    bufferMode)': names 'GLchar *const', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glTransformFeedbackVaryings' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glTransformFeedbackVaryings(GLuint "
        "program, GLsizei count, const GLchar *const *varyings, GLenum "
        "bufferMode)': names 'GLchar *const', which has no cute class yet.")

  @staticmethod
  def glUniform1dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glUniform1dv(GLint location,
    GLsizei count, const GLdouble *value)': names 'GLdouble', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glUniform1dv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_4_0_Core::glUniform1dv(GLint location, "
        "GLsizei count, const GLdouble *value)': names 'GLdouble', which "
        "has no cute class yet.")

  @staticmethod
  def glUniform1fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glUniform1fv(GLint location,
    GLsizei count, const GLfloat *value)': names 'GLfloat', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glUniform1fv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_4_0_Core::glUniform1fv(GLint location, "
        "GLsizei count, const GLfloat *value)': names 'GLfloat', which has "
        "no cute class yet.")

  @staticmethod
  def glUniform1iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glUniform1iv(GLint location,
    GLsizei count, const GLint *value)': names 'GLint', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glUniform1iv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_4_0_Core::glUniform1iv(GLint location, "
        "GLsizei count, const GLint *value)': names 'GLint', which has no "
        "cute class yet.")

  @staticmethod
  def glUniform1uiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glUniform1uiv(GLint location,
    GLsizei count, const GLuint *value)': names 'GLuint', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glUniform1uiv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_0_Core::glUniform1uiv(GLint "
        "location, GLsizei count, const GLuint *value)': names 'GLuint', "
        "which has no cute class yet.")

  @staticmethod
  def glUniform2dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glUniform2dv(GLint location,
    GLsizei count, const GLdouble *value)': names 'GLdouble', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glUniform2dv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_4_0_Core::glUniform2dv(GLint location, "
        "GLsizei count, const GLdouble *value)': names 'GLdouble', which "
        "has no cute class yet.")

  @staticmethod
  def glUniform2fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glUniform2fv(GLint location,
    GLsizei count, const GLfloat *value)': names 'GLfloat', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glUniform2fv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_4_0_Core::glUniform2fv(GLint location, "
        "GLsizei count, const GLfloat *value)': names 'GLfloat', which has "
        "no cute class yet.")

  @staticmethod
  def glUniform2iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glUniform2iv(GLint location,
    GLsizei count, const GLint *value)': names 'GLint', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glUniform2iv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_4_0_Core::glUniform2iv(GLint location, "
        "GLsizei count, const GLint *value)': names 'GLint', which has no "
        "cute class yet.")

  @staticmethod
  def glUniform2uiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glUniform2uiv(GLint location,
    GLsizei count, const GLuint *value)': names 'GLuint', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glUniform2uiv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_0_Core::glUniform2uiv(GLint "
        "location, GLsizei count, const GLuint *value)': names 'GLuint', "
        "which has no cute class yet.")

  @staticmethod
  def glUniform3dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glUniform3dv(GLint location,
    GLsizei count, const GLdouble *value)': names 'GLdouble', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glUniform3dv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_4_0_Core::glUniform3dv(GLint location, "
        "GLsizei count, const GLdouble *value)': names 'GLdouble', which "
        "has no cute class yet.")

  @staticmethod
  def glUniform3fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glUniform3fv(GLint location,
    GLsizei count, const GLfloat *value)': names 'GLfloat', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glUniform3fv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_4_0_Core::glUniform3fv(GLint location, "
        "GLsizei count, const GLfloat *value)': names 'GLfloat', which has "
        "no cute class yet.")

  @staticmethod
  def glUniform3iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glUniform3iv(GLint location,
    GLsizei count, const GLint *value)': names 'GLint', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glUniform3iv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_4_0_Core::glUniform3iv(GLint location, "
        "GLsizei count, const GLint *value)': names 'GLint', which has no "
        "cute class yet.")

  @staticmethod
  def glUniform3uiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glUniform3uiv(GLint location,
    GLsizei count, const GLuint *value)': names 'GLuint', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glUniform3uiv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_0_Core::glUniform3uiv(GLint "
        "location, GLsizei count, const GLuint *value)': names 'GLuint', "
        "which has no cute class yet.")

  @staticmethod
  def glUniform4dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glUniform4dv(GLint location,
    GLsizei count, const GLdouble *value)': names 'GLdouble', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glUniform4dv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_4_0_Core::glUniform4dv(GLint location, "
        "GLsizei count, const GLdouble *value)': names 'GLdouble', which "
        "has no cute class yet.")

  @staticmethod
  def glUniform4fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glUniform4fv(GLint location,
    GLsizei count, const GLfloat *value)': names 'GLfloat', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glUniform4fv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_4_0_Core::glUniform4fv(GLint location, "
        "GLsizei count, const GLfloat *value)': names 'GLfloat', which has "
        "no cute class yet.")

  @staticmethod
  def glUniform4iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glUniform4iv(GLint location,
    GLsizei count, const GLint *value)': names 'GLint', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glUniform4iv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_4_0_Core::glUniform4iv(GLint location, "
        "GLsizei count, const GLint *value)': names 'GLint', which has no "
        "cute class yet.")

  @staticmethod
  def glUniform4uiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glUniform4uiv(GLint location,
    GLsizei count, const GLuint *value)': names 'GLuint', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glUniform4uiv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_0_Core::glUniform4uiv(GLint "
        "location, GLsizei count, const GLuint *value)': names 'GLuint', "
        "which has no cute class yet.")

  @staticmethod
  def glUniformMatrix2dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glUniformMatrix2dv(GLint location,
    GLsizei count, GLboolean transpose, const GLdouble *value)': names
    'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glUniformMatrix2dv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glUniformMatrix2dv(GLint location, "
        "GLsizei count, GLboolean transpose, const GLdouble *value)': names "
        "'GLdouble', which has no cute class yet.")

  @staticmethod
  def glUniformMatrix2fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glUniformMatrix2fv(GLint location,
    GLsizei count, GLboolean transpose, const GLfloat *value)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glUniformMatrix2fv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glUniformMatrix2fv(GLint location, "
        "GLsizei count, GLboolean transpose, const GLfloat *value)': names "
        "'GLfloat', which has no cute class yet.")

  @staticmethod
  def glUniformMatrix2x3dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glUniformMatrix2x3dv(GLint
    location, GLsizei count, GLboolean transpose, const GLdouble *value)':
    names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glUniformMatrix2x3dv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glUniformMatrix2x3dv(GLint location, "
        "GLsizei count, GLboolean transpose, const GLdouble *value)': names "
        "'GLdouble', which has no cute class yet.")

  @staticmethod
  def glUniformMatrix2x3fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glUniformMatrix2x3fv(GLint
    location, GLsizei count, GLboolean transpose, const GLfloat *value)':
    names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glUniformMatrix2x3fv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glUniformMatrix2x3fv(GLint location, "
        "GLsizei count, GLboolean transpose, const GLfloat *value)': names "
        "'GLfloat', which has no cute class yet.")

  @staticmethod
  def glUniformMatrix2x4dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glUniformMatrix2x4dv(GLint
    location, GLsizei count, GLboolean transpose, const GLdouble *value)':
    names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glUniformMatrix2x4dv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glUniformMatrix2x4dv(GLint location, "
        "GLsizei count, GLboolean transpose, const GLdouble *value)': names "
        "'GLdouble', which has no cute class yet.")

  @staticmethod
  def glUniformMatrix2x4fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glUniformMatrix2x4fv(GLint
    location, GLsizei count, GLboolean transpose, const GLfloat *value)':
    names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glUniformMatrix2x4fv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glUniformMatrix2x4fv(GLint location, "
        "GLsizei count, GLboolean transpose, const GLfloat *value)': names "
        "'GLfloat', which has no cute class yet.")

  @staticmethod
  def glUniformMatrix3dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glUniformMatrix3dv(GLint location,
    GLsizei count, GLboolean transpose, const GLdouble *value)': names
    'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glUniformMatrix3dv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glUniformMatrix3dv(GLint location, "
        "GLsizei count, GLboolean transpose, const GLdouble *value)': names "
        "'GLdouble', which has no cute class yet.")

  @staticmethod
  def glUniformMatrix3fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glUniformMatrix3fv(GLint location,
    GLsizei count, GLboolean transpose, const GLfloat *value)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glUniformMatrix3fv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glUniformMatrix3fv(GLint location, "
        "GLsizei count, GLboolean transpose, const GLfloat *value)': names "
        "'GLfloat', which has no cute class yet.")

  @staticmethod
  def glUniformMatrix3x2dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glUniformMatrix3x2dv(GLint
    location, GLsizei count, GLboolean transpose, const GLdouble *value)':
    names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glUniformMatrix3x2dv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glUniformMatrix3x2dv(GLint location, "
        "GLsizei count, GLboolean transpose, const GLdouble *value)': names "
        "'GLdouble', which has no cute class yet.")

  @staticmethod
  def glUniformMatrix3x2fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glUniformMatrix3x2fv(GLint
    location, GLsizei count, GLboolean transpose, const GLfloat *value)':
    names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glUniformMatrix3x2fv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glUniformMatrix3x2fv(GLint location, "
        "GLsizei count, GLboolean transpose, const GLfloat *value)': names "
        "'GLfloat', which has no cute class yet.")

  @staticmethod
  def glUniformMatrix3x4dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glUniformMatrix3x4dv(GLint
    location, GLsizei count, GLboolean transpose, const GLdouble *value)':
    names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glUniformMatrix3x4dv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glUniformMatrix3x4dv(GLint location, "
        "GLsizei count, GLboolean transpose, const GLdouble *value)': names "
        "'GLdouble', which has no cute class yet.")

  @staticmethod
  def glUniformMatrix3x4fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glUniformMatrix3x4fv(GLint
    location, GLsizei count, GLboolean transpose, const GLfloat *value)':
    names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glUniformMatrix3x4fv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glUniformMatrix3x4fv(GLint location, "
        "GLsizei count, GLboolean transpose, const GLfloat *value)': names "
        "'GLfloat', which has no cute class yet.")

  @staticmethod
  def glUniformMatrix4dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glUniformMatrix4dv(GLint location,
    GLsizei count, GLboolean transpose, const GLdouble *value)': names
    'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glUniformMatrix4dv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glUniformMatrix4dv(GLint location, "
        "GLsizei count, GLboolean transpose, const GLdouble *value)': names "
        "'GLdouble', which has no cute class yet.")

  @staticmethod
  def glUniformMatrix4fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glUniformMatrix4fv(GLint location,
    GLsizei count, GLboolean transpose, const GLfloat *value)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glUniformMatrix4fv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glUniformMatrix4fv(GLint location, "
        "GLsizei count, GLboolean transpose, const GLfloat *value)': names "
        "'GLfloat', which has no cute class yet.")

  @staticmethod
  def glUniformMatrix4x2dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glUniformMatrix4x2dv(GLint
    location, GLsizei count, GLboolean transpose, const GLdouble *value)':
    names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glUniformMatrix4x2dv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glUniformMatrix4x2dv(GLint location, "
        "GLsizei count, GLboolean transpose, const GLdouble *value)': names "
        "'GLdouble', which has no cute class yet.")

  @staticmethod
  def glUniformMatrix4x2fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glUniformMatrix4x2fv(GLint
    location, GLsizei count, GLboolean transpose, const GLfloat *value)':
    names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glUniformMatrix4x2fv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glUniformMatrix4x2fv(GLint location, "
        "GLsizei count, GLboolean transpose, const GLfloat *value)': names "
        "'GLfloat', which has no cute class yet.")

  @staticmethod
  def glUniformMatrix4x3dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glUniformMatrix4x3dv(GLint
    location, GLsizei count, GLboolean transpose, const GLdouble *value)':
    names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glUniformMatrix4x3dv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glUniformMatrix4x3dv(GLint location, "
        "GLsizei count, GLboolean transpose, const GLdouble *value)': names "
        "'GLdouble', which has no cute class yet.")

  @staticmethod
  def glUniformMatrix4x3fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glUniformMatrix4x3fv(GLint
    location, GLsizei count, GLboolean transpose, const GLfloat *value)':
    names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glUniformMatrix4x3fv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glUniformMatrix4x3fv(GLint location, "
        "GLsizei count, GLboolean transpose, const GLfloat *value)': names "
        "'GLfloat', which has no cute class yet.")

  @staticmethod
  def glUniformSubroutinesuiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glUniformSubroutinesuiv(GLenum
    shadertype, GLsizei count, const GLuint *indices)': names 'GLuint', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glUniformSubroutinesuiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glUniformSubroutinesuiv(GLenum "
        "shadertype, GLsizei count, const GLuint *indices)': names "
        "'GLuint', which has no cute class yet.")

  @staticmethod
  def glVertexAttribIPointer(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glVertexAttribIPointer(GLuint
    index, GLint size, GLenum type, GLsizei stride, const GLvoid *pointer)':
    names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glVertexAttribIPointer' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glVertexAttribIPointer(GLuint index, "
        "GLint size, GLenum type, GLsizei stride, const GLvoid *pointer)': "
        "names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glVertexAttribP1uiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glVertexAttribP1uiv(GLuint index,
    GLenum type, GLboolean normalized, const GLuint *value)': names 'GLuint',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glVertexAttribP1uiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glVertexAttribP1uiv(GLuint index, "
        "GLenum type, GLboolean normalized, const GLuint *value)': names "
        "'GLuint', which has no cute class yet.")

  @staticmethod
  def glVertexAttribP2uiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glVertexAttribP2uiv(GLuint index,
    GLenum type, GLboolean normalized, const GLuint *value)': names 'GLuint',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glVertexAttribP2uiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glVertexAttribP2uiv(GLuint index, "
        "GLenum type, GLboolean normalized, const GLuint *value)': names "
        "'GLuint', which has no cute class yet.")

  @staticmethod
  def glVertexAttribP3uiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glVertexAttribP3uiv(GLuint index,
    GLenum type, GLboolean normalized, const GLuint *value)': names 'GLuint',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glVertexAttribP3uiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glVertexAttribP3uiv(GLuint index, "
        "GLenum type, GLboolean normalized, const GLuint *value)': names "
        "'GLuint', which has no cute class yet.")

  @staticmethod
  def glVertexAttribP4uiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glVertexAttribP4uiv(GLuint index,
    GLenum type, GLboolean normalized, const GLuint *value)': names 'GLuint',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glVertexAttribP4uiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glVertexAttribP4uiv(GLuint index, "
        "GLenum type, GLboolean normalized, const GLuint *value)': names "
        "'GLuint', which has no cute class yet.")

  @staticmethod
  def glVertexAttribPointer(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glVertexAttribPointer(GLuint index,
    GLint size, GLenum type, GLboolean normalized, GLsizei stride, const
    GLvoid *pointer)': names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glVertexAttribPointer' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_0_Core::glVertexAttribPointer(GLuint index, "
        "GLint size, GLenum type, GLboolean normalized, GLsizei stride, "
        "const GLvoid *pointer)': names 'GLvoid', which has no cute class "
        "yet.")

  @staticmethod
  def glWaitSync(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_0_Core::glWaitSync(GLsync sync, GLbitfield
    flags, GLuint64 timeout)': names 'struct __GLsync', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_0_Core.glWaitSync' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_4_0_Core::glWaitSync(GLsync sync, "
        "GLbitfield flags, GLuint64 timeout)': names 'struct __GLsync', "
        "which has no cute class yet.")
