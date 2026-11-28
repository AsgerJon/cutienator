"""
QOpenGLFunctions_3_1 binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpenGL/qopenglfunctions_3_1.h, Qt 6.12.0. Changes made here are lost.
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


class QOpenGLFunctions_3_1(QAbstractOpenGLFunctions):
  """
  The cute side of Qt's QOpenGLFunctions_3_1: a plain Python object standing
  in front of one C++ QOpenGLFunctions_3_1.

  It is built on the cute 'QAbstractOpenGLFunctions', as Qt's
  QOpenGLFunctions_3_1 is built on Qt's QAbstractOpenGLFunctions, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QOpenGLFunctions_3_1 that has a ritual and that
  Python can call so far, 122 names in all: 'initializeOpenGLFunctions',
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
  'glTexBuffer', 'glDrawArraysInstanced', 'isContextCompatible',
  'versionProfile'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpenGLFunctions_3_1::~QOpenGLFunctions_3_1()': the destructor:
    Python never removes a C++ QOpenGLFunctions_3_1.
  - Qt's 'void QOpenGLFunctions_3_1::glGetTexLevelParameteriv(GLenum target,
    GLint level, GLenum pname, GLint *params)': takes a number to change
    where it is.
  - Qt's 'void QOpenGLFunctions_3_1::glGetTexLevelParameterfv(GLenum target,
    GLint level, GLenum pname, GLfloat *params)': takes a number to change
    where it is.
  - Qt's 'void QOpenGLFunctions_3_1::glGetTexParameteriv(GLenum target,
    GLenum pname, GLint *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_3_1::glGetTexParameterfv(GLenum target,
    GLenum pname, GLfloat *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_3_1::glGetTexImage(GLenum target, GLint
    level, GLenum format, GLenum type, GLvoid *pixels)': names 'GLvoid',
    which has no cute class yet.
  - Qt's 'const GLubyte *QOpenGLFunctions_3_1::glGetString(GLenum name)':
    gives 'unsigned char', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_3_1::glGetIntegerv(GLenum pname, GLint
    *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_3_1::glGetFloatv(GLenum pname, GLfloat
    *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_3_1::glGetDoublev(GLenum pname, GLdouble
    *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_3_1::glGetBooleanv(GLenum pname, GLboolean
    *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_3_1::glReadPixels(GLint x, GLint y, GLsizei
    width, GLsizei height, GLenum format, GLenum type, GLvoid *pixels)':
    names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_3_1::glTexImage2D(GLenum target, GLint level,
    GLint internalformat, GLsizei width, GLsizei height, GLint border, GLenum
    format, GLenum type, const GLvoid *pixels)': names 'GLvoid', which has no
    cute class yet.
  - Qt's 'void QOpenGLFunctions_3_1::glTexImage1D(GLenum target, GLint level,
    GLint internalformat, GLsizei width, GLint border, GLenum format, GLenum
    type, const GLvoid *pixels)': names 'GLvoid', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_3_1::glTexParameteriv(GLenum target, GLenum
    pname, const GLint *params)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_3_1::glTexParameterfv(GLenum target, GLenum
    pname, const GLfloat *params)': names 'GLfloat', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_3_1::glGenTextures(GLsizei n, GLuint
    *textures)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_3_1::glDeleteTextures(GLsizei n, const GLuint
    *textures)': names 'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_3_1::glTexSubImage2D(GLenum target, GLint
    level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height,
    GLenum format, GLenum type, const GLvoid *pixels)': names 'GLvoid', which
    has no cute class yet.
  - Qt's 'void QOpenGLFunctions_3_1::glTexSubImage1D(GLenum target, GLint
    level, GLint xoffset, GLsizei width, GLenum format, GLenum type, const
    GLvoid *pixels)': names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_3_1::glDrawElements(GLenum mode, GLsizei
    count, GLenum type, const GLvoid *indices)': names 'GLvoid', which has no
    cute class yet.
  - Qt's 'void QOpenGLFunctions_3_1::glTexSubImage3D(GLenum target, GLint
    level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width,
    GLsizei height, GLsizei depth, GLenum format, GLenum type, const GLvoid
    *pixels)': names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_3_1::glTexImage3D(GLenum target, GLint level,
    GLint internalformat, GLsizei width, GLsizei height, GLsizei depth, GLint
    border, GLenum format, GLenum type, const GLvoid *pixels)': names
    'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_3_1::glDrawRangeElements(GLenum mode, GLuint
    start, GLuint end, GLsizei count, GLenum type, const GLvoid *indices)':
    names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_3_1::glGetCompressedTexImage(GLenum target,
    GLint level, GLvoid *img)': names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_3_1::glCompressedTexSubImage1D(GLenum target,
    GLint level, GLint xoffset, GLsizei width, GLenum format, GLsizei
    imageSize, const GLvoid *data)': names 'GLvoid', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_3_1::glCompressedTexSubImage2D(GLenum target,
    GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height,
    GLenum format, GLsizei imageSize, const GLvoid *data)': names 'GLvoid',
    which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_3_1::glCompressedTexSubImage3D(GLenum target,
    GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width,
    GLsizei height, GLsizei depth, GLenum format, GLsizei imageSize, const
    GLvoid *data)': names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_3_1::glCompressedTexImage1D(GLenum target,
    GLint level, GLenum internalformat, GLsizei width, GLint border, GLsizei
    imageSize, const GLvoid *data)': names 'GLvoid', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_3_1::glCompressedTexImage2D(GLenum target,
    GLint level, GLenum internalformat, GLsizei width, GLsizei height, GLint
    border, GLsizei imageSize, const GLvoid *data)': names 'GLvoid', which
    has no cute class yet.
  - Qt's 'void QOpenGLFunctions_3_1::glCompressedTexImage3D(GLenum target,
    GLint level, GLenum internalformat, GLsizei width, GLsizei height,
    GLsizei depth, GLint border, GLsizei imageSize, const GLvoid *data)':
    names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_3_1::glPointParameteriv(GLenum pname, const
    GLint *params)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_3_1::glPointParameterfv(GLenum pname, const
    GLfloat *params)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_3_1::glMultiDrawElements(GLenum mode, const
    GLsizei *count, GLenum type, const GLvoid *const *indices, GLsizei
    drawcount)': names 'GLsizei', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_3_1::glMultiDrawArrays(GLenum mode, const
    GLint *first, const GLsizei *count, GLsizei drawcount)': names 'GLint',
    which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_3_1::glGetBufferPointerv(GLenum target,
    GLenum pname, GLvoid **params)': takes a type Python has no way to hand
    over yet.
  - Qt's 'void QOpenGLFunctions_3_1::glGetBufferParameteriv(GLenum target,
    GLenum pname, GLint *params)': takes a number to change where it is.
  - Qt's 'GLvoid *QOpenGLFunctions_3_1::glMapBuffer(GLenum target, GLenum
    access)': gives 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_3_1::glGetBufferSubData(GLenum target,
    GLintptr offset, GLsizeiptr size, GLvoid *data)': names 'GLvoid', which
    has no cute class yet.
  - Qt's 'void QOpenGLFunctions_3_1::glBufferSubData(GLenum target, GLintptr
    offset, GLsizeiptr size, const GLvoid *data)': names 'GLvoid', which has
    no cute class yet.
  - Qt's 'void QOpenGLFunctions_3_1::glBufferData(GLenum target, GLsizeiptr
    size, const GLvoid *data, GLenum usage)': names 'GLvoid', which has no
    cute class yet.
  - Qt's 'void QOpenGLFunctions_3_1::glGenBuffers(GLsizei n, GLuint
    *buffers)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_3_1::glDeleteBuffers(GLsizei n, const GLuint
    *buffers)': names 'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_3_1::glGetQueryObjectuiv(GLuint id, GLenum
    pname, GLuint *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_3_1::glGetQueryObjectiv(GLuint id, GLenum
    pname, GLint *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_3_1::glGetQueryiv(GLenum target, GLenum
    pname, GLint *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_3_1::glDeleteQueries(GLsizei n, const GLuint
    *ids)': names 'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_3_1::glGenQueries(GLsizei n, GLuint *ids)':
    takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_3_1::glVertexAttribPointer(GLuint index,
    GLint size, GLenum type, GLboolean normalized, GLsizei stride, const
    GLvoid *pointer)': names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_3_1::glUniformMatrix4fv(GLint location,
    GLsizei count, GLboolean transpose, const GLfloat *value)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_3_1::glUniformMatrix3fv(GLint location,
    GLsizei count, GLboolean transpose, const GLfloat *value)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_3_1::glUniformMatrix2fv(GLint location,
    GLsizei count, GLboolean transpose, const GLfloat *value)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_3_1::glUniform4iv(GLint location, GLsizei
    count, const GLint *value)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_3_1::glUniform3iv(GLint location, GLsizei
    count, const GLint *value)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_3_1::glUniform2iv(GLint location, GLsizei
    count, const GLint *value)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_3_1::glUniform1iv(GLint location, GLsizei
    count, const GLint *value)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_3_1::glUniform4fv(GLint location, GLsizei
    count, const GLfloat *value)': names 'GLfloat', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_3_1::glUniform3fv(GLint location, GLsizei
    count, const GLfloat *value)': names 'GLfloat', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_3_1::glUniform2fv(GLint location, GLsizei
    count, const GLfloat *value)': names 'GLfloat', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_3_1::glUniform1fv(GLint location, GLsizei
    count, const GLfloat *value)': names 'GLfloat', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_3_1::glShaderSource(GLuint shader, GLsizei
    count, const GLchar *const *string, const GLint *length)': names 'GLchar
    *const', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_3_1::glGetVertexAttribPointerv(GLuint index,
    GLenum pname, GLvoid **pointer)': takes a type Python has no way to hand
    over yet.
  - Qt's 'void QOpenGLFunctions_3_1::glGetVertexAttribiv(GLuint index, GLenum
    pname, GLint *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_3_1::glGetVertexAttribfv(GLuint index, GLenum
    pname, GLfloat *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_3_1::glGetVertexAttribdv(GLuint index, GLenum
    pname, GLdouble *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_3_1::glGetUniformiv(GLuint program, GLint
    location, GLint *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_3_1::glGetUniformfv(GLuint program, GLint
    location, GLfloat *params)': takes a number to change where it is.
  - Qt's 'GLint QOpenGLFunctions_3_1::glGetUniformLocation(GLuint program,
    const GLchar *name)': names 'GLchar', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_3_1::glGetShaderSource(GLuint shader, GLsizei
    bufSize, GLsizei *length, GLchar *source)': takes a number to change
    where it is.
  - Qt's 'void QOpenGLFunctions_3_1::glGetShaderInfoLog(GLuint shader,
    GLsizei bufSize, GLsizei *length, GLchar *infoLog)': takes a number to
    change where it is.
  - Qt's 'void QOpenGLFunctions_3_1::glGetShaderiv(GLuint shader, GLenum
    pname, GLint *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_3_1::glGetProgramInfoLog(GLuint program,
    GLsizei bufSize, GLsizei *length, GLchar *infoLog)': takes a number to
    change where it is.
  - Qt's 'void QOpenGLFunctions_3_1::glGetProgramiv(GLuint program, GLenum
    pname, GLint *params)': takes a number to change where it is.
  - Qt's 'GLint QOpenGLFunctions_3_1::glGetAttribLocation(GLuint program,
    const GLchar *name)': names 'GLchar', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_3_1::glGetAttachedShaders(GLuint program,
    GLsizei maxCount, GLsizei *count, GLuint *obj)': takes a number to change
    where it is.
  - Qt's 'void QOpenGLFunctions_3_1::glGetActiveUniform(GLuint program,
    GLuint index, GLsizei bufSize, GLsizei *length, GLint *size, GLenum
    *type, GLchar *name)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_3_1::glGetActiveAttrib(GLuint program, GLuint
    index, GLsizei bufSize, GLsizei *length, GLint *size, GLenum *type,
    GLchar *name)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_3_1::glBindAttribLocation(GLuint program,
    GLuint index, const GLchar *name)': names 'GLchar', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_3_1::glDrawBuffers(GLsizei n, const GLenum
    *bufs)': names 'GLenum', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_3_1::glUniformMatrix4x3fv(GLint location,
    GLsizei count, GLboolean transpose, const GLfloat *value)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_3_1::glUniformMatrix3x4fv(GLint location,
    GLsizei count, GLboolean transpose, const GLfloat *value)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_3_1::glUniformMatrix4x2fv(GLint location,
    GLsizei count, GLboolean transpose, const GLfloat *value)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_3_1::glUniformMatrix2x4fv(GLint location,
    GLsizei count, GLboolean transpose, const GLfloat *value)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_3_1::glUniformMatrix3x2fv(GLint location,
    GLsizei count, GLboolean transpose, const GLfloat *value)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_3_1::glUniformMatrix2x3fv(GLint location,
    GLsizei count, GLboolean transpose, const GLfloat *value)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_3_1::glGenVertexArrays(GLsizei n, GLuint
    *arrays)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_3_1::glDeleteVertexArrays(GLsizei n, const
    GLuint *arrays)': names 'GLuint', which has no cute class yet.
  - Qt's 'GLvoid *QOpenGLFunctions_3_1::glMapBufferRange(GLenum target,
    GLintptr offset, GLsizeiptr length, GLbitfield access)': gives 'GLvoid',
    which has no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_3_1::glGetFramebufferAttachmentParameteriv(GLenum
    target, GLenum attachment, GLenum pname, GLint *params)': takes a number
    to change where it is.
  - Qt's 'void QOpenGLFunctions_3_1::glGenFramebuffers(GLsizei n, GLuint
    *framebuffers)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_3_1::glDeleteFramebuffers(GLsizei n, const
    GLuint *framebuffers)': names 'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_3_1::glGetRenderbufferParameteriv(GLenum
    target, GLenum pname, GLint *params)': takes a number to change where it
    is.
  - Qt's 'void QOpenGLFunctions_3_1::glGenRenderbuffers(GLsizei n, GLuint
    *renderbuffers)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_3_1::glDeleteRenderbuffers(GLsizei n, const
    GLuint *renderbuffers)': names 'GLuint', which has no cute class yet.
  - Qt's 'const GLubyte *QOpenGLFunctions_3_1::glGetStringi(GLenum name,
    GLuint index)': gives 'unsigned char', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_3_1::glClearBufferfv(GLenum buffer, GLint
    drawbuffer, const GLfloat *value)': names 'GLfloat', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_3_1::glClearBufferuiv(GLenum buffer, GLint
    drawbuffer, const GLuint *value)': names 'GLuint', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_3_1::glClearBufferiv(GLenum buffer, GLint
    drawbuffer, const GLint *value)': names 'GLint', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_3_1::glGetTexParameterIuiv(GLenum target,
    GLenum pname, GLuint *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_3_1::glGetTexParameterIiv(GLenum target,
    GLenum pname, GLint *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_3_1::glTexParameterIuiv(GLenum target, GLenum
    pname, const GLuint *params)': names 'GLuint', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_3_1::glTexParameterIiv(GLenum target, GLenum
    pname, const GLint *params)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_3_1::glUniform4uiv(GLint location, GLsizei
    count, const GLuint *value)': names 'GLuint', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_3_1::glUniform3uiv(GLint location, GLsizei
    count, const GLuint *value)': names 'GLuint', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_3_1::glUniform2uiv(GLint location, GLsizei
    count, const GLuint *value)': names 'GLuint', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_3_1::glUniform1uiv(GLint location, GLsizei
    count, const GLuint *value)': names 'GLuint', which has no cute class
    yet.
  - Qt's 'GLint QOpenGLFunctions_3_1::glGetFragDataLocation(GLuint program,
    const GLchar *name)': names 'GLchar', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_3_1::glBindFragDataLocation(GLuint program,
    GLuint color, const GLchar *name)': names 'GLchar', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_3_1::glGetUniformuiv(GLuint program, GLint
    location, GLuint *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_3_1::glGetVertexAttribIuiv(GLuint index,
    GLenum pname, GLuint *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_3_1::glGetVertexAttribIiv(GLuint index,
    GLenum pname, GLint *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_3_1::glVertexAttribIPointer(GLuint index,
    GLint size, GLenum type, GLsizei stride, const GLvoid *pointer)': names
    'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_3_1::glGetTransformFeedbackVarying(GLuint
    program, GLuint index, GLsizei bufSize, GLsizei *length, GLsizei *size,
    GLenum *type, GLchar *name)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_3_1::glTransformFeedbackVaryings(GLuint
    program, GLsizei count, const GLchar *const *varyings, GLenum
    bufferMode)': names 'GLchar *const', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_3_1::glGetIntegeri_v(GLenum target, GLuint
    index, GLint *data)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_3_1::glGetBooleani_v(GLenum target, GLuint
    index, GLboolean *data)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_3_1::glGetActiveUniformBlockName(GLuint
    program, GLuint uniformBlockIndex, GLsizei bufSize, GLsizei *length,
    GLchar *uniformBlockName)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_3_1::glGetActiveUniformBlockiv(GLuint
    program, GLuint uniformBlockIndex, GLenum pname, GLint *params)': takes a
    number to change where it is.
  - Qt's 'GLuint QOpenGLFunctions_3_1::glGetUniformBlockIndex(GLuint program,
    const GLchar *uniformBlockName)': names 'GLchar', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_3_1::glGetActiveUniformName(GLuint program,
    GLuint uniformIndex, GLsizei bufSize, GLsizei *length, GLchar
    *uniformName)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_3_1::glGetActiveUniformsiv(GLuint program,
    GLsizei uniformCount, const GLuint *uniformIndices, GLenum pname, GLint
    *params)': names 'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_3_1::glGetUniformIndices(GLuint program,
    GLsizei uniformCount, const GLchar *const *uniformNames, GLuint
    *uniformIndices)': names 'GLchar *const', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_3_1::glDrawElementsInstanced(GLenum mode,
    GLsizei count, GLenum type, const GLvoid *indices, GLsizei
    instancecount)': names 'GLvoid', which has no cute class yet.

  What to expect
  --------------

  - The C++ QOpenGLFunctions_3_1 is created at the first use, not by
    'QOpenGLFunctions_3_1(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QOpenGLFunctions_3_1.
  - Each name of Qt's QOpenGLFunctions_3_1 that has no cute function yet,
    'glBindAttribLocation', 'glBindFragDataLocation', 'glBufferData',
    'glBufferSubData', 'glClearBufferfv', 'glClearBufferiv',
    'glClearBufferuiv', 'glCompressedTexImage1D', 'glCompressedTexImage2D',
    'glCompressedTexImage3D', 'glCompressedTexSubImage1D',
    'glCompressedTexSubImage2D', 'glCompressedTexSubImage3D',
    'glDeleteBuffers', 'glDeleteFramebuffers', 'glDeleteQueries',
    'glDeleteRenderbuffers', 'glDeleteTextures', 'glDeleteVertexArrays',
    'glDrawBuffers', 'glDrawElements', 'glDrawElementsInstanced',
    'glDrawRangeElements', 'glGenBuffers', 'glGenFramebuffers',
    'glGenQueries', 'glGenRenderbuffers', 'glGenTextures',
    'glGenVertexArrays', 'glGetActiveAttrib', 'glGetActiveUniform',
    'glGetActiveUniformBlockName', 'glGetActiveUniformBlockiv',
    'glGetActiveUniformName', 'glGetActiveUniformsiv',
    'glGetAttachedShaders', 'glGetAttribLocation', 'glGetBooleani_v',
    'glGetBooleanv', 'glGetBufferParameteriv', 'glGetBufferPointerv',
    'glGetBufferSubData', 'glGetCompressedTexImage', 'glGetDoublev',
    'glGetFloatv', 'glGetFragDataLocation',
    'glGetFramebufferAttachmentParameteriv', 'glGetIntegeri_v',
    'glGetIntegerv', 'glGetProgramInfoLog', 'glGetProgramiv',
    'glGetQueryObjectiv', 'glGetQueryObjectuiv', 'glGetQueryiv',
    'glGetRenderbufferParameteriv', 'glGetShaderInfoLog',
    'glGetShaderSource', 'glGetShaderiv', 'glGetString', 'glGetStringi',
    'glGetTexImage', 'glGetTexLevelParameterfv', 'glGetTexLevelParameteriv',
    'glGetTexParameterIiv', 'glGetTexParameterIuiv', 'glGetTexParameterfv',
    'glGetTexParameteriv', 'glGetTransformFeedbackVarying',
    'glGetUniformBlockIndex', 'glGetUniformIndices', 'glGetUniformLocation',
    'glGetUniformfv', 'glGetUniformiv', 'glGetUniformuiv',
    'glGetVertexAttribIiv', 'glGetVertexAttribIuiv',
    'glGetVertexAttribPointerv', 'glGetVertexAttribdv',
    'glGetVertexAttribfv', 'glGetVertexAttribiv', 'glMapBuffer',
    'glMapBufferRange', 'glMultiDrawArrays', 'glMultiDrawElements',
    'glPointParameterfv', 'glPointParameteriv', 'glReadPixels',
    'glShaderSource', 'glTexImage1D', 'glTexImage2D', 'glTexImage3D',
    'glTexParameterIiv', 'glTexParameterIuiv', 'glTexParameterfv',
    'glTexParameteriv', 'glTexSubImage1D', 'glTexSubImage2D',
    'glTexSubImage3D', 'glTransformFeedbackVaryings', 'glUniform1fv',
    'glUniform1iv', 'glUniform1uiv', 'glUniform2fv', 'glUniform2iv',
    'glUniform2uiv', 'glUniform3fv', 'glUniform3iv', 'glUniform3uiv',
    'glUniform4fv', 'glUniform4iv', 'glUniform4uiv', 'glUniformMatrix2fv',
    'glUniformMatrix2x3fv', 'glUniformMatrix2x4fv', 'glUniformMatrix3fv',
    'glUniformMatrix3x2fv', 'glUniformMatrix3x4fv', 'glUniformMatrix4fv',
    'glUniformMatrix4x2fv', 'glUniformMatrix4x3fv', 'glVertexAttribIPointer',
    'glVertexAttribPointer', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QOpenGLContext)
  @overload(NoneType)
  def isContextCompatible(context: Optional[QOpenGLContext]) -> bool:
    """
    Calls Qt's 'bool QOpenGLFunctions_3_1::isContextCompatible(QOpenGLContext
    *context)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#isContextCompatible

    Parameters
    ----------

    context : Optional[QOpenGLContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QOpenGLFunctions_3_1::isContextCompatible(QOpenGLContext
    #      *context)
    return Rituals.call(
        'ritual_ZN20QOpenGLFunctions_3_119isContextCompatibleEP14QOpenGLCon'
        'text',
        CuteMixin._addressOf(context),
    )

  @staticmethod
  def versionProfile() -> QOpenGLVersionProfile:
    """
    Calls Qt's 'QOpenGLVersionProfile
    QOpenGLFunctions_3_1::versionProfile()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#versionProfile

    Returns
    -------

    QOpenGLVersionProfile
      A new cute QOpenGLVersionProfile around the copy Qt gave back. Python
      owns it.
    """
    #  QOpenGLVersionProfile QOpenGLFunctions_3_1::versionProfile()
    address = Rituals.call(
        'ritual_ZN20QOpenGLFunctions_3_114versionProfileEv',
    )
    from . import QOpenGLVersionProfile
    return QOpenGLVersionProfile._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpenGLFunctions_3_1'

  #  A C++ QOpenGLFunctions_3_1 Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QOpenGLFunctions_3_1'

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
    'QOpenGLFunctions_3_1::QOpenGLFunctions_3_1()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#QOpenGLFunctions_3_1
    """
    #  QOpenGLFunctions_3_1::QOpenGLFunctions_3_1()
    self._noteCreation(QOpenGLFunctions_3_1, lambda: Rituals.call(
        'ritual_ZN20QOpenGLFunctions_3_1C1Ev',
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
    Calls Qt's 'bool QOpenGLFunctions_3_1::initializeOpenGLFunctions()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html
    """
    #  bool QOpenGLFunctions_3_1::initializeOpenGLFunctions()
    ritual = 'ritual_ZN20QOpenGLFunctions_3_125initializeOpenGLFunctionsEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QOpenGLFunctions_3_125initializeOpenGLFunctionsEv')
    return self.uglySide.call(ritual)

  @overload(int, int, int, int)
  def glViewport(self, x: int, y: int, width: int, height: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glViewport(GLint x, GLint y,
    GLsizei width, GLsizei height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glViewport

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
    #  void QOpenGLFunctions_3_1::glViewport(GLint x, GLint y, GLsizei width,
    #      GLsizei height)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_110glViewportEiiii',
        x, y, width, height,
    )

  @overload(float, float)
  def glDepthRange(self, nearVal: float, farVal: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glDepthRange(GLdouble nearVal,
    GLdouble farVal)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glDepthRange

    Parameters
    ----------

    nearVal : float
      Passed on as it is.

    farVal : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_3_1::glDepthRange(GLdouble nearVal, GLdouble
    #      farVal)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_112glDepthRangeEdd', nearVal, farVal,
    )

  @overload(int)
  def glIsEnabled(self, cap: int) -> int:
    """
    Calls Qt's 'GLboolean QOpenGLFunctions_3_1::glIsEnabled(GLenum cap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glIsEnabled

    Parameters
    ----------

    cap : int
      Passed on as it is.
    """
    #  GLboolean QOpenGLFunctions_3_1::glIsEnabled(GLenum cap)
    return self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_111glIsEnabledEj', cap,
    )

  def glGetError(self) -> int:
    """
    Calls Qt's 'GLenum QOpenGLFunctions_3_1::glGetError()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glGetError
    """
    #  GLenum QOpenGLFunctions_3_1::glGetError()
    return self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_110glGetErrorEv',
    )

  @overload(int)
  def glReadBuffer(self, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glReadBuffer(GLenum mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glReadBuffer

    Parameters
    ----------

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_3_1::glReadBuffer(GLenum mode)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_112glReadBufferEj', mode,
    )

  @overload(int, int)
  def glPixelStorei(self, pname: int, param: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glPixelStorei(GLenum pname, GLint
    param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glPixelStorei

    Parameters
    ----------

    pname : int
      Passed on as it is.

    param : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_3_1::glPixelStorei(GLenum pname, GLint param)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_113glPixelStoreiEji', pname, param,
    )

  @overload(int, float)
  def glPixelStoref(self, pname: int, param: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glPixelStoref(GLenum pname,
    GLfloat param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glPixelStoref

    Parameters
    ----------

    pname : int
      Passed on as it is.

    param : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_3_1::glPixelStoref(GLenum pname, GLfloat param)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_113glPixelStorefEjf', pname, param,
    )

  @overload(int)
  def glDepthFunc(self, func: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glDepthFunc(GLenum func)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glDepthFunc

    Parameters
    ----------

    func : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_3_1::glDepthFunc(GLenum func)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_111glDepthFuncEj', func,
    )

  @overload(int, int, int)
  def glStencilOp(self, fail: int, zfail: int, zpass: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glStencilOp(GLenum fail, GLenum
    zfail, GLenum zpass)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glStencilOp

    Parameters
    ----------

    fail : int
      Passed on as it is.

    zfail : int
      Passed on as it is.

    zpass : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_3_1::glStencilOp(GLenum fail, GLenum zfail,
    #      GLenum zpass)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_111glStencilOpEjjj',
        fail, zfail, zpass,
    )

  @overload(int, int, int)
  def glStencilFunc(self, func: int, ref: int, mask: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glStencilFunc(GLenum func, GLint
    ref, GLuint mask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glStencilFunc

    Parameters
    ----------

    func : int
      Passed on as it is.

    ref : int
      Passed on as it is.

    mask : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_3_1::glStencilFunc(GLenum func, GLint ref,
    #      GLuint mask)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_113glStencilFuncEjij',
        func, ref, mask,
    )

  @overload(int)
  def glLogicOp(self, opcode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glLogicOp(GLenum opcode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glLogicOp

    Parameters
    ----------

    opcode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_3_1::glLogicOp(GLenum opcode)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_3_19glLogicOpEj', opcode)

  @overload(int, int)
  def glBlendFunc(self, sfactor: int, dfactor: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glBlendFunc(GLenum sfactor, GLenum
    dfactor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glBlendFunc

    Parameters
    ----------

    sfactor : int
      Passed on as it is.

    dfactor : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_3_1::glBlendFunc(GLenum sfactor, GLenum dfactor)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_111glBlendFuncEjj', sfactor, dfactor,
    )

  def glFlush(self) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glFlush()'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glFlush
    """
    #  void QOpenGLFunctions_3_1::glFlush()
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_3_17glFlushEv')

  def glFinish(self) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glFinish()'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glFinish
    """
    #  void QOpenGLFunctions_3_1::glFinish()
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_3_18glFinishEv')

  @overload(int)
  def glEnable(self, cap: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glEnable(GLenum cap)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glEnable

    Parameters
    ----------

    cap : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_3_1::glEnable(GLenum cap)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_3_18glEnableEj', cap)

  @overload(int)
  def glDisable(self, cap: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glDisable(GLenum cap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glDisable

    Parameters
    ----------

    cap : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_3_1::glDisable(GLenum cap)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_3_19glDisableEj', cap)

  @overload(int)
  def glDepthMask(self, flag: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glDepthMask(GLboolean flag)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glDepthMask

    Parameters
    ----------

    flag : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_3_1::glDepthMask(GLboolean flag)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_111glDepthMaskEh', flag,
    )

  @overload(int, int, int, int)
  def glColorMask(self, red: int, green: int, blue: int, alpha: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glColorMask(GLboolean red,
    GLboolean green, GLboolean blue, GLboolean alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glColorMask

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
    #  void QOpenGLFunctions_3_1::glColorMask(GLboolean red, GLboolean green,
    #      GLboolean blue, GLboolean alpha)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_111glColorMaskEhhhh',
        red, green, blue, alpha,
    )

  @overload(int)
  def glStencilMask(self, mask: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glStencilMask(GLuint mask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glStencilMask

    Parameters
    ----------

    mask : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_3_1::glStencilMask(GLuint mask)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_113glStencilMaskEj', mask,
    )

  @overload(float)
  def glClearDepth(self, depth: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glClearDepth(GLdouble depth)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glClearDepth

    Parameters
    ----------

    depth : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_3_1::glClearDepth(GLdouble depth)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_112glClearDepthEd', depth,
    )

  @overload(int)
  def glClearStencil(self, s: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glClearStencil(GLint s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glClearStencil

    Parameters
    ----------

    s : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_3_1::glClearStencil(GLint s)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_114glClearStencilEi', s,
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
    Calls Qt's 'void QOpenGLFunctions_3_1::glClearColor(GLfloat red, GLfloat
    green, GLfloat blue, GLfloat alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glClearColor

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
    #  void QOpenGLFunctions_3_1::glClearColor(GLfloat red, GLfloat green,
    #      GLfloat blue, GLfloat alpha)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_112glClearColorEffff',
        red, green, blue, alpha,
    )

  @overload(int)
  def glClear(self, mask: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glClear(GLbitfield mask)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glClear

    Parameters
    ----------

    mask : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_3_1::glClear(GLbitfield mask)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_3_17glClearEj', mask)

  @overload(int)
  def glDrawBuffer(self, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glDrawBuffer(GLenum mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glDrawBuffer

    Parameters
    ----------

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_3_1::glDrawBuffer(GLenum mode)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_112glDrawBufferEj', mode,
    )

  @overload(int, int, int)
  def glTexParameteri(self, target: int, pname: int, param: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glTexParameteri(GLenum target,
    GLenum pname, GLint param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glTexParameteri

    Parameters
    ----------

    target : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    param : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_3_1::glTexParameteri(GLenum target, GLenum
    #      pname, GLint param)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_115glTexParameteriEjji',
        target, pname, param,
    )

  @overload(int, int, float)
  def glTexParameterf(self, target: int, pname: int, param: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glTexParameterf(GLenum target,
    GLenum pname, GLfloat param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glTexParameterf

    Parameters
    ----------

    target : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    param : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_3_1::glTexParameterf(GLenum target, GLenum
    #      pname, GLfloat param)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_115glTexParameterfEjjf',
        target, pname, param,
    )

  @overload(int, int, int, int)
  def glScissor(self, x: int, y: int, width: int, height: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glScissor(GLint x, GLint y,
    GLsizei width, GLsizei height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glScissor

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
    #  void QOpenGLFunctions_3_1::glScissor(GLint x, GLint y, GLsizei width,
    #      GLsizei height)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_19glScissorEiiii',
        x, y, width, height,
    )

  @overload(int, int)
  def glPolygonMode(self, face: int, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glPolygonMode(GLenum face, GLenum
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glPolygonMode

    Parameters
    ----------

    face : int
      Passed on as it is.

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_3_1::glPolygonMode(GLenum face, GLenum mode)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_113glPolygonModeEjj', face, mode,
    )

  @overload(float)
  def glPointSize(self, size: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glPointSize(GLfloat size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glPointSize

    Parameters
    ----------

    size : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_3_1::glPointSize(GLfloat size)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_111glPointSizeEf', size,
    )

  @overload(float)
  def glLineWidth(self, width: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glLineWidth(GLfloat width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glLineWidth

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_3_1::glLineWidth(GLfloat width)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_111glLineWidthEf', width,
    )

  @overload(int, int)
  def glHint(self, target: int, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glHint(GLenum target, GLenum
    mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glHint

    Parameters
    ----------

    target : int
      Passed on as it is.

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_3_1::glHint(GLenum target, GLenum mode)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_16glHintEjj', target, mode,
    )

  @overload(int)
  def glFrontFace(self, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glFrontFace(GLenum mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glFrontFace

    Parameters
    ----------

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_3_1::glFrontFace(GLenum mode)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_111glFrontFaceEj', mode,
    )

  @overload(int)
  def glCullFace(self, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glCullFace(GLenum mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glCullFace

    Parameters
    ----------

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_3_1::glCullFace(GLenum mode)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_3_110glCullFaceEj', mode)

  @overload(int)
  def glIsTexture(self, texture: int) -> int:
    """
    Calls Qt's 'GLboolean QOpenGLFunctions_3_1::glIsTexture(GLuint texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glIsTexture

    Parameters
    ----------

    texture : int
      Passed on as it is.
    """
    #  GLboolean QOpenGLFunctions_3_1::glIsTexture(GLuint texture)
    return self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_111glIsTextureEj', texture,
    )

  @overload(int, int)
  def glBindTexture(self, target: int, texture: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glBindTexture(GLenum target,
    GLuint texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glBindTexture

    Parameters
    ----------

    target : int
      Passed on as it is.

    texture : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_3_1::glBindTexture(GLenum target, GLuint
    #      texture)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_113glBindTextureEjj', target, texture,
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
    Calls Qt's 'void QOpenGLFunctions_3_1::glCopyTexSubImage2D(GLenum target,
    GLint level, GLint xoffset, GLint yoffset, GLint x, GLint y, GLsizei
    width, GLsizei height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glCopyTexSubImage2D

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
    #  void QOpenGLFunctions_3_1::glCopyTexSubImage2D(GLenum target, GLint
    #      level, GLint xoffset, GLint yoffset, GLint x, GLint y, GLsizei
    #      width, GLsizei height)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_119glCopyTexSubImage2DEjiiiiiii',
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
    Calls Qt's 'void QOpenGLFunctions_3_1::glCopyTexSubImage1D(GLenum target,
    GLint level, GLint xoffset, GLint x, GLint y, GLsizei width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glCopyTexSubImage1D

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
    #  void QOpenGLFunctions_3_1::glCopyTexSubImage1D(GLenum target, GLint
    #      level, GLint xoffset, GLint x, GLint y, GLsizei width)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_119glCopyTexSubImage1DEjiiiii',
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
    Calls Qt's 'void QOpenGLFunctions_3_1::glCopyTexImage2D(GLenum target,
    GLint level, GLenum internalformat, GLint x, GLint y, GLsizei width,
    GLsizei height, GLint border)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glCopyTexImage2D

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
    #  void QOpenGLFunctions_3_1::glCopyTexImage2D(GLenum target, GLint
    #      level, GLenum internalformat, GLint x, GLint y, GLsizei width,
    #      GLsizei height, GLint border)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_116glCopyTexImage2DEjijiiiii',
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
    Calls Qt's 'void QOpenGLFunctions_3_1::glCopyTexImage1D(GLenum target,
    GLint level, GLenum internalformat, GLint x, GLint y, GLsizei width,
    GLint border)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glCopyTexImage1D

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
    #  void QOpenGLFunctions_3_1::glCopyTexImage1D(GLenum target, GLint
    #      level, GLenum internalformat, GLint x, GLint y, GLsizei width,
    #      GLint border)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_116glCopyTexImage1DEjijiiii',
        target, level, internalformat, x, y, width, border,
    )

  @overload(float, float)
  def glPolygonOffset(self, factor: float, units: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glPolygonOffset(GLfloat factor,
    GLfloat units)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glPolygonOffset

    Parameters
    ----------

    factor : float
      Passed on as it is.

    units : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_3_1::glPolygonOffset(GLfloat factor, GLfloat
    #      units)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_115glPolygonOffsetEff', factor, units,
    )

  @overload(int, int, int)
  def glDrawArrays(self, mode: int, first: int, count: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glDrawArrays(GLenum mode, GLint
    first, GLsizei count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glDrawArrays

    Parameters
    ----------

    mode : int
      Passed on as it is.

    first : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_3_1::glDrawArrays(GLenum mode, GLint first,
    #      GLsizei count)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_112glDrawArraysEjii',
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
    Calls Qt's 'void QOpenGLFunctions_3_1::glCopyTexSubImage3D(GLenum target,
    GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLint x, GLint
    y, GLsizei width, GLsizei height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glCopyTexSubImage3D

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
    #  void QOpenGLFunctions_3_1::glCopyTexSubImage3D(GLenum target, GLint
    #      level, GLint xoffset, GLint yoffset, GLint zoffset, GLint x, GLint
    #      y, GLsizei width, GLsizei height)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_119glCopyTexSubImage3DEjiiiiiiii',
        target, level, xoffset, yoffset, zoffset, x, y, width, height,
    )

  @overload(int)
  def glBlendEquation(self, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glBlendEquation(GLenum mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glBlendEquation

    Parameters
    ----------

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_3_1::glBlendEquation(GLenum mode)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_115glBlendEquationEj', mode,
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
    Calls Qt's 'void QOpenGLFunctions_3_1::glBlendColor(GLfloat red, GLfloat
    green, GLfloat blue, GLfloat alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glBlendColor

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
    #  void QOpenGLFunctions_3_1::glBlendColor(GLfloat red, GLfloat green,
    #      GLfloat blue, GLfloat alpha)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_112glBlendColorEffff',
        red, green, blue, alpha,
    )

  @overload(float, int)
  def glSampleCoverage(self, value: float, invert: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glSampleCoverage(GLfloat value,
    GLboolean invert)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glSampleCoverage

    Parameters
    ----------

    value : float
      Passed on as it is.

    invert : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_3_1::glSampleCoverage(GLfloat value, GLboolean
    #      invert)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_116glSampleCoverageEfh',
        value, invert,
    )

  @overload(int)
  def glActiveTexture(self, texture: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glActiveTexture(GLenum texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glActiveTexture

    Parameters
    ----------

    texture : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_3_1::glActiveTexture(GLenum texture)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_115glActiveTextureEj', texture,
    )

  @overload(int, int)
  def glPointParameteri(self, pname: int, param: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glPointParameteri(GLenum pname,
    GLint param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glPointParameteri

    Parameters
    ----------

    pname : int
      Passed on as it is.

    param : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_3_1::glPointParameteri(GLenum pname, GLint
    #      param)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_117glPointParameteriEji',
        pname, param,
    )

  @overload(int, float)
  def glPointParameterf(self, pname: int, param: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glPointParameterf(GLenum pname,
    GLfloat param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glPointParameterf

    Parameters
    ----------

    pname : int
      Passed on as it is.

    param : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_3_1::glPointParameterf(GLenum pname, GLfloat
    #      param)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_117glPointParameterfEjf',
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
    Calls Qt's 'void QOpenGLFunctions_3_1::glBlendFuncSeparate(GLenum
    sfactorRGB, GLenum dfactorRGB, GLenum sfactorAlpha, GLenum
    dfactorAlpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glBlendFuncSeparate

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
    #  void QOpenGLFunctions_3_1::glBlendFuncSeparate(GLenum sfactorRGB,
    #      GLenum dfactorRGB, GLenum sfactorAlpha, GLenum dfactorAlpha)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_119glBlendFuncSeparateEjjjj',
        sfactorRGB, dfactorRGB, sfactorAlpha, dfactorAlpha,
    )

  @overload(int)
  def glUnmapBuffer(self, target: int) -> int:
    """
    Calls Qt's 'GLboolean QOpenGLFunctions_3_1::glUnmapBuffer(GLenum
    target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glUnmapBuffer

    Parameters
    ----------

    target : int
      Passed on as it is.
    """
    #  GLboolean QOpenGLFunctions_3_1::glUnmapBuffer(GLenum target)
    return self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_113glUnmapBufferEj', target,
    )

  @overload(int)
  def glIsBuffer(self, buffer: int) -> int:
    """
    Calls Qt's 'GLboolean QOpenGLFunctions_3_1::glIsBuffer(GLuint buffer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glIsBuffer

    Parameters
    ----------

    buffer : int
      Passed on as it is.
    """
    #  GLboolean QOpenGLFunctions_3_1::glIsBuffer(GLuint buffer)
    return self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_110glIsBufferEj', buffer,
    )

  @overload(int, int)
  def glBindBuffer(self, target: int, buffer: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glBindBuffer(GLenum target, GLuint
    buffer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glBindBuffer

    Parameters
    ----------

    target : int
      Passed on as it is.

    buffer : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_3_1::glBindBuffer(GLenum target, GLuint buffer)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_112glBindBufferEjj', target, buffer,
    )

  @overload(int)
  def glEndQuery(self, target: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glEndQuery(GLenum target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glEndQuery

    Parameters
    ----------

    target : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_3_1::glEndQuery(GLenum target)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_110glEndQueryEj', target,
    )

  @overload(int, int)
  def glBeginQuery(self, target: int, id: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glBeginQuery(GLenum target, GLuint
    id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glBeginQuery

    Parameters
    ----------

    target : int
      Passed on as it is.

    id : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_3_1::glBeginQuery(GLenum target, GLuint id)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_112glBeginQueryEjj', target, id,
    )

  @overload(int)
  def glIsQuery(self, id: int) -> int:
    """
    Calls Qt's 'GLboolean QOpenGLFunctions_3_1::glIsQuery(GLuint id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glIsQuery

    Parameters
    ----------

    id : int
      Passed on as it is.
    """
    #  GLboolean QOpenGLFunctions_3_1::glIsQuery(GLuint id)
    return self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_19glIsQueryEj', id,
    )

  @overload(int)
  def glValidateProgram(self, program: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glValidateProgram(GLuint
    program)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glValidateProgram

    Parameters
    ----------

    program : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_3_1::glValidateProgram(GLuint program)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_117glValidateProgramEj', program,
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
    Calls Qt's 'void QOpenGLFunctions_3_1::glUniform4i(GLint location, GLint
    v0, GLint v1, GLint v2, GLint v3)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glUniform4i

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
    #  void QOpenGLFunctions_3_1::glUniform4i(GLint location, GLint v0, GLint
    #      v1, GLint v2, GLint v3)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_111glUniform4iEiiiii',
        location, v0, v1, v2, v3,
    )

  @overload(int, int, int, int)
  def glUniform3i(self, location: int, v0: int, v1: int, v2: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glUniform3i(GLint location, GLint
    v0, GLint v1, GLint v2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glUniform3i

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
    #  void QOpenGLFunctions_3_1::glUniform3i(GLint location, GLint v0, GLint
    #      v1, GLint v2)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_111glUniform3iEiiii',
        location, v0, v1, v2,
    )

  @overload(int, int, int)
  def glUniform2i(self, location: int, v0: int, v1: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glUniform2i(GLint location, GLint
    v0, GLint v1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glUniform2i

    Parameters
    ----------

    location : int
      Passed on as it is.

    v0 : int
      Passed on as it is.

    v1 : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_3_1::glUniform2i(GLint location, GLint v0, GLint
    #      v1)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_111glUniform2iEiii', location, v0, v1,
    )

  @overload(int, int)
  def glUniform1i(self, location: int, v0: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glUniform1i(GLint location, GLint
    v0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glUniform1i

    Parameters
    ----------

    location : int
      Passed on as it is.

    v0 : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_3_1::glUniform1i(GLint location, GLint v0)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_111glUniform1iEii', location, v0,
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
    Calls Qt's 'void QOpenGLFunctions_3_1::glUniform4f(GLint location,
    GLfloat v0, GLfloat v1, GLfloat v2, GLfloat v3)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glUniform4f

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
    #  void QOpenGLFunctions_3_1::glUniform4f(GLint location, GLfloat v0,
    #      GLfloat v1, GLfloat v2, GLfloat v3)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_111glUniform4fEiffff',
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
    Calls Qt's 'void QOpenGLFunctions_3_1::glUniform3f(GLint location,
    GLfloat v0, GLfloat v1, GLfloat v2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glUniform3f

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
    #  void QOpenGLFunctions_3_1::glUniform3f(GLint location, GLfloat v0,
    #      GLfloat v1, GLfloat v2)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_111glUniform3fEifff',
        location, v0, v1, v2,
    )

  @overload(int, float, float)
  def glUniform2f(self, location: int, v0: float, v1: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glUniform2f(GLint location,
    GLfloat v0, GLfloat v1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glUniform2f

    Parameters
    ----------

    location : int
      Passed on as it is.

    v0 : float
      Passed on as it is.

    v1 : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_3_1::glUniform2f(GLint location, GLfloat v0,
    #      GLfloat v1)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_111glUniform2fEiff', location, v0, v1,
    )

  @overload(int, float)
  def glUniform1f(self, location: int, v0: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glUniform1f(GLint location,
    GLfloat v0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glUniform1f

    Parameters
    ----------

    location : int
      Passed on as it is.

    v0 : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_3_1::glUniform1f(GLint location, GLfloat v0)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_111glUniform1fEif', location, v0,
    )

  @overload(int)
  def glUseProgram(self, program: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glUseProgram(GLuint program)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glUseProgram

    Parameters
    ----------

    program : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_3_1::glUseProgram(GLuint program)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_112glUseProgramEj', program,
    )

  @overload(int)
  def glLinkProgram(self, program: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glLinkProgram(GLuint program)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glLinkProgram

    Parameters
    ----------

    program : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_3_1::glLinkProgram(GLuint program)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_113glLinkProgramEj', program,
    )

  @overload(int)
  def glIsShader(self, shader: int) -> int:
    """
    Calls Qt's 'GLboolean QOpenGLFunctions_3_1::glIsShader(GLuint shader)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glIsShader

    Parameters
    ----------

    shader : int
      Passed on as it is.
    """
    #  GLboolean QOpenGLFunctions_3_1::glIsShader(GLuint shader)
    return self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_110glIsShaderEj', shader,
    )

  @overload(int)
  def glIsProgram(self, program: int) -> int:
    """
    Calls Qt's 'GLboolean QOpenGLFunctions_3_1::glIsProgram(GLuint program)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glIsProgram

    Parameters
    ----------

    program : int
      Passed on as it is.
    """
    #  GLboolean QOpenGLFunctions_3_1::glIsProgram(GLuint program)
    return self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_111glIsProgramEj', program,
    )

  @overload(int)
  def glEnableVertexAttribArray(self, index: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glEnableVertexAttribArray(GLuint
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_3_1::glEnableVertexAttribArray(GLuint index)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_125glEnableVertexAttribArrayEj',
        index,
    )

  @overload(int)
  def glDisableVertexAttribArray(self, index: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glDisableVertexAttribArray(GLuint
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_3_1::glDisableVertexAttribArray(GLuint index)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_126glDisableVertexAttribArrayEj',
        index,
    )

  @overload(int, int)
  def glDetachShader(self, program: int, shader: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glDetachShader(GLuint program,
    GLuint shader)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glDetachShader

    Parameters
    ----------

    program : int
      Passed on as it is.

    shader : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_3_1::glDetachShader(GLuint program, GLuint
    #      shader)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_114glDetachShaderEjj',
        program, shader,
    )

  @overload(int)
  def glDeleteShader(self, shader: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glDeleteShader(GLuint shader)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glDeleteShader

    Parameters
    ----------

    shader : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_3_1::glDeleteShader(GLuint shader)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_114glDeleteShaderEj', shader,
    )

  @overload(int)
  def glDeleteProgram(self, program: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glDeleteProgram(GLuint program)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glDeleteProgram

    Parameters
    ----------

    program : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_3_1::glDeleteProgram(GLuint program)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_115glDeleteProgramEj', program,
    )

  @overload(int)
  def glCreateShader(self, type: int) -> int:
    """
    Calls Qt's 'GLuint QOpenGLFunctions_3_1::glCreateShader(GLenum type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glCreateShader

    Parameters
    ----------

    type : int
      Passed on as it is.
    """
    #  GLuint QOpenGLFunctions_3_1::glCreateShader(GLenum type)
    return self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_114glCreateShaderEj', type,
    )

  def glCreateProgram(self) -> int:
    """
    Calls Qt's 'GLuint QOpenGLFunctions_3_1::glCreateProgram()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glCreateProgram
    """
    #  GLuint QOpenGLFunctions_3_1::glCreateProgram()
    return self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_115glCreateProgramEv',
    )

  @overload(int)
  def glCompileShader(self, shader: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glCompileShader(GLuint shader)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glCompileShader

    Parameters
    ----------

    shader : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_3_1::glCompileShader(GLuint shader)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_115glCompileShaderEj', shader,
    )

  @overload(int, int)
  def glAttachShader(self, program: int, shader: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glAttachShader(GLuint program,
    GLuint shader)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glAttachShader

    Parameters
    ----------

    program : int
      Passed on as it is.

    shader : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_3_1::glAttachShader(GLuint program, GLuint
    #      shader)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_114glAttachShaderEjj',
        program, shader,
    )

  @overload(int, int)
  def glStencilMaskSeparate(self, face: int, mask: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glStencilMaskSeparate(GLenum face,
    GLuint mask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glStencilMaskSeparate

    Parameters
    ----------

    face : int
      Passed on as it is.

    mask : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_3_1::glStencilMaskSeparate(GLenum face, GLuint
    #      mask)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_121glStencilMaskSeparateEjj',
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
    Calls Qt's 'void QOpenGLFunctions_3_1::glStencilFuncSeparate(GLenum face,
    GLenum func, GLint ref, GLuint mask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glStencilFuncSeparate

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
    #  void QOpenGLFunctions_3_1::glStencilFuncSeparate(GLenum face, GLenum
    #      func, GLint ref, GLuint mask)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_121glStencilFuncSeparateEjjij',
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
    Calls Qt's 'void QOpenGLFunctions_3_1::glStencilOpSeparate(GLenum face,
    GLenum sfail, GLenum dpfail, GLenum dppass)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glStencilOpSeparate

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
    #  void QOpenGLFunctions_3_1::glStencilOpSeparate(GLenum face, GLenum
    #      sfail, GLenum dpfail, GLenum dppass)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_119glStencilOpSeparateEjjjj',
        face, sfail, dpfail, dppass,
    )

  @overload(int, int)
  def glBlendEquationSeparate(self, modeRGB: int, modeAlpha: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glBlendEquationSeparate(GLenum
    modeRGB, GLenum modeAlpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glBlendEquationSeparate

    Parameters
    ----------

    modeRGB : int
      Passed on as it is.

    modeAlpha : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_3_1::glBlendEquationSeparate(GLenum modeRGB,
    #      GLenum modeAlpha)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_123glBlendEquationSeparateEjj',
        modeRGB, modeAlpha,
    )

  @overload(int)
  def glIsVertexArray(self, array: int) -> int:
    """
    Calls Qt's 'GLboolean QOpenGLFunctions_3_1::glIsVertexArray(GLuint
    array)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glIsVertexArray

    Parameters
    ----------

    array : int
      Passed on as it is.
    """
    #  GLboolean QOpenGLFunctions_3_1::glIsVertexArray(GLuint array)
    return self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_115glIsVertexArrayEj', array,
    )

  @overload(int)
  def glBindVertexArray(self, array: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glBindVertexArray(GLuint array)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glBindVertexArray

    Parameters
    ----------

    array : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_3_1::glBindVertexArray(GLuint array)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_117glBindVertexArrayEj', array,
    )

  @overload(int, int, int)
  def glFlushMappedBufferRange(
      self,
      target: int,
      offset: int,
      length: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glFlushMappedBufferRange(GLenum
    target, GLintptr offset, GLsizeiptr length)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glFlushMappedBufferRange

    Parameters
    ----------

    target : int
      Passed on as it is.

    offset : int
      Passed on as it is.

    length : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_3_1::glFlushMappedBufferRange(GLenum target,
    #      GLintptr offset, GLsizeiptr length)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_124glFlushMappedBufferRangeEjll',
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
    Calls Qt's 'void QOpenGLFunctions_3_1::glFramebufferTextureLayer(GLenum
    target, GLenum attachment, GLuint texture, GLint level, GLint layer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html

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
    #  void QOpenGLFunctions_3_1::glFramebufferTextureLayer(GLenum target,
    #      GLenum attachment, GLuint texture, GLint level, GLint layer)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_125glFramebufferTextureLayerEjjjii',
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
    QOpenGLFunctions_3_1::glRenderbufferStorageMultisample(GLenum target,
    GLsizei samples, GLenum internalformat, GLsizei width, GLsizei height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html

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
    #  void QOpenGLFunctions_3_1::glRenderbufferStorageMultisample(GLenum
    #      target, GLsizei samples, GLenum internalformat, GLsizei width,
    #      GLsizei height)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_132glRenderbufferStorageMultisampleE'
        'jijii',
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
    Calls Qt's 'void QOpenGLFunctions_3_1::glBlitFramebuffer(GLint srcX0,
    GLint srcY0, GLint srcX1, GLint srcY1, GLint dstX0, GLint dstY0, GLint
    dstX1, GLint dstY1, GLbitfield mask, GLenum filter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glBlitFramebuffer

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
    #  void QOpenGLFunctions_3_1::glBlitFramebuffer(GLint srcX0, GLint srcY0,
    #      GLint srcX1, GLint srcY1, GLint dstX0, GLint dstY0, GLint dstX1,
    #      GLint dstY1, GLbitfield mask, GLenum filter)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_117glBlitFramebufferEiiiiiiiijj',
        srcX0, srcY0, srcX1, srcY1, dstX0, dstY0, dstX1, dstY1, mask, filter,
    )

  @overload(int)
  def glGenerateMipmap(self, target: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glGenerateMipmap(GLenum target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glGenerateMipmap

    Parameters
    ----------

    target : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_3_1::glGenerateMipmap(GLenum target)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_116glGenerateMipmapEj', target,
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
    Calls Qt's 'void QOpenGLFunctions_3_1::glFramebufferRenderbuffer(GLenum
    target, GLenum attachment, GLenum renderbuffertarget, GLuint
    renderbuffer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html

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
    #  void QOpenGLFunctions_3_1::glFramebufferRenderbuffer(GLenum target,
    #      GLenum attachment, GLenum renderbuffertarget, GLuint renderbuffer)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_125glFramebufferRenderbufferEjjjj',
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
    Calls Qt's 'void QOpenGLFunctions_3_1::glFramebufferTexture3D(GLenum
    target, GLenum attachment, GLenum textarget, GLuint texture, GLint level,
    GLint zoffset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glFramebufferTexture3D

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
    #  void QOpenGLFunctions_3_1::glFramebufferTexture3D(GLenum target,
    #      GLenum attachment, GLenum textarget, GLuint texture, GLint level,
    #      GLint zoffset)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_122glFramebufferTexture3DEjjjjii',
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
    Calls Qt's 'void QOpenGLFunctions_3_1::glFramebufferTexture2D(GLenum
    target, GLenum attachment, GLenum textarget, GLuint texture, GLint
    level)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glFramebufferTexture2D

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
    #  void QOpenGLFunctions_3_1::glFramebufferTexture2D(GLenum target,
    #      GLenum attachment, GLenum textarget, GLuint texture, GLint level)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_122glFramebufferTexture2DEjjjji',
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
    Calls Qt's 'void QOpenGLFunctions_3_1::glFramebufferTexture1D(GLenum
    target, GLenum attachment, GLenum textarget, GLuint texture, GLint
    level)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glFramebufferTexture1D

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
    #  void QOpenGLFunctions_3_1::glFramebufferTexture1D(GLenum target,
    #      GLenum attachment, GLenum textarget, GLuint texture, GLint level)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_122glFramebufferTexture1DEjjjji',
        target, attachment, textarget, texture, level,
    )

  @overload(int)
  def glCheckFramebufferStatus(self, target: int) -> int:
    """
    Calls Qt's 'GLenum QOpenGLFunctions_3_1::glCheckFramebufferStatus(GLenum
    target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glCheckFramebufferStatus

    Parameters
    ----------

    target : int
      Passed on as it is.
    """
    #  GLenum QOpenGLFunctions_3_1::glCheckFramebufferStatus(GLenum target)
    return self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_124glCheckFramebufferStatusEj',
        target,
    )

  @overload(int, int)
  def glBindFramebuffer(self, target: int, framebuffer: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glBindFramebuffer(GLenum target,
    GLuint framebuffer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glBindFramebuffer

    Parameters
    ----------

    target : int
      Passed on as it is.

    framebuffer : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_3_1::glBindFramebuffer(GLenum target, GLuint
    #      framebuffer)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_117glBindFramebufferEjj',
        target, framebuffer,
    )

  @overload(int)
  def glIsFramebuffer(self, framebuffer: int) -> int:
    """
    Calls Qt's 'GLboolean QOpenGLFunctions_3_1::glIsFramebuffer(GLuint
    framebuffer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glIsFramebuffer

    Parameters
    ----------

    framebuffer : int
      Passed on as it is.
    """
    #  GLboolean QOpenGLFunctions_3_1::glIsFramebuffer(GLuint framebuffer)
    return self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_115glIsFramebufferEj', framebuffer,
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
    Calls Qt's 'void QOpenGLFunctions_3_1::glRenderbufferStorage(GLenum
    target, GLenum internalformat, GLsizei width, GLsizei height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glRenderbufferStorage

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
    #  void QOpenGLFunctions_3_1::glRenderbufferStorage(GLenum target, GLenum
    #      internalformat, GLsizei width, GLsizei height)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_121glRenderbufferStorageEjjii',
        target, internalformat, width, height,
    )

  @overload(int, int)
  def glBindRenderbuffer(self, target: int, renderbuffer: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glBindRenderbuffer(GLenum target,
    GLuint renderbuffer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glBindRenderbuffer

    Parameters
    ----------

    target : int
      Passed on as it is.

    renderbuffer : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_3_1::glBindRenderbuffer(GLenum target, GLuint
    #      renderbuffer)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_118glBindRenderbufferEjj',
        target, renderbuffer,
    )

  @overload(int)
  def glIsRenderbuffer(self, renderbuffer: int) -> int:
    """
    Calls Qt's 'GLboolean QOpenGLFunctions_3_1::glIsRenderbuffer(GLuint
    renderbuffer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glIsRenderbuffer

    Parameters
    ----------

    renderbuffer : int
      Passed on as it is.
    """
    #  GLboolean QOpenGLFunctions_3_1::glIsRenderbuffer(GLuint renderbuffer)
    return self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_116glIsRenderbufferEj', renderbuffer,
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
    Calls Qt's 'void QOpenGLFunctions_3_1::glClearBufferfi(GLenum buffer,
    GLint drawbuffer, GLfloat depth, GLint stencil)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glClearBufferfi

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
    #  void QOpenGLFunctions_3_1::glClearBufferfi(GLenum buffer, GLint
    #      drawbuffer, GLfloat depth, GLint stencil)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_115glClearBufferfiEjifi',
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
    Calls Qt's 'void QOpenGLFunctions_3_1::glUniform4ui(GLint location,
    GLuint v0, GLuint v1, GLuint v2, GLuint v3)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glUniform4ui

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
    #  void QOpenGLFunctions_3_1::glUniform4ui(GLint location, GLuint v0,
    #      GLuint v1, GLuint v2, GLuint v3)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_112glUniform4uiEijjjj',
        location, v0, v1, v2, v3,
    )

  @overload(int, int, int, int)
  def glUniform3ui(self, location: int, v0: int, v1: int, v2: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glUniform3ui(GLint location,
    GLuint v0, GLuint v1, GLuint v2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glUniform3ui

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
    #  void QOpenGLFunctions_3_1::glUniform3ui(GLint location, GLuint v0,
    #      GLuint v1, GLuint v2)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_112glUniform3uiEijjj',
        location, v0, v1, v2,
    )

  @overload(int, int, int)
  def glUniform2ui(self, location: int, v0: int, v1: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glUniform2ui(GLint location,
    GLuint v0, GLuint v1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glUniform2ui

    Parameters
    ----------

    location : int
      Passed on as it is.

    v0 : int
      Passed on as it is.

    v1 : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_3_1::glUniform2ui(GLint location, GLuint v0,
    #      GLuint v1)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_112glUniform2uiEijj',
        location, v0, v1,
    )

  @overload(int, int)
  def glUniform1ui(self, location: int, v0: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glUniform1ui(GLint location,
    GLuint v0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glUniform1ui

    Parameters
    ----------

    location : int
      Passed on as it is.

    v0 : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_3_1::glUniform1ui(GLint location, GLuint v0)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_112glUniform1uiEij', location, v0,
    )

  def glEndConditionalRender(self) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glEndConditionalRender()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glEndConditionalRender
    """
    #  void QOpenGLFunctions_3_1::glEndConditionalRender()
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_122glEndConditionalRenderEv',
    )

  @overload(int, int)
  def glBeginConditionalRender(self, id: int, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glBeginConditionalRender(GLuint
    id, GLenum mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glBeginConditionalRender

    Parameters
    ----------

    id : int
      Passed on as it is.

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_3_1::glBeginConditionalRender(GLuint id, GLenum
    #      mode)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_124glBeginConditionalRenderEjj',
        id, mode,
    )

  @overload(int, int)
  def glClampColor(self, target: int, clamp: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glClampColor(GLenum target, GLenum
    clamp)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glClampColor

    Parameters
    ----------

    target : int
      Passed on as it is.

    clamp : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_3_1::glClampColor(GLenum target, GLenum clamp)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_112glClampColorEjj', target, clamp,
    )

  @overload(int, int, int)
  def glBindBufferBase(self, target: int, index: int, buffer: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glBindBufferBase(GLenum target,
    GLuint index, GLuint buffer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glBindBufferBase

    Parameters
    ----------

    target : int
      Passed on as it is.

    index : int
      Passed on as it is.

    buffer : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_3_1::glBindBufferBase(GLenum target, GLuint
    #      index, GLuint buffer)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_116glBindBufferBaseEjjj',
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
    Calls Qt's 'void QOpenGLFunctions_3_1::glBindBufferRange(GLenum target,
    GLuint index, GLuint buffer, GLintptr offset, GLsizeiptr size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glBindBufferRange

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
    #  void QOpenGLFunctions_3_1::glBindBufferRange(GLenum target, GLuint
    #      index, GLuint buffer, GLintptr offset, GLsizeiptr size)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_117glBindBufferRangeEjjjll',
        target, index, buffer, offset, size,
    )

  def glEndTransformFeedback(self) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glEndTransformFeedback()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glEndTransformFeedback
    """
    #  void QOpenGLFunctions_3_1::glEndTransformFeedback()
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_122glEndTransformFeedbackEv',
    )

  @overload(int)
  def glBeginTransformFeedback(self, primitiveMode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glBeginTransformFeedback(GLenum
    primitiveMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glBeginTransformFeedback

    Parameters
    ----------

    primitiveMode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_3_1::glBeginTransformFeedback(GLenum
    #      primitiveMode)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_124glBeginTransformFeedbackEj',
        primitiveMode,
    )

  @overload(int, int)
  def glIsEnabledi(self, target: int, index: int) -> int:
    """
    Calls Qt's 'GLboolean QOpenGLFunctions_3_1::glIsEnabledi(GLenum target,
    GLuint index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glIsEnabledi

    Parameters
    ----------

    target : int
      Passed on as it is.

    index : int
      Passed on as it is.
    """
    #  GLboolean QOpenGLFunctions_3_1::glIsEnabledi(GLenum target, GLuint
    #      index)
    return self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_112glIsEnablediEjj', target, index,
    )

  @overload(int, int)
  def glDisablei(self, target: int, index: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glDisablei(GLenum target, GLuint
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glDisablei

    Parameters
    ----------

    target : int
      Passed on as it is.

    index : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_3_1::glDisablei(GLenum target, GLuint index)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_110glDisableiEjj', target, index,
    )

  @overload(int, int)
  def glEnablei(self, target: int, index: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glEnablei(GLenum target, GLuint
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glEnablei

    Parameters
    ----------

    target : int
      Passed on as it is.

    index : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_3_1::glEnablei(GLenum target, GLuint index)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_19glEnableiEjj', target, index,
    )

  @overload(int, int, int, int, int)
  def glColorMaski(self, index: int, r: int, g: int, b: int, a: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glColorMaski(GLuint index,
    GLboolean r, GLboolean g, GLboolean b, GLboolean a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glColorMaski

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
    #  void QOpenGLFunctions_3_1::glColorMaski(GLuint index, GLboolean r,
    #      GLboolean g, GLboolean b, GLboolean a)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_112glColorMaskiEjhhhh',
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
    Calls Qt's 'void QOpenGLFunctions_3_1::glCopyBufferSubData(GLenum
    readTarget, GLenum writeTarget, GLintptr readOffset, GLintptr
    writeOffset, GLsizeiptr size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glCopyBufferSubData

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
    #  void QOpenGLFunctions_3_1::glCopyBufferSubData(GLenum readTarget,
    #      GLenum writeTarget, GLintptr readOffset, GLintptr writeOffset,
    #      GLsizeiptr size)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_119glCopyBufferSubDataEjjlll',
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
    Calls Qt's 'void QOpenGLFunctions_3_1::glUniformBlockBinding(GLuint
    program, GLuint uniformBlockIndex, GLuint uniformBlockBinding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glUniformBlockBinding

    Parameters
    ----------

    program : int
      Passed on as it is.

    uniformBlockIndex : int
      Passed on as it is.

    uniformBlockBinding : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_3_1::glUniformBlockBinding(GLuint program,
    #      GLuint uniformBlockIndex, GLuint uniformBlockBinding)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_121glUniformBlockBindingEjjj',
        program, uniformBlockIndex, uniformBlockBinding,
    )

  @overload(int)
  def glPrimitiveRestartIndex(self, index: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glPrimitiveRestartIndex(GLuint
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glPrimitiveRestartIndex

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_3_1::glPrimitiveRestartIndex(GLuint index)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_123glPrimitiveRestartIndexEj', index,
    )

  @overload(int, int, int)
  def glTexBuffer(
      self,
      target: int,
      internalformat: int,
      buffer: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_3_1::glTexBuffer(GLenum target, GLenum
    internalformat, GLuint buffer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glTexBuffer

    Parameters
    ----------

    target : int
      Passed on as it is.

    internalformat : int
      Passed on as it is.

    buffer : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_3_1::glTexBuffer(GLenum target, GLenum
    #      internalformat, GLuint buffer)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_111glTexBufferEjjj',
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
    Calls Qt's 'void QOpenGLFunctions_3_1::glDrawArraysInstanced(GLenum mode,
    GLint first, GLsizei count, GLsizei instancecount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_3_1.html#glDrawArraysInstanced

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
    #  void QOpenGLFunctions_3_1::glDrawArraysInstanced(GLenum mode, GLint
    #      first, GLsizei count, GLsizei instancecount)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_3_121glDrawArraysInstancedEjiii',
        mode, first, count, instancecount,
    )

  @staticmethod
  def glBindAttribLocation(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glBindAttribLocation(GLuint program,
    GLuint index, const GLchar *name)': names 'GLchar', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glBindAttribLocation' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_3_1::glBindAttribLocation(GLuint "
        "program, GLuint index, const GLchar *name)': names 'GLchar', which "
        "has no cute class yet.")

  @staticmethod
  def glBindFragDataLocation(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glBindFragDataLocation(GLuint program,
    GLuint color, const GLchar *name)': names 'GLchar', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glBindFragDataLocation' has no cute function "
        "yet. Qt's 'void "
        "QOpenGLFunctions_3_1::glBindFragDataLocation(GLuint program, "
        "GLuint color, const GLchar *name)': names 'GLchar', which has no "
        "cute class yet.")

  @staticmethod
  def glBufferData(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glBufferData(GLenum target, GLsizeiptr
    size, const GLvoid *data, GLenum usage)': names 'GLvoid', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glBufferData' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_3_1::glBufferData(GLenum target, GLsizeiptr "
        "size, const GLvoid *data, GLenum usage)': names 'GLvoid', which "
        "has no cute class yet.")

  @staticmethod
  def glBufferSubData(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glBufferSubData(GLenum target, GLintptr
    offset, GLsizeiptr size, const GLvoid *data)': names 'GLvoid', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glBufferSubData' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_3_1::glBufferSubData(GLenum target, "
        "GLintptr offset, GLsizeiptr size, const GLvoid *data)': names "
        "'GLvoid', which has no cute class yet.")

  @staticmethod
  def glClearBufferfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glClearBufferfv(GLenum buffer, GLint
    drawbuffer, const GLfloat *value)': names 'GLfloat', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glClearBufferfv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_3_1::glClearBufferfv(GLenum buffer, "
        "GLint drawbuffer, const GLfloat *value)': names 'GLfloat', which "
        "has no cute class yet.")

  @staticmethod
  def glClearBufferiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glClearBufferiv(GLenum buffer, GLint
    drawbuffer, const GLint *value)': names 'GLint', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glClearBufferiv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_3_1::glClearBufferiv(GLenum buffer, "
        "GLint drawbuffer, const GLint *value)': names 'GLint', which has "
        "no cute class yet.")

  @staticmethod
  def glClearBufferuiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glClearBufferuiv(GLenum buffer, GLint
    drawbuffer, const GLuint *value)': names 'GLuint', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glClearBufferuiv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_3_1::glClearBufferuiv(GLenum buffer, "
        "GLint drawbuffer, const GLuint *value)': names 'GLuint', which has "
        "no cute class yet.")

  @staticmethod
  def glCompressedTexImage1D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glCompressedTexImage1D(GLenum target,
    GLint level, GLenum internalformat, GLsizei width, GLint border, GLsizei
    imageSize, const GLvoid *data)': names 'GLvoid', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glCompressedTexImage1D' has no cute function "
        "yet. Qt's 'void "
        "QOpenGLFunctions_3_1::glCompressedTexImage1D(GLenum target, GLint "
        "level, GLenum internalformat, GLsizei width, GLint border, GLsizei "
        "imageSize, const GLvoid *data)': names 'GLvoid', which has no cute "
        "class yet.")

  @staticmethod
  def glCompressedTexImage2D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glCompressedTexImage2D(GLenum target,
    GLint level, GLenum internalformat, GLsizei width, GLsizei height, GLint
    border, GLsizei imageSize, const GLvoid *data)': names 'GLvoid', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glCompressedTexImage2D' has no cute function "
        "yet. Qt's 'void "
        "QOpenGLFunctions_3_1::glCompressedTexImage2D(GLenum target, GLint "
        "level, GLenum internalformat, GLsizei width, GLsizei height, GLint "
        "border, GLsizei imageSize, const GLvoid *data)': names 'GLvoid', "
        "which has no cute class yet.")

  @staticmethod
  def glCompressedTexImage3D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glCompressedTexImage3D(GLenum target,
    GLint level, GLenum internalformat, GLsizei width, GLsizei height,
    GLsizei depth, GLint border, GLsizei imageSize, const GLvoid *data)':
    names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glCompressedTexImage3D' has no cute function "
        "yet. Qt's 'void "
        "QOpenGLFunctions_3_1::glCompressedTexImage3D(GLenum target, GLint "
        "level, GLenum internalformat, GLsizei width, GLsizei height, "
        "GLsizei depth, GLint border, GLsizei imageSize, const GLvoid "
        "*data)': names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glCompressedTexSubImage1D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glCompressedTexSubImage1D(GLenum target,
    GLint level, GLint xoffset, GLsizei width, GLenum format, GLsizei
    imageSize, const GLvoid *data)': names 'GLvoid', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glCompressedTexSubImage1D' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_3_1::glCompressedTexSubImage1D(GLenum target, "
        "GLint level, GLint xoffset, GLsizei width, GLenum format, GLsizei "
        "imageSize, const GLvoid *data)': names 'GLvoid', which has no cute "
        "class yet.")

  @staticmethod
  def glCompressedTexSubImage2D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glCompressedTexSubImage2D(GLenum target,
    GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height,
    GLenum format, GLsizei imageSize, const GLvoid *data)': names 'GLvoid',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glCompressedTexSubImage2D' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_3_1::glCompressedTexSubImage2D(GLenum target, "
        "GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei "
        "height, GLenum format, GLsizei imageSize, const GLvoid *data)': "
        "names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glCompressedTexSubImage3D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glCompressedTexSubImage3D(GLenum target,
    GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width,
    GLsizei height, GLsizei depth, GLenum format, GLsizei imageSize, const
    GLvoid *data)': names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glCompressedTexSubImage3D' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_3_1::glCompressedTexSubImage3D(GLenum target, "
        "GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei "
        "width, GLsizei height, GLsizei depth, GLenum format, GLsizei "
        "imageSize, const GLvoid *data)': names 'GLvoid', which has no cute "
        "class yet.")

  @staticmethod
  def glDeleteBuffers(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glDeleteBuffers(GLsizei n, const GLuint
    *buffers)': names 'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glDeleteBuffers' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_3_1::glDeleteBuffers(GLsizei n, const "
        "GLuint *buffers)': names 'GLuint', which has no cute class yet.")

  @staticmethod
  def glDeleteFramebuffers(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glDeleteFramebuffers(GLsizei n, const
    GLuint *framebuffers)': names 'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glDeleteFramebuffers' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_3_1::glDeleteFramebuffers(GLsizei "
        "n, const GLuint *framebuffers)': names 'GLuint', which has no cute "
        "class yet.")

  @staticmethod
  def glDeleteQueries(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glDeleteQueries(GLsizei n, const GLuint
    *ids)': names 'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glDeleteQueries' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_3_1::glDeleteQueries(GLsizei n, const "
        "GLuint *ids)': names 'GLuint', which has no cute class yet.")

  @staticmethod
  def glDeleteRenderbuffers(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glDeleteRenderbuffers(GLsizei n, const
    GLuint *renderbuffers)': names 'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glDeleteRenderbuffers' has no cute function "
        "yet. Qt's 'void "
        "QOpenGLFunctions_3_1::glDeleteRenderbuffers(GLsizei n, const "
        "GLuint *renderbuffers)': names 'GLuint', which has no cute class "
        "yet.")

  @staticmethod
  def glDeleteTextures(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glDeleteTextures(GLsizei n, const GLuint
    *textures)': names 'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glDeleteTextures' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_3_1::glDeleteTextures(GLsizei n, const "
        "GLuint *textures)': names 'GLuint', which has no cute class yet.")

  @staticmethod
  def glDeleteVertexArrays(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glDeleteVertexArrays(GLsizei n, const
    GLuint *arrays)': names 'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glDeleteVertexArrays' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_3_1::glDeleteVertexArrays(GLsizei "
        "n, const GLuint *arrays)': names 'GLuint', which has no cute class "
        "yet.")

  @staticmethod
  def glDrawBuffers(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glDrawBuffers(GLsizei n, const GLenum
    *bufs)': names 'GLenum', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glDrawBuffers' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_3_1::glDrawBuffers(GLsizei n, const "
        "GLenum *bufs)': names 'GLenum', which has no cute class yet.")

  @staticmethod
  def glDrawElements(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glDrawElements(GLenum mode, GLsizei
    count, GLenum type, const GLvoid *indices)': names 'GLvoid', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glDrawElements' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_3_1::glDrawElements(GLenum mode, "
        "GLsizei count, GLenum type, const GLvoid *indices)': names "
        "'GLvoid', which has no cute class yet.")

  @staticmethod
  def glDrawElementsInstanced(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glDrawElementsInstanced(GLenum mode,
    GLsizei count, GLenum type, const GLvoid *indices, GLsizei
    instancecount)': names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glDrawElementsInstanced' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_3_1::glDrawElementsInstanced(GLenum mode, GLsizei "
        "count, GLenum type, const GLvoid *indices, GLsizei "
        "instancecount)': names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glDrawRangeElements(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glDrawRangeElements(GLenum mode, GLuint
    start, GLuint end, GLsizei count, GLenum type, const GLvoid *indices)':
    names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glDrawRangeElements' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_3_1::glDrawRangeElements(GLenum "
        "mode, GLuint start, GLuint end, GLsizei count, GLenum type, const "
        "GLvoid *indices)': names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glGenBuffers(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glGenBuffers(GLsizei n, GLuint
    *buffers)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glGenBuffers' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_3_1::glGenBuffers(GLsizei n, GLuint "
        "*buffers)': takes a number to change where it is.")

  @staticmethod
  def glGenFramebuffers(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glGenFramebuffers(GLsizei n, GLuint
    *framebuffers)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glGenFramebuffers' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_3_1::glGenFramebuffers(GLsizei n, "
        "GLuint *framebuffers)': takes a number to change where it is.")

  @staticmethod
  def glGenQueries(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glGenQueries(GLsizei n, GLuint *ids)':
    takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glGenQueries' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_3_1::glGenQueries(GLsizei n, GLuint *ids)': "
        "takes a number to change where it is.")

  @staticmethod
  def glGenRenderbuffers(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glGenRenderbuffers(GLsizei n, GLuint
    *renderbuffers)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glGenRenderbuffers' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_3_1::glGenRenderbuffers(GLsizei "
        "n, GLuint *renderbuffers)': takes a number to change where it is.")

  @staticmethod
  def glGenTextures(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glGenTextures(GLsizei n, GLuint
    *textures)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glGenTextures' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_3_1::glGenTextures(GLsizei n, GLuint "
        "*textures)': takes a number to change where it is.")

  @staticmethod
  def glGenVertexArrays(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glGenVertexArrays(GLsizei n, GLuint
    *arrays)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glGenVertexArrays' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_3_1::glGenVertexArrays(GLsizei n, "
        "GLuint *arrays)': takes a number to change where it is.")

  @staticmethod
  def glGetActiveAttrib(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glGetActiveAttrib(GLuint program, GLuint
    index, GLsizei bufSize, GLsizei *length, GLint *size, GLenum *type,
    GLchar *name)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glGetActiveAttrib' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_3_1::glGetActiveAttrib(GLuint program, "
        "GLuint index, GLsizei bufSize, GLsizei *length, GLint *size, "
        "GLenum *type, GLchar *name)': takes a number to change where it is."
    )

  @staticmethod
  def glGetActiveUniform(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glGetActiveUniform(GLuint program,
    GLuint index, GLsizei bufSize, GLsizei *length, GLint *size, GLenum
    *type, GLchar *name)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glGetActiveUniform' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_3_1::glGetActiveUniform(GLuint "
        "program, GLuint index, GLsizei bufSize, GLsizei *length, GLint "
        "*size, GLenum *type, GLchar *name)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetActiveUniformBlockName(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glGetActiveUniformBlockName(GLuint
    program, GLuint uniformBlockIndex, GLsizei bufSize, GLsizei *length,
    GLchar *uniformBlockName)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glGetActiveUniformBlockName' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_3_1::glGetActiveUniformBlockName(GLuint program, "
        "GLuint uniformBlockIndex, GLsizei bufSize, GLsizei *length, GLchar "
        "*uniformBlockName)': takes a number to change where it is.")

  @staticmethod
  def glGetActiveUniformBlockiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glGetActiveUniformBlockiv(GLuint
    program, GLuint uniformBlockIndex, GLenum pname, GLint *params)': takes a
    number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glGetActiveUniformBlockiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_3_1::glGetActiveUniformBlockiv(GLuint program, "
        "GLuint uniformBlockIndex, GLenum pname, GLint *params)': takes a "
        "number to change where it is.")

  @staticmethod
  def glGetActiveUniformName(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glGetActiveUniformName(GLuint program,
    GLuint uniformIndex, GLsizei bufSize, GLsizei *length, GLchar
    *uniformName)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glGetActiveUniformName' has no cute function "
        "yet. Qt's 'void "
        "QOpenGLFunctions_3_1::glGetActiveUniformName(GLuint program, "
        "GLuint uniformIndex, GLsizei bufSize, GLsizei *length, GLchar "
        "*uniformName)': takes a number to change where it is.")

  @staticmethod
  def glGetActiveUniformsiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glGetActiveUniformsiv(GLuint program,
    GLsizei uniformCount, const GLuint *uniformIndices, GLenum pname, GLint
    *params)': names 'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glGetActiveUniformsiv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_3_1::glGetActiveUniformsiv(GLuint "
        "program, GLsizei uniformCount, const GLuint *uniformIndices, "
        "GLenum pname, GLint *params)': names 'GLuint', which has no cute "
        "class yet.")

  @staticmethod
  def glGetAttachedShaders(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glGetAttachedShaders(GLuint program,
    GLsizei maxCount, GLsizei *count, GLuint *obj)': takes a number to change
    where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glGetAttachedShaders' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_3_1::glGetAttachedShaders(GLuint "
        "program, GLsizei maxCount, GLsizei *count, GLuint *obj)': takes a "
        "number to change where it is.")

  @staticmethod
  def glGetAttribLocation(*__, **_) -> Never:
    """
    Qt's 'GLint QOpenGLFunctions_3_1::glGetAttribLocation(GLuint program,
    const GLchar *name)': names 'GLchar', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glGetAttribLocation' has no cute function "
        "yet. Qt's 'GLint QOpenGLFunctions_3_1::glGetAttribLocation(GLuint "
        "program, const GLchar *name)': names 'GLchar', which has no cute "
        "class yet.")

  @staticmethod
  def glGetBooleani_v(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glGetBooleani_v(GLenum target, GLuint
    index, GLboolean *data)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glGetBooleani_v' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_3_1::glGetBooleani_v(GLenum target, "
        "GLuint index, GLboolean *data)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetBooleanv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glGetBooleanv(GLenum pname, GLboolean
    *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glGetBooleanv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_3_1::glGetBooleanv(GLenum pname, "
        "GLboolean *params)': takes a number to change where it is.")

  @staticmethod
  def glGetBufferParameteriv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glGetBufferParameteriv(GLenum target,
    GLenum pname, GLint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glGetBufferParameteriv' has no cute function "
        "yet. Qt's 'void "
        "QOpenGLFunctions_3_1::glGetBufferParameteriv(GLenum target, GLenum "
        "pname, GLint *params)': takes a number to change where it is.")

  @staticmethod
  def glGetBufferPointerv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glGetBufferPointerv(GLenum target,
    GLenum pname, GLvoid **params)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glGetBufferPointerv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_3_1::glGetBufferPointerv(GLenum "
        "target, GLenum pname, GLvoid **params)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def glGetBufferSubData(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glGetBufferSubData(GLenum target,
    GLintptr offset, GLsizeiptr size, GLvoid *data)': names 'GLvoid', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glGetBufferSubData' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_3_1::glGetBufferSubData(GLenum "
        "target, GLintptr offset, GLsizeiptr size, GLvoid *data)': names "
        "'GLvoid', which has no cute class yet.")

  @staticmethod
  def glGetCompressedTexImage(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glGetCompressedTexImage(GLenum target,
    GLint level, GLvoid *img)': names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glGetCompressedTexImage' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_3_1::glGetCompressedTexImage(GLenum target, GLint "
        "level, GLvoid *img)': names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glGetDoublev(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glGetDoublev(GLenum pname, GLdouble
    *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glGetDoublev' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_3_1::glGetDoublev(GLenum pname, GLdouble "
        "*params)': takes a number to change where it is.")

  @staticmethod
  def glGetFloatv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glGetFloatv(GLenum pname, GLfloat
    *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glGetFloatv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_3_1::glGetFloatv(GLenum pname, GLfloat "
        "*params)': takes a number to change where it is.")

  @staticmethod
  def glGetFragDataLocation(*__, **_) -> Never:
    """
    Qt's 'GLint QOpenGLFunctions_3_1::glGetFragDataLocation(GLuint program,
    const GLchar *name)': names 'GLchar', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glGetFragDataLocation' has no cute function "
        "yet. Qt's 'GLint "
        "QOpenGLFunctions_3_1::glGetFragDataLocation(GLuint program, const "
        "GLchar *name)': names 'GLchar', which has no cute class yet.")

  @staticmethod
  def glGetFramebufferAttachmentParameteriv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_3_1::glGetFramebufferAttachmentParameteriv(GLenum
    target, GLenum attachment, GLenum pname, GLint *params)': takes a number
    to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glGetFramebufferAttachmentParameteriv' has "
        "no cute function yet. Qt's 'void "
        "QOpenGLFunctions_3_1::glGetFramebufferAttachmentParameteriv(GLenum "
        "target, GLenum attachment, GLenum pname, GLint *params)': takes a "
        "number to change where it is.")

  @staticmethod
  def glGetIntegeri_v(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glGetIntegeri_v(GLenum target, GLuint
    index, GLint *data)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glGetIntegeri_v' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_3_1::glGetIntegeri_v(GLenum target, "
        "GLuint index, GLint *data)': takes a number to change where it is.")

  @staticmethod
  def glGetIntegerv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glGetIntegerv(GLenum pname, GLint
    *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glGetIntegerv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_3_1::glGetIntegerv(GLenum pname, GLint "
        "*params)': takes a number to change where it is.")

  @staticmethod
  def glGetProgramInfoLog(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glGetProgramInfoLog(GLuint program,
    GLsizei bufSize, GLsizei *length, GLchar *infoLog)': takes a number to
    change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glGetProgramInfoLog' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_3_1::glGetProgramInfoLog(GLuint "
        "program, GLsizei bufSize, GLsizei *length, GLchar *infoLog)': "
        "takes a number to change where it is.")

  @staticmethod
  def glGetProgramiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glGetProgramiv(GLuint program, GLenum
    pname, GLint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glGetProgramiv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_3_1::glGetProgramiv(GLuint program, "
        "GLenum pname, GLint *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetQueryObjectiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glGetQueryObjectiv(GLuint id, GLenum
    pname, GLint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glGetQueryObjectiv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_3_1::glGetQueryObjectiv(GLuint "
        "id, GLenum pname, GLint *params)': takes a number to change where "
        "it is.")

  @staticmethod
  def glGetQueryObjectuiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glGetQueryObjectuiv(GLuint id, GLenum
    pname, GLuint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glGetQueryObjectuiv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_3_1::glGetQueryObjectuiv(GLuint "
        "id, GLenum pname, GLuint *params)': takes a number to change where "
        "it is.")

  @staticmethod
  def glGetQueryiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glGetQueryiv(GLenum target, GLenum
    pname, GLint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glGetQueryiv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_3_1::glGetQueryiv(GLenum target, GLenum "
        "pname, GLint *params)': takes a number to change where it is.")

  @staticmethod
  def glGetRenderbufferParameteriv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glGetRenderbufferParameteriv(GLenum
    target, GLenum pname, GLint *params)': takes a number to change where it
    is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glGetRenderbufferParameteriv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_3_1::glGetRenderbufferParameteriv(GLenum target, "
        "GLenum pname, GLint *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetShaderInfoLog(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glGetShaderInfoLog(GLuint shader,
    GLsizei bufSize, GLsizei *length, GLchar *infoLog)': takes a number to
    change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glGetShaderInfoLog' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_3_1::glGetShaderInfoLog(GLuint "
        "shader, GLsizei bufSize, GLsizei *length, GLchar *infoLog)': takes "
        "a number to change where it is.")

  @staticmethod
  def glGetShaderSource(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glGetShaderSource(GLuint shader, GLsizei
    bufSize, GLsizei *length, GLchar *source)': takes a number to change
    where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glGetShaderSource' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_3_1::glGetShaderSource(GLuint shader, "
        "GLsizei bufSize, GLsizei *length, GLchar *source)': takes a number "
        "to change where it is.")

  @staticmethod
  def glGetShaderiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glGetShaderiv(GLuint shader, GLenum
    pname, GLint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glGetShaderiv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_3_1::glGetShaderiv(GLuint shader, "
        "GLenum pname, GLint *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetString(*__, **_) -> Never:
    """
    Qt's 'const GLubyte *QOpenGLFunctions_3_1::glGetString(GLenum name)':
    gives 'unsigned char', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glGetString' has no cute function yet. Qt's "
        "'const GLubyte *QOpenGLFunctions_3_1::glGetString(GLenum name)': "
        "gives 'unsigned char', which has no cute class yet.")

  @staticmethod
  def glGetStringi(*__, **_) -> Never:
    """
    Qt's 'const GLubyte *QOpenGLFunctions_3_1::glGetStringi(GLenum name,
    GLuint index)': gives 'unsigned char', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glGetStringi' has no cute function yet. Qt's "
        "'const GLubyte *QOpenGLFunctions_3_1::glGetStringi(GLenum name, "
        "GLuint index)': gives 'unsigned char', which has no cute class yet."
    )

  @staticmethod
  def glGetTexImage(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glGetTexImage(GLenum target, GLint
    level, GLenum format, GLenum type, GLvoid *pixels)': names 'GLvoid',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glGetTexImage' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_3_1::glGetTexImage(GLenum target, "
        "GLint level, GLenum format, GLenum type, GLvoid *pixels)': names "
        "'GLvoid', which has no cute class yet.")

  @staticmethod
  def glGetTexLevelParameterfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glGetTexLevelParameterfv(GLenum target,
    GLint level, GLenum pname, GLfloat *params)': takes a number to change
    where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glGetTexLevelParameterfv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_3_1::glGetTexLevelParameterfv(GLenum target, "
        "GLint level, GLenum pname, GLfloat *params)': takes a number to "
        "change where it is.")

  @staticmethod
  def glGetTexLevelParameteriv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glGetTexLevelParameteriv(GLenum target,
    GLint level, GLenum pname, GLint *params)': takes a number to change
    where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glGetTexLevelParameteriv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_3_1::glGetTexLevelParameteriv(GLenum target, "
        "GLint level, GLenum pname, GLint *params)': takes a number to "
        "change where it is.")

  @staticmethod
  def glGetTexParameterIiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glGetTexParameterIiv(GLenum target,
    GLenum pname, GLint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glGetTexParameterIiv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_3_1::glGetTexParameterIiv(GLenum "
        "target, GLenum pname, GLint *params)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetTexParameterIuiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glGetTexParameterIuiv(GLenum target,
    GLenum pname, GLuint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glGetTexParameterIuiv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_3_1::glGetTexParameterIuiv(GLenum "
        "target, GLenum pname, GLuint *params)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetTexParameterfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glGetTexParameterfv(GLenum target,
    GLenum pname, GLfloat *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glGetTexParameterfv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_3_1::glGetTexParameterfv(GLenum "
        "target, GLenum pname, GLfloat *params)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetTexParameteriv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glGetTexParameteriv(GLenum target,
    GLenum pname, GLint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glGetTexParameteriv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_3_1::glGetTexParameteriv(GLenum "
        "target, GLenum pname, GLint *params)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetTransformFeedbackVarying(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glGetTransformFeedbackVarying(GLuint
    program, GLuint index, GLsizei bufSize, GLsizei *length, GLsizei *size,
    GLenum *type, GLchar *name)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glGetTransformFeedbackVarying' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_3_1::glGetTransformFeedbackVarying(GLuint "
        "program, GLuint index, GLsizei bufSize, GLsizei *length, GLsizei "
        "*size, GLenum *type, GLchar *name)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetUniformBlockIndex(*__, **_) -> Never:
    """
    Qt's 'GLuint QOpenGLFunctions_3_1::glGetUniformBlockIndex(GLuint program,
    const GLchar *uniformBlockName)': names 'GLchar', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glGetUniformBlockIndex' has no cute function "
        "yet. Qt's 'GLuint "
        "QOpenGLFunctions_3_1::glGetUniformBlockIndex(GLuint program, const "
        "GLchar *uniformBlockName)': names 'GLchar', which has no cute "
        "class yet.")

  @staticmethod
  def glGetUniformIndices(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glGetUniformIndices(GLuint program,
    GLsizei uniformCount, const GLchar *const *uniformNames, GLuint
    *uniformIndices)': names 'GLchar *const', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glGetUniformIndices' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_3_1::glGetUniformIndices(GLuint "
        "program, GLsizei uniformCount, const GLchar *const *uniformNames, "
        "GLuint *uniformIndices)': names 'GLchar *const', which has no cute "
        "class yet.")

  @staticmethod
  def glGetUniformLocation(*__, **_) -> Never:
    """
    Qt's 'GLint QOpenGLFunctions_3_1::glGetUniformLocation(GLuint program,
    const GLchar *name)': names 'GLchar', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glGetUniformLocation' has no cute function "
        "yet. Qt's 'GLint QOpenGLFunctions_3_1::glGetUniformLocation(GLuint "
        "program, const GLchar *name)': names 'GLchar', which has no cute "
        "class yet.")

  @staticmethod
  def glGetUniformfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glGetUniformfv(GLuint program, GLint
    location, GLfloat *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glGetUniformfv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_3_1::glGetUniformfv(GLuint program, "
        "GLint location, GLfloat *params)': takes a number to change where "
        "it is.")

  @staticmethod
  def glGetUniformiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glGetUniformiv(GLuint program, GLint
    location, GLint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glGetUniformiv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_3_1::glGetUniformiv(GLuint program, "
        "GLint location, GLint *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetUniformuiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glGetUniformuiv(GLuint program, GLint
    location, GLuint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glGetUniformuiv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_3_1::glGetUniformuiv(GLuint program, "
        "GLint location, GLuint *params)': takes a number to change where "
        "it is.")

  @staticmethod
  def glGetVertexAttribIiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glGetVertexAttribIiv(GLuint index,
    GLenum pname, GLint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glGetVertexAttribIiv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_3_1::glGetVertexAttribIiv(GLuint "
        "index, GLenum pname, GLint *params)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetVertexAttribIuiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glGetVertexAttribIuiv(GLuint index,
    GLenum pname, GLuint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glGetVertexAttribIuiv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_3_1::glGetVertexAttribIuiv(GLuint "
        "index, GLenum pname, GLuint *params)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetVertexAttribPointerv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glGetVertexAttribPointerv(GLuint index,
    GLenum pname, GLvoid **pointer)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glGetVertexAttribPointerv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_3_1::glGetVertexAttribPointerv(GLuint index, "
        "GLenum pname, GLvoid **pointer)': takes a type Python has no way "
        "to hand over yet.")

  @staticmethod
  def glGetVertexAttribdv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glGetVertexAttribdv(GLuint index, GLenum
    pname, GLdouble *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glGetVertexAttribdv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_3_1::glGetVertexAttribdv(GLuint "
        "index, GLenum pname, GLdouble *params)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetVertexAttribfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glGetVertexAttribfv(GLuint index, GLenum
    pname, GLfloat *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glGetVertexAttribfv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_3_1::glGetVertexAttribfv(GLuint "
        "index, GLenum pname, GLfloat *params)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetVertexAttribiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glGetVertexAttribiv(GLuint index, GLenum
    pname, GLint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glGetVertexAttribiv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_3_1::glGetVertexAttribiv(GLuint "
        "index, GLenum pname, GLint *params)': takes a number to change "
        "where it is.")

  @staticmethod
  def glMapBuffer(*__, **_) -> Never:
    """
    Qt's 'GLvoid *QOpenGLFunctions_3_1::glMapBuffer(GLenum target, GLenum
    access)': gives 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glMapBuffer' has no cute function yet. Qt's "
        "'GLvoid *QOpenGLFunctions_3_1::glMapBuffer(GLenum target, GLenum "
        "access)': gives 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glMapBufferRange(*__, **_) -> Never:
    """
    Qt's 'GLvoid *QOpenGLFunctions_3_1::glMapBufferRange(GLenum target,
    GLintptr offset, GLsizeiptr length, GLbitfield access)': gives 'GLvoid',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glMapBufferRange' has no cute function yet. "
        "Qt's 'GLvoid *QOpenGLFunctions_3_1::glMapBufferRange(GLenum "
        "target, GLintptr offset, GLsizeiptr length, GLbitfield access)': "
        "gives 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glMultiDrawArrays(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glMultiDrawArrays(GLenum mode, const
    GLint *first, const GLsizei *count, GLsizei drawcount)': names 'GLint',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glMultiDrawArrays' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_3_1::glMultiDrawArrays(GLenum mode, "
        "const GLint *first, const GLsizei *count, GLsizei drawcount)': "
        "names 'GLint', which has no cute class yet.")

  @staticmethod
  def glMultiDrawElements(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glMultiDrawElements(GLenum mode, const
    GLsizei *count, GLenum type, const GLvoid *const *indices, GLsizei
    drawcount)': names 'GLsizei', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glMultiDrawElements' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_3_1::glMultiDrawElements(GLenum "
        "mode, const GLsizei *count, GLenum type, const GLvoid *const "
        "*indices, GLsizei drawcount)': names 'GLsizei', which has no cute "
        "class yet.")

  @staticmethod
  def glPointParameterfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glPointParameterfv(GLenum pname, const
    GLfloat *params)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glPointParameterfv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_3_1::glPointParameterfv(GLenum "
        "pname, const GLfloat *params)': names 'GLfloat', which has no cute "
        "class yet.")

  @staticmethod
  def glPointParameteriv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glPointParameteriv(GLenum pname, const
    GLint *params)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glPointParameteriv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_3_1::glPointParameteriv(GLenum "
        "pname, const GLint *params)': names 'GLint', which has no cute "
        "class yet.")

  @staticmethod
  def glReadPixels(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glReadPixels(GLint x, GLint y, GLsizei
    width, GLsizei height, GLenum format, GLenum type, GLvoid *pixels)':
    names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glReadPixels' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_3_1::glReadPixels(GLint x, GLint y, GLsizei "
        "width, GLsizei height, GLenum format, GLenum type, GLvoid "
        "*pixels)': names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glShaderSource(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glShaderSource(GLuint shader, GLsizei
    count, const GLchar *const *string, const GLint *length)': names 'GLchar
    *const', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glShaderSource' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_3_1::glShaderSource(GLuint shader, "
        "GLsizei count, const GLchar *const *string, const GLint *length)': "
        "names 'GLchar *const', which has no cute class yet.")

  @staticmethod
  def glTexImage1D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glTexImage1D(GLenum target, GLint level,
    GLint internalformat, GLsizei width, GLint border, GLenum format, GLenum
    type, const GLvoid *pixels)': names 'GLvoid', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glTexImage1D' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_3_1::glTexImage1D(GLenum target, GLint "
        "level, GLint internalformat, GLsizei width, GLint border, GLenum "
        "format, GLenum type, const GLvoid *pixels)': names 'GLvoid', which "
        "has no cute class yet.")

  @staticmethod
  def glTexImage2D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glTexImage2D(GLenum target, GLint level,
    GLint internalformat, GLsizei width, GLsizei height, GLint border, GLenum
    format, GLenum type, const GLvoid *pixels)': names 'GLvoid', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glTexImage2D' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_3_1::glTexImage2D(GLenum target, GLint "
        "level, GLint internalformat, GLsizei width, GLsizei height, GLint "
        "border, GLenum format, GLenum type, const GLvoid *pixels)': names "
        "'GLvoid', which has no cute class yet.")

  @staticmethod
  def glTexImage3D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glTexImage3D(GLenum target, GLint level,
    GLint internalformat, GLsizei width, GLsizei height, GLsizei depth, GLint
    border, GLenum format, GLenum type, const GLvoid *pixels)': names
    'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glTexImage3D' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_3_1::glTexImage3D(GLenum target, GLint "
        "level, GLint internalformat, GLsizei width, GLsizei height, "
        "GLsizei depth, GLint border, GLenum format, GLenum type, const "
        "GLvoid *pixels)': names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glTexParameterIiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glTexParameterIiv(GLenum target, GLenum
    pname, const GLint *params)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glTexParameterIiv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_3_1::glTexParameterIiv(GLenum target, "
        "GLenum pname, const GLint *params)': names 'GLint', which has no "
        "cute class yet.")

  @staticmethod
  def glTexParameterIuiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glTexParameterIuiv(GLenum target, GLenum
    pname, const GLuint *params)': names 'GLuint', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glTexParameterIuiv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_3_1::glTexParameterIuiv(GLenum "
        "target, GLenum pname, const GLuint *params)': names 'GLuint', "
        "which has no cute class yet.")

  @staticmethod
  def glTexParameterfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glTexParameterfv(GLenum target, GLenum
    pname, const GLfloat *params)': names 'GLfloat', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glTexParameterfv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_3_1::glTexParameterfv(GLenum target, "
        "GLenum pname, const GLfloat *params)': names 'GLfloat', which has "
        "no cute class yet.")

  @staticmethod
  def glTexParameteriv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glTexParameteriv(GLenum target, GLenum
    pname, const GLint *params)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glTexParameteriv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_3_1::glTexParameteriv(GLenum target, "
        "GLenum pname, const GLint *params)': names 'GLint', which has no "
        "cute class yet.")

  @staticmethod
  def glTexSubImage1D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glTexSubImage1D(GLenum target, GLint
    level, GLint xoffset, GLsizei width, GLenum format, GLenum type, const
    GLvoid *pixels)': names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glTexSubImage1D' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_3_1::glTexSubImage1D(GLenum target, "
        "GLint level, GLint xoffset, GLsizei width, GLenum format, GLenum "
        "type, const GLvoid *pixels)': names 'GLvoid', which has no cute "
        "class yet.")

  @staticmethod
  def glTexSubImage2D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glTexSubImage2D(GLenum target, GLint
    level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height,
    GLenum format, GLenum type, const GLvoid *pixels)': names 'GLvoid', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glTexSubImage2D' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_3_1::glTexSubImage2D(GLenum target, "
        "GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei "
        "height, GLenum format, GLenum type, const GLvoid *pixels)': names "
        "'GLvoid', which has no cute class yet.")

  @staticmethod
  def glTexSubImage3D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glTexSubImage3D(GLenum target, GLint
    level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width,
    GLsizei height, GLsizei depth, GLenum format, GLenum type, const GLvoid
    *pixels)': names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glTexSubImage3D' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_3_1::glTexSubImage3D(GLenum target, "
        "GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei "
        "width, GLsizei height, GLsizei depth, GLenum format, GLenum type, "
        "const GLvoid *pixels)': names 'GLvoid', which has no cute class "
        "yet.")

  @staticmethod
  def glTransformFeedbackVaryings(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glTransformFeedbackVaryings(GLuint
    program, GLsizei count, const GLchar *const *varyings, GLenum
    bufferMode)': names 'GLchar *const', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glTransformFeedbackVaryings' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_3_1::glTransformFeedbackVaryings(GLuint program, "
        "GLsizei count, const GLchar *const *varyings, GLenum bufferMode)': "
        "names 'GLchar *const', which has no cute class yet.")

  @staticmethod
  def glUniform1fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glUniform1fv(GLint location, GLsizei
    count, const GLfloat *value)': names 'GLfloat', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glUniform1fv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_3_1::glUniform1fv(GLint location, GLsizei "
        "count, const GLfloat *value)': names 'GLfloat', which has no cute "
        "class yet.")

  @staticmethod
  def glUniform1iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glUniform1iv(GLint location, GLsizei
    count, const GLint *value)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glUniform1iv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_3_1::glUniform1iv(GLint location, GLsizei "
        "count, const GLint *value)': names 'GLint', which has no cute "
        "class yet.")

  @staticmethod
  def glUniform1uiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glUniform1uiv(GLint location, GLsizei
    count, const GLuint *value)': names 'GLuint', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glUniform1uiv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_3_1::glUniform1uiv(GLint location, "
        "GLsizei count, const GLuint *value)': names 'GLuint', which has no "
        "cute class yet.")

  @staticmethod
  def glUniform2fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glUniform2fv(GLint location, GLsizei
    count, const GLfloat *value)': names 'GLfloat', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glUniform2fv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_3_1::glUniform2fv(GLint location, GLsizei "
        "count, const GLfloat *value)': names 'GLfloat', which has no cute "
        "class yet.")

  @staticmethod
  def glUniform2iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glUniform2iv(GLint location, GLsizei
    count, const GLint *value)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glUniform2iv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_3_1::glUniform2iv(GLint location, GLsizei "
        "count, const GLint *value)': names 'GLint', which has no cute "
        "class yet.")

  @staticmethod
  def glUniform2uiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glUniform2uiv(GLint location, GLsizei
    count, const GLuint *value)': names 'GLuint', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glUniform2uiv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_3_1::glUniform2uiv(GLint location, "
        "GLsizei count, const GLuint *value)': names 'GLuint', which has no "
        "cute class yet.")

  @staticmethod
  def glUniform3fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glUniform3fv(GLint location, GLsizei
    count, const GLfloat *value)': names 'GLfloat', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glUniform3fv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_3_1::glUniform3fv(GLint location, GLsizei "
        "count, const GLfloat *value)': names 'GLfloat', which has no cute "
        "class yet.")

  @staticmethod
  def glUniform3iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glUniform3iv(GLint location, GLsizei
    count, const GLint *value)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glUniform3iv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_3_1::glUniform3iv(GLint location, GLsizei "
        "count, const GLint *value)': names 'GLint', which has no cute "
        "class yet.")

  @staticmethod
  def glUniform3uiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glUniform3uiv(GLint location, GLsizei
    count, const GLuint *value)': names 'GLuint', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glUniform3uiv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_3_1::glUniform3uiv(GLint location, "
        "GLsizei count, const GLuint *value)': names 'GLuint', which has no "
        "cute class yet.")

  @staticmethod
  def glUniform4fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glUniform4fv(GLint location, GLsizei
    count, const GLfloat *value)': names 'GLfloat', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glUniform4fv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_3_1::glUniform4fv(GLint location, GLsizei "
        "count, const GLfloat *value)': names 'GLfloat', which has no cute "
        "class yet.")

  @staticmethod
  def glUniform4iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glUniform4iv(GLint location, GLsizei
    count, const GLint *value)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glUniform4iv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_3_1::glUniform4iv(GLint location, GLsizei "
        "count, const GLint *value)': names 'GLint', which has no cute "
        "class yet.")

  @staticmethod
  def glUniform4uiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glUniform4uiv(GLint location, GLsizei
    count, const GLuint *value)': names 'GLuint', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glUniform4uiv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_3_1::glUniform4uiv(GLint location, "
        "GLsizei count, const GLuint *value)': names 'GLuint', which has no "
        "cute class yet.")

  @staticmethod
  def glUniformMatrix2fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glUniformMatrix2fv(GLint location,
    GLsizei count, GLboolean transpose, const GLfloat *value)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glUniformMatrix2fv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_3_1::glUniformMatrix2fv(GLint "
        "location, GLsizei count, GLboolean transpose, const GLfloat "
        "*value)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glUniformMatrix2x3fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glUniformMatrix2x3fv(GLint location,
    GLsizei count, GLboolean transpose, const GLfloat *value)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glUniformMatrix2x3fv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_3_1::glUniformMatrix2x3fv(GLint "
        "location, GLsizei count, GLboolean transpose, const GLfloat "
        "*value)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glUniformMatrix2x4fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glUniformMatrix2x4fv(GLint location,
    GLsizei count, GLboolean transpose, const GLfloat *value)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glUniformMatrix2x4fv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_3_1::glUniformMatrix2x4fv(GLint "
        "location, GLsizei count, GLboolean transpose, const GLfloat "
        "*value)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glUniformMatrix3fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glUniformMatrix3fv(GLint location,
    GLsizei count, GLboolean transpose, const GLfloat *value)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glUniformMatrix3fv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_3_1::glUniformMatrix3fv(GLint "
        "location, GLsizei count, GLboolean transpose, const GLfloat "
        "*value)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glUniformMatrix3x2fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glUniformMatrix3x2fv(GLint location,
    GLsizei count, GLboolean transpose, const GLfloat *value)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glUniformMatrix3x2fv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_3_1::glUniformMatrix3x2fv(GLint "
        "location, GLsizei count, GLboolean transpose, const GLfloat "
        "*value)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glUniformMatrix3x4fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glUniformMatrix3x4fv(GLint location,
    GLsizei count, GLboolean transpose, const GLfloat *value)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glUniformMatrix3x4fv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_3_1::glUniformMatrix3x4fv(GLint "
        "location, GLsizei count, GLboolean transpose, const GLfloat "
        "*value)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glUniformMatrix4fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glUniformMatrix4fv(GLint location,
    GLsizei count, GLboolean transpose, const GLfloat *value)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glUniformMatrix4fv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_3_1::glUniformMatrix4fv(GLint "
        "location, GLsizei count, GLboolean transpose, const GLfloat "
        "*value)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glUniformMatrix4x2fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glUniformMatrix4x2fv(GLint location,
    GLsizei count, GLboolean transpose, const GLfloat *value)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glUniformMatrix4x2fv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_3_1::glUniformMatrix4x2fv(GLint "
        "location, GLsizei count, GLboolean transpose, const GLfloat "
        "*value)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glUniformMatrix4x3fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glUniformMatrix4x3fv(GLint location,
    GLsizei count, GLboolean transpose, const GLfloat *value)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glUniformMatrix4x3fv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_3_1::glUniformMatrix4x3fv(GLint "
        "location, GLsizei count, GLboolean transpose, const GLfloat "
        "*value)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glVertexAttribIPointer(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glVertexAttribIPointer(GLuint index,
    GLint size, GLenum type, GLsizei stride, const GLvoid *pointer)': names
    'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glVertexAttribIPointer' has no cute function "
        "yet. Qt's 'void "
        "QOpenGLFunctions_3_1::glVertexAttribIPointer(GLuint index, GLint "
        "size, GLenum type, GLsizei stride, const GLvoid *pointer)': names "
        "'GLvoid', which has no cute class yet.")

  @staticmethod
  def glVertexAttribPointer(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_3_1::glVertexAttribPointer(GLuint index,
    GLint size, GLenum type, GLboolean normalized, GLsizei stride, const
    GLvoid *pointer)': names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_3_1.glVertexAttribPointer' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_3_1::glVertexAttribPointer(GLuint "
        "index, GLint size, GLenum type, GLboolean normalized, GLsizei "
        "stride, const GLvoid *pointer)': names 'GLvoid', which has no cute "
        "class yet.")
