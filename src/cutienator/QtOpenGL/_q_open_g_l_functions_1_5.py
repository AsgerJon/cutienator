"""
QOpenGLFunctions_1_5 binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpenGL/qopenglfunctions_1_5.h, Qt 6.12.0. Changes made here are lost.
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


class QOpenGLFunctions_1_5(QAbstractOpenGLFunctions):
  """
  The cute side of Qt's QOpenGLFunctions_1_5: a plain Python object standing
  in front of one C++ QOpenGLFunctions_1_5.

  It is built on the cute 'QAbstractOpenGLFunctions', as Qt's
  QOpenGLFunctions_1_5 is built on Qt's QAbstractOpenGLFunctions, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QOpenGLFunctions_1_5 that has a ritual and that
  Python can call so far, 245 names in all: 'initializeOpenGLFunctions',
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
  'glBindBuffer', 'glEndQuery', 'glBeginQuery', 'glIsQuery', 'glTranslatef',
  'glTranslated', 'glScalef', 'glScaled', 'glRotatef', 'glRotated',
  'glPushMatrix', 'glPopMatrix', 'glOrtho', 'glMatrixMode', 'glLoadIdentity',
  'glFrustum', 'glIsList', 'glCopyPixels', 'glPixelTransferi',
  'glPixelTransferf', 'glPixelZoom', 'glAlphaFunc', 'glEvalPoint2',
  'glEvalMesh2', 'glEvalPoint1', 'glEvalMesh1', 'glEvalCoord2f',
  'glEvalCoord2d', 'glEvalCoord1f', 'glEvalCoord1d', 'glMapGrid2f',
  'glMapGrid2d', 'glMapGrid1f', 'glMapGrid1d', 'glPushAttrib', 'glPopAttrib',
  'glAccum', 'glIndexMask', 'glClearIndex', 'glClearAccum', 'glPushName',
  'glPopName', 'glPassThrough', 'glLoadName', 'glInitNames', 'glRenderMode',
  'glTexGeni', 'glTexGenf', 'glTexGend', 'glTexEnvi', 'glTexEnvf',
  'glShadeModel', 'glMateriali', 'glMaterialf', 'glLineStipple',
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
  'glSecondaryColor3b', 'glFogCoordd', 'glFogCoordf', 'isContextCompatible',
  'versionProfile'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpenGLFunctions_1_5::~QOpenGLFunctions_1_5()': the destructor:
    Python never removes a C++ QOpenGLFunctions_1_5.
  - Qt's 'void QOpenGLFunctions_1_5::glGetTexLevelParameteriv(GLenum target,
    GLint level, GLenum pname, GLint *params)': takes a number to change
    where it is.
  - Qt's 'void QOpenGLFunctions_1_5::glGetTexLevelParameterfv(GLenum target,
    GLint level, GLenum pname, GLfloat *params)': takes a number to change
    where it is.
  - Qt's 'void QOpenGLFunctions_1_5::glGetTexParameteriv(GLenum target,
    GLenum pname, GLint *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_1_5::glGetTexParameterfv(GLenum target,
    GLenum pname, GLfloat *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_1_5::glGetTexImage(GLenum target, GLint
    level, GLenum format, GLenum type, GLvoid *pixels)': names 'GLvoid',
    which has no cute class yet.
  - Qt's 'const GLubyte *QOpenGLFunctions_1_5::glGetString(GLenum name)':
    gives 'unsigned char', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glGetIntegerv(GLenum pname, GLint
    *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_1_5::glGetFloatv(GLenum pname, GLfloat
    *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_1_5::glGetDoublev(GLenum pname, GLdouble
    *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_1_5::glGetBooleanv(GLenum pname, GLboolean
    *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_1_5::glReadPixels(GLint x, GLint y, GLsizei
    width, GLsizei height, GLenum format, GLenum type, GLvoid *pixels)':
    names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glTexImage2D(GLenum target, GLint level,
    GLint internalformat, GLsizei width, GLsizei height, GLint border, GLenum
    format, GLenum type, const GLvoid *pixels)': names 'GLvoid', which has no
    cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glTexImage1D(GLenum target, GLint level,
    GLint internalformat, GLsizei width, GLint border, GLenum format, GLenum
    type, const GLvoid *pixels)': names 'GLvoid', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_1_5::glTexParameteriv(GLenum target, GLenum
    pname, const GLint *params)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glTexParameterfv(GLenum target, GLenum
    pname, const GLfloat *params)': names 'GLfloat', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_1_5::glIndexubv(const GLubyte *c)': names
    'GLubyte', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glGenTextures(GLsizei n, GLuint
    *textures)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_1_5::glDeleteTextures(GLsizei n, const GLuint
    *textures)': names 'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glTexSubImage2D(GLenum target, GLint
    level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height,
    GLenum format, GLenum type, const GLvoid *pixels)': names 'GLvoid', which
    has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glTexSubImage1D(GLenum target, GLint
    level, GLint xoffset, GLsizei width, GLenum format, GLenum type, const
    GLvoid *pixels)': names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glGetPointerv(GLenum pname, GLvoid
    **params)': takes a type Python has no way to hand over yet.
  - Qt's 'void QOpenGLFunctions_1_5::glDrawElements(GLenum mode, GLsizei
    count, GLenum type, const GLvoid *indices)': names 'GLvoid', which has no
    cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glTexSubImage3D(GLenum target, GLint
    level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width,
    GLsizei height, GLsizei depth, GLenum format, GLenum type, const GLvoid
    *pixels)': names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glTexImage3D(GLenum target, GLint level,
    GLint internalformat, GLsizei width, GLsizei height, GLsizei depth, GLint
    border, GLenum format, GLenum type, const GLvoid *pixels)': names
    'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glDrawRangeElements(GLenum mode, GLuint
    start, GLuint end, GLsizei count, GLenum type, const GLvoid *indices)':
    names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glGetCompressedTexImage(GLenum target,
    GLint level, GLvoid *img)': names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glCompressedTexSubImage1D(GLenum target,
    GLint level, GLint xoffset, GLsizei width, GLenum format, GLsizei
    imageSize, const GLvoid *data)': names 'GLvoid', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_1_5::glCompressedTexSubImage2D(GLenum target,
    GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height,
    GLenum format, GLsizei imageSize, const GLvoid *data)': names 'GLvoid',
    which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glCompressedTexSubImage3D(GLenum target,
    GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width,
    GLsizei height, GLsizei depth, GLenum format, GLsizei imageSize, const
    GLvoid *data)': names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glCompressedTexImage1D(GLenum target,
    GLint level, GLenum internalformat, GLsizei width, GLint border, GLsizei
    imageSize, const GLvoid *data)': names 'GLvoid', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_1_5::glCompressedTexImage2D(GLenum target,
    GLint level, GLenum internalformat, GLsizei width, GLsizei height, GLint
    border, GLsizei imageSize, const GLvoid *data)': names 'GLvoid', which
    has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glCompressedTexImage3D(GLenum target,
    GLint level, GLenum internalformat, GLsizei width, GLsizei height,
    GLsizei depth, GLint border, GLsizei imageSize, const GLvoid *data)':
    names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glPointParameteriv(GLenum pname, const
    GLint *params)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glPointParameterfv(GLenum pname, const
    GLfloat *params)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glMultiDrawElements(GLenum mode, const
    GLsizei *count, GLenum type, const GLvoid *const *indices, GLsizei
    drawcount)': names 'GLsizei', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glMultiDrawArrays(GLenum mode, const
    GLint *first, const GLsizei *count, GLsizei drawcount)': names 'GLint',
    which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glGetBufferPointerv(GLenum target,
    GLenum pname, GLvoid **params)': takes a type Python has no way to hand
    over yet.
  - Qt's 'void QOpenGLFunctions_1_5::glGetBufferParameteriv(GLenum target,
    GLenum pname, GLint *params)': takes a number to change where it is.
  - Qt's 'GLvoid *QOpenGLFunctions_1_5::glMapBuffer(GLenum target, GLenum
    access)': gives 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glGetBufferSubData(GLenum target,
    GLintptr offset, GLsizeiptr size, GLvoid *data)': names 'GLvoid', which
    has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glBufferSubData(GLenum target, GLintptr
    offset, GLsizeiptr size, const GLvoid *data)': names 'GLvoid', which has
    no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glBufferData(GLenum target, GLsizeiptr
    size, const GLvoid *data, GLenum usage)': names 'GLvoid', which has no
    cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glGenBuffers(GLsizei n, GLuint
    *buffers)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_1_5::glDeleteBuffers(GLsizei n, const GLuint
    *buffers)': names 'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glGetQueryObjectuiv(GLuint id, GLenum
    pname, GLuint *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_1_5::glGetQueryObjectiv(GLuint id, GLenum
    pname, GLint *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_1_5::glGetQueryiv(GLenum target, GLenum
    pname, GLint *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_1_5::glDeleteQueries(GLsizei n, const GLuint
    *ids)': names 'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glGenQueries(GLsizei n, GLuint *ids)':
    takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_1_5::glMultMatrixd(const GLdouble *m)': names
    'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glMultMatrixf(const GLfloat *m)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glLoadMatrixd(const GLdouble *m)': names
    'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glLoadMatrixf(const GLfloat *m)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glGetTexGeniv(GLenum coord, GLenum
    pname, GLint *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_1_5::glGetTexGenfv(GLenum coord, GLenum
    pname, GLfloat *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_1_5::glGetTexGendv(GLenum coord, GLenum
    pname, GLdouble *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_1_5::glGetTexEnviv(GLenum target, GLenum
    pname, GLint *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_1_5::glGetTexEnvfv(GLenum target, GLenum
    pname, GLfloat *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_1_5::glGetPolygonStipple(GLubyte *mask)':
    takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_1_5::glGetPixelMapusv(GLenum map, GLushort
    *values)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_1_5::glGetPixelMapuiv(GLenum map, GLuint
    *values)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_1_5::glGetPixelMapfv(GLenum map, GLfloat
    *values)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_1_5::glGetMaterialiv(GLenum face, GLenum
    pname, GLint *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_1_5::glGetMaterialfv(GLenum face, GLenum
    pname, GLfloat *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_1_5::glGetMapiv(GLenum target, GLenum query,
    GLint *v)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_1_5::glGetMapfv(GLenum target, GLenum query,
    GLfloat *v)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_1_5::glGetMapdv(GLenum target, GLenum query,
    GLdouble *v)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_1_5::glGetLightiv(GLenum light, GLenum pname,
    GLint *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_1_5::glGetLightfv(GLenum light, GLenum pname,
    GLfloat *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_1_5::glGetClipPlane(GLenum plane, GLdouble
    *equation)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_1_5::glDrawPixels(GLsizei width, GLsizei
    height, GLenum format, GLenum type, const GLvoid *pixels)': names
    'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glPixelMapusv(GLenum map, GLint mapsize,
    const GLushort *values)': names 'GLushort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glPixelMapuiv(GLenum map, GLint mapsize,
    const GLuint *values)': names 'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glPixelMapfv(GLenum map, GLint mapsize,
    const GLfloat *values)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glEvalCoord2fv(const GLfloat *u)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glEvalCoord2dv(const GLdouble *u)':
    names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glEvalCoord1fv(const GLfloat *u)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glEvalCoord1dv(const GLdouble *u)':
    names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glMap2f(GLenum target, GLfloat u1,
    GLfloat u2, GLint ustride, GLint uorder, GLfloat v1, GLfloat v2, GLint
    vstride, GLint vorder, const GLfloat *points)': names 'GLfloat', which
    has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glMap2d(GLenum target, GLdouble u1,
    GLdouble u2, GLint ustride, GLint uorder, GLdouble v1, GLdouble v2, GLint
    vstride, GLint vorder, const GLdouble *points)': names 'GLdouble', which
    has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glMap1f(GLenum target, GLfloat u1,
    GLfloat u2, GLint stride, GLint order, const GLfloat *points)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glMap1d(GLenum target, GLdouble u1,
    GLdouble u2, GLint stride, GLint order, const GLdouble *points)': names
    'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glSelectBuffer(GLsizei size, GLuint
    *buffer)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_1_5::glFeedbackBuffer(GLsizei size, GLenum
    type, GLfloat *buffer)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_1_5::glTexGeniv(GLenum coord, GLenum pname,
    const GLint *params)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glTexGenfv(GLenum coord, GLenum pname,
    const GLfloat *params)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glTexGendv(GLenum coord, GLenum pname,
    const GLdouble *params)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glTexEnviv(GLenum target, GLenum pname,
    const GLint *params)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glTexEnvfv(GLenum target, GLenum pname,
    const GLfloat *params)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glPolygonStipple(const GLubyte *mask)':
    names 'GLubyte', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glMaterialiv(GLenum face, GLenum pname,
    const GLint *params)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glMaterialfv(GLenum face, GLenum pname,
    const GLfloat *params)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glLightModeliv(GLenum pname, const GLint
    *params)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glLightModelfv(GLenum pname, const
    GLfloat *params)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glLightiv(GLenum light, GLenum pname,
    const GLint *params)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glLightfv(GLenum light, GLenum pname,
    const GLfloat *params)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glFogiv(GLenum pname, const GLint
    *params)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glFogfv(GLenum pname, const GLfloat
    *params)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glClipPlane(GLenum plane, const GLdouble
    *equation)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glVertex4sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glVertex4iv(const GLint *v)': names
    'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glVertex4fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glVertex4dv(const GLdouble *v)': names
    'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glVertex3sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glVertex3iv(const GLint *v)': names
    'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glVertex3fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glVertex3dv(const GLdouble *v)': names
    'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glVertex2sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glVertex2iv(const GLint *v)': names
    'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glVertex2fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glVertex2dv(const GLdouble *v)': names
    'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glTexCoord4sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glTexCoord4iv(const GLint *v)': names
    'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glTexCoord4fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glTexCoord4dv(const GLdouble *v)': names
    'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glTexCoord3sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glTexCoord3iv(const GLint *v)': names
    'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glTexCoord3fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glTexCoord3dv(const GLdouble *v)': names
    'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glTexCoord2sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glTexCoord2iv(const GLint *v)': names
    'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glTexCoord2fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glTexCoord2dv(const GLdouble *v)': names
    'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glTexCoord1sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glTexCoord1iv(const GLint *v)': names
    'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glTexCoord1fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glTexCoord1dv(const GLdouble *v)': names
    'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glRectsv(const GLshort *v1, const
    GLshort *v2)': names 'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glRectiv(const GLint *v1, const GLint
    *v2)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glRectfv(const GLfloat *v1, const
    GLfloat *v2)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glRectdv(const GLdouble *v1, const
    GLdouble *v2)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glRasterPos4sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glRasterPos4iv(const GLint *v)': names
    'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glRasterPos4fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glRasterPos4dv(const GLdouble *v)':
    names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glRasterPos3sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glRasterPos3iv(const GLint *v)': names
    'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glRasterPos3fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glRasterPos3dv(const GLdouble *v)':
    names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glRasterPos2sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glRasterPos2iv(const GLint *v)': names
    'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glRasterPos2fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glRasterPos2dv(const GLdouble *v)':
    names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glNormal3sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glNormal3iv(const GLint *v)': names
    'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glNormal3fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glNormal3dv(const GLdouble *v)': names
    'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glNormal3bv(const GLbyte *v)': names
    'GLbyte', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glIndexsv(const GLshort *c)': names
    'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glIndexiv(const GLint *c)': names
    'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glIndexfv(const GLfloat *c)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glIndexdv(const GLdouble *c)': names
    'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glEdgeFlagv(const GLboolean *flag)':
    names 'GLboolean', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glColor4usv(const GLushort *v)': names
    'GLushort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glColor4uiv(const GLuint *v)': names
    'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glColor4ubv(const GLubyte *v)': names
    'GLubyte', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glColor4sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glColor4iv(const GLint *v)': names
    'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glColor4fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glColor4dv(const GLdouble *v)': names
    'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glColor4bv(const GLbyte *v)': names
    'GLbyte', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glColor3usv(const GLushort *v)': names
    'GLushort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glColor3uiv(const GLuint *v)': names
    'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glColor3ubv(const GLubyte *v)': names
    'GLubyte', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glColor3sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glColor3iv(const GLint *v)': names
    'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glColor3fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glColor3dv(const GLdouble *v)': names
    'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glColor3bv(const GLbyte *v)': names
    'GLbyte', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glBitmap(GLsizei width, GLsizei height,
    GLfloat xorig, GLfloat yorig, GLfloat xmove, GLfloat ymove, const GLubyte
    *bitmap)': names 'GLubyte', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glCallLists(GLsizei n, GLenum type,
    const GLvoid *lists)': names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glPrioritizeTextures(GLsizei n, const
    GLuint *textures, const GLfloat *priorities)': names 'GLuint', which has
    no cute class yet.
  - Qt's 'GLboolean QOpenGLFunctions_1_5::glAreTexturesResident(GLsizei n,
    const GLuint *textures, GLboolean *residences)': names 'GLuint', which
    has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glVertexPointer(GLint size, GLenum type,
    GLsizei stride, const GLvoid *pointer)': names 'GLvoid', which has no
    cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glTexCoordPointer(GLint size, GLenum
    type, GLsizei stride, const GLvoid *pointer)': names 'GLvoid', which has
    no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glNormalPointer(GLenum type, GLsizei
    stride, const GLvoid *pointer)': names 'GLvoid', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_1_5::glInterleavedArrays(GLenum format,
    GLsizei stride, const GLvoid *pointer)': names 'GLvoid', which has no
    cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glIndexPointer(GLenum type, GLsizei
    stride, const GLvoid *pointer)': names 'GLvoid', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_1_5::glEdgeFlagPointer(GLsizei stride, const
    GLvoid *pointer)': names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glColorPointer(GLint size, GLenum type,
    GLsizei stride, const GLvoid *pointer)': names 'GLvoid', which has no
    cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glGetMinmaxParameteriv(GLenum target,
    GLenum pname, GLint *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_1_5::glGetMinmaxParameterfv(GLenum target,
    GLenum pname, GLfloat *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_1_5::glGetMinmax(GLenum target, GLboolean
    reset, GLenum format, GLenum type, GLvoid *values)': names 'GLvoid',
    which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glGetHistogramParameteriv(GLenum target,
    GLenum pname, GLint *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_1_5::glGetHistogramParameterfv(GLenum target,
    GLenum pname, GLfloat *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_1_5::glGetHistogram(GLenum target, GLboolean
    reset, GLenum format, GLenum type, GLvoid *values)': names 'GLvoid',
    which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glSeparableFilter2D(GLenum target,
    GLenum internalformat, GLsizei width, GLsizei height, GLenum format,
    GLenum type, const GLvoid *row, const GLvoid *column)': names 'GLvoid',
    which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glGetSeparableFilter(GLenum target,
    GLenum format, GLenum type, GLvoid *row, GLvoid *column, GLvoid *span)':
    names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glGetConvolutionParameteriv(GLenum
    target, GLenum pname, GLint *params)': takes a number to change where it
    is.
  - Qt's 'void QOpenGLFunctions_1_5::glGetConvolutionParameterfv(GLenum
    target, GLenum pname, GLfloat *params)': takes a number to change where
    it is.
  - Qt's 'void QOpenGLFunctions_1_5::glGetConvolutionFilter(GLenum target,
    GLenum format, GLenum type, GLvoid *image)': names 'GLvoid', which has no
    cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glConvolutionParameteriv(GLenum target,
    GLenum pname, const GLint *params)': names 'GLint', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glConvolutionParameterfv(GLenum target,
    GLenum pname, const GLfloat *params)': names 'GLfloat', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glConvolutionFilter2D(GLenum target,
    GLenum internalformat, GLsizei width, GLsizei height, GLenum format,
    GLenum type, const GLvoid *image)': names 'GLvoid', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glConvolutionFilter1D(GLenum target,
    GLenum internalformat, GLsizei width, GLenum format, GLenum type, const
    GLvoid *image)': names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glColorSubTable(GLenum target, GLsizei
    start, GLsizei count, GLenum format, GLenum type, const GLvoid *data)':
    names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glGetColorTableParameteriv(GLenum
    target, GLenum pname, GLint *params)': takes a number to change where it
    is.
  - Qt's 'void QOpenGLFunctions_1_5::glGetColorTableParameterfv(GLenum
    target, GLenum pname, GLfloat *params)': takes a number to change where
    it is.
  - Qt's 'void QOpenGLFunctions_1_5::glGetColorTable(GLenum target, GLenum
    format, GLenum type, GLvoid *table)': names 'GLvoid', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glColorTableParameteriv(GLenum target,
    GLenum pname, const GLint *params)': names 'GLint', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glColorTableParameterfv(GLenum target,
    GLenum pname, const GLfloat *params)': names 'GLfloat', which has no cute
    class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glColorTable(GLenum target, GLenum
    internalformat, GLsizei width, GLenum format, GLenum type, const GLvoid
    *table)': names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glMultTransposeMatrixd(const GLdouble
    *m)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glMultTransposeMatrixf(const GLfloat
    *m)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glLoadTransposeMatrixd(const GLdouble
    *m)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glLoadTransposeMatrixf(const GLfloat
    *m)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glMultiTexCoord4sv(GLenum target, const
    GLshort *v)': names 'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glMultiTexCoord4iv(GLenum target, const
    GLint *v)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glMultiTexCoord4fv(GLenum target, const
    GLfloat *v)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glMultiTexCoord4dv(GLenum target, const
    GLdouble *v)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glMultiTexCoord3sv(GLenum target, const
    GLshort *v)': names 'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glMultiTexCoord3iv(GLenum target, const
    GLint *v)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glMultiTexCoord3fv(GLenum target, const
    GLfloat *v)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glMultiTexCoord3dv(GLenum target, const
    GLdouble *v)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glMultiTexCoord2sv(GLenum target, const
    GLshort *v)': names 'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glMultiTexCoord2iv(GLenum target, const
    GLint *v)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glMultiTexCoord2fv(GLenum target, const
    GLfloat *v)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glMultiTexCoord2dv(GLenum target, const
    GLdouble *v)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glMultiTexCoord1sv(GLenum target, const
    GLshort *v)': names 'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glMultiTexCoord1iv(GLenum target, const
    GLint *v)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glMultiTexCoord1fv(GLenum target, const
    GLfloat *v)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glMultiTexCoord1dv(GLenum target, const
    GLdouble *v)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glWindowPos3sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glWindowPos3iv(const GLint *v)': names
    'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glWindowPos3fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glWindowPos3dv(const GLdouble *v)':
    names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glWindowPos2sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glWindowPos2iv(const GLint *v)': names
    'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glWindowPos2fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glWindowPos2dv(const GLdouble *v)':
    names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glSecondaryColorPointer(GLint size,
    GLenum type, GLsizei stride, const GLvoid *pointer)': names 'GLvoid',
    which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glSecondaryColor3usv(const GLushort
    *v)': names 'GLushort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glSecondaryColor3uiv(const GLuint *v)':
    names 'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glSecondaryColor3ubv(const GLubyte *v)':
    names 'GLubyte', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glSecondaryColor3sv(const GLshort *v)':
    names 'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glSecondaryColor3iv(const GLint *v)':
    names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glSecondaryColor3fv(const GLfloat *v)':
    names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glSecondaryColor3dv(const GLdouble *v)':
    names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glSecondaryColor3bv(const GLbyte *v)':
    names 'GLbyte', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glFogCoordPointer(GLenum type, GLsizei
    stride, const GLvoid *pointer)': names 'GLvoid', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_1_5::glFogCoorddv(const GLdouble *coord)':
    names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_5::glFogCoordfv(const GLfloat *coord)':
    names 'GLfloat', which has no cute class yet.

  What to expect
  --------------

  - The C++ QOpenGLFunctions_1_5 is created at the first use, not by
    'QOpenGLFunctions_1_5(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QOpenGLFunctions_1_5.
  - Each name of Qt's QOpenGLFunctions_1_5 that has no cute function yet,
    'glAreTexturesResident', 'glBitmap', 'glBufferData', 'glBufferSubData',
    'glCallLists', 'glClipPlane', 'glColor3bv', 'glColor3dv', 'glColor3fv',
    'glColor3iv', 'glColor3sv', 'glColor3ubv', 'glColor3uiv', 'glColor3usv',
    'glColor4bv', 'glColor4dv', 'glColor4fv', 'glColor4iv', 'glColor4sv',
    'glColor4ubv', 'glColor4uiv', 'glColor4usv', 'glColorPointer',
    'glColorSubTable', 'glColorTable', 'glColorTableParameterfv',
    'glColorTableParameteriv', 'glCompressedTexImage1D',
    'glCompressedTexImage2D', 'glCompressedTexImage3D',
    'glCompressedTexSubImage1D', 'glCompressedTexSubImage2D',
    'glCompressedTexSubImage3D', 'glConvolutionFilter1D',
    'glConvolutionFilter2D', 'glConvolutionParameterfv',
    'glConvolutionParameteriv', 'glDeleteBuffers', 'glDeleteQueries',
    'glDeleteTextures', 'glDrawElements', 'glDrawPixels',
    'glDrawRangeElements', 'glEdgeFlagPointer', 'glEdgeFlagv',
    'glEvalCoord1dv', 'glEvalCoord1fv', 'glEvalCoord2dv', 'glEvalCoord2fv',
    'glFeedbackBuffer', 'glFogCoordPointer', 'glFogCoorddv', 'glFogCoordfv',
    'glFogfv', 'glFogiv', 'glGenBuffers', 'glGenQueries', 'glGenTextures',
    'glGetBooleanv', 'glGetBufferParameteriv', 'glGetBufferPointerv',
    'glGetBufferSubData', 'glGetClipPlane', 'glGetColorTable',
    'glGetColorTableParameterfv', 'glGetColorTableParameteriv',
    'glGetCompressedTexImage', 'glGetConvolutionFilter',
    'glGetConvolutionParameterfv', 'glGetConvolutionParameteriv',
    'glGetDoublev', 'glGetFloatv', 'glGetHistogram',
    'glGetHistogramParameterfv', 'glGetHistogramParameteriv',
    'glGetIntegerv', 'glGetLightfv', 'glGetLightiv', 'glGetMapdv',
    'glGetMapfv', 'glGetMapiv', 'glGetMaterialfv', 'glGetMaterialiv',
    'glGetMinmax', 'glGetMinmaxParameterfv', 'glGetMinmaxParameteriv',
    'glGetPixelMapfv', 'glGetPixelMapuiv', 'glGetPixelMapusv',
    'glGetPointerv', 'glGetPolygonStipple', 'glGetQueryObjectiv',
    'glGetQueryObjectuiv', 'glGetQueryiv', 'glGetSeparableFilter',
    'glGetString', 'glGetTexEnvfv', 'glGetTexEnviv', 'glGetTexGendv',
    'glGetTexGenfv', 'glGetTexGeniv', 'glGetTexImage',
    'glGetTexLevelParameterfv', 'glGetTexLevelParameteriv',
    'glGetTexParameterfv', 'glGetTexParameteriv', 'glIndexPointer',
    'glIndexdv', 'glIndexfv', 'glIndexiv', 'glIndexsv', 'glIndexubv',
    'glInterleavedArrays', 'glLightModelfv', 'glLightModeliv', 'glLightfv',
    'glLightiv', 'glLoadMatrixd', 'glLoadMatrixf', 'glLoadTransposeMatrixd',
    'glLoadTransposeMatrixf', 'glMap1d', 'glMap1f', 'glMap2d', 'glMap2f',
    'glMapBuffer', 'glMaterialfv', 'glMaterialiv', 'glMultMatrixd',
    'glMultMatrixf', 'glMultTransposeMatrixd', 'glMultTransposeMatrixf',
    'glMultiDrawArrays', 'glMultiDrawElements', 'glMultiTexCoord1dv',
    'glMultiTexCoord1fv', 'glMultiTexCoord1iv', 'glMultiTexCoord1sv',
    'glMultiTexCoord2dv', 'glMultiTexCoord2fv', 'glMultiTexCoord2iv',
    'glMultiTexCoord2sv', 'glMultiTexCoord3dv', 'glMultiTexCoord3fv',
    'glMultiTexCoord3iv', 'glMultiTexCoord3sv', 'glMultiTexCoord4dv',
    'glMultiTexCoord4fv', 'glMultiTexCoord4iv', 'glMultiTexCoord4sv',
    'glNormal3bv', 'glNormal3dv', 'glNormal3fv', 'glNormal3iv',
    'glNormal3sv', 'glNormalPointer', 'glPixelMapfv', 'glPixelMapuiv',
    'glPixelMapusv', 'glPointParameterfv', 'glPointParameteriv',
    'glPolygonStipple', 'glPrioritizeTextures', 'glRasterPos2dv',
    'glRasterPos2fv', 'glRasterPos2iv', 'glRasterPos2sv', 'glRasterPos3dv',
    'glRasterPos3fv', 'glRasterPos3iv', 'glRasterPos3sv', 'glRasterPos4dv',
    'glRasterPos4fv', 'glRasterPos4iv', 'glRasterPos4sv', 'glReadPixels',
    'glRectdv', 'glRectfv', 'glRectiv', 'glRectsv', 'glSecondaryColor3bv',
    'glSecondaryColor3dv', 'glSecondaryColor3fv', 'glSecondaryColor3iv',
    'glSecondaryColor3sv', 'glSecondaryColor3ubv', 'glSecondaryColor3uiv',
    'glSecondaryColor3usv', 'glSecondaryColorPointer', 'glSelectBuffer',
    'glSeparableFilter2D', 'glTexCoord1dv', 'glTexCoord1fv', 'glTexCoord1iv',
    'glTexCoord1sv', 'glTexCoord2dv', 'glTexCoord2fv', 'glTexCoord2iv',
    'glTexCoord2sv', 'glTexCoord3dv', 'glTexCoord3fv', 'glTexCoord3iv',
    'glTexCoord3sv', 'glTexCoord4dv', 'glTexCoord4fv', 'glTexCoord4iv',
    'glTexCoord4sv', 'glTexCoordPointer', 'glTexEnvfv', 'glTexEnviv',
    'glTexGendv', 'glTexGenfv', 'glTexGeniv', 'glTexImage1D', 'glTexImage2D',
    'glTexImage3D', 'glTexParameterfv', 'glTexParameteriv',
    'glTexSubImage1D', 'glTexSubImage2D', 'glTexSubImage3D', 'glVertex2dv',
    'glVertex2fv', 'glVertex2iv', 'glVertex2sv', 'glVertex3dv',
    'glVertex3fv', 'glVertex3iv', 'glVertex3sv', 'glVertex4dv',
    'glVertex4fv', 'glVertex4iv', 'glVertex4sv', 'glVertexPointer',
    'glWindowPos2dv', 'glWindowPos2fv', 'glWindowPos2iv', 'glWindowPos2sv',
    'glWindowPos3dv', 'glWindowPos3fv', 'glWindowPos3iv', 'glWindowPos3sv',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QOpenGLContext)
  @overload(NoneType)
  def isContextCompatible(context: Optional[QOpenGLContext]) -> bool:
    """
    Calls Qt's 'bool QOpenGLFunctions_1_5::isContextCompatible(QOpenGLContext
    *context)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#isContextCompatible

    Parameters
    ----------

    context : Optional[QOpenGLContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QOpenGLFunctions_1_5::isContextCompatible(QOpenGLContext
    #      *context)
    return Rituals.call(
        'ritual_ZN20QOpenGLFunctions_1_519isContextCompatibleEP14QOpenGLCon'
        'text',
        CuteMixin._addressOf(context),
    )

  @staticmethod
  def versionProfile() -> QOpenGLVersionProfile:
    """
    Calls Qt's 'QOpenGLVersionProfile
    QOpenGLFunctions_1_5::versionProfile()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#versionProfile

    Returns
    -------

    QOpenGLVersionProfile
      A new cute QOpenGLVersionProfile around the copy Qt gave back. Python
      owns it.
    """
    #  QOpenGLVersionProfile QOpenGLFunctions_1_5::versionProfile()
    address = Rituals.call(
        'ritual_ZN20QOpenGLFunctions_1_514versionProfileEv',
    )
    from . import QOpenGLVersionProfile
    return QOpenGLVersionProfile._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpenGLFunctions_1_5'

  #  A C++ QOpenGLFunctions_1_5 Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QOpenGLFunctions_1_5'

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
    'QOpenGLFunctions_1_5::QOpenGLFunctions_1_5()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#QOpenGLFunctions_1_5
    """
    #  QOpenGLFunctions_1_5::QOpenGLFunctions_1_5()
    self._noteCreation(QOpenGLFunctions_1_5, lambda: Rituals.call(
        'ritual_ZN20QOpenGLFunctions_1_5C1Ev',
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
    Calls Qt's 'bool QOpenGLFunctions_1_5::initializeOpenGLFunctions()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html
    """
    #  bool QOpenGLFunctions_1_5::initializeOpenGLFunctions()
    ritual = 'ritual_ZN20QOpenGLFunctions_1_525initializeOpenGLFunctionsEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QOpenGLFunctions_1_525initializeOpenGLFunctionsEv')
    return self.uglySide.call(ritual)

  @overload(int, int, int, int)
  def glViewport(self, x: int, y: int, width: int, height: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glViewport(GLint x, GLint y,
    GLsizei width, GLsizei height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glViewport

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
    #  void QOpenGLFunctions_1_5::glViewport(GLint x, GLint y, GLsizei width,
    #      GLsizei height)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_510glViewportEiiii',
        x, y, width, height,
    )

  @overload(float, float)
  def glDepthRange(self, nearVal: float, farVal: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glDepthRange(GLdouble nearVal,
    GLdouble farVal)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glDepthRange

    Parameters
    ----------

    nearVal : float
      Passed on as it is.

    farVal : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glDepthRange(GLdouble nearVal, GLdouble
    #      farVal)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_512glDepthRangeEdd', nearVal, farVal,
    )

  @overload(int)
  def glIsEnabled(self, cap: int) -> int:
    """
    Calls Qt's 'GLboolean QOpenGLFunctions_1_5::glIsEnabled(GLenum cap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glIsEnabled

    Parameters
    ----------

    cap : int
      Passed on as it is.
    """
    #  GLboolean QOpenGLFunctions_1_5::glIsEnabled(GLenum cap)
    return self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_511glIsEnabledEj', cap,
    )

  def glGetError(self) -> int:
    """
    Calls Qt's 'GLenum QOpenGLFunctions_1_5::glGetError()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glGetError
    """
    #  GLenum QOpenGLFunctions_1_5::glGetError()
    return self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_510glGetErrorEv',
    )

  @overload(int)
  def glReadBuffer(self, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glReadBuffer(GLenum mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glReadBuffer

    Parameters
    ----------

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glReadBuffer(GLenum mode)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_512glReadBufferEj', mode,
    )

  @overload(int, int)
  def glPixelStorei(self, pname: int, param: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glPixelStorei(GLenum pname, GLint
    param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glPixelStorei

    Parameters
    ----------

    pname : int
      Passed on as it is.

    param : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glPixelStorei(GLenum pname, GLint param)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_513glPixelStoreiEji', pname, param,
    )

  @overload(int, float)
  def glPixelStoref(self, pname: int, param: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glPixelStoref(GLenum pname,
    GLfloat param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glPixelStoref

    Parameters
    ----------

    pname : int
      Passed on as it is.

    param : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glPixelStoref(GLenum pname, GLfloat param)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_513glPixelStorefEjf', pname, param,
    )

  @overload(int)
  def glDepthFunc(self, func: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glDepthFunc(GLenum func)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glDepthFunc

    Parameters
    ----------

    func : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glDepthFunc(GLenum func)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_511glDepthFuncEj', func,
    )

  @overload(int, int, int)
  def glStencilOp(self, fail: int, zfail: int, zpass: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glStencilOp(GLenum fail, GLenum
    zfail, GLenum zpass)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glStencilOp

    Parameters
    ----------

    fail : int
      Passed on as it is.

    zfail : int
      Passed on as it is.

    zpass : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glStencilOp(GLenum fail, GLenum zfail,
    #      GLenum zpass)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_511glStencilOpEjjj',
        fail, zfail, zpass,
    )

  @overload(int, int, int)
  def glStencilFunc(self, func: int, ref: int, mask: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glStencilFunc(GLenum func, GLint
    ref, GLuint mask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glStencilFunc

    Parameters
    ----------

    func : int
      Passed on as it is.

    ref : int
      Passed on as it is.

    mask : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glStencilFunc(GLenum func, GLint ref,
    #      GLuint mask)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_513glStencilFuncEjij',
        func, ref, mask,
    )

  @overload(int)
  def glLogicOp(self, opcode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glLogicOp(GLenum opcode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glLogicOp

    Parameters
    ----------

    opcode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glLogicOp(GLenum opcode)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_1_59glLogicOpEj', opcode)

  @overload(int, int)
  def glBlendFunc(self, sfactor: int, dfactor: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glBlendFunc(GLenum sfactor, GLenum
    dfactor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glBlendFunc

    Parameters
    ----------

    sfactor : int
      Passed on as it is.

    dfactor : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glBlendFunc(GLenum sfactor, GLenum dfactor)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_511glBlendFuncEjj', sfactor, dfactor,
    )

  def glFlush(self) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glFlush()'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glFlush
    """
    #  void QOpenGLFunctions_1_5::glFlush()
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_1_57glFlushEv')

  def glFinish(self) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glFinish()'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glFinish
    """
    #  void QOpenGLFunctions_1_5::glFinish()
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_1_58glFinishEv')

  @overload(int)
  def glEnable(self, cap: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glEnable(GLenum cap)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glEnable

    Parameters
    ----------

    cap : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glEnable(GLenum cap)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_1_58glEnableEj', cap)

  @overload(int)
  def glDisable(self, cap: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glDisable(GLenum cap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glDisable

    Parameters
    ----------

    cap : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glDisable(GLenum cap)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_1_59glDisableEj', cap)

  @overload(int)
  def glDepthMask(self, flag: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glDepthMask(GLboolean flag)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glDepthMask

    Parameters
    ----------

    flag : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glDepthMask(GLboolean flag)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_511glDepthMaskEh', flag,
    )

  @overload(int, int, int, int)
  def glColorMask(self, red: int, green: int, blue: int, alpha: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glColorMask(GLboolean red,
    GLboolean green, GLboolean blue, GLboolean alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glColorMask

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
    #  void QOpenGLFunctions_1_5::glColorMask(GLboolean red, GLboolean green,
    #      GLboolean blue, GLboolean alpha)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_511glColorMaskEhhhh',
        red, green, blue, alpha,
    )

  @overload(int)
  def glStencilMask(self, mask: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glStencilMask(GLuint mask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glStencilMask

    Parameters
    ----------

    mask : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glStencilMask(GLuint mask)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_513glStencilMaskEj', mask,
    )

  @overload(float)
  def glClearDepth(self, depth: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glClearDepth(GLdouble depth)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glClearDepth

    Parameters
    ----------

    depth : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glClearDepth(GLdouble depth)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_512glClearDepthEd', depth,
    )

  @overload(int)
  def glClearStencil(self, s: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glClearStencil(GLint s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glClearStencil

    Parameters
    ----------

    s : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glClearStencil(GLint s)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_514glClearStencilEi', s,
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
    Calls Qt's 'void QOpenGLFunctions_1_5::glClearColor(GLfloat red, GLfloat
    green, GLfloat blue, GLfloat alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glClearColor

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
    #  void QOpenGLFunctions_1_5::glClearColor(GLfloat red, GLfloat green,
    #      GLfloat blue, GLfloat alpha)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_512glClearColorEffff',
        red, green, blue, alpha,
    )

  @overload(int)
  def glClear(self, mask: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glClear(GLbitfield mask)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glClear

    Parameters
    ----------

    mask : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glClear(GLbitfield mask)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_1_57glClearEj', mask)

  @overload(int)
  def glDrawBuffer(self, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glDrawBuffer(GLenum mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glDrawBuffer

    Parameters
    ----------

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glDrawBuffer(GLenum mode)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_512glDrawBufferEj', mode,
    )

  @overload(int, int, int)
  def glTexParameteri(self, target: int, pname: int, param: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glTexParameteri(GLenum target,
    GLenum pname, GLint param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glTexParameteri

    Parameters
    ----------

    target : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    param : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glTexParameteri(GLenum target, GLenum
    #      pname, GLint param)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_515glTexParameteriEjji',
        target, pname, param,
    )

  @overload(int, int, float)
  def glTexParameterf(self, target: int, pname: int, param: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glTexParameterf(GLenum target,
    GLenum pname, GLfloat param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glTexParameterf

    Parameters
    ----------

    target : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    param : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glTexParameterf(GLenum target, GLenum
    #      pname, GLfloat param)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_515glTexParameterfEjjf',
        target, pname, param,
    )

  @overload(int, int, int, int)
  def glScissor(self, x: int, y: int, width: int, height: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glScissor(GLint x, GLint y,
    GLsizei width, GLsizei height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glScissor

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
    #  void QOpenGLFunctions_1_5::glScissor(GLint x, GLint y, GLsizei width,
    #      GLsizei height)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_59glScissorEiiii',
        x, y, width, height,
    )

  @overload(int, int)
  def glPolygonMode(self, face: int, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glPolygonMode(GLenum face, GLenum
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glPolygonMode

    Parameters
    ----------

    face : int
      Passed on as it is.

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glPolygonMode(GLenum face, GLenum mode)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_513glPolygonModeEjj', face, mode,
    )

  @overload(float)
  def glPointSize(self, size: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glPointSize(GLfloat size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glPointSize

    Parameters
    ----------

    size : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glPointSize(GLfloat size)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_511glPointSizeEf', size,
    )

  @overload(float)
  def glLineWidth(self, width: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glLineWidth(GLfloat width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glLineWidth

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glLineWidth(GLfloat width)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_511glLineWidthEf', width,
    )

  @overload(int, int)
  def glHint(self, target: int, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glHint(GLenum target, GLenum
    mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glHint

    Parameters
    ----------

    target : int
      Passed on as it is.

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glHint(GLenum target, GLenum mode)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_56glHintEjj', target, mode,
    )

  @overload(int)
  def glFrontFace(self, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glFrontFace(GLenum mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glFrontFace

    Parameters
    ----------

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glFrontFace(GLenum mode)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_511glFrontFaceEj', mode,
    )

  @overload(int)
  def glCullFace(self, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glCullFace(GLenum mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glCullFace

    Parameters
    ----------

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glCullFace(GLenum mode)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_1_510glCullFaceEj', mode)

  @overload(int)
  def glIndexub(self, c: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glIndexub(GLubyte c)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glIndexub

    Parameters
    ----------

    c : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glIndexub(GLubyte c)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_1_59glIndexubEh', c)

  @overload(int)
  def glIsTexture(self, texture: int) -> int:
    """
    Calls Qt's 'GLboolean QOpenGLFunctions_1_5::glIsTexture(GLuint texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glIsTexture

    Parameters
    ----------

    texture : int
      Passed on as it is.
    """
    #  GLboolean QOpenGLFunctions_1_5::glIsTexture(GLuint texture)
    return self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_511glIsTextureEj', texture,
    )

  @overload(int, int)
  def glBindTexture(self, target: int, texture: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glBindTexture(GLenum target,
    GLuint texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glBindTexture

    Parameters
    ----------

    target : int
      Passed on as it is.

    texture : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glBindTexture(GLenum target, GLuint
    #      texture)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_513glBindTextureEjj', target, texture,
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
    Calls Qt's 'void QOpenGLFunctions_1_5::glCopyTexSubImage2D(GLenum target,
    GLint level, GLint xoffset, GLint yoffset, GLint x, GLint y, GLsizei
    width, GLsizei height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glCopyTexSubImage2D

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
    #  void QOpenGLFunctions_1_5::glCopyTexSubImage2D(GLenum target, GLint
    #      level, GLint xoffset, GLint yoffset, GLint x, GLint y, GLsizei
    #      width, GLsizei height)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_519glCopyTexSubImage2DEjiiiiiii',
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
    Calls Qt's 'void QOpenGLFunctions_1_5::glCopyTexSubImage1D(GLenum target,
    GLint level, GLint xoffset, GLint x, GLint y, GLsizei width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glCopyTexSubImage1D

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
    #  void QOpenGLFunctions_1_5::glCopyTexSubImage1D(GLenum target, GLint
    #      level, GLint xoffset, GLint x, GLint y, GLsizei width)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_519glCopyTexSubImage1DEjiiiii',
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
    Calls Qt's 'void QOpenGLFunctions_1_5::glCopyTexImage2D(GLenum target,
    GLint level, GLenum internalformat, GLint x, GLint y, GLsizei width,
    GLsizei height, GLint border)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glCopyTexImage2D

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
    #  void QOpenGLFunctions_1_5::glCopyTexImage2D(GLenum target, GLint
    #      level, GLenum internalformat, GLint x, GLint y, GLsizei width,
    #      GLsizei height, GLint border)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_516glCopyTexImage2DEjijiiiii',
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
    Calls Qt's 'void QOpenGLFunctions_1_5::glCopyTexImage1D(GLenum target,
    GLint level, GLenum internalformat, GLint x, GLint y, GLsizei width,
    GLint border)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glCopyTexImage1D

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
    #  void QOpenGLFunctions_1_5::glCopyTexImage1D(GLenum target, GLint
    #      level, GLenum internalformat, GLint x, GLint y, GLsizei width,
    #      GLint border)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_516glCopyTexImage1DEjijiiii',
        target, level, internalformat, x, y, width, border,
    )

  @overload(float, float)
  def glPolygonOffset(self, factor: float, units: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glPolygonOffset(GLfloat factor,
    GLfloat units)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glPolygonOffset

    Parameters
    ----------

    factor : float
      Passed on as it is.

    units : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glPolygonOffset(GLfloat factor, GLfloat
    #      units)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_515glPolygonOffsetEff', factor, units,
    )

  @overload(int, int, int)
  def glDrawArrays(self, mode: int, first: int, count: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glDrawArrays(GLenum mode, GLint
    first, GLsizei count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glDrawArrays

    Parameters
    ----------

    mode : int
      Passed on as it is.

    first : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glDrawArrays(GLenum mode, GLint first,
    #      GLsizei count)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_512glDrawArraysEjii',
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
    Calls Qt's 'void QOpenGLFunctions_1_5::glCopyTexSubImage3D(GLenum target,
    GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLint x, GLint
    y, GLsizei width, GLsizei height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glCopyTexSubImage3D

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
    #  void QOpenGLFunctions_1_5::glCopyTexSubImage3D(GLenum target, GLint
    #      level, GLint xoffset, GLint yoffset, GLint zoffset, GLint x, GLint
    #      y, GLsizei width, GLsizei height)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_519glCopyTexSubImage3DEjiiiiiiii',
        target, level, xoffset, yoffset, zoffset, x, y, width, height,
    )

  @overload(int)
  def glBlendEquation(self, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glBlendEquation(GLenum mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glBlendEquation

    Parameters
    ----------

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glBlendEquation(GLenum mode)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_515glBlendEquationEj', mode,
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
    Calls Qt's 'void QOpenGLFunctions_1_5::glBlendColor(GLfloat red, GLfloat
    green, GLfloat blue, GLfloat alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glBlendColor

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
    #  void QOpenGLFunctions_1_5::glBlendColor(GLfloat red, GLfloat green,
    #      GLfloat blue, GLfloat alpha)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_512glBlendColorEffff',
        red, green, blue, alpha,
    )

  @overload(float, int)
  def glSampleCoverage(self, value: float, invert: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glSampleCoverage(GLfloat value,
    GLboolean invert)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glSampleCoverage

    Parameters
    ----------

    value : float
      Passed on as it is.

    invert : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glSampleCoverage(GLfloat value, GLboolean
    #      invert)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_516glSampleCoverageEfh',
        value, invert,
    )

  @overload(int)
  def glActiveTexture(self, texture: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glActiveTexture(GLenum texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glActiveTexture

    Parameters
    ----------

    texture : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glActiveTexture(GLenum texture)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_515glActiveTextureEj', texture,
    )

  @overload(int, int)
  def glPointParameteri(self, pname: int, param: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glPointParameteri(GLenum pname,
    GLint param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glPointParameteri

    Parameters
    ----------

    pname : int
      Passed on as it is.

    param : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glPointParameteri(GLenum pname, GLint
    #      param)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_517glPointParameteriEji',
        pname, param,
    )

  @overload(int, float)
  def glPointParameterf(self, pname: int, param: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glPointParameterf(GLenum pname,
    GLfloat param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glPointParameterf

    Parameters
    ----------

    pname : int
      Passed on as it is.

    param : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glPointParameterf(GLenum pname, GLfloat
    #      param)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_517glPointParameterfEjf',
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
    Calls Qt's 'void QOpenGLFunctions_1_5::glBlendFuncSeparate(GLenum
    sfactorRGB, GLenum dfactorRGB, GLenum sfactorAlpha, GLenum
    dfactorAlpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glBlendFuncSeparate

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
    #  void QOpenGLFunctions_1_5::glBlendFuncSeparate(GLenum sfactorRGB,
    #      GLenum dfactorRGB, GLenum sfactorAlpha, GLenum dfactorAlpha)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_519glBlendFuncSeparateEjjjj',
        sfactorRGB, dfactorRGB, sfactorAlpha, dfactorAlpha,
    )

  @overload(int)
  def glUnmapBuffer(self, target: int) -> int:
    """
    Calls Qt's 'GLboolean QOpenGLFunctions_1_5::glUnmapBuffer(GLenum
    target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glUnmapBuffer

    Parameters
    ----------

    target : int
      Passed on as it is.
    """
    #  GLboolean QOpenGLFunctions_1_5::glUnmapBuffer(GLenum target)
    return self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_513glUnmapBufferEj', target,
    )

  @overload(int)
  def glIsBuffer(self, buffer: int) -> int:
    """
    Calls Qt's 'GLboolean QOpenGLFunctions_1_5::glIsBuffer(GLuint buffer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glIsBuffer

    Parameters
    ----------

    buffer : int
      Passed on as it is.
    """
    #  GLboolean QOpenGLFunctions_1_5::glIsBuffer(GLuint buffer)
    return self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_510glIsBufferEj', buffer,
    )

  @overload(int, int)
  def glBindBuffer(self, target: int, buffer: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glBindBuffer(GLenum target, GLuint
    buffer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glBindBuffer

    Parameters
    ----------

    target : int
      Passed on as it is.

    buffer : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glBindBuffer(GLenum target, GLuint buffer)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_512glBindBufferEjj', target, buffer,
    )

  @overload(int)
  def glEndQuery(self, target: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glEndQuery(GLenum target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glEndQuery

    Parameters
    ----------

    target : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glEndQuery(GLenum target)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_510glEndQueryEj', target,
    )

  @overload(int, int)
  def glBeginQuery(self, target: int, id: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glBeginQuery(GLenum target, GLuint
    id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glBeginQuery

    Parameters
    ----------

    target : int
      Passed on as it is.

    id : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glBeginQuery(GLenum target, GLuint id)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_512glBeginQueryEjj', target, id,
    )

  @overload(int)
  def glIsQuery(self, id: int) -> int:
    """
    Calls Qt's 'GLboolean QOpenGLFunctions_1_5::glIsQuery(GLuint id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glIsQuery

    Parameters
    ----------

    id : int
      Passed on as it is.
    """
    #  GLboolean QOpenGLFunctions_1_5::glIsQuery(GLuint id)
    return self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_59glIsQueryEj', id,
    )

  @overload(float, float, float)
  def glTranslatef(self, x: float, y: float, z: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glTranslatef(GLfloat x, GLfloat y,
    GLfloat z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glTranslatef

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glTranslatef(GLfloat x, GLfloat y, GLfloat
    #      z)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_512glTranslatefEfff', x, y, z,
    )

  @overload(float, float, float)
  def glTranslated(self, x: float, y: float, z: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glTranslated(GLdouble x, GLdouble
    y, GLdouble z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glTranslated

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glTranslated(GLdouble x, GLdouble y,
    #      GLdouble z)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_512glTranslatedEddd', x, y, z,
    )

  @overload(float, float, float)
  def glScalef(self, x: float, y: float, z: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glScalef(GLfloat x, GLfloat y,
    GLfloat z)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glScalef

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glScalef(GLfloat x, GLfloat y, GLfloat z)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_58glScalefEfff', x, y, z,
    )

  @overload(float, float, float)
  def glScaled(self, x: float, y: float, z: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glScaled(GLdouble x, GLdouble y,
    GLdouble z)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glScaled

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glScaled(GLdouble x, GLdouble y, GLdouble
    #      z)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_58glScaledEddd', x, y, z,
    )

  @overload(float, float, float, float)
  def glRotatef(self, angle: float, x: float, y: float, z: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glRotatef(GLfloat angle, GLfloat
    x, GLfloat y, GLfloat z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glRotatef

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
    #  void QOpenGLFunctions_1_5::glRotatef(GLfloat angle, GLfloat x, GLfloat
    #      y, GLfloat z)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_59glRotatefEffff', angle, x, y, z,
    )

  @overload(float, float, float, float)
  def glRotated(self, angle: float, x: float, y: float, z: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glRotated(GLdouble angle, GLdouble
    x, GLdouble y, GLdouble z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glRotated

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
    #  void QOpenGLFunctions_1_5::glRotated(GLdouble angle, GLdouble x,
    #      GLdouble y, GLdouble z)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_59glRotatedEdddd', angle, x, y, z,
    )

  def glPushMatrix(self) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glPushMatrix()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glPushMatrix
    """
    #  void QOpenGLFunctions_1_5::glPushMatrix()
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_1_512glPushMatrixEv')

  def glPopMatrix(self) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glPopMatrix()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glPopMatrix
    """
    #  void QOpenGLFunctions_1_5::glPopMatrix()
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_1_511glPopMatrixEv')

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
    Calls Qt's 'void QOpenGLFunctions_1_5::glOrtho(GLdouble left, GLdouble
    right, GLdouble bottom, GLdouble top, GLdouble zNear, GLdouble zFar)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glOrtho

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
    #  void QOpenGLFunctions_1_5::glOrtho(GLdouble left, GLdouble right,
    #      GLdouble bottom, GLdouble top, GLdouble zNear, GLdouble zFar)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_57glOrthoEdddddd',
        left, right, bottom, top, zNear, zFar,
    )

  @overload(int)
  def glMatrixMode(self, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glMatrixMode(GLenum mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glMatrixMode

    Parameters
    ----------

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glMatrixMode(GLenum mode)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_512glMatrixModeEj', mode,
    )

  def glLoadIdentity(self) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glLoadIdentity()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glLoadIdentity
    """
    #  void QOpenGLFunctions_1_5::glLoadIdentity()
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_1_514glLoadIdentityEv')

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
    Calls Qt's 'void QOpenGLFunctions_1_5::glFrustum(GLdouble left, GLdouble
    right, GLdouble bottom, GLdouble top, GLdouble zNear, GLdouble zFar)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glFrustum

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
    #  void QOpenGLFunctions_1_5::glFrustum(GLdouble left, GLdouble right,
    #      GLdouble bottom, GLdouble top, GLdouble zNear, GLdouble zFar)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_59glFrustumEdddddd',
        left, right, bottom, top, zNear, zFar,
    )

  @overload(int)
  def glIsList(self, list: int) -> int:
    """
    Calls Qt's 'GLboolean QOpenGLFunctions_1_5::glIsList(GLuint list)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glIsList

    Parameters
    ----------

    list : int
      Passed on as it is.
    """
    #  GLboolean QOpenGLFunctions_1_5::glIsList(GLuint list)
    return self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_58glIsListEj', list,
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
    Calls Qt's 'void QOpenGLFunctions_1_5::glCopyPixels(GLint x, GLint y,
    GLsizei width, GLsizei height, GLenum type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glCopyPixels

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
    #  void QOpenGLFunctions_1_5::glCopyPixels(GLint x, GLint y, GLsizei
    #      width, GLsizei height, GLenum type)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_512glCopyPixelsEiiiij',
        x, y, width, height, type,
    )

  @overload(int, int)
  def glPixelTransferi(self, pname: int, param: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glPixelTransferi(GLenum pname,
    GLint param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glPixelTransferi

    Parameters
    ----------

    pname : int
      Passed on as it is.

    param : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glPixelTransferi(GLenum pname, GLint param)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_516glPixelTransferiEji', pname, param,
    )

  @overload(int, float)
  def glPixelTransferf(self, pname: int, param: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glPixelTransferf(GLenum pname,
    GLfloat param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glPixelTransferf

    Parameters
    ----------

    pname : int
      Passed on as it is.

    param : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glPixelTransferf(GLenum pname, GLfloat
    #      param)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_516glPixelTransferfEjf', pname, param,
    )

  @overload(float, float)
  def glPixelZoom(self, xfactor: float, yfactor: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glPixelZoom(GLfloat xfactor,
    GLfloat yfactor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glPixelZoom

    Parameters
    ----------

    xfactor : float
      Passed on as it is.

    yfactor : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glPixelZoom(GLfloat xfactor, GLfloat
    #      yfactor)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_511glPixelZoomEff', xfactor, yfactor,
    )

  @overload(int, float)
  def glAlphaFunc(self, func: int, ref: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glAlphaFunc(GLenum func, GLfloat
    ref)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glAlphaFunc

    Parameters
    ----------

    func : int
      Passed on as it is.

    ref : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glAlphaFunc(GLenum func, GLfloat ref)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_511glAlphaFuncEjf', func, ref,
    )

  @overload(int, int)
  def glEvalPoint2(self, i: int, j: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glEvalPoint2(GLint i, GLint j)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glEvalPoint2

    Parameters
    ----------

    i : int
      Passed on as it is.

    j : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glEvalPoint2(GLint i, GLint j)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_512glEvalPoint2Eii', i, j,
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
    Calls Qt's 'void QOpenGLFunctions_1_5::glEvalMesh2(GLenum mode, GLint i1,
    GLint i2, GLint j1, GLint j2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glEvalMesh2

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
    #  void QOpenGLFunctions_1_5::glEvalMesh2(GLenum mode, GLint i1, GLint
    #      i2, GLint j1, GLint j2)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_511glEvalMesh2Ejiiii',
        mode, i1, i2, j1, j2,
    )

  @overload(int)
  def glEvalPoint1(self, i: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glEvalPoint1(GLint i)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glEvalPoint1

    Parameters
    ----------

    i : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glEvalPoint1(GLint i)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_1_512glEvalPoint1Ei', i)

  @overload(int, int, int)
  def glEvalMesh1(self, mode: int, i1: int, i2: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glEvalMesh1(GLenum mode, GLint i1,
    GLint i2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glEvalMesh1

    Parameters
    ----------

    mode : int
      Passed on as it is.

    i1 : int
      Passed on as it is.

    i2 : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glEvalMesh1(GLenum mode, GLint i1, GLint
    #      i2)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_511glEvalMesh1Ejii', mode, i1, i2,
    )

  @overload(float, float)
  def glEvalCoord2f(self, u: float, v: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glEvalCoord2f(GLfloat u, GLfloat
    v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glEvalCoord2f

    Parameters
    ----------

    u : float
      Passed on as it is.

    v : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glEvalCoord2f(GLfloat u, GLfloat v)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_513glEvalCoord2fEff', u, v,
    )

  @overload(float, float)
  def glEvalCoord2d(self, u: float, v: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glEvalCoord2d(GLdouble u, GLdouble
    v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glEvalCoord2d

    Parameters
    ----------

    u : float
      Passed on as it is.

    v : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glEvalCoord2d(GLdouble u, GLdouble v)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_513glEvalCoord2dEdd', u, v,
    )

  @overload(float)
  def glEvalCoord1f(self, u: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glEvalCoord1f(GLfloat u)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glEvalCoord1f

    Parameters
    ----------

    u : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glEvalCoord1f(GLfloat u)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_1_513glEvalCoord1fEf', u)

  @overload(float)
  def glEvalCoord1d(self, u: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glEvalCoord1d(GLdouble u)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glEvalCoord1d

    Parameters
    ----------

    u : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glEvalCoord1d(GLdouble u)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_1_513glEvalCoord1dEd', u)

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
    Calls Qt's 'void QOpenGLFunctions_1_5::glMapGrid2f(GLint un, GLfloat u1,
    GLfloat u2, GLint vn, GLfloat v1, GLfloat v2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glMapGrid2f

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
    #  void QOpenGLFunctions_1_5::glMapGrid2f(GLint un, GLfloat u1, GLfloat
    #      u2, GLint vn, GLfloat v1, GLfloat v2)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_511glMapGrid2fEiffiff',
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
    Calls Qt's 'void QOpenGLFunctions_1_5::glMapGrid2d(GLint un, GLdouble u1,
    GLdouble u2, GLint vn, GLdouble v1, GLdouble v2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glMapGrid2d

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
    #  void QOpenGLFunctions_1_5::glMapGrid2d(GLint un, GLdouble u1, GLdouble
    #      u2, GLint vn, GLdouble v1, GLdouble v2)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_511glMapGrid2dEiddidd',
        un, u1, u2, vn, v1, v2,
    )

  @overload(int, float, float)
  def glMapGrid1f(self, un: int, u1: float, u2: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glMapGrid1f(GLint un, GLfloat u1,
    GLfloat u2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glMapGrid1f

    Parameters
    ----------

    un : int
      Passed on as it is.

    u1 : float
      Passed on as it is.

    u2 : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glMapGrid1f(GLint un, GLfloat u1, GLfloat
    #      u2)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_511glMapGrid1fEiff', un, u1, u2,
    )

  @overload(int, float, float)
  def glMapGrid1d(self, un: int, u1: float, u2: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glMapGrid1d(GLint un, GLdouble u1,
    GLdouble u2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glMapGrid1d

    Parameters
    ----------

    un : int
      Passed on as it is.

    u1 : float
      Passed on as it is.

    u2 : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glMapGrid1d(GLint un, GLdouble u1, GLdouble
    #      u2)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_511glMapGrid1dEidd', un, u1, u2,
    )

  @overload(int)
  def glPushAttrib(self, mask: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glPushAttrib(GLbitfield mask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glPushAttrib

    Parameters
    ----------

    mask : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glPushAttrib(GLbitfield mask)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_512glPushAttribEj', mask,
    )

  def glPopAttrib(self) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glPopAttrib()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glPopAttrib
    """
    #  void QOpenGLFunctions_1_5::glPopAttrib()
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_1_511glPopAttribEv')

  @overload(int, float)
  def glAccum(self, op: int, value: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glAccum(GLenum op, GLfloat
    value)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glAccum

    Parameters
    ----------

    op : int
      Passed on as it is.

    value : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glAccum(GLenum op, GLfloat value)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_57glAccumEjf', op, value,
    )

  @overload(int)
  def glIndexMask(self, mask: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glIndexMask(GLuint mask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glIndexMask

    Parameters
    ----------

    mask : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glIndexMask(GLuint mask)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_511glIndexMaskEj', mask,
    )

  @overload(float)
  def glClearIndex(self, c: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glClearIndex(GLfloat c)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glClearIndex

    Parameters
    ----------

    c : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glClearIndex(GLfloat c)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_1_512glClearIndexEf', c)

  @overload(float, float, float, float)
  def glClearAccum(
      self,
      red: float,
      green: float,
      blue: float,
      alpha: float,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glClearAccum(GLfloat red, GLfloat
    green, GLfloat blue, GLfloat alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glClearAccum

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
    #  void QOpenGLFunctions_1_5::glClearAccum(GLfloat red, GLfloat green,
    #      GLfloat blue, GLfloat alpha)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_512glClearAccumEffff',
        red, green, blue, alpha,
    )

  @overload(int)
  def glPushName(self, name: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glPushName(GLuint name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glPushName

    Parameters
    ----------

    name : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glPushName(GLuint name)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_1_510glPushNameEj', name)

  def glPopName(self) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glPopName()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glPopName
    """
    #  void QOpenGLFunctions_1_5::glPopName()
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_1_59glPopNameEv')

  @overload(float)
  def glPassThrough(self, token: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glPassThrough(GLfloat token)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glPassThrough

    Parameters
    ----------

    token : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glPassThrough(GLfloat token)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_513glPassThroughEf', token,
    )

  @overload(int)
  def glLoadName(self, name: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glLoadName(GLuint name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glLoadName

    Parameters
    ----------

    name : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glLoadName(GLuint name)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_1_510glLoadNameEj', name)

  def glInitNames(self) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glInitNames()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glInitNames
    """
    #  void QOpenGLFunctions_1_5::glInitNames()
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_1_511glInitNamesEv')

  @overload(int)
  def glRenderMode(self, mode: int) -> int:
    """
    Calls Qt's 'GLint QOpenGLFunctions_1_5::glRenderMode(GLenum mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glRenderMode

    Parameters
    ----------

    mode : int
      Passed on as it is.
    """
    #  GLint QOpenGLFunctions_1_5::glRenderMode(GLenum mode)
    return self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_512glRenderModeEj', mode,
    )

  @overload(int, int, int)
  def glTexGeni(self, coord: int, pname: int, param: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glTexGeni(GLenum coord, GLenum
    pname, GLint param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glTexGeni

    Parameters
    ----------

    coord : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    param : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glTexGeni(GLenum coord, GLenum pname, GLint
    #      param)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_59glTexGeniEjji', coord, pname, param,
    )

  @overload(int, int, float)
  def glTexGenf(self, coord: int, pname: int, param: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glTexGenf(GLenum coord, GLenum
    pname, GLfloat param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glTexGenf

    Parameters
    ----------

    coord : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    param : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glTexGenf(GLenum coord, GLenum pname,
    #      GLfloat param)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_59glTexGenfEjjf', coord, pname, param,
    )

  @overload(int, int, float)
  def glTexGend(self, coord: int, pname: int, param: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glTexGend(GLenum coord, GLenum
    pname, GLdouble param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glTexGend

    Parameters
    ----------

    coord : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    param : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glTexGend(GLenum coord, GLenum pname,
    #      GLdouble param)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_59glTexGendEjjd', coord, pname, param,
    )

  @overload(int, int, int)
  def glTexEnvi(self, target: int, pname: int, param: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glTexEnvi(GLenum target, GLenum
    pname, GLint param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glTexEnvi

    Parameters
    ----------

    target : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    param : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glTexEnvi(GLenum target, GLenum pname,
    #      GLint param)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_59glTexEnviEjji',
        target, pname, param,
    )

  @overload(int, int, float)
  def glTexEnvf(self, target: int, pname: int, param: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glTexEnvf(GLenum target, GLenum
    pname, GLfloat param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glTexEnvf

    Parameters
    ----------

    target : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    param : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glTexEnvf(GLenum target, GLenum pname,
    #      GLfloat param)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_59glTexEnvfEjjf',
        target, pname, param,
    )

  @overload(int)
  def glShadeModel(self, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glShadeModel(GLenum mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glShadeModel

    Parameters
    ----------

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glShadeModel(GLenum mode)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_512glShadeModelEj', mode,
    )

  @overload(int, int, int)
  def glMateriali(self, face: int, pname: int, param: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glMateriali(GLenum face, GLenum
    pname, GLint param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glMateriali

    Parameters
    ----------

    face : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    param : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glMateriali(GLenum face, GLenum pname,
    #      GLint param)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_511glMaterialiEjji',
        face, pname, param,
    )

  @overload(int, int, float)
  def glMaterialf(self, face: int, pname: int, param: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glMaterialf(GLenum face, GLenum
    pname, GLfloat param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glMaterialf

    Parameters
    ----------

    face : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    param : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glMaterialf(GLenum face, GLenum pname,
    #      GLfloat param)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_511glMaterialfEjjf',
        face, pname, param,
    )

  @overload(int, int)
  def glLineStipple(self, factor: int, pattern: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glLineStipple(GLint factor,
    GLushort pattern)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glLineStipple

    Parameters
    ----------

    factor : int
      Passed on as it is.

    pattern : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glLineStipple(GLint factor, GLushort
    #      pattern)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_513glLineStippleEit', factor, pattern,
    )

  @overload(int, int)
  def glLightModeli(self, pname: int, param: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glLightModeli(GLenum pname, GLint
    param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glLightModeli

    Parameters
    ----------

    pname : int
      Passed on as it is.

    param : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glLightModeli(GLenum pname, GLint param)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_513glLightModeliEji', pname, param,
    )

  @overload(int, float)
  def glLightModelf(self, pname: int, param: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glLightModelf(GLenum pname,
    GLfloat param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glLightModelf

    Parameters
    ----------

    pname : int
      Passed on as it is.

    param : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glLightModelf(GLenum pname, GLfloat param)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_513glLightModelfEjf', pname, param,
    )

  @overload(int, int, int)
  def glLighti(self, light: int, pname: int, param: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glLighti(GLenum light, GLenum
    pname, GLint param)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glLighti

    Parameters
    ----------

    light : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    param : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glLighti(GLenum light, GLenum pname, GLint
    #      param)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_58glLightiEjji', light, pname, param,
    )

  @overload(int, int, float)
  def glLightf(self, light: int, pname: int, param: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glLightf(GLenum light, GLenum
    pname, GLfloat param)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glLightf

    Parameters
    ----------

    light : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    param : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glLightf(GLenum light, GLenum pname,
    #      GLfloat param)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_58glLightfEjjf', light, pname, param,
    )

  @overload(int, int)
  def glFogi(self, pname: int, param: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glFogi(GLenum pname, GLint
    param)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glFogi

    Parameters
    ----------

    pname : int
      Passed on as it is.

    param : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glFogi(GLenum pname, GLint param)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_56glFogiEji', pname, param,
    )

  @overload(int, float)
  def glFogf(self, pname: int, param: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glFogf(GLenum pname, GLfloat
    param)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glFogf

    Parameters
    ----------

    pname : int
      Passed on as it is.

    param : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glFogf(GLenum pname, GLfloat param)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_56glFogfEjf', pname, param,
    )

  @overload(int, int)
  def glColorMaterial(self, face: int, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glColorMaterial(GLenum face,
    GLenum mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glColorMaterial

    Parameters
    ----------

    face : int
      Passed on as it is.

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glColorMaterial(GLenum face, GLenum mode)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_515glColorMaterialEjj', face, mode,
    )

  @overload(int, int, int, int)
  def glVertex4s(self, x: int, y: int, z: int, w: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glVertex4s(GLshort x, GLshort y,
    GLshort z, GLshort w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glVertex4s

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
    #  void QOpenGLFunctions_1_5::glVertex4s(GLshort x, GLshort y, GLshort z,
    #      GLshort w)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_510glVertex4sEssss', x, y, z, w,
    )

  @overload(int, int, int, int)
  def glVertex4i(self, x: int, y: int, z: int, w: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glVertex4i(GLint x, GLint y, GLint
    z, GLint w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glVertex4i

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
    #  void QOpenGLFunctions_1_5::glVertex4i(GLint x, GLint y, GLint z, GLint
    #      w)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_510glVertex4iEiiii', x, y, z, w,
    )

  @overload(float, float, float, float)
  def glVertex4f(self, x: float, y: float, z: float, w: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glVertex4f(GLfloat x, GLfloat y,
    GLfloat z, GLfloat w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glVertex4f

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
    #  void QOpenGLFunctions_1_5::glVertex4f(GLfloat x, GLfloat y, GLfloat z,
    #      GLfloat w)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_510glVertex4fEffff', x, y, z, w,
    )

  @overload(float, float, float, float)
  def glVertex4d(self, x: float, y: float, z: float, w: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glVertex4d(GLdouble x, GLdouble y,
    GLdouble z, GLdouble w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glVertex4d

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
    #  void QOpenGLFunctions_1_5::glVertex4d(GLdouble x, GLdouble y, GLdouble
    #      z, GLdouble w)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_510glVertex4dEdddd', x, y, z, w,
    )

  @overload(int, int, int)
  def glVertex3s(self, x: int, y: int, z: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glVertex3s(GLshort x, GLshort y,
    GLshort z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glVertex3s

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    z : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glVertex3s(GLshort x, GLshort y, GLshort z)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_510glVertex3sEsss', x, y, z,
    )

  @overload(int, int, int)
  def glVertex3i(self, x: int, y: int, z: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glVertex3i(GLint x, GLint y, GLint
    z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glVertex3i

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    z : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glVertex3i(GLint x, GLint y, GLint z)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_510glVertex3iEiii', x, y, z,
    )

  @overload(float, float, float)
  def glVertex3f(self, x: float, y: float, z: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glVertex3f(GLfloat x, GLfloat y,
    GLfloat z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glVertex3f

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glVertex3f(GLfloat x, GLfloat y, GLfloat z)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_510glVertex3fEfff', x, y, z,
    )

  @overload(float, float, float)
  def glVertex3d(self, x: float, y: float, z: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glVertex3d(GLdouble x, GLdouble y,
    GLdouble z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glVertex3d

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glVertex3d(GLdouble x, GLdouble y, GLdouble
    #      z)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_510glVertex3dEddd', x, y, z,
    )

  @overload(int, int)
  def glVertex2s(self, x: int, y: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glVertex2s(GLshort x, GLshort y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glVertex2s

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glVertex2s(GLshort x, GLshort y)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_510glVertex2sEss', x, y,
    )

  @overload(int, int)
  def glVertex2i(self, x: int, y: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glVertex2i(GLint x, GLint y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glVertex2i

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glVertex2i(GLint x, GLint y)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_510glVertex2iEii', x, y,
    )

  @overload(float, float)
  def glVertex2f(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glVertex2f(GLfloat x, GLfloat y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glVertex2f

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glVertex2f(GLfloat x, GLfloat y)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_510glVertex2fEff', x, y,
    )

  @overload(float, float)
  def glVertex2d(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glVertex2d(GLdouble x, GLdouble
    y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glVertex2d

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glVertex2d(GLdouble x, GLdouble y)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_510glVertex2dEdd', x, y,
    )

  @overload(int, int, int, int)
  def glTexCoord4s(self, s: int, t: int, r: int, q: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glTexCoord4s(GLshort s, GLshort t,
    GLshort r, GLshort q)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glTexCoord4s

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
    #  void QOpenGLFunctions_1_5::glTexCoord4s(GLshort s, GLshort t, GLshort
    #      r, GLshort q)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_512glTexCoord4sEssss', s, t, r, q,
    )

  @overload(int, int, int, int)
  def glTexCoord4i(self, s: int, t: int, r: int, q: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glTexCoord4i(GLint s, GLint t,
    GLint r, GLint q)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glTexCoord4i

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
    #  void QOpenGLFunctions_1_5::glTexCoord4i(GLint s, GLint t, GLint r,
    #      GLint q)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_512glTexCoord4iEiiii', s, t, r, q,
    )

  @overload(float, float, float, float)
  def glTexCoord4f(self, s: float, t: float, r: float, q: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glTexCoord4f(GLfloat s, GLfloat t,
    GLfloat r, GLfloat q)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glTexCoord4f

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
    #  void QOpenGLFunctions_1_5::glTexCoord4f(GLfloat s, GLfloat t, GLfloat
    #      r, GLfloat q)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_512glTexCoord4fEffff', s, t, r, q,
    )

  @overload(float, float, float, float)
  def glTexCoord4d(self, s: float, t: float, r: float, q: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glTexCoord4d(GLdouble s, GLdouble
    t, GLdouble r, GLdouble q)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glTexCoord4d

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
    #  void QOpenGLFunctions_1_5::glTexCoord4d(GLdouble s, GLdouble t,
    #      GLdouble r, GLdouble q)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_512glTexCoord4dEdddd', s, t, r, q,
    )

  @overload(int, int, int)
  def glTexCoord3s(self, s: int, t: int, r: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glTexCoord3s(GLshort s, GLshort t,
    GLshort r)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glTexCoord3s

    Parameters
    ----------

    s : int
      Passed on as it is.

    t : int
      Passed on as it is.

    r : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glTexCoord3s(GLshort s, GLshort t, GLshort
    #      r)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_512glTexCoord3sEsss', s, t, r,
    )

  @overload(int, int, int)
  def glTexCoord3i(self, s: int, t: int, r: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glTexCoord3i(GLint s, GLint t,
    GLint r)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glTexCoord3i

    Parameters
    ----------

    s : int
      Passed on as it is.

    t : int
      Passed on as it is.

    r : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glTexCoord3i(GLint s, GLint t, GLint r)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_512glTexCoord3iEiii', s, t, r,
    )

  @overload(float, float, float)
  def glTexCoord3f(self, s: float, t: float, r: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glTexCoord3f(GLfloat s, GLfloat t,
    GLfloat r)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glTexCoord3f

    Parameters
    ----------

    s : float
      Passed on as it is.

    t : float
      Passed on as it is.

    r : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glTexCoord3f(GLfloat s, GLfloat t, GLfloat
    #      r)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_512glTexCoord3fEfff', s, t, r,
    )

  @overload(float, float, float)
  def glTexCoord3d(self, s: float, t: float, r: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glTexCoord3d(GLdouble s, GLdouble
    t, GLdouble r)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glTexCoord3d

    Parameters
    ----------

    s : float
      Passed on as it is.

    t : float
      Passed on as it is.

    r : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glTexCoord3d(GLdouble s, GLdouble t,
    #      GLdouble r)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_512glTexCoord3dEddd', s, t, r,
    )

  @overload(int, int)
  def glTexCoord2s(self, s: int, t: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glTexCoord2s(GLshort s, GLshort
    t)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glTexCoord2s

    Parameters
    ----------

    s : int
      Passed on as it is.

    t : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glTexCoord2s(GLshort s, GLshort t)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_512glTexCoord2sEss', s, t,
    )

  @overload(int, int)
  def glTexCoord2i(self, s: int, t: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glTexCoord2i(GLint s, GLint t)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glTexCoord2i

    Parameters
    ----------

    s : int
      Passed on as it is.

    t : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glTexCoord2i(GLint s, GLint t)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_512glTexCoord2iEii', s, t,
    )

  @overload(float, float)
  def glTexCoord2f(self, s: float, t: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glTexCoord2f(GLfloat s, GLfloat
    t)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glTexCoord2f

    Parameters
    ----------

    s : float
      Passed on as it is.

    t : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glTexCoord2f(GLfloat s, GLfloat t)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_512glTexCoord2fEff', s, t,
    )

  @overload(float, float)
  def glTexCoord2d(self, s: float, t: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glTexCoord2d(GLdouble s, GLdouble
    t)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glTexCoord2d

    Parameters
    ----------

    s : float
      Passed on as it is.

    t : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glTexCoord2d(GLdouble s, GLdouble t)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_512glTexCoord2dEdd', s, t,
    )

  @overload(int)
  def glTexCoord1s(self, s: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glTexCoord1s(GLshort s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glTexCoord1s

    Parameters
    ----------

    s : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glTexCoord1s(GLshort s)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_1_512glTexCoord1sEs', s)

  @overload(int)
  def glTexCoord1i(self, s: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glTexCoord1i(GLint s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glTexCoord1i

    Parameters
    ----------

    s : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glTexCoord1i(GLint s)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_1_512glTexCoord1iEi', s)

  @overload(float)
  def glTexCoord1f(self, s: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glTexCoord1f(GLfloat s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glTexCoord1f

    Parameters
    ----------

    s : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glTexCoord1f(GLfloat s)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_1_512glTexCoord1fEf', s)

  @overload(float)
  def glTexCoord1d(self, s: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glTexCoord1d(GLdouble s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glTexCoord1d

    Parameters
    ----------

    s : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glTexCoord1d(GLdouble s)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_1_512glTexCoord1dEd', s)

  @overload(int, int, int, int)
  def glRects(self, x1: int, y1: int, x2: int, y2: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glRects(GLshort x1, GLshort y1,
    GLshort x2, GLshort y2)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glRects

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
    #  void QOpenGLFunctions_1_5::glRects(GLshort x1, GLshort y1, GLshort x2,
    #      GLshort y2)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_57glRectsEssss', x1, y1, x2, y2,
    )

  @overload(int, int, int, int)
  def glRecti(self, x1: int, y1: int, x2: int, y2: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glRecti(GLint x1, GLint y1, GLint
    x2, GLint y2)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glRecti

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
    #  void QOpenGLFunctions_1_5::glRecti(GLint x1, GLint y1, GLint x2, GLint
    #      y2)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_57glRectiEiiii', x1, y1, x2, y2,
    )

  @overload(float, float, float, float)
  def glRectf(self, x1: float, y1: float, x2: float, y2: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glRectf(GLfloat x1, GLfloat y1,
    GLfloat x2, GLfloat y2)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glRectf

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
    #  void QOpenGLFunctions_1_5::glRectf(GLfloat x1, GLfloat y1, GLfloat x2,
    #      GLfloat y2)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_57glRectfEffff', x1, y1, x2, y2,
    )

  @overload(float, float, float, float)
  def glRectd(self, x1: float, y1: float, x2: float, y2: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glRectd(GLdouble x1, GLdouble y1,
    GLdouble x2, GLdouble y2)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glRectd

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
    #  void QOpenGLFunctions_1_5::glRectd(GLdouble x1, GLdouble y1, GLdouble
    #      x2, GLdouble y2)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_57glRectdEdddd', x1, y1, x2, y2,
    )

  @overload(int, int, int, int)
  def glRasterPos4s(self, x: int, y: int, z: int, w: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glRasterPos4s(GLshort x, GLshort
    y, GLshort z, GLshort w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glRasterPos4s

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
    #  void QOpenGLFunctions_1_5::glRasterPos4s(GLshort x, GLshort y, GLshort
    #      z, GLshort w)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_513glRasterPos4sEssss', x, y, z, w,
    )

  @overload(int, int, int, int)
  def glRasterPos4i(self, x: int, y: int, z: int, w: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glRasterPos4i(GLint x, GLint y,
    GLint z, GLint w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glRasterPos4i

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
    #  void QOpenGLFunctions_1_5::glRasterPos4i(GLint x, GLint y, GLint z,
    #      GLint w)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_513glRasterPos4iEiiii', x, y, z, w,
    )

  @overload(float, float, float, float)
  def glRasterPos4f(self, x: float, y: float, z: float, w: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glRasterPos4f(GLfloat x, GLfloat
    y, GLfloat z, GLfloat w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glRasterPos4f

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
    #  void QOpenGLFunctions_1_5::glRasterPos4f(GLfloat x, GLfloat y, GLfloat
    #      z, GLfloat w)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_513glRasterPos4fEffff', x, y, z, w,
    )

  @overload(float, float, float, float)
  def glRasterPos4d(self, x: float, y: float, z: float, w: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glRasterPos4d(GLdouble x, GLdouble
    y, GLdouble z, GLdouble w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glRasterPos4d

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
    #  void QOpenGLFunctions_1_5::glRasterPos4d(GLdouble x, GLdouble y,
    #      GLdouble z, GLdouble w)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_513glRasterPos4dEdddd', x, y, z, w,
    )

  @overload(int, int, int)
  def glRasterPos3s(self, x: int, y: int, z: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glRasterPos3s(GLshort x, GLshort
    y, GLshort z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glRasterPos3s

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    z : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glRasterPos3s(GLshort x, GLshort y, GLshort
    #      z)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_513glRasterPos3sEsss', x, y, z,
    )

  @overload(int, int, int)
  def glRasterPos3i(self, x: int, y: int, z: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glRasterPos3i(GLint x, GLint y,
    GLint z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glRasterPos3i

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    z : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glRasterPos3i(GLint x, GLint y, GLint z)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_513glRasterPos3iEiii', x, y, z,
    )

  @overload(float, float, float)
  def glRasterPos3f(self, x: float, y: float, z: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glRasterPos3f(GLfloat x, GLfloat
    y, GLfloat z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glRasterPos3f

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glRasterPos3f(GLfloat x, GLfloat y, GLfloat
    #      z)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_513glRasterPos3fEfff', x, y, z,
    )

  @overload(float, float, float)
  def glRasterPos3d(self, x: float, y: float, z: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glRasterPos3d(GLdouble x, GLdouble
    y, GLdouble z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glRasterPos3d

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glRasterPos3d(GLdouble x, GLdouble y,
    #      GLdouble z)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_513glRasterPos3dEddd', x, y, z,
    )

  @overload(int, int)
  def glRasterPos2s(self, x: int, y: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glRasterPos2s(GLshort x, GLshort
    y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glRasterPos2s

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glRasterPos2s(GLshort x, GLshort y)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_513glRasterPos2sEss', x, y,
    )

  @overload(int, int)
  def glRasterPos2i(self, x: int, y: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glRasterPos2i(GLint x, GLint y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glRasterPos2i

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glRasterPos2i(GLint x, GLint y)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_513glRasterPos2iEii', x, y,
    )

  @overload(float, float)
  def glRasterPos2f(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glRasterPos2f(GLfloat x, GLfloat
    y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glRasterPos2f

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glRasterPos2f(GLfloat x, GLfloat y)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_513glRasterPos2fEff', x, y,
    )

  @overload(float, float)
  def glRasterPos2d(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glRasterPos2d(GLdouble x, GLdouble
    y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glRasterPos2d

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glRasterPos2d(GLdouble x, GLdouble y)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_513glRasterPos2dEdd', x, y,
    )

  @overload(int, int, int)
  def glNormal3s(self, nx: int, ny: int, nz: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glNormal3s(GLshort nx, GLshort ny,
    GLshort nz)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glNormal3s

    Parameters
    ----------

    nx : int
      Passed on as it is.

    ny : int
      Passed on as it is.

    nz : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glNormal3s(GLshort nx, GLshort ny, GLshort
    #      nz)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_510glNormal3sEsss', nx, ny, nz,
    )

  @overload(int, int, int)
  def glNormal3i(self, nx: int, ny: int, nz: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glNormal3i(GLint nx, GLint ny,
    GLint nz)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glNormal3i

    Parameters
    ----------

    nx : int
      Passed on as it is.

    ny : int
      Passed on as it is.

    nz : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glNormal3i(GLint nx, GLint ny, GLint nz)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_510glNormal3iEiii', nx, ny, nz,
    )

  @overload(float, float, float)
  def glNormal3f(self, nx: float, ny: float, nz: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glNormal3f(GLfloat nx, GLfloat ny,
    GLfloat nz)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glNormal3f

    Parameters
    ----------

    nx : float
      Passed on as it is.

    ny : float
      Passed on as it is.

    nz : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glNormal3f(GLfloat nx, GLfloat ny, GLfloat
    #      nz)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_510glNormal3fEfff', nx, ny, nz,
    )

  @overload(float, float, float)
  def glNormal3d(self, nx: float, ny: float, nz: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glNormal3d(GLdouble nx, GLdouble
    ny, GLdouble nz)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glNormal3d

    Parameters
    ----------

    nx : float
      Passed on as it is.

    ny : float
      Passed on as it is.

    nz : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glNormal3d(GLdouble nx, GLdouble ny,
    #      GLdouble nz)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_510glNormal3dEddd', nx, ny, nz,
    )

  @overload(int, int, int)
  def glNormal3b(self, nx: int, ny: int, nz: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glNormal3b(GLbyte nx, GLbyte ny,
    GLbyte nz)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glNormal3b

    Parameters
    ----------

    nx : int
      Passed on as it is.

    ny : int
      Passed on as it is.

    nz : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glNormal3b(GLbyte nx, GLbyte ny, GLbyte nz)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_510glNormal3bEaaa', nx, ny, nz,
    )

  @overload(int)
  def glIndexs(self, c: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glIndexs(GLshort c)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glIndexs

    Parameters
    ----------

    c : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glIndexs(GLshort c)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_1_58glIndexsEs', c)

  @overload(int)
  def glIndexi(self, c: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glIndexi(GLint c)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glIndexi

    Parameters
    ----------

    c : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glIndexi(GLint c)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_1_58glIndexiEi', c)

  @overload(float)
  def glIndexf(self, c: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glIndexf(GLfloat c)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glIndexf

    Parameters
    ----------

    c : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glIndexf(GLfloat c)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_1_58glIndexfEf', c)

  @overload(float)
  def glIndexd(self, c: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glIndexd(GLdouble c)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glIndexd

    Parameters
    ----------

    c : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glIndexd(GLdouble c)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_1_58glIndexdEd', c)

  def glEnd(self) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glEnd()'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glEnd
    """
    #  void QOpenGLFunctions_1_5::glEnd()
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_1_55glEndEv')

  @overload(int)
  def glEdgeFlag(self, flag: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glEdgeFlag(GLboolean flag)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glEdgeFlag

    Parameters
    ----------

    flag : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glEdgeFlag(GLboolean flag)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_1_510glEdgeFlagEh', flag)

  @overload(int, int, int, int)
  def glColor4us(self, red: int, green: int, blue: int, alpha: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glColor4us(GLushort red, GLushort
    green, GLushort blue, GLushort alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glColor4us

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
    #  void QOpenGLFunctions_1_5::glColor4us(GLushort red, GLushort green,
    #      GLushort blue, GLushort alpha)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_510glColor4usEtttt',
        red, green, blue, alpha,
    )

  @overload(int, int, int, int)
  def glColor4ui(self, red: int, green: int, blue: int, alpha: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glColor4ui(GLuint red, GLuint
    green, GLuint blue, GLuint alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glColor4ui

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
    #  void QOpenGLFunctions_1_5::glColor4ui(GLuint red, GLuint green, GLuint
    #      blue, GLuint alpha)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_510glColor4uiEjjjj',
        red, green, blue, alpha,
    )

  @overload(int, int, int, int)
  def glColor4ub(self, red: int, green: int, blue: int, alpha: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glColor4ub(GLubyte red, GLubyte
    green, GLubyte blue, GLubyte alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glColor4ub

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
    #  void QOpenGLFunctions_1_5::glColor4ub(GLubyte red, GLubyte green,
    #      GLubyte blue, GLubyte alpha)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_510glColor4ubEhhhh',
        red, green, blue, alpha,
    )

  @overload(int, int, int, int)
  def glColor4s(self, red: int, green: int, blue: int, alpha: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glColor4s(GLshort red, GLshort
    green, GLshort blue, GLshort alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glColor4s

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
    #  void QOpenGLFunctions_1_5::glColor4s(GLshort red, GLshort green,
    #      GLshort blue, GLshort alpha)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_59glColor4sEssss',
        red, green, blue, alpha,
    )

  @overload(int, int, int, int)
  def glColor4i(self, red: int, green: int, blue: int, alpha: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glColor4i(GLint red, GLint green,
    GLint blue, GLint alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glColor4i

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
    #  void QOpenGLFunctions_1_5::glColor4i(GLint red, GLint green, GLint
    #      blue, GLint alpha)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_59glColor4iEiiii',
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
    Calls Qt's 'void QOpenGLFunctions_1_5::glColor4f(GLfloat red, GLfloat
    green, GLfloat blue, GLfloat alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glColor4f

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
    #  void QOpenGLFunctions_1_5::glColor4f(GLfloat red, GLfloat green,
    #      GLfloat blue, GLfloat alpha)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_59glColor4fEffff',
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
    Calls Qt's 'void QOpenGLFunctions_1_5::glColor4d(GLdouble red, GLdouble
    green, GLdouble blue, GLdouble alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glColor4d

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
    #  void QOpenGLFunctions_1_5::glColor4d(GLdouble red, GLdouble green,
    #      GLdouble blue, GLdouble alpha)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_59glColor4dEdddd',
        red, green, blue, alpha,
    )

  @overload(int, int, int, int)
  def glColor4b(self, red: int, green: int, blue: int, alpha: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glColor4b(GLbyte red, GLbyte
    green, GLbyte blue, GLbyte alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glColor4b

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
    #  void QOpenGLFunctions_1_5::glColor4b(GLbyte red, GLbyte green, GLbyte
    #      blue, GLbyte alpha)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_59glColor4bEaaaa',
        red, green, blue, alpha,
    )

  @overload(int, int, int)
  def glColor3us(self, red: int, green: int, blue: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glColor3us(GLushort red, GLushort
    green, GLushort blue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glColor3us

    Parameters
    ----------

    red : int
      Passed on as it is.

    green : int
      Passed on as it is.

    blue : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glColor3us(GLushort red, GLushort green,
    #      GLushort blue)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_510glColor3usEttt', red, green, blue,
    )

  @overload(int, int, int)
  def glColor3ui(self, red: int, green: int, blue: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glColor3ui(GLuint red, GLuint
    green, GLuint blue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glColor3ui

    Parameters
    ----------

    red : int
      Passed on as it is.

    green : int
      Passed on as it is.

    blue : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glColor3ui(GLuint red, GLuint green, GLuint
    #      blue)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_510glColor3uiEjjj', red, green, blue,
    )

  @overload(int, int, int)
  def glColor3ub(self, red: int, green: int, blue: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glColor3ub(GLubyte red, GLubyte
    green, GLubyte blue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glColor3ub

    Parameters
    ----------

    red : int
      Passed on as it is.

    green : int
      Passed on as it is.

    blue : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glColor3ub(GLubyte red, GLubyte green,
    #      GLubyte blue)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_510glColor3ubEhhh', red, green, blue,
    )

  @overload(int, int, int)
  def glColor3s(self, red: int, green: int, blue: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glColor3s(GLshort red, GLshort
    green, GLshort blue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glColor3s

    Parameters
    ----------

    red : int
      Passed on as it is.

    green : int
      Passed on as it is.

    blue : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glColor3s(GLshort red, GLshort green,
    #      GLshort blue)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_59glColor3sEsss', red, green, blue,
    )

  @overload(int, int, int)
  def glColor3i(self, red: int, green: int, blue: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glColor3i(GLint red, GLint green,
    GLint blue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glColor3i

    Parameters
    ----------

    red : int
      Passed on as it is.

    green : int
      Passed on as it is.

    blue : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glColor3i(GLint red, GLint green, GLint
    #      blue)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_59glColor3iEiii', red, green, blue,
    )

  @overload(float, float, float)
  def glColor3f(self, red: float, green: float, blue: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glColor3f(GLfloat red, GLfloat
    green, GLfloat blue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glColor3f

    Parameters
    ----------

    red : float
      Passed on as it is.

    green : float
      Passed on as it is.

    blue : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glColor3f(GLfloat red, GLfloat green,
    #      GLfloat blue)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_59glColor3fEfff', red, green, blue,
    )

  @overload(float, float, float)
  def glColor3d(self, red: float, green: float, blue: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glColor3d(GLdouble red, GLdouble
    green, GLdouble blue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glColor3d

    Parameters
    ----------

    red : float
      Passed on as it is.

    green : float
      Passed on as it is.

    blue : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glColor3d(GLdouble red, GLdouble green,
    #      GLdouble blue)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_59glColor3dEddd', red, green, blue,
    )

  @overload(int, int, int)
  def glColor3b(self, red: int, green: int, blue: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glColor3b(GLbyte red, GLbyte
    green, GLbyte blue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glColor3b

    Parameters
    ----------

    red : int
      Passed on as it is.

    green : int
      Passed on as it is.

    blue : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glColor3b(GLbyte red, GLbyte green, GLbyte
    #      blue)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_59glColor3bEaaa', red, green, blue,
    )

  @overload(int)
  def glBegin(self, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glBegin(GLenum mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glBegin

    Parameters
    ----------

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glBegin(GLenum mode)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_1_57glBeginEj', mode)

  @overload(int)
  def glListBase(self, base: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glListBase(GLuint base)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glListBase

    Parameters
    ----------

    base : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glListBase(GLuint base)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_1_510glListBaseEj', base)

  @overload(int)
  def glGenLists(self, range: int) -> int:
    """
    Calls Qt's 'GLuint QOpenGLFunctions_1_5::glGenLists(GLsizei range)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glGenLists

    Parameters
    ----------

    range : int
      Passed on as it is.
    """
    #  GLuint QOpenGLFunctions_1_5::glGenLists(GLsizei range)
    return self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_510glGenListsEi', range,
    )

  @overload(int, int)
  def glDeleteLists(self, list: int, range: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glDeleteLists(GLuint list, GLsizei
    range)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glDeleteLists

    Parameters
    ----------

    list : int
      Passed on as it is.

    range : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glDeleteLists(GLuint list, GLsizei range)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_513glDeleteListsEji', list, range,
    )

  @overload(int)
  def glCallList(self, list: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glCallList(GLuint list)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glCallList

    Parameters
    ----------

    list : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glCallList(GLuint list)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_1_510glCallListEj', list)

  def glEndList(self) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glEndList()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glEndList
    """
    #  void QOpenGLFunctions_1_5::glEndList()
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_1_59glEndListEv')

  @overload(int, int)
  def glNewList(self, list: int, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glNewList(GLuint list, GLenum
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glNewList

    Parameters
    ----------

    list : int
      Passed on as it is.

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glNewList(GLuint list, GLenum mode)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_59glNewListEjj', list, mode,
    )

  @overload(int)
  def glPushClientAttrib(self, mask: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glPushClientAttrib(GLbitfield
    mask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glPushClientAttrib

    Parameters
    ----------

    mask : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glPushClientAttrib(GLbitfield mask)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_518glPushClientAttribEj', mask,
    )

  def glPopClientAttrib(self) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glPopClientAttrib()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glPopClientAttrib
    """
    #  void QOpenGLFunctions_1_5::glPopClientAttrib()
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_517glPopClientAttribEv',
    )

  @overload(int)
  def glEnableClientState(self, array: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glEnableClientState(GLenum
    array)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glEnableClientState

    Parameters
    ----------

    array : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glEnableClientState(GLenum array)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_519glEnableClientStateEj', array,
    )

  @overload(int)
  def glDisableClientState(self, array: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glDisableClientState(GLenum
    array)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glDisableClientState

    Parameters
    ----------

    array : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glDisableClientState(GLenum array)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_520glDisableClientStateEj', array,
    )

  @overload(int)
  def glArrayElement(self, i: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glArrayElement(GLint i)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glArrayElement

    Parameters
    ----------

    i : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glArrayElement(GLint i)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_514glArrayElementEi', i,
    )

  @overload(int)
  def glResetMinmax(self, target: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glResetMinmax(GLenum target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glResetMinmax

    Parameters
    ----------

    target : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glResetMinmax(GLenum target)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_513glResetMinmaxEj', target,
    )

  @overload(int)
  def glResetHistogram(self, target: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glResetHistogram(GLenum target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glResetHistogram

    Parameters
    ----------

    target : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glResetHistogram(GLenum target)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_516glResetHistogramEj', target,
    )

  @overload(int, int, int)
  def glMinmax(self, target: int, internalformat: int, sink: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glMinmax(GLenum target, GLenum
    internalformat, GLboolean sink)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glMinmax

    Parameters
    ----------

    target : int
      Passed on as it is.

    internalformat : int
      Passed on as it is.

    sink : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glMinmax(GLenum target, GLenum
    #      internalformat, GLboolean sink)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_58glMinmaxEjjh',
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
    Calls Qt's 'void QOpenGLFunctions_1_5::glHistogram(GLenum target, GLsizei
    width, GLenum internalformat, GLboolean sink)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glHistogram

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
    #  void QOpenGLFunctions_1_5::glHistogram(GLenum target, GLsizei width,
    #      GLenum internalformat, GLboolean sink)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_511glHistogramEjijh',
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
    Calls Qt's 'void QOpenGLFunctions_1_5::glCopyConvolutionFilter2D(GLenum
    target, GLenum internalformat, GLint x, GLint y, GLsizei width, GLsizei
    height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html

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
    #  void QOpenGLFunctions_1_5::glCopyConvolutionFilter2D(GLenum target,
    #      GLenum internalformat, GLint x, GLint y, GLsizei width, GLsizei
    #      height)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_525glCopyConvolutionFilter2DEjjiiii',
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
    Calls Qt's 'void QOpenGLFunctions_1_5::glCopyConvolutionFilter1D(GLenum
    target, GLenum internalformat, GLint x, GLint y, GLsizei width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html

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
    #  void QOpenGLFunctions_1_5::glCopyConvolutionFilter1D(GLenum target,
    #      GLenum internalformat, GLint x, GLint y, GLsizei width)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_525glCopyConvolutionFilter1DEjjiii',
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
    Calls Qt's 'void QOpenGLFunctions_1_5::glConvolutionParameteri(GLenum
    target, GLenum pname, GLint params)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glConvolutionParameteri

    Parameters
    ----------

    target : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    params : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glConvolutionParameteri(GLenum target,
    #      GLenum pname, GLint params)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_523glConvolutionParameteriEjji',
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
    Calls Qt's 'void QOpenGLFunctions_1_5::glConvolutionParameterf(GLenum
    target, GLenum pname, GLfloat params)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glConvolutionParameterf

    Parameters
    ----------

    target : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    params : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glConvolutionParameterf(GLenum target,
    #      GLenum pname, GLfloat params)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_523glConvolutionParameterfEjjf',
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
    Calls Qt's 'void QOpenGLFunctions_1_5::glCopyColorSubTable(GLenum target,
    GLsizei start, GLint x, GLint y, GLsizei width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glCopyColorSubTable

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
    #  void QOpenGLFunctions_1_5::glCopyColorSubTable(GLenum target, GLsizei
    #      start, GLint x, GLint y, GLsizei width)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_519glCopyColorSubTableEjiiii',
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
    Calls Qt's 'void QOpenGLFunctions_1_5::glCopyColorTable(GLenum target,
    GLenum internalformat, GLint x, GLint y, GLsizei width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glCopyColorTable

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
    #  void QOpenGLFunctions_1_5::glCopyColorTable(GLenum target, GLenum
    #      internalformat, GLint x, GLint y, GLsizei width)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_516glCopyColorTableEjjiii',
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
    Calls Qt's 'void QOpenGLFunctions_1_5::glMultiTexCoord4s(GLenum target,
    GLshort s, GLshort t, GLshort r, GLshort q)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glMultiTexCoord4s

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
    #  void QOpenGLFunctions_1_5::glMultiTexCoord4s(GLenum target, GLshort s,
    #      GLshort t, GLshort r, GLshort q)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_517glMultiTexCoord4sEjssss',
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
    Calls Qt's 'void QOpenGLFunctions_1_5::glMultiTexCoord4i(GLenum target,
    GLint s, GLint t, GLint r, GLint q)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glMultiTexCoord4i

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
    #  void QOpenGLFunctions_1_5::glMultiTexCoord4i(GLenum target, GLint s,
    #      GLint t, GLint r, GLint q)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_517glMultiTexCoord4iEjiiii',
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
    Calls Qt's 'void QOpenGLFunctions_1_5::glMultiTexCoord4f(GLenum target,
    GLfloat s, GLfloat t, GLfloat r, GLfloat q)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glMultiTexCoord4f

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
    #  void QOpenGLFunctions_1_5::glMultiTexCoord4f(GLenum target, GLfloat s,
    #      GLfloat t, GLfloat r, GLfloat q)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_517glMultiTexCoord4fEjffff',
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
    Calls Qt's 'void QOpenGLFunctions_1_5::glMultiTexCoord4d(GLenum target,
    GLdouble s, GLdouble t, GLdouble r, GLdouble q)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glMultiTexCoord4d

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
    #  void QOpenGLFunctions_1_5::glMultiTexCoord4d(GLenum target, GLdouble
    #      s, GLdouble t, GLdouble r, GLdouble q)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_517glMultiTexCoord4dEjdddd',
        target, s, t, r, q,
    )

  @overload(int, int, int, int)
  def glMultiTexCoord3s(self, target: int, s: int, t: int, r: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glMultiTexCoord3s(GLenum target,
    GLshort s, GLshort t, GLshort r)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glMultiTexCoord3s

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
    #  void QOpenGLFunctions_1_5::glMultiTexCoord3s(GLenum target, GLshort s,
    #      GLshort t, GLshort r)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_517glMultiTexCoord3sEjsss',
        target, s, t, r,
    )

  @overload(int, int, int, int)
  def glMultiTexCoord3i(self, target: int, s: int, t: int, r: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glMultiTexCoord3i(GLenum target,
    GLint s, GLint t, GLint r)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glMultiTexCoord3i

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
    #  void QOpenGLFunctions_1_5::glMultiTexCoord3i(GLenum target, GLint s,
    #      GLint t, GLint r)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_517glMultiTexCoord3iEjiii',
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
    Calls Qt's 'void QOpenGLFunctions_1_5::glMultiTexCoord3f(GLenum target,
    GLfloat s, GLfloat t, GLfloat r)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glMultiTexCoord3f

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
    #  void QOpenGLFunctions_1_5::glMultiTexCoord3f(GLenum target, GLfloat s,
    #      GLfloat t, GLfloat r)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_517glMultiTexCoord3fEjfff',
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
    Calls Qt's 'void QOpenGLFunctions_1_5::glMultiTexCoord3d(GLenum target,
    GLdouble s, GLdouble t, GLdouble r)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glMultiTexCoord3d

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
    #  void QOpenGLFunctions_1_5::glMultiTexCoord3d(GLenum target, GLdouble
    #      s, GLdouble t, GLdouble r)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_517glMultiTexCoord3dEjddd',
        target, s, t, r,
    )

  @overload(int, int, int)
  def glMultiTexCoord2s(self, target: int, s: int, t: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glMultiTexCoord2s(GLenum target,
    GLshort s, GLshort t)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glMultiTexCoord2s

    Parameters
    ----------

    target : int
      Passed on as it is.

    s : int
      Passed on as it is.

    t : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glMultiTexCoord2s(GLenum target, GLshort s,
    #      GLshort t)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_517glMultiTexCoord2sEjss',
        target, s, t,
    )

  @overload(int, int, int)
  def glMultiTexCoord2i(self, target: int, s: int, t: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glMultiTexCoord2i(GLenum target,
    GLint s, GLint t)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glMultiTexCoord2i

    Parameters
    ----------

    target : int
      Passed on as it is.

    s : int
      Passed on as it is.

    t : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glMultiTexCoord2i(GLenum target, GLint s,
    #      GLint t)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_517glMultiTexCoord2iEjii',
        target, s, t,
    )

  @overload(int, float, float)
  def glMultiTexCoord2f(self, target: int, s: float, t: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glMultiTexCoord2f(GLenum target,
    GLfloat s, GLfloat t)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glMultiTexCoord2f

    Parameters
    ----------

    target : int
      Passed on as it is.

    s : float
      Passed on as it is.

    t : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glMultiTexCoord2f(GLenum target, GLfloat s,
    #      GLfloat t)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_517glMultiTexCoord2fEjff',
        target, s, t,
    )

  @overload(int, float, float)
  def glMultiTexCoord2d(self, target: int, s: float, t: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glMultiTexCoord2d(GLenum target,
    GLdouble s, GLdouble t)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glMultiTexCoord2d

    Parameters
    ----------

    target : int
      Passed on as it is.

    s : float
      Passed on as it is.

    t : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glMultiTexCoord2d(GLenum target, GLdouble
    #      s, GLdouble t)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_517glMultiTexCoord2dEjdd',
        target, s, t,
    )

  @overload(int, int)
  def glMultiTexCoord1s(self, target: int, s: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glMultiTexCoord1s(GLenum target,
    GLshort s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glMultiTexCoord1s

    Parameters
    ----------

    target : int
      Passed on as it is.

    s : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glMultiTexCoord1s(GLenum target, GLshort s)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_517glMultiTexCoord1sEjs', target, s,
    )

  @overload(int, int)
  def glMultiTexCoord1i(self, target: int, s: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glMultiTexCoord1i(GLenum target,
    GLint s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glMultiTexCoord1i

    Parameters
    ----------

    target : int
      Passed on as it is.

    s : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glMultiTexCoord1i(GLenum target, GLint s)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_517glMultiTexCoord1iEji', target, s,
    )

  @overload(int, float)
  def glMultiTexCoord1f(self, target: int, s: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glMultiTexCoord1f(GLenum target,
    GLfloat s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glMultiTexCoord1f

    Parameters
    ----------

    target : int
      Passed on as it is.

    s : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glMultiTexCoord1f(GLenum target, GLfloat s)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_517glMultiTexCoord1fEjf', target, s,
    )

  @overload(int, float)
  def glMultiTexCoord1d(self, target: int, s: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glMultiTexCoord1d(GLenum target,
    GLdouble s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glMultiTexCoord1d

    Parameters
    ----------

    target : int
      Passed on as it is.

    s : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glMultiTexCoord1d(GLenum target, GLdouble
    #      s)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_517glMultiTexCoord1dEjd', target, s,
    )

  @overload(int)
  def glClientActiveTexture(self, texture: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glClientActiveTexture(GLenum
    texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glClientActiveTexture

    Parameters
    ----------

    texture : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glClientActiveTexture(GLenum texture)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_521glClientActiveTextureEj', texture,
    )

  @overload(int, int, int)
  def glWindowPos3s(self, x: int, y: int, z: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glWindowPos3s(GLshort x, GLshort
    y, GLshort z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glWindowPos3s

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    z : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glWindowPos3s(GLshort x, GLshort y, GLshort
    #      z)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_513glWindowPos3sEsss', x, y, z,
    )

  @overload(int, int, int)
  def glWindowPos3i(self, x: int, y: int, z: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glWindowPos3i(GLint x, GLint y,
    GLint z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glWindowPos3i

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    z : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glWindowPos3i(GLint x, GLint y, GLint z)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_513glWindowPos3iEiii', x, y, z,
    )

  @overload(float, float, float)
  def glWindowPos3f(self, x: float, y: float, z: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glWindowPos3f(GLfloat x, GLfloat
    y, GLfloat z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glWindowPos3f

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glWindowPos3f(GLfloat x, GLfloat y, GLfloat
    #      z)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_513glWindowPos3fEfff', x, y, z,
    )

  @overload(float, float, float)
  def glWindowPos3d(self, x: float, y: float, z: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glWindowPos3d(GLdouble x, GLdouble
    y, GLdouble z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glWindowPos3d

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glWindowPos3d(GLdouble x, GLdouble y,
    #      GLdouble z)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_513glWindowPos3dEddd', x, y, z,
    )

  @overload(int, int)
  def glWindowPos2s(self, x: int, y: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glWindowPos2s(GLshort x, GLshort
    y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glWindowPos2s

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glWindowPos2s(GLshort x, GLshort y)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_513glWindowPos2sEss', x, y,
    )

  @overload(int, int)
  def glWindowPos2i(self, x: int, y: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glWindowPos2i(GLint x, GLint y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glWindowPos2i

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glWindowPos2i(GLint x, GLint y)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_513glWindowPos2iEii', x, y,
    )

  @overload(float, float)
  def glWindowPos2f(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glWindowPos2f(GLfloat x, GLfloat
    y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glWindowPos2f

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glWindowPos2f(GLfloat x, GLfloat y)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_513glWindowPos2fEff', x, y,
    )

  @overload(float, float)
  def glWindowPos2d(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glWindowPos2d(GLdouble x, GLdouble
    y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glWindowPos2d

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glWindowPos2d(GLdouble x, GLdouble y)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_513glWindowPos2dEdd', x, y,
    )

  @overload(int, int, int)
  def glSecondaryColor3us(self, red: int, green: int, blue: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glSecondaryColor3us(GLushort red,
    GLushort green, GLushort blue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glSecondaryColor3us

    Parameters
    ----------

    red : int
      Passed on as it is.

    green : int
      Passed on as it is.

    blue : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glSecondaryColor3us(GLushort red, GLushort
    #      green, GLushort blue)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_519glSecondaryColor3usEttt',
        red, green, blue,
    )

  @overload(int, int, int)
  def glSecondaryColor3ui(self, red: int, green: int, blue: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glSecondaryColor3ui(GLuint red,
    GLuint green, GLuint blue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glSecondaryColor3ui

    Parameters
    ----------

    red : int
      Passed on as it is.

    green : int
      Passed on as it is.

    blue : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glSecondaryColor3ui(GLuint red, GLuint
    #      green, GLuint blue)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_519glSecondaryColor3uiEjjj',
        red, green, blue,
    )

  @overload(int, int, int)
  def glSecondaryColor3ub(self, red: int, green: int, blue: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glSecondaryColor3ub(GLubyte red,
    GLubyte green, GLubyte blue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glSecondaryColor3ub

    Parameters
    ----------

    red : int
      Passed on as it is.

    green : int
      Passed on as it is.

    blue : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glSecondaryColor3ub(GLubyte red, GLubyte
    #      green, GLubyte blue)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_519glSecondaryColor3ubEhhh',
        red, green, blue,
    )

  @overload(int, int, int)
  def glSecondaryColor3s(self, red: int, green: int, blue: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glSecondaryColor3s(GLshort red,
    GLshort green, GLshort blue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glSecondaryColor3s

    Parameters
    ----------

    red : int
      Passed on as it is.

    green : int
      Passed on as it is.

    blue : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glSecondaryColor3s(GLshort red, GLshort
    #      green, GLshort blue)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_518glSecondaryColor3sEsss',
        red, green, blue,
    )

  @overload(int, int, int)
  def glSecondaryColor3i(self, red: int, green: int, blue: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glSecondaryColor3i(GLint red,
    GLint green, GLint blue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glSecondaryColor3i

    Parameters
    ----------

    red : int
      Passed on as it is.

    green : int
      Passed on as it is.

    blue : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glSecondaryColor3i(GLint red, GLint green,
    #      GLint blue)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_518glSecondaryColor3iEiii',
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
    Calls Qt's 'void QOpenGLFunctions_1_5::glSecondaryColor3f(GLfloat red,
    GLfloat green, GLfloat blue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glSecondaryColor3f

    Parameters
    ----------

    red : float
      Passed on as it is.

    green : float
      Passed on as it is.

    blue : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glSecondaryColor3f(GLfloat red, GLfloat
    #      green, GLfloat blue)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_518glSecondaryColor3fEfff',
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
    Calls Qt's 'void QOpenGLFunctions_1_5::glSecondaryColor3d(GLdouble red,
    GLdouble green, GLdouble blue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glSecondaryColor3d

    Parameters
    ----------

    red : float
      Passed on as it is.

    green : float
      Passed on as it is.

    blue : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glSecondaryColor3d(GLdouble red, GLdouble
    #      green, GLdouble blue)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_518glSecondaryColor3dEddd',
        red, green, blue,
    )

  @overload(int, int, int)
  def glSecondaryColor3b(self, red: int, green: int, blue: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glSecondaryColor3b(GLbyte red,
    GLbyte green, GLbyte blue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glSecondaryColor3b

    Parameters
    ----------

    red : int
      Passed on as it is.

    green : int
      Passed on as it is.

    blue : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glSecondaryColor3b(GLbyte red, GLbyte
    #      green, GLbyte blue)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_518glSecondaryColor3bEaaa',
        red, green, blue,
    )

  @overload(float)
  def glFogCoordd(self, coord: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glFogCoordd(GLdouble coord)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glFogCoordd

    Parameters
    ----------

    coord : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glFogCoordd(GLdouble coord)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_511glFogCoorddEd', coord,
    )

  @overload(float)
  def glFogCoordf(self, coord: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_5::glFogCoordf(GLfloat coord)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_5.html#glFogCoordf

    Parameters
    ----------

    coord : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_5::glFogCoordf(GLfloat coord)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_511glFogCoordfEf', coord,
    )

  @staticmethod
  def glAreTexturesResident(*__, **_) -> Never:
    """
    Qt's 'GLboolean QOpenGLFunctions_1_5::glAreTexturesResident(GLsizei n,
    const GLuint *textures, GLboolean *residences)': names 'GLuint', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glAreTexturesResident' has no cute function "
        "yet. Qt's 'GLboolean "
        "QOpenGLFunctions_1_5::glAreTexturesResident(GLsizei n, const "
        "GLuint *textures, GLboolean *residences)': names 'GLuint', which "
        "has no cute class yet.")

  @staticmethod
  def glBitmap(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glBitmap(GLsizei width, GLsizei height,
    GLfloat xorig, GLfloat yorig, GLfloat xmove, GLfloat ymove, const GLubyte
    *bitmap)': names 'GLubyte', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glBitmap' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glBitmap(GLsizei width, GLsizei "
        "height, GLfloat xorig, GLfloat yorig, GLfloat xmove, GLfloat "
        "ymove, const GLubyte *bitmap)': names 'GLubyte', which has no cute "
        "class yet.")

  @staticmethod
  def glBufferData(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glBufferData(GLenum target, GLsizeiptr
    size, const GLvoid *data, GLenum usage)': names 'GLvoid', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glBufferData' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glBufferData(GLenum target, GLsizeiptr "
        "size, const GLvoid *data, GLenum usage)': names 'GLvoid', which "
        "has no cute class yet.")

  @staticmethod
  def glBufferSubData(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glBufferSubData(GLenum target, GLintptr
    offset, GLsizeiptr size, const GLvoid *data)': names 'GLvoid', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glBufferSubData' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glBufferSubData(GLenum target, "
        "GLintptr offset, GLsizeiptr size, const GLvoid *data)': names "
        "'GLvoid', which has no cute class yet.")

  @staticmethod
  def glCallLists(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glCallLists(GLsizei n, GLenum type,
    const GLvoid *lists)': names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glCallLists' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glCallLists(GLsizei n, GLenum type, "
        "const GLvoid *lists)': names 'GLvoid', which has no cute class yet."
    )

  @staticmethod
  def glClipPlane(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glClipPlane(GLenum plane, const GLdouble
    *equation)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glClipPlane' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glClipPlane(GLenum plane, const "
        "GLdouble *equation)': names 'GLdouble', which has no cute class "
        "yet.")

  @staticmethod
  def glColor3bv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glColor3bv(const GLbyte *v)': names
    'GLbyte', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glColor3bv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glColor3bv(const GLbyte *v)': names "
        "'GLbyte', which has no cute class yet.")

  @staticmethod
  def glColor3dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glColor3dv(const GLdouble *v)': names
    'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glColor3dv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glColor3dv(const GLdouble *v)': names "
        "'GLdouble', which has no cute class yet.")

  @staticmethod
  def glColor3fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glColor3fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glColor3fv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glColor3fv(const GLfloat *v)': names "
        "'GLfloat', which has no cute class yet.")

  @staticmethod
  def glColor3iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glColor3iv(const GLint *v)': names
    'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glColor3iv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glColor3iv(const GLint *v)': names "
        "'GLint', which has no cute class yet.")

  @staticmethod
  def glColor3sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glColor3sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glColor3sv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glColor3sv(const GLshort *v)': names "
        "'GLshort', which has no cute class yet.")

  @staticmethod
  def glColor3ubv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glColor3ubv(const GLubyte *v)': names
    'GLubyte', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glColor3ubv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glColor3ubv(const GLubyte *v)': names "
        "'GLubyte', which has no cute class yet.")

  @staticmethod
  def glColor3uiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glColor3uiv(const GLuint *v)': names
    'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glColor3uiv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glColor3uiv(const GLuint *v)': names "
        "'GLuint', which has no cute class yet.")

  @staticmethod
  def glColor3usv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glColor3usv(const GLushort *v)': names
    'GLushort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glColor3usv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glColor3usv(const GLushort *v)': names "
        "'GLushort', which has no cute class yet.")

  @staticmethod
  def glColor4bv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glColor4bv(const GLbyte *v)': names
    'GLbyte', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glColor4bv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glColor4bv(const GLbyte *v)': names "
        "'GLbyte', which has no cute class yet.")

  @staticmethod
  def glColor4dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glColor4dv(const GLdouble *v)': names
    'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glColor4dv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glColor4dv(const GLdouble *v)': names "
        "'GLdouble', which has no cute class yet.")

  @staticmethod
  def glColor4fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glColor4fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glColor4fv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glColor4fv(const GLfloat *v)': names "
        "'GLfloat', which has no cute class yet.")

  @staticmethod
  def glColor4iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glColor4iv(const GLint *v)': names
    'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glColor4iv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glColor4iv(const GLint *v)': names "
        "'GLint', which has no cute class yet.")

  @staticmethod
  def glColor4sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glColor4sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glColor4sv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glColor4sv(const GLshort *v)': names "
        "'GLshort', which has no cute class yet.")

  @staticmethod
  def glColor4ubv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glColor4ubv(const GLubyte *v)': names
    'GLubyte', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glColor4ubv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glColor4ubv(const GLubyte *v)': names "
        "'GLubyte', which has no cute class yet.")

  @staticmethod
  def glColor4uiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glColor4uiv(const GLuint *v)': names
    'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glColor4uiv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glColor4uiv(const GLuint *v)': names "
        "'GLuint', which has no cute class yet.")

  @staticmethod
  def glColor4usv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glColor4usv(const GLushort *v)': names
    'GLushort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glColor4usv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glColor4usv(const GLushort *v)': names "
        "'GLushort', which has no cute class yet.")

  @staticmethod
  def glColorPointer(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glColorPointer(GLint size, GLenum type,
    GLsizei stride, const GLvoid *pointer)': names 'GLvoid', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glColorPointer' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glColorPointer(GLint size, GLenum "
        "type, GLsizei stride, const GLvoid *pointer)': names 'GLvoid', "
        "which has no cute class yet.")

  @staticmethod
  def glColorSubTable(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glColorSubTable(GLenum target, GLsizei
    start, GLsizei count, GLenum format, GLenum type, const GLvoid *data)':
    names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glColorSubTable' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glColorSubTable(GLenum target, "
        "GLsizei start, GLsizei count, GLenum format, GLenum type, const "
        "GLvoid *data)': names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glColorTable(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glColorTable(GLenum target, GLenum
    internalformat, GLsizei width, GLenum format, GLenum type, const GLvoid
    *table)': names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glColorTable' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glColorTable(GLenum target, GLenum "
        "internalformat, GLsizei width, GLenum format, GLenum type, const "
        "GLvoid *table)': names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glColorTableParameterfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glColorTableParameterfv(GLenum target,
    GLenum pname, const GLfloat *params)': names 'GLfloat', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glColorTableParameterfv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_1_5::glColorTableParameterfv(GLenum target, "
        "GLenum pname, const GLfloat *params)': names 'GLfloat', which has "
        "no cute class yet.")

  @staticmethod
  def glColorTableParameteriv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glColorTableParameteriv(GLenum target,
    GLenum pname, const GLint *params)': names 'GLint', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glColorTableParameteriv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_1_5::glColorTableParameteriv(GLenum target, "
        "GLenum pname, const GLint *params)': names 'GLint', which has no "
        "cute class yet.")

  @staticmethod
  def glCompressedTexImage1D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glCompressedTexImage1D(GLenum target,
    GLint level, GLenum internalformat, GLsizei width, GLint border, GLsizei
    imageSize, const GLvoid *data)': names 'GLvoid', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glCompressedTexImage1D' has no cute function "
        "yet. Qt's 'void "
        "QOpenGLFunctions_1_5::glCompressedTexImage1D(GLenum target, GLint "
        "level, GLenum internalformat, GLsizei width, GLint border, GLsizei "
        "imageSize, const GLvoid *data)': names 'GLvoid', which has no cute "
        "class yet.")

  @staticmethod
  def glCompressedTexImage2D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glCompressedTexImage2D(GLenum target,
    GLint level, GLenum internalformat, GLsizei width, GLsizei height, GLint
    border, GLsizei imageSize, const GLvoid *data)': names 'GLvoid', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glCompressedTexImage2D' has no cute function "
        "yet. Qt's 'void "
        "QOpenGLFunctions_1_5::glCompressedTexImage2D(GLenum target, GLint "
        "level, GLenum internalformat, GLsizei width, GLsizei height, GLint "
        "border, GLsizei imageSize, const GLvoid *data)': names 'GLvoid', "
        "which has no cute class yet.")

  @staticmethod
  def glCompressedTexImage3D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glCompressedTexImage3D(GLenum target,
    GLint level, GLenum internalformat, GLsizei width, GLsizei height,
    GLsizei depth, GLint border, GLsizei imageSize, const GLvoid *data)':
    names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glCompressedTexImage3D' has no cute function "
        "yet. Qt's 'void "
        "QOpenGLFunctions_1_5::glCompressedTexImage3D(GLenum target, GLint "
        "level, GLenum internalformat, GLsizei width, GLsizei height, "
        "GLsizei depth, GLint border, GLsizei imageSize, const GLvoid "
        "*data)': names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glCompressedTexSubImage1D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glCompressedTexSubImage1D(GLenum target,
    GLint level, GLint xoffset, GLsizei width, GLenum format, GLsizei
    imageSize, const GLvoid *data)': names 'GLvoid', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glCompressedTexSubImage1D' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_1_5::glCompressedTexSubImage1D(GLenum target, "
        "GLint level, GLint xoffset, GLsizei width, GLenum format, GLsizei "
        "imageSize, const GLvoid *data)': names 'GLvoid', which has no cute "
        "class yet.")

  @staticmethod
  def glCompressedTexSubImage2D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glCompressedTexSubImage2D(GLenum target,
    GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height,
    GLenum format, GLsizei imageSize, const GLvoid *data)': names 'GLvoid',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glCompressedTexSubImage2D' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_1_5::glCompressedTexSubImage2D(GLenum target, "
        "GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei "
        "height, GLenum format, GLsizei imageSize, const GLvoid *data)': "
        "names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glCompressedTexSubImage3D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glCompressedTexSubImage3D(GLenum target,
    GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width,
    GLsizei height, GLsizei depth, GLenum format, GLsizei imageSize, const
    GLvoid *data)': names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glCompressedTexSubImage3D' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_1_5::glCompressedTexSubImage3D(GLenum target, "
        "GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei "
        "width, GLsizei height, GLsizei depth, GLenum format, GLsizei "
        "imageSize, const GLvoid *data)': names 'GLvoid', which has no cute "
        "class yet.")

  @staticmethod
  def glConvolutionFilter1D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glConvolutionFilter1D(GLenum target,
    GLenum internalformat, GLsizei width, GLenum format, GLenum type, const
    GLvoid *image)': names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glConvolutionFilter1D' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_1_5::glConvolutionFilter1D(GLenum "
        "target, GLenum internalformat, GLsizei width, GLenum format, "
        "GLenum type, const GLvoid *image)': names 'GLvoid', which has no "
        "cute class yet.")

  @staticmethod
  def glConvolutionFilter2D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glConvolutionFilter2D(GLenum target,
    GLenum internalformat, GLsizei width, GLsizei height, GLenum format,
    GLenum type, const GLvoid *image)': names 'GLvoid', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glConvolutionFilter2D' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_1_5::glConvolutionFilter2D(GLenum "
        "target, GLenum internalformat, GLsizei width, GLsizei height, "
        "GLenum format, GLenum type, const GLvoid *image)': names 'GLvoid', "
        "which has no cute class yet.")

  @staticmethod
  def glConvolutionParameterfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glConvolutionParameterfv(GLenum target,
    GLenum pname, const GLfloat *params)': names 'GLfloat', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glConvolutionParameterfv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_1_5::glConvolutionParameterfv(GLenum target, "
        "GLenum pname, const GLfloat *params)': names 'GLfloat', which has "
        "no cute class yet.")

  @staticmethod
  def glConvolutionParameteriv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glConvolutionParameteriv(GLenum target,
    GLenum pname, const GLint *params)': names 'GLint', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glConvolutionParameteriv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_1_5::glConvolutionParameteriv(GLenum target, "
        "GLenum pname, const GLint *params)': names 'GLint', which has no "
        "cute class yet.")

  @staticmethod
  def glDeleteBuffers(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glDeleteBuffers(GLsizei n, const GLuint
    *buffers)': names 'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glDeleteBuffers' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glDeleteBuffers(GLsizei n, const "
        "GLuint *buffers)': names 'GLuint', which has no cute class yet.")

  @staticmethod
  def glDeleteQueries(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glDeleteQueries(GLsizei n, const GLuint
    *ids)': names 'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glDeleteQueries' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glDeleteQueries(GLsizei n, const "
        "GLuint *ids)': names 'GLuint', which has no cute class yet.")

  @staticmethod
  def glDeleteTextures(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glDeleteTextures(GLsizei n, const GLuint
    *textures)': names 'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glDeleteTextures' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glDeleteTextures(GLsizei n, const "
        "GLuint *textures)': names 'GLuint', which has no cute class yet.")

  @staticmethod
  def glDrawElements(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glDrawElements(GLenum mode, GLsizei
    count, GLenum type, const GLvoid *indices)': names 'GLvoid', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glDrawElements' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glDrawElements(GLenum mode, "
        "GLsizei count, GLenum type, const GLvoid *indices)': names "
        "'GLvoid', which has no cute class yet.")

  @staticmethod
  def glDrawPixels(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glDrawPixels(GLsizei width, GLsizei
    height, GLenum format, GLenum type, const GLvoid *pixels)': names
    'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glDrawPixels' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glDrawPixels(GLsizei width, GLsizei "
        "height, GLenum format, GLenum type, const GLvoid *pixels)': names "
        "'GLvoid', which has no cute class yet.")

  @staticmethod
  def glDrawRangeElements(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glDrawRangeElements(GLenum mode, GLuint
    start, GLuint end, GLsizei count, GLenum type, const GLvoid *indices)':
    names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glDrawRangeElements' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_1_5::glDrawRangeElements(GLenum "
        "mode, GLuint start, GLuint end, GLsizei count, GLenum type, const "
        "GLvoid *indices)': names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glEdgeFlagPointer(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glEdgeFlagPointer(GLsizei stride, const
    GLvoid *pointer)': names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glEdgeFlagPointer' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glEdgeFlagPointer(GLsizei stride, "
        "const GLvoid *pointer)': names 'GLvoid', which has no cute class "
        "yet.")

  @staticmethod
  def glEdgeFlagv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glEdgeFlagv(const GLboolean *flag)':
    names 'GLboolean', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glEdgeFlagv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glEdgeFlagv(const GLboolean *flag)': "
        "names 'GLboolean', which has no cute class yet.")

  @staticmethod
  def glEvalCoord1dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glEvalCoord1dv(const GLdouble *u)':
    names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glEvalCoord1dv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glEvalCoord1dv(const GLdouble "
        "*u)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glEvalCoord1fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glEvalCoord1fv(const GLfloat *u)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glEvalCoord1fv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glEvalCoord1fv(const GLfloat "
        "*u)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glEvalCoord2dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glEvalCoord2dv(const GLdouble *u)':
    names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glEvalCoord2dv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glEvalCoord2dv(const GLdouble "
        "*u)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glEvalCoord2fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glEvalCoord2fv(const GLfloat *u)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glEvalCoord2fv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glEvalCoord2fv(const GLfloat "
        "*u)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glFeedbackBuffer(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glFeedbackBuffer(GLsizei size, GLenum
    type, GLfloat *buffer)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glFeedbackBuffer' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glFeedbackBuffer(GLsizei size, "
        "GLenum type, GLfloat *buffer)': takes a number to change where it "
        "is.")

  @staticmethod
  def glFogCoordPointer(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glFogCoordPointer(GLenum type, GLsizei
    stride, const GLvoid *pointer)': names 'GLvoid', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glFogCoordPointer' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glFogCoordPointer(GLenum type, "
        "GLsizei stride, const GLvoid *pointer)': names 'GLvoid', which has "
        "no cute class yet.")

  @staticmethod
  def glFogCoorddv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glFogCoorddv(const GLdouble *coord)':
    names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glFogCoorddv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glFogCoorddv(const GLdouble *coord)': "
        "names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glFogCoordfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glFogCoordfv(const GLfloat *coord)':
    names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glFogCoordfv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glFogCoordfv(const GLfloat *coord)': "
        "names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glFogfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glFogfv(GLenum pname, const GLfloat
    *params)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glFogfv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glFogfv(GLenum pname, const GLfloat "
        "*params)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glFogiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glFogiv(GLenum pname, const GLint
    *params)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glFogiv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glFogiv(GLenum pname, const GLint "
        "*params)': names 'GLint', which has no cute class yet.")

  @staticmethod
  def glGenBuffers(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glGenBuffers(GLsizei n, GLuint
    *buffers)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glGenBuffers' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glGenBuffers(GLsizei n, GLuint "
        "*buffers)': takes a number to change where it is.")

  @staticmethod
  def glGenQueries(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glGenQueries(GLsizei n, GLuint *ids)':
    takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glGenQueries' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glGenQueries(GLsizei n, GLuint *ids)': "
        "takes a number to change where it is.")

  @staticmethod
  def glGenTextures(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glGenTextures(GLsizei n, GLuint
    *textures)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glGenTextures' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glGenTextures(GLsizei n, GLuint "
        "*textures)': takes a number to change where it is.")

  @staticmethod
  def glGetBooleanv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glGetBooleanv(GLenum pname, GLboolean
    *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glGetBooleanv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glGetBooleanv(GLenum pname, "
        "GLboolean *params)': takes a number to change where it is.")

  @staticmethod
  def glGetBufferParameteriv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glGetBufferParameteriv(GLenum target,
    GLenum pname, GLint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glGetBufferParameteriv' has no cute function "
        "yet. Qt's 'void "
        "QOpenGLFunctions_1_5::glGetBufferParameteriv(GLenum target, GLenum "
        "pname, GLint *params)': takes a number to change where it is.")

  @staticmethod
  def glGetBufferPointerv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glGetBufferPointerv(GLenum target,
    GLenum pname, GLvoid **params)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glGetBufferPointerv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_1_5::glGetBufferPointerv(GLenum "
        "target, GLenum pname, GLvoid **params)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def glGetBufferSubData(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glGetBufferSubData(GLenum target,
    GLintptr offset, GLsizeiptr size, GLvoid *data)': names 'GLvoid', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glGetBufferSubData' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_1_5::glGetBufferSubData(GLenum "
        "target, GLintptr offset, GLsizeiptr size, GLvoid *data)': names "
        "'GLvoid', which has no cute class yet.")

  @staticmethod
  def glGetClipPlane(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glGetClipPlane(GLenum plane, GLdouble
    *equation)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glGetClipPlane' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glGetClipPlane(GLenum plane, "
        "GLdouble *equation)': takes a number to change where it is.")

  @staticmethod
  def glGetColorTable(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glGetColorTable(GLenum target, GLenum
    format, GLenum type, GLvoid *table)': names 'GLvoid', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glGetColorTable' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glGetColorTable(GLenum target, "
        "GLenum format, GLenum type, GLvoid *table)': names 'GLvoid', which "
        "has no cute class yet.")

  @staticmethod
  def glGetColorTableParameterfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glGetColorTableParameterfv(GLenum
    target, GLenum pname, GLfloat *params)': takes a number to change where
    it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glGetColorTableParameterfv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_1_5::glGetColorTableParameterfv(GLenum target, "
        "GLenum pname, GLfloat *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetColorTableParameteriv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glGetColorTableParameteriv(GLenum
    target, GLenum pname, GLint *params)': takes a number to change where it
    is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glGetColorTableParameteriv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_1_5::glGetColorTableParameteriv(GLenum target, "
        "GLenum pname, GLint *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetCompressedTexImage(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glGetCompressedTexImage(GLenum target,
    GLint level, GLvoid *img)': names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glGetCompressedTexImage' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_1_5::glGetCompressedTexImage(GLenum target, GLint "
        "level, GLvoid *img)': names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glGetConvolutionFilter(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glGetConvolutionFilter(GLenum target,
    GLenum format, GLenum type, GLvoid *image)': names 'GLvoid', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glGetConvolutionFilter' has no cute function "
        "yet. Qt's 'void "
        "QOpenGLFunctions_1_5::glGetConvolutionFilter(GLenum target, GLenum "
        "format, GLenum type, GLvoid *image)': names 'GLvoid', which has no "
        "cute class yet.")

  @staticmethod
  def glGetConvolutionParameterfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glGetConvolutionParameterfv(GLenum
    target, GLenum pname, GLfloat *params)': takes a number to change where
    it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glGetConvolutionParameterfv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_1_5::glGetConvolutionParameterfv(GLenum target, "
        "GLenum pname, GLfloat *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetConvolutionParameteriv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glGetConvolutionParameteriv(GLenum
    target, GLenum pname, GLint *params)': takes a number to change where it
    is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glGetConvolutionParameteriv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_1_5::glGetConvolutionParameteriv(GLenum target, "
        "GLenum pname, GLint *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetDoublev(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glGetDoublev(GLenum pname, GLdouble
    *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glGetDoublev' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glGetDoublev(GLenum pname, GLdouble "
        "*params)': takes a number to change where it is.")

  @staticmethod
  def glGetFloatv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glGetFloatv(GLenum pname, GLfloat
    *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glGetFloatv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glGetFloatv(GLenum pname, GLfloat "
        "*params)': takes a number to change where it is.")

  @staticmethod
  def glGetHistogram(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glGetHistogram(GLenum target, GLboolean
    reset, GLenum format, GLenum type, GLvoid *values)': names 'GLvoid',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glGetHistogram' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glGetHistogram(GLenum target, "
        "GLboolean reset, GLenum format, GLenum type, GLvoid *values)': "
        "names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glGetHistogramParameterfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glGetHistogramParameterfv(GLenum target,
    GLenum pname, GLfloat *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glGetHistogramParameterfv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_1_5::glGetHistogramParameterfv(GLenum target, "
        "GLenum pname, GLfloat *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetHistogramParameteriv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glGetHistogramParameteriv(GLenum target,
    GLenum pname, GLint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glGetHistogramParameteriv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_1_5::glGetHistogramParameteriv(GLenum target, "
        "GLenum pname, GLint *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetIntegerv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glGetIntegerv(GLenum pname, GLint
    *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glGetIntegerv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glGetIntegerv(GLenum pname, GLint "
        "*params)': takes a number to change where it is.")

  @staticmethod
  def glGetLightfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glGetLightfv(GLenum light, GLenum pname,
    GLfloat *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glGetLightfv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glGetLightfv(GLenum light, GLenum "
        "pname, GLfloat *params)': takes a number to change where it is.")

  @staticmethod
  def glGetLightiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glGetLightiv(GLenum light, GLenum pname,
    GLint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glGetLightiv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glGetLightiv(GLenum light, GLenum "
        "pname, GLint *params)': takes a number to change where it is.")

  @staticmethod
  def glGetMapdv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glGetMapdv(GLenum target, GLenum query,
    GLdouble *v)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glGetMapdv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glGetMapdv(GLenum target, GLenum "
        "query, GLdouble *v)': takes a number to change where it is.")

  @staticmethod
  def glGetMapfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glGetMapfv(GLenum target, GLenum query,
    GLfloat *v)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glGetMapfv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glGetMapfv(GLenum target, GLenum "
        "query, GLfloat *v)': takes a number to change where it is.")

  @staticmethod
  def glGetMapiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glGetMapiv(GLenum target, GLenum query,
    GLint *v)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glGetMapiv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glGetMapiv(GLenum target, GLenum "
        "query, GLint *v)': takes a number to change where it is.")

  @staticmethod
  def glGetMaterialfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glGetMaterialfv(GLenum face, GLenum
    pname, GLfloat *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glGetMaterialfv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glGetMaterialfv(GLenum face, "
        "GLenum pname, GLfloat *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetMaterialiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glGetMaterialiv(GLenum face, GLenum
    pname, GLint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glGetMaterialiv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glGetMaterialiv(GLenum face, "
        "GLenum pname, GLint *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetMinmax(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glGetMinmax(GLenum target, GLboolean
    reset, GLenum format, GLenum type, GLvoid *values)': names 'GLvoid',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glGetMinmax' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glGetMinmax(GLenum target, GLboolean "
        "reset, GLenum format, GLenum type, GLvoid *values)': names "
        "'GLvoid', which has no cute class yet.")

  @staticmethod
  def glGetMinmaxParameterfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glGetMinmaxParameterfv(GLenum target,
    GLenum pname, GLfloat *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glGetMinmaxParameterfv' has no cute function "
        "yet. Qt's 'void "
        "QOpenGLFunctions_1_5::glGetMinmaxParameterfv(GLenum target, GLenum "
        "pname, GLfloat *params)': takes a number to change where it is.")

  @staticmethod
  def glGetMinmaxParameteriv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glGetMinmaxParameteriv(GLenum target,
    GLenum pname, GLint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glGetMinmaxParameteriv' has no cute function "
        "yet. Qt's 'void "
        "QOpenGLFunctions_1_5::glGetMinmaxParameteriv(GLenum target, GLenum "
        "pname, GLint *params)': takes a number to change where it is.")

  @staticmethod
  def glGetPixelMapfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glGetPixelMapfv(GLenum map, GLfloat
    *values)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glGetPixelMapfv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glGetPixelMapfv(GLenum map, "
        "GLfloat *values)': takes a number to change where it is.")

  @staticmethod
  def glGetPixelMapuiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glGetPixelMapuiv(GLenum map, GLuint
    *values)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glGetPixelMapuiv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glGetPixelMapuiv(GLenum map, "
        "GLuint *values)': takes a number to change where it is.")

  @staticmethod
  def glGetPixelMapusv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glGetPixelMapusv(GLenum map, GLushort
    *values)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glGetPixelMapusv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glGetPixelMapusv(GLenum map, "
        "GLushort *values)': takes a number to change where it is.")

  @staticmethod
  def glGetPointerv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glGetPointerv(GLenum pname, GLvoid
    **params)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glGetPointerv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glGetPointerv(GLenum pname, "
        "GLvoid **params)': takes a type Python has no way to hand over yet."
    )

  @staticmethod
  def glGetPolygonStipple(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glGetPolygonStipple(GLubyte *mask)':
    takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glGetPolygonStipple' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_1_5::glGetPolygonStipple(GLubyte "
        "*mask)': takes a number to change where it is.")

  @staticmethod
  def glGetQueryObjectiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glGetQueryObjectiv(GLuint id, GLenum
    pname, GLint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glGetQueryObjectiv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_1_5::glGetQueryObjectiv(GLuint "
        "id, GLenum pname, GLint *params)': takes a number to change where "
        "it is.")

  @staticmethod
  def glGetQueryObjectuiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glGetQueryObjectuiv(GLuint id, GLenum
    pname, GLuint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glGetQueryObjectuiv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_1_5::glGetQueryObjectuiv(GLuint "
        "id, GLenum pname, GLuint *params)': takes a number to change where "
        "it is.")

  @staticmethod
  def glGetQueryiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glGetQueryiv(GLenum target, GLenum
    pname, GLint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glGetQueryiv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glGetQueryiv(GLenum target, GLenum "
        "pname, GLint *params)': takes a number to change where it is.")

  @staticmethod
  def glGetSeparableFilter(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glGetSeparableFilter(GLenum target,
    GLenum format, GLenum type, GLvoid *row, GLvoid *column, GLvoid *span)':
    names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glGetSeparableFilter' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_1_5::glGetSeparableFilter(GLenum "
        "target, GLenum format, GLenum type, GLvoid *row, GLvoid *column, "
        "GLvoid *span)': names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glGetString(*__, **_) -> Never:
    """
    Qt's 'const GLubyte *QOpenGLFunctions_1_5::glGetString(GLenum name)':
    gives 'unsigned char', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glGetString' has no cute function yet. Qt's "
        "'const GLubyte *QOpenGLFunctions_1_5::glGetString(GLenum name)': "
        "gives 'unsigned char', which has no cute class yet.")

  @staticmethod
  def glGetTexEnvfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glGetTexEnvfv(GLenum target, GLenum
    pname, GLfloat *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glGetTexEnvfv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glGetTexEnvfv(GLenum target, "
        "GLenum pname, GLfloat *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetTexEnviv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glGetTexEnviv(GLenum target, GLenum
    pname, GLint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glGetTexEnviv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glGetTexEnviv(GLenum target, "
        "GLenum pname, GLint *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetTexGendv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glGetTexGendv(GLenum coord, GLenum
    pname, GLdouble *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glGetTexGendv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glGetTexGendv(GLenum coord, "
        "GLenum pname, GLdouble *params)': takes a number to change where "
        "it is.")

  @staticmethod
  def glGetTexGenfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glGetTexGenfv(GLenum coord, GLenum
    pname, GLfloat *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glGetTexGenfv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glGetTexGenfv(GLenum coord, "
        "GLenum pname, GLfloat *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetTexGeniv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glGetTexGeniv(GLenum coord, GLenum
    pname, GLint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glGetTexGeniv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glGetTexGeniv(GLenum coord, "
        "GLenum pname, GLint *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetTexImage(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glGetTexImage(GLenum target, GLint
    level, GLenum format, GLenum type, GLvoid *pixels)': names 'GLvoid',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glGetTexImage' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glGetTexImage(GLenum target, "
        "GLint level, GLenum format, GLenum type, GLvoid *pixels)': names "
        "'GLvoid', which has no cute class yet.")

  @staticmethod
  def glGetTexLevelParameterfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glGetTexLevelParameterfv(GLenum target,
    GLint level, GLenum pname, GLfloat *params)': takes a number to change
    where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glGetTexLevelParameterfv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_1_5::glGetTexLevelParameterfv(GLenum target, "
        "GLint level, GLenum pname, GLfloat *params)': takes a number to "
        "change where it is.")

  @staticmethod
  def glGetTexLevelParameteriv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glGetTexLevelParameteriv(GLenum target,
    GLint level, GLenum pname, GLint *params)': takes a number to change
    where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glGetTexLevelParameteriv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_1_5::glGetTexLevelParameteriv(GLenum target, "
        "GLint level, GLenum pname, GLint *params)': takes a number to "
        "change where it is.")

  @staticmethod
  def glGetTexParameterfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glGetTexParameterfv(GLenum target,
    GLenum pname, GLfloat *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glGetTexParameterfv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_1_5::glGetTexParameterfv(GLenum "
        "target, GLenum pname, GLfloat *params)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetTexParameteriv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glGetTexParameteriv(GLenum target,
    GLenum pname, GLint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glGetTexParameteriv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_1_5::glGetTexParameteriv(GLenum "
        "target, GLenum pname, GLint *params)': takes a number to change "
        "where it is.")

  @staticmethod
  def glIndexPointer(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glIndexPointer(GLenum type, GLsizei
    stride, const GLvoid *pointer)': names 'GLvoid', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glIndexPointer' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glIndexPointer(GLenum type, "
        "GLsizei stride, const GLvoid *pointer)': names 'GLvoid', which has "
        "no cute class yet.")

  @staticmethod
  def glIndexdv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glIndexdv(const GLdouble *c)': names
    'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glIndexdv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glIndexdv(const GLdouble *c)': names "
        "'GLdouble', which has no cute class yet.")

  @staticmethod
  def glIndexfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glIndexfv(const GLfloat *c)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glIndexfv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glIndexfv(const GLfloat *c)': names "
        "'GLfloat', which has no cute class yet.")

  @staticmethod
  def glIndexiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glIndexiv(const GLint *c)': names
    'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glIndexiv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glIndexiv(const GLint *c)': names "
        "'GLint', which has no cute class yet.")

  @staticmethod
  def glIndexsv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glIndexsv(const GLshort *c)': names
    'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glIndexsv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glIndexsv(const GLshort *c)': names "
        "'GLshort', which has no cute class yet.")

  @staticmethod
  def glIndexubv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glIndexubv(const GLubyte *c)': names
    'GLubyte', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glIndexubv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glIndexubv(const GLubyte *c)': names "
        "'GLubyte', which has no cute class yet.")

  @staticmethod
  def glInterleavedArrays(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glInterleavedArrays(GLenum format,
    GLsizei stride, const GLvoid *pointer)': names 'GLvoid', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glInterleavedArrays' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_1_5::glInterleavedArrays(GLenum "
        "format, GLsizei stride, const GLvoid *pointer)': names 'GLvoid', "
        "which has no cute class yet.")

  @staticmethod
  def glLightModelfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glLightModelfv(GLenum pname, const
    GLfloat *params)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glLightModelfv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glLightModelfv(GLenum pname, "
        "const GLfloat *params)': names 'GLfloat', which has no cute class "
        "yet.")

  @staticmethod
  def glLightModeliv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glLightModeliv(GLenum pname, const GLint
    *params)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glLightModeliv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glLightModeliv(GLenum pname, "
        "const GLint *params)': names 'GLint', which has no cute class yet.")

  @staticmethod
  def glLightfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glLightfv(GLenum light, GLenum pname,
    const GLfloat *params)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glLightfv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glLightfv(GLenum light, GLenum pname, "
        "const GLfloat *params)': names 'GLfloat', which has no cute class "
        "yet.")

  @staticmethod
  def glLightiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glLightiv(GLenum light, GLenum pname,
    const GLint *params)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glLightiv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glLightiv(GLenum light, GLenum pname, "
        "const GLint *params)': names 'GLint', which has no cute class yet.")

  @staticmethod
  def glLoadMatrixd(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glLoadMatrixd(const GLdouble *m)': names
    'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glLoadMatrixd' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glLoadMatrixd(const GLdouble "
        "*m)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glLoadMatrixf(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glLoadMatrixf(const GLfloat *m)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glLoadMatrixf' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glLoadMatrixf(const GLfloat *m)': "
        "names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glLoadTransposeMatrixd(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glLoadTransposeMatrixd(const GLdouble
    *m)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glLoadTransposeMatrixd' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_1_5::glLoadTransposeMatrixd(const "
        "GLdouble *m)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glLoadTransposeMatrixf(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glLoadTransposeMatrixf(const GLfloat
    *m)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glLoadTransposeMatrixf' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_1_5::glLoadTransposeMatrixf(const "
        "GLfloat *m)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glMap1d(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glMap1d(GLenum target, GLdouble u1,
    GLdouble u2, GLint stride, GLint order, const GLdouble *points)': names
    'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glMap1d' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glMap1d(GLenum target, GLdouble u1, "
        "GLdouble u2, GLint stride, GLint order, const GLdouble *points)': "
        "names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glMap1f(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glMap1f(GLenum target, GLfloat u1,
    GLfloat u2, GLint stride, GLint order, const GLfloat *points)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glMap1f' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glMap1f(GLenum target, GLfloat u1, "
        "GLfloat u2, GLint stride, GLint order, const GLfloat *points)': "
        "names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glMap2d(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glMap2d(GLenum target, GLdouble u1,
    GLdouble u2, GLint ustride, GLint uorder, GLdouble v1, GLdouble v2, GLint
    vstride, GLint vorder, const GLdouble *points)': names 'GLdouble', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glMap2d' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glMap2d(GLenum target, GLdouble u1, "
        "GLdouble u2, GLint ustride, GLint uorder, GLdouble v1, GLdouble "
        "v2, GLint vstride, GLint vorder, const GLdouble *points)': names "
        "'GLdouble', which has no cute class yet.")

  @staticmethod
  def glMap2f(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glMap2f(GLenum target, GLfloat u1,
    GLfloat u2, GLint ustride, GLint uorder, GLfloat v1, GLfloat v2, GLint
    vstride, GLint vorder, const GLfloat *points)': names 'GLfloat', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glMap2f' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glMap2f(GLenum target, GLfloat u1, "
        "GLfloat u2, GLint ustride, GLint uorder, GLfloat v1, GLfloat v2, "
        "GLint vstride, GLint vorder, const GLfloat *points)': names "
        "'GLfloat', which has no cute class yet.")

  @staticmethod
  def glMapBuffer(*__, **_) -> Never:
    """
    Qt's 'GLvoid *QOpenGLFunctions_1_5::glMapBuffer(GLenum target, GLenum
    access)': gives 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glMapBuffer' has no cute function yet. Qt's "
        "'GLvoid *QOpenGLFunctions_1_5::glMapBuffer(GLenum target, GLenum "
        "access)': gives 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glMaterialfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glMaterialfv(GLenum face, GLenum pname,
    const GLfloat *params)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glMaterialfv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glMaterialfv(GLenum face, GLenum "
        "pname, const GLfloat *params)': names 'GLfloat', which has no cute "
        "class yet.")

  @staticmethod
  def glMaterialiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glMaterialiv(GLenum face, GLenum pname,
    const GLint *params)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glMaterialiv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glMaterialiv(GLenum face, GLenum "
        "pname, const GLint *params)': names 'GLint', which has no cute "
        "class yet.")

  @staticmethod
  def glMultMatrixd(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glMultMatrixd(const GLdouble *m)': names
    'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glMultMatrixd' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glMultMatrixd(const GLdouble "
        "*m)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glMultMatrixf(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glMultMatrixf(const GLfloat *m)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glMultMatrixf' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glMultMatrixf(const GLfloat *m)': "
        "names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glMultTransposeMatrixd(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glMultTransposeMatrixd(const GLdouble
    *m)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glMultTransposeMatrixd' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_1_5::glMultTransposeMatrixd(const "
        "GLdouble *m)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glMultTransposeMatrixf(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glMultTransposeMatrixf(const GLfloat
    *m)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glMultTransposeMatrixf' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_1_5::glMultTransposeMatrixf(const "
        "GLfloat *m)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glMultiDrawArrays(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glMultiDrawArrays(GLenum mode, const
    GLint *first, const GLsizei *count, GLsizei drawcount)': names 'GLint',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glMultiDrawArrays' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glMultiDrawArrays(GLenum mode, "
        "const GLint *first, const GLsizei *count, GLsizei drawcount)': "
        "names 'GLint', which has no cute class yet.")

  @staticmethod
  def glMultiDrawElements(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glMultiDrawElements(GLenum mode, const
    GLsizei *count, GLenum type, const GLvoid *const *indices, GLsizei
    drawcount)': names 'GLsizei', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glMultiDrawElements' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_1_5::glMultiDrawElements(GLenum "
        "mode, const GLsizei *count, GLenum type, const GLvoid *const "
        "*indices, GLsizei drawcount)': names 'GLsizei', which has no cute "
        "class yet.")

  @staticmethod
  def glMultiTexCoord1dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glMultiTexCoord1dv(GLenum target, const
    GLdouble *v)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glMultiTexCoord1dv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_1_5::glMultiTexCoord1dv(GLenum "
        "target, const GLdouble *v)': names 'GLdouble', which has no cute "
        "class yet.")

  @staticmethod
  def glMultiTexCoord1fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glMultiTexCoord1fv(GLenum target, const
    GLfloat *v)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glMultiTexCoord1fv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_1_5::glMultiTexCoord1fv(GLenum "
        "target, const GLfloat *v)': names 'GLfloat', which has no cute "
        "class yet.")

  @staticmethod
  def glMultiTexCoord1iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glMultiTexCoord1iv(GLenum target, const
    GLint *v)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glMultiTexCoord1iv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_1_5::glMultiTexCoord1iv(GLenum "
        "target, const GLint *v)': names 'GLint', which has no cute class "
        "yet.")

  @staticmethod
  def glMultiTexCoord1sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glMultiTexCoord1sv(GLenum target, const
    GLshort *v)': names 'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glMultiTexCoord1sv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_1_5::glMultiTexCoord1sv(GLenum "
        "target, const GLshort *v)': names 'GLshort', which has no cute "
        "class yet.")

  @staticmethod
  def glMultiTexCoord2dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glMultiTexCoord2dv(GLenum target, const
    GLdouble *v)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glMultiTexCoord2dv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_1_5::glMultiTexCoord2dv(GLenum "
        "target, const GLdouble *v)': names 'GLdouble', which has no cute "
        "class yet.")

  @staticmethod
  def glMultiTexCoord2fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glMultiTexCoord2fv(GLenum target, const
    GLfloat *v)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glMultiTexCoord2fv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_1_5::glMultiTexCoord2fv(GLenum "
        "target, const GLfloat *v)': names 'GLfloat', which has no cute "
        "class yet.")

  @staticmethod
  def glMultiTexCoord2iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glMultiTexCoord2iv(GLenum target, const
    GLint *v)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glMultiTexCoord2iv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_1_5::glMultiTexCoord2iv(GLenum "
        "target, const GLint *v)': names 'GLint', which has no cute class "
        "yet.")

  @staticmethod
  def glMultiTexCoord2sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glMultiTexCoord2sv(GLenum target, const
    GLshort *v)': names 'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glMultiTexCoord2sv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_1_5::glMultiTexCoord2sv(GLenum "
        "target, const GLshort *v)': names 'GLshort', which has no cute "
        "class yet.")

  @staticmethod
  def glMultiTexCoord3dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glMultiTexCoord3dv(GLenum target, const
    GLdouble *v)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glMultiTexCoord3dv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_1_5::glMultiTexCoord3dv(GLenum "
        "target, const GLdouble *v)': names 'GLdouble', which has no cute "
        "class yet.")

  @staticmethod
  def glMultiTexCoord3fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glMultiTexCoord3fv(GLenum target, const
    GLfloat *v)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glMultiTexCoord3fv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_1_5::glMultiTexCoord3fv(GLenum "
        "target, const GLfloat *v)': names 'GLfloat', which has no cute "
        "class yet.")

  @staticmethod
  def glMultiTexCoord3iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glMultiTexCoord3iv(GLenum target, const
    GLint *v)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glMultiTexCoord3iv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_1_5::glMultiTexCoord3iv(GLenum "
        "target, const GLint *v)': names 'GLint', which has no cute class "
        "yet.")

  @staticmethod
  def glMultiTexCoord3sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glMultiTexCoord3sv(GLenum target, const
    GLshort *v)': names 'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glMultiTexCoord3sv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_1_5::glMultiTexCoord3sv(GLenum "
        "target, const GLshort *v)': names 'GLshort', which has no cute "
        "class yet.")

  @staticmethod
  def glMultiTexCoord4dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glMultiTexCoord4dv(GLenum target, const
    GLdouble *v)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glMultiTexCoord4dv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_1_5::glMultiTexCoord4dv(GLenum "
        "target, const GLdouble *v)': names 'GLdouble', which has no cute "
        "class yet.")

  @staticmethod
  def glMultiTexCoord4fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glMultiTexCoord4fv(GLenum target, const
    GLfloat *v)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glMultiTexCoord4fv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_1_5::glMultiTexCoord4fv(GLenum "
        "target, const GLfloat *v)': names 'GLfloat', which has no cute "
        "class yet.")

  @staticmethod
  def glMultiTexCoord4iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glMultiTexCoord4iv(GLenum target, const
    GLint *v)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glMultiTexCoord4iv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_1_5::glMultiTexCoord4iv(GLenum "
        "target, const GLint *v)': names 'GLint', which has no cute class "
        "yet.")

  @staticmethod
  def glMultiTexCoord4sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glMultiTexCoord4sv(GLenum target, const
    GLshort *v)': names 'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glMultiTexCoord4sv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_1_5::glMultiTexCoord4sv(GLenum "
        "target, const GLshort *v)': names 'GLshort', which has no cute "
        "class yet.")

  @staticmethod
  def glNormal3bv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glNormal3bv(const GLbyte *v)': names
    'GLbyte', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glNormal3bv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glNormal3bv(const GLbyte *v)': names "
        "'GLbyte', which has no cute class yet.")

  @staticmethod
  def glNormal3dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glNormal3dv(const GLdouble *v)': names
    'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glNormal3dv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glNormal3dv(const GLdouble *v)': names "
        "'GLdouble', which has no cute class yet.")

  @staticmethod
  def glNormal3fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glNormal3fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glNormal3fv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glNormal3fv(const GLfloat *v)': names "
        "'GLfloat', which has no cute class yet.")

  @staticmethod
  def glNormal3iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glNormal3iv(const GLint *v)': names
    'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glNormal3iv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glNormal3iv(const GLint *v)': names "
        "'GLint', which has no cute class yet.")

  @staticmethod
  def glNormal3sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glNormal3sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glNormal3sv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glNormal3sv(const GLshort *v)': names "
        "'GLshort', which has no cute class yet.")

  @staticmethod
  def glNormalPointer(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glNormalPointer(GLenum type, GLsizei
    stride, const GLvoid *pointer)': names 'GLvoid', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glNormalPointer' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glNormalPointer(GLenum type, "
        "GLsizei stride, const GLvoid *pointer)': names 'GLvoid', which has "
        "no cute class yet.")

  @staticmethod
  def glPixelMapfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glPixelMapfv(GLenum map, GLint mapsize,
    const GLfloat *values)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glPixelMapfv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glPixelMapfv(GLenum map, GLint "
        "mapsize, const GLfloat *values)': names 'GLfloat', which has no "
        "cute class yet.")

  @staticmethod
  def glPixelMapuiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glPixelMapuiv(GLenum map, GLint mapsize,
    const GLuint *values)': names 'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glPixelMapuiv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glPixelMapuiv(GLenum map, GLint "
        "mapsize, const GLuint *values)': names 'GLuint', which has no cute "
        "class yet.")

  @staticmethod
  def glPixelMapusv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glPixelMapusv(GLenum map, GLint mapsize,
    const GLushort *values)': names 'GLushort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glPixelMapusv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glPixelMapusv(GLenum map, GLint "
        "mapsize, const GLushort *values)': names 'GLushort', which has no "
        "cute class yet.")

  @staticmethod
  def glPointParameterfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glPointParameterfv(GLenum pname, const
    GLfloat *params)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glPointParameterfv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_1_5::glPointParameterfv(GLenum "
        "pname, const GLfloat *params)': names 'GLfloat', which has no cute "
        "class yet.")

  @staticmethod
  def glPointParameteriv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glPointParameteriv(GLenum pname, const
    GLint *params)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glPointParameteriv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_1_5::glPointParameteriv(GLenum "
        "pname, const GLint *params)': names 'GLint', which has no cute "
        "class yet.")

  @staticmethod
  def glPolygonStipple(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glPolygonStipple(const GLubyte *mask)':
    names 'GLubyte', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glPolygonStipple' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glPolygonStipple(const GLubyte "
        "*mask)': names 'GLubyte', which has no cute class yet.")

  @staticmethod
  def glPrioritizeTextures(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glPrioritizeTextures(GLsizei n, const
    GLuint *textures, const GLfloat *priorities)': names 'GLuint', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glPrioritizeTextures' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_1_5::glPrioritizeTextures(GLsizei "
        "n, const GLuint *textures, const GLfloat *priorities)': names "
        "'GLuint', which has no cute class yet.")

  @staticmethod
  def glRasterPos2dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glRasterPos2dv(const GLdouble *v)':
    names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glRasterPos2dv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glRasterPos2dv(const GLdouble "
        "*v)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glRasterPos2fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glRasterPos2fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glRasterPos2fv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glRasterPos2fv(const GLfloat "
        "*v)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glRasterPos2iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glRasterPos2iv(const GLint *v)': names
    'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glRasterPos2iv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glRasterPos2iv(const GLint *v)': "
        "names 'GLint', which has no cute class yet.")

  @staticmethod
  def glRasterPos2sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glRasterPos2sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glRasterPos2sv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glRasterPos2sv(const GLshort "
        "*v)': names 'GLshort', which has no cute class yet.")

  @staticmethod
  def glRasterPos3dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glRasterPos3dv(const GLdouble *v)':
    names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glRasterPos3dv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glRasterPos3dv(const GLdouble "
        "*v)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glRasterPos3fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glRasterPos3fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glRasterPos3fv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glRasterPos3fv(const GLfloat "
        "*v)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glRasterPos3iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glRasterPos3iv(const GLint *v)': names
    'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glRasterPos3iv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glRasterPos3iv(const GLint *v)': "
        "names 'GLint', which has no cute class yet.")

  @staticmethod
  def glRasterPos3sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glRasterPos3sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glRasterPos3sv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glRasterPos3sv(const GLshort "
        "*v)': names 'GLshort', which has no cute class yet.")

  @staticmethod
  def glRasterPos4dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glRasterPos4dv(const GLdouble *v)':
    names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glRasterPos4dv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glRasterPos4dv(const GLdouble "
        "*v)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glRasterPos4fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glRasterPos4fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glRasterPos4fv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glRasterPos4fv(const GLfloat "
        "*v)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glRasterPos4iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glRasterPos4iv(const GLint *v)': names
    'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glRasterPos4iv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glRasterPos4iv(const GLint *v)': "
        "names 'GLint', which has no cute class yet.")

  @staticmethod
  def glRasterPos4sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glRasterPos4sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glRasterPos4sv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glRasterPos4sv(const GLshort "
        "*v)': names 'GLshort', which has no cute class yet.")

  @staticmethod
  def glReadPixels(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glReadPixels(GLint x, GLint y, GLsizei
    width, GLsizei height, GLenum format, GLenum type, GLvoid *pixels)':
    names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glReadPixels' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glReadPixels(GLint x, GLint y, GLsizei "
        "width, GLsizei height, GLenum format, GLenum type, GLvoid "
        "*pixels)': names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glRectdv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glRectdv(const GLdouble *v1, const
    GLdouble *v2)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glRectdv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glRectdv(const GLdouble *v1, const "
        "GLdouble *v2)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glRectfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glRectfv(const GLfloat *v1, const
    GLfloat *v2)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glRectfv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glRectfv(const GLfloat *v1, const "
        "GLfloat *v2)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glRectiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glRectiv(const GLint *v1, const GLint
    *v2)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glRectiv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glRectiv(const GLint *v1, const GLint "
        "*v2)': names 'GLint', which has no cute class yet.")

  @staticmethod
  def glRectsv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glRectsv(const GLshort *v1, const
    GLshort *v2)': names 'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glRectsv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glRectsv(const GLshort *v1, const "
        "GLshort *v2)': names 'GLshort', which has no cute class yet.")

  @staticmethod
  def glSecondaryColor3bv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glSecondaryColor3bv(const GLbyte *v)':
    names 'GLbyte', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glSecondaryColor3bv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_1_5::glSecondaryColor3bv(const "
        "GLbyte *v)': names 'GLbyte', which has no cute class yet.")

  @staticmethod
  def glSecondaryColor3dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glSecondaryColor3dv(const GLdouble *v)':
    names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glSecondaryColor3dv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_1_5::glSecondaryColor3dv(const "
        "GLdouble *v)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glSecondaryColor3fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glSecondaryColor3fv(const GLfloat *v)':
    names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glSecondaryColor3fv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_1_5::glSecondaryColor3fv(const "
        "GLfloat *v)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glSecondaryColor3iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glSecondaryColor3iv(const GLint *v)':
    names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glSecondaryColor3iv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_1_5::glSecondaryColor3iv(const "
        "GLint *v)': names 'GLint', which has no cute class yet.")

  @staticmethod
  def glSecondaryColor3sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glSecondaryColor3sv(const GLshort *v)':
    names 'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glSecondaryColor3sv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_1_5::glSecondaryColor3sv(const "
        "GLshort *v)': names 'GLshort', which has no cute class yet.")

  @staticmethod
  def glSecondaryColor3ubv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glSecondaryColor3ubv(const GLubyte *v)':
    names 'GLubyte', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glSecondaryColor3ubv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_1_5::glSecondaryColor3ubv(const "
        "GLubyte *v)': names 'GLubyte', which has no cute class yet.")

  @staticmethod
  def glSecondaryColor3uiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glSecondaryColor3uiv(const GLuint *v)':
    names 'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glSecondaryColor3uiv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_1_5::glSecondaryColor3uiv(const "
        "GLuint *v)': names 'GLuint', which has no cute class yet.")

  @staticmethod
  def glSecondaryColor3usv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glSecondaryColor3usv(const GLushort
    *v)': names 'GLushort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glSecondaryColor3usv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_1_5::glSecondaryColor3usv(const "
        "GLushort *v)': names 'GLushort', which has no cute class yet.")

  @staticmethod
  def glSecondaryColorPointer(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glSecondaryColorPointer(GLint size,
    GLenum type, GLsizei stride, const GLvoid *pointer)': names 'GLvoid',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glSecondaryColorPointer' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_1_5::glSecondaryColorPointer(GLint size, GLenum "
        "type, GLsizei stride, const GLvoid *pointer)': names 'GLvoid', "
        "which has no cute class yet.")

  @staticmethod
  def glSelectBuffer(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glSelectBuffer(GLsizei size, GLuint
    *buffer)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glSelectBuffer' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glSelectBuffer(GLsizei size, "
        "GLuint *buffer)': takes a number to change where it is.")

  @staticmethod
  def glSeparableFilter2D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glSeparableFilter2D(GLenum target,
    GLenum internalformat, GLsizei width, GLsizei height, GLenum format,
    GLenum type, const GLvoid *row, const GLvoid *column)': names 'GLvoid',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glSeparableFilter2D' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_1_5::glSeparableFilter2D(GLenum "
        "target, GLenum internalformat, GLsizei width, GLsizei height, "
        "GLenum format, GLenum type, const GLvoid *row, const GLvoid "
        "*column)': names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glTexCoord1dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glTexCoord1dv(const GLdouble *v)': names
    'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glTexCoord1dv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glTexCoord1dv(const GLdouble "
        "*v)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glTexCoord1fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glTexCoord1fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glTexCoord1fv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glTexCoord1fv(const GLfloat *v)': "
        "names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glTexCoord1iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glTexCoord1iv(const GLint *v)': names
    'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glTexCoord1iv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glTexCoord1iv(const GLint *v)': "
        "names 'GLint', which has no cute class yet.")

  @staticmethod
  def glTexCoord1sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glTexCoord1sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glTexCoord1sv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glTexCoord1sv(const GLshort *v)': "
        "names 'GLshort', which has no cute class yet.")

  @staticmethod
  def glTexCoord2dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glTexCoord2dv(const GLdouble *v)': names
    'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glTexCoord2dv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glTexCoord2dv(const GLdouble "
        "*v)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glTexCoord2fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glTexCoord2fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glTexCoord2fv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glTexCoord2fv(const GLfloat *v)': "
        "names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glTexCoord2iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glTexCoord2iv(const GLint *v)': names
    'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glTexCoord2iv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glTexCoord2iv(const GLint *v)': "
        "names 'GLint', which has no cute class yet.")

  @staticmethod
  def glTexCoord2sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glTexCoord2sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glTexCoord2sv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glTexCoord2sv(const GLshort *v)': "
        "names 'GLshort', which has no cute class yet.")

  @staticmethod
  def glTexCoord3dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glTexCoord3dv(const GLdouble *v)': names
    'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glTexCoord3dv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glTexCoord3dv(const GLdouble "
        "*v)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glTexCoord3fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glTexCoord3fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glTexCoord3fv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glTexCoord3fv(const GLfloat *v)': "
        "names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glTexCoord3iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glTexCoord3iv(const GLint *v)': names
    'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glTexCoord3iv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glTexCoord3iv(const GLint *v)': "
        "names 'GLint', which has no cute class yet.")

  @staticmethod
  def glTexCoord3sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glTexCoord3sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glTexCoord3sv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glTexCoord3sv(const GLshort *v)': "
        "names 'GLshort', which has no cute class yet.")

  @staticmethod
  def glTexCoord4dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glTexCoord4dv(const GLdouble *v)': names
    'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glTexCoord4dv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glTexCoord4dv(const GLdouble "
        "*v)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glTexCoord4fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glTexCoord4fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glTexCoord4fv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glTexCoord4fv(const GLfloat *v)': "
        "names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glTexCoord4iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glTexCoord4iv(const GLint *v)': names
    'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glTexCoord4iv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glTexCoord4iv(const GLint *v)': "
        "names 'GLint', which has no cute class yet.")

  @staticmethod
  def glTexCoord4sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glTexCoord4sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glTexCoord4sv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glTexCoord4sv(const GLshort *v)': "
        "names 'GLshort', which has no cute class yet.")

  @staticmethod
  def glTexCoordPointer(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glTexCoordPointer(GLint size, GLenum
    type, GLsizei stride, const GLvoid *pointer)': names 'GLvoid', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glTexCoordPointer' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glTexCoordPointer(GLint size, "
        "GLenum type, GLsizei stride, const GLvoid *pointer)': names "
        "'GLvoid', which has no cute class yet.")

  @staticmethod
  def glTexEnvfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glTexEnvfv(GLenum target, GLenum pname,
    const GLfloat *params)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glTexEnvfv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glTexEnvfv(GLenum target, GLenum "
        "pname, const GLfloat *params)': names 'GLfloat', which has no cute "
        "class yet.")

  @staticmethod
  def glTexEnviv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glTexEnviv(GLenum target, GLenum pname,
    const GLint *params)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glTexEnviv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glTexEnviv(GLenum target, GLenum "
        "pname, const GLint *params)': names 'GLint', which has no cute "
        "class yet.")

  @staticmethod
  def glTexGendv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glTexGendv(GLenum coord, GLenum pname,
    const GLdouble *params)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glTexGendv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glTexGendv(GLenum coord, GLenum pname, "
        "const GLdouble *params)': names 'GLdouble', which has no cute "
        "class yet.")

  @staticmethod
  def glTexGenfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glTexGenfv(GLenum coord, GLenum pname,
    const GLfloat *params)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glTexGenfv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glTexGenfv(GLenum coord, GLenum pname, "
        "const GLfloat *params)': names 'GLfloat', which has no cute class "
        "yet.")

  @staticmethod
  def glTexGeniv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glTexGeniv(GLenum coord, GLenum pname,
    const GLint *params)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glTexGeniv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glTexGeniv(GLenum coord, GLenum pname, "
        "const GLint *params)': names 'GLint', which has no cute class yet.")

  @staticmethod
  def glTexImage1D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glTexImage1D(GLenum target, GLint level,
    GLint internalformat, GLsizei width, GLint border, GLenum format, GLenum
    type, const GLvoid *pixels)': names 'GLvoid', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glTexImage1D' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glTexImage1D(GLenum target, GLint "
        "level, GLint internalformat, GLsizei width, GLint border, GLenum "
        "format, GLenum type, const GLvoid *pixels)': names 'GLvoid', which "
        "has no cute class yet.")

  @staticmethod
  def glTexImage2D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glTexImage2D(GLenum target, GLint level,
    GLint internalformat, GLsizei width, GLsizei height, GLint border, GLenum
    format, GLenum type, const GLvoid *pixels)': names 'GLvoid', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glTexImage2D' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glTexImage2D(GLenum target, GLint "
        "level, GLint internalformat, GLsizei width, GLsizei height, GLint "
        "border, GLenum format, GLenum type, const GLvoid *pixels)': names "
        "'GLvoid', which has no cute class yet.")

  @staticmethod
  def glTexImage3D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glTexImage3D(GLenum target, GLint level,
    GLint internalformat, GLsizei width, GLsizei height, GLsizei depth, GLint
    border, GLenum format, GLenum type, const GLvoid *pixels)': names
    'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glTexImage3D' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glTexImage3D(GLenum target, GLint "
        "level, GLint internalformat, GLsizei width, GLsizei height, "
        "GLsizei depth, GLint border, GLenum format, GLenum type, const "
        "GLvoid *pixels)': names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glTexParameterfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glTexParameterfv(GLenum target, GLenum
    pname, const GLfloat *params)': names 'GLfloat', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glTexParameterfv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glTexParameterfv(GLenum target, "
        "GLenum pname, const GLfloat *params)': names 'GLfloat', which has "
        "no cute class yet.")

  @staticmethod
  def glTexParameteriv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glTexParameteriv(GLenum target, GLenum
    pname, const GLint *params)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glTexParameteriv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glTexParameteriv(GLenum target, "
        "GLenum pname, const GLint *params)': names 'GLint', which has no "
        "cute class yet.")

  @staticmethod
  def glTexSubImage1D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glTexSubImage1D(GLenum target, GLint
    level, GLint xoffset, GLsizei width, GLenum format, GLenum type, const
    GLvoid *pixels)': names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glTexSubImage1D' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glTexSubImage1D(GLenum target, "
        "GLint level, GLint xoffset, GLsizei width, GLenum format, GLenum "
        "type, const GLvoid *pixels)': names 'GLvoid', which has no cute "
        "class yet.")

  @staticmethod
  def glTexSubImage2D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glTexSubImage2D(GLenum target, GLint
    level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height,
    GLenum format, GLenum type, const GLvoid *pixels)': names 'GLvoid', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glTexSubImage2D' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glTexSubImage2D(GLenum target, "
        "GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei "
        "height, GLenum format, GLenum type, const GLvoid *pixels)': names "
        "'GLvoid', which has no cute class yet.")

  @staticmethod
  def glTexSubImage3D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glTexSubImage3D(GLenum target, GLint
    level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width,
    GLsizei height, GLsizei depth, GLenum format, GLenum type, const GLvoid
    *pixels)': names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glTexSubImage3D' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glTexSubImage3D(GLenum target, "
        "GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei "
        "width, GLsizei height, GLsizei depth, GLenum format, GLenum type, "
        "const GLvoid *pixels)': names 'GLvoid', which has no cute class "
        "yet.")

  @staticmethod
  def glVertex2dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glVertex2dv(const GLdouble *v)': names
    'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glVertex2dv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glVertex2dv(const GLdouble *v)': names "
        "'GLdouble', which has no cute class yet.")

  @staticmethod
  def glVertex2fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glVertex2fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glVertex2fv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glVertex2fv(const GLfloat *v)': names "
        "'GLfloat', which has no cute class yet.")

  @staticmethod
  def glVertex2iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glVertex2iv(const GLint *v)': names
    'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glVertex2iv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glVertex2iv(const GLint *v)': names "
        "'GLint', which has no cute class yet.")

  @staticmethod
  def glVertex2sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glVertex2sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glVertex2sv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glVertex2sv(const GLshort *v)': names "
        "'GLshort', which has no cute class yet.")

  @staticmethod
  def glVertex3dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glVertex3dv(const GLdouble *v)': names
    'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glVertex3dv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glVertex3dv(const GLdouble *v)': names "
        "'GLdouble', which has no cute class yet.")

  @staticmethod
  def glVertex3fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glVertex3fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glVertex3fv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glVertex3fv(const GLfloat *v)': names "
        "'GLfloat', which has no cute class yet.")

  @staticmethod
  def glVertex3iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glVertex3iv(const GLint *v)': names
    'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glVertex3iv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glVertex3iv(const GLint *v)': names "
        "'GLint', which has no cute class yet.")

  @staticmethod
  def glVertex3sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glVertex3sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glVertex3sv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glVertex3sv(const GLshort *v)': names "
        "'GLshort', which has no cute class yet.")

  @staticmethod
  def glVertex4dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glVertex4dv(const GLdouble *v)': names
    'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glVertex4dv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glVertex4dv(const GLdouble *v)': names "
        "'GLdouble', which has no cute class yet.")

  @staticmethod
  def glVertex4fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glVertex4fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glVertex4fv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glVertex4fv(const GLfloat *v)': names "
        "'GLfloat', which has no cute class yet.")

  @staticmethod
  def glVertex4iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glVertex4iv(const GLint *v)': names
    'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glVertex4iv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glVertex4iv(const GLint *v)': names "
        "'GLint', which has no cute class yet.")

  @staticmethod
  def glVertex4sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glVertex4sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glVertex4sv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_5::glVertex4sv(const GLshort *v)': names "
        "'GLshort', which has no cute class yet.")

  @staticmethod
  def glVertexPointer(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glVertexPointer(GLint size, GLenum type,
    GLsizei stride, const GLvoid *pointer)': names 'GLvoid', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glVertexPointer' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glVertexPointer(GLint size, "
        "GLenum type, GLsizei stride, const GLvoid *pointer)': names "
        "'GLvoid', which has no cute class yet.")

  @staticmethod
  def glWindowPos2dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glWindowPos2dv(const GLdouble *v)':
    names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glWindowPos2dv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glWindowPos2dv(const GLdouble "
        "*v)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glWindowPos2fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glWindowPos2fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glWindowPos2fv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glWindowPos2fv(const GLfloat "
        "*v)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glWindowPos2iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glWindowPos2iv(const GLint *v)': names
    'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glWindowPos2iv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glWindowPos2iv(const GLint *v)': "
        "names 'GLint', which has no cute class yet.")

  @staticmethod
  def glWindowPos2sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glWindowPos2sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glWindowPos2sv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glWindowPos2sv(const GLshort "
        "*v)': names 'GLshort', which has no cute class yet.")

  @staticmethod
  def glWindowPos3dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glWindowPos3dv(const GLdouble *v)':
    names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glWindowPos3dv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glWindowPos3dv(const GLdouble "
        "*v)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glWindowPos3fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glWindowPos3fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glWindowPos3fv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glWindowPos3fv(const GLfloat "
        "*v)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glWindowPos3iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glWindowPos3iv(const GLint *v)': names
    'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glWindowPos3iv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glWindowPos3iv(const GLint *v)': "
        "names 'GLint', which has no cute class yet.")

  @staticmethod
  def glWindowPos3sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_5::glWindowPos3sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_5.glWindowPos3sv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_5::glWindowPos3sv(const GLshort "
        "*v)': names 'GLshort', which has no cute class yet.")
