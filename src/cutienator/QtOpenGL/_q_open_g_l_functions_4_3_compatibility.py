"""
QOpenGLFunctions_4_3_Compatibility binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpenGL/qopenglfunctions_4_3_compatibility.h, Qt 6.12.0. Changes made
#  here are lost.
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


class QOpenGLFunctions_4_3_Compatibility(QAbstractOpenGLFunctions):
  """
  The cute side of Qt's QOpenGLFunctions_4_3_Compatibility: a plain Python
  object standing in front of one C++ QOpenGLFunctions_4_3_Compatibility.

  It is built on the cute 'QAbstractOpenGLFunctions', as Qt's
  QOpenGLFunctions_4_3_Compatibility is built on Qt's
  QAbstractOpenGLFunctions, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QOpenGLFunctions_4_3_Compatibility that has a ritual
  and that Python can call so far, 437 names in all:
  'initializeOpenGLFunctions', 'glViewport', 'glDepthRange', 'glIsEnabled',
  'glGetError', 'glReadBuffer', 'glPixelStorei', 'glPixelStoref',
  'glDepthFunc', 'glStencilOp', 'glStencilFunc', 'glLogicOp', 'glBlendFunc',
  'glFlush', 'glFinish', 'glEnable', 'glDisable', 'glDepthMask',
  'glColorMask', 'glStencilMask', 'glClearDepth', 'glClearStencil',
  'glClearColor', 'glClear', 'glDrawBuffer', 'glTexParameteri',
  'glTexParameterf', 'glScissor', 'glPolygonMode', 'glPointSize',
  'glLineWidth', 'glHint', 'glFrontFace', 'glCullFace', 'glIndexub',
  'glIsTexture', 'glBindTexture', 'glCopyTexSubImage2D',
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
  'glVertexAttribP2ui', 'glVertexAttribP1ui', 'glSecondaryColorP3ui',
  'glColorP4ui', 'glColorP3ui', 'glNormalP3ui', 'glMultiTexCoordP4ui',
  'glMultiTexCoordP3ui', 'glMultiTexCoordP2ui', 'glMultiTexCoordP1ui',
  'glTexCoordP4ui', 'glTexCoordP3ui', 'glTexCoordP2ui', 'glTexCoordP1ui',
  'glVertexP4ui', 'glVertexP3ui', 'glVertexP2ui', 'glQueryCounter',
  'glSamplerParameterf', 'glSamplerParameteri', 'glBindSampler',
  'glIsSampler', 'glVertexAttribDivisor', 'glEndQueryIndexed',
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
  'glTexStorage3D', 'glTexStorage2D', 'glTexStorage1D', 'glMemoryBarrier',
  'glBindImageTexture', 'glDrawTransformFeedbackStreamInstanced',
  'glDrawTransformFeedbackInstanced', 'glDrawArraysInstancedBaseInstance',
  'glTexStorage3DMultisample', 'glTexStorage2DMultisample',
  'glTexBufferRange', 'glShaderStorageBlockBinding',
  'glInvalidateBufferData', 'glInvalidateBufferSubData',
  'glInvalidateTexImage', 'glInvalidateTexSubImage',
  'glFramebufferParameteri', 'glVertexBindingDivisor',
  'glVertexAttribBinding', 'glVertexAttribLFormat', 'glVertexAttribIFormat',
  'glVertexAttribFormat', 'glBindVertexBuffer', 'glTextureView',
  'glCopyImageSubData', 'glDispatchComputeIndirect', 'glDispatchCompute',
  'glTranslatef', 'glTranslated', 'glScalef', 'glScaled', 'glRotatef',
  'glRotated', 'glPushMatrix', 'glPopMatrix', 'glOrtho', 'glMatrixMode',
  'glLoadIdentity', 'glFrustum', 'glIsList', 'glCopyPixels',
  'glPixelTransferi', 'glPixelTransferf', 'glPixelZoom', 'glAlphaFunc',
  'glEvalPoint2', 'glEvalMesh2', 'glEvalPoint1', 'glEvalMesh1',
  'glEvalCoord2f', 'glEvalCoord2d', 'glEvalCoord1f', 'glEvalCoord1d',
  'glMapGrid2f', 'glMapGrid2d', 'glMapGrid1f', 'glMapGrid1d', 'glPushAttrib',
  'glPopAttrib', 'glAccum', 'glIndexMask', 'glClearIndex', 'glClearAccum',
  'glPushName', 'glPopName', 'glPassThrough', 'glLoadName', 'glInitNames',
  'glRenderMode', 'glTexGeni', 'glTexGenf', 'glTexGend', 'glTexEnvi',
  'glTexEnvf', 'glShadeModel', 'glMateriali', 'glMaterialf', 'glLineStipple',
  'glLightModeli', 'glLightModelf', 'glLighti', 'glLightf', 'glFogi',
  'glFogf', 'glColorMaterial', 'glVertex4s', 'glVertex4i', 'glVertex4f',
  'glVertex4d', 'glVertex3s', 'glVertex3i', 'glVertex3f', 'glVertex3d',
  'glVertex2s', 'glVertex2i', 'glVertex2f', 'glVertex2d', 'glTexCoord4s',
  'glTexCoord4i', 'glTexCoord4f', 'glTexCoord4d', 'glTexCoord3s',
  'glTexCoord3i', 'glTexCoord3f', 'glTexCoord3d', 'glTexCoord2s',
  'glTexCoord2i', 'glTexCoord2f', 'glTexCoord2d', 'glTexCoord1s',
  'glTexCoord1i', 'glTexCoord1f', 'glTexCoord1d', 'glRects', 'glRecti',
  'glRectf', 'glRectd', 'glRasterPos4s', 'glRasterPos4i', 'glRasterPos4f',
  'glRasterPos4d', 'glRasterPos3s', 'glRasterPos3i', 'glRasterPos3f',
  'glRasterPos3d', 'glRasterPos2s', 'glRasterPos2i', 'glRasterPos2f',
  'glRasterPos2d', 'glNormal3s', 'glNormal3i', 'glNormal3f', 'glNormal3d',
  'glNormal3b', 'glIndexs', 'glIndexi', 'glIndexf', 'glIndexd', 'glEnd',
  'glEdgeFlag', 'glColor4us', 'glColor4ui', 'glColor4ub', 'glColor4s',
  'glColor4i', 'glColor4f', 'glColor4d', 'glColor4b', 'glColor3us',
  'glColor3ui', 'glColor3ub', 'glColor3s', 'glColor3i', 'glColor3f',
  'glColor3d', 'glColor3b', 'glBegin', 'glListBase', 'glGenLists',
  'glDeleteLists', 'glCallList', 'glEndList', 'glNewList',
  'glPushClientAttrib', 'glPopClientAttrib', 'glEnableClientState',
  'glDisableClientState', 'glArrayElement', 'glResetMinmax',
  'glResetHistogram', 'glMinmax', 'glHistogram', 'glCopyConvolutionFilter2D',
  'glCopyConvolutionFilter1D', 'glConvolutionParameteri',
  'glConvolutionParameterf', 'glCopyColorSubTable', 'glCopyColorTable',
  'glMultiTexCoord4s', 'glMultiTexCoord4i', 'glMultiTexCoord4f',
  'glMultiTexCoord4d', 'glMultiTexCoord3s', 'glMultiTexCoord3i',
  'glMultiTexCoord3f', 'glMultiTexCoord3d', 'glMultiTexCoord2s',
  'glMultiTexCoord2i', 'glMultiTexCoord2f', 'glMultiTexCoord2d',
  'glMultiTexCoord1s', 'glMultiTexCoord1i', 'glMultiTexCoord1f',
  'glMultiTexCoord1d', 'glClientActiveTexture', 'glWindowPos3s',
  'glWindowPos3i', 'glWindowPos3f', 'glWindowPos3d', 'glWindowPos2s',
  'glWindowPos2i', 'glWindowPos2f', 'glWindowPos2d', 'glSecondaryColor3us',
  'glSecondaryColor3ui', 'glSecondaryColor3ub', 'glSecondaryColor3s',
  'glSecondaryColor3i', 'glSecondaryColor3f', 'glSecondaryColor3d',
  'glSecondaryColor3b', 'glFogCoordd', 'glFogCoordf', 'glVertexAttrib4s',
  'glVertexAttrib4f', 'glVertexAttrib4d', 'glVertexAttrib4Nub',
  'glVertexAttrib3s', 'glVertexAttrib3f', 'glVertexAttrib3d',
  'glVertexAttrib2s', 'glVertexAttrib2f', 'glVertexAttrib2d',
  'glVertexAttrib1s', 'glVertexAttrib1f', 'glVertexAttrib1d',
  'glVertexAttribI4ui', 'glVertexAttribI3ui', 'glVertexAttribI2ui',
  'glVertexAttribI1ui', 'glVertexAttribI4i', 'glVertexAttribI3i',
  'glVertexAttribI2i', 'glVertexAttribI1i', 'isContextCompatible',
  'versionProfile'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'QOpenGLFunctions_4_3_Compatibility::~QOpenGLFunctions_4_3_Compatibility(
    )': the destructor: Python never removes a C++
    QOpenGLFunctions_4_3_Compatibility.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetTexLevelParameteriv(GLenum
    target, GLint level, GLenum pname, GLint *params)': takes a number to
    change where it is.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetTexLevelParameterfv(GLenum
    target, GLint level, GLenum pname, GLfloat *params)': takes a number to
    change where it is.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetTexParameteriv(GLenum
    target, GLenum pname, GLint *params)': takes a number to change where it
    is.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetTexParameterfv(GLenum
    target, GLenum pname, GLfloat *params)': takes a number to change where
    it is.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetTexImage(GLenum
    target, GLint level, GLenum format, GLenum type, GLvoid *pixels)': names
    'GLvoid', which has no cute class yet.
  - Qt's 'const GLubyte
    *QOpenGLFunctions_4_3_Compatibility::glGetString(GLenum name)': gives
    'unsigned char', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetIntegerv(GLenum
    pname, GLint *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetFloatv(GLenum pname,
    GLfloat *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetDoublev(GLenum pname,
    GLdouble *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetBooleanv(GLenum
    pname, GLboolean *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glReadPixels(GLint x,
    GLint y, GLsizei width, GLsizei height, GLenum format, GLenum type,
    GLvoid *pixels)': names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexImage2D(GLenum
    target, GLint level, GLint internalformat, GLsizei width, GLsizei height,
    GLint border, GLenum format, GLenum type, const GLvoid *pixels)': names
    'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexImage1D(GLenum
    target, GLint level, GLint internalformat, GLsizei width, GLint border,
    GLenum format, GLenum type, const GLvoid *pixels)': names 'GLvoid', which
    has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexParameteriv(GLenum
    target, GLenum pname, const GLint *params)': names 'GLint', which has no
    cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexParameterfv(GLenum
    target, GLenum pname, const GLfloat *params)': names 'GLfloat', which has
    no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glIndexubv(const GLubyte
    *c)': names 'GLubyte', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGenTextures(GLsizei n,
    GLuint *textures)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glDeleteTextures(GLsizei
    n, const GLuint *textures)': names 'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexSubImage2D(GLenum
    target, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei
    height, GLenum format, GLenum type, const GLvoid *pixels)': names
    'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexSubImage1D(GLenum
    target, GLint level, GLint xoffset, GLsizei width, GLenum format, GLenum
    type, const GLvoid *pixels)': names 'GLvoid', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetPointerv(GLenum
    pname, GLvoid **params)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glDrawElements(GLenum
    mode, GLsizei count, GLenum type, const GLvoid *indices)': names
    'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexSubImage3D(GLenum
    target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei
    width, GLsizei height, GLsizei depth, GLenum format, GLenum type, const
    GLvoid *pixels)': names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexImage3D(GLenum
    target, GLint level, GLint internalformat, GLsizei width, GLsizei height,
    GLsizei depth, GLint border, GLenum format, GLenum type, const GLvoid
    *pixels)': names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glDrawRangeElements(GLenum
    mode, GLuint start, GLuint end, GLsizei count, GLenum type, const GLvoid
    *indices)': names 'GLvoid', which has no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetCompressedTexImage(GLenum
    target, GLint level, GLvoid *img)': names 'GLvoid', which has no cute
    class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glCompressedTexSubImage1D(GLenum
    target, GLint level, GLint xoffset, GLsizei width, GLenum format, GLsizei
    imageSize, const GLvoid *data)': names 'GLvoid', which has no cute class
    yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glCompressedTexSubImage2D(GLenum
    target, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei
    height, GLenum format, GLsizei imageSize, const GLvoid *data)': names
    'GLvoid', which has no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glCompressedTexSubImage3D(GLenum
    target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei
    width, GLsizei height, GLsizei depth, GLenum format, GLsizei imageSize,
    const GLvoid *data)': names 'GLvoid', which has no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glCompressedTexImage1D(GLenum target,
    GLint level, GLenum internalformat, GLsizei width, GLint border, GLsizei
    imageSize, const GLvoid *data)': names 'GLvoid', which has no cute class
    yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glCompressedTexImage2D(GLenum target,
    GLint level, GLenum internalformat, GLsizei width, GLsizei height, GLint
    border, GLsizei imageSize, const GLvoid *data)': names 'GLvoid', which
    has no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glCompressedTexImage3D(GLenum target,
    GLint level, GLenum internalformat, GLsizei width, GLsizei height,
    GLsizei depth, GLint border, GLsizei imageSize, const GLvoid *data)':
    names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glPointParameteriv(GLenum
    pname, const GLint *params)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glPointParameterfv(GLenum
    pname, const GLfloat *params)': names 'GLfloat', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glMultiDrawElements(GLenum
    mode, const GLsizei *count, GLenum type, const GLvoid *const *indices,
    GLsizei drawcount)': names 'GLsizei', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glMultiDrawArrays(GLenum
    mode, const GLint *first, const GLsizei *count, GLsizei drawcount)':
    names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetBufferPointerv(GLenum
    target, GLenum pname, GLvoid **params)': takes a type Python has no way
    to hand over yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetBufferParameteriv(GLenum target,
    GLenum pname, GLint *params)': takes a number to change where it is.
  - Qt's 'GLvoid *QOpenGLFunctions_4_3_Compatibility::glMapBuffer(GLenum
    target, GLenum access)': gives 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetBufferSubData(GLenum
    target, GLintptr offset, GLsizeiptr size, GLvoid *data)': names 'GLvoid',
    which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glBufferSubData(GLenum
    target, GLintptr offset, GLsizeiptr size, const GLvoid *data)': names
    'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glBufferData(GLenum
    target, GLsizeiptr size, const GLvoid *data, GLenum usage)': names
    'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGenBuffers(GLsizei n,
    GLuint *buffers)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glDeleteBuffers(GLsizei n,
    const GLuint *buffers)': names 'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetQueryObjectuiv(GLuint
    id, GLenum pname, GLuint *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetQueryObjectiv(GLuint
    id, GLenum pname, GLint *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetQueryiv(GLenum
    target, GLenum pname, GLint *params)': takes a number to change where it
    is.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glDeleteQueries(GLsizei n,
    const GLuint *ids)': names 'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGenQueries(GLsizei n,
    GLuint *ids)': takes a number to change where it is.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glVertexAttribPointer(GLuint index,
    GLint size, GLenum type, GLboolean normalized, GLsizei stride, const
    GLvoid *pointer)': names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniformMatrix4fv(GLint
    location, GLsizei count, GLboolean transpose, const GLfloat *value)':
    names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniformMatrix3fv(GLint
    location, GLsizei count, GLboolean transpose, const GLfloat *value)':
    names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniformMatrix2fv(GLint
    location, GLsizei count, GLboolean transpose, const GLfloat *value)':
    names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniform4iv(GLint
    location, GLsizei count, const GLint *value)': names 'GLint', which has
    no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniform3iv(GLint
    location, GLsizei count, const GLint *value)': names 'GLint', which has
    no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniform2iv(GLint
    location, GLsizei count, const GLint *value)': names 'GLint', which has
    no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniform1iv(GLint
    location, GLsizei count, const GLint *value)': names 'GLint', which has
    no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniform4fv(GLint
    location, GLsizei count, const GLfloat *value)': names 'GLfloat', which
    has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniform3fv(GLint
    location, GLsizei count, const GLfloat *value)': names 'GLfloat', which
    has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniform2fv(GLint
    location, GLsizei count, const GLfloat *value)': names 'GLfloat', which
    has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniform1fv(GLint
    location, GLsizei count, const GLfloat *value)': names 'GLfloat', which
    has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glShaderSource(GLuint
    shader, GLsizei count, const GLchar *const *string, const GLint
    *length)': names 'GLchar *const', which has no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetVertexAttribPointerv(GLuint
    index, GLenum pname, GLvoid **pointer)': takes a type Python has no way
    to hand over yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetVertexAttribiv(GLuint
    index, GLenum pname, GLint *params)': takes a number to change where it
    is.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetVertexAttribfv(GLuint
    index, GLenum pname, GLfloat *params)': takes a number to change where it
    is.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetVertexAttribdv(GLuint
    index, GLenum pname, GLdouble *params)': takes a number to change where
    it is.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetUniformiv(GLuint
    program, GLint location, GLint *params)': takes a number to change where
    it is.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetUniformfv(GLuint
    program, GLint location, GLfloat *params)': takes a number to change
    where it is.
  - Qt's 'GLint
    QOpenGLFunctions_4_3_Compatibility::glGetUniformLocation(GLuint program,
    const GLchar *name)': names 'GLchar', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetShaderSource(GLuint
    shader, GLsizei bufSize, GLsizei *length, GLchar *source)': takes a
    number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetShaderInfoLog(GLuint
    shader, GLsizei bufSize, GLsizei *length, GLchar *infoLog)': takes a
    number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetShaderiv(GLuint
    shader, GLenum pname, GLint *params)': takes a number to change where it
    is.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetProgramInfoLog(GLuint
    program, GLsizei bufSize, GLsizei *length, GLchar *infoLog)': takes a
    number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetProgramiv(GLuint
    program, GLenum pname, GLint *params)': takes a number to change where it
    is.
  - Qt's 'GLint
    QOpenGLFunctions_4_3_Compatibility::glGetAttribLocation(GLuint program,
    const GLchar *name)': names 'GLchar', which has no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetAttachedShaders(GLuint program,
    GLsizei maxCount, GLsizei *count, GLuint *obj)': takes a number to change
    where it is.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetActiveUniform(GLuint
    program, GLuint index, GLsizei bufSize, GLsizei *length, GLint *size,
    GLenum *type, GLchar *name)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetActiveAttrib(GLuint
    program, GLuint index, GLsizei bufSize, GLsizei *length, GLint *size,
    GLenum *type, GLchar *name)': takes a number to change where it is.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glBindAttribLocation(GLuint program,
    GLuint index, const GLchar *name)': names 'GLchar', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glDrawBuffers(GLsizei n,
    const GLenum *bufs)': names 'GLenum', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniformMatrix4x3fv(GLint
    location, GLsizei count, GLboolean transpose, const GLfloat *value)':
    names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniformMatrix3x4fv(GLint
    location, GLsizei count, GLboolean transpose, const GLfloat *value)':
    names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniformMatrix4x2fv(GLint
    location, GLsizei count, GLboolean transpose, const GLfloat *value)':
    names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniformMatrix2x4fv(GLint
    location, GLsizei count, GLboolean transpose, const GLfloat *value)':
    names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniformMatrix3x2fv(GLint
    location, GLsizei count, GLboolean transpose, const GLfloat *value)':
    names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniformMatrix2x3fv(GLint
    location, GLsizei count, GLboolean transpose, const GLfloat *value)':
    names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGenVertexArrays(GLsizei
    n, GLuint *arrays)': takes a number to change where it is.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glDeleteVertexArrays(GLsizei n, const
    GLuint *arrays)': names 'GLuint', which has no cute class yet.
  - Qt's 'GLvoid *QOpenGLFunctions_4_3_Compatibility::glMapBufferRange(GLenum
    target, GLintptr offset, GLsizeiptr length, GLbitfield access)': gives
    'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::
    glGetFramebufferAttachmentParameteriv(GLenum target, GLenum attachment,
    GLenum pname, GLint *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGenFramebuffers(GLsizei
    n, GLuint *framebuffers)': takes a number to change where it is.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glDeleteFramebuffers(GLsizei n, const
    GLuint *framebuffers)': names 'GLuint', which has no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetRenderbufferParameteriv(GLenum
    target, GLenum pname, GLint *params)': takes a number to change where it
    is.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGenRenderbuffers(GLsizei
    n, GLuint *renderbuffers)': takes a number to change where it is.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glDeleteRenderbuffers(GLsizei n,
    const GLuint *renderbuffers)': names 'GLuint', which has no cute class
    yet.
  - Qt's 'const GLubyte
    *QOpenGLFunctions_4_3_Compatibility::glGetStringi(GLenum name, GLuint
    index)': gives 'unsigned char', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glClearBufferfv(GLenum
    buffer, GLint drawbuffer, const GLfloat *value)': names 'GLfloat', which
    has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glClearBufferuiv(GLenum
    buffer, GLint drawbuffer, const GLuint *value)': names 'GLuint', which
    has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glClearBufferiv(GLenum
    buffer, GLint drawbuffer, const GLint *value)': names 'GLint', which has
    no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetTexParameterIuiv(GLenum target,
    GLenum pname, GLuint *params)': takes a number to change where it is.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetTexParameterIiv(GLenum target,
    GLenum pname, GLint *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexParameterIuiv(GLenum
    target, GLenum pname, const GLuint *params)': names 'GLuint', which has
    no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexParameterIiv(GLenum
    target, GLenum pname, const GLint *params)': names 'GLint', which has no
    cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniform4uiv(GLint
    location, GLsizei count, const GLuint *value)': names 'GLuint', which has
    no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniform3uiv(GLint
    location, GLsizei count, const GLuint *value)': names 'GLuint', which has
    no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniform2uiv(GLint
    location, GLsizei count, const GLuint *value)': names 'GLuint', which has
    no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniform1uiv(GLint
    location, GLsizei count, const GLuint *value)': names 'GLuint', which has
    no cute class yet.
  - Qt's 'GLint
    QOpenGLFunctions_4_3_Compatibility::glGetFragDataLocation(GLuint program,
    const GLchar *name)': names 'GLchar', which has no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glBindFragDataLocation(GLuint
    program, GLuint color, const GLchar *name)': names 'GLchar', which has no
    cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetUniformuiv(GLuint
    program, GLint location, GLuint *params)': takes a number to change where
    it is.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetVertexAttribIuiv(GLuint index,
    GLenum pname, GLuint *params)': takes a number to change where it is.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetVertexAttribIiv(GLuint index,
    GLenum pname, GLint *params)': takes a number to change where it is.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glVertexAttribIPointer(GLuint index,
    GLint size, GLenum type, GLsizei stride, const GLvoid *pointer)': names
    'GLvoid', which has no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetTransformFeedbackVarying(GLuint
    program, GLuint index, GLsizei bufSize, GLsizei *length, GLsizei *size,
    GLenum *type, GLchar *name)': takes a number to change where it is.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glTransformFeedbackVaryings(GLuint
    program, GLsizei count, const GLchar *const *varyings, GLenum
    bufferMode)': names 'GLchar *const', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetIntegeri_v(GLenum
    target, GLuint index, GLint *data)': takes a number to change where it
    is.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetBooleani_v(GLenum
    target, GLuint index, GLboolean *data)': takes a number to change where
    it is.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetActiveUniformBlockName(GLuint
    program, GLuint uniformBlockIndex, GLsizei bufSize, GLsizei *length,
    GLchar *uniformBlockName)': takes a number to change where it is.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetActiveUniformBlockiv(GLuint
    program, GLuint uniformBlockIndex, GLenum pname, GLint *params)': takes a
    number to change where it is.
  - Qt's 'GLuint
    QOpenGLFunctions_4_3_Compatibility::glGetUniformBlockIndex(GLuint
    program, const GLchar *uniformBlockName)': names 'GLchar', which has no
    cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetActiveUniformName(GLuint
    program, GLuint uniformIndex, GLsizei bufSize, GLsizei *length, GLchar
    *uniformName)': takes a number to change where it is.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetActiveUniformsiv(GLuint program,
    GLsizei uniformCount, const GLuint *uniformIndices, GLenum pname, GLint
    *params)': names 'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetUniformIndices(GLuint
    program, GLsizei uniformCount, const GLchar *const *uniformNames, GLuint
    *uniformIndices)': names 'GLchar *const', which has no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glDrawElementsInstanced(GLenum mode,
    GLsizei count, GLenum type, const GLvoid *indices, GLsizei
    instancecount)': names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetMultisamplefv(GLenum
    pname, GLuint index, GLfloat *val)': takes a number to change where it
    is.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetSynciv(GLsync sync,
    GLenum pname, GLsizei bufSize, GLsizei *length, GLint *values)': names
    'struct __GLsync', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetInteger64v(GLenum
    pname, GLint64 *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glWaitSync(GLsync sync,
    GLbitfield flags, GLuint64 timeout)': names 'struct __GLsync', which has
    no cute class yet.
  - Qt's 'GLenum QOpenGLFunctions_4_3_Compatibility::glClientWaitSync(GLsync
    sync, GLbitfield flags, GLuint64 timeout)': names 'struct __GLsync',
    which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glDeleteSync(GLsync
    sync)': names 'struct __GLsync', which has no cute class yet.
  - Qt's 'GLboolean QOpenGLFunctions_4_3_Compatibility::glIsSync(GLsync
    sync)': names 'struct __GLsync', which has no cute class yet.
  - Qt's 'GLsync QOpenGLFunctions_4_3_Compatibility::glFenceSync(GLenum
    condition, GLbitfield flags)': gives a type Python has no way to take
    yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glMultiDrawElementsBaseVertex(GLenum
    mode, const GLsizei *count, GLenum type, const GLvoid *const *indices,
    GLsizei drawcount, const GLint *basevertex)': names 'GLsizei', which has
    no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glDrawElementsInstancedBaseVertex(
    GLenum mode, GLsizei count, GLenum type, const GLvoid *indices, GLsizei
    instancecount, GLint basevertex)': names 'GLvoid', which has no cute
    class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glDrawRangeElementsBaseVertex(GLenum
    mode, GLuint start, GLuint end, GLsizei count, GLenum type, const GLvoid
    *indices, GLint basevertex)': names 'GLvoid', which has no cute class
    yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glDrawElementsBaseVertex(GLenum mode,
    GLsizei count, GLenum type, const GLvoid *indices, GLint basevertex)':
    names 'GLvoid', which has no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetBufferParameteri64v(GLenum
    target, GLenum pname, GLint64 *params)': takes a number to change where
    it is.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetInteger64i_v(GLenum
    target, GLuint index, GLint64 *data)': takes a number to change where it
    is.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttribP4uiv(GLuint
    index, GLenum type, GLboolean normalized, const GLuint *value)': names
    'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttribP3uiv(GLuint
    index, GLenum type, GLboolean normalized, const GLuint *value)': names
    'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttribP2uiv(GLuint
    index, GLenum type, GLboolean normalized, const GLuint *value)': names
    'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttribP1uiv(GLuint
    index, GLenum type, GLboolean normalized, const GLuint *value)': names
    'GLuint', which has no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glSecondaryColorP3uiv(GLenum type,
    const GLuint *color)': names 'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glColorP4uiv(GLenum type,
    const GLuint *color)': names 'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glColorP3uiv(GLenum type,
    const GLuint *color)': names 'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glNormalP3uiv(GLenum type,
    const GLuint *coords)': names 'GLuint', which has no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glMultiTexCoordP4uiv(GLenum texture,
    GLenum type, const GLuint *coords)': names 'GLuint', which has no cute
    class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glMultiTexCoordP3uiv(GLenum texture,
    GLenum type, const GLuint *coords)': names 'GLuint', which has no cute
    class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glMultiTexCoordP2uiv(GLenum texture,
    GLenum type, const GLuint *coords)': names 'GLuint', which has no cute
    class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glMultiTexCoordP1uiv(GLenum texture,
    GLenum type, const GLuint *coords)': names 'GLuint', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexCoordP4uiv(GLenum
    type, const GLuint *coords)': names 'GLuint', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexCoordP3uiv(GLenum
    type, const GLuint *coords)': names 'GLuint', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexCoordP2uiv(GLenum
    type, const GLuint *coords)': names 'GLuint', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexCoordP1uiv(GLenum
    type, const GLuint *coords)': names 'GLuint', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexP4uiv(GLenum type,
    const GLuint *value)': names 'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexP3uiv(GLenum type,
    const GLuint *value)': names 'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexP2uiv(GLenum type,
    const GLuint *value)': names 'GLuint', which has no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetQueryObjectui64v(GLuint id,
    GLenum pname, GLuint64 *params)': takes a number to change where it is.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetQueryObjecti64v(GLuint id,
    GLenum pname, GLint64 *params)': takes a number to change where it is.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetSamplerParameterIuiv(GLuint
    sampler, GLenum pname, GLuint *params)': takes a number to change where
    it is.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetSamplerParameterfv(GLuint
    sampler, GLenum pname, GLfloat *params)': takes a number to change where
    it is.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetSamplerParameterIiv(GLuint
    sampler, GLenum pname, GLint *params)': takes a number to change where it
    is.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetSamplerParameteriv(GLuint
    sampler, GLenum pname, GLint *params)': takes a number to change where it
    is.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glSamplerParameterIuiv(GLuint
    sampler, GLenum pname, const GLuint *param)': names 'GLuint', which has
    no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glSamplerParameterIiv(GLuint sampler,
    GLenum pname, const GLint *param)': names 'GLint', which has no cute
    class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glSamplerParameterfv(GLuint sampler,
    GLenum pname, const GLfloat *param)': names 'GLfloat', which has no cute
    class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glSamplerParameteriv(GLuint sampler,
    GLenum pname, const GLint *param)': names 'GLint', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glDeleteSamplers(GLsizei
    count, const GLuint *samplers)': names 'GLuint', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGenSamplers(GLsizei
    count, GLuint *samplers)': takes a number to change where it is.
  - Qt's 'GLint QOpenGLFunctions_4_3_Compatibility::glGetFragDataIndex(GLuint
    program, const GLchar *name)': names 'GLchar', which has no cute class
    yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glBindFragDataLocationIndexed(GLuint
    program, GLuint colorNumber, GLuint index, const GLchar *name)': names
    'GLchar', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetQueryIndexediv(GLenum
    target, GLuint index, GLenum pname, GLint *params)': takes a number to
    change where it is.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGenTransformFeedbacks(GLsizei n,
    GLuint *ids)': takes a number to change where it is.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glDeleteTransformFeedbacks(GLsizei n,
    const GLuint *ids)': names 'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glPatchParameterfv(GLenum
    pname, const GLfloat *values)': names 'GLfloat', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetProgramStageiv(GLuint
    program, GLenum shadertype, GLenum pname, GLint *values)': takes a number
    to change where it is.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetUniformSubroutineuiv(GLenum
    shadertype, GLint location, GLuint *params)': takes a number to change
    where it is.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glUniformSubroutinesuiv(GLenum
    shadertype, GLsizei count, const GLuint *indices)': names 'GLuint', which
    has no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetActiveSubroutineName(GLuint
    program, GLenum shadertype, GLuint index, GLsizei bufsize, GLsizei
    *length, GLchar *name)': takes a number to change where it is.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetActiveSubroutineUniformName(
    GLuint program, GLenum shadertype, GLuint index, GLsizei bufsize, GLsizei
    *length, GLchar *name)': takes a number to change where it is.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetActiveSubroutineUniformiv(GLuint
    program, GLenum shadertype, GLuint index, GLenum pname, GLint *values)':
    takes a number to change where it is.
  - Qt's 'GLuint
    QOpenGLFunctions_4_3_Compatibility::glGetSubroutineIndex(GLuint program,
    GLenum shadertype, const GLchar *name)': names 'GLchar', which has no
    cute class yet.
  - Qt's 'GLint
    QOpenGLFunctions_4_3_Compatibility::glGetSubroutineUniformLocation(GLuint
    program, GLenum shadertype, const GLchar *name)': names 'GLchar', which
    has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetUniformdv(GLuint
    program, GLint location, GLdouble *params)': takes a number to change
    where it is.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniformMatrix4x3dv(GLint
    location, GLsizei count, GLboolean transpose, const GLdouble *value)':
    names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniformMatrix4x2dv(GLint
    location, GLsizei count, GLboolean transpose, const GLdouble *value)':
    names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniformMatrix3x4dv(GLint
    location, GLsizei count, GLboolean transpose, const GLdouble *value)':
    names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniformMatrix3x2dv(GLint
    location, GLsizei count, GLboolean transpose, const GLdouble *value)':
    names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniformMatrix2x4dv(GLint
    location, GLsizei count, GLboolean transpose, const GLdouble *value)':
    names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniformMatrix2x3dv(GLint
    location, GLsizei count, GLboolean transpose, const GLdouble *value)':
    names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniformMatrix4dv(GLint
    location, GLsizei count, GLboolean transpose, const GLdouble *value)':
    names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniformMatrix3dv(GLint
    location, GLsizei count, GLboolean transpose, const GLdouble *value)':
    names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniformMatrix2dv(GLint
    location, GLsizei count, GLboolean transpose, const GLdouble *value)':
    names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniform4dv(GLint
    location, GLsizei count, const GLdouble *value)': names 'GLdouble', which
    has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniform3dv(GLint
    location, GLsizei count, const GLdouble *value)': names 'GLdouble', which
    has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniform2dv(GLint
    location, GLsizei count, const GLdouble *value)': names 'GLdouble', which
    has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniform1dv(GLint
    location, GLsizei count, const GLdouble *value)': names 'GLdouble', which
    has no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glDrawElementsIndirect(GLenum mode,
    GLenum type, const GLvoid *indirect)': names 'GLvoid', which has no cute
    class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glDrawArraysIndirect(GLenum mode,
    const GLvoid *indirect)': names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetDoublei_v(GLenum
    target, GLuint index, GLdouble *data)': takes a number to change where it
    is.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetFloati_v(GLenum
    target, GLuint index, GLfloat *data)': takes a number to change where it
    is.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glDepthRangeArrayv(GLuint
    first, GLsizei count, const GLdouble *v)': names 'GLdouble', which has no
    cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glScissorIndexedv(GLuint
    index, const GLint *v)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glScissorArrayv(GLuint
    first, GLsizei count, const GLint *v)': names 'GLint', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glViewportIndexedfv(GLuint
    index, const GLfloat *v)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glViewportArrayv(GLuint
    first, GLsizei count, const GLfloat *v)': names 'GLfloat', which has no
    cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetVertexAttribLdv(GLuint index,
    GLenum pname, GLdouble *params)': takes a number to change where it is.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glVertexAttribLPointer(GLuint index,
    GLint size, GLenum type, GLsizei stride, const GLvoid *pointer)': names
    'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttribL4dv(GLuint
    index, const GLdouble *v)': names 'GLdouble', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttribL3dv(GLuint
    index, const GLdouble *v)': names 'GLdouble', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttribL2dv(GLuint
    index, const GLdouble *v)': names 'GLdouble', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttribL1dv(GLuint
    index, const GLdouble *v)': names 'GLdouble', which has no cute class
    yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetProgramPipelineInfoLog(GLuint
    pipeline, GLsizei bufSize, GLsizei *length, GLchar *infoLog)': takes a
    number to change where it is.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glProgramUniformMatrix4x3dv(GLuint
    program, GLint location, GLsizei count, GLboolean transpose, const
    GLdouble *value)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glProgramUniformMatrix3x4dv(GLuint
    program, GLint location, GLsizei count, GLboolean transpose, const
    GLdouble *value)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glProgramUniformMatrix4x2dv(GLuint
    program, GLint location, GLsizei count, GLboolean transpose, const
    GLdouble *value)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glProgramUniformMatrix2x4dv(GLuint
    program, GLint location, GLsizei count, GLboolean transpose, const
    GLdouble *value)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glProgramUniformMatrix3x2dv(GLuint
    program, GLint location, GLsizei count, GLboolean transpose, const
    GLdouble *value)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glProgramUniformMatrix2x3dv(GLuint
    program, GLint location, GLsizei count, GLboolean transpose, const
    GLdouble *value)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glProgramUniformMatrix4x3fv(GLuint
    program, GLint location, GLsizei count, GLboolean transpose, const
    GLfloat *value)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glProgramUniformMatrix3x4fv(GLuint
    program, GLint location, GLsizei count, GLboolean transpose, const
    GLfloat *value)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glProgramUniformMatrix4x2fv(GLuint
    program, GLint location, GLsizei count, GLboolean transpose, const
    GLfloat *value)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glProgramUniformMatrix2x4fv(GLuint
    program, GLint location, GLsizei count, GLboolean transpose, const
    GLfloat *value)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glProgramUniformMatrix3x2fv(GLuint
    program, GLint location, GLsizei count, GLboolean transpose, const
    GLfloat *value)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glProgramUniformMatrix2x3fv(GLuint
    program, GLint location, GLsizei count, GLboolean transpose, const
    GLfloat *value)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glProgramUniformMatrix4dv(GLuint
    program, GLint location, GLsizei count, GLboolean transpose, const
    GLdouble *value)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glProgramUniformMatrix3dv(GLuint
    program, GLint location, GLsizei count, GLboolean transpose, const
    GLdouble *value)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glProgramUniformMatrix2dv(GLuint
    program, GLint location, GLsizei count, GLboolean transpose, const
    GLdouble *value)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glProgramUniformMatrix4fv(GLuint
    program, GLint location, GLsizei count, GLboolean transpose, const
    GLfloat *value)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glProgramUniformMatrix3fv(GLuint
    program, GLint location, GLsizei count, GLboolean transpose, const
    GLfloat *value)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glProgramUniformMatrix2fv(GLuint
    program, GLint location, GLsizei count, GLboolean transpose, const
    GLfloat *value)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glProgramUniform4uiv(GLuint program,
    GLint location, GLsizei count, const GLuint *value)': names 'GLuint',
    which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glProgramUniform4dv(GLuint
    program, GLint location, GLsizei count, const GLdouble *value)': names
    'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glProgramUniform4fv(GLuint
    program, GLint location, GLsizei count, const GLfloat *value)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glProgramUniform4iv(GLuint
    program, GLint location, GLsizei count, const GLint *value)': names
    'GLint', which has no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glProgramUniform3uiv(GLuint program,
    GLint location, GLsizei count, const GLuint *value)': names 'GLuint',
    which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glProgramUniform3dv(GLuint
    program, GLint location, GLsizei count, const GLdouble *value)': names
    'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glProgramUniform3fv(GLuint
    program, GLint location, GLsizei count, const GLfloat *value)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glProgramUniform3iv(GLuint
    program, GLint location, GLsizei count, const GLint *value)': names
    'GLint', which has no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glProgramUniform2uiv(GLuint program,
    GLint location, GLsizei count, const GLuint *value)': names 'GLuint',
    which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glProgramUniform2dv(GLuint
    program, GLint location, GLsizei count, const GLdouble *value)': names
    'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glProgramUniform2fv(GLuint
    program, GLint location, GLsizei count, const GLfloat *value)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glProgramUniform2iv(GLuint
    program, GLint location, GLsizei count, const GLint *value)': names
    'GLint', which has no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glProgramUniform1uiv(GLuint program,
    GLint location, GLsizei count, const GLuint *value)': names 'GLuint',
    which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glProgramUniform1dv(GLuint
    program, GLint location, GLsizei count, const GLdouble *value)': names
    'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glProgramUniform1fv(GLuint
    program, GLint location, GLsizei count, const GLfloat *value)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glProgramUniform1iv(GLuint
    program, GLint location, GLsizei count, const GLint *value)': names
    'GLint', which has no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetProgramPipelineiv(GLuint
    pipeline, GLenum pname, GLint *params)': takes a number to change where
    it is.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGenProgramPipelines(GLsizei n,
    GLuint *pipelines)': takes a number to change where it is.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glDeleteProgramPipelines(GLsizei n,
    const GLuint *pipelines)': names 'GLuint', which has no cute class yet.
  - Qt's 'GLuint
    QOpenGLFunctions_4_3_Compatibility::glCreateShaderProgramv(GLenum type,
    GLsizei count, const GLchar *const *strings)': names 'GLchar *const',
    which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glProgramBinary(GLuint
    program, GLenum binaryFormat, const GLvoid *binary, GLsizei length)':
    names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetProgramBinary(GLuint
    program, GLsizei bufSize, GLsizei *length, GLenum *binaryFormat, GLvoid
    *binary)': takes a number to change where it is.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetShaderPrecisionFormat(GLenum
    shadertype, GLenum precisiontype, GLint *range, GLint *precision)': takes
    a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glShaderBinary(GLsizei
    count, const GLuint *shaders, GLenum binaryformat, const GLvoid *binary,
    GLsizei length)': names 'GLuint', which has no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetActiveAtomicCounterBufferiv(
    GLuint program, GLuint bufferIndex, GLenum pname, GLint *params)': takes
    a number to change where it is.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetInternalformativ(GLenum target,
    GLenum internalformat, GLenum pname, GLsizei bufSize, GLint *params)':
    takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::
    glDrawElementsInstancedBaseVertexBaseInstance(GLenum mode, GLsizei count,
    GLenum type, const void *indices, GLsizei instancecount, GLint
    basevertex, GLuint baseinstance)': names 'void', which has no cute class
    yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glDrawElementsInstancedBaseInstance(
    GLenum mode, GLsizei count, GLenum type, const void *indices, GLsizei
    instancecount, GLuint baseinstance)': names 'void', which has no cute
    class yet.
  - Qt's 'GLint
    QOpenGLFunctions_4_3_Compatibility::glGetProgramResourceLocationIndex(
    GLuint program, GLenum programInterface, const GLchar *name)': names
    'GLchar', which has no cute class yet.
  - Qt's 'GLint
    QOpenGLFunctions_4_3_Compatibility::glGetProgramResourceLocation(GLuint
    program, GLenum programInterface, const GLchar *name)': names 'GLchar',
    which has no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetProgramResourceiv(GLuint
    program, GLenum programInterface, GLuint index, GLsizei propCount, const
    GLenum *props, GLsizei bufSize, GLsizei *length, GLint *params)': names
    'GLenum', which has no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetProgramResourceName(GLuint
    program, GLenum programInterface, GLuint index, GLsizei bufSize, GLsizei
    *length, GLchar *name)': takes a number to change where it is.
  - Qt's 'GLuint
    QOpenGLFunctions_4_3_Compatibility::glGetProgramResourceIndex(GLuint
    program, GLenum programInterface, const GLchar *name)': names 'GLchar',
    which has no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetProgramInterfaceiv(GLuint
    program, GLenum programInterface, GLenum pname, GLint *params)': takes a
    number to change where it is.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glMultiDrawElementsIndirect(GLenum
    mode, GLenum type, const void *indirect, GLsizei drawcount, GLsizei
    stride)': names 'void', which has no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glMultiDrawArraysIndirect(GLenum
    mode, const void *indirect, GLsizei drawcount, GLsizei stride)': names
    'void', which has no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glInvalidateSubFramebuffer(GLenum
    target, GLsizei numAttachments, const GLenum *attachments, GLint x, GLint
    y, GLsizei width, GLsizei height)': names 'GLenum', which has no cute
    class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glInvalidateFramebuffer(GLenum
    target, GLsizei numAttachments, const GLenum *attachments)': names
    'GLenum', which has no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetInternalformati64v(GLenum
    target, GLenum internalformat, GLenum pname, GLsizei bufSize, GLint64
    *params)': takes a number to change where it is.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetFramebufferParameteriv(GLenum
    target, GLenum pname, GLint *params)': takes a number to change where it
    is.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glClearBufferSubData(GLenum target,
    GLenum internalformat, GLintptr offset, GLsizeiptr size, GLenum format,
    GLenum type, const void *data)': names 'void', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glClearBufferData(GLenum
    target, GLenum internalformat, GLenum format, GLenum type, const void
    *data)': names 'void', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glMultMatrixd(const
    GLdouble *m)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glMultMatrixf(const
    GLfloat *m)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glLoadMatrixd(const
    GLdouble *m)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glLoadMatrixf(const
    GLfloat *m)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetTexGeniv(GLenum
    coord, GLenum pname, GLint *params)': takes a number to change where it
    is.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetTexGenfv(GLenum
    coord, GLenum pname, GLfloat *params)': takes a number to change where it
    is.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetTexGendv(GLenum
    coord, GLenum pname, GLdouble *params)': takes a number to change where
    it is.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetTexEnviv(GLenum
    target, GLenum pname, GLint *params)': takes a number to change where it
    is.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetTexEnvfv(GLenum
    target, GLenum pname, GLfloat *params)': takes a number to change where
    it is.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetPolygonStipple(GLubyte *mask)':
    takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetPixelMapusv(GLenum
    map, GLushort *values)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetPixelMapuiv(GLenum
    map, GLuint *values)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetPixelMapfv(GLenum
    map, GLfloat *values)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetMaterialiv(GLenum
    face, GLenum pname, GLint *params)': takes a number to change where it
    is.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetMaterialfv(GLenum
    face, GLenum pname, GLfloat *params)': takes a number to change where it
    is.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetMapiv(GLenum target,
    GLenum query, GLint *v)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetMapfv(GLenum target,
    GLenum query, GLfloat *v)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetMapdv(GLenum target,
    GLenum query, GLdouble *v)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetLightiv(GLenum light,
    GLenum pname, GLint *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetLightfv(GLenum light,
    GLenum pname, GLfloat *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetClipPlane(GLenum
    plane, GLdouble *equation)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glDrawPixels(GLsizei
    width, GLsizei height, GLenum format, GLenum type, const GLvoid
    *pixels)': names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glPixelMapusv(GLenum map,
    GLint mapsize, const GLushort *values)': names 'GLushort', which has no
    cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glPixelMapuiv(GLenum map,
    GLint mapsize, const GLuint *values)': names 'GLuint', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glPixelMapfv(GLenum map,
    GLint mapsize, const GLfloat *values)': names 'GLfloat', which has no
    cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glEvalCoord2fv(const
    GLfloat *u)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glEvalCoord2dv(const
    GLdouble *u)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glEvalCoord1fv(const
    GLfloat *u)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glEvalCoord1dv(const
    GLdouble *u)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glMap2f(GLenum target,
    GLfloat u1, GLfloat u2, GLint ustride, GLint uorder, GLfloat v1, GLfloat
    v2, GLint vstride, GLint vorder, const GLfloat *points)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glMap2d(GLenum target,
    GLdouble u1, GLdouble u2, GLint ustride, GLint uorder, GLdouble v1,
    GLdouble v2, GLint vstride, GLint vorder, const GLdouble *points)': names
    'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glMap1f(GLenum target,
    GLfloat u1, GLfloat u2, GLint stride, GLint order, const GLfloat
    *points)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glMap1d(GLenum target,
    GLdouble u1, GLdouble u2, GLint stride, GLint order, const GLdouble
    *points)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glSelectBuffer(GLsizei
    size, GLuint *buffer)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glFeedbackBuffer(GLsizei
    size, GLenum type, GLfloat *buffer)': takes a number to change where it
    is.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexGeniv(GLenum coord,
    GLenum pname, const GLint *params)': names 'GLint', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexGenfv(GLenum coord,
    GLenum pname, const GLfloat *params)': names 'GLfloat', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexGendv(GLenum coord,
    GLenum pname, const GLdouble *params)': names 'GLdouble', which has no
    cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexEnviv(GLenum target,
    GLenum pname, const GLint *params)': names 'GLint', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexEnvfv(GLenum target,
    GLenum pname, const GLfloat *params)': names 'GLfloat', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glPolygonStipple(const
    GLubyte *mask)': names 'GLubyte', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glMaterialiv(GLenum face,
    GLenum pname, const GLint *params)': names 'GLint', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glMaterialfv(GLenum face,
    GLenum pname, const GLfloat *params)': names 'GLfloat', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glLightModeliv(GLenum
    pname, const GLint *params)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glLightModelfv(GLenum
    pname, const GLfloat *params)': names 'GLfloat', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glLightiv(GLenum light,
    GLenum pname, const GLint *params)': names 'GLint', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glLightfv(GLenum light,
    GLenum pname, const GLfloat *params)': names 'GLfloat', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glFogiv(GLenum pname,
    const GLint *params)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glFogfv(GLenum pname,
    const GLfloat *params)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glClipPlane(GLenum plane,
    const GLdouble *equation)': names 'GLdouble', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertex4sv(const GLshort
    *v)': names 'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertex4iv(const GLint
    *v)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertex4fv(const GLfloat
    *v)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertex4dv(const GLdouble
    *v)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertex3sv(const GLshort
    *v)': names 'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertex3iv(const GLint
    *v)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertex3fv(const GLfloat
    *v)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertex3dv(const GLdouble
    *v)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertex2sv(const GLshort
    *v)': names 'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertex2iv(const GLint
    *v)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertex2fv(const GLfloat
    *v)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertex2dv(const GLdouble
    *v)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexCoord4sv(const
    GLshort *v)': names 'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexCoord4iv(const GLint
    *v)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexCoord4fv(const
    GLfloat *v)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexCoord4dv(const
    GLdouble *v)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexCoord3sv(const
    GLshort *v)': names 'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexCoord3iv(const GLint
    *v)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexCoord3fv(const
    GLfloat *v)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexCoord3dv(const
    GLdouble *v)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexCoord2sv(const
    GLshort *v)': names 'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexCoord2iv(const GLint
    *v)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexCoord2fv(const
    GLfloat *v)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexCoord2dv(const
    GLdouble *v)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexCoord1sv(const
    GLshort *v)': names 'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexCoord1iv(const GLint
    *v)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexCoord1fv(const
    GLfloat *v)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexCoord1dv(const
    GLdouble *v)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glRectsv(const GLshort
    *v1, const GLshort *v2)': names 'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glRectiv(const GLint *v1,
    const GLint *v2)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glRectfv(const GLfloat
    *v1, const GLfloat *v2)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glRectdv(const GLdouble
    *v1, const GLdouble *v2)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glRasterPos4sv(const
    GLshort *v)': names 'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glRasterPos4iv(const GLint
    *v)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glRasterPos4fv(const
    GLfloat *v)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glRasterPos4dv(const
    GLdouble *v)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glRasterPos3sv(const
    GLshort *v)': names 'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glRasterPos3iv(const GLint
    *v)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glRasterPos3fv(const
    GLfloat *v)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glRasterPos3dv(const
    GLdouble *v)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glRasterPos2sv(const
    GLshort *v)': names 'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glRasterPos2iv(const GLint
    *v)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glRasterPos2fv(const
    GLfloat *v)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glRasterPos2dv(const
    GLdouble *v)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glNormal3sv(const GLshort
    *v)': names 'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glNormal3iv(const GLint
    *v)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glNormal3fv(const GLfloat
    *v)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glNormal3dv(const GLdouble
    *v)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glNormal3bv(const GLbyte
    *v)': names 'GLbyte', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glIndexsv(const GLshort
    *c)': names 'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glIndexiv(const GLint
    *c)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glIndexfv(const GLfloat
    *c)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glIndexdv(const GLdouble
    *c)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glEdgeFlagv(const
    GLboolean *flag)': names 'GLboolean', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glColor4usv(const GLushort
    *v)': names 'GLushort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glColor4uiv(const GLuint
    *v)': names 'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glColor4ubv(const GLubyte
    *v)': names 'GLubyte', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glColor4sv(const GLshort
    *v)': names 'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glColor4iv(const GLint
    *v)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glColor4fv(const GLfloat
    *v)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glColor4dv(const GLdouble
    *v)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glColor4bv(const GLbyte
    *v)': names 'GLbyte', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glColor3usv(const GLushort
    *v)': names 'GLushort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glColor3uiv(const GLuint
    *v)': names 'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glColor3ubv(const GLubyte
    *v)': names 'GLubyte', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glColor3sv(const GLshort
    *v)': names 'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glColor3iv(const GLint
    *v)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glColor3fv(const GLfloat
    *v)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glColor3dv(const GLdouble
    *v)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glColor3bv(const GLbyte
    *v)': names 'GLbyte', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glBitmap(GLsizei width,
    GLsizei height, GLfloat xorig, GLfloat yorig, GLfloat xmove, GLfloat
    ymove, const GLubyte *bitmap)': names 'GLubyte', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glCallLists(GLsizei n,
    GLenum type, const GLvoid *lists)': names 'GLvoid', which has no cute
    class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glPrioritizeTextures(GLsizei n, const
    GLuint *textures, const GLfloat *priorities)': names 'GLuint', which has
    no cute class yet.
  - Qt's 'GLboolean
    QOpenGLFunctions_4_3_Compatibility::glAreTexturesResident(GLsizei n,
    const GLuint *textures, GLboolean *residences)': names 'GLuint', which
    has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexPointer(GLint
    size, GLenum type, GLsizei stride, const GLvoid *pointer)': names
    'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexCoordPointer(GLint
    size, GLenum type, GLsizei stride, const GLvoid *pointer)': names
    'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glNormalPointer(GLenum
    type, GLsizei stride, const GLvoid *pointer)': names 'GLvoid', which has
    no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glInterleavedArrays(GLenum
    format, GLsizei stride, const GLvoid *pointer)': names 'GLvoid', which
    has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glIndexPointer(GLenum
    type, GLsizei stride, const GLvoid *pointer)': names 'GLvoid', which has
    no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glEdgeFlagPointer(GLsizei
    stride, const GLvoid *pointer)': names 'GLvoid', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glColorPointer(GLint size,
    GLenum type, GLsizei stride, const GLvoid *pointer)': names 'GLvoid',
    which has no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetMinmaxParameteriv(GLenum target,
    GLenum pname, GLint *params)': takes a number to change where it is.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetMinmaxParameterfv(GLenum target,
    GLenum pname, GLfloat *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetMinmax(GLenum target,
    GLboolean reset, GLenum format, GLenum type, GLvoid *values)': names
    'GLvoid', which has no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetHistogramParameteriv(GLenum
    target, GLenum pname, GLint *params)': takes a number to change where it
    is.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetHistogramParameterfv(GLenum
    target, GLenum pname, GLfloat *params)': takes a number to change where
    it is.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetHistogram(GLenum
    target, GLboolean reset, GLenum format, GLenum type, GLvoid *values)':
    names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glSeparableFilter2D(GLenum
    target, GLenum internalformat, GLsizei width, GLsizei height, GLenum
    format, GLenum type, const GLvoid *row, const GLvoid *column)': names
    'GLvoid', which has no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetSeparableFilter(GLenum target,
    GLenum format, GLenum type, GLvoid *row, GLvoid *column, GLvoid *span)':
    names 'GLvoid', which has no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetConvolutionParameteriv(GLenum
    target, GLenum pname, GLint *params)': takes a number to change where it
    is.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetConvolutionParameterfv(GLenum
    target, GLenum pname, GLfloat *params)': takes a number to change where
    it is.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetConvolutionFilter(GLenum target,
    GLenum format, GLenum type, GLvoid *image)': names 'GLvoid', which has no
    cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glConvolutionParameteriv(GLenum
    target, GLenum pname, const GLint *params)': names 'GLint', which has no
    cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glConvolutionParameterfv(GLenum
    target, GLenum pname, const GLfloat *params)': names 'GLfloat', which has
    no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glConvolutionFilter2D(GLenum target,
    GLenum internalformat, GLsizei width, GLsizei height, GLenum format,
    GLenum type, const GLvoid *image)': names 'GLvoid', which has no cute
    class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glConvolutionFilter1D(GLenum target,
    GLenum internalformat, GLsizei width, GLenum format, GLenum type, const
    GLvoid *image)': names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glColorSubTable(GLenum
    target, GLsizei start, GLsizei count, GLenum format, GLenum type, const
    GLvoid *data)': names 'GLvoid', which has no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetColorTableParameteriv(GLenum
    target, GLenum pname, GLint *params)': takes a number to change where it
    is.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetColorTableParameterfv(GLenum
    target, GLenum pname, GLfloat *params)': takes a number to change where
    it is.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetColorTable(GLenum
    target, GLenum format, GLenum type, GLvoid *table)': names 'GLvoid',
    which has no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glColorTableParameteriv(GLenum
    target, GLenum pname, const GLint *params)': names 'GLint', which has no
    cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glColorTableParameterfv(GLenum
    target, GLenum pname, const GLfloat *params)': names 'GLfloat', which has
    no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glColorTable(GLenum
    target, GLenum internalformat, GLsizei width, GLenum format, GLenum type,
    const GLvoid *table)': names 'GLvoid', which has no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glMultTransposeMatrixd(const GLdouble
    *m)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glMultTransposeMatrixf(const GLfloat
    *m)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glLoadTransposeMatrixd(const GLdouble
    *m)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glLoadTransposeMatrixf(const GLfloat
    *m)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord4sv(GLenum
    target, const GLshort *v)': names 'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord4iv(GLenum
    target, const GLint *v)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord4fv(GLenum
    target, const GLfloat *v)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord4dv(GLenum
    target, const GLdouble *v)': names 'GLdouble', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord3sv(GLenum
    target, const GLshort *v)': names 'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord3iv(GLenum
    target, const GLint *v)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord3fv(GLenum
    target, const GLfloat *v)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord3dv(GLenum
    target, const GLdouble *v)': names 'GLdouble', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord2sv(GLenum
    target, const GLshort *v)': names 'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord2iv(GLenum
    target, const GLint *v)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord2fv(GLenum
    target, const GLfloat *v)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord2dv(GLenum
    target, const GLdouble *v)': names 'GLdouble', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord1sv(GLenum
    target, const GLshort *v)': names 'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord1iv(GLenum
    target, const GLint *v)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord1fv(GLenum
    target, const GLfloat *v)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord1dv(GLenum
    target, const GLdouble *v)': names 'GLdouble', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glWindowPos3sv(const
    GLshort *v)': names 'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glWindowPos3iv(const GLint
    *v)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glWindowPos3fv(const
    GLfloat *v)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glWindowPos3dv(const
    GLdouble *v)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glWindowPos2sv(const
    GLshort *v)': names 'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glWindowPos2iv(const GLint
    *v)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glWindowPos2fv(const
    GLfloat *v)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glWindowPos2dv(const
    GLdouble *v)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glSecondaryColorPointer(GLint size,
    GLenum type, GLsizei stride, const GLvoid *pointer)': names 'GLvoid',
    which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glSecondaryColor3usv(const
    GLushort *v)': names 'GLushort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glSecondaryColor3uiv(const
    GLuint *v)': names 'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glSecondaryColor3ubv(const
    GLubyte *v)': names 'GLubyte', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glSecondaryColor3sv(const
    GLshort *v)': names 'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glSecondaryColor3iv(const
    GLint *v)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glSecondaryColor3fv(const
    GLfloat *v)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glSecondaryColor3dv(const
    GLdouble *v)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glSecondaryColor3bv(const
    GLbyte *v)': names 'GLbyte', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glFogCoordPointer(GLenum
    type, GLsizei stride, const GLvoid *pointer)': names 'GLvoid', which has
    no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glFogCoorddv(const
    GLdouble *coord)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glFogCoordfv(const GLfloat
    *coord)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttrib4usv(GLuint
    index, const GLushort *v)': names 'GLushort', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttrib4uiv(GLuint
    index, const GLuint *v)': names 'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttrib4ubv(GLuint
    index, const GLubyte *v)': names 'GLubyte', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttrib4sv(GLuint
    index, const GLshort *v)': names 'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttrib4iv(GLuint
    index, const GLint *v)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttrib4fv(GLuint
    index, const GLfloat *v)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttrib4dv(GLuint
    index, const GLdouble *v)': names 'GLdouble', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttrib4bv(GLuint
    index, const GLbyte *v)': names 'GLbyte', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttrib4Nusv(GLuint
    index, const GLushort *v)': names 'GLushort', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttrib4Nuiv(GLuint
    index, const GLuint *v)': names 'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttrib4Nubv(GLuint
    index, const GLubyte *v)': names 'GLubyte', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttrib4Nsv(GLuint
    index, const GLshort *v)': names 'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttrib4Niv(GLuint
    index, const GLint *v)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttrib4Nbv(GLuint
    index, const GLbyte *v)': names 'GLbyte', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttrib3sv(GLuint
    index, const GLshort *v)': names 'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttrib3fv(GLuint
    index, const GLfloat *v)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttrib3dv(GLuint
    index, const GLdouble *v)': names 'GLdouble', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttrib2sv(GLuint
    index, const GLshort *v)': names 'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttrib2fv(GLuint
    index, const GLfloat *v)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttrib2dv(GLuint
    index, const GLdouble *v)': names 'GLdouble', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttrib1sv(GLuint
    index, const GLshort *v)': names 'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttrib1fv(GLuint
    index, const GLfloat *v)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttrib1dv(GLuint
    index, const GLdouble *v)': names 'GLdouble', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttribI4usv(GLuint
    index, const GLushort *v)': names 'GLushort', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttribI4ubv(GLuint
    index, const GLubyte *v)': names 'GLubyte', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttribI4sv(GLuint
    index, const GLshort *v)': names 'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttribI4bv(GLuint
    index, const GLbyte *v)': names 'GLbyte', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttribI4uiv(GLuint
    index, const GLuint *v)': names 'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttribI3uiv(GLuint
    index, const GLuint *v)': names 'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttribI2uiv(GLuint
    index, const GLuint *v)': names 'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttribI1uiv(GLuint
    index, const GLuint *v)': names 'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttribI4iv(GLuint
    index, const GLint *v)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttribI3iv(GLuint
    index, const GLint *v)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttribI2iv(GLuint
    index, const GLint *v)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttribI1iv(GLuint
    index, const GLint *v)': names 'GLint', which has no cute class yet.

  What to expect
  --------------

  - The C++ QOpenGLFunctions_4_3_Compatibility is created at the first use,
    not by 'QOpenGLFunctions_4_3_Compatibility(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QOpenGLFunctions_4_3_Compatibility.
  - Each name of Qt's QOpenGLFunctions_4_3_Compatibility that has no cute
    function yet, 'glAreTexturesResident', 'glBindAttribLocation',
    'glBindFragDataLocation', 'glBindFragDataLocationIndexed', 'glBitmap',
    'glBufferData', 'glBufferSubData', 'glCallLists', 'glClearBufferData',
    'glClearBufferSubData', 'glClearBufferfv', 'glClearBufferiv',
    'glClearBufferuiv', 'glClientWaitSync', 'glClipPlane', 'glColor3bv',
    'glColor3dv', 'glColor3fv', 'glColor3iv', 'glColor3sv', 'glColor3ubv',
    'glColor3uiv', 'glColor3usv', 'glColor4bv', 'glColor4dv', 'glColor4fv',
    'glColor4iv', 'glColor4sv', 'glColor4ubv', 'glColor4uiv', 'glColor4usv',
    'glColorP3uiv', 'glColorP4uiv', 'glColorPointer', 'glColorSubTable',
    'glColorTable', 'glColorTableParameterfv', 'glColorTableParameteriv',
    'glCompressedTexImage1D', 'glCompressedTexImage2D',
    'glCompressedTexImage3D', 'glCompressedTexSubImage1D',
    'glCompressedTexSubImage2D', 'glCompressedTexSubImage3D',
    'glConvolutionFilter1D', 'glConvolutionFilter2D',
    'glConvolutionParameterfv', 'glConvolutionParameteriv',
    'glCreateShaderProgramv', 'glDeleteBuffers', 'glDeleteFramebuffers',
    'glDeleteProgramPipelines', 'glDeleteQueries', 'glDeleteRenderbuffers',
    'glDeleteSamplers', 'glDeleteSync', 'glDeleteTextures',
    'glDeleteTransformFeedbacks', 'glDeleteVertexArrays',
    'glDepthRangeArrayv', 'glDrawArraysIndirect', 'glDrawBuffers',
    'glDrawElements', 'glDrawElementsBaseVertex', 'glDrawElementsIndirect',
    'glDrawElementsInstanced', 'glDrawElementsInstancedBaseInstance',
    'glDrawElementsInstancedBaseVertex',
    'glDrawElementsInstancedBaseVertexBaseInstance', 'glDrawPixels',
    'glDrawRangeElements', 'glDrawRangeElementsBaseVertex',
    'glEdgeFlagPointer', 'glEdgeFlagv', 'glEvalCoord1dv', 'glEvalCoord1fv',
    'glEvalCoord2dv', 'glEvalCoord2fv', 'glFeedbackBuffer', 'glFenceSync',
    'glFogCoordPointer', 'glFogCoorddv', 'glFogCoordfv', 'glFogfv',
    'glFogiv', 'glGenBuffers', 'glGenFramebuffers', 'glGenProgramPipelines',
    'glGenQueries', 'glGenRenderbuffers', 'glGenSamplers', 'glGenTextures',
    'glGenTransformFeedbacks', 'glGenVertexArrays',
    'glGetActiveAtomicCounterBufferiv', 'glGetActiveAttrib',
    'glGetActiveSubroutineName', 'glGetActiveSubroutineUniformName',
    'glGetActiveSubroutineUniformiv', 'glGetActiveUniform',
    'glGetActiveUniformBlockName', 'glGetActiveUniformBlockiv',
    'glGetActiveUniformName', 'glGetActiveUniformsiv',
    'glGetAttachedShaders', 'glGetAttribLocation', 'glGetBooleani_v',
    'glGetBooleanv', 'glGetBufferParameteri64v', 'glGetBufferParameteriv',
    'glGetBufferPointerv', 'glGetBufferSubData', 'glGetClipPlane',
    'glGetColorTable', 'glGetColorTableParameterfv',
    'glGetColorTableParameteriv', 'glGetCompressedTexImage',
    'glGetConvolutionFilter', 'glGetConvolutionParameterfv',
    'glGetConvolutionParameteriv', 'glGetDoublei_v', 'glGetDoublev',
    'glGetFloati_v', 'glGetFloatv', 'glGetFragDataIndex',
    'glGetFragDataLocation', 'glGetFramebufferAttachmentParameteriv',
    'glGetFramebufferParameteriv', 'glGetHistogram',
    'glGetHistogramParameterfv', 'glGetHistogramParameteriv',
    'glGetInteger64i_v', 'glGetInteger64v', 'glGetIntegeri_v',
    'glGetIntegerv', 'glGetInternalformati64v', 'glGetInternalformativ',
    'glGetLightfv', 'glGetLightiv', 'glGetMapdv', 'glGetMapfv', 'glGetMapiv',
    'glGetMaterialfv', 'glGetMaterialiv', 'glGetMinmax',
    'glGetMinmaxParameterfv', 'glGetMinmaxParameteriv', 'glGetMultisamplefv',
    'glGetPixelMapfv', 'glGetPixelMapuiv', 'glGetPixelMapusv',
    'glGetPointerv', 'glGetPolygonStipple', 'glGetProgramBinary',
    'glGetProgramInfoLog', 'glGetProgramInterfaceiv',
    'glGetProgramPipelineInfoLog', 'glGetProgramPipelineiv',
    'glGetProgramResourceIndex', 'glGetProgramResourceLocation',
    'glGetProgramResourceLocationIndex', 'glGetProgramResourceName',
    'glGetProgramResourceiv', 'glGetProgramStageiv', 'glGetProgramiv',
    'glGetQueryIndexediv', 'glGetQueryObjecti64v', 'glGetQueryObjectiv',
    'glGetQueryObjectui64v', 'glGetQueryObjectuiv', 'glGetQueryiv',
    'glGetRenderbufferParameteriv', 'glGetSamplerParameterIiv',
    'glGetSamplerParameterIuiv', 'glGetSamplerParameterfv',
    'glGetSamplerParameteriv', 'glGetSeparableFilter', 'glGetShaderInfoLog',
    'glGetShaderPrecisionFormat', 'glGetShaderSource', 'glGetShaderiv',
    'glGetString', 'glGetStringi', 'glGetSubroutineIndex',
    'glGetSubroutineUniformLocation', 'glGetSynciv', 'glGetTexEnvfv',
    'glGetTexEnviv', 'glGetTexGendv', 'glGetTexGenfv', 'glGetTexGeniv',
    'glGetTexImage', 'glGetTexLevelParameterfv', 'glGetTexLevelParameteriv',
    'glGetTexParameterIiv', 'glGetTexParameterIuiv', 'glGetTexParameterfv',
    'glGetTexParameteriv', 'glGetTransformFeedbackVarying',
    'glGetUniformBlockIndex', 'glGetUniformIndices', 'glGetUniformLocation',
    'glGetUniformSubroutineuiv', 'glGetUniformdv', 'glGetUniformfv',
    'glGetUniformiv', 'glGetUniformuiv', 'glGetVertexAttribIiv',
    'glGetVertexAttribIuiv', 'glGetVertexAttribLdv',
    'glGetVertexAttribPointerv', 'glGetVertexAttribdv',
    'glGetVertexAttribfv', 'glGetVertexAttribiv', 'glIndexPointer',
    'glIndexdv', 'glIndexfv', 'glIndexiv', 'glIndexsv', 'glIndexubv',
    'glInterleavedArrays', 'glInvalidateFramebuffer',
    'glInvalidateSubFramebuffer', 'glIsSync', 'glLightModelfv',
    'glLightModeliv', 'glLightfv', 'glLightiv', 'glLoadMatrixd',
    'glLoadMatrixf', 'glLoadTransposeMatrixd', 'glLoadTransposeMatrixf',
    'glMap1d', 'glMap1f', 'glMap2d', 'glMap2f', 'glMapBuffer',
    'glMapBufferRange', 'glMaterialfv', 'glMaterialiv', 'glMultMatrixd',
    'glMultMatrixf', 'glMultTransposeMatrixd', 'glMultTransposeMatrixf',
    'glMultiDrawArrays', 'glMultiDrawArraysIndirect', 'glMultiDrawElements',
    'glMultiDrawElementsBaseVertex', 'glMultiDrawElementsIndirect',
    'glMultiTexCoord1dv', 'glMultiTexCoord1fv', 'glMultiTexCoord1iv',
    'glMultiTexCoord1sv', 'glMultiTexCoord2dv', 'glMultiTexCoord2fv',
    'glMultiTexCoord2iv', 'glMultiTexCoord2sv', 'glMultiTexCoord3dv',
    'glMultiTexCoord3fv', 'glMultiTexCoord3iv', 'glMultiTexCoord3sv',
    'glMultiTexCoord4dv', 'glMultiTexCoord4fv', 'glMultiTexCoord4iv',
    'glMultiTexCoord4sv', 'glMultiTexCoordP1uiv', 'glMultiTexCoordP2uiv',
    'glMultiTexCoordP3uiv', 'glMultiTexCoordP4uiv', 'glNormal3bv',
    'glNormal3dv', 'glNormal3fv', 'glNormal3iv', 'glNormal3sv',
    'glNormalP3uiv', 'glNormalPointer', 'glPatchParameterfv', 'glPixelMapfv',
    'glPixelMapuiv', 'glPixelMapusv', 'glPointParameterfv',
    'glPointParameteriv', 'glPolygonStipple', 'glPrioritizeTextures',
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
    'glRasterPos2dv', 'glRasterPos2fv', 'glRasterPos2iv', 'glRasterPos2sv',
    'glRasterPos3dv', 'glRasterPos3fv', 'glRasterPos3iv', 'glRasterPos3sv',
    'glRasterPos4dv', 'glRasterPos4fv', 'glRasterPos4iv', 'glRasterPos4sv',
    'glReadPixels', 'glRectdv', 'glRectfv', 'glRectiv', 'glRectsv',
    'glSamplerParameterIiv', 'glSamplerParameterIuiv',
    'glSamplerParameterfv', 'glSamplerParameteriv', 'glScissorArrayv',
    'glScissorIndexedv', 'glSecondaryColor3bv', 'glSecondaryColor3dv',
    'glSecondaryColor3fv', 'glSecondaryColor3iv', 'glSecondaryColor3sv',
    'glSecondaryColor3ubv', 'glSecondaryColor3uiv', 'glSecondaryColor3usv',
    'glSecondaryColorP3uiv', 'glSecondaryColorPointer', 'glSelectBuffer',
    'glSeparableFilter2D', 'glShaderBinary', 'glShaderSource',
    'glTexCoord1dv', 'glTexCoord1fv', 'glTexCoord1iv', 'glTexCoord1sv',
    'glTexCoord2dv', 'glTexCoord2fv', 'glTexCoord2iv', 'glTexCoord2sv',
    'glTexCoord3dv', 'glTexCoord3fv', 'glTexCoord3iv', 'glTexCoord3sv',
    'glTexCoord4dv', 'glTexCoord4fv', 'glTexCoord4iv', 'glTexCoord4sv',
    'glTexCoordP1uiv', 'glTexCoordP2uiv', 'glTexCoordP3uiv',
    'glTexCoordP4uiv', 'glTexCoordPointer', 'glTexEnvfv', 'glTexEnviv',
    'glTexGendv', 'glTexGenfv', 'glTexGeniv', 'glTexImage1D', 'glTexImage2D',
    'glTexImage3D', 'glTexParameterIiv', 'glTexParameterIuiv',
    'glTexParameterfv', 'glTexParameteriv', 'glTexSubImage1D',
    'glTexSubImage2D', 'glTexSubImage3D', 'glTransformFeedbackVaryings',
    'glUniform1dv', 'glUniform1fv', 'glUniform1iv', 'glUniform1uiv',
    'glUniform2dv', 'glUniform2fv', 'glUniform2iv', 'glUniform2uiv',
    'glUniform3dv', 'glUniform3fv', 'glUniform3iv', 'glUniform3uiv',
    'glUniform4dv', 'glUniform4fv', 'glUniform4iv', 'glUniform4uiv',
    'glUniformMatrix2dv', 'glUniformMatrix2fv', 'glUniformMatrix2x3dv',
    'glUniformMatrix2x3fv', 'glUniformMatrix2x4dv', 'glUniformMatrix2x4fv',
    'glUniformMatrix3dv', 'glUniformMatrix3fv', 'glUniformMatrix3x2dv',
    'glUniformMatrix3x2fv', 'glUniformMatrix3x4dv', 'glUniformMatrix3x4fv',
    'glUniformMatrix4dv', 'glUniformMatrix4fv', 'glUniformMatrix4x2dv',
    'glUniformMatrix4x2fv', 'glUniformMatrix4x3dv', 'glUniformMatrix4x3fv',
    'glUniformSubroutinesuiv', 'glVertex2dv', 'glVertex2fv', 'glVertex2iv',
    'glVertex2sv', 'glVertex3dv', 'glVertex3fv', 'glVertex3iv',
    'glVertex3sv', 'glVertex4dv', 'glVertex4fv', 'glVertex4iv',
    'glVertex4sv', 'glVertexAttrib1dv', 'glVertexAttrib1fv',
    'glVertexAttrib1sv', 'glVertexAttrib2dv', 'glVertexAttrib2fv',
    'glVertexAttrib2sv', 'glVertexAttrib3dv', 'glVertexAttrib3fv',
    'glVertexAttrib3sv', 'glVertexAttrib4Nbv', 'glVertexAttrib4Niv',
    'glVertexAttrib4Nsv', 'glVertexAttrib4Nubv', 'glVertexAttrib4Nuiv',
    'glVertexAttrib4Nusv', 'glVertexAttrib4bv', 'glVertexAttrib4dv',
    'glVertexAttrib4fv', 'glVertexAttrib4iv', 'glVertexAttrib4sv',
    'glVertexAttrib4ubv', 'glVertexAttrib4uiv', 'glVertexAttrib4usv',
    'glVertexAttribI1iv', 'glVertexAttribI1uiv', 'glVertexAttribI2iv',
    'glVertexAttribI2uiv', 'glVertexAttribI3iv', 'glVertexAttribI3uiv',
    'glVertexAttribI4bv', 'glVertexAttribI4iv', 'glVertexAttribI4sv',
    'glVertexAttribI4ubv', 'glVertexAttribI4uiv', 'glVertexAttribI4usv',
    'glVertexAttribIPointer', 'glVertexAttribL1dv', 'glVertexAttribL2dv',
    'glVertexAttribL3dv', 'glVertexAttribL4dv', 'glVertexAttribLPointer',
    'glVertexAttribP1uiv', 'glVertexAttribP2uiv', 'glVertexAttribP3uiv',
    'glVertexAttribP4uiv', 'glVertexAttribPointer', 'glVertexP2uiv',
    'glVertexP3uiv', 'glVertexP4uiv', 'glVertexPointer', 'glViewportArrayv',
    'glViewportIndexedfv', 'glWaitSync', 'glWindowPos2dv', 'glWindowPos2fv',
    'glWindowPos2iv', 'glWindowPos2sv', 'glWindowPos3dv', 'glWindowPos3fv',
    'glWindowPos3iv', 'glWindowPos3sv', holds a function that raises
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
    Calls Qt's 'bool
    QOpenGLFunctions_4_3_Compatibility::isContextCompatible(QOpenGLContext
    *context)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    context : Optional[QOpenGLContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QOpenGLFunctions_4_3_Compatibility::isContextCompatible(
    #      QOpenGLContext *context)
    return Rituals.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility19isContextCompatible'
        'EP14QOpenGLContext',
        CuteMixin._addressOf(context),
    )

  @staticmethod
  def versionProfile() -> QOpenGLVersionProfile:
    """
    Calls Qt's 'QOpenGLVersionProfile
    QOpenGLFunctions_4_3_Compatibility::versionProfile()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Returns
    -------

    QOpenGLVersionProfile
      A new cute QOpenGLVersionProfile around the copy Qt gave back. Python
      owns it.
    """
    #  QOpenGLVersionProfile
    #      QOpenGLFunctions_4_3_Compatibility::versionProfile()
    address = Rituals.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility14versionProfileEv',
    )
    from . import QOpenGLVersionProfile
    return QOpenGLVersionProfile._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpenGLFunctions_4_3_Compatibility'

  #  A C++ QOpenGLFunctions_4_3_Compatibility Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QOpenGLFunctions_4_3_Compatibility'

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
    'QOpenGLFunctions_4_3_Compatibility::QOpenGLFunctions_4_3_Compatibility(
    )', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html
    """
    #  QOpenGLFunctions_4_3_Compatibility::
    #      QOpenGLFunctions_4_3_Compatibility()
    self._noteCreation(
        QOpenGLFunctions_4_3_Compatibility, lambda: Rituals.call(
            'ritual_ZN34QOpenGLFunctions_4_3_CompatibilityC1Ev',
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
    Calls Qt's 'bool
    QOpenGLFunctions_4_3_Compatibility::initializeOpenGLFunctions()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html
    """
    #  bool QOpenGLFunctions_4_3_Compatibility::initializeOpenGLFunctions()
    ritual = (
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility25initializeOpenGLFun'
        'ctionsEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN34QOpenGLFunctions_4_3_Compatibility25initializeOpe'
          'nGLFunctionsEv')
    return self.uglySide.call(ritual)

  @overload(int, int, int, int)
  def glViewport(self, x: int, y: int, width: int, height: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glViewport(GLint x,
    GLint y, GLsizei width, GLsizei height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glViewport

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
    #  void QOpenGLFunctions_4_3_Compatibility::glViewport(GLint x, GLint y,
    #      GLsizei width, GLsizei height)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility10glViewportEiiii',
        x, y, width, height,
    )

  @overload(float, float)
  def glDepthRange(self, nearVal: float, farVal: float) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glDepthRange(GLdouble nearVal,
    GLdouble farVal)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    nearVal : float
      Passed on as it is.

    farVal : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glDepthRange(GLdouble
    #      nearVal, GLdouble farVal)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility12glDepthRangeEdd',
        nearVal, farVal,
    )

  @overload(int)
  def glIsEnabled(self, cap: int) -> int:
    """
    Calls Qt's 'GLboolean
    QOpenGLFunctions_4_3_Compatibility::glIsEnabled(GLenum cap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    cap : int
      Passed on as it is.
    """
    #  GLboolean QOpenGLFunctions_4_3_Compatibility::glIsEnabled(GLenum cap)
    return self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility11glIsEnabledEj', cap,
    )

  def glGetError(self) -> int:
    """
    Calls Qt's 'GLenum QOpenGLFunctions_4_3_Compatibility::glGetError()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glGetError
    """
    #  GLenum QOpenGLFunctions_4_3_Compatibility::glGetError()
    return self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility10glGetErrorEv',
    )

  @overload(int)
  def glReadBuffer(self, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glReadBuffer(GLenum
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glReadBuffer(GLenum mode)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility12glReadBufferEj',
        mode,
    )

  @overload(int, int)
  def glPixelStorei(self, pname: int, param: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glPixelStorei(GLenum
    pname, GLint param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    pname : int
      Passed on as it is.

    param : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glPixelStorei(GLenum pname,
    #      GLint param)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility13glPixelStoreiEji',
        pname, param,
    )

  @overload(int, float)
  def glPixelStoref(self, pname: int, param: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glPixelStoref(GLenum
    pname, GLfloat param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    pname : int
      Passed on as it is.

    param : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glPixelStoref(GLenum pname,
    #      GLfloat param)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility13glPixelStorefEjf',
        pname, param,
    )

  @overload(int)
  def glDepthFunc(self, func: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glDepthFunc(GLenum
    func)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    func : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glDepthFunc(GLenum func)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility11glDepthFuncEj', func,
    )

  @overload(int, int, int)
  def glStencilOp(self, fail: int, zfail: int, zpass: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glStencilOp(GLenum
    fail, GLenum zfail, GLenum zpass)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    fail : int
      Passed on as it is.

    zfail : int
      Passed on as it is.

    zpass : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glStencilOp(GLenum fail,
    #      GLenum zfail, GLenum zpass)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility11glStencilOpEjjj',
        fail, zfail, zpass,
    )

  @overload(int, int, int)
  def glStencilFunc(self, func: int, ref: int, mask: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glStencilFunc(GLenum
    func, GLint ref, GLuint mask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    func : int
      Passed on as it is.

    ref : int
      Passed on as it is.

    mask : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glStencilFunc(GLenum func,
    #      GLint ref, GLuint mask)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility13glStencilFuncEjij',
        func, ref, mask,
    )

  @overload(int)
  def glLogicOp(self, opcode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glLogicOp(GLenum
    opcode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glLogicOp

    Parameters
    ----------

    opcode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glLogicOp(GLenum opcode)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility9glLogicOpEj', opcode,
    )

  @overload(int, int)
  def glBlendFunc(self, sfactor: int, dfactor: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glBlendFunc(GLenum
    sfactor, GLenum dfactor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    sfactor : int
      Passed on as it is.

    dfactor : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glBlendFunc(GLenum sfactor,
    #      GLenum dfactor)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility11glBlendFuncEjj',
        sfactor, dfactor,
    )

  def glFlush(self) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glFlush()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glFlush
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glFlush()
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility7glFlushEv',
    )

  def glFinish(self) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glFinish()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glFinish
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glFinish()
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility8glFinishEv',
    )

  @overload(int)
  def glEnable(self, cap: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glEnable(GLenum
    cap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glEnable

    Parameters
    ----------

    cap : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glEnable(GLenum cap)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility8glEnableEj', cap,
    )

  @overload(int)
  def glDisable(self, cap: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glDisable(GLenum
    cap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glDisable

    Parameters
    ----------

    cap : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glDisable(GLenum cap)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility9glDisableEj', cap,
    )

  @overload(int)
  def glDepthMask(self, flag: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glDepthMask(GLboolean flag)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    flag : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glDepthMask(GLboolean flag)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility11glDepthMaskEh', flag,
    )

  @overload(int, int, int, int)
  def glColorMask(self, red: int, green: int, blue: int, alpha: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glColorMask(GLboolean red, GLboolean
    green, GLboolean blue, GLboolean alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glColorMask(GLboolean red,
    #      GLboolean green, GLboolean blue, GLboolean alpha)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility11glColorMaskEhhhh',
        red, green, blue, alpha,
    )

  @overload(int)
  def glStencilMask(self, mask: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glStencilMask(GLuint
    mask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    mask : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glStencilMask(GLuint mask)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility13glStencilMaskEj',
        mask,
    )

  @overload(float)
  def glClearDepth(self, depth: float) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glClearDepth(GLdouble depth)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    depth : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glClearDepth(GLdouble depth)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility12glClearDepthEd',
        depth,
    )

  @overload(int)
  def glClearStencil(self, s: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glClearStencil(GLint
    s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    s : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glClearStencil(GLint s)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility14glClearStencilEi', s,
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
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glClearColor(GLfloat
    red, GLfloat green, GLfloat blue, GLfloat alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glClearColor(GLfloat red,
    #      GLfloat green, GLfloat blue, GLfloat alpha)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility12glClearColorEffff',
        red, green, blue, alpha,
    )

  @overload(int)
  def glClear(self, mask: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glClear(GLbitfield
    mask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glClear

    Parameters
    ----------

    mask : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glClear(GLbitfield mask)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility7glClearEj', mask,
    )

  @overload(int)
  def glDrawBuffer(self, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glDrawBuffer(GLenum
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glDrawBuffer(GLenum mode)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility12glDrawBufferEj',
        mode,
    )

  @overload(int, int, int)
  def glTexParameteri(self, target: int, pname: int, param: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glTexParameteri(GLenum target, GLenum
    pname, GLint param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    target : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    param : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glTexParameteri(GLenum
    #      target, GLenum pname, GLint param)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility15glTexParameteriEjji',
        target, pname, param,
    )

  @overload(int, int, float)
  def glTexParameterf(self, target: int, pname: int, param: float) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glTexParameterf(GLenum target, GLenum
    pname, GLfloat param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    target : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    param : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glTexParameterf(GLenum
    #      target, GLenum pname, GLfloat param)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility15glTexParameterfEjjf',
        target, pname, param,
    )

  @overload(int, int, int, int)
  def glScissor(self, x: int, y: int, width: int, height: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glScissor(GLint x,
    GLint y, GLsizei width, GLsizei height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glScissor

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
    #  void QOpenGLFunctions_4_3_Compatibility::glScissor(GLint x, GLint y,
    #      GLsizei width, GLsizei height)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility9glScissorEiiii',
        x, y, width, height,
    )

  @overload(int, int)
  def glPolygonMode(self, face: int, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glPolygonMode(GLenum
    face, GLenum mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    face : int
      Passed on as it is.

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glPolygonMode(GLenum face,
    #      GLenum mode)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility13glPolygonModeEjj',
        face, mode,
    )

  @overload(float)
  def glPointSize(self, size: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glPointSize(GLfloat
    size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    size : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glPointSize(GLfloat size)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility11glPointSizeEf', size,
    )

  @overload(float)
  def glLineWidth(self, width: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glLineWidth(GLfloat
    width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glLineWidth(GLfloat width)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility11glLineWidthEf',
        width,
    )

  @overload(int, int)
  def glHint(self, target: int, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glHint(GLenum
    target, GLenum mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glHint

    Parameters
    ----------

    target : int
      Passed on as it is.

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glHint(GLenum target, GLenum
    #      mode)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility6glHintEjj',
        target, mode,
    )

  @overload(int)
  def glFrontFace(self, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glFrontFace(GLenum
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glFrontFace(GLenum mode)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility11glFrontFaceEj', mode,
    )

  @overload(int)
  def glCullFace(self, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glCullFace(GLenum
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glCullFace

    Parameters
    ----------

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glCullFace(GLenum mode)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility10glCullFaceEj', mode,
    )

  @overload(int)
  def glIndexub(self, c: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glIndexub(GLubyte
    c)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glIndexub

    Parameters
    ----------

    c : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glIndexub(GLubyte c)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility9glIndexubEh', c,
    )

  @overload(int)
  def glIsTexture(self, texture: int) -> int:
    """
    Calls Qt's 'GLboolean
    QOpenGLFunctions_4_3_Compatibility::glIsTexture(GLuint texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    texture : int
      Passed on as it is.
    """
    #  GLboolean QOpenGLFunctions_4_3_Compatibility::glIsTexture(GLuint
    #      texture)
    return self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility11glIsTextureEj',
        texture,
    )

  @overload(int, int)
  def glBindTexture(self, target: int, texture: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glBindTexture(GLenum
    target, GLuint texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    target : int
      Passed on as it is.

    texture : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glBindTexture(GLenum target,
    #      GLuint texture)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility13glBindTextureEjj',
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
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glCopyTexSubImage2D(GLenum target,
    GLint level, GLint xoffset, GLint yoffset, GLint x, GLint y, GLsizei
    width, GLsizei height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glCopyTexSubImage2D(GLenum
    #      target, GLint level, GLint xoffset, GLint yoffset, GLint x, GLint
    #      y, GLsizei width, GLsizei height)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility19glCopyTexSubImage2D'
        'Ejiiiiiii',
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
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glCopyTexSubImage1D(GLenum target,
    GLint level, GLint xoffset, GLint x, GLint y, GLsizei width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glCopyTexSubImage1D(GLenum
    #      target, GLint level, GLint xoffset, GLint x, GLint y, GLsizei
    #      width)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility19glCopyTexSubImage1D'
        'Ejiiiii',
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
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glCopyTexImage2D(GLenum target, GLint
    level, GLenum internalformat, GLint x, GLint y, GLsizei width, GLsizei
    height, GLint border)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glCopyTexImage2D(GLenum
    #      target, GLint level, GLenum internalformat, GLint x, GLint y,
    #      GLsizei width, GLsizei height, GLint border)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility16glCopyTexImage2DEji'
        'jiiiii',
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
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glCopyTexImage1D(GLenum target, GLint
    level, GLenum internalformat, GLint x, GLint y, GLsizei width, GLint
    border)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glCopyTexImage1D(GLenum
    #      target, GLint level, GLenum internalformat, GLint x, GLint y,
    #      GLsizei width, GLint border)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility16glCopyTexImage1DEji'
        'jiiii',
        target, level, internalformat, x, y, width, border,
    )

  @overload(float, float)
  def glPolygonOffset(self, factor: float, units: float) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glPolygonOffset(GLfloat factor,
    GLfloat units)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    factor : float
      Passed on as it is.

    units : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glPolygonOffset(GLfloat
    #      factor, GLfloat units)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility15glPolygonOffsetEff',
        factor, units,
    )

  @overload(int, int, int)
  def glDrawArrays(self, mode: int, first: int, count: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glDrawArrays(GLenum
    mode, GLint first, GLsizei count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    mode : int
      Passed on as it is.

    first : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glDrawArrays(GLenum mode,
    #      GLint first, GLsizei count)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility12glDrawArraysEjii',
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
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glCopyTexSubImage3D(GLenum target,
    GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLint x, GLint
    y, GLsizei width, GLsizei height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glCopyTexSubImage3D(GLenum
    #      target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset,
    #      GLint x, GLint y, GLsizei width, GLsizei height)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility19glCopyTexSubImage3D'
        'Ejiiiiiiii',
        target, level, xoffset, yoffset, zoffset, x, y, width, height,
    )

  @overload(int)
  def glBlendEquation(self, mode: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glBlendEquation(GLenum mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glBlendEquation(GLenum mode)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility15glBlendEquationEj',
        mode,
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
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glBlendColor(GLfloat
    red, GLfloat green, GLfloat blue, GLfloat alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glBlendColor(GLfloat red,
    #      GLfloat green, GLfloat blue, GLfloat alpha)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility12glBlendColorEffff',
        red, green, blue, alpha,
    )

  @overload(float, int)
  def glSampleCoverage(self, value: float, invert: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glSampleCoverage(GLfloat value,
    GLboolean invert)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    value : float
      Passed on as it is.

    invert : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glSampleCoverage(GLfloat
    #      value, GLboolean invert)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility16glSampleCoverageEfh',
        value, invert,
    )

  @overload(int)
  def glActiveTexture(self, texture: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glActiveTexture(GLenum texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    texture : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glActiveTexture(GLenum
    #      texture)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility15glActiveTextureEj',
        texture,
    )

  @overload(int, int)
  def glPointParameteri(self, pname: int, param: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glPointParameteri(GLenum pname, GLint
    param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    pname : int
      Passed on as it is.

    param : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glPointParameteri(GLenum
    #      pname, GLint param)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility17glPointParameteriEj'
        'i',
        pname, param,
    )

  @overload(int, float)
  def glPointParameterf(self, pname: int, param: float) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glPointParameterf(GLenum pname,
    GLfloat param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    pname : int
      Passed on as it is.

    param : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glPointParameterf(GLenum
    #      pname, GLfloat param)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility17glPointParameterfEj'
        'f',
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
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glBlendFuncSeparate(GLenum
    sfactorRGB, GLenum dfactorRGB, GLenum sfactorAlpha, GLenum
    dfactorAlpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glBlendFuncSeparate(GLenum
    #      sfactorRGB, GLenum dfactorRGB, GLenum sfactorAlpha, GLenum
    #      dfactorAlpha)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility19glBlendFuncSeparate'
        'Ejjjj',
        sfactorRGB, dfactorRGB, sfactorAlpha, dfactorAlpha,
    )

  @overload(int)
  def glUnmapBuffer(self, target: int) -> int:
    """
    Calls Qt's 'GLboolean
    QOpenGLFunctions_4_3_Compatibility::glUnmapBuffer(GLenum target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    target : int
      Passed on as it is.
    """
    #  GLboolean QOpenGLFunctions_4_3_Compatibility::glUnmapBuffer(GLenum
    #      target)
    return self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility13glUnmapBufferEj',
        target,
    )

  @overload(int)
  def glIsBuffer(self, buffer: int) -> int:
    """
    Calls Qt's 'GLboolean
    QOpenGLFunctions_4_3_Compatibility::glIsBuffer(GLuint buffer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glIsBuffer

    Parameters
    ----------

    buffer : int
      Passed on as it is.
    """
    #  GLboolean QOpenGLFunctions_4_3_Compatibility::glIsBuffer(GLuint
    #      buffer)
    return self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility10glIsBufferEj',
        buffer,
    )

  @overload(int, int)
  def glBindBuffer(self, target: int, buffer: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glBindBuffer(GLenum
    target, GLuint buffer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    target : int
      Passed on as it is.

    buffer : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glBindBuffer(GLenum target,
    #      GLuint buffer)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility12glBindBufferEjj',
        target, buffer,
    )

  @overload(int)
  def glEndQuery(self, target: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glEndQuery(GLenum
    target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glEndQuery

    Parameters
    ----------

    target : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glEndQuery(GLenum target)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility10glEndQueryEj',
        target,
    )

  @overload(int, int)
  def glBeginQuery(self, target: int, id: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glBeginQuery(GLenum
    target, GLuint id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    target : int
      Passed on as it is.

    id : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glBeginQuery(GLenum target,
    #      GLuint id)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility12glBeginQueryEjj',
        target, id,
    )

  @overload(int)
  def glIsQuery(self, id: int) -> int:
    """
    Calls Qt's 'GLboolean
    QOpenGLFunctions_4_3_Compatibility::glIsQuery(GLuint id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glIsQuery

    Parameters
    ----------

    id : int
      Passed on as it is.
    """
    #  GLboolean QOpenGLFunctions_4_3_Compatibility::glIsQuery(GLuint id)
    return self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility9glIsQueryEj', id,
    )

  @overload(int)
  def glValidateProgram(self, program: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glValidateProgram(GLuint program)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    program : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glValidateProgram(GLuint
    #      program)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility17glValidateProgramEj',
        program,
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
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniform4i(GLint
    location, GLint v0, GLint v1, GLint v2, GLint v3)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glUniform4i(GLint location,
    #      GLint v0, GLint v1, GLint v2, GLint v3)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility11glUniform4iEiiiii',
        location, v0, v1, v2, v3,
    )

  @overload(int, int, int, int)
  def glUniform3i(self, location: int, v0: int, v1: int, v2: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniform3i(GLint
    location, GLint v0, GLint v1, GLint v2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glUniform3i(GLint location,
    #      GLint v0, GLint v1, GLint v2)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility11glUniform3iEiiii',
        location, v0, v1, v2,
    )

  @overload(int, int, int)
  def glUniform2i(self, location: int, v0: int, v1: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniform2i(GLint
    location, GLint v0, GLint v1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    location : int
      Passed on as it is.

    v0 : int
      Passed on as it is.

    v1 : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glUniform2i(GLint location,
    #      GLint v0, GLint v1)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility11glUniform2iEiii',
        location, v0, v1,
    )

  @overload(int, int)
  def glUniform1i(self, location: int, v0: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniform1i(GLint
    location, GLint v0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    location : int
      Passed on as it is.

    v0 : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glUniform1i(GLint location,
    #      GLint v0)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility11glUniform1iEii',
        location, v0,
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
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniform4f(GLint
    location, GLfloat v0, GLfloat v1, GLfloat v2, GLfloat v3)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glUniform4f(GLint location,
    #      GLfloat v0, GLfloat v1, GLfloat v2, GLfloat v3)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility11glUniform4fEiffff',
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
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniform3f(GLint
    location, GLfloat v0, GLfloat v1, GLfloat v2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glUniform3f(GLint location,
    #      GLfloat v0, GLfloat v1, GLfloat v2)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility11glUniform3fEifff',
        location, v0, v1, v2,
    )

  @overload(int, float, float)
  def glUniform2f(self, location: int, v0: float, v1: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniform2f(GLint
    location, GLfloat v0, GLfloat v1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    location : int
      Passed on as it is.

    v0 : float
      Passed on as it is.

    v1 : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glUniform2f(GLint location,
    #      GLfloat v0, GLfloat v1)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility11glUniform2fEiff',
        location, v0, v1,
    )

  @overload(int, float)
  def glUniform1f(self, location: int, v0: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniform1f(GLint
    location, GLfloat v0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    location : int
      Passed on as it is.

    v0 : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glUniform1f(GLint location,
    #      GLfloat v0)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility11glUniform1fEif',
        location, v0,
    )

  @overload(int)
  def glUseProgram(self, program: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUseProgram(GLuint
    program)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    program : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glUseProgram(GLuint program)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility12glUseProgramEj',
        program,
    )

  @overload(int)
  def glLinkProgram(self, program: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glLinkProgram(GLuint
    program)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    program : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glLinkProgram(GLuint program)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility13glLinkProgramEj',
        program,
    )

  @overload(int)
  def glIsShader(self, shader: int) -> int:
    """
    Calls Qt's 'GLboolean
    QOpenGLFunctions_4_3_Compatibility::glIsShader(GLuint shader)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glIsShader

    Parameters
    ----------

    shader : int
      Passed on as it is.
    """
    #  GLboolean QOpenGLFunctions_4_3_Compatibility::glIsShader(GLuint
    #      shader)
    return self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility10glIsShaderEj',
        shader,
    )

  @overload(int)
  def glIsProgram(self, program: int) -> int:
    """
    Calls Qt's 'GLboolean
    QOpenGLFunctions_4_3_Compatibility::glIsProgram(GLuint program)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    program : int
      Passed on as it is.
    """
    #  GLboolean QOpenGLFunctions_4_3_Compatibility::glIsProgram(GLuint
    #      program)
    return self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility11glIsProgramEj',
        program,
    )

  @overload(int)
  def glEnableVertexAttribArray(self, index: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glEnableVertexAttribArray(GLuint
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glEnableVertexAttribArray(
    #      GLuint index)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility25glEnableVertexAttri'
        'bArrayEj',
        index,
    )

  @overload(int)
  def glDisableVertexAttribArray(self, index: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glDisableVertexAttribArray(GLuint
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glDisableVertexAttribArray(
    #      GLuint index)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility26glDisableVertexAttr'
        'ibArrayEj',
        index,
    )

  @overload(int, int)
  def glDetachShader(self, program: int, shader: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glDetachShader(GLuint program, GLuint
    shader)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    program : int
      Passed on as it is.

    shader : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glDetachShader(GLuint
    #      program, GLuint shader)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility14glDetachShaderEjj',
        program, shader,
    )

  @overload(int)
  def glDeleteShader(self, shader: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glDeleteShader(GLuint shader)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    shader : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glDeleteShader(GLuint shader)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility14glDeleteShaderEj',
        shader,
    )

  @overload(int)
  def glDeleteProgram(self, program: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glDeleteProgram(GLuint program)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    program : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glDeleteProgram(GLuint
    #      program)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility15glDeleteProgramEj',
        program,
    )

  @overload(int)
  def glCreateShader(self, type: int) -> int:
    """
    Calls Qt's 'GLuint
    QOpenGLFunctions_4_3_Compatibility::glCreateShader(GLenum type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    type : int
      Passed on as it is.
    """
    #  GLuint QOpenGLFunctions_4_3_Compatibility::glCreateShader(GLenum type)
    return self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility14glCreateShaderEj',
        type,
    )

  def glCreateProgram(self) -> int:
    """
    Calls Qt's 'GLuint
    QOpenGLFunctions_4_3_Compatibility::glCreateProgram()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html
    """
    #  GLuint QOpenGLFunctions_4_3_Compatibility::glCreateProgram()
    return self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility15glCreateProgramEv',
    )

  @overload(int)
  def glCompileShader(self, shader: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glCompileShader(GLuint shader)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    shader : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glCompileShader(GLuint
    #      shader)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility15glCompileShaderEj',
        shader,
    )

  @overload(int, int)
  def glAttachShader(self, program: int, shader: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glAttachShader(GLuint program, GLuint
    shader)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    program : int
      Passed on as it is.

    shader : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glAttachShader(GLuint
    #      program, GLuint shader)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility14glAttachShaderEjj',
        program, shader,
    )

  @overload(int, int)
  def glStencilMaskSeparate(self, face: int, mask: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glStencilMaskSeparate(GLenum face,
    GLuint mask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    face : int
      Passed on as it is.

    mask : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glStencilMaskSeparate(GLenum
    #      face, GLuint mask)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility21glStencilMaskSepara'
        'teEjj',
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
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glStencilFuncSeparate(GLenum face,
    GLenum func, GLint ref, GLuint mask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glStencilFuncSeparate(GLenum
    #      face, GLenum func, GLint ref, GLuint mask)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility21glStencilFuncSepara'
        'teEjjij',
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
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glStencilOpSeparate(GLenum face,
    GLenum sfail, GLenum dpfail, GLenum dppass)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glStencilOpSeparate(GLenum
    #      face, GLenum sfail, GLenum dpfail, GLenum dppass)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility19glStencilOpSeparate'
        'Ejjjj',
        face, sfail, dpfail, dppass,
    )

  @overload(int, int)
  def glBlendEquationSeparate(self, modeRGB: int, modeAlpha: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glBlendEquationSeparate(GLenum
    modeRGB, GLenum modeAlpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    modeRGB : int
      Passed on as it is.

    modeAlpha : int
      Passed on as it is.
    """
    #  void
    #      QOpenGLFunctions_4_3_Compatibility::glBlendEquationSeparate(GLenum
    #      modeRGB, GLenum modeAlpha)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility23glBlendEquationSepa'
        'rateEjj',
        modeRGB, modeAlpha,
    )

  @overload(int)
  def glIsVertexArray(self, array: int) -> int:
    """
    Calls Qt's 'GLboolean
    QOpenGLFunctions_4_3_Compatibility::glIsVertexArray(GLuint array)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    array : int
      Passed on as it is.
    """
    #  GLboolean QOpenGLFunctions_4_3_Compatibility::glIsVertexArray(GLuint
    #      array)
    return self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility15glIsVertexArrayEj',
        array,
    )

  @overload(int)
  def glBindVertexArray(self, array: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glBindVertexArray(GLuint array)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    array : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glBindVertexArray(GLuint
    #      array)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility17glBindVertexArrayEj',
        array,
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
    QOpenGLFunctions_4_3_Compatibility::glFlushMappedBufferRange(GLenum
    target, GLintptr offset, GLsizeiptr length)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    target : int
      Passed on as it is.

    offset : int
      Passed on as it is.

    length : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glFlushMappedBufferRange(
    #      GLenum target, GLintptr offset, GLsizeiptr length)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility24glFlushMappedBuffer'
        'RangeEjll',
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
    QOpenGLFunctions_4_3_Compatibility::glFramebufferTextureLayer(GLenum
    target, GLenum attachment, GLuint texture, GLint level, GLint layer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glFramebufferTextureLayer(
    #      GLenum target, GLenum attachment, GLuint texture, GLint level,
    #      GLint layer)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility25glFramebufferTextur'
        'eLayerEjjjii',
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
    QOpenGLFunctions_4_3_Compatibility::glRenderbufferStorageMultisample(
    GLenum target, GLsizei samples, GLenum internalformat, GLsizei width,
    GLsizei height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::
    #      glRenderbufferStorageMultisample(GLenum target, GLsizei samples,
    #      GLenum internalformat, GLsizei width, GLsizei height)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility32glRenderbufferStora'
        'geMultisampleEjijii',
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
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glBlitFramebuffer(GLint srcX0, GLint
    srcY0, GLint srcX1, GLint srcY1, GLint dstX0, GLint dstY0, GLint dstX1,
    GLint dstY1, GLbitfield mask, GLenum filter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glBlitFramebuffer(GLint
    #      srcX0, GLint srcY0, GLint srcX1, GLint srcY1, GLint dstX0, GLint
    #      dstY0, GLint dstX1, GLint dstY1, GLbitfield mask, GLenum filter)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility17glBlitFramebufferEi'
        'iiiiiiijj',
        srcX0, srcY0, srcX1, srcY1, dstX0, dstY0, dstX1, dstY1, mask, filter,
    )

  @overload(int)
  def glGenerateMipmap(self, target: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGenerateMipmap(GLenum target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    target : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glGenerateMipmap(GLenum
    #      target)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility16glGenerateMipmapEj',
        target,
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
    QOpenGLFunctions_4_3_Compatibility::glFramebufferRenderbuffer(GLenum
    target, GLenum attachment, GLenum renderbuffertarget, GLuint
    renderbuffer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glFramebufferRenderbuffer(
    #      GLenum target, GLenum attachment, GLenum renderbuffertarget,
    #      GLuint renderbuffer)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility25glFramebufferRender'
        'bufferEjjjj',
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
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glFramebufferTexture3D(GLenum target,
    GLenum attachment, GLenum textarget, GLuint texture, GLint level, GLint
    zoffset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glFramebufferTexture3D(GLenum
    #      target, GLenum attachment, GLenum textarget, GLuint texture, GLint
    #      level, GLint zoffset)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility22glFramebufferTextur'
        'e3DEjjjjii',
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
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glFramebufferTexture2D(GLenum target,
    GLenum attachment, GLenum textarget, GLuint texture, GLint level)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glFramebufferTexture2D(GLenum
    #      target, GLenum attachment, GLenum textarget, GLuint texture, GLint
    #      level)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility22glFramebufferTextur'
        'e2DEjjjji',
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
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glFramebufferTexture1D(GLenum target,
    GLenum attachment, GLenum textarget, GLuint texture, GLint level)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glFramebufferTexture1D(GLenum
    #      target, GLenum attachment, GLenum textarget, GLuint texture, GLint
    #      level)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility22glFramebufferTextur'
        'e1DEjjjji',
        target, attachment, textarget, texture, level,
    )

  @overload(int)
  def glCheckFramebufferStatus(self, target: int) -> int:
    """
    Calls Qt's 'GLenum
    QOpenGLFunctions_4_3_Compatibility::glCheckFramebufferStatus(GLenum
    target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    target : int
      Passed on as it is.
    """
    #  GLenum QOpenGLFunctions_4_3_Compatibility::glCheckFramebufferStatus(
    #      GLenum target)
    return self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility24glCheckFramebufferS'
        'tatusEj',
        target,
    )

  @overload(int, int)
  def glBindFramebuffer(self, target: int, framebuffer: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glBindFramebuffer(GLenum target,
    GLuint framebuffer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    target : int
      Passed on as it is.

    framebuffer : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glBindFramebuffer(GLenum
    #      target, GLuint framebuffer)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility17glBindFramebufferEj'
        'j',
        target, framebuffer,
    )

  @overload(int)
  def glIsFramebuffer(self, framebuffer: int) -> int:
    """
    Calls Qt's 'GLboolean
    QOpenGLFunctions_4_3_Compatibility::glIsFramebuffer(GLuint framebuffer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    framebuffer : int
      Passed on as it is.
    """
    #  GLboolean QOpenGLFunctions_4_3_Compatibility::glIsFramebuffer(GLuint
    #      framebuffer)
    return self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility15glIsFramebufferEj',
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
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glRenderbufferStorage(GLenum target,
    GLenum internalformat, GLsizei width, GLsizei height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glRenderbufferStorage(GLenum
    #      target, GLenum internalformat, GLsizei width, GLsizei height)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility21glRenderbufferStora'
        'geEjjii',
        target, internalformat, width, height,
    )

  @overload(int, int)
  def glBindRenderbuffer(self, target: int, renderbuffer: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glBindRenderbuffer(GLenum target,
    GLuint renderbuffer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    target : int
      Passed on as it is.

    renderbuffer : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glBindRenderbuffer(GLenum
    #      target, GLuint renderbuffer)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility18glBindRenderbufferE'
        'jj',
        target, renderbuffer,
    )

  @overload(int)
  def glIsRenderbuffer(self, renderbuffer: int) -> int:
    """
    Calls Qt's 'GLboolean
    QOpenGLFunctions_4_3_Compatibility::glIsRenderbuffer(GLuint
    renderbuffer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    renderbuffer : int
      Passed on as it is.
    """
    #  GLboolean QOpenGLFunctions_4_3_Compatibility::glIsRenderbuffer(GLuint
    #      renderbuffer)
    return self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility16glIsRenderbufferEj',
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
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glClearBufferfi(GLenum buffer, GLint
    drawbuffer, GLfloat depth, GLint stencil)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glClearBufferfi(GLenum
    #      buffer, GLint drawbuffer, GLfloat depth, GLint stencil)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility15glClearBufferfiEjif'
        'i',
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
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniform4ui(GLint
    location, GLuint v0, GLuint v1, GLuint v2, GLuint v3)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glUniform4ui(GLint location,
    #      GLuint v0, GLuint v1, GLuint v2, GLuint v3)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility12glUniform4uiEijjjj',
        location, v0, v1, v2, v3,
    )

  @overload(int, int, int, int)
  def glUniform3ui(self, location: int, v0: int, v1: int, v2: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniform3ui(GLint
    location, GLuint v0, GLuint v1, GLuint v2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glUniform3ui(GLint location,
    #      GLuint v0, GLuint v1, GLuint v2)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility12glUniform3uiEijjj',
        location, v0, v1, v2,
    )

  @overload(int, int, int)
  def glUniform2ui(self, location: int, v0: int, v1: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniform2ui(GLint
    location, GLuint v0, GLuint v1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    location : int
      Passed on as it is.

    v0 : int
      Passed on as it is.

    v1 : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glUniform2ui(GLint location,
    #      GLuint v0, GLuint v1)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility12glUniform2uiEijj',
        location, v0, v1,
    )

  @overload(int, int)
  def glUniform1ui(self, location: int, v0: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniform1ui(GLint
    location, GLuint v0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    location : int
      Passed on as it is.

    v0 : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glUniform1ui(GLint location,
    #      GLuint v0)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility12glUniform1uiEij',
        location, v0,
    )

  def glEndConditionalRender(self) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glEndConditionalRender()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glEndConditionalRender()
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility22glEndConditionalRen'
        'derEv',
    )

  @overload(int, int)
  def glBeginConditionalRender(self, id: int, mode: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glBeginConditionalRender(GLuint id,
    GLenum mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    id : int
      Passed on as it is.

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glBeginConditionalRender(
    #      GLuint id, GLenum mode)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility24glBeginConditionalR'
        'enderEjj',
        id, mode,
    )

  @overload(int, int)
  def glClampColor(self, target: int, clamp: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glClampColor(GLenum
    target, GLenum clamp)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    target : int
      Passed on as it is.

    clamp : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glClampColor(GLenum target,
    #      GLenum clamp)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility12glClampColorEjj',
        target, clamp,
    )

  @overload(int, int, int)
  def glBindBufferBase(self, target: int, index: int, buffer: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glBindBufferBase(GLenum target,
    GLuint index, GLuint buffer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    target : int
      Passed on as it is.

    index : int
      Passed on as it is.

    buffer : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glBindBufferBase(GLenum
    #      target, GLuint index, GLuint buffer)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility16glBindBufferBaseEjj'
        'j',
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
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glBindBufferRange(GLenum target,
    GLuint index, GLuint buffer, GLintptr offset, GLsizeiptr size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glBindBufferRange(GLenum
    #      target, GLuint index, GLuint buffer, GLintptr offset, GLsizeiptr
    #      size)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility17glBindBufferRangeEj'
        'jjll',
        target, index, buffer, offset, size,
    )

  def glEndTransformFeedback(self) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glEndTransformFeedback()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glEndTransformFeedback()
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility22glEndTransformFeedb'
        'ackEv',
    )

  @overload(int)
  def glBeginTransformFeedback(self, primitiveMode: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glBeginTransformFeedback(GLenum
    primitiveMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    primitiveMode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glBeginTransformFeedback(
    #      GLenum primitiveMode)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility24glBeginTransformFee'
        'dbackEj',
        primitiveMode,
    )

  @overload(int, int)
  def glIsEnabledi(self, target: int, index: int) -> int:
    """
    Calls Qt's 'GLboolean
    QOpenGLFunctions_4_3_Compatibility::glIsEnabledi(GLenum target, GLuint
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    target : int
      Passed on as it is.

    index : int
      Passed on as it is.
    """
    #  GLboolean QOpenGLFunctions_4_3_Compatibility::glIsEnabledi(GLenum
    #      target, GLuint index)
    return self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility12glIsEnablediEjj',
        target, index,
    )

  @overload(int, int)
  def glDisablei(self, target: int, index: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glDisablei(GLenum
    target, GLuint index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glDisablei

    Parameters
    ----------

    target : int
      Passed on as it is.

    index : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glDisablei(GLenum target,
    #      GLuint index)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility10glDisableiEjj',
        target, index,
    )

  @overload(int, int)
  def glEnablei(self, target: int, index: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glEnablei(GLenum
    target, GLuint index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glEnablei

    Parameters
    ----------

    target : int
      Passed on as it is.

    index : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glEnablei(GLenum target,
    #      GLuint index)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility9glEnableiEjj',
        target, index,
    )

  @overload(int, int, int, int, int)
  def glColorMaski(self, index: int, r: int, g: int, b: int, a: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glColorMaski(GLuint
    index, GLboolean r, GLboolean g, GLboolean b, GLboolean a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glColorMaski(GLuint index,
    #      GLboolean r, GLboolean g, GLboolean b, GLboolean a)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility12glColorMaskiEjhhhh',
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
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glCopyBufferSubData(GLenum
    readTarget, GLenum writeTarget, GLintptr readOffset, GLintptr
    writeOffset, GLsizeiptr size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glCopyBufferSubData(GLenum
    #      readTarget, GLenum writeTarget, GLintptr readOffset, GLintptr
    #      writeOffset, GLsizeiptr size)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility19glCopyBufferSubData'
        'Ejjlll',
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
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glUniformBlockBinding(GLuint program,
    GLuint uniformBlockIndex, GLuint uniformBlockBinding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    program : int
      Passed on as it is.

    uniformBlockIndex : int
      Passed on as it is.

    uniformBlockBinding : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glUniformBlockBinding(GLuint
    #      program, GLuint uniformBlockIndex, GLuint uniformBlockBinding)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility21glUniformBlockBindi'
        'ngEjjj',
        program, uniformBlockIndex, uniformBlockBinding,
    )

  @overload(int)
  def glPrimitiveRestartIndex(self, index: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glPrimitiveRestartIndex(GLuint
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void
    #      QOpenGLFunctions_4_3_Compatibility::glPrimitiveRestartIndex(GLuint
    #      index)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility23glPrimitiveRestartI'
        'ndexEj',
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
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexBuffer(GLenum
    target, GLenum internalformat, GLuint buffer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    target : int
      Passed on as it is.

    internalformat : int
      Passed on as it is.

    buffer : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glTexBuffer(GLenum target,
    #      GLenum internalformat, GLuint buffer)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility11glTexBufferEjjj',
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
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glDrawArraysInstanced(GLenum mode,
    GLint first, GLsizei count, GLsizei instancecount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glDrawArraysInstanced(GLenum
    #      mode, GLint first, GLsizei count, GLsizei instancecount)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility21glDrawArraysInstanc'
        'edEjiii',
        mode, first, count, instancecount,
    )

  @overload(int, int)
  def glSampleMaski(self, index: int, mask: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glSampleMaski(GLuint
    index, GLbitfield mask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    index : int
      Passed on as it is.

    mask : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glSampleMaski(GLuint index,
    #      GLbitfield mask)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility13glSampleMaskiEjj',
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
    QOpenGLFunctions_4_3_Compatibility::glTexImage3DMultisample(GLenum
    target, GLsizei samples, GLint internalformat, GLsizei width, GLsizei
    height, GLsizei depth, GLboolean fixedsamplelocations)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void
    #      QOpenGLFunctions_4_3_Compatibility::glTexImage3DMultisample(GLenum
    #      target, GLsizei samples, GLint internalformat, GLsizei width,
    #      GLsizei height, GLsizei depth, GLboolean fixedsamplelocations)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility23glTexImage3DMultisa'
        'mpleEjiiiiih',
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
    QOpenGLFunctions_4_3_Compatibility::glTexImage2DMultisample(GLenum
    target, GLsizei samples, GLint internalformat, GLsizei width, GLsizei
    height, GLboolean fixedsamplelocations)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void
    #      QOpenGLFunctions_4_3_Compatibility::glTexImage2DMultisample(GLenum
    #      target, GLsizei samples, GLint internalformat, GLsizei width,
    #      GLsizei height, GLboolean fixedsamplelocations)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility23glTexImage2DMultisa'
        'mpleEjiiiih',
        target, samples, internalformat, width, height, fixedsamplelocations,
    )

  @overload(int)
  def glProvokingVertex(self, mode: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glProvokingVertex(GLenum mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glProvokingVertex(GLenum
    #      mode)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility17glProvokingVertexEj',
        mode,
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
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glFramebufferTexture(GLenum target,
    GLenum attachment, GLuint texture, GLint level)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glFramebufferTexture(GLenum
    #      target, GLenum attachment, GLuint texture, GLint level)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility20glFramebufferTextur'
        'eEjjji',
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
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glVertexAttribP4ui(GLuint index,
    GLenum type, GLboolean normalized, GLuint value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glVertexAttribP4ui(GLuint
    #      index, GLenum type, GLboolean normalized, GLuint value)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility18glVertexAttribP4uiE'
        'jjhj',
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
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glVertexAttribP3ui(GLuint index,
    GLenum type, GLboolean normalized, GLuint value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glVertexAttribP3ui(GLuint
    #      index, GLenum type, GLboolean normalized, GLuint value)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility18glVertexAttribP3uiE'
        'jjhj',
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
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glVertexAttribP2ui(GLuint index,
    GLenum type, GLboolean normalized, GLuint value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glVertexAttribP2ui(GLuint
    #      index, GLenum type, GLboolean normalized, GLuint value)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility18glVertexAttribP2uiE'
        'jjhj',
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
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glVertexAttribP1ui(GLuint index,
    GLenum type, GLboolean normalized, GLuint value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glVertexAttribP1ui(GLuint
    #      index, GLenum type, GLboolean normalized, GLuint value)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility18glVertexAttribP1uiE'
        'jjhj',
        index, type, normalized, value,
    )

  @overload(int, int)
  def glSecondaryColorP3ui(self, type: int, color: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glSecondaryColorP3ui(GLenum type,
    GLuint color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    type : int
      Passed on as it is.

    color : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glSecondaryColorP3ui(GLenum
    #      type, GLuint color)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility20glSecondaryColorP3u'
        'iEjj',
        type, color,
    )

  @overload(int, int)
  def glColorP4ui(self, type: int, color: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glColorP4ui(GLenum
    type, GLuint color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    type : int
      Passed on as it is.

    color : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glColorP4ui(GLenum type,
    #      GLuint color)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility11glColorP4uiEjj',
        type, color,
    )

  @overload(int, int)
  def glColorP3ui(self, type: int, color: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glColorP3ui(GLenum
    type, GLuint color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    type : int
      Passed on as it is.

    color : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glColorP3ui(GLenum type,
    #      GLuint color)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility11glColorP3uiEjj',
        type, color,
    )

  @overload(int, int)
  def glNormalP3ui(self, type: int, coords: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glNormalP3ui(GLenum
    type, GLuint coords)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    type : int
      Passed on as it is.

    coords : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glNormalP3ui(GLenum type,
    #      GLuint coords)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility12glNormalP3uiEjj',
        type, coords,
    )

  @overload(int, int, int)
  def glMultiTexCoordP4ui(
      self,
      texture: int,
      type: int,
      coords: int,
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glMultiTexCoordP4ui(GLenum texture,
    GLenum type, GLuint coords)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    texture : int
      Passed on as it is.

    type : int
      Passed on as it is.

    coords : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glMultiTexCoordP4ui(GLenum
    #      texture, GLenum type, GLuint coords)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility19glMultiTexCoordP4ui'
        'Ejjj',
        texture, type, coords,
    )

  @overload(int, int, int)
  def glMultiTexCoordP3ui(
      self,
      texture: int,
      type: int,
      coords: int,
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glMultiTexCoordP3ui(GLenum texture,
    GLenum type, GLuint coords)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    texture : int
      Passed on as it is.

    type : int
      Passed on as it is.

    coords : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glMultiTexCoordP3ui(GLenum
    #      texture, GLenum type, GLuint coords)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility19glMultiTexCoordP3ui'
        'Ejjj',
        texture, type, coords,
    )

  @overload(int, int, int)
  def glMultiTexCoordP2ui(
      self,
      texture: int,
      type: int,
      coords: int,
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glMultiTexCoordP2ui(GLenum texture,
    GLenum type, GLuint coords)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    texture : int
      Passed on as it is.

    type : int
      Passed on as it is.

    coords : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glMultiTexCoordP2ui(GLenum
    #      texture, GLenum type, GLuint coords)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility19glMultiTexCoordP2ui'
        'Ejjj',
        texture, type, coords,
    )

  @overload(int, int, int)
  def glMultiTexCoordP1ui(
      self,
      texture: int,
      type: int,
      coords: int,
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glMultiTexCoordP1ui(GLenum texture,
    GLenum type, GLuint coords)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    texture : int
      Passed on as it is.

    type : int
      Passed on as it is.

    coords : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glMultiTexCoordP1ui(GLenum
    #      texture, GLenum type, GLuint coords)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility19glMultiTexCoordP1ui'
        'Ejjj',
        texture, type, coords,
    )

  @overload(int, int)
  def glTexCoordP4ui(self, type: int, coords: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glTexCoordP4ui(GLenum type, GLuint
    coords)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    type : int
      Passed on as it is.

    coords : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glTexCoordP4ui(GLenum type,
    #      GLuint coords)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility14glTexCoordP4uiEjj',
        type, coords,
    )

  @overload(int, int)
  def glTexCoordP3ui(self, type: int, coords: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glTexCoordP3ui(GLenum type, GLuint
    coords)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    type : int
      Passed on as it is.

    coords : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glTexCoordP3ui(GLenum type,
    #      GLuint coords)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility14glTexCoordP3uiEjj',
        type, coords,
    )

  @overload(int, int)
  def glTexCoordP2ui(self, type: int, coords: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glTexCoordP2ui(GLenum type, GLuint
    coords)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    type : int
      Passed on as it is.

    coords : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glTexCoordP2ui(GLenum type,
    #      GLuint coords)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility14glTexCoordP2uiEjj',
        type, coords,
    )

  @overload(int, int)
  def glTexCoordP1ui(self, type: int, coords: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glTexCoordP1ui(GLenum type, GLuint
    coords)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    type : int
      Passed on as it is.

    coords : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glTexCoordP1ui(GLenum type,
    #      GLuint coords)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility14glTexCoordP1uiEjj',
        type, coords,
    )

  @overload(int, int)
  def glVertexP4ui(self, type: int, value: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexP4ui(GLenum
    type, GLuint value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    type : int
      Passed on as it is.

    value : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glVertexP4ui(GLenum type,
    #      GLuint value)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility12glVertexP4uiEjj',
        type, value,
    )

  @overload(int, int)
  def glVertexP3ui(self, type: int, value: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexP3ui(GLenum
    type, GLuint value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    type : int
      Passed on as it is.

    value : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glVertexP3ui(GLenum type,
    #      GLuint value)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility12glVertexP3uiEjj',
        type, value,
    )

  @overload(int, int)
  def glVertexP2ui(self, type: int, value: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexP2ui(GLenum
    type, GLuint value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    type : int
      Passed on as it is.

    value : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glVertexP2ui(GLenum type,
    #      GLuint value)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility12glVertexP2uiEjj',
        type, value,
    )

  @overload(int, int)
  def glQueryCounter(self, id: int, target: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glQueryCounter(GLuint id, GLenum
    target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    id : int
      Passed on as it is.

    target : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glQueryCounter(GLuint id,
    #      GLenum target)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility14glQueryCounterEjj',
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
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glSamplerParameterf(GLuint sampler,
    GLenum pname, GLfloat param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    sampler : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    param : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glSamplerParameterf(GLuint
    #      sampler, GLenum pname, GLfloat param)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility19glSamplerParameterf'
        'Ejjf',
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
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glSamplerParameteri(GLuint sampler,
    GLenum pname, GLint param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    sampler : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    param : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glSamplerParameteri(GLuint
    #      sampler, GLenum pname, GLint param)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility19glSamplerParameteri'
        'Ejji',
        sampler, pname, param,
    )

  @overload(int, int)
  def glBindSampler(self, unit: int, sampler: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glBindSampler(GLuint
    unit, GLuint sampler)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    unit : int
      Passed on as it is.

    sampler : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glBindSampler(GLuint unit,
    #      GLuint sampler)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility13glBindSamplerEjj',
        unit, sampler,
    )

  @overload(int)
  def glIsSampler(self, sampler: int) -> int:
    """
    Calls Qt's 'GLboolean
    QOpenGLFunctions_4_3_Compatibility::glIsSampler(GLuint sampler)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    sampler : int
      Passed on as it is.
    """
    #  GLboolean QOpenGLFunctions_4_3_Compatibility::glIsSampler(GLuint
    #      sampler)
    return self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility11glIsSamplerEj',
        sampler,
    )

  @overload(int, int)
  def glVertexAttribDivisor(self, index: int, divisor: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glVertexAttribDivisor(GLuint index,
    GLuint divisor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    index : int
      Passed on as it is.

    divisor : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glVertexAttribDivisor(GLuint
    #      index, GLuint divisor)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility21glVertexAttribDivis'
        'orEjj',
        index, divisor,
    )

  @overload(int, int)
  def glEndQueryIndexed(self, target: int, index: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glEndQueryIndexed(GLenum target,
    GLuint index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    target : int
      Passed on as it is.

    index : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glEndQueryIndexed(GLenum
    #      target, GLuint index)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility17glEndQueryIndexedEj'
        'j',
        target, index,
    )

  @overload(int, int, int)
  def glBeginQueryIndexed(self, target: int, index: int, id: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glBeginQueryIndexed(GLenum target,
    GLuint index, GLuint id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    target : int
      Passed on as it is.

    index : int
      Passed on as it is.

    id : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glBeginQueryIndexed(GLenum
    #      target, GLuint index, GLuint id)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility19glBeginQueryIndexed'
        'Ejjj',
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
    QOpenGLFunctions_4_3_Compatibility::glDrawTransformFeedbackStream(GLenum
    mode, GLuint id, GLuint stream)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    mode : int
      Passed on as it is.

    id : int
      Passed on as it is.

    stream : int
      Passed on as it is.
    """
    #  void
    #      QOpenGLFunctions_4_3_Compatibility::glDrawTransformFeedbackStream(
    #      GLenum mode, GLuint id, GLuint stream)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility29glDrawTransformFeed'
        'backStreamEjjj',
        mode, id, stream,
    )

  @overload(int, int)
  def glDrawTransformFeedback(self, mode: int, id: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glDrawTransformFeedback(GLenum mode,
    GLuint id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    mode : int
      Passed on as it is.

    id : int
      Passed on as it is.
    """
    #  void
    #      QOpenGLFunctions_4_3_Compatibility::glDrawTransformFeedback(GLenum
    #      mode, GLuint id)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility23glDrawTransformFeed'
        'backEjj',
        mode, id,
    )

  def glResumeTransformFeedback(self) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glResumeTransformFeedback()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glResumeTransformFeedback()
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility25glResumeTransformFe'
        'edbackEv',
    )

  def glPauseTransformFeedback(self) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glPauseTransformFeedback()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glPauseTransformFeedback()
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility24glPauseTransformFee'
        'dbackEv',
    )

  @overload(int)
  def glIsTransformFeedback(self, id: int) -> int:
    """
    Calls Qt's 'GLboolean
    QOpenGLFunctions_4_3_Compatibility::glIsTransformFeedback(GLuint id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    id : int
      Passed on as it is.
    """
    #  GLboolean
    #      QOpenGLFunctions_4_3_Compatibility::glIsTransformFeedback(GLuint
    #      id)
    return self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility21glIsTransformFeedba'
        'ckEj',
        id,
    )

  @overload(int, int)
  def glBindTransformFeedback(self, target: int, id: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glBindTransformFeedback(GLenum
    target, GLuint id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    target : int
      Passed on as it is.

    id : int
      Passed on as it is.
    """
    #  void
    #      QOpenGLFunctions_4_3_Compatibility::glBindTransformFeedback(GLenum
    #      target, GLuint id)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility23glBindTransformFeed'
        'backEjj',
        target, id,
    )

  @overload(int, int)
  def glPatchParameteri(self, pname: int, value: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glPatchParameteri(GLenum pname, GLint
    value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    pname : int
      Passed on as it is.

    value : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glPatchParameteri(GLenum
    #      pname, GLint value)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility17glPatchParameteriEj'
        'i',
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
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniform4d(GLint
    location, GLdouble x, GLdouble y, GLdouble z, GLdouble w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glUniform4d(GLint location,
    #      GLdouble x, GLdouble y, GLdouble z, GLdouble w)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility11glUniform4dEidddd',
        location, x, y, z, w,
    )

  @overload(int, float, float, float)
  def glUniform3d(self, location: int, x: float, y: float, z: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniform3d(GLint
    location, GLdouble x, GLdouble y, GLdouble z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glUniform3d(GLint location,
    #      GLdouble x, GLdouble y, GLdouble z)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility11glUniform3dEiddd',
        location, x, y, z,
    )

  @overload(int, float, float)
  def glUniform2d(self, location: int, x: float, y: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniform2d(GLint
    location, GLdouble x, GLdouble y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    location : int
      Passed on as it is.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glUniform2d(GLint location,
    #      GLdouble x, GLdouble y)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility11glUniform2dEidd',
        location, x, y,
    )

  @overload(int, float)
  def glUniform1d(self, location: int, x: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniform1d(GLint
    location, GLdouble x)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    location : int
      Passed on as it is.

    x : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glUniform1d(GLint location,
    #      GLdouble x)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility11glUniform1dEid',
        location, x,
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
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glBlendFuncSeparatei(GLuint buf,
    GLenum srcRGB, GLenum dstRGB, GLenum srcAlpha, GLenum dstAlpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glBlendFuncSeparatei(GLuint
    #      buf, GLenum srcRGB, GLenum dstRGB, GLenum srcAlpha, GLenum
    #      dstAlpha)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility20glBlendFuncSeparate'
        'iEjjjjj',
        buf, srcRGB, dstRGB, srcAlpha, dstAlpha,
    )

  @overload(int, int, int)
  def glBlendFunci(self, buf: int, src: int, dst: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glBlendFunci(GLuint
    buf, GLenum src, GLenum dst)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    buf : int
      Passed on as it is.

    src : int
      Passed on as it is.

    dst : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glBlendFunci(GLuint buf,
    #      GLenum src, GLenum dst)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility12glBlendFunciEjjj',
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
    QOpenGLFunctions_4_3_Compatibility::glBlendEquationSeparatei(GLuint buf,
    GLenum modeRGB, GLenum modeAlpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    buf : int
      Passed on as it is.

    modeRGB : int
      Passed on as it is.

    modeAlpha : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glBlendEquationSeparatei(
    #      GLuint buf, GLenum modeRGB, GLenum modeAlpha)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility24glBlendEquationSepa'
        'rateiEjjj',
        buf, modeRGB, modeAlpha,
    )

  @overload(int, int)
  def glBlendEquationi(self, buf: int, mode: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glBlendEquationi(GLuint buf, GLenum
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    buf : int
      Passed on as it is.

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glBlendEquationi(GLuint buf,
    #      GLenum mode)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility16glBlendEquationiEjj',
        buf, mode,
    )

  @overload(float)
  def glMinSampleShading(self, value: float) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glMinSampleShading(GLfloat value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glMinSampleShading(GLfloat
    #      value)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility18glMinSampleShadingE'
        'f',
        value,
    )

  @overload(int, float, float)
  def glDepthRangeIndexed(self, index: int, n: float, f: float) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glDepthRangeIndexed(GLuint index,
    GLdouble n, GLdouble f)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    index : int
      Passed on as it is.

    n : float
      Passed on as it is.

    f : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glDepthRangeIndexed(GLuint
    #      index, GLdouble n, GLdouble f)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility19glDepthRangeIndexed'
        'Ejdd',
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
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glScissorIndexed(GLuint index, GLint
    left, GLint bottom, GLsizei width, GLsizei height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glScissorIndexed(GLuint
    #      index, GLint left, GLint bottom, GLsizei width, GLsizei height)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility16glScissorIndexedEji'
        'iii',
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
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glViewportIndexedf(GLuint index,
    GLfloat x, GLfloat y, GLfloat w, GLfloat h)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glViewportIndexedf(GLuint
    #      index, GLfloat x, GLfloat y, GLfloat w, GLfloat h)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility18glViewportIndexedfE'
        'jffff',
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
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glVertexAttribL4d(GLuint index,
    GLdouble x, GLdouble y, GLdouble z, GLdouble w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glVertexAttribL4d(GLuint
    #      index, GLdouble x, GLdouble y, GLdouble z, GLdouble w)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility17glVertexAttribL4dEj'
        'dddd',
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
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glVertexAttribL3d(GLuint index,
    GLdouble x, GLdouble y, GLdouble z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glVertexAttribL3d(GLuint
    #      index, GLdouble x, GLdouble y, GLdouble z)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility17glVertexAttribL3dEj'
        'ddd',
        index, x, y, z,
    )

  @overload(int, float, float)
  def glVertexAttribL2d(self, index: int, x: float, y: float) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glVertexAttribL2d(GLuint index,
    GLdouble x, GLdouble y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    index : int
      Passed on as it is.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glVertexAttribL2d(GLuint
    #      index, GLdouble x, GLdouble y)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility17glVertexAttribL2dEj'
        'dd',
        index, x, y,
    )

  @overload(int, float)
  def glVertexAttribL1d(self, index: int, x: float) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glVertexAttribL1d(GLuint index,
    GLdouble x)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    index : int
      Passed on as it is.

    x : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glVertexAttribL1d(GLuint
    #      index, GLdouble x)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility17glVertexAttribL1dEj'
        'd',
        index, x,
    )

  @overload(int)
  def glValidateProgramPipeline(self, pipeline: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glValidateProgramPipeline(GLuint
    pipeline)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    pipeline : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glValidateProgramPipeline(
    #      GLuint pipeline)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility25glValidateProgramPi'
        'pelineEj',
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
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glProgramUniform4ui(GLuint program,
    GLint location, GLuint v0, GLuint v1, GLuint v2, GLuint v3)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glProgramUniform4ui(GLuint
    #      program, GLint location, GLuint v0, GLuint v1, GLuint v2, GLuint
    #      v3)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility19glProgramUniform4ui'
        'Ejijjjj',
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
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glProgramUniform4d(GLuint program,
    GLint location, GLdouble v0, GLdouble v1, GLdouble v2, GLdouble v3)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glProgramUniform4d(GLuint
    #      program, GLint location, GLdouble v0, GLdouble v1, GLdouble v2,
    #      GLdouble v3)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility18glProgramUniform4dE'
        'jidddd',
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
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glProgramUniform4f(GLuint program,
    GLint location, GLfloat v0, GLfloat v1, GLfloat v2, GLfloat v3)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glProgramUniform4f(GLuint
    #      program, GLint location, GLfloat v0, GLfloat v1, GLfloat v2,
    #      GLfloat v3)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility18glProgramUniform4fE'
        'jiffff',
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
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glProgramUniform4i(GLuint program,
    GLint location, GLint v0, GLint v1, GLint v2, GLint v3)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glProgramUniform4i(GLuint
    #      program, GLint location, GLint v0, GLint v1, GLint v2, GLint v3)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility18glProgramUniform4iE'
        'jiiiii',
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
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glProgramUniform3ui(GLuint program,
    GLint location, GLuint v0, GLuint v1, GLuint v2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glProgramUniform3ui(GLuint
    #      program, GLint location, GLuint v0, GLuint v1, GLuint v2)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility19glProgramUniform3ui'
        'Ejijjj',
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
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glProgramUniform3d(GLuint program,
    GLint location, GLdouble v0, GLdouble v1, GLdouble v2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glProgramUniform3d(GLuint
    #      program, GLint location, GLdouble v0, GLdouble v1, GLdouble v2)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility18glProgramUniform3dE'
        'jiddd',
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
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glProgramUniform3f(GLuint program,
    GLint location, GLfloat v0, GLfloat v1, GLfloat v2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glProgramUniform3f(GLuint
    #      program, GLint location, GLfloat v0, GLfloat v1, GLfloat v2)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility18glProgramUniform3fE'
        'jifff',
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
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glProgramUniform3i(GLuint program,
    GLint location, GLint v0, GLint v1, GLint v2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glProgramUniform3i(GLuint
    #      program, GLint location, GLint v0, GLint v1, GLint v2)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility18glProgramUniform3iE'
        'jiiii',
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
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glProgramUniform2ui(GLuint program,
    GLint location, GLuint v0, GLuint v1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glProgramUniform2ui(GLuint
    #      program, GLint location, GLuint v0, GLuint v1)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility19glProgramUniform2ui'
        'Ejijj',
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
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glProgramUniform2d(GLuint program,
    GLint location, GLdouble v0, GLdouble v1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glProgramUniform2d(GLuint
    #      program, GLint location, GLdouble v0, GLdouble v1)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility18glProgramUniform2dE'
        'jidd',
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
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glProgramUniform2f(GLuint program,
    GLint location, GLfloat v0, GLfloat v1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glProgramUniform2f(GLuint
    #      program, GLint location, GLfloat v0, GLfloat v1)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility18glProgramUniform2fE'
        'jiff',
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
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glProgramUniform2i(GLuint program,
    GLint location, GLint v0, GLint v1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glProgramUniform2i(GLuint
    #      program, GLint location, GLint v0, GLint v1)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility18glProgramUniform2iE'
        'jiii',
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
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glProgramUniform1ui(GLuint program,
    GLint location, GLuint v0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    program : int
      Passed on as it is.

    location : int
      Passed on as it is.

    v0 : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glProgramUniform1ui(GLuint
    #      program, GLint location, GLuint v0)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility19glProgramUniform1ui'
        'Ejij',
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
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glProgramUniform1d(GLuint program,
    GLint location, GLdouble v0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    program : int
      Passed on as it is.

    location : int
      Passed on as it is.

    v0 : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glProgramUniform1d(GLuint
    #      program, GLint location, GLdouble v0)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility18glProgramUniform1dE'
        'jid',
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
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glProgramUniform1f(GLuint program,
    GLint location, GLfloat v0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    program : int
      Passed on as it is.

    location : int
      Passed on as it is.

    v0 : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glProgramUniform1f(GLuint
    #      program, GLint location, GLfloat v0)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility18glProgramUniform1fE'
        'jif',
        program, location, v0,
    )

  @overload(int, int, int)
  def glProgramUniform1i(self, program: int, location: int, v0: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glProgramUniform1i(GLuint program,
    GLint location, GLint v0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    program : int
      Passed on as it is.

    location : int
      Passed on as it is.

    v0 : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glProgramUniform1i(GLuint
    #      program, GLint location, GLint v0)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility18glProgramUniform1iE'
        'jii',
        program, location, v0,
    )

  @overload(int)
  def glIsProgramPipeline(self, pipeline: int) -> int:
    """
    Calls Qt's 'GLboolean
    QOpenGLFunctions_4_3_Compatibility::glIsProgramPipeline(GLuint
    pipeline)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    pipeline : int
      Passed on as it is.
    """
    #  GLboolean
    #      QOpenGLFunctions_4_3_Compatibility::glIsProgramPipeline(GLuint
    #      pipeline)
    return self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility19glIsProgramPipeline'
        'Ej',
        pipeline,
    )

  @overload(int)
  def glBindProgramPipeline(self, pipeline: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glBindProgramPipeline(GLuint
    pipeline)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    pipeline : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glBindProgramPipeline(GLuint
    #      pipeline)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility21glBindProgramPipeli'
        'neEj',
        pipeline,
    )

  @overload(int, int)
  def glActiveShaderProgram(self, pipeline: int, program: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glActiveShaderProgram(GLuint
    pipeline, GLuint program)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    pipeline : int
      Passed on as it is.

    program : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glActiveShaderProgram(GLuint
    #      pipeline, GLuint program)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility21glActiveShaderProgr'
        'amEjj',
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
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glUseProgramStages(GLuint pipeline,
    GLbitfield stages, GLuint program)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    pipeline : int
      Passed on as it is.

    stages : int
      Passed on as it is.

    program : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glUseProgramStages(GLuint
    #      pipeline, GLbitfield stages, GLuint program)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility18glUseProgramStagesE'
        'jjj',
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
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glProgramParameteri(GLuint program,
    GLenum pname, GLint value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    program : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    value : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glProgramParameteri(GLuint
    #      program, GLenum pname, GLint value)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility19glProgramParameteri'
        'Ejji',
        program, pname, value,
    )

  @overload(float)
  def glClearDepthf(self, dd: float) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glClearDepthf(GLfloat dd)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    dd : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glClearDepthf(GLfloat dd)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility13glClearDepthfEf', dd,
    )

  @overload(float, float)
  def glDepthRangef(self, n: float, f: float) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glDepthRangef(GLfloat n, GLfloat f)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    n : float
      Passed on as it is.

    f : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glDepthRangef(GLfloat n,
    #      GLfloat f)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility13glDepthRangefEff',
        n, f,
    )

  def glReleaseShaderCompiler(self) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glReleaseShaderCompiler()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glReleaseShaderCompiler()
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility23glReleaseShaderComp'
        'ilerEv',
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
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glTexStorage3D(GLenum target, GLsizei
    levels, GLenum internalformat, GLsizei width, GLsizei height, GLsizei
    depth)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glTexStorage3D(GLenum target,
    #      GLsizei levels, GLenum internalformat, GLsizei width, GLsizei
    #      height, GLsizei depth)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility14glTexStorage3DEjiji'
        'ii',
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
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glTexStorage2D(GLenum target, GLsizei
    levels, GLenum internalformat, GLsizei width, GLsizei height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glTexStorage2D(GLenum target,
    #      GLsizei levels, GLenum internalformat, GLsizei width, GLsizei
    #      height)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility14glTexStorage2DEjiji'
        'i',
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
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glTexStorage1D(GLenum target, GLsizei
    levels, GLenum internalformat, GLsizei width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glTexStorage1D(GLenum target,
    #      GLsizei levels, GLenum internalformat, GLsizei width)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility14glTexStorage1DEjiji',
        target, levels, internalformat, width,
    )

  @overload(int)
  def glMemoryBarrier(self, barriers: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glMemoryBarrier(GLbitfield
    barriers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    barriers : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glMemoryBarrier(GLbitfield
    #      barriers)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility15glMemoryBarrierEj',
        barriers,
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
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glBindImageTexture(GLuint unit,
    GLuint texture, GLint level, GLboolean layered, GLint layer, GLenum
    access, GLenum format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glBindImageTexture(GLuint
    #      unit, GLuint texture, GLint level, GLboolean layered, GLint layer,
    #      GLenum access, GLenum format)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility18glBindImageTextureE'
        'jjihijj',
        unit, texture, level, layered, layer, access, format,
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
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::
    glDrawTransformFeedbackStreamInstanced(GLenum mode, GLuint id, GLuint
    stream, GLsizei instancecount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::
    #      glDrawTransformFeedbackStreamInstanced(GLenum mode, GLuint id,
    #      GLuint stream, GLsizei instancecount)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility38glDrawTransformFeed'
        'backStreamInstancedEjjji',
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
    QOpenGLFunctions_4_3_Compatibility::glDrawTransformFeedbackInstanced(
    GLenum mode, GLuint id, GLsizei instancecount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    mode : int
      Passed on as it is.

    id : int
      Passed on as it is.

    instancecount : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::
    #      glDrawTransformFeedbackInstanced(GLenum mode, GLuint id, GLsizei
    #      instancecount)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility32glDrawTransformFeed'
        'backInstancedEjji',
        mode, id, instancecount,
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
    QOpenGLFunctions_4_3_Compatibility::glDrawArraysInstancedBaseInstance(
    GLenum mode, GLint first, GLsizei count, GLsizei instancecount, GLuint
    baseinstance)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::
    #      glDrawArraysInstancedBaseInstance(GLenum mode, GLint first,
    #      GLsizei count, GLsizei instancecount, GLuint baseinstance)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility33glDrawArraysInstanc'
        'edBaseInstanceEjiiij',
        mode, first, count, instancecount, baseinstance,
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
    QOpenGLFunctions_4_3_Compatibility::glTexStorage3DMultisample(GLenum
    target, GLsizei samples, GLenum internalformat, GLsizei width, GLsizei
    height, GLsizei depth, GLboolean fixedsamplelocations)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glTexStorage3DMultisample(
    #      GLenum target, GLsizei samples, GLenum internalformat, GLsizei
    #      width, GLsizei height, GLsizei depth, GLboolean
    #      fixedsamplelocations)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility25glTexStorage3DMulti'
        'sampleEjijiiih',
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
    QOpenGLFunctions_4_3_Compatibility::glTexStorage2DMultisample(GLenum
    target, GLsizei samples, GLenum internalformat, GLsizei width, GLsizei
    height, GLboolean fixedsamplelocations)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glTexStorage2DMultisample(
    #      GLenum target, GLsizei samples, GLenum internalformat, GLsizei
    #      width, GLsizei height, GLboolean fixedsamplelocations)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility25glTexStorage2DMulti'
        'sampleEjijiih',
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
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glTexBufferRange(GLenum target,
    GLenum internalformat, GLuint buffer, GLintptr offset, GLsizeiptr size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glTexBufferRange(GLenum
    #      target, GLenum internalformat, GLuint buffer, GLintptr offset,
    #      GLsizeiptr size)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility16glTexBufferRangeEjj'
        'jll',
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
    QOpenGLFunctions_4_3_Compatibility::glShaderStorageBlockBinding(GLuint
    program, GLuint storageBlockIndex, GLuint storageBlockBinding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    program : int
      Passed on as it is.

    storageBlockIndex : int
      Passed on as it is.

    storageBlockBinding : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glShaderStorageBlockBinding(
    #      GLuint program, GLuint storageBlockIndex, GLuint
    #      storageBlockBinding)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility27glShaderStorageBloc'
        'kBindingEjjj',
        program, storageBlockIndex, storageBlockBinding,
    )

  @overload(int)
  def glInvalidateBufferData(self, buffer: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glInvalidateBufferData(GLuint
    buffer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    buffer : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glInvalidateBufferData(GLuint
    #      buffer)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility22glInvalidateBufferD'
        'ataEj',
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
    QOpenGLFunctions_4_3_Compatibility::glInvalidateBufferSubData(GLuint
    buffer, GLintptr offset, GLsizeiptr length)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    buffer : int
      Passed on as it is.

    offset : int
      Passed on as it is.

    length : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glInvalidateBufferSubData(
    #      GLuint buffer, GLintptr offset, GLsizeiptr length)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility25glInvalidateBufferS'
        'ubDataEjll',
        buffer, offset, length,
    )

  @overload(int, int)
  def glInvalidateTexImage(self, texture: int, level: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glInvalidateTexImage(GLuint texture,
    GLint level)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    texture : int
      Passed on as it is.

    level : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glInvalidateTexImage(GLuint
    #      texture, GLint level)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility20glInvalidateTexImag'
        'eEji',
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
    QOpenGLFunctions_4_3_Compatibility::glInvalidateTexSubImage(GLuint
    texture, GLint level, GLint xoffset, GLint yoffset, GLint zoffset,
    GLsizei width, GLsizei height, GLsizei depth)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void
    #      QOpenGLFunctions_4_3_Compatibility::glInvalidateTexSubImage(GLuint
    #      texture, GLint level, GLint xoffset, GLint yoffset, GLint zoffset,
    #      GLsizei width, GLsizei height, GLsizei depth)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility23glInvalidateTexSubI'
        'mageEjiiiiiii',
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
    QOpenGLFunctions_4_3_Compatibility::glFramebufferParameteri(GLenum
    target, GLenum pname, GLint param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    target : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    param : int
      Passed on as it is.
    """
    #  void
    #      QOpenGLFunctions_4_3_Compatibility::glFramebufferParameteri(GLenum
    #      target, GLenum pname, GLint param)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility23glFramebufferParame'
        'teriEjji',
        target, pname, param,
    )

  @overload(int, int)
  def glVertexBindingDivisor(self, bindingindex: int, divisor: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glVertexBindingDivisor(GLuint
    bindingindex, GLuint divisor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    bindingindex : int
      Passed on as it is.

    divisor : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glVertexBindingDivisor(GLuint
    #      bindingindex, GLuint divisor)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility22glVertexBindingDivi'
        'sorEjj',
        bindingindex, divisor,
    )

  @overload(int, int)
  def glVertexAttribBinding(
      self,
      attribindex: int,
      bindingindex: int,
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glVertexAttribBinding(GLuint
    attribindex, GLuint bindingindex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    attribindex : int
      Passed on as it is.

    bindingindex : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glVertexAttribBinding(GLuint
    #      attribindex, GLuint bindingindex)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility21glVertexAttribBindi'
        'ngEjj',
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
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glVertexAttribLFormat(GLuint
    attribindex, GLint size, GLenum type, GLuint relativeoffset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glVertexAttribLFormat(GLuint
    #      attribindex, GLint size, GLenum type, GLuint relativeoffset)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility21glVertexAttribLForm'
        'atEjijj',
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
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glVertexAttribIFormat(GLuint
    attribindex, GLint size, GLenum type, GLuint relativeoffset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glVertexAttribIFormat(GLuint
    #      attribindex, GLint size, GLenum type, GLuint relativeoffset)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility21glVertexAttribIForm'
        'atEjijj',
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
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glVertexAttribFormat(GLuint
    attribindex, GLint size, GLenum type, GLboolean normalized, GLuint
    relativeoffset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glVertexAttribFormat(GLuint
    #      attribindex, GLint size, GLenum type, GLboolean normalized, GLuint
    #      relativeoffset)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility20glVertexAttribForma'
        'tEjijhj',
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
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glBindVertexBuffer(GLuint
    bindingindex, GLuint buffer, GLintptr offset, GLsizei stride)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glBindVertexBuffer(GLuint
    #      bindingindex, GLuint buffer, GLintptr offset, GLsizei stride)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility18glBindVertexBufferE'
        'jjli',
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
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTextureView(GLuint
    texture, GLenum target, GLuint origtexture, GLenum internalformat, GLuint
    minlevel, GLuint numlevels, GLuint minlayer, GLuint numlayers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glTextureView(GLuint texture,
    #      GLenum target, GLuint origtexture, GLenum internalformat, GLuint
    #      minlevel, GLuint numlevels, GLuint minlayer, GLuint numlayers)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility13glTextureViewEjjjjj'
        'jjj',
        texture, target, origtexture, internalformat, minlevel, numlevels,
        minlayer, numlayers,
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
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glCopyImageSubData(GLuint srcName,
    GLenum srcTarget, GLint srcLevel, GLint srcX, GLint srcY, GLint srcZ,
    GLuint dstName, GLenum dstTarget, GLint dstLevel, GLint dstX, GLint dstY,
    GLint dstZ, GLsizei srcWidth, GLsizei srcHeight, GLsizei srcDepth)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glCopyImageSubData(GLuint
    #      srcName, GLenum srcTarget, GLint srcLevel, GLint srcX, GLint srcY,
    #      GLint srcZ, GLuint dstName, GLenum dstTarget, GLint dstLevel,
    #      GLint dstX, GLint dstY, GLint dstZ, GLsizei srcWidth, GLsizei
    #      srcHeight, GLsizei srcDepth)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility18glCopyImageSubDataE'
        'jjiiiijjiiiiiii',
        srcName, srcTarget, srcLevel, srcX, srcY, srcZ, dstName, dstTarget,
        dstLevel, dstX, dstY, dstZ, srcWidth, srcHeight, srcDepth,
    )

  @overload(int)
  def glDispatchComputeIndirect(self, indirect: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glDispatchComputeIndirect(GLintptr
    indirect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    indirect : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glDispatchComputeIndirect(
    #      GLintptr indirect)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility25glDispatchComputeIn'
        'directEl',
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
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glDispatchCompute(GLuint
    num_groups_x, GLuint num_groups_y, GLuint num_groups_z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    num_groups_x : int
      Passed on as it is.

    num_groups_y : int
      Passed on as it is.

    num_groups_z : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glDispatchCompute(GLuint
    #      num_groups_x, GLuint num_groups_y, GLuint num_groups_z)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility17glDispatchComputeEj'
        'jj',
        num_groups_x, num_groups_y, num_groups_z,
    )

  @overload(float, float, float)
  def glTranslatef(self, x: float, y: float, z: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTranslatef(GLfloat
    x, GLfloat y, GLfloat z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glTranslatef(GLfloat x,
    #      GLfloat y, GLfloat z)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility12glTranslatefEfff',
        x, y, z,
    )

  @overload(float, float, float)
  def glTranslated(self, x: float, y: float, z: float) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glTranslated(GLdouble x, GLdouble y,
    GLdouble z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glTranslated(GLdouble x,
    #      GLdouble y, GLdouble z)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility12glTranslatedEddd',
        x, y, z,
    )

  @overload(float, float, float)
  def glScalef(self, x: float, y: float, z: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glScalef(GLfloat x,
    GLfloat y, GLfloat z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glScalef

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glScalef(GLfloat x, GLfloat
    #      y, GLfloat z)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility8glScalefEfff',
        x, y, z,
    )

  @overload(float, float, float)
  def glScaled(self, x: float, y: float, z: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glScaled(GLdouble x,
    GLdouble y, GLdouble z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glScaled

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glScaled(GLdouble x, GLdouble
    #      y, GLdouble z)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility8glScaledEddd',
        x, y, z,
    )

  @overload(float, float, float, float)
  def glRotatef(self, angle: float, x: float, y: float, z: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glRotatef(GLfloat
    angle, GLfloat x, GLfloat y, GLfloat z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glRotatef

    Parameters
    ----------

    angle : float
      Passed on as it is.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glRotatef(GLfloat angle,
    #      GLfloat x, GLfloat y, GLfloat z)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility9glRotatefEffff',
        angle, x, y, z,
    )

  @overload(float, float, float, float)
  def glRotated(self, angle: float, x: float, y: float, z: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glRotated(GLdouble
    angle, GLdouble x, GLdouble y, GLdouble z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glRotated

    Parameters
    ----------

    angle : float
      Passed on as it is.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glRotated(GLdouble angle,
    #      GLdouble x, GLdouble y, GLdouble z)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility9glRotatedEdddd',
        angle, x, y, z,
    )

  def glPushMatrix(self) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glPushMatrix()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glPushMatrix()
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility12glPushMatrixEv',
    )

  def glPopMatrix(self) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glPopMatrix()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glPopMatrix()
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility11glPopMatrixEv',
    )

  @overload(float, float, float, float, float, float)
  def glOrtho(
      self,
      left: float,
      right: float,
      bottom: float,
      top: float,
      zNear: float,
      zFar: float,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glOrtho(GLdouble
    left, GLdouble right, GLdouble bottom, GLdouble top, GLdouble zNear,
    GLdouble zFar)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glOrtho

    Parameters
    ----------

    left : float
      Passed on as it is.

    right : float
      Passed on as it is.

    bottom : float
      Passed on as it is.

    top : float
      Passed on as it is.

    zNear : float
      Passed on as it is.

    zFar : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glOrtho(GLdouble left,
    #      GLdouble right, GLdouble bottom, GLdouble top, GLdouble zNear,
    #      GLdouble zFar)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility7glOrthoEdddddd',
        left, right, bottom, top, zNear, zFar,
    )

  @overload(int)
  def glMatrixMode(self, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glMatrixMode(GLenum
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glMatrixMode(GLenum mode)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility12glMatrixModeEj',
        mode,
    )

  def glLoadIdentity(self) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glLoadIdentity()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glLoadIdentity()
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility14glLoadIdentityEv',
    )

  @overload(float, float, float, float, float, float)
  def glFrustum(
      self,
      left: float,
      right: float,
      bottom: float,
      top: float,
      zNear: float,
      zFar: float,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glFrustum(GLdouble
    left, GLdouble right, GLdouble bottom, GLdouble top, GLdouble zNear,
    GLdouble zFar)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glFrustum

    Parameters
    ----------

    left : float
      Passed on as it is.

    right : float
      Passed on as it is.

    bottom : float
      Passed on as it is.

    top : float
      Passed on as it is.

    zNear : float
      Passed on as it is.

    zFar : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glFrustum(GLdouble left,
    #      GLdouble right, GLdouble bottom, GLdouble top, GLdouble zNear,
    #      GLdouble zFar)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility9glFrustumEdddddd',
        left, right, bottom, top, zNear, zFar,
    )

  @overload(int)
  def glIsList(self, list: int) -> int:
    """
    Calls Qt's 'GLboolean QOpenGLFunctions_4_3_Compatibility::glIsList(GLuint
    list)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glIsList

    Parameters
    ----------

    list : int
      Passed on as it is.
    """
    #  GLboolean QOpenGLFunctions_4_3_Compatibility::glIsList(GLuint list)
    return self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility8glIsListEj', list,
    )

  @overload(int, int, int, int, int)
  def glCopyPixels(
      self,
      x: int,
      y: int,
      width: int,
      height: int,
      type: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glCopyPixels(GLint
    x, GLint y, GLsizei width, GLsizei height, GLenum type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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

    type : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glCopyPixels(GLint x, GLint
    #      y, GLsizei width, GLsizei height, GLenum type)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility12glCopyPixelsEiiiij',
        x, y, width, height, type,
    )

  @overload(int, int)
  def glPixelTransferi(self, pname: int, param: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glPixelTransferi(GLenum pname, GLint
    param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    pname : int
      Passed on as it is.

    param : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glPixelTransferi(GLenum
    #      pname, GLint param)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility16glPixelTransferiEji',
        pname, param,
    )

  @overload(int, float)
  def glPixelTransferf(self, pname: int, param: float) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glPixelTransferf(GLenum pname,
    GLfloat param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    pname : int
      Passed on as it is.

    param : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glPixelTransferf(GLenum
    #      pname, GLfloat param)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility16glPixelTransferfEjf',
        pname, param,
    )

  @overload(float, float)
  def glPixelZoom(self, xfactor: float, yfactor: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glPixelZoom(GLfloat
    xfactor, GLfloat yfactor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    xfactor : float
      Passed on as it is.

    yfactor : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glPixelZoom(GLfloat xfactor,
    #      GLfloat yfactor)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility11glPixelZoomEff',
        xfactor, yfactor,
    )

  @overload(int, float)
  def glAlphaFunc(self, func: int, ref: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glAlphaFunc(GLenum
    func, GLfloat ref)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    func : int
      Passed on as it is.

    ref : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glAlphaFunc(GLenum func,
    #      GLfloat ref)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility11glAlphaFuncEjf',
        func, ref,
    )

  @overload(int, int)
  def glEvalPoint2(self, i: int, j: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glEvalPoint2(GLint
    i, GLint j)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    i : int
      Passed on as it is.

    j : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glEvalPoint2(GLint i, GLint
    #      j)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility12glEvalPoint2Eii',
        i, j,
    )

  @overload(int, int, int, int, int)
  def glEvalMesh2(
      self,
      mode: int,
      i1: int,
      i2: int,
      j1: int,
      j2: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glEvalMesh2(GLenum
    mode, GLint i1, GLint i2, GLint j1, GLint j2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    mode : int
      Passed on as it is.

    i1 : int
      Passed on as it is.

    i2 : int
      Passed on as it is.

    j1 : int
      Passed on as it is.

    j2 : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glEvalMesh2(GLenum mode,
    #      GLint i1, GLint i2, GLint j1, GLint j2)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility11glEvalMesh2Ejiiii',
        mode, i1, i2, j1, j2,
    )

  @overload(int)
  def glEvalPoint1(self, i: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glEvalPoint1(GLint
    i)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    i : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glEvalPoint1(GLint i)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility12glEvalPoint1Ei', i,
    )

  @overload(int, int, int)
  def glEvalMesh1(self, mode: int, i1: int, i2: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glEvalMesh1(GLenum
    mode, GLint i1, GLint i2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    mode : int
      Passed on as it is.

    i1 : int
      Passed on as it is.

    i2 : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glEvalMesh1(GLenum mode,
    #      GLint i1, GLint i2)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility11glEvalMesh1Ejii',
        mode, i1, i2,
    )

  @overload(float, float)
  def glEvalCoord2f(self, u: float, v: float) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glEvalCoord2f(GLfloat u, GLfloat v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    u : float
      Passed on as it is.

    v : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glEvalCoord2f(GLfloat u,
    #      GLfloat v)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility13glEvalCoord2fEff',
        u, v,
    )

  @overload(float, float)
  def glEvalCoord2d(self, u: float, v: float) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glEvalCoord2d(GLdouble u, GLdouble
    v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    u : float
      Passed on as it is.

    v : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glEvalCoord2d(GLdouble u,
    #      GLdouble v)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility13glEvalCoord2dEdd',
        u, v,
    )

  @overload(float)
  def glEvalCoord1f(self, u: float) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glEvalCoord1f(GLfloat u)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    u : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glEvalCoord1f(GLfloat u)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility13glEvalCoord1fEf', u,
    )

  @overload(float)
  def glEvalCoord1d(self, u: float) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glEvalCoord1d(GLdouble u)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    u : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glEvalCoord1d(GLdouble u)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility13glEvalCoord1dEd', u,
    )

  @overload(int, float, float, int, float, float)
  def glMapGrid2f(
      self,
      un: int,
      u1: float,
      u2: float,
      vn: int,
      v1: float,
      v2: float,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glMapGrid2f(GLint
    un, GLfloat u1, GLfloat u2, GLint vn, GLfloat v1, GLfloat v2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    un : int
      Passed on as it is.

    u1 : float
      Passed on as it is.

    u2 : float
      Passed on as it is.

    vn : int
      Passed on as it is.

    v1 : float
      Passed on as it is.

    v2 : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glMapGrid2f(GLint un, GLfloat
    #      u1, GLfloat u2, GLint vn, GLfloat v1, GLfloat v2)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility11glMapGrid2fEiffiff',
        un, u1, u2, vn, v1, v2,
    )

  @overload(int, float, float, int, float, float)
  def glMapGrid2d(
      self,
      un: int,
      u1: float,
      u2: float,
      vn: int,
      v1: float,
      v2: float,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glMapGrid2d(GLint
    un, GLdouble u1, GLdouble u2, GLint vn, GLdouble v1, GLdouble v2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    un : int
      Passed on as it is.

    u1 : float
      Passed on as it is.

    u2 : float
      Passed on as it is.

    vn : int
      Passed on as it is.

    v1 : float
      Passed on as it is.

    v2 : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glMapGrid2d(GLint un,
    #      GLdouble u1, GLdouble u2, GLint vn, GLdouble v1, GLdouble v2)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility11glMapGrid2dEiddidd',
        un, u1, u2, vn, v1, v2,
    )

  @overload(int, float, float)
  def glMapGrid1f(self, un: int, u1: float, u2: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glMapGrid1f(GLint
    un, GLfloat u1, GLfloat u2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    un : int
      Passed on as it is.

    u1 : float
      Passed on as it is.

    u2 : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glMapGrid1f(GLint un, GLfloat
    #      u1, GLfloat u2)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility11glMapGrid1fEiff',
        un, u1, u2,
    )

  @overload(int, float, float)
  def glMapGrid1d(self, un: int, u1: float, u2: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glMapGrid1d(GLint
    un, GLdouble u1, GLdouble u2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    un : int
      Passed on as it is.

    u1 : float
      Passed on as it is.

    u2 : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glMapGrid1d(GLint un,
    #      GLdouble u1, GLdouble u2)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility11glMapGrid1dEidd',
        un, u1, u2,
    )

  @overload(int)
  def glPushAttrib(self, mask: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glPushAttrib(GLbitfield mask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    mask : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glPushAttrib(GLbitfield mask)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility12glPushAttribEj',
        mask,
    )

  def glPopAttrib(self) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glPopAttrib()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glPopAttrib()
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility11glPopAttribEv',
    )

  @overload(int, float)
  def glAccum(self, op: int, value: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glAccum(GLenum op,
    GLfloat value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glAccum

    Parameters
    ----------

    op : int
      Passed on as it is.

    value : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glAccum(GLenum op, GLfloat
    #      value)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility7glAccumEjf',
        op, value,
    )

  @overload(int)
  def glIndexMask(self, mask: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glIndexMask(GLuint
    mask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    mask : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glIndexMask(GLuint mask)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility11glIndexMaskEj', mask,
    )

  @overload(float)
  def glClearIndex(self, c: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glClearIndex(GLfloat
    c)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    c : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glClearIndex(GLfloat c)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility12glClearIndexEf', c,
    )

  @overload(float, float, float, float)
  def glClearAccum(
      self,
      red: float,
      green: float,
      blue: float,
      alpha: float,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glClearAccum(GLfloat
    red, GLfloat green, GLfloat blue, GLfloat alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glClearAccum(GLfloat red,
    #      GLfloat green, GLfloat blue, GLfloat alpha)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility12glClearAccumEffff',
        red, green, blue, alpha,
    )

  @overload(int)
  def glPushName(self, name: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glPushName(GLuint
    name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glPushName

    Parameters
    ----------

    name : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glPushName(GLuint name)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility10glPushNameEj', name,
    )

  def glPopName(self) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glPopName()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glPopName
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glPopName()
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility9glPopNameEv',
    )

  @overload(float)
  def glPassThrough(self, token: float) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glPassThrough(GLfloat token)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    token : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glPassThrough(GLfloat token)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility13glPassThroughEf',
        token,
    )

  @overload(int)
  def glLoadName(self, name: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glLoadName(GLuint
    name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glLoadName

    Parameters
    ----------

    name : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glLoadName(GLuint name)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility10glLoadNameEj', name,
    )

  def glInitNames(self) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glInitNames()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glInitNames()
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility11glInitNamesEv',
    )

  @overload(int)
  def glRenderMode(self, mode: int) -> int:
    """
    Calls Qt's 'GLint QOpenGLFunctions_4_3_Compatibility::glRenderMode(GLenum
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    mode : int
      Passed on as it is.
    """
    #  GLint QOpenGLFunctions_4_3_Compatibility::glRenderMode(GLenum mode)
    return self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility12glRenderModeEj',
        mode,
    )

  @overload(int, int, int)
  def glTexGeni(self, coord: int, pname: int, param: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexGeni(GLenum
    coord, GLenum pname, GLint param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glTexGeni

    Parameters
    ----------

    coord : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    param : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glTexGeni(GLenum coord,
    #      GLenum pname, GLint param)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility9glTexGeniEjji',
        coord, pname, param,
    )

  @overload(int, int, float)
  def glTexGenf(self, coord: int, pname: int, param: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexGenf(GLenum
    coord, GLenum pname, GLfloat param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glTexGenf

    Parameters
    ----------

    coord : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    param : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glTexGenf(GLenum coord,
    #      GLenum pname, GLfloat param)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility9glTexGenfEjjf',
        coord, pname, param,
    )

  @overload(int, int, float)
  def glTexGend(self, coord: int, pname: int, param: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexGend(GLenum
    coord, GLenum pname, GLdouble param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glTexGend

    Parameters
    ----------

    coord : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    param : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glTexGend(GLenum coord,
    #      GLenum pname, GLdouble param)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility9glTexGendEjjd',
        coord, pname, param,
    )

  @overload(int, int, int)
  def glTexEnvi(self, target: int, pname: int, param: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexEnvi(GLenum
    target, GLenum pname, GLint param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glTexEnvi

    Parameters
    ----------

    target : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    param : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glTexEnvi(GLenum target,
    #      GLenum pname, GLint param)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility9glTexEnviEjji',
        target, pname, param,
    )

  @overload(int, int, float)
  def glTexEnvf(self, target: int, pname: int, param: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexEnvf(GLenum
    target, GLenum pname, GLfloat param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glTexEnvf

    Parameters
    ----------

    target : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    param : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glTexEnvf(GLenum target,
    #      GLenum pname, GLfloat param)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility9glTexEnvfEjjf',
        target, pname, param,
    )

  @overload(int)
  def glShadeModel(self, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glShadeModel(GLenum
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glShadeModel(GLenum mode)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility12glShadeModelEj',
        mode,
    )

  @overload(int, int, int)
  def glMateriali(self, face: int, pname: int, param: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glMateriali(GLenum
    face, GLenum pname, GLint param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    face : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    param : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glMateriali(GLenum face,
    #      GLenum pname, GLint param)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility11glMaterialiEjji',
        face, pname, param,
    )

  @overload(int, int, float)
  def glMaterialf(self, face: int, pname: int, param: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glMaterialf(GLenum
    face, GLenum pname, GLfloat param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    face : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    param : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glMaterialf(GLenum face,
    #      GLenum pname, GLfloat param)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility11glMaterialfEjjf',
        face, pname, param,
    )

  @overload(int, int)
  def glLineStipple(self, factor: int, pattern: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glLineStipple(GLint
    factor, GLushort pattern)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    factor : int
      Passed on as it is.

    pattern : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glLineStipple(GLint factor,
    #      GLushort pattern)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility13glLineStippleEit',
        factor, pattern,
    )

  @overload(int, int)
  def glLightModeli(self, pname: int, param: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glLightModeli(GLenum
    pname, GLint param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    pname : int
      Passed on as it is.

    param : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glLightModeli(GLenum pname,
    #      GLint param)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility13glLightModeliEji',
        pname, param,
    )

  @overload(int, float)
  def glLightModelf(self, pname: int, param: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glLightModelf(GLenum
    pname, GLfloat param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    pname : int
      Passed on as it is.

    param : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glLightModelf(GLenum pname,
    #      GLfloat param)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility13glLightModelfEjf',
        pname, param,
    )

  @overload(int, int, int)
  def glLighti(self, light: int, pname: int, param: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glLighti(GLenum
    light, GLenum pname, GLint param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glLighti

    Parameters
    ----------

    light : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    param : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glLighti(GLenum light, GLenum
    #      pname, GLint param)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility8glLightiEjji',
        light, pname, param,
    )

  @overload(int, int, float)
  def glLightf(self, light: int, pname: int, param: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glLightf(GLenum
    light, GLenum pname, GLfloat param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glLightf

    Parameters
    ----------

    light : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    param : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glLightf(GLenum light, GLenum
    #      pname, GLfloat param)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility8glLightfEjjf',
        light, pname, param,
    )

  @overload(int, int)
  def glFogi(self, pname: int, param: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glFogi(GLenum pname,
    GLint param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glFogi

    Parameters
    ----------

    pname : int
      Passed on as it is.

    param : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glFogi(GLenum pname, GLint
    #      param)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility6glFogiEji',
        pname, param,
    )

  @overload(int, float)
  def glFogf(self, pname: int, param: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glFogf(GLenum pname,
    GLfloat param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glFogf

    Parameters
    ----------

    pname : int
      Passed on as it is.

    param : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glFogf(GLenum pname, GLfloat
    #      param)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility6glFogfEjf',
        pname, param,
    )

  @overload(int, int)
  def glColorMaterial(self, face: int, mode: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glColorMaterial(GLenum face, GLenum
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    face : int
      Passed on as it is.

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glColorMaterial(GLenum face,
    #      GLenum mode)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility15glColorMaterialEjj',
        face, mode,
    )

  @overload(int, int, int, int)
  def glVertex4s(self, x: int, y: int, z: int, w: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertex4s(GLshort
    x, GLshort y, GLshort z, GLshort w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glVertex4s

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    z : int
      Passed on as it is.

    w : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glVertex4s(GLshort x, GLshort
    #      y, GLshort z, GLshort w)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility10glVertex4sEssss',
        x, y, z, w,
    )

  @overload(int, int, int, int)
  def glVertex4i(self, x: int, y: int, z: int, w: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertex4i(GLint x,
    GLint y, GLint z, GLint w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glVertex4i

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    z : int
      Passed on as it is.

    w : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glVertex4i(GLint x, GLint y,
    #      GLint z, GLint w)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility10glVertex4iEiiii',
        x, y, z, w,
    )

  @overload(float, float, float, float)
  def glVertex4f(self, x: float, y: float, z: float, w: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertex4f(GLfloat
    x, GLfloat y, GLfloat z, GLfloat w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glVertex4f

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.

    w : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glVertex4f(GLfloat x, GLfloat
    #      y, GLfloat z, GLfloat w)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility10glVertex4fEffff',
        x, y, z, w,
    )

  @overload(float, float, float, float)
  def glVertex4d(self, x: float, y: float, z: float, w: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertex4d(GLdouble
    x, GLdouble y, GLdouble z, GLdouble w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glVertex4d

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.

    w : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glVertex4d(GLdouble x,
    #      GLdouble y, GLdouble z, GLdouble w)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility10glVertex4dEdddd',
        x, y, z, w,
    )

  @overload(int, int, int)
  def glVertex3s(self, x: int, y: int, z: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertex3s(GLshort
    x, GLshort y, GLshort z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glVertex3s

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    z : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glVertex3s(GLshort x, GLshort
    #      y, GLshort z)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility10glVertex3sEsss',
        x, y, z,
    )

  @overload(int, int, int)
  def glVertex3i(self, x: int, y: int, z: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertex3i(GLint x,
    GLint y, GLint z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glVertex3i

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    z : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glVertex3i(GLint x, GLint y,
    #      GLint z)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility10glVertex3iEiii',
        x, y, z,
    )

  @overload(float, float, float)
  def glVertex3f(self, x: float, y: float, z: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertex3f(GLfloat
    x, GLfloat y, GLfloat z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glVertex3f

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glVertex3f(GLfloat x, GLfloat
    #      y, GLfloat z)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility10glVertex3fEfff',
        x, y, z,
    )

  @overload(float, float, float)
  def glVertex3d(self, x: float, y: float, z: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertex3d(GLdouble
    x, GLdouble y, GLdouble z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glVertex3d

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glVertex3d(GLdouble x,
    #      GLdouble y, GLdouble z)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility10glVertex3dEddd',
        x, y, z,
    )

  @overload(int, int)
  def glVertex2s(self, x: int, y: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertex2s(GLshort
    x, GLshort y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glVertex2s

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glVertex2s(GLshort x, GLshort
    #      y)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility10glVertex2sEss', x, y,
    )

  @overload(int, int)
  def glVertex2i(self, x: int, y: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertex2i(GLint x,
    GLint y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glVertex2i

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glVertex2i(GLint x, GLint y)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility10glVertex2iEii', x, y,
    )

  @overload(float, float)
  def glVertex2f(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertex2f(GLfloat
    x, GLfloat y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glVertex2f

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glVertex2f(GLfloat x, GLfloat
    #      y)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility10glVertex2fEff', x, y,
    )

  @overload(float, float)
  def glVertex2d(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertex2d(GLdouble
    x, GLdouble y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glVertex2d

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glVertex2d(GLdouble x,
    #      GLdouble y)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility10glVertex2dEdd', x, y,
    )

  @overload(int, int, int, int)
  def glTexCoord4s(self, s: int, t: int, r: int, q: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexCoord4s(GLshort
    s, GLshort t, GLshort r, GLshort q)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    s : int
      Passed on as it is.

    t : int
      Passed on as it is.

    r : int
      Passed on as it is.

    q : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glTexCoord4s(GLshort s,
    #      GLshort t, GLshort r, GLshort q)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility12glTexCoord4sEssss',
        s, t, r, q,
    )

  @overload(int, int, int, int)
  def glTexCoord4i(self, s: int, t: int, r: int, q: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexCoord4i(GLint
    s, GLint t, GLint r, GLint q)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    s : int
      Passed on as it is.

    t : int
      Passed on as it is.

    r : int
      Passed on as it is.

    q : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glTexCoord4i(GLint s, GLint
    #      t, GLint r, GLint q)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility12glTexCoord4iEiiii',
        s, t, r, q,
    )

  @overload(float, float, float, float)
  def glTexCoord4f(self, s: float, t: float, r: float, q: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexCoord4f(GLfloat
    s, GLfloat t, GLfloat r, GLfloat q)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    s : float
      Passed on as it is.

    t : float
      Passed on as it is.

    r : float
      Passed on as it is.

    q : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glTexCoord4f(GLfloat s,
    #      GLfloat t, GLfloat r, GLfloat q)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility12glTexCoord4fEffff',
        s, t, r, q,
    )

  @overload(float, float, float, float)
  def glTexCoord4d(self, s: float, t: float, r: float, q: float) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glTexCoord4d(GLdouble s, GLdouble t,
    GLdouble r, GLdouble q)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    s : float
      Passed on as it is.

    t : float
      Passed on as it is.

    r : float
      Passed on as it is.

    q : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glTexCoord4d(GLdouble s,
    #      GLdouble t, GLdouble r, GLdouble q)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility12glTexCoord4dEdddd',
        s, t, r, q,
    )

  @overload(int, int, int)
  def glTexCoord3s(self, s: int, t: int, r: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexCoord3s(GLshort
    s, GLshort t, GLshort r)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    s : int
      Passed on as it is.

    t : int
      Passed on as it is.

    r : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glTexCoord3s(GLshort s,
    #      GLshort t, GLshort r)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility12glTexCoord3sEsss',
        s, t, r,
    )

  @overload(int, int, int)
  def glTexCoord3i(self, s: int, t: int, r: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexCoord3i(GLint
    s, GLint t, GLint r)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    s : int
      Passed on as it is.

    t : int
      Passed on as it is.

    r : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glTexCoord3i(GLint s, GLint
    #      t, GLint r)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility12glTexCoord3iEiii',
        s, t, r,
    )

  @overload(float, float, float)
  def glTexCoord3f(self, s: float, t: float, r: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexCoord3f(GLfloat
    s, GLfloat t, GLfloat r)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    s : float
      Passed on as it is.

    t : float
      Passed on as it is.

    r : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glTexCoord3f(GLfloat s,
    #      GLfloat t, GLfloat r)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility12glTexCoord3fEfff',
        s, t, r,
    )

  @overload(float, float, float)
  def glTexCoord3d(self, s: float, t: float, r: float) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glTexCoord3d(GLdouble s, GLdouble t,
    GLdouble r)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    s : float
      Passed on as it is.

    t : float
      Passed on as it is.

    r : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glTexCoord3d(GLdouble s,
    #      GLdouble t, GLdouble r)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility12glTexCoord3dEddd',
        s, t, r,
    )

  @overload(int, int)
  def glTexCoord2s(self, s: int, t: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexCoord2s(GLshort
    s, GLshort t)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    s : int
      Passed on as it is.

    t : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glTexCoord2s(GLshort s,
    #      GLshort t)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility12glTexCoord2sEss',
        s, t,
    )

  @overload(int, int)
  def glTexCoord2i(self, s: int, t: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexCoord2i(GLint
    s, GLint t)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    s : int
      Passed on as it is.

    t : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glTexCoord2i(GLint s, GLint
    #      t)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility12glTexCoord2iEii',
        s, t,
    )

  @overload(float, float)
  def glTexCoord2f(self, s: float, t: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexCoord2f(GLfloat
    s, GLfloat t)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    s : float
      Passed on as it is.

    t : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glTexCoord2f(GLfloat s,
    #      GLfloat t)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility12glTexCoord2fEff',
        s, t,
    )

  @overload(float, float)
  def glTexCoord2d(self, s: float, t: float) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glTexCoord2d(GLdouble s, GLdouble
    t)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    s : float
      Passed on as it is.

    t : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glTexCoord2d(GLdouble s,
    #      GLdouble t)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility12glTexCoord2dEdd',
        s, t,
    )

  @overload(int)
  def glTexCoord1s(self, s: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexCoord1s(GLshort
    s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    s : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glTexCoord1s(GLshort s)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility12glTexCoord1sEs', s,
    )

  @overload(int)
  def glTexCoord1i(self, s: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexCoord1i(GLint
    s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    s : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glTexCoord1i(GLint s)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility12glTexCoord1iEi', s,
    )

  @overload(float)
  def glTexCoord1f(self, s: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexCoord1f(GLfloat
    s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    s : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glTexCoord1f(GLfloat s)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility12glTexCoord1fEf', s,
    )

  @overload(float)
  def glTexCoord1d(self, s: float) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glTexCoord1d(GLdouble s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    s : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glTexCoord1d(GLdouble s)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility12glTexCoord1dEd', s,
    )

  @overload(int, int, int, int)
  def glRects(self, x1: int, y1: int, x2: int, y2: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glRects(GLshort x1,
    GLshort y1, GLshort x2, GLshort y2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glRects

    Parameters
    ----------

    x1 : int
      Passed on as it is.

    y1 : int
      Passed on as it is.

    x2 : int
      Passed on as it is.

    y2 : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glRects(GLshort x1, GLshort
    #      y1, GLshort x2, GLshort y2)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility7glRectsEssss',
        x1, y1, x2, y2,
    )

  @overload(int, int, int, int)
  def glRecti(self, x1: int, y1: int, x2: int, y2: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glRecti(GLint x1,
    GLint y1, GLint x2, GLint y2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glRecti

    Parameters
    ----------

    x1 : int
      Passed on as it is.

    y1 : int
      Passed on as it is.

    x2 : int
      Passed on as it is.

    y2 : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glRecti(GLint x1, GLint y1,
    #      GLint x2, GLint y2)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility7glRectiEiiii',
        x1, y1, x2, y2,
    )

  @overload(float, float, float, float)
  def glRectf(self, x1: float, y1: float, x2: float, y2: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glRectf(GLfloat x1,
    GLfloat y1, GLfloat x2, GLfloat y2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glRectf

    Parameters
    ----------

    x1 : float
      Passed on as it is.

    y1 : float
      Passed on as it is.

    x2 : float
      Passed on as it is.

    y2 : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glRectf(GLfloat x1, GLfloat
    #      y1, GLfloat x2, GLfloat y2)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility7glRectfEffff',
        x1, y1, x2, y2,
    )

  @overload(float, float, float, float)
  def glRectd(self, x1: float, y1: float, x2: float, y2: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glRectd(GLdouble x1,
    GLdouble y1, GLdouble x2, GLdouble y2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glRectd

    Parameters
    ----------

    x1 : float
      Passed on as it is.

    y1 : float
      Passed on as it is.

    x2 : float
      Passed on as it is.

    y2 : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glRectd(GLdouble x1, GLdouble
    #      y1, GLdouble x2, GLdouble y2)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility7glRectdEdddd',
        x1, y1, x2, y2,
    )

  @overload(int, int, int, int)
  def glRasterPos4s(self, x: int, y: int, z: int, w: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glRasterPos4s(GLshort x, GLshort y,
    GLshort z, GLshort w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    z : int
      Passed on as it is.

    w : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glRasterPos4s(GLshort x,
    #      GLshort y, GLshort z, GLshort w)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility13glRasterPos4sEssss',
        x, y, z, w,
    )

  @overload(int, int, int, int)
  def glRasterPos4i(self, x: int, y: int, z: int, w: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glRasterPos4i(GLint
    x, GLint y, GLint z, GLint w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    z : int
      Passed on as it is.

    w : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glRasterPos4i(GLint x, GLint
    #      y, GLint z, GLint w)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility13glRasterPos4iEiiii',
        x, y, z, w,
    )

  @overload(float, float, float, float)
  def glRasterPos4f(self, x: float, y: float, z: float, w: float) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glRasterPos4f(GLfloat x, GLfloat y,
    GLfloat z, GLfloat w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.

    w : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glRasterPos4f(GLfloat x,
    #      GLfloat y, GLfloat z, GLfloat w)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility13glRasterPos4fEffff',
        x, y, z, w,
    )

  @overload(float, float, float, float)
  def glRasterPos4d(self, x: float, y: float, z: float, w: float) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glRasterPos4d(GLdouble x, GLdouble y,
    GLdouble z, GLdouble w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.

    w : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glRasterPos4d(GLdouble x,
    #      GLdouble y, GLdouble z, GLdouble w)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility13glRasterPos4dEdddd',
        x, y, z, w,
    )

  @overload(int, int, int)
  def glRasterPos3s(self, x: int, y: int, z: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glRasterPos3s(GLshort x, GLshort y,
    GLshort z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    z : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glRasterPos3s(GLshort x,
    #      GLshort y, GLshort z)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility13glRasterPos3sEsss',
        x, y, z,
    )

  @overload(int, int, int)
  def glRasterPos3i(self, x: int, y: int, z: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glRasterPos3i(GLint
    x, GLint y, GLint z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    z : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glRasterPos3i(GLint x, GLint
    #      y, GLint z)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility13glRasterPos3iEiii',
        x, y, z,
    )

  @overload(float, float, float)
  def glRasterPos3f(self, x: float, y: float, z: float) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glRasterPos3f(GLfloat x, GLfloat y,
    GLfloat z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glRasterPos3f(GLfloat x,
    #      GLfloat y, GLfloat z)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility13glRasterPos3fEfff',
        x, y, z,
    )

  @overload(float, float, float)
  def glRasterPos3d(self, x: float, y: float, z: float) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glRasterPos3d(GLdouble x, GLdouble y,
    GLdouble z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glRasterPos3d(GLdouble x,
    #      GLdouble y, GLdouble z)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility13glRasterPos3dEddd',
        x, y, z,
    )

  @overload(int, int)
  def glRasterPos2s(self, x: int, y: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glRasterPos2s(GLshort x, GLshort y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glRasterPos2s(GLshort x,
    #      GLshort y)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility13glRasterPos2sEss',
        x, y,
    )

  @overload(int, int)
  def glRasterPos2i(self, x: int, y: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glRasterPos2i(GLint
    x, GLint y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glRasterPos2i(GLint x, GLint
    #      y)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility13glRasterPos2iEii',
        x, y,
    )

  @overload(float, float)
  def glRasterPos2f(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glRasterPos2f(GLfloat x, GLfloat y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glRasterPos2f(GLfloat x,
    #      GLfloat y)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility13glRasterPos2fEff',
        x, y,
    )

  @overload(float, float)
  def glRasterPos2d(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glRasterPos2d(GLdouble x, GLdouble
    y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glRasterPos2d(GLdouble x,
    #      GLdouble y)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility13glRasterPos2dEdd',
        x, y,
    )

  @overload(int, int, int)
  def glNormal3s(self, nx: int, ny: int, nz: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glNormal3s(GLshort
    nx, GLshort ny, GLshort nz)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glNormal3s

    Parameters
    ----------

    nx : int
      Passed on as it is.

    ny : int
      Passed on as it is.

    nz : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glNormal3s(GLshort nx,
    #      GLshort ny, GLshort nz)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility10glNormal3sEsss',
        nx, ny, nz,
    )

  @overload(int, int, int)
  def glNormal3i(self, nx: int, ny: int, nz: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glNormal3i(GLint nx,
    GLint ny, GLint nz)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glNormal3i

    Parameters
    ----------

    nx : int
      Passed on as it is.

    ny : int
      Passed on as it is.

    nz : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glNormal3i(GLint nx, GLint
    #      ny, GLint nz)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility10glNormal3iEiii',
        nx, ny, nz,
    )

  @overload(float, float, float)
  def glNormal3f(self, nx: float, ny: float, nz: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glNormal3f(GLfloat
    nx, GLfloat ny, GLfloat nz)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glNormal3f

    Parameters
    ----------

    nx : float
      Passed on as it is.

    ny : float
      Passed on as it is.

    nz : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glNormal3f(GLfloat nx,
    #      GLfloat ny, GLfloat nz)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility10glNormal3fEfff',
        nx, ny, nz,
    )

  @overload(float, float, float)
  def glNormal3d(self, nx: float, ny: float, nz: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glNormal3d(GLdouble
    nx, GLdouble ny, GLdouble nz)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glNormal3d

    Parameters
    ----------

    nx : float
      Passed on as it is.

    ny : float
      Passed on as it is.

    nz : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glNormal3d(GLdouble nx,
    #      GLdouble ny, GLdouble nz)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility10glNormal3dEddd',
        nx, ny, nz,
    )

  @overload(int, int, int)
  def glNormal3b(self, nx: int, ny: int, nz: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glNormal3b(GLbyte
    nx, GLbyte ny, GLbyte nz)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glNormal3b

    Parameters
    ----------

    nx : int
      Passed on as it is.

    ny : int
      Passed on as it is.

    nz : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glNormal3b(GLbyte nx, GLbyte
    #      ny, GLbyte nz)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility10glNormal3bEaaa',
        nx, ny, nz,
    )

  @overload(int)
  def glIndexs(self, c: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glIndexs(GLshort
    c)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glIndexs

    Parameters
    ----------

    c : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glIndexs(GLshort c)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility8glIndexsEs', c,
    )

  @overload(int)
  def glIndexi(self, c: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glIndexi(GLint c)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glIndexi

    Parameters
    ----------

    c : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glIndexi(GLint c)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility8glIndexiEi', c,
    )

  @overload(float)
  def glIndexf(self, c: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glIndexf(GLfloat
    c)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glIndexf

    Parameters
    ----------

    c : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glIndexf(GLfloat c)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility8glIndexfEf', c,
    )

  @overload(float)
  def glIndexd(self, c: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glIndexd(GLdouble
    c)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glIndexd

    Parameters
    ----------

    c : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glIndexd(GLdouble c)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility8glIndexdEd', c,
    )

  def glEnd(self) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glEnd()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glEnd
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glEnd()
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility5glEndEv',
    )

  @overload(int)
  def glEdgeFlag(self, flag: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glEdgeFlag(GLboolean
    flag)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glEdgeFlag

    Parameters
    ----------

    flag : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glEdgeFlag(GLboolean flag)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility10glEdgeFlagEh', flag,
    )

  @overload(int, int, int, int)
  def glColor4us(self, red: int, green: int, blue: int, alpha: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glColor4us(GLushort
    red, GLushort green, GLushort blue, GLushort alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glColor4us

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
    #  void QOpenGLFunctions_4_3_Compatibility::glColor4us(GLushort red,
    #      GLushort green, GLushort blue, GLushort alpha)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility10glColor4usEtttt',
        red, green, blue, alpha,
    )

  @overload(int, int, int, int)
  def glColor4ui(self, red: int, green: int, blue: int, alpha: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glColor4ui(GLuint
    red, GLuint green, GLuint blue, GLuint alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glColor4ui

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
    #  void QOpenGLFunctions_4_3_Compatibility::glColor4ui(GLuint red, GLuint
    #      green, GLuint blue, GLuint alpha)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility10glColor4uiEjjjj',
        red, green, blue, alpha,
    )

  @overload(int, int, int, int)
  def glColor4ub(self, red: int, green: int, blue: int, alpha: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glColor4ub(GLubyte
    red, GLubyte green, GLubyte blue, GLubyte alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glColor4ub

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
    #  void QOpenGLFunctions_4_3_Compatibility::glColor4ub(GLubyte red,
    #      GLubyte green, GLubyte blue, GLubyte alpha)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility10glColor4ubEhhhh',
        red, green, blue, alpha,
    )

  @overload(int, int, int, int)
  def glColor4s(self, red: int, green: int, blue: int, alpha: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glColor4s(GLshort
    red, GLshort green, GLshort blue, GLshort alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glColor4s

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
    #  void QOpenGLFunctions_4_3_Compatibility::glColor4s(GLshort red,
    #      GLshort green, GLshort blue, GLshort alpha)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility9glColor4sEssss',
        red, green, blue, alpha,
    )

  @overload(int, int, int, int)
  def glColor4i(self, red: int, green: int, blue: int, alpha: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glColor4i(GLint red,
    GLint green, GLint blue, GLint alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glColor4i

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
    #  void QOpenGLFunctions_4_3_Compatibility::glColor4i(GLint red, GLint
    #      green, GLint blue, GLint alpha)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility9glColor4iEiiii',
        red, green, blue, alpha,
    )

  @overload(float, float, float, float)
  def glColor4f(
      self,
      red: float,
      green: float,
      blue: float,
      alpha: float,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glColor4f(GLfloat
    red, GLfloat green, GLfloat blue, GLfloat alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glColor4f

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
    #  void QOpenGLFunctions_4_3_Compatibility::glColor4f(GLfloat red,
    #      GLfloat green, GLfloat blue, GLfloat alpha)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility9glColor4fEffff',
        red, green, blue, alpha,
    )

  @overload(float, float, float, float)
  def glColor4d(
      self,
      red: float,
      green: float,
      blue: float,
      alpha: float,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glColor4d(GLdouble
    red, GLdouble green, GLdouble blue, GLdouble alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glColor4d

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
    #  void QOpenGLFunctions_4_3_Compatibility::glColor4d(GLdouble red,
    #      GLdouble green, GLdouble blue, GLdouble alpha)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility9glColor4dEdddd',
        red, green, blue, alpha,
    )

  @overload(int, int, int, int)
  def glColor4b(self, red: int, green: int, blue: int, alpha: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glColor4b(GLbyte
    red, GLbyte green, GLbyte blue, GLbyte alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glColor4b

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
    #  void QOpenGLFunctions_4_3_Compatibility::glColor4b(GLbyte red, GLbyte
    #      green, GLbyte blue, GLbyte alpha)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility9glColor4bEaaaa',
        red, green, blue, alpha,
    )

  @overload(int, int, int)
  def glColor3us(self, red: int, green: int, blue: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glColor3us(GLushort
    red, GLushort green, GLushort blue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glColor3us

    Parameters
    ----------

    red : int
      Passed on as it is.

    green : int
      Passed on as it is.

    blue : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glColor3us(GLushort red,
    #      GLushort green, GLushort blue)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility10glColor3usEttt',
        red, green, blue,
    )

  @overload(int, int, int)
  def glColor3ui(self, red: int, green: int, blue: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glColor3ui(GLuint
    red, GLuint green, GLuint blue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glColor3ui

    Parameters
    ----------

    red : int
      Passed on as it is.

    green : int
      Passed on as it is.

    blue : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glColor3ui(GLuint red, GLuint
    #      green, GLuint blue)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility10glColor3uiEjjj',
        red, green, blue,
    )

  @overload(int, int, int)
  def glColor3ub(self, red: int, green: int, blue: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glColor3ub(GLubyte
    red, GLubyte green, GLubyte blue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glColor3ub

    Parameters
    ----------

    red : int
      Passed on as it is.

    green : int
      Passed on as it is.

    blue : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glColor3ub(GLubyte red,
    #      GLubyte green, GLubyte blue)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility10glColor3ubEhhh',
        red, green, blue,
    )

  @overload(int, int, int)
  def glColor3s(self, red: int, green: int, blue: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glColor3s(GLshort
    red, GLshort green, GLshort blue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glColor3s

    Parameters
    ----------

    red : int
      Passed on as it is.

    green : int
      Passed on as it is.

    blue : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glColor3s(GLshort red,
    #      GLshort green, GLshort blue)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility9glColor3sEsss',
        red, green, blue,
    )

  @overload(int, int, int)
  def glColor3i(self, red: int, green: int, blue: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glColor3i(GLint red,
    GLint green, GLint blue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glColor3i

    Parameters
    ----------

    red : int
      Passed on as it is.

    green : int
      Passed on as it is.

    blue : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glColor3i(GLint red, GLint
    #      green, GLint blue)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility9glColor3iEiii',
        red, green, blue,
    )

  @overload(float, float, float)
  def glColor3f(self, red: float, green: float, blue: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glColor3f(GLfloat
    red, GLfloat green, GLfloat blue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glColor3f

    Parameters
    ----------

    red : float
      Passed on as it is.

    green : float
      Passed on as it is.

    blue : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glColor3f(GLfloat red,
    #      GLfloat green, GLfloat blue)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility9glColor3fEfff',
        red, green, blue,
    )

  @overload(float, float, float)
  def glColor3d(self, red: float, green: float, blue: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glColor3d(GLdouble
    red, GLdouble green, GLdouble blue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glColor3d

    Parameters
    ----------

    red : float
      Passed on as it is.

    green : float
      Passed on as it is.

    blue : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glColor3d(GLdouble red,
    #      GLdouble green, GLdouble blue)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility9glColor3dEddd',
        red, green, blue,
    )

  @overload(int, int, int)
  def glColor3b(self, red: int, green: int, blue: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glColor3b(GLbyte
    red, GLbyte green, GLbyte blue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glColor3b

    Parameters
    ----------

    red : int
      Passed on as it is.

    green : int
      Passed on as it is.

    blue : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glColor3b(GLbyte red, GLbyte
    #      green, GLbyte blue)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility9glColor3bEaaa',
        red, green, blue,
    )

  @overload(int)
  def glBegin(self, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glBegin(GLenum
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glBegin

    Parameters
    ----------

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glBegin(GLenum mode)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility7glBeginEj', mode,
    )

  @overload(int)
  def glListBase(self, base: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glListBase(GLuint
    base)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glListBase

    Parameters
    ----------

    base : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glListBase(GLuint base)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility10glListBaseEj', base,
    )

  @overload(int)
  def glGenLists(self, range: int) -> int:
    """
    Calls Qt's 'GLuint QOpenGLFunctions_4_3_Compatibility::glGenLists(GLsizei
    range)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glGenLists

    Parameters
    ----------

    range : int
      Passed on as it is.
    """
    #  GLuint QOpenGLFunctions_4_3_Compatibility::glGenLists(GLsizei range)
    return self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility10glGenListsEi', range,
    )

  @overload(int, int)
  def glDeleteLists(self, list: int, range: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glDeleteLists(GLuint
    list, GLsizei range)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    list : int
      Passed on as it is.

    range : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glDeleteLists(GLuint list,
    #      GLsizei range)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility13glDeleteListsEji',
        list, range,
    )

  @overload(int)
  def glCallList(self, list: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glCallList(GLuint
    list)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glCallList

    Parameters
    ----------

    list : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glCallList(GLuint list)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility10glCallListEj', list,
    )

  def glEndList(self) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glEndList()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glEndList
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glEndList()
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility9glEndListEv',
    )

  @overload(int, int)
  def glNewList(self, list: int, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glNewList(GLuint
    list, GLenum mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glNewList

    Parameters
    ----------

    list : int
      Passed on as it is.

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glNewList(GLuint list, GLenum
    #      mode)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility9glNewListEjj',
        list, mode,
    )

  @overload(int)
  def glPushClientAttrib(self, mask: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glPushClientAttrib(GLbitfield mask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    mask : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glPushClientAttrib(GLbitfield
    #      mask)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility18glPushClientAttribE'
        'j',
        mask,
    )

  def glPopClientAttrib(self) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glPopClientAttrib()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glPopClientAttrib()
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility17glPopClientAttribEv',
    )

  @overload(int)
  def glEnableClientState(self, array: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glEnableClientState(GLenum array)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    array : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glEnableClientState(GLenum
    #      array)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility19glEnableClientState'
        'Ej',
        array,
    )

  @overload(int)
  def glDisableClientState(self, array: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glDisableClientState(GLenum array)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    array : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glDisableClientState(GLenum
    #      array)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility20glDisableClientStat'
        'eEj',
        array,
    )

  @overload(int)
  def glArrayElement(self, i: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glArrayElement(GLint
    i)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    i : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glArrayElement(GLint i)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility14glArrayElementEi', i,
    )

  @overload(int)
  def glResetMinmax(self, target: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glResetMinmax(GLenum
    target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    target : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glResetMinmax(GLenum target)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility13glResetMinmaxEj',
        target,
    )

  @overload(int)
  def glResetHistogram(self, target: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glResetHistogram(GLenum target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    target : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glResetHistogram(GLenum
    #      target)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility16glResetHistogramEj',
        target,
    )

  @overload(int, int, int)
  def glMinmax(self, target: int, internalformat: int, sink: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glMinmax(GLenum
    target, GLenum internalformat, GLboolean sink)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html#glMinmax

    Parameters
    ----------

    target : int
      Passed on as it is.

    internalformat : int
      Passed on as it is.

    sink : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glMinmax(GLenum target,
    #      GLenum internalformat, GLboolean sink)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility8glMinmaxEjjh',
        target, internalformat, sink,
    )

  @overload(int, int, int, int)
  def glHistogram(
      self,
      target: int,
      width: int,
      internalformat: int,
      sink: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glHistogram(GLenum
    target, GLsizei width, GLenum internalformat, GLboolean sink)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    target : int
      Passed on as it is.

    width : int
      Passed on as it is.

    internalformat : int
      Passed on as it is.

    sink : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glHistogram(GLenum target,
    #      GLsizei width, GLenum internalformat, GLboolean sink)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility11glHistogramEjijh',
        target, width, internalformat, sink,
    )

  @overload(int, int, int, int, int, int)
  def glCopyConvolutionFilter2D(
      self,
      target: int,
      internalformat: int,
      x: int,
      y: int,
      width: int,
      height: int,
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glCopyConvolutionFilter2D(GLenum
    target, GLenum internalformat, GLint x, GLint y, GLsizei width, GLsizei
    height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    target : int
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
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glCopyConvolutionFilter2D(
    #      GLenum target, GLenum internalformat, GLint x, GLint y, GLsizei
    #      width, GLsizei height)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility25glCopyConvolutionFi'
        'lter2DEjjiiii',
        target, internalformat, x, y, width, height,
    )

  @overload(int, int, int, int, int)
  def glCopyConvolutionFilter1D(
      self,
      target: int,
      internalformat: int,
      x: int,
      y: int,
      width: int,
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glCopyConvolutionFilter1D(GLenum
    target, GLenum internalformat, GLint x, GLint y, GLsizei width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    target : int
      Passed on as it is.

    internalformat : int
      Passed on as it is.

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    width : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glCopyConvolutionFilter1D(
    #      GLenum target, GLenum internalformat, GLint x, GLint y, GLsizei
    #      width)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility25glCopyConvolutionFi'
        'lter1DEjjiii',
        target, internalformat, x, y, width,
    )

  @overload(int, int, int)
  def glConvolutionParameteri(
      self,
      target: int,
      pname: int,
      params: int,
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glConvolutionParameteri(GLenum
    target, GLenum pname, GLint params)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    target : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    params : int
      Passed on as it is.
    """
    #  void
    #      QOpenGLFunctions_4_3_Compatibility::glConvolutionParameteri(GLenum
    #      target, GLenum pname, GLint params)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility23glConvolutionParame'
        'teriEjji',
        target, pname, params,
    )

  @overload(int, int, float)
  def glConvolutionParameterf(
      self,
      target: int,
      pname: int,
      params: float,
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glConvolutionParameterf(GLenum
    target, GLenum pname, GLfloat params)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    target : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    params : float
      Passed on as it is.
    """
    #  void
    #      QOpenGLFunctions_4_3_Compatibility::glConvolutionParameterf(GLenum
    #      target, GLenum pname, GLfloat params)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility23glConvolutionParame'
        'terfEjjf',
        target, pname, params,
    )

  @overload(int, int, int, int, int)
  def glCopyColorSubTable(
      self,
      target: int,
      start: int,
      x: int,
      y: int,
      width: int,
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glCopyColorSubTable(GLenum target,
    GLsizei start, GLint x, GLint y, GLsizei width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    target : int
      Passed on as it is.

    start : int
      Passed on as it is.

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    width : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glCopyColorSubTable(GLenum
    #      target, GLsizei start, GLint x, GLint y, GLsizei width)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility19glCopyColorSubTable'
        'Ejiiii',
        target, start, x, y, width,
    )

  @overload(int, int, int, int, int)
  def glCopyColorTable(
      self,
      target: int,
      internalformat: int,
      x: int,
      y: int,
      width: int,
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glCopyColorTable(GLenum target,
    GLenum internalformat, GLint x, GLint y, GLsizei width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    target : int
      Passed on as it is.

    internalformat : int
      Passed on as it is.

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    width : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glCopyColorTable(GLenum
    #      target, GLenum internalformat, GLint x, GLint y, GLsizei width)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility16glCopyColorTableEjj'
        'iii',
        target, internalformat, x, y, width,
    )

  @overload(int, int, int, int, int)
  def glMultiTexCoord4s(
      self,
      target: int,
      s: int,
      t: int,
      r: int,
      q: int,
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord4s(GLenum target,
    GLshort s, GLshort t, GLshort r, GLshort q)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    target : int
      Passed on as it is.

    s : int
      Passed on as it is.

    t : int
      Passed on as it is.

    r : int
      Passed on as it is.

    q : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord4s(GLenum
    #      target, GLshort s, GLshort t, GLshort r, GLshort q)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility17glMultiTexCoord4sEj'
        'ssss',
        target, s, t, r, q,
    )

  @overload(int, int, int, int, int)
  def glMultiTexCoord4i(
      self,
      target: int,
      s: int,
      t: int,
      r: int,
      q: int,
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord4i(GLenum target,
    GLint s, GLint t, GLint r, GLint q)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    target : int
      Passed on as it is.

    s : int
      Passed on as it is.

    t : int
      Passed on as it is.

    r : int
      Passed on as it is.

    q : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord4i(GLenum
    #      target, GLint s, GLint t, GLint r, GLint q)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility17glMultiTexCoord4iEj'
        'iiii',
        target, s, t, r, q,
    )

  @overload(int, float, float, float, float)
  def glMultiTexCoord4f(
      self,
      target: int,
      s: float,
      t: float,
      r: float,
      q: float,
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord4f(GLenum target,
    GLfloat s, GLfloat t, GLfloat r, GLfloat q)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    target : int
      Passed on as it is.

    s : float
      Passed on as it is.

    t : float
      Passed on as it is.

    r : float
      Passed on as it is.

    q : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord4f(GLenum
    #      target, GLfloat s, GLfloat t, GLfloat r, GLfloat q)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility17glMultiTexCoord4fEj'
        'ffff',
        target, s, t, r, q,
    )

  @overload(int, float, float, float, float)
  def glMultiTexCoord4d(
      self,
      target: int,
      s: float,
      t: float,
      r: float,
      q: float,
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord4d(GLenum target,
    GLdouble s, GLdouble t, GLdouble r, GLdouble q)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    target : int
      Passed on as it is.

    s : float
      Passed on as it is.

    t : float
      Passed on as it is.

    r : float
      Passed on as it is.

    q : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord4d(GLenum
    #      target, GLdouble s, GLdouble t, GLdouble r, GLdouble q)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility17glMultiTexCoord4dEj'
        'dddd',
        target, s, t, r, q,
    )

  @overload(int, int, int, int)
  def glMultiTexCoord3s(self, target: int, s: int, t: int, r: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord3s(GLenum target,
    GLshort s, GLshort t, GLshort r)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    target : int
      Passed on as it is.

    s : int
      Passed on as it is.

    t : int
      Passed on as it is.

    r : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord3s(GLenum
    #      target, GLshort s, GLshort t, GLshort r)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility17glMultiTexCoord3sEj'
        'sss',
        target, s, t, r,
    )

  @overload(int, int, int, int)
  def glMultiTexCoord3i(self, target: int, s: int, t: int, r: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord3i(GLenum target,
    GLint s, GLint t, GLint r)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    target : int
      Passed on as it is.

    s : int
      Passed on as it is.

    t : int
      Passed on as it is.

    r : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord3i(GLenum
    #      target, GLint s, GLint t, GLint r)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility17glMultiTexCoord3iEj'
        'iii',
        target, s, t, r,
    )

  @overload(int, float, float, float)
  def glMultiTexCoord3f(
      self,
      target: int,
      s: float,
      t: float,
      r: float,
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord3f(GLenum target,
    GLfloat s, GLfloat t, GLfloat r)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    target : int
      Passed on as it is.

    s : float
      Passed on as it is.

    t : float
      Passed on as it is.

    r : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord3f(GLenum
    #      target, GLfloat s, GLfloat t, GLfloat r)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility17glMultiTexCoord3fEj'
        'fff',
        target, s, t, r,
    )

  @overload(int, float, float, float)
  def glMultiTexCoord3d(
      self,
      target: int,
      s: float,
      t: float,
      r: float,
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord3d(GLenum target,
    GLdouble s, GLdouble t, GLdouble r)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    target : int
      Passed on as it is.

    s : float
      Passed on as it is.

    t : float
      Passed on as it is.

    r : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord3d(GLenum
    #      target, GLdouble s, GLdouble t, GLdouble r)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility17glMultiTexCoord3dEj'
        'ddd',
        target, s, t, r,
    )

  @overload(int, int, int)
  def glMultiTexCoord2s(self, target: int, s: int, t: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord2s(GLenum target,
    GLshort s, GLshort t)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    target : int
      Passed on as it is.

    s : int
      Passed on as it is.

    t : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord2s(GLenum
    #      target, GLshort s, GLshort t)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility17glMultiTexCoord2sEj'
        'ss',
        target, s, t,
    )

  @overload(int, int, int)
  def glMultiTexCoord2i(self, target: int, s: int, t: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord2i(GLenum target,
    GLint s, GLint t)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    target : int
      Passed on as it is.

    s : int
      Passed on as it is.

    t : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord2i(GLenum
    #      target, GLint s, GLint t)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility17glMultiTexCoord2iEj'
        'ii',
        target, s, t,
    )

  @overload(int, float, float)
  def glMultiTexCoord2f(self, target: int, s: float, t: float) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord2f(GLenum target,
    GLfloat s, GLfloat t)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    target : int
      Passed on as it is.

    s : float
      Passed on as it is.

    t : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord2f(GLenum
    #      target, GLfloat s, GLfloat t)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility17glMultiTexCoord2fEj'
        'ff',
        target, s, t,
    )

  @overload(int, float, float)
  def glMultiTexCoord2d(self, target: int, s: float, t: float) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord2d(GLenum target,
    GLdouble s, GLdouble t)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    target : int
      Passed on as it is.

    s : float
      Passed on as it is.

    t : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord2d(GLenum
    #      target, GLdouble s, GLdouble t)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility17glMultiTexCoord2dEj'
        'dd',
        target, s, t,
    )

  @overload(int, int)
  def glMultiTexCoord1s(self, target: int, s: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord1s(GLenum target,
    GLshort s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    target : int
      Passed on as it is.

    s : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord1s(GLenum
    #      target, GLshort s)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility17glMultiTexCoord1sEj'
        's',
        target, s,
    )

  @overload(int, int)
  def glMultiTexCoord1i(self, target: int, s: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord1i(GLenum target,
    GLint s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    target : int
      Passed on as it is.

    s : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord1i(GLenum
    #      target, GLint s)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility17glMultiTexCoord1iEj'
        'i',
        target, s,
    )

  @overload(int, float)
  def glMultiTexCoord1f(self, target: int, s: float) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord1f(GLenum target,
    GLfloat s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    target : int
      Passed on as it is.

    s : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord1f(GLenum
    #      target, GLfloat s)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility17glMultiTexCoord1fEj'
        'f',
        target, s,
    )

  @overload(int, float)
  def glMultiTexCoord1d(self, target: int, s: float) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord1d(GLenum target,
    GLdouble s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    target : int
      Passed on as it is.

    s : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord1d(GLenum
    #      target, GLdouble s)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility17glMultiTexCoord1dEj'
        'd',
        target, s,
    )

  @overload(int)
  def glClientActiveTexture(self, texture: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glClientActiveTexture(GLenum
    texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    texture : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glClientActiveTexture(GLenum
    #      texture)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility21glClientActiveTextu'
        'reEj',
        texture,
    )

  @overload(int, int, int)
  def glWindowPos3s(self, x: int, y: int, z: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glWindowPos3s(GLshort x, GLshort y,
    GLshort z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    z : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glWindowPos3s(GLshort x,
    #      GLshort y, GLshort z)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility13glWindowPos3sEsss',
        x, y, z,
    )

  @overload(int, int, int)
  def glWindowPos3i(self, x: int, y: int, z: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glWindowPos3i(GLint
    x, GLint y, GLint z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    z : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glWindowPos3i(GLint x, GLint
    #      y, GLint z)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility13glWindowPos3iEiii',
        x, y, z,
    )

  @overload(float, float, float)
  def glWindowPos3f(self, x: float, y: float, z: float) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glWindowPos3f(GLfloat x, GLfloat y,
    GLfloat z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glWindowPos3f(GLfloat x,
    #      GLfloat y, GLfloat z)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility13glWindowPos3fEfff',
        x, y, z,
    )

  @overload(float, float, float)
  def glWindowPos3d(self, x: float, y: float, z: float) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glWindowPos3d(GLdouble x, GLdouble y,
    GLdouble z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glWindowPos3d(GLdouble x,
    #      GLdouble y, GLdouble z)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility13glWindowPos3dEddd',
        x, y, z,
    )

  @overload(int, int)
  def glWindowPos2s(self, x: int, y: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glWindowPos2s(GLshort x, GLshort y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glWindowPos2s(GLshort x,
    #      GLshort y)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility13glWindowPos2sEss',
        x, y,
    )

  @overload(int, int)
  def glWindowPos2i(self, x: int, y: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glWindowPos2i(GLint
    x, GLint y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glWindowPos2i(GLint x, GLint
    #      y)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility13glWindowPos2iEii',
        x, y,
    )

  @overload(float, float)
  def glWindowPos2f(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glWindowPos2f(GLfloat x, GLfloat y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glWindowPos2f(GLfloat x,
    #      GLfloat y)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility13glWindowPos2fEff',
        x, y,
    )

  @overload(float, float)
  def glWindowPos2d(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glWindowPos2d(GLdouble x, GLdouble
    y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glWindowPos2d(GLdouble x,
    #      GLdouble y)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility13glWindowPos2dEdd',
        x, y,
    )

  @overload(int, int, int)
  def glSecondaryColor3us(self, red: int, green: int, blue: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glSecondaryColor3us(GLushort red,
    GLushort green, GLushort blue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    red : int
      Passed on as it is.

    green : int
      Passed on as it is.

    blue : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glSecondaryColor3us(GLushort
    #      red, GLushort green, GLushort blue)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility19glSecondaryColor3us'
        'Ettt',
        red, green, blue,
    )

  @overload(int, int, int)
  def glSecondaryColor3ui(self, red: int, green: int, blue: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glSecondaryColor3ui(GLuint red,
    GLuint green, GLuint blue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    red : int
      Passed on as it is.

    green : int
      Passed on as it is.

    blue : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glSecondaryColor3ui(GLuint
    #      red, GLuint green, GLuint blue)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility19glSecondaryColor3ui'
        'Ejjj',
        red, green, blue,
    )

  @overload(int, int, int)
  def glSecondaryColor3ub(self, red: int, green: int, blue: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glSecondaryColor3ub(GLubyte red,
    GLubyte green, GLubyte blue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    red : int
      Passed on as it is.

    green : int
      Passed on as it is.

    blue : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glSecondaryColor3ub(GLubyte
    #      red, GLubyte green, GLubyte blue)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility19glSecondaryColor3ub'
        'Ehhh',
        red, green, blue,
    )

  @overload(int, int, int)
  def glSecondaryColor3s(self, red: int, green: int, blue: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glSecondaryColor3s(GLshort red,
    GLshort green, GLshort blue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    red : int
      Passed on as it is.

    green : int
      Passed on as it is.

    blue : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glSecondaryColor3s(GLshort
    #      red, GLshort green, GLshort blue)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility18glSecondaryColor3sE'
        'sss',
        red, green, blue,
    )

  @overload(int, int, int)
  def glSecondaryColor3i(self, red: int, green: int, blue: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glSecondaryColor3i(GLint red, GLint
    green, GLint blue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    red : int
      Passed on as it is.

    green : int
      Passed on as it is.

    blue : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glSecondaryColor3i(GLint red,
    #      GLint green, GLint blue)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility18glSecondaryColor3iE'
        'iii',
        red, green, blue,
    )

  @overload(float, float, float)
  def glSecondaryColor3f(
      self,
      red: float,
      green: float,
      blue: float,
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glSecondaryColor3f(GLfloat red,
    GLfloat green, GLfloat blue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    red : float
      Passed on as it is.

    green : float
      Passed on as it is.

    blue : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glSecondaryColor3f(GLfloat
    #      red, GLfloat green, GLfloat blue)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility18glSecondaryColor3fE'
        'fff',
        red, green, blue,
    )

  @overload(float, float, float)
  def glSecondaryColor3d(
      self,
      red: float,
      green: float,
      blue: float,
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glSecondaryColor3d(GLdouble red,
    GLdouble green, GLdouble blue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    red : float
      Passed on as it is.

    green : float
      Passed on as it is.

    blue : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glSecondaryColor3d(GLdouble
    #      red, GLdouble green, GLdouble blue)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility18glSecondaryColor3dE'
        'ddd',
        red, green, blue,
    )

  @overload(int, int, int)
  def glSecondaryColor3b(self, red: int, green: int, blue: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glSecondaryColor3b(GLbyte red, GLbyte
    green, GLbyte blue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    red : int
      Passed on as it is.

    green : int
      Passed on as it is.

    blue : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glSecondaryColor3b(GLbyte
    #      red, GLbyte green, GLbyte blue)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility18glSecondaryColor3bE'
        'aaa',
        red, green, blue,
    )

  @overload(float)
  def glFogCoordd(self, coord: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glFogCoordd(GLdouble
    coord)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    coord : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glFogCoordd(GLdouble coord)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility11glFogCoorddEd',
        coord,
    )

  @overload(float)
  def glFogCoordf(self, coord: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_4_3_Compatibility::glFogCoordf(GLfloat
    coord)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    coord : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glFogCoordf(GLfloat coord)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility11glFogCoordfEf',
        coord,
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
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glVertexAttrib4s(GLuint index,
    GLshort x, GLshort y, GLshort z, GLshort w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glVertexAttrib4s(GLuint
    #      index, GLshort x, GLshort y, GLshort z, GLshort w)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility16glVertexAttrib4sEjs'
        'sss',
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
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glVertexAttrib4f(GLuint index,
    GLfloat x, GLfloat y, GLfloat z, GLfloat w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glVertexAttrib4f(GLuint
    #      index, GLfloat x, GLfloat y, GLfloat z, GLfloat w)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility16glVertexAttrib4fEjf'
        'fff',
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
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glVertexAttrib4d(GLuint index,
    GLdouble x, GLdouble y, GLdouble z, GLdouble w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glVertexAttrib4d(GLuint
    #      index, GLdouble x, GLdouble y, GLdouble z, GLdouble w)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility16glVertexAttrib4dEjd'
        'ddd',
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
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glVertexAttrib4Nub(GLuint index,
    GLubyte x, GLubyte y, GLubyte z, GLubyte w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glVertexAttrib4Nub(GLuint
    #      index, GLubyte x, GLubyte y, GLubyte z, GLubyte w)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility18glVertexAttrib4NubE'
        'jhhhh',
        index, x, y, z, w,
    )

  @overload(int, int, int, int)
  def glVertexAttrib3s(self, index: int, x: int, y: int, z: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glVertexAttrib3s(GLuint index,
    GLshort x, GLshort y, GLshort z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glVertexAttrib3s(GLuint
    #      index, GLshort x, GLshort y, GLshort z)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility16glVertexAttrib3sEjs'
        'ss',
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
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glVertexAttrib3f(GLuint index,
    GLfloat x, GLfloat y, GLfloat z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glVertexAttrib3f(GLuint
    #      index, GLfloat x, GLfloat y, GLfloat z)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility16glVertexAttrib3fEjf'
        'ff',
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
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glVertexAttrib3d(GLuint index,
    GLdouble x, GLdouble y, GLdouble z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glVertexAttrib3d(GLuint
    #      index, GLdouble x, GLdouble y, GLdouble z)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility16glVertexAttrib3dEjd'
        'dd',
        index, x, y, z,
    )

  @overload(int, int, int)
  def glVertexAttrib2s(self, index: int, x: int, y: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glVertexAttrib2s(GLuint index,
    GLshort x, GLshort y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    index : int
      Passed on as it is.

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glVertexAttrib2s(GLuint
    #      index, GLshort x, GLshort y)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility16glVertexAttrib2sEjs'
        's',
        index, x, y,
    )

  @overload(int, float, float)
  def glVertexAttrib2f(self, index: int, x: float, y: float) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glVertexAttrib2f(GLuint index,
    GLfloat x, GLfloat y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    index : int
      Passed on as it is.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glVertexAttrib2f(GLuint
    #      index, GLfloat x, GLfloat y)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility16glVertexAttrib2fEjf'
        'f',
        index, x, y,
    )

  @overload(int, float, float)
  def glVertexAttrib2d(self, index: int, x: float, y: float) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glVertexAttrib2d(GLuint index,
    GLdouble x, GLdouble y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    index : int
      Passed on as it is.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glVertexAttrib2d(GLuint
    #      index, GLdouble x, GLdouble y)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility16glVertexAttrib2dEjd'
        'd',
        index, x, y,
    )

  @overload(int, int)
  def glVertexAttrib1s(self, index: int, x: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glVertexAttrib1s(GLuint index,
    GLshort x)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    index : int
      Passed on as it is.

    x : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glVertexAttrib1s(GLuint
    #      index, GLshort x)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility16glVertexAttrib1sEjs',
        index, x,
    )

  @overload(int, float)
  def glVertexAttrib1f(self, index: int, x: float) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glVertexAttrib1f(GLuint index,
    GLfloat x)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    index : int
      Passed on as it is.

    x : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glVertexAttrib1f(GLuint
    #      index, GLfloat x)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility16glVertexAttrib1fEjf',
        index, x,
    )

  @overload(int, float)
  def glVertexAttrib1d(self, index: int, x: float) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glVertexAttrib1d(GLuint index,
    GLdouble x)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    index : int
      Passed on as it is.

    x : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glVertexAttrib1d(GLuint
    #      index, GLdouble x)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility16glVertexAttrib1dEjd',
        index, x,
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
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glVertexAttribI4ui(GLuint index,
    GLuint x, GLuint y, GLuint z, GLuint w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glVertexAttribI4ui(GLuint
    #      index, GLuint x, GLuint y, GLuint z, GLuint w)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility18glVertexAttribI4uiE'
        'jjjjj',
        index, x, y, z, w,
    )

  @overload(int, int, int, int)
  def glVertexAttribI3ui(self, index: int, x: int, y: int, z: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glVertexAttribI3ui(GLuint index,
    GLuint x, GLuint y, GLuint z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glVertexAttribI3ui(GLuint
    #      index, GLuint x, GLuint y, GLuint z)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility18glVertexAttribI3uiE'
        'jjjj',
        index, x, y, z,
    )

  @overload(int, int, int)
  def glVertexAttribI2ui(self, index: int, x: int, y: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glVertexAttribI2ui(GLuint index,
    GLuint x, GLuint y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    index : int
      Passed on as it is.

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glVertexAttribI2ui(GLuint
    #      index, GLuint x, GLuint y)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility18glVertexAttribI2uiE'
        'jjj',
        index, x, y,
    )

  @overload(int, int)
  def glVertexAttribI1ui(self, index: int, x: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glVertexAttribI1ui(GLuint index,
    GLuint x)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    index : int
      Passed on as it is.

    x : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glVertexAttribI1ui(GLuint
    #      index, GLuint x)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility18glVertexAttribI1uiE'
        'jj',
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
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glVertexAttribI4i(GLuint index, GLint
    x, GLint y, GLint z, GLint w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glVertexAttribI4i(GLuint
    #      index, GLint x, GLint y, GLint z, GLint w)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility17glVertexAttribI4iEj'
        'iiii',
        index, x, y, z, w,
    )

  @overload(int, int, int, int)
  def glVertexAttribI3i(self, index: int, x: int, y: int, z: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glVertexAttribI3i(GLuint index, GLint
    x, GLint y, GLint z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

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
    #  void QOpenGLFunctions_4_3_Compatibility::glVertexAttribI3i(GLuint
    #      index, GLint x, GLint y, GLint z)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility17glVertexAttribI3iEj'
        'iii',
        index, x, y, z,
    )

  @overload(int, int, int)
  def glVertexAttribI2i(self, index: int, x: int, y: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glVertexAttribI2i(GLuint index, GLint
    x, GLint y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    index : int
      Passed on as it is.

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glVertexAttribI2i(GLuint
    #      index, GLint x, GLint y)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility17glVertexAttribI2iEj'
        'ii',
        index, x, y,
    )

  @overload(int, int)
  def glVertexAttribI1i(self, index: int, x: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glVertexAttribI1i(GLuint index, GLint
    x)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_3_compatibility.html

    Parameters
    ----------

    index : int
      Passed on as it is.

    x : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_4_3_Compatibility::glVertexAttribI1i(GLuint
    #      index, GLint x)
    self.uglySide.call(
        'ritual_ZN34QOpenGLFunctions_4_3_Compatibility17glVertexAttribI1iEj'
        'i',
        index, x,
    )

  @staticmethod
  def glAreTexturesResident(*__, **_) -> Never:
    """
    Qt's 'GLboolean
    QOpenGLFunctions_4_3_Compatibility::glAreTexturesResident(GLsizei n,
    const GLuint *textures, GLboolean *residences)': names 'GLuint', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glAreTexturesResident' has no "
        "cute function yet. Qt's 'GLboolean "
        "QOpenGLFunctions_4_3_Compatibility::glAreTexturesResident(GLsizei "
        "n, const GLuint *textures, GLboolean *residences)': names "
        "'GLuint', which has no cute class yet.")

  @staticmethod
  def glBindAttribLocation(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glBindAttribLocation(GLuint program,
    GLuint index, const GLchar *name)': names 'GLchar', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glBindAttribLocation' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glBindAttribLocation(GLuint "
        "program, GLuint index, const GLchar *name)': names 'GLchar', which "
        "has no cute class yet.")

  @staticmethod
  def glBindFragDataLocation(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glBindFragDataLocation(GLuint
    program, GLuint color, const GLchar *name)': names 'GLchar', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glBindFragDataLocation' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glBindFragDataLocation(GLuint "
        "program, GLuint color, const GLchar *name)': names 'GLchar', which "
        "has no cute class yet.")

  @staticmethod
  def glBindFragDataLocationIndexed(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glBindFragDataLocationIndexed(GLuint
    program, GLuint colorNumber, GLuint index, const GLchar *name)': names
    'GLchar', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glBindFragDataLocationIndexed' "
        "has no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glBindFragDataLocationIndexed(G"
        "Luint program, GLuint colorNumber, GLuint index, const GLchar "
        "*name)': names 'GLchar', which has no cute class yet.")

  @staticmethod
  def glBitmap(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glBitmap(GLsizei width,
    GLsizei height, GLfloat xorig, GLfloat yorig, GLfloat xmove, GLfloat
    ymove, const GLubyte *bitmap)': names 'GLubyte', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glBitmap' has no cute function "
        "yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glBitmap(GLsizei width, "
        "GLsizei height, GLfloat xorig, GLfloat yorig, GLfloat xmove, "
        "GLfloat ymove, const GLubyte *bitmap)': names 'GLubyte', which has "
        "no cute class yet.")

  @staticmethod
  def glBufferData(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glBufferData(GLenum
    target, GLsizeiptr size, const GLvoid *data, GLenum usage)': names
    'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glBufferData' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glBufferData(GLenum target, "
        "GLsizeiptr size, const GLvoid *data, GLenum usage)': names "
        "'GLvoid', which has no cute class yet.")

  @staticmethod
  def glBufferSubData(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glBufferSubData(GLenum
    target, GLintptr offset, GLsizeiptr size, const GLvoid *data)': names
    'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glBufferSubData' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glBufferSubData(GLenum target, "
        "GLintptr offset, GLsizeiptr size, const GLvoid *data)': names "
        "'GLvoid', which has no cute class yet.")

  @staticmethod
  def glCallLists(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glCallLists(GLsizei n,
    GLenum type, const GLvoid *lists)': names 'GLvoid', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glCallLists' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glCallLists(GLsizei n, GLenum "
        "type, const GLvoid *lists)': names 'GLvoid', which has no cute "
        "class yet.")

  @staticmethod
  def glClearBufferData(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glClearBufferData(GLenum
    target, GLenum internalformat, GLenum format, GLenum type, const void
    *data)': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glClearBufferData' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glClearBufferData(GLenum "
        "target, GLenum internalformat, GLenum format, GLenum type, const "
        "void *data)': names 'void', which has no cute class yet.")

  @staticmethod
  def glClearBufferSubData(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glClearBufferSubData(GLenum target,
    GLenum internalformat, GLintptr offset, GLsizeiptr size, GLenum format,
    GLenum type, const void *data)': names 'void', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glClearBufferSubData' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glClearBufferSubData(GLenum "
        "target, GLenum internalformat, GLintptr offset, GLsizeiptr size, "
        "GLenum format, GLenum type, const void *data)': names 'void', "
        "which has no cute class yet.")

  @staticmethod
  def glClearBufferfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glClearBufferfv(GLenum
    buffer, GLint drawbuffer, const GLfloat *value)': names 'GLfloat', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glClearBufferfv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glClearBufferfv(GLenum buffer, "
        "GLint drawbuffer, const GLfloat *value)': names 'GLfloat', which "
        "has no cute class yet.")

  @staticmethod
  def glClearBufferiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glClearBufferiv(GLenum
    buffer, GLint drawbuffer, const GLint *value)': names 'GLint', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glClearBufferiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glClearBufferiv(GLenum buffer, "
        "GLint drawbuffer, const GLint *value)': names 'GLint', which has "
        "no cute class yet.")

  @staticmethod
  def glClearBufferuiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glClearBufferuiv(GLenum
    buffer, GLint drawbuffer, const GLuint *value)': names 'GLuint', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glClearBufferuiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glClearBufferuiv(GLenum "
        "buffer, GLint drawbuffer, const GLuint *value)': names 'GLuint', "
        "which has no cute class yet.")

  @staticmethod
  def glClientWaitSync(*__, **_) -> Never:
    """
    Qt's 'GLenum QOpenGLFunctions_4_3_Compatibility::glClientWaitSync(GLsync
    sync, GLbitfield flags, GLuint64 timeout)': names 'struct __GLsync',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glClientWaitSync' has no cute "
        "function yet. Qt's 'GLenum "
        "QOpenGLFunctions_4_3_Compatibility::glClientWaitSync(GLsync sync, "
        "GLbitfield flags, GLuint64 timeout)': names 'struct __GLsync', "
        "which has no cute class yet.")

  @staticmethod
  def glClipPlane(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glClipPlane(GLenum plane,
    const GLdouble *equation)': names 'GLdouble', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glClipPlane' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glClipPlane(GLenum plane, "
        "const GLdouble *equation)': names 'GLdouble', which has no cute "
        "class yet.")

  @staticmethod
  def glColor3bv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glColor3bv(const GLbyte
    *v)': names 'GLbyte', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glColor3bv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glColor3bv(const GLbyte *v)': "
        "names 'GLbyte', which has no cute class yet.")

  @staticmethod
  def glColor3dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glColor3dv(const GLdouble
    *v)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glColor3dv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glColor3dv(const GLdouble "
        "*v)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glColor3fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glColor3fv(const GLfloat
    *v)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glColor3fv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glColor3fv(const GLfloat *v)': "
        "names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glColor3iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glColor3iv(const GLint
    *v)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glColor3iv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glColor3iv(const GLint *v)': "
        "names 'GLint', which has no cute class yet.")

  @staticmethod
  def glColor3sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glColor3sv(const GLshort
    *v)': names 'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glColor3sv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glColor3sv(const GLshort *v)': "
        "names 'GLshort', which has no cute class yet.")

  @staticmethod
  def glColor3ubv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glColor3ubv(const GLubyte
    *v)': names 'GLubyte', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glColor3ubv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glColor3ubv(const GLubyte "
        "*v)': names 'GLubyte', which has no cute class yet.")

  @staticmethod
  def glColor3uiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glColor3uiv(const GLuint
    *v)': names 'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glColor3uiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glColor3uiv(const GLuint *v)': "
        "names 'GLuint', which has no cute class yet.")

  @staticmethod
  def glColor3usv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glColor3usv(const GLushort
    *v)': names 'GLushort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glColor3usv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glColor3usv(const GLushort "
        "*v)': names 'GLushort', which has no cute class yet.")

  @staticmethod
  def glColor4bv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glColor4bv(const GLbyte
    *v)': names 'GLbyte', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glColor4bv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glColor4bv(const GLbyte *v)': "
        "names 'GLbyte', which has no cute class yet.")

  @staticmethod
  def glColor4dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glColor4dv(const GLdouble
    *v)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glColor4dv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glColor4dv(const GLdouble "
        "*v)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glColor4fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glColor4fv(const GLfloat
    *v)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glColor4fv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glColor4fv(const GLfloat *v)': "
        "names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glColor4iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glColor4iv(const GLint
    *v)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glColor4iv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glColor4iv(const GLint *v)': "
        "names 'GLint', which has no cute class yet.")

  @staticmethod
  def glColor4sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glColor4sv(const GLshort
    *v)': names 'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glColor4sv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glColor4sv(const GLshort *v)': "
        "names 'GLshort', which has no cute class yet.")

  @staticmethod
  def glColor4ubv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glColor4ubv(const GLubyte
    *v)': names 'GLubyte', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glColor4ubv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glColor4ubv(const GLubyte "
        "*v)': names 'GLubyte', which has no cute class yet.")

  @staticmethod
  def glColor4uiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glColor4uiv(const GLuint
    *v)': names 'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glColor4uiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glColor4uiv(const GLuint *v)': "
        "names 'GLuint', which has no cute class yet.")

  @staticmethod
  def glColor4usv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glColor4usv(const GLushort
    *v)': names 'GLushort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glColor4usv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glColor4usv(const GLushort "
        "*v)': names 'GLushort', which has no cute class yet.")

  @staticmethod
  def glColorP3uiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glColorP3uiv(GLenum type,
    const GLuint *color)': names 'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glColorP3uiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glColorP3uiv(GLenum type, "
        "const GLuint *color)': names 'GLuint', which has no cute class yet."
    )

  @staticmethod
  def glColorP4uiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glColorP4uiv(GLenum type,
    const GLuint *color)': names 'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glColorP4uiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glColorP4uiv(GLenum type, "
        "const GLuint *color)': names 'GLuint', which has no cute class yet."
    )

  @staticmethod
  def glColorPointer(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glColorPointer(GLint size,
    GLenum type, GLsizei stride, const GLvoid *pointer)': names 'GLvoid',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glColorPointer' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glColorPointer(GLint size, "
        "GLenum type, GLsizei stride, const GLvoid *pointer)': names "
        "'GLvoid', which has no cute class yet.")

  @staticmethod
  def glColorSubTable(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glColorSubTable(GLenum
    target, GLsizei start, GLsizei count, GLenum format, GLenum type, const
    GLvoid *data)': names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glColorSubTable' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glColorSubTable(GLenum target, "
        "GLsizei start, GLsizei count, GLenum format, GLenum type, const "
        "GLvoid *data)': names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glColorTable(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glColorTable(GLenum
    target, GLenum internalformat, GLsizei width, GLenum format, GLenum type,
    const GLvoid *table)': names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glColorTable' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glColorTable(GLenum target, "
        "GLenum internalformat, GLsizei width, GLenum format, GLenum type, "
        "const GLvoid *table)': names 'GLvoid', which has no cute class yet."
    )

  @staticmethod
  def glColorTableParameterfv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glColorTableParameterfv(GLenum
    target, GLenum pname, const GLfloat *params)': names 'GLfloat', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glColorTableParameterfv' has "
        "no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glColorTableParameterfv(GLenum "
        "target, GLenum pname, const GLfloat *params)': names 'GLfloat', "
        "which has no cute class yet.")

  @staticmethod
  def glColorTableParameteriv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glColorTableParameteriv(GLenum
    target, GLenum pname, const GLint *params)': names 'GLint', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glColorTableParameteriv' has "
        "no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glColorTableParameteriv(GLenum "
        "target, GLenum pname, const GLint *params)': names 'GLint', which "
        "has no cute class yet.")

  @staticmethod
  def glCompressedTexImage1D(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glCompressedTexImage1D(GLenum target,
    GLint level, GLenum internalformat, GLsizei width, GLint border, GLsizei
    imageSize, const GLvoid *data)': names 'GLvoid', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glCompressedTexImage1D' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glCompressedTexImage1D(GLenum "
        "target, GLint level, GLenum internalformat, GLsizei width, GLint "
        "border, GLsizei imageSize, const GLvoid *data)': names 'GLvoid', "
        "which has no cute class yet.")

  @staticmethod
  def glCompressedTexImage2D(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glCompressedTexImage2D(GLenum target,
    GLint level, GLenum internalformat, GLsizei width, GLsizei height, GLint
    border, GLsizei imageSize, const GLvoid *data)': names 'GLvoid', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glCompressedTexImage2D' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glCompressedTexImage2D(GLenum "
        "target, GLint level, GLenum internalformat, GLsizei width, GLsizei "
        "height, GLint border, GLsizei imageSize, const GLvoid *data)': "
        "names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glCompressedTexImage3D(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glCompressedTexImage3D(GLenum target,
    GLint level, GLenum internalformat, GLsizei width, GLsizei height,
    GLsizei depth, GLint border, GLsizei imageSize, const GLvoid *data)':
    names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glCompressedTexImage3D' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glCompressedTexImage3D(GLenum "
        "target, GLint level, GLenum internalformat, GLsizei width, GLsizei "
        "height, GLsizei depth, GLint border, GLsizei imageSize, const "
        "GLvoid *data)': names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glCompressedTexSubImage1D(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glCompressedTexSubImage1D(GLenum
    target, GLint level, GLint xoffset, GLsizei width, GLenum format, GLsizei
    imageSize, const GLvoid *data)': names 'GLvoid', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glCompressedTexSubImage1D' has "
        "no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glCompressedTexSubImage1D(GLenu"
        "m target, GLint level, GLint xoffset, GLsizei width, GLenum "
        "format, GLsizei imageSize, const GLvoid *data)': names 'GLvoid', "
        "which has no cute class yet.")

  @staticmethod
  def glCompressedTexSubImage2D(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glCompressedTexSubImage2D(GLenum
    target, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei
    height, GLenum format, GLsizei imageSize, const GLvoid *data)': names
    'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glCompressedTexSubImage2D' has "
        "no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glCompressedTexSubImage2D(GLenu"
        "m target, GLint level, GLint xoffset, GLint yoffset, GLsizei "
        "width, GLsizei height, GLenum format, GLsizei imageSize, const "
        "GLvoid *data)': names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glCompressedTexSubImage3D(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glCompressedTexSubImage3D(GLenum
    target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei
    width, GLsizei height, GLsizei depth, GLenum format, GLsizei imageSize,
    const GLvoid *data)': names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glCompressedTexSubImage3D' has "
        "no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glCompressedTexSubImage3D(GLenu"
        "m target, GLint level, GLint xoffset, GLint yoffset, GLint "
        "zoffset, GLsizei width, GLsizei height, GLsizei depth, GLenum "
        "format, GLsizei imageSize, const GLvoid *data)': names 'GLvoid', "
        "which has no cute class yet.")

  @staticmethod
  def glConvolutionFilter1D(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glConvolutionFilter1D(GLenum target,
    GLenum internalformat, GLsizei width, GLenum format, GLenum type, const
    GLvoid *image)': names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glConvolutionFilter1D' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glConvolutionFilter1D(GLenum "
        "target, GLenum internalformat, GLsizei width, GLenum format, "
        "GLenum type, const GLvoid *image)': names 'GLvoid', which has no "
        "cute class yet.")

  @staticmethod
  def glConvolutionFilter2D(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glConvolutionFilter2D(GLenum target,
    GLenum internalformat, GLsizei width, GLsizei height, GLenum format,
    GLenum type, const GLvoid *image)': names 'GLvoid', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glConvolutionFilter2D' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glConvolutionFilter2D(GLenum "
        "target, GLenum internalformat, GLsizei width, GLsizei height, "
        "GLenum format, GLenum type, const GLvoid *image)': names 'GLvoid', "
        "which has no cute class yet.")

  @staticmethod
  def glConvolutionParameterfv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glConvolutionParameterfv(GLenum
    target, GLenum pname, const GLfloat *params)': names 'GLfloat', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glConvolutionParameterfv' has "
        "no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glConvolutionParameterfv(GLenum"
        " target, GLenum pname, const GLfloat *params)': names 'GLfloat', "
        "which has no cute class yet.")

  @staticmethod
  def glConvolutionParameteriv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glConvolutionParameteriv(GLenum
    target, GLenum pname, const GLint *params)': names 'GLint', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glConvolutionParameteriv' has "
        "no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glConvolutionParameteriv(GLenum"
        " target, GLenum pname, const GLint *params)': names 'GLint', which "
        "has no cute class yet.")

  @staticmethod
  def glCreateShaderProgramv(*__, **_) -> Never:
    """
    Qt's 'GLuint
    QOpenGLFunctions_4_3_Compatibility::glCreateShaderProgramv(GLenum type,
    GLsizei count, const GLchar *const *strings)': names 'GLchar *const',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glCreateShaderProgramv' has no "
        "cute function yet. Qt's 'GLuint "
        "QOpenGLFunctions_4_3_Compatibility::glCreateShaderProgramv(GLenum "
        "type, GLsizei count, const GLchar *const *strings)': names 'GLchar "
        "*const', which has no cute class yet.")

  @staticmethod
  def glDeleteBuffers(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glDeleteBuffers(GLsizei n,
    const GLuint *buffers)': names 'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glDeleteBuffers' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glDeleteBuffers(GLsizei n, "
        "const GLuint *buffers)': names 'GLuint', which has no cute class "
        "yet.")

  @staticmethod
  def glDeleteFramebuffers(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glDeleteFramebuffers(GLsizei n, const
    GLuint *framebuffers)': names 'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glDeleteFramebuffers' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glDeleteFramebuffers(GLsizei "
        "n, const GLuint *framebuffers)': names 'GLuint', which has no cute "
        "class yet.")

  @staticmethod
  def glDeleteProgramPipelines(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glDeleteProgramPipelines(GLsizei n,
    const GLuint *pipelines)': names 'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glDeleteProgramPipelines' has "
        "no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glDeleteProgramPipelines(GLsize"
        "i n, const GLuint *pipelines)': names 'GLuint', which has no cute "
        "class yet.")

  @staticmethod
  def glDeleteQueries(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glDeleteQueries(GLsizei n,
    const GLuint *ids)': names 'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glDeleteQueries' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glDeleteQueries(GLsizei n, "
        "const GLuint *ids)': names 'GLuint', which has no cute class yet.")

  @staticmethod
  def glDeleteRenderbuffers(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glDeleteRenderbuffers(GLsizei n,
    const GLuint *renderbuffers)': names 'GLuint', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glDeleteRenderbuffers' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glDeleteRenderbuffers(GLsizei "
        "n, const GLuint *renderbuffers)': names 'GLuint', which has no "
        "cute class yet.")

  @staticmethod
  def glDeleteSamplers(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glDeleteSamplers(GLsizei
    count, const GLuint *samplers)': names 'GLuint', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glDeleteSamplers' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glDeleteSamplers(GLsizei "
        "count, const GLuint *samplers)': names 'GLuint', which has no cute "
        "class yet.")

  @staticmethod
  def glDeleteSync(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glDeleteSync(GLsync
    sync)': names 'struct __GLsync', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glDeleteSync' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glDeleteSync(GLsync sync)': "
        "names 'struct __GLsync', which has no cute class yet.")

  @staticmethod
  def glDeleteTextures(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glDeleteTextures(GLsizei
    n, const GLuint *textures)': names 'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glDeleteTextures' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glDeleteTextures(GLsizei n, "
        "const GLuint *textures)': names 'GLuint', which has no cute class "
        "yet.")

  @staticmethod
  def glDeleteTransformFeedbacks(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glDeleteTransformFeedbacks(GLsizei n,
    const GLuint *ids)': names 'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glDeleteTransformFeedbacks' "
        "has no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glDeleteTransformFeedbacks(GLsi"
        "zei n, const GLuint *ids)': names 'GLuint', which has no cute "
        "class yet.")

  @staticmethod
  def glDeleteVertexArrays(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glDeleteVertexArrays(GLsizei n, const
    GLuint *arrays)': names 'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glDeleteVertexArrays' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glDeleteVertexArrays(GLsizei "
        "n, const GLuint *arrays)': names 'GLuint', which has no cute class "
        "yet.")

  @staticmethod
  def glDepthRangeArrayv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glDepthRangeArrayv(GLuint
    first, GLsizei count, const GLdouble *v)': names 'GLdouble', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glDepthRangeArrayv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glDepthRangeArrayv(GLuint "
        "first, GLsizei count, const GLdouble *v)': names 'GLdouble', which "
        "has no cute class yet.")

  @staticmethod
  def glDrawArraysIndirect(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glDrawArraysIndirect(GLenum mode,
    const GLvoid *indirect)': names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glDrawArraysIndirect' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glDrawArraysIndirect(GLenum "
        "mode, const GLvoid *indirect)': names 'GLvoid', which has no cute "
        "class yet.")

  @staticmethod
  def glDrawBuffers(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glDrawBuffers(GLsizei n,
    const GLenum *bufs)': names 'GLenum', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glDrawBuffers' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glDrawBuffers(GLsizei n, const "
        "GLenum *bufs)': names 'GLenum', which has no cute class yet.")

  @staticmethod
  def glDrawElements(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glDrawElements(GLenum
    mode, GLsizei count, GLenum type, const GLvoid *indices)': names
    'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glDrawElements' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glDrawElements(GLenum mode, "
        "GLsizei count, GLenum type, const GLvoid *indices)': names "
        "'GLvoid', which has no cute class yet.")

  @staticmethod
  def glDrawElementsBaseVertex(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glDrawElementsBaseVertex(GLenum mode,
    GLsizei count, GLenum type, const GLvoid *indices, GLint basevertex)':
    names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glDrawElementsBaseVertex' has "
        "no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glDrawElementsBaseVertex(GLenum"
        " mode, GLsizei count, GLenum type, const GLvoid *indices, GLint "
        "basevertex)': names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glDrawElementsIndirect(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glDrawElementsIndirect(GLenum mode,
    GLenum type, const GLvoid *indirect)': names 'GLvoid', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glDrawElementsIndirect' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glDrawElementsIndirect(GLenum "
        "mode, GLenum type, const GLvoid *indirect)': names 'GLvoid', which "
        "has no cute class yet.")

  @staticmethod
  def glDrawElementsInstanced(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glDrawElementsInstanced(GLenum mode,
    GLsizei count, GLenum type, const GLvoid *indices, GLsizei
    instancecount)': names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glDrawElementsInstanced' has "
        "no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glDrawElementsInstanced(GLenum "
        "mode, GLsizei count, GLenum type, const GLvoid *indices, GLsizei "
        "instancecount)': names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glDrawElementsInstancedBaseInstance(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glDrawElementsInstancedBaseInstance(
    GLenum mode, GLsizei count, GLenum type, const void *indices, GLsizei
    instancecount, GLuint baseinstance)': names 'void', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glDrawElementsInstancedBaseInst"
        "ance' has no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glDrawElementsInstancedBaseInst"
        "ance(GLenum mode, GLsizei count, GLenum type, const void *indices, "
        "GLsizei instancecount, GLuint baseinstance)': names 'void', which "
        "has no cute class yet.")

  @staticmethod
  def glDrawElementsInstancedBaseVertex(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glDrawElementsInstancedBaseVertex(
    GLenum mode, GLsizei count, GLenum type, const GLvoid *indices, GLsizei
    instancecount, GLint basevertex)': names 'GLvoid', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glDrawElementsInstancedBaseVert"
        "ex' has no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glDrawElementsInstancedBaseVert"
        "ex(GLenum mode, GLsizei count, GLenum type, const GLvoid *indices, "
        "GLsizei instancecount, GLint basevertex)': names 'GLvoid', which "
        "has no cute class yet.")

  @staticmethod
  def glDrawElementsInstancedBaseVertexBaseInstance(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::
    glDrawElementsInstancedBaseVertexBaseInstance(GLenum mode, GLsizei count,
    GLenum type, const void *indices, GLsizei instancecount, GLint
    basevertex, GLuint baseinstance)': names 'void', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glDrawElementsInstancedBaseVert"
        "exBaseInstance' has no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glDrawElementsInstancedBaseVert"
        "exBaseInstance(GLenum mode, GLsizei count, GLenum type, const void "
        "*indices, GLsizei instancecount, GLint basevertex, GLuint "
        "baseinstance)': names 'void', which has no cute class yet.")

  @staticmethod
  def glDrawPixels(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glDrawPixels(GLsizei
    width, GLsizei height, GLenum format, GLenum type, const GLvoid
    *pixels)': names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glDrawPixels' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glDrawPixels(GLsizei width, "
        "GLsizei height, GLenum format, GLenum type, const GLvoid "
        "*pixels)': names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glDrawRangeElements(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glDrawRangeElements(GLenum
    mode, GLuint start, GLuint end, GLsizei count, GLenum type, const GLvoid
    *indices)': names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glDrawRangeElements' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glDrawRangeElements(GLenum "
        "mode, GLuint start, GLuint end, GLsizei count, GLenum type, const "
        "GLvoid *indices)': names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glDrawRangeElementsBaseVertex(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glDrawRangeElementsBaseVertex(GLenum
    mode, GLuint start, GLuint end, GLsizei count, GLenum type, const GLvoid
    *indices, GLint basevertex)': names 'GLvoid', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glDrawRangeElementsBaseVertex' "
        "has no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glDrawRangeElementsBaseVertex(G"
        "Lenum mode, GLuint start, GLuint end, GLsizei count, GLenum type, "
        "const GLvoid *indices, GLint basevertex)': names 'GLvoid', which "
        "has no cute class yet.")

  @staticmethod
  def glEdgeFlagPointer(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glEdgeFlagPointer(GLsizei
    stride, const GLvoid *pointer)': names 'GLvoid', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glEdgeFlagPointer' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glEdgeFlagPointer(GLsizei "
        "stride, const GLvoid *pointer)': names 'GLvoid', which has no cute "
        "class yet.")

  @staticmethod
  def glEdgeFlagv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glEdgeFlagv(const
    GLboolean *flag)': names 'GLboolean', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glEdgeFlagv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glEdgeFlagv(const GLboolean "
        "*flag)': names 'GLboolean', which has no cute class yet.")

  @staticmethod
  def glEvalCoord1dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glEvalCoord1dv(const
    GLdouble *u)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glEvalCoord1dv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glEvalCoord1dv(const GLdouble "
        "*u)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glEvalCoord1fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glEvalCoord1fv(const
    GLfloat *u)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glEvalCoord1fv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glEvalCoord1fv(const GLfloat "
        "*u)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glEvalCoord2dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glEvalCoord2dv(const
    GLdouble *u)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glEvalCoord2dv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glEvalCoord2dv(const GLdouble "
        "*u)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glEvalCoord2fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glEvalCoord2fv(const
    GLfloat *u)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glEvalCoord2fv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glEvalCoord2fv(const GLfloat "
        "*u)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glFeedbackBuffer(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glFeedbackBuffer(GLsizei
    size, GLenum type, GLfloat *buffer)': takes a number to change where it
    is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glFeedbackBuffer' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glFeedbackBuffer(GLsizei size, "
        "GLenum type, GLfloat *buffer)': takes a number to change where it "
        "is.")

  @staticmethod
  def glFenceSync(*__, **_) -> Never:
    """
    Qt's 'GLsync QOpenGLFunctions_4_3_Compatibility::glFenceSync(GLenum
    condition, GLbitfield flags)': gives a type Python has no way to take
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glFenceSync' has no cute "
        "function yet. Qt's 'GLsync "
        "QOpenGLFunctions_4_3_Compatibility::glFenceSync(GLenum condition, "
        "GLbitfield flags)': gives a type Python has no way to take yet.")

  @staticmethod
  def glFogCoordPointer(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glFogCoordPointer(GLenum
    type, GLsizei stride, const GLvoid *pointer)': names 'GLvoid', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glFogCoordPointer' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glFogCoordPointer(GLenum type, "
        "GLsizei stride, const GLvoid *pointer)': names 'GLvoid', which has "
        "no cute class yet.")

  @staticmethod
  def glFogCoorddv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glFogCoorddv(const
    GLdouble *coord)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glFogCoorddv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glFogCoorddv(const GLdouble "
        "*coord)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glFogCoordfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glFogCoordfv(const GLfloat
    *coord)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glFogCoordfv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glFogCoordfv(const GLfloat "
        "*coord)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glFogfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glFogfv(GLenum pname,
    const GLfloat *params)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glFogfv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_3_Compatibility::glFogfv(GLenum "
        "pname, const GLfloat *params)': names 'GLfloat', which has no cute "
        "class yet.")

  @staticmethod
  def glFogiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glFogiv(GLenum pname,
    const GLint *params)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glFogiv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_3_Compatibility::glFogiv(GLenum "
        "pname, const GLint *params)': names 'GLint', which has no cute "
        "class yet.")

  @staticmethod
  def glGenBuffers(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGenBuffers(GLsizei n,
    GLuint *buffers)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGenBuffers' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGenBuffers(GLsizei n, GLuint "
        "*buffers)': takes a number to change where it is.")

  @staticmethod
  def glGenFramebuffers(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGenFramebuffers(GLsizei
    n, GLuint *framebuffers)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGenFramebuffers' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGenFramebuffers(GLsizei n, "
        "GLuint *framebuffers)': takes a number to change where it is.")

  @staticmethod
  def glGenProgramPipelines(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGenProgramPipelines(GLsizei n,
    GLuint *pipelines)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGenProgramPipelines' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGenProgramPipelines(GLsizei "
        "n, GLuint *pipelines)': takes a number to change where it is.")

  @staticmethod
  def glGenQueries(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGenQueries(GLsizei n,
    GLuint *ids)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGenQueries' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGenQueries(GLsizei n, GLuint "
        "*ids)': takes a number to change where it is.")

  @staticmethod
  def glGenRenderbuffers(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGenRenderbuffers(GLsizei
    n, GLuint *renderbuffers)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGenRenderbuffers' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGenRenderbuffers(GLsizei n, "
        "GLuint *renderbuffers)': takes a number to change where it is.")

  @staticmethod
  def glGenSamplers(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGenSamplers(GLsizei
    count, GLuint *samplers)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGenSamplers' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGenSamplers(GLsizei count, "
        "GLuint *samplers)': takes a number to change where it is.")

  @staticmethod
  def glGenTextures(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGenTextures(GLsizei n,
    GLuint *textures)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGenTextures' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGenTextures(GLsizei n, "
        "GLuint *textures)': takes a number to change where it is.")

  @staticmethod
  def glGenTransformFeedbacks(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGenTransformFeedbacks(GLsizei n,
    GLuint *ids)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGenTransformFeedbacks' has "
        "no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGenTransformFeedbacks(GLsizei"
        " n, GLuint *ids)': takes a number to change where it is.")

  @staticmethod
  def glGenVertexArrays(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGenVertexArrays(GLsizei
    n, GLuint *arrays)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGenVertexArrays' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGenVertexArrays(GLsizei n, "
        "GLuint *arrays)': takes a number to change where it is.")

  @staticmethod
  def glGetActiveAtomicCounterBufferiv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetActiveAtomicCounterBufferiv(
    GLuint program, GLuint bufferIndex, GLenum pname, GLint *params)': takes
    a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetActiveAtomicCounterBufferi"
        "v' has no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetActiveAtomicCounterBufferi"
        "v(GLuint program, GLuint bufferIndex, GLenum pname, GLint "
        "*params)': takes a number to change where it is.")

  @staticmethod
  def glGetActiveAttrib(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetActiveAttrib(GLuint
    program, GLuint index, GLsizei bufSize, GLsizei *length, GLint *size,
    GLenum *type, GLchar *name)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetActiveAttrib' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetActiveAttrib(GLuint "
        "program, GLuint index, GLsizei bufSize, GLsizei *length, GLint "
        "*size, GLenum *type, GLchar *name)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetActiveSubroutineName(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetActiveSubroutineName(GLuint
    program, GLenum shadertype, GLuint index, GLsizei bufsize, GLsizei
    *length, GLchar *name)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetActiveSubroutineName' has "
        "no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetActiveSubroutineName(GLuin"
        "t program, GLenum shadertype, GLuint index, GLsizei bufsize, "
        "GLsizei *length, GLchar *name)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetActiveSubroutineUniformName(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetActiveSubroutineUniformName(
    GLuint program, GLenum shadertype, GLuint index, GLsizei bufsize, GLsizei
    *length, GLchar *name)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetActiveSubroutineUniformNam"
        "e' has no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetActiveSubroutineUniformNam"
        "e(GLuint program, GLenum shadertype, GLuint index, GLsizei "
        "bufsize, GLsizei *length, GLchar *name)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetActiveSubroutineUniformiv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetActiveSubroutineUniformiv(GLuint
    program, GLenum shadertype, GLuint index, GLenum pname, GLint *values)':
    takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetActiveSubroutineUniformiv'"
        " has no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetActiveSubroutineUniformiv("
        "GLuint program, GLenum shadertype, GLuint index, GLenum pname, "
        "GLint *values)': takes a number to change where it is.")

  @staticmethod
  def glGetActiveUniform(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetActiveUniform(GLuint
    program, GLuint index, GLsizei bufSize, GLsizei *length, GLint *size,
    GLenum *type, GLchar *name)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetActiveUniform' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetActiveUniform(GLuint "
        "program, GLuint index, GLsizei bufSize, GLsizei *length, GLint "
        "*size, GLenum *type, GLchar *name)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetActiveUniformBlockName(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetActiveUniformBlockName(GLuint
    program, GLuint uniformBlockIndex, GLsizei bufSize, GLsizei *length,
    GLchar *uniformBlockName)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetActiveUniformBlockName' "
        "has no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetActiveUniformBlockName(GLu"
        "int program, GLuint uniformBlockIndex, GLsizei bufSize, GLsizei "
        "*length, GLchar *uniformBlockName)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetActiveUniformBlockiv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetActiveUniformBlockiv(GLuint
    program, GLuint uniformBlockIndex, GLenum pname, GLint *params)': takes a
    number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetActiveUniformBlockiv' has "
        "no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetActiveUniformBlockiv(GLuin"
        "t program, GLuint uniformBlockIndex, GLenum pname, GLint "
        "*params)': takes a number to change where it is.")

  @staticmethod
  def glGetActiveUniformName(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetActiveUniformName(GLuint
    program, GLuint uniformIndex, GLsizei bufSize, GLsizei *length, GLchar
    *uniformName)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetActiveUniformName' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetActiveUniformName(GLuint "
        "program, GLuint uniformIndex, GLsizei bufSize, GLsizei *length, "
        "GLchar *uniformName)': takes a number to change where it is.")

  @staticmethod
  def glGetActiveUniformsiv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetActiveUniformsiv(GLuint program,
    GLsizei uniformCount, const GLuint *uniformIndices, GLenum pname, GLint
    *params)': names 'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetActiveUniformsiv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetActiveUniformsiv(GLuint "
        "program, GLsizei uniformCount, const GLuint *uniformIndices, "
        "GLenum pname, GLint *params)': names 'GLuint', which has no cute "
        "class yet.")

  @staticmethod
  def glGetAttachedShaders(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetAttachedShaders(GLuint program,
    GLsizei maxCount, GLsizei *count, GLuint *obj)': takes a number to change
    where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetAttachedShaders' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetAttachedShaders(GLuint "
        "program, GLsizei maxCount, GLsizei *count, GLuint *obj)': takes a "
        "number to change where it is.")

  @staticmethod
  def glGetAttribLocation(*__, **_) -> Never:
    """
    Qt's 'GLint
    QOpenGLFunctions_4_3_Compatibility::glGetAttribLocation(GLuint program,
    const GLchar *name)': names 'GLchar', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetAttribLocation' has no "
        "cute function yet. Qt's 'GLint "
        "QOpenGLFunctions_4_3_Compatibility::glGetAttribLocation(GLuint "
        "program, const GLchar *name)': names 'GLchar', which has no cute "
        "class yet.")

  @staticmethod
  def glGetBooleani_v(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetBooleani_v(GLenum
    target, GLuint index, GLboolean *data)': takes a number to change where
    it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetBooleani_v' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetBooleani_v(GLenum target, "
        "GLuint index, GLboolean *data)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetBooleanv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetBooleanv(GLenum
    pname, GLboolean *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetBooleanv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetBooleanv(GLenum pname, "
        "GLboolean *params)': takes a number to change where it is.")

  @staticmethod
  def glGetBufferParameteri64v(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetBufferParameteri64v(GLenum
    target, GLenum pname, GLint64 *params)': takes a number to change where
    it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetBufferParameteri64v' has "
        "no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetBufferParameteri64v(GLenum"
        " target, GLenum pname, GLint64 *params)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetBufferParameteriv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetBufferParameteriv(GLenum target,
    GLenum pname, GLint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetBufferParameteriv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetBufferParameteriv(GLenum "
        "target, GLenum pname, GLint *params)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetBufferPointerv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetBufferPointerv(GLenum
    target, GLenum pname, GLvoid **params)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetBufferPointerv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetBufferPointerv(GLenum "
        "target, GLenum pname, GLvoid **params)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def glGetBufferSubData(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetBufferSubData(GLenum
    target, GLintptr offset, GLsizeiptr size, GLvoid *data)': names 'GLvoid',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetBufferSubData' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetBufferSubData(GLenum "
        "target, GLintptr offset, GLsizeiptr size, GLvoid *data)': names "
        "'GLvoid', which has no cute class yet.")

  @staticmethod
  def glGetClipPlane(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetClipPlane(GLenum
    plane, GLdouble *equation)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetClipPlane' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetClipPlane(GLenum plane, "
        "GLdouble *equation)': takes a number to change where it is.")

  @staticmethod
  def glGetColorTable(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetColorTable(GLenum
    target, GLenum format, GLenum type, GLvoid *table)': names 'GLvoid',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetColorTable' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetColorTable(GLenum target, "
        "GLenum format, GLenum type, GLvoid *table)': names 'GLvoid', which "
        "has no cute class yet.")

  @staticmethod
  def glGetColorTableParameterfv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetColorTableParameterfv(GLenum
    target, GLenum pname, GLfloat *params)': takes a number to change where
    it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetColorTableParameterfv' "
        "has no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetColorTableParameterfv(GLen"
        "um target, GLenum pname, GLfloat *params)': takes a number to "
        "change where it is.")

  @staticmethod
  def glGetColorTableParameteriv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetColorTableParameteriv(GLenum
    target, GLenum pname, GLint *params)': takes a number to change where it
    is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetColorTableParameteriv' "
        "has no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetColorTableParameteriv(GLen"
        "um target, GLenum pname, GLint *params)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetCompressedTexImage(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetCompressedTexImage(GLenum
    target, GLint level, GLvoid *img)': names 'GLvoid', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetCompressedTexImage' has "
        "no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetCompressedTexImage(GLenum "
        "target, GLint level, GLvoid *img)': names 'GLvoid', which has no "
        "cute class yet.")

  @staticmethod
  def glGetConvolutionFilter(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetConvolutionFilter(GLenum target,
    GLenum format, GLenum type, GLvoid *image)': names 'GLvoid', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetConvolutionFilter' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetConvolutionFilter(GLenum "
        "target, GLenum format, GLenum type, GLvoid *image)': names "
        "'GLvoid', which has no cute class yet.")

  @staticmethod
  def glGetConvolutionParameterfv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetConvolutionParameterfv(GLenum
    target, GLenum pname, GLfloat *params)': takes a number to change where
    it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetConvolutionParameterfv' "
        "has no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetConvolutionParameterfv(GLe"
        "num target, GLenum pname, GLfloat *params)': takes a number to "
        "change where it is.")

  @staticmethod
  def glGetConvolutionParameteriv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetConvolutionParameteriv(GLenum
    target, GLenum pname, GLint *params)': takes a number to change where it
    is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetConvolutionParameteriv' "
        "has no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetConvolutionParameteriv(GLe"
        "num target, GLenum pname, GLint *params)': takes a number to "
        "change where it is.")

  @staticmethod
  def glGetDoublei_v(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetDoublei_v(GLenum
    target, GLuint index, GLdouble *data)': takes a number to change where it
    is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetDoublei_v' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetDoublei_v(GLenum target, "
        "GLuint index, GLdouble *data)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetDoublev(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetDoublev(GLenum pname,
    GLdouble *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetDoublev' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetDoublev(GLenum pname, "
        "GLdouble *params)': takes a number to change where it is.")

  @staticmethod
  def glGetFloati_v(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetFloati_v(GLenum
    target, GLuint index, GLfloat *data)': takes a number to change where it
    is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetFloati_v' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetFloati_v(GLenum target, "
        "GLuint index, GLfloat *data)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetFloatv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetFloatv(GLenum pname,
    GLfloat *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetFloatv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetFloatv(GLenum pname, "
        "GLfloat *params)': takes a number to change where it is.")

  @staticmethod
  def glGetFragDataIndex(*__, **_) -> Never:
    """
    Qt's 'GLint QOpenGLFunctions_4_3_Compatibility::glGetFragDataIndex(GLuint
    program, const GLchar *name)': names 'GLchar', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetFragDataIndex' has no "
        "cute function yet. Qt's 'GLint "
        "QOpenGLFunctions_4_3_Compatibility::glGetFragDataIndex(GLuint "
        "program, const GLchar *name)': names 'GLchar', which has no cute "
        "class yet.")

  @staticmethod
  def glGetFragDataLocation(*__, **_) -> Never:
    """
    Qt's 'GLint
    QOpenGLFunctions_4_3_Compatibility::glGetFragDataLocation(GLuint program,
    const GLchar *name)': names 'GLchar', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetFragDataLocation' has no "
        "cute function yet. Qt's 'GLint "
        "QOpenGLFunctions_4_3_Compatibility::glGetFragDataLocation(GLuint "
        "program, const GLchar *name)': names 'GLchar', which has no cute "
        "class yet.")

  @staticmethod
  def glGetFramebufferAttachmentParameteriv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::
    glGetFramebufferAttachmentParameteriv(GLenum target, GLenum attachment,
    GLenum pname, GLint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetFramebufferAttachmentParam"
        "eteriv' has no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetFramebufferAttachmentParam"
        "eteriv(GLenum target, GLenum attachment, GLenum pname, GLint "
        "*params)': takes a number to change where it is.")

  @staticmethod
  def glGetFramebufferParameteriv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetFramebufferParameteriv(GLenum
    target, GLenum pname, GLint *params)': takes a number to change where it
    is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetFramebufferParameteriv' "
        "has no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetFramebufferParameteriv(GLe"
        "num target, GLenum pname, GLint *params)': takes a number to "
        "change where it is.")

  @staticmethod
  def glGetHistogram(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetHistogram(GLenum
    target, GLboolean reset, GLenum format, GLenum type, GLvoid *values)':
    names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetHistogram' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetHistogram(GLenum target, "
        "GLboolean reset, GLenum format, GLenum type, GLvoid *values)': "
        "names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glGetHistogramParameterfv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetHistogramParameterfv(GLenum
    target, GLenum pname, GLfloat *params)': takes a number to change where
    it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetHistogramParameterfv' has "
        "no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetHistogramParameterfv(GLenu"
        "m target, GLenum pname, GLfloat *params)': takes a number to "
        "change where it is.")

  @staticmethod
  def glGetHistogramParameteriv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetHistogramParameteriv(GLenum
    target, GLenum pname, GLint *params)': takes a number to change where it
    is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetHistogramParameteriv' has "
        "no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetHistogramParameteriv(GLenu"
        "m target, GLenum pname, GLint *params)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetInteger64i_v(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetInteger64i_v(GLenum
    target, GLuint index, GLint64 *data)': takes a number to change where it
    is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetInteger64i_v' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetInteger64i_v(GLenum "
        "target, GLuint index, GLint64 *data)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetInteger64v(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetInteger64v(GLenum
    pname, GLint64 *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetInteger64v' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetInteger64v(GLenum pname, "
        "GLint64 *params)': takes a number to change where it is.")

  @staticmethod
  def glGetIntegeri_v(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetIntegeri_v(GLenum
    target, GLuint index, GLint *data)': takes a number to change where it
    is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetIntegeri_v' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetIntegeri_v(GLenum target, "
        "GLuint index, GLint *data)': takes a number to change where it is.")

  @staticmethod
  def glGetIntegerv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetIntegerv(GLenum
    pname, GLint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetIntegerv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetIntegerv(GLenum pname, "
        "GLint *params)': takes a number to change where it is.")

  @staticmethod
  def glGetInternalformati64v(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetInternalformati64v(GLenum
    target, GLenum internalformat, GLenum pname, GLsizei bufSize, GLint64
    *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetInternalformati64v' has "
        "no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetInternalformati64v(GLenum "
        "target, GLenum internalformat, GLenum pname, GLsizei bufSize, "
        "GLint64 *params)': takes a number to change where it is.")

  @staticmethod
  def glGetInternalformativ(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetInternalformativ(GLenum target,
    GLenum internalformat, GLenum pname, GLsizei bufSize, GLint *params)':
    takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetInternalformativ' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetInternalformativ(GLenum "
        "target, GLenum internalformat, GLenum pname, GLsizei bufSize, "
        "GLint *params)': takes a number to change where it is.")

  @staticmethod
  def glGetLightfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetLightfv(GLenum light,
    GLenum pname, GLfloat *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetLightfv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetLightfv(GLenum light, "
        "GLenum pname, GLfloat *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetLightiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetLightiv(GLenum light,
    GLenum pname, GLint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetLightiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetLightiv(GLenum light, "
        "GLenum pname, GLint *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetMapdv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetMapdv(GLenum target,
    GLenum query, GLdouble *v)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetMapdv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetMapdv(GLenum target, "
        "GLenum query, GLdouble *v)': takes a number to change where it is.")

  @staticmethod
  def glGetMapfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetMapfv(GLenum target,
    GLenum query, GLfloat *v)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetMapfv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetMapfv(GLenum target, "
        "GLenum query, GLfloat *v)': takes a number to change where it is.")

  @staticmethod
  def glGetMapiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetMapiv(GLenum target,
    GLenum query, GLint *v)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetMapiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetMapiv(GLenum target, "
        "GLenum query, GLint *v)': takes a number to change where it is.")

  @staticmethod
  def glGetMaterialfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetMaterialfv(GLenum
    face, GLenum pname, GLfloat *params)': takes a number to change where it
    is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetMaterialfv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetMaterialfv(GLenum face, "
        "GLenum pname, GLfloat *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetMaterialiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetMaterialiv(GLenum
    face, GLenum pname, GLint *params)': takes a number to change where it
    is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetMaterialiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetMaterialiv(GLenum face, "
        "GLenum pname, GLint *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetMinmax(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetMinmax(GLenum target,
    GLboolean reset, GLenum format, GLenum type, GLvoid *values)': names
    'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetMinmax' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetMinmax(GLenum target, "
        "GLboolean reset, GLenum format, GLenum type, GLvoid *values)': "
        "names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glGetMinmaxParameterfv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetMinmaxParameterfv(GLenum target,
    GLenum pname, GLfloat *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetMinmaxParameterfv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetMinmaxParameterfv(GLenum "
        "target, GLenum pname, GLfloat *params)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetMinmaxParameteriv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetMinmaxParameteriv(GLenum target,
    GLenum pname, GLint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetMinmaxParameteriv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetMinmaxParameteriv(GLenum "
        "target, GLenum pname, GLint *params)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetMultisamplefv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetMultisamplefv(GLenum
    pname, GLuint index, GLfloat *val)': takes a number to change where it
    is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetMultisamplefv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetMultisamplefv(GLenum "
        "pname, GLuint index, GLfloat *val)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetPixelMapfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetPixelMapfv(GLenum
    map, GLfloat *values)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetPixelMapfv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetPixelMapfv(GLenum map, "
        "GLfloat *values)': takes a number to change where it is.")

  @staticmethod
  def glGetPixelMapuiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetPixelMapuiv(GLenum
    map, GLuint *values)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetPixelMapuiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetPixelMapuiv(GLenum map, "
        "GLuint *values)': takes a number to change where it is.")

  @staticmethod
  def glGetPixelMapusv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetPixelMapusv(GLenum
    map, GLushort *values)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetPixelMapusv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetPixelMapusv(GLenum map, "
        "GLushort *values)': takes a number to change where it is.")

  @staticmethod
  def glGetPointerv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetPointerv(GLenum
    pname, GLvoid **params)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetPointerv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetPointerv(GLenum pname, "
        "GLvoid **params)': takes a type Python has no way to hand over yet."
    )

  @staticmethod
  def glGetPolygonStipple(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetPolygonStipple(GLubyte *mask)':
    takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetPolygonStipple' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetPolygonStipple(GLubyte "
        "*mask)': takes a number to change where it is.")

  @staticmethod
  def glGetProgramBinary(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetProgramBinary(GLuint
    program, GLsizei bufSize, GLsizei *length, GLenum *binaryFormat, GLvoid
    *binary)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetProgramBinary' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetProgramBinary(GLuint "
        "program, GLsizei bufSize, GLsizei *length, GLenum *binaryFormat, "
        "GLvoid *binary)': takes a number to change where it is.")

  @staticmethod
  def glGetProgramInfoLog(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetProgramInfoLog(GLuint
    program, GLsizei bufSize, GLsizei *length, GLchar *infoLog)': takes a
    number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetProgramInfoLog' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetProgramInfoLog(GLuint "
        "program, GLsizei bufSize, GLsizei *length, GLchar *infoLog)': "
        "takes a number to change where it is.")

  @staticmethod
  def glGetProgramInterfaceiv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetProgramInterfaceiv(GLuint
    program, GLenum programInterface, GLenum pname, GLint *params)': takes a
    number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetProgramInterfaceiv' has "
        "no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetProgramInterfaceiv(GLuint "
        "program, GLenum programInterface, GLenum pname, GLint *params)': "
        "takes a number to change where it is.")

  @staticmethod
  def glGetProgramPipelineInfoLog(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetProgramPipelineInfoLog(GLuint
    pipeline, GLsizei bufSize, GLsizei *length, GLchar *infoLog)': takes a
    number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetProgramPipelineInfoLog' "
        "has no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetProgramPipelineInfoLog(GLu"
        "int pipeline, GLsizei bufSize, GLsizei *length, GLchar *infoLog)': "
        "takes a number to change where it is.")

  @staticmethod
  def glGetProgramPipelineiv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetProgramPipelineiv(GLuint
    pipeline, GLenum pname, GLint *params)': takes a number to change where
    it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetProgramPipelineiv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetProgramPipelineiv(GLuint "
        "pipeline, GLenum pname, GLint *params)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetProgramResourceIndex(*__, **_) -> Never:
    """
    Qt's 'GLuint
    QOpenGLFunctions_4_3_Compatibility::glGetProgramResourceIndex(GLuint
    program, GLenum programInterface, const GLchar *name)': names 'GLchar',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetProgramResourceIndex' has "
        "no cute function yet. Qt's 'GLuint "
        "QOpenGLFunctions_4_3_Compatibility::glGetProgramResourceIndex(GLuin"
        "t program, GLenum programInterface, const GLchar *name)': names "
        "'GLchar', which has no cute class yet.")

  @staticmethod
  def glGetProgramResourceLocation(*__, **_) -> Never:
    """
    Qt's 'GLint
    QOpenGLFunctions_4_3_Compatibility::glGetProgramResourceLocation(GLuint
    program, GLenum programInterface, const GLchar *name)': names 'GLchar',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetProgramResourceLocation' "
        "has no cute function yet. Qt's 'GLint "
        "QOpenGLFunctions_4_3_Compatibility::glGetProgramResourceLocation(GL"
        "uint program, GLenum programInterface, const GLchar *name)': names "
        "'GLchar', which has no cute class yet.")

  @staticmethod
  def glGetProgramResourceLocationIndex(*__, **_) -> Never:
    """
    Qt's 'GLint
    QOpenGLFunctions_4_3_Compatibility::glGetProgramResourceLocationIndex(
    GLuint program, GLenum programInterface, const GLchar *name)': names
    'GLchar', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetProgramResourceLocationInd"
        "ex' has no cute function yet. Qt's 'GLint "
        "QOpenGLFunctions_4_3_Compatibility::glGetProgramResourceLocationInd"
        "ex(GLuint program, GLenum programInterface, const GLchar *name)': "
        "names 'GLchar', which has no cute class yet.")

  @staticmethod
  def glGetProgramResourceName(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetProgramResourceName(GLuint
    program, GLenum programInterface, GLuint index, GLsizei bufSize, GLsizei
    *length, GLchar *name)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetProgramResourceName' has "
        "no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetProgramResourceName(GLuint"
        " program, GLenum programInterface, GLuint index, GLsizei bufSize, "
        "GLsizei *length, GLchar *name)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetProgramResourceiv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetProgramResourceiv(GLuint
    program, GLenum programInterface, GLuint index, GLsizei propCount, const
    GLenum *props, GLsizei bufSize, GLsizei *length, GLint *params)': names
    'GLenum', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetProgramResourceiv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetProgramResourceiv(GLuint "
        "program, GLenum programInterface, GLuint index, GLsizei propCount, "
        "const GLenum *props, GLsizei bufSize, GLsizei *length, GLint "
        "*params)': names 'GLenum', which has no cute class yet.")

  @staticmethod
  def glGetProgramStageiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetProgramStageiv(GLuint
    program, GLenum shadertype, GLenum pname, GLint *values)': takes a number
    to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetProgramStageiv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetProgramStageiv(GLuint "
        "program, GLenum shadertype, GLenum pname, GLint *values)': takes a "
        "number to change where it is.")

  @staticmethod
  def glGetProgramiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetProgramiv(GLuint
    program, GLenum pname, GLint *params)': takes a number to change where it
    is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetProgramiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetProgramiv(GLuint program, "
        "GLenum pname, GLint *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetQueryIndexediv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetQueryIndexediv(GLenum
    target, GLuint index, GLenum pname, GLint *params)': takes a number to
    change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetQueryIndexediv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetQueryIndexediv(GLenum "
        "target, GLuint index, GLenum pname, GLint *params)': takes a "
        "number to change where it is.")

  @staticmethod
  def glGetQueryObjecti64v(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetQueryObjecti64v(GLuint id,
    GLenum pname, GLint64 *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetQueryObjecti64v' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetQueryObjecti64v(GLuint "
        "id, GLenum pname, GLint64 *params)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetQueryObjectiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetQueryObjectiv(GLuint
    id, GLenum pname, GLint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetQueryObjectiv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetQueryObjectiv(GLuint id, "
        "GLenum pname, GLint *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetQueryObjectui64v(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetQueryObjectui64v(GLuint id,
    GLenum pname, GLuint64 *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetQueryObjectui64v' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetQueryObjectui64v(GLuint "
        "id, GLenum pname, GLuint64 *params)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetQueryObjectuiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetQueryObjectuiv(GLuint
    id, GLenum pname, GLuint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetQueryObjectuiv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetQueryObjectuiv(GLuint id, "
        "GLenum pname, GLuint *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetQueryiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetQueryiv(GLenum
    target, GLenum pname, GLint *params)': takes a number to change where it
    is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetQueryiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetQueryiv(GLenum target, "
        "GLenum pname, GLint *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetRenderbufferParameteriv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetRenderbufferParameteriv(GLenum
    target, GLenum pname, GLint *params)': takes a number to change where it
    is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetRenderbufferParameteriv' "
        "has no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetRenderbufferParameteriv(GL"
        "enum target, GLenum pname, GLint *params)': takes a number to "
        "change where it is.")

  @staticmethod
  def glGetSamplerParameterIiv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetSamplerParameterIiv(GLuint
    sampler, GLenum pname, GLint *params)': takes a number to change where it
    is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetSamplerParameterIiv' has "
        "no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetSamplerParameterIiv(GLuint"
        " sampler, GLenum pname, GLint *params)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetSamplerParameterIuiv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetSamplerParameterIuiv(GLuint
    sampler, GLenum pname, GLuint *params)': takes a number to change where
    it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetSamplerParameterIuiv' has "
        "no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetSamplerParameterIuiv(GLuin"
        "t sampler, GLenum pname, GLuint *params)': takes a number to "
        "change where it is.")

  @staticmethod
  def glGetSamplerParameterfv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetSamplerParameterfv(GLuint
    sampler, GLenum pname, GLfloat *params)': takes a number to change where
    it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetSamplerParameterfv' has "
        "no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetSamplerParameterfv(GLuint "
        "sampler, GLenum pname, GLfloat *params)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetSamplerParameteriv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetSamplerParameteriv(GLuint
    sampler, GLenum pname, GLint *params)': takes a number to change where it
    is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetSamplerParameteriv' has "
        "no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetSamplerParameteriv(GLuint "
        "sampler, GLenum pname, GLint *params)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetSeparableFilter(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetSeparableFilter(GLenum target,
    GLenum format, GLenum type, GLvoid *row, GLvoid *column, GLvoid *span)':
    names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetSeparableFilter' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetSeparableFilter(GLenum "
        "target, GLenum format, GLenum type, GLvoid *row, GLvoid *column, "
        "GLvoid *span)': names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glGetShaderInfoLog(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetShaderInfoLog(GLuint
    shader, GLsizei bufSize, GLsizei *length, GLchar *infoLog)': takes a
    number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetShaderInfoLog' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetShaderInfoLog(GLuint "
        "shader, GLsizei bufSize, GLsizei *length, GLchar *infoLog)': takes "
        "a number to change where it is.")

  @staticmethod
  def glGetShaderPrecisionFormat(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetShaderPrecisionFormat(GLenum
    shadertype, GLenum precisiontype, GLint *range, GLint *precision)': takes
    a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetShaderPrecisionFormat' "
        "has no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetShaderPrecisionFormat(GLen"
        "um shadertype, GLenum precisiontype, GLint *range, GLint "
        "*precision)': takes a number to change where it is.")

  @staticmethod
  def glGetShaderSource(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetShaderSource(GLuint
    shader, GLsizei bufSize, GLsizei *length, GLchar *source)': takes a
    number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetShaderSource' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetShaderSource(GLuint "
        "shader, GLsizei bufSize, GLsizei *length, GLchar *source)': takes "
        "a number to change where it is.")

  @staticmethod
  def glGetShaderiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetShaderiv(GLuint
    shader, GLenum pname, GLint *params)': takes a number to change where it
    is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetShaderiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetShaderiv(GLuint shader, "
        "GLenum pname, GLint *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetString(*__, **_) -> Never:
    """
    Qt's 'const GLubyte
    *QOpenGLFunctions_4_3_Compatibility::glGetString(GLenum name)': gives
    'unsigned char', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetString' has no cute "
        "function yet. Qt's 'const GLubyte "
        "*QOpenGLFunctions_4_3_Compatibility::glGetString(GLenum name)': "
        "gives 'unsigned char', which has no cute class yet.")

  @staticmethod
  def glGetStringi(*__, **_) -> Never:
    """
    Qt's 'const GLubyte
    *QOpenGLFunctions_4_3_Compatibility::glGetStringi(GLenum name, GLuint
    index)': gives 'unsigned char', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetStringi' has no cute "
        "function yet. Qt's 'const GLubyte "
        "*QOpenGLFunctions_4_3_Compatibility::glGetStringi(GLenum name, "
        "GLuint index)': gives 'unsigned char', which has no cute class yet."
    )

  @staticmethod
  def glGetSubroutineIndex(*__, **_) -> Never:
    """
    Qt's 'GLuint
    QOpenGLFunctions_4_3_Compatibility::glGetSubroutineIndex(GLuint program,
    GLenum shadertype, const GLchar *name)': names 'GLchar', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetSubroutineIndex' has no "
        "cute function yet. Qt's 'GLuint "
        "QOpenGLFunctions_4_3_Compatibility::glGetSubroutineIndex(GLuint "
        "program, GLenum shadertype, const GLchar *name)': names 'GLchar', "
        "which has no cute class yet.")

  @staticmethod
  def glGetSubroutineUniformLocation(*__, **_) -> Never:
    """
    Qt's 'GLint
    QOpenGLFunctions_4_3_Compatibility::glGetSubroutineUniformLocation(GLuint
    program, GLenum shadertype, const GLchar *name)': names 'GLchar', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetSubroutineUniformLocation'"
        " has no cute function yet. Qt's 'GLint "
        "QOpenGLFunctions_4_3_Compatibility::glGetSubroutineUniformLocation("
        "GLuint program, GLenum shadertype, const GLchar *name)': names "
        "'GLchar', which has no cute class yet.")

  @staticmethod
  def glGetSynciv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetSynciv(GLsync sync,
    GLenum pname, GLsizei bufSize, GLsizei *length, GLint *values)': names
    'struct __GLsync', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetSynciv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetSynciv(GLsync sync, "
        "GLenum pname, GLsizei bufSize, GLsizei *length, GLint *values)': "
        "names 'struct __GLsync', which has no cute class yet.")

  @staticmethod
  def glGetTexEnvfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetTexEnvfv(GLenum
    target, GLenum pname, GLfloat *params)': takes a number to change where
    it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetTexEnvfv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetTexEnvfv(GLenum target, "
        "GLenum pname, GLfloat *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetTexEnviv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetTexEnviv(GLenum
    target, GLenum pname, GLint *params)': takes a number to change where it
    is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetTexEnviv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetTexEnviv(GLenum target, "
        "GLenum pname, GLint *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetTexGendv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetTexGendv(GLenum
    coord, GLenum pname, GLdouble *params)': takes a number to change where
    it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetTexGendv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetTexGendv(GLenum coord, "
        "GLenum pname, GLdouble *params)': takes a number to change where "
        "it is.")

  @staticmethod
  def glGetTexGenfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetTexGenfv(GLenum
    coord, GLenum pname, GLfloat *params)': takes a number to change where it
    is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetTexGenfv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetTexGenfv(GLenum coord, "
        "GLenum pname, GLfloat *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetTexGeniv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetTexGeniv(GLenum
    coord, GLenum pname, GLint *params)': takes a number to change where it
    is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetTexGeniv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetTexGeniv(GLenum coord, "
        "GLenum pname, GLint *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetTexImage(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetTexImage(GLenum
    target, GLint level, GLenum format, GLenum type, GLvoid *pixels)': names
    'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetTexImage' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetTexImage(GLenum target, "
        "GLint level, GLenum format, GLenum type, GLvoid *pixels)': names "
        "'GLvoid', which has no cute class yet.")

  @staticmethod
  def glGetTexLevelParameterfv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetTexLevelParameterfv(GLenum
    target, GLint level, GLenum pname, GLfloat *params)': takes a number to
    change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetTexLevelParameterfv' has "
        "no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetTexLevelParameterfv(GLenum"
        " target, GLint level, GLenum pname, GLfloat *params)': takes a "
        "number to change where it is.")

  @staticmethod
  def glGetTexLevelParameteriv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetTexLevelParameteriv(GLenum
    target, GLint level, GLenum pname, GLint *params)': takes a number to
    change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetTexLevelParameteriv' has "
        "no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetTexLevelParameteriv(GLenum"
        " target, GLint level, GLenum pname, GLint *params)': takes a "
        "number to change where it is.")

  @staticmethod
  def glGetTexParameterIiv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetTexParameterIiv(GLenum target,
    GLenum pname, GLint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetTexParameterIiv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetTexParameterIiv(GLenum "
        "target, GLenum pname, GLint *params)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetTexParameterIuiv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetTexParameterIuiv(GLenum target,
    GLenum pname, GLuint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetTexParameterIuiv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetTexParameterIuiv(GLenum "
        "target, GLenum pname, GLuint *params)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetTexParameterfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetTexParameterfv(GLenum
    target, GLenum pname, GLfloat *params)': takes a number to change where
    it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetTexParameterfv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetTexParameterfv(GLenum "
        "target, GLenum pname, GLfloat *params)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetTexParameteriv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetTexParameteriv(GLenum
    target, GLenum pname, GLint *params)': takes a number to change where it
    is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetTexParameteriv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetTexParameteriv(GLenum "
        "target, GLenum pname, GLint *params)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetTransformFeedbackVarying(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetTransformFeedbackVarying(GLuint
    program, GLuint index, GLsizei bufSize, GLsizei *length, GLsizei *size,
    GLenum *type, GLchar *name)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetTransformFeedbackVarying' "
        "has no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetTransformFeedbackVarying(G"
        "Luint program, GLuint index, GLsizei bufSize, GLsizei *length, "
        "GLsizei *size, GLenum *type, GLchar *name)': takes a number to "
        "change where it is.")

  @staticmethod
  def glGetUniformBlockIndex(*__, **_) -> Never:
    """
    Qt's 'GLuint
    QOpenGLFunctions_4_3_Compatibility::glGetUniformBlockIndex(GLuint
    program, const GLchar *uniformBlockName)': names 'GLchar', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetUniformBlockIndex' has no "
        "cute function yet. Qt's 'GLuint "
        "QOpenGLFunctions_4_3_Compatibility::glGetUniformBlockIndex(GLuint "
        "program, const GLchar *uniformBlockName)': names 'GLchar', which "
        "has no cute class yet.")

  @staticmethod
  def glGetUniformIndices(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetUniformIndices(GLuint
    program, GLsizei uniformCount, const GLchar *const *uniformNames, GLuint
    *uniformIndices)': names 'GLchar *const', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetUniformIndices' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetUniformIndices(GLuint "
        "program, GLsizei uniformCount, const GLchar *const *uniformNames, "
        "GLuint *uniformIndices)': names 'GLchar *const', which has no cute "
        "class yet.")

  @staticmethod
  def glGetUniformLocation(*__, **_) -> Never:
    """
    Qt's 'GLint
    QOpenGLFunctions_4_3_Compatibility::glGetUniformLocation(GLuint program,
    const GLchar *name)': names 'GLchar', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetUniformLocation' has no "
        "cute function yet. Qt's 'GLint "
        "QOpenGLFunctions_4_3_Compatibility::glGetUniformLocation(GLuint "
        "program, const GLchar *name)': names 'GLchar', which has no cute "
        "class yet.")

  @staticmethod
  def glGetUniformSubroutineuiv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetUniformSubroutineuiv(GLenum
    shadertype, GLint location, GLuint *params)': takes a number to change
    where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetUniformSubroutineuiv' has "
        "no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetUniformSubroutineuiv(GLenu"
        "m shadertype, GLint location, GLuint *params)': takes a number to "
        "change where it is.")

  @staticmethod
  def glGetUniformdv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetUniformdv(GLuint
    program, GLint location, GLdouble *params)': takes a number to change
    where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetUniformdv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetUniformdv(GLuint program, "
        "GLint location, GLdouble *params)': takes a number to change where "
        "it is.")

  @staticmethod
  def glGetUniformfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetUniformfv(GLuint
    program, GLint location, GLfloat *params)': takes a number to change
    where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetUniformfv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetUniformfv(GLuint program, "
        "GLint location, GLfloat *params)': takes a number to change where "
        "it is.")

  @staticmethod
  def glGetUniformiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetUniformiv(GLuint
    program, GLint location, GLint *params)': takes a number to change where
    it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetUniformiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetUniformiv(GLuint program, "
        "GLint location, GLint *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetUniformuiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetUniformuiv(GLuint
    program, GLint location, GLuint *params)': takes a number to change where
    it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetUniformuiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetUniformuiv(GLuint "
        "program, GLint location, GLuint *params)': takes a number to "
        "change where it is.")

  @staticmethod
  def glGetVertexAttribIiv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetVertexAttribIiv(GLuint index,
    GLenum pname, GLint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetVertexAttribIiv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetVertexAttribIiv(GLuint "
        "index, GLenum pname, GLint *params)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetVertexAttribIuiv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetVertexAttribIuiv(GLuint index,
    GLenum pname, GLuint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetVertexAttribIuiv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetVertexAttribIuiv(GLuint "
        "index, GLenum pname, GLuint *params)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetVertexAttribLdv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetVertexAttribLdv(GLuint index,
    GLenum pname, GLdouble *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetVertexAttribLdv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetVertexAttribLdv(GLuint "
        "index, GLenum pname, GLdouble *params)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetVertexAttribPointerv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glGetVertexAttribPointerv(GLuint
    index, GLenum pname, GLvoid **pointer)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetVertexAttribPointerv' has "
        "no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetVertexAttribPointerv(GLuin"
        "t index, GLenum pname, GLvoid **pointer)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def glGetVertexAttribdv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetVertexAttribdv(GLuint
    index, GLenum pname, GLdouble *params)': takes a number to change where
    it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetVertexAttribdv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetVertexAttribdv(GLuint "
        "index, GLenum pname, GLdouble *params)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetVertexAttribfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetVertexAttribfv(GLuint
    index, GLenum pname, GLfloat *params)': takes a number to change where it
    is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetVertexAttribfv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetVertexAttribfv(GLuint "
        "index, GLenum pname, GLfloat *params)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetVertexAttribiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glGetVertexAttribiv(GLuint
    index, GLenum pname, GLint *params)': takes a number to change where it
    is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glGetVertexAttribiv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glGetVertexAttribiv(GLuint "
        "index, GLenum pname, GLint *params)': takes a number to change "
        "where it is.")

  @staticmethod
  def glIndexPointer(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glIndexPointer(GLenum
    type, GLsizei stride, const GLvoid *pointer)': names 'GLvoid', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glIndexPointer' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glIndexPointer(GLenum type, "
        "GLsizei stride, const GLvoid *pointer)': names 'GLvoid', which has "
        "no cute class yet.")

  @staticmethod
  def glIndexdv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glIndexdv(const GLdouble
    *c)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glIndexdv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glIndexdv(const GLdouble *c)': "
        "names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glIndexfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glIndexfv(const GLfloat
    *c)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glIndexfv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glIndexfv(const GLfloat *c)': "
        "names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glIndexiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glIndexiv(const GLint
    *c)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glIndexiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glIndexiv(const GLint *c)': "
        "names 'GLint', which has no cute class yet.")

  @staticmethod
  def glIndexsv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glIndexsv(const GLshort
    *c)': names 'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glIndexsv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glIndexsv(const GLshort *c)': "
        "names 'GLshort', which has no cute class yet.")

  @staticmethod
  def glIndexubv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glIndexubv(const GLubyte
    *c)': names 'GLubyte', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glIndexubv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glIndexubv(const GLubyte *c)': "
        "names 'GLubyte', which has no cute class yet.")

  @staticmethod
  def glInterleavedArrays(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glInterleavedArrays(GLenum
    format, GLsizei stride, const GLvoid *pointer)': names 'GLvoid', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glInterleavedArrays' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glInterleavedArrays(GLenum "
        "format, GLsizei stride, const GLvoid *pointer)': names 'GLvoid', "
        "which has no cute class yet.")

  @staticmethod
  def glInvalidateFramebuffer(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glInvalidateFramebuffer(GLenum
    target, GLsizei numAttachments, const GLenum *attachments)': names
    'GLenum', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glInvalidateFramebuffer' has "
        "no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glInvalidateFramebuffer(GLenum "
        "target, GLsizei numAttachments, const GLenum *attachments)': names "
        "'GLenum', which has no cute class yet.")

  @staticmethod
  def glInvalidateSubFramebuffer(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glInvalidateSubFramebuffer(GLenum
    target, GLsizei numAttachments, const GLenum *attachments, GLint x, GLint
    y, GLsizei width, GLsizei height)': names 'GLenum', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glInvalidateSubFramebuffer' "
        "has no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glInvalidateSubFramebuffer(GLen"
        "um target, GLsizei numAttachments, const GLenum *attachments, "
        "GLint x, GLint y, GLsizei width, GLsizei height)': names 'GLenum', "
        "which has no cute class yet.")

  @staticmethod
  def glIsSync(*__, **_) -> Never:
    """
    Qt's 'GLboolean QOpenGLFunctions_4_3_Compatibility::glIsSync(GLsync
    sync)': names 'struct __GLsync', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glIsSync' has no cute function "
        "yet. Qt's 'GLboolean "
        "QOpenGLFunctions_4_3_Compatibility::glIsSync(GLsync sync)': names "
        "'struct __GLsync', which has no cute class yet.")

  @staticmethod
  def glLightModelfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glLightModelfv(GLenum
    pname, const GLfloat *params)': names 'GLfloat', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glLightModelfv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glLightModelfv(GLenum pname, "
        "const GLfloat *params)': names 'GLfloat', which has no cute class "
        "yet.")

  @staticmethod
  def glLightModeliv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glLightModeliv(GLenum
    pname, const GLint *params)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glLightModeliv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glLightModeliv(GLenum pname, "
        "const GLint *params)': names 'GLint', which has no cute class yet.")

  @staticmethod
  def glLightfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glLightfv(GLenum light,
    GLenum pname, const GLfloat *params)': names 'GLfloat', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glLightfv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glLightfv(GLenum light, GLenum "
        "pname, const GLfloat *params)': names 'GLfloat', which has no cute "
        "class yet.")

  @staticmethod
  def glLightiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glLightiv(GLenum light,
    GLenum pname, const GLint *params)': names 'GLint', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glLightiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glLightiv(GLenum light, GLenum "
        "pname, const GLint *params)': names 'GLint', which has no cute "
        "class yet.")

  @staticmethod
  def glLoadMatrixd(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glLoadMatrixd(const
    GLdouble *m)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glLoadMatrixd' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glLoadMatrixd(const GLdouble "
        "*m)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glLoadMatrixf(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glLoadMatrixf(const
    GLfloat *m)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glLoadMatrixf' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glLoadMatrixf(const GLfloat "
        "*m)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glLoadTransposeMatrixd(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glLoadTransposeMatrixd(const GLdouble
    *m)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glLoadTransposeMatrixd' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glLoadTransposeMatrixd(const "
        "GLdouble *m)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glLoadTransposeMatrixf(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glLoadTransposeMatrixf(const GLfloat
    *m)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glLoadTransposeMatrixf' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glLoadTransposeMatrixf(const "
        "GLfloat *m)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glMap1d(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glMap1d(GLenum target,
    GLdouble u1, GLdouble u2, GLint stride, GLint order, const GLdouble
    *points)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glMap1d' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_3_Compatibility::glMap1d(GLenum "
        "target, GLdouble u1, GLdouble u2, GLint stride, GLint order, const "
        "GLdouble *points)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glMap1f(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glMap1f(GLenum target,
    GLfloat u1, GLfloat u2, GLint stride, GLint order, const GLfloat
    *points)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glMap1f' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_3_Compatibility::glMap1f(GLenum "
        "target, GLfloat u1, GLfloat u2, GLint stride, GLint order, const "
        "GLfloat *points)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glMap2d(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glMap2d(GLenum target,
    GLdouble u1, GLdouble u2, GLint ustride, GLint uorder, GLdouble v1,
    GLdouble v2, GLint vstride, GLint vorder, const GLdouble *points)': names
    'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glMap2d' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_3_Compatibility::glMap2d(GLenum "
        "target, GLdouble u1, GLdouble u2, GLint ustride, GLint uorder, "
        "GLdouble v1, GLdouble v2, GLint vstride, GLint vorder, const "
        "GLdouble *points)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glMap2f(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glMap2f(GLenum target,
    GLfloat u1, GLfloat u2, GLint ustride, GLint uorder, GLfloat v1, GLfloat
    v2, GLint vstride, GLint vorder, const GLfloat *points)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glMap2f' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_3_Compatibility::glMap2f(GLenum "
        "target, GLfloat u1, GLfloat u2, GLint ustride, GLint uorder, "
        "GLfloat v1, GLfloat v2, GLint vstride, GLint vorder, const GLfloat "
        "*points)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glMapBuffer(*__, **_) -> Never:
    """
    Qt's 'GLvoid *QOpenGLFunctions_4_3_Compatibility::glMapBuffer(GLenum
    target, GLenum access)': gives 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glMapBuffer' has no cute "
        "function yet. Qt's 'GLvoid "
        "*QOpenGLFunctions_4_3_Compatibility::glMapBuffer(GLenum target, "
        "GLenum access)': gives 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glMapBufferRange(*__, **_) -> Never:
    """
    Qt's 'GLvoid *QOpenGLFunctions_4_3_Compatibility::glMapBufferRange(GLenum
    target, GLintptr offset, GLsizeiptr length, GLbitfield access)': gives
    'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glMapBufferRange' has no cute "
        "function yet. Qt's 'GLvoid "
        "*QOpenGLFunctions_4_3_Compatibility::glMapBufferRange(GLenum "
        "target, GLintptr offset, GLsizeiptr length, GLbitfield access)': "
        "gives 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glMaterialfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glMaterialfv(GLenum face,
    GLenum pname, const GLfloat *params)': names 'GLfloat', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glMaterialfv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glMaterialfv(GLenum face, "
        "GLenum pname, const GLfloat *params)': names 'GLfloat', which has "
        "no cute class yet.")

  @staticmethod
  def glMaterialiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glMaterialiv(GLenum face,
    GLenum pname, const GLint *params)': names 'GLint', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glMaterialiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glMaterialiv(GLenum face, "
        "GLenum pname, const GLint *params)': names 'GLint', which has no "
        "cute class yet.")

  @staticmethod
  def glMultMatrixd(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glMultMatrixd(const
    GLdouble *m)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glMultMatrixd' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glMultMatrixd(const GLdouble "
        "*m)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glMultMatrixf(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glMultMatrixf(const
    GLfloat *m)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glMultMatrixf' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glMultMatrixf(const GLfloat "
        "*m)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glMultTransposeMatrixd(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glMultTransposeMatrixd(const GLdouble
    *m)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glMultTransposeMatrixd' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glMultTransposeMatrixd(const "
        "GLdouble *m)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glMultTransposeMatrixf(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glMultTransposeMatrixf(const GLfloat
    *m)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glMultTransposeMatrixf' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glMultTransposeMatrixf(const "
        "GLfloat *m)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glMultiDrawArrays(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glMultiDrawArrays(GLenum
    mode, const GLint *first, const GLsizei *count, GLsizei drawcount)':
    names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glMultiDrawArrays' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glMultiDrawArrays(GLenum mode, "
        "const GLint *first, const GLsizei *count, GLsizei drawcount)': "
        "names 'GLint', which has no cute class yet.")

  @staticmethod
  def glMultiDrawArraysIndirect(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glMultiDrawArraysIndirect(GLenum
    mode, const void *indirect, GLsizei drawcount, GLsizei stride)': names
    'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glMultiDrawArraysIndirect' has "
        "no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glMultiDrawArraysIndirect(GLenu"
        "m mode, const void *indirect, GLsizei drawcount, GLsizei stride)': "
        "names 'void', which has no cute class yet.")

  @staticmethod
  def glMultiDrawElements(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glMultiDrawElements(GLenum
    mode, const GLsizei *count, GLenum type, const GLvoid *const *indices,
    GLsizei drawcount)': names 'GLsizei', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glMultiDrawElements' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glMultiDrawElements(GLenum "
        "mode, const GLsizei *count, GLenum type, const GLvoid *const "
        "*indices, GLsizei drawcount)': names 'GLsizei', which has no cute "
        "class yet.")

  @staticmethod
  def glMultiDrawElementsBaseVertex(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glMultiDrawElementsBaseVertex(GLenum
    mode, const GLsizei *count, GLenum type, const GLvoid *const *indices,
    GLsizei drawcount, const GLint *basevertex)': names 'GLsizei', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glMultiDrawElementsBaseVertex' "
        "has no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glMultiDrawElementsBaseVertex(G"
        "Lenum mode, const GLsizei *count, GLenum type, const GLvoid *const "
        "*indices, GLsizei drawcount, const GLint *basevertex)': names "
        "'GLsizei', which has no cute class yet.")

  @staticmethod
  def glMultiDrawElementsIndirect(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glMultiDrawElementsIndirect(GLenum
    mode, GLenum type, const void *indirect, GLsizei drawcount, GLsizei
    stride)': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glMultiDrawElementsIndirect' "
        "has no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glMultiDrawElementsIndirect(GLe"
        "num mode, GLenum type, const void *indirect, GLsizei drawcount, "
        "GLsizei stride)': names 'void', which has no cute class yet.")

  @staticmethod
  def glMultiTexCoord1dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord1dv(GLenum
    target, const GLdouble *v)': names 'GLdouble', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glMultiTexCoord1dv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord1dv(GLenum "
        "target, const GLdouble *v)': names 'GLdouble', which has no cute "
        "class yet.")

  @staticmethod
  def glMultiTexCoord1fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord1fv(GLenum
    target, const GLfloat *v)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glMultiTexCoord1fv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord1fv(GLenum "
        "target, const GLfloat *v)': names 'GLfloat', which has no cute "
        "class yet.")

  @staticmethod
  def glMultiTexCoord1iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord1iv(GLenum
    target, const GLint *v)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glMultiTexCoord1iv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord1iv(GLenum "
        "target, const GLint *v)': names 'GLint', which has no cute class "
        "yet.")

  @staticmethod
  def glMultiTexCoord1sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord1sv(GLenum
    target, const GLshort *v)': names 'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glMultiTexCoord1sv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord1sv(GLenum "
        "target, const GLshort *v)': names 'GLshort', which has no cute "
        "class yet.")

  @staticmethod
  def glMultiTexCoord2dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord2dv(GLenum
    target, const GLdouble *v)': names 'GLdouble', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glMultiTexCoord2dv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord2dv(GLenum "
        "target, const GLdouble *v)': names 'GLdouble', which has no cute "
        "class yet.")

  @staticmethod
  def glMultiTexCoord2fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord2fv(GLenum
    target, const GLfloat *v)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glMultiTexCoord2fv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord2fv(GLenum "
        "target, const GLfloat *v)': names 'GLfloat', which has no cute "
        "class yet.")

  @staticmethod
  def glMultiTexCoord2iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord2iv(GLenum
    target, const GLint *v)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glMultiTexCoord2iv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord2iv(GLenum "
        "target, const GLint *v)': names 'GLint', which has no cute class "
        "yet.")

  @staticmethod
  def glMultiTexCoord2sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord2sv(GLenum
    target, const GLshort *v)': names 'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glMultiTexCoord2sv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord2sv(GLenum "
        "target, const GLshort *v)': names 'GLshort', which has no cute "
        "class yet.")

  @staticmethod
  def glMultiTexCoord3dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord3dv(GLenum
    target, const GLdouble *v)': names 'GLdouble', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glMultiTexCoord3dv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord3dv(GLenum "
        "target, const GLdouble *v)': names 'GLdouble', which has no cute "
        "class yet.")

  @staticmethod
  def glMultiTexCoord3fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord3fv(GLenum
    target, const GLfloat *v)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glMultiTexCoord3fv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord3fv(GLenum "
        "target, const GLfloat *v)': names 'GLfloat', which has no cute "
        "class yet.")

  @staticmethod
  def glMultiTexCoord3iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord3iv(GLenum
    target, const GLint *v)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glMultiTexCoord3iv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord3iv(GLenum "
        "target, const GLint *v)': names 'GLint', which has no cute class "
        "yet.")

  @staticmethod
  def glMultiTexCoord3sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord3sv(GLenum
    target, const GLshort *v)': names 'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glMultiTexCoord3sv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord3sv(GLenum "
        "target, const GLshort *v)': names 'GLshort', which has no cute "
        "class yet.")

  @staticmethod
  def glMultiTexCoord4dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord4dv(GLenum
    target, const GLdouble *v)': names 'GLdouble', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glMultiTexCoord4dv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord4dv(GLenum "
        "target, const GLdouble *v)': names 'GLdouble', which has no cute "
        "class yet.")

  @staticmethod
  def glMultiTexCoord4fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord4fv(GLenum
    target, const GLfloat *v)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glMultiTexCoord4fv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord4fv(GLenum "
        "target, const GLfloat *v)': names 'GLfloat', which has no cute "
        "class yet.")

  @staticmethod
  def glMultiTexCoord4iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord4iv(GLenum
    target, const GLint *v)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glMultiTexCoord4iv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord4iv(GLenum "
        "target, const GLint *v)': names 'GLint', which has no cute class "
        "yet.")

  @staticmethod
  def glMultiTexCoord4sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord4sv(GLenum
    target, const GLshort *v)': names 'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glMultiTexCoord4sv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glMultiTexCoord4sv(GLenum "
        "target, const GLshort *v)': names 'GLshort', which has no cute "
        "class yet.")

  @staticmethod
  def glMultiTexCoordP1uiv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glMultiTexCoordP1uiv(GLenum texture,
    GLenum type, const GLuint *coords)': names 'GLuint', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glMultiTexCoordP1uiv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glMultiTexCoordP1uiv(GLenum "
        "texture, GLenum type, const GLuint *coords)': names 'GLuint', "
        "which has no cute class yet.")

  @staticmethod
  def glMultiTexCoordP2uiv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glMultiTexCoordP2uiv(GLenum texture,
    GLenum type, const GLuint *coords)': names 'GLuint', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glMultiTexCoordP2uiv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glMultiTexCoordP2uiv(GLenum "
        "texture, GLenum type, const GLuint *coords)': names 'GLuint', "
        "which has no cute class yet.")

  @staticmethod
  def glMultiTexCoordP3uiv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glMultiTexCoordP3uiv(GLenum texture,
    GLenum type, const GLuint *coords)': names 'GLuint', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glMultiTexCoordP3uiv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glMultiTexCoordP3uiv(GLenum "
        "texture, GLenum type, const GLuint *coords)': names 'GLuint', "
        "which has no cute class yet.")

  @staticmethod
  def glMultiTexCoordP4uiv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glMultiTexCoordP4uiv(GLenum texture,
    GLenum type, const GLuint *coords)': names 'GLuint', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glMultiTexCoordP4uiv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glMultiTexCoordP4uiv(GLenum "
        "texture, GLenum type, const GLuint *coords)': names 'GLuint', "
        "which has no cute class yet.")

  @staticmethod
  def glNormal3bv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glNormal3bv(const GLbyte
    *v)': names 'GLbyte', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glNormal3bv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glNormal3bv(const GLbyte *v)': "
        "names 'GLbyte', which has no cute class yet.")

  @staticmethod
  def glNormal3dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glNormal3dv(const GLdouble
    *v)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glNormal3dv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glNormal3dv(const GLdouble "
        "*v)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glNormal3fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glNormal3fv(const GLfloat
    *v)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glNormal3fv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glNormal3fv(const GLfloat "
        "*v)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glNormal3iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glNormal3iv(const GLint
    *v)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glNormal3iv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glNormal3iv(const GLint *v)': "
        "names 'GLint', which has no cute class yet.")

  @staticmethod
  def glNormal3sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glNormal3sv(const GLshort
    *v)': names 'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glNormal3sv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glNormal3sv(const GLshort "
        "*v)': names 'GLshort', which has no cute class yet.")

  @staticmethod
  def glNormalP3uiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glNormalP3uiv(GLenum type,
    const GLuint *coords)': names 'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glNormalP3uiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glNormalP3uiv(GLenum type, "
        "const GLuint *coords)': names 'GLuint', which has no cute class "
        "yet.")

  @staticmethod
  def glNormalPointer(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glNormalPointer(GLenum
    type, GLsizei stride, const GLvoid *pointer)': names 'GLvoid', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glNormalPointer' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glNormalPointer(GLenum type, "
        "GLsizei stride, const GLvoid *pointer)': names 'GLvoid', which has "
        "no cute class yet.")

  @staticmethod
  def glPatchParameterfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glPatchParameterfv(GLenum
    pname, const GLfloat *values)': names 'GLfloat', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glPatchParameterfv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glPatchParameterfv(GLenum "
        "pname, const GLfloat *values)': names 'GLfloat', which has no cute "
        "class yet.")

  @staticmethod
  def glPixelMapfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glPixelMapfv(GLenum map,
    GLint mapsize, const GLfloat *values)': names 'GLfloat', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glPixelMapfv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glPixelMapfv(GLenum map, GLint "
        "mapsize, const GLfloat *values)': names 'GLfloat', which has no "
        "cute class yet.")

  @staticmethod
  def glPixelMapuiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glPixelMapuiv(GLenum map,
    GLint mapsize, const GLuint *values)': names 'GLuint', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glPixelMapuiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glPixelMapuiv(GLenum map, "
        "GLint mapsize, const GLuint *values)': names 'GLuint', which has "
        "no cute class yet.")

  @staticmethod
  def glPixelMapusv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glPixelMapusv(GLenum map,
    GLint mapsize, const GLushort *values)': names 'GLushort', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glPixelMapusv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glPixelMapusv(GLenum map, "
        "GLint mapsize, const GLushort *values)': names 'GLushort', which "
        "has no cute class yet.")

  @staticmethod
  def glPointParameterfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glPointParameterfv(GLenum
    pname, const GLfloat *params)': names 'GLfloat', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glPointParameterfv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glPointParameterfv(GLenum "
        "pname, const GLfloat *params)': names 'GLfloat', which has no cute "
        "class yet.")

  @staticmethod
  def glPointParameteriv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glPointParameteriv(GLenum
    pname, const GLint *params)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glPointParameteriv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glPointParameteriv(GLenum "
        "pname, const GLint *params)': names 'GLint', which has no cute "
        "class yet.")

  @staticmethod
  def glPolygonStipple(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glPolygonStipple(const
    GLubyte *mask)': names 'GLubyte', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glPolygonStipple' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glPolygonStipple(const GLubyte "
        "*mask)': names 'GLubyte', which has no cute class yet.")

  @staticmethod
  def glPrioritizeTextures(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glPrioritizeTextures(GLsizei n, const
    GLuint *textures, const GLfloat *priorities)': names 'GLuint', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glPrioritizeTextures' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glPrioritizeTextures(GLsizei "
        "n, const GLuint *textures, const GLfloat *priorities)': names "
        "'GLuint', which has no cute class yet.")

  @staticmethod
  def glProgramBinary(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glProgramBinary(GLuint
    program, GLenum binaryFormat, const GLvoid *binary, GLsizei length)':
    names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glProgramBinary' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glProgramBinary(GLuint "
        "program, GLenum binaryFormat, const GLvoid *binary, GLsizei "
        "length)': names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glProgramUniform1dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glProgramUniform1dv(GLuint
    program, GLint location, GLsizei count, const GLdouble *value)': names
    'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glProgramUniform1dv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glProgramUniform1dv(GLuint "
        "program, GLint location, GLsizei count, const GLdouble *value)': "
        "names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glProgramUniform1fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glProgramUniform1fv(GLuint
    program, GLint location, GLsizei count, const GLfloat *value)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glProgramUniform1fv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glProgramUniform1fv(GLuint "
        "program, GLint location, GLsizei count, const GLfloat *value)': "
        "names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glProgramUniform1iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glProgramUniform1iv(GLuint
    program, GLint location, GLsizei count, const GLint *value)': names
    'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glProgramUniform1iv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glProgramUniform1iv(GLuint "
        "program, GLint location, GLsizei count, const GLint *value)': "
        "names 'GLint', which has no cute class yet.")

  @staticmethod
  def glProgramUniform1uiv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glProgramUniform1uiv(GLuint program,
    GLint location, GLsizei count, const GLuint *value)': names 'GLuint',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glProgramUniform1uiv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glProgramUniform1uiv(GLuint "
        "program, GLint location, GLsizei count, const GLuint *value)': "
        "names 'GLuint', which has no cute class yet.")

  @staticmethod
  def glProgramUniform2dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glProgramUniform2dv(GLuint
    program, GLint location, GLsizei count, const GLdouble *value)': names
    'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glProgramUniform2dv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glProgramUniform2dv(GLuint "
        "program, GLint location, GLsizei count, const GLdouble *value)': "
        "names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glProgramUniform2fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glProgramUniform2fv(GLuint
    program, GLint location, GLsizei count, const GLfloat *value)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glProgramUniform2fv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glProgramUniform2fv(GLuint "
        "program, GLint location, GLsizei count, const GLfloat *value)': "
        "names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glProgramUniform2iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glProgramUniform2iv(GLuint
    program, GLint location, GLsizei count, const GLint *value)': names
    'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glProgramUniform2iv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glProgramUniform2iv(GLuint "
        "program, GLint location, GLsizei count, const GLint *value)': "
        "names 'GLint', which has no cute class yet.")

  @staticmethod
  def glProgramUniform2uiv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glProgramUniform2uiv(GLuint program,
    GLint location, GLsizei count, const GLuint *value)': names 'GLuint',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glProgramUniform2uiv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glProgramUniform2uiv(GLuint "
        "program, GLint location, GLsizei count, const GLuint *value)': "
        "names 'GLuint', which has no cute class yet.")

  @staticmethod
  def glProgramUniform3dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glProgramUniform3dv(GLuint
    program, GLint location, GLsizei count, const GLdouble *value)': names
    'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glProgramUniform3dv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glProgramUniform3dv(GLuint "
        "program, GLint location, GLsizei count, const GLdouble *value)': "
        "names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glProgramUniform3fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glProgramUniform3fv(GLuint
    program, GLint location, GLsizei count, const GLfloat *value)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glProgramUniform3fv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glProgramUniform3fv(GLuint "
        "program, GLint location, GLsizei count, const GLfloat *value)': "
        "names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glProgramUniform3iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glProgramUniform3iv(GLuint
    program, GLint location, GLsizei count, const GLint *value)': names
    'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glProgramUniform3iv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glProgramUniform3iv(GLuint "
        "program, GLint location, GLsizei count, const GLint *value)': "
        "names 'GLint', which has no cute class yet.")

  @staticmethod
  def glProgramUniform3uiv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glProgramUniform3uiv(GLuint program,
    GLint location, GLsizei count, const GLuint *value)': names 'GLuint',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glProgramUniform3uiv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glProgramUniform3uiv(GLuint "
        "program, GLint location, GLsizei count, const GLuint *value)': "
        "names 'GLuint', which has no cute class yet.")

  @staticmethod
  def glProgramUniform4dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glProgramUniform4dv(GLuint
    program, GLint location, GLsizei count, const GLdouble *value)': names
    'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glProgramUniform4dv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glProgramUniform4dv(GLuint "
        "program, GLint location, GLsizei count, const GLdouble *value)': "
        "names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glProgramUniform4fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glProgramUniform4fv(GLuint
    program, GLint location, GLsizei count, const GLfloat *value)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glProgramUniform4fv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glProgramUniform4fv(GLuint "
        "program, GLint location, GLsizei count, const GLfloat *value)': "
        "names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glProgramUniform4iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glProgramUniform4iv(GLuint
    program, GLint location, GLsizei count, const GLint *value)': names
    'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glProgramUniform4iv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glProgramUniform4iv(GLuint "
        "program, GLint location, GLsizei count, const GLint *value)': "
        "names 'GLint', which has no cute class yet.")

  @staticmethod
  def glProgramUniform4uiv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glProgramUniform4uiv(GLuint program,
    GLint location, GLsizei count, const GLuint *value)': names 'GLuint',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glProgramUniform4uiv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glProgramUniform4uiv(GLuint "
        "program, GLint location, GLsizei count, const GLuint *value)': "
        "names 'GLuint', which has no cute class yet.")

  @staticmethod
  def glProgramUniformMatrix2dv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glProgramUniformMatrix2dv(GLuint
    program, GLint location, GLsizei count, GLboolean transpose, const
    GLdouble *value)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glProgramUniformMatrix2dv' has "
        "no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glProgramUniformMatrix2dv(GLuin"
        "t program, GLint location, GLsizei count, GLboolean transpose, "
        "const GLdouble *value)': names 'GLdouble', which has no cute class "
        "yet.")

  @staticmethod
  def glProgramUniformMatrix2fv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glProgramUniformMatrix2fv(GLuint
    program, GLint location, GLsizei count, GLboolean transpose, const
    GLfloat *value)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glProgramUniformMatrix2fv' has "
        "no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glProgramUniformMatrix2fv(GLuin"
        "t program, GLint location, GLsizei count, GLboolean transpose, "
        "const GLfloat *value)': names 'GLfloat', which has no cute class "
        "yet.")

  @staticmethod
  def glProgramUniformMatrix2x3dv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glProgramUniformMatrix2x3dv(GLuint
    program, GLint location, GLsizei count, GLboolean transpose, const
    GLdouble *value)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glProgramUniformMatrix2x3dv' "
        "has no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glProgramUniformMatrix2x3dv(GLu"
        "int program, GLint location, GLsizei count, GLboolean transpose, "
        "const GLdouble *value)': names 'GLdouble', which has no cute class "
        "yet.")

  @staticmethod
  def glProgramUniformMatrix2x3fv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glProgramUniformMatrix2x3fv(GLuint
    program, GLint location, GLsizei count, GLboolean transpose, const
    GLfloat *value)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glProgramUniformMatrix2x3fv' "
        "has no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glProgramUniformMatrix2x3fv(GLu"
        "int program, GLint location, GLsizei count, GLboolean transpose, "
        "const GLfloat *value)': names 'GLfloat', which has no cute class "
        "yet.")

  @staticmethod
  def glProgramUniformMatrix2x4dv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glProgramUniformMatrix2x4dv(GLuint
    program, GLint location, GLsizei count, GLboolean transpose, const
    GLdouble *value)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glProgramUniformMatrix2x4dv' "
        "has no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glProgramUniformMatrix2x4dv(GLu"
        "int program, GLint location, GLsizei count, GLboolean transpose, "
        "const GLdouble *value)': names 'GLdouble', which has no cute class "
        "yet.")

  @staticmethod
  def glProgramUniformMatrix2x4fv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glProgramUniformMatrix2x4fv(GLuint
    program, GLint location, GLsizei count, GLboolean transpose, const
    GLfloat *value)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glProgramUniformMatrix2x4fv' "
        "has no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glProgramUniformMatrix2x4fv(GLu"
        "int program, GLint location, GLsizei count, GLboolean transpose, "
        "const GLfloat *value)': names 'GLfloat', which has no cute class "
        "yet.")

  @staticmethod
  def glProgramUniformMatrix3dv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glProgramUniformMatrix3dv(GLuint
    program, GLint location, GLsizei count, GLboolean transpose, const
    GLdouble *value)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glProgramUniformMatrix3dv' has "
        "no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glProgramUniformMatrix3dv(GLuin"
        "t program, GLint location, GLsizei count, GLboolean transpose, "
        "const GLdouble *value)': names 'GLdouble', which has no cute class "
        "yet.")

  @staticmethod
  def glProgramUniformMatrix3fv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glProgramUniformMatrix3fv(GLuint
    program, GLint location, GLsizei count, GLboolean transpose, const
    GLfloat *value)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glProgramUniformMatrix3fv' has "
        "no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glProgramUniformMatrix3fv(GLuin"
        "t program, GLint location, GLsizei count, GLboolean transpose, "
        "const GLfloat *value)': names 'GLfloat', which has no cute class "
        "yet.")

  @staticmethod
  def glProgramUniformMatrix3x2dv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glProgramUniformMatrix3x2dv(GLuint
    program, GLint location, GLsizei count, GLboolean transpose, const
    GLdouble *value)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glProgramUniformMatrix3x2dv' "
        "has no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glProgramUniformMatrix3x2dv(GLu"
        "int program, GLint location, GLsizei count, GLboolean transpose, "
        "const GLdouble *value)': names 'GLdouble', which has no cute class "
        "yet.")

  @staticmethod
  def glProgramUniformMatrix3x2fv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glProgramUniformMatrix3x2fv(GLuint
    program, GLint location, GLsizei count, GLboolean transpose, const
    GLfloat *value)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glProgramUniformMatrix3x2fv' "
        "has no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glProgramUniformMatrix3x2fv(GLu"
        "int program, GLint location, GLsizei count, GLboolean transpose, "
        "const GLfloat *value)': names 'GLfloat', which has no cute class "
        "yet.")

  @staticmethod
  def glProgramUniformMatrix3x4dv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glProgramUniformMatrix3x4dv(GLuint
    program, GLint location, GLsizei count, GLboolean transpose, const
    GLdouble *value)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glProgramUniformMatrix3x4dv' "
        "has no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glProgramUniformMatrix3x4dv(GLu"
        "int program, GLint location, GLsizei count, GLboolean transpose, "
        "const GLdouble *value)': names 'GLdouble', which has no cute class "
        "yet.")

  @staticmethod
  def glProgramUniformMatrix3x4fv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glProgramUniformMatrix3x4fv(GLuint
    program, GLint location, GLsizei count, GLboolean transpose, const
    GLfloat *value)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glProgramUniformMatrix3x4fv' "
        "has no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glProgramUniformMatrix3x4fv(GLu"
        "int program, GLint location, GLsizei count, GLboolean transpose, "
        "const GLfloat *value)': names 'GLfloat', which has no cute class "
        "yet.")

  @staticmethod
  def glProgramUniformMatrix4dv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glProgramUniformMatrix4dv(GLuint
    program, GLint location, GLsizei count, GLboolean transpose, const
    GLdouble *value)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glProgramUniformMatrix4dv' has "
        "no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glProgramUniformMatrix4dv(GLuin"
        "t program, GLint location, GLsizei count, GLboolean transpose, "
        "const GLdouble *value)': names 'GLdouble', which has no cute class "
        "yet.")

  @staticmethod
  def glProgramUniformMatrix4fv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glProgramUniformMatrix4fv(GLuint
    program, GLint location, GLsizei count, GLboolean transpose, const
    GLfloat *value)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glProgramUniformMatrix4fv' has "
        "no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glProgramUniformMatrix4fv(GLuin"
        "t program, GLint location, GLsizei count, GLboolean transpose, "
        "const GLfloat *value)': names 'GLfloat', which has no cute class "
        "yet.")

  @staticmethod
  def glProgramUniformMatrix4x2dv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glProgramUniformMatrix4x2dv(GLuint
    program, GLint location, GLsizei count, GLboolean transpose, const
    GLdouble *value)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glProgramUniformMatrix4x2dv' "
        "has no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glProgramUniformMatrix4x2dv(GLu"
        "int program, GLint location, GLsizei count, GLboolean transpose, "
        "const GLdouble *value)': names 'GLdouble', which has no cute class "
        "yet.")

  @staticmethod
  def glProgramUniformMatrix4x2fv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glProgramUniformMatrix4x2fv(GLuint
    program, GLint location, GLsizei count, GLboolean transpose, const
    GLfloat *value)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glProgramUniformMatrix4x2fv' "
        "has no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glProgramUniformMatrix4x2fv(GLu"
        "int program, GLint location, GLsizei count, GLboolean transpose, "
        "const GLfloat *value)': names 'GLfloat', which has no cute class "
        "yet.")

  @staticmethod
  def glProgramUniformMatrix4x3dv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glProgramUniformMatrix4x3dv(GLuint
    program, GLint location, GLsizei count, GLboolean transpose, const
    GLdouble *value)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glProgramUniformMatrix4x3dv' "
        "has no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glProgramUniformMatrix4x3dv(GLu"
        "int program, GLint location, GLsizei count, GLboolean transpose, "
        "const GLdouble *value)': names 'GLdouble', which has no cute class "
        "yet.")

  @staticmethod
  def glProgramUniformMatrix4x3fv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glProgramUniformMatrix4x3fv(GLuint
    program, GLint location, GLsizei count, GLboolean transpose, const
    GLfloat *value)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glProgramUniformMatrix4x3fv' "
        "has no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glProgramUniformMatrix4x3fv(GLu"
        "int program, GLint location, GLsizei count, GLboolean transpose, "
        "const GLfloat *value)': names 'GLfloat', which has no cute class "
        "yet.")

  @staticmethod
  def glRasterPos2dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glRasterPos2dv(const
    GLdouble *v)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glRasterPos2dv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glRasterPos2dv(const GLdouble "
        "*v)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glRasterPos2fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glRasterPos2fv(const
    GLfloat *v)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glRasterPos2fv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glRasterPos2fv(const GLfloat "
        "*v)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glRasterPos2iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glRasterPos2iv(const GLint
    *v)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glRasterPos2iv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glRasterPos2iv(const GLint "
        "*v)': names 'GLint', which has no cute class yet.")

  @staticmethod
  def glRasterPos2sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glRasterPos2sv(const
    GLshort *v)': names 'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glRasterPos2sv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glRasterPos2sv(const GLshort "
        "*v)': names 'GLshort', which has no cute class yet.")

  @staticmethod
  def glRasterPos3dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glRasterPos3dv(const
    GLdouble *v)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glRasterPos3dv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glRasterPos3dv(const GLdouble "
        "*v)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glRasterPos3fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glRasterPos3fv(const
    GLfloat *v)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glRasterPos3fv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glRasterPos3fv(const GLfloat "
        "*v)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glRasterPos3iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glRasterPos3iv(const GLint
    *v)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glRasterPos3iv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glRasterPos3iv(const GLint "
        "*v)': names 'GLint', which has no cute class yet.")

  @staticmethod
  def glRasterPos3sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glRasterPos3sv(const
    GLshort *v)': names 'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glRasterPos3sv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glRasterPos3sv(const GLshort "
        "*v)': names 'GLshort', which has no cute class yet.")

  @staticmethod
  def glRasterPos4dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glRasterPos4dv(const
    GLdouble *v)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glRasterPos4dv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glRasterPos4dv(const GLdouble "
        "*v)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glRasterPos4fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glRasterPos4fv(const
    GLfloat *v)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glRasterPos4fv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glRasterPos4fv(const GLfloat "
        "*v)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glRasterPos4iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glRasterPos4iv(const GLint
    *v)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glRasterPos4iv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glRasterPos4iv(const GLint "
        "*v)': names 'GLint', which has no cute class yet.")

  @staticmethod
  def glRasterPos4sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glRasterPos4sv(const
    GLshort *v)': names 'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glRasterPos4sv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glRasterPos4sv(const GLshort "
        "*v)': names 'GLshort', which has no cute class yet.")

  @staticmethod
  def glReadPixels(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glReadPixels(GLint x,
    GLint y, GLsizei width, GLsizei height, GLenum format, GLenum type,
    GLvoid *pixels)': names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glReadPixels' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glReadPixels(GLint x, GLint y, "
        "GLsizei width, GLsizei height, GLenum format, GLenum type, GLvoid "
        "*pixels)': names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glRectdv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glRectdv(const GLdouble
    *v1, const GLdouble *v2)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glRectdv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_3_Compatibility::glRectdv(const "
        "GLdouble *v1, const GLdouble *v2)': names 'GLdouble', which has no "
        "cute class yet.")

  @staticmethod
  def glRectfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glRectfv(const GLfloat
    *v1, const GLfloat *v2)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glRectfv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_3_Compatibility::glRectfv(const "
        "GLfloat *v1, const GLfloat *v2)': names 'GLfloat', which has no "
        "cute class yet.")

  @staticmethod
  def glRectiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glRectiv(const GLint *v1,
    const GLint *v2)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glRectiv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_3_Compatibility::glRectiv(const "
        "GLint *v1, const GLint *v2)': names 'GLint', which has no cute "
        "class yet.")

  @staticmethod
  def glRectsv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glRectsv(const GLshort
    *v1, const GLshort *v2)': names 'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glRectsv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_4_3_Compatibility::glRectsv(const "
        "GLshort *v1, const GLshort *v2)': names 'GLshort', which has no "
        "cute class yet.")

  @staticmethod
  def glSamplerParameterIiv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glSamplerParameterIiv(GLuint sampler,
    GLenum pname, const GLint *param)': names 'GLint', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glSamplerParameterIiv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glSamplerParameterIiv(GLuint "
        "sampler, GLenum pname, const GLint *param)': names 'GLint', which "
        "has no cute class yet.")

  @staticmethod
  def glSamplerParameterIuiv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glSamplerParameterIuiv(GLuint
    sampler, GLenum pname, const GLuint *param)': names 'GLuint', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glSamplerParameterIuiv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glSamplerParameterIuiv(GLuint "
        "sampler, GLenum pname, const GLuint *param)': names 'GLuint', "
        "which has no cute class yet.")

  @staticmethod
  def glSamplerParameterfv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glSamplerParameterfv(GLuint sampler,
    GLenum pname, const GLfloat *param)': names 'GLfloat', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glSamplerParameterfv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glSamplerParameterfv(GLuint "
        "sampler, GLenum pname, const GLfloat *param)': names 'GLfloat', "
        "which has no cute class yet.")

  @staticmethod
  def glSamplerParameteriv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glSamplerParameteriv(GLuint sampler,
    GLenum pname, const GLint *param)': names 'GLint', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glSamplerParameteriv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glSamplerParameteriv(GLuint "
        "sampler, GLenum pname, const GLint *param)': names 'GLint', which "
        "has no cute class yet.")

  @staticmethod
  def glScissorArrayv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glScissorArrayv(GLuint
    first, GLsizei count, const GLint *v)': names 'GLint', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glScissorArrayv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glScissorArrayv(GLuint first, "
        "GLsizei count, const GLint *v)': names 'GLint', which has no cute "
        "class yet.")

  @staticmethod
  def glScissorIndexedv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glScissorIndexedv(GLuint
    index, const GLint *v)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glScissorIndexedv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glScissorIndexedv(GLuint "
        "index, const GLint *v)': names 'GLint', which has no cute class "
        "yet.")

  @staticmethod
  def glSecondaryColor3bv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glSecondaryColor3bv(const
    GLbyte *v)': names 'GLbyte', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glSecondaryColor3bv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glSecondaryColor3bv(const "
        "GLbyte *v)': names 'GLbyte', which has no cute class yet.")

  @staticmethod
  def glSecondaryColor3dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glSecondaryColor3dv(const
    GLdouble *v)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glSecondaryColor3dv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glSecondaryColor3dv(const "
        "GLdouble *v)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glSecondaryColor3fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glSecondaryColor3fv(const
    GLfloat *v)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glSecondaryColor3fv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glSecondaryColor3fv(const "
        "GLfloat *v)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glSecondaryColor3iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glSecondaryColor3iv(const
    GLint *v)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glSecondaryColor3iv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glSecondaryColor3iv(const "
        "GLint *v)': names 'GLint', which has no cute class yet.")

  @staticmethod
  def glSecondaryColor3sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glSecondaryColor3sv(const
    GLshort *v)': names 'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glSecondaryColor3sv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glSecondaryColor3sv(const "
        "GLshort *v)': names 'GLshort', which has no cute class yet.")

  @staticmethod
  def glSecondaryColor3ubv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glSecondaryColor3ubv(const
    GLubyte *v)': names 'GLubyte', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glSecondaryColor3ubv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glSecondaryColor3ubv(const "
        "GLubyte *v)': names 'GLubyte', which has no cute class yet.")

  @staticmethod
  def glSecondaryColor3uiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glSecondaryColor3uiv(const
    GLuint *v)': names 'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glSecondaryColor3uiv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glSecondaryColor3uiv(const "
        "GLuint *v)': names 'GLuint', which has no cute class yet.")

  @staticmethod
  def glSecondaryColor3usv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glSecondaryColor3usv(const
    GLushort *v)': names 'GLushort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glSecondaryColor3usv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glSecondaryColor3usv(const "
        "GLushort *v)': names 'GLushort', which has no cute class yet.")

  @staticmethod
  def glSecondaryColorP3uiv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glSecondaryColorP3uiv(GLenum type,
    const GLuint *color)': names 'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glSecondaryColorP3uiv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glSecondaryColorP3uiv(GLenum "
        "type, const GLuint *color)': names 'GLuint', which has no cute "
        "class yet.")

  @staticmethod
  def glSecondaryColorPointer(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glSecondaryColorPointer(GLint size,
    GLenum type, GLsizei stride, const GLvoid *pointer)': names 'GLvoid',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glSecondaryColorPointer' has "
        "no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glSecondaryColorPointer(GLint "
        "size, GLenum type, GLsizei stride, const GLvoid *pointer)': names "
        "'GLvoid', which has no cute class yet.")

  @staticmethod
  def glSelectBuffer(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glSelectBuffer(GLsizei
    size, GLuint *buffer)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glSelectBuffer' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glSelectBuffer(GLsizei size, "
        "GLuint *buffer)': takes a number to change where it is.")

  @staticmethod
  def glSeparableFilter2D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glSeparableFilter2D(GLenum
    target, GLenum internalformat, GLsizei width, GLsizei height, GLenum
    format, GLenum type, const GLvoid *row, const GLvoid *column)': names
    'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glSeparableFilter2D' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glSeparableFilter2D(GLenum "
        "target, GLenum internalformat, GLsizei width, GLsizei height, "
        "GLenum format, GLenum type, const GLvoid *row, const GLvoid "
        "*column)': names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glShaderBinary(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glShaderBinary(GLsizei
    count, const GLuint *shaders, GLenum binaryformat, const GLvoid *binary,
    GLsizei length)': names 'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glShaderBinary' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glShaderBinary(GLsizei count, "
        "const GLuint *shaders, GLenum binaryformat, const GLvoid *binary, "
        "GLsizei length)': names 'GLuint', which has no cute class yet.")

  @staticmethod
  def glShaderSource(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glShaderSource(GLuint
    shader, GLsizei count, const GLchar *const *string, const GLint
    *length)': names 'GLchar *const', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glShaderSource' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glShaderSource(GLuint shader, "
        "GLsizei count, const GLchar *const *string, const GLint *length)': "
        "names 'GLchar *const', which has no cute class yet.")

  @staticmethod
  def glTexCoord1dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexCoord1dv(const
    GLdouble *v)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glTexCoord1dv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glTexCoord1dv(const GLdouble "
        "*v)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glTexCoord1fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexCoord1fv(const
    GLfloat *v)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glTexCoord1fv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glTexCoord1fv(const GLfloat "
        "*v)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glTexCoord1iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexCoord1iv(const GLint
    *v)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glTexCoord1iv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glTexCoord1iv(const GLint "
        "*v)': names 'GLint', which has no cute class yet.")

  @staticmethod
  def glTexCoord1sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexCoord1sv(const
    GLshort *v)': names 'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glTexCoord1sv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glTexCoord1sv(const GLshort "
        "*v)': names 'GLshort', which has no cute class yet.")

  @staticmethod
  def glTexCoord2dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexCoord2dv(const
    GLdouble *v)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glTexCoord2dv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glTexCoord2dv(const GLdouble "
        "*v)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glTexCoord2fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexCoord2fv(const
    GLfloat *v)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glTexCoord2fv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glTexCoord2fv(const GLfloat "
        "*v)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glTexCoord2iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexCoord2iv(const GLint
    *v)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glTexCoord2iv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glTexCoord2iv(const GLint "
        "*v)': names 'GLint', which has no cute class yet.")

  @staticmethod
  def glTexCoord2sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexCoord2sv(const
    GLshort *v)': names 'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glTexCoord2sv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glTexCoord2sv(const GLshort "
        "*v)': names 'GLshort', which has no cute class yet.")

  @staticmethod
  def glTexCoord3dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexCoord3dv(const
    GLdouble *v)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glTexCoord3dv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glTexCoord3dv(const GLdouble "
        "*v)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glTexCoord3fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexCoord3fv(const
    GLfloat *v)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glTexCoord3fv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glTexCoord3fv(const GLfloat "
        "*v)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glTexCoord3iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexCoord3iv(const GLint
    *v)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glTexCoord3iv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glTexCoord3iv(const GLint "
        "*v)': names 'GLint', which has no cute class yet.")

  @staticmethod
  def glTexCoord3sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexCoord3sv(const
    GLshort *v)': names 'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glTexCoord3sv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glTexCoord3sv(const GLshort "
        "*v)': names 'GLshort', which has no cute class yet.")

  @staticmethod
  def glTexCoord4dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexCoord4dv(const
    GLdouble *v)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glTexCoord4dv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glTexCoord4dv(const GLdouble "
        "*v)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glTexCoord4fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexCoord4fv(const
    GLfloat *v)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glTexCoord4fv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glTexCoord4fv(const GLfloat "
        "*v)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glTexCoord4iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexCoord4iv(const GLint
    *v)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glTexCoord4iv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glTexCoord4iv(const GLint "
        "*v)': names 'GLint', which has no cute class yet.")

  @staticmethod
  def glTexCoord4sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexCoord4sv(const
    GLshort *v)': names 'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glTexCoord4sv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glTexCoord4sv(const GLshort "
        "*v)': names 'GLshort', which has no cute class yet.")

  @staticmethod
  def glTexCoordP1uiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexCoordP1uiv(GLenum
    type, const GLuint *coords)': names 'GLuint', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glTexCoordP1uiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glTexCoordP1uiv(GLenum type, "
        "const GLuint *coords)': names 'GLuint', which has no cute class "
        "yet.")

  @staticmethod
  def glTexCoordP2uiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexCoordP2uiv(GLenum
    type, const GLuint *coords)': names 'GLuint', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glTexCoordP2uiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glTexCoordP2uiv(GLenum type, "
        "const GLuint *coords)': names 'GLuint', which has no cute class "
        "yet.")

  @staticmethod
  def glTexCoordP3uiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexCoordP3uiv(GLenum
    type, const GLuint *coords)': names 'GLuint', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glTexCoordP3uiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glTexCoordP3uiv(GLenum type, "
        "const GLuint *coords)': names 'GLuint', which has no cute class "
        "yet.")

  @staticmethod
  def glTexCoordP4uiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexCoordP4uiv(GLenum
    type, const GLuint *coords)': names 'GLuint', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glTexCoordP4uiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glTexCoordP4uiv(GLenum type, "
        "const GLuint *coords)': names 'GLuint', which has no cute class "
        "yet.")

  @staticmethod
  def glTexCoordPointer(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexCoordPointer(GLint
    size, GLenum type, GLsizei stride, const GLvoid *pointer)': names
    'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glTexCoordPointer' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glTexCoordPointer(GLint size, "
        "GLenum type, GLsizei stride, const GLvoid *pointer)': names "
        "'GLvoid', which has no cute class yet.")

  @staticmethod
  def glTexEnvfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexEnvfv(GLenum target,
    GLenum pname, const GLfloat *params)': names 'GLfloat', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glTexEnvfv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glTexEnvfv(GLenum target, "
        "GLenum pname, const GLfloat *params)': names 'GLfloat', which has "
        "no cute class yet.")

  @staticmethod
  def glTexEnviv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexEnviv(GLenum target,
    GLenum pname, const GLint *params)': names 'GLint', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glTexEnviv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glTexEnviv(GLenum target, "
        "GLenum pname, const GLint *params)': names 'GLint', which has no "
        "cute class yet.")

  @staticmethod
  def glTexGendv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexGendv(GLenum coord,
    GLenum pname, const GLdouble *params)': names 'GLdouble', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glTexGendv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glTexGendv(GLenum coord, "
        "GLenum pname, const GLdouble *params)': names 'GLdouble', which "
        "has no cute class yet.")

  @staticmethod
  def glTexGenfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexGenfv(GLenum coord,
    GLenum pname, const GLfloat *params)': names 'GLfloat', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glTexGenfv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glTexGenfv(GLenum coord, "
        "GLenum pname, const GLfloat *params)': names 'GLfloat', which has "
        "no cute class yet.")

  @staticmethod
  def glTexGeniv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexGeniv(GLenum coord,
    GLenum pname, const GLint *params)': names 'GLint', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glTexGeniv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glTexGeniv(GLenum coord, "
        "GLenum pname, const GLint *params)': names 'GLint', which has no "
        "cute class yet.")

  @staticmethod
  def glTexImage1D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexImage1D(GLenum
    target, GLint level, GLint internalformat, GLsizei width, GLint border,
    GLenum format, GLenum type, const GLvoid *pixels)': names 'GLvoid', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glTexImage1D' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glTexImage1D(GLenum target, "
        "GLint level, GLint internalformat, GLsizei width, GLint border, "
        "GLenum format, GLenum type, const GLvoid *pixels)': names "
        "'GLvoid', which has no cute class yet.")

  @staticmethod
  def glTexImage2D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexImage2D(GLenum
    target, GLint level, GLint internalformat, GLsizei width, GLsizei height,
    GLint border, GLenum format, GLenum type, const GLvoid *pixels)': names
    'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glTexImage2D' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glTexImage2D(GLenum target, "
        "GLint level, GLint internalformat, GLsizei width, GLsizei height, "
        "GLint border, GLenum format, GLenum type, const GLvoid *pixels)': "
        "names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glTexImage3D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexImage3D(GLenum
    target, GLint level, GLint internalformat, GLsizei width, GLsizei height,
    GLsizei depth, GLint border, GLenum format, GLenum type, const GLvoid
    *pixels)': names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glTexImage3D' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glTexImage3D(GLenum target, "
        "GLint level, GLint internalformat, GLsizei width, GLsizei height, "
        "GLsizei depth, GLint border, GLenum format, GLenum type, const "
        "GLvoid *pixels)': names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glTexParameterIiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexParameterIiv(GLenum
    target, GLenum pname, const GLint *params)': names 'GLint', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glTexParameterIiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glTexParameterIiv(GLenum "
        "target, GLenum pname, const GLint *params)': names 'GLint', which "
        "has no cute class yet.")

  @staticmethod
  def glTexParameterIuiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexParameterIuiv(GLenum
    target, GLenum pname, const GLuint *params)': names 'GLuint', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glTexParameterIuiv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glTexParameterIuiv(GLenum "
        "target, GLenum pname, const GLuint *params)': names 'GLuint', "
        "which has no cute class yet.")

  @staticmethod
  def glTexParameterfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexParameterfv(GLenum
    target, GLenum pname, const GLfloat *params)': names 'GLfloat', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glTexParameterfv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glTexParameterfv(GLenum "
        "target, GLenum pname, const GLfloat *params)': names 'GLfloat', "
        "which has no cute class yet.")

  @staticmethod
  def glTexParameteriv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexParameteriv(GLenum
    target, GLenum pname, const GLint *params)': names 'GLint', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glTexParameteriv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glTexParameteriv(GLenum "
        "target, GLenum pname, const GLint *params)': names 'GLint', which "
        "has no cute class yet.")

  @staticmethod
  def glTexSubImage1D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexSubImage1D(GLenum
    target, GLint level, GLint xoffset, GLsizei width, GLenum format, GLenum
    type, const GLvoid *pixels)': names 'GLvoid', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glTexSubImage1D' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glTexSubImage1D(GLenum target, "
        "GLint level, GLint xoffset, GLsizei width, GLenum format, GLenum "
        "type, const GLvoid *pixels)': names 'GLvoid', which has no cute "
        "class yet.")

  @staticmethod
  def glTexSubImage2D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexSubImage2D(GLenum
    target, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei
    height, GLenum format, GLenum type, const GLvoid *pixels)': names
    'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glTexSubImage2D' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glTexSubImage2D(GLenum target, "
        "GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei "
        "height, GLenum format, GLenum type, const GLvoid *pixels)': names "
        "'GLvoid', which has no cute class yet.")

  @staticmethod
  def glTexSubImage3D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glTexSubImage3D(GLenum
    target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei
    width, GLsizei height, GLsizei depth, GLenum format, GLenum type, const
    GLvoid *pixels)': names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glTexSubImage3D' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glTexSubImage3D(GLenum target, "
        "GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei "
        "width, GLsizei height, GLsizei depth, GLenum format, GLenum type, "
        "const GLvoid *pixels)': names 'GLvoid', which has no cute class "
        "yet.")

  @staticmethod
  def glTransformFeedbackVaryings(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glTransformFeedbackVaryings(GLuint
    program, GLsizei count, const GLchar *const *varyings, GLenum
    bufferMode)': names 'GLchar *const', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glTransformFeedbackVaryings' "
        "has no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glTransformFeedbackVaryings(GLu"
        "int program, GLsizei count, const GLchar *const *varyings, GLenum "
        "bufferMode)': names 'GLchar *const', which has no cute class yet.")

  @staticmethod
  def glUniform1dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniform1dv(GLint
    location, GLsizei count, const GLdouble *value)': names 'GLdouble', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glUniform1dv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glUniform1dv(GLint location, "
        "GLsizei count, const GLdouble *value)': names 'GLdouble', which "
        "has no cute class yet.")

  @staticmethod
  def glUniform1fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniform1fv(GLint
    location, GLsizei count, const GLfloat *value)': names 'GLfloat', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glUniform1fv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glUniform1fv(GLint location, "
        "GLsizei count, const GLfloat *value)': names 'GLfloat', which has "
        "no cute class yet.")

  @staticmethod
  def glUniform1iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniform1iv(GLint
    location, GLsizei count, const GLint *value)': names 'GLint', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glUniform1iv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glUniform1iv(GLint location, "
        "GLsizei count, const GLint *value)': names 'GLint', which has no "
        "cute class yet.")

  @staticmethod
  def glUniform1uiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniform1uiv(GLint
    location, GLsizei count, const GLuint *value)': names 'GLuint', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glUniform1uiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glUniform1uiv(GLint location, "
        "GLsizei count, const GLuint *value)': names 'GLuint', which has no "
        "cute class yet.")

  @staticmethod
  def glUniform2dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniform2dv(GLint
    location, GLsizei count, const GLdouble *value)': names 'GLdouble', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glUniform2dv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glUniform2dv(GLint location, "
        "GLsizei count, const GLdouble *value)': names 'GLdouble', which "
        "has no cute class yet.")

  @staticmethod
  def glUniform2fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniform2fv(GLint
    location, GLsizei count, const GLfloat *value)': names 'GLfloat', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glUniform2fv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glUniform2fv(GLint location, "
        "GLsizei count, const GLfloat *value)': names 'GLfloat', which has "
        "no cute class yet.")

  @staticmethod
  def glUniform2iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniform2iv(GLint
    location, GLsizei count, const GLint *value)': names 'GLint', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glUniform2iv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glUniform2iv(GLint location, "
        "GLsizei count, const GLint *value)': names 'GLint', which has no "
        "cute class yet.")

  @staticmethod
  def glUniform2uiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniform2uiv(GLint
    location, GLsizei count, const GLuint *value)': names 'GLuint', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glUniform2uiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glUniform2uiv(GLint location, "
        "GLsizei count, const GLuint *value)': names 'GLuint', which has no "
        "cute class yet.")

  @staticmethod
  def glUniform3dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniform3dv(GLint
    location, GLsizei count, const GLdouble *value)': names 'GLdouble', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glUniform3dv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glUniform3dv(GLint location, "
        "GLsizei count, const GLdouble *value)': names 'GLdouble', which "
        "has no cute class yet.")

  @staticmethod
  def glUniform3fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniform3fv(GLint
    location, GLsizei count, const GLfloat *value)': names 'GLfloat', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glUniform3fv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glUniform3fv(GLint location, "
        "GLsizei count, const GLfloat *value)': names 'GLfloat', which has "
        "no cute class yet.")

  @staticmethod
  def glUniform3iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniform3iv(GLint
    location, GLsizei count, const GLint *value)': names 'GLint', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glUniform3iv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glUniform3iv(GLint location, "
        "GLsizei count, const GLint *value)': names 'GLint', which has no "
        "cute class yet.")

  @staticmethod
  def glUniform3uiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniform3uiv(GLint
    location, GLsizei count, const GLuint *value)': names 'GLuint', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glUniform3uiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glUniform3uiv(GLint location, "
        "GLsizei count, const GLuint *value)': names 'GLuint', which has no "
        "cute class yet.")

  @staticmethod
  def glUniform4dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniform4dv(GLint
    location, GLsizei count, const GLdouble *value)': names 'GLdouble', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glUniform4dv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glUniform4dv(GLint location, "
        "GLsizei count, const GLdouble *value)': names 'GLdouble', which "
        "has no cute class yet.")

  @staticmethod
  def glUniform4fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniform4fv(GLint
    location, GLsizei count, const GLfloat *value)': names 'GLfloat', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glUniform4fv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glUniform4fv(GLint location, "
        "GLsizei count, const GLfloat *value)': names 'GLfloat', which has "
        "no cute class yet.")

  @staticmethod
  def glUniform4iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniform4iv(GLint
    location, GLsizei count, const GLint *value)': names 'GLint', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glUniform4iv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glUniform4iv(GLint location, "
        "GLsizei count, const GLint *value)': names 'GLint', which has no "
        "cute class yet.")

  @staticmethod
  def glUniform4uiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniform4uiv(GLint
    location, GLsizei count, const GLuint *value)': names 'GLuint', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glUniform4uiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glUniform4uiv(GLint location, "
        "GLsizei count, const GLuint *value)': names 'GLuint', which has no "
        "cute class yet.")

  @staticmethod
  def glUniformMatrix2dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniformMatrix2dv(GLint
    location, GLsizei count, GLboolean transpose, const GLdouble *value)':
    names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glUniformMatrix2dv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glUniformMatrix2dv(GLint "
        "location, GLsizei count, GLboolean transpose, const GLdouble "
        "*value)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glUniformMatrix2fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniformMatrix2fv(GLint
    location, GLsizei count, GLboolean transpose, const GLfloat *value)':
    names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glUniformMatrix2fv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glUniformMatrix2fv(GLint "
        "location, GLsizei count, GLboolean transpose, const GLfloat "
        "*value)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glUniformMatrix2x3dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniformMatrix2x3dv(GLint
    location, GLsizei count, GLboolean transpose, const GLdouble *value)':
    names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glUniformMatrix2x3dv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glUniformMatrix2x3dv(GLint "
        "location, GLsizei count, GLboolean transpose, const GLdouble "
        "*value)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glUniformMatrix2x3fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniformMatrix2x3fv(GLint
    location, GLsizei count, GLboolean transpose, const GLfloat *value)':
    names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glUniformMatrix2x3fv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glUniformMatrix2x3fv(GLint "
        "location, GLsizei count, GLboolean transpose, const GLfloat "
        "*value)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glUniformMatrix2x4dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniformMatrix2x4dv(GLint
    location, GLsizei count, GLboolean transpose, const GLdouble *value)':
    names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glUniformMatrix2x4dv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glUniformMatrix2x4dv(GLint "
        "location, GLsizei count, GLboolean transpose, const GLdouble "
        "*value)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glUniformMatrix2x4fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniformMatrix2x4fv(GLint
    location, GLsizei count, GLboolean transpose, const GLfloat *value)':
    names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glUniformMatrix2x4fv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glUniformMatrix2x4fv(GLint "
        "location, GLsizei count, GLboolean transpose, const GLfloat "
        "*value)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glUniformMatrix3dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniformMatrix3dv(GLint
    location, GLsizei count, GLboolean transpose, const GLdouble *value)':
    names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glUniformMatrix3dv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glUniformMatrix3dv(GLint "
        "location, GLsizei count, GLboolean transpose, const GLdouble "
        "*value)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glUniformMatrix3fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniformMatrix3fv(GLint
    location, GLsizei count, GLboolean transpose, const GLfloat *value)':
    names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glUniformMatrix3fv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glUniformMatrix3fv(GLint "
        "location, GLsizei count, GLboolean transpose, const GLfloat "
        "*value)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glUniformMatrix3x2dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniformMatrix3x2dv(GLint
    location, GLsizei count, GLboolean transpose, const GLdouble *value)':
    names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glUniformMatrix3x2dv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glUniformMatrix3x2dv(GLint "
        "location, GLsizei count, GLboolean transpose, const GLdouble "
        "*value)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glUniformMatrix3x2fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniformMatrix3x2fv(GLint
    location, GLsizei count, GLboolean transpose, const GLfloat *value)':
    names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glUniformMatrix3x2fv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glUniformMatrix3x2fv(GLint "
        "location, GLsizei count, GLboolean transpose, const GLfloat "
        "*value)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glUniformMatrix3x4dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniformMatrix3x4dv(GLint
    location, GLsizei count, GLboolean transpose, const GLdouble *value)':
    names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glUniformMatrix3x4dv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glUniformMatrix3x4dv(GLint "
        "location, GLsizei count, GLboolean transpose, const GLdouble "
        "*value)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glUniformMatrix3x4fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniformMatrix3x4fv(GLint
    location, GLsizei count, GLboolean transpose, const GLfloat *value)':
    names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glUniformMatrix3x4fv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glUniformMatrix3x4fv(GLint "
        "location, GLsizei count, GLboolean transpose, const GLfloat "
        "*value)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glUniformMatrix4dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniformMatrix4dv(GLint
    location, GLsizei count, GLboolean transpose, const GLdouble *value)':
    names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glUniformMatrix4dv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glUniformMatrix4dv(GLint "
        "location, GLsizei count, GLboolean transpose, const GLdouble "
        "*value)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glUniformMatrix4fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniformMatrix4fv(GLint
    location, GLsizei count, GLboolean transpose, const GLfloat *value)':
    names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glUniformMatrix4fv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glUniformMatrix4fv(GLint "
        "location, GLsizei count, GLboolean transpose, const GLfloat "
        "*value)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glUniformMatrix4x2dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniformMatrix4x2dv(GLint
    location, GLsizei count, GLboolean transpose, const GLdouble *value)':
    names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glUniformMatrix4x2dv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glUniformMatrix4x2dv(GLint "
        "location, GLsizei count, GLboolean transpose, const GLdouble "
        "*value)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glUniformMatrix4x2fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniformMatrix4x2fv(GLint
    location, GLsizei count, GLboolean transpose, const GLfloat *value)':
    names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glUniformMatrix4x2fv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glUniformMatrix4x2fv(GLint "
        "location, GLsizei count, GLboolean transpose, const GLfloat "
        "*value)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glUniformMatrix4x3dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniformMatrix4x3dv(GLint
    location, GLsizei count, GLboolean transpose, const GLdouble *value)':
    names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glUniformMatrix4x3dv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glUniformMatrix4x3dv(GLint "
        "location, GLsizei count, GLboolean transpose, const GLdouble "
        "*value)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glUniformMatrix4x3fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glUniformMatrix4x3fv(GLint
    location, GLsizei count, GLboolean transpose, const GLfloat *value)':
    names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glUniformMatrix4x3fv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glUniformMatrix4x3fv(GLint "
        "location, GLsizei count, GLboolean transpose, const GLfloat "
        "*value)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glUniformSubroutinesuiv(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glUniformSubroutinesuiv(GLenum
    shadertype, GLsizei count, const GLuint *indices)': names 'GLuint', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glUniformSubroutinesuiv' has "
        "no cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glUniformSubroutinesuiv(GLenum "
        "shadertype, GLsizei count, const GLuint *indices)': names "
        "'GLuint', which has no cute class yet.")

  @staticmethod
  def glVertex2dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertex2dv(const GLdouble
    *v)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glVertex2dv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glVertex2dv(const GLdouble "
        "*v)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glVertex2fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertex2fv(const GLfloat
    *v)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glVertex2fv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glVertex2fv(const GLfloat "
        "*v)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glVertex2iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertex2iv(const GLint
    *v)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glVertex2iv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glVertex2iv(const GLint *v)': "
        "names 'GLint', which has no cute class yet.")

  @staticmethod
  def glVertex2sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertex2sv(const GLshort
    *v)': names 'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glVertex2sv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glVertex2sv(const GLshort "
        "*v)': names 'GLshort', which has no cute class yet.")

  @staticmethod
  def glVertex3dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertex3dv(const GLdouble
    *v)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glVertex3dv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glVertex3dv(const GLdouble "
        "*v)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glVertex3fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertex3fv(const GLfloat
    *v)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glVertex3fv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glVertex3fv(const GLfloat "
        "*v)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glVertex3iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertex3iv(const GLint
    *v)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glVertex3iv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glVertex3iv(const GLint *v)': "
        "names 'GLint', which has no cute class yet.")

  @staticmethod
  def glVertex3sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertex3sv(const GLshort
    *v)': names 'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glVertex3sv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glVertex3sv(const GLshort "
        "*v)': names 'GLshort', which has no cute class yet.")

  @staticmethod
  def glVertex4dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertex4dv(const GLdouble
    *v)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glVertex4dv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glVertex4dv(const GLdouble "
        "*v)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glVertex4fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertex4fv(const GLfloat
    *v)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glVertex4fv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glVertex4fv(const GLfloat "
        "*v)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glVertex4iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertex4iv(const GLint
    *v)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glVertex4iv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glVertex4iv(const GLint *v)': "
        "names 'GLint', which has no cute class yet.")

  @staticmethod
  def glVertex4sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertex4sv(const GLshort
    *v)': names 'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glVertex4sv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glVertex4sv(const GLshort "
        "*v)': names 'GLshort', which has no cute class yet.")

  @staticmethod
  def glVertexAttrib1dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttrib1dv(GLuint
    index, const GLdouble *v)': names 'GLdouble', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glVertexAttrib1dv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glVertexAttrib1dv(GLuint "
        "index, const GLdouble *v)': names 'GLdouble', which has no cute "
        "class yet.")

  @staticmethod
  def glVertexAttrib1fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttrib1fv(GLuint
    index, const GLfloat *v)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glVertexAttrib1fv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glVertexAttrib1fv(GLuint "
        "index, const GLfloat *v)': names 'GLfloat', which has no cute "
        "class yet.")

  @staticmethod
  def glVertexAttrib1sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttrib1sv(GLuint
    index, const GLshort *v)': names 'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glVertexAttrib1sv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glVertexAttrib1sv(GLuint "
        "index, const GLshort *v)': names 'GLshort', which has no cute "
        "class yet.")

  @staticmethod
  def glVertexAttrib2dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttrib2dv(GLuint
    index, const GLdouble *v)': names 'GLdouble', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glVertexAttrib2dv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glVertexAttrib2dv(GLuint "
        "index, const GLdouble *v)': names 'GLdouble', which has no cute "
        "class yet.")

  @staticmethod
  def glVertexAttrib2fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttrib2fv(GLuint
    index, const GLfloat *v)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glVertexAttrib2fv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glVertexAttrib2fv(GLuint "
        "index, const GLfloat *v)': names 'GLfloat', which has no cute "
        "class yet.")

  @staticmethod
  def glVertexAttrib2sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttrib2sv(GLuint
    index, const GLshort *v)': names 'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glVertexAttrib2sv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glVertexAttrib2sv(GLuint "
        "index, const GLshort *v)': names 'GLshort', which has no cute "
        "class yet.")

  @staticmethod
  def glVertexAttrib3dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttrib3dv(GLuint
    index, const GLdouble *v)': names 'GLdouble', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glVertexAttrib3dv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glVertexAttrib3dv(GLuint "
        "index, const GLdouble *v)': names 'GLdouble', which has no cute "
        "class yet.")

  @staticmethod
  def glVertexAttrib3fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttrib3fv(GLuint
    index, const GLfloat *v)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glVertexAttrib3fv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glVertexAttrib3fv(GLuint "
        "index, const GLfloat *v)': names 'GLfloat', which has no cute "
        "class yet.")

  @staticmethod
  def glVertexAttrib3sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttrib3sv(GLuint
    index, const GLshort *v)': names 'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glVertexAttrib3sv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glVertexAttrib3sv(GLuint "
        "index, const GLshort *v)': names 'GLshort', which has no cute "
        "class yet.")

  @staticmethod
  def glVertexAttrib4Nbv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttrib4Nbv(GLuint
    index, const GLbyte *v)': names 'GLbyte', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glVertexAttrib4Nbv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glVertexAttrib4Nbv(GLuint "
        "index, const GLbyte *v)': names 'GLbyte', which has no cute class "
        "yet.")

  @staticmethod
  def glVertexAttrib4Niv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttrib4Niv(GLuint
    index, const GLint *v)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glVertexAttrib4Niv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glVertexAttrib4Niv(GLuint "
        "index, const GLint *v)': names 'GLint', which has no cute class "
        "yet.")

  @staticmethod
  def glVertexAttrib4Nsv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttrib4Nsv(GLuint
    index, const GLshort *v)': names 'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glVertexAttrib4Nsv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glVertexAttrib4Nsv(GLuint "
        "index, const GLshort *v)': names 'GLshort', which has no cute "
        "class yet.")

  @staticmethod
  def glVertexAttrib4Nubv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttrib4Nubv(GLuint
    index, const GLubyte *v)': names 'GLubyte', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glVertexAttrib4Nubv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glVertexAttrib4Nubv(GLuint "
        "index, const GLubyte *v)': names 'GLubyte', which has no cute "
        "class yet.")

  @staticmethod
  def glVertexAttrib4Nuiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttrib4Nuiv(GLuint
    index, const GLuint *v)': names 'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glVertexAttrib4Nuiv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glVertexAttrib4Nuiv(GLuint "
        "index, const GLuint *v)': names 'GLuint', which has no cute class "
        "yet.")

  @staticmethod
  def glVertexAttrib4Nusv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttrib4Nusv(GLuint
    index, const GLushort *v)': names 'GLushort', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glVertexAttrib4Nusv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glVertexAttrib4Nusv(GLuint "
        "index, const GLushort *v)': names 'GLushort', which has no cute "
        "class yet.")

  @staticmethod
  def glVertexAttrib4bv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttrib4bv(GLuint
    index, const GLbyte *v)': names 'GLbyte', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glVertexAttrib4bv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glVertexAttrib4bv(GLuint "
        "index, const GLbyte *v)': names 'GLbyte', which has no cute class "
        "yet.")

  @staticmethod
  def glVertexAttrib4dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttrib4dv(GLuint
    index, const GLdouble *v)': names 'GLdouble', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glVertexAttrib4dv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glVertexAttrib4dv(GLuint "
        "index, const GLdouble *v)': names 'GLdouble', which has no cute "
        "class yet.")

  @staticmethod
  def glVertexAttrib4fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttrib4fv(GLuint
    index, const GLfloat *v)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glVertexAttrib4fv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glVertexAttrib4fv(GLuint "
        "index, const GLfloat *v)': names 'GLfloat', which has no cute "
        "class yet.")

  @staticmethod
  def glVertexAttrib4iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttrib4iv(GLuint
    index, const GLint *v)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glVertexAttrib4iv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glVertexAttrib4iv(GLuint "
        "index, const GLint *v)': names 'GLint', which has no cute class "
        "yet.")

  @staticmethod
  def glVertexAttrib4sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttrib4sv(GLuint
    index, const GLshort *v)': names 'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glVertexAttrib4sv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glVertexAttrib4sv(GLuint "
        "index, const GLshort *v)': names 'GLshort', which has no cute "
        "class yet.")

  @staticmethod
  def glVertexAttrib4ubv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttrib4ubv(GLuint
    index, const GLubyte *v)': names 'GLubyte', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glVertexAttrib4ubv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glVertexAttrib4ubv(GLuint "
        "index, const GLubyte *v)': names 'GLubyte', which has no cute "
        "class yet.")

  @staticmethod
  def glVertexAttrib4uiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttrib4uiv(GLuint
    index, const GLuint *v)': names 'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glVertexAttrib4uiv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glVertexAttrib4uiv(GLuint "
        "index, const GLuint *v)': names 'GLuint', which has no cute class "
        "yet.")

  @staticmethod
  def glVertexAttrib4usv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttrib4usv(GLuint
    index, const GLushort *v)': names 'GLushort', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glVertexAttrib4usv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glVertexAttrib4usv(GLuint "
        "index, const GLushort *v)': names 'GLushort', which has no cute "
        "class yet.")

  @staticmethod
  def glVertexAttribI1iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttribI1iv(GLuint
    index, const GLint *v)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glVertexAttribI1iv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glVertexAttribI1iv(GLuint "
        "index, const GLint *v)': names 'GLint', which has no cute class "
        "yet.")

  @staticmethod
  def glVertexAttribI1uiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttribI1uiv(GLuint
    index, const GLuint *v)': names 'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glVertexAttribI1uiv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glVertexAttribI1uiv(GLuint "
        "index, const GLuint *v)': names 'GLuint', which has no cute class "
        "yet.")

  @staticmethod
  def glVertexAttribI2iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttribI2iv(GLuint
    index, const GLint *v)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glVertexAttribI2iv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glVertexAttribI2iv(GLuint "
        "index, const GLint *v)': names 'GLint', which has no cute class "
        "yet.")

  @staticmethod
  def glVertexAttribI2uiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttribI2uiv(GLuint
    index, const GLuint *v)': names 'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glVertexAttribI2uiv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glVertexAttribI2uiv(GLuint "
        "index, const GLuint *v)': names 'GLuint', which has no cute class "
        "yet.")

  @staticmethod
  def glVertexAttribI3iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttribI3iv(GLuint
    index, const GLint *v)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glVertexAttribI3iv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glVertexAttribI3iv(GLuint "
        "index, const GLint *v)': names 'GLint', which has no cute class "
        "yet.")

  @staticmethod
  def glVertexAttribI3uiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttribI3uiv(GLuint
    index, const GLuint *v)': names 'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glVertexAttribI3uiv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glVertexAttribI3uiv(GLuint "
        "index, const GLuint *v)': names 'GLuint', which has no cute class "
        "yet.")

  @staticmethod
  def glVertexAttribI4bv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttribI4bv(GLuint
    index, const GLbyte *v)': names 'GLbyte', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glVertexAttribI4bv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glVertexAttribI4bv(GLuint "
        "index, const GLbyte *v)': names 'GLbyte', which has no cute class "
        "yet.")

  @staticmethod
  def glVertexAttribI4iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttribI4iv(GLuint
    index, const GLint *v)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glVertexAttribI4iv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glVertexAttribI4iv(GLuint "
        "index, const GLint *v)': names 'GLint', which has no cute class "
        "yet.")

  @staticmethod
  def glVertexAttribI4sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttribI4sv(GLuint
    index, const GLshort *v)': names 'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glVertexAttribI4sv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glVertexAttribI4sv(GLuint "
        "index, const GLshort *v)': names 'GLshort', which has no cute "
        "class yet.")

  @staticmethod
  def glVertexAttribI4ubv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttribI4ubv(GLuint
    index, const GLubyte *v)': names 'GLubyte', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glVertexAttribI4ubv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glVertexAttribI4ubv(GLuint "
        "index, const GLubyte *v)': names 'GLubyte', which has no cute "
        "class yet.")

  @staticmethod
  def glVertexAttribI4uiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttribI4uiv(GLuint
    index, const GLuint *v)': names 'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glVertexAttribI4uiv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glVertexAttribI4uiv(GLuint "
        "index, const GLuint *v)': names 'GLuint', which has no cute class "
        "yet.")

  @staticmethod
  def glVertexAttribI4usv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttribI4usv(GLuint
    index, const GLushort *v)': names 'GLushort', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glVertexAttribI4usv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glVertexAttribI4usv(GLuint "
        "index, const GLushort *v)': names 'GLushort', which has no cute "
        "class yet.")

  @staticmethod
  def glVertexAttribIPointer(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glVertexAttribIPointer(GLuint index,
    GLint size, GLenum type, GLsizei stride, const GLvoid *pointer)': names
    'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glVertexAttribIPointer' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glVertexAttribIPointer(GLuint "
        "index, GLint size, GLenum type, GLsizei stride, const GLvoid "
        "*pointer)': names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glVertexAttribL1dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttribL1dv(GLuint
    index, const GLdouble *v)': names 'GLdouble', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glVertexAttribL1dv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glVertexAttribL1dv(GLuint "
        "index, const GLdouble *v)': names 'GLdouble', which has no cute "
        "class yet.")

  @staticmethod
  def glVertexAttribL2dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttribL2dv(GLuint
    index, const GLdouble *v)': names 'GLdouble', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glVertexAttribL2dv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glVertexAttribL2dv(GLuint "
        "index, const GLdouble *v)': names 'GLdouble', which has no cute "
        "class yet.")

  @staticmethod
  def glVertexAttribL3dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttribL3dv(GLuint
    index, const GLdouble *v)': names 'GLdouble', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glVertexAttribL3dv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glVertexAttribL3dv(GLuint "
        "index, const GLdouble *v)': names 'GLdouble', which has no cute "
        "class yet.")

  @staticmethod
  def glVertexAttribL4dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttribL4dv(GLuint
    index, const GLdouble *v)': names 'GLdouble', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glVertexAttribL4dv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glVertexAttribL4dv(GLuint "
        "index, const GLdouble *v)': names 'GLdouble', which has no cute "
        "class yet.")

  @staticmethod
  def glVertexAttribLPointer(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glVertexAttribLPointer(GLuint index,
    GLint size, GLenum type, GLsizei stride, const GLvoid *pointer)': names
    'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glVertexAttribLPointer' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glVertexAttribLPointer(GLuint "
        "index, GLint size, GLenum type, GLsizei stride, const GLvoid "
        "*pointer)': names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glVertexAttribP1uiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttribP1uiv(GLuint
    index, GLenum type, GLboolean normalized, const GLuint *value)': names
    'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glVertexAttribP1uiv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glVertexAttribP1uiv(GLuint "
        "index, GLenum type, GLboolean normalized, const GLuint *value)': "
        "names 'GLuint', which has no cute class yet.")

  @staticmethod
  def glVertexAttribP2uiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttribP2uiv(GLuint
    index, GLenum type, GLboolean normalized, const GLuint *value)': names
    'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glVertexAttribP2uiv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glVertexAttribP2uiv(GLuint "
        "index, GLenum type, GLboolean normalized, const GLuint *value)': "
        "names 'GLuint', which has no cute class yet.")

  @staticmethod
  def glVertexAttribP3uiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttribP3uiv(GLuint
    index, GLenum type, GLboolean normalized, const GLuint *value)': names
    'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glVertexAttribP3uiv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glVertexAttribP3uiv(GLuint "
        "index, GLenum type, GLboolean normalized, const GLuint *value)': "
        "names 'GLuint', which has no cute class yet.")

  @staticmethod
  def glVertexAttribP4uiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexAttribP4uiv(GLuint
    index, GLenum type, GLboolean normalized, const GLuint *value)': names
    'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glVertexAttribP4uiv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glVertexAttribP4uiv(GLuint "
        "index, GLenum type, GLboolean normalized, const GLuint *value)': "
        "names 'GLuint', which has no cute class yet.")

  @staticmethod
  def glVertexAttribPointer(*__, **_) -> Never:
    """
    Qt's 'void
    QOpenGLFunctions_4_3_Compatibility::glVertexAttribPointer(GLuint index,
    GLint size, GLenum type, GLboolean normalized, GLsizei stride, const
    GLvoid *pointer)': names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glVertexAttribPointer' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glVertexAttribPointer(GLuint "
        "index, GLint size, GLenum type, GLboolean normalized, GLsizei "
        "stride, const GLvoid *pointer)': names 'GLvoid', which has no cute "
        "class yet.")

  @staticmethod
  def glVertexP2uiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexP2uiv(GLenum type,
    const GLuint *value)': names 'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glVertexP2uiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glVertexP2uiv(GLenum type, "
        "const GLuint *value)': names 'GLuint', which has no cute class yet."
    )

  @staticmethod
  def glVertexP3uiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexP3uiv(GLenum type,
    const GLuint *value)': names 'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glVertexP3uiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glVertexP3uiv(GLenum type, "
        "const GLuint *value)': names 'GLuint', which has no cute class yet."
    )

  @staticmethod
  def glVertexP4uiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexP4uiv(GLenum type,
    const GLuint *value)': names 'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glVertexP4uiv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glVertexP4uiv(GLenum type, "
        "const GLuint *value)': names 'GLuint', which has no cute class yet."
    )

  @staticmethod
  def glVertexPointer(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glVertexPointer(GLint
    size, GLenum type, GLsizei stride, const GLvoid *pointer)': names
    'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glVertexPointer' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glVertexPointer(GLint size, "
        "GLenum type, GLsizei stride, const GLvoid *pointer)': names "
        "'GLvoid', which has no cute class yet.")

  @staticmethod
  def glViewportArrayv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glViewportArrayv(GLuint
    first, GLsizei count, const GLfloat *v)': names 'GLfloat', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glViewportArrayv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glViewportArrayv(GLuint first, "
        "GLsizei count, const GLfloat *v)': names 'GLfloat', which has no "
        "cute class yet.")

  @staticmethod
  def glViewportIndexedfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glViewportIndexedfv(GLuint
    index, const GLfloat *v)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glViewportIndexedfv' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glViewportIndexedfv(GLuint "
        "index, const GLfloat *v)': names 'GLfloat', which has no cute "
        "class yet.")

  @staticmethod
  def glWaitSync(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glWaitSync(GLsync sync,
    GLbitfield flags, GLuint64 timeout)': names 'struct __GLsync', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glWaitSync' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glWaitSync(GLsync sync, "
        "GLbitfield flags, GLuint64 timeout)': names 'struct __GLsync', "
        "which has no cute class yet.")

  @staticmethod
  def glWindowPos2dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glWindowPos2dv(const
    GLdouble *v)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glWindowPos2dv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glWindowPos2dv(const GLdouble "
        "*v)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glWindowPos2fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glWindowPos2fv(const
    GLfloat *v)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glWindowPos2fv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glWindowPos2fv(const GLfloat "
        "*v)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glWindowPos2iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glWindowPos2iv(const GLint
    *v)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glWindowPos2iv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glWindowPos2iv(const GLint "
        "*v)': names 'GLint', which has no cute class yet.")

  @staticmethod
  def glWindowPos2sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glWindowPos2sv(const
    GLshort *v)': names 'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glWindowPos2sv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glWindowPos2sv(const GLshort "
        "*v)': names 'GLshort', which has no cute class yet.")

  @staticmethod
  def glWindowPos3dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glWindowPos3dv(const
    GLdouble *v)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glWindowPos3dv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glWindowPos3dv(const GLdouble "
        "*v)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glWindowPos3fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glWindowPos3fv(const
    GLfloat *v)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glWindowPos3fv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glWindowPos3fv(const GLfloat "
        "*v)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glWindowPos3iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glWindowPos3iv(const GLint
    *v)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glWindowPos3iv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glWindowPos3iv(const GLint "
        "*v)': names 'GLint', which has no cute class yet.")

  @staticmethod
  def glWindowPos3sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_3_Compatibility::glWindowPos3sv(const
    GLshort *v)': names 'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_3_Compatibility.glWindowPos3sv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_4_3_Compatibility::glWindowPos3sv(const GLshort "
        "*v)': names 'GLshort', which has no cute class yet.")
