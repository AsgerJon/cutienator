"""
QOpenGLFunctions_2_0 binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpenGL/qopenglfunctions_2_0.h, Qt 6.12.0. Changes made here are lost.
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


class QOpenGLFunctions_2_0(QAbstractOpenGLFunctions):
  """
  The cute side of Qt's QOpenGLFunctions_2_0: a plain Python object standing
  in front of one C++ QOpenGLFunctions_2_0.

  It is built on the cute 'QAbstractOpenGLFunctions', as Qt's
  QOpenGLFunctions_2_0 is built on Qt's QAbstractOpenGLFunctions, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QOpenGLFunctions_2_0 that has a ritual and that
  Python can call so far, 284 names in all: 'initializeOpenGLFunctions',
  'glViewport', 'glDepthRange', 'glIsEnabled', 'glGetError', 'glReadBuffer',
  'glPixelStorei', 'glPixelStoref', 'glDepthFunc', 'glStencilOp',
  'glStencilFunc', 'glLogicOp', 'glBlendFunc', 'glFlush', 'glFinish',
  'glEnable', 'glDisable', 'glDepthMask', 'glColorMask', 'glStencilMask',
  'glClearDepth', 'glClearStencil', 'glClearColor', 'glClear',
  'glDrawBuffer', 'glTexParameteri', 'glTexParameterf', 'glScissor',
  'glPolygonMode', 'glPointSize', 'glLineWidth', 'glHint', 'glFrontFace',
  'glCullFace', 'glIndexub', 'glIsTexture', 'glBindTexture',
  'glCopyTexSubImage2D', 'glCopyTexSubImage1D', 'glCopyTexImage2D',
  'glCopyTexImage1D', 'glPolygonOffset', 'glDrawArrays',
  'glCopyTexSubImage3D', 'glBlendEquation', 'glBlendColor',
  'glSampleCoverage', 'glActiveTexture', 'glPointParameteri',
  'glPointParameterf', 'glBlendFuncSeparate', 'glUnmapBuffer', 'glIsBuffer',
  'glBindBuffer', 'glEndQuery', 'glBeginQuery', 'glIsQuery',
  'glValidateProgram', 'glUniform4i', 'glUniform3i', 'glUniform2i',
  'glUniform1i', 'glUniform4f', 'glUniform3f', 'glUniform2f', 'glUniform1f',
  'glUseProgram', 'glLinkProgram', 'glIsShader', 'glIsProgram',
  'glEnableVertexAttribArray', 'glDisableVertexAttribArray',
  'glDetachShader', 'glDeleteShader', 'glDeleteProgram', 'glCreateShader',
  'glCreateProgram', 'glCompileShader', 'glAttachShader',
  'glStencilMaskSeparate', 'glStencilFuncSeparate', 'glStencilOpSeparate',
  'glBlendEquationSeparate', 'glTranslatef', 'glTranslated', 'glScalef',
  'glScaled', 'glRotatef', 'glRotated', 'glPushMatrix', 'glPopMatrix',
  'glOrtho', 'glMatrixMode', 'glLoadIdentity', 'glFrustum', 'glIsList',
  'glCopyPixels', 'glPixelTransferi', 'glPixelTransferf', 'glPixelZoom',
  'glAlphaFunc', 'glEvalPoint2', 'glEvalMesh2', 'glEvalPoint1',
  'glEvalMesh1', 'glEvalCoord2f', 'glEvalCoord2d', 'glEvalCoord1f',
  'glEvalCoord1d', 'glMapGrid2f', 'glMapGrid2d', 'glMapGrid1f',
  'glMapGrid1d', 'glPushAttrib', 'glPopAttrib', 'glAccum', 'glIndexMask',
  'glClearIndex', 'glClearAccum', 'glPushName', 'glPopName', 'glPassThrough',
  'glLoadName', 'glInitNames', 'glRenderMode', 'glTexGeni', 'glTexGenf',
  'glTexGend', 'glTexEnvi', 'glTexEnvf', 'glShadeModel', 'glMateriali',
  'glMaterialf', 'glLineStipple', 'glLightModeli', 'glLightModelf',
  'glLighti', 'glLightf', 'glFogi', 'glFogf', 'glColorMaterial',
  'glVertex4s', 'glVertex4i', 'glVertex4f', 'glVertex4d', 'glVertex3s',
  'glVertex3i', 'glVertex3f', 'glVertex3d', 'glVertex2s', 'glVertex2i',
  'glVertex2f', 'glVertex2d', 'glTexCoord4s', 'glTexCoord4i', 'glTexCoord4f',
  'glTexCoord4d', 'glTexCoord3s', 'glTexCoord3i', 'glTexCoord3f',
  'glTexCoord3d', 'glTexCoord2s', 'glTexCoord2i', 'glTexCoord2f',
  'glTexCoord2d', 'glTexCoord1s', 'glTexCoord1i', 'glTexCoord1f',
  'glTexCoord1d', 'glRects', 'glRecti', 'glRectf', 'glRectd',
  'glRasterPos4s', 'glRasterPos4i', 'glRasterPos4f', 'glRasterPos4d',
  'glRasterPos3s', 'glRasterPos3i', 'glRasterPos3f', 'glRasterPos3d',
  'glRasterPos2s', 'glRasterPos2i', 'glRasterPos2f', 'glRasterPos2d',
  'glNormal3s', 'glNormal3i', 'glNormal3f', 'glNormal3d', 'glNormal3b',
  'glIndexs', 'glIndexi', 'glIndexf', 'glIndexd', 'glEnd', 'glEdgeFlag',
  'glColor4us', 'glColor4ui', 'glColor4ub', 'glColor4s', 'glColor4i',
  'glColor4f', 'glColor4d', 'glColor4b', 'glColor3us', 'glColor3ui',
  'glColor3ub', 'glColor3s', 'glColor3i', 'glColor3f', 'glColor3d',
  'glColor3b', 'glBegin', 'glListBase', 'glGenLists', 'glDeleteLists',
  'glCallList', 'glEndList', 'glNewList', 'glPushClientAttrib',
  'glPopClientAttrib', 'glEnableClientState', 'glDisableClientState',
  'glArrayElement', 'glResetMinmax', 'glResetHistogram', 'glMinmax',
  'glHistogram', 'glCopyConvolutionFilter2D', 'glCopyConvolutionFilter1D',
  'glConvolutionParameteri', 'glConvolutionParameterf',
  'glCopyColorSubTable', 'glCopyColorTable', 'glMultiTexCoord4s',
  'glMultiTexCoord4i', 'glMultiTexCoord4f', 'glMultiTexCoord4d',
  'glMultiTexCoord3s', 'glMultiTexCoord3i', 'glMultiTexCoord3f',
  'glMultiTexCoord3d', 'glMultiTexCoord2s', 'glMultiTexCoord2i',
  'glMultiTexCoord2f', 'glMultiTexCoord2d', 'glMultiTexCoord1s',
  'glMultiTexCoord1i', 'glMultiTexCoord1f', 'glMultiTexCoord1d',
  'glClientActiveTexture', 'glWindowPos3s', 'glWindowPos3i', 'glWindowPos3f',
  'glWindowPos3d', 'glWindowPos2s', 'glWindowPos2i', 'glWindowPos2f',
  'glWindowPos2d', 'glSecondaryColor3us', 'glSecondaryColor3ui',
  'glSecondaryColor3ub', 'glSecondaryColor3s', 'glSecondaryColor3i',
  'glSecondaryColor3f', 'glSecondaryColor3d', 'glSecondaryColor3b',
  'glFogCoordd', 'glFogCoordf', 'glVertexAttrib4s', 'glVertexAttrib4f',
  'glVertexAttrib4d', 'glVertexAttrib4Nub', 'glVertexAttrib3s',
  'glVertexAttrib3f', 'glVertexAttrib3d', 'glVertexAttrib2s',
  'glVertexAttrib2f', 'glVertexAttrib2d', 'glVertexAttrib1s',
  'glVertexAttrib1f', 'glVertexAttrib1d', 'isContextCompatible',
  'versionProfile'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpenGLFunctions_2_0::~QOpenGLFunctions_2_0()': the destructor:
    Python never removes a C++ QOpenGLFunctions_2_0.
  - Qt's 'void QOpenGLFunctions_2_0::glGetTexLevelParameteriv(GLenum target,
    GLint level, GLenum pname, GLint *params)': takes a number to change
    where it is.
  - Qt's 'void QOpenGLFunctions_2_0::glGetTexLevelParameterfv(GLenum target,
    GLint level, GLenum pname, GLfloat *params)': takes a number to change
    where it is.
  - Qt's 'void QOpenGLFunctions_2_0::glGetTexParameteriv(GLenum target,
    GLenum pname, GLint *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_2_0::glGetTexParameterfv(GLenum target,
    GLenum pname, GLfloat *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_2_0::glGetTexImage(GLenum target, GLint
    level, GLenum format, GLenum type, GLvoid *pixels)': names 'GLvoid',
    which has no cute class yet.
  - Qt's 'const GLubyte *QOpenGLFunctions_2_0::glGetString(GLenum name)':
    gives 'unsigned char', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glGetIntegerv(GLenum pname, GLint
    *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_2_0::glGetFloatv(GLenum pname, GLfloat
    *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_2_0::glGetDoublev(GLenum pname, GLdouble
    *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_2_0::glGetBooleanv(GLenum pname, GLboolean
    *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_2_0::glReadPixels(GLint x, GLint y, GLsizei
    width, GLsizei height, GLenum format, GLenum type, GLvoid *pixels)':
    names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glTexImage2D(GLenum target, GLint level,
    GLint internalformat, GLsizei width, GLsizei height, GLint border, GLenum
    format, GLenum type, const GLvoid *pixels)': names 'GLvoid', which has no
    cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glTexImage1D(GLenum target, GLint level,
    GLint internalformat, GLsizei width, GLint border, GLenum format, GLenum
    type, const GLvoid *pixels)': names 'GLvoid', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_2_0::glTexParameteriv(GLenum target, GLenum
    pname, const GLint *params)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glTexParameterfv(GLenum target, GLenum
    pname, const GLfloat *params)': names 'GLfloat', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_2_0::glIndexubv(const GLubyte *c)': names
    'GLubyte', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glGenTextures(GLsizei n, GLuint
    *textures)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_2_0::glDeleteTextures(GLsizei n, const GLuint
    *textures)': names 'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glTexSubImage2D(GLenum target, GLint
    level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height,
    GLenum format, GLenum type, const GLvoid *pixels)': names 'GLvoid', which
    has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glTexSubImage1D(GLenum target, GLint
    level, GLint xoffset, GLsizei width, GLenum format, GLenum type, const
    GLvoid *pixels)': names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glGetPointerv(GLenum pname, GLvoid
    **params)': takes a type Python has no way to hand over yet.
  - Qt's 'void QOpenGLFunctions_2_0::glDrawElements(GLenum mode, GLsizei
    count, GLenum type, const GLvoid *indices)': names 'GLvoid', which has no
    cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glTexSubImage3D(GLenum target, GLint
    level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width,
    GLsizei height, GLsizei depth, GLenum format, GLenum type, const GLvoid
    *pixels)': names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glTexImage3D(GLenum target, GLint level,
    GLint internalformat, GLsizei width, GLsizei height, GLsizei depth, GLint
    border, GLenum format, GLenum type, const GLvoid *pixels)': names
    'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glDrawRangeElements(GLenum mode, GLuint
    start, GLuint end, GLsizei count, GLenum type, const GLvoid *indices)':
    names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glGetCompressedTexImage(GLenum target,
    GLint level, GLvoid *img)': names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glCompressedTexSubImage1D(GLenum target,
    GLint level, GLint xoffset, GLsizei width, GLenum format, GLsizei
    imageSize, const GLvoid *data)': names 'GLvoid', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_2_0::glCompressedTexSubImage2D(GLenum target,
    GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height,
    GLenum format, GLsizei imageSize, const GLvoid *data)': names 'GLvoid',
    which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glCompressedTexSubImage3D(GLenum target,
    GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width,
    GLsizei height, GLsizei depth, GLenum format, GLsizei imageSize, const
    GLvoid *data)': names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glCompressedTexImage1D(GLenum target,
    GLint level, GLenum internalformat, GLsizei width, GLint border, GLsizei
    imageSize, const GLvoid *data)': names 'GLvoid', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_2_0::glCompressedTexImage2D(GLenum target,
    GLint level, GLenum internalformat, GLsizei width, GLsizei height, GLint
    border, GLsizei imageSize, const GLvoid *data)': names 'GLvoid', which
    has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glCompressedTexImage3D(GLenum target,
    GLint level, GLenum internalformat, GLsizei width, GLsizei height,
    GLsizei depth, GLint border, GLsizei imageSize, const GLvoid *data)':
    names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glPointParameteriv(GLenum pname, const
    GLint *params)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glPointParameterfv(GLenum pname, const
    GLfloat *params)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glMultiDrawElements(GLenum mode, const
    GLsizei *count, GLenum type, const GLvoid *const *indices, GLsizei
    drawcount)': names 'GLsizei', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glMultiDrawArrays(GLenum mode, const
    GLint *first, const GLsizei *count, GLsizei drawcount)': names 'GLint',
    which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glGetBufferPointerv(GLenum target,
    GLenum pname, GLvoid **params)': takes a type Python has no way to hand
    over yet.
  - Qt's 'void QOpenGLFunctions_2_0::glGetBufferParameteriv(GLenum target,
    GLenum pname, GLint *params)': takes a number to change where it is.
  - Qt's 'GLvoid *QOpenGLFunctions_2_0::glMapBuffer(GLenum target, GLenum
    access)': gives 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glGetBufferSubData(GLenum target,
    GLintptr offset, GLsizeiptr size, GLvoid *data)': names 'GLvoid', which
    has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glBufferSubData(GLenum target, GLintptr
    offset, GLsizeiptr size, const GLvoid *data)': names 'GLvoid', which has
    no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glBufferData(GLenum target, GLsizeiptr
    size, const GLvoid *data, GLenum usage)': names 'GLvoid', which has no
    cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glGenBuffers(GLsizei n, GLuint
    *buffers)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_2_0::glDeleteBuffers(GLsizei n, const GLuint
    *buffers)': names 'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glGetQueryObjectuiv(GLuint id, GLenum
    pname, GLuint *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_2_0::glGetQueryObjectiv(GLuint id, GLenum
    pname, GLint *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_2_0::glGetQueryiv(GLenum target, GLenum
    pname, GLint *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_2_0::glDeleteQueries(GLsizei n, const GLuint
    *ids)': names 'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glGenQueries(GLsizei n, GLuint *ids)':
    takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_2_0::glVertexAttribPointer(GLuint index,
    GLint size, GLenum type, GLboolean normalized, GLsizei stride, const
    GLvoid *pointer)': names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glUniformMatrix4fv(GLint location,
    GLsizei count, GLboolean transpose, const GLfloat *value)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glUniformMatrix3fv(GLint location,
    GLsizei count, GLboolean transpose, const GLfloat *value)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glUniformMatrix2fv(GLint location,
    GLsizei count, GLboolean transpose, const GLfloat *value)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glUniform4iv(GLint location, GLsizei
    count, const GLint *value)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glUniform3iv(GLint location, GLsizei
    count, const GLint *value)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glUniform2iv(GLint location, GLsizei
    count, const GLint *value)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glUniform1iv(GLint location, GLsizei
    count, const GLint *value)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glUniform4fv(GLint location, GLsizei
    count, const GLfloat *value)': names 'GLfloat', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_2_0::glUniform3fv(GLint location, GLsizei
    count, const GLfloat *value)': names 'GLfloat', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_2_0::glUniform2fv(GLint location, GLsizei
    count, const GLfloat *value)': names 'GLfloat', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_2_0::glUniform1fv(GLint location, GLsizei
    count, const GLfloat *value)': names 'GLfloat', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_2_0::glShaderSource(GLuint shader, GLsizei
    count, const GLchar *const *string, const GLint *length)': names 'GLchar
    *const', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glGetVertexAttribPointerv(GLuint index,
    GLenum pname, GLvoid **pointer)': takes a type Python has no way to hand
    over yet.
  - Qt's 'void QOpenGLFunctions_2_0::glGetVertexAttribiv(GLuint index, GLenum
    pname, GLint *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_2_0::glGetVertexAttribfv(GLuint index, GLenum
    pname, GLfloat *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_2_0::glGetVertexAttribdv(GLuint index, GLenum
    pname, GLdouble *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_2_0::glGetUniformiv(GLuint program, GLint
    location, GLint *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_2_0::glGetUniformfv(GLuint program, GLint
    location, GLfloat *params)': takes a number to change where it is.
  - Qt's 'GLint QOpenGLFunctions_2_0::glGetUniformLocation(GLuint program,
    const GLchar *name)': names 'GLchar', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glGetShaderSource(GLuint shader, GLsizei
    bufSize, GLsizei *length, GLchar *source)': takes a number to change
    where it is.
  - Qt's 'void QOpenGLFunctions_2_0::glGetShaderInfoLog(GLuint shader,
    GLsizei bufSize, GLsizei *length, GLchar *infoLog)': takes a number to
    change where it is.
  - Qt's 'void QOpenGLFunctions_2_0::glGetShaderiv(GLuint shader, GLenum
    pname, GLint *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_2_0::glGetProgramInfoLog(GLuint program,
    GLsizei bufSize, GLsizei *length, GLchar *infoLog)': takes a number to
    change where it is.
  - Qt's 'void QOpenGLFunctions_2_0::glGetProgramiv(GLuint program, GLenum
    pname, GLint *params)': takes a number to change where it is.
  - Qt's 'GLint QOpenGLFunctions_2_0::glGetAttribLocation(GLuint program,
    const GLchar *name)': names 'GLchar', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glGetAttachedShaders(GLuint program,
    GLsizei maxCount, GLsizei *count, GLuint *obj)': takes a number to change
    where it is.
  - Qt's 'void QOpenGLFunctions_2_0::glGetActiveUniform(GLuint program,
    GLuint index, GLsizei bufSize, GLsizei *length, GLint *size, GLenum
    *type, GLchar *name)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_2_0::glGetActiveAttrib(GLuint program, GLuint
    index, GLsizei bufSize, GLsizei *length, GLint *size, GLenum *type,
    GLchar *name)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_2_0::glBindAttribLocation(GLuint program,
    GLuint index, const GLchar *name)': names 'GLchar', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glDrawBuffers(GLsizei n, const GLenum
    *bufs)': names 'GLenum', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glMultMatrixd(const GLdouble *m)': names
    'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glMultMatrixf(const GLfloat *m)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glLoadMatrixd(const GLdouble *m)': names
    'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glLoadMatrixf(const GLfloat *m)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glGetTexGeniv(GLenum coord, GLenum
    pname, GLint *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_2_0::glGetTexGenfv(GLenum coord, GLenum
    pname, GLfloat *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_2_0::glGetTexGendv(GLenum coord, GLenum
    pname, GLdouble *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_2_0::glGetTexEnviv(GLenum target, GLenum
    pname, GLint *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_2_0::glGetTexEnvfv(GLenum target, GLenum
    pname, GLfloat *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_2_0::glGetPolygonStipple(GLubyte *mask)':
    takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_2_0::glGetPixelMapusv(GLenum map, GLushort
    *values)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_2_0::glGetPixelMapuiv(GLenum map, GLuint
    *values)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_2_0::glGetPixelMapfv(GLenum map, GLfloat
    *values)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_2_0::glGetMaterialiv(GLenum face, GLenum
    pname, GLint *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_2_0::glGetMaterialfv(GLenum face, GLenum
    pname, GLfloat *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_2_0::glGetMapiv(GLenum target, GLenum query,
    GLint *v)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_2_0::glGetMapfv(GLenum target, GLenum query,
    GLfloat *v)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_2_0::glGetMapdv(GLenum target, GLenum query,
    GLdouble *v)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_2_0::glGetLightiv(GLenum light, GLenum pname,
    GLint *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_2_0::glGetLightfv(GLenum light, GLenum pname,
    GLfloat *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_2_0::glGetClipPlane(GLenum plane, GLdouble
    *equation)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_2_0::glDrawPixels(GLsizei width, GLsizei
    height, GLenum format, GLenum type, const GLvoid *pixels)': names
    'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glPixelMapusv(GLenum map, GLint mapsize,
    const GLushort *values)': names 'GLushort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glPixelMapuiv(GLenum map, GLint mapsize,
    const GLuint *values)': names 'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glPixelMapfv(GLenum map, GLint mapsize,
    const GLfloat *values)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glEvalCoord2fv(const GLfloat *u)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glEvalCoord2dv(const GLdouble *u)':
    names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glEvalCoord1fv(const GLfloat *u)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glEvalCoord1dv(const GLdouble *u)':
    names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glMap2f(GLenum target, GLfloat u1,
    GLfloat u2, GLint ustride, GLint uorder, GLfloat v1, GLfloat v2, GLint
    vstride, GLint vorder, const GLfloat *points)': names 'GLfloat', which
    has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glMap2d(GLenum target, GLdouble u1,
    GLdouble u2, GLint ustride, GLint uorder, GLdouble v1, GLdouble v2, GLint
    vstride, GLint vorder, const GLdouble *points)': names 'GLdouble', which
    has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glMap1f(GLenum target, GLfloat u1,
    GLfloat u2, GLint stride, GLint order, const GLfloat *points)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glMap1d(GLenum target, GLdouble u1,
    GLdouble u2, GLint stride, GLint order, const GLdouble *points)': names
    'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glSelectBuffer(GLsizei size, GLuint
    *buffer)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_2_0::glFeedbackBuffer(GLsizei size, GLenum
    type, GLfloat *buffer)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_2_0::glTexGeniv(GLenum coord, GLenum pname,
    const GLint *params)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glTexGenfv(GLenum coord, GLenum pname,
    const GLfloat *params)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glTexGendv(GLenum coord, GLenum pname,
    const GLdouble *params)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glTexEnviv(GLenum target, GLenum pname,
    const GLint *params)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glTexEnvfv(GLenum target, GLenum pname,
    const GLfloat *params)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glPolygonStipple(const GLubyte *mask)':
    names 'GLubyte', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glMaterialiv(GLenum face, GLenum pname,
    const GLint *params)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glMaterialfv(GLenum face, GLenum pname,
    const GLfloat *params)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glLightModeliv(GLenum pname, const GLint
    *params)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glLightModelfv(GLenum pname, const
    GLfloat *params)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glLightiv(GLenum light, GLenum pname,
    const GLint *params)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glLightfv(GLenum light, GLenum pname,
    const GLfloat *params)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glFogiv(GLenum pname, const GLint
    *params)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glFogfv(GLenum pname, const GLfloat
    *params)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glClipPlane(GLenum plane, const GLdouble
    *equation)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glVertex4sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glVertex4iv(const GLint *v)': names
    'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glVertex4fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glVertex4dv(const GLdouble *v)': names
    'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glVertex3sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glVertex3iv(const GLint *v)': names
    'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glVertex3fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glVertex3dv(const GLdouble *v)': names
    'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glVertex2sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glVertex2iv(const GLint *v)': names
    'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glVertex2fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glVertex2dv(const GLdouble *v)': names
    'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glTexCoord4sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glTexCoord4iv(const GLint *v)': names
    'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glTexCoord4fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glTexCoord4dv(const GLdouble *v)': names
    'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glTexCoord3sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glTexCoord3iv(const GLint *v)': names
    'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glTexCoord3fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glTexCoord3dv(const GLdouble *v)': names
    'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glTexCoord2sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glTexCoord2iv(const GLint *v)': names
    'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glTexCoord2fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glTexCoord2dv(const GLdouble *v)': names
    'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glTexCoord1sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glTexCoord1iv(const GLint *v)': names
    'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glTexCoord1fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glTexCoord1dv(const GLdouble *v)': names
    'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glRectsv(const GLshort *v1, const
    GLshort *v2)': names 'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glRectiv(const GLint *v1, const GLint
    *v2)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glRectfv(const GLfloat *v1, const
    GLfloat *v2)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glRectdv(const GLdouble *v1, const
    GLdouble *v2)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glRasterPos4sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glRasterPos4iv(const GLint *v)': names
    'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glRasterPos4fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glRasterPos4dv(const GLdouble *v)':
    names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glRasterPos3sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glRasterPos3iv(const GLint *v)': names
    'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glRasterPos3fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glRasterPos3dv(const GLdouble *v)':
    names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glRasterPos2sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glRasterPos2iv(const GLint *v)': names
    'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glRasterPos2fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glRasterPos2dv(const GLdouble *v)':
    names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glNormal3sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glNormal3iv(const GLint *v)': names
    'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glNormal3fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glNormal3dv(const GLdouble *v)': names
    'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glNormal3bv(const GLbyte *v)': names
    'GLbyte', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glIndexsv(const GLshort *c)': names
    'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glIndexiv(const GLint *c)': names
    'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glIndexfv(const GLfloat *c)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glIndexdv(const GLdouble *c)': names
    'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glEdgeFlagv(const GLboolean *flag)':
    names 'GLboolean', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glColor4usv(const GLushort *v)': names
    'GLushort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glColor4uiv(const GLuint *v)': names
    'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glColor4ubv(const GLubyte *v)': names
    'GLubyte', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glColor4sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glColor4iv(const GLint *v)': names
    'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glColor4fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glColor4dv(const GLdouble *v)': names
    'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glColor4bv(const GLbyte *v)': names
    'GLbyte', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glColor3usv(const GLushort *v)': names
    'GLushort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glColor3uiv(const GLuint *v)': names
    'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glColor3ubv(const GLubyte *v)': names
    'GLubyte', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glColor3sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glColor3iv(const GLint *v)': names
    'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glColor3fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glColor3dv(const GLdouble *v)': names
    'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glColor3bv(const GLbyte *v)': names
    'GLbyte', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glBitmap(GLsizei width, GLsizei height,
    GLfloat xorig, GLfloat yorig, GLfloat xmove, GLfloat ymove, const GLubyte
    *bitmap)': names 'GLubyte', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glCallLists(GLsizei n, GLenum type,
    const GLvoid *lists)': names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glPrioritizeTextures(GLsizei n, const
    GLuint *textures, const GLfloat *priorities)': names 'GLuint', which has
    no cute class yet.
  - Qt's 'GLboolean QOpenGLFunctions_2_0::glAreTexturesResident(GLsizei n,
    const GLuint *textures, GLboolean *residences)': names 'GLuint', which
    has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glVertexPointer(GLint size, GLenum type,
    GLsizei stride, const GLvoid *pointer)': names 'GLvoid', which has no
    cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glTexCoordPointer(GLint size, GLenum
    type, GLsizei stride, const GLvoid *pointer)': names 'GLvoid', which has
    no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glNormalPointer(GLenum type, GLsizei
    stride, const GLvoid *pointer)': names 'GLvoid', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_2_0::glInterleavedArrays(GLenum format,
    GLsizei stride, const GLvoid *pointer)': names 'GLvoid', which has no
    cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glIndexPointer(GLenum type, GLsizei
    stride, const GLvoid *pointer)': names 'GLvoid', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_2_0::glEdgeFlagPointer(GLsizei stride, const
    GLvoid *pointer)': names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glColorPointer(GLint size, GLenum type,
    GLsizei stride, const GLvoid *pointer)': names 'GLvoid', which has no
    cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glGetMinmaxParameteriv(GLenum target,
    GLenum pname, GLint *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_2_0::glGetMinmaxParameterfv(GLenum target,
    GLenum pname, GLfloat *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_2_0::glGetMinmax(GLenum target, GLboolean
    reset, GLenum format, GLenum type, GLvoid *values)': names 'GLvoid',
    which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glGetHistogramParameteriv(GLenum target,
    GLenum pname, GLint *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_2_0::glGetHistogramParameterfv(GLenum target,
    GLenum pname, GLfloat *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_2_0::glGetHistogram(GLenum target, GLboolean
    reset, GLenum format, GLenum type, GLvoid *values)': names 'GLvoid',
    which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glSeparableFilter2D(GLenum target,
    GLenum internalformat, GLsizei width, GLsizei height, GLenum format,
    GLenum type, const GLvoid *row, const GLvoid *column)': names 'GLvoid',
    which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glGetSeparableFilter(GLenum target,
    GLenum format, GLenum type, GLvoid *row, GLvoid *column, GLvoid *span)':
    names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glGetConvolutionParameteriv(GLenum
    target, GLenum pname, GLint *params)': takes a number to change where it
    is.
  - Qt's 'void QOpenGLFunctions_2_0::glGetConvolutionParameterfv(GLenum
    target, GLenum pname, GLfloat *params)': takes a number to change where
    it is.
  - Qt's 'void QOpenGLFunctions_2_0::glGetConvolutionFilter(GLenum target,
    GLenum format, GLenum type, GLvoid *image)': names 'GLvoid', which has no
    cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glConvolutionParameteriv(GLenum target,
    GLenum pname, const GLint *params)': names 'GLint', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glConvolutionParameterfv(GLenum target,
    GLenum pname, const GLfloat *params)': names 'GLfloat', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glConvolutionFilter2D(GLenum target,
    GLenum internalformat, GLsizei width, GLsizei height, GLenum format,
    GLenum type, const GLvoid *image)': names 'GLvoid', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glConvolutionFilter1D(GLenum target,
    GLenum internalformat, GLsizei width, GLenum format, GLenum type, const
    GLvoid *image)': names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glColorSubTable(GLenum target, GLsizei
    start, GLsizei count, GLenum format, GLenum type, const GLvoid *data)':
    names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glGetColorTableParameteriv(GLenum
    target, GLenum pname, GLint *params)': takes a number to change where it
    is.
  - Qt's 'void QOpenGLFunctions_2_0::glGetColorTableParameterfv(GLenum
    target, GLenum pname, GLfloat *params)': takes a number to change where
    it is.
  - Qt's 'void QOpenGLFunctions_2_0::glGetColorTable(GLenum target, GLenum
    format, GLenum type, GLvoid *table)': names 'GLvoid', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glColorTableParameteriv(GLenum target,
    GLenum pname, const GLint *params)': names 'GLint', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glColorTableParameterfv(GLenum target,
    GLenum pname, const GLfloat *params)': names 'GLfloat', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glColorTable(GLenum target, GLenum
    internalformat, GLsizei width, GLenum format, GLenum type, const GLvoid
    *table)': names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glMultTransposeMatrixd(const GLdouble
    *m)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glMultTransposeMatrixf(const GLfloat
    *m)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glLoadTransposeMatrixd(const GLdouble
    *m)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glLoadTransposeMatrixf(const GLfloat
    *m)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glMultiTexCoord4sv(GLenum target, const
    GLshort *v)': names 'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glMultiTexCoord4iv(GLenum target, const
    GLint *v)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glMultiTexCoord4fv(GLenum target, const
    GLfloat *v)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glMultiTexCoord4dv(GLenum target, const
    GLdouble *v)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glMultiTexCoord3sv(GLenum target, const
    GLshort *v)': names 'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glMultiTexCoord3iv(GLenum target, const
    GLint *v)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glMultiTexCoord3fv(GLenum target, const
    GLfloat *v)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glMultiTexCoord3dv(GLenum target, const
    GLdouble *v)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glMultiTexCoord2sv(GLenum target, const
    GLshort *v)': names 'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glMultiTexCoord2iv(GLenum target, const
    GLint *v)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glMultiTexCoord2fv(GLenum target, const
    GLfloat *v)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glMultiTexCoord2dv(GLenum target, const
    GLdouble *v)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glMultiTexCoord1sv(GLenum target, const
    GLshort *v)': names 'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glMultiTexCoord1iv(GLenum target, const
    GLint *v)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glMultiTexCoord1fv(GLenum target, const
    GLfloat *v)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glMultiTexCoord1dv(GLenum target, const
    GLdouble *v)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glWindowPos3sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glWindowPos3iv(const GLint *v)': names
    'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glWindowPos3fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glWindowPos3dv(const GLdouble *v)':
    names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glWindowPos2sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glWindowPos2iv(const GLint *v)': names
    'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glWindowPos2fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glWindowPos2dv(const GLdouble *v)':
    names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glSecondaryColorPointer(GLint size,
    GLenum type, GLsizei stride, const GLvoid *pointer)': names 'GLvoid',
    which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glSecondaryColor3usv(const GLushort
    *v)': names 'GLushort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glSecondaryColor3uiv(const GLuint *v)':
    names 'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glSecondaryColor3ubv(const GLubyte *v)':
    names 'GLubyte', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glSecondaryColor3sv(const GLshort *v)':
    names 'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glSecondaryColor3iv(const GLint *v)':
    names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glSecondaryColor3fv(const GLfloat *v)':
    names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glSecondaryColor3dv(const GLdouble *v)':
    names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glSecondaryColor3bv(const GLbyte *v)':
    names 'GLbyte', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glFogCoordPointer(GLenum type, GLsizei
    stride, const GLvoid *pointer)': names 'GLvoid', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_2_0::glFogCoorddv(const GLdouble *coord)':
    names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glFogCoordfv(const GLfloat *coord)':
    names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib4usv(GLuint index, const
    GLushort *v)': names 'GLushort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib4uiv(GLuint index, const
    GLuint *v)': names 'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib4ubv(GLuint index, const
    GLubyte *v)': names 'GLubyte', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib4sv(GLuint index, const
    GLshort *v)': names 'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib4iv(GLuint index, const
    GLint *v)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib4fv(GLuint index, const
    GLfloat *v)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib4dv(GLuint index, const
    GLdouble *v)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib4bv(GLuint index, const
    GLbyte *v)': names 'GLbyte', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib4Nusv(GLuint index, const
    GLushort *v)': names 'GLushort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib4Nuiv(GLuint index, const
    GLuint *v)': names 'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib4Nubv(GLuint index, const
    GLubyte *v)': names 'GLubyte', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib4Nsv(GLuint index, const
    GLshort *v)': names 'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib4Niv(GLuint index, const
    GLint *v)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib4Nbv(GLuint index, const
    GLbyte *v)': names 'GLbyte', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib3sv(GLuint index, const
    GLshort *v)': names 'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib3fv(GLuint index, const
    GLfloat *v)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib3dv(GLuint index, const
    GLdouble *v)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib2sv(GLuint index, const
    GLshort *v)': names 'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib2fv(GLuint index, const
    GLfloat *v)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib2dv(GLuint index, const
    GLdouble *v)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib1sv(GLuint index, const
    GLshort *v)': names 'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib1fv(GLuint index, const
    GLfloat *v)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib1dv(GLuint index, const
    GLdouble *v)': names 'GLdouble', which has no cute class yet.

  What to expect
  --------------

  - The C++ QOpenGLFunctions_2_0 is created at the first use, not by
    'QOpenGLFunctions_2_0(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QOpenGLFunctions_2_0.
  - Each name of Qt's QOpenGLFunctions_2_0 that has no cute function yet,
    'glAreTexturesResident', 'glBindAttribLocation', 'glBitmap',
    'glBufferData', 'glBufferSubData', 'glCallLists', 'glClipPlane',
    'glColor3bv', 'glColor3dv', 'glColor3fv', 'glColor3iv', 'glColor3sv',
    'glColor3ubv', 'glColor3uiv', 'glColor3usv', 'glColor4bv', 'glColor4dv',
    'glColor4fv', 'glColor4iv', 'glColor4sv', 'glColor4ubv', 'glColor4uiv',
    'glColor4usv', 'glColorPointer', 'glColorSubTable', 'glColorTable',
    'glColorTableParameterfv', 'glColorTableParameteriv',
    'glCompressedTexImage1D', 'glCompressedTexImage2D',
    'glCompressedTexImage3D', 'glCompressedTexSubImage1D',
    'glCompressedTexSubImage2D', 'glCompressedTexSubImage3D',
    'glConvolutionFilter1D', 'glConvolutionFilter2D',
    'glConvolutionParameterfv', 'glConvolutionParameteriv',
    'glDeleteBuffers', 'glDeleteQueries', 'glDeleteTextures',
    'glDrawBuffers', 'glDrawElements', 'glDrawPixels', 'glDrawRangeElements',
    'glEdgeFlagPointer', 'glEdgeFlagv', 'glEvalCoord1dv', 'glEvalCoord1fv',
    'glEvalCoord2dv', 'glEvalCoord2fv', 'glFeedbackBuffer',
    'glFogCoordPointer', 'glFogCoorddv', 'glFogCoordfv', 'glFogfv',
    'glFogiv', 'glGenBuffers', 'glGenQueries', 'glGenTextures',
    'glGetActiveAttrib', 'glGetActiveUniform', 'glGetAttachedShaders',
    'glGetAttribLocation', 'glGetBooleanv', 'glGetBufferParameteriv',
    'glGetBufferPointerv', 'glGetBufferSubData', 'glGetClipPlane',
    'glGetColorTable', 'glGetColorTableParameterfv',
    'glGetColorTableParameteriv', 'glGetCompressedTexImage',
    'glGetConvolutionFilter', 'glGetConvolutionParameterfv',
    'glGetConvolutionParameteriv', 'glGetDoublev', 'glGetFloatv',
    'glGetHistogram', 'glGetHistogramParameterfv',
    'glGetHistogramParameteriv', 'glGetIntegerv', 'glGetLightfv',
    'glGetLightiv', 'glGetMapdv', 'glGetMapfv', 'glGetMapiv',
    'glGetMaterialfv', 'glGetMaterialiv', 'glGetMinmax',
    'glGetMinmaxParameterfv', 'glGetMinmaxParameteriv', 'glGetPixelMapfv',
    'glGetPixelMapuiv', 'glGetPixelMapusv', 'glGetPointerv',
    'glGetPolygonStipple', 'glGetProgramInfoLog', 'glGetProgramiv',
    'glGetQueryObjectiv', 'glGetQueryObjectuiv', 'glGetQueryiv',
    'glGetSeparableFilter', 'glGetShaderInfoLog', 'glGetShaderSource',
    'glGetShaderiv', 'glGetString', 'glGetTexEnvfv', 'glGetTexEnviv',
    'glGetTexGendv', 'glGetTexGenfv', 'glGetTexGeniv', 'glGetTexImage',
    'glGetTexLevelParameterfv', 'glGetTexLevelParameteriv',
    'glGetTexParameterfv', 'glGetTexParameteriv', 'glGetUniformLocation',
    'glGetUniformfv', 'glGetUniformiv', 'glGetVertexAttribPointerv',
    'glGetVertexAttribdv', 'glGetVertexAttribfv', 'glGetVertexAttribiv',
    'glIndexPointer', 'glIndexdv', 'glIndexfv', 'glIndexiv', 'glIndexsv',
    'glIndexubv', 'glInterleavedArrays', 'glLightModelfv', 'glLightModeliv',
    'glLightfv', 'glLightiv', 'glLoadMatrixd', 'glLoadMatrixf',
    'glLoadTransposeMatrixd', 'glLoadTransposeMatrixf', 'glMap1d', 'glMap1f',
    'glMap2d', 'glMap2f', 'glMapBuffer', 'glMaterialfv', 'glMaterialiv',
    'glMultMatrixd', 'glMultMatrixf', 'glMultTransposeMatrixd',
    'glMultTransposeMatrixf', 'glMultiDrawArrays', 'glMultiDrawElements',
    'glMultiTexCoord1dv', 'glMultiTexCoord1fv', 'glMultiTexCoord1iv',
    'glMultiTexCoord1sv', 'glMultiTexCoord2dv', 'glMultiTexCoord2fv',
    'glMultiTexCoord2iv', 'glMultiTexCoord2sv', 'glMultiTexCoord3dv',
    'glMultiTexCoord3fv', 'glMultiTexCoord3iv', 'glMultiTexCoord3sv',
    'glMultiTexCoord4dv', 'glMultiTexCoord4fv', 'glMultiTexCoord4iv',
    'glMultiTexCoord4sv', 'glNormal3bv', 'glNormal3dv', 'glNormal3fv',
    'glNormal3iv', 'glNormal3sv', 'glNormalPointer', 'glPixelMapfv',
    'glPixelMapuiv', 'glPixelMapusv', 'glPointParameterfv',
    'glPointParameteriv', 'glPolygonStipple', 'glPrioritizeTextures',
    'glRasterPos2dv', 'glRasterPos2fv', 'glRasterPos2iv', 'glRasterPos2sv',
    'glRasterPos3dv', 'glRasterPos3fv', 'glRasterPos3iv', 'glRasterPos3sv',
    'glRasterPos4dv', 'glRasterPos4fv', 'glRasterPos4iv', 'glRasterPos4sv',
    'glReadPixels', 'glRectdv', 'glRectfv', 'glRectiv', 'glRectsv',
    'glSecondaryColor3bv', 'glSecondaryColor3dv', 'glSecondaryColor3fv',
    'glSecondaryColor3iv', 'glSecondaryColor3sv', 'glSecondaryColor3ubv',
    'glSecondaryColor3uiv', 'glSecondaryColor3usv',
    'glSecondaryColorPointer', 'glSelectBuffer', 'glSeparableFilter2D',
    'glShaderSource', 'glTexCoord1dv', 'glTexCoord1fv', 'glTexCoord1iv',
    'glTexCoord1sv', 'glTexCoord2dv', 'glTexCoord2fv', 'glTexCoord2iv',
    'glTexCoord2sv', 'glTexCoord3dv', 'glTexCoord3fv', 'glTexCoord3iv',
    'glTexCoord3sv', 'glTexCoord4dv', 'glTexCoord4fv', 'glTexCoord4iv',
    'glTexCoord4sv', 'glTexCoordPointer', 'glTexEnvfv', 'glTexEnviv',
    'glTexGendv', 'glTexGenfv', 'glTexGeniv', 'glTexImage1D', 'glTexImage2D',
    'glTexImage3D', 'glTexParameterfv', 'glTexParameteriv',
    'glTexSubImage1D', 'glTexSubImage2D', 'glTexSubImage3D', 'glUniform1fv',
    'glUniform1iv', 'glUniform2fv', 'glUniform2iv', 'glUniform3fv',
    'glUniform3iv', 'glUniform4fv', 'glUniform4iv', 'glUniformMatrix2fv',
    'glUniformMatrix3fv', 'glUniformMatrix4fv', 'glVertex2dv', 'glVertex2fv',
    'glVertex2iv', 'glVertex2sv', 'glVertex3dv', 'glVertex3fv',
    'glVertex3iv', 'glVertex3sv', 'glVertex4dv', 'glVertex4fv',
    'glVertex4iv', 'glVertex4sv', 'glVertexAttrib1dv', 'glVertexAttrib1fv',
    'glVertexAttrib1sv', 'glVertexAttrib2dv', 'glVertexAttrib2fv',
    'glVertexAttrib2sv', 'glVertexAttrib3dv', 'glVertexAttrib3fv',
    'glVertexAttrib3sv', 'glVertexAttrib4Nbv', 'glVertexAttrib4Niv',
    'glVertexAttrib4Nsv', 'glVertexAttrib4Nubv', 'glVertexAttrib4Nuiv',
    'glVertexAttrib4Nusv', 'glVertexAttrib4bv', 'glVertexAttrib4dv',
    'glVertexAttrib4fv', 'glVertexAttrib4iv', 'glVertexAttrib4sv',
    'glVertexAttrib4ubv', 'glVertexAttrib4uiv', 'glVertexAttrib4usv',
    'glVertexAttribPointer', 'glVertexPointer', 'glWindowPos2dv',
    'glWindowPos2fv', 'glWindowPos2iv', 'glWindowPos2sv', 'glWindowPos3dv',
    'glWindowPos3fv', 'glWindowPos3iv', 'glWindowPos3sv', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QOpenGLContext)
  @overload(NoneType)
  def isContextCompatible(context: Optional[QOpenGLContext]) -> bool:
    """
    Calls Qt's 'bool QOpenGLFunctions_2_0::isContextCompatible(QOpenGLContext
    *context)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#isContextCompatible

    Parameters
    ----------

    context : Optional[QOpenGLContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QOpenGLFunctions_2_0::isContextCompatible(QOpenGLContext
    #      *context)
    return Rituals.call(
        'ritual_ZN20QOpenGLFunctions_2_019isContextCompatibleEP14QOpenGLCon'
        'text',
        CuteMixin._addressOf(context),
    )

  @staticmethod
  def versionProfile() -> QOpenGLVersionProfile:
    """
    Calls Qt's 'QOpenGLVersionProfile
    QOpenGLFunctions_2_0::versionProfile()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#versionProfile

    Returns
    -------

    QOpenGLVersionProfile
      A new cute QOpenGLVersionProfile around the copy Qt gave back. Python
      owns it.
    """
    #  QOpenGLVersionProfile QOpenGLFunctions_2_0::versionProfile()
    address = Rituals.call(
        'ritual_ZN20QOpenGLFunctions_2_014versionProfileEv',
    )
    from . import QOpenGLVersionProfile
    return QOpenGLVersionProfile._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpenGLFunctions_2_0'

  #  A C++ QOpenGLFunctions_2_0 Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QOpenGLFunctions_2_0'

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
    'QOpenGLFunctions_2_0::QOpenGLFunctions_2_0()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#QOpenGLFunctions_2_0
    """
    #  QOpenGLFunctions_2_0::QOpenGLFunctions_2_0()
    self._noteCreation(QOpenGLFunctions_2_0, lambda: Rituals.call(
        'ritual_ZN20QOpenGLFunctions_2_0C1Ev',
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
    Calls Qt's 'bool QOpenGLFunctions_2_0::initializeOpenGLFunctions()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html
    """
    #  bool QOpenGLFunctions_2_0::initializeOpenGLFunctions()
    ritual = 'ritual_ZN20QOpenGLFunctions_2_025initializeOpenGLFunctionsEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QOpenGLFunctions_2_025initializeOpenGLFunctionsEv')
    return self.uglySide.call(ritual)

  @overload(int, int, int, int)
  def glViewport(self, x: int, y: int, width: int, height: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glViewport(GLint x, GLint y,
    GLsizei width, GLsizei height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glViewport

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
    #  void QOpenGLFunctions_2_0::glViewport(GLint x, GLint y, GLsizei width,
    #      GLsizei height)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_010glViewportEiiii',
        x, y, width, height,
    )

  @overload(float, float)
  def glDepthRange(self, nearVal: float, farVal: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glDepthRange(GLdouble nearVal,
    GLdouble farVal)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glDepthRange

    Parameters
    ----------

    nearVal : float
      Passed on as it is.

    farVal : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glDepthRange(GLdouble nearVal, GLdouble
    #      farVal)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_012glDepthRangeEdd', nearVal, farVal,
    )

  @overload(int)
  def glIsEnabled(self, cap: int) -> int:
    """
    Calls Qt's 'GLboolean QOpenGLFunctions_2_0::glIsEnabled(GLenum cap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glIsEnabled

    Parameters
    ----------

    cap : int
      Passed on as it is.
    """
    #  GLboolean QOpenGLFunctions_2_0::glIsEnabled(GLenum cap)
    return self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_011glIsEnabledEj', cap,
    )

  def glGetError(self) -> int:
    """
    Calls Qt's 'GLenum QOpenGLFunctions_2_0::glGetError()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glGetError
    """
    #  GLenum QOpenGLFunctions_2_0::glGetError()
    return self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_010glGetErrorEv',
    )

  @overload(int)
  def glReadBuffer(self, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glReadBuffer(GLenum mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glReadBuffer

    Parameters
    ----------

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glReadBuffer(GLenum mode)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_012glReadBufferEj', mode,
    )

  @overload(int, int)
  def glPixelStorei(self, pname: int, param: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glPixelStorei(GLenum pname, GLint
    param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glPixelStorei

    Parameters
    ----------

    pname : int
      Passed on as it is.

    param : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glPixelStorei(GLenum pname, GLint param)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_013glPixelStoreiEji', pname, param,
    )

  @overload(int, float)
  def glPixelStoref(self, pname: int, param: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glPixelStoref(GLenum pname,
    GLfloat param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glPixelStoref

    Parameters
    ----------

    pname : int
      Passed on as it is.

    param : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glPixelStoref(GLenum pname, GLfloat param)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_013glPixelStorefEjf', pname, param,
    )

  @overload(int)
  def glDepthFunc(self, func: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glDepthFunc(GLenum func)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glDepthFunc

    Parameters
    ----------

    func : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glDepthFunc(GLenum func)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_011glDepthFuncEj', func,
    )

  @overload(int, int, int)
  def glStencilOp(self, fail: int, zfail: int, zpass: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glStencilOp(GLenum fail, GLenum
    zfail, GLenum zpass)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glStencilOp

    Parameters
    ----------

    fail : int
      Passed on as it is.

    zfail : int
      Passed on as it is.

    zpass : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glStencilOp(GLenum fail, GLenum zfail,
    #      GLenum zpass)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_011glStencilOpEjjj',
        fail, zfail, zpass,
    )

  @overload(int, int, int)
  def glStencilFunc(self, func: int, ref: int, mask: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glStencilFunc(GLenum func, GLint
    ref, GLuint mask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glStencilFunc

    Parameters
    ----------

    func : int
      Passed on as it is.

    ref : int
      Passed on as it is.

    mask : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glStencilFunc(GLenum func, GLint ref,
    #      GLuint mask)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_013glStencilFuncEjij',
        func, ref, mask,
    )

  @overload(int)
  def glLogicOp(self, opcode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glLogicOp(GLenum opcode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glLogicOp

    Parameters
    ----------

    opcode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glLogicOp(GLenum opcode)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_2_09glLogicOpEj', opcode)

  @overload(int, int)
  def glBlendFunc(self, sfactor: int, dfactor: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glBlendFunc(GLenum sfactor, GLenum
    dfactor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glBlendFunc

    Parameters
    ----------

    sfactor : int
      Passed on as it is.

    dfactor : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glBlendFunc(GLenum sfactor, GLenum dfactor)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_011glBlendFuncEjj', sfactor, dfactor,
    )

  def glFlush(self) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glFlush()'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glFlush
    """
    #  void QOpenGLFunctions_2_0::glFlush()
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_2_07glFlushEv')

  def glFinish(self) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glFinish()'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glFinish
    """
    #  void QOpenGLFunctions_2_0::glFinish()
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_2_08glFinishEv')

  @overload(int)
  def glEnable(self, cap: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glEnable(GLenum cap)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glEnable

    Parameters
    ----------

    cap : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glEnable(GLenum cap)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_2_08glEnableEj', cap)

  @overload(int)
  def glDisable(self, cap: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glDisable(GLenum cap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glDisable

    Parameters
    ----------

    cap : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glDisable(GLenum cap)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_2_09glDisableEj', cap)

  @overload(int)
  def glDepthMask(self, flag: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glDepthMask(GLboolean flag)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glDepthMask

    Parameters
    ----------

    flag : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glDepthMask(GLboolean flag)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_011glDepthMaskEh', flag,
    )

  @overload(int, int, int, int)
  def glColorMask(self, red: int, green: int, blue: int, alpha: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glColorMask(GLboolean red,
    GLboolean green, GLboolean blue, GLboolean alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glColorMask

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
    #  void QOpenGLFunctions_2_0::glColorMask(GLboolean red, GLboolean green,
    #      GLboolean blue, GLboolean alpha)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_011glColorMaskEhhhh',
        red, green, blue, alpha,
    )

  @overload(int)
  def glStencilMask(self, mask: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glStencilMask(GLuint mask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glStencilMask

    Parameters
    ----------

    mask : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glStencilMask(GLuint mask)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_013glStencilMaskEj', mask,
    )

  @overload(float)
  def glClearDepth(self, depth: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glClearDepth(GLdouble depth)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glClearDepth

    Parameters
    ----------

    depth : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glClearDepth(GLdouble depth)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_012glClearDepthEd', depth,
    )

  @overload(int)
  def glClearStencil(self, s: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glClearStencil(GLint s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glClearStencil

    Parameters
    ----------

    s : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glClearStencil(GLint s)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_014glClearStencilEi', s,
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
    Calls Qt's 'void QOpenGLFunctions_2_0::glClearColor(GLfloat red, GLfloat
    green, GLfloat blue, GLfloat alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glClearColor

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
    #  void QOpenGLFunctions_2_0::glClearColor(GLfloat red, GLfloat green,
    #      GLfloat blue, GLfloat alpha)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_012glClearColorEffff',
        red, green, blue, alpha,
    )

  @overload(int)
  def glClear(self, mask: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glClear(GLbitfield mask)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glClear

    Parameters
    ----------

    mask : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glClear(GLbitfield mask)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_2_07glClearEj', mask)

  @overload(int)
  def glDrawBuffer(self, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glDrawBuffer(GLenum mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glDrawBuffer

    Parameters
    ----------

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glDrawBuffer(GLenum mode)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_012glDrawBufferEj', mode,
    )

  @overload(int, int, int)
  def glTexParameteri(self, target: int, pname: int, param: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glTexParameteri(GLenum target,
    GLenum pname, GLint param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glTexParameteri

    Parameters
    ----------

    target : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    param : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glTexParameteri(GLenum target, GLenum
    #      pname, GLint param)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_015glTexParameteriEjji',
        target, pname, param,
    )

  @overload(int, int, float)
  def glTexParameterf(self, target: int, pname: int, param: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glTexParameterf(GLenum target,
    GLenum pname, GLfloat param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glTexParameterf

    Parameters
    ----------

    target : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    param : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glTexParameterf(GLenum target, GLenum
    #      pname, GLfloat param)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_015glTexParameterfEjjf',
        target, pname, param,
    )

  @overload(int, int, int, int)
  def glScissor(self, x: int, y: int, width: int, height: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glScissor(GLint x, GLint y,
    GLsizei width, GLsizei height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glScissor

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
    #  void QOpenGLFunctions_2_0::glScissor(GLint x, GLint y, GLsizei width,
    #      GLsizei height)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_09glScissorEiiii',
        x, y, width, height,
    )

  @overload(int, int)
  def glPolygonMode(self, face: int, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glPolygonMode(GLenum face, GLenum
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glPolygonMode

    Parameters
    ----------

    face : int
      Passed on as it is.

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glPolygonMode(GLenum face, GLenum mode)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_013glPolygonModeEjj', face, mode,
    )

  @overload(float)
  def glPointSize(self, size: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glPointSize(GLfloat size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glPointSize

    Parameters
    ----------

    size : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glPointSize(GLfloat size)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_011glPointSizeEf', size,
    )

  @overload(float)
  def glLineWidth(self, width: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glLineWidth(GLfloat width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glLineWidth

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glLineWidth(GLfloat width)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_011glLineWidthEf', width,
    )

  @overload(int, int)
  def glHint(self, target: int, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glHint(GLenum target, GLenum
    mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glHint

    Parameters
    ----------

    target : int
      Passed on as it is.

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glHint(GLenum target, GLenum mode)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_06glHintEjj', target, mode,
    )

  @overload(int)
  def glFrontFace(self, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glFrontFace(GLenum mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glFrontFace

    Parameters
    ----------

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glFrontFace(GLenum mode)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_011glFrontFaceEj', mode,
    )

  @overload(int)
  def glCullFace(self, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glCullFace(GLenum mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glCullFace

    Parameters
    ----------

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glCullFace(GLenum mode)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_2_010glCullFaceEj', mode)

  @overload(int)
  def glIndexub(self, c: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glIndexub(GLubyte c)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glIndexub

    Parameters
    ----------

    c : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glIndexub(GLubyte c)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_2_09glIndexubEh', c)

  @overload(int)
  def glIsTexture(self, texture: int) -> int:
    """
    Calls Qt's 'GLboolean QOpenGLFunctions_2_0::glIsTexture(GLuint texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glIsTexture

    Parameters
    ----------

    texture : int
      Passed on as it is.
    """
    #  GLboolean QOpenGLFunctions_2_0::glIsTexture(GLuint texture)
    return self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_011glIsTextureEj', texture,
    )

  @overload(int, int)
  def glBindTexture(self, target: int, texture: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glBindTexture(GLenum target,
    GLuint texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glBindTexture

    Parameters
    ----------

    target : int
      Passed on as it is.

    texture : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glBindTexture(GLenum target, GLuint
    #      texture)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_013glBindTextureEjj', target, texture,
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
    Calls Qt's 'void QOpenGLFunctions_2_0::glCopyTexSubImage2D(GLenum target,
    GLint level, GLint xoffset, GLint yoffset, GLint x, GLint y, GLsizei
    width, GLsizei height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glCopyTexSubImage2D

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
    #  void QOpenGLFunctions_2_0::glCopyTexSubImage2D(GLenum target, GLint
    #      level, GLint xoffset, GLint yoffset, GLint x, GLint y, GLsizei
    #      width, GLsizei height)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_019glCopyTexSubImage2DEjiiiiiii',
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
    Calls Qt's 'void QOpenGLFunctions_2_0::glCopyTexSubImage1D(GLenum target,
    GLint level, GLint xoffset, GLint x, GLint y, GLsizei width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glCopyTexSubImage1D

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
    #  void QOpenGLFunctions_2_0::glCopyTexSubImage1D(GLenum target, GLint
    #      level, GLint xoffset, GLint x, GLint y, GLsizei width)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_019glCopyTexSubImage1DEjiiiii',
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
    Calls Qt's 'void QOpenGLFunctions_2_0::glCopyTexImage2D(GLenum target,
    GLint level, GLenum internalformat, GLint x, GLint y, GLsizei width,
    GLsizei height, GLint border)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glCopyTexImage2D

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
    #  void QOpenGLFunctions_2_0::glCopyTexImage2D(GLenum target, GLint
    #      level, GLenum internalformat, GLint x, GLint y, GLsizei width,
    #      GLsizei height, GLint border)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_016glCopyTexImage2DEjijiiiii',
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
    Calls Qt's 'void QOpenGLFunctions_2_0::glCopyTexImage1D(GLenum target,
    GLint level, GLenum internalformat, GLint x, GLint y, GLsizei width,
    GLint border)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glCopyTexImage1D

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
    #  void QOpenGLFunctions_2_0::glCopyTexImage1D(GLenum target, GLint
    #      level, GLenum internalformat, GLint x, GLint y, GLsizei width,
    #      GLint border)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_016glCopyTexImage1DEjijiiii',
        target, level, internalformat, x, y, width, border,
    )

  @overload(float, float)
  def glPolygonOffset(self, factor: float, units: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glPolygonOffset(GLfloat factor,
    GLfloat units)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glPolygonOffset

    Parameters
    ----------

    factor : float
      Passed on as it is.

    units : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glPolygonOffset(GLfloat factor, GLfloat
    #      units)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_015glPolygonOffsetEff', factor, units,
    )

  @overload(int, int, int)
  def glDrawArrays(self, mode: int, first: int, count: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glDrawArrays(GLenum mode, GLint
    first, GLsizei count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glDrawArrays

    Parameters
    ----------

    mode : int
      Passed on as it is.

    first : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glDrawArrays(GLenum mode, GLint first,
    #      GLsizei count)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_012glDrawArraysEjii',
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
    Calls Qt's 'void QOpenGLFunctions_2_0::glCopyTexSubImage3D(GLenum target,
    GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLint x, GLint
    y, GLsizei width, GLsizei height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glCopyTexSubImage3D

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
    #  void QOpenGLFunctions_2_0::glCopyTexSubImage3D(GLenum target, GLint
    #      level, GLint xoffset, GLint yoffset, GLint zoffset, GLint x, GLint
    #      y, GLsizei width, GLsizei height)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_019glCopyTexSubImage3DEjiiiiiiii',
        target, level, xoffset, yoffset, zoffset, x, y, width, height,
    )

  @overload(int)
  def glBlendEquation(self, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glBlendEquation(GLenum mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glBlendEquation

    Parameters
    ----------

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glBlendEquation(GLenum mode)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_015glBlendEquationEj', mode,
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
    Calls Qt's 'void QOpenGLFunctions_2_0::glBlendColor(GLfloat red, GLfloat
    green, GLfloat blue, GLfloat alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glBlendColor

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
    #  void QOpenGLFunctions_2_0::glBlendColor(GLfloat red, GLfloat green,
    #      GLfloat blue, GLfloat alpha)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_012glBlendColorEffff',
        red, green, blue, alpha,
    )

  @overload(float, int)
  def glSampleCoverage(self, value: float, invert: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glSampleCoverage(GLfloat value,
    GLboolean invert)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glSampleCoverage

    Parameters
    ----------

    value : float
      Passed on as it is.

    invert : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glSampleCoverage(GLfloat value, GLboolean
    #      invert)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_016glSampleCoverageEfh',
        value, invert,
    )

  @overload(int)
  def glActiveTexture(self, texture: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glActiveTexture(GLenum texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glActiveTexture

    Parameters
    ----------

    texture : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glActiveTexture(GLenum texture)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_015glActiveTextureEj', texture,
    )

  @overload(int, int)
  def glPointParameteri(self, pname: int, param: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glPointParameteri(GLenum pname,
    GLint param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glPointParameteri

    Parameters
    ----------

    pname : int
      Passed on as it is.

    param : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glPointParameteri(GLenum pname, GLint
    #      param)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_017glPointParameteriEji',
        pname, param,
    )

  @overload(int, float)
  def glPointParameterf(self, pname: int, param: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glPointParameterf(GLenum pname,
    GLfloat param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glPointParameterf

    Parameters
    ----------

    pname : int
      Passed on as it is.

    param : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glPointParameterf(GLenum pname, GLfloat
    #      param)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_017glPointParameterfEjf',
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
    Calls Qt's 'void QOpenGLFunctions_2_0::glBlendFuncSeparate(GLenum
    sfactorRGB, GLenum dfactorRGB, GLenum sfactorAlpha, GLenum
    dfactorAlpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glBlendFuncSeparate

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
    #  void QOpenGLFunctions_2_0::glBlendFuncSeparate(GLenum sfactorRGB,
    #      GLenum dfactorRGB, GLenum sfactorAlpha, GLenum dfactorAlpha)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_019glBlendFuncSeparateEjjjj',
        sfactorRGB, dfactorRGB, sfactorAlpha, dfactorAlpha,
    )

  @overload(int)
  def glUnmapBuffer(self, target: int) -> int:
    """
    Calls Qt's 'GLboolean QOpenGLFunctions_2_0::glUnmapBuffer(GLenum
    target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glUnmapBuffer

    Parameters
    ----------

    target : int
      Passed on as it is.
    """
    #  GLboolean QOpenGLFunctions_2_0::glUnmapBuffer(GLenum target)
    return self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_013glUnmapBufferEj', target,
    )

  @overload(int)
  def glIsBuffer(self, buffer: int) -> int:
    """
    Calls Qt's 'GLboolean QOpenGLFunctions_2_0::glIsBuffer(GLuint buffer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glIsBuffer

    Parameters
    ----------

    buffer : int
      Passed on as it is.
    """
    #  GLboolean QOpenGLFunctions_2_0::glIsBuffer(GLuint buffer)
    return self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_010glIsBufferEj', buffer,
    )

  @overload(int, int)
  def glBindBuffer(self, target: int, buffer: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glBindBuffer(GLenum target, GLuint
    buffer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glBindBuffer

    Parameters
    ----------

    target : int
      Passed on as it is.

    buffer : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glBindBuffer(GLenum target, GLuint buffer)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_012glBindBufferEjj', target, buffer,
    )

  @overload(int)
  def glEndQuery(self, target: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glEndQuery(GLenum target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glEndQuery

    Parameters
    ----------

    target : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glEndQuery(GLenum target)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_010glEndQueryEj', target,
    )

  @overload(int, int)
  def glBeginQuery(self, target: int, id: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glBeginQuery(GLenum target, GLuint
    id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glBeginQuery

    Parameters
    ----------

    target : int
      Passed on as it is.

    id : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glBeginQuery(GLenum target, GLuint id)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_012glBeginQueryEjj', target, id,
    )

  @overload(int)
  def glIsQuery(self, id: int) -> int:
    """
    Calls Qt's 'GLboolean QOpenGLFunctions_2_0::glIsQuery(GLuint id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glIsQuery

    Parameters
    ----------

    id : int
      Passed on as it is.
    """
    #  GLboolean QOpenGLFunctions_2_0::glIsQuery(GLuint id)
    return self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_09glIsQueryEj', id,
    )

  @overload(int)
  def glValidateProgram(self, program: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glValidateProgram(GLuint
    program)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glValidateProgram

    Parameters
    ----------

    program : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glValidateProgram(GLuint program)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_017glValidateProgramEj', program,
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
    Calls Qt's 'void QOpenGLFunctions_2_0::glUniform4i(GLint location, GLint
    v0, GLint v1, GLint v2, GLint v3)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glUniform4i

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
    #  void QOpenGLFunctions_2_0::glUniform4i(GLint location, GLint v0, GLint
    #      v1, GLint v2, GLint v3)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_011glUniform4iEiiiii',
        location, v0, v1, v2, v3,
    )

  @overload(int, int, int, int)
  def glUniform3i(self, location: int, v0: int, v1: int, v2: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glUniform3i(GLint location, GLint
    v0, GLint v1, GLint v2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glUniform3i

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
    #  void QOpenGLFunctions_2_0::glUniform3i(GLint location, GLint v0, GLint
    #      v1, GLint v2)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_011glUniform3iEiiii',
        location, v0, v1, v2,
    )

  @overload(int, int, int)
  def glUniform2i(self, location: int, v0: int, v1: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glUniform2i(GLint location, GLint
    v0, GLint v1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glUniform2i

    Parameters
    ----------

    location : int
      Passed on as it is.

    v0 : int
      Passed on as it is.

    v1 : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glUniform2i(GLint location, GLint v0, GLint
    #      v1)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_011glUniform2iEiii', location, v0, v1,
    )

  @overload(int, int)
  def glUniform1i(self, location: int, v0: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glUniform1i(GLint location, GLint
    v0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glUniform1i

    Parameters
    ----------

    location : int
      Passed on as it is.

    v0 : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glUniform1i(GLint location, GLint v0)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_011glUniform1iEii', location, v0,
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
    Calls Qt's 'void QOpenGLFunctions_2_0::glUniform4f(GLint location,
    GLfloat v0, GLfloat v1, GLfloat v2, GLfloat v3)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glUniform4f

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
    #  void QOpenGLFunctions_2_0::glUniform4f(GLint location, GLfloat v0,
    #      GLfloat v1, GLfloat v2, GLfloat v3)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_011glUniform4fEiffff',
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
    Calls Qt's 'void QOpenGLFunctions_2_0::glUniform3f(GLint location,
    GLfloat v0, GLfloat v1, GLfloat v2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glUniform3f

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
    #  void QOpenGLFunctions_2_0::glUniform3f(GLint location, GLfloat v0,
    #      GLfloat v1, GLfloat v2)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_011glUniform3fEifff',
        location, v0, v1, v2,
    )

  @overload(int, float, float)
  def glUniform2f(self, location: int, v0: float, v1: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glUniform2f(GLint location,
    GLfloat v0, GLfloat v1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glUniform2f

    Parameters
    ----------

    location : int
      Passed on as it is.

    v0 : float
      Passed on as it is.

    v1 : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glUniform2f(GLint location, GLfloat v0,
    #      GLfloat v1)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_011glUniform2fEiff', location, v0, v1,
    )

  @overload(int, float)
  def glUniform1f(self, location: int, v0: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glUniform1f(GLint location,
    GLfloat v0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glUniform1f

    Parameters
    ----------

    location : int
      Passed on as it is.

    v0 : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glUniform1f(GLint location, GLfloat v0)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_011glUniform1fEif', location, v0,
    )

  @overload(int)
  def glUseProgram(self, program: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glUseProgram(GLuint program)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glUseProgram

    Parameters
    ----------

    program : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glUseProgram(GLuint program)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_012glUseProgramEj', program,
    )

  @overload(int)
  def glLinkProgram(self, program: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glLinkProgram(GLuint program)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glLinkProgram

    Parameters
    ----------

    program : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glLinkProgram(GLuint program)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_013glLinkProgramEj', program,
    )

  @overload(int)
  def glIsShader(self, shader: int) -> int:
    """
    Calls Qt's 'GLboolean QOpenGLFunctions_2_0::glIsShader(GLuint shader)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glIsShader

    Parameters
    ----------

    shader : int
      Passed on as it is.
    """
    #  GLboolean QOpenGLFunctions_2_0::glIsShader(GLuint shader)
    return self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_010glIsShaderEj', shader,
    )

  @overload(int)
  def glIsProgram(self, program: int) -> int:
    """
    Calls Qt's 'GLboolean QOpenGLFunctions_2_0::glIsProgram(GLuint program)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glIsProgram

    Parameters
    ----------

    program : int
      Passed on as it is.
    """
    #  GLboolean QOpenGLFunctions_2_0::glIsProgram(GLuint program)
    return self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_011glIsProgramEj', program,
    )

  @overload(int)
  def glEnableVertexAttribArray(self, index: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glEnableVertexAttribArray(GLuint
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glEnableVertexAttribArray(GLuint index)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_025glEnableVertexAttribArrayEj',
        index,
    )

  @overload(int)
  def glDisableVertexAttribArray(self, index: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glDisableVertexAttribArray(GLuint
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glDisableVertexAttribArray(GLuint index)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_026glDisableVertexAttribArrayEj',
        index,
    )

  @overload(int, int)
  def glDetachShader(self, program: int, shader: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glDetachShader(GLuint program,
    GLuint shader)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glDetachShader

    Parameters
    ----------

    program : int
      Passed on as it is.

    shader : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glDetachShader(GLuint program, GLuint
    #      shader)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_014glDetachShaderEjj',
        program, shader,
    )

  @overload(int)
  def glDeleteShader(self, shader: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glDeleteShader(GLuint shader)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glDeleteShader

    Parameters
    ----------

    shader : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glDeleteShader(GLuint shader)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_014glDeleteShaderEj', shader,
    )

  @overload(int)
  def glDeleteProgram(self, program: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glDeleteProgram(GLuint program)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glDeleteProgram

    Parameters
    ----------

    program : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glDeleteProgram(GLuint program)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_015glDeleteProgramEj', program,
    )

  @overload(int)
  def glCreateShader(self, type: int) -> int:
    """
    Calls Qt's 'GLuint QOpenGLFunctions_2_0::glCreateShader(GLenum type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glCreateShader

    Parameters
    ----------

    type : int
      Passed on as it is.
    """
    #  GLuint QOpenGLFunctions_2_0::glCreateShader(GLenum type)
    return self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_014glCreateShaderEj', type,
    )

  def glCreateProgram(self) -> int:
    """
    Calls Qt's 'GLuint QOpenGLFunctions_2_0::glCreateProgram()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glCreateProgram
    """
    #  GLuint QOpenGLFunctions_2_0::glCreateProgram()
    return self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_015glCreateProgramEv',
    )

  @overload(int)
  def glCompileShader(self, shader: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glCompileShader(GLuint shader)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glCompileShader

    Parameters
    ----------

    shader : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glCompileShader(GLuint shader)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_015glCompileShaderEj', shader,
    )

  @overload(int, int)
  def glAttachShader(self, program: int, shader: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glAttachShader(GLuint program,
    GLuint shader)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glAttachShader

    Parameters
    ----------

    program : int
      Passed on as it is.

    shader : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glAttachShader(GLuint program, GLuint
    #      shader)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_014glAttachShaderEjj',
        program, shader,
    )

  @overload(int, int)
  def glStencilMaskSeparate(self, face: int, mask: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glStencilMaskSeparate(GLenum face,
    GLuint mask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glStencilMaskSeparate

    Parameters
    ----------

    face : int
      Passed on as it is.

    mask : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glStencilMaskSeparate(GLenum face, GLuint
    #      mask)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_021glStencilMaskSeparateEjj',
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
    Calls Qt's 'void QOpenGLFunctions_2_0::glStencilFuncSeparate(GLenum face,
    GLenum func, GLint ref, GLuint mask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glStencilFuncSeparate

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
    #  void QOpenGLFunctions_2_0::glStencilFuncSeparate(GLenum face, GLenum
    #      func, GLint ref, GLuint mask)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_021glStencilFuncSeparateEjjij',
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
    Calls Qt's 'void QOpenGLFunctions_2_0::glStencilOpSeparate(GLenum face,
    GLenum sfail, GLenum dpfail, GLenum dppass)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glStencilOpSeparate

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
    #  void QOpenGLFunctions_2_0::glStencilOpSeparate(GLenum face, GLenum
    #      sfail, GLenum dpfail, GLenum dppass)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_019glStencilOpSeparateEjjjj',
        face, sfail, dpfail, dppass,
    )

  @overload(int, int)
  def glBlendEquationSeparate(self, modeRGB: int, modeAlpha: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glBlendEquationSeparate(GLenum
    modeRGB, GLenum modeAlpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glBlendEquationSeparate

    Parameters
    ----------

    modeRGB : int
      Passed on as it is.

    modeAlpha : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glBlendEquationSeparate(GLenum modeRGB,
    #      GLenum modeAlpha)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_023glBlendEquationSeparateEjj',
        modeRGB, modeAlpha,
    )

  @overload(float, float, float)
  def glTranslatef(self, x: float, y: float, z: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glTranslatef(GLfloat x, GLfloat y,
    GLfloat z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glTranslatef

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glTranslatef(GLfloat x, GLfloat y, GLfloat
    #      z)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_012glTranslatefEfff', x, y, z,
    )

  @overload(float, float, float)
  def glTranslated(self, x: float, y: float, z: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glTranslated(GLdouble x, GLdouble
    y, GLdouble z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glTranslated

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glTranslated(GLdouble x, GLdouble y,
    #      GLdouble z)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_012glTranslatedEddd', x, y, z,
    )

  @overload(float, float, float)
  def glScalef(self, x: float, y: float, z: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glScalef(GLfloat x, GLfloat y,
    GLfloat z)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glScalef

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glScalef(GLfloat x, GLfloat y, GLfloat z)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_08glScalefEfff', x, y, z,
    )

  @overload(float, float, float)
  def glScaled(self, x: float, y: float, z: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glScaled(GLdouble x, GLdouble y,
    GLdouble z)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glScaled

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glScaled(GLdouble x, GLdouble y, GLdouble
    #      z)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_08glScaledEddd', x, y, z,
    )

  @overload(float, float, float, float)
  def glRotatef(self, angle: float, x: float, y: float, z: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glRotatef(GLfloat angle, GLfloat
    x, GLfloat y, GLfloat z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glRotatef

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
    #  void QOpenGLFunctions_2_0::glRotatef(GLfloat angle, GLfloat x, GLfloat
    #      y, GLfloat z)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_09glRotatefEffff', angle, x, y, z,
    )

  @overload(float, float, float, float)
  def glRotated(self, angle: float, x: float, y: float, z: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glRotated(GLdouble angle, GLdouble
    x, GLdouble y, GLdouble z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glRotated

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
    #  void QOpenGLFunctions_2_0::glRotated(GLdouble angle, GLdouble x,
    #      GLdouble y, GLdouble z)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_09glRotatedEdddd', angle, x, y, z,
    )

  def glPushMatrix(self) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glPushMatrix()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glPushMatrix
    """
    #  void QOpenGLFunctions_2_0::glPushMatrix()
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_2_012glPushMatrixEv')

  def glPopMatrix(self) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glPopMatrix()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glPopMatrix
    """
    #  void QOpenGLFunctions_2_0::glPopMatrix()
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_2_011glPopMatrixEv')

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
    Calls Qt's 'void QOpenGLFunctions_2_0::glOrtho(GLdouble left, GLdouble
    right, GLdouble bottom, GLdouble top, GLdouble zNear, GLdouble zFar)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glOrtho

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
    #  void QOpenGLFunctions_2_0::glOrtho(GLdouble left, GLdouble right,
    #      GLdouble bottom, GLdouble top, GLdouble zNear, GLdouble zFar)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_07glOrthoEdddddd',
        left, right, bottom, top, zNear, zFar,
    )

  @overload(int)
  def glMatrixMode(self, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glMatrixMode(GLenum mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glMatrixMode

    Parameters
    ----------

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glMatrixMode(GLenum mode)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_012glMatrixModeEj', mode,
    )

  def glLoadIdentity(self) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glLoadIdentity()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glLoadIdentity
    """
    #  void QOpenGLFunctions_2_0::glLoadIdentity()
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_2_014glLoadIdentityEv')

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
    Calls Qt's 'void QOpenGLFunctions_2_0::glFrustum(GLdouble left, GLdouble
    right, GLdouble bottom, GLdouble top, GLdouble zNear, GLdouble zFar)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glFrustum

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
    #  void QOpenGLFunctions_2_0::glFrustum(GLdouble left, GLdouble right,
    #      GLdouble bottom, GLdouble top, GLdouble zNear, GLdouble zFar)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_09glFrustumEdddddd',
        left, right, bottom, top, zNear, zFar,
    )

  @overload(int)
  def glIsList(self, list: int) -> int:
    """
    Calls Qt's 'GLboolean QOpenGLFunctions_2_0::glIsList(GLuint list)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glIsList

    Parameters
    ----------

    list : int
      Passed on as it is.
    """
    #  GLboolean QOpenGLFunctions_2_0::glIsList(GLuint list)
    return self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_08glIsListEj', list,
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
    Calls Qt's 'void QOpenGLFunctions_2_0::glCopyPixels(GLint x, GLint y,
    GLsizei width, GLsizei height, GLenum type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glCopyPixels

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
    #  void QOpenGLFunctions_2_0::glCopyPixels(GLint x, GLint y, GLsizei
    #      width, GLsizei height, GLenum type)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_012glCopyPixelsEiiiij',
        x, y, width, height, type,
    )

  @overload(int, int)
  def glPixelTransferi(self, pname: int, param: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glPixelTransferi(GLenum pname,
    GLint param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glPixelTransferi

    Parameters
    ----------

    pname : int
      Passed on as it is.

    param : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glPixelTransferi(GLenum pname, GLint param)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_016glPixelTransferiEji', pname, param,
    )

  @overload(int, float)
  def glPixelTransferf(self, pname: int, param: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glPixelTransferf(GLenum pname,
    GLfloat param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glPixelTransferf

    Parameters
    ----------

    pname : int
      Passed on as it is.

    param : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glPixelTransferf(GLenum pname, GLfloat
    #      param)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_016glPixelTransferfEjf', pname, param,
    )

  @overload(float, float)
  def glPixelZoom(self, xfactor: float, yfactor: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glPixelZoom(GLfloat xfactor,
    GLfloat yfactor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glPixelZoom

    Parameters
    ----------

    xfactor : float
      Passed on as it is.

    yfactor : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glPixelZoom(GLfloat xfactor, GLfloat
    #      yfactor)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_011glPixelZoomEff', xfactor, yfactor,
    )

  @overload(int, float)
  def glAlphaFunc(self, func: int, ref: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glAlphaFunc(GLenum func, GLfloat
    ref)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glAlphaFunc

    Parameters
    ----------

    func : int
      Passed on as it is.

    ref : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glAlphaFunc(GLenum func, GLfloat ref)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_011glAlphaFuncEjf', func, ref,
    )

  @overload(int, int)
  def glEvalPoint2(self, i: int, j: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glEvalPoint2(GLint i, GLint j)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glEvalPoint2

    Parameters
    ----------

    i : int
      Passed on as it is.

    j : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glEvalPoint2(GLint i, GLint j)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_012glEvalPoint2Eii', i, j,
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
    Calls Qt's 'void QOpenGLFunctions_2_0::glEvalMesh2(GLenum mode, GLint i1,
    GLint i2, GLint j1, GLint j2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glEvalMesh2

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
    #  void QOpenGLFunctions_2_0::glEvalMesh2(GLenum mode, GLint i1, GLint
    #      i2, GLint j1, GLint j2)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_011glEvalMesh2Ejiiii',
        mode, i1, i2, j1, j2,
    )

  @overload(int)
  def glEvalPoint1(self, i: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glEvalPoint1(GLint i)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glEvalPoint1

    Parameters
    ----------

    i : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glEvalPoint1(GLint i)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_2_012glEvalPoint1Ei', i)

  @overload(int, int, int)
  def glEvalMesh1(self, mode: int, i1: int, i2: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glEvalMesh1(GLenum mode, GLint i1,
    GLint i2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glEvalMesh1

    Parameters
    ----------

    mode : int
      Passed on as it is.

    i1 : int
      Passed on as it is.

    i2 : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glEvalMesh1(GLenum mode, GLint i1, GLint
    #      i2)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_011glEvalMesh1Ejii', mode, i1, i2,
    )

  @overload(float, float)
  def glEvalCoord2f(self, u: float, v: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glEvalCoord2f(GLfloat u, GLfloat
    v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glEvalCoord2f

    Parameters
    ----------

    u : float
      Passed on as it is.

    v : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glEvalCoord2f(GLfloat u, GLfloat v)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_013glEvalCoord2fEff', u, v,
    )

  @overload(float, float)
  def glEvalCoord2d(self, u: float, v: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glEvalCoord2d(GLdouble u, GLdouble
    v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glEvalCoord2d

    Parameters
    ----------

    u : float
      Passed on as it is.

    v : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glEvalCoord2d(GLdouble u, GLdouble v)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_013glEvalCoord2dEdd', u, v,
    )

  @overload(float)
  def glEvalCoord1f(self, u: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glEvalCoord1f(GLfloat u)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glEvalCoord1f

    Parameters
    ----------

    u : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glEvalCoord1f(GLfloat u)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_2_013glEvalCoord1fEf', u)

  @overload(float)
  def glEvalCoord1d(self, u: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glEvalCoord1d(GLdouble u)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glEvalCoord1d

    Parameters
    ----------

    u : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glEvalCoord1d(GLdouble u)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_2_013glEvalCoord1dEd', u)

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
    Calls Qt's 'void QOpenGLFunctions_2_0::glMapGrid2f(GLint un, GLfloat u1,
    GLfloat u2, GLint vn, GLfloat v1, GLfloat v2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glMapGrid2f

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
    #  void QOpenGLFunctions_2_0::glMapGrid2f(GLint un, GLfloat u1, GLfloat
    #      u2, GLint vn, GLfloat v1, GLfloat v2)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_011glMapGrid2fEiffiff',
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
    Calls Qt's 'void QOpenGLFunctions_2_0::glMapGrid2d(GLint un, GLdouble u1,
    GLdouble u2, GLint vn, GLdouble v1, GLdouble v2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glMapGrid2d

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
    #  void QOpenGLFunctions_2_0::glMapGrid2d(GLint un, GLdouble u1, GLdouble
    #      u2, GLint vn, GLdouble v1, GLdouble v2)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_011glMapGrid2dEiddidd',
        un, u1, u2, vn, v1, v2,
    )

  @overload(int, float, float)
  def glMapGrid1f(self, un: int, u1: float, u2: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glMapGrid1f(GLint un, GLfloat u1,
    GLfloat u2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glMapGrid1f

    Parameters
    ----------

    un : int
      Passed on as it is.

    u1 : float
      Passed on as it is.

    u2 : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glMapGrid1f(GLint un, GLfloat u1, GLfloat
    #      u2)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_011glMapGrid1fEiff', un, u1, u2,
    )

  @overload(int, float, float)
  def glMapGrid1d(self, un: int, u1: float, u2: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glMapGrid1d(GLint un, GLdouble u1,
    GLdouble u2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glMapGrid1d

    Parameters
    ----------

    un : int
      Passed on as it is.

    u1 : float
      Passed on as it is.

    u2 : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glMapGrid1d(GLint un, GLdouble u1, GLdouble
    #      u2)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_011glMapGrid1dEidd', un, u1, u2,
    )

  @overload(int)
  def glPushAttrib(self, mask: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glPushAttrib(GLbitfield mask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glPushAttrib

    Parameters
    ----------

    mask : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glPushAttrib(GLbitfield mask)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_012glPushAttribEj', mask,
    )

  def glPopAttrib(self) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glPopAttrib()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glPopAttrib
    """
    #  void QOpenGLFunctions_2_0::glPopAttrib()
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_2_011glPopAttribEv')

  @overload(int, float)
  def glAccum(self, op: int, value: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glAccum(GLenum op, GLfloat
    value)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glAccum

    Parameters
    ----------

    op : int
      Passed on as it is.

    value : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glAccum(GLenum op, GLfloat value)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_07glAccumEjf', op, value,
    )

  @overload(int)
  def glIndexMask(self, mask: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glIndexMask(GLuint mask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glIndexMask

    Parameters
    ----------

    mask : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glIndexMask(GLuint mask)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_011glIndexMaskEj', mask,
    )

  @overload(float)
  def glClearIndex(self, c: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glClearIndex(GLfloat c)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glClearIndex

    Parameters
    ----------

    c : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glClearIndex(GLfloat c)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_2_012glClearIndexEf', c)

  @overload(float, float, float, float)
  def glClearAccum(
      self,
      red: float,
      green: float,
      blue: float,
      alpha: float,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glClearAccum(GLfloat red, GLfloat
    green, GLfloat blue, GLfloat alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glClearAccum

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
    #  void QOpenGLFunctions_2_0::glClearAccum(GLfloat red, GLfloat green,
    #      GLfloat blue, GLfloat alpha)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_012glClearAccumEffff',
        red, green, blue, alpha,
    )

  @overload(int)
  def glPushName(self, name: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glPushName(GLuint name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glPushName

    Parameters
    ----------

    name : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glPushName(GLuint name)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_2_010glPushNameEj', name)

  def glPopName(self) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glPopName()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glPopName
    """
    #  void QOpenGLFunctions_2_0::glPopName()
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_2_09glPopNameEv')

  @overload(float)
  def glPassThrough(self, token: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glPassThrough(GLfloat token)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glPassThrough

    Parameters
    ----------

    token : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glPassThrough(GLfloat token)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_013glPassThroughEf', token,
    )

  @overload(int)
  def glLoadName(self, name: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glLoadName(GLuint name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glLoadName

    Parameters
    ----------

    name : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glLoadName(GLuint name)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_2_010glLoadNameEj', name)

  def glInitNames(self) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glInitNames()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glInitNames
    """
    #  void QOpenGLFunctions_2_0::glInitNames()
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_2_011glInitNamesEv')

  @overload(int)
  def glRenderMode(self, mode: int) -> int:
    """
    Calls Qt's 'GLint QOpenGLFunctions_2_0::glRenderMode(GLenum mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glRenderMode

    Parameters
    ----------

    mode : int
      Passed on as it is.
    """
    #  GLint QOpenGLFunctions_2_0::glRenderMode(GLenum mode)
    return self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_012glRenderModeEj', mode,
    )

  @overload(int, int, int)
  def glTexGeni(self, coord: int, pname: int, param: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glTexGeni(GLenum coord, GLenum
    pname, GLint param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glTexGeni

    Parameters
    ----------

    coord : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    param : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glTexGeni(GLenum coord, GLenum pname, GLint
    #      param)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_09glTexGeniEjji', coord, pname, param,
    )

  @overload(int, int, float)
  def glTexGenf(self, coord: int, pname: int, param: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glTexGenf(GLenum coord, GLenum
    pname, GLfloat param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glTexGenf

    Parameters
    ----------

    coord : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    param : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glTexGenf(GLenum coord, GLenum pname,
    #      GLfloat param)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_09glTexGenfEjjf', coord, pname, param,
    )

  @overload(int, int, float)
  def glTexGend(self, coord: int, pname: int, param: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glTexGend(GLenum coord, GLenum
    pname, GLdouble param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glTexGend

    Parameters
    ----------

    coord : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    param : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glTexGend(GLenum coord, GLenum pname,
    #      GLdouble param)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_09glTexGendEjjd', coord, pname, param,
    )

  @overload(int, int, int)
  def glTexEnvi(self, target: int, pname: int, param: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glTexEnvi(GLenum target, GLenum
    pname, GLint param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glTexEnvi

    Parameters
    ----------

    target : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    param : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glTexEnvi(GLenum target, GLenum pname,
    #      GLint param)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_09glTexEnviEjji',
        target, pname, param,
    )

  @overload(int, int, float)
  def glTexEnvf(self, target: int, pname: int, param: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glTexEnvf(GLenum target, GLenum
    pname, GLfloat param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glTexEnvf

    Parameters
    ----------

    target : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    param : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glTexEnvf(GLenum target, GLenum pname,
    #      GLfloat param)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_09glTexEnvfEjjf',
        target, pname, param,
    )

  @overload(int)
  def glShadeModel(self, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glShadeModel(GLenum mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glShadeModel

    Parameters
    ----------

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glShadeModel(GLenum mode)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_012glShadeModelEj', mode,
    )

  @overload(int, int, int)
  def glMateriali(self, face: int, pname: int, param: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glMateriali(GLenum face, GLenum
    pname, GLint param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glMateriali

    Parameters
    ----------

    face : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    param : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glMateriali(GLenum face, GLenum pname,
    #      GLint param)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_011glMaterialiEjji',
        face, pname, param,
    )

  @overload(int, int, float)
  def glMaterialf(self, face: int, pname: int, param: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glMaterialf(GLenum face, GLenum
    pname, GLfloat param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glMaterialf

    Parameters
    ----------

    face : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    param : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glMaterialf(GLenum face, GLenum pname,
    #      GLfloat param)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_011glMaterialfEjjf',
        face, pname, param,
    )

  @overload(int, int)
  def glLineStipple(self, factor: int, pattern: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glLineStipple(GLint factor,
    GLushort pattern)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glLineStipple

    Parameters
    ----------

    factor : int
      Passed on as it is.

    pattern : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glLineStipple(GLint factor, GLushort
    #      pattern)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_013glLineStippleEit', factor, pattern,
    )

  @overload(int, int)
  def glLightModeli(self, pname: int, param: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glLightModeli(GLenum pname, GLint
    param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glLightModeli

    Parameters
    ----------

    pname : int
      Passed on as it is.

    param : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glLightModeli(GLenum pname, GLint param)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_013glLightModeliEji', pname, param,
    )

  @overload(int, float)
  def glLightModelf(self, pname: int, param: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glLightModelf(GLenum pname,
    GLfloat param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glLightModelf

    Parameters
    ----------

    pname : int
      Passed on as it is.

    param : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glLightModelf(GLenum pname, GLfloat param)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_013glLightModelfEjf', pname, param,
    )

  @overload(int, int, int)
  def glLighti(self, light: int, pname: int, param: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glLighti(GLenum light, GLenum
    pname, GLint param)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glLighti

    Parameters
    ----------

    light : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    param : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glLighti(GLenum light, GLenum pname, GLint
    #      param)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_08glLightiEjji', light, pname, param,
    )

  @overload(int, int, float)
  def glLightf(self, light: int, pname: int, param: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glLightf(GLenum light, GLenum
    pname, GLfloat param)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glLightf

    Parameters
    ----------

    light : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    param : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glLightf(GLenum light, GLenum pname,
    #      GLfloat param)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_08glLightfEjjf', light, pname, param,
    )

  @overload(int, int)
  def glFogi(self, pname: int, param: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glFogi(GLenum pname, GLint
    param)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glFogi

    Parameters
    ----------

    pname : int
      Passed on as it is.

    param : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glFogi(GLenum pname, GLint param)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_06glFogiEji', pname, param,
    )

  @overload(int, float)
  def glFogf(self, pname: int, param: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glFogf(GLenum pname, GLfloat
    param)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glFogf

    Parameters
    ----------

    pname : int
      Passed on as it is.

    param : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glFogf(GLenum pname, GLfloat param)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_06glFogfEjf', pname, param,
    )

  @overload(int, int)
  def glColorMaterial(self, face: int, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glColorMaterial(GLenum face,
    GLenum mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glColorMaterial

    Parameters
    ----------

    face : int
      Passed on as it is.

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glColorMaterial(GLenum face, GLenum mode)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_015glColorMaterialEjj', face, mode,
    )

  @overload(int, int, int, int)
  def glVertex4s(self, x: int, y: int, z: int, w: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glVertex4s(GLshort x, GLshort y,
    GLshort z, GLshort w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glVertex4s

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
    #  void QOpenGLFunctions_2_0::glVertex4s(GLshort x, GLshort y, GLshort z,
    #      GLshort w)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_010glVertex4sEssss', x, y, z, w,
    )

  @overload(int, int, int, int)
  def glVertex4i(self, x: int, y: int, z: int, w: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glVertex4i(GLint x, GLint y, GLint
    z, GLint w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glVertex4i

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
    #  void QOpenGLFunctions_2_0::glVertex4i(GLint x, GLint y, GLint z, GLint
    #      w)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_010glVertex4iEiiii', x, y, z, w,
    )

  @overload(float, float, float, float)
  def glVertex4f(self, x: float, y: float, z: float, w: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glVertex4f(GLfloat x, GLfloat y,
    GLfloat z, GLfloat w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glVertex4f

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
    #  void QOpenGLFunctions_2_0::glVertex4f(GLfloat x, GLfloat y, GLfloat z,
    #      GLfloat w)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_010glVertex4fEffff', x, y, z, w,
    )

  @overload(float, float, float, float)
  def glVertex4d(self, x: float, y: float, z: float, w: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glVertex4d(GLdouble x, GLdouble y,
    GLdouble z, GLdouble w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glVertex4d

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
    #  void QOpenGLFunctions_2_0::glVertex4d(GLdouble x, GLdouble y, GLdouble
    #      z, GLdouble w)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_010glVertex4dEdddd', x, y, z, w,
    )

  @overload(int, int, int)
  def glVertex3s(self, x: int, y: int, z: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glVertex3s(GLshort x, GLshort y,
    GLshort z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glVertex3s

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    z : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glVertex3s(GLshort x, GLshort y, GLshort z)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_010glVertex3sEsss', x, y, z,
    )

  @overload(int, int, int)
  def glVertex3i(self, x: int, y: int, z: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glVertex3i(GLint x, GLint y, GLint
    z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glVertex3i

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    z : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glVertex3i(GLint x, GLint y, GLint z)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_010glVertex3iEiii', x, y, z,
    )

  @overload(float, float, float)
  def glVertex3f(self, x: float, y: float, z: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glVertex3f(GLfloat x, GLfloat y,
    GLfloat z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glVertex3f

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glVertex3f(GLfloat x, GLfloat y, GLfloat z)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_010glVertex3fEfff', x, y, z,
    )

  @overload(float, float, float)
  def glVertex3d(self, x: float, y: float, z: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glVertex3d(GLdouble x, GLdouble y,
    GLdouble z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glVertex3d

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glVertex3d(GLdouble x, GLdouble y, GLdouble
    #      z)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_010glVertex3dEddd', x, y, z,
    )

  @overload(int, int)
  def glVertex2s(self, x: int, y: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glVertex2s(GLshort x, GLshort y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glVertex2s

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glVertex2s(GLshort x, GLshort y)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_010glVertex2sEss', x, y,
    )

  @overload(int, int)
  def glVertex2i(self, x: int, y: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glVertex2i(GLint x, GLint y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glVertex2i

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glVertex2i(GLint x, GLint y)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_010glVertex2iEii', x, y,
    )

  @overload(float, float)
  def glVertex2f(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glVertex2f(GLfloat x, GLfloat y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glVertex2f

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glVertex2f(GLfloat x, GLfloat y)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_010glVertex2fEff', x, y,
    )

  @overload(float, float)
  def glVertex2d(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glVertex2d(GLdouble x, GLdouble
    y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glVertex2d

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glVertex2d(GLdouble x, GLdouble y)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_010glVertex2dEdd', x, y,
    )

  @overload(int, int, int, int)
  def glTexCoord4s(self, s: int, t: int, r: int, q: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glTexCoord4s(GLshort s, GLshort t,
    GLshort r, GLshort q)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glTexCoord4s

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
    #  void QOpenGLFunctions_2_0::glTexCoord4s(GLshort s, GLshort t, GLshort
    #      r, GLshort q)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_012glTexCoord4sEssss', s, t, r, q,
    )

  @overload(int, int, int, int)
  def glTexCoord4i(self, s: int, t: int, r: int, q: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glTexCoord4i(GLint s, GLint t,
    GLint r, GLint q)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glTexCoord4i

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
    #  void QOpenGLFunctions_2_0::glTexCoord4i(GLint s, GLint t, GLint r,
    #      GLint q)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_012glTexCoord4iEiiii', s, t, r, q,
    )

  @overload(float, float, float, float)
  def glTexCoord4f(self, s: float, t: float, r: float, q: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glTexCoord4f(GLfloat s, GLfloat t,
    GLfloat r, GLfloat q)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glTexCoord4f

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
    #  void QOpenGLFunctions_2_0::glTexCoord4f(GLfloat s, GLfloat t, GLfloat
    #      r, GLfloat q)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_012glTexCoord4fEffff', s, t, r, q,
    )

  @overload(float, float, float, float)
  def glTexCoord4d(self, s: float, t: float, r: float, q: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glTexCoord4d(GLdouble s, GLdouble
    t, GLdouble r, GLdouble q)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glTexCoord4d

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
    #  void QOpenGLFunctions_2_0::glTexCoord4d(GLdouble s, GLdouble t,
    #      GLdouble r, GLdouble q)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_012glTexCoord4dEdddd', s, t, r, q,
    )

  @overload(int, int, int)
  def glTexCoord3s(self, s: int, t: int, r: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glTexCoord3s(GLshort s, GLshort t,
    GLshort r)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glTexCoord3s

    Parameters
    ----------

    s : int
      Passed on as it is.

    t : int
      Passed on as it is.

    r : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glTexCoord3s(GLshort s, GLshort t, GLshort
    #      r)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_012glTexCoord3sEsss', s, t, r,
    )

  @overload(int, int, int)
  def glTexCoord3i(self, s: int, t: int, r: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glTexCoord3i(GLint s, GLint t,
    GLint r)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glTexCoord3i

    Parameters
    ----------

    s : int
      Passed on as it is.

    t : int
      Passed on as it is.

    r : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glTexCoord3i(GLint s, GLint t, GLint r)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_012glTexCoord3iEiii', s, t, r,
    )

  @overload(float, float, float)
  def glTexCoord3f(self, s: float, t: float, r: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glTexCoord3f(GLfloat s, GLfloat t,
    GLfloat r)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glTexCoord3f

    Parameters
    ----------

    s : float
      Passed on as it is.

    t : float
      Passed on as it is.

    r : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glTexCoord3f(GLfloat s, GLfloat t, GLfloat
    #      r)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_012glTexCoord3fEfff', s, t, r,
    )

  @overload(float, float, float)
  def glTexCoord3d(self, s: float, t: float, r: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glTexCoord3d(GLdouble s, GLdouble
    t, GLdouble r)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glTexCoord3d

    Parameters
    ----------

    s : float
      Passed on as it is.

    t : float
      Passed on as it is.

    r : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glTexCoord3d(GLdouble s, GLdouble t,
    #      GLdouble r)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_012glTexCoord3dEddd', s, t, r,
    )

  @overload(int, int)
  def glTexCoord2s(self, s: int, t: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glTexCoord2s(GLshort s, GLshort
    t)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glTexCoord2s

    Parameters
    ----------

    s : int
      Passed on as it is.

    t : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glTexCoord2s(GLshort s, GLshort t)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_012glTexCoord2sEss', s, t,
    )

  @overload(int, int)
  def glTexCoord2i(self, s: int, t: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glTexCoord2i(GLint s, GLint t)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glTexCoord2i

    Parameters
    ----------

    s : int
      Passed on as it is.

    t : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glTexCoord2i(GLint s, GLint t)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_012glTexCoord2iEii', s, t,
    )

  @overload(float, float)
  def glTexCoord2f(self, s: float, t: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glTexCoord2f(GLfloat s, GLfloat
    t)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glTexCoord2f

    Parameters
    ----------

    s : float
      Passed on as it is.

    t : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glTexCoord2f(GLfloat s, GLfloat t)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_012glTexCoord2fEff', s, t,
    )

  @overload(float, float)
  def glTexCoord2d(self, s: float, t: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glTexCoord2d(GLdouble s, GLdouble
    t)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glTexCoord2d

    Parameters
    ----------

    s : float
      Passed on as it is.

    t : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glTexCoord2d(GLdouble s, GLdouble t)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_012glTexCoord2dEdd', s, t,
    )

  @overload(int)
  def glTexCoord1s(self, s: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glTexCoord1s(GLshort s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glTexCoord1s

    Parameters
    ----------

    s : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glTexCoord1s(GLshort s)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_2_012glTexCoord1sEs', s)

  @overload(int)
  def glTexCoord1i(self, s: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glTexCoord1i(GLint s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glTexCoord1i

    Parameters
    ----------

    s : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glTexCoord1i(GLint s)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_2_012glTexCoord1iEi', s)

  @overload(float)
  def glTexCoord1f(self, s: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glTexCoord1f(GLfloat s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glTexCoord1f

    Parameters
    ----------

    s : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glTexCoord1f(GLfloat s)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_2_012glTexCoord1fEf', s)

  @overload(float)
  def glTexCoord1d(self, s: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glTexCoord1d(GLdouble s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glTexCoord1d

    Parameters
    ----------

    s : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glTexCoord1d(GLdouble s)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_2_012glTexCoord1dEd', s)

  @overload(int, int, int, int)
  def glRects(self, x1: int, y1: int, x2: int, y2: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glRects(GLshort x1, GLshort y1,
    GLshort x2, GLshort y2)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glRects

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
    #  void QOpenGLFunctions_2_0::glRects(GLshort x1, GLshort y1, GLshort x2,
    #      GLshort y2)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_07glRectsEssss', x1, y1, x2, y2,
    )

  @overload(int, int, int, int)
  def glRecti(self, x1: int, y1: int, x2: int, y2: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glRecti(GLint x1, GLint y1, GLint
    x2, GLint y2)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glRecti

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
    #  void QOpenGLFunctions_2_0::glRecti(GLint x1, GLint y1, GLint x2, GLint
    #      y2)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_07glRectiEiiii', x1, y1, x2, y2,
    )

  @overload(float, float, float, float)
  def glRectf(self, x1: float, y1: float, x2: float, y2: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glRectf(GLfloat x1, GLfloat y1,
    GLfloat x2, GLfloat y2)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glRectf

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
    #  void QOpenGLFunctions_2_0::glRectf(GLfloat x1, GLfloat y1, GLfloat x2,
    #      GLfloat y2)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_07glRectfEffff', x1, y1, x2, y2,
    )

  @overload(float, float, float, float)
  def glRectd(self, x1: float, y1: float, x2: float, y2: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glRectd(GLdouble x1, GLdouble y1,
    GLdouble x2, GLdouble y2)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glRectd

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
    #  void QOpenGLFunctions_2_0::glRectd(GLdouble x1, GLdouble y1, GLdouble
    #      x2, GLdouble y2)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_07glRectdEdddd', x1, y1, x2, y2,
    )

  @overload(int, int, int, int)
  def glRasterPos4s(self, x: int, y: int, z: int, w: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glRasterPos4s(GLshort x, GLshort
    y, GLshort z, GLshort w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glRasterPos4s

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
    #  void QOpenGLFunctions_2_0::glRasterPos4s(GLshort x, GLshort y, GLshort
    #      z, GLshort w)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_013glRasterPos4sEssss', x, y, z, w,
    )

  @overload(int, int, int, int)
  def glRasterPos4i(self, x: int, y: int, z: int, w: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glRasterPos4i(GLint x, GLint y,
    GLint z, GLint w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glRasterPos4i

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
    #  void QOpenGLFunctions_2_0::glRasterPos4i(GLint x, GLint y, GLint z,
    #      GLint w)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_013glRasterPos4iEiiii', x, y, z, w,
    )

  @overload(float, float, float, float)
  def glRasterPos4f(self, x: float, y: float, z: float, w: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glRasterPos4f(GLfloat x, GLfloat
    y, GLfloat z, GLfloat w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glRasterPos4f

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
    #  void QOpenGLFunctions_2_0::glRasterPos4f(GLfloat x, GLfloat y, GLfloat
    #      z, GLfloat w)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_013glRasterPos4fEffff', x, y, z, w,
    )

  @overload(float, float, float, float)
  def glRasterPos4d(self, x: float, y: float, z: float, w: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glRasterPos4d(GLdouble x, GLdouble
    y, GLdouble z, GLdouble w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glRasterPos4d

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
    #  void QOpenGLFunctions_2_0::glRasterPos4d(GLdouble x, GLdouble y,
    #      GLdouble z, GLdouble w)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_013glRasterPos4dEdddd', x, y, z, w,
    )

  @overload(int, int, int)
  def glRasterPos3s(self, x: int, y: int, z: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glRasterPos3s(GLshort x, GLshort
    y, GLshort z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glRasterPos3s

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    z : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glRasterPos3s(GLshort x, GLshort y, GLshort
    #      z)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_013glRasterPos3sEsss', x, y, z,
    )

  @overload(int, int, int)
  def glRasterPos3i(self, x: int, y: int, z: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glRasterPos3i(GLint x, GLint y,
    GLint z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glRasterPos3i

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    z : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glRasterPos3i(GLint x, GLint y, GLint z)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_013glRasterPos3iEiii', x, y, z,
    )

  @overload(float, float, float)
  def glRasterPos3f(self, x: float, y: float, z: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glRasterPos3f(GLfloat x, GLfloat
    y, GLfloat z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glRasterPos3f

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glRasterPos3f(GLfloat x, GLfloat y, GLfloat
    #      z)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_013glRasterPos3fEfff', x, y, z,
    )

  @overload(float, float, float)
  def glRasterPos3d(self, x: float, y: float, z: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glRasterPos3d(GLdouble x, GLdouble
    y, GLdouble z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glRasterPos3d

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glRasterPos3d(GLdouble x, GLdouble y,
    #      GLdouble z)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_013glRasterPos3dEddd', x, y, z,
    )

  @overload(int, int)
  def glRasterPos2s(self, x: int, y: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glRasterPos2s(GLshort x, GLshort
    y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glRasterPos2s

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glRasterPos2s(GLshort x, GLshort y)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_013glRasterPos2sEss', x, y,
    )

  @overload(int, int)
  def glRasterPos2i(self, x: int, y: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glRasterPos2i(GLint x, GLint y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glRasterPos2i

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glRasterPos2i(GLint x, GLint y)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_013glRasterPos2iEii', x, y,
    )

  @overload(float, float)
  def glRasterPos2f(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glRasterPos2f(GLfloat x, GLfloat
    y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glRasterPos2f

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glRasterPos2f(GLfloat x, GLfloat y)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_013glRasterPos2fEff', x, y,
    )

  @overload(float, float)
  def glRasterPos2d(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glRasterPos2d(GLdouble x, GLdouble
    y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glRasterPos2d

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glRasterPos2d(GLdouble x, GLdouble y)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_013glRasterPos2dEdd', x, y,
    )

  @overload(int, int, int)
  def glNormal3s(self, nx: int, ny: int, nz: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glNormal3s(GLshort nx, GLshort ny,
    GLshort nz)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glNormal3s

    Parameters
    ----------

    nx : int
      Passed on as it is.

    ny : int
      Passed on as it is.

    nz : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glNormal3s(GLshort nx, GLshort ny, GLshort
    #      nz)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_010glNormal3sEsss', nx, ny, nz,
    )

  @overload(int, int, int)
  def glNormal3i(self, nx: int, ny: int, nz: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glNormal3i(GLint nx, GLint ny,
    GLint nz)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glNormal3i

    Parameters
    ----------

    nx : int
      Passed on as it is.

    ny : int
      Passed on as it is.

    nz : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glNormal3i(GLint nx, GLint ny, GLint nz)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_010glNormal3iEiii', nx, ny, nz,
    )

  @overload(float, float, float)
  def glNormal3f(self, nx: float, ny: float, nz: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glNormal3f(GLfloat nx, GLfloat ny,
    GLfloat nz)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glNormal3f

    Parameters
    ----------

    nx : float
      Passed on as it is.

    ny : float
      Passed on as it is.

    nz : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glNormal3f(GLfloat nx, GLfloat ny, GLfloat
    #      nz)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_010glNormal3fEfff', nx, ny, nz,
    )

  @overload(float, float, float)
  def glNormal3d(self, nx: float, ny: float, nz: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glNormal3d(GLdouble nx, GLdouble
    ny, GLdouble nz)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glNormal3d

    Parameters
    ----------

    nx : float
      Passed on as it is.

    ny : float
      Passed on as it is.

    nz : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glNormal3d(GLdouble nx, GLdouble ny,
    #      GLdouble nz)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_010glNormal3dEddd', nx, ny, nz,
    )

  @overload(int, int, int)
  def glNormal3b(self, nx: int, ny: int, nz: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glNormal3b(GLbyte nx, GLbyte ny,
    GLbyte nz)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glNormal3b

    Parameters
    ----------

    nx : int
      Passed on as it is.

    ny : int
      Passed on as it is.

    nz : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glNormal3b(GLbyte nx, GLbyte ny, GLbyte nz)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_010glNormal3bEaaa', nx, ny, nz,
    )

  @overload(int)
  def glIndexs(self, c: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glIndexs(GLshort c)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glIndexs

    Parameters
    ----------

    c : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glIndexs(GLshort c)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_2_08glIndexsEs', c)

  @overload(int)
  def glIndexi(self, c: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glIndexi(GLint c)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glIndexi

    Parameters
    ----------

    c : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glIndexi(GLint c)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_2_08glIndexiEi', c)

  @overload(float)
  def glIndexf(self, c: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glIndexf(GLfloat c)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glIndexf

    Parameters
    ----------

    c : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glIndexf(GLfloat c)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_2_08glIndexfEf', c)

  @overload(float)
  def glIndexd(self, c: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glIndexd(GLdouble c)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glIndexd

    Parameters
    ----------

    c : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glIndexd(GLdouble c)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_2_08glIndexdEd', c)

  def glEnd(self) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glEnd()'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glEnd
    """
    #  void QOpenGLFunctions_2_0::glEnd()
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_2_05glEndEv')

  @overload(int)
  def glEdgeFlag(self, flag: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glEdgeFlag(GLboolean flag)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glEdgeFlag

    Parameters
    ----------

    flag : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glEdgeFlag(GLboolean flag)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_2_010glEdgeFlagEh', flag)

  @overload(int, int, int, int)
  def glColor4us(self, red: int, green: int, blue: int, alpha: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glColor4us(GLushort red, GLushort
    green, GLushort blue, GLushort alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glColor4us

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
    #  void QOpenGLFunctions_2_0::glColor4us(GLushort red, GLushort green,
    #      GLushort blue, GLushort alpha)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_010glColor4usEtttt',
        red, green, blue, alpha,
    )

  @overload(int, int, int, int)
  def glColor4ui(self, red: int, green: int, blue: int, alpha: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glColor4ui(GLuint red, GLuint
    green, GLuint blue, GLuint alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glColor4ui

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
    #  void QOpenGLFunctions_2_0::glColor4ui(GLuint red, GLuint green, GLuint
    #      blue, GLuint alpha)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_010glColor4uiEjjjj',
        red, green, blue, alpha,
    )

  @overload(int, int, int, int)
  def glColor4ub(self, red: int, green: int, blue: int, alpha: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glColor4ub(GLubyte red, GLubyte
    green, GLubyte blue, GLubyte alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glColor4ub

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
    #  void QOpenGLFunctions_2_0::glColor4ub(GLubyte red, GLubyte green,
    #      GLubyte blue, GLubyte alpha)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_010glColor4ubEhhhh',
        red, green, blue, alpha,
    )

  @overload(int, int, int, int)
  def glColor4s(self, red: int, green: int, blue: int, alpha: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glColor4s(GLshort red, GLshort
    green, GLshort blue, GLshort alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glColor4s

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
    #  void QOpenGLFunctions_2_0::glColor4s(GLshort red, GLshort green,
    #      GLshort blue, GLshort alpha)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_09glColor4sEssss',
        red, green, blue, alpha,
    )

  @overload(int, int, int, int)
  def glColor4i(self, red: int, green: int, blue: int, alpha: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glColor4i(GLint red, GLint green,
    GLint blue, GLint alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glColor4i

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
    #  void QOpenGLFunctions_2_0::glColor4i(GLint red, GLint green, GLint
    #      blue, GLint alpha)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_09glColor4iEiiii',
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
    Calls Qt's 'void QOpenGLFunctions_2_0::glColor4f(GLfloat red, GLfloat
    green, GLfloat blue, GLfloat alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glColor4f

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
    #  void QOpenGLFunctions_2_0::glColor4f(GLfloat red, GLfloat green,
    #      GLfloat blue, GLfloat alpha)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_09glColor4fEffff',
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
    Calls Qt's 'void QOpenGLFunctions_2_0::glColor4d(GLdouble red, GLdouble
    green, GLdouble blue, GLdouble alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glColor4d

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
    #  void QOpenGLFunctions_2_0::glColor4d(GLdouble red, GLdouble green,
    #      GLdouble blue, GLdouble alpha)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_09glColor4dEdddd',
        red, green, blue, alpha,
    )

  @overload(int, int, int, int)
  def glColor4b(self, red: int, green: int, blue: int, alpha: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glColor4b(GLbyte red, GLbyte
    green, GLbyte blue, GLbyte alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glColor4b

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
    #  void QOpenGLFunctions_2_0::glColor4b(GLbyte red, GLbyte green, GLbyte
    #      blue, GLbyte alpha)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_09glColor4bEaaaa',
        red, green, blue, alpha,
    )

  @overload(int, int, int)
  def glColor3us(self, red: int, green: int, blue: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glColor3us(GLushort red, GLushort
    green, GLushort blue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glColor3us

    Parameters
    ----------

    red : int
      Passed on as it is.

    green : int
      Passed on as it is.

    blue : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glColor3us(GLushort red, GLushort green,
    #      GLushort blue)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_010glColor3usEttt', red, green, blue,
    )

  @overload(int, int, int)
  def glColor3ui(self, red: int, green: int, blue: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glColor3ui(GLuint red, GLuint
    green, GLuint blue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glColor3ui

    Parameters
    ----------

    red : int
      Passed on as it is.

    green : int
      Passed on as it is.

    blue : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glColor3ui(GLuint red, GLuint green, GLuint
    #      blue)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_010glColor3uiEjjj', red, green, blue,
    )

  @overload(int, int, int)
  def glColor3ub(self, red: int, green: int, blue: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glColor3ub(GLubyte red, GLubyte
    green, GLubyte blue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glColor3ub

    Parameters
    ----------

    red : int
      Passed on as it is.

    green : int
      Passed on as it is.

    blue : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glColor3ub(GLubyte red, GLubyte green,
    #      GLubyte blue)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_010glColor3ubEhhh', red, green, blue,
    )

  @overload(int, int, int)
  def glColor3s(self, red: int, green: int, blue: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glColor3s(GLshort red, GLshort
    green, GLshort blue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glColor3s

    Parameters
    ----------

    red : int
      Passed on as it is.

    green : int
      Passed on as it is.

    blue : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glColor3s(GLshort red, GLshort green,
    #      GLshort blue)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_09glColor3sEsss', red, green, blue,
    )

  @overload(int, int, int)
  def glColor3i(self, red: int, green: int, blue: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glColor3i(GLint red, GLint green,
    GLint blue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glColor3i

    Parameters
    ----------

    red : int
      Passed on as it is.

    green : int
      Passed on as it is.

    blue : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glColor3i(GLint red, GLint green, GLint
    #      blue)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_09glColor3iEiii', red, green, blue,
    )

  @overload(float, float, float)
  def glColor3f(self, red: float, green: float, blue: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glColor3f(GLfloat red, GLfloat
    green, GLfloat blue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glColor3f

    Parameters
    ----------

    red : float
      Passed on as it is.

    green : float
      Passed on as it is.

    blue : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glColor3f(GLfloat red, GLfloat green,
    #      GLfloat blue)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_09glColor3fEfff', red, green, blue,
    )

  @overload(float, float, float)
  def glColor3d(self, red: float, green: float, blue: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glColor3d(GLdouble red, GLdouble
    green, GLdouble blue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glColor3d

    Parameters
    ----------

    red : float
      Passed on as it is.

    green : float
      Passed on as it is.

    blue : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glColor3d(GLdouble red, GLdouble green,
    #      GLdouble blue)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_09glColor3dEddd', red, green, blue,
    )

  @overload(int, int, int)
  def glColor3b(self, red: int, green: int, blue: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glColor3b(GLbyte red, GLbyte
    green, GLbyte blue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glColor3b

    Parameters
    ----------

    red : int
      Passed on as it is.

    green : int
      Passed on as it is.

    blue : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glColor3b(GLbyte red, GLbyte green, GLbyte
    #      blue)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_09glColor3bEaaa', red, green, blue,
    )

  @overload(int)
  def glBegin(self, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glBegin(GLenum mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glBegin

    Parameters
    ----------

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glBegin(GLenum mode)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_2_07glBeginEj', mode)

  @overload(int)
  def glListBase(self, base: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glListBase(GLuint base)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glListBase

    Parameters
    ----------

    base : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glListBase(GLuint base)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_2_010glListBaseEj', base)

  @overload(int)
  def glGenLists(self, range: int) -> int:
    """
    Calls Qt's 'GLuint QOpenGLFunctions_2_0::glGenLists(GLsizei range)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glGenLists

    Parameters
    ----------

    range : int
      Passed on as it is.
    """
    #  GLuint QOpenGLFunctions_2_0::glGenLists(GLsizei range)
    return self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_010glGenListsEi', range,
    )

  @overload(int, int)
  def glDeleteLists(self, list: int, range: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glDeleteLists(GLuint list, GLsizei
    range)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glDeleteLists

    Parameters
    ----------

    list : int
      Passed on as it is.

    range : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glDeleteLists(GLuint list, GLsizei range)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_013glDeleteListsEji', list, range,
    )

  @overload(int)
  def glCallList(self, list: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glCallList(GLuint list)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glCallList

    Parameters
    ----------

    list : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glCallList(GLuint list)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_2_010glCallListEj', list)

  def glEndList(self) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glEndList()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glEndList
    """
    #  void QOpenGLFunctions_2_0::glEndList()
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_2_09glEndListEv')

  @overload(int, int)
  def glNewList(self, list: int, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glNewList(GLuint list, GLenum
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glNewList

    Parameters
    ----------

    list : int
      Passed on as it is.

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glNewList(GLuint list, GLenum mode)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_09glNewListEjj', list, mode,
    )

  @overload(int)
  def glPushClientAttrib(self, mask: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glPushClientAttrib(GLbitfield
    mask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glPushClientAttrib

    Parameters
    ----------

    mask : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glPushClientAttrib(GLbitfield mask)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_018glPushClientAttribEj', mask,
    )

  def glPopClientAttrib(self) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glPopClientAttrib()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glPopClientAttrib
    """
    #  void QOpenGLFunctions_2_0::glPopClientAttrib()
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_017glPopClientAttribEv',
    )

  @overload(int)
  def glEnableClientState(self, array: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glEnableClientState(GLenum
    array)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glEnableClientState

    Parameters
    ----------

    array : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glEnableClientState(GLenum array)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_019glEnableClientStateEj', array,
    )

  @overload(int)
  def glDisableClientState(self, array: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glDisableClientState(GLenum
    array)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glDisableClientState

    Parameters
    ----------

    array : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glDisableClientState(GLenum array)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_020glDisableClientStateEj', array,
    )

  @overload(int)
  def glArrayElement(self, i: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glArrayElement(GLint i)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glArrayElement

    Parameters
    ----------

    i : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glArrayElement(GLint i)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_014glArrayElementEi', i,
    )

  @overload(int)
  def glResetMinmax(self, target: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glResetMinmax(GLenum target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glResetMinmax

    Parameters
    ----------

    target : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glResetMinmax(GLenum target)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_013glResetMinmaxEj', target,
    )

  @overload(int)
  def glResetHistogram(self, target: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glResetHistogram(GLenum target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glResetHistogram

    Parameters
    ----------

    target : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glResetHistogram(GLenum target)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_016glResetHistogramEj', target,
    )

  @overload(int, int, int)
  def glMinmax(self, target: int, internalformat: int, sink: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glMinmax(GLenum target, GLenum
    internalformat, GLboolean sink)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glMinmax

    Parameters
    ----------

    target : int
      Passed on as it is.

    internalformat : int
      Passed on as it is.

    sink : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glMinmax(GLenum target, GLenum
    #      internalformat, GLboolean sink)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_08glMinmaxEjjh',
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
    Calls Qt's 'void QOpenGLFunctions_2_0::glHistogram(GLenum target, GLsizei
    width, GLenum internalformat, GLboolean sink)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glHistogram

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
    #  void QOpenGLFunctions_2_0::glHistogram(GLenum target, GLsizei width,
    #      GLenum internalformat, GLboolean sink)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_011glHistogramEjijh',
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
    Calls Qt's 'void QOpenGLFunctions_2_0::glCopyConvolutionFilter2D(GLenum
    target, GLenum internalformat, GLint x, GLint y, GLsizei width, GLsizei
    height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html

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
    #  void QOpenGLFunctions_2_0::glCopyConvolutionFilter2D(GLenum target,
    #      GLenum internalformat, GLint x, GLint y, GLsizei width, GLsizei
    #      height)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_025glCopyConvolutionFilter2DEjjiiii',
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
    Calls Qt's 'void QOpenGLFunctions_2_0::glCopyConvolutionFilter1D(GLenum
    target, GLenum internalformat, GLint x, GLint y, GLsizei width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html

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
    #  void QOpenGLFunctions_2_0::glCopyConvolutionFilter1D(GLenum target,
    #      GLenum internalformat, GLint x, GLint y, GLsizei width)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_025glCopyConvolutionFilter1DEjjiii',
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
    Calls Qt's 'void QOpenGLFunctions_2_0::glConvolutionParameteri(GLenum
    target, GLenum pname, GLint params)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glConvolutionParameteri

    Parameters
    ----------

    target : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    params : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glConvolutionParameteri(GLenum target,
    #      GLenum pname, GLint params)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_023glConvolutionParameteriEjji',
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
    Calls Qt's 'void QOpenGLFunctions_2_0::glConvolutionParameterf(GLenum
    target, GLenum pname, GLfloat params)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glConvolutionParameterf

    Parameters
    ----------

    target : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    params : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glConvolutionParameterf(GLenum target,
    #      GLenum pname, GLfloat params)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_023glConvolutionParameterfEjjf',
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
    Calls Qt's 'void QOpenGLFunctions_2_0::glCopyColorSubTable(GLenum target,
    GLsizei start, GLint x, GLint y, GLsizei width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glCopyColorSubTable

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
    #  void QOpenGLFunctions_2_0::glCopyColorSubTable(GLenum target, GLsizei
    #      start, GLint x, GLint y, GLsizei width)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_019glCopyColorSubTableEjiiii',
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
    Calls Qt's 'void QOpenGLFunctions_2_0::glCopyColorTable(GLenum target,
    GLenum internalformat, GLint x, GLint y, GLsizei width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glCopyColorTable

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
    #  void QOpenGLFunctions_2_0::glCopyColorTable(GLenum target, GLenum
    #      internalformat, GLint x, GLint y, GLsizei width)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_016glCopyColorTableEjjiii',
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
    Calls Qt's 'void QOpenGLFunctions_2_0::glMultiTexCoord4s(GLenum target,
    GLshort s, GLshort t, GLshort r, GLshort q)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glMultiTexCoord4s

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
    #  void QOpenGLFunctions_2_0::glMultiTexCoord4s(GLenum target, GLshort s,
    #      GLshort t, GLshort r, GLshort q)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_017glMultiTexCoord4sEjssss',
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
    Calls Qt's 'void QOpenGLFunctions_2_0::glMultiTexCoord4i(GLenum target,
    GLint s, GLint t, GLint r, GLint q)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glMultiTexCoord4i

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
    #  void QOpenGLFunctions_2_0::glMultiTexCoord4i(GLenum target, GLint s,
    #      GLint t, GLint r, GLint q)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_017glMultiTexCoord4iEjiiii',
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
    Calls Qt's 'void QOpenGLFunctions_2_0::glMultiTexCoord4f(GLenum target,
    GLfloat s, GLfloat t, GLfloat r, GLfloat q)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glMultiTexCoord4f

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
    #  void QOpenGLFunctions_2_0::glMultiTexCoord4f(GLenum target, GLfloat s,
    #      GLfloat t, GLfloat r, GLfloat q)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_017glMultiTexCoord4fEjffff',
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
    Calls Qt's 'void QOpenGLFunctions_2_0::glMultiTexCoord4d(GLenum target,
    GLdouble s, GLdouble t, GLdouble r, GLdouble q)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glMultiTexCoord4d

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
    #  void QOpenGLFunctions_2_0::glMultiTexCoord4d(GLenum target, GLdouble
    #      s, GLdouble t, GLdouble r, GLdouble q)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_017glMultiTexCoord4dEjdddd',
        target, s, t, r, q,
    )

  @overload(int, int, int, int)
  def glMultiTexCoord3s(self, target: int, s: int, t: int, r: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glMultiTexCoord3s(GLenum target,
    GLshort s, GLshort t, GLshort r)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glMultiTexCoord3s

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
    #  void QOpenGLFunctions_2_0::glMultiTexCoord3s(GLenum target, GLshort s,
    #      GLshort t, GLshort r)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_017glMultiTexCoord3sEjsss',
        target, s, t, r,
    )

  @overload(int, int, int, int)
  def glMultiTexCoord3i(self, target: int, s: int, t: int, r: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glMultiTexCoord3i(GLenum target,
    GLint s, GLint t, GLint r)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glMultiTexCoord3i

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
    #  void QOpenGLFunctions_2_0::glMultiTexCoord3i(GLenum target, GLint s,
    #      GLint t, GLint r)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_017glMultiTexCoord3iEjiii',
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
    Calls Qt's 'void QOpenGLFunctions_2_0::glMultiTexCoord3f(GLenum target,
    GLfloat s, GLfloat t, GLfloat r)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glMultiTexCoord3f

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
    #  void QOpenGLFunctions_2_0::glMultiTexCoord3f(GLenum target, GLfloat s,
    #      GLfloat t, GLfloat r)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_017glMultiTexCoord3fEjfff',
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
    Calls Qt's 'void QOpenGLFunctions_2_0::glMultiTexCoord3d(GLenum target,
    GLdouble s, GLdouble t, GLdouble r)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glMultiTexCoord3d

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
    #  void QOpenGLFunctions_2_0::glMultiTexCoord3d(GLenum target, GLdouble
    #      s, GLdouble t, GLdouble r)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_017glMultiTexCoord3dEjddd',
        target, s, t, r,
    )

  @overload(int, int, int)
  def glMultiTexCoord2s(self, target: int, s: int, t: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glMultiTexCoord2s(GLenum target,
    GLshort s, GLshort t)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glMultiTexCoord2s

    Parameters
    ----------

    target : int
      Passed on as it is.

    s : int
      Passed on as it is.

    t : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glMultiTexCoord2s(GLenum target, GLshort s,
    #      GLshort t)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_017glMultiTexCoord2sEjss',
        target, s, t,
    )

  @overload(int, int, int)
  def glMultiTexCoord2i(self, target: int, s: int, t: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glMultiTexCoord2i(GLenum target,
    GLint s, GLint t)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glMultiTexCoord2i

    Parameters
    ----------

    target : int
      Passed on as it is.

    s : int
      Passed on as it is.

    t : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glMultiTexCoord2i(GLenum target, GLint s,
    #      GLint t)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_017glMultiTexCoord2iEjii',
        target, s, t,
    )

  @overload(int, float, float)
  def glMultiTexCoord2f(self, target: int, s: float, t: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glMultiTexCoord2f(GLenum target,
    GLfloat s, GLfloat t)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glMultiTexCoord2f

    Parameters
    ----------

    target : int
      Passed on as it is.

    s : float
      Passed on as it is.

    t : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glMultiTexCoord2f(GLenum target, GLfloat s,
    #      GLfloat t)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_017glMultiTexCoord2fEjff',
        target, s, t,
    )

  @overload(int, float, float)
  def glMultiTexCoord2d(self, target: int, s: float, t: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glMultiTexCoord2d(GLenum target,
    GLdouble s, GLdouble t)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glMultiTexCoord2d

    Parameters
    ----------

    target : int
      Passed on as it is.

    s : float
      Passed on as it is.

    t : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glMultiTexCoord2d(GLenum target, GLdouble
    #      s, GLdouble t)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_017glMultiTexCoord2dEjdd',
        target, s, t,
    )

  @overload(int, int)
  def glMultiTexCoord1s(self, target: int, s: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glMultiTexCoord1s(GLenum target,
    GLshort s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glMultiTexCoord1s

    Parameters
    ----------

    target : int
      Passed on as it is.

    s : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glMultiTexCoord1s(GLenum target, GLshort s)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_017glMultiTexCoord1sEjs', target, s,
    )

  @overload(int, int)
  def glMultiTexCoord1i(self, target: int, s: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glMultiTexCoord1i(GLenum target,
    GLint s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glMultiTexCoord1i

    Parameters
    ----------

    target : int
      Passed on as it is.

    s : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glMultiTexCoord1i(GLenum target, GLint s)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_017glMultiTexCoord1iEji', target, s,
    )

  @overload(int, float)
  def glMultiTexCoord1f(self, target: int, s: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glMultiTexCoord1f(GLenum target,
    GLfloat s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glMultiTexCoord1f

    Parameters
    ----------

    target : int
      Passed on as it is.

    s : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glMultiTexCoord1f(GLenum target, GLfloat s)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_017glMultiTexCoord1fEjf', target, s,
    )

  @overload(int, float)
  def glMultiTexCoord1d(self, target: int, s: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glMultiTexCoord1d(GLenum target,
    GLdouble s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glMultiTexCoord1d

    Parameters
    ----------

    target : int
      Passed on as it is.

    s : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glMultiTexCoord1d(GLenum target, GLdouble
    #      s)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_017glMultiTexCoord1dEjd', target, s,
    )

  @overload(int)
  def glClientActiveTexture(self, texture: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glClientActiveTexture(GLenum
    texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glClientActiveTexture

    Parameters
    ----------

    texture : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glClientActiveTexture(GLenum texture)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_021glClientActiveTextureEj', texture,
    )

  @overload(int, int, int)
  def glWindowPos3s(self, x: int, y: int, z: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glWindowPos3s(GLshort x, GLshort
    y, GLshort z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glWindowPos3s

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    z : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glWindowPos3s(GLshort x, GLshort y, GLshort
    #      z)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_013glWindowPos3sEsss', x, y, z,
    )

  @overload(int, int, int)
  def glWindowPos3i(self, x: int, y: int, z: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glWindowPos3i(GLint x, GLint y,
    GLint z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glWindowPos3i

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    z : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glWindowPos3i(GLint x, GLint y, GLint z)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_013glWindowPos3iEiii', x, y, z,
    )

  @overload(float, float, float)
  def glWindowPos3f(self, x: float, y: float, z: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glWindowPos3f(GLfloat x, GLfloat
    y, GLfloat z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glWindowPos3f

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glWindowPos3f(GLfloat x, GLfloat y, GLfloat
    #      z)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_013glWindowPos3fEfff', x, y, z,
    )

  @overload(float, float, float)
  def glWindowPos3d(self, x: float, y: float, z: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glWindowPos3d(GLdouble x, GLdouble
    y, GLdouble z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glWindowPos3d

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glWindowPos3d(GLdouble x, GLdouble y,
    #      GLdouble z)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_013glWindowPos3dEddd', x, y, z,
    )

  @overload(int, int)
  def glWindowPos2s(self, x: int, y: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glWindowPos2s(GLshort x, GLshort
    y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glWindowPos2s

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glWindowPos2s(GLshort x, GLshort y)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_013glWindowPos2sEss', x, y,
    )

  @overload(int, int)
  def glWindowPos2i(self, x: int, y: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glWindowPos2i(GLint x, GLint y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glWindowPos2i

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glWindowPos2i(GLint x, GLint y)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_013glWindowPos2iEii', x, y,
    )

  @overload(float, float)
  def glWindowPos2f(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glWindowPos2f(GLfloat x, GLfloat
    y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glWindowPos2f

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glWindowPos2f(GLfloat x, GLfloat y)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_013glWindowPos2fEff', x, y,
    )

  @overload(float, float)
  def glWindowPos2d(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glWindowPos2d(GLdouble x, GLdouble
    y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glWindowPos2d

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glWindowPos2d(GLdouble x, GLdouble y)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_013glWindowPos2dEdd', x, y,
    )

  @overload(int, int, int)
  def glSecondaryColor3us(self, red: int, green: int, blue: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glSecondaryColor3us(GLushort red,
    GLushort green, GLushort blue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glSecondaryColor3us

    Parameters
    ----------

    red : int
      Passed on as it is.

    green : int
      Passed on as it is.

    blue : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glSecondaryColor3us(GLushort red, GLushort
    #      green, GLushort blue)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_019glSecondaryColor3usEttt',
        red, green, blue,
    )

  @overload(int, int, int)
  def glSecondaryColor3ui(self, red: int, green: int, blue: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glSecondaryColor3ui(GLuint red,
    GLuint green, GLuint blue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glSecondaryColor3ui

    Parameters
    ----------

    red : int
      Passed on as it is.

    green : int
      Passed on as it is.

    blue : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glSecondaryColor3ui(GLuint red, GLuint
    #      green, GLuint blue)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_019glSecondaryColor3uiEjjj',
        red, green, blue,
    )

  @overload(int, int, int)
  def glSecondaryColor3ub(self, red: int, green: int, blue: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glSecondaryColor3ub(GLubyte red,
    GLubyte green, GLubyte blue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glSecondaryColor3ub

    Parameters
    ----------

    red : int
      Passed on as it is.

    green : int
      Passed on as it is.

    blue : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glSecondaryColor3ub(GLubyte red, GLubyte
    #      green, GLubyte blue)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_019glSecondaryColor3ubEhhh',
        red, green, blue,
    )

  @overload(int, int, int)
  def glSecondaryColor3s(self, red: int, green: int, blue: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glSecondaryColor3s(GLshort red,
    GLshort green, GLshort blue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glSecondaryColor3s

    Parameters
    ----------

    red : int
      Passed on as it is.

    green : int
      Passed on as it is.

    blue : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glSecondaryColor3s(GLshort red, GLshort
    #      green, GLshort blue)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_018glSecondaryColor3sEsss',
        red, green, blue,
    )

  @overload(int, int, int)
  def glSecondaryColor3i(self, red: int, green: int, blue: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glSecondaryColor3i(GLint red,
    GLint green, GLint blue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glSecondaryColor3i

    Parameters
    ----------

    red : int
      Passed on as it is.

    green : int
      Passed on as it is.

    blue : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glSecondaryColor3i(GLint red, GLint green,
    #      GLint blue)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_018glSecondaryColor3iEiii',
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
    Calls Qt's 'void QOpenGLFunctions_2_0::glSecondaryColor3f(GLfloat red,
    GLfloat green, GLfloat blue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glSecondaryColor3f

    Parameters
    ----------

    red : float
      Passed on as it is.

    green : float
      Passed on as it is.

    blue : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glSecondaryColor3f(GLfloat red, GLfloat
    #      green, GLfloat blue)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_018glSecondaryColor3fEfff',
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
    Calls Qt's 'void QOpenGLFunctions_2_0::glSecondaryColor3d(GLdouble red,
    GLdouble green, GLdouble blue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glSecondaryColor3d

    Parameters
    ----------

    red : float
      Passed on as it is.

    green : float
      Passed on as it is.

    blue : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glSecondaryColor3d(GLdouble red, GLdouble
    #      green, GLdouble blue)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_018glSecondaryColor3dEddd',
        red, green, blue,
    )

  @overload(int, int, int)
  def glSecondaryColor3b(self, red: int, green: int, blue: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glSecondaryColor3b(GLbyte red,
    GLbyte green, GLbyte blue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glSecondaryColor3b

    Parameters
    ----------

    red : int
      Passed on as it is.

    green : int
      Passed on as it is.

    blue : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glSecondaryColor3b(GLbyte red, GLbyte
    #      green, GLbyte blue)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_018glSecondaryColor3bEaaa',
        red, green, blue,
    )

  @overload(float)
  def glFogCoordd(self, coord: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glFogCoordd(GLdouble coord)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glFogCoordd

    Parameters
    ----------

    coord : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glFogCoordd(GLdouble coord)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_011glFogCoorddEd', coord,
    )

  @overload(float)
  def glFogCoordf(self, coord: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glFogCoordf(GLfloat coord)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glFogCoordf

    Parameters
    ----------

    coord : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glFogCoordf(GLfloat coord)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_011glFogCoordfEf', coord,
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
    Calls Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib4s(GLuint index,
    GLshort x, GLshort y, GLshort z, GLshort w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glVertexAttrib4s

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
    #  void QOpenGLFunctions_2_0::glVertexAttrib4s(GLuint index, GLshort x,
    #      GLshort y, GLshort z, GLshort w)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_016glVertexAttrib4sEjssss',
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
    Calls Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib4f(GLuint index,
    GLfloat x, GLfloat y, GLfloat z, GLfloat w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glVertexAttrib4f

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
    #  void QOpenGLFunctions_2_0::glVertexAttrib4f(GLuint index, GLfloat x,
    #      GLfloat y, GLfloat z, GLfloat w)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_016glVertexAttrib4fEjffff',
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
    Calls Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib4d(GLuint index,
    GLdouble x, GLdouble y, GLdouble z, GLdouble w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glVertexAttrib4d

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
    #  void QOpenGLFunctions_2_0::glVertexAttrib4d(GLuint index, GLdouble x,
    #      GLdouble y, GLdouble z, GLdouble w)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_016glVertexAttrib4dEjdddd',
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
    Calls Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib4Nub(GLuint index,
    GLubyte x, GLubyte y, GLubyte z, GLubyte w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glVertexAttrib4Nub

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
    #  void QOpenGLFunctions_2_0::glVertexAttrib4Nub(GLuint index, GLubyte x,
    #      GLubyte y, GLubyte z, GLubyte w)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_018glVertexAttrib4NubEjhhhh',
        index, x, y, z, w,
    )

  @overload(int, int, int, int)
  def glVertexAttrib3s(self, index: int, x: int, y: int, z: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib3s(GLuint index,
    GLshort x, GLshort y, GLshort z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glVertexAttrib3s

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
    #  void QOpenGLFunctions_2_0::glVertexAttrib3s(GLuint index, GLshort x,
    #      GLshort y, GLshort z)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_016glVertexAttrib3sEjsss',
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
    Calls Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib3f(GLuint index,
    GLfloat x, GLfloat y, GLfloat z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glVertexAttrib3f

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
    #  void QOpenGLFunctions_2_0::glVertexAttrib3f(GLuint index, GLfloat x,
    #      GLfloat y, GLfloat z)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_016glVertexAttrib3fEjfff',
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
    Calls Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib3d(GLuint index,
    GLdouble x, GLdouble y, GLdouble z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glVertexAttrib3d

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
    #  void QOpenGLFunctions_2_0::glVertexAttrib3d(GLuint index, GLdouble x,
    #      GLdouble y, GLdouble z)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_016glVertexAttrib3dEjddd',
        index, x, y, z,
    )

  @overload(int, int, int)
  def glVertexAttrib2s(self, index: int, x: int, y: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib2s(GLuint index,
    GLshort x, GLshort y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glVertexAttrib2s

    Parameters
    ----------

    index : int
      Passed on as it is.

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glVertexAttrib2s(GLuint index, GLshort x,
    #      GLshort y)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_016glVertexAttrib2sEjss', index, x, y,
    )

  @overload(int, float, float)
  def glVertexAttrib2f(self, index: int, x: float, y: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib2f(GLuint index,
    GLfloat x, GLfloat y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glVertexAttrib2f

    Parameters
    ----------

    index : int
      Passed on as it is.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glVertexAttrib2f(GLuint index, GLfloat x,
    #      GLfloat y)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_016glVertexAttrib2fEjff', index, x, y,
    )

  @overload(int, float, float)
  def glVertexAttrib2d(self, index: int, x: float, y: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib2d(GLuint index,
    GLdouble x, GLdouble y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glVertexAttrib2d

    Parameters
    ----------

    index : int
      Passed on as it is.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glVertexAttrib2d(GLuint index, GLdouble x,
    #      GLdouble y)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_016glVertexAttrib2dEjdd', index, x, y,
    )

  @overload(int, int)
  def glVertexAttrib1s(self, index: int, x: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib1s(GLuint index,
    GLshort x)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glVertexAttrib1s

    Parameters
    ----------

    index : int
      Passed on as it is.

    x : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glVertexAttrib1s(GLuint index, GLshort x)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_016glVertexAttrib1sEjs', index, x,
    )

  @overload(int, float)
  def glVertexAttrib1f(self, index: int, x: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib1f(GLuint index,
    GLfloat x)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glVertexAttrib1f

    Parameters
    ----------

    index : int
      Passed on as it is.

    x : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glVertexAttrib1f(GLuint index, GLfloat x)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_016glVertexAttrib1fEjf', index, x,
    )

  @overload(int, float)
  def glVertexAttrib1d(self, index: int, x: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib1d(GLuint index,
    GLdouble x)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_2_0.html#glVertexAttrib1d

    Parameters
    ----------

    index : int
      Passed on as it is.

    x : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_2_0::glVertexAttrib1d(GLuint index, GLdouble x)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_2_016glVertexAttrib1dEjd', index, x,
    )

  @staticmethod
  def glAreTexturesResident(*__, **_) -> Never:
    """
    Qt's 'GLboolean QOpenGLFunctions_2_0::glAreTexturesResident(GLsizei n,
    const GLuint *textures, GLboolean *residences)': names 'GLuint', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glAreTexturesResident' has no cute function "
        "yet. Qt's 'GLboolean "
        "QOpenGLFunctions_2_0::glAreTexturesResident(GLsizei n, const "
        "GLuint *textures, GLboolean *residences)': names 'GLuint', which "
        "has no cute class yet.")

  @staticmethod
  def glBindAttribLocation(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glBindAttribLocation(GLuint program,
    GLuint index, const GLchar *name)': names 'GLchar', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glBindAttribLocation' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_2_0::glBindAttribLocation(GLuint "
        "program, GLuint index, const GLchar *name)': names 'GLchar', which "
        "has no cute class yet.")

  @staticmethod
  def glBitmap(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glBitmap(GLsizei width, GLsizei height,
    GLfloat xorig, GLfloat yorig, GLfloat xmove, GLfloat ymove, const GLubyte
    *bitmap)': names 'GLubyte', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glBitmap' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glBitmap(GLsizei width, GLsizei "
        "height, GLfloat xorig, GLfloat yorig, GLfloat xmove, GLfloat "
        "ymove, const GLubyte *bitmap)': names 'GLubyte', which has no cute "
        "class yet.")

  @staticmethod
  def glBufferData(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glBufferData(GLenum target, GLsizeiptr
    size, const GLvoid *data, GLenum usage)': names 'GLvoid', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glBufferData' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glBufferData(GLenum target, GLsizeiptr "
        "size, const GLvoid *data, GLenum usage)': names 'GLvoid', which "
        "has no cute class yet.")

  @staticmethod
  def glBufferSubData(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glBufferSubData(GLenum target, GLintptr
    offset, GLsizeiptr size, const GLvoid *data)': names 'GLvoid', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glBufferSubData' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glBufferSubData(GLenum target, "
        "GLintptr offset, GLsizeiptr size, const GLvoid *data)': names "
        "'GLvoid', which has no cute class yet.")

  @staticmethod
  def glCallLists(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glCallLists(GLsizei n, GLenum type,
    const GLvoid *lists)': names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glCallLists' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glCallLists(GLsizei n, GLenum type, "
        "const GLvoid *lists)': names 'GLvoid', which has no cute class yet."
    )

  @staticmethod
  def glClipPlane(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glClipPlane(GLenum plane, const GLdouble
    *equation)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glClipPlane' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glClipPlane(GLenum plane, const "
        "GLdouble *equation)': names 'GLdouble', which has no cute class "
        "yet.")

  @staticmethod
  def glColor3bv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glColor3bv(const GLbyte *v)': names
    'GLbyte', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glColor3bv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glColor3bv(const GLbyte *v)': names "
        "'GLbyte', which has no cute class yet.")

  @staticmethod
  def glColor3dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glColor3dv(const GLdouble *v)': names
    'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glColor3dv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glColor3dv(const GLdouble *v)': names "
        "'GLdouble', which has no cute class yet.")

  @staticmethod
  def glColor3fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glColor3fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glColor3fv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glColor3fv(const GLfloat *v)': names "
        "'GLfloat', which has no cute class yet.")

  @staticmethod
  def glColor3iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glColor3iv(const GLint *v)': names
    'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glColor3iv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glColor3iv(const GLint *v)': names "
        "'GLint', which has no cute class yet.")

  @staticmethod
  def glColor3sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glColor3sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glColor3sv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glColor3sv(const GLshort *v)': names "
        "'GLshort', which has no cute class yet.")

  @staticmethod
  def glColor3ubv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glColor3ubv(const GLubyte *v)': names
    'GLubyte', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glColor3ubv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glColor3ubv(const GLubyte *v)': names "
        "'GLubyte', which has no cute class yet.")

  @staticmethod
  def glColor3uiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glColor3uiv(const GLuint *v)': names
    'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glColor3uiv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glColor3uiv(const GLuint *v)': names "
        "'GLuint', which has no cute class yet.")

  @staticmethod
  def glColor3usv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glColor3usv(const GLushort *v)': names
    'GLushort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glColor3usv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glColor3usv(const GLushort *v)': names "
        "'GLushort', which has no cute class yet.")

  @staticmethod
  def glColor4bv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glColor4bv(const GLbyte *v)': names
    'GLbyte', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glColor4bv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glColor4bv(const GLbyte *v)': names "
        "'GLbyte', which has no cute class yet.")

  @staticmethod
  def glColor4dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glColor4dv(const GLdouble *v)': names
    'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glColor4dv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glColor4dv(const GLdouble *v)': names "
        "'GLdouble', which has no cute class yet.")

  @staticmethod
  def glColor4fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glColor4fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glColor4fv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glColor4fv(const GLfloat *v)': names "
        "'GLfloat', which has no cute class yet.")

  @staticmethod
  def glColor4iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glColor4iv(const GLint *v)': names
    'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glColor4iv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glColor4iv(const GLint *v)': names "
        "'GLint', which has no cute class yet.")

  @staticmethod
  def glColor4sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glColor4sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glColor4sv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glColor4sv(const GLshort *v)': names "
        "'GLshort', which has no cute class yet.")

  @staticmethod
  def glColor4ubv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glColor4ubv(const GLubyte *v)': names
    'GLubyte', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glColor4ubv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glColor4ubv(const GLubyte *v)': names "
        "'GLubyte', which has no cute class yet.")

  @staticmethod
  def glColor4uiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glColor4uiv(const GLuint *v)': names
    'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glColor4uiv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glColor4uiv(const GLuint *v)': names "
        "'GLuint', which has no cute class yet.")

  @staticmethod
  def glColor4usv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glColor4usv(const GLushort *v)': names
    'GLushort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glColor4usv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glColor4usv(const GLushort *v)': names "
        "'GLushort', which has no cute class yet.")

  @staticmethod
  def glColorPointer(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glColorPointer(GLint size, GLenum type,
    GLsizei stride, const GLvoid *pointer)': names 'GLvoid', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glColorPointer' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glColorPointer(GLint size, GLenum "
        "type, GLsizei stride, const GLvoid *pointer)': names 'GLvoid', "
        "which has no cute class yet.")

  @staticmethod
  def glColorSubTable(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glColorSubTable(GLenum target, GLsizei
    start, GLsizei count, GLenum format, GLenum type, const GLvoid *data)':
    names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glColorSubTable' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glColorSubTable(GLenum target, "
        "GLsizei start, GLsizei count, GLenum format, GLenum type, const "
        "GLvoid *data)': names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glColorTable(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glColorTable(GLenum target, GLenum
    internalformat, GLsizei width, GLenum format, GLenum type, const GLvoid
    *table)': names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glColorTable' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glColorTable(GLenum target, GLenum "
        "internalformat, GLsizei width, GLenum format, GLenum type, const "
        "GLvoid *table)': names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glColorTableParameterfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glColorTableParameterfv(GLenum target,
    GLenum pname, const GLfloat *params)': names 'GLfloat', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glColorTableParameterfv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_2_0::glColorTableParameterfv(GLenum target, "
        "GLenum pname, const GLfloat *params)': names 'GLfloat', which has "
        "no cute class yet.")

  @staticmethod
  def glColorTableParameteriv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glColorTableParameteriv(GLenum target,
    GLenum pname, const GLint *params)': names 'GLint', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glColorTableParameteriv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_2_0::glColorTableParameteriv(GLenum target, "
        "GLenum pname, const GLint *params)': names 'GLint', which has no "
        "cute class yet.")

  @staticmethod
  def glCompressedTexImage1D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glCompressedTexImage1D(GLenum target,
    GLint level, GLenum internalformat, GLsizei width, GLint border, GLsizei
    imageSize, const GLvoid *data)': names 'GLvoid', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glCompressedTexImage1D' has no cute function "
        "yet. Qt's 'void "
        "QOpenGLFunctions_2_0::glCompressedTexImage1D(GLenum target, GLint "
        "level, GLenum internalformat, GLsizei width, GLint border, GLsizei "
        "imageSize, const GLvoid *data)': names 'GLvoid', which has no cute "
        "class yet.")

  @staticmethod
  def glCompressedTexImage2D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glCompressedTexImage2D(GLenum target,
    GLint level, GLenum internalformat, GLsizei width, GLsizei height, GLint
    border, GLsizei imageSize, const GLvoid *data)': names 'GLvoid', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glCompressedTexImage2D' has no cute function "
        "yet. Qt's 'void "
        "QOpenGLFunctions_2_0::glCompressedTexImage2D(GLenum target, GLint "
        "level, GLenum internalformat, GLsizei width, GLsizei height, GLint "
        "border, GLsizei imageSize, const GLvoid *data)': names 'GLvoid', "
        "which has no cute class yet.")

  @staticmethod
  def glCompressedTexImage3D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glCompressedTexImage3D(GLenum target,
    GLint level, GLenum internalformat, GLsizei width, GLsizei height,
    GLsizei depth, GLint border, GLsizei imageSize, const GLvoid *data)':
    names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glCompressedTexImage3D' has no cute function "
        "yet. Qt's 'void "
        "QOpenGLFunctions_2_0::glCompressedTexImage3D(GLenum target, GLint "
        "level, GLenum internalformat, GLsizei width, GLsizei height, "
        "GLsizei depth, GLint border, GLsizei imageSize, const GLvoid "
        "*data)': names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glCompressedTexSubImage1D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glCompressedTexSubImage1D(GLenum target,
    GLint level, GLint xoffset, GLsizei width, GLenum format, GLsizei
    imageSize, const GLvoid *data)': names 'GLvoid', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glCompressedTexSubImage1D' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_2_0::glCompressedTexSubImage1D(GLenum target, "
        "GLint level, GLint xoffset, GLsizei width, GLenum format, GLsizei "
        "imageSize, const GLvoid *data)': names 'GLvoid', which has no cute "
        "class yet.")

  @staticmethod
  def glCompressedTexSubImage2D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glCompressedTexSubImage2D(GLenum target,
    GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height,
    GLenum format, GLsizei imageSize, const GLvoid *data)': names 'GLvoid',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glCompressedTexSubImage2D' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_2_0::glCompressedTexSubImage2D(GLenum target, "
        "GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei "
        "height, GLenum format, GLsizei imageSize, const GLvoid *data)': "
        "names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glCompressedTexSubImage3D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glCompressedTexSubImage3D(GLenum target,
    GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width,
    GLsizei height, GLsizei depth, GLenum format, GLsizei imageSize, const
    GLvoid *data)': names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glCompressedTexSubImage3D' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_2_0::glCompressedTexSubImage3D(GLenum target, "
        "GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei "
        "width, GLsizei height, GLsizei depth, GLenum format, GLsizei "
        "imageSize, const GLvoid *data)': names 'GLvoid', which has no cute "
        "class yet.")

  @staticmethod
  def glConvolutionFilter1D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glConvolutionFilter1D(GLenum target,
    GLenum internalformat, GLsizei width, GLenum format, GLenum type, const
    GLvoid *image)': names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glConvolutionFilter1D' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_2_0::glConvolutionFilter1D(GLenum "
        "target, GLenum internalformat, GLsizei width, GLenum format, "
        "GLenum type, const GLvoid *image)': names 'GLvoid', which has no "
        "cute class yet.")

  @staticmethod
  def glConvolutionFilter2D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glConvolutionFilter2D(GLenum target,
    GLenum internalformat, GLsizei width, GLsizei height, GLenum format,
    GLenum type, const GLvoid *image)': names 'GLvoid', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glConvolutionFilter2D' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_2_0::glConvolutionFilter2D(GLenum "
        "target, GLenum internalformat, GLsizei width, GLsizei height, "
        "GLenum format, GLenum type, const GLvoid *image)': names 'GLvoid', "
        "which has no cute class yet.")

  @staticmethod
  def glConvolutionParameterfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glConvolutionParameterfv(GLenum target,
    GLenum pname, const GLfloat *params)': names 'GLfloat', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glConvolutionParameterfv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_2_0::glConvolutionParameterfv(GLenum target, "
        "GLenum pname, const GLfloat *params)': names 'GLfloat', which has "
        "no cute class yet.")

  @staticmethod
  def glConvolutionParameteriv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glConvolutionParameteriv(GLenum target,
    GLenum pname, const GLint *params)': names 'GLint', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glConvolutionParameteriv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_2_0::glConvolutionParameteriv(GLenum target, "
        "GLenum pname, const GLint *params)': names 'GLint', which has no "
        "cute class yet.")

  @staticmethod
  def glDeleteBuffers(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glDeleteBuffers(GLsizei n, const GLuint
    *buffers)': names 'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glDeleteBuffers' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glDeleteBuffers(GLsizei n, const "
        "GLuint *buffers)': names 'GLuint', which has no cute class yet.")

  @staticmethod
  def glDeleteQueries(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glDeleteQueries(GLsizei n, const GLuint
    *ids)': names 'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glDeleteQueries' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glDeleteQueries(GLsizei n, const "
        "GLuint *ids)': names 'GLuint', which has no cute class yet.")

  @staticmethod
  def glDeleteTextures(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glDeleteTextures(GLsizei n, const GLuint
    *textures)': names 'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glDeleteTextures' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glDeleteTextures(GLsizei n, const "
        "GLuint *textures)': names 'GLuint', which has no cute class yet.")

  @staticmethod
  def glDrawBuffers(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glDrawBuffers(GLsizei n, const GLenum
    *bufs)': names 'GLenum', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glDrawBuffers' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glDrawBuffers(GLsizei n, const "
        "GLenum *bufs)': names 'GLenum', which has no cute class yet.")

  @staticmethod
  def glDrawElements(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glDrawElements(GLenum mode, GLsizei
    count, GLenum type, const GLvoid *indices)': names 'GLvoid', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glDrawElements' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glDrawElements(GLenum mode, "
        "GLsizei count, GLenum type, const GLvoid *indices)': names "
        "'GLvoid', which has no cute class yet.")

  @staticmethod
  def glDrawPixels(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glDrawPixels(GLsizei width, GLsizei
    height, GLenum format, GLenum type, const GLvoid *pixels)': names
    'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glDrawPixels' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glDrawPixels(GLsizei width, GLsizei "
        "height, GLenum format, GLenum type, const GLvoid *pixels)': names "
        "'GLvoid', which has no cute class yet.")

  @staticmethod
  def glDrawRangeElements(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glDrawRangeElements(GLenum mode, GLuint
    start, GLuint end, GLsizei count, GLenum type, const GLvoid *indices)':
    names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glDrawRangeElements' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_2_0::glDrawRangeElements(GLenum "
        "mode, GLuint start, GLuint end, GLsizei count, GLenum type, const "
        "GLvoid *indices)': names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glEdgeFlagPointer(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glEdgeFlagPointer(GLsizei stride, const
    GLvoid *pointer)': names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glEdgeFlagPointer' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glEdgeFlagPointer(GLsizei stride, "
        "const GLvoid *pointer)': names 'GLvoid', which has no cute class "
        "yet.")

  @staticmethod
  def glEdgeFlagv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glEdgeFlagv(const GLboolean *flag)':
    names 'GLboolean', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glEdgeFlagv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glEdgeFlagv(const GLboolean *flag)': "
        "names 'GLboolean', which has no cute class yet.")

  @staticmethod
  def glEvalCoord1dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glEvalCoord1dv(const GLdouble *u)':
    names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glEvalCoord1dv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glEvalCoord1dv(const GLdouble "
        "*u)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glEvalCoord1fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glEvalCoord1fv(const GLfloat *u)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glEvalCoord1fv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glEvalCoord1fv(const GLfloat "
        "*u)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glEvalCoord2dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glEvalCoord2dv(const GLdouble *u)':
    names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glEvalCoord2dv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glEvalCoord2dv(const GLdouble "
        "*u)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glEvalCoord2fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glEvalCoord2fv(const GLfloat *u)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glEvalCoord2fv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glEvalCoord2fv(const GLfloat "
        "*u)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glFeedbackBuffer(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glFeedbackBuffer(GLsizei size, GLenum
    type, GLfloat *buffer)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glFeedbackBuffer' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glFeedbackBuffer(GLsizei size, "
        "GLenum type, GLfloat *buffer)': takes a number to change where it "
        "is.")

  @staticmethod
  def glFogCoordPointer(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glFogCoordPointer(GLenum type, GLsizei
    stride, const GLvoid *pointer)': names 'GLvoid', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glFogCoordPointer' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glFogCoordPointer(GLenum type, "
        "GLsizei stride, const GLvoid *pointer)': names 'GLvoid', which has "
        "no cute class yet.")

  @staticmethod
  def glFogCoorddv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glFogCoorddv(const GLdouble *coord)':
    names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glFogCoorddv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glFogCoorddv(const GLdouble *coord)': "
        "names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glFogCoordfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glFogCoordfv(const GLfloat *coord)':
    names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glFogCoordfv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glFogCoordfv(const GLfloat *coord)': "
        "names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glFogfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glFogfv(GLenum pname, const GLfloat
    *params)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glFogfv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glFogfv(GLenum pname, const GLfloat "
        "*params)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glFogiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glFogiv(GLenum pname, const GLint
    *params)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glFogiv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glFogiv(GLenum pname, const GLint "
        "*params)': names 'GLint', which has no cute class yet.")

  @staticmethod
  def glGenBuffers(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glGenBuffers(GLsizei n, GLuint
    *buffers)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glGenBuffers' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glGenBuffers(GLsizei n, GLuint "
        "*buffers)': takes a number to change where it is.")

  @staticmethod
  def glGenQueries(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glGenQueries(GLsizei n, GLuint *ids)':
    takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glGenQueries' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glGenQueries(GLsizei n, GLuint *ids)': "
        "takes a number to change where it is.")

  @staticmethod
  def glGenTextures(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glGenTextures(GLsizei n, GLuint
    *textures)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glGenTextures' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glGenTextures(GLsizei n, GLuint "
        "*textures)': takes a number to change where it is.")

  @staticmethod
  def glGetActiveAttrib(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glGetActiveAttrib(GLuint program, GLuint
    index, GLsizei bufSize, GLsizei *length, GLint *size, GLenum *type,
    GLchar *name)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glGetActiveAttrib' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glGetActiveAttrib(GLuint program, "
        "GLuint index, GLsizei bufSize, GLsizei *length, GLint *size, "
        "GLenum *type, GLchar *name)': takes a number to change where it is."
    )

  @staticmethod
  def glGetActiveUniform(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glGetActiveUniform(GLuint program,
    GLuint index, GLsizei bufSize, GLsizei *length, GLint *size, GLenum
    *type, GLchar *name)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glGetActiveUniform' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_2_0::glGetActiveUniform(GLuint "
        "program, GLuint index, GLsizei bufSize, GLsizei *length, GLint "
        "*size, GLenum *type, GLchar *name)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetAttachedShaders(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glGetAttachedShaders(GLuint program,
    GLsizei maxCount, GLsizei *count, GLuint *obj)': takes a number to change
    where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glGetAttachedShaders' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_2_0::glGetAttachedShaders(GLuint "
        "program, GLsizei maxCount, GLsizei *count, GLuint *obj)': takes a "
        "number to change where it is.")

  @staticmethod
  def glGetAttribLocation(*__, **_) -> Never:
    """
    Qt's 'GLint QOpenGLFunctions_2_0::glGetAttribLocation(GLuint program,
    const GLchar *name)': names 'GLchar', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glGetAttribLocation' has no cute function "
        "yet. Qt's 'GLint QOpenGLFunctions_2_0::glGetAttribLocation(GLuint "
        "program, const GLchar *name)': names 'GLchar', which has no cute "
        "class yet.")

  @staticmethod
  def glGetBooleanv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glGetBooleanv(GLenum pname, GLboolean
    *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glGetBooleanv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glGetBooleanv(GLenum pname, "
        "GLboolean *params)': takes a number to change where it is.")

  @staticmethod
  def glGetBufferParameteriv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glGetBufferParameteriv(GLenum target,
    GLenum pname, GLint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glGetBufferParameteriv' has no cute function "
        "yet. Qt's 'void "
        "QOpenGLFunctions_2_0::glGetBufferParameteriv(GLenum target, GLenum "
        "pname, GLint *params)': takes a number to change where it is.")

  @staticmethod
  def glGetBufferPointerv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glGetBufferPointerv(GLenum target,
    GLenum pname, GLvoid **params)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glGetBufferPointerv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_2_0::glGetBufferPointerv(GLenum "
        "target, GLenum pname, GLvoid **params)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def glGetBufferSubData(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glGetBufferSubData(GLenum target,
    GLintptr offset, GLsizeiptr size, GLvoid *data)': names 'GLvoid', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glGetBufferSubData' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_2_0::glGetBufferSubData(GLenum "
        "target, GLintptr offset, GLsizeiptr size, GLvoid *data)': names "
        "'GLvoid', which has no cute class yet.")

  @staticmethod
  def glGetClipPlane(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glGetClipPlane(GLenum plane, GLdouble
    *equation)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glGetClipPlane' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glGetClipPlane(GLenum plane, "
        "GLdouble *equation)': takes a number to change where it is.")

  @staticmethod
  def glGetColorTable(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glGetColorTable(GLenum target, GLenum
    format, GLenum type, GLvoid *table)': names 'GLvoid', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glGetColorTable' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glGetColorTable(GLenum target, "
        "GLenum format, GLenum type, GLvoid *table)': names 'GLvoid', which "
        "has no cute class yet.")

  @staticmethod
  def glGetColorTableParameterfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glGetColorTableParameterfv(GLenum
    target, GLenum pname, GLfloat *params)': takes a number to change where
    it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glGetColorTableParameterfv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_2_0::glGetColorTableParameterfv(GLenum target, "
        "GLenum pname, GLfloat *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetColorTableParameteriv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glGetColorTableParameteriv(GLenum
    target, GLenum pname, GLint *params)': takes a number to change where it
    is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glGetColorTableParameteriv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_2_0::glGetColorTableParameteriv(GLenum target, "
        "GLenum pname, GLint *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetCompressedTexImage(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glGetCompressedTexImage(GLenum target,
    GLint level, GLvoid *img)': names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glGetCompressedTexImage' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_2_0::glGetCompressedTexImage(GLenum target, GLint "
        "level, GLvoid *img)': names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glGetConvolutionFilter(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glGetConvolutionFilter(GLenum target,
    GLenum format, GLenum type, GLvoid *image)': names 'GLvoid', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glGetConvolutionFilter' has no cute function "
        "yet. Qt's 'void "
        "QOpenGLFunctions_2_0::glGetConvolutionFilter(GLenum target, GLenum "
        "format, GLenum type, GLvoid *image)': names 'GLvoid', which has no "
        "cute class yet.")

  @staticmethod
  def glGetConvolutionParameterfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glGetConvolutionParameterfv(GLenum
    target, GLenum pname, GLfloat *params)': takes a number to change where
    it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glGetConvolutionParameterfv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_2_0::glGetConvolutionParameterfv(GLenum target, "
        "GLenum pname, GLfloat *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetConvolutionParameteriv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glGetConvolutionParameteriv(GLenum
    target, GLenum pname, GLint *params)': takes a number to change where it
    is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glGetConvolutionParameteriv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_2_0::glGetConvolutionParameteriv(GLenum target, "
        "GLenum pname, GLint *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetDoublev(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glGetDoublev(GLenum pname, GLdouble
    *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glGetDoublev' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glGetDoublev(GLenum pname, GLdouble "
        "*params)': takes a number to change where it is.")

  @staticmethod
  def glGetFloatv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glGetFloatv(GLenum pname, GLfloat
    *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glGetFloatv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glGetFloatv(GLenum pname, GLfloat "
        "*params)': takes a number to change where it is.")

  @staticmethod
  def glGetHistogram(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glGetHistogram(GLenum target, GLboolean
    reset, GLenum format, GLenum type, GLvoid *values)': names 'GLvoid',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glGetHistogram' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glGetHistogram(GLenum target, "
        "GLboolean reset, GLenum format, GLenum type, GLvoid *values)': "
        "names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glGetHistogramParameterfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glGetHistogramParameterfv(GLenum target,
    GLenum pname, GLfloat *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glGetHistogramParameterfv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_2_0::glGetHistogramParameterfv(GLenum target, "
        "GLenum pname, GLfloat *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetHistogramParameteriv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glGetHistogramParameteriv(GLenum target,
    GLenum pname, GLint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glGetHistogramParameteriv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_2_0::glGetHistogramParameteriv(GLenum target, "
        "GLenum pname, GLint *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetIntegerv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glGetIntegerv(GLenum pname, GLint
    *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glGetIntegerv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glGetIntegerv(GLenum pname, GLint "
        "*params)': takes a number to change where it is.")

  @staticmethod
  def glGetLightfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glGetLightfv(GLenum light, GLenum pname,
    GLfloat *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glGetLightfv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glGetLightfv(GLenum light, GLenum "
        "pname, GLfloat *params)': takes a number to change where it is.")

  @staticmethod
  def glGetLightiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glGetLightiv(GLenum light, GLenum pname,
    GLint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glGetLightiv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glGetLightiv(GLenum light, GLenum "
        "pname, GLint *params)': takes a number to change where it is.")

  @staticmethod
  def glGetMapdv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glGetMapdv(GLenum target, GLenum query,
    GLdouble *v)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glGetMapdv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glGetMapdv(GLenum target, GLenum "
        "query, GLdouble *v)': takes a number to change where it is.")

  @staticmethod
  def glGetMapfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glGetMapfv(GLenum target, GLenum query,
    GLfloat *v)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glGetMapfv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glGetMapfv(GLenum target, GLenum "
        "query, GLfloat *v)': takes a number to change where it is.")

  @staticmethod
  def glGetMapiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glGetMapiv(GLenum target, GLenum query,
    GLint *v)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glGetMapiv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glGetMapiv(GLenum target, GLenum "
        "query, GLint *v)': takes a number to change where it is.")

  @staticmethod
  def glGetMaterialfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glGetMaterialfv(GLenum face, GLenum
    pname, GLfloat *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glGetMaterialfv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glGetMaterialfv(GLenum face, "
        "GLenum pname, GLfloat *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetMaterialiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glGetMaterialiv(GLenum face, GLenum
    pname, GLint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glGetMaterialiv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glGetMaterialiv(GLenum face, "
        "GLenum pname, GLint *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetMinmax(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glGetMinmax(GLenum target, GLboolean
    reset, GLenum format, GLenum type, GLvoid *values)': names 'GLvoid',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glGetMinmax' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glGetMinmax(GLenum target, GLboolean "
        "reset, GLenum format, GLenum type, GLvoid *values)': names "
        "'GLvoid', which has no cute class yet.")

  @staticmethod
  def glGetMinmaxParameterfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glGetMinmaxParameterfv(GLenum target,
    GLenum pname, GLfloat *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glGetMinmaxParameterfv' has no cute function "
        "yet. Qt's 'void "
        "QOpenGLFunctions_2_0::glGetMinmaxParameterfv(GLenum target, GLenum "
        "pname, GLfloat *params)': takes a number to change where it is.")

  @staticmethod
  def glGetMinmaxParameteriv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glGetMinmaxParameteriv(GLenum target,
    GLenum pname, GLint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glGetMinmaxParameteriv' has no cute function "
        "yet. Qt's 'void "
        "QOpenGLFunctions_2_0::glGetMinmaxParameteriv(GLenum target, GLenum "
        "pname, GLint *params)': takes a number to change where it is.")

  @staticmethod
  def glGetPixelMapfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glGetPixelMapfv(GLenum map, GLfloat
    *values)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glGetPixelMapfv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glGetPixelMapfv(GLenum map, "
        "GLfloat *values)': takes a number to change where it is.")

  @staticmethod
  def glGetPixelMapuiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glGetPixelMapuiv(GLenum map, GLuint
    *values)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glGetPixelMapuiv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glGetPixelMapuiv(GLenum map, "
        "GLuint *values)': takes a number to change where it is.")

  @staticmethod
  def glGetPixelMapusv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glGetPixelMapusv(GLenum map, GLushort
    *values)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glGetPixelMapusv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glGetPixelMapusv(GLenum map, "
        "GLushort *values)': takes a number to change where it is.")

  @staticmethod
  def glGetPointerv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glGetPointerv(GLenum pname, GLvoid
    **params)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glGetPointerv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glGetPointerv(GLenum pname, "
        "GLvoid **params)': takes a type Python has no way to hand over yet."
    )

  @staticmethod
  def glGetPolygonStipple(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glGetPolygonStipple(GLubyte *mask)':
    takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glGetPolygonStipple' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_2_0::glGetPolygonStipple(GLubyte "
        "*mask)': takes a number to change where it is.")

  @staticmethod
  def glGetProgramInfoLog(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glGetProgramInfoLog(GLuint program,
    GLsizei bufSize, GLsizei *length, GLchar *infoLog)': takes a number to
    change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glGetProgramInfoLog' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_2_0::glGetProgramInfoLog(GLuint "
        "program, GLsizei bufSize, GLsizei *length, GLchar *infoLog)': "
        "takes a number to change where it is.")

  @staticmethod
  def glGetProgramiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glGetProgramiv(GLuint program, GLenum
    pname, GLint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glGetProgramiv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glGetProgramiv(GLuint program, "
        "GLenum pname, GLint *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetQueryObjectiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glGetQueryObjectiv(GLuint id, GLenum
    pname, GLint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glGetQueryObjectiv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_2_0::glGetQueryObjectiv(GLuint "
        "id, GLenum pname, GLint *params)': takes a number to change where "
        "it is.")

  @staticmethod
  def glGetQueryObjectuiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glGetQueryObjectuiv(GLuint id, GLenum
    pname, GLuint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glGetQueryObjectuiv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_2_0::glGetQueryObjectuiv(GLuint "
        "id, GLenum pname, GLuint *params)': takes a number to change where "
        "it is.")

  @staticmethod
  def glGetQueryiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glGetQueryiv(GLenum target, GLenum
    pname, GLint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glGetQueryiv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glGetQueryiv(GLenum target, GLenum "
        "pname, GLint *params)': takes a number to change where it is.")

  @staticmethod
  def glGetSeparableFilter(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glGetSeparableFilter(GLenum target,
    GLenum format, GLenum type, GLvoid *row, GLvoid *column, GLvoid *span)':
    names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glGetSeparableFilter' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_2_0::glGetSeparableFilter(GLenum "
        "target, GLenum format, GLenum type, GLvoid *row, GLvoid *column, "
        "GLvoid *span)': names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glGetShaderInfoLog(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glGetShaderInfoLog(GLuint shader,
    GLsizei bufSize, GLsizei *length, GLchar *infoLog)': takes a number to
    change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glGetShaderInfoLog' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_2_0::glGetShaderInfoLog(GLuint "
        "shader, GLsizei bufSize, GLsizei *length, GLchar *infoLog)': takes "
        "a number to change where it is.")

  @staticmethod
  def glGetShaderSource(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glGetShaderSource(GLuint shader, GLsizei
    bufSize, GLsizei *length, GLchar *source)': takes a number to change
    where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glGetShaderSource' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glGetShaderSource(GLuint shader, "
        "GLsizei bufSize, GLsizei *length, GLchar *source)': takes a number "
        "to change where it is.")

  @staticmethod
  def glGetShaderiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glGetShaderiv(GLuint shader, GLenum
    pname, GLint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glGetShaderiv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glGetShaderiv(GLuint shader, "
        "GLenum pname, GLint *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetString(*__, **_) -> Never:
    """
    Qt's 'const GLubyte *QOpenGLFunctions_2_0::glGetString(GLenum name)':
    gives 'unsigned char', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glGetString' has no cute function yet. Qt's "
        "'const GLubyte *QOpenGLFunctions_2_0::glGetString(GLenum name)': "
        "gives 'unsigned char', which has no cute class yet.")

  @staticmethod
  def glGetTexEnvfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glGetTexEnvfv(GLenum target, GLenum
    pname, GLfloat *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glGetTexEnvfv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glGetTexEnvfv(GLenum target, "
        "GLenum pname, GLfloat *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetTexEnviv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glGetTexEnviv(GLenum target, GLenum
    pname, GLint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glGetTexEnviv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glGetTexEnviv(GLenum target, "
        "GLenum pname, GLint *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetTexGendv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glGetTexGendv(GLenum coord, GLenum
    pname, GLdouble *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glGetTexGendv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glGetTexGendv(GLenum coord, "
        "GLenum pname, GLdouble *params)': takes a number to change where "
        "it is.")

  @staticmethod
  def glGetTexGenfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glGetTexGenfv(GLenum coord, GLenum
    pname, GLfloat *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glGetTexGenfv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glGetTexGenfv(GLenum coord, "
        "GLenum pname, GLfloat *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetTexGeniv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glGetTexGeniv(GLenum coord, GLenum
    pname, GLint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glGetTexGeniv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glGetTexGeniv(GLenum coord, "
        "GLenum pname, GLint *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetTexImage(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glGetTexImage(GLenum target, GLint
    level, GLenum format, GLenum type, GLvoid *pixels)': names 'GLvoid',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glGetTexImage' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glGetTexImage(GLenum target, "
        "GLint level, GLenum format, GLenum type, GLvoid *pixels)': names "
        "'GLvoid', which has no cute class yet.")

  @staticmethod
  def glGetTexLevelParameterfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glGetTexLevelParameterfv(GLenum target,
    GLint level, GLenum pname, GLfloat *params)': takes a number to change
    where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glGetTexLevelParameterfv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_2_0::glGetTexLevelParameterfv(GLenum target, "
        "GLint level, GLenum pname, GLfloat *params)': takes a number to "
        "change where it is.")

  @staticmethod
  def glGetTexLevelParameteriv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glGetTexLevelParameteriv(GLenum target,
    GLint level, GLenum pname, GLint *params)': takes a number to change
    where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glGetTexLevelParameteriv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_2_0::glGetTexLevelParameteriv(GLenum target, "
        "GLint level, GLenum pname, GLint *params)': takes a number to "
        "change where it is.")

  @staticmethod
  def glGetTexParameterfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glGetTexParameterfv(GLenum target,
    GLenum pname, GLfloat *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glGetTexParameterfv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_2_0::glGetTexParameterfv(GLenum "
        "target, GLenum pname, GLfloat *params)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetTexParameteriv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glGetTexParameteriv(GLenum target,
    GLenum pname, GLint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glGetTexParameteriv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_2_0::glGetTexParameteriv(GLenum "
        "target, GLenum pname, GLint *params)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetUniformLocation(*__, **_) -> Never:
    """
    Qt's 'GLint QOpenGLFunctions_2_0::glGetUniformLocation(GLuint program,
    const GLchar *name)': names 'GLchar', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glGetUniformLocation' has no cute function "
        "yet. Qt's 'GLint QOpenGLFunctions_2_0::glGetUniformLocation(GLuint "
        "program, const GLchar *name)': names 'GLchar', which has no cute "
        "class yet.")

  @staticmethod
  def glGetUniformfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glGetUniformfv(GLuint program, GLint
    location, GLfloat *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glGetUniformfv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glGetUniformfv(GLuint program, "
        "GLint location, GLfloat *params)': takes a number to change where "
        "it is.")

  @staticmethod
  def glGetUniformiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glGetUniformiv(GLuint program, GLint
    location, GLint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glGetUniformiv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glGetUniformiv(GLuint program, "
        "GLint location, GLint *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetVertexAttribPointerv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glGetVertexAttribPointerv(GLuint index,
    GLenum pname, GLvoid **pointer)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glGetVertexAttribPointerv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_2_0::glGetVertexAttribPointerv(GLuint index, "
        "GLenum pname, GLvoid **pointer)': takes a type Python has no way "
        "to hand over yet.")

  @staticmethod
  def glGetVertexAttribdv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glGetVertexAttribdv(GLuint index, GLenum
    pname, GLdouble *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glGetVertexAttribdv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_2_0::glGetVertexAttribdv(GLuint "
        "index, GLenum pname, GLdouble *params)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetVertexAttribfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glGetVertexAttribfv(GLuint index, GLenum
    pname, GLfloat *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glGetVertexAttribfv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_2_0::glGetVertexAttribfv(GLuint "
        "index, GLenum pname, GLfloat *params)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetVertexAttribiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glGetVertexAttribiv(GLuint index, GLenum
    pname, GLint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glGetVertexAttribiv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_2_0::glGetVertexAttribiv(GLuint "
        "index, GLenum pname, GLint *params)': takes a number to change "
        "where it is.")

  @staticmethod
  def glIndexPointer(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glIndexPointer(GLenum type, GLsizei
    stride, const GLvoid *pointer)': names 'GLvoid', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glIndexPointer' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glIndexPointer(GLenum type, "
        "GLsizei stride, const GLvoid *pointer)': names 'GLvoid', which has "
        "no cute class yet.")

  @staticmethod
  def glIndexdv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glIndexdv(const GLdouble *c)': names
    'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glIndexdv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glIndexdv(const GLdouble *c)': names "
        "'GLdouble', which has no cute class yet.")

  @staticmethod
  def glIndexfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glIndexfv(const GLfloat *c)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glIndexfv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glIndexfv(const GLfloat *c)': names "
        "'GLfloat', which has no cute class yet.")

  @staticmethod
  def glIndexiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glIndexiv(const GLint *c)': names
    'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glIndexiv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glIndexiv(const GLint *c)': names "
        "'GLint', which has no cute class yet.")

  @staticmethod
  def glIndexsv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glIndexsv(const GLshort *c)': names
    'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glIndexsv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glIndexsv(const GLshort *c)': names "
        "'GLshort', which has no cute class yet.")

  @staticmethod
  def glIndexubv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glIndexubv(const GLubyte *c)': names
    'GLubyte', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glIndexubv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glIndexubv(const GLubyte *c)': names "
        "'GLubyte', which has no cute class yet.")

  @staticmethod
  def glInterleavedArrays(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glInterleavedArrays(GLenum format,
    GLsizei stride, const GLvoid *pointer)': names 'GLvoid', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glInterleavedArrays' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_2_0::glInterleavedArrays(GLenum "
        "format, GLsizei stride, const GLvoid *pointer)': names 'GLvoid', "
        "which has no cute class yet.")

  @staticmethod
  def glLightModelfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glLightModelfv(GLenum pname, const
    GLfloat *params)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glLightModelfv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glLightModelfv(GLenum pname, "
        "const GLfloat *params)': names 'GLfloat', which has no cute class "
        "yet.")

  @staticmethod
  def glLightModeliv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glLightModeliv(GLenum pname, const GLint
    *params)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glLightModeliv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glLightModeliv(GLenum pname, "
        "const GLint *params)': names 'GLint', which has no cute class yet.")

  @staticmethod
  def glLightfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glLightfv(GLenum light, GLenum pname,
    const GLfloat *params)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glLightfv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glLightfv(GLenum light, GLenum pname, "
        "const GLfloat *params)': names 'GLfloat', which has no cute class "
        "yet.")

  @staticmethod
  def glLightiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glLightiv(GLenum light, GLenum pname,
    const GLint *params)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glLightiv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glLightiv(GLenum light, GLenum pname, "
        "const GLint *params)': names 'GLint', which has no cute class yet.")

  @staticmethod
  def glLoadMatrixd(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glLoadMatrixd(const GLdouble *m)': names
    'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glLoadMatrixd' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glLoadMatrixd(const GLdouble "
        "*m)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glLoadMatrixf(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glLoadMatrixf(const GLfloat *m)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glLoadMatrixf' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glLoadMatrixf(const GLfloat *m)': "
        "names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glLoadTransposeMatrixd(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glLoadTransposeMatrixd(const GLdouble
    *m)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glLoadTransposeMatrixd' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_2_0::glLoadTransposeMatrixd(const "
        "GLdouble *m)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glLoadTransposeMatrixf(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glLoadTransposeMatrixf(const GLfloat
    *m)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glLoadTransposeMatrixf' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_2_0::glLoadTransposeMatrixf(const "
        "GLfloat *m)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glMap1d(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glMap1d(GLenum target, GLdouble u1,
    GLdouble u2, GLint stride, GLint order, const GLdouble *points)': names
    'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glMap1d' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glMap1d(GLenum target, GLdouble u1, "
        "GLdouble u2, GLint stride, GLint order, const GLdouble *points)': "
        "names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glMap1f(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glMap1f(GLenum target, GLfloat u1,
    GLfloat u2, GLint stride, GLint order, const GLfloat *points)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glMap1f' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glMap1f(GLenum target, GLfloat u1, "
        "GLfloat u2, GLint stride, GLint order, const GLfloat *points)': "
        "names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glMap2d(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glMap2d(GLenum target, GLdouble u1,
    GLdouble u2, GLint ustride, GLint uorder, GLdouble v1, GLdouble v2, GLint
    vstride, GLint vorder, const GLdouble *points)': names 'GLdouble', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glMap2d' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glMap2d(GLenum target, GLdouble u1, "
        "GLdouble u2, GLint ustride, GLint uorder, GLdouble v1, GLdouble "
        "v2, GLint vstride, GLint vorder, const GLdouble *points)': names "
        "'GLdouble', which has no cute class yet.")

  @staticmethod
  def glMap2f(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glMap2f(GLenum target, GLfloat u1,
    GLfloat u2, GLint ustride, GLint uorder, GLfloat v1, GLfloat v2, GLint
    vstride, GLint vorder, const GLfloat *points)': names 'GLfloat', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glMap2f' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glMap2f(GLenum target, GLfloat u1, "
        "GLfloat u2, GLint ustride, GLint uorder, GLfloat v1, GLfloat v2, "
        "GLint vstride, GLint vorder, const GLfloat *points)': names "
        "'GLfloat', which has no cute class yet.")

  @staticmethod
  def glMapBuffer(*__, **_) -> Never:
    """
    Qt's 'GLvoid *QOpenGLFunctions_2_0::glMapBuffer(GLenum target, GLenum
    access)': gives 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glMapBuffer' has no cute function yet. Qt's "
        "'GLvoid *QOpenGLFunctions_2_0::glMapBuffer(GLenum target, GLenum "
        "access)': gives 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glMaterialfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glMaterialfv(GLenum face, GLenum pname,
    const GLfloat *params)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glMaterialfv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glMaterialfv(GLenum face, GLenum "
        "pname, const GLfloat *params)': names 'GLfloat', which has no cute "
        "class yet.")

  @staticmethod
  def glMaterialiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glMaterialiv(GLenum face, GLenum pname,
    const GLint *params)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glMaterialiv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glMaterialiv(GLenum face, GLenum "
        "pname, const GLint *params)': names 'GLint', which has no cute "
        "class yet.")

  @staticmethod
  def glMultMatrixd(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glMultMatrixd(const GLdouble *m)': names
    'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glMultMatrixd' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glMultMatrixd(const GLdouble "
        "*m)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glMultMatrixf(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glMultMatrixf(const GLfloat *m)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glMultMatrixf' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glMultMatrixf(const GLfloat *m)': "
        "names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glMultTransposeMatrixd(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glMultTransposeMatrixd(const GLdouble
    *m)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glMultTransposeMatrixd' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_2_0::glMultTransposeMatrixd(const "
        "GLdouble *m)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glMultTransposeMatrixf(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glMultTransposeMatrixf(const GLfloat
    *m)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glMultTransposeMatrixf' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_2_0::glMultTransposeMatrixf(const "
        "GLfloat *m)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glMultiDrawArrays(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glMultiDrawArrays(GLenum mode, const
    GLint *first, const GLsizei *count, GLsizei drawcount)': names 'GLint',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glMultiDrawArrays' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glMultiDrawArrays(GLenum mode, "
        "const GLint *first, const GLsizei *count, GLsizei drawcount)': "
        "names 'GLint', which has no cute class yet.")

  @staticmethod
  def glMultiDrawElements(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glMultiDrawElements(GLenum mode, const
    GLsizei *count, GLenum type, const GLvoid *const *indices, GLsizei
    drawcount)': names 'GLsizei', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glMultiDrawElements' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_2_0::glMultiDrawElements(GLenum "
        "mode, const GLsizei *count, GLenum type, const GLvoid *const "
        "*indices, GLsizei drawcount)': names 'GLsizei', which has no cute "
        "class yet.")

  @staticmethod
  def glMultiTexCoord1dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glMultiTexCoord1dv(GLenum target, const
    GLdouble *v)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glMultiTexCoord1dv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_2_0::glMultiTexCoord1dv(GLenum "
        "target, const GLdouble *v)': names 'GLdouble', which has no cute "
        "class yet.")

  @staticmethod
  def glMultiTexCoord1fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glMultiTexCoord1fv(GLenum target, const
    GLfloat *v)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glMultiTexCoord1fv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_2_0::glMultiTexCoord1fv(GLenum "
        "target, const GLfloat *v)': names 'GLfloat', which has no cute "
        "class yet.")

  @staticmethod
  def glMultiTexCoord1iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glMultiTexCoord1iv(GLenum target, const
    GLint *v)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glMultiTexCoord1iv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_2_0::glMultiTexCoord1iv(GLenum "
        "target, const GLint *v)': names 'GLint', which has no cute class "
        "yet.")

  @staticmethod
  def glMultiTexCoord1sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glMultiTexCoord1sv(GLenum target, const
    GLshort *v)': names 'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glMultiTexCoord1sv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_2_0::glMultiTexCoord1sv(GLenum "
        "target, const GLshort *v)': names 'GLshort', which has no cute "
        "class yet.")

  @staticmethod
  def glMultiTexCoord2dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glMultiTexCoord2dv(GLenum target, const
    GLdouble *v)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glMultiTexCoord2dv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_2_0::glMultiTexCoord2dv(GLenum "
        "target, const GLdouble *v)': names 'GLdouble', which has no cute "
        "class yet.")

  @staticmethod
  def glMultiTexCoord2fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glMultiTexCoord2fv(GLenum target, const
    GLfloat *v)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glMultiTexCoord2fv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_2_0::glMultiTexCoord2fv(GLenum "
        "target, const GLfloat *v)': names 'GLfloat', which has no cute "
        "class yet.")

  @staticmethod
  def glMultiTexCoord2iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glMultiTexCoord2iv(GLenum target, const
    GLint *v)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glMultiTexCoord2iv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_2_0::glMultiTexCoord2iv(GLenum "
        "target, const GLint *v)': names 'GLint', which has no cute class "
        "yet.")

  @staticmethod
  def glMultiTexCoord2sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glMultiTexCoord2sv(GLenum target, const
    GLshort *v)': names 'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glMultiTexCoord2sv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_2_0::glMultiTexCoord2sv(GLenum "
        "target, const GLshort *v)': names 'GLshort', which has no cute "
        "class yet.")

  @staticmethod
  def glMultiTexCoord3dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glMultiTexCoord3dv(GLenum target, const
    GLdouble *v)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glMultiTexCoord3dv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_2_0::glMultiTexCoord3dv(GLenum "
        "target, const GLdouble *v)': names 'GLdouble', which has no cute "
        "class yet.")

  @staticmethod
  def glMultiTexCoord3fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glMultiTexCoord3fv(GLenum target, const
    GLfloat *v)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glMultiTexCoord3fv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_2_0::glMultiTexCoord3fv(GLenum "
        "target, const GLfloat *v)': names 'GLfloat', which has no cute "
        "class yet.")

  @staticmethod
  def glMultiTexCoord3iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glMultiTexCoord3iv(GLenum target, const
    GLint *v)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glMultiTexCoord3iv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_2_0::glMultiTexCoord3iv(GLenum "
        "target, const GLint *v)': names 'GLint', which has no cute class "
        "yet.")

  @staticmethod
  def glMultiTexCoord3sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glMultiTexCoord3sv(GLenum target, const
    GLshort *v)': names 'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glMultiTexCoord3sv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_2_0::glMultiTexCoord3sv(GLenum "
        "target, const GLshort *v)': names 'GLshort', which has no cute "
        "class yet.")

  @staticmethod
  def glMultiTexCoord4dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glMultiTexCoord4dv(GLenum target, const
    GLdouble *v)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glMultiTexCoord4dv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_2_0::glMultiTexCoord4dv(GLenum "
        "target, const GLdouble *v)': names 'GLdouble', which has no cute "
        "class yet.")

  @staticmethod
  def glMultiTexCoord4fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glMultiTexCoord4fv(GLenum target, const
    GLfloat *v)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glMultiTexCoord4fv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_2_0::glMultiTexCoord4fv(GLenum "
        "target, const GLfloat *v)': names 'GLfloat', which has no cute "
        "class yet.")

  @staticmethod
  def glMultiTexCoord4iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glMultiTexCoord4iv(GLenum target, const
    GLint *v)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glMultiTexCoord4iv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_2_0::glMultiTexCoord4iv(GLenum "
        "target, const GLint *v)': names 'GLint', which has no cute class "
        "yet.")

  @staticmethod
  def glMultiTexCoord4sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glMultiTexCoord4sv(GLenum target, const
    GLshort *v)': names 'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glMultiTexCoord4sv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_2_0::glMultiTexCoord4sv(GLenum "
        "target, const GLshort *v)': names 'GLshort', which has no cute "
        "class yet.")

  @staticmethod
  def glNormal3bv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glNormal3bv(const GLbyte *v)': names
    'GLbyte', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glNormal3bv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glNormal3bv(const GLbyte *v)': names "
        "'GLbyte', which has no cute class yet.")

  @staticmethod
  def glNormal3dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glNormal3dv(const GLdouble *v)': names
    'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glNormal3dv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glNormal3dv(const GLdouble *v)': names "
        "'GLdouble', which has no cute class yet.")

  @staticmethod
  def glNormal3fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glNormal3fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glNormal3fv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glNormal3fv(const GLfloat *v)': names "
        "'GLfloat', which has no cute class yet.")

  @staticmethod
  def glNormal3iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glNormal3iv(const GLint *v)': names
    'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glNormal3iv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glNormal3iv(const GLint *v)': names "
        "'GLint', which has no cute class yet.")

  @staticmethod
  def glNormal3sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glNormal3sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glNormal3sv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glNormal3sv(const GLshort *v)': names "
        "'GLshort', which has no cute class yet.")

  @staticmethod
  def glNormalPointer(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glNormalPointer(GLenum type, GLsizei
    stride, const GLvoid *pointer)': names 'GLvoid', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glNormalPointer' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glNormalPointer(GLenum type, "
        "GLsizei stride, const GLvoid *pointer)': names 'GLvoid', which has "
        "no cute class yet.")

  @staticmethod
  def glPixelMapfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glPixelMapfv(GLenum map, GLint mapsize,
    const GLfloat *values)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glPixelMapfv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glPixelMapfv(GLenum map, GLint "
        "mapsize, const GLfloat *values)': names 'GLfloat', which has no "
        "cute class yet.")

  @staticmethod
  def glPixelMapuiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glPixelMapuiv(GLenum map, GLint mapsize,
    const GLuint *values)': names 'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glPixelMapuiv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glPixelMapuiv(GLenum map, GLint "
        "mapsize, const GLuint *values)': names 'GLuint', which has no cute "
        "class yet.")

  @staticmethod
  def glPixelMapusv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glPixelMapusv(GLenum map, GLint mapsize,
    const GLushort *values)': names 'GLushort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glPixelMapusv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glPixelMapusv(GLenum map, GLint "
        "mapsize, const GLushort *values)': names 'GLushort', which has no "
        "cute class yet.")

  @staticmethod
  def glPointParameterfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glPointParameterfv(GLenum pname, const
    GLfloat *params)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glPointParameterfv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_2_0::glPointParameterfv(GLenum "
        "pname, const GLfloat *params)': names 'GLfloat', which has no cute "
        "class yet.")

  @staticmethod
  def glPointParameteriv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glPointParameteriv(GLenum pname, const
    GLint *params)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glPointParameteriv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_2_0::glPointParameteriv(GLenum "
        "pname, const GLint *params)': names 'GLint', which has no cute "
        "class yet.")

  @staticmethod
  def glPolygonStipple(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glPolygonStipple(const GLubyte *mask)':
    names 'GLubyte', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glPolygonStipple' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glPolygonStipple(const GLubyte "
        "*mask)': names 'GLubyte', which has no cute class yet.")

  @staticmethod
  def glPrioritizeTextures(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glPrioritizeTextures(GLsizei n, const
    GLuint *textures, const GLfloat *priorities)': names 'GLuint', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glPrioritizeTextures' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_2_0::glPrioritizeTextures(GLsizei "
        "n, const GLuint *textures, const GLfloat *priorities)': names "
        "'GLuint', which has no cute class yet.")

  @staticmethod
  def glRasterPos2dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glRasterPos2dv(const GLdouble *v)':
    names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glRasterPos2dv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glRasterPos2dv(const GLdouble "
        "*v)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glRasterPos2fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glRasterPos2fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glRasterPos2fv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glRasterPos2fv(const GLfloat "
        "*v)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glRasterPos2iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glRasterPos2iv(const GLint *v)': names
    'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glRasterPos2iv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glRasterPos2iv(const GLint *v)': "
        "names 'GLint', which has no cute class yet.")

  @staticmethod
  def glRasterPos2sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glRasterPos2sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glRasterPos2sv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glRasterPos2sv(const GLshort "
        "*v)': names 'GLshort', which has no cute class yet.")

  @staticmethod
  def glRasterPos3dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glRasterPos3dv(const GLdouble *v)':
    names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glRasterPos3dv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glRasterPos3dv(const GLdouble "
        "*v)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glRasterPos3fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glRasterPos3fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glRasterPos3fv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glRasterPos3fv(const GLfloat "
        "*v)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glRasterPos3iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glRasterPos3iv(const GLint *v)': names
    'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glRasterPos3iv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glRasterPos3iv(const GLint *v)': "
        "names 'GLint', which has no cute class yet.")

  @staticmethod
  def glRasterPos3sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glRasterPos3sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glRasterPos3sv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glRasterPos3sv(const GLshort "
        "*v)': names 'GLshort', which has no cute class yet.")

  @staticmethod
  def glRasterPos4dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glRasterPos4dv(const GLdouble *v)':
    names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glRasterPos4dv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glRasterPos4dv(const GLdouble "
        "*v)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glRasterPos4fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glRasterPos4fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glRasterPos4fv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glRasterPos4fv(const GLfloat "
        "*v)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glRasterPos4iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glRasterPos4iv(const GLint *v)': names
    'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glRasterPos4iv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glRasterPos4iv(const GLint *v)': "
        "names 'GLint', which has no cute class yet.")

  @staticmethod
  def glRasterPos4sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glRasterPos4sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glRasterPos4sv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glRasterPos4sv(const GLshort "
        "*v)': names 'GLshort', which has no cute class yet.")

  @staticmethod
  def glReadPixels(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glReadPixels(GLint x, GLint y, GLsizei
    width, GLsizei height, GLenum format, GLenum type, GLvoid *pixels)':
    names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glReadPixels' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glReadPixels(GLint x, GLint y, GLsizei "
        "width, GLsizei height, GLenum format, GLenum type, GLvoid "
        "*pixels)': names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glRectdv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glRectdv(const GLdouble *v1, const
    GLdouble *v2)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glRectdv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glRectdv(const GLdouble *v1, const "
        "GLdouble *v2)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glRectfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glRectfv(const GLfloat *v1, const
    GLfloat *v2)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glRectfv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glRectfv(const GLfloat *v1, const "
        "GLfloat *v2)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glRectiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glRectiv(const GLint *v1, const GLint
    *v2)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glRectiv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glRectiv(const GLint *v1, const GLint "
        "*v2)': names 'GLint', which has no cute class yet.")

  @staticmethod
  def glRectsv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glRectsv(const GLshort *v1, const
    GLshort *v2)': names 'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glRectsv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glRectsv(const GLshort *v1, const "
        "GLshort *v2)': names 'GLshort', which has no cute class yet.")

  @staticmethod
  def glSecondaryColor3bv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glSecondaryColor3bv(const GLbyte *v)':
    names 'GLbyte', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glSecondaryColor3bv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_2_0::glSecondaryColor3bv(const "
        "GLbyte *v)': names 'GLbyte', which has no cute class yet.")

  @staticmethod
  def glSecondaryColor3dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glSecondaryColor3dv(const GLdouble *v)':
    names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glSecondaryColor3dv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_2_0::glSecondaryColor3dv(const "
        "GLdouble *v)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glSecondaryColor3fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glSecondaryColor3fv(const GLfloat *v)':
    names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glSecondaryColor3fv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_2_0::glSecondaryColor3fv(const "
        "GLfloat *v)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glSecondaryColor3iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glSecondaryColor3iv(const GLint *v)':
    names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glSecondaryColor3iv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_2_0::glSecondaryColor3iv(const "
        "GLint *v)': names 'GLint', which has no cute class yet.")

  @staticmethod
  def glSecondaryColor3sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glSecondaryColor3sv(const GLshort *v)':
    names 'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glSecondaryColor3sv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_2_0::glSecondaryColor3sv(const "
        "GLshort *v)': names 'GLshort', which has no cute class yet.")

  @staticmethod
  def glSecondaryColor3ubv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glSecondaryColor3ubv(const GLubyte *v)':
    names 'GLubyte', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glSecondaryColor3ubv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_2_0::glSecondaryColor3ubv(const "
        "GLubyte *v)': names 'GLubyte', which has no cute class yet.")

  @staticmethod
  def glSecondaryColor3uiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glSecondaryColor3uiv(const GLuint *v)':
    names 'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glSecondaryColor3uiv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_2_0::glSecondaryColor3uiv(const "
        "GLuint *v)': names 'GLuint', which has no cute class yet.")

  @staticmethod
  def glSecondaryColor3usv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glSecondaryColor3usv(const GLushort
    *v)': names 'GLushort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glSecondaryColor3usv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_2_0::glSecondaryColor3usv(const "
        "GLushort *v)': names 'GLushort', which has no cute class yet.")

  @staticmethod
  def glSecondaryColorPointer(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glSecondaryColorPointer(GLint size,
    GLenum type, GLsizei stride, const GLvoid *pointer)': names 'GLvoid',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glSecondaryColorPointer' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_2_0::glSecondaryColorPointer(GLint size, GLenum "
        "type, GLsizei stride, const GLvoid *pointer)': names 'GLvoid', "
        "which has no cute class yet.")

  @staticmethod
  def glSelectBuffer(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glSelectBuffer(GLsizei size, GLuint
    *buffer)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glSelectBuffer' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glSelectBuffer(GLsizei size, "
        "GLuint *buffer)': takes a number to change where it is.")

  @staticmethod
  def glSeparableFilter2D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glSeparableFilter2D(GLenum target,
    GLenum internalformat, GLsizei width, GLsizei height, GLenum format,
    GLenum type, const GLvoid *row, const GLvoid *column)': names 'GLvoid',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glSeparableFilter2D' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_2_0::glSeparableFilter2D(GLenum "
        "target, GLenum internalformat, GLsizei width, GLsizei height, "
        "GLenum format, GLenum type, const GLvoid *row, const GLvoid "
        "*column)': names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glShaderSource(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glShaderSource(GLuint shader, GLsizei
    count, const GLchar *const *string, const GLint *length)': names 'GLchar
    *const', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glShaderSource' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glShaderSource(GLuint shader, "
        "GLsizei count, const GLchar *const *string, const GLint *length)': "
        "names 'GLchar *const', which has no cute class yet.")

  @staticmethod
  def glTexCoord1dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glTexCoord1dv(const GLdouble *v)': names
    'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glTexCoord1dv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glTexCoord1dv(const GLdouble "
        "*v)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glTexCoord1fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glTexCoord1fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glTexCoord1fv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glTexCoord1fv(const GLfloat *v)': "
        "names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glTexCoord1iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glTexCoord1iv(const GLint *v)': names
    'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glTexCoord1iv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glTexCoord1iv(const GLint *v)': "
        "names 'GLint', which has no cute class yet.")

  @staticmethod
  def glTexCoord1sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glTexCoord1sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glTexCoord1sv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glTexCoord1sv(const GLshort *v)': "
        "names 'GLshort', which has no cute class yet.")

  @staticmethod
  def glTexCoord2dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glTexCoord2dv(const GLdouble *v)': names
    'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glTexCoord2dv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glTexCoord2dv(const GLdouble "
        "*v)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glTexCoord2fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glTexCoord2fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glTexCoord2fv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glTexCoord2fv(const GLfloat *v)': "
        "names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glTexCoord2iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glTexCoord2iv(const GLint *v)': names
    'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glTexCoord2iv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glTexCoord2iv(const GLint *v)': "
        "names 'GLint', which has no cute class yet.")

  @staticmethod
  def glTexCoord2sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glTexCoord2sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glTexCoord2sv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glTexCoord2sv(const GLshort *v)': "
        "names 'GLshort', which has no cute class yet.")

  @staticmethod
  def glTexCoord3dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glTexCoord3dv(const GLdouble *v)': names
    'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glTexCoord3dv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glTexCoord3dv(const GLdouble "
        "*v)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glTexCoord3fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glTexCoord3fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glTexCoord3fv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glTexCoord3fv(const GLfloat *v)': "
        "names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glTexCoord3iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glTexCoord3iv(const GLint *v)': names
    'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glTexCoord3iv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glTexCoord3iv(const GLint *v)': "
        "names 'GLint', which has no cute class yet.")

  @staticmethod
  def glTexCoord3sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glTexCoord3sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glTexCoord3sv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glTexCoord3sv(const GLshort *v)': "
        "names 'GLshort', which has no cute class yet.")

  @staticmethod
  def glTexCoord4dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glTexCoord4dv(const GLdouble *v)': names
    'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glTexCoord4dv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glTexCoord4dv(const GLdouble "
        "*v)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glTexCoord4fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glTexCoord4fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glTexCoord4fv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glTexCoord4fv(const GLfloat *v)': "
        "names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glTexCoord4iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glTexCoord4iv(const GLint *v)': names
    'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glTexCoord4iv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glTexCoord4iv(const GLint *v)': "
        "names 'GLint', which has no cute class yet.")

  @staticmethod
  def glTexCoord4sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glTexCoord4sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glTexCoord4sv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glTexCoord4sv(const GLshort *v)': "
        "names 'GLshort', which has no cute class yet.")

  @staticmethod
  def glTexCoordPointer(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glTexCoordPointer(GLint size, GLenum
    type, GLsizei stride, const GLvoid *pointer)': names 'GLvoid', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glTexCoordPointer' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glTexCoordPointer(GLint size, "
        "GLenum type, GLsizei stride, const GLvoid *pointer)': names "
        "'GLvoid', which has no cute class yet.")

  @staticmethod
  def glTexEnvfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glTexEnvfv(GLenum target, GLenum pname,
    const GLfloat *params)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glTexEnvfv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glTexEnvfv(GLenum target, GLenum "
        "pname, const GLfloat *params)': names 'GLfloat', which has no cute "
        "class yet.")

  @staticmethod
  def glTexEnviv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glTexEnviv(GLenum target, GLenum pname,
    const GLint *params)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glTexEnviv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glTexEnviv(GLenum target, GLenum "
        "pname, const GLint *params)': names 'GLint', which has no cute "
        "class yet.")

  @staticmethod
  def glTexGendv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glTexGendv(GLenum coord, GLenum pname,
    const GLdouble *params)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glTexGendv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glTexGendv(GLenum coord, GLenum pname, "
        "const GLdouble *params)': names 'GLdouble', which has no cute "
        "class yet.")

  @staticmethod
  def glTexGenfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glTexGenfv(GLenum coord, GLenum pname,
    const GLfloat *params)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glTexGenfv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glTexGenfv(GLenum coord, GLenum pname, "
        "const GLfloat *params)': names 'GLfloat', which has no cute class "
        "yet.")

  @staticmethod
  def glTexGeniv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glTexGeniv(GLenum coord, GLenum pname,
    const GLint *params)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glTexGeniv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glTexGeniv(GLenum coord, GLenum pname, "
        "const GLint *params)': names 'GLint', which has no cute class yet.")

  @staticmethod
  def glTexImage1D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glTexImage1D(GLenum target, GLint level,
    GLint internalformat, GLsizei width, GLint border, GLenum format, GLenum
    type, const GLvoid *pixels)': names 'GLvoid', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glTexImage1D' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glTexImage1D(GLenum target, GLint "
        "level, GLint internalformat, GLsizei width, GLint border, GLenum "
        "format, GLenum type, const GLvoid *pixels)': names 'GLvoid', which "
        "has no cute class yet.")

  @staticmethod
  def glTexImage2D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glTexImage2D(GLenum target, GLint level,
    GLint internalformat, GLsizei width, GLsizei height, GLint border, GLenum
    format, GLenum type, const GLvoid *pixels)': names 'GLvoid', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glTexImage2D' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glTexImage2D(GLenum target, GLint "
        "level, GLint internalformat, GLsizei width, GLsizei height, GLint "
        "border, GLenum format, GLenum type, const GLvoid *pixels)': names "
        "'GLvoid', which has no cute class yet.")

  @staticmethod
  def glTexImage3D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glTexImage3D(GLenum target, GLint level,
    GLint internalformat, GLsizei width, GLsizei height, GLsizei depth, GLint
    border, GLenum format, GLenum type, const GLvoid *pixels)': names
    'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glTexImage3D' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glTexImage3D(GLenum target, GLint "
        "level, GLint internalformat, GLsizei width, GLsizei height, "
        "GLsizei depth, GLint border, GLenum format, GLenum type, const "
        "GLvoid *pixels)': names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glTexParameterfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glTexParameterfv(GLenum target, GLenum
    pname, const GLfloat *params)': names 'GLfloat', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glTexParameterfv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glTexParameterfv(GLenum target, "
        "GLenum pname, const GLfloat *params)': names 'GLfloat', which has "
        "no cute class yet.")

  @staticmethod
  def glTexParameteriv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glTexParameteriv(GLenum target, GLenum
    pname, const GLint *params)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glTexParameteriv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glTexParameteriv(GLenum target, "
        "GLenum pname, const GLint *params)': names 'GLint', which has no "
        "cute class yet.")

  @staticmethod
  def glTexSubImage1D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glTexSubImage1D(GLenum target, GLint
    level, GLint xoffset, GLsizei width, GLenum format, GLenum type, const
    GLvoid *pixels)': names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glTexSubImage1D' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glTexSubImage1D(GLenum target, "
        "GLint level, GLint xoffset, GLsizei width, GLenum format, GLenum "
        "type, const GLvoid *pixels)': names 'GLvoid', which has no cute "
        "class yet.")

  @staticmethod
  def glTexSubImage2D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glTexSubImage2D(GLenum target, GLint
    level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height,
    GLenum format, GLenum type, const GLvoid *pixels)': names 'GLvoid', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glTexSubImage2D' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glTexSubImage2D(GLenum target, "
        "GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei "
        "height, GLenum format, GLenum type, const GLvoid *pixels)': names "
        "'GLvoid', which has no cute class yet.")

  @staticmethod
  def glTexSubImage3D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glTexSubImage3D(GLenum target, GLint
    level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width,
    GLsizei height, GLsizei depth, GLenum format, GLenum type, const GLvoid
    *pixels)': names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glTexSubImage3D' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glTexSubImage3D(GLenum target, "
        "GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei "
        "width, GLsizei height, GLsizei depth, GLenum format, GLenum type, "
        "const GLvoid *pixels)': names 'GLvoid', which has no cute class "
        "yet.")

  @staticmethod
  def glUniform1fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glUniform1fv(GLint location, GLsizei
    count, const GLfloat *value)': names 'GLfloat', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glUniform1fv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glUniform1fv(GLint location, GLsizei "
        "count, const GLfloat *value)': names 'GLfloat', which has no cute "
        "class yet.")

  @staticmethod
  def glUniform1iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glUniform1iv(GLint location, GLsizei
    count, const GLint *value)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glUniform1iv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glUniform1iv(GLint location, GLsizei "
        "count, const GLint *value)': names 'GLint', which has no cute "
        "class yet.")

  @staticmethod
  def glUniform2fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glUniform2fv(GLint location, GLsizei
    count, const GLfloat *value)': names 'GLfloat', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glUniform2fv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glUniform2fv(GLint location, GLsizei "
        "count, const GLfloat *value)': names 'GLfloat', which has no cute "
        "class yet.")

  @staticmethod
  def glUniform2iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glUniform2iv(GLint location, GLsizei
    count, const GLint *value)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glUniform2iv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glUniform2iv(GLint location, GLsizei "
        "count, const GLint *value)': names 'GLint', which has no cute "
        "class yet.")

  @staticmethod
  def glUniform3fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glUniform3fv(GLint location, GLsizei
    count, const GLfloat *value)': names 'GLfloat', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glUniform3fv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glUniform3fv(GLint location, GLsizei "
        "count, const GLfloat *value)': names 'GLfloat', which has no cute "
        "class yet.")

  @staticmethod
  def glUniform3iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glUniform3iv(GLint location, GLsizei
    count, const GLint *value)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glUniform3iv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glUniform3iv(GLint location, GLsizei "
        "count, const GLint *value)': names 'GLint', which has no cute "
        "class yet.")

  @staticmethod
  def glUniform4fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glUniform4fv(GLint location, GLsizei
    count, const GLfloat *value)': names 'GLfloat', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glUniform4fv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glUniform4fv(GLint location, GLsizei "
        "count, const GLfloat *value)': names 'GLfloat', which has no cute "
        "class yet.")

  @staticmethod
  def glUniform4iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glUniform4iv(GLint location, GLsizei
    count, const GLint *value)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glUniform4iv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glUniform4iv(GLint location, GLsizei "
        "count, const GLint *value)': names 'GLint', which has no cute "
        "class yet.")

  @staticmethod
  def glUniformMatrix2fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glUniformMatrix2fv(GLint location,
    GLsizei count, GLboolean transpose, const GLfloat *value)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glUniformMatrix2fv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_2_0::glUniformMatrix2fv(GLint "
        "location, GLsizei count, GLboolean transpose, const GLfloat "
        "*value)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glUniformMatrix3fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glUniformMatrix3fv(GLint location,
    GLsizei count, GLboolean transpose, const GLfloat *value)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glUniformMatrix3fv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_2_0::glUniformMatrix3fv(GLint "
        "location, GLsizei count, GLboolean transpose, const GLfloat "
        "*value)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glUniformMatrix4fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glUniformMatrix4fv(GLint location,
    GLsizei count, GLboolean transpose, const GLfloat *value)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glUniformMatrix4fv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_2_0::glUniformMatrix4fv(GLint "
        "location, GLsizei count, GLboolean transpose, const GLfloat "
        "*value)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glVertex2dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glVertex2dv(const GLdouble *v)': names
    'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glVertex2dv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glVertex2dv(const GLdouble *v)': names "
        "'GLdouble', which has no cute class yet.")

  @staticmethod
  def glVertex2fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glVertex2fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glVertex2fv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glVertex2fv(const GLfloat *v)': names "
        "'GLfloat', which has no cute class yet.")

  @staticmethod
  def glVertex2iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glVertex2iv(const GLint *v)': names
    'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glVertex2iv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glVertex2iv(const GLint *v)': names "
        "'GLint', which has no cute class yet.")

  @staticmethod
  def glVertex2sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glVertex2sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glVertex2sv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glVertex2sv(const GLshort *v)': names "
        "'GLshort', which has no cute class yet.")

  @staticmethod
  def glVertex3dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glVertex3dv(const GLdouble *v)': names
    'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glVertex3dv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glVertex3dv(const GLdouble *v)': names "
        "'GLdouble', which has no cute class yet.")

  @staticmethod
  def glVertex3fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glVertex3fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glVertex3fv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glVertex3fv(const GLfloat *v)': names "
        "'GLfloat', which has no cute class yet.")

  @staticmethod
  def glVertex3iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glVertex3iv(const GLint *v)': names
    'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glVertex3iv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glVertex3iv(const GLint *v)': names "
        "'GLint', which has no cute class yet.")

  @staticmethod
  def glVertex3sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glVertex3sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glVertex3sv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glVertex3sv(const GLshort *v)': names "
        "'GLshort', which has no cute class yet.")

  @staticmethod
  def glVertex4dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glVertex4dv(const GLdouble *v)': names
    'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glVertex4dv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glVertex4dv(const GLdouble *v)': names "
        "'GLdouble', which has no cute class yet.")

  @staticmethod
  def glVertex4fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glVertex4fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glVertex4fv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glVertex4fv(const GLfloat *v)': names "
        "'GLfloat', which has no cute class yet.")

  @staticmethod
  def glVertex4iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glVertex4iv(const GLint *v)': names
    'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glVertex4iv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glVertex4iv(const GLint *v)': names "
        "'GLint', which has no cute class yet.")

  @staticmethod
  def glVertex4sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glVertex4sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glVertex4sv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_2_0::glVertex4sv(const GLshort *v)': names "
        "'GLshort', which has no cute class yet.")

  @staticmethod
  def glVertexAttrib1dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib1dv(GLuint index, const
    GLdouble *v)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glVertexAttrib1dv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib1dv(GLuint index, "
        "const GLdouble *v)': names 'GLdouble', which has no cute class yet."
    )

  @staticmethod
  def glVertexAttrib1fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib1fv(GLuint index, const
    GLfloat *v)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glVertexAttrib1fv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib1fv(GLuint index, "
        "const GLfloat *v)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glVertexAttrib1sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib1sv(GLuint index, const
    GLshort *v)': names 'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glVertexAttrib1sv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib1sv(GLuint index, "
        "const GLshort *v)': names 'GLshort', which has no cute class yet.")

  @staticmethod
  def glVertexAttrib2dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib2dv(GLuint index, const
    GLdouble *v)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glVertexAttrib2dv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib2dv(GLuint index, "
        "const GLdouble *v)': names 'GLdouble', which has no cute class yet."
    )

  @staticmethod
  def glVertexAttrib2fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib2fv(GLuint index, const
    GLfloat *v)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glVertexAttrib2fv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib2fv(GLuint index, "
        "const GLfloat *v)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glVertexAttrib2sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib2sv(GLuint index, const
    GLshort *v)': names 'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glVertexAttrib2sv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib2sv(GLuint index, "
        "const GLshort *v)': names 'GLshort', which has no cute class yet.")

  @staticmethod
  def glVertexAttrib3dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib3dv(GLuint index, const
    GLdouble *v)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glVertexAttrib3dv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib3dv(GLuint index, "
        "const GLdouble *v)': names 'GLdouble', which has no cute class yet."
    )

  @staticmethod
  def glVertexAttrib3fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib3fv(GLuint index, const
    GLfloat *v)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glVertexAttrib3fv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib3fv(GLuint index, "
        "const GLfloat *v)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glVertexAttrib3sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib3sv(GLuint index, const
    GLshort *v)': names 'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glVertexAttrib3sv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib3sv(GLuint index, "
        "const GLshort *v)': names 'GLshort', which has no cute class yet.")

  @staticmethod
  def glVertexAttrib4Nbv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib4Nbv(GLuint index, const
    GLbyte *v)': names 'GLbyte', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glVertexAttrib4Nbv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib4Nbv(GLuint "
        "index, const GLbyte *v)': names 'GLbyte', which has no cute class "
        "yet.")

  @staticmethod
  def glVertexAttrib4Niv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib4Niv(GLuint index, const
    GLint *v)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glVertexAttrib4Niv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib4Niv(GLuint "
        "index, const GLint *v)': names 'GLint', which has no cute class "
        "yet.")

  @staticmethod
  def glVertexAttrib4Nsv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib4Nsv(GLuint index, const
    GLshort *v)': names 'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glVertexAttrib4Nsv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib4Nsv(GLuint "
        "index, const GLshort *v)': names 'GLshort', which has no cute "
        "class yet.")

  @staticmethod
  def glVertexAttrib4Nubv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib4Nubv(GLuint index, const
    GLubyte *v)': names 'GLubyte', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glVertexAttrib4Nubv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib4Nubv(GLuint "
        "index, const GLubyte *v)': names 'GLubyte', which has no cute "
        "class yet.")

  @staticmethod
  def glVertexAttrib4Nuiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib4Nuiv(GLuint index, const
    GLuint *v)': names 'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glVertexAttrib4Nuiv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib4Nuiv(GLuint "
        "index, const GLuint *v)': names 'GLuint', which has no cute class "
        "yet.")

  @staticmethod
  def glVertexAttrib4Nusv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib4Nusv(GLuint index, const
    GLushort *v)': names 'GLushort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glVertexAttrib4Nusv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib4Nusv(GLuint "
        "index, const GLushort *v)': names 'GLushort', which has no cute "
        "class yet.")

  @staticmethod
  def glVertexAttrib4bv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib4bv(GLuint index, const
    GLbyte *v)': names 'GLbyte', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glVertexAttrib4bv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib4bv(GLuint index, "
        "const GLbyte *v)': names 'GLbyte', which has no cute class yet.")

  @staticmethod
  def glVertexAttrib4dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib4dv(GLuint index, const
    GLdouble *v)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glVertexAttrib4dv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib4dv(GLuint index, "
        "const GLdouble *v)': names 'GLdouble', which has no cute class yet."
    )

  @staticmethod
  def glVertexAttrib4fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib4fv(GLuint index, const
    GLfloat *v)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glVertexAttrib4fv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib4fv(GLuint index, "
        "const GLfloat *v)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glVertexAttrib4iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib4iv(GLuint index, const
    GLint *v)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glVertexAttrib4iv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib4iv(GLuint index, "
        "const GLint *v)': names 'GLint', which has no cute class yet.")

  @staticmethod
  def glVertexAttrib4sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib4sv(GLuint index, const
    GLshort *v)': names 'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glVertexAttrib4sv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib4sv(GLuint index, "
        "const GLshort *v)': names 'GLshort', which has no cute class yet.")

  @staticmethod
  def glVertexAttrib4ubv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib4ubv(GLuint index, const
    GLubyte *v)': names 'GLubyte', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glVertexAttrib4ubv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib4ubv(GLuint "
        "index, const GLubyte *v)': names 'GLubyte', which has no cute "
        "class yet.")

  @staticmethod
  def glVertexAttrib4uiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib4uiv(GLuint index, const
    GLuint *v)': names 'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glVertexAttrib4uiv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib4uiv(GLuint "
        "index, const GLuint *v)': names 'GLuint', which has no cute class "
        "yet.")

  @staticmethod
  def glVertexAttrib4usv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib4usv(GLuint index, const
    GLushort *v)': names 'GLushort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glVertexAttrib4usv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_2_0::glVertexAttrib4usv(GLuint "
        "index, const GLushort *v)': names 'GLushort', which has no cute "
        "class yet.")

  @staticmethod
  def glVertexAttribPointer(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glVertexAttribPointer(GLuint index,
    GLint size, GLenum type, GLboolean normalized, GLsizei stride, const
    GLvoid *pointer)': names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glVertexAttribPointer' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_2_0::glVertexAttribPointer(GLuint "
        "index, GLint size, GLenum type, GLboolean normalized, GLsizei "
        "stride, const GLvoid *pointer)': names 'GLvoid', which has no cute "
        "class yet.")

  @staticmethod
  def glVertexPointer(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glVertexPointer(GLint size, GLenum type,
    GLsizei stride, const GLvoid *pointer)': names 'GLvoid', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glVertexPointer' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glVertexPointer(GLint size, "
        "GLenum type, GLsizei stride, const GLvoid *pointer)': names "
        "'GLvoid', which has no cute class yet.")

  @staticmethod
  def glWindowPos2dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glWindowPos2dv(const GLdouble *v)':
    names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glWindowPos2dv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glWindowPos2dv(const GLdouble "
        "*v)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glWindowPos2fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glWindowPos2fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glWindowPos2fv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glWindowPos2fv(const GLfloat "
        "*v)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glWindowPos2iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glWindowPos2iv(const GLint *v)': names
    'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glWindowPos2iv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glWindowPos2iv(const GLint *v)': "
        "names 'GLint', which has no cute class yet.")

  @staticmethod
  def glWindowPos2sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glWindowPos2sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glWindowPos2sv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glWindowPos2sv(const GLshort "
        "*v)': names 'GLshort', which has no cute class yet.")

  @staticmethod
  def glWindowPos3dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glWindowPos3dv(const GLdouble *v)':
    names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glWindowPos3dv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glWindowPos3dv(const GLdouble "
        "*v)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glWindowPos3fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glWindowPos3fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glWindowPos3fv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glWindowPos3fv(const GLfloat "
        "*v)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glWindowPos3iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glWindowPos3iv(const GLint *v)': names
    'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glWindowPos3iv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glWindowPos3iv(const GLint *v)': "
        "names 'GLint', which has no cute class yet.")

  @staticmethod
  def glWindowPos3sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_2_0::glWindowPos3sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_2_0.glWindowPos3sv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_2_0::glWindowPos3sv(const GLshort "
        "*v)': names 'GLshort', which has no cute class yet.")
