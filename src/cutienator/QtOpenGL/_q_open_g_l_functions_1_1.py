"""
QOpenGLFunctions_1_1 binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpenGL/qopenglfunctions_1_1.h, Qt 6.12.0. Changes made here are lost.
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


class QOpenGLFunctions_1_1(QAbstractOpenGLFunctions):
  """
  The cute side of Qt's QOpenGLFunctions_1_1: a plain Python object standing
  in front of one C++ QOpenGLFunctions_1_1.

  It is built on the cute 'QAbstractOpenGLFunctions', as Qt's
  QOpenGLFunctions_1_1 is built on Qt's QAbstractOpenGLFunctions, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QOpenGLFunctions_1_1 that has a ritual and that
  Python can call so far, 186 names in all: 'initializeOpenGLFunctions',
  'glViewport', 'glDepthRange', 'glIsEnabled', 'glGetError', 'glReadBuffer',
  'glPixelStorei', 'glPixelStoref', 'glDepthFunc', 'glStencilOp',
  'glStencilFunc', 'glLogicOp', 'glBlendFunc', 'glFlush', 'glFinish',
  'glEnable', 'glDisable', 'glDepthMask', 'glColorMask', 'glStencilMask',
  'glClearDepth', 'glClearStencil', 'glClearColor', 'glClear',
  'glDrawBuffer', 'glTexParameteri', 'glTexParameterf', 'glScissor',
  'glPolygonMode', 'glPointSize', 'glLineWidth', 'glHint', 'glFrontFace',
  'glCullFace', 'glIndexub', 'glIsTexture', 'glBindTexture',
  'glCopyTexSubImage2D', 'glCopyTexSubImage1D', 'glCopyTexImage2D',
  'glCopyTexImage1D', 'glPolygonOffset', 'glDrawArrays', 'glTranslatef',
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
  'glDisableClientState', 'glArrayElement', 'isContextCompatible',
  'versionProfile'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpenGLFunctions_1_1::~QOpenGLFunctions_1_1()': the destructor:
    Python never removes a C++ QOpenGLFunctions_1_1.
  - Qt's 'void QOpenGLFunctions_1_1::glGetTexLevelParameteriv(GLenum target,
    GLint level, GLenum pname, GLint *params)': takes a number to change
    where it is.
  - Qt's 'void QOpenGLFunctions_1_1::glGetTexLevelParameterfv(GLenum target,
    GLint level, GLenum pname, GLfloat *params)': takes a number to change
    where it is.
  - Qt's 'void QOpenGLFunctions_1_1::glGetTexParameteriv(GLenum target,
    GLenum pname, GLint *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_1_1::glGetTexParameterfv(GLenum target,
    GLenum pname, GLfloat *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_1_1::glGetTexImage(GLenum target, GLint
    level, GLenum format, GLenum type, GLvoid *pixels)': names 'GLvoid',
    which has no cute class yet.
  - Qt's 'const GLubyte *QOpenGLFunctions_1_1::glGetString(GLenum name)':
    gives 'unsigned char', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glGetIntegerv(GLenum pname, GLint
    *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_1_1::glGetFloatv(GLenum pname, GLfloat
    *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_1_1::glGetDoublev(GLenum pname, GLdouble
    *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_1_1::glGetBooleanv(GLenum pname, GLboolean
    *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_1_1::glReadPixels(GLint x, GLint y, GLsizei
    width, GLsizei height, GLenum format, GLenum type, GLvoid *pixels)':
    names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glTexImage2D(GLenum target, GLint level,
    GLint internalformat, GLsizei width, GLsizei height, GLint border, GLenum
    format, GLenum type, const GLvoid *pixels)': names 'GLvoid', which has no
    cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glTexImage1D(GLenum target, GLint level,
    GLint internalformat, GLsizei width, GLint border, GLenum format, GLenum
    type, const GLvoid *pixels)': names 'GLvoid', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_1_1::glTexParameteriv(GLenum target, GLenum
    pname, const GLint *params)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glTexParameterfv(GLenum target, GLenum
    pname, const GLfloat *params)': names 'GLfloat', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_1_1::glIndexubv(const GLubyte *c)': names
    'GLubyte', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glGenTextures(GLsizei n, GLuint
    *textures)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_1_1::glDeleteTextures(GLsizei n, const GLuint
    *textures)': names 'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glTexSubImage2D(GLenum target, GLint
    level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height,
    GLenum format, GLenum type, const GLvoid *pixels)': names 'GLvoid', which
    has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glTexSubImage1D(GLenum target, GLint
    level, GLint xoffset, GLsizei width, GLenum format, GLenum type, const
    GLvoid *pixels)': names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glGetPointerv(GLenum pname, GLvoid
    **params)': takes a type Python has no way to hand over yet.
  - Qt's 'void QOpenGLFunctions_1_1::glDrawElements(GLenum mode, GLsizei
    count, GLenum type, const GLvoid *indices)': names 'GLvoid', which has no
    cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glMultMatrixd(const GLdouble *m)': names
    'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glMultMatrixf(const GLfloat *m)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glLoadMatrixd(const GLdouble *m)': names
    'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glLoadMatrixf(const GLfloat *m)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glGetTexGeniv(GLenum coord, GLenum
    pname, GLint *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_1_1::glGetTexGenfv(GLenum coord, GLenum
    pname, GLfloat *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_1_1::glGetTexGendv(GLenum coord, GLenum
    pname, GLdouble *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_1_1::glGetTexEnviv(GLenum target, GLenum
    pname, GLint *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_1_1::glGetTexEnvfv(GLenum target, GLenum
    pname, GLfloat *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_1_1::glGetPolygonStipple(GLubyte *mask)':
    takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_1_1::glGetPixelMapusv(GLenum map, GLushort
    *values)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_1_1::glGetPixelMapuiv(GLenum map, GLuint
    *values)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_1_1::glGetPixelMapfv(GLenum map, GLfloat
    *values)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_1_1::glGetMaterialiv(GLenum face, GLenum
    pname, GLint *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_1_1::glGetMaterialfv(GLenum face, GLenum
    pname, GLfloat *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_1_1::glGetMapiv(GLenum target, GLenum query,
    GLint *v)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_1_1::glGetMapfv(GLenum target, GLenum query,
    GLfloat *v)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_1_1::glGetMapdv(GLenum target, GLenum query,
    GLdouble *v)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_1_1::glGetLightiv(GLenum light, GLenum pname,
    GLint *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_1_1::glGetLightfv(GLenum light, GLenum pname,
    GLfloat *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_1_1::glGetClipPlane(GLenum plane, GLdouble
    *equation)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_1_1::glDrawPixels(GLsizei width, GLsizei
    height, GLenum format, GLenum type, const GLvoid *pixels)': names
    'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glPixelMapusv(GLenum map, GLint mapsize,
    const GLushort *values)': names 'GLushort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glPixelMapuiv(GLenum map, GLint mapsize,
    const GLuint *values)': names 'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glPixelMapfv(GLenum map, GLint mapsize,
    const GLfloat *values)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glEvalCoord2fv(const GLfloat *u)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glEvalCoord2dv(const GLdouble *u)':
    names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glEvalCoord1fv(const GLfloat *u)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glEvalCoord1dv(const GLdouble *u)':
    names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glMap2f(GLenum target, GLfloat u1,
    GLfloat u2, GLint ustride, GLint uorder, GLfloat v1, GLfloat v2, GLint
    vstride, GLint vorder, const GLfloat *points)': names 'GLfloat', which
    has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glMap2d(GLenum target, GLdouble u1,
    GLdouble u2, GLint ustride, GLint uorder, GLdouble v1, GLdouble v2, GLint
    vstride, GLint vorder, const GLdouble *points)': names 'GLdouble', which
    has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glMap1f(GLenum target, GLfloat u1,
    GLfloat u2, GLint stride, GLint order, const GLfloat *points)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glMap1d(GLenum target, GLdouble u1,
    GLdouble u2, GLint stride, GLint order, const GLdouble *points)': names
    'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glSelectBuffer(GLsizei size, GLuint
    *buffer)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_1_1::glFeedbackBuffer(GLsizei size, GLenum
    type, GLfloat *buffer)': takes a number to change where it is.
  - Qt's 'void QOpenGLFunctions_1_1::glTexGeniv(GLenum coord, GLenum pname,
    const GLint *params)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glTexGenfv(GLenum coord, GLenum pname,
    const GLfloat *params)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glTexGendv(GLenum coord, GLenum pname,
    const GLdouble *params)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glTexEnviv(GLenum target, GLenum pname,
    const GLint *params)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glTexEnvfv(GLenum target, GLenum pname,
    const GLfloat *params)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glPolygonStipple(const GLubyte *mask)':
    names 'GLubyte', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glMaterialiv(GLenum face, GLenum pname,
    const GLint *params)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glMaterialfv(GLenum face, GLenum pname,
    const GLfloat *params)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glLightModeliv(GLenum pname, const GLint
    *params)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glLightModelfv(GLenum pname, const
    GLfloat *params)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glLightiv(GLenum light, GLenum pname,
    const GLint *params)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glLightfv(GLenum light, GLenum pname,
    const GLfloat *params)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glFogiv(GLenum pname, const GLint
    *params)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glFogfv(GLenum pname, const GLfloat
    *params)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glClipPlane(GLenum plane, const GLdouble
    *equation)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glVertex4sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glVertex4iv(const GLint *v)': names
    'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glVertex4fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glVertex4dv(const GLdouble *v)': names
    'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glVertex3sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glVertex3iv(const GLint *v)': names
    'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glVertex3fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glVertex3dv(const GLdouble *v)': names
    'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glVertex2sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glVertex2iv(const GLint *v)': names
    'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glVertex2fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glVertex2dv(const GLdouble *v)': names
    'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glTexCoord4sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glTexCoord4iv(const GLint *v)': names
    'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glTexCoord4fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glTexCoord4dv(const GLdouble *v)': names
    'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glTexCoord3sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glTexCoord3iv(const GLint *v)': names
    'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glTexCoord3fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glTexCoord3dv(const GLdouble *v)': names
    'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glTexCoord2sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glTexCoord2iv(const GLint *v)': names
    'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glTexCoord2fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glTexCoord2dv(const GLdouble *v)': names
    'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glTexCoord1sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glTexCoord1iv(const GLint *v)': names
    'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glTexCoord1fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glTexCoord1dv(const GLdouble *v)': names
    'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glRectsv(const GLshort *v1, const
    GLshort *v2)': names 'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glRectiv(const GLint *v1, const GLint
    *v2)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glRectfv(const GLfloat *v1, const
    GLfloat *v2)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glRectdv(const GLdouble *v1, const
    GLdouble *v2)': names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glRasterPos4sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glRasterPos4iv(const GLint *v)': names
    'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glRasterPos4fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glRasterPos4dv(const GLdouble *v)':
    names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glRasterPos3sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glRasterPos3iv(const GLint *v)': names
    'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glRasterPos3fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glRasterPos3dv(const GLdouble *v)':
    names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glRasterPos2sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glRasterPos2iv(const GLint *v)': names
    'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glRasterPos2fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glRasterPos2dv(const GLdouble *v)':
    names 'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glNormal3sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glNormal3iv(const GLint *v)': names
    'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glNormal3fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glNormal3dv(const GLdouble *v)': names
    'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glNormal3bv(const GLbyte *v)': names
    'GLbyte', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glIndexsv(const GLshort *c)': names
    'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glIndexiv(const GLint *c)': names
    'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glIndexfv(const GLfloat *c)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glIndexdv(const GLdouble *c)': names
    'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glEdgeFlagv(const GLboolean *flag)':
    names 'GLboolean', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glColor4usv(const GLushort *v)': names
    'GLushort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glColor4uiv(const GLuint *v)': names
    'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glColor4ubv(const GLubyte *v)': names
    'GLubyte', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glColor4sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glColor4iv(const GLint *v)': names
    'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glColor4fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glColor4dv(const GLdouble *v)': names
    'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glColor4bv(const GLbyte *v)': names
    'GLbyte', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glColor3usv(const GLushort *v)': names
    'GLushort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glColor3uiv(const GLuint *v)': names
    'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glColor3ubv(const GLubyte *v)': names
    'GLubyte', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glColor3sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glColor3iv(const GLint *v)': names
    'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glColor3fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glColor3dv(const GLdouble *v)': names
    'GLdouble', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glColor3bv(const GLbyte *v)': names
    'GLbyte', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glBitmap(GLsizei width, GLsizei height,
    GLfloat xorig, GLfloat yorig, GLfloat xmove, GLfloat ymove, const GLubyte
    *bitmap)': names 'GLubyte', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glCallLists(GLsizei n, GLenum type,
    const GLvoid *lists)': names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glPrioritizeTextures(GLsizei n, const
    GLuint *textures, const GLfloat *priorities)': names 'GLuint', which has
    no cute class yet.
  - Qt's 'GLboolean QOpenGLFunctions_1_1::glAreTexturesResident(GLsizei n,
    const GLuint *textures, GLboolean *residences)': names 'GLuint', which
    has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glVertexPointer(GLint size, GLenum type,
    GLsizei stride, const GLvoid *pointer)': names 'GLvoid', which has no
    cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glTexCoordPointer(GLint size, GLenum
    type, GLsizei stride, const GLvoid *pointer)': names 'GLvoid', which has
    no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glNormalPointer(GLenum type, GLsizei
    stride, const GLvoid *pointer)': names 'GLvoid', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_1_1::glInterleavedArrays(GLenum format,
    GLsizei stride, const GLvoid *pointer)': names 'GLvoid', which has no
    cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glIndexPointer(GLenum type, GLsizei
    stride, const GLvoid *pointer)': names 'GLvoid', which has no cute class
    yet.
  - Qt's 'void QOpenGLFunctions_1_1::glEdgeFlagPointer(GLsizei stride, const
    GLvoid *pointer)': names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLFunctions_1_1::glColorPointer(GLint size, GLenum type,
    GLsizei stride, const GLvoid *pointer)': names 'GLvoid', which has no
    cute class yet.

  What to expect
  --------------

  - The C++ QOpenGLFunctions_1_1 is created at the first use, not by
    'QOpenGLFunctions_1_1(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QOpenGLFunctions_1_1.
  - Each name of Qt's QOpenGLFunctions_1_1 that has no cute function yet,
    'glAreTexturesResident', 'glBitmap', 'glCallLists', 'glClipPlane',
    'glColor3bv', 'glColor3dv', 'glColor3fv', 'glColor3iv', 'glColor3sv',
    'glColor3ubv', 'glColor3uiv', 'glColor3usv', 'glColor4bv', 'glColor4dv',
    'glColor4fv', 'glColor4iv', 'glColor4sv', 'glColor4ubv', 'glColor4uiv',
    'glColor4usv', 'glColorPointer', 'glDeleteTextures', 'glDrawElements',
    'glDrawPixels', 'glEdgeFlagPointer', 'glEdgeFlagv', 'glEvalCoord1dv',
    'glEvalCoord1fv', 'glEvalCoord2dv', 'glEvalCoord2fv', 'glFeedbackBuffer',
    'glFogfv', 'glFogiv', 'glGenTextures', 'glGetBooleanv', 'glGetClipPlane',
    'glGetDoublev', 'glGetFloatv', 'glGetIntegerv', 'glGetLightfv',
    'glGetLightiv', 'glGetMapdv', 'glGetMapfv', 'glGetMapiv',
    'glGetMaterialfv', 'glGetMaterialiv', 'glGetPixelMapfv',
    'glGetPixelMapuiv', 'glGetPixelMapusv', 'glGetPointerv',
    'glGetPolygonStipple', 'glGetString', 'glGetTexEnvfv', 'glGetTexEnviv',
    'glGetTexGendv', 'glGetTexGenfv', 'glGetTexGeniv', 'glGetTexImage',
    'glGetTexLevelParameterfv', 'glGetTexLevelParameteriv',
    'glGetTexParameterfv', 'glGetTexParameteriv', 'glIndexPointer',
    'glIndexdv', 'glIndexfv', 'glIndexiv', 'glIndexsv', 'glIndexubv',
    'glInterleavedArrays', 'glLightModelfv', 'glLightModeliv', 'glLightfv',
    'glLightiv', 'glLoadMatrixd', 'glLoadMatrixf', 'glMap1d', 'glMap1f',
    'glMap2d', 'glMap2f', 'glMaterialfv', 'glMaterialiv', 'glMultMatrixd',
    'glMultMatrixf', 'glNormal3bv', 'glNormal3dv', 'glNormal3fv',
    'glNormal3iv', 'glNormal3sv', 'glNormalPointer', 'glPixelMapfv',
    'glPixelMapuiv', 'glPixelMapusv', 'glPolygonStipple',
    'glPrioritizeTextures', 'glRasterPos2dv', 'glRasterPos2fv',
    'glRasterPos2iv', 'glRasterPos2sv', 'glRasterPos3dv', 'glRasterPos3fv',
    'glRasterPos3iv', 'glRasterPos3sv', 'glRasterPos4dv', 'glRasterPos4fv',
    'glRasterPos4iv', 'glRasterPos4sv', 'glReadPixels', 'glRectdv',
    'glRectfv', 'glRectiv', 'glRectsv', 'glSelectBuffer', 'glTexCoord1dv',
    'glTexCoord1fv', 'glTexCoord1iv', 'glTexCoord1sv', 'glTexCoord2dv',
    'glTexCoord2fv', 'glTexCoord2iv', 'glTexCoord2sv', 'glTexCoord3dv',
    'glTexCoord3fv', 'glTexCoord3iv', 'glTexCoord3sv', 'glTexCoord4dv',
    'glTexCoord4fv', 'glTexCoord4iv', 'glTexCoord4sv', 'glTexCoordPointer',
    'glTexEnvfv', 'glTexEnviv', 'glTexGendv', 'glTexGenfv', 'glTexGeniv',
    'glTexImage1D', 'glTexImage2D', 'glTexParameterfv', 'glTexParameteriv',
    'glTexSubImage1D', 'glTexSubImage2D', 'glVertex2dv', 'glVertex2fv',
    'glVertex2iv', 'glVertex2sv', 'glVertex3dv', 'glVertex3fv',
    'glVertex3iv', 'glVertex3sv', 'glVertex4dv', 'glVertex4fv',
    'glVertex4iv', 'glVertex4sv', 'glVertexPointer', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QOpenGLContext)
  @overload(NoneType)
  def isContextCompatible(context: Optional[QOpenGLContext]) -> bool:
    """
    Calls Qt's 'bool QOpenGLFunctions_1_1::isContextCompatible(QOpenGLContext
    *context)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#isContextCompatible

    Parameters
    ----------

    context : Optional[QOpenGLContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QOpenGLFunctions_1_1::isContextCompatible(QOpenGLContext
    #      *context)
    return Rituals.call(
        'ritual_ZN20QOpenGLFunctions_1_119isContextCompatibleEP14QOpenGLCon'
        'text',
        CuteMixin._addressOf(context),
    )

  @staticmethod
  def versionProfile() -> QOpenGLVersionProfile:
    """
    Calls Qt's 'QOpenGLVersionProfile
    QOpenGLFunctions_1_1::versionProfile()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#versionProfile

    Returns
    -------

    QOpenGLVersionProfile
      A new cute QOpenGLVersionProfile around the copy Qt gave back. Python
      owns it.
    """
    #  QOpenGLVersionProfile QOpenGLFunctions_1_1::versionProfile()
    address = Rituals.call(
        'ritual_ZN20QOpenGLFunctions_1_114versionProfileEv',
    )
    from . import QOpenGLVersionProfile
    return QOpenGLVersionProfile._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpenGLFunctions_1_1'

  #  A C++ QOpenGLFunctions_1_1 Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QOpenGLFunctions_1_1'

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
    'QOpenGLFunctions_1_1::QOpenGLFunctions_1_1()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#QOpenGLFunctions_1_1
    """
    #  QOpenGLFunctions_1_1::QOpenGLFunctions_1_1()
    self._noteCreation(QOpenGLFunctions_1_1, lambda: Rituals.call(
        'ritual_ZN20QOpenGLFunctions_1_1C1Ev',
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
    Calls Qt's 'bool QOpenGLFunctions_1_1::initializeOpenGLFunctions()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html
    """
    #  bool QOpenGLFunctions_1_1::initializeOpenGLFunctions()
    ritual = 'ritual_ZN20QOpenGLFunctions_1_125initializeOpenGLFunctionsEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QOpenGLFunctions_1_125initializeOpenGLFunctionsEv')
    return self.uglySide.call(ritual)

  @overload(int, int, int, int)
  def glViewport(self, x: int, y: int, width: int, height: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glViewport(GLint x, GLint y,
    GLsizei width, GLsizei height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glViewport

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
    #  void QOpenGLFunctions_1_1::glViewport(GLint x, GLint y, GLsizei width,
    #      GLsizei height)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_110glViewportEiiii',
        x, y, width, height,
    )

  @overload(float, float)
  def glDepthRange(self, nearVal: float, farVal: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glDepthRange(GLdouble nearVal,
    GLdouble farVal)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glDepthRange

    Parameters
    ----------

    nearVal : float
      Passed on as it is.

    farVal : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glDepthRange(GLdouble nearVal, GLdouble
    #      farVal)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_112glDepthRangeEdd', nearVal, farVal,
    )

  @overload(int)
  def glIsEnabled(self, cap: int) -> int:
    """
    Calls Qt's 'GLboolean QOpenGLFunctions_1_1::glIsEnabled(GLenum cap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glIsEnabled

    Parameters
    ----------

    cap : int
      Passed on as it is.
    """
    #  GLboolean QOpenGLFunctions_1_1::glIsEnabled(GLenum cap)
    return self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_111glIsEnabledEj', cap,
    )

  def glGetError(self) -> int:
    """
    Calls Qt's 'GLenum QOpenGLFunctions_1_1::glGetError()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glGetError
    """
    #  GLenum QOpenGLFunctions_1_1::glGetError()
    return self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_110glGetErrorEv',
    )

  @overload(int)
  def glReadBuffer(self, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glReadBuffer(GLenum mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glReadBuffer

    Parameters
    ----------

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glReadBuffer(GLenum mode)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_112glReadBufferEj', mode,
    )

  @overload(int, int)
  def glPixelStorei(self, pname: int, param: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glPixelStorei(GLenum pname, GLint
    param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glPixelStorei

    Parameters
    ----------

    pname : int
      Passed on as it is.

    param : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glPixelStorei(GLenum pname, GLint param)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_113glPixelStoreiEji', pname, param,
    )

  @overload(int, float)
  def glPixelStoref(self, pname: int, param: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glPixelStoref(GLenum pname,
    GLfloat param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glPixelStoref

    Parameters
    ----------

    pname : int
      Passed on as it is.

    param : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glPixelStoref(GLenum pname, GLfloat param)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_113glPixelStorefEjf', pname, param,
    )

  @overload(int)
  def glDepthFunc(self, func: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glDepthFunc(GLenum func)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glDepthFunc

    Parameters
    ----------

    func : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glDepthFunc(GLenum func)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_111glDepthFuncEj', func,
    )

  @overload(int, int, int)
  def glStencilOp(self, fail: int, zfail: int, zpass: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glStencilOp(GLenum fail, GLenum
    zfail, GLenum zpass)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glStencilOp

    Parameters
    ----------

    fail : int
      Passed on as it is.

    zfail : int
      Passed on as it is.

    zpass : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glStencilOp(GLenum fail, GLenum zfail,
    #      GLenum zpass)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_111glStencilOpEjjj',
        fail, zfail, zpass,
    )

  @overload(int, int, int)
  def glStencilFunc(self, func: int, ref: int, mask: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glStencilFunc(GLenum func, GLint
    ref, GLuint mask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glStencilFunc

    Parameters
    ----------

    func : int
      Passed on as it is.

    ref : int
      Passed on as it is.

    mask : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glStencilFunc(GLenum func, GLint ref,
    #      GLuint mask)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_113glStencilFuncEjij',
        func, ref, mask,
    )

  @overload(int)
  def glLogicOp(self, opcode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glLogicOp(GLenum opcode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glLogicOp

    Parameters
    ----------

    opcode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glLogicOp(GLenum opcode)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_1_19glLogicOpEj', opcode)

  @overload(int, int)
  def glBlendFunc(self, sfactor: int, dfactor: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glBlendFunc(GLenum sfactor, GLenum
    dfactor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glBlendFunc

    Parameters
    ----------

    sfactor : int
      Passed on as it is.

    dfactor : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glBlendFunc(GLenum sfactor, GLenum dfactor)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_111glBlendFuncEjj', sfactor, dfactor,
    )

  def glFlush(self) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glFlush()'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glFlush
    """
    #  void QOpenGLFunctions_1_1::glFlush()
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_1_17glFlushEv')

  def glFinish(self) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glFinish()'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glFinish
    """
    #  void QOpenGLFunctions_1_1::glFinish()
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_1_18glFinishEv')

  @overload(int)
  def glEnable(self, cap: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glEnable(GLenum cap)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glEnable

    Parameters
    ----------

    cap : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glEnable(GLenum cap)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_1_18glEnableEj', cap)

  @overload(int)
  def glDisable(self, cap: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glDisable(GLenum cap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glDisable

    Parameters
    ----------

    cap : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glDisable(GLenum cap)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_1_19glDisableEj', cap)

  @overload(int)
  def glDepthMask(self, flag: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glDepthMask(GLboolean flag)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glDepthMask

    Parameters
    ----------

    flag : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glDepthMask(GLboolean flag)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_111glDepthMaskEh', flag,
    )

  @overload(int, int, int, int)
  def glColorMask(self, red: int, green: int, blue: int, alpha: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glColorMask(GLboolean red,
    GLboolean green, GLboolean blue, GLboolean alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glColorMask

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
    #  void QOpenGLFunctions_1_1::glColorMask(GLboolean red, GLboolean green,
    #      GLboolean blue, GLboolean alpha)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_111glColorMaskEhhhh',
        red, green, blue, alpha,
    )

  @overload(int)
  def glStencilMask(self, mask: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glStencilMask(GLuint mask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glStencilMask

    Parameters
    ----------

    mask : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glStencilMask(GLuint mask)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_113glStencilMaskEj', mask,
    )

  @overload(float)
  def glClearDepth(self, depth: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glClearDepth(GLdouble depth)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glClearDepth

    Parameters
    ----------

    depth : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glClearDepth(GLdouble depth)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_112glClearDepthEd', depth,
    )

  @overload(int)
  def glClearStencil(self, s: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glClearStencil(GLint s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glClearStencil

    Parameters
    ----------

    s : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glClearStencil(GLint s)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_114glClearStencilEi', s,
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
    Calls Qt's 'void QOpenGLFunctions_1_1::glClearColor(GLfloat red, GLfloat
    green, GLfloat blue, GLfloat alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glClearColor

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
    #  void QOpenGLFunctions_1_1::glClearColor(GLfloat red, GLfloat green,
    #      GLfloat blue, GLfloat alpha)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_112glClearColorEffff',
        red, green, blue, alpha,
    )

  @overload(int)
  def glClear(self, mask: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glClear(GLbitfield mask)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glClear

    Parameters
    ----------

    mask : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glClear(GLbitfield mask)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_1_17glClearEj', mask)

  @overload(int)
  def glDrawBuffer(self, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glDrawBuffer(GLenum mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glDrawBuffer

    Parameters
    ----------

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glDrawBuffer(GLenum mode)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_112glDrawBufferEj', mode,
    )

  @overload(int, int, int)
  def glTexParameteri(self, target: int, pname: int, param: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glTexParameteri(GLenum target,
    GLenum pname, GLint param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glTexParameteri

    Parameters
    ----------

    target : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    param : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glTexParameteri(GLenum target, GLenum
    #      pname, GLint param)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_115glTexParameteriEjji',
        target, pname, param,
    )

  @overload(int, int, float)
  def glTexParameterf(self, target: int, pname: int, param: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glTexParameterf(GLenum target,
    GLenum pname, GLfloat param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glTexParameterf

    Parameters
    ----------

    target : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    param : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glTexParameterf(GLenum target, GLenum
    #      pname, GLfloat param)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_115glTexParameterfEjjf',
        target, pname, param,
    )

  @overload(int, int, int, int)
  def glScissor(self, x: int, y: int, width: int, height: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glScissor(GLint x, GLint y,
    GLsizei width, GLsizei height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glScissor

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
    #  void QOpenGLFunctions_1_1::glScissor(GLint x, GLint y, GLsizei width,
    #      GLsizei height)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_19glScissorEiiii',
        x, y, width, height,
    )

  @overload(int, int)
  def glPolygonMode(self, face: int, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glPolygonMode(GLenum face, GLenum
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glPolygonMode

    Parameters
    ----------

    face : int
      Passed on as it is.

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glPolygonMode(GLenum face, GLenum mode)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_113glPolygonModeEjj', face, mode,
    )

  @overload(float)
  def glPointSize(self, size: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glPointSize(GLfloat size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glPointSize

    Parameters
    ----------

    size : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glPointSize(GLfloat size)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_111glPointSizeEf', size,
    )

  @overload(float)
  def glLineWidth(self, width: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glLineWidth(GLfloat width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glLineWidth

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glLineWidth(GLfloat width)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_111glLineWidthEf', width,
    )

  @overload(int, int)
  def glHint(self, target: int, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glHint(GLenum target, GLenum
    mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glHint

    Parameters
    ----------

    target : int
      Passed on as it is.

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glHint(GLenum target, GLenum mode)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_16glHintEjj', target, mode,
    )

  @overload(int)
  def glFrontFace(self, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glFrontFace(GLenum mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glFrontFace

    Parameters
    ----------

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glFrontFace(GLenum mode)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_111glFrontFaceEj', mode,
    )

  @overload(int)
  def glCullFace(self, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glCullFace(GLenum mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glCullFace

    Parameters
    ----------

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glCullFace(GLenum mode)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_1_110glCullFaceEj', mode)

  @overload(int)
  def glIndexub(self, c: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glIndexub(GLubyte c)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glIndexub

    Parameters
    ----------

    c : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glIndexub(GLubyte c)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_1_19glIndexubEh', c)

  @overload(int)
  def glIsTexture(self, texture: int) -> int:
    """
    Calls Qt's 'GLboolean QOpenGLFunctions_1_1::glIsTexture(GLuint texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glIsTexture

    Parameters
    ----------

    texture : int
      Passed on as it is.
    """
    #  GLboolean QOpenGLFunctions_1_1::glIsTexture(GLuint texture)
    return self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_111glIsTextureEj', texture,
    )

  @overload(int, int)
  def glBindTexture(self, target: int, texture: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glBindTexture(GLenum target,
    GLuint texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glBindTexture

    Parameters
    ----------

    target : int
      Passed on as it is.

    texture : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glBindTexture(GLenum target, GLuint
    #      texture)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_113glBindTextureEjj', target, texture,
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
    Calls Qt's 'void QOpenGLFunctions_1_1::glCopyTexSubImage2D(GLenum target,
    GLint level, GLint xoffset, GLint yoffset, GLint x, GLint y, GLsizei
    width, GLsizei height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glCopyTexSubImage2D

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
    #  void QOpenGLFunctions_1_1::glCopyTexSubImage2D(GLenum target, GLint
    #      level, GLint xoffset, GLint yoffset, GLint x, GLint y, GLsizei
    #      width, GLsizei height)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_119glCopyTexSubImage2DEjiiiiiii',
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
    Calls Qt's 'void QOpenGLFunctions_1_1::glCopyTexSubImage1D(GLenum target,
    GLint level, GLint xoffset, GLint x, GLint y, GLsizei width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glCopyTexSubImage1D

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
    #  void QOpenGLFunctions_1_1::glCopyTexSubImage1D(GLenum target, GLint
    #      level, GLint xoffset, GLint x, GLint y, GLsizei width)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_119glCopyTexSubImage1DEjiiiii',
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
    Calls Qt's 'void QOpenGLFunctions_1_1::glCopyTexImage2D(GLenum target,
    GLint level, GLenum internalformat, GLint x, GLint y, GLsizei width,
    GLsizei height, GLint border)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glCopyTexImage2D

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
    #  void QOpenGLFunctions_1_1::glCopyTexImage2D(GLenum target, GLint
    #      level, GLenum internalformat, GLint x, GLint y, GLsizei width,
    #      GLsizei height, GLint border)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_116glCopyTexImage2DEjijiiiii',
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
    Calls Qt's 'void QOpenGLFunctions_1_1::glCopyTexImage1D(GLenum target,
    GLint level, GLenum internalformat, GLint x, GLint y, GLsizei width,
    GLint border)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glCopyTexImage1D

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
    #  void QOpenGLFunctions_1_1::glCopyTexImage1D(GLenum target, GLint
    #      level, GLenum internalformat, GLint x, GLint y, GLsizei width,
    #      GLint border)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_116glCopyTexImage1DEjijiiii',
        target, level, internalformat, x, y, width, border,
    )

  @overload(float, float)
  def glPolygonOffset(self, factor: float, units: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glPolygonOffset(GLfloat factor,
    GLfloat units)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glPolygonOffset

    Parameters
    ----------

    factor : float
      Passed on as it is.

    units : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glPolygonOffset(GLfloat factor, GLfloat
    #      units)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_115glPolygonOffsetEff', factor, units,
    )

  @overload(int, int, int)
  def glDrawArrays(self, mode: int, first: int, count: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glDrawArrays(GLenum mode, GLint
    first, GLsizei count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glDrawArrays

    Parameters
    ----------

    mode : int
      Passed on as it is.

    first : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glDrawArrays(GLenum mode, GLint first,
    #      GLsizei count)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_112glDrawArraysEjii',
        mode, first, count,
    )

  @overload(float, float, float)
  def glTranslatef(self, x: float, y: float, z: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glTranslatef(GLfloat x, GLfloat y,
    GLfloat z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glTranslatef

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glTranslatef(GLfloat x, GLfloat y, GLfloat
    #      z)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_112glTranslatefEfff', x, y, z,
    )

  @overload(float, float, float)
  def glTranslated(self, x: float, y: float, z: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glTranslated(GLdouble x, GLdouble
    y, GLdouble z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glTranslated

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glTranslated(GLdouble x, GLdouble y,
    #      GLdouble z)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_112glTranslatedEddd', x, y, z,
    )

  @overload(float, float, float)
  def glScalef(self, x: float, y: float, z: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glScalef(GLfloat x, GLfloat y,
    GLfloat z)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glScalef

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glScalef(GLfloat x, GLfloat y, GLfloat z)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_18glScalefEfff', x, y, z,
    )

  @overload(float, float, float)
  def glScaled(self, x: float, y: float, z: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glScaled(GLdouble x, GLdouble y,
    GLdouble z)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glScaled

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glScaled(GLdouble x, GLdouble y, GLdouble
    #      z)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_18glScaledEddd', x, y, z,
    )

  @overload(float, float, float, float)
  def glRotatef(self, angle: float, x: float, y: float, z: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glRotatef(GLfloat angle, GLfloat
    x, GLfloat y, GLfloat z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glRotatef

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
    #  void QOpenGLFunctions_1_1::glRotatef(GLfloat angle, GLfloat x, GLfloat
    #      y, GLfloat z)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_19glRotatefEffff', angle, x, y, z,
    )

  @overload(float, float, float, float)
  def glRotated(self, angle: float, x: float, y: float, z: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glRotated(GLdouble angle, GLdouble
    x, GLdouble y, GLdouble z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glRotated

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
    #  void QOpenGLFunctions_1_1::glRotated(GLdouble angle, GLdouble x,
    #      GLdouble y, GLdouble z)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_19glRotatedEdddd', angle, x, y, z,
    )

  def glPushMatrix(self) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glPushMatrix()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glPushMatrix
    """
    #  void QOpenGLFunctions_1_1::glPushMatrix()
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_1_112glPushMatrixEv')

  def glPopMatrix(self) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glPopMatrix()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glPopMatrix
    """
    #  void QOpenGLFunctions_1_1::glPopMatrix()
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_1_111glPopMatrixEv')

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
    Calls Qt's 'void QOpenGLFunctions_1_1::glOrtho(GLdouble left, GLdouble
    right, GLdouble bottom, GLdouble top, GLdouble zNear, GLdouble zFar)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glOrtho

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
    #  void QOpenGLFunctions_1_1::glOrtho(GLdouble left, GLdouble right,
    #      GLdouble bottom, GLdouble top, GLdouble zNear, GLdouble zFar)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_17glOrthoEdddddd',
        left, right, bottom, top, zNear, zFar,
    )

  @overload(int)
  def glMatrixMode(self, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glMatrixMode(GLenum mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glMatrixMode

    Parameters
    ----------

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glMatrixMode(GLenum mode)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_112glMatrixModeEj', mode,
    )

  def glLoadIdentity(self) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glLoadIdentity()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glLoadIdentity
    """
    #  void QOpenGLFunctions_1_1::glLoadIdentity()
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_1_114glLoadIdentityEv')

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
    Calls Qt's 'void QOpenGLFunctions_1_1::glFrustum(GLdouble left, GLdouble
    right, GLdouble bottom, GLdouble top, GLdouble zNear, GLdouble zFar)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glFrustum

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
    #  void QOpenGLFunctions_1_1::glFrustum(GLdouble left, GLdouble right,
    #      GLdouble bottom, GLdouble top, GLdouble zNear, GLdouble zFar)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_19glFrustumEdddddd',
        left, right, bottom, top, zNear, zFar,
    )

  @overload(int)
  def glIsList(self, list: int) -> int:
    """
    Calls Qt's 'GLboolean QOpenGLFunctions_1_1::glIsList(GLuint list)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glIsList

    Parameters
    ----------

    list : int
      Passed on as it is.
    """
    #  GLboolean QOpenGLFunctions_1_1::glIsList(GLuint list)
    return self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_18glIsListEj', list,
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
    Calls Qt's 'void QOpenGLFunctions_1_1::glCopyPixels(GLint x, GLint y,
    GLsizei width, GLsizei height, GLenum type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glCopyPixels

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
    #  void QOpenGLFunctions_1_1::glCopyPixels(GLint x, GLint y, GLsizei
    #      width, GLsizei height, GLenum type)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_112glCopyPixelsEiiiij',
        x, y, width, height, type,
    )

  @overload(int, int)
  def glPixelTransferi(self, pname: int, param: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glPixelTransferi(GLenum pname,
    GLint param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glPixelTransferi

    Parameters
    ----------

    pname : int
      Passed on as it is.

    param : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glPixelTransferi(GLenum pname, GLint param)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_116glPixelTransferiEji', pname, param,
    )

  @overload(int, float)
  def glPixelTransferf(self, pname: int, param: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glPixelTransferf(GLenum pname,
    GLfloat param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glPixelTransferf

    Parameters
    ----------

    pname : int
      Passed on as it is.

    param : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glPixelTransferf(GLenum pname, GLfloat
    #      param)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_116glPixelTransferfEjf', pname, param,
    )

  @overload(float, float)
  def glPixelZoom(self, xfactor: float, yfactor: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glPixelZoom(GLfloat xfactor,
    GLfloat yfactor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glPixelZoom

    Parameters
    ----------

    xfactor : float
      Passed on as it is.

    yfactor : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glPixelZoom(GLfloat xfactor, GLfloat
    #      yfactor)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_111glPixelZoomEff', xfactor, yfactor,
    )

  @overload(int, float)
  def glAlphaFunc(self, func: int, ref: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glAlphaFunc(GLenum func, GLfloat
    ref)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glAlphaFunc

    Parameters
    ----------

    func : int
      Passed on as it is.

    ref : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glAlphaFunc(GLenum func, GLfloat ref)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_111glAlphaFuncEjf', func, ref,
    )

  @overload(int, int)
  def glEvalPoint2(self, i: int, j: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glEvalPoint2(GLint i, GLint j)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glEvalPoint2

    Parameters
    ----------

    i : int
      Passed on as it is.

    j : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glEvalPoint2(GLint i, GLint j)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_112glEvalPoint2Eii', i, j,
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
    Calls Qt's 'void QOpenGLFunctions_1_1::glEvalMesh2(GLenum mode, GLint i1,
    GLint i2, GLint j1, GLint j2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glEvalMesh2

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
    #  void QOpenGLFunctions_1_1::glEvalMesh2(GLenum mode, GLint i1, GLint
    #      i2, GLint j1, GLint j2)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_111glEvalMesh2Ejiiii',
        mode, i1, i2, j1, j2,
    )

  @overload(int)
  def glEvalPoint1(self, i: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glEvalPoint1(GLint i)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glEvalPoint1

    Parameters
    ----------

    i : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glEvalPoint1(GLint i)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_1_112glEvalPoint1Ei', i)

  @overload(int, int, int)
  def glEvalMesh1(self, mode: int, i1: int, i2: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glEvalMesh1(GLenum mode, GLint i1,
    GLint i2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glEvalMesh1

    Parameters
    ----------

    mode : int
      Passed on as it is.

    i1 : int
      Passed on as it is.

    i2 : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glEvalMesh1(GLenum mode, GLint i1, GLint
    #      i2)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_111glEvalMesh1Ejii', mode, i1, i2,
    )

  @overload(float, float)
  def glEvalCoord2f(self, u: float, v: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glEvalCoord2f(GLfloat u, GLfloat
    v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glEvalCoord2f

    Parameters
    ----------

    u : float
      Passed on as it is.

    v : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glEvalCoord2f(GLfloat u, GLfloat v)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_113glEvalCoord2fEff', u, v,
    )

  @overload(float, float)
  def glEvalCoord2d(self, u: float, v: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glEvalCoord2d(GLdouble u, GLdouble
    v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glEvalCoord2d

    Parameters
    ----------

    u : float
      Passed on as it is.

    v : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glEvalCoord2d(GLdouble u, GLdouble v)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_113glEvalCoord2dEdd', u, v,
    )

  @overload(float)
  def glEvalCoord1f(self, u: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glEvalCoord1f(GLfloat u)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glEvalCoord1f

    Parameters
    ----------

    u : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glEvalCoord1f(GLfloat u)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_1_113glEvalCoord1fEf', u)

  @overload(float)
  def glEvalCoord1d(self, u: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glEvalCoord1d(GLdouble u)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glEvalCoord1d

    Parameters
    ----------

    u : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glEvalCoord1d(GLdouble u)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_1_113glEvalCoord1dEd', u)

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
    Calls Qt's 'void QOpenGLFunctions_1_1::glMapGrid2f(GLint un, GLfloat u1,
    GLfloat u2, GLint vn, GLfloat v1, GLfloat v2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glMapGrid2f

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
    #  void QOpenGLFunctions_1_1::glMapGrid2f(GLint un, GLfloat u1, GLfloat
    #      u2, GLint vn, GLfloat v1, GLfloat v2)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_111glMapGrid2fEiffiff',
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
    Calls Qt's 'void QOpenGLFunctions_1_1::glMapGrid2d(GLint un, GLdouble u1,
    GLdouble u2, GLint vn, GLdouble v1, GLdouble v2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glMapGrid2d

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
    #  void QOpenGLFunctions_1_1::glMapGrid2d(GLint un, GLdouble u1, GLdouble
    #      u2, GLint vn, GLdouble v1, GLdouble v2)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_111glMapGrid2dEiddidd',
        un, u1, u2, vn, v1, v2,
    )

  @overload(int, float, float)
  def glMapGrid1f(self, un: int, u1: float, u2: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glMapGrid1f(GLint un, GLfloat u1,
    GLfloat u2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glMapGrid1f

    Parameters
    ----------

    un : int
      Passed on as it is.

    u1 : float
      Passed on as it is.

    u2 : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glMapGrid1f(GLint un, GLfloat u1, GLfloat
    #      u2)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_111glMapGrid1fEiff', un, u1, u2,
    )

  @overload(int, float, float)
  def glMapGrid1d(self, un: int, u1: float, u2: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glMapGrid1d(GLint un, GLdouble u1,
    GLdouble u2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glMapGrid1d

    Parameters
    ----------

    un : int
      Passed on as it is.

    u1 : float
      Passed on as it is.

    u2 : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glMapGrid1d(GLint un, GLdouble u1, GLdouble
    #      u2)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_111glMapGrid1dEidd', un, u1, u2,
    )

  @overload(int)
  def glPushAttrib(self, mask: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glPushAttrib(GLbitfield mask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glPushAttrib

    Parameters
    ----------

    mask : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glPushAttrib(GLbitfield mask)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_112glPushAttribEj', mask,
    )

  def glPopAttrib(self) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glPopAttrib()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glPopAttrib
    """
    #  void QOpenGLFunctions_1_1::glPopAttrib()
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_1_111glPopAttribEv')

  @overload(int, float)
  def glAccum(self, op: int, value: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glAccum(GLenum op, GLfloat
    value)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glAccum

    Parameters
    ----------

    op : int
      Passed on as it is.

    value : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glAccum(GLenum op, GLfloat value)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_17glAccumEjf', op, value,
    )

  @overload(int)
  def glIndexMask(self, mask: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glIndexMask(GLuint mask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glIndexMask

    Parameters
    ----------

    mask : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glIndexMask(GLuint mask)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_111glIndexMaskEj', mask,
    )

  @overload(float)
  def glClearIndex(self, c: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glClearIndex(GLfloat c)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glClearIndex

    Parameters
    ----------

    c : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glClearIndex(GLfloat c)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_1_112glClearIndexEf', c)

  @overload(float, float, float, float)
  def glClearAccum(
      self,
      red: float,
      green: float,
      blue: float,
      alpha: float,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glClearAccum(GLfloat red, GLfloat
    green, GLfloat blue, GLfloat alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glClearAccum

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
    #  void QOpenGLFunctions_1_1::glClearAccum(GLfloat red, GLfloat green,
    #      GLfloat blue, GLfloat alpha)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_112glClearAccumEffff',
        red, green, blue, alpha,
    )

  @overload(int)
  def glPushName(self, name: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glPushName(GLuint name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glPushName

    Parameters
    ----------

    name : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glPushName(GLuint name)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_1_110glPushNameEj', name)

  def glPopName(self) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glPopName()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glPopName
    """
    #  void QOpenGLFunctions_1_1::glPopName()
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_1_19glPopNameEv')

  @overload(float)
  def glPassThrough(self, token: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glPassThrough(GLfloat token)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glPassThrough

    Parameters
    ----------

    token : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glPassThrough(GLfloat token)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_113glPassThroughEf', token,
    )

  @overload(int)
  def glLoadName(self, name: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glLoadName(GLuint name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glLoadName

    Parameters
    ----------

    name : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glLoadName(GLuint name)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_1_110glLoadNameEj', name)

  def glInitNames(self) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glInitNames()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glInitNames
    """
    #  void QOpenGLFunctions_1_1::glInitNames()
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_1_111glInitNamesEv')

  @overload(int)
  def glRenderMode(self, mode: int) -> int:
    """
    Calls Qt's 'GLint QOpenGLFunctions_1_1::glRenderMode(GLenum mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glRenderMode

    Parameters
    ----------

    mode : int
      Passed on as it is.
    """
    #  GLint QOpenGLFunctions_1_1::glRenderMode(GLenum mode)
    return self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_112glRenderModeEj', mode,
    )

  @overload(int, int, int)
  def glTexGeni(self, coord: int, pname: int, param: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glTexGeni(GLenum coord, GLenum
    pname, GLint param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glTexGeni

    Parameters
    ----------

    coord : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    param : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glTexGeni(GLenum coord, GLenum pname, GLint
    #      param)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_19glTexGeniEjji', coord, pname, param,
    )

  @overload(int, int, float)
  def glTexGenf(self, coord: int, pname: int, param: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glTexGenf(GLenum coord, GLenum
    pname, GLfloat param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glTexGenf

    Parameters
    ----------

    coord : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    param : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glTexGenf(GLenum coord, GLenum pname,
    #      GLfloat param)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_19glTexGenfEjjf', coord, pname, param,
    )

  @overload(int, int, float)
  def glTexGend(self, coord: int, pname: int, param: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glTexGend(GLenum coord, GLenum
    pname, GLdouble param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glTexGend

    Parameters
    ----------

    coord : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    param : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glTexGend(GLenum coord, GLenum pname,
    #      GLdouble param)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_19glTexGendEjjd', coord, pname, param,
    )

  @overload(int, int, int)
  def glTexEnvi(self, target: int, pname: int, param: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glTexEnvi(GLenum target, GLenum
    pname, GLint param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glTexEnvi

    Parameters
    ----------

    target : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    param : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glTexEnvi(GLenum target, GLenum pname,
    #      GLint param)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_19glTexEnviEjji',
        target, pname, param,
    )

  @overload(int, int, float)
  def glTexEnvf(self, target: int, pname: int, param: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glTexEnvf(GLenum target, GLenum
    pname, GLfloat param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glTexEnvf

    Parameters
    ----------

    target : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    param : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glTexEnvf(GLenum target, GLenum pname,
    #      GLfloat param)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_19glTexEnvfEjjf',
        target, pname, param,
    )

  @overload(int)
  def glShadeModel(self, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glShadeModel(GLenum mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glShadeModel

    Parameters
    ----------

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glShadeModel(GLenum mode)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_112glShadeModelEj', mode,
    )

  @overload(int, int, int)
  def glMateriali(self, face: int, pname: int, param: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glMateriali(GLenum face, GLenum
    pname, GLint param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glMateriali

    Parameters
    ----------

    face : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    param : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glMateriali(GLenum face, GLenum pname,
    #      GLint param)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_111glMaterialiEjji',
        face, pname, param,
    )

  @overload(int, int, float)
  def glMaterialf(self, face: int, pname: int, param: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glMaterialf(GLenum face, GLenum
    pname, GLfloat param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glMaterialf

    Parameters
    ----------

    face : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    param : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glMaterialf(GLenum face, GLenum pname,
    #      GLfloat param)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_111glMaterialfEjjf',
        face, pname, param,
    )

  @overload(int, int)
  def glLineStipple(self, factor: int, pattern: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glLineStipple(GLint factor,
    GLushort pattern)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glLineStipple

    Parameters
    ----------

    factor : int
      Passed on as it is.

    pattern : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glLineStipple(GLint factor, GLushort
    #      pattern)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_113glLineStippleEit', factor, pattern,
    )

  @overload(int, int)
  def glLightModeli(self, pname: int, param: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glLightModeli(GLenum pname, GLint
    param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glLightModeli

    Parameters
    ----------

    pname : int
      Passed on as it is.

    param : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glLightModeli(GLenum pname, GLint param)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_113glLightModeliEji', pname, param,
    )

  @overload(int, float)
  def glLightModelf(self, pname: int, param: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glLightModelf(GLenum pname,
    GLfloat param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glLightModelf

    Parameters
    ----------

    pname : int
      Passed on as it is.

    param : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glLightModelf(GLenum pname, GLfloat param)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_113glLightModelfEjf', pname, param,
    )

  @overload(int, int, int)
  def glLighti(self, light: int, pname: int, param: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glLighti(GLenum light, GLenum
    pname, GLint param)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glLighti

    Parameters
    ----------

    light : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    param : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glLighti(GLenum light, GLenum pname, GLint
    #      param)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_18glLightiEjji', light, pname, param,
    )

  @overload(int, int, float)
  def glLightf(self, light: int, pname: int, param: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glLightf(GLenum light, GLenum
    pname, GLfloat param)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glLightf

    Parameters
    ----------

    light : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    param : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glLightf(GLenum light, GLenum pname,
    #      GLfloat param)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_18glLightfEjjf', light, pname, param,
    )

  @overload(int, int)
  def glFogi(self, pname: int, param: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glFogi(GLenum pname, GLint
    param)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glFogi

    Parameters
    ----------

    pname : int
      Passed on as it is.

    param : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glFogi(GLenum pname, GLint param)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_16glFogiEji', pname, param,
    )

  @overload(int, float)
  def glFogf(self, pname: int, param: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glFogf(GLenum pname, GLfloat
    param)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glFogf

    Parameters
    ----------

    pname : int
      Passed on as it is.

    param : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glFogf(GLenum pname, GLfloat param)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_16glFogfEjf', pname, param,
    )

  @overload(int, int)
  def glColorMaterial(self, face: int, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glColorMaterial(GLenum face,
    GLenum mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glColorMaterial

    Parameters
    ----------

    face : int
      Passed on as it is.

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glColorMaterial(GLenum face, GLenum mode)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_115glColorMaterialEjj', face, mode,
    )

  @overload(int, int, int, int)
  def glVertex4s(self, x: int, y: int, z: int, w: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glVertex4s(GLshort x, GLshort y,
    GLshort z, GLshort w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glVertex4s

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
    #  void QOpenGLFunctions_1_1::glVertex4s(GLshort x, GLshort y, GLshort z,
    #      GLshort w)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_110glVertex4sEssss', x, y, z, w,
    )

  @overload(int, int, int, int)
  def glVertex4i(self, x: int, y: int, z: int, w: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glVertex4i(GLint x, GLint y, GLint
    z, GLint w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glVertex4i

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
    #  void QOpenGLFunctions_1_1::glVertex4i(GLint x, GLint y, GLint z, GLint
    #      w)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_110glVertex4iEiiii', x, y, z, w,
    )

  @overload(float, float, float, float)
  def glVertex4f(self, x: float, y: float, z: float, w: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glVertex4f(GLfloat x, GLfloat y,
    GLfloat z, GLfloat w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glVertex4f

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
    #  void QOpenGLFunctions_1_1::glVertex4f(GLfloat x, GLfloat y, GLfloat z,
    #      GLfloat w)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_110glVertex4fEffff', x, y, z, w,
    )

  @overload(float, float, float, float)
  def glVertex4d(self, x: float, y: float, z: float, w: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glVertex4d(GLdouble x, GLdouble y,
    GLdouble z, GLdouble w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glVertex4d

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
    #  void QOpenGLFunctions_1_1::glVertex4d(GLdouble x, GLdouble y, GLdouble
    #      z, GLdouble w)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_110glVertex4dEdddd', x, y, z, w,
    )

  @overload(int, int, int)
  def glVertex3s(self, x: int, y: int, z: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glVertex3s(GLshort x, GLshort y,
    GLshort z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glVertex3s

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    z : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glVertex3s(GLshort x, GLshort y, GLshort z)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_110glVertex3sEsss', x, y, z,
    )

  @overload(int, int, int)
  def glVertex3i(self, x: int, y: int, z: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glVertex3i(GLint x, GLint y, GLint
    z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glVertex3i

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    z : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glVertex3i(GLint x, GLint y, GLint z)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_110glVertex3iEiii', x, y, z,
    )

  @overload(float, float, float)
  def glVertex3f(self, x: float, y: float, z: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glVertex3f(GLfloat x, GLfloat y,
    GLfloat z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glVertex3f

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glVertex3f(GLfloat x, GLfloat y, GLfloat z)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_110glVertex3fEfff', x, y, z,
    )

  @overload(float, float, float)
  def glVertex3d(self, x: float, y: float, z: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glVertex3d(GLdouble x, GLdouble y,
    GLdouble z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glVertex3d

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glVertex3d(GLdouble x, GLdouble y, GLdouble
    #      z)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_110glVertex3dEddd', x, y, z,
    )

  @overload(int, int)
  def glVertex2s(self, x: int, y: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glVertex2s(GLshort x, GLshort y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glVertex2s

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glVertex2s(GLshort x, GLshort y)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_110glVertex2sEss', x, y,
    )

  @overload(int, int)
  def glVertex2i(self, x: int, y: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glVertex2i(GLint x, GLint y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glVertex2i

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glVertex2i(GLint x, GLint y)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_110glVertex2iEii', x, y,
    )

  @overload(float, float)
  def glVertex2f(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glVertex2f(GLfloat x, GLfloat y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glVertex2f

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glVertex2f(GLfloat x, GLfloat y)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_110glVertex2fEff', x, y,
    )

  @overload(float, float)
  def glVertex2d(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glVertex2d(GLdouble x, GLdouble
    y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glVertex2d

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glVertex2d(GLdouble x, GLdouble y)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_110glVertex2dEdd', x, y,
    )

  @overload(int, int, int, int)
  def glTexCoord4s(self, s: int, t: int, r: int, q: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glTexCoord4s(GLshort s, GLshort t,
    GLshort r, GLshort q)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glTexCoord4s

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
    #  void QOpenGLFunctions_1_1::glTexCoord4s(GLshort s, GLshort t, GLshort
    #      r, GLshort q)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_112glTexCoord4sEssss', s, t, r, q,
    )

  @overload(int, int, int, int)
  def glTexCoord4i(self, s: int, t: int, r: int, q: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glTexCoord4i(GLint s, GLint t,
    GLint r, GLint q)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glTexCoord4i

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
    #  void QOpenGLFunctions_1_1::glTexCoord4i(GLint s, GLint t, GLint r,
    #      GLint q)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_112glTexCoord4iEiiii', s, t, r, q,
    )

  @overload(float, float, float, float)
  def glTexCoord4f(self, s: float, t: float, r: float, q: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glTexCoord4f(GLfloat s, GLfloat t,
    GLfloat r, GLfloat q)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glTexCoord4f

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
    #  void QOpenGLFunctions_1_1::glTexCoord4f(GLfloat s, GLfloat t, GLfloat
    #      r, GLfloat q)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_112glTexCoord4fEffff', s, t, r, q,
    )

  @overload(float, float, float, float)
  def glTexCoord4d(self, s: float, t: float, r: float, q: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glTexCoord4d(GLdouble s, GLdouble
    t, GLdouble r, GLdouble q)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glTexCoord4d

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
    #  void QOpenGLFunctions_1_1::glTexCoord4d(GLdouble s, GLdouble t,
    #      GLdouble r, GLdouble q)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_112glTexCoord4dEdddd', s, t, r, q,
    )

  @overload(int, int, int)
  def glTexCoord3s(self, s: int, t: int, r: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glTexCoord3s(GLshort s, GLshort t,
    GLshort r)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glTexCoord3s

    Parameters
    ----------

    s : int
      Passed on as it is.

    t : int
      Passed on as it is.

    r : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glTexCoord3s(GLshort s, GLshort t, GLshort
    #      r)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_112glTexCoord3sEsss', s, t, r,
    )

  @overload(int, int, int)
  def glTexCoord3i(self, s: int, t: int, r: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glTexCoord3i(GLint s, GLint t,
    GLint r)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glTexCoord3i

    Parameters
    ----------

    s : int
      Passed on as it is.

    t : int
      Passed on as it is.

    r : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glTexCoord3i(GLint s, GLint t, GLint r)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_112glTexCoord3iEiii', s, t, r,
    )

  @overload(float, float, float)
  def glTexCoord3f(self, s: float, t: float, r: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glTexCoord3f(GLfloat s, GLfloat t,
    GLfloat r)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glTexCoord3f

    Parameters
    ----------

    s : float
      Passed on as it is.

    t : float
      Passed on as it is.

    r : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glTexCoord3f(GLfloat s, GLfloat t, GLfloat
    #      r)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_112glTexCoord3fEfff', s, t, r,
    )

  @overload(float, float, float)
  def glTexCoord3d(self, s: float, t: float, r: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glTexCoord3d(GLdouble s, GLdouble
    t, GLdouble r)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glTexCoord3d

    Parameters
    ----------

    s : float
      Passed on as it is.

    t : float
      Passed on as it is.

    r : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glTexCoord3d(GLdouble s, GLdouble t,
    #      GLdouble r)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_112glTexCoord3dEddd', s, t, r,
    )

  @overload(int, int)
  def glTexCoord2s(self, s: int, t: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glTexCoord2s(GLshort s, GLshort
    t)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glTexCoord2s

    Parameters
    ----------

    s : int
      Passed on as it is.

    t : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glTexCoord2s(GLshort s, GLshort t)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_112glTexCoord2sEss', s, t,
    )

  @overload(int, int)
  def glTexCoord2i(self, s: int, t: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glTexCoord2i(GLint s, GLint t)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glTexCoord2i

    Parameters
    ----------

    s : int
      Passed on as it is.

    t : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glTexCoord2i(GLint s, GLint t)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_112glTexCoord2iEii', s, t,
    )

  @overload(float, float)
  def glTexCoord2f(self, s: float, t: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glTexCoord2f(GLfloat s, GLfloat
    t)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glTexCoord2f

    Parameters
    ----------

    s : float
      Passed on as it is.

    t : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glTexCoord2f(GLfloat s, GLfloat t)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_112glTexCoord2fEff', s, t,
    )

  @overload(float, float)
  def glTexCoord2d(self, s: float, t: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glTexCoord2d(GLdouble s, GLdouble
    t)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glTexCoord2d

    Parameters
    ----------

    s : float
      Passed on as it is.

    t : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glTexCoord2d(GLdouble s, GLdouble t)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_112glTexCoord2dEdd', s, t,
    )

  @overload(int)
  def glTexCoord1s(self, s: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glTexCoord1s(GLshort s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glTexCoord1s

    Parameters
    ----------

    s : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glTexCoord1s(GLshort s)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_1_112glTexCoord1sEs', s)

  @overload(int)
  def glTexCoord1i(self, s: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glTexCoord1i(GLint s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glTexCoord1i

    Parameters
    ----------

    s : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glTexCoord1i(GLint s)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_1_112glTexCoord1iEi', s)

  @overload(float)
  def glTexCoord1f(self, s: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glTexCoord1f(GLfloat s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glTexCoord1f

    Parameters
    ----------

    s : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glTexCoord1f(GLfloat s)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_1_112glTexCoord1fEf', s)

  @overload(float)
  def glTexCoord1d(self, s: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glTexCoord1d(GLdouble s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glTexCoord1d

    Parameters
    ----------

    s : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glTexCoord1d(GLdouble s)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_1_112glTexCoord1dEd', s)

  @overload(int, int, int, int)
  def glRects(self, x1: int, y1: int, x2: int, y2: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glRects(GLshort x1, GLshort y1,
    GLshort x2, GLshort y2)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glRects

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
    #  void QOpenGLFunctions_1_1::glRects(GLshort x1, GLshort y1, GLshort x2,
    #      GLshort y2)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_17glRectsEssss', x1, y1, x2, y2,
    )

  @overload(int, int, int, int)
  def glRecti(self, x1: int, y1: int, x2: int, y2: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glRecti(GLint x1, GLint y1, GLint
    x2, GLint y2)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glRecti

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
    #  void QOpenGLFunctions_1_1::glRecti(GLint x1, GLint y1, GLint x2, GLint
    #      y2)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_17glRectiEiiii', x1, y1, x2, y2,
    )

  @overload(float, float, float, float)
  def glRectf(self, x1: float, y1: float, x2: float, y2: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glRectf(GLfloat x1, GLfloat y1,
    GLfloat x2, GLfloat y2)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glRectf

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
    #  void QOpenGLFunctions_1_1::glRectf(GLfloat x1, GLfloat y1, GLfloat x2,
    #      GLfloat y2)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_17glRectfEffff', x1, y1, x2, y2,
    )

  @overload(float, float, float, float)
  def glRectd(self, x1: float, y1: float, x2: float, y2: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glRectd(GLdouble x1, GLdouble y1,
    GLdouble x2, GLdouble y2)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glRectd

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
    #  void QOpenGLFunctions_1_1::glRectd(GLdouble x1, GLdouble y1, GLdouble
    #      x2, GLdouble y2)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_17glRectdEdddd', x1, y1, x2, y2,
    )

  @overload(int, int, int, int)
  def glRasterPos4s(self, x: int, y: int, z: int, w: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glRasterPos4s(GLshort x, GLshort
    y, GLshort z, GLshort w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glRasterPos4s

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
    #  void QOpenGLFunctions_1_1::glRasterPos4s(GLshort x, GLshort y, GLshort
    #      z, GLshort w)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_113glRasterPos4sEssss', x, y, z, w,
    )

  @overload(int, int, int, int)
  def glRasterPos4i(self, x: int, y: int, z: int, w: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glRasterPos4i(GLint x, GLint y,
    GLint z, GLint w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glRasterPos4i

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
    #  void QOpenGLFunctions_1_1::glRasterPos4i(GLint x, GLint y, GLint z,
    #      GLint w)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_113glRasterPos4iEiiii', x, y, z, w,
    )

  @overload(float, float, float, float)
  def glRasterPos4f(self, x: float, y: float, z: float, w: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glRasterPos4f(GLfloat x, GLfloat
    y, GLfloat z, GLfloat w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glRasterPos4f

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
    #  void QOpenGLFunctions_1_1::glRasterPos4f(GLfloat x, GLfloat y, GLfloat
    #      z, GLfloat w)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_113glRasterPos4fEffff', x, y, z, w,
    )

  @overload(float, float, float, float)
  def glRasterPos4d(self, x: float, y: float, z: float, w: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glRasterPos4d(GLdouble x, GLdouble
    y, GLdouble z, GLdouble w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glRasterPos4d

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
    #  void QOpenGLFunctions_1_1::glRasterPos4d(GLdouble x, GLdouble y,
    #      GLdouble z, GLdouble w)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_113glRasterPos4dEdddd', x, y, z, w,
    )

  @overload(int, int, int)
  def glRasterPos3s(self, x: int, y: int, z: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glRasterPos3s(GLshort x, GLshort
    y, GLshort z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glRasterPos3s

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    z : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glRasterPos3s(GLshort x, GLshort y, GLshort
    #      z)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_113glRasterPos3sEsss', x, y, z,
    )

  @overload(int, int, int)
  def glRasterPos3i(self, x: int, y: int, z: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glRasterPos3i(GLint x, GLint y,
    GLint z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glRasterPos3i

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    z : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glRasterPos3i(GLint x, GLint y, GLint z)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_113glRasterPos3iEiii', x, y, z,
    )

  @overload(float, float, float)
  def glRasterPos3f(self, x: float, y: float, z: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glRasterPos3f(GLfloat x, GLfloat
    y, GLfloat z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glRasterPos3f

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glRasterPos3f(GLfloat x, GLfloat y, GLfloat
    #      z)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_113glRasterPos3fEfff', x, y, z,
    )

  @overload(float, float, float)
  def glRasterPos3d(self, x: float, y: float, z: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glRasterPos3d(GLdouble x, GLdouble
    y, GLdouble z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glRasterPos3d

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glRasterPos3d(GLdouble x, GLdouble y,
    #      GLdouble z)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_113glRasterPos3dEddd', x, y, z,
    )

  @overload(int, int)
  def glRasterPos2s(self, x: int, y: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glRasterPos2s(GLshort x, GLshort
    y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glRasterPos2s

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glRasterPos2s(GLshort x, GLshort y)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_113glRasterPos2sEss', x, y,
    )

  @overload(int, int)
  def glRasterPos2i(self, x: int, y: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glRasterPos2i(GLint x, GLint y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glRasterPos2i

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glRasterPos2i(GLint x, GLint y)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_113glRasterPos2iEii', x, y,
    )

  @overload(float, float)
  def glRasterPos2f(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glRasterPos2f(GLfloat x, GLfloat
    y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glRasterPos2f

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glRasterPos2f(GLfloat x, GLfloat y)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_113glRasterPos2fEff', x, y,
    )

  @overload(float, float)
  def glRasterPos2d(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glRasterPos2d(GLdouble x, GLdouble
    y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glRasterPos2d

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glRasterPos2d(GLdouble x, GLdouble y)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_113glRasterPos2dEdd', x, y,
    )

  @overload(int, int, int)
  def glNormal3s(self, nx: int, ny: int, nz: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glNormal3s(GLshort nx, GLshort ny,
    GLshort nz)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glNormal3s

    Parameters
    ----------

    nx : int
      Passed on as it is.

    ny : int
      Passed on as it is.

    nz : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glNormal3s(GLshort nx, GLshort ny, GLshort
    #      nz)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_110glNormal3sEsss', nx, ny, nz,
    )

  @overload(int, int, int)
  def glNormal3i(self, nx: int, ny: int, nz: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glNormal3i(GLint nx, GLint ny,
    GLint nz)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glNormal3i

    Parameters
    ----------

    nx : int
      Passed on as it is.

    ny : int
      Passed on as it is.

    nz : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glNormal3i(GLint nx, GLint ny, GLint nz)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_110glNormal3iEiii', nx, ny, nz,
    )

  @overload(float, float, float)
  def glNormal3f(self, nx: float, ny: float, nz: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glNormal3f(GLfloat nx, GLfloat ny,
    GLfloat nz)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glNormal3f

    Parameters
    ----------

    nx : float
      Passed on as it is.

    ny : float
      Passed on as it is.

    nz : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glNormal3f(GLfloat nx, GLfloat ny, GLfloat
    #      nz)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_110glNormal3fEfff', nx, ny, nz,
    )

  @overload(float, float, float)
  def glNormal3d(self, nx: float, ny: float, nz: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glNormal3d(GLdouble nx, GLdouble
    ny, GLdouble nz)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glNormal3d

    Parameters
    ----------

    nx : float
      Passed on as it is.

    ny : float
      Passed on as it is.

    nz : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glNormal3d(GLdouble nx, GLdouble ny,
    #      GLdouble nz)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_110glNormal3dEddd', nx, ny, nz,
    )

  @overload(int, int, int)
  def glNormal3b(self, nx: int, ny: int, nz: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glNormal3b(GLbyte nx, GLbyte ny,
    GLbyte nz)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glNormal3b

    Parameters
    ----------

    nx : int
      Passed on as it is.

    ny : int
      Passed on as it is.

    nz : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glNormal3b(GLbyte nx, GLbyte ny, GLbyte nz)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_110glNormal3bEaaa', nx, ny, nz,
    )

  @overload(int)
  def glIndexs(self, c: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glIndexs(GLshort c)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glIndexs

    Parameters
    ----------

    c : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glIndexs(GLshort c)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_1_18glIndexsEs', c)

  @overload(int)
  def glIndexi(self, c: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glIndexi(GLint c)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glIndexi

    Parameters
    ----------

    c : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glIndexi(GLint c)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_1_18glIndexiEi', c)

  @overload(float)
  def glIndexf(self, c: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glIndexf(GLfloat c)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glIndexf

    Parameters
    ----------

    c : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glIndexf(GLfloat c)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_1_18glIndexfEf', c)

  @overload(float)
  def glIndexd(self, c: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glIndexd(GLdouble c)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glIndexd

    Parameters
    ----------

    c : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glIndexd(GLdouble c)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_1_18glIndexdEd', c)

  def glEnd(self) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glEnd()'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glEnd
    """
    #  void QOpenGLFunctions_1_1::glEnd()
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_1_15glEndEv')

  @overload(int)
  def glEdgeFlag(self, flag: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glEdgeFlag(GLboolean flag)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glEdgeFlag

    Parameters
    ----------

    flag : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glEdgeFlag(GLboolean flag)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_1_110glEdgeFlagEh', flag)

  @overload(int, int, int, int)
  def glColor4us(self, red: int, green: int, blue: int, alpha: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glColor4us(GLushort red, GLushort
    green, GLushort blue, GLushort alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glColor4us

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
    #  void QOpenGLFunctions_1_1::glColor4us(GLushort red, GLushort green,
    #      GLushort blue, GLushort alpha)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_110glColor4usEtttt',
        red, green, blue, alpha,
    )

  @overload(int, int, int, int)
  def glColor4ui(self, red: int, green: int, blue: int, alpha: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glColor4ui(GLuint red, GLuint
    green, GLuint blue, GLuint alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glColor4ui

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
    #  void QOpenGLFunctions_1_1::glColor4ui(GLuint red, GLuint green, GLuint
    #      blue, GLuint alpha)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_110glColor4uiEjjjj',
        red, green, blue, alpha,
    )

  @overload(int, int, int, int)
  def glColor4ub(self, red: int, green: int, blue: int, alpha: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glColor4ub(GLubyte red, GLubyte
    green, GLubyte blue, GLubyte alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glColor4ub

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
    #  void QOpenGLFunctions_1_1::glColor4ub(GLubyte red, GLubyte green,
    #      GLubyte blue, GLubyte alpha)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_110glColor4ubEhhhh',
        red, green, blue, alpha,
    )

  @overload(int, int, int, int)
  def glColor4s(self, red: int, green: int, blue: int, alpha: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glColor4s(GLshort red, GLshort
    green, GLshort blue, GLshort alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glColor4s

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
    #  void QOpenGLFunctions_1_1::glColor4s(GLshort red, GLshort green,
    #      GLshort blue, GLshort alpha)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_19glColor4sEssss',
        red, green, blue, alpha,
    )

  @overload(int, int, int, int)
  def glColor4i(self, red: int, green: int, blue: int, alpha: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glColor4i(GLint red, GLint green,
    GLint blue, GLint alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glColor4i

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
    #  void QOpenGLFunctions_1_1::glColor4i(GLint red, GLint green, GLint
    #      blue, GLint alpha)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_19glColor4iEiiii',
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
    Calls Qt's 'void QOpenGLFunctions_1_1::glColor4f(GLfloat red, GLfloat
    green, GLfloat blue, GLfloat alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glColor4f

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
    #  void QOpenGLFunctions_1_1::glColor4f(GLfloat red, GLfloat green,
    #      GLfloat blue, GLfloat alpha)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_19glColor4fEffff',
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
    Calls Qt's 'void QOpenGLFunctions_1_1::glColor4d(GLdouble red, GLdouble
    green, GLdouble blue, GLdouble alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glColor4d

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
    #  void QOpenGLFunctions_1_1::glColor4d(GLdouble red, GLdouble green,
    #      GLdouble blue, GLdouble alpha)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_19glColor4dEdddd',
        red, green, blue, alpha,
    )

  @overload(int, int, int, int)
  def glColor4b(self, red: int, green: int, blue: int, alpha: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glColor4b(GLbyte red, GLbyte
    green, GLbyte blue, GLbyte alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glColor4b

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
    #  void QOpenGLFunctions_1_1::glColor4b(GLbyte red, GLbyte green, GLbyte
    #      blue, GLbyte alpha)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_19glColor4bEaaaa',
        red, green, blue, alpha,
    )

  @overload(int, int, int)
  def glColor3us(self, red: int, green: int, blue: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glColor3us(GLushort red, GLushort
    green, GLushort blue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glColor3us

    Parameters
    ----------

    red : int
      Passed on as it is.

    green : int
      Passed on as it is.

    blue : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glColor3us(GLushort red, GLushort green,
    #      GLushort blue)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_110glColor3usEttt', red, green, blue,
    )

  @overload(int, int, int)
  def glColor3ui(self, red: int, green: int, blue: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glColor3ui(GLuint red, GLuint
    green, GLuint blue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glColor3ui

    Parameters
    ----------

    red : int
      Passed on as it is.

    green : int
      Passed on as it is.

    blue : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glColor3ui(GLuint red, GLuint green, GLuint
    #      blue)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_110glColor3uiEjjj', red, green, blue,
    )

  @overload(int, int, int)
  def glColor3ub(self, red: int, green: int, blue: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glColor3ub(GLubyte red, GLubyte
    green, GLubyte blue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glColor3ub

    Parameters
    ----------

    red : int
      Passed on as it is.

    green : int
      Passed on as it is.

    blue : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glColor3ub(GLubyte red, GLubyte green,
    #      GLubyte blue)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_110glColor3ubEhhh', red, green, blue,
    )

  @overload(int, int, int)
  def glColor3s(self, red: int, green: int, blue: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glColor3s(GLshort red, GLshort
    green, GLshort blue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glColor3s

    Parameters
    ----------

    red : int
      Passed on as it is.

    green : int
      Passed on as it is.

    blue : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glColor3s(GLshort red, GLshort green,
    #      GLshort blue)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_19glColor3sEsss', red, green, blue,
    )

  @overload(int, int, int)
  def glColor3i(self, red: int, green: int, blue: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glColor3i(GLint red, GLint green,
    GLint blue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glColor3i

    Parameters
    ----------

    red : int
      Passed on as it is.

    green : int
      Passed on as it is.

    blue : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glColor3i(GLint red, GLint green, GLint
    #      blue)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_19glColor3iEiii', red, green, blue,
    )

  @overload(float, float, float)
  def glColor3f(self, red: float, green: float, blue: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glColor3f(GLfloat red, GLfloat
    green, GLfloat blue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glColor3f

    Parameters
    ----------

    red : float
      Passed on as it is.

    green : float
      Passed on as it is.

    blue : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glColor3f(GLfloat red, GLfloat green,
    #      GLfloat blue)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_19glColor3fEfff', red, green, blue,
    )

  @overload(float, float, float)
  def glColor3d(self, red: float, green: float, blue: float) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glColor3d(GLdouble red, GLdouble
    green, GLdouble blue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glColor3d

    Parameters
    ----------

    red : float
      Passed on as it is.

    green : float
      Passed on as it is.

    blue : float
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glColor3d(GLdouble red, GLdouble green,
    #      GLdouble blue)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_19glColor3dEddd', red, green, blue,
    )

  @overload(int, int, int)
  def glColor3b(self, red: int, green: int, blue: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glColor3b(GLbyte red, GLbyte
    green, GLbyte blue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glColor3b

    Parameters
    ----------

    red : int
      Passed on as it is.

    green : int
      Passed on as it is.

    blue : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glColor3b(GLbyte red, GLbyte green, GLbyte
    #      blue)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_19glColor3bEaaa', red, green, blue,
    )

  @overload(int)
  def glBegin(self, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glBegin(GLenum mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glBegin

    Parameters
    ----------

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glBegin(GLenum mode)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_1_17glBeginEj', mode)

  @overload(int)
  def glListBase(self, base: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glListBase(GLuint base)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glListBase

    Parameters
    ----------

    base : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glListBase(GLuint base)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_1_110glListBaseEj', base)

  @overload(int)
  def glGenLists(self, range: int) -> int:
    """
    Calls Qt's 'GLuint QOpenGLFunctions_1_1::glGenLists(GLsizei range)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glGenLists

    Parameters
    ----------

    range : int
      Passed on as it is.
    """
    #  GLuint QOpenGLFunctions_1_1::glGenLists(GLsizei range)
    return self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_110glGenListsEi', range,
    )

  @overload(int, int)
  def glDeleteLists(self, list: int, range: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glDeleteLists(GLuint list, GLsizei
    range)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glDeleteLists

    Parameters
    ----------

    list : int
      Passed on as it is.

    range : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glDeleteLists(GLuint list, GLsizei range)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_113glDeleteListsEji', list, range,
    )

  @overload(int)
  def glCallList(self, list: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glCallList(GLuint list)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glCallList

    Parameters
    ----------

    list : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glCallList(GLuint list)
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_1_110glCallListEj', list)

  def glEndList(self) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glEndList()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glEndList
    """
    #  void QOpenGLFunctions_1_1::glEndList()
    self.uglySide.call('ritual_ZN20QOpenGLFunctions_1_19glEndListEv')

  @overload(int, int)
  def glNewList(self, list: int, mode: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glNewList(GLuint list, GLenum
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glNewList

    Parameters
    ----------

    list : int
      Passed on as it is.

    mode : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glNewList(GLuint list, GLenum mode)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_19glNewListEjj', list, mode,
    )

  @overload(int)
  def glPushClientAttrib(self, mask: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glPushClientAttrib(GLbitfield
    mask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glPushClientAttrib

    Parameters
    ----------

    mask : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glPushClientAttrib(GLbitfield mask)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_118glPushClientAttribEj', mask,
    )

  def glPopClientAttrib(self) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glPopClientAttrib()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glPopClientAttrib
    """
    #  void QOpenGLFunctions_1_1::glPopClientAttrib()
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_117glPopClientAttribEv',
    )

  @overload(int)
  def glEnableClientState(self, array: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glEnableClientState(GLenum
    array)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glEnableClientState

    Parameters
    ----------

    array : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glEnableClientState(GLenum array)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_119glEnableClientStateEj', array,
    )

  @overload(int)
  def glDisableClientState(self, array: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glDisableClientState(GLenum
    array)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glDisableClientState

    Parameters
    ----------

    array : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glDisableClientState(GLenum array)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_120glDisableClientStateEj', array,
    )

  @overload(int)
  def glArrayElement(self, i: int) -> None:
    """
    Calls Qt's 'void QOpenGLFunctions_1_1::glArrayElement(GLint i)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_1.html#glArrayElement

    Parameters
    ----------

    i : int
      Passed on as it is.
    """
    #  void QOpenGLFunctions_1_1::glArrayElement(GLint i)
    self.uglySide.call(
        'ritual_ZN20QOpenGLFunctions_1_114glArrayElementEi', i,
    )

  @staticmethod
  def glAreTexturesResident(*__, **_) -> Never:
    """
    Qt's 'GLboolean QOpenGLFunctions_1_1::glAreTexturesResident(GLsizei n,
    const GLuint *textures, GLboolean *residences)': names 'GLuint', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glAreTexturesResident' has no cute function "
        "yet. Qt's 'GLboolean "
        "QOpenGLFunctions_1_1::glAreTexturesResident(GLsizei n, const "
        "GLuint *textures, GLboolean *residences)': names 'GLuint', which "
        "has no cute class yet.")

  @staticmethod
  def glBitmap(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glBitmap(GLsizei width, GLsizei height,
    GLfloat xorig, GLfloat yorig, GLfloat xmove, GLfloat ymove, const GLubyte
    *bitmap)': names 'GLubyte', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glBitmap' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glBitmap(GLsizei width, GLsizei "
        "height, GLfloat xorig, GLfloat yorig, GLfloat xmove, GLfloat "
        "ymove, const GLubyte *bitmap)': names 'GLubyte', which has no cute "
        "class yet.")

  @staticmethod
  def glCallLists(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glCallLists(GLsizei n, GLenum type,
    const GLvoid *lists)': names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glCallLists' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glCallLists(GLsizei n, GLenum type, "
        "const GLvoid *lists)': names 'GLvoid', which has no cute class yet."
    )

  @staticmethod
  def glClipPlane(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glClipPlane(GLenum plane, const GLdouble
    *equation)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glClipPlane' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glClipPlane(GLenum plane, const "
        "GLdouble *equation)': names 'GLdouble', which has no cute class "
        "yet.")

  @staticmethod
  def glColor3bv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glColor3bv(const GLbyte *v)': names
    'GLbyte', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glColor3bv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glColor3bv(const GLbyte *v)': names "
        "'GLbyte', which has no cute class yet.")

  @staticmethod
  def glColor3dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glColor3dv(const GLdouble *v)': names
    'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glColor3dv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glColor3dv(const GLdouble *v)': names "
        "'GLdouble', which has no cute class yet.")

  @staticmethod
  def glColor3fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glColor3fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glColor3fv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glColor3fv(const GLfloat *v)': names "
        "'GLfloat', which has no cute class yet.")

  @staticmethod
  def glColor3iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glColor3iv(const GLint *v)': names
    'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glColor3iv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glColor3iv(const GLint *v)': names "
        "'GLint', which has no cute class yet.")

  @staticmethod
  def glColor3sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glColor3sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glColor3sv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glColor3sv(const GLshort *v)': names "
        "'GLshort', which has no cute class yet.")

  @staticmethod
  def glColor3ubv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glColor3ubv(const GLubyte *v)': names
    'GLubyte', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glColor3ubv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glColor3ubv(const GLubyte *v)': names "
        "'GLubyte', which has no cute class yet.")

  @staticmethod
  def glColor3uiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glColor3uiv(const GLuint *v)': names
    'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glColor3uiv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glColor3uiv(const GLuint *v)': names "
        "'GLuint', which has no cute class yet.")

  @staticmethod
  def glColor3usv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glColor3usv(const GLushort *v)': names
    'GLushort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glColor3usv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glColor3usv(const GLushort *v)': names "
        "'GLushort', which has no cute class yet.")

  @staticmethod
  def glColor4bv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glColor4bv(const GLbyte *v)': names
    'GLbyte', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glColor4bv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glColor4bv(const GLbyte *v)': names "
        "'GLbyte', which has no cute class yet.")

  @staticmethod
  def glColor4dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glColor4dv(const GLdouble *v)': names
    'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glColor4dv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glColor4dv(const GLdouble *v)': names "
        "'GLdouble', which has no cute class yet.")

  @staticmethod
  def glColor4fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glColor4fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glColor4fv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glColor4fv(const GLfloat *v)': names "
        "'GLfloat', which has no cute class yet.")

  @staticmethod
  def glColor4iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glColor4iv(const GLint *v)': names
    'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glColor4iv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glColor4iv(const GLint *v)': names "
        "'GLint', which has no cute class yet.")

  @staticmethod
  def glColor4sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glColor4sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glColor4sv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glColor4sv(const GLshort *v)': names "
        "'GLshort', which has no cute class yet.")

  @staticmethod
  def glColor4ubv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glColor4ubv(const GLubyte *v)': names
    'GLubyte', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glColor4ubv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glColor4ubv(const GLubyte *v)': names "
        "'GLubyte', which has no cute class yet.")

  @staticmethod
  def glColor4uiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glColor4uiv(const GLuint *v)': names
    'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glColor4uiv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glColor4uiv(const GLuint *v)': names "
        "'GLuint', which has no cute class yet.")

  @staticmethod
  def glColor4usv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glColor4usv(const GLushort *v)': names
    'GLushort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glColor4usv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glColor4usv(const GLushort *v)': names "
        "'GLushort', which has no cute class yet.")

  @staticmethod
  def glColorPointer(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glColorPointer(GLint size, GLenum type,
    GLsizei stride, const GLvoid *pointer)': names 'GLvoid', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glColorPointer' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_1::glColorPointer(GLint size, GLenum "
        "type, GLsizei stride, const GLvoid *pointer)': names 'GLvoid', "
        "which has no cute class yet.")

  @staticmethod
  def glDeleteTextures(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glDeleteTextures(GLsizei n, const GLuint
    *textures)': names 'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glDeleteTextures' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_1::glDeleteTextures(GLsizei n, const "
        "GLuint *textures)': names 'GLuint', which has no cute class yet.")

  @staticmethod
  def glDrawElements(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glDrawElements(GLenum mode, GLsizei
    count, GLenum type, const GLvoid *indices)': names 'GLvoid', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glDrawElements' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_1::glDrawElements(GLenum mode, "
        "GLsizei count, GLenum type, const GLvoid *indices)': names "
        "'GLvoid', which has no cute class yet.")

  @staticmethod
  def glDrawPixels(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glDrawPixels(GLsizei width, GLsizei
    height, GLenum format, GLenum type, const GLvoid *pixels)': names
    'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glDrawPixels' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glDrawPixels(GLsizei width, GLsizei "
        "height, GLenum format, GLenum type, const GLvoid *pixels)': names "
        "'GLvoid', which has no cute class yet.")

  @staticmethod
  def glEdgeFlagPointer(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glEdgeFlagPointer(GLsizei stride, const
    GLvoid *pointer)': names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glEdgeFlagPointer' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_1::glEdgeFlagPointer(GLsizei stride, "
        "const GLvoid *pointer)': names 'GLvoid', which has no cute class "
        "yet.")

  @staticmethod
  def glEdgeFlagv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glEdgeFlagv(const GLboolean *flag)':
    names 'GLboolean', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glEdgeFlagv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glEdgeFlagv(const GLboolean *flag)': "
        "names 'GLboolean', which has no cute class yet.")

  @staticmethod
  def glEvalCoord1dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glEvalCoord1dv(const GLdouble *u)':
    names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glEvalCoord1dv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_1::glEvalCoord1dv(const GLdouble "
        "*u)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glEvalCoord1fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glEvalCoord1fv(const GLfloat *u)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glEvalCoord1fv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_1::glEvalCoord1fv(const GLfloat "
        "*u)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glEvalCoord2dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glEvalCoord2dv(const GLdouble *u)':
    names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glEvalCoord2dv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_1::glEvalCoord2dv(const GLdouble "
        "*u)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glEvalCoord2fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glEvalCoord2fv(const GLfloat *u)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glEvalCoord2fv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_1::glEvalCoord2fv(const GLfloat "
        "*u)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glFeedbackBuffer(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glFeedbackBuffer(GLsizei size, GLenum
    type, GLfloat *buffer)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glFeedbackBuffer' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_1::glFeedbackBuffer(GLsizei size, "
        "GLenum type, GLfloat *buffer)': takes a number to change where it "
        "is.")

  @staticmethod
  def glFogfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glFogfv(GLenum pname, const GLfloat
    *params)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glFogfv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glFogfv(GLenum pname, const GLfloat "
        "*params)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glFogiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glFogiv(GLenum pname, const GLint
    *params)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glFogiv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glFogiv(GLenum pname, const GLint "
        "*params)': names 'GLint', which has no cute class yet.")

  @staticmethod
  def glGenTextures(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glGenTextures(GLsizei n, GLuint
    *textures)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glGenTextures' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_1::glGenTextures(GLsizei n, GLuint "
        "*textures)': takes a number to change where it is.")

  @staticmethod
  def glGetBooleanv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glGetBooleanv(GLenum pname, GLboolean
    *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glGetBooleanv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_1::glGetBooleanv(GLenum pname, "
        "GLboolean *params)': takes a number to change where it is.")

  @staticmethod
  def glGetClipPlane(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glGetClipPlane(GLenum plane, GLdouble
    *equation)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glGetClipPlane' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_1::glGetClipPlane(GLenum plane, "
        "GLdouble *equation)': takes a number to change where it is.")

  @staticmethod
  def glGetDoublev(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glGetDoublev(GLenum pname, GLdouble
    *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glGetDoublev' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glGetDoublev(GLenum pname, GLdouble "
        "*params)': takes a number to change where it is.")

  @staticmethod
  def glGetFloatv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glGetFloatv(GLenum pname, GLfloat
    *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glGetFloatv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glGetFloatv(GLenum pname, GLfloat "
        "*params)': takes a number to change where it is.")

  @staticmethod
  def glGetIntegerv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glGetIntegerv(GLenum pname, GLint
    *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glGetIntegerv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_1::glGetIntegerv(GLenum pname, GLint "
        "*params)': takes a number to change where it is.")

  @staticmethod
  def glGetLightfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glGetLightfv(GLenum light, GLenum pname,
    GLfloat *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glGetLightfv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glGetLightfv(GLenum light, GLenum "
        "pname, GLfloat *params)': takes a number to change where it is.")

  @staticmethod
  def glGetLightiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glGetLightiv(GLenum light, GLenum pname,
    GLint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glGetLightiv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glGetLightiv(GLenum light, GLenum "
        "pname, GLint *params)': takes a number to change where it is.")

  @staticmethod
  def glGetMapdv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glGetMapdv(GLenum target, GLenum query,
    GLdouble *v)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glGetMapdv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glGetMapdv(GLenum target, GLenum "
        "query, GLdouble *v)': takes a number to change where it is.")

  @staticmethod
  def glGetMapfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glGetMapfv(GLenum target, GLenum query,
    GLfloat *v)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glGetMapfv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glGetMapfv(GLenum target, GLenum "
        "query, GLfloat *v)': takes a number to change where it is.")

  @staticmethod
  def glGetMapiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glGetMapiv(GLenum target, GLenum query,
    GLint *v)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glGetMapiv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glGetMapiv(GLenum target, GLenum "
        "query, GLint *v)': takes a number to change where it is.")

  @staticmethod
  def glGetMaterialfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glGetMaterialfv(GLenum face, GLenum
    pname, GLfloat *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glGetMaterialfv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_1::glGetMaterialfv(GLenum face, "
        "GLenum pname, GLfloat *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetMaterialiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glGetMaterialiv(GLenum face, GLenum
    pname, GLint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glGetMaterialiv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_1::glGetMaterialiv(GLenum face, "
        "GLenum pname, GLint *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetPixelMapfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glGetPixelMapfv(GLenum map, GLfloat
    *values)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glGetPixelMapfv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_1::glGetPixelMapfv(GLenum map, "
        "GLfloat *values)': takes a number to change where it is.")

  @staticmethod
  def glGetPixelMapuiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glGetPixelMapuiv(GLenum map, GLuint
    *values)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glGetPixelMapuiv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_1::glGetPixelMapuiv(GLenum map, "
        "GLuint *values)': takes a number to change where it is.")

  @staticmethod
  def glGetPixelMapusv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glGetPixelMapusv(GLenum map, GLushort
    *values)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glGetPixelMapusv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_1::glGetPixelMapusv(GLenum map, "
        "GLushort *values)': takes a number to change where it is.")

  @staticmethod
  def glGetPointerv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glGetPointerv(GLenum pname, GLvoid
    **params)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glGetPointerv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_1::glGetPointerv(GLenum pname, "
        "GLvoid **params)': takes a type Python has no way to hand over yet."
    )

  @staticmethod
  def glGetPolygonStipple(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glGetPolygonStipple(GLubyte *mask)':
    takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glGetPolygonStipple' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_1_1::glGetPolygonStipple(GLubyte "
        "*mask)': takes a number to change where it is.")

  @staticmethod
  def glGetString(*__, **_) -> Never:
    """
    Qt's 'const GLubyte *QOpenGLFunctions_1_1::glGetString(GLenum name)':
    gives 'unsigned char', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glGetString' has no cute function yet. Qt's "
        "'const GLubyte *QOpenGLFunctions_1_1::glGetString(GLenum name)': "
        "gives 'unsigned char', which has no cute class yet.")

  @staticmethod
  def glGetTexEnvfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glGetTexEnvfv(GLenum target, GLenum
    pname, GLfloat *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glGetTexEnvfv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_1::glGetTexEnvfv(GLenum target, "
        "GLenum pname, GLfloat *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetTexEnviv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glGetTexEnviv(GLenum target, GLenum
    pname, GLint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glGetTexEnviv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_1::glGetTexEnviv(GLenum target, "
        "GLenum pname, GLint *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetTexGendv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glGetTexGendv(GLenum coord, GLenum
    pname, GLdouble *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glGetTexGendv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_1::glGetTexGendv(GLenum coord, "
        "GLenum pname, GLdouble *params)': takes a number to change where "
        "it is.")

  @staticmethod
  def glGetTexGenfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glGetTexGenfv(GLenum coord, GLenum
    pname, GLfloat *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glGetTexGenfv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_1::glGetTexGenfv(GLenum coord, "
        "GLenum pname, GLfloat *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetTexGeniv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glGetTexGeniv(GLenum coord, GLenum
    pname, GLint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glGetTexGeniv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_1::glGetTexGeniv(GLenum coord, "
        "GLenum pname, GLint *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetTexImage(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glGetTexImage(GLenum target, GLint
    level, GLenum format, GLenum type, GLvoid *pixels)': names 'GLvoid',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glGetTexImage' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_1::glGetTexImage(GLenum target, "
        "GLint level, GLenum format, GLenum type, GLvoid *pixels)': names "
        "'GLvoid', which has no cute class yet.")

  @staticmethod
  def glGetTexLevelParameterfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glGetTexLevelParameterfv(GLenum target,
    GLint level, GLenum pname, GLfloat *params)': takes a number to change
    where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glGetTexLevelParameterfv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_1_1::glGetTexLevelParameterfv(GLenum target, "
        "GLint level, GLenum pname, GLfloat *params)': takes a number to "
        "change where it is.")

  @staticmethod
  def glGetTexLevelParameteriv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glGetTexLevelParameteriv(GLenum target,
    GLint level, GLenum pname, GLint *params)': takes a number to change
    where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glGetTexLevelParameteriv' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFunctions_1_1::glGetTexLevelParameteriv(GLenum target, "
        "GLint level, GLenum pname, GLint *params)': takes a number to "
        "change where it is.")

  @staticmethod
  def glGetTexParameterfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glGetTexParameterfv(GLenum target,
    GLenum pname, GLfloat *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glGetTexParameterfv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_1_1::glGetTexParameterfv(GLenum "
        "target, GLenum pname, GLfloat *params)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetTexParameteriv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glGetTexParameteriv(GLenum target,
    GLenum pname, GLint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glGetTexParameteriv' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_1_1::glGetTexParameteriv(GLenum "
        "target, GLenum pname, GLint *params)': takes a number to change "
        "where it is.")

  @staticmethod
  def glIndexPointer(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glIndexPointer(GLenum type, GLsizei
    stride, const GLvoid *pointer)': names 'GLvoid', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glIndexPointer' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_1::glIndexPointer(GLenum type, "
        "GLsizei stride, const GLvoid *pointer)': names 'GLvoid', which has "
        "no cute class yet.")

  @staticmethod
  def glIndexdv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glIndexdv(const GLdouble *c)': names
    'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glIndexdv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glIndexdv(const GLdouble *c)': names "
        "'GLdouble', which has no cute class yet.")

  @staticmethod
  def glIndexfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glIndexfv(const GLfloat *c)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glIndexfv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glIndexfv(const GLfloat *c)': names "
        "'GLfloat', which has no cute class yet.")

  @staticmethod
  def glIndexiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glIndexiv(const GLint *c)': names
    'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glIndexiv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glIndexiv(const GLint *c)': names "
        "'GLint', which has no cute class yet.")

  @staticmethod
  def glIndexsv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glIndexsv(const GLshort *c)': names
    'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glIndexsv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glIndexsv(const GLshort *c)': names "
        "'GLshort', which has no cute class yet.")

  @staticmethod
  def glIndexubv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glIndexubv(const GLubyte *c)': names
    'GLubyte', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glIndexubv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glIndexubv(const GLubyte *c)': names "
        "'GLubyte', which has no cute class yet.")

  @staticmethod
  def glInterleavedArrays(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glInterleavedArrays(GLenum format,
    GLsizei stride, const GLvoid *pointer)': names 'GLvoid', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glInterleavedArrays' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_1_1::glInterleavedArrays(GLenum "
        "format, GLsizei stride, const GLvoid *pointer)': names 'GLvoid', "
        "which has no cute class yet.")

  @staticmethod
  def glLightModelfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glLightModelfv(GLenum pname, const
    GLfloat *params)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glLightModelfv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_1::glLightModelfv(GLenum pname, "
        "const GLfloat *params)': names 'GLfloat', which has no cute class "
        "yet.")

  @staticmethod
  def glLightModeliv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glLightModeliv(GLenum pname, const GLint
    *params)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glLightModeliv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_1::glLightModeliv(GLenum pname, "
        "const GLint *params)': names 'GLint', which has no cute class yet.")

  @staticmethod
  def glLightfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glLightfv(GLenum light, GLenum pname,
    const GLfloat *params)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glLightfv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glLightfv(GLenum light, GLenum pname, "
        "const GLfloat *params)': names 'GLfloat', which has no cute class "
        "yet.")

  @staticmethod
  def glLightiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glLightiv(GLenum light, GLenum pname,
    const GLint *params)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glLightiv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glLightiv(GLenum light, GLenum pname, "
        "const GLint *params)': names 'GLint', which has no cute class yet.")

  @staticmethod
  def glLoadMatrixd(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glLoadMatrixd(const GLdouble *m)': names
    'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glLoadMatrixd' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_1::glLoadMatrixd(const GLdouble "
        "*m)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glLoadMatrixf(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glLoadMatrixf(const GLfloat *m)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glLoadMatrixf' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_1::glLoadMatrixf(const GLfloat *m)': "
        "names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glMap1d(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glMap1d(GLenum target, GLdouble u1,
    GLdouble u2, GLint stride, GLint order, const GLdouble *points)': names
    'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glMap1d' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glMap1d(GLenum target, GLdouble u1, "
        "GLdouble u2, GLint stride, GLint order, const GLdouble *points)': "
        "names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glMap1f(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glMap1f(GLenum target, GLfloat u1,
    GLfloat u2, GLint stride, GLint order, const GLfloat *points)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glMap1f' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glMap1f(GLenum target, GLfloat u1, "
        "GLfloat u2, GLint stride, GLint order, const GLfloat *points)': "
        "names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glMap2d(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glMap2d(GLenum target, GLdouble u1,
    GLdouble u2, GLint ustride, GLint uorder, GLdouble v1, GLdouble v2, GLint
    vstride, GLint vorder, const GLdouble *points)': names 'GLdouble', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glMap2d' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glMap2d(GLenum target, GLdouble u1, "
        "GLdouble u2, GLint ustride, GLint uorder, GLdouble v1, GLdouble "
        "v2, GLint vstride, GLint vorder, const GLdouble *points)': names "
        "'GLdouble', which has no cute class yet.")

  @staticmethod
  def glMap2f(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glMap2f(GLenum target, GLfloat u1,
    GLfloat u2, GLint ustride, GLint uorder, GLfloat v1, GLfloat v2, GLint
    vstride, GLint vorder, const GLfloat *points)': names 'GLfloat', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glMap2f' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glMap2f(GLenum target, GLfloat u1, "
        "GLfloat u2, GLint ustride, GLint uorder, GLfloat v1, GLfloat v2, "
        "GLint vstride, GLint vorder, const GLfloat *points)': names "
        "'GLfloat', which has no cute class yet.")

  @staticmethod
  def glMaterialfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glMaterialfv(GLenum face, GLenum pname,
    const GLfloat *params)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glMaterialfv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glMaterialfv(GLenum face, GLenum "
        "pname, const GLfloat *params)': names 'GLfloat', which has no cute "
        "class yet.")

  @staticmethod
  def glMaterialiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glMaterialiv(GLenum face, GLenum pname,
    const GLint *params)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glMaterialiv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glMaterialiv(GLenum face, GLenum "
        "pname, const GLint *params)': names 'GLint', which has no cute "
        "class yet.")

  @staticmethod
  def glMultMatrixd(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glMultMatrixd(const GLdouble *m)': names
    'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glMultMatrixd' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_1::glMultMatrixd(const GLdouble "
        "*m)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glMultMatrixf(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glMultMatrixf(const GLfloat *m)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glMultMatrixf' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_1::glMultMatrixf(const GLfloat *m)': "
        "names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glNormal3bv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glNormal3bv(const GLbyte *v)': names
    'GLbyte', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glNormal3bv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glNormal3bv(const GLbyte *v)': names "
        "'GLbyte', which has no cute class yet.")

  @staticmethod
  def glNormal3dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glNormal3dv(const GLdouble *v)': names
    'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glNormal3dv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glNormal3dv(const GLdouble *v)': names "
        "'GLdouble', which has no cute class yet.")

  @staticmethod
  def glNormal3fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glNormal3fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glNormal3fv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glNormal3fv(const GLfloat *v)': names "
        "'GLfloat', which has no cute class yet.")

  @staticmethod
  def glNormal3iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glNormal3iv(const GLint *v)': names
    'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glNormal3iv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glNormal3iv(const GLint *v)': names "
        "'GLint', which has no cute class yet.")

  @staticmethod
  def glNormal3sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glNormal3sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glNormal3sv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glNormal3sv(const GLshort *v)': names "
        "'GLshort', which has no cute class yet.")

  @staticmethod
  def glNormalPointer(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glNormalPointer(GLenum type, GLsizei
    stride, const GLvoid *pointer)': names 'GLvoid', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glNormalPointer' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_1::glNormalPointer(GLenum type, "
        "GLsizei stride, const GLvoid *pointer)': names 'GLvoid', which has "
        "no cute class yet.")

  @staticmethod
  def glPixelMapfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glPixelMapfv(GLenum map, GLint mapsize,
    const GLfloat *values)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glPixelMapfv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glPixelMapfv(GLenum map, GLint "
        "mapsize, const GLfloat *values)': names 'GLfloat', which has no "
        "cute class yet.")

  @staticmethod
  def glPixelMapuiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glPixelMapuiv(GLenum map, GLint mapsize,
    const GLuint *values)': names 'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glPixelMapuiv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_1::glPixelMapuiv(GLenum map, GLint "
        "mapsize, const GLuint *values)': names 'GLuint', which has no cute "
        "class yet.")

  @staticmethod
  def glPixelMapusv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glPixelMapusv(GLenum map, GLint mapsize,
    const GLushort *values)': names 'GLushort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glPixelMapusv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_1::glPixelMapusv(GLenum map, GLint "
        "mapsize, const GLushort *values)': names 'GLushort', which has no "
        "cute class yet.")

  @staticmethod
  def glPolygonStipple(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glPolygonStipple(const GLubyte *mask)':
    names 'GLubyte', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glPolygonStipple' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_1::glPolygonStipple(const GLubyte "
        "*mask)': names 'GLubyte', which has no cute class yet.")

  @staticmethod
  def glPrioritizeTextures(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glPrioritizeTextures(GLsizei n, const
    GLuint *textures, const GLfloat *priorities)': names 'GLuint', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glPrioritizeTextures' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_1_1::glPrioritizeTextures(GLsizei "
        "n, const GLuint *textures, const GLfloat *priorities)': names "
        "'GLuint', which has no cute class yet.")

  @staticmethod
  def glRasterPos2dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glRasterPos2dv(const GLdouble *v)':
    names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glRasterPos2dv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_1::glRasterPos2dv(const GLdouble "
        "*v)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glRasterPos2fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glRasterPos2fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glRasterPos2fv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_1::glRasterPos2fv(const GLfloat "
        "*v)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glRasterPos2iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glRasterPos2iv(const GLint *v)': names
    'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glRasterPos2iv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_1::glRasterPos2iv(const GLint *v)': "
        "names 'GLint', which has no cute class yet.")

  @staticmethod
  def glRasterPos2sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glRasterPos2sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glRasterPos2sv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_1::glRasterPos2sv(const GLshort "
        "*v)': names 'GLshort', which has no cute class yet.")

  @staticmethod
  def glRasterPos3dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glRasterPos3dv(const GLdouble *v)':
    names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glRasterPos3dv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_1::glRasterPos3dv(const GLdouble "
        "*v)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glRasterPos3fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glRasterPos3fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glRasterPos3fv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_1::glRasterPos3fv(const GLfloat "
        "*v)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glRasterPos3iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glRasterPos3iv(const GLint *v)': names
    'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glRasterPos3iv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_1::glRasterPos3iv(const GLint *v)': "
        "names 'GLint', which has no cute class yet.")

  @staticmethod
  def glRasterPos3sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glRasterPos3sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glRasterPos3sv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_1::glRasterPos3sv(const GLshort "
        "*v)': names 'GLshort', which has no cute class yet.")

  @staticmethod
  def glRasterPos4dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glRasterPos4dv(const GLdouble *v)':
    names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glRasterPos4dv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_1::glRasterPos4dv(const GLdouble "
        "*v)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glRasterPos4fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glRasterPos4fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glRasterPos4fv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_1::glRasterPos4fv(const GLfloat "
        "*v)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glRasterPos4iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glRasterPos4iv(const GLint *v)': names
    'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glRasterPos4iv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_1::glRasterPos4iv(const GLint *v)': "
        "names 'GLint', which has no cute class yet.")

  @staticmethod
  def glRasterPos4sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glRasterPos4sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glRasterPos4sv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_1::glRasterPos4sv(const GLshort "
        "*v)': names 'GLshort', which has no cute class yet.")

  @staticmethod
  def glReadPixels(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glReadPixels(GLint x, GLint y, GLsizei
    width, GLsizei height, GLenum format, GLenum type, GLvoid *pixels)':
    names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glReadPixels' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glReadPixels(GLint x, GLint y, GLsizei "
        "width, GLsizei height, GLenum format, GLenum type, GLvoid "
        "*pixels)': names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glRectdv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glRectdv(const GLdouble *v1, const
    GLdouble *v2)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glRectdv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glRectdv(const GLdouble *v1, const "
        "GLdouble *v2)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glRectfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glRectfv(const GLfloat *v1, const
    GLfloat *v2)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glRectfv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glRectfv(const GLfloat *v1, const "
        "GLfloat *v2)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glRectiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glRectiv(const GLint *v1, const GLint
    *v2)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glRectiv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glRectiv(const GLint *v1, const GLint "
        "*v2)': names 'GLint', which has no cute class yet.")

  @staticmethod
  def glRectsv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glRectsv(const GLshort *v1, const
    GLshort *v2)': names 'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glRectsv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glRectsv(const GLshort *v1, const "
        "GLshort *v2)': names 'GLshort', which has no cute class yet.")

  @staticmethod
  def glSelectBuffer(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glSelectBuffer(GLsizei size, GLuint
    *buffer)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glSelectBuffer' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_1::glSelectBuffer(GLsizei size, "
        "GLuint *buffer)': takes a number to change where it is.")

  @staticmethod
  def glTexCoord1dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glTexCoord1dv(const GLdouble *v)': names
    'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glTexCoord1dv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_1::glTexCoord1dv(const GLdouble "
        "*v)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glTexCoord1fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glTexCoord1fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glTexCoord1fv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_1::glTexCoord1fv(const GLfloat *v)': "
        "names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glTexCoord1iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glTexCoord1iv(const GLint *v)': names
    'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glTexCoord1iv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_1::glTexCoord1iv(const GLint *v)': "
        "names 'GLint', which has no cute class yet.")

  @staticmethod
  def glTexCoord1sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glTexCoord1sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glTexCoord1sv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_1::glTexCoord1sv(const GLshort *v)': "
        "names 'GLshort', which has no cute class yet.")

  @staticmethod
  def glTexCoord2dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glTexCoord2dv(const GLdouble *v)': names
    'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glTexCoord2dv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_1::glTexCoord2dv(const GLdouble "
        "*v)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glTexCoord2fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glTexCoord2fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glTexCoord2fv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_1::glTexCoord2fv(const GLfloat *v)': "
        "names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glTexCoord2iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glTexCoord2iv(const GLint *v)': names
    'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glTexCoord2iv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_1::glTexCoord2iv(const GLint *v)': "
        "names 'GLint', which has no cute class yet.")

  @staticmethod
  def glTexCoord2sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glTexCoord2sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glTexCoord2sv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_1::glTexCoord2sv(const GLshort *v)': "
        "names 'GLshort', which has no cute class yet.")

  @staticmethod
  def glTexCoord3dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glTexCoord3dv(const GLdouble *v)': names
    'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glTexCoord3dv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_1::glTexCoord3dv(const GLdouble "
        "*v)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glTexCoord3fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glTexCoord3fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glTexCoord3fv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_1::glTexCoord3fv(const GLfloat *v)': "
        "names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glTexCoord3iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glTexCoord3iv(const GLint *v)': names
    'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glTexCoord3iv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_1::glTexCoord3iv(const GLint *v)': "
        "names 'GLint', which has no cute class yet.")

  @staticmethod
  def glTexCoord3sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glTexCoord3sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glTexCoord3sv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_1::glTexCoord3sv(const GLshort *v)': "
        "names 'GLshort', which has no cute class yet.")

  @staticmethod
  def glTexCoord4dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glTexCoord4dv(const GLdouble *v)': names
    'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glTexCoord4dv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_1::glTexCoord4dv(const GLdouble "
        "*v)': names 'GLdouble', which has no cute class yet.")

  @staticmethod
  def glTexCoord4fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glTexCoord4fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glTexCoord4fv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_1::glTexCoord4fv(const GLfloat *v)': "
        "names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glTexCoord4iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glTexCoord4iv(const GLint *v)': names
    'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glTexCoord4iv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_1::glTexCoord4iv(const GLint *v)': "
        "names 'GLint', which has no cute class yet.")

  @staticmethod
  def glTexCoord4sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glTexCoord4sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glTexCoord4sv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_1::glTexCoord4sv(const GLshort *v)': "
        "names 'GLshort', which has no cute class yet.")

  @staticmethod
  def glTexCoordPointer(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glTexCoordPointer(GLint size, GLenum
    type, GLsizei stride, const GLvoid *pointer)': names 'GLvoid', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glTexCoordPointer' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_1::glTexCoordPointer(GLint size, "
        "GLenum type, GLsizei stride, const GLvoid *pointer)': names "
        "'GLvoid', which has no cute class yet.")

  @staticmethod
  def glTexEnvfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glTexEnvfv(GLenum target, GLenum pname,
    const GLfloat *params)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glTexEnvfv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glTexEnvfv(GLenum target, GLenum "
        "pname, const GLfloat *params)': names 'GLfloat', which has no cute "
        "class yet.")

  @staticmethod
  def glTexEnviv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glTexEnviv(GLenum target, GLenum pname,
    const GLint *params)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glTexEnviv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glTexEnviv(GLenum target, GLenum "
        "pname, const GLint *params)': names 'GLint', which has no cute "
        "class yet.")

  @staticmethod
  def glTexGendv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glTexGendv(GLenum coord, GLenum pname,
    const GLdouble *params)': names 'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glTexGendv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glTexGendv(GLenum coord, GLenum pname, "
        "const GLdouble *params)': names 'GLdouble', which has no cute "
        "class yet.")

  @staticmethod
  def glTexGenfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glTexGenfv(GLenum coord, GLenum pname,
    const GLfloat *params)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glTexGenfv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glTexGenfv(GLenum coord, GLenum pname, "
        "const GLfloat *params)': names 'GLfloat', which has no cute class "
        "yet.")

  @staticmethod
  def glTexGeniv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glTexGeniv(GLenum coord, GLenum pname,
    const GLint *params)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glTexGeniv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glTexGeniv(GLenum coord, GLenum pname, "
        "const GLint *params)': names 'GLint', which has no cute class yet.")

  @staticmethod
  def glTexImage1D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glTexImage1D(GLenum target, GLint level,
    GLint internalformat, GLsizei width, GLint border, GLenum format, GLenum
    type, const GLvoid *pixels)': names 'GLvoid', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glTexImage1D' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glTexImage1D(GLenum target, GLint "
        "level, GLint internalformat, GLsizei width, GLint border, GLenum "
        "format, GLenum type, const GLvoid *pixels)': names 'GLvoid', which "
        "has no cute class yet.")

  @staticmethod
  def glTexImage2D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glTexImage2D(GLenum target, GLint level,
    GLint internalformat, GLsizei width, GLsizei height, GLint border, GLenum
    format, GLenum type, const GLvoid *pixels)': names 'GLvoid', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glTexImage2D' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glTexImage2D(GLenum target, GLint "
        "level, GLint internalformat, GLsizei width, GLsizei height, GLint "
        "border, GLenum format, GLenum type, const GLvoid *pixels)': names "
        "'GLvoid', which has no cute class yet.")

  @staticmethod
  def glTexParameterfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glTexParameterfv(GLenum target, GLenum
    pname, const GLfloat *params)': names 'GLfloat', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glTexParameterfv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_1::glTexParameterfv(GLenum target, "
        "GLenum pname, const GLfloat *params)': names 'GLfloat', which has "
        "no cute class yet.")

  @staticmethod
  def glTexParameteriv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glTexParameteriv(GLenum target, GLenum
    pname, const GLint *params)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glTexParameteriv' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_1::glTexParameteriv(GLenum target, "
        "GLenum pname, const GLint *params)': names 'GLint', which has no "
        "cute class yet.")

  @staticmethod
  def glTexSubImage1D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glTexSubImage1D(GLenum target, GLint
    level, GLint xoffset, GLsizei width, GLenum format, GLenum type, const
    GLvoid *pixels)': names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glTexSubImage1D' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_1::glTexSubImage1D(GLenum target, "
        "GLint level, GLint xoffset, GLsizei width, GLenum format, GLenum "
        "type, const GLvoid *pixels)': names 'GLvoid', which has no cute "
        "class yet.")

  @staticmethod
  def glTexSubImage2D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glTexSubImage2D(GLenum target, GLint
    level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height,
    GLenum format, GLenum type, const GLvoid *pixels)': names 'GLvoid', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glTexSubImage2D' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_1::glTexSubImage2D(GLenum target, "
        "GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei "
        "height, GLenum format, GLenum type, const GLvoid *pixels)': names "
        "'GLvoid', which has no cute class yet.")

  @staticmethod
  def glVertex2dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glVertex2dv(const GLdouble *v)': names
    'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glVertex2dv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glVertex2dv(const GLdouble *v)': names "
        "'GLdouble', which has no cute class yet.")

  @staticmethod
  def glVertex2fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glVertex2fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glVertex2fv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glVertex2fv(const GLfloat *v)': names "
        "'GLfloat', which has no cute class yet.")

  @staticmethod
  def glVertex2iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glVertex2iv(const GLint *v)': names
    'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glVertex2iv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glVertex2iv(const GLint *v)': names "
        "'GLint', which has no cute class yet.")

  @staticmethod
  def glVertex2sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glVertex2sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glVertex2sv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glVertex2sv(const GLshort *v)': names "
        "'GLshort', which has no cute class yet.")

  @staticmethod
  def glVertex3dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glVertex3dv(const GLdouble *v)': names
    'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glVertex3dv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glVertex3dv(const GLdouble *v)': names "
        "'GLdouble', which has no cute class yet.")

  @staticmethod
  def glVertex3fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glVertex3fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glVertex3fv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glVertex3fv(const GLfloat *v)': names "
        "'GLfloat', which has no cute class yet.")

  @staticmethod
  def glVertex3iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glVertex3iv(const GLint *v)': names
    'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glVertex3iv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glVertex3iv(const GLint *v)': names "
        "'GLint', which has no cute class yet.")

  @staticmethod
  def glVertex3sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glVertex3sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glVertex3sv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glVertex3sv(const GLshort *v)': names "
        "'GLshort', which has no cute class yet.")

  @staticmethod
  def glVertex4dv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glVertex4dv(const GLdouble *v)': names
    'GLdouble', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glVertex4dv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glVertex4dv(const GLdouble *v)': names "
        "'GLdouble', which has no cute class yet.")

  @staticmethod
  def glVertex4fv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glVertex4fv(const GLfloat *v)': names
    'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glVertex4fv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glVertex4fv(const GLfloat *v)': names "
        "'GLfloat', which has no cute class yet.")

  @staticmethod
  def glVertex4iv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glVertex4iv(const GLint *v)': names
    'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glVertex4iv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glVertex4iv(const GLint *v)': names "
        "'GLint', which has no cute class yet.")

  @staticmethod
  def glVertex4sv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glVertex4sv(const GLshort *v)': names
    'GLshort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glVertex4sv' has no cute function yet. Qt's "
        "'void QOpenGLFunctions_1_1::glVertex4sv(const GLshort *v)': names "
        "'GLshort', which has no cute class yet.")

  @staticmethod
  def glVertexPointer(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_1_1::glVertexPointer(GLint size, GLenum type,
    GLsizei stride, const GLvoid *pointer)': names 'GLvoid', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_1.glVertexPointer' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_1_1::glVertexPointer(GLint size, "
        "GLenum type, GLsizei stride, const GLvoid *pointer)': names "
        "'GLvoid', which has no cute class yet.")
