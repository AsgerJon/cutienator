"""
QOpenGLFunctions_4_5_Core binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpenGL/qopenglfunctions_4_5_core.h, Qt 6.12.0. Changes made here are
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


class QOpenGLFunctions_4_5_Core(QAbstractOpenGLFunctions):
  """
  The cute side of Qt's QOpenGLFunctions_4_5_Core: a plain Python object
  standing in front of one C++ QOpenGLFunctions_4_5_Core.

  It is built on the cute 'QAbstractOpenGLFunctions', as Qt's
  QOpenGLFunctions_4_5_Core is built on Qt's QAbstractOpenGLFunctions, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QOpenGLFunctions_4_5_Core that has a ritual and that
  Python can call so far, 279 names in all: 'initializeOpenGLFunctions',
  'glViewport', 'glDepthRange', 'glIsEnabled', 'glGetError', 'glReadBuffer',
  'glPixelStorei', 'glPixelStoref', 'glDepthFunc', 'glStencilOp',
  'glStencilFunc', 'glLogicOp', 'glBlendFunc', 'glFlush', 'glFinish',
  'glEnable', 'glDisable', 'glDepthMask', 'glColorMask', 'glStencilMask',
  'glClearDepth', 'glClearStencil', 'glClearColor', 'glClear',
  'glDrawBuffer', 'glTexParameteri', 'glTexParameterf', 'glScissor',
  'glPolygonMode', 'glPointSize', 'glLineWidth', 'glHint', 'glFrontFace',
  'glCullFace', 'glIsTexture', 'glBindTexture', 'glCopyTexSubImage2D',
  'glCopyTexSubImage1D', 'glCopyTexImage2D', 'glCopyTexImage1D',
  'glPolygonOffset', 'glDrawArrays', 'glBlendColor', 'glBlendEquation',
  'glCopyTexSubImage3D', 'glSampleCoverage', 'glActiveTexture',
  'glPointParameteri', 'glPointParameterf', 'glBlendFuncSeparate',
  'glUnmapBuffer', 'glIsBuffer', 'glBindBuffer', 'glEndQuery',
  'glBeginQuery', 'glIsQuery', 'glVertexAttrib4s', 'glVertexAttrib4f',
  'glVertexAttrib4d', 'glVertexAttrib4Nub', 'glVertexAttrib3s',
  'glVertexAttrib3f', 'glVertexAttrib3d', 'glVertexAttrib2s',
  'glVertexAttrib2f', 'glVertexAttrib2d', 'glVertexAttrib1s',
  'glVertexAttrib1f', 'glVertexAttrib1d', 'glValidateProgram', 'glUniform4i',
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
  'glUniform2ui', 'glUniform1ui', 'glVertexAttribI4ui', 'glVertexAttribI3ui',
  'glVertexAttribI2ui', 'glVertexAttribI1ui', 'glVertexAttribI4i',
  'glVertexAttribI3i', 'glVertexAttribI2i', 'glVertexAttribI1i',
  'glEndConditionalRender', 'glBeginConditionalRender', 'glClampColor',
  'glBindBufferBase', 'glBindBufferRange', 'glEndTransformFeedback',
  'glBeginTransformFeedback', 'glIsEnabledi', 'glDisablei', 'glEnablei',
  'glColorMaski', 'glUniformBlockBinding', 'glCopyBufferSubData',
  'glPrimitiveRestartIndex', 'glTexBuffer', 'glDrawArraysInstanced',
  'glSampleMaski', 'glTexImage3DMultisample', 'glTexImage2DMultisample',
  'glFramebufferTexture', 'glProvokingVertex', 'glVertexAttribP4ui',
  'glVertexAttribP3ui', 'glVertexAttribP2ui', 'glVertexAttribP1ui',
  'glVertexAttribDivisor', 'glQueryCounter', 'glSamplerParameterf',
  'glSamplerParameteri', 'glBindSampler', 'glIsSampler', 'glEndQueryIndexed',
  'glBeginQueryIndexed', 'glDrawTransformFeedbackStream',
  'glDrawTransformFeedback', 'glResumeTransformFeedback',
  'glPauseTransformFeedback', 'glIsTransformFeedback',
  'glBindTransformFeedback', 'glPatchParameteri', 'glUniform4d',
  'glUniform3d', 'glUniform2d', 'glUniform1d', 'glBlendFuncSeparatei',
  'glBlendFunci', 'glBlendEquationSeparatei', 'glBlendEquationi',
  'glMinSampleShading', 'glDepthRangeIndexed', 'glScissorIndexed',
  'glViewportIndexedf', 'glVertexAttribL4d', 'glVertexAttribL3d',
  'glVertexAttribL2d', 'glVertexAttribL1d', 'glValidateProgramPipeline',
  'glProgramUniform4ui', 'glProgramUniform4d', 'glProgramUniform4f',
  'glProgramUniform4i', 'glProgramUniform3ui', 'glProgramUniform3d',
  'glProgramUniform3f', 'glProgramUniform3i', 'glProgramUniform2ui',
  'glProgramUniform2d', 'glProgramUniform2f', 'glProgramUniform2i',
  'glProgramUniform1ui', 'glProgramUniform1d', 'glProgramUniform1f',
  'glProgramUniform1i', 'glIsProgramPipeline', 'glBindProgramPipeline',
  'glActiveShaderProgram', 'glUseProgramStages', 'glProgramParameteri',
  'glClearDepthf', 'glDepthRangef', 'glReleaseShaderCompiler',
  'glDrawTransformFeedbackStreamInstanced',
  'glDrawTransformFeedbackInstanced', 'glTexStorage3D', 'glTexStorage2D',
  'glTexStorage1D', 'glMemoryBarrier', 'glBindImageTexture',
  'glDrawArraysInstancedBaseInstance', 'glPopDebugGroup',
  'glVertexBindingDivisor', 'glVertexAttribBinding', 'glVertexAttribLFormat',
  'glVertexAttribIFormat', 'glVertexAttribFormat', 'glBindVertexBuffer',
  'glTextureView', 'glTexStorage3DMultisample', 'glTexStorage2DMultisample',
  'glTexBufferRange', 'glShaderStorageBlockBinding',
  'glInvalidateBufferData', 'glInvalidateBufferSubData',
  'glInvalidateTexImage', 'glInvalidateTexSubImage',
  'glFramebufferParameteri', 'glCopyImageSubData',
  'glDispatchComputeIndirect', 'glDispatchCompute', 'glTextureBarrier',
  'glGetGraphicsResetStatus', 'glMemoryBarrierByRegion',
  'glVertexArrayBindingDivisor', 'glVertexArrayAttribLFormat',
  'glVertexArrayAttribIFormat', 'glVertexArrayAttribFormat',
  'glVertexArrayAttribBinding', 'glVertexArrayVertexBuffer',
  'glVertexArrayElementBuffer', 'glEnableVertexArrayAttrib',
  'glDisableVertexArrayAttrib', 'glBindTextureUnit',
  'glGenerateTextureMipmap', 'glTextureParameteri', 'glTextureParameterf',
  'glCopyTextureSubImage3D', 'glCopyTextureSubImage2D',
  'glCopyTextureSubImage1D', 'glTextureStorage3DMultisample',
  'glTextureStorage2DMultisample', 'glTextureStorage3D',
  'glTextureStorage2D', 'glTextureStorage1D', 'glTextureBufferRange',
  'glTextureBuffer', 'glNamedRenderbufferStorageMultisample',
  'glNamedRenderbufferStorage', 'glCheckNamedFramebufferStatus',
  'glBlitNamedFramebuffer', 'glClearNamedFramebufferfi',
  'glNamedFramebufferReadBuffer', 'glNamedFramebufferDrawBuffer',
  'glNamedFramebufferTextureLayer', 'glNamedFramebufferTexture',
  'glNamedFramebufferParameteri', 'glNamedFramebufferRenderbuffer',
  'glFlushMappedNamedBufferRange', 'glUnmapNamedBuffer',
  'glCopyNamedBufferSubData', 'glTransformFeedbackBufferRange',
  'glTransformFeedbackBufferBase', 'glClipControl', 'isContextCompatible',
  'versionProfile'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpenGLFunctions_4_5_Core::~QOpenGLFunctions_4_5_Core()': the
    destructor: Python never removes a C++ QOpenGLFunctions_4_5_Core.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetTexLevelParameteriv(GLenum
    target, GLint level, GLenum pname, GLint *params)': takes a number to
    change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetTexLevelParameterfv(GLenum
    target, GLint level, GLenum pname, GLfloat *params)': takes a number to
    change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetTexParameteriv(GLenum target,
    GLenum pname, GLint *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetTexParameterfv(GLenum target,
    GLenum pname, GLfloat *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetTexImage(GLenum target, GLint
    level, GLenum format, GLenum type, void *pixels)': names 'void', which
    has no cute class yet.
  - Qt's 'const GLubyte *QOpenGLFunctions_4_5_Core::glGetString(GLenum
    name)': gives 'unsigned char', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetIntegerv(GLenum pname, GLint
    *data)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetFloatv(GLenum pname, GLfloat
    *data)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetDoublev(GLenum pname, GLdouble
    *data)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetBooleanv(GLenum pname,
    GLboolean *data)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glReadPixels(GLint x, GLint y,
    GLsizei width, GLsizei height, GLenum format, GLenum type, void
    *pixels)': names 'void', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glTexImage2D(GLenum target, GLint
    level, GLint internalformat, GLsizei width, GLsizei height, GLint border,
    GLenum format, GLenum type, const void *pixels)': names 'void', which has
    no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glTexImage1D(GLenum target, GLint
    level, GLint internalformat, GLsizei width, GLint border, GLenum format,
    GLenum type, const void *pixels)': names 'void', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glTexParameteriv(GLenum target,
    GLenum pname, const GLint *params)': names 'GLint', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glTexParameterfv(GLenum target,
    GLenum pname, const GLfloat *params)': names 'GLfloat', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGenTextures(GLsizei n, GLuint
    *textures)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glDeleteTextures(GLsizei n, const
    GLuint *textures)': names 'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glTexSubImage2D(GLenum target,
    GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height,
    GLenum format, GLenum type, const void *pixels)': names 'void', which has
    no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glTexSubImage1D(GLenum target,
    GLint level, GLint xoffset, GLsizei width, GLenum format, GLenum type,
    const void *pixels)': names 'void', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glDrawElements(GLenum mode, GLsizei
    count, GLenum type, const void *indices)': names 'void', which has no
    cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glTexSubImage3D(GLenum target,
    GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width,
    GLsizei height, GLsizei depth, GLenum format, GLenum type, const void
    *pixels)': names 'void', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glTexImage3D(GLenum target, GLint
    level, GLint internalformat, GLsizei width, GLsizei height, GLsizei
    depth, GLint border, GLenum format, GLenum type, const void *pixels)':
    names 'void', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glDrawRangeElements(GLenum mode,
    GLuint start, GLuint end, GLsizei count, GLenum type, const void
    *indices)': names 'void', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetCompressedTexImage(GLenum
    target, GLint level, void *img)': names 'void', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glCompressedTexSubImage1D(GLenum
    target, GLint level, GLint xoffset, GLsizei width, GLenum format, GLsizei
    imageSize, const void *data)': names 'void', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glCompressedTexSubImage2D(GLenum
    target, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei
    height, GLenum format, GLsizei imageSize, const void *data)': names
    'void', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glCompressedTexSubImage3D(GLenum
    target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei
    width, GLsizei height, GLsizei depth, GLenum format, GLsizei imageSize,
    const void *data)': names 'void', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glCompressedTexImage1D(GLenum
    target, GLint level, GLenum internalformat, GLsizei width, GLint border,
    GLsizei imageSize, const void *data)': names 'void', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glCompressedTexImage2D(GLenum
    target, GLint level, GLenum internalformat, GLsizei width, GLsizei
    height, GLint border, GLsizei imageSize, const void *data)': names
    'void', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glCompressedTexImage3D(GLenum
    target, GLint level, GLenum internalformat, GLsizei width, GLsizei
    height, GLsizei depth, GLint border, GLsizei imageSize, const void
    *data)': names 'void', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glPointParameteriv(GLenum pname,
    const GLint *params)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glPointParameterfv(GLenum pname,
    const GLfloat *params)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glMultiDrawElements(GLenum mode,
    const GLsizei *count, GLenum type, const void *const *indices, GLsizei
    drawcount)': names 'GLsizei', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glMultiDrawArrays(GLenum mode,
    const GLint *first, const GLsizei *count, GLsizei drawcount)': names
    'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetBufferPointerv(GLenum target,
    GLenum pname, void **params)': takes a type Python has no way to hand
    over yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetBufferParameteriv(GLenum
    target, GLenum pname, GLint *params)': takes a number to change where it
    is.
  - Qt's 'void *QOpenGLFunctions_4_5_Core::glMapBuffer(GLenum target, GLenum
    access)': gives 'void', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetBufferSubData(GLenum target,
    GLintptr offset, GLsizeiptr size, void *data)': names 'void', which has
    no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glBufferSubData(GLenum target,
    GLintptr offset, GLsizeiptr size, const void *data)': names 'void', which
    has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glBufferData(GLenum target,
    GLsizeiptr size, const void *data, GLenum usage)': names 'void', which
    has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGenBuffers(GLsizei n, GLuint
    *buffers)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glDeleteBuffers(GLsizei n, const
    GLuint *buffers)': names 'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetQueryObjectuiv(GLuint id,
    GLenum pname, GLuint *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetQueryObjectiv(GLuint id,
    GLenum pname, GLint *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetQueryiv(GLenum target, GLenum
    pname, GLint *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glDeleteQueries(GLsizei n, const
    GLuint *ids)': names 'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGenQueries(GLsizei n, GLuint
    *ids)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttribPointer(GLuint index,
    GLint size, GLenum type, GLboolean normalized, GLsizei stride, const void
    *pointer)': names 'void', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttrib4usv(GLuint index,
    const GLushort *v)': names 'GLushort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttrib4uiv(GLuint index,
    const GLuint *v)': names 'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttrib4ubv(GLuint index,
    const GLubyte *v)': names 'GLubyte', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttrib4sv(GLuint index,
    const GLshort *v)': names 'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttrib4iv(GLuint index,
    const GLint *v)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttrib4fv(GLuint index,
    const GLfloat *v)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttrib4dv(GLuint index,
    const GLdouble *v)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttrib4bv(GLuint index,
    const GLbyte *v)': names 'GLbyte', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttrib4Nusv(GLuint index,
    const GLushort *v)': names 'GLushort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttrib4Nuiv(GLuint index,
    const GLuint *v)': names 'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttrib4Nubv(GLuint index,
    const GLubyte *v)': names 'GLubyte', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttrib4Nsv(GLuint index,
    const GLshort *v)': names 'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttrib4Niv(GLuint index,
    const GLint *v)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttrib4Nbv(GLuint index,
    const GLbyte *v)': names 'GLbyte', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttrib3sv(GLuint index,
    const GLshort *v)': names 'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttrib3fv(GLuint index,
    const GLfloat *v)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttrib3dv(GLuint index,
    const GLdouble *v)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttrib2sv(GLuint index,
    const GLshort *v)': names 'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttrib2fv(GLuint index,
    const GLfloat *v)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttrib2dv(GLuint index,
    const GLdouble *v)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttrib1sv(GLuint index,
    const GLshort *v)': names 'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttrib1fv(GLuint index,
    const GLfloat *v)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttrib1dv(GLuint index,
    const GLdouble *v)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glUniformMatrix4fv(GLint location,
    GLsizei count, GLboolean transpose, const GLfloat *value)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glUniformMatrix3fv(GLint location,
    GLsizei count, GLboolean transpose, const GLfloat *value)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glUniformMatrix2fv(GLint location,
    GLsizei count, GLboolean transpose, const GLfloat *value)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glUniform4iv(GLint location,
    GLsizei count, const GLint *value)': names 'GLint', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glUniform3iv(GLint location,
    GLsizei count, const GLint *value)': names 'GLint', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glUniform2iv(GLint location,
    GLsizei count, const GLint *value)': names 'GLint', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glUniform1iv(GLint location,
    GLsizei count, const GLint *value)': names 'GLint', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glUniform4fv(GLint location,
    GLsizei count, const GLfloat *value)': names 'GLfloat', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glUniform3fv(GLint location,
    GLsizei count, const GLfloat *value)': names 'GLfloat', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glUniform2fv(GLint location,
    GLsizei count, const GLfloat *value)': names 'GLfloat', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glUniform1fv(GLint location,
    GLsizei count, const GLfloat *value)': names 'GLfloat', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glShaderSource(GLuint shader,
    GLsizei count, const GLchar *const *string, const GLint *length)': names
    'GLchar *const', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetVertexAttribPointerv(GLuint
    index, GLenum pname, void **pointer)': takes a type Python has no way to
    hand over yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetVertexAttribiv(GLuint index,
    GLenum pname, GLint *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetVertexAttribfv(GLuint index,
    GLenum pname, GLfloat *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetVertexAttribdv(GLuint index,
    GLenum pname, GLdouble *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetUniformiv(GLuint program,
    GLint location, GLint *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetUniformfv(GLuint program,
    GLint location, GLfloat *params)': takes a number to change where it is.
  - Qt's 'GLint QOpenGLFunctions_4_5_Core::glGetUniformLocation(GLuint
    program, const GLchar *name)': names 'GLchar', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetShaderSource(GLuint shader,
    GLsizei bufSize, GLsizei *length, GLchar *source)': takes a number to
    change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetShaderInfoLog(GLuint shader,
    GLsizei bufSize, GLsizei *length, GLchar *infoLog)': takes a number to
    change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetShaderiv(GLuint shader, GLenum
    pname, GLint *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetProgramInfoLog(GLuint program,
    GLsizei bufSize, GLsizei *length, GLchar *infoLog)': takes a number to
    change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetProgramiv(GLuint program,
    GLenum pname, GLint *params)': takes a number to change where it is.
  - Qt's 'GLint QOpenGLFunctions_4_5_Core::glGetAttribLocation(GLuint
    program, const GLchar *name)': names 'GLchar', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetAttachedShaders(GLuint
    program, GLsizei maxCount, GLsizei *count, GLuint *shaders)': takes a
    number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetActiveUniform(GLuint program,
    GLuint index, GLsizei bufSize, GLsizei *length, GLint *size, GLenum
    *type, GLchar *name)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetActiveAttrib(GLuint program,
    GLuint index, GLsizei bufSize, GLsizei *length, GLint *size, GLenum
    *type, GLchar *name)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glBindAttribLocation(GLuint
    program, GLuint index, const GLchar *name)': names 'GLchar', which has no
    cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glDrawBuffers(GLsizei n, const
    GLenum *bufs)': names 'GLenum', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glUniformMatrix4x3fv(GLint
    location, GLsizei count, GLboolean transpose, const GLfloat *value)':
    names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glUniformMatrix3x4fv(GLint
    location, GLsizei count, GLboolean transpose, const GLfloat *value)':
    names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glUniformMatrix4x2fv(GLint
    location, GLsizei count, GLboolean transpose, const GLfloat *value)':
    names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glUniformMatrix2x4fv(GLint
    location, GLsizei count, GLboolean transpose, const GLfloat *value)':
    names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glUniformMatrix3x2fv(GLint
    location, GLsizei count, GLboolean transpose, const GLfloat *value)':
    names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glUniformMatrix2x3fv(GLint
    location, GLsizei count, GLboolean transpose, const GLfloat *value)':
    names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGenVertexArrays(GLsizei n, GLuint
    *arrays)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glDeleteVertexArrays(GLsizei n,
    const GLuint *arrays)': names 'GLuint', which has no cute class yet.
  - Qt's 'void *QOpenGLFunctions_4_5_Core::glMapBufferRange(GLenum target,
    GLintptr offset, GLsizeiptr length, GLbitfield access)': gives 'void',
    which has no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_5_Core::glGetFramebufferAttachmentParameteriv(GLenum
    target, GLenum attachment, GLenum pname, GLint *params)': takes a number
    to change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGenFramebuffers(GLsizei n, GLuint
    *framebuffers)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glDeleteFramebuffers(GLsizei n,
    const GLuint *framebuffers)': names 'GLuint', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetRenderbufferParameteriv(GLenum
    target, GLenum pname, GLint *params)': takes a number to change where it
    is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGenRenderbuffers(GLsizei n,
    GLuint *renderbuffers)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glDeleteRenderbuffers(GLsizei n,
    const GLuint *renderbuffers)': names 'GLuint', which has no cute class
    yet.
  - Qt's 'const GLubyte *QOpenGLFunctions_4_5_Core::glGetStringi(GLenum name,
    GLuint index)': gives 'unsigned char', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glClearBufferfv(GLenum buffer,
    GLint drawbuffer, const GLfloat *value)': names 'GLfloat', which has no
    cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glClearBufferuiv(GLenum buffer,
    GLint drawbuffer, const GLuint *value)': names 'GLuint', which has no
    cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glClearBufferiv(GLenum buffer,
    GLint drawbuffer, const GLint *value)': names 'GLint', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetTexParameterIuiv(GLenum
    target, GLenum pname, GLuint *params)': takes a number to change where it
    is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetTexParameterIiv(GLenum target,
    GLenum pname, GLint *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glTexParameterIuiv(GLenum target,
    GLenum pname, const GLuint *params)': names 'GLuint', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glTexParameterIiv(GLenum target,
    GLenum pname, const GLint *params)': names 'GLint', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glUniform4uiv(GLint location,
    GLsizei count, const GLuint *value)': names 'GLuint', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glUniform3uiv(GLint location,
    GLsizei count, const GLuint *value)': names 'GLuint', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glUniform2uiv(GLint location,
    GLsizei count, const GLuint *value)': names 'GLuint', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glUniform1uiv(GLint location,
    GLsizei count, const GLuint *value)': names 'GLuint', which has no cute
    class yet.
  - Qt's 'GLint QOpenGLFunctions_4_5_Core::glGetFragDataLocation(GLuint
    program, const GLchar *name)': names 'GLchar', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glBindFragDataLocation(GLuint
    program, GLuint color, const GLchar *name)': names 'GLchar', which has no
    cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetUniformuiv(GLuint program,
    GLint location, GLuint *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttribI4usv(GLuint index,
    const GLushort *v)': names 'GLushort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttribI4ubv(GLuint index,
    const GLubyte *v)': names 'GLubyte', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttribI4sv(GLuint index,
    const GLshort *v)': names 'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttribI4bv(GLuint index,
    const GLbyte *v)': names 'GLbyte', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttribI4uiv(GLuint index,
    const GLuint *v)': names 'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttribI3uiv(GLuint index,
    const GLuint *v)': names 'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttribI2uiv(GLuint index,
    const GLuint *v)': names 'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttribI1uiv(GLuint index,
    const GLuint *v)': names 'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttribI4iv(GLuint index,
    const GLint *v)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttribI3iv(GLuint index,
    const GLint *v)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttribI2iv(GLuint index,
    const GLint *v)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttribI1iv(GLuint index,
    const GLint *v)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetVertexAttribIuiv(GLuint index,
    GLenum pname, GLuint *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetVertexAttribIiv(GLuint index,
    GLenum pname, GLint *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttribIPointer(GLuint
    index, GLint size, GLenum type, GLsizei stride, const void *pointer)':
    names 'void', which has no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_5_Core::glGetTransformFeedbackVarying(GLuint program,
    GLuint index, GLsizei bufSize, GLsizei *length, GLsizei *size, GLenum
    *type, GLchar *name)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glTransformFeedbackVaryings(GLuint
    program, GLsizei count, const GLchar *const *varyings, GLenum
    bufferMode)': names 'GLchar *const', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetIntegeri_v(GLenum target,
    GLuint index, GLint *data)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetBooleani_v(GLenum target,
    GLuint index, GLboolean *data)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetActiveUniformBlockName(GLuint
    program, GLuint uniformBlockIndex, GLsizei bufSize, GLsizei *length,
    GLchar *uniformBlockName)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetActiveUniformBlockiv(GLuint
    program, GLuint uniformBlockIndex, GLenum pname, GLint *params)': takes a
    number to change where it is.
  - Qt's 'GLuint QOpenGLFunctions_4_5_Core::glGetUniformBlockIndex(GLuint
    program, const GLchar *uniformBlockName)': names 'GLchar', which has no
    cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetActiveUniformName(GLuint
    program, GLuint uniformIndex, GLsizei bufSize, GLsizei *length, GLchar
    *uniformName)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetActiveUniformsiv(GLuint
    program, GLsizei uniformCount, const GLuint *uniformIndices, GLenum
    pname, GLint *params)': names 'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetUniformIndices(GLuint program,
    GLsizei uniformCount, const GLchar *const *uniformNames, GLuint
    *uniformIndices)': names 'GLchar *const', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glDrawElementsInstanced(GLenum
    mode, GLsizei count, GLenum type, const void *indices, GLsizei
    instancecount)': names 'void', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetMultisamplefv(GLenum pname,
    GLuint index, GLfloat *val)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetBufferParameteri64v(GLenum
    target, GLenum pname, GLint64 *params)': takes a number to change where
    it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetInteger64i_v(GLenum target,
    GLuint index, GLint64 *data)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetSynciv(GLsync sync, GLenum
    pname, GLsizei bufSize, GLsizei *length, GLint *values)': names 'struct
    __GLsync', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetInteger64v(GLenum pname,
    GLint64 *data)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glWaitSync(GLsync sync, GLbitfield
    flags, GLuint64 timeout)': names 'struct __GLsync', which has no cute
    class yet.
  - Qt's 'GLenum QOpenGLFunctions_4_5_Core::glClientWaitSync(GLsync sync,
    GLbitfield flags, GLuint64 timeout)': names 'struct __GLsync', which has
    no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glDeleteSync(GLsync sync)': names
    'struct __GLsync', which has no cute class yet.
  - Qt's 'GLboolean QOpenGLFunctions_4_5_Core::glIsSync(GLsync sync)': names
    'struct __GLsync', which has no cute class yet.
  - Qt's 'GLsync QOpenGLFunctions_4_5_Core::glFenceSync(GLenum condition,
    GLbitfield flags)': gives a type Python has no way to take yet.
  - Qt's 'void
    QOpenGLFunctions_4_5_Core::glMultiDrawElementsBaseVertex(GLenum mode,
    const GLsizei *count, GLenum type, const void *const *indices, GLsizei
    drawcount, const GLint *basevertex)': names 'GLsizei', which has no cute
    class yet.
  - Qt's 'void
    QOpenGLFunctions_4_5_Core::glDrawElementsInstancedBaseVertex(GLenum mode,
    GLsizei count, GLenum type, const void *indices, GLsizei instancecount,
    GLint basevertex)': names 'void', which has no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_5_Core::glDrawRangeElementsBaseVertex(GLenum mode,
    GLuint start, GLuint end, GLsizei count, GLenum type, const void
    *indices, GLint basevertex)': names 'void', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glDrawElementsBaseVertex(GLenum
    mode, GLsizei count, GLenum type, const void *indices, GLint
    basevertex)': names 'void', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttribP4uiv(GLuint index,
    GLenum type, GLboolean normalized, const GLuint *value)': names 'GLuint',
    which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttribP3uiv(GLuint index,
    GLenum type, GLboolean normalized, const GLuint *value)': names 'GLuint',
    which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttribP2uiv(GLuint index,
    GLenum type, GLboolean normalized, const GLuint *value)': names 'GLuint',
    which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttribP1uiv(GLuint index,
    GLenum type, GLboolean normalized, const GLuint *value)': names 'GLuint',
    which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetQueryObjectui64v(GLuint id,
    GLenum pname, GLuint64 *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetQueryObjecti64v(GLuint id,
    GLenum pname, GLint64 *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetSamplerParameterIuiv(GLuint
    sampler, GLenum pname, GLuint *params)': takes a number to change where
    it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetSamplerParameterfv(GLuint
    sampler, GLenum pname, GLfloat *params)': takes a number to change where
    it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetSamplerParameterIiv(GLuint
    sampler, GLenum pname, GLint *params)': takes a number to change where it
    is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetSamplerParameteriv(GLuint
    sampler, GLenum pname, GLint *params)': takes a number to change where it
    is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glSamplerParameterIuiv(GLuint
    sampler, GLenum pname, const GLuint *param)': names 'GLuint', which has
    no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glSamplerParameterIiv(GLuint
    sampler, GLenum pname, const GLint *param)': names 'GLint', which has no
    cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glSamplerParameterfv(GLuint
    sampler, GLenum pname, const GLfloat *param)': names 'GLfloat', which has
    no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glSamplerParameteriv(GLuint
    sampler, GLenum pname, const GLint *param)': names 'GLint', which has no
    cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glDeleteSamplers(GLsizei count,
    const GLuint *samplers)': names 'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGenSamplers(GLsizei count, GLuint
    *samplers)': takes a number to change where it is.
  - Qt's 'GLint QOpenGLFunctions_4_5_Core::glGetFragDataIndex(GLuint program,
    const GLchar *name)': names 'GLchar', which has no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_5_Core::glBindFragDataLocationIndexed(GLuint program,
    GLuint colorNumber, GLuint index, const GLchar *name)': names 'GLchar',
    which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetQueryIndexediv(GLenum target,
    GLuint index, GLenum pname, GLint *params)': takes a number to change
    where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGenTransformFeedbacks(GLsizei n,
    GLuint *ids)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glDeleteTransformFeedbacks(GLsizei
    n, const GLuint *ids)': names 'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glPatchParameterfv(GLenum pname,
    const GLfloat *values)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetProgramStageiv(GLuint program,
    GLenum shadertype, GLenum pname, GLint *values)': takes a number to
    change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetUniformSubroutineuiv(GLenum
    shadertype, GLint location, GLuint *params)': takes a number to change
    where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glUniformSubroutinesuiv(GLenum
    shadertype, GLsizei count, const GLuint *indices)': names 'GLuint', which
    has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetActiveSubroutineName(GLuint
    program, GLenum shadertype, GLuint index, GLsizei bufsize, GLsizei
    *length, GLchar *name)': takes a number to change where it is.
  - Qt's 'void
    QOpenGLFunctions_4_5_Core::glGetActiveSubroutineUniformName(GLuint
    program, GLenum shadertype, GLuint index, GLsizei bufsize, GLsizei
    *length, GLchar *name)': takes a number to change where it is.
  - Qt's 'void
    QOpenGLFunctions_4_5_Core::glGetActiveSubroutineUniformiv(GLuint program,
    GLenum shadertype, GLuint index, GLenum pname, GLint *values)': takes a
    number to change where it is.
  - Qt's 'GLuint QOpenGLFunctions_4_5_Core::glGetSubroutineIndex(GLuint
    program, GLenum shadertype, const GLchar *name)': names 'GLchar', which
    has no cute class yet.
  - Qt's 'GLint
    QOpenGLFunctions_4_5_Core::glGetSubroutineUniformLocation(GLuint program,
    GLenum shadertype, const GLchar *name)': names 'GLchar', which has no
    cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetUniformdv(GLuint program,
    GLint location, GLdouble *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glUniformMatrix4x3dv(GLint
    location, GLsizei count, GLboolean transpose, const GLdouble *value)':
    names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glUniformMatrix4x2dv(GLint
    location, GLsizei count, GLboolean transpose, const GLdouble *value)':
    names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glUniformMatrix3x4dv(GLint
    location, GLsizei count, GLboolean transpose, const GLdouble *value)':
    names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glUniformMatrix3x2dv(GLint
    location, GLsizei count, GLboolean transpose, const GLdouble *value)':
    names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glUniformMatrix2x4dv(GLint
    location, GLsizei count, GLboolean transpose, const GLdouble *value)':
    names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glUniformMatrix2x3dv(GLint
    location, GLsizei count, GLboolean transpose, const GLdouble *value)':
    names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glUniformMatrix4dv(GLint location,
    GLsizei count, GLboolean transpose, const GLdouble *value)': names
    'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glUniformMatrix3dv(GLint location,
    GLsizei count, GLboolean transpose, const GLdouble *value)': names
    'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glUniformMatrix2dv(GLint location,
    GLsizei count, GLboolean transpose, const GLdouble *value)': names
    'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glUniform4dv(GLint location,
    GLsizei count, const GLdouble *value)': names 'GLdouble', which has no
    cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glUniform3dv(GLint location,
    GLsizei count, const GLdouble *value)': names 'GLdouble', which has no
    cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glUniform2dv(GLint location,
    GLsizei count, const GLdouble *value)': names 'GLdouble', which has no
    cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glUniform1dv(GLint location,
    GLsizei count, const GLdouble *value)': names 'GLdouble', which has no
    cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glDrawElementsIndirect(GLenum mode,
    GLenum type, const void *indirect)': names 'void', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glDrawArraysIndirect(GLenum mode,
    const void *indirect)': names 'void', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetDoublei_v(GLenum target,
    GLuint index, GLdouble *data)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetFloati_v(GLenum target, GLuint
    index, GLfloat *data)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glDepthRangeArrayv(GLuint first,
    GLsizei count, const GLdouble *v)': names 'GLdouble', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glScissorIndexedv(GLuint index,
    const GLint *v)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glScissorArrayv(GLuint first,
    GLsizei count, const GLint *v)': names 'GLint', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glViewportIndexedfv(GLuint index,
    const GLfloat *v)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glViewportArrayv(GLuint first,
    GLsizei count, const GLfloat *v)': names 'GLfloat', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetVertexAttribLdv(GLuint index,
    GLenum pname, GLdouble *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttribLPointer(GLuint
    index, GLint size, GLenum type, GLsizei stride, const void *pointer)':
    names 'void', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttribL4dv(GLuint index,
    const GLdouble *v)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttribL3dv(GLuint index,
    const GLdouble *v)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttribL2dv(GLuint index,
    const GLdouble *v)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttribL1dv(GLuint index,
    const GLdouble *v)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetProgramPipelineInfoLog(GLuint
    pipeline, GLsizei bufSize, GLsizei *length, GLchar *infoLog)': takes a
    number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniformMatrix4x3dv(GLuint
    program, GLint location, GLsizei count, GLboolean transpose, const
    GLdouble *value)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniformMatrix3x4dv(GLuint
    program, GLint location, GLsizei count, GLboolean transpose, const
    GLdouble *value)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniformMatrix4x2dv(GLuint
    program, GLint location, GLsizei count, GLboolean transpose, const
    GLdouble *value)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniformMatrix2x4dv(GLuint
    program, GLint location, GLsizei count, GLboolean transpose, const
    GLdouble *value)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniformMatrix3x2dv(GLuint
    program, GLint location, GLsizei count, GLboolean transpose, const
    GLdouble *value)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniformMatrix2x3dv(GLuint
    program, GLint location, GLsizei count, GLboolean transpose, const
    GLdouble *value)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniformMatrix4x3fv(GLuint
    program, GLint location, GLsizei count, GLboolean transpose, const
    GLfloat *value)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniformMatrix3x4fv(GLuint
    program, GLint location, GLsizei count, GLboolean transpose, const
    GLfloat *value)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniformMatrix4x2fv(GLuint
    program, GLint location, GLsizei count, GLboolean transpose, const
    GLfloat *value)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniformMatrix2x4fv(GLuint
    program, GLint location, GLsizei count, GLboolean transpose, const
    GLfloat *value)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniformMatrix3x2fv(GLuint
    program, GLint location, GLsizei count, GLboolean transpose, const
    GLfloat *value)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniformMatrix2x3fv(GLuint
    program, GLint location, GLsizei count, GLboolean transpose, const
    GLfloat *value)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniformMatrix4dv(GLuint
    program, GLint location, GLsizei count, GLboolean transpose, const
    GLdouble *value)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniformMatrix3dv(GLuint
    program, GLint location, GLsizei count, GLboolean transpose, const
    GLdouble *value)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniformMatrix2dv(GLuint
    program, GLint location, GLsizei count, GLboolean transpose, const
    GLdouble *value)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniformMatrix4fv(GLuint
    program, GLint location, GLsizei count, GLboolean transpose, const
    GLfloat *value)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniformMatrix3fv(GLuint
    program, GLint location, GLsizei count, GLboolean transpose, const
    GLfloat *value)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniformMatrix2fv(GLuint
    program, GLint location, GLsizei count, GLboolean transpose, const
    GLfloat *value)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniform4uiv(GLuint
    program, GLint location, GLsizei count, const GLuint *value)': names
    'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniform4dv(GLuint program,
    GLint location, GLsizei count, const GLdouble *value)': names 'GLdouble',
    which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniform4fv(GLuint program,
    GLint location, GLsizei count, const GLfloat *value)': names 'GLfloat',
    which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniform4iv(GLuint program,
    GLint location, GLsizei count, const GLint *value)': names 'GLint', which
    has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniform3uiv(GLuint
    program, GLint location, GLsizei count, const GLuint *value)': names
    'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniform3dv(GLuint program,
    GLint location, GLsizei count, const GLdouble *value)': names 'GLdouble',
    which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniform3fv(GLuint program,
    GLint location, GLsizei count, const GLfloat *value)': names 'GLfloat',
    which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniform3iv(GLuint program,
    GLint location, GLsizei count, const GLint *value)': names 'GLint', which
    has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniform2uiv(GLuint
    program, GLint location, GLsizei count, const GLuint *value)': names
    'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniform2dv(GLuint program,
    GLint location, GLsizei count, const GLdouble *value)': names 'GLdouble',
    which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniform2fv(GLuint program,
    GLint location, GLsizei count, const GLfloat *value)': names 'GLfloat',
    which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniform2iv(GLuint program,
    GLint location, GLsizei count, const GLint *value)': names 'GLint', which
    has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniform1uiv(GLuint
    program, GLint location, GLsizei count, const GLuint *value)': names
    'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniform1dv(GLuint program,
    GLint location, GLsizei count, const GLdouble *value)': names 'GLdouble',
    which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniform1fv(GLuint program,
    GLint location, GLsizei count, const GLfloat *value)': names 'GLfloat',
    which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniform1iv(GLuint program,
    GLint location, GLsizei count, const GLint *value)': names 'GLint', which
    has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetProgramPipelineiv(GLuint
    pipeline, GLenum pname, GLint *params)': takes a number to change where
    it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGenProgramPipelines(GLsizei n,
    GLuint *pipelines)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glDeleteProgramPipelines(GLsizei n,
    const GLuint *pipelines)': names 'GLuint', which has no cute class yet.
  - Qt's 'GLuint QOpenGLFunctions_4_5_Core::glCreateShaderProgramv(GLenum
    type, GLsizei count, const GLchar *const *strings)': names 'GLchar
    *const', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glProgramBinary(GLuint program,
    GLenum binaryFormat, const void *binary, GLsizei length)': names 'void',
    which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetProgramBinary(GLuint program,
    GLsizei bufSize, GLsizei *length, GLenum *binaryFormat, void *binary)':
    takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetShaderPrecisionFormat(GLenum
    shadertype, GLenum precisiontype, GLint *range, GLint *precision)': takes
    a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glShaderBinary(GLsizei count, const
    GLuint *shaders, GLenum binaryformat, const void *binary, GLsizei
    length)': names 'GLuint', which has no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_5_Core::glGetActiveAtomicCounterBufferiv(GLuint
    program, GLuint bufferIndex, GLenum pname, GLint *params)': takes a
    number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetInternalformativ(GLenum
    target, GLenum internalformat, GLenum pname, GLsizei bufSize, GLint
    *params)': takes a number to change where it is.
  - Qt's 'void
    QOpenGLFunctions_4_5_Core::glDrawElementsInstancedBaseVertexBaseInstance(
    GLenum mode, GLsizei count, GLenum type, const void *indices, GLsizei
    instancecount, GLint basevertex, GLuint baseinstance)': names 'void',
    which has no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_5_Core::glDrawElementsInstancedBaseInstance(GLenum
    mode, GLsizei count, GLenum type, const void *indices, GLsizei
    instancecount, GLuint baseinstance)': names 'void', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetObjectPtrLabel(const void
    *ptr, GLsizei bufSize, GLsizei *length, GLchar *label)': names 'void',
    which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glObjectPtrLabel(const void *ptr,
    GLsizei length, const GLchar *label)': names 'void', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetObjectLabel(GLenum identifier,
    GLuint name, GLsizei bufSize, GLsizei *length, GLchar *label)': takes a
    number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glObjectLabel(GLenum identifier,
    GLuint name, GLsizei length, const GLchar *label)': names 'GLchar', which
    has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glPushDebugGroup(GLenum source,
    GLuint id, GLsizei length, const GLchar *message)': names 'GLchar', which
    has no cute class yet.
  - Qt's 'GLuint QOpenGLFunctions_4_5_Core::glGetDebugMessageLog(GLuint
    count, GLsizei bufSize, GLenum *sources, GLenum *types, GLuint *ids,
    GLenum *severities, GLsizei *lengths, GLchar *messageLog)': takes a
    number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glDebugMessageCallback(GLDEBUGPROC
    callback, const void *userParam)': takes a type Python has no way to hand
    over yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glDebugMessageInsert(GLenum source,
    GLenum type, GLuint id, GLenum severity, GLsizei length, const GLchar
    *buf)': names 'GLchar', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glDebugMessageControl(GLenum
    source, GLenum type, GLenum severity, GLsizei count, const GLuint *ids,
    GLboolean enabled)': names 'GLuint', which has no cute class yet.
  - Qt's 'GLint
    QOpenGLFunctions_4_5_Core::glGetProgramResourceLocationIndex(GLuint
    program, GLenum programInterface, const GLchar *name)': names 'GLchar',
    which has no cute class yet.
  - Qt's 'GLint
    QOpenGLFunctions_4_5_Core::glGetProgramResourceLocation(GLuint program,
    GLenum programInterface, const GLchar *name)': names 'GLchar', which has
    no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetProgramResourceiv(GLuint
    program, GLenum programInterface, GLuint index, GLsizei propCount, const
    GLenum *props, GLsizei bufSize, GLsizei *length, GLint *params)': names
    'GLenum', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetProgramResourceName(GLuint
    program, GLenum programInterface, GLuint index, GLsizei bufSize, GLsizei
    *length, GLchar *name)': takes a number to change where it is.
  - Qt's 'GLuint QOpenGLFunctions_4_5_Core::glGetProgramResourceIndex(GLuint
    program, GLenum programInterface, const GLchar *name)': names 'GLchar',
    which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetProgramInterfaceiv(GLuint
    program, GLenum programInterface, GLenum pname, GLint *params)': takes a
    number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glMultiDrawElementsIndirect(GLenum
    mode, GLenum type, const void *indirect, GLsizei drawcount, GLsizei
    stride)': names 'void', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glMultiDrawArraysIndirect(GLenum
    mode, const void *indirect, GLsizei drawcount, GLsizei stride)': names
    'void', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glInvalidateSubFramebuffer(GLenum
    target, GLsizei numAttachments, const GLenum *attachments, GLint x, GLint
    y, GLsizei width, GLsizei height)': names 'GLenum', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glInvalidateFramebuffer(GLenum
    target, GLsizei numAttachments, const GLenum *attachments)': names
    'GLenum', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetInternalformati64v(GLenum
    target, GLenum internalformat, GLenum pname, GLsizei bufSize, GLint64
    *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetFramebufferParameteriv(GLenum
    target, GLenum pname, GLint *params)': takes a number to change where it
    is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glClearBufferSubData(GLenum target,
    GLenum internalformat, GLintptr offset, GLsizeiptr size, GLenum format,
    GLenum type, const void *data)': names 'void', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glClearBufferData(GLenum target,
    GLenum internalformat, GLenum format, GLenum type, const void *data)':
    names 'void', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glBindVertexBuffers(GLuint first,
    GLsizei count, const GLuint *buffers, const GLintptr *offsets, const
    GLsizei *strides)': names 'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glBindImageTextures(GLuint first,
    GLsizei count, const GLuint *textures)': names 'GLuint', which has no
    cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glBindSamplers(GLuint first,
    GLsizei count, const GLuint *samplers)': names 'GLuint', which has no
    cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glBindTextures(GLuint first,
    GLsizei count, const GLuint *textures)': names 'GLuint', which has no
    cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glBindBuffersRange(GLenum target,
    GLuint first, GLsizei count, const GLuint *buffers, const GLintptr
    *offsets, const GLsizeiptr *sizes)': names 'GLuint', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glBindBuffersBase(GLenum target,
    GLuint first, GLsizei count, const GLuint *buffers)': names 'GLuint',
    which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glClearTexSubImage(GLuint texture,
    GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width,
    GLsizei height, GLsizei depth, GLenum format, GLenum type, const void
    *data)': names 'void', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glClearTexImage(GLuint texture,
    GLint level, GLenum format, GLenum type, const void *data)': names
    'void', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glBufferStorage(GLenum target,
    GLsizeiptr size, const void *data, GLbitfield flags)': names 'void',
    which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glReadnPixels(GLint x, GLint y,
    GLsizei width, GLsizei height, GLenum format, GLenum type, GLsizei
    bufSize, void *data)': names 'void', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetnUniformuiv(GLuint program,
    GLint location, GLsizei bufSize, GLuint *params)': takes a number to
    change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetnUniformiv(GLuint program,
    GLint location, GLsizei bufSize, GLint *params)': takes a number to
    change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetnUniformfv(GLuint program,
    GLint location, GLsizei bufSize, GLfloat *params)': takes a number to
    change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetnUniformdv(GLuint program,
    GLint location, GLsizei bufSize, GLdouble *params)': takes a number to
    change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetnTexImage(GLenum target, GLint
    level, GLenum format, GLenum type, GLsizei bufSize, void *pixels)': names
    'void', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetnCompressedTexImage(GLenum
    target, GLint lod, GLsizei bufSize, void *pixels)': names 'void', which
    has no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_5_Core::glGetCompressedTextureSubImage(GLuint texture,
    GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width,
    GLsizei height, GLsizei depth, GLsizei bufSize, void *pixels)': names
    'void', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetTextureSubImage(GLuint
    texture, GLint level, GLint xoffset, GLint yoffset, GLint zoffset,
    GLsizei width, GLsizei height, GLsizei depth, GLenum format, GLenum type,
    GLsizei bufSize, void *pixels)': names 'void', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glCreateQueries(GLenum target,
    GLsizei n, GLuint *ids)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glCreateProgramPipelines(GLsizei n,
    GLuint *pipelines)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glCreateSamplers(GLsizei n, GLuint
    *samplers)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetVertexArrayIndexed64iv(GLuint
    vaobj, GLuint index, GLenum pname, GLint64 *param)': takes a number to
    change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetVertexArrayIndexediv(GLuint
    vaobj, GLuint index, GLenum pname, GLint *param)': takes a number to
    change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetVertexArrayiv(GLuint vaobj,
    GLenum pname, GLint *param)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glVertexArrayVertexBuffers(GLuint
    vaobj, GLuint first, GLsizei count, const GLuint *buffers, const GLintptr
    *offsets, const GLsizei *strides)': names 'GLuint', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glCreateVertexArrays(GLsizei n,
    GLuint *arrays)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetTextureParameteriv(GLuint
    texture, GLenum pname, GLint *params)': takes a number to change where it
    is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetTextureParameterIuiv(GLuint
    texture, GLenum pname, GLuint *params)': takes a number to change where
    it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetTextureParameterIiv(GLuint
    texture, GLenum pname, GLint *params)': takes a number to change where it
    is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetTextureParameterfv(GLuint
    texture, GLenum pname, GLfloat *params)': takes a number to change where
    it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetTextureLevelParameteriv(GLuint
    texture, GLint level, GLenum pname, GLint *params)': takes a number to
    change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetTextureLevelParameterfv(GLuint
    texture, GLint level, GLenum pname, GLfloat *params)': takes a number to
    change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetCompressedTextureImage(GLuint
    texture, GLint level, GLsizei bufSize, void *pixels)': names 'void',
    which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetTextureImage(GLuint texture,
    GLint level, GLenum format, GLenum type, GLsizei bufSize, void *pixels)':
    names 'void', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glTextureParameteriv(GLuint
    texture, GLenum pname, const GLint *param)': names 'GLint', which has no
    cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glTextureParameterIuiv(GLuint
    texture, GLenum pname, const GLuint *params)': names 'GLuint', which has
    no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glTextureParameterIiv(GLuint
    texture, GLenum pname, const GLint *params)': names 'GLint', which has no
    cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glTextureParameterfv(GLuint
    texture, GLenum pname, const GLfloat *param)': names 'GLfloat', which has
    no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_5_Core::glCompressedTextureSubImage3D(GLuint texture,
    GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width,
    GLsizei height, GLsizei depth, GLenum format, GLsizei imageSize, const
    void *data)': names 'void', which has no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_5_Core::glCompressedTextureSubImage2D(GLuint texture,
    GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height,
    GLenum format, GLsizei imageSize, const void *data)': names 'void', which
    has no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_5_Core::glCompressedTextureSubImage1D(GLuint texture,
    GLint level, GLint xoffset, GLsizei width, GLenum format, GLsizei
    imageSize, const void *data)': names 'void', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glTextureSubImage3D(GLuint texture,
    GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width,
    GLsizei height, GLsizei depth, GLenum format, GLenum type, const void
    *pixels)': names 'void', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glTextureSubImage2D(GLuint texture,
    GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height,
    GLenum format, GLenum type, const void *pixels)': names 'void', which has
    no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glTextureSubImage1D(GLuint texture,
    GLint level, GLint xoffset, GLsizei width, GLenum format, GLenum type,
    const void *pixels)': names 'void', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glCreateTextures(GLenum target,
    GLsizei n, GLuint *textures)': takes a number to change where it is.
  - Qt's 'void
    QOpenGLFunctions_4_5_Core::glGetNamedRenderbufferParameteriv(GLuint
    renderbuffer, GLenum pname, GLint *params)': takes a number to change
    where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glCreateRenderbuffers(GLsizei n,
    GLuint *renderbuffers)': takes a number to change where it is.
  - Qt's 'void
    QOpenGLFunctions_4_5_Core::glGetNamedFramebufferAttachmentParameteriv(
    GLuint framebuffer, GLenum attachment, GLenum pname, GLint *params)':
    takes a number to change where it is.
  - Qt's 'void
    QOpenGLFunctions_4_5_Core::glGetNamedFramebufferParameteriv(GLuint
    framebuffer, GLenum pname, GLint *param)': takes a number to change where
    it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glClearNamedFramebufferfv(GLuint
    framebuffer, GLenum buffer, GLint drawbuffer, const GLfloat *value)':
    names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glClearNamedFramebufferuiv(GLuint
    framebuffer, GLenum buffer, GLint drawbuffer, const GLuint *value)':
    names 'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glClearNamedFramebufferiv(GLuint
    framebuffer, GLenum buffer, GLint drawbuffer, const GLint *value)': names
    'GLint', which has no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_5_Core::glInvalidateNamedFramebufferSubData(GLuint
    framebuffer, GLsizei numAttachments, const GLenum *attachments, GLint x,
    GLint y, GLsizei width, GLsizei height)': names 'GLenum', which has no
    cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_5_Core::glInvalidateNamedFramebufferData(GLuint
    framebuffer, GLsizei numAttachments, const GLenum *attachments)': names
    'GLenum', which has no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_5_Core::glNamedFramebufferDrawBuffers(GLuint
    framebuffer, GLsizei n, const GLenum *bufs)': names 'GLenum', which has
    no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glCreateFramebuffers(GLsizei n,
    GLuint *framebuffers)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetNamedBufferSubData(GLuint
    buffer, GLintptr offset, GLsizeiptr size, void *data)': names 'void',
    which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetNamedBufferPointerv(GLuint
    buffer, GLenum pname, void **params)': takes a type Python has no way to
    hand over yet.
  - Qt's 'void
    QOpenGLFunctions_4_5_Core::glGetNamedBufferParameteri64v(GLuint buffer,
    GLenum pname, GLint64 *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetNamedBufferParameteriv(GLuint
    buffer, GLenum pname, GLint *params)': takes a number to change where it
    is.
  - Qt's 'void *QOpenGLFunctions_4_5_Core::glMapNamedBufferRange(GLuint
    buffer, GLintptr offset, GLsizeiptr length, GLbitfield access)': gives
    'void', which has no cute class yet.
  - Qt's 'void *QOpenGLFunctions_4_5_Core::glMapNamedBuffer(GLuint buffer,
    GLenum access)': gives 'void', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glClearNamedBufferSubData(GLuint
    buffer, GLenum internalformat, GLintptr offset, GLsizeiptr size, GLenum
    format, GLenum type, const void *data)': names 'void', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glClearNamedBufferData(GLuint
    buffer, GLenum internalformat, GLenum format, GLenum type, const void
    *data)': names 'void', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glNamedBufferSubData(GLuint buffer,
    GLintptr offset, GLsizeiptr size, const void *data)': names 'void', which
    has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glNamedBufferData(GLuint buffer,
    GLsizeiptr size, const void *data, GLenum usage)': names 'void', which
    has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glNamedBufferStorage(GLuint buffer,
    GLsizeiptr size, const void *data, GLbitfield flags)': names 'void',
    which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glCreateBuffers(GLsizei n, GLuint
    *buffers)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetTransformFeedbacki64_v(GLuint
    xfb, GLenum pname, GLuint index, GLint64 *param)': takes a number to
    change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetTransformFeedbacki_v(GLuint
    xfb, GLenum pname, GLuint index, GLint *param)': takes a number to change
    where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glGetTransformFeedbackiv(GLuint
    xfb, GLenum pname, GLint *param)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_5_Core::glCreateTransformFeedbacks(GLsizei
    n, GLuint *ids)': takes a number to change where it is.

  What to expect
  --------------

  - The C++ QOpenGLFunctions_4_5_Core is created at the first use, not by
    'QOpenGLFunctions_4_5_Core(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QOpenGLFunctions_4_5_Core.
  - Each name of Qt's QOpenGLFunctions_4_5_Core that has no cute function
    yet, 'glBindAttribLocation', 'glBindBuffersBase', 'glBindBuffersRange',
    'glBindFragDataLocation', 'glBindFragDataLocationIndexed',
    'glBindImageTextures', 'glBindSamplers', 'glBindTextures',
    'glBindVertexBuffers', 'glBufferData', 'glBufferStorage',
    'glBufferSubData', 'glClearBufferData', 'glClearBufferSubData',
    'glClearBufferfv', 'glClearBufferiv', 'glClearBufferuiv',
    'glClearNamedBufferData', 'glClearNamedBufferSubData',
    'glClearNamedFramebufferfv', 'glClearNamedFramebufferiv',
    'glClearNamedFramebufferuiv', 'glClearTexImage', 'glClearTexSubImage',
    'glClientWaitSync', 'glCompressedTexImage1D', 'glCompressedTexImage2D',
    'glCompressedTexImage3D', 'glCompressedTexSubImage1D',
    'glCompressedTexSubImage2D', 'glCompressedTexSubImage3D',
    'glCompressedTextureSubImage1D', 'glCompressedTextureSubImage2D',
    'glCompressedTextureSubImage3D', 'glCreateBuffers',
    'glCreateFramebuffers', 'glCreateProgramPipelines', 'glCreateQueries',
    'glCreateRenderbuffers', 'glCreateSamplers', 'glCreateShaderProgramv',
    'glCreateTextures', 'glCreateTransformFeedbacks', 'glCreateVertexArrays',
    'glDebugMessageCallback', 'glDebugMessageControl',
    'glDebugMessageInsert', 'glDeleteBuffers', 'glDeleteFramebuffers',
    'glDeleteProgramPipelines', 'glDeleteQueries', 'glDeleteRenderbuffers',
    'glDeleteSamplers', 'glDeleteSync', 'glDeleteTextures',
    'glDeleteTransformFeedbacks', 'glDeleteVertexArrays',
    'glDepthRangeArrayv', 'glDrawArraysIndirect', 'glDrawBuffers',
    'glDrawElements', 'glDrawElementsBaseVertex', 'glDrawElementsIndirect',
    'glDrawElementsInstanced', 'glDrawElementsInstancedBaseInstance',
    'glDrawElementsInstancedBaseVertex',
    'glDrawElementsInstancedBaseVertexBaseInstance', 'glDrawRangeElements',
    'glDrawRangeElementsBaseVertex', 'glFenceSync', 'glGenBuffers',
    'glGenFramebuffers', 'glGenProgramPipelines', 'glGenQueries',
    'glGenRenderbuffers', 'glGenSamplers', 'glGenTextures',
    'glGenTransformFeedbacks', 'glGenVertexArrays',
    'glGetActiveAtomicCounterBufferiv', 'glGetActiveAttrib',
    'glGetActiveSubroutineName', 'glGetActiveSubroutineUniformName',
    'glGetActiveSubroutineUniformiv', 'glGetActiveUniform',
    'glGetActiveUniformBlockName', 'glGetActiveUniformBlockiv',
    'glGetActiveUniformName', 'glGetActiveUniformsiv',
    'glGetAttachedShaders', 'glGetAttribLocation', 'glGetBooleani_v',
    'glGetBooleanv', 'glGetBufferParameteri64v', 'glGetBufferParameteriv',
    'glGetBufferPointerv', 'glGetBufferSubData', 'glGetCompressedTexImage',
    'glGetCompressedTextureImage', 'glGetCompressedTextureSubImage',
    'glGetDebugMessageLog', 'glGetDoublei_v', 'glGetDoublev',
    'glGetFloati_v', 'glGetFloatv', 'glGetFragDataIndex',
    'glGetFragDataLocation', 'glGetFramebufferAttachmentParameteriv',
    'glGetFramebufferParameteriv', 'glGetInteger64i_v', 'glGetInteger64v',
    'glGetIntegeri_v', 'glGetIntegerv', 'glGetInternalformati64v',
    'glGetInternalformativ', 'glGetMultisamplefv',
    'glGetNamedBufferParameteri64v', 'glGetNamedBufferParameteriv',
    'glGetNamedBufferPointerv', 'glGetNamedBufferSubData',
    'glGetNamedFramebufferAttachmentParameteriv',
    'glGetNamedFramebufferParameteriv', 'glGetNamedRenderbufferParameteriv',
    'glGetObjectLabel', 'glGetObjectPtrLabel', 'glGetProgramBinary',
    'glGetProgramInfoLog', 'glGetProgramInterfaceiv',
    'glGetProgramPipelineInfoLog', 'glGetProgramPipelineiv',
    'glGetProgramResourceIndex', 'glGetProgramResourceLocation',
    'glGetProgramResourceLocationIndex', 'glGetProgramResourceName',
    'glGetProgramResourceiv', 'glGetProgramStageiv', 'glGetProgramiv',
    'glGetQueryIndexediv', 'glGetQueryObjecti64v', 'glGetQueryObjectiv',
    'glGetQueryObjectui64v', 'glGetQueryObjectuiv', 'glGetQueryiv',
    'glGetRenderbufferParameteriv', 'glGetSamplerParameterIiv',
    'glGetSamplerParameterIuiv', 'glGetSamplerParameterfv',
    'glGetSamplerParameteriv', 'glGetShaderInfoLog',
    'glGetShaderPrecisionFormat', 'glGetShaderSource', 'glGetShaderiv',
    'glGetString', 'glGetStringi', 'glGetSubroutineIndex',
    'glGetSubroutineUniformLocation', 'glGetSynciv', 'glGetTexImage',
    'glGetTexLevelParameterfv', 'glGetTexLevelParameteriv',
    'glGetTexParameterIiv', 'glGetTexParameterIuiv', 'glGetTexParameterfv',
    'glGetTexParameteriv', 'glGetTextureImage',
    'glGetTextureLevelParameterfv', 'glGetTextureLevelParameteriv',
    'glGetTextureParameterIiv', 'glGetTextureParameterIuiv',
    'glGetTextureParameterfv', 'glGetTextureParameteriv',
    'glGetTextureSubImage', 'glGetTransformFeedbackVarying',
    'glGetTransformFeedbacki64_v', 'glGetTransformFeedbacki_v',
    'glGetTransformFeedbackiv', 'glGetUniformBlockIndex',
    'glGetUniformIndices', 'glGetUniformLocation',
    'glGetUniformSubroutineuiv', 'glGetUniformdv', 'glGetUniformfv',
    'glGetUniformiv', 'glGetUniformuiv', 'glGetVertexArrayIndexed64iv',
    'glGetVertexArrayIndexediv', 'glGetVertexArrayiv',
    'glGetVertexAttribIiv', 'glGetVertexAttribIuiv', 'glGetVertexAttribLdv',
    'glGetVertexAttribPointerv', 'glGetVertexAttribdv',
    'glGetVertexAttribfv', 'glGetVertexAttribiv', 'glGetnCompressedTexImage',
    'glGetnTexImage', 'glGetnUniformdv', 'glGetnUniformfv',
    'glGetnUniformiv', 'glGetnUniformuiv', 'glInvalidateFramebuffer',
    'glInvalidateNamedFramebufferData',
    'glInvalidateNamedFramebufferSubData', 'glInvalidateSubFramebuffer',
    'glIsSync', 'glMapBuffer', 'glMapBufferRange', 'glMapNamedBuffer',
    'glMapNamedBufferRange', 'glMultiDrawArrays',
    'glMultiDrawArraysIndirect', 'glMultiDrawElements',
    'glMultiDrawElementsBaseVertex', 'glMultiDrawElementsIndirect',
    'glNamedBufferData', 'glNamedBufferStorage', 'glNamedBufferSubData',
    'glNamedFramebufferDrawBuffers', 'glObjectLabel', 'glObjectPtrLabel',
    'glPatchParameterfv', 'glPointParameterfv', 'glPointParameteriv',
    'glProgramBinary', 'glProgramUniform1dv', 'glProgramUniform1fv',
    'glProgramUniform1iv', 'glProgramUniform1uiv', 'glProgramUniform2dv',
    'glProgramUniform2fv', 'glProgramUniform2iv', 'glProgramUniform2uiv',
    'glProgramUniform3dv', 'glProgramUniform3fv', 'glProgramUniform3iv',
    'glProgramUniform3uiv', 'glProgramUniform4dv', 'glProgramUniform4fv',
    'glProgramUniform4iv', 'glProgramUniform4uiv',
    'glProgramUniformMatrix2dv', 'glProgramUniformMatrix2fv',
    'glProgramUniformMatrix2x3dv', 'glProgramUniformMatrix2x3fv',
    'glProgramUniformMatrix2x4dv', 'glProgramUniformMatrix2x4fv',
    'glProgramUniformMatrix3dv', 'glProgramUniformMatrix3fv',
    'glProgramUniformMatrix3x2dv', 'glProgramUniformMatrix3x2fv',
    'glProgramUniformMatrix3x4dv', 'glProgramUniformMatrix3x4fv',
    'glProgramUniformMatrix4dv', 'glProgramUniformMatrix4fv',
    'glProgramUniformMatrix4x2dv', 'glProgramUniformMatrix4x2fv',
    'glProgramUniformMatrix4x3dv', 'glProgramUniformMatrix4x3fv',
    'glPushDebugGroup', 'glReadPixels', 'glReadnPixels',
    'glSamplerParameterIiv', 'glSamplerParameterIuiv',
    'glSamplerParameterfv', 'glSamplerParameteriv', 'glScissorArrayv',
    'glScissorIndexedv', 'glShaderBinary', 'glShaderSource', 'glTexImage1D',
    'glTexImage2D', 'glTexImage3D', 'glTexParameterIiv',
    'glTexParameterIuiv', 'glTexParameterfv', 'glTexParameteriv',
    'glTexSubImage1D', 'glTexSubImage2D', 'glTexSubImage3D',
    'glTextureParameterIiv', 'glTextureParameterIuiv',
    'glTextureParameterfv', 'glTextureParameteriv', 'glTextureSubImage1D',
    'glTextureSubImage2D', 'glTextureSubImage3D',
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
    'glUniformSubroutinesuiv', 'glVertexArrayVertexBuffers',
    'glVertexAttrib1dv', 'glVertexAttrib1fv', 'glVertexAttrib1sv',
    'glVertexAttrib2dv', 'glVertexAttrib2fv', 'glVertexAttrib2sv',
    'glVertexAttrib3dv', 'glVertexAttrib3fv', 'glVertexAttrib3sv',
    'glVertexAttrib4Nbv', 'glVertexAttrib4Niv', 'glVertexAttrib4Nsv',
    'glVertexAttrib4Nubv', 'glVertexAttrib4Nuiv', 'glVertexAttrib4Nusv',
    'glVertexAttrib4bv', 'glVertexAttrib4dv', 'glVertexAttrib4fv',
    'glVertexAttrib4iv', 'glVertexAttrib4sv', 'glVertexAttrib4ubv',
    'glVertexAttrib4uiv', 'glVertexAttrib4usv', 'glVertexAttribI1iv',
    'glVertexAttribI1uiv', 'glVertexAttribI2iv', 'glVertexAttribI2uiv',
    'glVertexAttribI3iv', 'glVertexAttribI3uiv', 'glVertexAttribI4bv',
    'glVertexAttribI4iv', 'glVertexAttribI4sv', 'glVertexAttribI4ubv',
    'glVertexAttribI4uiv', 'glVertexAttribI4usv', 'glVertexAttribIPointer',
    'glVertexAttribL1dv', 'glVertexAttribL2dv', 'glVertexAttribL3dv',
    'glVertexAttribL4dv', 'glVertexAttribLPointer', 'glVertexAttribP1uiv',
    'glVertexAttribP2uiv', 'glVertexAttribP3uiv', 'glVertexAttribP4uiv',
    'glVertexAttribPointer', 'glViewportArrayv', 'glViewportIndexedfv',
    'glWaitSync', holds a function that raises 'NotImplementedError', and its
    docstring says why.
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
    QOpenGLFunctions_4_5_Core::isContextCompatible(QOpenGLContext *context)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#isContextCompatible

    Parameters
    ----------

    context : Optional[QOpenGLContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QOpenGLFunctions_4_5_Core::isContextCompatible(QOpenGLContext
    #      *context)
    return Rituals.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core19isContextCompatibleEP14QOpen'
        'GLContext',
        CuteMixin._addressOf(context),
    )

  @staticmethod
  def versionProfile() -> QOpenGLVersionProfile:
    """
    Calls Qt's 'QOpenGLVersionProfile
    QOpenGLFunctions_4_5_Core::versionProfile()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#versionProfile

    Returns
    -------

    QOpenGLVersionProfile
      A new cute QOpenGLVersionProfile around the copy Qt gave back. Python
      owns it.
    """
    #  QOpenGLVersionProfile QOpenGLFunctions_4_5_Core::versionProfile()
    address = Rituals.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core14versionProfileEv',
    )
    from . import QOpenGLVersionProfile
    return QOpenGLVersionProfile._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpenGLFunctions_4_5_Core'

  #  A C++ QOpenGLFunctions_4_5_Core Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QOpenGLFunctions_4_5_Core'

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
    'QOpenGLFunctions_4_5_Core::QOpenGLFunctions_4_5_Core()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html
    """
    #  QOpenGLFunctions_4_5_Core::QOpenGLFunctions_4_5_Core()
    self._noteCreation(QOpenGLFunctions_4_5_Core, lambda: Rituals.call(
        'ritual_ZN25QOpenGLFunctions_4_5_CoreC1Ev',
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
    Calls Qt's 'bool QOpenGLFunctions_4_5_Core::initializeOpenGLFunctions()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html
    """
    #  bool QOpenGLFunctions_4_5_Core::initializeOpenGLFunctions()
    ritual = (
        'ritual_ZN25QOpenGLFunctions_4_5_Core25initializeOpenGLFunctionsEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QOpenGLFunctions_4_5_Core25initializeOpenGLFuncti'
          'onsEv')
    return self.uglySide.call(ritual)

  @overload(int, int, int, int)
  def glViewport(self, x: int, y: int, width: int, height: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glViewport(GLint x, GLint y,
    GLsizei width, GLsizei height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glViewport

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
    #  void QOpenGLFunctions_4_5_Core::glViewport(GLint x, GLint y, GLsizei
    #      width, GLsizei height)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core10glViewportEiiii',
        x, y, width, height,
    )

  @overload(float, float)
  def glDepthRange(self, nearVal: float, farVal: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glDepthRange(GLdouble
    nearVal, GLdouble farVal)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glDepthRange

    Parameters
    ----------

    nearVal : float
      Passed on as it is.

    farVal : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glDepthRange(GLdouble nearVal,
    #      GLdouble farVal)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core12glDepthRangeEdd',
        nearVal, farVal,
    )

  @overload(int)
  def glIsEnabled(self, cap: int) -> int:
    """
    Calls Qt's 'GLboolean QOpenGLFunctions_4_5_Core::glIsEnabled(GLenum
    cap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glIsEnabled

    Parameters
    ----------

    cap : int
      Passed on as it is.
    """
    #  GLboolean QOpenGLFunctions_4_5_Core::glIsEnabled(GLenum cap)
    return self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core11glIsEnabledEj', cap,
    )

  def glGetError(self) -> int:
    """
    Calls Qt's 'GLenum QOpenGLFunctions_4_5_Core::glGetError()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glGetError
    """
    #  GLenum QOpenGLFunctions_4_5_Core::glGetError()
    return self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core10glGetErrorEv',
    )

  @overload(int)
  def glReadBuffer(self, src: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glReadBuffer(GLenum src)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glReadBuffer

    Parameters
    ----------

    src : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glReadBuffer(GLenum src)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core12glReadBufferEj', src,
    )

  @overload(int, int)
  def glPixelStorei(self, pname: int, param: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glPixelStorei(GLenum pname,
    GLint param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glPixelStorei

    Parameters
    ----------

    pname : int
      Passed on as it is.

    param : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glPixelStorei(GLenum pname, GLint
    #      param)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core13glPixelStoreiEji',
        pname, param,
    )

  @overload(int, float)
  def glPixelStoref(self, pname: int, param: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glPixelStoref(GLenum pname,
    GLfloat param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glPixelStoref

    Parameters
    ----------

    pname : int
      Passed on as it is.

    param : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glPixelStoref(GLenum pname, GLfloat
    #      param)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core13glPixelStorefEjf',
        pname, param,
    )

  @overload(int)
  def glDepthFunc(self, func: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glDepthFunc(GLenum func)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glDepthFunc

    Parameters
    ----------

    func : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glDepthFunc(GLenum func)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core11glDepthFuncEj', func,
    )

  @overload(int, int, int)
  def glStencilOp(self, fail: int, zfail: int, zpass: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glStencilOp(GLenum fail,
    GLenum zfail, GLenum zpass)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glStencilOp

    Parameters
    ----------

    fail : int
      Passed on as it is.

    zfail : int
      Passed on as it is.

    zpass : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glStencilOp(GLenum fail, GLenum zfail,
    #      GLenum zpass)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core11glStencilOpEjjj',
        fail, zfail, zpass,
    )

  @overload(int, int, int)
  def glStencilFunc(self, func: int, ref: int, mask: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glStencilFunc(GLenum func,
    GLint ref, GLuint mask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glStencilFunc

    Parameters
    ----------

    func : int
      Passed on as it is.

    ref : int
      Passed on as it is.

    mask : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glStencilFunc(GLenum func, GLint ref,
    #      GLuint mask)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core13glStencilFuncEjij',
        func, ref, mask,
    )

  @overload(int)
  def glLogicOp(self, opcode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glLogicOp(GLenum opcode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glLogicOp

    Parameters
    ----------

    opcode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glLogicOp(GLenum opcode)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core9glLogicOpEj', opcode,
    )

  @overload(int, int)
  def glBlendFunc(self, sfactor: int, dfactor: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glBlendFunc(GLenum sfactor,
    GLenum dfactor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glBlendFunc

    Parameters
    ----------

    sfactor : int
      Passed on as it is.

    dfactor : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glBlendFunc(GLenum sfactor, GLenum
    #      dfactor)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core11glBlendFuncEjj',
        sfactor, dfactor,
    )

  def glFlush(self) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glFlush()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glFlush
    """
    #  void QOpenGLFunctions_4_5_Core::glFlush()
    self.uglySide.call('ritual_ZN25QOpenGLFunctions_4_5_Core7glFlushEv')

  def glFinish(self) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glFinish()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glFinish
    """
    #  void QOpenGLFunctions_4_5_Core::glFinish()
    self.uglySide.call('ritual_ZN25QOpenGLFunctions_4_5_Core8glFinishEv')

  @overload(int)
  def glEnable(self, cap: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glEnable(GLenum cap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glEnable

    Parameters
    ----------

    cap : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glEnable(GLenum cap)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core8glEnableEj', cap,
    )

  @overload(int)
  def glDisable(self, cap: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glDisable(GLenum cap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glDisable

    Parameters
    ----------

    cap : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glDisable(GLenum cap)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core9glDisableEj', cap,
    )

  @overload(int)
  def glDepthMask(self, flag: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glDepthMask(GLboolean flag)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glDepthMask

    Parameters
    ----------

    flag : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glDepthMask(GLboolean flag)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core11glDepthMaskEh', flag,
    )

  @overload(int, int, int, int)
  def glColorMask(self, red: int, green: int, blue: int, alpha: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glColorMask(GLboolean red,
    GLboolean green, GLboolean blue, GLboolean alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glColorMask

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
    #  void QOpenGLFunctions_4_5_Core::glColorMask(GLboolean red, GLboolean
    #      green, GLboolean blue, GLboolean alpha)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core11glColorMaskEhhhh',
        red, green, blue, alpha,
    )

  @overload(int)
  def glStencilMask(self, mask: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glStencilMask(GLuint mask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glStencilMask

    Parameters
    ----------

    mask : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glStencilMask(GLuint mask)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core13glStencilMaskEj', mask,
    )

  @overload(float)
  def glClearDepth(self, depth: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glClearDepth(GLdouble
    depth)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glClearDepth

    Parameters
    ----------

    depth : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glClearDepth(GLdouble depth)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core12glClearDepthEd', depth,
    )

  @overload(int)
  def glClearStencil(self, s: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glClearStencil(GLint s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glClearStencil

    Parameters
    ----------

    s : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glClearStencil(GLint s)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core14glClearStencilEi', s,
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
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glClearColor(GLfloat red,
    GLfloat green, GLfloat blue, GLfloat alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glClearColor

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
    #  void QOpenGLFunctions_4_5_Core::glClearColor(GLfloat red, GLfloat
    #      green, GLfloat blue, GLfloat alpha)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core12glClearColorEffff',
        red, green, blue, alpha,
    )

  @overload(int)
  def glClear(self, mask: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glClear(GLbitfield mask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glClear

    Parameters
    ----------

    mask : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glClear(GLbitfield mask)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core7glClearEj', mask,
    )

  @overload(int)
  def glDrawBuffer(self, buf: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glDrawBuffer(GLenum buf)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glDrawBuffer

    Parameters
    ----------

    buf : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glDrawBuffer(GLenum buf)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core12glDrawBufferEj', buf,
    )

  @overload(int, int, int)
  def glTexParameteri(self, target: int, pname: int, param: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glTexParameteri(GLenum
    target, GLenum pname, GLint param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glTexParameteri

    Parameters
    ----------

    target : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    param : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glTexParameteri(GLenum target, GLenum
    #      pname, GLint param)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core15glTexParameteriEjji',
        target, pname, param,
    )

  @overload(int, int, float)
  def glTexParameterf(self, target: int, pname: int, param: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glTexParameterf(GLenum
    target, GLenum pname, GLfloat param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glTexParameterf

    Parameters
    ----------

    target : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    param : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glTexParameterf(GLenum target, GLenum
    #      pname, GLfloat param)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core15glTexParameterfEjjf',
        target, pname, param,
    )

  @overload(int, int, int, int)
  def glScissor(self, x: int, y: int, width: int, height: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glScissor(GLint x, GLint y,
    GLsizei width, GLsizei height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glScissor

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
    #  void QOpenGLFunctions_4_5_Core::glScissor(GLint x, GLint y, GLsizei
    #      width, GLsizei height)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core9glScissorEiiii',
        x, y, width, height,
    )

  @overload(int, int)
  def glPolygonMode(self, face: int, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glPolygonMode(GLenum face,
    GLenum mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glPolygonMode

    Parameters
    ----------

    face : int
      Passed on as it is.

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glPolygonMode(GLenum face, GLenum
    #      mode)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core13glPolygonModeEjj', face, mode,
    )

  @overload(float)
  def glPointSize(self, size: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glPointSize(GLfloat size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glPointSize

    Parameters
    ----------

    size : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glPointSize(GLfloat size)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core11glPointSizeEf', size,
    )

  @overload(float)
  def glLineWidth(self, width: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glLineWidth(GLfloat width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glLineWidth

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glLineWidth(GLfloat width)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core11glLineWidthEf', width,
    )

  @overload(int, int)
  def glHint(self, target: int, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glHint(GLenum target, GLenum
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glHint

    Parameters
    ----------

    target : int
      Passed on as it is.

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glHint(GLenum target, GLenum mode)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core6glHintEjj', target, mode,
    )

  @overload(int)
  def glFrontFace(self, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glFrontFace(GLenum mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glFrontFace

    Parameters
    ----------

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glFrontFace(GLenum mode)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core11glFrontFaceEj', mode,
    )

  @overload(int)
  def glCullFace(self, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glCullFace(GLenum mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glCullFace

    Parameters
    ----------

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glCullFace(GLenum mode)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core10glCullFaceEj', mode,
    )

  @overload(int)
  def glIsTexture(self, texture: int) -> int:
    """
    Calls Qt's 'GLboolean QOpenGLFunctions_4_5_Core::glIsTexture(GLuint
    texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glIsTexture

    Parameters
    ----------

    texture : int
      Passed on as it is.
    """
    #  GLboolean QOpenGLFunctions_4_5_Core::glIsTexture(GLuint texture)
    return self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core11glIsTextureEj', texture,
    )

  @overload(int, int)
  def glBindTexture(self, target: int, texture: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glBindTexture(GLenum target,
    GLuint texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glBindTexture

    Parameters
    ----------

    target : int
      Passed on as it is.

    texture : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glBindTexture(GLenum target, GLuint
    #      texture)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core13glBindTextureEjj',
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
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glCopyTexSubImage2D(GLenum
    target, GLint level, GLint xoffset, GLint yoffset, GLint x, GLint y,
    GLsizei width, GLsizei height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glCopyTexSubImage2D

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
    #  void QOpenGLFunctions_4_5_Core::glCopyTexSubImage2D(GLenum target,
    #      GLint level, GLint xoffset, GLint yoffset, GLint x, GLint y,
    #      GLsizei width, GLsizei height)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core19glCopyTexSubImage2DEjiiiiiii',
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
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glCopyTexSubImage1D(GLenum
    target, GLint level, GLint xoffset, GLint x, GLint y, GLsizei width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glCopyTexSubImage1D

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
    #  void QOpenGLFunctions_4_5_Core::glCopyTexSubImage1D(GLenum target,
    #      GLint level, GLint xoffset, GLint x, GLint y, GLsizei width)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core19glCopyTexSubImage1DEjiiiii',
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
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glCopyTexImage2D(GLenum
    target, GLint level, GLenum internalformat, GLint x, GLint y, GLsizei
    width, GLsizei height, GLint border)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glCopyTexImage2D

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
    #  void QOpenGLFunctions_4_5_Core::glCopyTexImage2D(GLenum target, GLint
    #      level, GLenum internalformat, GLint x, GLint y, GLsizei width,
    #      GLsizei height, GLint border)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core16glCopyTexImage2DEjijiiiii',
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
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glCopyTexImage1D(GLenum
    target, GLint level, GLenum internalformat, GLint x, GLint y, GLsizei
    width, GLint border)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glCopyTexImage1D

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
    #  void QOpenGLFunctions_4_5_Core::glCopyTexImage1D(GLenum target, GLint
    #      level, GLenum internalformat, GLint x, GLint y, GLsizei width,
    #      GLint border)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core16glCopyTexImage1DEjijiiii',
        target, level, internalformat, x, y, width, border,
    )

  @overload(float, float)
  def glPolygonOffset(self, factor: float, units: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glPolygonOffset(GLfloat
    factor, GLfloat units)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glPolygonOffset

    Parameters
    ----------

    factor : float
      Passed on as it is.

    units : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glPolygonOffset(GLfloat factor,
    #      GLfloat units)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core15glPolygonOffsetEff',
        factor, units,
    )

  @overload(int, int, int)
  def glDrawArrays(self, mode: int, first: int, count: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glDrawArrays(GLenum mode,
    GLint first, GLsizei count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glDrawArrays

    Parameters
    ----------

    mode : int
      Passed on as it is.

    first : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glDrawArrays(GLenum mode, GLint first,
    #      GLsizei count)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core12glDrawArraysEjii',
        mode, first, count,
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
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glBlendColor(GLfloat red,
    GLfloat green, GLfloat blue, GLfloat alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glBlendColor

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
    #  void QOpenGLFunctions_4_5_Core::glBlendColor(GLfloat red, GLfloat
    #      green, GLfloat blue, GLfloat alpha)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core12glBlendColorEffff',
        red, green, blue, alpha,
    )

  @overload(int)
  def glBlendEquation(self, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glBlendEquation(GLenum
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glBlendEquation

    Parameters
    ----------

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glBlendEquation(GLenum mode)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core15glBlendEquationEj', mode,
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
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glCopyTexSubImage3D(GLenum
    target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLint
    x, GLint y, GLsizei width, GLsizei height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glCopyTexSubImage3D

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
    #  void QOpenGLFunctions_4_5_Core::glCopyTexSubImage3D(GLenum target,
    #      GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLint x,
    #      GLint y, GLsizei width, GLsizei height)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core19glCopyTexSubImage3DEjiiiiiii'
        'i',
        target, level, xoffset, yoffset, zoffset, x, y, width, height,
    )

  @overload(float, int)
  def glSampleCoverage(self, value: float, invert: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glSampleCoverage(GLfloat
    value, GLboolean invert)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glSampleCoverage

    Parameters
    ----------

    value : float
      Passed on as it is.

    invert : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glSampleCoverage(GLfloat value,
    #      GLboolean invert)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core16glSampleCoverageEfh',
        value, invert,
    )

  @overload(int)
  def glActiveTexture(self, texture: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glActiveTexture(GLenum
    texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glActiveTexture

    Parameters
    ----------

    texture : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glActiveTexture(GLenum texture)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core15glActiveTextureEj', texture,
    )

  @overload(int, int)
  def glPointParameteri(self, pname: int, param: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glPointParameteri(GLenum
    pname, GLint param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glPointParameteri

    Parameters
    ----------

    pname : int
      Passed on as it is.

    param : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glPointParameteri(GLenum pname, GLint
    #      param)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core17glPointParameteriEji',
        pname, param,
    )

  @overload(int, float)
  def glPointParameterf(self, pname: int, param: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glPointParameterf(GLenum
    pname, GLfloat param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glPointParameterf

    Parameters
    ----------

    pname : int
      Passed on as it is.

    param : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glPointParameterf(GLenum pname,
    #      GLfloat param)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core17glPointParameterfEjf',
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
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glBlendFuncSeparate(GLenum
    sfactorRGB, GLenum dfactorRGB, GLenum sfactorAlpha, GLenum
    dfactorAlpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glBlendFuncSeparate

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
    #  void QOpenGLFunctions_4_5_Core::glBlendFuncSeparate(GLenum sfactorRGB,
    #      GLenum dfactorRGB, GLenum sfactorAlpha, GLenum dfactorAlpha)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core19glBlendFuncSeparateEjjjj',
        sfactorRGB, dfactorRGB, sfactorAlpha, dfactorAlpha,
    )

  @overload(int)
  def glUnmapBuffer(self, target: int) -> int:
    """
    Calls Qt's 'GLboolean QOpenGLFunctions_4_5_Core::glUnmapBuffer(GLenum
    target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glUnmapBuffer

    Parameters
    ----------

    target : int
      Passed on as it is.
    """
    #  GLboolean QOpenGLFunctions_4_5_Core::glUnmapBuffer(GLenum target)
    return self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core13glUnmapBufferEj', target,
    )

  @overload(int)
  def glIsBuffer(self, buffer: int) -> int:
    """
    Calls Qt's 'GLboolean QOpenGLFunctions_4_5_Core::glIsBuffer(GLuint
    buffer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glIsBuffer

    Parameters
    ----------

    buffer : int
      Passed on as it is.
    """
    #  GLboolean QOpenGLFunctions_4_5_Core::glIsBuffer(GLuint buffer)
    return self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core10glIsBufferEj', buffer,
    )

  @overload(int, int)
  def glBindBuffer(self, target: int, buffer: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glBindBuffer(GLenum target,
    GLuint buffer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glBindBuffer

    Parameters
    ----------

    target : int
      Passed on as it is.

    buffer : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glBindBuffer(GLenum target, GLuint
    #      buffer)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core12glBindBufferEjj',
        target, buffer,
    )

  @overload(int)
  def glEndQuery(self, target: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glEndQuery(GLenum target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glEndQuery

    Parameters
    ----------

    target : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glEndQuery(GLenum target)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core10glEndQueryEj', target,
    )

  @overload(int, int)
  def glBeginQuery(self, target: int, id: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glBeginQuery(GLenum target,
    GLuint id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glBeginQuery

    Parameters
    ----------

    target : int
      Passed on as it is.

    id : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glBeginQuery(GLenum target, GLuint id)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core12glBeginQueryEjj', target, id,
    )

  @overload(int)
  def glIsQuery(self, id: int) -> int:
    """
    Calls Qt's 'GLboolean QOpenGLFunctions_4_5_Core::glIsQuery(GLuint id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glIsQuery

    Parameters
    ----------

    id : int
      Passed on as it is.
    """
    #  GLboolean QOpenGLFunctions_4_5_Core::glIsQuery(GLuint id)
    return self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core9glIsQueryEj', id,
    )

  @overload(int, int, int, int, int)
  def glVertexAttrib4s(
      self,
      index: int,
      x: int,
      y: int,
      z: int,
      w: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttrib4s(GLuint
    index, GLshort x, GLshort y, GLshort z, GLshort w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glVertexAttrib4s

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
    #  void QOpenGLFunctions_4_5_Core::glVertexAttrib4s(GLuint index, GLshort
    #      x, GLshort y, GLshort z, GLshort w)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core16glVertexAttrib4sEjssss',
        index, x, y, z, w,
    )

  @overload(int, float, float, float, float)
  def glVertexAttrib4f(
      self,
      index: int,
      x: float,
      y: float,
      z: float,
      w: float,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttrib4f(GLuint
    index, GLfloat x, GLfloat y, GLfloat z, GLfloat w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glVertexAttrib4f

    Parameters
    ----------

    index : int
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
    #  void QOpenGLFunctions_4_5_Core::glVertexAttrib4f(GLuint index, GLfloat
    #      x, GLfloat y, GLfloat z, GLfloat w)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core16glVertexAttrib4fEjffff',
        index, x, y, z, w,
    )

  @overload(int, float, float, float, float)
  def glVertexAttrib4d(
      self,
      index: int,
      x: float,
      y: float,
      z: float,
      w: float,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttrib4d(GLuint
    index, GLdouble x, GLdouble y, GLdouble z, GLdouble w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glVertexAttrib4d

    Parameters
    ----------

    index : int
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
    #  void QOpenGLFunctions_4_5_Core::glVertexAttrib4d(GLuint index,
    #      GLdouble x, GLdouble y, GLdouble z, GLdouble w)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core16glVertexAttrib4dEjdddd',
        index, x, y, z, w,
    )

  @overload(int, int, int, int, int)
  def glVertexAttrib4Nub(
      self,
      index: int,
      x: int,
      y: int,
      z: int,
      w: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttrib4Nub(GLuint
    index, GLubyte x, GLubyte y, GLubyte z, GLubyte w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glVertexAttrib4Nub

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
    #  void QOpenGLFunctions_4_5_Core::glVertexAttrib4Nub(GLuint index,
    #      GLubyte x, GLubyte y, GLubyte z, GLubyte w)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core18glVertexAttrib4NubEjhhhh',
        index, x, y, z, w,
    )

  @overload(int, int, int, int)
  def glVertexAttrib3s(self, index: int, x: int, y: int, z: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttrib3s(GLuint
    index, GLshort x, GLshort y, GLshort z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glVertexAttrib3s

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
    """
    #  void QOpenGLFunctions_4_5_Core::glVertexAttrib3s(GLuint index, GLshort
    #      x, GLshort y, GLshort z)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core16glVertexAttrib3sEjsss',
        index, x, y, z,
    )

  @overload(int, float, float, float)
  def glVertexAttrib3f(
      self,
      index: int,
      x: float,
      y: float,
      z: float,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttrib3f(GLuint
    index, GLfloat x, GLfloat y, GLfloat z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glVertexAttrib3f

    Parameters
    ----------

    index : int
      Passed on as it is.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glVertexAttrib3f(GLuint index, GLfloat
    #      x, GLfloat y, GLfloat z)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core16glVertexAttrib3fEjfff',
        index, x, y, z,
    )

  @overload(int, float, float, float)
  def glVertexAttrib3d(
      self,
      index: int,
      x: float,
      y: float,
      z: float,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttrib3d(GLuint
    index, GLdouble x, GLdouble y, GLdouble z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glVertexAttrib3d

    Parameters
    ----------

    index : int
      Passed on as it is.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glVertexAttrib3d(GLuint index,
    #      GLdouble x, GLdouble y, GLdouble z)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core16glVertexAttrib3dEjddd',
        index, x, y, z,
    )

  @overload(int, int, int)
  def glVertexAttrib2s(self, index: int, x: int, y: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttrib2s(GLuint
    index, GLshort x, GLshort y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glVertexAttrib2s

    Parameters
    ----------

    index : int
      Passed on as it is.

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glVertexAttrib2s(GLuint index, GLshort
    #      x, GLshort y)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core16glVertexAttrib2sEjss',
        index, x, y,
    )

  @overload(int, float, float)
  def glVertexAttrib2f(self, index: int, x: float, y: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttrib2f(GLuint
    index, GLfloat x, GLfloat y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glVertexAttrib2f

    Parameters
    ----------

    index : int
      Passed on as it is.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glVertexAttrib2f(GLuint index, GLfloat
    #      x, GLfloat y)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core16glVertexAttrib2fEjff',
        index, x, y,
    )

  @overload(int, float, float)
  def glVertexAttrib2d(self, index: int, x: float, y: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttrib2d(GLuint
    index, GLdouble x, GLdouble y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glVertexAttrib2d

    Parameters
    ----------

    index : int
      Passed on as it is.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glVertexAttrib2d(GLuint index,
    #      GLdouble x, GLdouble y)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core16glVertexAttrib2dEjdd',
        index, x, y,
    )

  @overload(int, int)
  def glVertexAttrib1s(self, index: int, x: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttrib1s(GLuint
    index, GLshort x)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glVertexAttrib1s

    Parameters
    ----------

    index : int
      Passed on as it is.

    x : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glVertexAttrib1s(GLuint index, GLshort
    #      x)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core16glVertexAttrib1sEjs',
        index, x,
    )

  @overload(int, float)
  def glVertexAttrib1f(self, index: int, x: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttrib1f(GLuint
    index, GLfloat x)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glVertexAttrib1f

    Parameters
    ----------

    index : int
      Passed on as it is.

    x : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glVertexAttrib1f(GLuint index, GLfloat
    #      x)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core16glVertexAttrib1fEjf',
        index, x,
    )

  @overload(int, float)
  def glVertexAttrib1d(self, index: int, x: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttrib1d(GLuint
    index, GLdouble x)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glVertexAttrib1d

    Parameters
    ----------

    index : int
      Passed on as it is.

    x : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glVertexAttrib1d(GLuint index,
    #      GLdouble x)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core16glVertexAttrib1dEjd',
        index, x,
    )

  @overload(int)
  def glValidateProgram(self, program: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glValidateProgram(GLuint
    program)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glValidateProgram

    Parameters
    ----------

    program : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glValidateProgram(GLuint program)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core17glValidateProgramEj', program,
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
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glUniform4i(GLint location,
    GLint v0, GLint v1, GLint v2, GLint v3)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glUniform4i

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
    #  void QOpenGLFunctions_4_5_Core::glUniform4i(GLint location, GLint v0,
    #      GLint v1, GLint v2, GLint v3)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core11glUniform4iEiiiii',
        location, v0, v1, v2, v3,
    )

  @overload(int, int, int, int)
  def glUniform3i(self, location: int, v0: int, v1: int, v2: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glUniform3i(GLint location,
    GLint v0, GLint v1, GLint v2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glUniform3i

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
    #  void QOpenGLFunctions_4_5_Core::glUniform3i(GLint location, GLint v0,
    #      GLint v1, GLint v2)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core11glUniform3iEiiii',
        location, v0, v1, v2,
    )

  @overload(int, int, int)
  def glUniform2i(self, location: int, v0: int, v1: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glUniform2i(GLint location,
    GLint v0, GLint v1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glUniform2i

    Parameters
    ----------

    location : int
      Passed on as it is.

    v0 : int
      Passed on as it is.

    v1 : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glUniform2i(GLint location, GLint v0,
    #      GLint v1)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core11glUniform2iEiii',
        location, v0, v1,
    )

  @overload(int, int)
  def glUniform1i(self, location: int, v0: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glUniform1i(GLint location,
    GLint v0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glUniform1i

    Parameters
    ----------

    location : int
      Passed on as it is.

    v0 : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glUniform1i(GLint location, GLint v0)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core11glUniform1iEii', location, v0,
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
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glUniform4f(GLint location,
    GLfloat v0, GLfloat v1, GLfloat v2, GLfloat v3)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glUniform4f

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
    #  void QOpenGLFunctions_4_5_Core::glUniform4f(GLint location, GLfloat
    #      v0, GLfloat v1, GLfloat v2, GLfloat v3)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core11glUniform4fEiffff',
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
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glUniform3f(GLint location,
    GLfloat v0, GLfloat v1, GLfloat v2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glUniform3f

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
    #  void QOpenGLFunctions_4_5_Core::glUniform3f(GLint location, GLfloat
    #      v0, GLfloat v1, GLfloat v2)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core11glUniform3fEifff',
        location, v0, v1, v2,
    )

  @overload(int, float, float)
  def glUniform2f(self, location: int, v0: float, v1: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glUniform2f(GLint location,
    GLfloat v0, GLfloat v1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glUniform2f

    Parameters
    ----------

    location : int
      Passed on as it is.

    v0 : float
      Passed on as it is.

    v1 : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glUniform2f(GLint location, GLfloat
    #      v0, GLfloat v1)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core11glUniform2fEiff',
        location, v0, v1,
    )

  @overload(int, float)
  def glUniform1f(self, location: int, v0: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glUniform1f(GLint location,
    GLfloat v0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glUniform1f

    Parameters
    ----------

    location : int
      Passed on as it is.

    v0 : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glUniform1f(GLint location, GLfloat
    #      v0)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core11glUniform1fEif', location, v0,
    )

  @overload(int)
  def glUseProgram(self, program: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glUseProgram(GLuint
    program)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glUseProgram

    Parameters
    ----------

    program : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glUseProgram(GLuint program)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core12glUseProgramEj', program,
    )

  @overload(int)
  def glLinkProgram(self, program: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glLinkProgram(GLuint
    program)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glLinkProgram

    Parameters
    ----------

    program : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glLinkProgram(GLuint program)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core13glLinkProgramEj', program,
    )

  @overload(int)
  def glIsShader(self, shader: int) -> int:
    """
    Calls Qt's 'GLboolean QOpenGLFunctions_4_5_Core::glIsShader(GLuint
    shader)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glIsShader

    Parameters
    ----------

    shader : int
      Passed on as it is.
    """
    #  GLboolean QOpenGLFunctions_4_5_Core::glIsShader(GLuint shader)
    return self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core10glIsShaderEj', shader,
    )

  @overload(int)
  def glIsProgram(self, program: int) -> int:
    """
    Calls Qt's 'GLboolean QOpenGLFunctions_4_5_Core::glIsProgram(GLuint
    program)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glIsProgram

    Parameters
    ----------

    program : int
      Passed on as it is.
    """
    #  GLboolean QOpenGLFunctions_4_5_Core::glIsProgram(GLuint program)
    return self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core11glIsProgramEj', program,
    )

  @overload(int)
  def glEnableVertexAttribArray(self, index: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_5_Core::glEnableVertexAttribArray(GLuint index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glEnableVertexAttribArray(GLuint
    #      index)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core25glEnableVertexAttribArrayEj',
        index,
    )

  @overload(int)
  def glDisableVertexAttribArray(self, index: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_5_Core::glDisableVertexAttribArray(GLuint index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glDisableVertexAttribArray(GLuint
    #      index)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core26glDisableVertexAttribArrayEj',
        index,
    )

  @overload(int, int)
  def glDetachShader(self, program: int, shader: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glDetachShader(GLuint
    program, GLuint shader)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glDetachShader

    Parameters
    ----------

    program : int
      Passed on as it is.

    shader : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glDetachShader(GLuint program, GLuint
    #      shader)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core14glDetachShaderEjj',
        program, shader,
    )

  @overload(int)
  def glDeleteShader(self, shader: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glDeleteShader(GLuint
    shader)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glDeleteShader

    Parameters
    ----------

    shader : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glDeleteShader(GLuint shader)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core14glDeleteShaderEj', shader,
    )

  @overload(int)
  def glDeleteProgram(self, program: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glDeleteProgram(GLuint
    program)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glDeleteProgram

    Parameters
    ----------

    program : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glDeleteProgram(GLuint program)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core15glDeleteProgramEj', program,
    )

  @overload(int)
  def glCreateShader(self, type: int) -> int:
    """
    Calls Qt's 'GLuint QOpenGLFunctions_4_5_Core::glCreateShader(GLenum
    type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glCreateShader

    Parameters
    ----------

    type : int
      Passed on as it is.
    """
    #  GLuint QOpenGLFunctions_4_5_Core::glCreateShader(GLenum type)
    return self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core14glCreateShaderEj', type,
    )

  def glCreateProgram(self) -> int:
    """
    Calls Qt's 'GLuint QOpenGLFunctions_4_5_Core::glCreateProgram()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glCreateProgram
    """
    #  GLuint QOpenGLFunctions_4_5_Core::glCreateProgram()
    return self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core15glCreateProgramEv',
    )

  @overload(int)
  def glCompileShader(self, shader: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glCompileShader(GLuint
    shader)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glCompileShader

    Parameters
    ----------

    shader : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glCompileShader(GLuint shader)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core15glCompileShaderEj', shader,
    )

  @overload(int, int)
  def glAttachShader(self, program: int, shader: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glAttachShader(GLuint
    program, GLuint shader)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glAttachShader

    Parameters
    ----------

    program : int
      Passed on as it is.

    shader : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glAttachShader(GLuint program, GLuint
    #      shader)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core14glAttachShaderEjj',
        program, shader,
    )

  @overload(int, int)
  def glStencilMaskSeparate(self, face: int, mask: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glStencilMaskSeparate(GLenum
    face, GLuint mask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

    Parameters
    ----------

    face : int
      Passed on as it is.

    mask : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glStencilMaskSeparate(GLenum face,
    #      GLuint mask)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core21glStencilMaskSeparateEjj',
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
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glStencilFuncSeparate(GLenum
    face, GLenum func, GLint ref, GLuint mask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

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
    #  void QOpenGLFunctions_4_5_Core::glStencilFuncSeparate(GLenum face,
    #      GLenum func, GLint ref, GLuint mask)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core21glStencilFuncSeparateEjjij',
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
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glStencilOpSeparate(GLenum
    face, GLenum sfail, GLenum dpfail, GLenum dppass)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glStencilOpSeparate

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
    #  void QOpenGLFunctions_4_5_Core::glStencilOpSeparate(GLenum face,
    #      GLenum sfail, GLenum dpfail, GLenum dppass)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core19glStencilOpSeparateEjjjj',
        face, sfail, dpfail, dppass,
    )

  @overload(int, int)
  def glBlendEquationSeparate(self, modeRGB: int, modeAlpha: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_5_Core::glBlendEquationSeparate(GLenum modeRGB, GLenum
    modeAlpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

    Parameters
    ----------

    modeRGB : int
      Passed on as it is.

    modeAlpha : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glBlendEquationSeparate(GLenum
    #      modeRGB, GLenum modeAlpha)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core23glBlendEquationSeparateEjj',
        modeRGB, modeAlpha,
    )

  @overload(int)
  def glIsVertexArray(self, array: int) -> int:
    """
    Calls Qt's 'GLboolean QOpenGLFunctions_4_5_Core::glIsVertexArray(GLuint
    array)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glIsVertexArray

    Parameters
    ----------

    array : int
      Passed on as it is.
    """
    #  GLboolean QOpenGLFunctions_4_5_Core::glIsVertexArray(GLuint array)
    return self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core15glIsVertexArrayEj', array,
    )

  @overload(int)
  def glBindVertexArray(self, array: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glBindVertexArray(GLuint
    array)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glBindVertexArray

    Parameters
    ----------

    array : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glBindVertexArray(GLuint array)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core17glBindVertexArrayEj', array,
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
    QOpenGLFunctions_4_5_Core::glFlushMappedBufferRange(GLenum target,
    GLintptr offset, GLsizeiptr length)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

    Parameters
    ----------

    target : int
      Passed on as it is.

    offset : int
      Passed on as it is.

    length : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glFlushMappedBufferRange(GLenum
    #      target, GLintptr offset, GLsizeiptr length)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core24glFlushMappedBufferRangeEjll',
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
    QOpenGLFunctions_4_5_Core::glFramebufferTextureLayer(GLenum target,
    GLenum attachment, GLuint texture, GLint level, GLint layer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

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
    #  void QOpenGLFunctions_4_5_Core::glFramebufferTextureLayer(GLenum
    #      target, GLenum attachment, GLuint texture, GLint level, GLint
    #      layer)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core25glFramebufferTextureLayerEjj'
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
    QOpenGLFunctions_4_5_Core::glRenderbufferStorageMultisample(GLenum
    target, GLsizei samples, GLenum internalformat, GLsizei width, GLsizei
    height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

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
    #      QOpenGLFunctions_4_5_Core::glRenderbufferStorageMultisample(GLenum
    #      target, GLsizei samples, GLenum internalformat, GLsizei width,
    #      GLsizei height)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core32glRenderbufferStorageMultisa'
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
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glBlitFramebuffer(GLint
    srcX0, GLint srcY0, GLint srcX1, GLint srcY1, GLint dstX0, GLint dstY0,
    GLint dstX1, GLint dstY1, GLbitfield mask, GLenum filter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glBlitFramebuffer

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
    #  void QOpenGLFunctions_4_5_Core::glBlitFramebuffer(GLint srcX0, GLint
    #      srcY0, GLint srcX1, GLint srcY1, GLint dstX0, GLint dstY0, GLint
    #      dstX1, GLint dstY1, GLbitfield mask, GLenum filter)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core17glBlitFramebufferEiiiiiiiijj',
        srcX0, srcY0, srcX1, srcY1, dstX0, dstY0, dstX1, dstY1, mask, filter,
    )

  @overload(int)
  def glGenerateMipmap(self, target: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glGenerateMipmap(GLenum
    target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glGenerateMipmap

    Parameters
    ----------

    target : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glGenerateMipmap(GLenum target)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core16glGenerateMipmapEj', target,
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
    QOpenGLFunctions_4_5_Core::glFramebufferRenderbuffer(GLenum target,
    GLenum attachment, GLenum renderbuffertarget, GLuint renderbuffer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

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
    #  void QOpenGLFunctions_4_5_Core::glFramebufferRenderbuffer(GLenum
    #      target, GLenum attachment, GLenum renderbuffertarget, GLuint
    #      renderbuffer)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core25glFramebufferRenderbufferEjj'
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
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glFramebufferTexture3D(GLenum
    target, GLenum attachment, GLenum textarget, GLuint texture, GLint level,
    GLint zoffset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

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
    #  void QOpenGLFunctions_4_5_Core::glFramebufferTexture3D(GLenum target,
    #      GLenum attachment, GLenum textarget, GLuint texture, GLint level,
    #      GLint zoffset)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core22glFramebufferTexture3DEjjjji'
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
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glFramebufferTexture2D(GLenum
    target, GLenum attachment, GLenum textarget, GLuint texture, GLint
    level)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

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
    #  void QOpenGLFunctions_4_5_Core::glFramebufferTexture2D(GLenum target,
    #      GLenum attachment, GLenum textarget, GLuint texture, GLint level)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core22glFramebufferTexture2DEjjjji',
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
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glFramebufferTexture1D(GLenum
    target, GLenum attachment, GLenum textarget, GLuint texture, GLint
    level)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

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
    #  void QOpenGLFunctions_4_5_Core::glFramebufferTexture1D(GLenum target,
    #      GLenum attachment, GLenum textarget, GLuint texture, GLint level)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core22glFramebufferTexture1DEjjjji',
        target, attachment, textarget, texture, level,
    )

  @overload(int)
  def glCheckFramebufferStatus(self, target: int) -> int:
    """
    Calls Qt's 'GLenum
    QOpenGLFunctions_4_5_Core::glCheckFramebufferStatus(GLenum target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

    Parameters
    ----------

    target : int
      Passed on as it is.
    """
    #  GLenum QOpenGLFunctions_4_5_Core::glCheckFramebufferStatus(GLenum
    #      target)
    return self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core24glCheckFramebufferStatusEj',
        target,
    )

  @overload(int, int)
  def glBindFramebuffer(self, target: int, framebuffer: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glBindFramebuffer(GLenum
    target, GLuint framebuffer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glBindFramebuffer

    Parameters
    ----------

    target : int
      Passed on as it is.

    framebuffer : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glBindFramebuffer(GLenum target,
    #      GLuint framebuffer)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core17glBindFramebufferEjj',
        target, framebuffer,
    )

  @overload(int)
  def glIsFramebuffer(self, framebuffer: int) -> int:
    """
    Calls Qt's 'GLboolean QOpenGLFunctions_4_5_Core::glIsFramebuffer(GLuint
    framebuffer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glIsFramebuffer

    Parameters
    ----------

    framebuffer : int
      Passed on as it is.
    """
    #  GLboolean QOpenGLFunctions_4_5_Core::glIsFramebuffer(GLuint
    #      framebuffer)
    return self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core15glIsFramebufferEj',
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
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glRenderbufferStorage(GLenum
    target, GLenum internalformat, GLsizei width, GLsizei height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

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
    #  void QOpenGLFunctions_4_5_Core::glRenderbufferStorage(GLenum target,
    #      GLenum internalformat, GLsizei width, GLsizei height)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core21glRenderbufferStorageEjjii',
        target, internalformat, width, height,
    )

  @overload(int, int)
  def glBindRenderbuffer(self, target: int, renderbuffer: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glBindRenderbuffer(GLenum
    target, GLuint renderbuffer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glBindRenderbuffer

    Parameters
    ----------

    target : int
      Passed on as it is.

    renderbuffer : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glBindRenderbuffer(GLenum target,
    #      GLuint renderbuffer)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core18glBindRenderbufferEjj',
        target, renderbuffer,
    )

  @overload(int)
  def glIsRenderbuffer(self, renderbuffer: int) -> int:
    """
    Calls Qt's 'GLboolean QOpenGLFunctions_4_5_Core::glIsRenderbuffer(GLuint
    renderbuffer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glIsRenderbuffer

    Parameters
    ----------

    renderbuffer : int
      Passed on as it is.
    """
    #  GLboolean QOpenGLFunctions_4_5_Core::glIsRenderbuffer(GLuint
    #      renderbuffer)
    return self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core16glIsRenderbufferEj',
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
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glClearBufferfi(GLenum
    buffer, GLint drawbuffer, GLfloat depth, GLint stencil)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glClearBufferfi

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
    #  void QOpenGLFunctions_4_5_Core::glClearBufferfi(GLenum buffer, GLint
    #      drawbuffer, GLfloat depth, GLint stencil)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core15glClearBufferfiEjifi',
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
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glUniform4ui(GLint location,
    GLuint v0, GLuint v1, GLuint v2, GLuint v3)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glUniform4ui

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
    #  void QOpenGLFunctions_4_5_Core::glUniform4ui(GLint location, GLuint
    #      v0, GLuint v1, GLuint v2, GLuint v3)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core12glUniform4uiEijjjj',
        location, v0, v1, v2, v3,
    )

  @overload(int, int, int, int)
  def glUniform3ui(self, location: int, v0: int, v1: int, v2: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glUniform3ui(GLint location,
    GLuint v0, GLuint v1, GLuint v2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glUniform3ui

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
    #  void QOpenGLFunctions_4_5_Core::glUniform3ui(GLint location, GLuint
    #      v0, GLuint v1, GLuint v2)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core12glUniform3uiEijjj',
        location, v0, v1, v2,
    )

  @overload(int, int, int)
  def glUniform2ui(self, location: int, v0: int, v1: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glUniform2ui(GLint location,
    GLuint v0, GLuint v1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glUniform2ui

    Parameters
    ----------

    location : int
      Passed on as it is.

    v0 : int
      Passed on as it is.

    v1 : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glUniform2ui(GLint location, GLuint
    #      v0, GLuint v1)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core12glUniform2uiEijj',
        location, v0, v1,
    )

  @overload(int, int)
  def glUniform1ui(self, location: int, v0: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glUniform1ui(GLint location,
    GLuint v0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glUniform1ui

    Parameters
    ----------

    location : int
      Passed on as it is.

    v0 : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glUniform1ui(GLint location, GLuint
    #      v0)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core12glUniform1uiEij',
        location, v0,
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
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttribI4ui(GLuint
    index, GLuint x, GLuint y, GLuint z, GLuint w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glVertexAttribI4ui

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
    #  void QOpenGLFunctions_4_5_Core::glVertexAttribI4ui(GLuint index,
    #      GLuint x, GLuint y, GLuint z, GLuint w)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core18glVertexAttribI4uiEjjjjj',
        index, x, y, z, w,
    )

  @overload(int, int, int, int)
  def glVertexAttribI3ui(self, index: int, x: int, y: int, z: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttribI3ui(GLuint
    index, GLuint x, GLuint y, GLuint z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glVertexAttribI3ui

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
    """
    #  void QOpenGLFunctions_4_5_Core::glVertexAttribI3ui(GLuint index,
    #      GLuint x, GLuint y, GLuint z)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core18glVertexAttribI3uiEjjjj',
        index, x, y, z,
    )

  @overload(int, int, int)
  def glVertexAttribI2ui(self, index: int, x: int, y: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttribI2ui(GLuint
    index, GLuint x, GLuint y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glVertexAttribI2ui

    Parameters
    ----------

    index : int
      Passed on as it is.

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glVertexAttribI2ui(GLuint index,
    #      GLuint x, GLuint y)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core18glVertexAttribI2uiEjjj',
        index, x, y,
    )

  @overload(int, int)
  def glVertexAttribI1ui(self, index: int, x: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttribI1ui(GLuint
    index, GLuint x)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glVertexAttribI1ui

    Parameters
    ----------

    index : int
      Passed on as it is.

    x : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glVertexAttribI1ui(GLuint index,
    #      GLuint x)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core18glVertexAttribI1uiEjj',
        index, x,
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
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttribI4i(GLuint
    index, GLint x, GLint y, GLint z, GLint w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glVertexAttribI4i

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
    #  void QOpenGLFunctions_4_5_Core::glVertexAttribI4i(GLuint index, GLint
    #      x, GLint y, GLint z, GLint w)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core17glVertexAttribI4iEjiiii',
        index, x, y, z, w,
    )

  @overload(int, int, int, int)
  def glVertexAttribI3i(self, index: int, x: int, y: int, z: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttribI3i(GLuint
    index, GLint x, GLint y, GLint z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glVertexAttribI3i

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
    """
    #  void QOpenGLFunctions_4_5_Core::glVertexAttribI3i(GLuint index, GLint
    #      x, GLint y, GLint z)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core17glVertexAttribI3iEjiii',
        index, x, y, z,
    )

  @overload(int, int, int)
  def glVertexAttribI2i(self, index: int, x: int, y: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttribI2i(GLuint
    index, GLint x, GLint y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glVertexAttribI2i

    Parameters
    ----------

    index : int
      Passed on as it is.

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glVertexAttribI2i(GLuint index, GLint
    #      x, GLint y)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core17glVertexAttribI2iEjii',
        index, x, y,
    )

  @overload(int, int)
  def glVertexAttribI1i(self, index: int, x: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttribI1i(GLuint
    index, GLint x)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glVertexAttribI1i

    Parameters
    ----------

    index : int
      Passed on as it is.

    x : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glVertexAttribI1i(GLuint index, GLint
    #      x)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core17glVertexAttribI1iEji',
        index, x,
    )

  def glEndConditionalRender(self) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glEndConditionalRender()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html
    """
    #  void QOpenGLFunctions_4_5_Core::glEndConditionalRender()
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core22glEndConditionalRenderEv',
    )

  @overload(int, int)
  def glBeginConditionalRender(self, id: int, mode: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_5_Core::glBeginConditionalRender(GLuint id, GLenum
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

    Parameters
    ----------

    id : int
      Passed on as it is.

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glBeginConditionalRender(GLuint id,
    #      GLenum mode)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core24glBeginConditionalRenderEjj',
        id, mode,
    )

  @overload(int, int)
  def glClampColor(self, target: int, clamp: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glClampColor(GLenum target,
    GLenum clamp)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glClampColor

    Parameters
    ----------

    target : int
      Passed on as it is.

    clamp : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glClampColor(GLenum target, GLenum
    #      clamp)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core12glClampColorEjj',
        target, clamp,
    )

  @overload(int, int, int)
  def glBindBufferBase(self, target: int, index: int, buffer: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glBindBufferBase(GLenum
    target, GLuint index, GLuint buffer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glBindBufferBase

    Parameters
    ----------

    target : int
      Passed on as it is.

    index : int
      Passed on as it is.

    buffer : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glBindBufferBase(GLenum target, GLuint
    #      index, GLuint buffer)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core16glBindBufferBaseEjjj',
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
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glBindBufferRange(GLenum
    target, GLuint index, GLuint buffer, GLintptr offset, GLsizeiptr size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glBindBufferRange

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
    #  void QOpenGLFunctions_4_5_Core::glBindBufferRange(GLenum target,
    #      GLuint index, GLuint buffer, GLintptr offset, GLsizeiptr size)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core17glBindBufferRangeEjjjll',
        target, index, buffer, offset, size,
    )

  def glEndTransformFeedback(self) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glEndTransformFeedback()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html
    """
    #  void QOpenGLFunctions_4_5_Core::glEndTransformFeedback()
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core22glEndTransformFeedbackEv',
    )

  @overload(int)
  def glBeginTransformFeedback(self, primitiveMode: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_5_Core::glBeginTransformFeedback(GLenum
    primitiveMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

    Parameters
    ----------

    primitiveMode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glBeginTransformFeedback(GLenum
    #      primitiveMode)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core24glBeginTransformFeedbackEj',
        primitiveMode,
    )

  @overload(int, int)
  def glIsEnabledi(self, target: int, index: int) -> int:
    """
    Calls Qt's 'GLboolean QOpenGLFunctions_4_5_Core::glIsEnabledi(GLenum
    target, GLuint index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glIsEnabledi

    Parameters
    ----------

    target : int
      Passed on as it is.

    index : int
      Passed on as it is.
    """
    #  GLboolean QOpenGLFunctions_4_5_Core::glIsEnabledi(GLenum target,
    #      GLuint index)
    return self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core12glIsEnablediEjj',
        target, index,
    )

  @overload(int, int)
  def glDisablei(self, target: int, index: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glDisablei(GLenum target,
    GLuint index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glDisablei

    Parameters
    ----------

    target : int
      Passed on as it is.

    index : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glDisablei(GLenum target, GLuint
    #      index)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core10glDisableiEjj', target, index,
    )

  @overload(int, int)
  def glEnablei(self, target: int, index: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glEnablei(GLenum target,
    GLuint index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glEnablei

    Parameters
    ----------

    target : int
      Passed on as it is.

    index : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glEnablei(GLenum target, GLuint index)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core9glEnableiEjj', target, index,
    )

  @overload(int, int, int, int, int)
  def glColorMaski(self, index: int, r: int, g: int, b: int, a: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glColorMaski(GLuint index,
    GLboolean r, GLboolean g, GLboolean b, GLboolean a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glColorMaski

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
    #  void QOpenGLFunctions_4_5_Core::glColorMaski(GLuint index, GLboolean
    #      r, GLboolean g, GLboolean b, GLboolean a)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core12glColorMaskiEjhhhh',
        index, r, g, b, a,
    )

  @overload(int, int, int)
  def glUniformBlockBinding(
      self,
      program: int,
      uniformBlockIndex: int,
      uniformBlockBinding: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glUniformBlockBinding(GLuint
    program, GLuint uniformBlockIndex, GLuint uniformBlockBinding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

    Parameters
    ----------

    program : int
      Passed on as it is.

    uniformBlockIndex : int
      Passed on as it is.

    uniformBlockBinding : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glUniformBlockBinding(GLuint program,
    #      GLuint uniformBlockIndex, GLuint uniformBlockBinding)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core21glUniformBlockBindingEjjj',
        program, uniformBlockIndex, uniformBlockBinding,
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
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glCopyBufferSubData(GLenum
    readTarget, GLenum writeTarget, GLintptr readOffset, GLintptr
    writeOffset, GLsizeiptr size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glCopyBufferSubData

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
    #  void QOpenGLFunctions_4_5_Core::glCopyBufferSubData(GLenum readTarget,
    #      GLenum writeTarget, GLintptr readOffset, GLintptr writeOffset,
    #      GLsizeiptr size)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core19glCopyBufferSubDataEjjlll',
        readTarget, writeTarget, readOffset, writeOffset, size,
    )

  @overload(int)
  def glPrimitiveRestartIndex(self, index: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_5_Core::glPrimitiveRestartIndex(GLuint index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glPrimitiveRestartIndex(GLuint index)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core23glPrimitiveRestartIndexEj',
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
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glTexBuffer(GLenum target,
    GLenum internalformat, GLuint buffer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glTexBuffer

    Parameters
    ----------

    target : int
      Passed on as it is.

    internalformat : int
      Passed on as it is.

    buffer : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glTexBuffer(GLenum target, GLenum
    #      internalformat, GLuint buffer)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core11glTexBufferEjjj',
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
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glDrawArraysInstanced(GLenum
    mode, GLint first, GLsizei count, GLsizei instancecount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

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
    #  void QOpenGLFunctions_4_5_Core::glDrawArraysInstanced(GLenum mode,
    #      GLint first, GLsizei count, GLsizei instancecount)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core21glDrawArraysInstancedEjiii',
        mode, first, count, instancecount,
    )

  @overload(int, int)
  def glSampleMaski(self, maskNumber: int, mask: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glSampleMaski(GLuint
    maskNumber, GLbitfield mask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glSampleMaski

    Parameters
    ----------

    maskNumber : int
      Passed on as it is.

    mask : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glSampleMaski(GLuint maskNumber,
    #      GLbitfield mask)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core13glSampleMaskiEjj',
        maskNumber, mask,
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
    QOpenGLFunctions_4_5_Core::glTexImage3DMultisample(GLenum target, GLsizei
    samples, GLenum internalformat, GLsizei width, GLsizei height, GLsizei
    depth, GLboolean fixedsamplelocations)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

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
    #  void QOpenGLFunctions_4_5_Core::glTexImage3DMultisample(GLenum target,
    #      GLsizei samples, GLenum internalformat, GLsizei width, GLsizei
    #      height, GLsizei depth, GLboolean fixedsamplelocations)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core23glTexImage3DMultisampleEjiji'
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
    QOpenGLFunctions_4_5_Core::glTexImage2DMultisample(GLenum target, GLsizei
    samples, GLenum internalformat, GLsizei width, GLsizei height, GLboolean
    fixedsamplelocations)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

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
    #  void QOpenGLFunctions_4_5_Core::glTexImage2DMultisample(GLenum target,
    #      GLsizei samples, GLenum internalformat, GLsizei width, GLsizei
    #      height, GLboolean fixedsamplelocations)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core23glTexImage2DMultisampleEjiji'
        'ih',
        target, samples, internalformat, width, height, fixedsamplelocations,
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
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glFramebufferTexture(GLenum
    target, GLenum attachment, GLuint texture, GLint level)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

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
    #  void QOpenGLFunctions_4_5_Core::glFramebufferTexture(GLenum target,
    #      GLenum attachment, GLuint texture, GLint level)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core20glFramebufferTextureEjjji',
        target, attachment, texture, level,
    )

  @overload(int)
  def glProvokingVertex(self, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glProvokingVertex(GLenum
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glProvokingVertex

    Parameters
    ----------

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glProvokingVertex(GLenum mode)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core17glProvokingVertexEj', mode,
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
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttribP4ui(GLuint
    index, GLenum type, GLboolean normalized, GLuint value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glVertexAttribP4ui

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
    #  void QOpenGLFunctions_4_5_Core::glVertexAttribP4ui(GLuint index,
    #      GLenum type, GLboolean normalized, GLuint value)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core18glVertexAttribP4uiEjjhj',
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
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttribP3ui(GLuint
    index, GLenum type, GLboolean normalized, GLuint value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glVertexAttribP3ui

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
    #  void QOpenGLFunctions_4_5_Core::glVertexAttribP3ui(GLuint index,
    #      GLenum type, GLboolean normalized, GLuint value)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core18glVertexAttribP3uiEjjhj',
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
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttribP2ui(GLuint
    index, GLenum type, GLboolean normalized, GLuint value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glVertexAttribP2ui

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
    #  void QOpenGLFunctions_4_5_Core::glVertexAttribP2ui(GLuint index,
    #      GLenum type, GLboolean normalized, GLuint value)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core18glVertexAttribP2uiEjjhj',
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
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttribP1ui(GLuint
    index, GLenum type, GLboolean normalized, GLuint value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glVertexAttribP1ui

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
    #  void QOpenGLFunctions_4_5_Core::glVertexAttribP1ui(GLuint index,
    #      GLenum type, GLboolean normalized, GLuint value)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core18glVertexAttribP1uiEjjhj',
        index, type, normalized, value,
    )

  @overload(int, int)
  def glVertexAttribDivisor(self, index: int, divisor: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttribDivisor(GLuint
    index, GLuint divisor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

    Parameters
    ----------

    index : int
      Passed on as it is.

    divisor : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glVertexAttribDivisor(GLuint index,
    #      GLuint divisor)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core21glVertexAttribDivisorEjj',
        index, divisor,
    )

  @overload(int, int)
  def glQueryCounter(self, id: int, target: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glQueryCounter(GLuint id,
    GLenum target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glQueryCounter

    Parameters
    ----------

    id : int
      Passed on as it is.

    target : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glQueryCounter(GLuint id, GLenum
    #      target)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core14glQueryCounterEjj',
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
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glSamplerParameterf(GLuint
    sampler, GLenum pname, GLfloat param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glSamplerParameterf

    Parameters
    ----------

    sampler : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    param : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glSamplerParameterf(GLuint sampler,
    #      GLenum pname, GLfloat param)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core19glSamplerParameterfEjjf',
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
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glSamplerParameteri(GLuint
    sampler, GLenum pname, GLint param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glSamplerParameteri

    Parameters
    ----------

    sampler : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    param : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glSamplerParameteri(GLuint sampler,
    #      GLenum pname, GLint param)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core19glSamplerParameteriEjji',
        sampler, pname, param,
    )

  @overload(int, int)
  def glBindSampler(self, unit: int, sampler: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glBindSampler(GLuint unit,
    GLuint sampler)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glBindSampler

    Parameters
    ----------

    unit : int
      Passed on as it is.

    sampler : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glBindSampler(GLuint unit, GLuint
    #      sampler)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core13glBindSamplerEjj',
        unit, sampler,
    )

  @overload(int)
  def glIsSampler(self, sampler: int) -> int:
    """
    Calls Qt's 'GLboolean QOpenGLFunctions_4_5_Core::glIsSampler(GLuint
    sampler)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glIsSampler

    Parameters
    ----------

    sampler : int
      Passed on as it is.
    """
    #  GLboolean QOpenGLFunctions_4_5_Core::glIsSampler(GLuint sampler)
    return self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core11glIsSamplerEj', sampler,
    )

  @overload(int, int)
  def glEndQueryIndexed(self, target: int, index: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glEndQueryIndexed(GLenum
    target, GLuint index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glEndQueryIndexed

    Parameters
    ----------

    target : int
      Passed on as it is.

    index : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glEndQueryIndexed(GLenum target,
    #      GLuint index)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core17glEndQueryIndexedEjj',
        target, index,
    )

  @overload(int, int, int)
  def glBeginQueryIndexed(self, target: int, index: int, id: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glBeginQueryIndexed(GLenum
    target, GLuint index, GLuint id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glBeginQueryIndexed

    Parameters
    ----------

    target : int
      Passed on as it is.

    index : int
      Passed on as it is.

    id : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glBeginQueryIndexed(GLenum target,
    #      GLuint index, GLuint id)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core19glBeginQueryIndexedEjjj',
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
    QOpenGLFunctions_4_5_Core::glDrawTransformFeedbackStream(GLenum mode,
    GLuint id, GLuint stream)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

    Parameters
    ----------

    mode : int
      Passed on as it is.

    id : int
      Passed on as it is.

    stream : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glDrawTransformFeedbackStream(GLenum
    #      mode, GLuint id, GLuint stream)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core29glDrawTransformFeedbackStrea'
        'mEjjj',
        mode, id, stream,
    )

  @overload(int, int)
  def glDrawTransformFeedback(self, mode: int, id: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_5_Core::glDrawTransformFeedback(GLenum mode, GLuint
    id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

    Parameters
    ----------

    mode : int
      Passed on as it is.

    id : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glDrawTransformFeedback(GLenum mode,
    #      GLuint id)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core23glDrawTransformFeedbackEjj',
        mode, id,
    )

  def glResumeTransformFeedback(self) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glResumeTransformFeedback()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html
    """
    #  void QOpenGLFunctions_4_5_Core::glResumeTransformFeedback()
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core25glResumeTransformFeedbackEv',
    )

  def glPauseTransformFeedback(self) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glPauseTransformFeedback()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html
    """
    #  void QOpenGLFunctions_4_5_Core::glPauseTransformFeedback()
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core24glPauseTransformFeedbackEv',
    )

  @overload(int)
  def glIsTransformFeedback(self, id: int) -> int:
    """
    Calls Qt's 'GLboolean
    QOpenGLFunctions_4_5_Core::glIsTransformFeedback(GLuint id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

    Parameters
    ----------

    id : int
      Passed on as it is.
    """
    #  GLboolean QOpenGLFunctions_4_5_Core::glIsTransformFeedback(GLuint id)
    return self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core21glIsTransformFeedbackEj', id,
    )

  @overload(int, int)
  def glBindTransformFeedback(self, target: int, id: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_5_Core::glBindTransformFeedback(GLenum target, GLuint
    id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

    Parameters
    ----------

    target : int
      Passed on as it is.

    id : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glBindTransformFeedback(GLenum target,
    #      GLuint id)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core23glBindTransformFeedbackEjj',
        target, id,
    )

  @overload(int, int)
  def glPatchParameteri(self, pname: int, value: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glPatchParameteri(GLenum
    pname, GLint value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glPatchParameteri

    Parameters
    ----------

    pname : int
      Passed on as it is.

    value : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glPatchParameteri(GLenum pname, GLint
    #      value)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core17glPatchParameteriEji',
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
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glUniform4d(GLint location,
    GLdouble x, GLdouble y, GLdouble z, GLdouble w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glUniform4d

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
    #  void QOpenGLFunctions_4_5_Core::glUniform4d(GLint location, GLdouble
    #      x, GLdouble y, GLdouble z, GLdouble w)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core11glUniform4dEidddd',
        location, x, y, z, w,
    )

  @overload(int, float, float, float)
  def glUniform3d(self, location: int, x: float, y: float, z: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glUniform3d(GLint location,
    GLdouble x, GLdouble y, GLdouble z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glUniform3d

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
    #  void QOpenGLFunctions_4_5_Core::glUniform3d(GLint location, GLdouble
    #      x, GLdouble y, GLdouble z)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core11glUniform3dEiddd',
        location, x, y, z,
    )

  @overload(int, float, float)
  def glUniform2d(self, location: int, x: float, y: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glUniform2d(GLint location,
    GLdouble x, GLdouble y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glUniform2d

    Parameters
    ----------

    location : int
      Passed on as it is.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glUniform2d(GLint location, GLdouble
    #      x, GLdouble y)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core11glUniform2dEidd',
        location, x, y,
    )

  @overload(int, float)
  def glUniform1d(self, location: int, x: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glUniform1d(GLint location,
    GLdouble x)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glUniform1d

    Parameters
    ----------

    location : int
      Passed on as it is.

    x : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glUniform1d(GLint location, GLdouble
    #      x)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core11glUniform1dEid', location, x,
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
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glBlendFuncSeparatei(GLuint
    buf, GLenum srcRGB, GLenum dstRGB, GLenum srcAlpha, GLenum dstAlpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

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
    #  void QOpenGLFunctions_4_5_Core::glBlendFuncSeparatei(GLuint buf,
    #      GLenum srcRGB, GLenum dstRGB, GLenum srcAlpha, GLenum dstAlpha)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core20glBlendFuncSeparateiEjjjjj',
        buf, srcRGB, dstRGB, srcAlpha, dstAlpha,
    )

  @overload(int, int, int)
  def glBlendFunci(self, buf: int, src: int, dst: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glBlendFunci(GLuint buf,
    GLenum src, GLenum dst)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glBlendFunci

    Parameters
    ----------

    buf : int
      Passed on as it is.

    src : int
      Passed on as it is.

    dst : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glBlendFunci(GLuint buf, GLenum src,
    #      GLenum dst)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core12glBlendFunciEjjj',
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
    QOpenGLFunctions_4_5_Core::glBlendEquationSeparatei(GLuint buf, GLenum
    modeRGB, GLenum modeAlpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

    Parameters
    ----------

    buf : int
      Passed on as it is.

    modeRGB : int
      Passed on as it is.

    modeAlpha : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glBlendEquationSeparatei(GLuint buf,
    #      GLenum modeRGB, GLenum modeAlpha)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core24glBlendEquationSeparateiEjjj',
        buf, modeRGB, modeAlpha,
    )

  @overload(int, int)
  def glBlendEquationi(self, buf: int, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glBlendEquationi(GLuint buf,
    GLenum mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glBlendEquationi

    Parameters
    ----------

    buf : int
      Passed on as it is.

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glBlendEquationi(GLuint buf, GLenum
    #      mode)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core16glBlendEquationiEjj',
        buf, mode,
    )

  @overload(float)
  def glMinSampleShading(self, value: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glMinSampleShading(GLfloat
    value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glMinSampleShading

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glMinSampleShading(GLfloat value)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core18glMinSampleShadingEf', value,
    )

  @overload(int, float, float)
  def glDepthRangeIndexed(self, index: int, n: float, f: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glDepthRangeIndexed(GLuint
    index, GLdouble n, GLdouble f)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glDepthRangeIndexed

    Parameters
    ----------

    index : int
      Passed on as it is.

    n : float
      Passed on as it is.

    f : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glDepthRangeIndexed(GLuint index,
    #      GLdouble n, GLdouble f)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core19glDepthRangeIndexedEjdd',
        index, n, f,
    )

  @overload(int, int, int, int, int)
  def glScissorIndexed(
      self,
      index: int,
      left: int,
      bottom: int,
      width: int,
      height: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glScissorIndexed(GLuint
    index, GLint left, GLint bottom, GLsizei width, GLsizei height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glScissorIndexed

    Parameters
    ----------

    index : int
      Passed on as it is.

    left : int
      Passed on as it is.

    bottom : int
      Passed on as it is.

    width : int
      Passed on as it is.

    height : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glScissorIndexed(GLuint index, GLint
    #      left, GLint bottom, GLsizei width, GLsizei height)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core16glScissorIndexedEjiiii',
        index, left, bottom, width, height,
    )

  @overload(int, float, float, float, float)
  def glViewportIndexedf(
      self,
      index: int,
      x: float,
      y: float,
      w: float,
      h: float,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glViewportIndexedf(GLuint
    index, GLfloat x, GLfloat y, GLfloat w, GLfloat h)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glViewportIndexedf

    Parameters
    ----------

    index : int
      Passed on as it is.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    w : float
      Passed on as it is.

    h : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glViewportIndexedf(GLuint index,
    #      GLfloat x, GLfloat y, GLfloat w, GLfloat h)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core18glViewportIndexedfEjffff',
        index, x, y, w, h,
    )

  @overload(int, float, float, float, float)
  def glVertexAttribL4d(
      self,
      index: int,
      x: float,
      y: float,
      z: float,
      w: float,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttribL4d(GLuint
    index, GLdouble x, GLdouble y, GLdouble z, GLdouble w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glVertexAttribL4d

    Parameters
    ----------

    index : int
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
    #  void QOpenGLFunctions_4_5_Core::glVertexAttribL4d(GLuint index,
    #      GLdouble x, GLdouble y, GLdouble z, GLdouble w)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core17glVertexAttribL4dEjdddd',
        index, x, y, z, w,
    )

  @overload(int, float, float, float)
  def glVertexAttribL3d(
      self,
      index: int,
      x: float,
      y: float,
      z: float,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttribL3d(GLuint
    index, GLdouble x, GLdouble y, GLdouble z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glVertexAttribL3d

    Parameters
    ----------

    index : int
      Passed on as it is.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glVertexAttribL3d(GLuint index,
    #      GLdouble x, GLdouble y, GLdouble z)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core17glVertexAttribL3dEjddd',
        index, x, y, z,
    )

  @overload(int, float, float)
  def glVertexAttribL2d(self, index: int, x: float, y: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttribL2d(GLuint
    index, GLdouble x, GLdouble y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glVertexAttribL2d

    Parameters
    ----------

    index : int
      Passed on as it is.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glVertexAttribL2d(GLuint index,
    #      GLdouble x, GLdouble y)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core17glVertexAttribL2dEjdd',
        index, x, y,
    )

  @overload(int, float)
  def glVertexAttribL1d(self, index: int, x: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttribL1d(GLuint
    index, GLdouble x)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glVertexAttribL1d

    Parameters
    ----------

    index : int
      Passed on as it is.

    x : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glVertexAttribL1d(GLuint index,
    #      GLdouble x)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core17glVertexAttribL1dEjd',
        index, x,
    )

  @overload(int)
  def glValidateProgramPipeline(self, pipeline: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_5_Core::glValidateProgramPipeline(GLuint pipeline)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

    Parameters
    ----------

    pipeline : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glValidateProgramPipeline(GLuint
    #      pipeline)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core25glValidateProgramPipelineEj',
        pipeline,
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
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniform4ui(GLuint
    program, GLint location, GLuint v0, GLuint v1, GLuint v2, GLuint v3)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glProgramUniform4ui

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
    #  void QOpenGLFunctions_4_5_Core::glProgramUniform4ui(GLuint program,
    #      GLint location, GLuint v0, GLuint v1, GLuint v2, GLuint v3)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core19glProgramUniform4uiEjijjjj',
        program, location, v0, v1, v2, v3,
    )

  @overload(int, int, float, float, float, float)
  def glProgramUniform4d(
      self,
      program: int,
      location: int,
      v0: float,
      v1: float,
      v2: float,
      v3: float,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniform4d(GLuint
    program, GLint location, GLdouble v0, GLdouble v1, GLdouble v2, GLdouble
    v3)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glProgramUniform4d

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
    #  void QOpenGLFunctions_4_5_Core::glProgramUniform4d(GLuint program,
    #      GLint location, GLdouble v0, GLdouble v1, GLdouble v2, GLdouble
    #      v3)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core18glProgramUniform4dEjidddd',
        program, location, v0, v1, v2, v3,
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
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniform4f(GLuint
    program, GLint location, GLfloat v0, GLfloat v1, GLfloat v2, GLfloat
    v3)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glProgramUniform4f

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
    #  void QOpenGLFunctions_4_5_Core::glProgramUniform4f(GLuint program,
    #      GLint location, GLfloat v0, GLfloat v1, GLfloat v2, GLfloat v3)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core18glProgramUniform4fEjiffff',
        program, location, v0, v1, v2, v3,
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
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniform4i(GLuint
    program, GLint location, GLint v0, GLint v1, GLint v2, GLint v3)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glProgramUniform4i

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
    #  void QOpenGLFunctions_4_5_Core::glProgramUniform4i(GLuint program,
    #      GLint location, GLint v0, GLint v1, GLint v2, GLint v3)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core18glProgramUniform4iEjiiiii',
        program, location, v0, v1, v2, v3,
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
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniform3ui(GLuint
    program, GLint location, GLuint v0, GLuint v1, GLuint v2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glProgramUniform3ui

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
    #  void QOpenGLFunctions_4_5_Core::glProgramUniform3ui(GLuint program,
    #      GLint location, GLuint v0, GLuint v1, GLuint v2)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core19glProgramUniform3uiEjijjj',
        program, location, v0, v1, v2,
    )

  @overload(int, int, float, float, float)
  def glProgramUniform3d(
      self,
      program: int,
      location: int,
      v0: float,
      v1: float,
      v2: float,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniform3d(GLuint
    program, GLint location, GLdouble v0, GLdouble v1, GLdouble v2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glProgramUniform3d

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
    #  void QOpenGLFunctions_4_5_Core::glProgramUniform3d(GLuint program,
    #      GLint location, GLdouble v0, GLdouble v1, GLdouble v2)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core18glProgramUniform3dEjiddd',
        program, location, v0, v1, v2,
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
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniform3f(GLuint
    program, GLint location, GLfloat v0, GLfloat v1, GLfloat v2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glProgramUniform3f

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
    #  void QOpenGLFunctions_4_5_Core::glProgramUniform3f(GLuint program,
    #      GLint location, GLfloat v0, GLfloat v1, GLfloat v2)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core18glProgramUniform3fEjifff',
        program, location, v0, v1, v2,
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
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniform3i(GLuint
    program, GLint location, GLint v0, GLint v1, GLint v2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glProgramUniform3i

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
    #  void QOpenGLFunctions_4_5_Core::glProgramUniform3i(GLuint program,
    #      GLint location, GLint v0, GLint v1, GLint v2)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core18glProgramUniform3iEjiiii',
        program, location, v0, v1, v2,
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
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniform2ui(GLuint
    program, GLint location, GLuint v0, GLuint v1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glProgramUniform2ui

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
    #  void QOpenGLFunctions_4_5_Core::glProgramUniform2ui(GLuint program,
    #      GLint location, GLuint v0, GLuint v1)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core19glProgramUniform2uiEjijj',
        program, location, v0, v1,
    )

  @overload(int, int, float, float)
  def glProgramUniform2d(
      self,
      program: int,
      location: int,
      v0: float,
      v1: float,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniform2d(GLuint
    program, GLint location, GLdouble v0, GLdouble v1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glProgramUniform2d

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
    #  void QOpenGLFunctions_4_5_Core::glProgramUniform2d(GLuint program,
    #      GLint location, GLdouble v0, GLdouble v1)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core18glProgramUniform2dEjidd',
        program, location, v0, v1,
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
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniform2f(GLuint
    program, GLint location, GLfloat v0, GLfloat v1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glProgramUniform2f

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
    #  void QOpenGLFunctions_4_5_Core::glProgramUniform2f(GLuint program,
    #      GLint location, GLfloat v0, GLfloat v1)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core18glProgramUniform2fEjiff',
        program, location, v0, v1,
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
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniform2i(GLuint
    program, GLint location, GLint v0, GLint v1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glProgramUniform2i

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
    #  void QOpenGLFunctions_4_5_Core::glProgramUniform2i(GLuint program,
    #      GLint location, GLint v0, GLint v1)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core18glProgramUniform2iEjiii',
        program, location, v0, v1,
    )

  @overload(int, int, int)
  def glProgramUniform1ui(
      self,
      program: int,
      location: int,
      v0: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniform1ui(GLuint
    program, GLint location, GLuint v0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glProgramUniform1ui

    Parameters
    ----------

    program : int
      Passed on as it is.

    location : int
      Passed on as it is.

    v0 : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glProgramUniform1ui(GLuint program,
    #      GLint location, GLuint v0)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core19glProgramUniform1uiEjij',
        program, location, v0,
    )

  @overload(int, int, float)
  def glProgramUniform1d(
      self,
      program: int,
      location: int,
      v0: float,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniform1d(GLuint
    program, GLint location, GLdouble v0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glProgramUniform1d

    Parameters
    ----------

    program : int
      Passed on as it is.

    location : int
      Passed on as it is.

    v0 : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glProgramUniform1d(GLuint program,
    #      GLint location, GLdouble v0)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core18glProgramUniform1dEjid',
        program, location, v0,
    )

  @overload(int, int, float)
  def glProgramUniform1f(
      self,
      program: int,
      location: int,
      v0: float,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniform1f(GLuint
    program, GLint location, GLfloat v0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glProgramUniform1f

    Parameters
    ----------

    program : int
      Passed on as it is.

    location : int
      Passed on as it is.

    v0 : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glProgramUniform1f(GLuint program,
    #      GLint location, GLfloat v0)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core18glProgramUniform1fEjif',
        program, location, v0,
    )

  @overload(int, int, int)
  def glProgramUniform1i(self, program: int, location: int, v0: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniform1i(GLuint
    program, GLint location, GLint v0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glProgramUniform1i

    Parameters
    ----------

    program : int
      Passed on as it is.

    location : int
      Passed on as it is.

    v0 : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glProgramUniform1i(GLuint program,
    #      GLint location, GLint v0)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core18glProgramUniform1iEjii',
        program, location, v0,
    )

  @overload(int)
  def glIsProgramPipeline(self, pipeline: int) -> int:
    """
    Calls Qt's 'GLboolean
    QOpenGLFunctions_4_5_Core::glIsProgramPipeline(GLuint pipeline)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glIsProgramPipeline

    Parameters
    ----------

    pipeline : int
      Passed on as it is.
    """
    #  GLboolean QOpenGLFunctions_4_5_Core::glIsProgramPipeline(GLuint
    #      pipeline)
    return self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core19glIsProgramPipelineEj',
        pipeline,
    )

  @overload(int)
  def glBindProgramPipeline(self, pipeline: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glBindProgramPipeline(GLuint
    pipeline)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

    Parameters
    ----------

    pipeline : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glBindProgramPipeline(GLuint pipeline)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core21glBindProgramPipelineEj',
        pipeline,
    )

  @overload(int, int)
  def glActiveShaderProgram(self, pipeline: int, program: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glActiveShaderProgram(GLuint
    pipeline, GLuint program)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

    Parameters
    ----------

    pipeline : int
      Passed on as it is.

    program : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glActiveShaderProgram(GLuint pipeline,
    #      GLuint program)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core21glActiveShaderProgramEjj',
        pipeline, program,
    )

  @overload(int, int, int)
  def glUseProgramStages(
      self,
      pipeline: int,
      stages: int,
      program: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glUseProgramStages(GLuint
    pipeline, GLbitfield stages, GLuint program)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glUseProgramStages

    Parameters
    ----------

    pipeline : int
      Passed on as it is.

    stages : int
      Passed on as it is.

    program : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glUseProgramStages(GLuint pipeline,
    #      GLbitfield stages, GLuint program)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core18glUseProgramStagesEjjj',
        pipeline, stages, program,
    )

  @overload(int, int, int)
  def glProgramParameteri(
      self,
      program: int,
      pname: int,
      value: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glProgramParameteri(GLuint
    program, GLenum pname, GLint value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glProgramParameteri

    Parameters
    ----------

    program : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    value : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glProgramParameteri(GLuint program,
    #      GLenum pname, GLint value)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core19glProgramParameteriEjji',
        program, pname, value,
    )

  @overload(float)
  def glClearDepthf(self, dd: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glClearDepthf(GLfloat dd)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glClearDepthf

    Parameters
    ----------

    dd : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glClearDepthf(GLfloat dd)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core13glClearDepthfEf', dd,
    )

  @overload(float, float)
  def glDepthRangef(self, n: float, f: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glDepthRangef(GLfloat n,
    GLfloat f)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glDepthRangef

    Parameters
    ----------

    n : float
      Passed on as it is.

    f : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glDepthRangef(GLfloat n, GLfloat f)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core13glDepthRangefEff', n, f,
    )

  def glReleaseShaderCompiler(self) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glReleaseShaderCompiler()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html
    """
    #  void QOpenGLFunctions_4_5_Core::glReleaseShaderCompiler()
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core23glReleaseShaderCompilerEv',
    )

  @overload(int, int, int, int)
  def glDrawTransformFeedbackStreamInstanced(
      self,
      mode: int,
      id: int,
      stream: int,
      instancecount: int,
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_5_Core::glDrawTransformFeedbackStreamInstanced(GLenum
    mode, GLuint id, GLuint stream, GLsizei instancecount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

    Parameters
    ----------

    mode : int
      Passed on as it is.

    id : int
      Passed on as it is.

    stream : int
      Passed on as it is.

    instancecount : int
      Passed on as it is.
    """
    #  void
    #      QOpenGLFunctions_4_5_Core::glDrawTransformFeedbackStreamInstanced(
    #      GLenum mode, GLuint id, GLuint stream, GLsizei instancecount)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core38glDrawTransformFeedbackStrea'
        'mInstancedEjjji',
        mode, id, stream, instancecount,
    )

  @overload(int, int, int)
  def glDrawTransformFeedbackInstanced(
      self,
      mode: int,
      id: int,
      instancecount: int,
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_5_Core::glDrawTransformFeedbackInstanced(GLenum mode,
    GLuint id, GLsizei instancecount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

    Parameters
    ----------

    mode : int
      Passed on as it is.

    id : int
      Passed on as it is.

    instancecount : int
      Passed on as it is.
    """
    #  void
    #      QOpenGLFunctions_4_5_Core::glDrawTransformFeedbackInstanced(GLenum
    #      mode, GLuint id, GLsizei instancecount)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core32glDrawTransformFeedbackInsta'
        'ncedEjji',
        mode, id, instancecount,
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
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glTexStorage3D(GLenum target,
    GLsizei levels, GLenum internalformat, GLsizei width, GLsizei height,
    GLsizei depth)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glTexStorage3D

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
    #  void QOpenGLFunctions_4_5_Core::glTexStorage3D(GLenum target, GLsizei
    #      levels, GLenum internalformat, GLsizei width, GLsizei height,
    #      GLsizei depth)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core14glTexStorage3DEjijiii',
        target, levels, internalformat, width, height, depth,
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
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glTexStorage2D(GLenum target,
    GLsizei levels, GLenum internalformat, GLsizei width, GLsizei height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glTexStorage2D

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
    #  void QOpenGLFunctions_4_5_Core::glTexStorage2D(GLenum target, GLsizei
    #      levels, GLenum internalformat, GLsizei width, GLsizei height)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core14glTexStorage2DEjijii',
        target, levels, internalformat, width, height,
    )

  @overload(int, int, int, int)
  def glTexStorage1D(
      self,
      target: int,
      levels: int,
      internalformat: int,
      width: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glTexStorage1D(GLenum target,
    GLsizei levels, GLenum internalformat, GLsizei width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glTexStorage1D

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
    """
    #  void QOpenGLFunctions_4_5_Core::glTexStorage1D(GLenum target, GLsizei
    #      levels, GLenum internalformat, GLsizei width)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core14glTexStorage1DEjiji',
        target, levels, internalformat, width,
    )

  @overload(int)
  def glMemoryBarrier(self, barriers: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glMemoryBarrier(GLbitfield
    barriers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glMemoryBarrier

    Parameters
    ----------

    barriers : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glMemoryBarrier(GLbitfield barriers)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core15glMemoryBarrierEj', barriers,
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
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glBindImageTexture(GLuint
    unit, GLuint texture, GLint level, GLboolean layered, GLint layer, GLenum
    access, GLenum format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glBindImageTexture

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
    #  void QOpenGLFunctions_4_5_Core::glBindImageTexture(GLuint unit, GLuint
    #      texture, GLint level, GLboolean layered, GLint layer, GLenum
    #      access, GLenum format)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core18glBindImageTextureEjjihijj',
        unit, texture, level, layered, layer, access, format,
    )

  @overload(int, int, int, int, int)
  def glDrawArraysInstancedBaseInstance(
      self,
      mode: int,
      first: int,
      count: int,
      instancecount: int,
      baseinstance: int,
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_5_Core::glDrawArraysInstancedBaseInstance(GLenum mode,
    GLint first, GLsizei count, GLsizei instancecount, GLuint baseinstance)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

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

    baseinstance : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glDrawArraysInstancedBaseInstance(
    #      GLenum mode, GLint first, GLsizei count, GLsizei instancecount,
    #      GLuint baseinstance)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core33glDrawArraysInstancedBaseIns'
        'tanceEjiiij',
        mode, first, count, instancecount, baseinstance,
    )

  def glPopDebugGroup(self) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glPopDebugGroup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glPopDebugGroup
    """
    #  void QOpenGLFunctions_4_5_Core::glPopDebugGroup()
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core15glPopDebugGroupEv',
    )

  @overload(int, int)
  def glVertexBindingDivisor(self, bindingindex: int, divisor: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glVertexBindingDivisor(GLuint
    bindingindex, GLuint divisor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

    Parameters
    ----------

    bindingindex : int
      Passed on as it is.

    divisor : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glVertexBindingDivisor(GLuint
    #      bindingindex, GLuint divisor)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core22glVertexBindingDivisorEjj',
        bindingindex, divisor,
    )

  @overload(int, int)
  def glVertexAttribBinding(
      self,
      attribindex: int,
      bindingindex: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttribBinding(GLuint
    attribindex, GLuint bindingindex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

    Parameters
    ----------

    attribindex : int
      Passed on as it is.

    bindingindex : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glVertexAttribBinding(GLuint
    #      attribindex, GLuint bindingindex)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core21glVertexAttribBindingEjj',
        attribindex, bindingindex,
    )

  @overload(int, int, int, int)
  def glVertexAttribLFormat(
      self,
      attribindex: int,
      size: int,
      type: int,
      relativeoffset: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttribLFormat(GLuint
    attribindex, GLint size, GLenum type, GLuint relativeoffset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

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
    #  void QOpenGLFunctions_4_5_Core::glVertexAttribLFormat(GLuint
    #      attribindex, GLint size, GLenum type, GLuint relativeoffset)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core21glVertexAttribLFormatEjijj',
        attribindex, size, type, relativeoffset,
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
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttribIFormat(GLuint
    attribindex, GLint size, GLenum type, GLuint relativeoffset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

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
    #  void QOpenGLFunctions_4_5_Core::glVertexAttribIFormat(GLuint
    #      attribindex, GLint size, GLenum type, GLuint relativeoffset)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core21glVertexAttribIFormatEjijj',
        attribindex, size, type, relativeoffset,
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
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttribFormat(GLuint
    attribindex, GLint size, GLenum type, GLboolean normalized, GLuint
    relativeoffset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

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
    #  void QOpenGLFunctions_4_5_Core::glVertexAttribFormat(GLuint
    #      attribindex, GLint size, GLenum type, GLboolean normalized, GLuint
    #      relativeoffset)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core20glVertexAttribFormatEjijhj',
        attribindex, size, type, normalized, relativeoffset,
    )

  @overload(int, int, int, int)
  def glBindVertexBuffer(
      self,
      bindingindex: int,
      buffer: int,
      offset: int,
      stride: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glBindVertexBuffer(GLuint
    bindingindex, GLuint buffer, GLintptr offset, GLsizei stride)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glBindVertexBuffer

    Parameters
    ----------

    bindingindex : int
      Passed on as it is.

    buffer : int
      Passed on as it is.

    offset : int
      Passed on as it is.

    stride : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glBindVertexBuffer(GLuint
    #      bindingindex, GLuint buffer, GLintptr offset, GLsizei stride)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core18glBindVertexBufferEjjli',
        bindingindex, buffer, offset, stride,
    )

  @overload(int, int, int, int, int, int, int, int)
  def glTextureView(
      self,
      texture: int,
      target: int,
      origtexture: int,
      internalformat: int,
      minlevel: int,
      numlevels: int,
      minlayer: int,
      numlayers: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glTextureView(GLuint texture,
    GLenum target, GLuint origtexture, GLenum internalformat, GLuint
    minlevel, GLuint numlevels, GLuint minlayer, GLuint numlayers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glTextureView

    Parameters
    ----------

    texture : int
      Passed on as it is.

    target : int
      Passed on as it is.

    origtexture : int
      Passed on as it is.

    internalformat : int
      Passed on as it is.

    minlevel : int
      Passed on as it is.

    numlevels : int
      Passed on as it is.

    minlayer : int
      Passed on as it is.

    numlayers : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glTextureView(GLuint texture, GLenum
    #      target, GLuint origtexture, GLenum internalformat, GLuint
    #      minlevel, GLuint numlevels, GLuint minlayer, GLuint numlayers)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core13glTextureViewEjjjjjjjj',
        texture, target, origtexture, internalformat, minlevel, numlevels,
        minlayer, numlayers,
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
    Calls Qt's 'void
    QOpenGLFunctions_4_5_Core::glTexStorage3DMultisample(GLenum target,
    GLsizei samples, GLenum internalformat, GLsizei width, GLsizei height,
    GLsizei depth, GLboolean fixedsamplelocations)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

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
    #  void QOpenGLFunctions_4_5_Core::glTexStorage3DMultisample(GLenum
    #      target, GLsizei samples, GLenum internalformat, GLsizei width,
    #      GLsizei height, GLsizei depth, GLboolean fixedsamplelocations)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core25glTexStorage3DMultisampleEji'
        'jiiih',
        target, samples, internalformat, width, height, depth,
        fixedsamplelocations,
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
    Calls Qt's 'void
    QOpenGLFunctions_4_5_Core::glTexStorage2DMultisample(GLenum target,
    GLsizei samples, GLenum internalformat, GLsizei width, GLsizei height,
    GLboolean fixedsamplelocations)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

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
    #  void QOpenGLFunctions_4_5_Core::glTexStorage2DMultisample(GLenum
    #      target, GLsizei samples, GLenum internalformat, GLsizei width,
    #      GLsizei height, GLboolean fixedsamplelocations)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core25glTexStorage2DMultisampleEji'
        'jiih',
        target, samples, internalformat, width, height, fixedsamplelocations,
    )

  @overload(int, int, int, int, int)
  def glTexBufferRange(
      self,
      target: int,
      internalformat: int,
      buffer: int,
      offset: int,
      size: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glTexBufferRange(GLenum
    target, GLenum internalformat, GLuint buffer, GLintptr offset, GLsizeiptr
    size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glTexBufferRange

    Parameters
    ----------

    target : int
      Passed on as it is.

    internalformat : int
      Passed on as it is.

    buffer : int
      Passed on as it is.

    offset : int
      Passed on as it is.

    size : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glTexBufferRange(GLenum target, GLenum
    #      internalformat, GLuint buffer, GLintptr offset, GLsizeiptr size)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core16glTexBufferRangeEjjjll',
        target, internalformat, buffer, offset, size,
    )

  @overload(int, int, int)
  def glShaderStorageBlockBinding(
      self,
      program: int,
      storageBlockIndex: int,
      storageBlockBinding: int,
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_5_Core::glShaderStorageBlockBinding(GLuint program,
    GLuint storageBlockIndex, GLuint storageBlockBinding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

    Parameters
    ----------

    program : int
      Passed on as it is.

    storageBlockIndex : int
      Passed on as it is.

    storageBlockBinding : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glShaderStorageBlockBinding(GLuint
    #      program, GLuint storageBlockIndex, GLuint storageBlockBinding)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core27glShaderStorageBlockBindingE'
        'jjj',
        program, storageBlockIndex, storageBlockBinding,
    )

  @overload(int)
  def glInvalidateBufferData(self, buffer: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glInvalidateBufferData(GLuint
    buffer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

    Parameters
    ----------

    buffer : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glInvalidateBufferData(GLuint buffer)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core22glInvalidateBufferDataEj',
        buffer,
    )

  @overload(int, int, int)
  def glInvalidateBufferSubData(
      self,
      buffer: int,
      offset: int,
      length: int,
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_5_Core::glInvalidateBufferSubData(GLuint buffer,
    GLintptr offset, GLsizeiptr length)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

    Parameters
    ----------

    buffer : int
      Passed on as it is.

    offset : int
      Passed on as it is.

    length : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glInvalidateBufferSubData(GLuint
    #      buffer, GLintptr offset, GLsizeiptr length)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core25glInvalidateBufferSubDataEjl'
        'l',
        buffer, offset, length,
    )

  @overload(int, int)
  def glInvalidateTexImage(self, texture: int, level: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glInvalidateTexImage(GLuint
    texture, GLint level)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

    Parameters
    ----------

    texture : int
      Passed on as it is.

    level : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glInvalidateTexImage(GLuint texture,
    #      GLint level)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core20glInvalidateTexImageEji',
        texture, level,
    )

  @overload(int, int, int, int, int, int, int, int)
  def glInvalidateTexSubImage(
      self,
      texture: int,
      level: int,
      xoffset: int,
      yoffset: int,
      zoffset: int,
      width: int,
      height: int,
      depth: int,
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_5_Core::glInvalidateTexSubImage(GLuint texture, GLint
    level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width,
    GLsizei height, GLsizei depth)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

    Parameters
    ----------

    texture : int
      Passed on as it is.

    level : int
      Passed on as it is.

    xoffset : int
      Passed on as it is.

    yoffset : int
      Passed on as it is.

    zoffset : int
      Passed on as it is.

    width : int
      Passed on as it is.

    height : int
      Passed on as it is.

    depth : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glInvalidateTexSubImage(GLuint
    #      texture, GLint level, GLint xoffset, GLint yoffset, GLint zoffset,
    #      GLsizei width, GLsizei height, GLsizei depth)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core23glInvalidateTexSubImageEjiii'
        'iiii',
        texture, level, xoffset, yoffset, zoffset, width, height, depth,
    )

  @overload(int, int, int)
  def glFramebufferParameteri(
      self,
      target: int,
      pname: int,
      param: int,
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_5_Core::glFramebufferParameteri(GLenum target, GLenum
    pname, GLint param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

    Parameters
    ----------

    target : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    param : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glFramebufferParameteri(GLenum target,
    #      GLenum pname, GLint param)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core23glFramebufferParameteriEjji',
        target, pname, param,
    )

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
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glCopyImageSubData(GLuint
    srcName, GLenum srcTarget, GLint srcLevel, GLint srcX, GLint srcY, GLint
    srcZ, GLuint dstName, GLenum dstTarget, GLint dstLevel, GLint dstX, GLint
    dstY, GLint dstZ, GLsizei srcWidth, GLsizei srcHeight, GLsizei
    srcDepth)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glCopyImageSubData

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
    #  void QOpenGLFunctions_4_5_Core::glCopyImageSubData(GLuint srcName,
    #      GLenum srcTarget, GLint srcLevel, GLint srcX, GLint srcY, GLint
    #      srcZ, GLuint dstName, GLenum dstTarget, GLint dstLevel, GLint
    #      dstX, GLint dstY, GLint dstZ, GLsizei srcWidth, GLsizei srcHeight,
    #      GLsizei srcDepth)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core18glCopyImageSubDataEjjiiiijji'
        'iiiiii',
        srcName, srcTarget, srcLevel, srcX, srcY, srcZ, dstName, dstTarget,
        dstLevel, dstX, dstY, dstZ, srcWidth, srcHeight, srcDepth,
    )

  @overload(int)
  def glDispatchComputeIndirect(self, indirect: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_5_Core::glDispatchComputeIndirect(GLintptr indirect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

    Parameters
    ----------

    indirect : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glDispatchComputeIndirect(GLintptr
    #      indirect)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core25glDispatchComputeIndirectEl',
        indirect,
    )

  @overload(int, int, int)
  def glDispatchCompute(
      self,
      num_groups_x: int,
      num_groups_y: int,
      num_groups_z: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glDispatchCompute(GLuint
    num_groups_x, GLuint num_groups_y, GLuint num_groups_z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glDispatchCompute

    Parameters
    ----------

    num_groups_x : int
      Passed on as it is.

    num_groups_y : int
      Passed on as it is.

    num_groups_z : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glDispatchCompute(GLuint num_groups_x,
    #      GLuint num_groups_y, GLuint num_groups_z)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core17glDispatchComputeEjjj',
        num_groups_x, num_groups_y, num_groups_z,
    )

  def glTextureBarrier(self) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glTextureBarrier()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glTextureBarrier
    """
    #  void QOpenGLFunctions_4_5_Core::glTextureBarrier()
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core16glTextureBarrierEv',
    )

  def glGetGraphicsResetStatus(self) -> int:
    """
    Calls Qt's 'GLenum
    QOpenGLFunctions_4_5_Core::glGetGraphicsResetStatus()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html
    """
    #  GLenum QOpenGLFunctions_4_5_Core::glGetGraphicsResetStatus()
    return self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core24glGetGraphicsResetStatusEv',
    )

  @overload(int)
  def glMemoryBarrierByRegion(self, barriers: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_5_Core::glMemoryBarrierByRegion(GLbitfield barriers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

    Parameters
    ----------

    barriers : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glMemoryBarrierByRegion(GLbitfield
    #      barriers)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core23glMemoryBarrierByRegionEj',
        barriers,
    )

  @overload(int, int, int)
  def glVertexArrayBindingDivisor(
      self,
      vaobj: int,
      bindingindex: int,
      divisor: int,
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_5_Core::glVertexArrayBindingDivisor(GLuint vaobj,
    GLuint bindingindex, GLuint divisor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

    Parameters
    ----------

    vaobj : int
      Passed on as it is.

    bindingindex : int
      Passed on as it is.

    divisor : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glVertexArrayBindingDivisor(GLuint
    #      vaobj, GLuint bindingindex, GLuint divisor)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core27glVertexArrayBindingDivisorE'
        'jjj',
        vaobj, bindingindex, divisor,
    )

  @overload(int, int, int, int, int)
  def glVertexArrayAttribLFormat(
      self,
      vaobj: int,
      attribindex: int,
      size: int,
      type: int,
      relativeoffset: int,
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_5_Core::glVertexArrayAttribLFormat(GLuint vaobj,
    GLuint attribindex, GLint size, GLenum type, GLuint relativeoffset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

    Parameters
    ----------

    vaobj : int
      Passed on as it is.

    attribindex : int
      Passed on as it is.

    size : int
      Passed on as it is.

    type : int
      Passed on as it is.

    relativeoffset : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glVertexArrayAttribLFormat(GLuint
    #      vaobj, GLuint attribindex, GLint size, GLenum type, GLuint
    #      relativeoffset)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core26glVertexArrayAttribLFormatEj'
        'jijj',
        vaobj, attribindex, size, type, relativeoffset,
    )

  @overload(int, int, int, int, int)
  def glVertexArrayAttribIFormat(
      self,
      vaobj: int,
      attribindex: int,
      size: int,
      type: int,
      relativeoffset: int,
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_5_Core::glVertexArrayAttribIFormat(GLuint vaobj,
    GLuint attribindex, GLint size, GLenum type, GLuint relativeoffset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

    Parameters
    ----------

    vaobj : int
      Passed on as it is.

    attribindex : int
      Passed on as it is.

    size : int
      Passed on as it is.

    type : int
      Passed on as it is.

    relativeoffset : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glVertexArrayAttribIFormat(GLuint
    #      vaobj, GLuint attribindex, GLint size, GLenum type, GLuint
    #      relativeoffset)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core26glVertexArrayAttribIFormatEj'
        'jijj',
        vaobj, attribindex, size, type, relativeoffset,
    )

  @overload(int, int, int, int, int, int)
  def glVertexArrayAttribFormat(
      self,
      vaobj: int,
      attribindex: int,
      size: int,
      type: int,
      normalized: int,
      relativeoffset: int,
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_5_Core::glVertexArrayAttribFormat(GLuint vaobj, GLuint
    attribindex, GLint size, GLenum type, GLboolean normalized, GLuint
    relativeoffset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

    Parameters
    ----------

    vaobj : int
      Passed on as it is.

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
    #  void QOpenGLFunctions_4_5_Core::glVertexArrayAttribFormat(GLuint
    #      vaobj, GLuint attribindex, GLint size, GLenum type, GLboolean
    #      normalized, GLuint relativeoffset)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core25glVertexArrayAttribFormatEjj'
        'ijhj',
        vaobj, attribindex, size, type, normalized, relativeoffset,
    )

  @overload(int, int, int)
  def glVertexArrayAttribBinding(
      self,
      vaobj: int,
      attribindex: int,
      bindingindex: int,
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_5_Core::glVertexArrayAttribBinding(GLuint vaobj,
    GLuint attribindex, GLuint bindingindex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

    Parameters
    ----------

    vaobj : int
      Passed on as it is.

    attribindex : int
      Passed on as it is.

    bindingindex : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glVertexArrayAttribBinding(GLuint
    #      vaobj, GLuint attribindex, GLuint bindingindex)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core26glVertexArrayAttribBindingEj'
        'jj',
        vaobj, attribindex, bindingindex,
    )

  @overload(int, int, int, int, int)
  def glVertexArrayVertexBuffer(
      self,
      vaobj: int,
      bindingindex: int,
      buffer: int,
      offset: int,
      stride: int,
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_5_Core::glVertexArrayVertexBuffer(GLuint vaobj, GLuint
    bindingindex, GLuint buffer, GLintptr offset, GLsizei stride)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

    Parameters
    ----------

    vaobj : int
      Passed on as it is.

    bindingindex : int
      Passed on as it is.

    buffer : int
      Passed on as it is.

    offset : int
      Passed on as it is.

    stride : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glVertexArrayVertexBuffer(GLuint
    #      vaobj, GLuint bindingindex, GLuint buffer, GLintptr offset,
    #      GLsizei stride)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core25glVertexArrayVertexBufferEjj'
        'jli',
        vaobj, bindingindex, buffer, offset, stride,
    )

  @overload(int, int)
  def glVertexArrayElementBuffer(self, vaobj: int, buffer: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_5_Core::glVertexArrayElementBuffer(GLuint vaobj,
    GLuint buffer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

    Parameters
    ----------

    vaobj : int
      Passed on as it is.

    buffer : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glVertexArrayElementBuffer(GLuint
    #      vaobj, GLuint buffer)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core26glVertexArrayElementBufferEj'
        'j',
        vaobj, buffer,
    )

  @overload(int, int)
  def glEnableVertexArrayAttrib(self, vaobj: int, index: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_5_Core::glEnableVertexArrayAttrib(GLuint vaobj, GLuint
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

    Parameters
    ----------

    vaobj : int
      Passed on as it is.

    index : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glEnableVertexArrayAttrib(GLuint
    #      vaobj, GLuint index)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core25glEnableVertexArrayAttribEjj',
        vaobj, index,
    )

  @overload(int, int)
  def glDisableVertexArrayAttrib(self, vaobj: int, index: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_5_Core::glDisableVertexArrayAttrib(GLuint vaobj,
    GLuint index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

    Parameters
    ----------

    vaobj : int
      Passed on as it is.

    index : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glDisableVertexArrayAttrib(GLuint
    #      vaobj, GLuint index)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core26glDisableVertexArrayAttribEj'
        'j',
        vaobj, index,
    )

  @overload(int, int)
  def glBindTextureUnit(self, unit: int, texture: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glBindTextureUnit(GLuint
    unit, GLuint texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glBindTextureUnit

    Parameters
    ----------

    unit : int
      Passed on as it is.

    texture : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glBindTextureUnit(GLuint unit, GLuint
    #      texture)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core17glBindTextureUnitEjj',
        unit, texture,
    )

  @overload(int)
  def glGenerateTextureMipmap(self, texture: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_5_Core::glGenerateTextureMipmap(GLuint texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

    Parameters
    ----------

    texture : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glGenerateTextureMipmap(GLuint
    #      texture)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core23glGenerateTextureMipmapEj',
        texture,
    )

  @overload(int, int, int)
  def glTextureParameteri(
      self,
      texture: int,
      pname: int,
      param: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glTextureParameteri(GLuint
    texture, GLenum pname, GLint param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glTextureParameteri

    Parameters
    ----------

    texture : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    param : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glTextureParameteri(GLuint texture,
    #      GLenum pname, GLint param)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core19glTextureParameteriEjji',
        texture, pname, param,
    )

  @overload(int, int, float)
  def glTextureParameterf(
      self,
      texture: int,
      pname: int,
      param: float,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glTextureParameterf(GLuint
    texture, GLenum pname, GLfloat param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glTextureParameterf

    Parameters
    ----------

    texture : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    param : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glTextureParameterf(GLuint texture,
    #      GLenum pname, GLfloat param)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core19glTextureParameterfEjjf',
        texture, pname, param,
    )

  @overload(int, int, int, int, int, int, int, int, int)
  def glCopyTextureSubImage3D(
      self,
      texture: int,
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
    Calls Qt's 'void
    QOpenGLFunctions_4_5_Core::glCopyTextureSubImage3D(GLuint texture, GLint
    level, GLint xoffset, GLint yoffset, GLint zoffset, GLint x, GLint y,
    GLsizei width, GLsizei height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

    Parameters
    ----------

    texture : int
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
    #  void QOpenGLFunctions_4_5_Core::glCopyTextureSubImage3D(GLuint
    #      texture, GLint level, GLint xoffset, GLint yoffset, GLint zoffset,
    #      GLint x, GLint y, GLsizei width, GLsizei height)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core23glCopyTextureSubImage3DEjiii'
        'iiiii',
        texture, level, xoffset, yoffset, zoffset, x, y, width, height,
    )

  @overload(int, int, int, int, int, int, int, int)
  def glCopyTextureSubImage2D(
      self,
      texture: int,
      level: int,
      xoffset: int,
      yoffset: int,
      x: int,
      y: int,
      width: int,
      height: int,
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_5_Core::glCopyTextureSubImage2D(GLuint texture, GLint
    level, GLint xoffset, GLint yoffset, GLint x, GLint y, GLsizei width,
    GLsizei height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

    Parameters
    ----------

    texture : int
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
    #  void QOpenGLFunctions_4_5_Core::glCopyTextureSubImage2D(GLuint
    #      texture, GLint level, GLint xoffset, GLint yoffset, GLint x, GLint
    #      y, GLsizei width, GLsizei height)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core23glCopyTextureSubImage2DEjiii'
        'iiii',
        texture, level, xoffset, yoffset, x, y, width, height,
    )

  @overload(int, int, int, int, int, int)
  def glCopyTextureSubImage1D(
      self,
      texture: int,
      level: int,
      xoffset: int,
      x: int,
      y: int,
      width: int,
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_5_Core::glCopyTextureSubImage1D(GLuint texture, GLint
    level, GLint xoffset, GLint x, GLint y, GLsizei width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

    Parameters
    ----------

    texture : int
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
    #  void QOpenGLFunctions_4_5_Core::glCopyTextureSubImage1D(GLuint
    #      texture, GLint level, GLint xoffset, GLint x, GLint y, GLsizei
    #      width)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core23glCopyTextureSubImage1DEjiii'
        'ii',
        texture, level, xoffset, x, y, width,
    )

  @overload(int, int, int, int, int, int, int)
  def glTextureStorage3DMultisample(
      self,
      texture: int,
      samples: int,
      internalformat: int,
      width: int,
      height: int,
      depth: int,
      fixedsamplelocations: int,
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_5_Core::glTextureStorage3DMultisample(GLuint texture,
    GLsizei samples, GLenum internalformat, GLsizei width, GLsizei height,
    GLsizei depth, GLboolean fixedsamplelocations)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

    Parameters
    ----------

    texture : int
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
    #  void QOpenGLFunctions_4_5_Core::glTextureStorage3DMultisample(GLuint
    #      texture, GLsizei samples, GLenum internalformat, GLsizei width,
    #      GLsizei height, GLsizei depth, GLboolean fixedsamplelocations)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core29glTextureStorage3DMultisampl'
        'eEjijiiih',
        texture, samples, internalformat, width, height, depth,
        fixedsamplelocations,
    )

  @overload(int, int, int, int, int, int)
  def glTextureStorage2DMultisample(
      self,
      texture: int,
      samples: int,
      internalformat: int,
      width: int,
      height: int,
      fixedsamplelocations: int,
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_5_Core::glTextureStorage2DMultisample(GLuint texture,
    GLsizei samples, GLenum internalformat, GLsizei width, GLsizei height,
    GLboolean fixedsamplelocations)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

    Parameters
    ----------

    texture : int
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
    #  void QOpenGLFunctions_4_5_Core::glTextureStorage2DMultisample(GLuint
    #      texture, GLsizei samples, GLenum internalformat, GLsizei width,
    #      GLsizei height, GLboolean fixedsamplelocations)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core29glTextureStorage2DMultisampl'
        'eEjijiih',
        texture, samples, internalformat, width, height,
        fixedsamplelocations,
    )

  @overload(int, int, int, int, int, int)
  def glTextureStorage3D(
      self,
      texture: int,
      levels: int,
      internalformat: int,
      width: int,
      height: int,
      depth: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glTextureStorage3D(GLuint
    texture, GLsizei levels, GLenum internalformat, GLsizei width, GLsizei
    height, GLsizei depth)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glTextureStorage3D

    Parameters
    ----------

    texture : int
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
    #  void QOpenGLFunctions_4_5_Core::glTextureStorage3D(GLuint texture,
    #      GLsizei levels, GLenum internalformat, GLsizei width, GLsizei
    #      height, GLsizei depth)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core18glTextureStorage3DEjijiii',
        texture, levels, internalformat, width, height, depth,
    )

  @overload(int, int, int, int, int)
  def glTextureStorage2D(
      self,
      texture: int,
      levels: int,
      internalformat: int,
      width: int,
      height: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glTextureStorage2D(GLuint
    texture, GLsizei levels, GLenum internalformat, GLsizei width, GLsizei
    height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glTextureStorage2D

    Parameters
    ----------

    texture : int
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
    #  void QOpenGLFunctions_4_5_Core::glTextureStorage2D(GLuint texture,
    #      GLsizei levels, GLenum internalformat, GLsizei width, GLsizei
    #      height)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core18glTextureStorage2DEjijii',
        texture, levels, internalformat, width, height,
    )

  @overload(int, int, int, int)
  def glTextureStorage1D(
      self,
      texture: int,
      levels: int,
      internalformat: int,
      width: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glTextureStorage1D(GLuint
    texture, GLsizei levels, GLenum internalformat, GLsizei width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glTextureStorage1D

    Parameters
    ----------

    texture : int
      Passed on as it is.

    levels : int
      Passed on as it is.

    internalformat : int
      Passed on as it is.

    width : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glTextureStorage1D(GLuint texture,
    #      GLsizei levels, GLenum internalformat, GLsizei width)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core18glTextureStorage1DEjiji',
        texture, levels, internalformat, width,
    )

  @overload(int, int, int, int, int)
  def glTextureBufferRange(
      self,
      texture: int,
      internalformat: int,
      buffer: int,
      offset: int,
      size: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glTextureBufferRange(GLuint
    texture, GLenum internalformat, GLuint buffer, GLintptr offset, GLsizei
    size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

    Parameters
    ----------

    texture : int
      Passed on as it is.

    internalformat : int
      Passed on as it is.

    buffer : int
      Passed on as it is.

    offset : int
      Passed on as it is.

    size : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glTextureBufferRange(GLuint texture,
    #      GLenum internalformat, GLuint buffer, GLintptr offset, GLsizei
    #      size)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core20glTextureBufferRangeEjjjli',
        texture, internalformat, buffer, offset, size,
    )

  @overload(int, int, int)
  def glTextureBuffer(
      self,
      texture: int,
      internalformat: int,
      buffer: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glTextureBuffer(GLuint
    texture, GLenum internalformat, GLuint buffer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glTextureBuffer

    Parameters
    ----------

    texture : int
      Passed on as it is.

    internalformat : int
      Passed on as it is.

    buffer : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glTextureBuffer(GLuint texture, GLenum
    #      internalformat, GLuint buffer)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core15glTextureBufferEjjj',
        texture, internalformat, buffer,
    )

  @overload(int, int, int, int, int)
  def glNamedRenderbufferStorageMultisample(
      self,
      renderbuffer: int,
      samples: int,
      internalformat: int,
      width: int,
      height: int,
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_5_Core::glNamedRenderbufferStorageMultisample(GLuint
    renderbuffer, GLsizei samples, GLenum internalformat, GLsizei width,
    GLsizei height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

    Parameters
    ----------

    renderbuffer : int
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
    #  void QOpenGLFunctions_4_5_Core::glNamedRenderbufferStorageMultisample(
    #      GLuint renderbuffer, GLsizei samples, GLenum internalformat,
    #      GLsizei width, GLsizei height)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core37glNamedRenderbufferStorageMu'
        'ltisampleEjijii',
        renderbuffer, samples, internalformat, width, height,
    )

  @overload(int, int, int, int)
  def glNamedRenderbufferStorage(
      self,
      renderbuffer: int,
      internalformat: int,
      width: int,
      height: int,
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_5_Core::glNamedRenderbufferStorage(GLuint
    renderbuffer, GLenum internalformat, GLsizei width, GLsizei height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

    Parameters
    ----------

    renderbuffer : int
      Passed on as it is.

    internalformat : int
      Passed on as it is.

    width : int
      Passed on as it is.

    height : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glNamedRenderbufferStorage(GLuint
    #      renderbuffer, GLenum internalformat, GLsizei width, GLsizei
    #      height)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core26glNamedRenderbufferStorageEj'
        'jii',
        renderbuffer, internalformat, width, height,
    )

  @overload(int, int)
  def glCheckNamedFramebufferStatus(
      self,
      framebuffer: int,
      target: int,
  ) -> int:
    """
    Calls Qt's 'GLenum
    QOpenGLFunctions_4_5_Core::glCheckNamedFramebufferStatus(GLuint
    framebuffer, GLenum target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

    Parameters
    ----------

    framebuffer : int
      Passed on as it is.

    target : int
      Passed on as it is.
    """
    #  GLenum QOpenGLFunctions_4_5_Core::glCheckNamedFramebufferStatus(GLuint
    #      framebuffer, GLenum target)
    return self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core29glCheckNamedFramebufferStatu'
        'sEjj',
        framebuffer, target,
    )

  @overload(int, int, int, int, int, int, int, int, int, int, int, int)
  def glBlitNamedFramebuffer(
      self,
      readFramebuffer: int,
      drawFramebuffer: int,
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
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glBlitNamedFramebuffer(GLuint
    readFramebuffer, GLuint drawFramebuffer, GLint srcX0, GLint srcY0, GLint
    srcX1, GLint srcY1, GLint dstX0, GLint dstY0, GLint dstX1, GLint dstY1,
    GLbitfield mask, GLenum filter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

    Parameters
    ----------

    readFramebuffer : int
      Passed on as it is.

    drawFramebuffer : int
      Passed on as it is.

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
    #  void QOpenGLFunctions_4_5_Core::glBlitNamedFramebuffer(GLuint
    #      readFramebuffer, GLuint drawFramebuffer, GLint srcX0, GLint srcY0,
    #      GLint srcX1, GLint srcY1, GLint dstX0, GLint dstY0, GLint dstX1,
    #      GLint dstY1, GLbitfield mask, GLenum filter)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core22glBlitNamedFramebufferEjjiii'
        'iiiiijj',
        readFramebuffer, drawFramebuffer, srcX0, srcY0, srcX1, srcY1, dstX0,
        dstY0, dstX1, dstY1, mask, filter,
    )

  @overload(int, int, float, int)
  def glClearNamedFramebufferfi(
      self,
      framebuffer: int,
      buffer: int,
      depth: float,
      stencil: int,
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_5_Core::glClearNamedFramebufferfi(GLuint framebuffer,
    GLenum buffer, GLfloat depth, GLint stencil)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

    Parameters
    ----------

    framebuffer : int
      Passed on as it is.

    buffer : int
      Passed on as it is.

    depth : float
      Passed on as it is.

    stencil : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glClearNamedFramebufferfi(GLuint
    #      framebuffer, GLenum buffer, GLfloat depth, GLint stencil)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core25glClearNamedFramebufferfiEjj'
        'fi',
        framebuffer, buffer, depth, stencil,
    )

  @overload(int, int)
  def glNamedFramebufferReadBuffer(self, framebuffer: int, src: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_5_Core::glNamedFramebufferReadBuffer(GLuint
    framebuffer, GLenum src)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

    Parameters
    ----------

    framebuffer : int
      Passed on as it is.

    src : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glNamedFramebufferReadBuffer(GLuint
    #      framebuffer, GLenum src)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core28glNamedFramebufferReadBuffer'
        'Ejj',
        framebuffer, src,
    )

  @overload(int, int)
  def glNamedFramebufferDrawBuffer(self, framebuffer: int, buf: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_5_Core::glNamedFramebufferDrawBuffer(GLuint
    framebuffer, GLenum buf)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

    Parameters
    ----------

    framebuffer : int
      Passed on as it is.

    buf : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glNamedFramebufferDrawBuffer(GLuint
    #      framebuffer, GLenum buf)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core28glNamedFramebufferDrawBuffer'
        'Ejj',
        framebuffer, buf,
    )

  @overload(int, int, int, int, int)
  def glNamedFramebufferTextureLayer(
      self,
      framebuffer: int,
      attachment: int,
      texture: int,
      level: int,
      layer: int,
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_5_Core::glNamedFramebufferTextureLayer(GLuint
    framebuffer, GLenum attachment, GLuint texture, GLint level, GLint
    layer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

    Parameters
    ----------

    framebuffer : int
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
    #  void QOpenGLFunctions_4_5_Core::glNamedFramebufferTextureLayer(GLuint
    #      framebuffer, GLenum attachment, GLuint texture, GLint level, GLint
    #      layer)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core30glNamedFramebufferTextureLay'
        'erEjjjii',
        framebuffer, attachment, texture, level, layer,
    )

  @overload(int, int, int, int)
  def glNamedFramebufferTexture(
      self,
      framebuffer: int,
      attachment: int,
      texture: int,
      level: int,
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_5_Core::glNamedFramebufferTexture(GLuint framebuffer,
    GLenum attachment, GLuint texture, GLint level)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

    Parameters
    ----------

    framebuffer : int
      Passed on as it is.

    attachment : int
      Passed on as it is.

    texture : int
      Passed on as it is.

    level : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glNamedFramebufferTexture(GLuint
    #      framebuffer, GLenum attachment, GLuint texture, GLint level)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core25glNamedFramebufferTextureEjj'
        'ji',
        framebuffer, attachment, texture, level,
    )

  @overload(int, int, int)
  def glNamedFramebufferParameteri(
      self,
      framebuffer: int,
      pname: int,
      param: int,
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_5_Core::glNamedFramebufferParameteri(GLuint
    framebuffer, GLenum pname, GLint param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

    Parameters
    ----------

    framebuffer : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    param : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glNamedFramebufferParameteri(GLuint
    #      framebuffer, GLenum pname, GLint param)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core28glNamedFramebufferParameteri'
        'Ejji',
        framebuffer, pname, param,
    )

  @overload(int, int, int, int)
  def glNamedFramebufferRenderbuffer(
      self,
      framebuffer: int,
      attachment: int,
      renderbuffertarget: int,
      renderbuffer: int,
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_5_Core::glNamedFramebufferRenderbuffer(GLuint
    framebuffer, GLenum attachment, GLenum renderbuffertarget, GLuint
    renderbuffer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

    Parameters
    ----------

    framebuffer : int
      Passed on as it is.

    attachment : int
      Passed on as it is.

    renderbuffertarget : int
      Passed on as it is.

    renderbuffer : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glNamedFramebufferRenderbuffer(GLuint
    #      framebuffer, GLenum attachment, GLenum renderbuffertarget, GLuint
    #      renderbuffer)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core30glNamedFramebufferRenderbuff'
        'erEjjjj',
        framebuffer, attachment, renderbuffertarget, renderbuffer,
    )

  @overload(int, int, int)
  def glFlushMappedNamedBufferRange(
      self,
      buffer: int,
      offset: int,
      length: int,
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_5_Core::glFlushMappedNamedBufferRange(GLuint buffer,
    GLintptr offset, GLsizeiptr length)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

    Parameters
    ----------

    buffer : int
      Passed on as it is.

    offset : int
      Passed on as it is.

    length : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glFlushMappedNamedBufferRange(GLuint
    #      buffer, GLintptr offset, GLsizeiptr length)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core29glFlushMappedNamedBufferRang'
        'eEjll',
        buffer, offset, length,
    )

  @overload(int)
  def glUnmapNamedBuffer(self, buffer: int) -> int:
    """
    Calls Qt's 'GLboolean
    QOpenGLFunctions_4_5_Core::glUnmapNamedBuffer(GLuint buffer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glUnmapNamedBuffer

    Parameters
    ----------

    buffer : int
      Passed on as it is.
    """
    #  GLboolean QOpenGLFunctions_4_5_Core::glUnmapNamedBuffer(GLuint buffer)
    return self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core18glUnmapNamedBufferEj', buffer,
    )

  @overload(int, int, int, int, int)
  def glCopyNamedBufferSubData(
      self,
      readBuffer: int,
      writeBuffer: int,
      readOffset: int,
      writeOffset: int,
      size: int,
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_5_Core::glCopyNamedBufferSubData(GLuint readBuffer,
    GLuint writeBuffer, GLintptr readOffset, GLintptr writeOffset, GLsizeiptr
    size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

    Parameters
    ----------

    readBuffer : int
      Passed on as it is.

    writeBuffer : int
      Passed on as it is.

    readOffset : int
      Passed on as it is.

    writeOffset : int
      Passed on as it is.

    size : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glCopyNamedBufferSubData(GLuint
    #      readBuffer, GLuint writeBuffer, GLintptr readOffset, GLintptr
    #      writeOffset, GLsizeiptr size)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core24glCopyNamedBufferSubDataEjjl'
        'll',
        readBuffer, writeBuffer, readOffset, writeOffset, size,
    )

  @overload(int, int, int, int, int)
  def glTransformFeedbackBufferRange(
      self,
      xfb: int,
      index: int,
      buffer: int,
      offset: int,
      size: int,
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_5_Core::glTransformFeedbackBufferRange(GLuint xfb,
    GLuint index, GLuint buffer, GLintptr offset, GLsizeiptr size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

    Parameters
    ----------

    xfb : int
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
    #  void QOpenGLFunctions_4_5_Core::glTransformFeedbackBufferRange(GLuint
    #      xfb, GLuint index, GLuint buffer, GLintptr offset, GLsizeiptr
    #      size)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core30glTransformFeedbackBufferRan'
        'geEjjjll',
        xfb, index, buffer, offset, size,
    )

  @overload(int, int, int)
  def glTransformFeedbackBufferBase(
      self,
      xfb: int,
      index: int,
      buffer: int,
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_5_Core::glTransformFeedbackBufferBase(GLuint xfb,
    GLuint index, GLuint buffer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html

    Parameters
    ----------

    xfb : int
      Passed on as it is.

    index : int
      Passed on as it is.

    buffer : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glTransformFeedbackBufferBase(GLuint
    #      xfb, GLuint index, GLuint buffer)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core29glTransformFeedbackBufferBas'
        'eEjjj',
        xfb, index, buffer,
    )

  @overload(int, int)
  def glClipControl(self, origin: int, depth: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_5_Core::glClipControl(GLenum origin,
    GLenum depth)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_5_core.html#glClipControl

    Parameters
    ----------

    origin : int
      Passed on as it is.

    depth : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_5_Core::glClipControl(GLenum origin, GLenum
    #      depth)
    self.uglySide.call(
        'ritual_ZN25QOpenGLFunctions_4_5_Core13glClipControlEjj',
        origin, depth,
    )

  @staticmethod
  def glBindAttribLocation(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glBindAttribLocation(GLuint
    program, GLuint index, const GLchar *name)': names 'GLchar', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glBindAttribLocation' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glBindAttribLocation(GLuint program, "
        "GLuint index, const GLchar *name)': names 'GLchar', which has no "
        "cute class yet.")

  @staticmethod
  def glBindBuffersBase(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glBindBuffersBase(GLenum target,
    GLuint first, GLsizei count, const GLuint *buffers)': names 'GLuint',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glBindBuffersBase' has no cute function "
        "yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glBindBuffersBase(GLenum target, GLuint "
        "first, GLsizei count, const GLuint *buffers)': names 'GLuint', "
        "which has no cute class yet.")

  @staticmethod
  def glBindBuffersRange(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glBindBuffersRange(GLenum target,
    GLuint first, GLsizei count, const GLuint *buffers, const GLintptr
    *offsets, const GLsizeiptr *sizes)': names 'GLuint', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glBindBuffersRange' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glBindBuffersRange(GLenum target, "
        "GLuint first, GLsizei count, const GLuint *buffers, const GLintptr "
        "*offsets, const GLsizeiptr *sizes)': names 'GLuint', which has no "
        "cute class yet.")

  @staticmethod
  def glBindFragDataLocation(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glBindFragDataLocation(GLuint
    program, GLuint color, const GLchar *name)': names 'GLchar', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glBindFragDataLocation' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glBindFragDataLocation(GLuint program, "
        "GLuint color, const GLchar *name)': names 'GLchar', which has no "
        "cute class yet.")

  @staticmethod
  def glBindFragDataLocationIndexed(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_5_Core::glBindFragDataLocationIndexed(GLuint program,
    GLuint colorNumber, GLuint index, const GLchar *name)': names 'GLchar',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glBindFragDataLocationIndexed' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glBindFragDataLocationIndexed(GLuint "
        "program, GLuint colorNumber, GLuint index, const GLchar *name)': "
        "names 'GLchar', which has no cute class yet.")

  @staticmethod
  def glBindImageTextures(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glBindImageTextures(GLuint first,
    GLsizei count, const GLuint *textures)': names 'GLuint', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glBindImageTextures' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glBindImageTextures(GLuint first, "
        "GLsizei count, const GLuint *textures)': names 'GLuint', which has "
        "no cute class yet.")

  @staticmethod
  def glBindSamplers(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glBindSamplers(GLuint first,
    GLsizei count, const GLuint *samplers)': names 'GLuint', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glBindSamplers' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_5_Core::glBindSamplers(GLuint "
        "first, GLsizei count, const GLuint *samplers)': names 'GLuint', "
        "which has no cute class yet.")

  @staticmethod
  def glBindTextures(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glBindTextures(GLuint first,
    GLsizei count, const GLuint *textures)': names 'GLuint', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glBindTextures' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_5_Core::glBindTextures(GLuint "
        "first, GLsizei count, const GLuint *textures)': names 'GLuint', "
        "which has no cute class yet.")

  @staticmethod
  def glBindVertexBuffers(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glBindVertexBuffers(GLuint first,
    GLsizei count, const GLuint *buffers, const GLintptr *offsets, const
    GLsizei *strides)': names 'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glBindVertexBuffers' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glBindVertexBuffers(GLuint first, "
        "GLsizei count, const GLuint *buffers, const GLintptr *offsets, "
        "const GLsizei *strides)': names 'GLuint', which has no cute class "
        "yet.")

  @staticmethod
  def glBufferData(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glBufferData(GLenum target,
    GLsizeiptr size, const void *data, GLenum usage)': names 'void', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glBufferData' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_4_5_Core::glBufferData(GLenum target, "
        "GLsizeiptr size, const void *data, GLenum usage)': names 'void', "
        "which has no cute class yet.")

  @staticmethod
  def glBufferStorage(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glBufferStorage(GLenum target,
    GLsizeiptr size, const void *data, GLbitfield flags)': names 'void',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glBufferStorage' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_5_Core::glBufferStorage(GLenum "
        "target, GLsizeiptr size, const void *data, GLbitfield flags)': "
        "names 'void', which has no cute class yet.")

  @staticmethod
  def glBufferSubData(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glBufferSubData(GLenum target,
    GLintptr offset, GLsizeiptr size, const void *data)': names 'void', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glBufferSubData' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_5_Core::glBufferSubData(GLenum "
        "target, GLintptr offset, GLsizeiptr size, const void *data)': "
        "names 'void', which has no cute class yet.")

  @staticmethod
  def glClearBufferData(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glClearBufferData(GLenum target,
    GLenum internalformat, GLenum format, GLenum type, const void *data)':
    names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glClearBufferData' has no cute function "
        "yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glClearBufferData(GLenum target, GLenum "
        "internalformat, GLenum format, GLenum type, const void *data)': "
        "names 'void', which has no cute class yet.")

  @staticmethod
  def glClearBufferSubData(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glClearBufferSubData(GLenum target,
    GLenum internalformat, GLintptr offset, GLsizeiptr size, GLenum format,
    GLenum type, const void *data)': names 'void', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glClearBufferSubData' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glClearBufferSubData(GLenum target, "
        "GLenum internalformat, GLintptr offset, GLsizeiptr size, GLenum "
        "format, GLenum type, const void *data)': names 'void', which has "
        "no cute class yet.")

  @staticmethod
  def glClearBufferfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glClearBufferfv(GLenum buffer,
    GLint drawbuffer, const GLfloat *value)': names 'GLfloat', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glClearBufferfv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_5_Core::glClearBufferfv(GLenum "
        "buffer, GLint drawbuffer, const GLfloat *value)': names 'GLfloat', "
        "which has no cute class yet.")

  @staticmethod
  def glClearBufferiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glClearBufferiv(GLenum buffer,
    GLint drawbuffer, const GLint *value)': names 'GLint', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glClearBufferiv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_5_Core::glClearBufferiv(GLenum "
        "buffer, GLint drawbuffer, const GLint *value)': names 'GLint', "
        "which has no cute class yet.")

  @staticmethod
  def glClearBufferuiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glClearBufferuiv(GLenum buffer,
    GLint drawbuffer, const GLuint *value)': names 'GLuint', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glClearBufferuiv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_5_Core::glClearBufferuiv(GLenum "
        "buffer, GLint drawbuffer, const GLuint *value)': names 'GLuint', "
        "which has no cute class yet.")

  @staticmethod
  def glClearNamedBufferData(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glClearNamedBufferData(GLuint
    buffer, GLenum internalformat, GLenum format, GLenum type, const void
    *data)': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glClearNamedBufferData' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glClearNamedBufferData(GLuint buffer, "
        "GLenum internalformat, GLenum format, GLenum type, const void "
        "*data)': names 'void', which has no cute class yet.")

  @staticmethod
  def glClearNamedBufferSubData(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glClearNamedBufferSubData(GLuint
    buffer, GLenum internalformat, GLintptr offset, GLsizeiptr size, GLenum
    format, GLenum type, const void *data)': names 'void', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glClearNamedBufferSubData' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glClearNamedBufferSubData(GLuint "
        "buffer, GLenum internalformat, GLintptr offset, GLsizeiptr size, "
        "GLenum format, GLenum type, const void *data)': names 'void', "
        "which has no cute class yet.")

  @staticmethod
  def glClearNamedFramebufferfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glClearNamedFramebufferfv(GLuint
    framebuffer, GLenum buffer, GLint drawbuffer, const GLfloat *value)':
    names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glClearNamedFramebufferfv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glClearNamedFramebufferfv(GLuint "
        "framebuffer, GLenum buffer, GLint drawbuffer, const GLfloat "
        "*value)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glClearNamedFramebufferiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glClearNamedFramebufferiv(GLuint
    framebuffer, GLenum buffer, GLint drawbuffer, const GLint *value)': names
    'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glClearNamedFramebufferiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glClearNamedFramebufferiv(GLuint "
        "framebuffer, GLenum buffer, GLint drawbuffer, const GLint "
        "*value)': names 'GLint', which has no cute class yet.")

  @staticmethod
  def glClearNamedFramebufferuiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glClearNamedFramebufferuiv(GLuint
    framebuffer, GLenum buffer, GLint drawbuffer, const GLuint *value)':
    names 'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glClearNamedFramebufferuiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glClearNamedFramebufferuiv(GLuint "
        "framebuffer, GLenum buffer, GLint drawbuffer, const GLuint "
        "*value)': names 'GLuint', which has no cute class yet.")

  @staticmethod
  def glClearTexImage(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glClearTexImage(GLuint texture,
    GLint level, GLenum format, GLenum type, const void *data)': names
    'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glClearTexImage' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_5_Core::glClearTexImage(GLuint "
        "texture, GLint level, GLenum format, GLenum type, const void "
        "*data)': names 'void', which has no cute class yet.")

  @staticmethod
  def glClearTexSubImage(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glClearTexSubImage(GLuint texture,
    GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width,
    GLsizei height, GLsizei depth, GLenum format, GLenum type, const void
    *data)': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glClearTexSubImage' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glClearTexSubImage(GLuint texture, "
        "GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei "
        "width, GLsizei height, GLsizei depth, GLenum format, GLenum type, "
        "const void *data)': names 'void', which has no cute class yet.")

  @staticmethod
  def glClientWaitSync(*__, **_) -> Never:
    """
    Qt's 'GLenum QOpenGLFunctions_4_5_Core::glClientWaitSync(GLsync sync,
    GLbitfield flags, GLuint64 timeout)': names 'struct __GLsync', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glClientWaitSync' has no cute function "
        "yet. Qt's 'GLenum "
        "QOpenGLFunctions_4_5_Core::glClientWaitSync(GLsync sync, "
        "GLbitfield flags, GLuint64 timeout)': names 'struct __GLsync', "
        "which has no cute class yet.")

  @staticmethod
  def glCompressedTexImage1D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glCompressedTexImage1D(GLenum
    target, GLint level, GLenum internalformat, GLsizei width, GLint border,
    GLsizei imageSize, const void *data)': names 'void', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glCompressedTexImage1D' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glCompressedTexImage1D(GLenum target, "
        "GLint level, GLenum internalformat, GLsizei width, GLint border, "
        "GLsizei imageSize, const void *data)': names 'void', which has no "
        "cute class yet.")

  @staticmethod
  def glCompressedTexImage2D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glCompressedTexImage2D(GLenum
    target, GLint level, GLenum internalformat, GLsizei width, GLsizei
    height, GLint border, GLsizei imageSize, const void *data)': names
    'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glCompressedTexImage2D' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glCompressedTexImage2D(GLenum target, "
        "GLint level, GLenum internalformat, GLsizei width, GLsizei height, "
        "GLint border, GLsizei imageSize, const void *data)': names 'void', "
        "which has no cute class yet.")

  @staticmethod
  def glCompressedTexImage3D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glCompressedTexImage3D(GLenum
    target, GLint level, GLenum internalformat, GLsizei width, GLsizei
    height, GLsizei depth, GLint border, GLsizei imageSize, const void
    *data)': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glCompressedTexImage3D' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glCompressedTexImage3D(GLenum target, "
        "GLint level, GLenum internalformat, GLsizei width, GLsizei height, "
        "GLsizei depth, GLint border, GLsizei imageSize, const void "
        "*data)': names 'void', which has no cute class yet.")

  @staticmethod
  def glCompressedTexSubImage1D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glCompressedTexSubImage1D(GLenum
    target, GLint level, GLint xoffset, GLsizei width, GLenum format, GLsizei
    imageSize, const void *data)': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glCompressedTexSubImage1D' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glCompressedTexSubImage1D(GLenum "
        "target, GLint level, GLint xoffset, GLsizei width, GLenum format, "
        "GLsizei imageSize, const void *data)': names 'void', which has no "
        "cute class yet.")

  @staticmethod
  def glCompressedTexSubImage2D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glCompressedTexSubImage2D(GLenum
    target, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei
    height, GLenum format, GLsizei imageSize, const void *data)': names
    'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glCompressedTexSubImage2D' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glCompressedTexSubImage2D(GLenum "
        "target, GLint level, GLint xoffset, GLint yoffset, GLsizei width, "
        "GLsizei height, GLenum format, GLsizei imageSize, const void "
        "*data)': names 'void', which has no cute class yet.")

  @staticmethod
  def glCompressedTexSubImage3D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glCompressedTexSubImage3D(GLenum
    target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei
    width, GLsizei height, GLsizei depth, GLenum format, GLsizei imageSize,
    const void *data)': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glCompressedTexSubImage3D' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glCompressedTexSubImage3D(GLenum "
        "target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, "
        "GLsizei width, GLsizei height, GLsizei depth, GLenum format, "
        "GLsizei imageSize, const void *data)': names 'void', which has no "
        "cute class yet.")

  @staticmethod
  def glCompressedTextureSubImage1D(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_5_Core::glCompressedTextureSubImage1D(GLuint texture,
    GLint level, GLint xoffset, GLsizei width, GLenum format, GLsizei
    imageSize, const void *data)': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glCompressedTextureSubImage1D' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glCompressedTextureSubImage1D(GLuint "
        "texture, GLint level, GLint xoffset, GLsizei width, GLenum format, "
        "GLsizei imageSize, const void *data)': names 'void', which has no "
        "cute class yet.")

  @staticmethod
  def glCompressedTextureSubImage2D(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_5_Core::glCompressedTextureSubImage2D(GLuint texture,
    GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height,
    GLenum format, GLsizei imageSize, const void *data)': names 'void', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glCompressedTextureSubImage2D' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glCompressedTextureSubImage2D(GLuint "
        "texture, GLint level, GLint xoffset, GLint yoffset, GLsizei width, "
        "GLsizei height, GLenum format, GLsizei imageSize, const void "
        "*data)': names 'void', which has no cute class yet.")

  @staticmethod
  def glCompressedTextureSubImage3D(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_5_Core::glCompressedTextureSubImage3D(GLuint texture,
    GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width,
    GLsizei height, GLsizei depth, GLenum format, GLsizei imageSize, const
    void *data)': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glCompressedTextureSubImage3D' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glCompressedTextureSubImage3D(GLuint "
        "texture, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, "
        "GLsizei width, GLsizei height, GLsizei depth, GLenum format, "
        "GLsizei imageSize, const void *data)': names 'void', which has no "
        "cute class yet.")

  @staticmethod
  def glCreateBuffers(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glCreateBuffers(GLsizei n, GLuint
    *buffers)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glCreateBuffers' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_5_Core::glCreateBuffers(GLsizei "
        "n, GLuint *buffers)': takes a number to change where it is.")

  @staticmethod
  def glCreateFramebuffers(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glCreateFramebuffers(GLsizei n,
    GLuint *framebuffers)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glCreateFramebuffers' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glCreateFramebuffers(GLsizei n, GLuint "
        "*framebuffers)': takes a number to change where it is.")

  @staticmethod
  def glCreateProgramPipelines(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glCreateProgramPipelines(GLsizei n,
    GLuint *pipelines)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glCreateProgramPipelines' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glCreateProgramPipelines(GLsizei n, "
        "GLuint *pipelines)': takes a number to change where it is.")

  @staticmethod
  def glCreateQueries(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glCreateQueries(GLenum target,
    GLsizei n, GLuint *ids)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glCreateQueries' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_5_Core::glCreateQueries(GLenum "
        "target, GLsizei n, GLuint *ids)': takes a number to change where "
        "it is.")

  @staticmethod
  def glCreateRenderbuffers(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glCreateRenderbuffers(GLsizei n,
    GLuint *renderbuffers)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glCreateRenderbuffers' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glCreateRenderbuffers(GLsizei n, GLuint "
        "*renderbuffers)': takes a number to change where it is.")

  @staticmethod
  def glCreateSamplers(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glCreateSamplers(GLsizei n, GLuint
    *samplers)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glCreateSamplers' has no cute function "
        "yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glCreateSamplers(GLsizei n, GLuint "
        "*samplers)': takes a number to change where it is.")

  @staticmethod
  def glCreateShaderProgramv(*__, **_) -> Never:
    """
    Qt's 'GLuint QOpenGLFunctions_4_5_Core::glCreateShaderProgramv(GLenum
    type, GLsizei count, const GLchar *const *strings)': names 'GLchar
    *const', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glCreateShaderProgramv' has no cute "
        "function yet. Qt's 'GLuint "
        "QOpenGLFunctions_4_5_Core::glCreateShaderProgramv(GLenum type, "
        "GLsizei count, const GLchar *const *strings)': names 'GLchar "
        "*const', which has no cute class yet.")

  @staticmethod
  def glCreateTextures(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glCreateTextures(GLenum target,
    GLsizei n, GLuint *textures)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glCreateTextures' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_5_Core::glCreateTextures(GLenum "
        "target, GLsizei n, GLuint *textures)': takes a number to change "
        "where it is.")

  @staticmethod
  def glCreateTransformFeedbacks(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glCreateTransformFeedbacks(GLsizei
    n, GLuint *ids)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glCreateTransformFeedbacks' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glCreateTransformFeedbacks(GLsizei n, "
        "GLuint *ids)': takes a number to change where it is.")

  @staticmethod
  def glCreateVertexArrays(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glCreateVertexArrays(GLsizei n,
    GLuint *arrays)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glCreateVertexArrays' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glCreateVertexArrays(GLsizei n, GLuint "
        "*arrays)': takes a number to change where it is.")

  @staticmethod
  def glDebugMessageCallback(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glDebugMessageCallback(GLDEBUGPROC
    callback, const void *userParam)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glDebugMessageCallback' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glDebugMessageCallback(GLDEBUGPROC "
        "callback, const void *userParam)': takes a type Python has no way "
        "to hand over yet.")

  @staticmethod
  def glDebugMessageControl(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glDebugMessageControl(GLenum
    source, GLenum type, GLenum severity, GLsizei count, const GLuint *ids,
    GLboolean enabled)': names 'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glDebugMessageControl' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glDebugMessageControl(GLenum source, "
        "GLenum type, GLenum severity, GLsizei count, const GLuint *ids, "
        "GLboolean enabled)': names 'GLuint', which has no cute class yet.")

  @staticmethod
  def glDebugMessageInsert(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glDebugMessageInsert(GLenum source,
    GLenum type, GLuint id, GLenum severity, GLsizei length, const GLchar
    *buf)': names 'GLchar', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glDebugMessageInsert' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glDebugMessageInsert(GLenum source, "
        "GLenum type, GLuint id, GLenum severity, GLsizei length, const "
        "GLchar *buf)': names 'GLchar', which has no cute class yet.")

  @staticmethod
  def glDeleteBuffers(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glDeleteBuffers(GLsizei n, const
    GLuint *buffers)': names 'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glDeleteBuffers' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_5_Core::glDeleteBuffers(GLsizei "
        "n, const GLuint *buffers)': names 'GLuint', which has no cute "
        "class yet.")

  @staticmethod
  def glDeleteFramebuffers(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glDeleteFramebuffers(GLsizei n,
    const GLuint *framebuffers)': names 'GLuint', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glDeleteFramebuffers' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glDeleteFramebuffers(GLsizei n, const "
        "GLuint *framebuffers)': names 'GLuint', which has no cute class "
        "yet.")

  @staticmethod
  def glDeleteProgramPipelines(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glDeleteProgramPipelines(GLsizei n,
    const GLuint *pipelines)': names 'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glDeleteProgramPipelines' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glDeleteProgramPipelines(GLsizei n, "
        "const GLuint *pipelines)': names 'GLuint', which has no cute class "
        "yet.")

  @staticmethod
  def glDeleteQueries(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glDeleteQueries(GLsizei n, const
    GLuint *ids)': names 'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glDeleteQueries' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_5_Core::glDeleteQueries(GLsizei "
        "n, const GLuint *ids)': names 'GLuint', which has no cute class "
        "yet.")

  @staticmethod
  def glDeleteRenderbuffers(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glDeleteRenderbuffers(GLsizei n,
    const GLuint *renderbuffers)': names 'GLuint', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glDeleteRenderbuffers' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glDeleteRenderbuffers(GLsizei n, const "
        "GLuint *renderbuffers)': names 'GLuint', which has no cute class "
        "yet.")

  @staticmethod
  def glDeleteSamplers(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glDeleteSamplers(GLsizei count,
    const GLuint *samplers)': names 'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glDeleteSamplers' has no cute function "
        "yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glDeleteSamplers(GLsizei count, const "
        "GLuint *samplers)': names 'GLuint', which has no cute class yet.")

  @staticmethod
  def glDeleteSync(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glDeleteSync(GLsync sync)': names
    'struct __GLsync', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glDeleteSync' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_4_5_Core::glDeleteSync(GLsync sync)': "
        "names 'struct __GLsync', which has no cute class yet.")

  @staticmethod
  def glDeleteTextures(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glDeleteTextures(GLsizei n, const
    GLuint *textures)': names 'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glDeleteTextures' has no cute function "
        "yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glDeleteTextures(GLsizei n, const "
        "GLuint *textures)': names 'GLuint', which has no cute class yet.")

  @staticmethod
  def glDeleteTransformFeedbacks(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glDeleteTransformFeedbacks(GLsizei
    n, const GLuint *ids)': names 'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glDeleteTransformFeedbacks' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glDeleteTransformFeedbacks(GLsizei n, "
        "const GLuint *ids)': names 'GLuint', which has no cute class yet.")

  @staticmethod
  def glDeleteVertexArrays(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glDeleteVertexArrays(GLsizei n,
    const GLuint *arrays)': names 'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glDeleteVertexArrays' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glDeleteVertexArrays(GLsizei n, const "
        "GLuint *arrays)': names 'GLuint', which has no cute class yet.")

  @staticmethod
  def glDepthRangeArrayv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glDepthRangeArrayv(GLuint first,
    GLsizei count, const GLdouble *v)': names 'GLdouble', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glDepthRangeArrayv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glDepthRangeArrayv(GLuint first, "
        "GLsizei count, const GLdouble *v)': names 'GLdouble', which has no "
        "cute class yet.")

  @staticmethod
  def glDrawArraysIndirect(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glDrawArraysIndirect(GLenum mode,
    const void *indirect)': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glDrawArraysIndirect' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glDrawArraysIndirect(GLenum mode, const "
        "void *indirect)': names 'void', which has no cute class yet.")

  @staticmethod
  def glDrawBuffers(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glDrawBuffers(GLsizei n, const
    GLenum *bufs)': names 'GLenum', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glDrawBuffers' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_5_Core::glDrawBuffers(GLsizei "
        "n, const GLenum *bufs)': names 'GLenum', which has no cute class "
        "yet.")

  @staticmethod
  def glDrawElements(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glDrawElements(GLenum mode, GLsizei
    count, GLenum type, const void *indices)': names 'void', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glDrawElements' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_5_Core::glDrawElements(GLenum "
        "mode, GLsizei count, GLenum type, const void *indices)': names "
        "'void', which has no cute class yet.")

  @staticmethod
  def glDrawElementsBaseVertex(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glDrawElementsBaseVertex(GLenum
    mode, GLsizei count, GLenum type, const void *indices, GLint
    basevertex)': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glDrawElementsBaseVertex' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glDrawElementsBaseVertex(GLenum mode, "
        "GLsizei count, GLenum type, const void *indices, GLint "
        "basevertex)': names 'void', which has no cute class yet.")

  @staticmethod
  def glDrawElementsIndirect(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glDrawElementsIndirect(GLenum mode,
    GLenum type, const void *indirect)': names 'void', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glDrawElementsIndirect' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glDrawElementsIndirect(GLenum mode, "
        "GLenum type, const void *indirect)': names 'void', which has no "
        "cute class yet.")

  @staticmethod
  def glDrawElementsInstanced(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glDrawElementsInstanced(GLenum
    mode, GLsizei count, GLenum type, const void *indices, GLsizei
    instancecount)': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glDrawElementsInstanced' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glDrawElementsInstanced(GLenum mode, "
        "GLsizei count, GLenum type, const void *indices, GLsizei "
        "instancecount)': names 'void', which has no cute class yet.")

  @staticmethod
  def glDrawElementsInstancedBaseInstance(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_5_Core::glDrawElementsInstancedBaseInstance(GLenum
    mode, GLsizei count, GLenum type, const void *indices, GLsizei
    instancecount, GLuint baseinstance)': names 'void', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glDrawElementsInstancedBaseInstance' "
        "has no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glDrawElementsInstancedBaseInstance(GLen"
        "um mode, GLsizei count, GLenum type, const void *indices, GLsizei "
        "instancecount, GLuint baseinstance)': names 'void', which has no "
        "cute class yet.")

  @staticmethod
  def glDrawElementsInstancedBaseVertex(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_5_Core::glDrawElementsInstancedBaseVertex(GLenum mode,
    GLsizei count, GLenum type, const void *indices, GLsizei instancecount,
    GLint basevertex)': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glDrawElementsInstancedBaseVertex' has "
        "no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glDrawElementsInstancedBaseVertex(GLenum"
        " mode, GLsizei count, GLenum type, const void *indices, GLsizei "
        "instancecount, GLint basevertex)': names 'void', which has no cute "
        "class yet.")

  @staticmethod
  def glDrawElementsInstancedBaseVertexBaseInstance(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_5_Core::glDrawElementsInstancedBaseVertexBaseInstance(
    GLenum mode, GLsizei count, GLenum type, const void *indices, GLsizei
    instancecount, GLint basevertex, GLuint baseinstance)': names 'void',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glDrawElementsInstancedBaseVertexBaseIns"
        "tance' has no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glDrawElementsInstancedBaseVertexBaseIns"
        "tance(GLenum mode, GLsizei count, GLenum type, const void "
        "*indices, GLsizei instancecount, GLint basevertex, GLuint "
        "baseinstance)': names 'void', which has no cute class yet.")

  @staticmethod
  def glDrawRangeElements(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glDrawRangeElements(GLenum mode,
    GLuint start, GLuint end, GLsizei count, GLenum type, const void
    *indices)': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glDrawRangeElements' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glDrawRangeElements(GLenum mode, GLuint "
        "start, GLuint end, GLsizei count, GLenum type, const void "
        "*indices)': names 'void', which has no cute class yet.")

  @staticmethod
  def glDrawRangeElementsBaseVertex(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_5_Core::glDrawRangeElementsBaseVertex(GLenum mode,
    GLuint start, GLuint end, GLsizei count, GLenum type, const void
    *indices, GLint basevertex)': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glDrawRangeElementsBaseVertex' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glDrawRangeElementsBaseVertex(GLenum "
        "mode, GLuint start, GLuint end, GLsizei count, GLenum type, const "
        "void *indices, GLint basevertex)': names 'void', which has no cute "
        "class yet.")

  @staticmethod
  def glFenceSync(*__, **_) -> Never:
    """
    Qt's 'GLsync QOpenGLFunctions_4_5_Core::glFenceSync(GLenum condition,
    GLbitfield flags)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glFenceSync' has no cute function yet. "
        "Qt's 'GLsync QOpenGLFunctions_4_5_Core::glFenceSync(GLenum "
        "condition, GLbitfield flags)': gives a type Python has no way to "
        "take yet.")

  @staticmethod
  def glGenBuffers(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGenBuffers(GLsizei n, GLuint
    *buffers)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGenBuffers' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_4_5_Core::glGenBuffers(GLsizei n, "
        "GLuint *buffers)': takes a number to change where it is.")

  @staticmethod
  def glGenFramebuffers(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGenFramebuffers(GLsizei n, GLuint
    *framebuffers)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGenFramebuffers' has no cute function "
        "yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGenFramebuffers(GLsizei n, GLuint "
        "*framebuffers)': takes a number to change where it is.")

  @staticmethod
  def glGenProgramPipelines(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGenProgramPipelines(GLsizei n,
    GLuint *pipelines)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGenProgramPipelines' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGenProgramPipelines(GLsizei n, GLuint "
        "*pipelines)': takes a number to change where it is.")

  @staticmethod
  def glGenQueries(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGenQueries(GLsizei n, GLuint
    *ids)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGenQueries' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_4_5_Core::glGenQueries(GLsizei n, "
        "GLuint *ids)': takes a number to change where it is.")

  @staticmethod
  def glGenRenderbuffers(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGenRenderbuffers(GLsizei n,
    GLuint *renderbuffers)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGenRenderbuffers' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGenRenderbuffers(GLsizei n, GLuint "
        "*renderbuffers)': takes a number to change where it is.")

  @staticmethod
  def glGenSamplers(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGenSamplers(GLsizei count, GLuint
    *samplers)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGenSamplers' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_5_Core::glGenSamplers(GLsizei "
        "count, GLuint *samplers)': takes a number to change where it is.")

  @staticmethod
  def glGenTextures(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGenTextures(GLsizei n, GLuint
    *textures)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGenTextures' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_5_Core::glGenTextures(GLsizei "
        "n, GLuint *textures)': takes a number to change where it is.")

  @staticmethod
  def glGenTransformFeedbacks(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGenTransformFeedbacks(GLsizei n,
    GLuint *ids)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGenTransformFeedbacks' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGenTransformFeedbacks(GLsizei n, "
        "GLuint *ids)': takes a number to change where it is.")

  @staticmethod
  def glGenVertexArrays(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGenVertexArrays(GLsizei n, GLuint
    *arrays)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGenVertexArrays' has no cute function "
        "yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGenVertexArrays(GLsizei n, GLuint "
        "*arrays)': takes a number to change where it is.")

  @staticmethod
  def glGetActiveAtomicCounterBufferiv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_5_Core::glGetActiveAtomicCounterBufferiv(GLuint
    program, GLuint bufferIndex, GLenum pname, GLint *params)': takes a
    number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetActiveAtomicCounterBufferiv' has "
        "no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetActiveAtomicCounterBufferiv(GLuint "
        "program, GLuint bufferIndex, GLenum pname, GLint *params)': takes "
        "a number to change where it is.")

  @staticmethod
  def glGetActiveAttrib(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetActiveAttrib(GLuint program,
    GLuint index, GLsizei bufSize, GLsizei *length, GLint *size, GLenum
    *type, GLchar *name)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetActiveAttrib' has no cute function "
        "yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetActiveAttrib(GLuint program, "
        "GLuint index, GLsizei bufSize, GLsizei *length, GLint *size, "
        "GLenum *type, GLchar *name)': takes a number to change where it is."
    )

  @staticmethod
  def glGetActiveSubroutineName(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetActiveSubroutineName(GLuint
    program, GLenum shadertype, GLuint index, GLsizei bufsize, GLsizei
    *length, GLchar *name)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetActiveSubroutineName' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetActiveSubroutineName(GLuint "
        "program, GLenum shadertype, GLuint index, GLsizei bufsize, GLsizei "
        "*length, GLchar *name)': takes a number to change where it is.")

  @staticmethod
  def glGetActiveSubroutineUniformName(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_5_Core::glGetActiveSubroutineUniformName(GLuint
    program, GLenum shadertype, GLuint index, GLsizei bufsize, GLsizei
    *length, GLchar *name)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetActiveSubroutineUniformName' has "
        "no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetActiveSubroutineUniformName(GLuint "
        "program, GLenum shadertype, GLuint index, GLsizei bufsize, GLsizei "
        "*length, GLchar *name)': takes a number to change where it is.")

  @staticmethod
  def glGetActiveSubroutineUniformiv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_5_Core::glGetActiveSubroutineUniformiv(GLuint program,
    GLenum shadertype, GLuint index, GLenum pname, GLint *values)': takes a
    number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetActiveSubroutineUniformiv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetActiveSubroutineUniformiv(GLuint "
        "program, GLenum shadertype, GLuint index, GLenum pname, GLint "
        "*values)': takes a number to change where it is.")

  @staticmethod
  def glGetActiveUniform(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetActiveUniform(GLuint program,
    GLuint index, GLsizei bufSize, GLsizei *length, GLint *size, GLenum
    *type, GLchar *name)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetActiveUniform' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetActiveUniform(GLuint program, "
        "GLuint index, GLsizei bufSize, GLsizei *length, GLint *size, "
        "GLenum *type, GLchar *name)': takes a number to change where it is."
    )

  @staticmethod
  def glGetActiveUniformBlockName(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetActiveUniformBlockName(GLuint
    program, GLuint uniformBlockIndex, GLsizei bufSize, GLsizei *length,
    GLchar *uniformBlockName)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetActiveUniformBlockName' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetActiveUniformBlockName(GLuint "
        "program, GLuint uniformBlockIndex, GLsizei bufSize, GLsizei "
        "*length, GLchar *uniformBlockName)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetActiveUniformBlockiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetActiveUniformBlockiv(GLuint
    program, GLuint uniformBlockIndex, GLenum pname, GLint *params)': takes a
    number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetActiveUniformBlockiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetActiveUniformBlockiv(GLuint "
        "program, GLuint uniformBlockIndex, GLenum pname, GLint *params)': "
        "takes a number to change where it is.")

  @staticmethod
  def glGetActiveUniformName(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetActiveUniformName(GLuint
    program, GLuint uniformIndex, GLsizei bufSize, GLsizei *length, GLchar
    *uniformName)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetActiveUniformName' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetActiveUniformName(GLuint program, "
        "GLuint uniformIndex, GLsizei bufSize, GLsizei *length, GLchar "
        "*uniformName)': takes a number to change where it is.")

  @staticmethod
  def glGetActiveUniformsiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetActiveUniformsiv(GLuint
    program, GLsizei uniformCount, const GLuint *uniformIndices, GLenum
    pname, GLint *params)': names 'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetActiveUniformsiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetActiveUniformsiv(GLuint program, "
        "GLsizei uniformCount, const GLuint *uniformIndices, GLenum pname, "
        "GLint *params)': names 'GLuint', which has no cute class yet.")

  @staticmethod
  def glGetAttachedShaders(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetAttachedShaders(GLuint
    program, GLsizei maxCount, GLsizei *count, GLuint *shaders)': takes a
    number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetAttachedShaders' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetAttachedShaders(GLuint program, "
        "GLsizei maxCount, GLsizei *count, GLuint *shaders)': takes a "
        "number to change where it is.")

  @staticmethod
  def glGetAttribLocation(*__, **_) -> Never:
    """
    Qt's 'GLint QOpenGLFunctions_4_5_Core::glGetAttribLocation(GLuint
    program, const GLchar *name)': names 'GLchar', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetAttribLocation' has no cute "
        "function yet. Qt's 'GLint "
        "QOpenGLFunctions_4_5_Core::glGetAttribLocation(GLuint program, "
        "const GLchar *name)': names 'GLchar', which has no cute class yet.")

  @staticmethod
  def glGetBooleani_v(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetBooleani_v(GLenum target,
    GLuint index, GLboolean *data)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetBooleani_v' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_5_Core::glGetBooleani_v(GLenum "
        "target, GLuint index, GLboolean *data)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetBooleanv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetBooleanv(GLenum pname,
    GLboolean *data)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetBooleanv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_5_Core::glGetBooleanv(GLenum "
        "pname, GLboolean *data)': takes a number to change where it is.")

  @staticmethod
  def glGetBufferParameteri64v(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetBufferParameteri64v(GLenum
    target, GLenum pname, GLint64 *params)': takes a number to change where
    it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetBufferParameteri64v' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetBufferParameteri64v(GLenum target, "
        "GLenum pname, GLint64 *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetBufferParameteriv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetBufferParameteriv(GLenum
    target, GLenum pname, GLint *params)': takes a number to change where it
    is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetBufferParameteriv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetBufferParameteriv(GLenum target, "
        "GLenum pname, GLint *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetBufferPointerv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetBufferPointerv(GLenum target,
    GLenum pname, void **params)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetBufferPointerv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetBufferPointerv(GLenum target, "
        "GLenum pname, void **params)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def glGetBufferSubData(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetBufferSubData(GLenum target,
    GLintptr offset, GLsizeiptr size, void *data)': names 'void', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetBufferSubData' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetBufferSubData(GLenum target, "
        "GLintptr offset, GLsizeiptr size, void *data)': names 'void', "
        "which has no cute class yet.")

  @staticmethod
  def glGetCompressedTexImage(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetCompressedTexImage(GLenum
    target, GLint level, void *img)': names 'void', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetCompressedTexImage' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetCompressedTexImage(GLenum target, "
        "GLint level, void *img)': names 'void', which has no cute class "
        "yet.")

  @staticmethod
  def glGetCompressedTextureImage(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetCompressedTextureImage(GLuint
    texture, GLint level, GLsizei bufSize, void *pixels)': names 'void',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetCompressedTextureImage' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetCompressedTextureImage(GLuint "
        "texture, GLint level, GLsizei bufSize, void *pixels)': names "
        "'void', which has no cute class yet.")

  @staticmethod
  def glGetCompressedTextureSubImage(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_5_Core::glGetCompressedTextureSubImage(GLuint texture,
    GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width,
    GLsizei height, GLsizei depth, GLsizei bufSize, void *pixels)': names
    'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetCompressedTextureSubImage' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetCompressedTextureSubImage(GLuint "
        "texture, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, "
        "GLsizei width, GLsizei height, GLsizei depth, GLsizei bufSize, "
        "void *pixels)': names 'void', which has no cute class yet.")

  @staticmethod
  def glGetDebugMessageLog(*__, **_) -> Never:
    """
    Qt's 'GLuint QOpenGLFunctions_4_5_Core::glGetDebugMessageLog(GLuint
    count, GLsizei bufSize, GLenum *sources, GLenum *types, GLuint *ids,
    GLenum *severities, GLsizei *lengths, GLchar *messageLog)': takes a
    number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetDebugMessageLog' has no cute "
        "function yet. Qt's 'GLuint "
        "QOpenGLFunctions_4_5_Core::glGetDebugMessageLog(GLuint count, "
        "GLsizei bufSize, GLenum *sources, GLenum *types, GLuint *ids, "
        "GLenum *severities, GLsizei *lengths, GLchar *messageLog)': takes "
        "a number to change where it is.")

  @staticmethod
  def glGetDoublei_v(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetDoublei_v(GLenum target,
    GLuint index, GLdouble *data)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetDoublei_v' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_5_Core::glGetDoublei_v(GLenum "
        "target, GLuint index, GLdouble *data)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetDoublev(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetDoublev(GLenum pname, GLdouble
    *data)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetDoublev' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_4_5_Core::glGetDoublev(GLenum pname, "
        "GLdouble *data)': takes a number to change where it is.")

  @staticmethod
  def glGetFloati_v(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetFloati_v(GLenum target, GLuint
    index, GLfloat *data)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetFloati_v' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_5_Core::glGetFloati_v(GLenum "
        "target, GLuint index, GLfloat *data)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetFloatv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetFloatv(GLenum pname, GLfloat
    *data)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetFloatv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_4_5_Core::glGetFloatv(GLenum pname, "
        "GLfloat *data)': takes a number to change where it is.")

  @staticmethod
  def glGetFragDataIndex(*__, **_) -> Never:
    """
    Qt's 'GLint QOpenGLFunctions_4_5_Core::glGetFragDataIndex(GLuint program,
    const GLchar *name)': names 'GLchar', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetFragDataIndex' has no cute "
        "function yet. Qt's 'GLint "
        "QOpenGLFunctions_4_5_Core::glGetFragDataIndex(GLuint program, "
        "const GLchar *name)': names 'GLchar', which has no cute class yet.")

  @staticmethod
  def glGetFragDataLocation(*__, **_) -> Never:
    """
    Qt's 'GLint QOpenGLFunctions_4_5_Core::glGetFragDataLocation(GLuint
    program, const GLchar *name)': names 'GLchar', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetFragDataLocation' has no cute "
        "function yet. Qt's 'GLint "
        "QOpenGLFunctions_4_5_Core::glGetFragDataLocation(GLuint program, "
        "const GLchar *name)': names 'GLchar', which has no cute class yet.")

  @staticmethod
  def glGetFramebufferAttachmentParameteriv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_5_Core::glGetFramebufferAttachmentParameteriv(GLenum
    target, GLenum attachment, GLenum pname, GLint *params)': takes a number
    to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetFramebufferAttachmentParameteriv' "
        "has no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetFramebufferAttachmentParameteriv(GL"
        "enum target, GLenum attachment, GLenum pname, GLint *params)': "
        "takes a number to change where it is.")

  @staticmethod
  def glGetFramebufferParameteriv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetFramebufferParameteriv(GLenum
    target, GLenum pname, GLint *params)': takes a number to change where it
    is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetFramebufferParameteriv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetFramebufferParameteriv(GLenum "
        "target, GLenum pname, GLint *params)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetInteger64i_v(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetInteger64i_v(GLenum target,
    GLuint index, GLint64 *data)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetInteger64i_v' has no cute function "
        "yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetInteger64i_v(GLenum target, GLuint "
        "index, GLint64 *data)': takes a number to change where it is.")

  @staticmethod
  def glGetInteger64v(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetInteger64v(GLenum pname,
    GLint64 *data)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetInteger64v' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_5_Core::glGetInteger64v(GLenum "
        "pname, GLint64 *data)': takes a number to change where it is.")

  @staticmethod
  def glGetIntegeri_v(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetIntegeri_v(GLenum target,
    GLuint index, GLint *data)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetIntegeri_v' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_5_Core::glGetIntegeri_v(GLenum "
        "target, GLuint index, GLint *data)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetIntegerv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetIntegerv(GLenum pname, GLint
    *data)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetIntegerv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_5_Core::glGetIntegerv(GLenum "
        "pname, GLint *data)': takes a number to change where it is.")

  @staticmethod
  def glGetInternalformati64v(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetInternalformati64v(GLenum
    target, GLenum internalformat, GLenum pname, GLsizei bufSize, GLint64
    *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetInternalformati64v' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetInternalformati64v(GLenum target, "
        "GLenum internalformat, GLenum pname, GLsizei bufSize, GLint64 "
        "*params)': takes a number to change where it is.")

  @staticmethod
  def glGetInternalformativ(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetInternalformativ(GLenum
    target, GLenum internalformat, GLenum pname, GLsizei bufSize, GLint
    *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetInternalformativ' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetInternalformativ(GLenum target, "
        "GLenum internalformat, GLenum pname, GLsizei bufSize, GLint "
        "*params)': takes a number to change where it is.")

  @staticmethod
  def glGetMultisamplefv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetMultisamplefv(GLenum pname,
    GLuint index, GLfloat *val)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetMultisamplefv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetMultisamplefv(GLenum pname, GLuint "
        "index, GLfloat *val)': takes a number to change where it is.")

  @staticmethod
  def glGetNamedBufferParameteri64v(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_5_Core::glGetNamedBufferParameteri64v(GLuint buffer,
    GLenum pname, GLint64 *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetNamedBufferParameteri64v' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetNamedBufferParameteri64v(GLuint "
        "buffer, GLenum pname, GLint64 *params)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetNamedBufferParameteriv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetNamedBufferParameteriv(GLuint
    buffer, GLenum pname, GLint *params)': takes a number to change where it
    is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetNamedBufferParameteriv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetNamedBufferParameteriv(GLuint "
        "buffer, GLenum pname, GLint *params)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetNamedBufferPointerv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetNamedBufferPointerv(GLuint
    buffer, GLenum pname, void **params)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetNamedBufferPointerv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetNamedBufferPointerv(GLuint buffer, "
        "GLenum pname, void **params)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def glGetNamedBufferSubData(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetNamedBufferSubData(GLuint
    buffer, GLintptr offset, GLsizeiptr size, void *data)': names 'void',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetNamedBufferSubData' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetNamedBufferSubData(GLuint buffer, "
        "GLintptr offset, GLsizeiptr size, void *data)': names 'void', "
        "which has no cute class yet.")

  @staticmethod
  def glGetNamedFramebufferAttachmentParameteriv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_5_Core::glGetNamedFramebufferAttachmentParameteriv(
    GLuint framebuffer, GLenum attachment, GLenum pname, GLint *params)':
    takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetNamedFramebufferAttachmentParameter"
        "iv' has no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetNamedFramebufferAttachmentParameter"
        "iv(GLuint framebuffer, GLenum attachment, GLenum pname, GLint "
        "*params)': takes a number to change where it is.")

  @staticmethod
  def glGetNamedFramebufferParameteriv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_5_Core::glGetNamedFramebufferParameteriv(GLuint
    framebuffer, GLenum pname, GLint *param)': takes a number to change where
    it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetNamedFramebufferParameteriv' has "
        "no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetNamedFramebufferParameteriv(GLuint "
        "framebuffer, GLenum pname, GLint *param)': takes a number to "
        "change where it is.")

  @staticmethod
  def glGetNamedRenderbufferParameteriv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_5_Core::glGetNamedRenderbufferParameteriv(GLuint
    renderbuffer, GLenum pname, GLint *params)': takes a number to change
    where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetNamedRenderbufferParameteriv' has "
        "no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetNamedRenderbufferParameteriv(GLuint"
        " renderbuffer, GLenum pname, GLint *params)': takes a number to "
        "change where it is.")

  @staticmethod
  def glGetObjectLabel(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetObjectLabel(GLenum identifier,
    GLuint name, GLsizei bufSize, GLsizei *length, GLchar *label)': takes a
    number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetObjectLabel' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_5_Core::glGetObjectLabel(GLenum "
        "identifier, GLuint name, GLsizei bufSize, GLsizei *length, GLchar "
        "*label)': takes a number to change where it is.")

  @staticmethod
  def glGetObjectPtrLabel(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetObjectPtrLabel(const void
    *ptr, GLsizei bufSize, GLsizei *length, GLchar *label)': names 'void',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetObjectPtrLabel' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetObjectPtrLabel(const void *ptr, "
        "GLsizei bufSize, GLsizei *length, GLchar *label)': names 'void', "
        "which has no cute class yet.")

  @staticmethod
  def glGetProgramBinary(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetProgramBinary(GLuint program,
    GLsizei bufSize, GLsizei *length, GLenum *binaryFormat, void *binary)':
    takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetProgramBinary' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetProgramBinary(GLuint program, "
        "GLsizei bufSize, GLsizei *length, GLenum *binaryFormat, void "
        "*binary)': takes a number to change where it is.")

  @staticmethod
  def glGetProgramInfoLog(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetProgramInfoLog(GLuint program,
    GLsizei bufSize, GLsizei *length, GLchar *infoLog)': takes a number to
    change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetProgramInfoLog' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetProgramInfoLog(GLuint program, "
        "GLsizei bufSize, GLsizei *length, GLchar *infoLog)': takes a "
        "number to change where it is.")

  @staticmethod
  def glGetProgramInterfaceiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetProgramInterfaceiv(GLuint
    program, GLenum programInterface, GLenum pname, GLint *params)': takes a
    number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetProgramInterfaceiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetProgramInterfaceiv(GLuint program, "
        "GLenum programInterface, GLenum pname, GLint *params)': takes a "
        "number to change where it is.")

  @staticmethod
  def glGetProgramPipelineInfoLog(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetProgramPipelineInfoLog(GLuint
    pipeline, GLsizei bufSize, GLsizei *length, GLchar *infoLog)': takes a
    number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetProgramPipelineInfoLog' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetProgramPipelineInfoLog(GLuint "
        "pipeline, GLsizei bufSize, GLsizei *length, GLchar *infoLog)': "
        "takes a number to change where it is.")

  @staticmethod
  def glGetProgramPipelineiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetProgramPipelineiv(GLuint
    pipeline, GLenum pname, GLint *params)': takes a number to change where
    it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetProgramPipelineiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetProgramPipelineiv(GLuint pipeline, "
        "GLenum pname, GLint *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetProgramResourceIndex(*__, **_) -> Never:
    """
    Qt's 'GLuint QOpenGLFunctions_4_5_Core::glGetProgramResourceIndex(GLuint
    program, GLenum programInterface, const GLchar *name)': names 'GLchar',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetProgramResourceIndex' has no cute "
        "function yet. Qt's 'GLuint "
        "QOpenGLFunctions_4_5_Core::glGetProgramResourceIndex(GLuint "
        "program, GLenum programInterface, const GLchar *name)': names "
        "'GLchar', which has no cute class yet.")

  @staticmethod
  def glGetProgramResourceLocation(*__, **_) -> Never:
    """
    Qt's 'GLint
    QOpenGLFunctions_4_5_Core::glGetProgramResourceLocation(GLuint program,
    GLenum programInterface, const GLchar *name)': names 'GLchar', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetProgramResourceLocation' has no "
        "cute function yet. Qt's 'GLint "
        "QOpenGLFunctions_4_5_Core::glGetProgramResourceLocation(GLuint "
        "program, GLenum programInterface, const GLchar *name)': names "
        "'GLchar', which has no cute class yet.")

  @staticmethod
  def glGetProgramResourceLocationIndex(*__, **_) -> Never:
    """
    Qt's 'GLint
    QOpenGLFunctions_4_5_Core::glGetProgramResourceLocationIndex(GLuint
    program, GLenum programInterface, const GLchar *name)': names 'GLchar',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetProgramResourceLocationIndex' has "
        "no cute function yet. Qt's 'GLint "
        "QOpenGLFunctions_4_5_Core::glGetProgramResourceLocationIndex(GLuint"
        " program, GLenum programInterface, const GLchar *name)': names "
        "'GLchar', which has no cute class yet.")

  @staticmethod
  def glGetProgramResourceName(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetProgramResourceName(GLuint
    program, GLenum programInterface, GLuint index, GLsizei bufSize, GLsizei
    *length, GLchar *name)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetProgramResourceName' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetProgramResourceName(GLuint "
        "program, GLenum programInterface, GLuint index, GLsizei bufSize, "
        "GLsizei *length, GLchar *name)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetProgramResourceiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetProgramResourceiv(GLuint
    program, GLenum programInterface, GLuint index, GLsizei propCount, const
    GLenum *props, GLsizei bufSize, GLsizei *length, GLint *params)': names
    'GLenum', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetProgramResourceiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetProgramResourceiv(GLuint program, "
        "GLenum programInterface, GLuint index, GLsizei propCount, const "
        "GLenum *props, GLsizei bufSize, GLsizei *length, GLint *params)': "
        "names 'GLenum', which has no cute class yet.")

  @staticmethod
  def glGetProgramStageiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetProgramStageiv(GLuint program,
    GLenum shadertype, GLenum pname, GLint *values)': takes a number to
    change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetProgramStageiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetProgramStageiv(GLuint program, "
        "GLenum shadertype, GLenum pname, GLint *values)': takes a number "
        "to change where it is.")

  @staticmethod
  def glGetProgramiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetProgramiv(GLuint program,
    GLenum pname, GLint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetProgramiv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_5_Core::glGetProgramiv(GLuint "
        "program, GLenum pname, GLint *params)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetQueryIndexediv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetQueryIndexediv(GLenum target,
    GLuint index, GLenum pname, GLint *params)': takes a number to change
    where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetQueryIndexediv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetQueryIndexediv(GLenum target, "
        "GLuint index, GLenum pname, GLint *params)': takes a number to "
        "change where it is.")

  @staticmethod
  def glGetQueryObjecti64v(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetQueryObjecti64v(GLuint id,
    GLenum pname, GLint64 *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetQueryObjecti64v' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetQueryObjecti64v(GLuint id, GLenum "
        "pname, GLint64 *params)': takes a number to change where it is.")

  @staticmethod
  def glGetQueryObjectiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetQueryObjectiv(GLuint id,
    GLenum pname, GLint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetQueryObjectiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetQueryObjectiv(GLuint id, GLenum "
        "pname, GLint *params)': takes a number to change where it is.")

  @staticmethod
  def glGetQueryObjectui64v(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetQueryObjectui64v(GLuint id,
    GLenum pname, GLuint64 *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetQueryObjectui64v' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetQueryObjectui64v(GLuint id, GLenum "
        "pname, GLuint64 *params)': takes a number to change where it is.")

  @staticmethod
  def glGetQueryObjectuiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetQueryObjectuiv(GLuint id,
    GLenum pname, GLuint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetQueryObjectuiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetQueryObjectuiv(GLuint id, GLenum "
        "pname, GLuint *params)': takes a number to change where it is.")

  @staticmethod
  def glGetQueryiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetQueryiv(GLenum target, GLenum
    pname, GLint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetQueryiv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_4_5_Core::glGetQueryiv(GLenum target, "
        "GLenum pname, GLint *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetRenderbufferParameteriv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetRenderbufferParameteriv(GLenum
    target, GLenum pname, GLint *params)': takes a number to change where it
    is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetRenderbufferParameteriv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetRenderbufferParameteriv(GLenum "
        "target, GLenum pname, GLint *params)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetSamplerParameterIiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetSamplerParameterIiv(GLuint
    sampler, GLenum pname, GLint *params)': takes a number to change where it
    is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetSamplerParameterIiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetSamplerParameterIiv(GLuint "
        "sampler, GLenum pname, GLint *params)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetSamplerParameterIuiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetSamplerParameterIuiv(GLuint
    sampler, GLenum pname, GLuint *params)': takes a number to change where
    it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetSamplerParameterIuiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetSamplerParameterIuiv(GLuint "
        "sampler, GLenum pname, GLuint *params)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetSamplerParameterfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetSamplerParameterfv(GLuint
    sampler, GLenum pname, GLfloat *params)': takes a number to change where
    it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetSamplerParameterfv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetSamplerParameterfv(GLuint sampler, "
        "GLenum pname, GLfloat *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetSamplerParameteriv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetSamplerParameteriv(GLuint
    sampler, GLenum pname, GLint *params)': takes a number to change where it
    is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetSamplerParameteriv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetSamplerParameteriv(GLuint sampler, "
        "GLenum pname, GLint *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetShaderInfoLog(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetShaderInfoLog(GLuint shader,
    GLsizei bufSize, GLsizei *length, GLchar *infoLog)': takes a number to
    change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetShaderInfoLog' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetShaderInfoLog(GLuint shader, "
        "GLsizei bufSize, GLsizei *length, GLchar *infoLog)': takes a "
        "number to change where it is.")

  @staticmethod
  def glGetShaderPrecisionFormat(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetShaderPrecisionFormat(GLenum
    shadertype, GLenum precisiontype, GLint *range, GLint *precision)': takes
    a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetShaderPrecisionFormat' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetShaderPrecisionFormat(GLenum "
        "shadertype, GLenum precisiontype, GLint *range, GLint "
        "*precision)': takes a number to change where it is.")

  @staticmethod
  def glGetShaderSource(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetShaderSource(GLuint shader,
    GLsizei bufSize, GLsizei *length, GLchar *source)': takes a number to
    change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetShaderSource' has no cute function "
        "yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetShaderSource(GLuint shader, "
        "GLsizei bufSize, GLsizei *length, GLchar *source)': takes a number "
        "to change where it is.")

  @staticmethod
  def glGetShaderiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetShaderiv(GLuint shader, GLenum
    pname, GLint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetShaderiv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_5_Core::glGetShaderiv(GLuint "
        "shader, GLenum pname, GLint *params)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetString(*__, **_) -> Never:
    """
    Qt's 'const GLubyte *QOpenGLFunctions_4_5_Core::glGetString(GLenum
    name)': gives 'unsigned char', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetString' has no cute function yet. "
        "Qt's 'const GLubyte *QOpenGLFunctions_4_5_Core::glGetString(GLenum "
        "name)': gives 'unsigned char', which has no cute class yet.")

  @staticmethod
  def glGetStringi(*__, **_) -> Never:
    """
    Qt's 'const GLubyte *QOpenGLFunctions_4_5_Core::glGetStringi(GLenum name,
    GLuint index)': gives 'unsigned char', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetStringi' has no cute function yet. "
        "Qt's 'const GLubyte "
        "*QOpenGLFunctions_4_5_Core::glGetStringi(GLenum name, GLuint "
        "index)': gives 'unsigned char', which has no cute class yet.")

  @staticmethod
  def glGetSubroutineIndex(*__, **_) -> Never:
    """
    Qt's 'GLuint QOpenGLFunctions_4_5_Core::glGetSubroutineIndex(GLuint
    program, GLenum shadertype, const GLchar *name)': names 'GLchar', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetSubroutineIndex' has no cute "
        "function yet. Qt's 'GLuint "
        "QOpenGLFunctions_4_5_Core::glGetSubroutineIndex(GLuint program, "
        "GLenum shadertype, const GLchar *name)': names 'GLchar', which has "
        "no cute class yet.")

  @staticmethod
  def glGetSubroutineUniformLocation(*__, **_) -> Never:
    """
    Qt's 'GLint
    QOpenGLFunctions_4_5_Core::glGetSubroutineUniformLocation(GLuint program,
    GLenum shadertype, const GLchar *name)': names 'GLchar', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetSubroutineUniformLocation' has no "
        "cute function yet. Qt's 'GLint "
        "QOpenGLFunctions_4_5_Core::glGetSubroutineUniformLocation(GLuint "
        "program, GLenum shadertype, const GLchar *name)': names 'GLchar', "
        "which has no cute class yet.")

  @staticmethod
  def glGetSynciv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetSynciv(GLsync sync, GLenum
    pname, GLsizei bufSize, GLsizei *length, GLint *values)': names 'struct
    __GLsync', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetSynciv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_4_5_Core::glGetSynciv(GLsync sync, "
        "GLenum pname, GLsizei bufSize, GLsizei *length, GLint *values)': "
        "names 'struct __GLsync', which has no cute class yet.")

  @staticmethod
  def glGetTexImage(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetTexImage(GLenum target, GLint
    level, GLenum format, GLenum type, void *pixels)': names 'void', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetTexImage' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_5_Core::glGetTexImage(GLenum "
        "target, GLint level, GLenum format, GLenum type, void *pixels)': "
        "names 'void', which has no cute class yet.")

  @staticmethod
  def glGetTexLevelParameterfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetTexLevelParameterfv(GLenum
    target, GLint level, GLenum pname, GLfloat *params)': takes a number to
    change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetTexLevelParameterfv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetTexLevelParameterfv(GLenum target, "
        "GLint level, GLenum pname, GLfloat *params)': takes a number to "
        "change where it is.")

  @staticmethod
  def glGetTexLevelParameteriv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetTexLevelParameteriv(GLenum
    target, GLint level, GLenum pname, GLint *params)': takes a number to
    change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetTexLevelParameteriv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetTexLevelParameteriv(GLenum target, "
        "GLint level, GLenum pname, GLint *params)': takes a number to "
        "change where it is.")

  @staticmethod
  def glGetTexParameterIiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetTexParameterIiv(GLenum target,
    GLenum pname, GLint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetTexParameterIiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetTexParameterIiv(GLenum target, "
        "GLenum pname, GLint *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetTexParameterIuiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetTexParameterIuiv(GLenum
    target, GLenum pname, GLuint *params)': takes a number to change where it
    is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetTexParameterIuiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetTexParameterIuiv(GLenum target, "
        "GLenum pname, GLuint *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetTexParameterfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetTexParameterfv(GLenum target,
    GLenum pname, GLfloat *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetTexParameterfv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetTexParameterfv(GLenum target, "
        "GLenum pname, GLfloat *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetTexParameteriv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetTexParameteriv(GLenum target,
    GLenum pname, GLint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetTexParameteriv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetTexParameteriv(GLenum target, "
        "GLenum pname, GLint *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetTextureImage(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetTextureImage(GLuint texture,
    GLint level, GLenum format, GLenum type, GLsizei bufSize, void *pixels)':
    names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetTextureImage' has no cute function "
        "yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetTextureImage(GLuint texture, GLint "
        "level, GLenum format, GLenum type, GLsizei bufSize, void "
        "*pixels)': names 'void', which has no cute class yet.")

  @staticmethod
  def glGetTextureLevelParameterfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetTextureLevelParameterfv(GLuint
    texture, GLint level, GLenum pname, GLfloat *params)': takes a number to
    change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetTextureLevelParameterfv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetTextureLevelParameterfv(GLuint "
        "texture, GLint level, GLenum pname, GLfloat *params)': takes a "
        "number to change where it is.")

  @staticmethod
  def glGetTextureLevelParameteriv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetTextureLevelParameteriv(GLuint
    texture, GLint level, GLenum pname, GLint *params)': takes a number to
    change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetTextureLevelParameteriv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetTextureLevelParameteriv(GLuint "
        "texture, GLint level, GLenum pname, GLint *params)': takes a "
        "number to change where it is.")

  @staticmethod
  def glGetTextureParameterIiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetTextureParameterIiv(GLuint
    texture, GLenum pname, GLint *params)': takes a number to change where it
    is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetTextureParameterIiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetTextureParameterIiv(GLuint "
        "texture, GLenum pname, GLint *params)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetTextureParameterIuiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetTextureParameterIuiv(GLuint
    texture, GLenum pname, GLuint *params)': takes a number to change where
    it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetTextureParameterIuiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetTextureParameterIuiv(GLuint "
        "texture, GLenum pname, GLuint *params)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetTextureParameterfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetTextureParameterfv(GLuint
    texture, GLenum pname, GLfloat *params)': takes a number to change where
    it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetTextureParameterfv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetTextureParameterfv(GLuint texture, "
        "GLenum pname, GLfloat *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetTextureParameteriv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetTextureParameteriv(GLuint
    texture, GLenum pname, GLint *params)': takes a number to change where it
    is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetTextureParameteriv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetTextureParameteriv(GLuint texture, "
        "GLenum pname, GLint *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetTextureSubImage(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetTextureSubImage(GLuint
    texture, GLint level, GLint xoffset, GLint yoffset, GLint zoffset,
    GLsizei width, GLsizei height, GLsizei depth, GLenum format, GLenum type,
    GLsizei bufSize, void *pixels)': names 'void', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetTextureSubImage' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetTextureSubImage(GLuint texture, "
        "GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei "
        "width, GLsizei height, GLsizei depth, GLenum format, GLenum type, "
        "GLsizei bufSize, void *pixels)': names 'void', which has no cute "
        "class yet.")

  @staticmethod
  def glGetTransformFeedbackVarying(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_5_Core::glGetTransformFeedbackVarying(GLuint program,
    GLuint index, GLsizei bufSize, GLsizei *length, GLsizei *size, GLenum
    *type, GLchar *name)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetTransformFeedbackVarying' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetTransformFeedbackVarying(GLuint "
        "program, GLuint index, GLsizei bufSize, GLsizei *length, GLsizei "
        "*size, GLenum *type, GLchar *name)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetTransformFeedbacki64_v(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetTransformFeedbacki64_v(GLuint
    xfb, GLenum pname, GLuint index, GLint64 *param)': takes a number to
    change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetTransformFeedbacki64_v' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetTransformFeedbacki64_v(GLuint xfb, "
        "GLenum pname, GLuint index, GLint64 *param)': takes a number to "
        "change where it is.")

  @staticmethod
  def glGetTransformFeedbacki_v(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetTransformFeedbacki_v(GLuint
    xfb, GLenum pname, GLuint index, GLint *param)': takes a number to change
    where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetTransformFeedbacki_v' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetTransformFeedbacki_v(GLuint xfb, "
        "GLenum pname, GLuint index, GLint *param)': takes a number to "
        "change where it is.")

  @staticmethod
  def glGetTransformFeedbackiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetTransformFeedbackiv(GLuint
    xfb, GLenum pname, GLint *param)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetTransformFeedbackiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetTransformFeedbackiv(GLuint xfb, "
        "GLenum pname, GLint *param)': takes a number to change where it is."
    )

  @staticmethod
  def glGetUniformBlockIndex(*__, **_) -> Never:
    """
    Qt's 'GLuint QOpenGLFunctions_4_5_Core::glGetUniformBlockIndex(GLuint
    program, const GLchar *uniformBlockName)': names 'GLchar', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetUniformBlockIndex' has no cute "
        "function yet. Qt's 'GLuint "
        "QOpenGLFunctions_4_5_Core::glGetUniformBlockIndex(GLuint program, "
        "const GLchar *uniformBlockName)': names 'GLchar', which has no "
        "cute class yet.")

  @staticmethod
  def glGetUniformIndices(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetUniformIndices(GLuint program,
    GLsizei uniformCount, const GLchar *const *uniformNames, GLuint
    *uniformIndices)': names 'GLchar *const', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetUniformIndices' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetUniformIndices(GLuint program, "
        "GLsizei uniformCount, const GLchar *const *uniformNames, GLuint "
        "*uniformIndices)': names 'GLchar *const', which has no cute class "
        "yet.")

  @staticmethod
  def glGetUniformLocation(*__, **_) -> Never:
    """
    Qt's 'GLint QOpenGLFunctions_4_5_Core::glGetUniformLocation(GLuint
    program, const GLchar *name)': names 'GLchar', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetUniformLocation' has no cute "
        "function yet. Qt's 'GLint "
        "QOpenGLFunctions_4_5_Core::glGetUniformLocation(GLuint program, "
        "const GLchar *name)': names 'GLchar', which has no cute class yet.")

  @staticmethod
  def glGetUniformSubroutineuiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetUniformSubroutineuiv(GLenum
    shadertype, GLint location, GLuint *params)': takes a number to change
    where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetUniformSubroutineuiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetUniformSubroutineuiv(GLenum "
        "shadertype, GLint location, GLuint *params)': takes a number to "
        "change where it is.")

  @staticmethod
  def glGetUniformdv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetUniformdv(GLuint program,
    GLint location, GLdouble *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetUniformdv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_5_Core::glGetUniformdv(GLuint "
        "program, GLint location, GLdouble *params)': takes a number to "
        "change where it is.")

  @staticmethod
  def glGetUniformfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetUniformfv(GLuint program,
    GLint location, GLfloat *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetUniformfv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_5_Core::glGetUniformfv(GLuint "
        "program, GLint location, GLfloat *params)': takes a number to "
        "change where it is.")

  @staticmethod
  def glGetUniformiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetUniformiv(GLuint program,
    GLint location, GLint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetUniformiv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_5_Core::glGetUniformiv(GLuint "
        "program, GLint location, GLint *params)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetUniformuiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetUniformuiv(GLuint program,
    GLint location, GLuint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetUniformuiv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_5_Core::glGetUniformuiv(GLuint "
        "program, GLint location, GLuint *params)': takes a number to "
        "change where it is.")

  @staticmethod
  def glGetVertexArrayIndexed64iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetVertexArrayIndexed64iv(GLuint
    vaobj, GLuint index, GLenum pname, GLint64 *param)': takes a number to
    change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetVertexArrayIndexed64iv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetVertexArrayIndexed64iv(GLuint "
        "vaobj, GLuint index, GLenum pname, GLint64 *param)': takes a "
        "number to change where it is.")

  @staticmethod
  def glGetVertexArrayIndexediv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetVertexArrayIndexediv(GLuint
    vaobj, GLuint index, GLenum pname, GLint *param)': takes a number to
    change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetVertexArrayIndexediv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetVertexArrayIndexediv(GLuint vaobj, "
        "GLuint index, GLenum pname, GLint *param)': takes a number to "
        "change where it is.")

  @staticmethod
  def glGetVertexArrayiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetVertexArrayiv(GLuint vaobj,
    GLenum pname, GLint *param)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetVertexArrayiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetVertexArrayiv(GLuint vaobj, GLenum "
        "pname, GLint *param)': takes a number to change where it is.")

  @staticmethod
  def glGetVertexAttribIiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetVertexAttribIiv(GLuint index,
    GLenum pname, GLint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetVertexAttribIiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetVertexAttribIiv(GLuint index, "
        "GLenum pname, GLint *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetVertexAttribIuiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetVertexAttribIuiv(GLuint index,
    GLenum pname, GLuint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetVertexAttribIuiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetVertexAttribIuiv(GLuint index, "
        "GLenum pname, GLuint *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetVertexAttribLdv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetVertexAttribLdv(GLuint index,
    GLenum pname, GLdouble *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetVertexAttribLdv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetVertexAttribLdv(GLuint index, "
        "GLenum pname, GLdouble *params)': takes a number to change where "
        "it is.")

  @staticmethod
  def glGetVertexAttribPointerv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetVertexAttribPointerv(GLuint
    index, GLenum pname, void **pointer)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetVertexAttribPointerv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetVertexAttribPointerv(GLuint index, "
        "GLenum pname, void **pointer)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def glGetVertexAttribdv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetVertexAttribdv(GLuint index,
    GLenum pname, GLdouble *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetVertexAttribdv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetVertexAttribdv(GLuint index, "
        "GLenum pname, GLdouble *params)': takes a number to change where "
        "it is.")

  @staticmethod
  def glGetVertexAttribfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetVertexAttribfv(GLuint index,
    GLenum pname, GLfloat *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetVertexAttribfv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetVertexAttribfv(GLuint index, "
        "GLenum pname, GLfloat *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetVertexAttribiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetVertexAttribiv(GLuint index,
    GLenum pname, GLint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetVertexAttribiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetVertexAttribiv(GLuint index, "
        "GLenum pname, GLint *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetnCompressedTexImage(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetnCompressedTexImage(GLenum
    target, GLint lod, GLsizei bufSize, void *pixels)': names 'void', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetnCompressedTexImage' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glGetnCompressedTexImage(GLenum target, "
        "GLint lod, GLsizei bufSize, void *pixels)': names 'void', which "
        "has no cute class yet.")

  @staticmethod
  def glGetnTexImage(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetnTexImage(GLenum target, GLint
    level, GLenum format, GLenum type, GLsizei bufSize, void *pixels)': names
    'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetnTexImage' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_5_Core::glGetnTexImage(GLenum "
        "target, GLint level, GLenum format, GLenum type, GLsizei bufSize, "
        "void *pixels)': names 'void', which has no cute class yet.")

  @staticmethod
  def glGetnUniformdv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetnUniformdv(GLuint program,
    GLint location, GLsizei bufSize, GLdouble *params)': takes a number to
    change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetnUniformdv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_5_Core::glGetnUniformdv(GLuint "
        "program, GLint location, GLsizei bufSize, GLdouble *params)': "
        "takes a number to change where it is.")

  @staticmethod
  def glGetnUniformfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetnUniformfv(GLuint program,
    GLint location, GLsizei bufSize, GLfloat *params)': takes a number to
    change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetnUniformfv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_5_Core::glGetnUniformfv(GLuint "
        "program, GLint location, GLsizei bufSize, GLfloat *params)': takes "
        "a number to change where it is.")

  @staticmethod
  def glGetnUniformiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetnUniformiv(GLuint program,
    GLint location, GLsizei bufSize, GLint *params)': takes a number to
    change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetnUniformiv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_5_Core::glGetnUniformiv(GLuint "
        "program, GLint location, GLsizei bufSize, GLint *params)': takes a "
        "number to change where it is.")

  @staticmethod
  def glGetnUniformuiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glGetnUniformuiv(GLuint program,
    GLint location, GLsizei bufSize, GLuint *params)': takes a number to
    change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glGetnUniformuiv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_5_Core::glGetnUniformuiv(GLuint "
        "program, GLint location, GLsizei bufSize, GLuint *params)': takes "
        "a number to change where it is.")

  @staticmethod
  def glInvalidateFramebuffer(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glInvalidateFramebuffer(GLenum
    target, GLsizei numAttachments, const GLenum *attachments)': names
    'GLenum', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glInvalidateFramebuffer' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glInvalidateFramebuffer(GLenum target, "
        "GLsizei numAttachments, const GLenum *attachments)': names "
        "'GLenum', which has no cute class yet.")

  @staticmethod
  def glInvalidateNamedFramebufferData(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_5_Core::glInvalidateNamedFramebufferData(GLuint
    framebuffer, GLsizei numAttachments, const GLenum *attachments)': names
    'GLenum', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glInvalidateNamedFramebufferData' has "
        "no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glInvalidateNamedFramebufferData(GLuint "
        "framebuffer, GLsizei numAttachments, const GLenum *attachments)': "
        "names 'GLenum', which has no cute class yet.")

  @staticmethod
  def glInvalidateNamedFramebufferSubData(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_5_Core::glInvalidateNamedFramebufferSubData(GLuint
    framebuffer, GLsizei numAttachments, const GLenum *attachments, GLint x,
    GLint y, GLsizei width, GLsizei height)': names 'GLenum', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glInvalidateNamedFramebufferSubData' "
        "has no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glInvalidateNamedFramebufferSubData(GLui"
        "nt framebuffer, GLsizei numAttachments, const GLenum *attachments, "
        "GLint x, GLint y, GLsizei width, GLsizei height)': names 'GLenum', "
        "which has no cute class yet.")

  @staticmethod
  def glInvalidateSubFramebuffer(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glInvalidateSubFramebuffer(GLenum
    target, GLsizei numAttachments, const GLenum *attachments, GLint x, GLint
    y, GLsizei width, GLsizei height)': names 'GLenum', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glInvalidateSubFramebuffer' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glInvalidateSubFramebuffer(GLenum "
        "target, GLsizei numAttachments, const GLenum *attachments, GLint "
        "x, GLint y, GLsizei width, GLsizei height)': names 'GLenum', which "
        "has no cute class yet.")

  @staticmethod
  def glIsSync(*__, **_) -> Never:
    """
    Qt's 'GLboolean QOpenGLFunctions_4_5_Core::glIsSync(GLsync sync)': names
    'struct __GLsync', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glIsSync' has no cute function yet. "
        "Qt's 'GLboolean QOpenGLFunctions_4_5_Core::glIsSync(GLsync sync)': "
        "names 'struct __GLsync', which has no cute class yet.")

  @staticmethod
  def glMapBuffer(*__, **_) -> Never:
    """
    Qt's 'void *QOpenGLFunctions_4_5_Core::glMapBuffer(GLenum target, GLenum
    access)': gives 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glMapBuffer' has no cute function yet. "
        "Qt's 'void *QOpenGLFunctions_4_5_Core::glMapBuffer(GLenum target, "
        "GLenum access)': gives 'void', which has no cute class yet.")

  @staticmethod
  def glMapBufferRange(*__, **_) -> Never:
    """
    Qt's 'void *QOpenGLFunctions_4_5_Core::glMapBufferRange(GLenum target,
    GLintptr offset, GLsizeiptr length, GLbitfield access)': gives 'void',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glMapBufferRange' has no cute function "
        "yet. Qt's 'void "
        "*QOpenGLFunctions_4_5_Core::glMapBufferRange(GLenum target, "
        "GLintptr offset, GLsizeiptr length, GLbitfield access)': gives "
        "'void', which has no cute class yet.")

  @staticmethod
  def glMapNamedBuffer(*__, **_) -> Never:
    """
    Qt's 'void *QOpenGLFunctions_4_5_Core::glMapNamedBuffer(GLuint buffer,
    GLenum access)': gives 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glMapNamedBuffer' has no cute function "
        "yet. Qt's 'void "
        "*QOpenGLFunctions_4_5_Core::glMapNamedBuffer(GLuint buffer, GLenum "
        "access)': gives 'void', which has no cute class yet.")

  @staticmethod
  def glMapNamedBufferRange(*__, **_) -> Never:
    """
    Qt's 'void *QOpenGLFunctions_4_5_Core::glMapNamedBufferRange(GLuint
    buffer, GLintptr offset, GLsizeiptr length, GLbitfield access)': gives
    'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glMapNamedBufferRange' has no cute "
        "function yet. Qt's 'void "
        "*QOpenGLFunctions_4_5_Core::glMapNamedBufferRange(GLuint buffer, "
        "GLintptr offset, GLsizeiptr length, GLbitfield access)': gives "
        "'void', which has no cute class yet.")

  @staticmethod
  def glMultiDrawArrays(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glMultiDrawArrays(GLenum mode,
    const GLint *first, const GLsizei *count, GLsizei drawcount)': names
    'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glMultiDrawArrays' has no cute function "
        "yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glMultiDrawArrays(GLenum mode, const "
        "GLint *first, const GLsizei *count, GLsizei drawcount)': names "
        "'GLint', which has no cute class yet.")

  @staticmethod
  def glMultiDrawArraysIndirect(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glMultiDrawArraysIndirect(GLenum
    mode, const void *indirect, GLsizei drawcount, GLsizei stride)': names
    'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glMultiDrawArraysIndirect' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glMultiDrawArraysIndirect(GLenum mode, "
        "const void *indirect, GLsizei drawcount, GLsizei stride)': names "
        "'void', which has no cute class yet.")

  @staticmethod
  def glMultiDrawElements(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glMultiDrawElements(GLenum mode,
    const GLsizei *count, GLenum type, const void *const *indices, GLsizei
    drawcount)': names 'GLsizei', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glMultiDrawElements' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glMultiDrawElements(GLenum mode, const "
        "GLsizei *count, GLenum type, const void *const *indices, GLsizei "
        "drawcount)': names 'GLsizei', which has no cute class yet.")

  @staticmethod
  def glMultiDrawElementsBaseVertex(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_5_Core::glMultiDrawElementsBaseVertex(GLenum mode,
    const GLsizei *count, GLenum type, const void *const *indices, GLsizei
    drawcount, const GLint *basevertex)': names 'GLsizei', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glMultiDrawElementsBaseVertex' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glMultiDrawElementsBaseVertex(GLenum "
        "mode, const GLsizei *count, GLenum type, const void *const "
        "*indices, GLsizei drawcount, const GLint *basevertex)': names "
        "'GLsizei', which has no cute class yet.")

  @staticmethod
  def glMultiDrawElementsIndirect(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glMultiDrawElementsIndirect(GLenum
    mode, GLenum type, const void *indirect, GLsizei drawcount, GLsizei
    stride)': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glMultiDrawElementsIndirect' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glMultiDrawElementsIndirect(GLenum "
        "mode, GLenum type, const void *indirect, GLsizei drawcount, "
        "GLsizei stride)': names 'void', which has no cute class yet.")

  @staticmethod
  def glNamedBufferData(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glNamedBufferData(GLuint buffer,
    GLsizeiptr size, const void *data, GLenum usage)': names 'void', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glNamedBufferData' has no cute function "
        "yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glNamedBufferData(GLuint buffer, "
        "GLsizeiptr size, const void *data, GLenum usage)': names 'void', "
        "which has no cute class yet.")

  @staticmethod
  def glNamedBufferStorage(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glNamedBufferStorage(GLuint buffer,
    GLsizeiptr size, const void *data, GLbitfield flags)': names 'void',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glNamedBufferStorage' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glNamedBufferStorage(GLuint buffer, "
        "GLsizeiptr size, const void *data, GLbitfield flags)': names "
        "'void', which has no cute class yet.")

  @staticmethod
  def glNamedBufferSubData(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glNamedBufferSubData(GLuint buffer,
    GLintptr offset, GLsizeiptr size, const void *data)': names 'void', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glNamedBufferSubData' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glNamedBufferSubData(GLuint buffer, "
        "GLintptr offset, GLsizeiptr size, const void *data)': names "
        "'void', which has no cute class yet.")

  @staticmethod
  def glNamedFramebufferDrawBuffers(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_5_Core::glNamedFramebufferDrawBuffers(GLuint
    framebuffer, GLsizei n, const GLenum *bufs)': names 'GLenum', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glNamedFramebufferDrawBuffers' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glNamedFramebufferDrawBuffers(GLuint "
        "framebuffer, GLsizei n, const GLenum *bufs)': names 'GLenum', "
        "which has no cute class yet.")

  @staticmethod
  def glObjectLabel(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glObjectLabel(GLenum identifier,
    GLuint name, GLsizei length, const GLchar *label)': names 'GLchar', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glObjectLabel' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_5_Core::glObjectLabel(GLenum "
        "identifier, GLuint name, GLsizei length, const GLchar *label)': "
        "names 'GLchar', which has no cute class yet.")

  @staticmethod
  def glObjectPtrLabel(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glObjectPtrLabel(const void *ptr,
    GLsizei length, const GLchar *label)': names 'void', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glObjectPtrLabel' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_5_Core::glObjectPtrLabel(const "
        "void *ptr, GLsizei length, const GLchar *label)': names 'void', "
        "which has no cute class yet.")

  @staticmethod
  def glPatchParameterfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glPatchParameterfv(GLenum pname,
    const GLfloat *values)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glPatchParameterfv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glPatchParameterfv(GLenum pname, const "
        "GLfloat *values)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glPointParameterfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glPointParameterfv(GLenum pname,
    const GLfloat *params)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glPointParameterfv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glPointParameterfv(GLenum pname, const "
        "GLfloat *params)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glPointParameteriv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glPointParameteriv(GLenum pname,
    const GLint *params)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glPointParameteriv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glPointParameteriv(GLenum pname, const "
        "GLint *params)': names 'GLint', which has no cute class yet.")

  @staticmethod
  def glProgramBinary(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glProgramBinary(GLuint program,
    GLenum binaryFormat, const void *binary, GLsizei length)': names 'void',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glProgramBinary' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_5_Core::glProgramBinary(GLuint "
        "program, GLenum binaryFormat, const void *binary, GLsizei "
        "length)': names 'void', which has no cute class yet.")

  @staticmethod
  def glProgramUniform1dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniform1dv(GLuint program,
    GLint location, GLsizei count, const GLdouble *value)': names 'GLdouble',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glProgramUniform1dv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glProgramUniform1dv(GLuint program, "
        "GLint location, GLsizei count, const GLdouble *value)': names "
        "'GLdouble', which has no cute class yet.")

  @staticmethod
  def glProgramUniform1fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniform1fv(GLuint program,
    GLint location, GLsizei count, const GLfloat *value)': names 'GLfloat',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glProgramUniform1fv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glProgramUniform1fv(GLuint program, "
        "GLint location, GLsizei count, const GLfloat *value)': names "
        "'GLfloat', which has no cute class yet.")

  @staticmethod
  def glProgramUniform1iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniform1iv(GLuint program,
    GLint location, GLsizei count, const GLint *value)': names 'GLint', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glProgramUniform1iv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glProgramUniform1iv(GLuint program, "
        "GLint location, GLsizei count, const GLint *value)': names "
        "'GLint', which has no cute class yet.")

  @staticmethod
  def glProgramUniform1uiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniform1uiv(GLuint
    program, GLint location, GLsizei count, const GLuint *value)': names
    'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glProgramUniform1uiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glProgramUniform1uiv(GLuint program, "
        "GLint location, GLsizei count, const GLuint *value)': names "
        "'GLuint', which has no cute class yet.")

  @staticmethod
  def glProgramUniform2dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniform2dv(GLuint program,
    GLint location, GLsizei count, const GLdouble *value)': names 'GLdouble',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glProgramUniform2dv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glProgramUniform2dv(GLuint program, "
        "GLint location, GLsizei count, const GLdouble *value)': names "
        "'GLdouble', which has no cute class yet.")

  @staticmethod
  def glProgramUniform2fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniform2fv(GLuint program,
    GLint location, GLsizei count, const GLfloat *value)': names 'GLfloat',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glProgramUniform2fv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glProgramUniform2fv(GLuint program, "
        "GLint location, GLsizei count, const GLfloat *value)': names "
        "'GLfloat', which has no cute class yet.")

  @staticmethod
  def glProgramUniform2iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniform2iv(GLuint program,
    GLint location, GLsizei count, const GLint *value)': names 'GLint', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glProgramUniform2iv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glProgramUniform2iv(GLuint program, "
        "GLint location, GLsizei count, const GLint *value)': names "
        "'GLint', which has no cute class yet.")

  @staticmethod
  def glProgramUniform2uiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniform2uiv(GLuint
    program, GLint location, GLsizei count, const GLuint *value)': names
    'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glProgramUniform2uiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glProgramUniform2uiv(GLuint program, "
        "GLint location, GLsizei count, const GLuint *value)': names "
        "'GLuint', which has no cute class yet.")

  @staticmethod
  def glProgramUniform3dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniform3dv(GLuint program,
    GLint location, GLsizei count, const GLdouble *value)': names 'GLdouble',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glProgramUniform3dv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glProgramUniform3dv(GLuint program, "
        "GLint location, GLsizei count, const GLdouble *value)': names "
        "'GLdouble', which has no cute class yet.")

  @staticmethod
  def glProgramUniform3fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniform3fv(GLuint program,
    GLint location, GLsizei count, const GLfloat *value)': names 'GLfloat',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glProgramUniform3fv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glProgramUniform3fv(GLuint program, "
        "GLint location, GLsizei count, const GLfloat *value)': names "
        "'GLfloat', which has no cute class yet.")

  @staticmethod
  def glProgramUniform3iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniform3iv(GLuint program,
    GLint location, GLsizei count, const GLint *value)': names 'GLint', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glProgramUniform3iv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glProgramUniform3iv(GLuint program, "
        "GLint location, GLsizei count, const GLint *value)': names "
        "'GLint', which has no cute class yet.")

  @staticmethod
  def glProgramUniform3uiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniform3uiv(GLuint
    program, GLint location, GLsizei count, const GLuint *value)': names
    'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glProgramUniform3uiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glProgramUniform3uiv(GLuint program, "
        "GLint location, GLsizei count, const GLuint *value)': names "
        "'GLuint', which has no cute class yet.")

  @staticmethod
  def glProgramUniform4dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniform4dv(GLuint program,
    GLint location, GLsizei count, const GLdouble *value)': names 'GLdouble',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glProgramUniform4dv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glProgramUniform4dv(GLuint program, "
        "GLint location, GLsizei count, const GLdouble *value)': names "
        "'GLdouble', which has no cute class yet.")

  @staticmethod
  def glProgramUniform4fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniform4fv(GLuint program,
    GLint location, GLsizei count, const GLfloat *value)': names 'GLfloat',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glProgramUniform4fv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glProgramUniform4fv(GLuint program, "
        "GLint location, GLsizei count, const GLfloat *value)': names "
        "'GLfloat', which has no cute class yet.")

  @staticmethod
  def glProgramUniform4iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniform4iv(GLuint program,
    GLint location, GLsizei count, const GLint *value)': names 'GLint', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glProgramUniform4iv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glProgramUniform4iv(GLuint program, "
        "GLint location, GLsizei count, const GLint *value)': names "
        "'GLint', which has no cute class yet.")

  @staticmethod
  def glProgramUniform4uiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniform4uiv(GLuint
    program, GLint location, GLsizei count, const GLuint *value)': names
    'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glProgramUniform4uiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glProgramUniform4uiv(GLuint program, "
        "GLint location, GLsizei count, const GLuint *value)': names "
        "'GLuint', which has no cute class yet.")

  @staticmethod
  def glProgramUniformMatrix2dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniformMatrix2dv(GLuint
    program, GLint location, GLsizei count, GLboolean transpose, const
    GLdouble *value)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glProgramUniformMatrix2dv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glProgramUniformMatrix2dv(GLuint "
        "program, GLint location, GLsizei count, GLboolean transpose, const "
        "GLdouble *value)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glProgramUniformMatrix2fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniformMatrix2fv(GLuint
    program, GLint location, GLsizei count, GLboolean transpose, const
    GLfloat *value)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glProgramUniformMatrix2fv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glProgramUniformMatrix2fv(GLuint "
        "program, GLint location, GLsizei count, GLboolean transpose, const "
        "GLfloat *value)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glProgramUniformMatrix2x3dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniformMatrix2x3dv(GLuint
    program, GLint location, GLsizei count, GLboolean transpose, const
    GLdouble *value)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glProgramUniformMatrix2x3dv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glProgramUniformMatrix2x3dv(GLuint "
        "program, GLint location, GLsizei count, GLboolean transpose, const "
        "GLdouble *value)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glProgramUniformMatrix2x3fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniformMatrix2x3fv(GLuint
    program, GLint location, GLsizei count, GLboolean transpose, const
    GLfloat *value)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glProgramUniformMatrix2x3fv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glProgramUniformMatrix2x3fv(GLuint "
        "program, GLint location, GLsizei count, GLboolean transpose, const "
        "GLfloat *value)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glProgramUniformMatrix2x4dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniformMatrix2x4dv(GLuint
    program, GLint location, GLsizei count, GLboolean transpose, const
    GLdouble *value)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glProgramUniformMatrix2x4dv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glProgramUniformMatrix2x4dv(GLuint "
        "program, GLint location, GLsizei count, GLboolean transpose, const "
        "GLdouble *value)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glProgramUniformMatrix2x4fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniformMatrix2x4fv(GLuint
    program, GLint location, GLsizei count, GLboolean transpose, const
    GLfloat *value)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glProgramUniformMatrix2x4fv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glProgramUniformMatrix2x4fv(GLuint "
        "program, GLint location, GLsizei count, GLboolean transpose, const "
        "GLfloat *value)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glProgramUniformMatrix3dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniformMatrix3dv(GLuint
    program, GLint location, GLsizei count, GLboolean transpose, const
    GLdouble *value)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glProgramUniformMatrix3dv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glProgramUniformMatrix3dv(GLuint "
        "program, GLint location, GLsizei count, GLboolean transpose, const "
        "GLdouble *value)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glProgramUniformMatrix3fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniformMatrix3fv(GLuint
    program, GLint location, GLsizei count, GLboolean transpose, const
    GLfloat *value)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glProgramUniformMatrix3fv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glProgramUniformMatrix3fv(GLuint "
        "program, GLint location, GLsizei count, GLboolean transpose, const "
        "GLfloat *value)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glProgramUniformMatrix3x2dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniformMatrix3x2dv(GLuint
    program, GLint location, GLsizei count, GLboolean transpose, const
    GLdouble *value)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glProgramUniformMatrix3x2dv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glProgramUniformMatrix3x2dv(GLuint "
        "program, GLint location, GLsizei count, GLboolean transpose, const "
        "GLdouble *value)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glProgramUniformMatrix3x2fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniformMatrix3x2fv(GLuint
    program, GLint location, GLsizei count, GLboolean transpose, const
    GLfloat *value)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glProgramUniformMatrix3x2fv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glProgramUniformMatrix3x2fv(GLuint "
        "program, GLint location, GLsizei count, GLboolean transpose, const "
        "GLfloat *value)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glProgramUniformMatrix3x4dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniformMatrix3x4dv(GLuint
    program, GLint location, GLsizei count, GLboolean transpose, const
    GLdouble *value)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glProgramUniformMatrix3x4dv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glProgramUniformMatrix3x4dv(GLuint "
        "program, GLint location, GLsizei count, GLboolean transpose, const "
        "GLdouble *value)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glProgramUniformMatrix3x4fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniformMatrix3x4fv(GLuint
    program, GLint location, GLsizei count, GLboolean transpose, const
    GLfloat *value)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glProgramUniformMatrix3x4fv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glProgramUniformMatrix3x4fv(GLuint "
        "program, GLint location, GLsizei count, GLboolean transpose, const "
        "GLfloat *value)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glProgramUniformMatrix4dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniformMatrix4dv(GLuint
    program, GLint location, GLsizei count, GLboolean transpose, const
    GLdouble *value)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glProgramUniformMatrix4dv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glProgramUniformMatrix4dv(GLuint "
        "program, GLint location, GLsizei count, GLboolean transpose, const "
        "GLdouble *value)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glProgramUniformMatrix4fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniformMatrix4fv(GLuint
    program, GLint location, GLsizei count, GLboolean transpose, const
    GLfloat *value)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glProgramUniformMatrix4fv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glProgramUniformMatrix4fv(GLuint "
        "program, GLint location, GLsizei count, GLboolean transpose, const "
        "GLfloat *value)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glProgramUniformMatrix4x2dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniformMatrix4x2dv(GLuint
    program, GLint location, GLsizei count, GLboolean transpose, const
    GLdouble *value)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glProgramUniformMatrix4x2dv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glProgramUniformMatrix4x2dv(GLuint "
        "program, GLint location, GLsizei count, GLboolean transpose, const "
        "GLdouble *value)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glProgramUniformMatrix4x2fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniformMatrix4x2fv(GLuint
    program, GLint location, GLsizei count, GLboolean transpose, const
    GLfloat *value)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glProgramUniformMatrix4x2fv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glProgramUniformMatrix4x2fv(GLuint "
        "program, GLint location, GLsizei count, GLboolean transpose, const "
        "GLfloat *value)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glProgramUniformMatrix4x3dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniformMatrix4x3dv(GLuint
    program, GLint location, GLsizei count, GLboolean transpose, const
    GLdouble *value)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glProgramUniformMatrix4x3dv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glProgramUniformMatrix4x3dv(GLuint "
        "program, GLint location, GLsizei count, GLboolean transpose, const "
        "GLdouble *value)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glProgramUniformMatrix4x3fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glProgramUniformMatrix4x3fv(GLuint
    program, GLint location, GLsizei count, GLboolean transpose, const
    GLfloat *value)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glProgramUniformMatrix4x3fv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glProgramUniformMatrix4x3fv(GLuint "
        "program, GLint location, GLsizei count, GLboolean transpose, const "
        "GLfloat *value)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glPushDebugGroup(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glPushDebugGroup(GLenum source,
    GLuint id, GLsizei length, const GLchar *message)': names 'GLchar', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glPushDebugGroup' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_5_Core::glPushDebugGroup(GLenum "
        "source, GLuint id, GLsizei length, const GLchar *message)': names "
        "'GLchar', which has no cute class yet.")

  @staticmethod
  def glReadPixels(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glReadPixels(GLint x, GLint y,
    GLsizei width, GLsizei height, GLenum format, GLenum type, void
    *pixels)': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glReadPixels' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_4_5_Core::glReadPixels(GLint x, GLint "
        "y, GLsizei width, GLsizei height, GLenum format, GLenum type, void "
        "*pixels)': names 'void', which has no cute class yet.")

  @staticmethod
  def glReadnPixels(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glReadnPixels(GLint x, GLint y,
    GLsizei width, GLsizei height, GLenum format, GLenum type, GLsizei
    bufSize, void *data)': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glReadnPixels' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_5_Core::glReadnPixels(GLint x, "
        "GLint y, GLsizei width, GLsizei height, GLenum format, GLenum "
        "type, GLsizei bufSize, void *data)': names 'void', which has no "
        "cute class yet.")

  @staticmethod
  def glSamplerParameterIiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glSamplerParameterIiv(GLuint
    sampler, GLenum pname, const GLint *param)': names 'GLint', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glSamplerParameterIiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glSamplerParameterIiv(GLuint sampler, "
        "GLenum pname, const GLint *param)': names 'GLint', which has no "
        "cute class yet.")

  @staticmethod
  def glSamplerParameterIuiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glSamplerParameterIuiv(GLuint
    sampler, GLenum pname, const GLuint *param)': names 'GLuint', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glSamplerParameterIuiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glSamplerParameterIuiv(GLuint sampler, "
        "GLenum pname, const GLuint *param)': names 'GLuint', which has no "
        "cute class yet.")

  @staticmethod
  def glSamplerParameterfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glSamplerParameterfv(GLuint
    sampler, GLenum pname, const GLfloat *param)': names 'GLfloat', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glSamplerParameterfv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glSamplerParameterfv(GLuint sampler, "
        "GLenum pname, const GLfloat *param)': names 'GLfloat', which has "
        "no cute class yet.")

  @staticmethod
  def glSamplerParameteriv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glSamplerParameteriv(GLuint
    sampler, GLenum pname, const GLint *param)': names 'GLint', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glSamplerParameteriv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glSamplerParameteriv(GLuint sampler, "
        "GLenum pname, const GLint *param)': names 'GLint', which has no "
        "cute class yet.")

  @staticmethod
  def glScissorArrayv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glScissorArrayv(GLuint first,
    GLsizei count, const GLint *v)': names 'GLint', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glScissorArrayv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_5_Core::glScissorArrayv(GLuint "
        "first, GLsizei count, const GLint *v)': names 'GLint', which has "
        "no cute class yet.")

  @staticmethod
  def glScissorIndexedv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glScissorIndexedv(GLuint index,
    const GLint *v)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glScissorIndexedv' has no cute function "
        "yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glScissorIndexedv(GLuint index, const "
        "GLint *v)': names 'GLint', which has no cute class yet.")

  @staticmethod
  def glShaderBinary(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glShaderBinary(GLsizei count, const
    GLuint *shaders, GLenum binaryformat, const void *binary, GLsizei
    length)': names 'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glShaderBinary' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_5_Core::glShaderBinary(GLsizei "
        "count, const GLuint *shaders, GLenum binaryformat, const void "
        "*binary, GLsizei length)': names 'GLuint', which has no cute class "
        "yet.")

  @staticmethod
  def glShaderSource(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glShaderSource(GLuint shader,
    GLsizei count, const GLchar *const *string, const GLint *length)': names
    'GLchar *const', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glShaderSource' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_5_Core::glShaderSource(GLuint "
        "shader, GLsizei count, const GLchar *const *string, const GLint "
        "*length)': names 'GLchar *const', which has no cute class yet.")

  @staticmethod
  def glTexImage1D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glTexImage1D(GLenum target, GLint
    level, GLint internalformat, GLsizei width, GLint border, GLenum format,
    GLenum type, const void *pixels)': names 'void', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glTexImage1D' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_4_5_Core::glTexImage1D(GLenum target, "
        "GLint level, GLint internalformat, GLsizei width, GLint border, "
        "GLenum format, GLenum type, const void *pixels)': names 'void', "
        "which has no cute class yet.")

  @staticmethod
  def glTexImage2D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glTexImage2D(GLenum target, GLint
    level, GLint internalformat, GLsizei width, GLsizei height, GLint border,
    GLenum format, GLenum type, const void *pixels)': names 'void', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glTexImage2D' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_4_5_Core::glTexImage2D(GLenum target, "
        "GLint level, GLint internalformat, GLsizei width, GLsizei height, "
        "GLint border, GLenum format, GLenum type, const void *pixels)': "
        "names 'void', which has no cute class yet.")

  @staticmethod
  def glTexImage3D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glTexImage3D(GLenum target, GLint
    level, GLint internalformat, GLsizei width, GLsizei height, GLsizei
    depth, GLint border, GLenum format, GLenum type, const void *pixels)':
    names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glTexImage3D' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_4_5_Core::glTexImage3D(GLenum target, "
        "GLint level, GLint internalformat, GLsizei width, GLsizei height, "
        "GLsizei depth, GLint border, GLenum format, GLenum type, const "
        "void *pixels)': names 'void', which has no cute class yet.")

  @staticmethod
  def glTexParameterIiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glTexParameterIiv(GLenum target,
    GLenum pname, const GLint *params)': names 'GLint', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glTexParameterIiv' has no cute function "
        "yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glTexParameterIiv(GLenum target, GLenum "
        "pname, const GLint *params)': names 'GLint', which has no cute "
        "class yet.")

  @staticmethod
  def glTexParameterIuiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glTexParameterIuiv(GLenum target,
    GLenum pname, const GLuint *params)': names 'GLuint', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glTexParameterIuiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glTexParameterIuiv(GLenum target, "
        "GLenum pname, const GLuint *params)': names 'GLuint', which has no "
        "cute class yet.")

  @staticmethod
  def glTexParameterfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glTexParameterfv(GLenum target,
    GLenum pname, const GLfloat *params)': names 'GLfloat', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glTexParameterfv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_5_Core::glTexParameterfv(GLenum "
        "target, GLenum pname, const GLfloat *params)': names 'GLfloat', "
        "which has no cute class yet.")

  @staticmethod
  def glTexParameteriv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glTexParameteriv(GLenum target,
    GLenum pname, const GLint *params)': names 'GLint', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glTexParameteriv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_5_Core::glTexParameteriv(GLenum "
        "target, GLenum pname, const GLint *params)': names 'GLint', which "
        "has no cute class yet.")

  @staticmethod
  def glTexSubImage1D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glTexSubImage1D(GLenum target,
    GLint level, GLint xoffset, GLsizei width, GLenum format, GLenum type,
    const void *pixels)': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glTexSubImage1D' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_5_Core::glTexSubImage1D(GLenum "
        "target, GLint level, GLint xoffset, GLsizei width, GLenum format, "
        "GLenum type, const void *pixels)': names 'void', which has no cute "
        "class yet.")

  @staticmethod
  def glTexSubImage2D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glTexSubImage2D(GLenum target,
    GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height,
    GLenum format, GLenum type, const void *pixels)': names 'void', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glTexSubImage2D' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_5_Core::glTexSubImage2D(GLenum "
        "target, GLint level, GLint xoffset, GLint yoffset, GLsizei width, "
        "GLsizei height, GLenum format, GLenum type, const void *pixels)': "
        "names 'void', which has no cute class yet.")

  @staticmethod
  def glTexSubImage3D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glTexSubImage3D(GLenum target,
    GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width,
    GLsizei height, GLsizei depth, GLenum format, GLenum type, const void
    *pixels)': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glTexSubImage3D' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_5_Core::glTexSubImage3D(GLenum "
        "target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, "
        "GLsizei width, GLsizei height, GLsizei depth, GLenum format, "
        "GLenum type, const void *pixels)': names 'void', which has no cute "
        "class yet.")

  @staticmethod
  def glTextureParameterIiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glTextureParameterIiv(GLuint
    texture, GLenum pname, const GLint *params)': names 'GLint', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glTextureParameterIiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glTextureParameterIiv(GLuint texture, "
        "GLenum pname, const GLint *params)': names 'GLint', which has no "
        "cute class yet.")

  @staticmethod
  def glTextureParameterIuiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glTextureParameterIuiv(GLuint
    texture, GLenum pname, const GLuint *params)': names 'GLuint', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glTextureParameterIuiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glTextureParameterIuiv(GLuint texture, "
        "GLenum pname, const GLuint *params)': names 'GLuint', which has no "
        "cute class yet.")

  @staticmethod
  def glTextureParameterfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glTextureParameterfv(GLuint
    texture, GLenum pname, const GLfloat *param)': names 'GLfloat', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glTextureParameterfv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glTextureParameterfv(GLuint texture, "
        "GLenum pname, const GLfloat *param)': names 'GLfloat', which has "
        "no cute class yet.")

  @staticmethod
  def glTextureParameteriv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glTextureParameteriv(GLuint
    texture, GLenum pname, const GLint *param)': names 'GLint', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glTextureParameteriv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glTextureParameteriv(GLuint texture, "
        "GLenum pname, const GLint *param)': names 'GLint', which has no "
        "cute class yet.")

  @staticmethod
  def glTextureSubImage1D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glTextureSubImage1D(GLuint texture,
    GLint level, GLint xoffset, GLsizei width, GLenum format, GLenum type,
    const void *pixels)': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glTextureSubImage1D' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glTextureSubImage1D(GLuint texture, "
        "GLint level, GLint xoffset, GLsizei width, GLenum format, GLenum "
        "type, const void *pixels)': names 'void', which has no cute class "
        "yet.")

  @staticmethod
  def glTextureSubImage2D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glTextureSubImage2D(GLuint texture,
    GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height,
    GLenum format, GLenum type, const void *pixels)': names 'void', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glTextureSubImage2D' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glTextureSubImage2D(GLuint texture, "
        "GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei "
        "height, GLenum format, GLenum type, const void *pixels)': names "
        "'void', which has no cute class yet.")

  @staticmethod
  def glTextureSubImage3D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glTextureSubImage3D(GLuint texture,
    GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width,
    GLsizei height, GLsizei depth, GLenum format, GLenum type, const void
    *pixels)': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glTextureSubImage3D' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glTextureSubImage3D(GLuint texture, "
        "GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei "
        "width, GLsizei height, GLsizei depth, GLenum format, GLenum type, "
        "const void *pixels)': names 'void', which has no cute class yet.")

  @staticmethod
  def glTransformFeedbackVaryings(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glTransformFeedbackVaryings(GLuint
    program, GLsizei count, const GLchar *const *varyings, GLenum
    bufferMode)': names 'GLchar *const', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glTransformFeedbackVaryings' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glTransformFeedbackVaryings(GLuint "
        "program, GLsizei count, const GLchar *const *varyings, GLenum "
        "bufferMode)': names 'GLchar *const', which has no cute class yet.")

  @staticmethod
  def glUniform1dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glUniform1dv(GLint location,
    GLsizei count, const GLdouble *value)': names 'GLdouble', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glUniform1dv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_4_5_Core::glUniform1dv(GLint location, "
        "GLsizei count, const GLdouble *value)': names 'GLdouble', which "
        "has no cute class yet.")

  @staticmethod
  def glUniform1fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glUniform1fv(GLint location,
    GLsizei count, const GLfloat *value)': names 'GLfloat', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glUniform1fv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_4_5_Core::glUniform1fv(GLint location, "
        "GLsizei count, const GLfloat *value)': names 'GLfloat', which has "
        "no cute class yet.")

  @staticmethod
  def glUniform1iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glUniform1iv(GLint location,
    GLsizei count, const GLint *value)': names 'GLint', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glUniform1iv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_4_5_Core::glUniform1iv(GLint location, "
        "GLsizei count, const GLint *value)': names 'GLint', which has no "
        "cute class yet.")

  @staticmethod
  def glUniform1uiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glUniform1uiv(GLint location,
    GLsizei count, const GLuint *value)': names 'GLuint', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glUniform1uiv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_5_Core::glUniform1uiv(GLint "
        "location, GLsizei count, const GLuint *value)': names 'GLuint', "
        "which has no cute class yet.")

  @staticmethod
  def glUniform2dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glUniform2dv(GLint location,
    GLsizei count, const GLdouble *value)': names 'GLdouble', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glUniform2dv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_4_5_Core::glUniform2dv(GLint location, "
        "GLsizei count, const GLdouble *value)': names 'GLdouble', which "
        "has no cute class yet.")

  @staticmethod
  def glUniform2fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glUniform2fv(GLint location,
    GLsizei count, const GLfloat *value)': names 'GLfloat', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glUniform2fv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_4_5_Core::glUniform2fv(GLint location, "
        "GLsizei count, const GLfloat *value)': names 'GLfloat', which has "
        "no cute class yet.")

  @staticmethod
  def glUniform2iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glUniform2iv(GLint location,
    GLsizei count, const GLint *value)': names 'GLint', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glUniform2iv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_4_5_Core::glUniform2iv(GLint location, "
        "GLsizei count, const GLint *value)': names 'GLint', which has no "
        "cute class yet.")

  @staticmethod
  def glUniform2uiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glUniform2uiv(GLint location,
    GLsizei count, const GLuint *value)': names 'GLuint', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glUniform2uiv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_5_Core::glUniform2uiv(GLint "
        "location, GLsizei count, const GLuint *value)': names 'GLuint', "
        "which has no cute class yet.")

  @staticmethod
  def glUniform3dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glUniform3dv(GLint location,
    GLsizei count, const GLdouble *value)': names 'GLdouble', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glUniform3dv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_4_5_Core::glUniform3dv(GLint location, "
        "GLsizei count, const GLdouble *value)': names 'GLdouble', which "
        "has no cute class yet.")

  @staticmethod
  def glUniform3fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glUniform3fv(GLint location,
    GLsizei count, const GLfloat *value)': names 'GLfloat', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glUniform3fv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_4_5_Core::glUniform3fv(GLint location, "
        "GLsizei count, const GLfloat *value)': names 'GLfloat', which has "
        "no cute class yet.")

  @staticmethod
  def glUniform3iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glUniform3iv(GLint location,
    GLsizei count, const GLint *value)': names 'GLint', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glUniform3iv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_4_5_Core::glUniform3iv(GLint location, "
        "GLsizei count, const GLint *value)': names 'GLint', which has no "
        "cute class yet.")

  @staticmethod
  def glUniform3uiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glUniform3uiv(GLint location,
    GLsizei count, const GLuint *value)': names 'GLuint', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glUniform3uiv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_5_Core::glUniform3uiv(GLint "
        "location, GLsizei count, const GLuint *value)': names 'GLuint', "
        "which has no cute class yet.")

  @staticmethod
  def glUniform4dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glUniform4dv(GLint location,
    GLsizei count, const GLdouble *value)': names 'GLdouble', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glUniform4dv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_4_5_Core::glUniform4dv(GLint location, "
        "GLsizei count, const GLdouble *value)': names 'GLdouble', which "
        "has no cute class yet.")

  @staticmethod
  def glUniform4fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glUniform4fv(GLint location,
    GLsizei count, const GLfloat *value)': names 'GLfloat', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glUniform4fv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_4_5_Core::glUniform4fv(GLint location, "
        "GLsizei count, const GLfloat *value)': names 'GLfloat', which has "
        "no cute class yet.")

  @staticmethod
  def glUniform4iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glUniform4iv(GLint location,
    GLsizei count, const GLint *value)': names 'GLint', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glUniform4iv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_4_5_Core::glUniform4iv(GLint location, "
        "GLsizei count, const GLint *value)': names 'GLint', which has no "
        "cute class yet.")

  @staticmethod
  def glUniform4uiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glUniform4uiv(GLint location,
    GLsizei count, const GLuint *value)': names 'GLuint', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glUniform4uiv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_5_Core::glUniform4uiv(GLint "
        "location, GLsizei count, const GLuint *value)': names 'GLuint', "
        "which has no cute class yet.")

  @staticmethod
  def glUniformMatrix2dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glUniformMatrix2dv(GLint location,
    GLsizei count, GLboolean transpose, const GLdouble *value)': names
    'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glUniformMatrix2dv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glUniformMatrix2dv(GLint location, "
        "GLsizei count, GLboolean transpose, const GLdouble *value)': names "
        "'GLdouble', which has no cute class yet.")

  @staticmethod
  def glUniformMatrix2fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glUniformMatrix2fv(GLint location,
    GLsizei count, GLboolean transpose, const GLfloat *value)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glUniformMatrix2fv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glUniformMatrix2fv(GLint location, "
        "GLsizei count, GLboolean transpose, const GLfloat *value)': names "
        "'GLfloat', which has no cute class yet.")

  @staticmethod
  def glUniformMatrix2x3dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glUniformMatrix2x3dv(GLint
    location, GLsizei count, GLboolean transpose, const GLdouble *value)':
    names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glUniformMatrix2x3dv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glUniformMatrix2x3dv(GLint location, "
        "GLsizei count, GLboolean transpose, const GLdouble *value)': names "
        "'GLdouble', which has no cute class yet.")

  @staticmethod
  def glUniformMatrix2x3fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glUniformMatrix2x3fv(GLint
    location, GLsizei count, GLboolean transpose, const GLfloat *value)':
    names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glUniformMatrix2x3fv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glUniformMatrix2x3fv(GLint location, "
        "GLsizei count, GLboolean transpose, const GLfloat *value)': names "
        "'GLfloat', which has no cute class yet.")

  @staticmethod
  def glUniformMatrix2x4dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glUniformMatrix2x4dv(GLint
    location, GLsizei count, GLboolean transpose, const GLdouble *value)':
    names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glUniformMatrix2x4dv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glUniformMatrix2x4dv(GLint location, "
        "GLsizei count, GLboolean transpose, const GLdouble *value)': names "
        "'GLdouble', which has no cute class yet.")

  @staticmethod
  def glUniformMatrix2x4fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glUniformMatrix2x4fv(GLint
    location, GLsizei count, GLboolean transpose, const GLfloat *value)':
    names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glUniformMatrix2x4fv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glUniformMatrix2x4fv(GLint location, "
        "GLsizei count, GLboolean transpose, const GLfloat *value)': names "
        "'GLfloat', which has no cute class yet.")

  @staticmethod
  def glUniformMatrix3dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glUniformMatrix3dv(GLint location,
    GLsizei count, GLboolean transpose, const GLdouble *value)': names
    'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glUniformMatrix3dv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glUniformMatrix3dv(GLint location, "
        "GLsizei count, GLboolean transpose, const GLdouble *value)': names "
        "'GLdouble', which has no cute class yet.")

  @staticmethod
  def glUniformMatrix3fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glUniformMatrix3fv(GLint location,
    GLsizei count, GLboolean transpose, const GLfloat *value)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glUniformMatrix3fv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glUniformMatrix3fv(GLint location, "
        "GLsizei count, GLboolean transpose, const GLfloat *value)': names "
        "'GLfloat', which has no cute class yet.")

  @staticmethod
  def glUniformMatrix3x2dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glUniformMatrix3x2dv(GLint
    location, GLsizei count, GLboolean transpose, const GLdouble *value)':
    names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glUniformMatrix3x2dv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glUniformMatrix3x2dv(GLint location, "
        "GLsizei count, GLboolean transpose, const GLdouble *value)': names "
        "'GLdouble', which has no cute class yet.")

  @staticmethod
  def glUniformMatrix3x2fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glUniformMatrix3x2fv(GLint
    location, GLsizei count, GLboolean transpose, const GLfloat *value)':
    names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glUniformMatrix3x2fv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glUniformMatrix3x2fv(GLint location, "
        "GLsizei count, GLboolean transpose, const GLfloat *value)': names "
        "'GLfloat', which has no cute class yet.")

  @staticmethod
  def glUniformMatrix3x4dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glUniformMatrix3x4dv(GLint
    location, GLsizei count, GLboolean transpose, const GLdouble *value)':
    names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glUniformMatrix3x4dv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glUniformMatrix3x4dv(GLint location, "
        "GLsizei count, GLboolean transpose, const GLdouble *value)': names "
        "'GLdouble', which has no cute class yet.")

  @staticmethod
  def glUniformMatrix3x4fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glUniformMatrix3x4fv(GLint
    location, GLsizei count, GLboolean transpose, const GLfloat *value)':
    names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glUniformMatrix3x4fv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glUniformMatrix3x4fv(GLint location, "
        "GLsizei count, GLboolean transpose, const GLfloat *value)': names "
        "'GLfloat', which has no cute class yet.")

  @staticmethod
  def glUniformMatrix4dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glUniformMatrix4dv(GLint location,
    GLsizei count, GLboolean transpose, const GLdouble *value)': names
    'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glUniformMatrix4dv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glUniformMatrix4dv(GLint location, "
        "GLsizei count, GLboolean transpose, const GLdouble *value)': names "
        "'GLdouble', which has no cute class yet.")

  @staticmethod
  def glUniformMatrix4fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glUniformMatrix4fv(GLint location,
    GLsizei count, GLboolean transpose, const GLfloat *value)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glUniformMatrix4fv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glUniformMatrix4fv(GLint location, "
        "GLsizei count, GLboolean transpose, const GLfloat *value)': names "
        "'GLfloat', which has no cute class yet.")

  @staticmethod
  def glUniformMatrix4x2dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glUniformMatrix4x2dv(GLint
    location, GLsizei count, GLboolean transpose, const GLdouble *value)':
    names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glUniformMatrix4x2dv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glUniformMatrix4x2dv(GLint location, "
        "GLsizei count, GLboolean transpose, const GLdouble *value)': names "
        "'GLdouble', which has no cute class yet.")

  @staticmethod
  def glUniformMatrix4x2fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glUniformMatrix4x2fv(GLint
    location, GLsizei count, GLboolean transpose, const GLfloat *value)':
    names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glUniformMatrix4x2fv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glUniformMatrix4x2fv(GLint location, "
        "GLsizei count, GLboolean transpose, const GLfloat *value)': names "
        "'GLfloat', which has no cute class yet.")

  @staticmethod
  def glUniformMatrix4x3dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glUniformMatrix4x3dv(GLint
    location, GLsizei count, GLboolean transpose, const GLdouble *value)':
    names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glUniformMatrix4x3dv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glUniformMatrix4x3dv(GLint location, "
        "GLsizei count, GLboolean transpose, const GLdouble *value)': names "
        "'GLdouble', which has no cute class yet.")

  @staticmethod
  def glUniformMatrix4x3fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glUniformMatrix4x3fv(GLint
    location, GLsizei count, GLboolean transpose, const GLfloat *value)':
    names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glUniformMatrix4x3fv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glUniformMatrix4x3fv(GLint location, "
        "GLsizei count, GLboolean transpose, const GLfloat *value)': names "
        "'GLfloat', which has no cute class yet.")

  @staticmethod
  def glUniformSubroutinesuiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glUniformSubroutinesuiv(GLenum
    shadertype, GLsizei count, const GLuint *indices)': names 'GLuint', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glUniformSubroutinesuiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glUniformSubroutinesuiv(GLenum "
        "shadertype, GLsizei count, const GLuint *indices)': names "
        "'GLuint', which has no cute class yet.")

  @staticmethod
  def glVertexArrayVertexBuffers(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glVertexArrayVertexBuffers(GLuint
    vaobj, GLuint first, GLsizei count, const GLuint *buffers, const GLintptr
    *offsets, const GLsizei *strides)': names 'GLuint', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glVertexArrayVertexBuffers' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glVertexArrayVertexBuffers(GLuint "
        "vaobj, GLuint first, GLsizei count, const GLuint *buffers, const "
        "GLintptr *offsets, const GLsizei *strides)': names 'GLuint', which "
        "has no cute class yet.")

  @staticmethod
  def glVertexAttrib1dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttrib1dv(GLuint index,
    const GLdouble *v)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glVertexAttrib1dv' has no cute function "
        "yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glVertexAttrib1dv(GLuint index, const "
        "GLdouble *v)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glVertexAttrib1fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttrib1fv(GLuint index,
    const GLfloat *v)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glVertexAttrib1fv' has no cute function "
        "yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glVertexAttrib1fv(GLuint index, const "
        "GLfloat *v)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glVertexAttrib1sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttrib1sv(GLuint index,
    const GLshort *v)': names 'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glVertexAttrib1sv' has no cute function "
        "yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glVertexAttrib1sv(GLuint index, const "
        "GLshort *v)': names 'GLshort', which has no cute class yet.")

  @staticmethod
  def glVertexAttrib2dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttrib2dv(GLuint index,
    const GLdouble *v)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glVertexAttrib2dv' has no cute function "
        "yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glVertexAttrib2dv(GLuint index, const "
        "GLdouble *v)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glVertexAttrib2fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttrib2fv(GLuint index,
    const GLfloat *v)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glVertexAttrib2fv' has no cute function "
        "yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glVertexAttrib2fv(GLuint index, const "
        "GLfloat *v)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glVertexAttrib2sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttrib2sv(GLuint index,
    const GLshort *v)': names 'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glVertexAttrib2sv' has no cute function "
        "yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glVertexAttrib2sv(GLuint index, const "
        "GLshort *v)': names 'GLshort', which has no cute class yet.")

  @staticmethod
  def glVertexAttrib3dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttrib3dv(GLuint index,
    const GLdouble *v)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glVertexAttrib3dv' has no cute function "
        "yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glVertexAttrib3dv(GLuint index, const "
        "GLdouble *v)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glVertexAttrib3fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttrib3fv(GLuint index,
    const GLfloat *v)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glVertexAttrib3fv' has no cute function "
        "yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glVertexAttrib3fv(GLuint index, const "
        "GLfloat *v)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glVertexAttrib3sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttrib3sv(GLuint index,
    const GLshort *v)': names 'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glVertexAttrib3sv' has no cute function "
        "yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glVertexAttrib3sv(GLuint index, const "
        "GLshort *v)': names 'GLshort', which has no cute class yet.")

  @staticmethod
  def glVertexAttrib4Nbv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttrib4Nbv(GLuint index,
    const GLbyte *v)': names 'GLbyte', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glVertexAttrib4Nbv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glVertexAttrib4Nbv(GLuint index, const "
        "GLbyte *v)': names 'GLbyte', which has no cute class yet.")

  @staticmethod
  def glVertexAttrib4Niv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttrib4Niv(GLuint index,
    const GLint *v)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glVertexAttrib4Niv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glVertexAttrib4Niv(GLuint index, const "
        "GLint *v)': names 'GLint', which has no cute class yet.")

  @staticmethod
  def glVertexAttrib4Nsv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttrib4Nsv(GLuint index,
    const GLshort *v)': names 'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glVertexAttrib4Nsv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glVertexAttrib4Nsv(GLuint index, const "
        "GLshort *v)': names 'GLshort', which has no cute class yet.")

  @staticmethod
  def glVertexAttrib4Nubv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttrib4Nubv(GLuint index,
    const GLubyte *v)': names 'GLubyte', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glVertexAttrib4Nubv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glVertexAttrib4Nubv(GLuint index, const "
        "GLubyte *v)': names 'GLubyte', which has no cute class yet.")

  @staticmethod
  def glVertexAttrib4Nuiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttrib4Nuiv(GLuint index,
    const GLuint *v)': names 'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glVertexAttrib4Nuiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glVertexAttrib4Nuiv(GLuint index, const "
        "GLuint *v)': names 'GLuint', which has no cute class yet.")

  @staticmethod
  def glVertexAttrib4Nusv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttrib4Nusv(GLuint index,
    const GLushort *v)': names 'GLushort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glVertexAttrib4Nusv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glVertexAttrib4Nusv(GLuint index, const "
        "GLushort *v)': names 'GLushort', which has no cute class yet.")

  @staticmethod
  def glVertexAttrib4bv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttrib4bv(GLuint index,
    const GLbyte *v)': names 'GLbyte', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glVertexAttrib4bv' has no cute function "
        "yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glVertexAttrib4bv(GLuint index, const "
        "GLbyte *v)': names 'GLbyte', which has no cute class yet.")

  @staticmethod
  def glVertexAttrib4dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttrib4dv(GLuint index,
    const GLdouble *v)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glVertexAttrib4dv' has no cute function "
        "yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glVertexAttrib4dv(GLuint index, const "
        "GLdouble *v)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glVertexAttrib4fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttrib4fv(GLuint index,
    const GLfloat *v)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glVertexAttrib4fv' has no cute function "
        "yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glVertexAttrib4fv(GLuint index, const "
        "GLfloat *v)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glVertexAttrib4iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttrib4iv(GLuint index,
    const GLint *v)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glVertexAttrib4iv' has no cute function "
        "yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glVertexAttrib4iv(GLuint index, const "
        "GLint *v)': names 'GLint', which has no cute class yet.")

  @staticmethod
  def glVertexAttrib4sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttrib4sv(GLuint index,
    const GLshort *v)': names 'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glVertexAttrib4sv' has no cute function "
        "yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glVertexAttrib4sv(GLuint index, const "
        "GLshort *v)': names 'GLshort', which has no cute class yet.")

  @staticmethod
  def glVertexAttrib4ubv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttrib4ubv(GLuint index,
    const GLubyte *v)': names 'GLubyte', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glVertexAttrib4ubv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glVertexAttrib4ubv(GLuint index, const "
        "GLubyte *v)': names 'GLubyte', which has no cute class yet.")

  @staticmethod
  def glVertexAttrib4uiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttrib4uiv(GLuint index,
    const GLuint *v)': names 'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glVertexAttrib4uiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glVertexAttrib4uiv(GLuint index, const "
        "GLuint *v)': names 'GLuint', which has no cute class yet.")

  @staticmethod
  def glVertexAttrib4usv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttrib4usv(GLuint index,
    const GLushort *v)': names 'GLushort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glVertexAttrib4usv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glVertexAttrib4usv(GLuint index, const "
        "GLushort *v)': names 'GLushort', which has no cute class yet.")

  @staticmethod
  def glVertexAttribI1iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttribI1iv(GLuint index,
    const GLint *v)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glVertexAttribI1iv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glVertexAttribI1iv(GLuint index, const "
        "GLint *v)': names 'GLint', which has no cute class yet.")

  @staticmethod
  def glVertexAttribI1uiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttribI1uiv(GLuint index,
    const GLuint *v)': names 'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glVertexAttribI1uiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glVertexAttribI1uiv(GLuint index, const "
        "GLuint *v)': names 'GLuint', which has no cute class yet.")

  @staticmethod
  def glVertexAttribI2iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttribI2iv(GLuint index,
    const GLint *v)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glVertexAttribI2iv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glVertexAttribI2iv(GLuint index, const "
        "GLint *v)': names 'GLint', which has no cute class yet.")

  @staticmethod
  def glVertexAttribI2uiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttribI2uiv(GLuint index,
    const GLuint *v)': names 'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glVertexAttribI2uiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glVertexAttribI2uiv(GLuint index, const "
        "GLuint *v)': names 'GLuint', which has no cute class yet.")

  @staticmethod
  def glVertexAttribI3iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttribI3iv(GLuint index,
    const GLint *v)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glVertexAttribI3iv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glVertexAttribI3iv(GLuint index, const "
        "GLint *v)': names 'GLint', which has no cute class yet.")

  @staticmethod
  def glVertexAttribI3uiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttribI3uiv(GLuint index,
    const GLuint *v)': names 'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glVertexAttribI3uiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glVertexAttribI3uiv(GLuint index, const "
        "GLuint *v)': names 'GLuint', which has no cute class yet.")

  @staticmethod
  def glVertexAttribI4bv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttribI4bv(GLuint index,
    const GLbyte *v)': names 'GLbyte', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glVertexAttribI4bv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glVertexAttribI4bv(GLuint index, const "
        "GLbyte *v)': names 'GLbyte', which has no cute class yet.")

  @staticmethod
  def glVertexAttribI4iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttribI4iv(GLuint index,
    const GLint *v)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glVertexAttribI4iv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glVertexAttribI4iv(GLuint index, const "
        "GLint *v)': names 'GLint', which has no cute class yet.")

  @staticmethod
  def glVertexAttribI4sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttribI4sv(GLuint index,
    const GLshort *v)': names 'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glVertexAttribI4sv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glVertexAttribI4sv(GLuint index, const "
        "GLshort *v)': names 'GLshort', which has no cute class yet.")

  @staticmethod
  def glVertexAttribI4ubv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttribI4ubv(GLuint index,
    const GLubyte *v)': names 'GLubyte', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glVertexAttribI4ubv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glVertexAttribI4ubv(GLuint index, const "
        "GLubyte *v)': names 'GLubyte', which has no cute class yet.")

  @staticmethod
  def glVertexAttribI4uiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttribI4uiv(GLuint index,
    const GLuint *v)': names 'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glVertexAttribI4uiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glVertexAttribI4uiv(GLuint index, const "
        "GLuint *v)': names 'GLuint', which has no cute class yet.")

  @staticmethod
  def glVertexAttribI4usv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttribI4usv(GLuint index,
    const GLushort *v)': names 'GLushort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glVertexAttribI4usv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glVertexAttribI4usv(GLuint index, const "
        "GLushort *v)': names 'GLushort', which has no cute class yet.")

  @staticmethod
  def glVertexAttribIPointer(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttribIPointer(GLuint
    index, GLint size, GLenum type, GLsizei stride, const void *pointer)':
    names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glVertexAttribIPointer' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glVertexAttribIPointer(GLuint index, "
        "GLint size, GLenum type, GLsizei stride, const void *pointer)': "
        "names 'void', which has no cute class yet.")

  @staticmethod
  def glVertexAttribL1dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttribL1dv(GLuint index,
    const GLdouble *v)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glVertexAttribL1dv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glVertexAttribL1dv(GLuint index, const "
        "GLdouble *v)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glVertexAttribL2dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttribL2dv(GLuint index,
    const GLdouble *v)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glVertexAttribL2dv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glVertexAttribL2dv(GLuint index, const "
        "GLdouble *v)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glVertexAttribL3dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttribL3dv(GLuint index,
    const GLdouble *v)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glVertexAttribL3dv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glVertexAttribL3dv(GLuint index, const "
        "GLdouble *v)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glVertexAttribL4dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttribL4dv(GLuint index,
    const GLdouble *v)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glVertexAttribL4dv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glVertexAttribL4dv(GLuint index, const "
        "GLdouble *v)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glVertexAttribLPointer(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttribLPointer(GLuint
    index, GLint size, GLenum type, GLsizei stride, const void *pointer)':
    names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glVertexAttribLPointer' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glVertexAttribLPointer(GLuint index, "
        "GLint size, GLenum type, GLsizei stride, const void *pointer)': "
        "names 'void', which has no cute class yet.")

  @staticmethod
  def glVertexAttribP1uiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttribP1uiv(GLuint index,
    GLenum type, GLboolean normalized, const GLuint *value)': names 'GLuint',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glVertexAttribP1uiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glVertexAttribP1uiv(GLuint index, "
        "GLenum type, GLboolean normalized, const GLuint *value)': names "
        "'GLuint', which has no cute class yet.")

  @staticmethod
  def glVertexAttribP2uiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttribP2uiv(GLuint index,
    GLenum type, GLboolean normalized, const GLuint *value)': names 'GLuint',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glVertexAttribP2uiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glVertexAttribP2uiv(GLuint index, "
        "GLenum type, GLboolean normalized, const GLuint *value)': names "
        "'GLuint', which has no cute class yet.")

  @staticmethod
  def glVertexAttribP3uiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttribP3uiv(GLuint index,
    GLenum type, GLboolean normalized, const GLuint *value)': names 'GLuint',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glVertexAttribP3uiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glVertexAttribP3uiv(GLuint index, "
        "GLenum type, GLboolean normalized, const GLuint *value)': names "
        "'GLuint', which has no cute class yet.")

  @staticmethod
  def glVertexAttribP4uiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttribP4uiv(GLuint index,
    GLenum type, GLboolean normalized, const GLuint *value)': names 'GLuint',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glVertexAttribP4uiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glVertexAttribP4uiv(GLuint index, "
        "GLenum type, GLboolean normalized, const GLuint *value)': names "
        "'GLuint', which has no cute class yet.")

  @staticmethod
  def glVertexAttribPointer(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glVertexAttribPointer(GLuint index,
    GLint size, GLenum type, GLboolean normalized, GLsizei stride, const void
    *pointer)': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glVertexAttribPointer' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glVertexAttribPointer(GLuint index, "
        "GLint size, GLenum type, GLboolean normalized, GLsizei stride, "
        "const void *pointer)': names 'void', which has no cute class yet.")

  @staticmethod
  def glViewportArrayv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glViewportArrayv(GLuint first,
    GLsizei count, const GLfloat *v)': names 'GLfloat', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glViewportArrayv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_5_Core::glViewportArrayv(GLuint "
        "first, GLsizei count, const GLfloat *v)': names 'GLfloat', which "
        "has no cute class yet.")

  @staticmethod
  def glViewportIndexedfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glViewportIndexedfv(GLuint index,
    const GLfloat *v)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glViewportIndexedfv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_5_Core::glViewportIndexedfv(GLuint index, const "
        "GLfloat *v)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glWaitSync(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_5_Core::glWaitSync(GLsync sync, GLbitfield
    flags, GLuint64 timeout)': names 'struct __GLsync', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_5_Core.glWaitSync' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_4_5_Core::glWaitSync(GLsync sync, "
        "GLbitfield flags, GLuint64 timeout)': names 'struct __GLsync', "
        "which has no cute class yet.")
