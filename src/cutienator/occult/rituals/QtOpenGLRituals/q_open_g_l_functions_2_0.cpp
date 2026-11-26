//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/qopenglfunctions_2_0.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtOpenGL/qtopenglglobal.h>
#if !QT_CONFIG(opengles2)
#if !defined(QT_NO_OPENGL) && !QT_CONFIG(opengles2)
#include <QtOpenGL/QtOpenGL>
#include <QtOpenGL/qopenglfunctions_2_0.h>
#include <QtOpenGL/qopenglversionprofile.h>
#include <cstring>

//  A QOpenGLFunctions_2_0 that Python can take functions over in. Every QOpenGLFunctions_2_0
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL) && !QT_CONFIG(opengles2)
typedef bool (*CuteQOpenGLFunctions_2_0Call0)(const void *, int *);
#endif  // !defined(QT_NO_OPENGL) && !QT_CONFIG(opengles2)
#endif  // !defined(QT_NO_OPENGL)
class CuteQOpenGLFunctions_2_0 : public QOpenGLFunctions_2_0 {
public:
  using QOpenGLFunctions_2_0::QOpenGLFunctions_2_0;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL) && !QT_CONFIG(opengles2)
    if (!std::strcmp(key, "_ZN24QAbstractOpenGLFunctions25initializeOpenGLFunctionsEv")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_OPENGL) && !QT_CONFIG(opengles2)
#endif  // !defined(QT_NO_OPENGL)
    return false;
  }

#if !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL) && !QT_CONFIG(opengles2)
  //  bool QOpenGLFunctions_2_0::initializeOpenGLFunctions()
  bool initializeOpenGLFunctions() override {
    if (taken[0]) {
      int handled = 0;
      CuteQOpenGLFunctions_2_0Call0 call = reinterpret_cast<CuteQOpenGLFunctions_2_0Call0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QOpenGLFunctions_2_0::initializeOpenGLFunctions();
  }
#endif  // !defined(QT_NO_OPENGL) && !QT_CONFIG(opengles2)
#endif  // !defined(QT_NO_OPENGL)
};

//  QOpenGLFunctions_2_0::QOpenGLFunctions_2_0()
extern "C" Q_DECL_EXPORT
QOpenGLFunctions_2_0 *ritual_ZN20QOpenGLFunctions_2_0C1Ev() {
  return new CuteQOpenGLFunctions_2_0();
}

//  QOpenGLFunctions_2_0::~QOpenGLFunctions_2_0()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_0D1Ev(QOpenGLFunctions_2_0 *self) {
  delete self;
}

//  bool QOpenGLFunctions_2_0::initializeOpenGLFunctions()
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QOpenGLFunctions_2_025initializeOpenGLFunctionsEv(
    QOpenGLFunctions_2_0 *self) {
  return self->initializeOpenGLFunctions();
}

//  void QOpenGLFunctions_2_0::glViewport(GLint x, GLint y, GLsizei width,
//      GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_010glViewportEiiii(
    QOpenGLFunctions_2_0 *self,
    GLint x,
    GLint y,
    GLsizei width,
    GLsizei height) {
  self->glViewport(x, y, width, height);
}

//  void QOpenGLFunctions_2_0::glDepthRange(GLdouble nearVal, GLdouble
//      farVal)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glDepthRangeEdd(
    QOpenGLFunctions_2_0 *self,
    GLdouble nearVal,
    GLdouble farVal) {
  self->glDepthRange(nearVal, farVal);
}

//  GLboolean QOpenGLFunctions_2_0::glIsEnabled(GLenum cap)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN20QOpenGLFunctions_2_011glIsEnabledEj(
    QOpenGLFunctions_2_0 *self,
    GLenum cap) {
  return self->glIsEnabled(cap);
}

//  void QOpenGLFunctions_2_0::glGetTexLevelParameteriv(GLenum target, GLint
//      level, GLenum pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_024glGetTexLevelParameterivEjijPi(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLint level,
    GLenum pname,
    GLint *params) {
  self->glGetTexLevelParameteriv(target, level, pname, params);
}

//  void QOpenGLFunctions_2_0::glGetTexLevelParameterfv(GLenum target, GLint
//      level, GLenum pname, GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_024glGetTexLevelParameterfvEjijPf(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLint level,
    GLenum pname,
    GLfloat *params) {
  self->glGetTexLevelParameterfv(target, level, pname, params);
}

//  void QOpenGLFunctions_2_0::glGetTexParameteriv(GLenum target, GLenum
//      pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_019glGetTexParameterivEjjPi(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLenum pname,
    GLint *params) {
  self->glGetTexParameteriv(target, pname, params);
}

//  void QOpenGLFunctions_2_0::glGetTexParameterfv(GLenum target, GLenum
//      pname, GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_019glGetTexParameterfvEjjPf(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLenum pname,
    GLfloat *params) {
  self->glGetTexParameterfv(target, pname, params);
}

//  void QOpenGLFunctions_2_0::glGetTexImage(GLenum target, GLint level,
//      GLenum format, GLenum type, GLvoid *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glGetTexImageEjijjPv(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLint level,
    GLenum format,
    GLenum type,
    GLvoid *pixels) {
  self->glGetTexImage(target, level, format, type, pixels);
}

//  const GLubyte *QOpenGLFunctions_2_0::glGetString(GLenum name)
extern "C" Q_DECL_EXPORT
const GLubyte *ritual_ZN20QOpenGLFunctions_2_011glGetStringEj(
    QOpenGLFunctions_2_0 *self,
    GLenum name) {
  return self->glGetString(name);
}

//  void QOpenGLFunctions_2_0::glGetIntegerv(GLenum pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glGetIntegervEjPi(
    QOpenGLFunctions_2_0 *self,
    GLenum pname,
    GLint *params) {
  self->glGetIntegerv(pname, params);
}

//  void QOpenGLFunctions_2_0::glGetFloatv(GLenum pname, GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_011glGetFloatvEjPf(
    QOpenGLFunctions_2_0 *self,
    GLenum pname,
    GLfloat *params) {
  self->glGetFloatv(pname, params);
}

//  GLenum QOpenGLFunctions_2_0::glGetError()
extern "C" Q_DECL_EXPORT
GLenum ritual_ZN20QOpenGLFunctions_2_010glGetErrorEv(
    QOpenGLFunctions_2_0 *self) {
  return self->glGetError();
}

//  void QOpenGLFunctions_2_0::glGetDoublev(GLenum pname, GLdouble *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glGetDoublevEjPd(
    QOpenGLFunctions_2_0 *self,
    GLenum pname,
    GLdouble *params) {
  self->glGetDoublev(pname, params);
}

//  void QOpenGLFunctions_2_0::glGetBooleanv(GLenum pname, GLboolean *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glGetBooleanvEjPh(
    QOpenGLFunctions_2_0 *self,
    GLenum pname,
    GLboolean *params) {
  self->glGetBooleanv(pname, params);
}

//  void QOpenGLFunctions_2_0::glReadPixels(GLint x, GLint y, GLsizei width,
//      GLsizei height, GLenum format, GLenum type, GLvoid *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glReadPixelsEiiiijjPv(
    QOpenGLFunctions_2_0 *self,
    GLint x,
    GLint y,
    GLsizei width,
    GLsizei height,
    GLenum format,
    GLenum type,
    GLvoid *pixels) {
  self->glReadPixels(x, y, width, height, format, type, pixels);
}

//  void QOpenGLFunctions_2_0::glReadBuffer(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glReadBufferEj(
    QOpenGLFunctions_2_0 *self,
    GLenum mode) {
  self->glReadBuffer(mode);
}

//  void QOpenGLFunctions_2_0::glPixelStorei(GLenum pname, GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glPixelStoreiEji(
    QOpenGLFunctions_2_0 *self,
    GLenum pname,
    GLint param) {
  self->glPixelStorei(pname, param);
}

//  void QOpenGLFunctions_2_0::glPixelStoref(GLenum pname, GLfloat param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glPixelStorefEjf(
    QOpenGLFunctions_2_0 *self,
    GLenum pname,
    GLfloat param) {
  self->glPixelStoref(pname, param);
}

//  void QOpenGLFunctions_2_0::glDepthFunc(GLenum func)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_011glDepthFuncEj(
    QOpenGLFunctions_2_0 *self,
    GLenum func) {
  self->glDepthFunc(func);
}

//  void QOpenGLFunctions_2_0::glStencilOp(GLenum fail, GLenum zfail, GLenum
//      zpass)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_011glStencilOpEjjj(
    QOpenGLFunctions_2_0 *self,
    GLenum fail,
    GLenum zfail,
    GLenum zpass) {
  self->glStencilOp(fail, zfail, zpass);
}

//  void QOpenGLFunctions_2_0::glStencilFunc(GLenum func, GLint ref, GLuint
//      mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glStencilFuncEjij(
    QOpenGLFunctions_2_0 *self,
    GLenum func,
    GLint ref,
    GLuint mask) {
  self->glStencilFunc(func, ref, mask);
}

//  void QOpenGLFunctions_2_0::glLogicOp(GLenum opcode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_09glLogicOpEj(
    QOpenGLFunctions_2_0 *self,
    GLenum opcode) {
  self->glLogicOp(opcode);
}

//  void QOpenGLFunctions_2_0::glBlendFunc(GLenum sfactor, GLenum dfactor)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_011glBlendFuncEjj(
    QOpenGLFunctions_2_0 *self,
    GLenum sfactor,
    GLenum dfactor) {
  self->glBlendFunc(sfactor, dfactor);
}

//  void QOpenGLFunctions_2_0::glFlush()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_07glFlushEv(QOpenGLFunctions_2_0 *self) {
  self->glFlush();
}

//  void QOpenGLFunctions_2_0::glFinish()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_08glFinishEv(QOpenGLFunctions_2_0 *self) {
  self->glFinish();
}

//  void QOpenGLFunctions_2_0::glEnable(GLenum cap)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_08glEnableEj(
    QOpenGLFunctions_2_0 *self,
    GLenum cap) {
  self->glEnable(cap);
}

//  void QOpenGLFunctions_2_0::glDisable(GLenum cap)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_09glDisableEj(
    QOpenGLFunctions_2_0 *self,
    GLenum cap) {
  self->glDisable(cap);
}

//  void QOpenGLFunctions_2_0::glDepthMask(GLboolean flag)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_011glDepthMaskEh(
    QOpenGLFunctions_2_0 *self,
    GLboolean flag) {
  self->glDepthMask(flag);
}

//  void QOpenGLFunctions_2_0::glColorMask(GLboolean red, GLboolean green,
//      GLboolean blue, GLboolean alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_011glColorMaskEhhhh(
    QOpenGLFunctions_2_0 *self,
    GLboolean red,
    GLboolean green,
    GLboolean blue,
    GLboolean alpha) {
  self->glColorMask(red, green, blue, alpha);
}

//  void QOpenGLFunctions_2_0::glStencilMask(GLuint mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glStencilMaskEj(
    QOpenGLFunctions_2_0 *self,
    GLuint mask) {
  self->glStencilMask(mask);
}

//  void QOpenGLFunctions_2_0::glClearDepth(GLdouble depth)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glClearDepthEd(
    QOpenGLFunctions_2_0 *self,
    GLdouble depth) {
  self->glClearDepth(depth);
}

//  void QOpenGLFunctions_2_0::glClearStencil(GLint s)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_014glClearStencilEi(
    QOpenGLFunctions_2_0 *self,
    GLint s) {
  self->glClearStencil(s);
}

//  void QOpenGLFunctions_2_0::glClearColor(GLfloat red, GLfloat green,
//      GLfloat blue, GLfloat alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glClearColorEffff(
    QOpenGLFunctions_2_0 *self,
    GLfloat red,
    GLfloat green,
    GLfloat blue,
    GLfloat alpha) {
  self->glClearColor(red, green, blue, alpha);
}

//  void QOpenGLFunctions_2_0::glClear(GLbitfield mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_07glClearEj(
    QOpenGLFunctions_2_0 *self,
    GLbitfield mask) {
  self->glClear(mask);
}

//  void QOpenGLFunctions_2_0::glDrawBuffer(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glDrawBufferEj(
    QOpenGLFunctions_2_0 *self,
    GLenum mode) {
  self->glDrawBuffer(mode);
}

//  void QOpenGLFunctions_2_0::glTexImage2D(GLenum target, GLint level, GLint
//      internalformat, GLsizei width, GLsizei height, GLint border, GLenum
//      format, GLenum type, const GLvoid *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glTexImage2DEjiiiiijjPKv(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLint level,
    GLint internalformat,
    GLsizei width,
    GLsizei height,
    GLint border,
    GLenum format,
    GLenum type,
    const GLvoid *pixels) {
  self->glTexImage2D(
      target,
      level,
      internalformat,
      width,
      height,
      border,
      format,
      type,
      pixels);
}

//  void QOpenGLFunctions_2_0::glTexImage1D(GLenum target, GLint level, GLint
//      internalformat, GLsizei width, GLint border, GLenum format, GLenum
//      type, const GLvoid *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glTexImage1DEjiiiijjPKv(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLint level,
    GLint internalformat,
    GLsizei width,
    GLint border,
    GLenum format,
    GLenum type,
    const GLvoid *pixels) {
  self->glTexImage1D(
      target,
      level,
      internalformat,
      width,
      border,
      format,
      type,
      pixels);
}

//  void QOpenGLFunctions_2_0::glTexParameteriv(GLenum target, GLenum pname,
//      const GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_016glTexParameterivEjjPKi(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLenum pname,
    const GLint *params) {
  self->glTexParameteriv(target, pname, params);
}

//  void QOpenGLFunctions_2_0::glTexParameteri(GLenum target, GLenum pname,
//      GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_015glTexParameteriEjji(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLenum pname,
    GLint param) {
  self->glTexParameteri(target, pname, param);
}

//  void QOpenGLFunctions_2_0::glTexParameterfv(GLenum target, GLenum pname,
//      const GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_016glTexParameterfvEjjPKf(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLenum pname,
    const GLfloat *params) {
  self->glTexParameterfv(target, pname, params);
}

//  void QOpenGLFunctions_2_0::glTexParameterf(GLenum target, GLenum pname,
//      GLfloat param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_015glTexParameterfEjjf(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLenum pname,
    GLfloat param) {
  self->glTexParameterf(target, pname, param);
}

//  void QOpenGLFunctions_2_0::glScissor(GLint x, GLint y, GLsizei width,
//      GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_09glScissorEiiii(
    QOpenGLFunctions_2_0 *self,
    GLint x,
    GLint y,
    GLsizei width,
    GLsizei height) {
  self->glScissor(x, y, width, height);
}

//  void QOpenGLFunctions_2_0::glPolygonMode(GLenum face, GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glPolygonModeEjj(
    QOpenGLFunctions_2_0 *self,
    GLenum face,
    GLenum mode) {
  self->glPolygonMode(face, mode);
}

//  void QOpenGLFunctions_2_0::glPointSize(GLfloat size)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_011glPointSizeEf(
    QOpenGLFunctions_2_0 *self,
    GLfloat size) {
  self->glPointSize(size);
}

//  void QOpenGLFunctions_2_0::glLineWidth(GLfloat width)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_011glLineWidthEf(
    QOpenGLFunctions_2_0 *self,
    GLfloat width) {
  self->glLineWidth(width);
}

//  void QOpenGLFunctions_2_0::glHint(GLenum target, GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_06glHintEjj(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLenum mode) {
  self->glHint(target, mode);
}

//  void QOpenGLFunctions_2_0::glFrontFace(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_011glFrontFaceEj(
    QOpenGLFunctions_2_0 *self,
    GLenum mode) {
  self->glFrontFace(mode);
}

//  void QOpenGLFunctions_2_0::glCullFace(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_010glCullFaceEj(
    QOpenGLFunctions_2_0 *self,
    GLenum mode) {
  self->glCullFace(mode);
}

//  void QOpenGLFunctions_2_0::glIndexubv(const GLubyte *c)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_010glIndexubvEPKh(
    QOpenGLFunctions_2_0 *self,
    const GLubyte *c) {
  self->glIndexubv(c);
}

//  void QOpenGLFunctions_2_0::glIndexub(GLubyte c)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_09glIndexubEh(
    QOpenGLFunctions_2_0 *self,
    GLubyte c) {
  self->glIndexub(c);
}

//  GLboolean QOpenGLFunctions_2_0::glIsTexture(GLuint texture)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN20QOpenGLFunctions_2_011glIsTextureEj(
    QOpenGLFunctions_2_0 *self,
    GLuint texture) {
  return self->glIsTexture(texture);
}

//  void QOpenGLFunctions_2_0::glGenTextures(GLsizei n, GLuint *textures)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glGenTexturesEiPj(
    QOpenGLFunctions_2_0 *self,
    GLsizei n,
    GLuint *textures) {
  self->glGenTextures(n, textures);
}

//  void QOpenGLFunctions_2_0::glDeleteTextures(GLsizei n, const GLuint
//      *textures)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_016glDeleteTexturesEiPKj(
    QOpenGLFunctions_2_0 *self,
    GLsizei n,
    const GLuint *textures) {
  self->glDeleteTextures(n, textures);
}

//  void QOpenGLFunctions_2_0::glBindTexture(GLenum target, GLuint texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glBindTextureEjj(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLuint texture) {
  self->glBindTexture(target, texture);
}

//  void QOpenGLFunctions_2_0::glTexSubImage2D(GLenum target, GLint level,
//      GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum
//      format, GLenum type, const GLvoid *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_015glTexSubImage2DEjiiiiijjPKv(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLint level,
    GLint xoffset,
    GLint yoffset,
    GLsizei width,
    GLsizei height,
    GLenum format,
    GLenum type,
    const GLvoid *pixels) {
  self->glTexSubImage2D(
      target,
      level,
      xoffset,
      yoffset,
      width,
      height,
      format,
      type,
      pixels);
}

//  void QOpenGLFunctions_2_0::glTexSubImage1D(GLenum target, GLint level,
//      GLint xoffset, GLsizei width, GLenum format, GLenum type, const
//      GLvoid *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_015glTexSubImage1DEjiiijjPKv(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLint level,
    GLint xoffset,
    GLsizei width,
    GLenum format,
    GLenum type,
    const GLvoid *pixels) {
  self->glTexSubImage1D(target, level, xoffset, width, format, type, pixels);
}

//  void QOpenGLFunctions_2_0::glCopyTexSubImage2D(GLenum target, GLint
//      level, GLint xoffset, GLint yoffset, GLint x, GLint y, GLsizei width,
//      GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_019glCopyTexSubImage2DEjiiiiiii(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLint level,
    GLint xoffset,
    GLint yoffset,
    GLint x,
    GLint y,
    GLsizei width,
    GLsizei height) {
  self->glCopyTexSubImage2D(
      target,
      level,
      xoffset,
      yoffset,
      x,
      y,
      width,
      height);
}

//  void QOpenGLFunctions_2_0::glCopyTexSubImage1D(GLenum target, GLint
//      level, GLint xoffset, GLint x, GLint y, GLsizei width)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_019glCopyTexSubImage1DEjiiiii(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLint level,
    GLint xoffset,
    GLint x,
    GLint y,
    GLsizei width) {
  self->glCopyTexSubImage1D(target, level, xoffset, x, y, width);
}

//  void QOpenGLFunctions_2_0::glCopyTexImage2D(GLenum target, GLint level,
//      GLenum internalformat, GLint x, GLint y, GLsizei width, GLsizei
//      height, GLint border)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_016glCopyTexImage2DEjijiiiii(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLint level,
    GLenum internalformat,
    GLint x,
    GLint y,
    GLsizei width,
    GLsizei height,
    GLint border) {
  self->glCopyTexImage2D(
      target,
      level,
      internalformat,
      x,
      y,
      width,
      height,
      border);
}

//  void QOpenGLFunctions_2_0::glCopyTexImage1D(GLenum target, GLint level,
//      GLenum internalformat, GLint x, GLint y, GLsizei width, GLint border)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_016glCopyTexImage1DEjijiiii(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLint level,
    GLenum internalformat,
    GLint x,
    GLint y,
    GLsizei width,
    GLint border) {
  self->glCopyTexImage1D(target, level, internalformat, x, y, width, border);
}

//  void QOpenGLFunctions_2_0::glPolygonOffset(GLfloat factor, GLfloat units)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_015glPolygonOffsetEff(
    QOpenGLFunctions_2_0 *self,
    GLfloat factor,
    GLfloat units) {
  self->glPolygonOffset(factor, units);
}

//  void QOpenGLFunctions_2_0::glGetPointerv(GLenum pname, GLvoid **params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glGetPointervEjPPv(
    QOpenGLFunctions_2_0 *self,
    GLenum pname,
    GLvoid **params) {
  self->glGetPointerv(pname, params);
}

//  void QOpenGLFunctions_2_0::glDrawElements(GLenum mode, GLsizei count,
//      GLenum type, const GLvoid *indices)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_014glDrawElementsEjijPKv(
    QOpenGLFunctions_2_0 *self,
    GLenum mode,
    GLsizei count,
    GLenum type,
    const GLvoid *indices) {
  self->glDrawElements(mode, count, type, indices);
}

//  void QOpenGLFunctions_2_0::glDrawArrays(GLenum mode, GLint first, GLsizei
//      count)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glDrawArraysEjii(
    QOpenGLFunctions_2_0 *self,
    GLenum mode,
    GLint first,
    GLsizei count) {
  self->glDrawArrays(mode, first, count);
}

//  void QOpenGLFunctions_2_0::glCopyTexSubImage3D(GLenum target, GLint
//      level, GLint xoffset, GLint yoffset, GLint zoffset, GLint x, GLint y,
//      GLsizei width, GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_019glCopyTexSubImage3DEjiiiiiiii(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLint level,
    GLint xoffset,
    GLint yoffset,
    GLint zoffset,
    GLint x,
    GLint y,
    GLsizei width,
    GLsizei height) {
  self->glCopyTexSubImage3D(
      target,
      level,
      xoffset,
      yoffset,
      zoffset,
      x,
      y,
      width,
      height);
}

//  void QOpenGLFunctions_2_0::glTexSubImage3D(GLenum target, GLint level,
//      GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei
//      height, GLsizei depth, GLenum format, GLenum type, const GLvoid
//      *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_015glTexSubImage3DEjiiiiiiijjPKv(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLint level,
    GLint xoffset,
    GLint yoffset,
    GLint zoffset,
    GLsizei width,
    GLsizei height,
    GLsizei depth,
    GLenum format,
    GLenum type,
    const GLvoid *pixels) {
  self->glTexSubImage3D(
      target,
      level,
      xoffset,
      yoffset,
      zoffset,
      width,
      height,
      depth,
      format,
      type,
      pixels);
}

//  void QOpenGLFunctions_2_0::glTexImage3D(GLenum target, GLint level, GLint
//      internalformat, GLsizei width, GLsizei height, GLsizei depth, GLint
//      border, GLenum format, GLenum type, const GLvoid *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glTexImage3DEjiiiiiijjPKv(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLint level,
    GLint internalformat,
    GLsizei width,
    GLsizei height,
    GLsizei depth,
    GLint border,
    GLenum format,
    GLenum type,
    const GLvoid *pixels) {
  self->glTexImage3D(
      target,
      level,
      internalformat,
      width,
      height,
      depth,
      border,
      format,
      type,
      pixels);
}

//  void QOpenGLFunctions_2_0::glDrawRangeElements(GLenum mode, GLuint start,
//      GLuint end, GLsizei count, GLenum type, const GLvoid *indices)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_019glDrawRangeElementsEjjjijPKv(
    QOpenGLFunctions_2_0 *self,
    GLenum mode,
    GLuint start,
    GLuint end,
    GLsizei count,
    GLenum type,
    const GLvoid *indices) {
  self->glDrawRangeElements(mode, start, end, count, type, indices);
}

//  void QOpenGLFunctions_2_0::glBlendEquation(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_015glBlendEquationEj(
    QOpenGLFunctions_2_0 *self,
    GLenum mode) {
  self->glBlendEquation(mode);
}

//  void QOpenGLFunctions_2_0::glBlendColor(GLfloat red, GLfloat green,
//      GLfloat blue, GLfloat alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glBlendColorEffff(
    QOpenGLFunctions_2_0 *self,
    GLfloat red,
    GLfloat green,
    GLfloat blue,
    GLfloat alpha) {
  self->glBlendColor(red, green, blue, alpha);
}

//  void QOpenGLFunctions_2_0::glGetCompressedTexImage(GLenum target, GLint
//      level, GLvoid *img)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_023glGetCompressedTexImageEjiPv(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLint level,
    GLvoid *img) {
  self->glGetCompressedTexImage(target, level, img);
}

//  void QOpenGLFunctions_2_0::glCompressedTexSubImage1D(GLenum target, GLint
//      level, GLint xoffset, GLsizei width, GLenum format, GLsizei
//      imageSize, const GLvoid *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_025glCompressedTexSubImage1DEjiiijiPKv(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLint level,
    GLint xoffset,
    GLsizei width,
    GLenum format,
    GLsizei imageSize,
    const GLvoid *data) {
  self->glCompressedTexSubImage1D(
      target,
      level,
      xoffset,
      width,
      format,
      imageSize,
      data);
}

//  void QOpenGLFunctions_2_0::glCompressedTexSubImage2D(GLenum target, GLint
//      level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height,
//      GLenum format, GLsizei imageSize, const GLvoid *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_025glCompressedTexSubImage2DEjiiiiijiPKv(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLint level,
    GLint xoffset,
    GLint yoffset,
    GLsizei width,
    GLsizei height,
    GLenum format,
    GLsizei imageSize,
    const GLvoid *data) {
  self->glCompressedTexSubImage2D(
      target,
      level,
      xoffset,
      yoffset,
      width,
      height,
      format,
      imageSize,
      data);
}

//  void QOpenGLFunctions_2_0::glCompressedTexSubImage3D(GLenum target, GLint
//      level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width,
//      GLsizei height, GLsizei depth, GLenum format, GLsizei imageSize,
//      const GLvoid *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_025glCompressedTexSubImage3DEjiiiiiiijiPKv(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLint level,
    GLint xoffset,
    GLint yoffset,
    GLint zoffset,
    GLsizei width,
    GLsizei height,
    GLsizei depth,
    GLenum format,
    GLsizei imageSize,
    const GLvoid *data) {
  self->glCompressedTexSubImage3D(
      target,
      level,
      xoffset,
      yoffset,
      zoffset,
      width,
      height,
      depth,
      format,
      imageSize,
      data);
}

//  void QOpenGLFunctions_2_0::glCompressedTexImage1D(GLenum target, GLint
//      level, GLenum internalformat, GLsizei width, GLint border, GLsizei
//      imageSize, const GLvoid *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_022glCompressedTexImage1DEjijiiiPKv(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLint level,
    GLenum internalformat,
    GLsizei width,
    GLint border,
    GLsizei imageSize,
    const GLvoid *data) {
  self->glCompressedTexImage1D(
      target,
      level,
      internalformat,
      width,
      border,
      imageSize,
      data);
}

//  void QOpenGLFunctions_2_0::glCompressedTexImage2D(GLenum target, GLint
//      level, GLenum internalformat, GLsizei width, GLsizei height, GLint
//      border, GLsizei imageSize, const GLvoid *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_022glCompressedTexImage2DEjijiiiiPKv(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLint level,
    GLenum internalformat,
    GLsizei width,
    GLsizei height,
    GLint border,
    GLsizei imageSize,
    const GLvoid *data) {
  self->glCompressedTexImage2D(
      target,
      level,
      internalformat,
      width,
      height,
      border,
      imageSize,
      data);
}

//  void QOpenGLFunctions_2_0::glCompressedTexImage3D(GLenum target, GLint
//      level, GLenum internalformat, GLsizei width, GLsizei height, GLsizei
//      depth, GLint border, GLsizei imageSize, const GLvoid *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_022glCompressedTexImage3DEjijiiiiiPKv(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLint level,
    GLenum internalformat,
    GLsizei width,
    GLsizei height,
    GLsizei depth,
    GLint border,
    GLsizei imageSize,
    const GLvoid *data) {
  self->glCompressedTexImage3D(
      target,
      level,
      internalformat,
      width,
      height,
      depth,
      border,
      imageSize,
      data);
}

//  void QOpenGLFunctions_2_0::glSampleCoverage(GLfloat value, GLboolean
//      invert)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_016glSampleCoverageEfh(
    QOpenGLFunctions_2_0 *self,
    GLfloat value,
    GLboolean invert) {
  self->glSampleCoverage(value, invert);
}

//  void QOpenGLFunctions_2_0::glActiveTexture(GLenum texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_015glActiveTextureEj(
    QOpenGLFunctions_2_0 *self,
    GLenum texture) {
  self->glActiveTexture(texture);
}

//  void QOpenGLFunctions_2_0::glPointParameteriv(GLenum pname, const GLint
//      *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_018glPointParameterivEjPKi(
    QOpenGLFunctions_2_0 *self,
    GLenum pname,
    const GLint *params) {
  self->glPointParameteriv(pname, params);
}

//  void QOpenGLFunctions_2_0::glPointParameteri(GLenum pname, GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_017glPointParameteriEji(
    QOpenGLFunctions_2_0 *self,
    GLenum pname,
    GLint param) {
  self->glPointParameteri(pname, param);
}

//  void QOpenGLFunctions_2_0::glPointParameterfv(GLenum pname, const GLfloat
//      *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_018glPointParameterfvEjPKf(
    QOpenGLFunctions_2_0 *self,
    GLenum pname,
    const GLfloat *params) {
  self->glPointParameterfv(pname, params);
}

//  void QOpenGLFunctions_2_0::glPointParameterf(GLenum pname, GLfloat param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_017glPointParameterfEjf(
    QOpenGLFunctions_2_0 *self,
    GLenum pname,
    GLfloat param) {
  self->glPointParameterf(pname, param);
}

//  void QOpenGLFunctions_2_0::glMultiDrawElements(GLenum mode, const GLsizei
//      *count, GLenum type, const GLvoid *const *indices, GLsizei drawcount)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_019glMultiDrawElementsEjPKijPKPKvi(
    QOpenGLFunctions_2_0 *self,
    GLenum mode,
    const GLsizei *count,
    GLenum type,
    const GLvoid *const *indices,
    GLsizei drawcount) {
  self->glMultiDrawElements(mode, count, type, indices, drawcount);
}

//  void QOpenGLFunctions_2_0::glMultiDrawArrays(GLenum mode, const GLint
//      *first, const GLsizei *count, GLsizei drawcount)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_017glMultiDrawArraysEjPKiS1_i(
    QOpenGLFunctions_2_0 *self,
    GLenum mode,
    const GLint *first,
    const GLsizei *count,
    GLsizei drawcount) {
  self->glMultiDrawArrays(mode, first, count, drawcount);
}

//  void QOpenGLFunctions_2_0::glBlendFuncSeparate(GLenum sfactorRGB, GLenum
//      dfactorRGB, GLenum sfactorAlpha, GLenum dfactorAlpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_019glBlendFuncSeparateEjjjj(
    QOpenGLFunctions_2_0 *self,
    GLenum sfactorRGB,
    GLenum dfactorRGB,
    GLenum sfactorAlpha,
    GLenum dfactorAlpha) {
  self->glBlendFuncSeparate(
      sfactorRGB,
      dfactorRGB,
      sfactorAlpha,
      dfactorAlpha);
}

//  void QOpenGLFunctions_2_0::glGetBufferPointerv(GLenum target, GLenum
//      pname, GLvoid **params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_019glGetBufferPointervEjjPPv(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLenum pname,
    GLvoid **params) {
  self->glGetBufferPointerv(target, pname, params);
}

//  void QOpenGLFunctions_2_0::glGetBufferParameteriv(GLenum target, GLenum
//      pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_022glGetBufferParameterivEjjPi(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLenum pname,
    GLint *params) {
  self->glGetBufferParameteriv(target, pname, params);
}

//  GLboolean QOpenGLFunctions_2_0::glUnmapBuffer(GLenum target)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN20QOpenGLFunctions_2_013glUnmapBufferEj(
    QOpenGLFunctions_2_0 *self,
    GLenum target) {
  return self->glUnmapBuffer(target);
}

//  GLvoid *QOpenGLFunctions_2_0::glMapBuffer(GLenum target, GLenum access)
extern "C" Q_DECL_EXPORT
GLvoid *ritual_ZN20QOpenGLFunctions_2_011glMapBufferEjj(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLenum access) {
  return self->glMapBuffer(target, access);
}

//  void QOpenGLFunctions_2_0::glGetBufferSubData(GLenum target, GLintptr
//      offset, GLsizeiptr size, GLvoid *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_018glGetBufferSubDataEjllPv(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    long long offset,
    long long size,
    GLvoid *data) {
  self->glGetBufferSubData(target, offset, size, data);
}

//  void QOpenGLFunctions_2_0::glBufferSubData(GLenum target, GLintptr
//      offset, GLsizeiptr size, const GLvoid *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_015glBufferSubDataEjllPKv(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    long long offset,
    long long size,
    const GLvoid *data) {
  self->glBufferSubData(target, offset, size, data);
}

//  void QOpenGLFunctions_2_0::glBufferData(GLenum target, GLsizeiptr size,
//      const GLvoid *data, GLenum usage)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glBufferDataEjlPKvj(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    long long size,
    const GLvoid *data,
    GLenum usage) {
  self->glBufferData(target, size, data, usage);
}

//  GLboolean QOpenGLFunctions_2_0::glIsBuffer(GLuint buffer)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN20QOpenGLFunctions_2_010glIsBufferEj(
    QOpenGLFunctions_2_0 *self,
    GLuint buffer) {
  return self->glIsBuffer(buffer);
}

//  void QOpenGLFunctions_2_0::glGenBuffers(GLsizei n, GLuint *buffers)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glGenBuffersEiPj(
    QOpenGLFunctions_2_0 *self,
    GLsizei n,
    GLuint *buffers) {
  self->glGenBuffers(n, buffers);
}

//  void QOpenGLFunctions_2_0::glDeleteBuffers(GLsizei n, const GLuint
//      *buffers)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_015glDeleteBuffersEiPKj(
    QOpenGLFunctions_2_0 *self,
    GLsizei n,
    const GLuint *buffers) {
  self->glDeleteBuffers(n, buffers);
}

//  void QOpenGLFunctions_2_0::glBindBuffer(GLenum target, GLuint buffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glBindBufferEjj(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLuint buffer) {
  self->glBindBuffer(target, buffer);
}

//  void QOpenGLFunctions_2_0::glGetQueryObjectuiv(GLuint id, GLenum pname,
//      GLuint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_019glGetQueryObjectuivEjjPj(
    QOpenGLFunctions_2_0 *self,
    GLuint id,
    GLenum pname,
    GLuint *params) {
  self->glGetQueryObjectuiv(id, pname, params);
}

//  void QOpenGLFunctions_2_0::glGetQueryObjectiv(GLuint id, GLenum pname,
//      GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_018glGetQueryObjectivEjjPi(
    QOpenGLFunctions_2_0 *self,
    GLuint id,
    GLenum pname,
    GLint *params) {
  self->glGetQueryObjectiv(id, pname, params);
}

//  void QOpenGLFunctions_2_0::glGetQueryiv(GLenum target, GLenum pname,
//      GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glGetQueryivEjjPi(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLenum pname,
    GLint *params) {
  self->glGetQueryiv(target, pname, params);
}

//  void QOpenGLFunctions_2_0::glEndQuery(GLenum target)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_010glEndQueryEj(
    QOpenGLFunctions_2_0 *self,
    GLenum target) {
  self->glEndQuery(target);
}

//  void QOpenGLFunctions_2_0::glBeginQuery(GLenum target, GLuint id)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glBeginQueryEjj(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLuint id) {
  self->glBeginQuery(target, id);
}

//  GLboolean QOpenGLFunctions_2_0::glIsQuery(GLuint id)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN20QOpenGLFunctions_2_09glIsQueryEj(
    QOpenGLFunctions_2_0 *self,
    GLuint id) {
  return self->glIsQuery(id);
}

//  void QOpenGLFunctions_2_0::glDeleteQueries(GLsizei n, const GLuint *ids)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_015glDeleteQueriesEiPKj(
    QOpenGLFunctions_2_0 *self,
    GLsizei n,
    const GLuint *ids) {
  self->glDeleteQueries(n, ids);
}

//  void QOpenGLFunctions_2_0::glGenQueries(GLsizei n, GLuint *ids)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glGenQueriesEiPj(
    QOpenGLFunctions_2_0 *self,
    GLsizei n,
    GLuint *ids) {
  self->glGenQueries(n, ids);
}

//  void QOpenGLFunctions_2_0::glVertexAttribPointer(GLuint index, GLint
//      size, GLenum type, GLboolean normalized, GLsizei stride, const GLvoid
//      *pointer)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_021glVertexAttribPointerEjijhiPKv(
    QOpenGLFunctions_2_0 *self,
    GLuint index,
    GLint size,
    GLenum type,
    GLboolean normalized,
    GLsizei stride,
    const GLvoid *pointer) {
  self->glVertexAttribPointer(
      index,
      size,
      type,
      normalized,
      stride,
      pointer);
}

//  void QOpenGLFunctions_2_0::glValidateProgram(GLuint program)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_017glValidateProgramEj(
    QOpenGLFunctions_2_0 *self,
    GLuint program) {
  self->glValidateProgram(program);
}

//  void QOpenGLFunctions_2_0::glUniformMatrix4fv(GLint location, GLsizei
//      count, GLboolean transpose, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_018glUniformMatrix4fvEiihPKf(
    QOpenGLFunctions_2_0 *self,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLfloat *value) {
  self->glUniformMatrix4fv(location, count, transpose, value);
}

//  void QOpenGLFunctions_2_0::glUniformMatrix3fv(GLint location, GLsizei
//      count, GLboolean transpose, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_018glUniformMatrix3fvEiihPKf(
    QOpenGLFunctions_2_0 *self,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLfloat *value) {
  self->glUniformMatrix3fv(location, count, transpose, value);
}

//  void QOpenGLFunctions_2_0::glUniformMatrix2fv(GLint location, GLsizei
//      count, GLboolean transpose, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_018glUniformMatrix2fvEiihPKf(
    QOpenGLFunctions_2_0 *self,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLfloat *value) {
  self->glUniformMatrix2fv(location, count, transpose, value);
}

//  void QOpenGLFunctions_2_0::glUniform4iv(GLint location, GLsizei count,
//      const GLint *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glUniform4ivEiiPKi(
    QOpenGLFunctions_2_0 *self,
    GLint location,
    GLsizei count,
    const GLint *value) {
  self->glUniform4iv(location, count, value);
}

//  void QOpenGLFunctions_2_0::glUniform3iv(GLint location, GLsizei count,
//      const GLint *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glUniform3ivEiiPKi(
    QOpenGLFunctions_2_0 *self,
    GLint location,
    GLsizei count,
    const GLint *value) {
  self->glUniform3iv(location, count, value);
}

//  void QOpenGLFunctions_2_0::glUniform2iv(GLint location, GLsizei count,
//      const GLint *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glUniform2ivEiiPKi(
    QOpenGLFunctions_2_0 *self,
    GLint location,
    GLsizei count,
    const GLint *value) {
  self->glUniform2iv(location, count, value);
}

//  void QOpenGLFunctions_2_0::glUniform1iv(GLint location, GLsizei count,
//      const GLint *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glUniform1ivEiiPKi(
    QOpenGLFunctions_2_0 *self,
    GLint location,
    GLsizei count,
    const GLint *value) {
  self->glUniform1iv(location, count, value);
}

//  void QOpenGLFunctions_2_0::glUniform4fv(GLint location, GLsizei count,
//      const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glUniform4fvEiiPKf(
    QOpenGLFunctions_2_0 *self,
    GLint location,
    GLsizei count,
    const GLfloat *value) {
  self->glUniform4fv(location, count, value);
}

//  void QOpenGLFunctions_2_0::glUniform3fv(GLint location, GLsizei count,
//      const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glUniform3fvEiiPKf(
    QOpenGLFunctions_2_0 *self,
    GLint location,
    GLsizei count,
    const GLfloat *value) {
  self->glUniform3fv(location, count, value);
}

//  void QOpenGLFunctions_2_0::glUniform2fv(GLint location, GLsizei count,
//      const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glUniform2fvEiiPKf(
    QOpenGLFunctions_2_0 *self,
    GLint location,
    GLsizei count,
    const GLfloat *value) {
  self->glUniform2fv(location, count, value);
}

//  void QOpenGLFunctions_2_0::glUniform1fv(GLint location, GLsizei count,
//      const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glUniform1fvEiiPKf(
    QOpenGLFunctions_2_0 *self,
    GLint location,
    GLsizei count,
    const GLfloat *value) {
  self->glUniform1fv(location, count, value);
}

//  void QOpenGLFunctions_2_0::glUniform4i(GLint location, GLint v0, GLint
//      v1, GLint v2, GLint v3)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_011glUniform4iEiiiii(
    QOpenGLFunctions_2_0 *self,
    GLint location,
    GLint v0,
    GLint v1,
    GLint v2,
    GLint v3) {
  self->glUniform4i(location, v0, v1, v2, v3);
}

//  void QOpenGLFunctions_2_0::glUniform3i(GLint location, GLint v0, GLint
//      v1, GLint v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_011glUniform3iEiiii(
    QOpenGLFunctions_2_0 *self,
    GLint location,
    GLint v0,
    GLint v1,
    GLint v2) {
  self->glUniform3i(location, v0, v1, v2);
}

//  void QOpenGLFunctions_2_0::glUniform2i(GLint location, GLint v0, GLint
//      v1)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_011glUniform2iEiii(
    QOpenGLFunctions_2_0 *self,
    GLint location,
    GLint v0,
    GLint v1) {
  self->glUniform2i(location, v0, v1);
}

//  void QOpenGLFunctions_2_0::glUniform1i(GLint location, GLint v0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_011glUniform1iEii(
    QOpenGLFunctions_2_0 *self,
    GLint location,
    GLint v0) {
  self->glUniform1i(location, v0);
}

//  void QOpenGLFunctions_2_0::glUniform4f(GLint location, GLfloat v0,
//      GLfloat v1, GLfloat v2, GLfloat v3)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_011glUniform4fEiffff(
    QOpenGLFunctions_2_0 *self,
    GLint location,
    GLfloat v0,
    GLfloat v1,
    GLfloat v2,
    GLfloat v3) {
  self->glUniform4f(location, v0, v1, v2, v3);
}

//  void QOpenGLFunctions_2_0::glUniform3f(GLint location, GLfloat v0,
//      GLfloat v1, GLfloat v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_011glUniform3fEifff(
    QOpenGLFunctions_2_0 *self,
    GLint location,
    GLfloat v0,
    GLfloat v1,
    GLfloat v2) {
  self->glUniform3f(location, v0, v1, v2);
}

//  void QOpenGLFunctions_2_0::glUniform2f(GLint location, GLfloat v0,
//      GLfloat v1)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_011glUniform2fEiff(
    QOpenGLFunctions_2_0 *self,
    GLint location,
    GLfloat v0,
    GLfloat v1) {
  self->glUniform2f(location, v0, v1);
}

//  void QOpenGLFunctions_2_0::glUniform1f(GLint location, GLfloat v0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_011glUniform1fEif(
    QOpenGLFunctions_2_0 *self,
    GLint location,
    GLfloat v0) {
  self->glUniform1f(location, v0);
}

//  void QOpenGLFunctions_2_0::glUseProgram(GLuint program)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glUseProgramEj(
    QOpenGLFunctions_2_0 *self,
    GLuint program) {
  self->glUseProgram(program);
}

//  void QOpenGLFunctions_2_0::glShaderSource(GLuint shader, GLsizei count,
//      const GLchar *const *string, const GLint *length)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_014glShaderSourceEjiPKPKcPKi(
    QOpenGLFunctions_2_0 *self,
    GLuint shader,
    GLsizei count,
    const GLchar *const *string,
    const GLint *length) {
  self->glShaderSource(shader, count, string, length);
}

//  void QOpenGLFunctions_2_0::glLinkProgram(GLuint program)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glLinkProgramEj(
    QOpenGLFunctions_2_0 *self,
    GLuint program) {
  self->glLinkProgram(program);
}

//  GLboolean QOpenGLFunctions_2_0::glIsShader(GLuint shader)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN20QOpenGLFunctions_2_010glIsShaderEj(
    QOpenGLFunctions_2_0 *self,
    GLuint shader) {
  return self->glIsShader(shader);
}

//  GLboolean QOpenGLFunctions_2_0::glIsProgram(GLuint program)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN20QOpenGLFunctions_2_011glIsProgramEj(
    QOpenGLFunctions_2_0 *self,
    GLuint program) {
  return self->glIsProgram(program);
}

//  void QOpenGLFunctions_2_0::glGetVertexAttribPointerv(GLuint index, GLenum
//      pname, GLvoid **pointer)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_025glGetVertexAttribPointervEjjPPv(
    QOpenGLFunctions_2_0 *self,
    GLuint index,
    GLenum pname,
    GLvoid **pointer) {
  self->glGetVertexAttribPointerv(index, pname, pointer);
}

//  void QOpenGLFunctions_2_0::glGetVertexAttribiv(GLuint index, GLenum
//      pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_019glGetVertexAttribivEjjPi(
    QOpenGLFunctions_2_0 *self,
    GLuint index,
    GLenum pname,
    GLint *params) {
  self->glGetVertexAttribiv(index, pname, params);
}

//  void QOpenGLFunctions_2_0::glGetVertexAttribfv(GLuint index, GLenum
//      pname, GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_019glGetVertexAttribfvEjjPf(
    QOpenGLFunctions_2_0 *self,
    GLuint index,
    GLenum pname,
    GLfloat *params) {
  self->glGetVertexAttribfv(index, pname, params);
}

//  void QOpenGLFunctions_2_0::glGetVertexAttribdv(GLuint index, GLenum
//      pname, GLdouble *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_019glGetVertexAttribdvEjjPd(
    QOpenGLFunctions_2_0 *self,
    GLuint index,
    GLenum pname,
    GLdouble *params) {
  self->glGetVertexAttribdv(index, pname, params);
}

//  void QOpenGLFunctions_2_0::glGetUniformiv(GLuint program, GLint location,
//      GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_014glGetUniformivEjiPi(
    QOpenGLFunctions_2_0 *self,
    GLuint program,
    GLint location,
    GLint *params) {
  self->glGetUniformiv(program, location, params);
}

//  void QOpenGLFunctions_2_0::glGetUniformfv(GLuint program, GLint location,
//      GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_014glGetUniformfvEjiPf(
    QOpenGLFunctions_2_0 *self,
    GLuint program,
    GLint location,
    GLfloat *params) {
  self->glGetUniformfv(program, location, params);
}

//  GLint QOpenGLFunctions_2_0::glGetUniformLocation(GLuint program, const
//      GLchar *name)
extern "C" Q_DECL_EXPORT
GLint ritual_ZN20QOpenGLFunctions_2_020glGetUniformLocationEjPKc(
    QOpenGLFunctions_2_0 *self,
    GLuint program,
    const GLchar *name) {
  return self->glGetUniformLocation(program, name);
}

//  void QOpenGLFunctions_2_0::glGetShaderSource(GLuint shader, GLsizei
//      bufSize, GLsizei *length, GLchar *source)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_017glGetShaderSourceEjiPiPc(
    QOpenGLFunctions_2_0 *self,
    GLuint shader,
    GLsizei bufSize,
    GLsizei *length,
    GLchar *source) {
  self->glGetShaderSource(shader, bufSize, length, source);
}

//  void QOpenGLFunctions_2_0::glGetShaderInfoLog(GLuint shader, GLsizei
//      bufSize, GLsizei *length, GLchar *infoLog)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_018glGetShaderInfoLogEjiPiPc(
    QOpenGLFunctions_2_0 *self,
    GLuint shader,
    GLsizei bufSize,
    GLsizei *length,
    GLchar *infoLog) {
  self->glGetShaderInfoLog(shader, bufSize, length, infoLog);
}

//  void QOpenGLFunctions_2_0::glGetShaderiv(GLuint shader, GLenum pname,
//      GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glGetShaderivEjjPi(
    QOpenGLFunctions_2_0 *self,
    GLuint shader,
    GLenum pname,
    GLint *params) {
  self->glGetShaderiv(shader, pname, params);
}

//  void QOpenGLFunctions_2_0::glGetProgramInfoLog(GLuint program, GLsizei
//      bufSize, GLsizei *length, GLchar *infoLog)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_019glGetProgramInfoLogEjiPiPc(
    QOpenGLFunctions_2_0 *self,
    GLuint program,
    GLsizei bufSize,
    GLsizei *length,
    GLchar *infoLog) {
  self->glGetProgramInfoLog(program, bufSize, length, infoLog);
}

//  void QOpenGLFunctions_2_0::glGetProgramiv(GLuint program, GLenum pname,
//      GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_014glGetProgramivEjjPi(
    QOpenGLFunctions_2_0 *self,
    GLuint program,
    GLenum pname,
    GLint *params) {
  self->glGetProgramiv(program, pname, params);
}

//  GLint QOpenGLFunctions_2_0::glGetAttribLocation(GLuint program, const
//      GLchar *name)
extern "C" Q_DECL_EXPORT
GLint ritual_ZN20QOpenGLFunctions_2_019glGetAttribLocationEjPKc(
    QOpenGLFunctions_2_0 *self,
    GLuint program,
    const GLchar *name) {
  return self->glGetAttribLocation(program, name);
}

//  void QOpenGLFunctions_2_0::glGetAttachedShaders(GLuint program, GLsizei
//      maxCount, GLsizei *count, GLuint *obj)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_020glGetAttachedShadersEjiPiPj(
    QOpenGLFunctions_2_0 *self,
    GLuint program,
    GLsizei maxCount,
    GLsizei *count,
    GLuint *obj) {
  self->glGetAttachedShaders(program, maxCount, count, obj);
}

//  void QOpenGLFunctions_2_0::glGetActiveUniform(GLuint program, GLuint
//      index, GLsizei bufSize, GLsizei *length, GLint *size, GLenum *type,
//      GLchar *name)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_018glGetActiveUniformEjjiPiS0_PjPc(
    QOpenGLFunctions_2_0 *self,
    GLuint program,
    GLuint index,
    GLsizei bufSize,
    GLsizei *length,
    GLint *size,
    GLenum *type,
    GLchar *name) {
  self->glGetActiveUniform(
      program,
      index,
      bufSize,
      length,
      size,
      type,
      name);
}

//  void QOpenGLFunctions_2_0::glGetActiveAttrib(GLuint program, GLuint
//      index, GLsizei bufSize, GLsizei *length, GLint *size, GLenum *type,
//      GLchar *name)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_017glGetActiveAttribEjjiPiS0_PjPc(
    QOpenGLFunctions_2_0 *self,
    GLuint program,
    GLuint index,
    GLsizei bufSize,
    GLsizei *length,
    GLint *size,
    GLenum *type,
    GLchar *name) {
  self->glGetActiveAttrib(program, index, bufSize, length, size, type, name);
}

//  void QOpenGLFunctions_2_0::glEnableVertexAttribArray(GLuint index)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_025glEnableVertexAttribArrayEj(
    QOpenGLFunctions_2_0 *self,
    GLuint index) {
  self->glEnableVertexAttribArray(index);
}

//  void QOpenGLFunctions_2_0::glDisableVertexAttribArray(GLuint index)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_026glDisableVertexAttribArrayEj(
    QOpenGLFunctions_2_0 *self,
    GLuint index) {
  self->glDisableVertexAttribArray(index);
}

//  void QOpenGLFunctions_2_0::glDetachShader(GLuint program, GLuint shader)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_014glDetachShaderEjj(
    QOpenGLFunctions_2_0 *self,
    GLuint program,
    GLuint shader) {
  self->glDetachShader(program, shader);
}

//  void QOpenGLFunctions_2_0::glDeleteShader(GLuint shader)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_014glDeleteShaderEj(
    QOpenGLFunctions_2_0 *self,
    GLuint shader) {
  self->glDeleteShader(shader);
}

//  void QOpenGLFunctions_2_0::glDeleteProgram(GLuint program)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_015glDeleteProgramEj(
    QOpenGLFunctions_2_0 *self,
    GLuint program) {
  self->glDeleteProgram(program);
}

//  GLuint QOpenGLFunctions_2_0::glCreateShader(GLenum type)
extern "C" Q_DECL_EXPORT
GLuint ritual_ZN20QOpenGLFunctions_2_014glCreateShaderEj(
    QOpenGLFunctions_2_0 *self,
    GLenum type) {
  return self->glCreateShader(type);
}

//  GLuint QOpenGLFunctions_2_0::glCreateProgram()
extern "C" Q_DECL_EXPORT
GLuint ritual_ZN20QOpenGLFunctions_2_015glCreateProgramEv(
    QOpenGLFunctions_2_0 *self) {
  return self->glCreateProgram();
}

//  void QOpenGLFunctions_2_0::glCompileShader(GLuint shader)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_015glCompileShaderEj(
    QOpenGLFunctions_2_0 *self,
    GLuint shader) {
  self->glCompileShader(shader);
}

//  void QOpenGLFunctions_2_0::glBindAttribLocation(GLuint program, GLuint
//      index, const GLchar *name)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_020glBindAttribLocationEjjPKc(
    QOpenGLFunctions_2_0 *self,
    GLuint program,
    GLuint index,
    const GLchar *name) {
  self->glBindAttribLocation(program, index, name);
}

//  void QOpenGLFunctions_2_0::glAttachShader(GLuint program, GLuint shader)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_014glAttachShaderEjj(
    QOpenGLFunctions_2_0 *self,
    GLuint program,
    GLuint shader) {
  self->glAttachShader(program, shader);
}

//  void QOpenGLFunctions_2_0::glStencilMaskSeparate(GLenum face, GLuint
//      mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_021glStencilMaskSeparateEjj(
    QOpenGLFunctions_2_0 *self,
    GLenum face,
    GLuint mask) {
  self->glStencilMaskSeparate(face, mask);
}

//  void QOpenGLFunctions_2_0::glStencilFuncSeparate(GLenum face, GLenum
//      func, GLint ref, GLuint mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_021glStencilFuncSeparateEjjij(
    QOpenGLFunctions_2_0 *self,
    GLenum face,
    GLenum func,
    GLint ref,
    GLuint mask) {
  self->glStencilFuncSeparate(face, func, ref, mask);
}

//  void QOpenGLFunctions_2_0::glStencilOpSeparate(GLenum face, GLenum sfail,
//      GLenum dpfail, GLenum dppass)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_019glStencilOpSeparateEjjjj(
    QOpenGLFunctions_2_0 *self,
    GLenum face,
    GLenum sfail,
    GLenum dpfail,
    GLenum dppass) {
  self->glStencilOpSeparate(face, sfail, dpfail, dppass);
}

//  void QOpenGLFunctions_2_0::glDrawBuffers(GLsizei n, const GLenum *bufs)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glDrawBuffersEiPKj(
    QOpenGLFunctions_2_0 *self,
    GLsizei n,
    const GLenum *bufs) {
  self->glDrawBuffers(n, bufs);
}

//  void QOpenGLFunctions_2_0::glBlendEquationSeparate(GLenum modeRGB, GLenum
//      modeAlpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_023glBlendEquationSeparateEjj(
    QOpenGLFunctions_2_0 *self,
    GLenum modeRGB,
    GLenum modeAlpha) {
  self->glBlendEquationSeparate(modeRGB, modeAlpha);
}

//  void QOpenGLFunctions_2_0::glTranslatef(GLfloat x, GLfloat y, GLfloat z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glTranslatefEfff(
    QOpenGLFunctions_2_0 *self,
    GLfloat x,
    GLfloat y,
    GLfloat z) {
  self->glTranslatef(x, y, z);
}

//  void QOpenGLFunctions_2_0::glTranslated(GLdouble x, GLdouble y, GLdouble
//      z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glTranslatedEddd(
    QOpenGLFunctions_2_0 *self,
    GLdouble x,
    GLdouble y,
    GLdouble z) {
  self->glTranslated(x, y, z);
}

//  void QOpenGLFunctions_2_0::glScalef(GLfloat x, GLfloat y, GLfloat z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_08glScalefEfff(
    QOpenGLFunctions_2_0 *self,
    GLfloat x,
    GLfloat y,
    GLfloat z) {
  self->glScalef(x, y, z);
}

//  void QOpenGLFunctions_2_0::glScaled(GLdouble x, GLdouble y, GLdouble z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_08glScaledEddd(
    QOpenGLFunctions_2_0 *self,
    GLdouble x,
    GLdouble y,
    GLdouble z) {
  self->glScaled(x, y, z);
}

//  void QOpenGLFunctions_2_0::glRotatef(GLfloat angle, GLfloat x, GLfloat y,
//      GLfloat z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_09glRotatefEffff(
    QOpenGLFunctions_2_0 *self,
    GLfloat angle,
    GLfloat x,
    GLfloat y,
    GLfloat z) {
  self->glRotatef(angle, x, y, z);
}

//  void QOpenGLFunctions_2_0::glRotated(GLdouble angle, GLdouble x, GLdouble
//      y, GLdouble z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_09glRotatedEdddd(
    QOpenGLFunctions_2_0 *self,
    GLdouble angle,
    GLdouble x,
    GLdouble y,
    GLdouble z) {
  self->glRotated(angle, x, y, z);
}

//  void QOpenGLFunctions_2_0::glPushMatrix()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glPushMatrixEv(
    QOpenGLFunctions_2_0 *self) {
  self->glPushMatrix();
}

//  void QOpenGLFunctions_2_0::glPopMatrix()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_011glPopMatrixEv(
    QOpenGLFunctions_2_0 *self) {
  self->glPopMatrix();
}

//  void QOpenGLFunctions_2_0::glOrtho(GLdouble left, GLdouble right,
//      GLdouble bottom, GLdouble top, GLdouble zNear, GLdouble zFar)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_07glOrthoEdddddd(
    QOpenGLFunctions_2_0 *self,
    GLdouble left,
    GLdouble right,
    GLdouble bottom,
    GLdouble top,
    GLdouble zNear,
    GLdouble zFar) {
  self->glOrtho(left, right, bottom, top, zNear, zFar);
}

//  void QOpenGLFunctions_2_0::glMultMatrixd(const GLdouble *m)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glMultMatrixdEPKd(
    QOpenGLFunctions_2_0 *self,
    const GLdouble *m) {
  self->glMultMatrixd(m);
}

//  void QOpenGLFunctions_2_0::glMultMatrixf(const GLfloat *m)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glMultMatrixfEPKf(
    QOpenGLFunctions_2_0 *self,
    const GLfloat *m) {
  self->glMultMatrixf(m);
}

//  void QOpenGLFunctions_2_0::glMatrixMode(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glMatrixModeEj(
    QOpenGLFunctions_2_0 *self,
    GLenum mode) {
  self->glMatrixMode(mode);
}

//  void QOpenGLFunctions_2_0::glLoadMatrixd(const GLdouble *m)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glLoadMatrixdEPKd(
    QOpenGLFunctions_2_0 *self,
    const GLdouble *m) {
  self->glLoadMatrixd(m);
}

//  void QOpenGLFunctions_2_0::glLoadMatrixf(const GLfloat *m)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glLoadMatrixfEPKf(
    QOpenGLFunctions_2_0 *self,
    const GLfloat *m) {
  self->glLoadMatrixf(m);
}

//  void QOpenGLFunctions_2_0::glLoadIdentity()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_014glLoadIdentityEv(
    QOpenGLFunctions_2_0 *self) {
  self->glLoadIdentity();
}

//  void QOpenGLFunctions_2_0::glFrustum(GLdouble left, GLdouble right,
//      GLdouble bottom, GLdouble top, GLdouble zNear, GLdouble zFar)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_09glFrustumEdddddd(
    QOpenGLFunctions_2_0 *self,
    GLdouble left,
    GLdouble right,
    GLdouble bottom,
    GLdouble top,
    GLdouble zNear,
    GLdouble zFar) {
  self->glFrustum(left, right, bottom, top, zNear, zFar);
}

//  GLboolean QOpenGLFunctions_2_0::glIsList(GLuint list)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN20QOpenGLFunctions_2_08glIsListEj(
    QOpenGLFunctions_2_0 *self,
    GLuint list) {
  return self->glIsList(list);
}

//  void QOpenGLFunctions_2_0::glGetTexGeniv(GLenum coord, GLenum pname,
//      GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glGetTexGenivEjjPi(
    QOpenGLFunctions_2_0 *self,
    GLenum coord,
    GLenum pname,
    GLint *params) {
  self->glGetTexGeniv(coord, pname, params);
}

//  void QOpenGLFunctions_2_0::glGetTexGenfv(GLenum coord, GLenum pname,
//      GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glGetTexGenfvEjjPf(
    QOpenGLFunctions_2_0 *self,
    GLenum coord,
    GLenum pname,
    GLfloat *params) {
  self->glGetTexGenfv(coord, pname, params);
}

//  void QOpenGLFunctions_2_0::glGetTexGendv(GLenum coord, GLenum pname,
//      GLdouble *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glGetTexGendvEjjPd(
    QOpenGLFunctions_2_0 *self,
    GLenum coord,
    GLenum pname,
    GLdouble *params) {
  self->glGetTexGendv(coord, pname, params);
}

//  void QOpenGLFunctions_2_0::glGetTexEnviv(GLenum target, GLenum pname,
//      GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glGetTexEnvivEjjPi(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLenum pname,
    GLint *params) {
  self->glGetTexEnviv(target, pname, params);
}

//  void QOpenGLFunctions_2_0::glGetTexEnvfv(GLenum target, GLenum pname,
//      GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glGetTexEnvfvEjjPf(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLenum pname,
    GLfloat *params) {
  self->glGetTexEnvfv(target, pname, params);
}

//  void QOpenGLFunctions_2_0::glGetPolygonStipple(GLubyte *mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_019glGetPolygonStippleEPh(
    QOpenGLFunctions_2_0 *self,
    GLubyte *mask) {
  self->glGetPolygonStipple(mask);
}

//  void QOpenGLFunctions_2_0::glGetPixelMapusv(GLenum map, GLushort *values)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_016glGetPixelMapusvEjPt(
    QOpenGLFunctions_2_0 *self,
    GLenum map,
    GLushort *values) {
  self->glGetPixelMapusv(map, values);
}

//  void QOpenGLFunctions_2_0::glGetPixelMapuiv(GLenum map, GLuint *values)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_016glGetPixelMapuivEjPj(
    QOpenGLFunctions_2_0 *self,
    GLenum map,
    GLuint *values) {
  self->glGetPixelMapuiv(map, values);
}

//  void QOpenGLFunctions_2_0::glGetPixelMapfv(GLenum map, GLfloat *values)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_015glGetPixelMapfvEjPf(
    QOpenGLFunctions_2_0 *self,
    GLenum map,
    GLfloat *values) {
  self->glGetPixelMapfv(map, values);
}

//  void QOpenGLFunctions_2_0::glGetMaterialiv(GLenum face, GLenum pname,
//      GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_015glGetMaterialivEjjPi(
    QOpenGLFunctions_2_0 *self,
    GLenum face,
    GLenum pname,
    GLint *params) {
  self->glGetMaterialiv(face, pname, params);
}

//  void QOpenGLFunctions_2_0::glGetMaterialfv(GLenum face, GLenum pname,
//      GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_015glGetMaterialfvEjjPf(
    QOpenGLFunctions_2_0 *self,
    GLenum face,
    GLenum pname,
    GLfloat *params) {
  self->glGetMaterialfv(face, pname, params);
}

//  void QOpenGLFunctions_2_0::glGetMapiv(GLenum target, GLenum query, GLint
//      *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_010glGetMapivEjjPi(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLenum query,
    GLint *v) {
  self->glGetMapiv(target, query, v);
}

//  void QOpenGLFunctions_2_0::glGetMapfv(GLenum target, GLenum query,
//      GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_010glGetMapfvEjjPf(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLenum query,
    GLfloat *v) {
  self->glGetMapfv(target, query, v);
}

//  void QOpenGLFunctions_2_0::glGetMapdv(GLenum target, GLenum query,
//      GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_010glGetMapdvEjjPd(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLenum query,
    GLdouble *v) {
  self->glGetMapdv(target, query, v);
}

//  void QOpenGLFunctions_2_0::glGetLightiv(GLenum light, GLenum pname, GLint
//      *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glGetLightivEjjPi(
    QOpenGLFunctions_2_0 *self,
    GLenum light,
    GLenum pname,
    GLint *params) {
  self->glGetLightiv(light, pname, params);
}

//  void QOpenGLFunctions_2_0::glGetLightfv(GLenum light, GLenum pname,
//      GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glGetLightfvEjjPf(
    QOpenGLFunctions_2_0 *self,
    GLenum light,
    GLenum pname,
    GLfloat *params) {
  self->glGetLightfv(light, pname, params);
}

//  void QOpenGLFunctions_2_0::glGetClipPlane(GLenum plane, GLdouble
//      *equation)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_014glGetClipPlaneEjPd(
    QOpenGLFunctions_2_0 *self,
    GLenum plane,
    GLdouble *equation) {
  self->glGetClipPlane(plane, equation);
}

//  void QOpenGLFunctions_2_0::glDrawPixels(GLsizei width, GLsizei height,
//      GLenum format, GLenum type, const GLvoid *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glDrawPixelsEiijjPKv(
    QOpenGLFunctions_2_0 *self,
    GLsizei width,
    GLsizei height,
    GLenum format,
    GLenum type,
    const GLvoid *pixels) {
  self->glDrawPixels(width, height, format, type, pixels);
}

//  void QOpenGLFunctions_2_0::glCopyPixels(GLint x, GLint y, GLsizei width,
//      GLsizei height, GLenum type)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glCopyPixelsEiiiij(
    QOpenGLFunctions_2_0 *self,
    GLint x,
    GLint y,
    GLsizei width,
    GLsizei height,
    GLenum type) {
  self->glCopyPixels(x, y, width, height, type);
}

//  void QOpenGLFunctions_2_0::glPixelMapusv(GLenum map, GLint mapsize, const
//      GLushort *values)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glPixelMapusvEjiPKt(
    QOpenGLFunctions_2_0 *self,
    GLenum map,
    GLint mapsize,
    const GLushort *values) {
  self->glPixelMapusv(map, mapsize, values);
}

//  void QOpenGLFunctions_2_0::glPixelMapuiv(GLenum map, GLint mapsize, const
//      GLuint *values)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glPixelMapuivEjiPKj(
    QOpenGLFunctions_2_0 *self,
    GLenum map,
    GLint mapsize,
    const GLuint *values) {
  self->glPixelMapuiv(map, mapsize, values);
}

//  void QOpenGLFunctions_2_0::glPixelMapfv(GLenum map, GLint mapsize, const
//      GLfloat *values)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glPixelMapfvEjiPKf(
    QOpenGLFunctions_2_0 *self,
    GLenum map,
    GLint mapsize,
    const GLfloat *values) {
  self->glPixelMapfv(map, mapsize, values);
}

//  void QOpenGLFunctions_2_0::glPixelTransferi(GLenum pname, GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_016glPixelTransferiEji(
    QOpenGLFunctions_2_0 *self,
    GLenum pname,
    GLint param) {
  self->glPixelTransferi(pname, param);
}

//  void QOpenGLFunctions_2_0::glPixelTransferf(GLenum pname, GLfloat param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_016glPixelTransferfEjf(
    QOpenGLFunctions_2_0 *self,
    GLenum pname,
    GLfloat param) {
  self->glPixelTransferf(pname, param);
}

//  void QOpenGLFunctions_2_0::glPixelZoom(GLfloat xfactor, GLfloat yfactor)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_011glPixelZoomEff(
    QOpenGLFunctions_2_0 *self,
    GLfloat xfactor,
    GLfloat yfactor) {
  self->glPixelZoom(xfactor, yfactor);
}

//  void QOpenGLFunctions_2_0::glAlphaFunc(GLenum func, GLfloat ref)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_011glAlphaFuncEjf(
    QOpenGLFunctions_2_0 *self,
    GLenum func,
    GLfloat ref) {
  self->glAlphaFunc(func, ref);
}

//  void QOpenGLFunctions_2_0::glEvalPoint2(GLint i, GLint j)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glEvalPoint2Eii(
    QOpenGLFunctions_2_0 *self,
    GLint i,
    GLint j) {
  self->glEvalPoint2(i, j);
}

//  void QOpenGLFunctions_2_0::glEvalMesh2(GLenum mode, GLint i1, GLint i2,
//      GLint j1, GLint j2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_011glEvalMesh2Ejiiii(
    QOpenGLFunctions_2_0 *self,
    GLenum mode,
    GLint i1,
    GLint i2,
    GLint j1,
    GLint j2) {
  self->glEvalMesh2(mode, i1, i2, j1, j2);
}

//  void QOpenGLFunctions_2_0::glEvalPoint1(GLint i)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glEvalPoint1Ei(
    QOpenGLFunctions_2_0 *self,
    GLint i) {
  self->glEvalPoint1(i);
}

//  void QOpenGLFunctions_2_0::glEvalMesh1(GLenum mode, GLint i1, GLint i2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_011glEvalMesh1Ejii(
    QOpenGLFunctions_2_0 *self,
    GLenum mode,
    GLint i1,
    GLint i2) {
  self->glEvalMesh1(mode, i1, i2);
}

//  void QOpenGLFunctions_2_0::glEvalCoord2fv(const GLfloat *u)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_014glEvalCoord2fvEPKf(
    QOpenGLFunctions_2_0 *self,
    const GLfloat *u) {
  self->glEvalCoord2fv(u);
}

//  void QOpenGLFunctions_2_0::glEvalCoord2f(GLfloat u, GLfloat v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glEvalCoord2fEff(
    QOpenGLFunctions_2_0 *self,
    GLfloat u,
    GLfloat v) {
  self->glEvalCoord2f(u, v);
}

//  void QOpenGLFunctions_2_0::glEvalCoord2dv(const GLdouble *u)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_014glEvalCoord2dvEPKd(
    QOpenGLFunctions_2_0 *self,
    const GLdouble *u) {
  self->glEvalCoord2dv(u);
}

//  void QOpenGLFunctions_2_0::glEvalCoord2d(GLdouble u, GLdouble v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glEvalCoord2dEdd(
    QOpenGLFunctions_2_0 *self,
    GLdouble u,
    GLdouble v) {
  self->glEvalCoord2d(u, v);
}

//  void QOpenGLFunctions_2_0::glEvalCoord1fv(const GLfloat *u)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_014glEvalCoord1fvEPKf(
    QOpenGLFunctions_2_0 *self,
    const GLfloat *u) {
  self->glEvalCoord1fv(u);
}

//  void QOpenGLFunctions_2_0::glEvalCoord1f(GLfloat u)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glEvalCoord1fEf(
    QOpenGLFunctions_2_0 *self,
    GLfloat u) {
  self->glEvalCoord1f(u);
}

//  void QOpenGLFunctions_2_0::glEvalCoord1dv(const GLdouble *u)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_014glEvalCoord1dvEPKd(
    QOpenGLFunctions_2_0 *self,
    const GLdouble *u) {
  self->glEvalCoord1dv(u);
}

//  void QOpenGLFunctions_2_0::glEvalCoord1d(GLdouble u)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glEvalCoord1dEd(
    QOpenGLFunctions_2_0 *self,
    GLdouble u) {
  self->glEvalCoord1d(u);
}

//  void QOpenGLFunctions_2_0::glMapGrid2f(GLint un, GLfloat u1, GLfloat u2,
//      GLint vn, GLfloat v1, GLfloat v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_011glMapGrid2fEiffiff(
    QOpenGLFunctions_2_0 *self,
    GLint un,
    GLfloat u1,
    GLfloat u2,
    GLint vn,
    GLfloat v1,
    GLfloat v2) {
  self->glMapGrid2f(un, u1, u2, vn, v1, v2);
}

//  void QOpenGLFunctions_2_0::glMapGrid2d(GLint un, GLdouble u1, GLdouble
//      u2, GLint vn, GLdouble v1, GLdouble v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_011glMapGrid2dEiddidd(
    QOpenGLFunctions_2_0 *self,
    GLint un,
    GLdouble u1,
    GLdouble u2,
    GLint vn,
    GLdouble v1,
    GLdouble v2) {
  self->glMapGrid2d(un, u1, u2, vn, v1, v2);
}

//  void QOpenGLFunctions_2_0::glMapGrid1f(GLint un, GLfloat u1, GLfloat u2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_011glMapGrid1fEiff(
    QOpenGLFunctions_2_0 *self,
    GLint un,
    GLfloat u1,
    GLfloat u2) {
  self->glMapGrid1f(un, u1, u2);
}

//  void QOpenGLFunctions_2_0::glMapGrid1d(GLint un, GLdouble u1, GLdouble
//      u2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_011glMapGrid1dEidd(
    QOpenGLFunctions_2_0 *self,
    GLint un,
    GLdouble u1,
    GLdouble u2) {
  self->glMapGrid1d(un, u1, u2);
}

//  void QOpenGLFunctions_2_0::glMap2f(GLenum target, GLfloat u1, GLfloat u2,
//      GLint ustride, GLint uorder, GLfloat v1, GLfloat v2, GLint vstride,
//      GLint vorder, const GLfloat *points)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_07glMap2fEjffiiffiiPKf(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLfloat u1,
    GLfloat u2,
    GLint ustride,
    GLint uorder,
    GLfloat v1,
    GLfloat v2,
    GLint vstride,
    GLint vorder,
    const GLfloat *points) {
  self->glMap2f(
      target,
      u1,
      u2,
      ustride,
      uorder,
      v1,
      v2,
      vstride,
      vorder,
      points);
}

//  void QOpenGLFunctions_2_0::glMap2d(GLenum target, GLdouble u1, GLdouble
//      u2, GLint ustride, GLint uorder, GLdouble v1, GLdouble v2, GLint
//      vstride, GLint vorder, const GLdouble *points)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_07glMap2dEjddiiddiiPKd(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLdouble u1,
    GLdouble u2,
    GLint ustride,
    GLint uorder,
    GLdouble v1,
    GLdouble v2,
    GLint vstride,
    GLint vorder,
    const GLdouble *points) {
  self->glMap2d(
      target,
      u1,
      u2,
      ustride,
      uorder,
      v1,
      v2,
      vstride,
      vorder,
      points);
}

//  void QOpenGLFunctions_2_0::glMap1f(GLenum target, GLfloat u1, GLfloat u2,
//      GLint stride, GLint order, const GLfloat *points)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_07glMap1fEjffiiPKf(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLfloat u1,
    GLfloat u2,
    GLint stride,
    GLint order,
    const GLfloat *points) {
  self->glMap1f(target, u1, u2, stride, order, points);
}

//  void QOpenGLFunctions_2_0::glMap1d(GLenum target, GLdouble u1, GLdouble
//      u2, GLint stride, GLint order, const GLdouble *points)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_07glMap1dEjddiiPKd(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLdouble u1,
    GLdouble u2,
    GLint stride,
    GLint order,
    const GLdouble *points) {
  self->glMap1d(target, u1, u2, stride, order, points);
}

//  void QOpenGLFunctions_2_0::glPushAttrib(GLbitfield mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glPushAttribEj(
    QOpenGLFunctions_2_0 *self,
    GLbitfield mask) {
  self->glPushAttrib(mask);
}

//  void QOpenGLFunctions_2_0::glPopAttrib()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_011glPopAttribEv(
    QOpenGLFunctions_2_0 *self) {
  self->glPopAttrib();
}

//  void QOpenGLFunctions_2_0::glAccum(GLenum op, GLfloat value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_07glAccumEjf(
    QOpenGLFunctions_2_0 *self,
    GLenum op,
    GLfloat value) {
  self->glAccum(op, value);
}

//  void QOpenGLFunctions_2_0::glIndexMask(GLuint mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_011glIndexMaskEj(
    QOpenGLFunctions_2_0 *self,
    GLuint mask) {
  self->glIndexMask(mask);
}

//  void QOpenGLFunctions_2_0::glClearIndex(GLfloat c)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glClearIndexEf(
    QOpenGLFunctions_2_0 *self,
    GLfloat c) {
  self->glClearIndex(c);
}

//  void QOpenGLFunctions_2_0::glClearAccum(GLfloat red, GLfloat green,
//      GLfloat blue, GLfloat alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glClearAccumEffff(
    QOpenGLFunctions_2_0 *self,
    GLfloat red,
    GLfloat green,
    GLfloat blue,
    GLfloat alpha) {
  self->glClearAccum(red, green, blue, alpha);
}

//  void QOpenGLFunctions_2_0::glPushName(GLuint name)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_010glPushNameEj(
    QOpenGLFunctions_2_0 *self,
    GLuint name) {
  self->glPushName(name);
}

//  void QOpenGLFunctions_2_0::glPopName()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_09glPopNameEv(
    QOpenGLFunctions_2_0 *self) {
  self->glPopName();
}

//  void QOpenGLFunctions_2_0::glPassThrough(GLfloat token)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glPassThroughEf(
    QOpenGLFunctions_2_0 *self,
    GLfloat token) {
  self->glPassThrough(token);
}

//  void QOpenGLFunctions_2_0::glLoadName(GLuint name)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_010glLoadNameEj(
    QOpenGLFunctions_2_0 *self,
    GLuint name) {
  self->glLoadName(name);
}

//  void QOpenGLFunctions_2_0::glInitNames()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_011glInitNamesEv(
    QOpenGLFunctions_2_0 *self) {
  self->glInitNames();
}

//  GLint QOpenGLFunctions_2_0::glRenderMode(GLenum mode)
extern "C" Q_DECL_EXPORT
GLint ritual_ZN20QOpenGLFunctions_2_012glRenderModeEj(
    QOpenGLFunctions_2_0 *self,
    GLenum mode) {
  return self->glRenderMode(mode);
}

//  void QOpenGLFunctions_2_0::glSelectBuffer(GLsizei size, GLuint *buffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_014glSelectBufferEiPj(
    QOpenGLFunctions_2_0 *self,
    GLsizei size,
    GLuint *buffer) {
  self->glSelectBuffer(size, buffer);
}

//  void QOpenGLFunctions_2_0::glFeedbackBuffer(GLsizei size, GLenum type,
//      GLfloat *buffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_016glFeedbackBufferEijPf(
    QOpenGLFunctions_2_0 *self,
    GLsizei size,
    GLenum type,
    GLfloat *buffer) {
  self->glFeedbackBuffer(size, type, buffer);
}

//  void QOpenGLFunctions_2_0::glTexGeniv(GLenum coord, GLenum pname, const
//      GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_010glTexGenivEjjPKi(
    QOpenGLFunctions_2_0 *self,
    GLenum coord,
    GLenum pname,
    const GLint *params) {
  self->glTexGeniv(coord, pname, params);
}

//  void QOpenGLFunctions_2_0::glTexGeni(GLenum coord, GLenum pname, GLint
//      param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_09glTexGeniEjji(
    QOpenGLFunctions_2_0 *self,
    GLenum coord,
    GLenum pname,
    GLint param) {
  self->glTexGeni(coord, pname, param);
}

//  void QOpenGLFunctions_2_0::glTexGenfv(GLenum coord, GLenum pname, const
//      GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_010glTexGenfvEjjPKf(
    QOpenGLFunctions_2_0 *self,
    GLenum coord,
    GLenum pname,
    const GLfloat *params) {
  self->glTexGenfv(coord, pname, params);
}

//  void QOpenGLFunctions_2_0::glTexGenf(GLenum coord, GLenum pname, GLfloat
//      param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_09glTexGenfEjjf(
    QOpenGLFunctions_2_0 *self,
    GLenum coord,
    GLenum pname,
    GLfloat param) {
  self->glTexGenf(coord, pname, param);
}

//  void QOpenGLFunctions_2_0::glTexGendv(GLenum coord, GLenum pname, const
//      GLdouble *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_010glTexGendvEjjPKd(
    QOpenGLFunctions_2_0 *self,
    GLenum coord,
    GLenum pname,
    const GLdouble *params) {
  self->glTexGendv(coord, pname, params);
}

//  void QOpenGLFunctions_2_0::glTexGend(GLenum coord, GLenum pname, GLdouble
//      param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_09glTexGendEjjd(
    QOpenGLFunctions_2_0 *self,
    GLenum coord,
    GLenum pname,
    GLdouble param) {
  self->glTexGend(coord, pname, param);
}

//  void QOpenGLFunctions_2_0::glTexEnviv(GLenum target, GLenum pname, const
//      GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_010glTexEnvivEjjPKi(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLenum pname,
    const GLint *params) {
  self->glTexEnviv(target, pname, params);
}

//  void QOpenGLFunctions_2_0::glTexEnvi(GLenum target, GLenum pname, GLint
//      param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_09glTexEnviEjji(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLenum pname,
    GLint param) {
  self->glTexEnvi(target, pname, param);
}

//  void QOpenGLFunctions_2_0::glTexEnvfv(GLenum target, GLenum pname, const
//      GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_010glTexEnvfvEjjPKf(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLenum pname,
    const GLfloat *params) {
  self->glTexEnvfv(target, pname, params);
}

//  void QOpenGLFunctions_2_0::glTexEnvf(GLenum target, GLenum pname, GLfloat
//      param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_09glTexEnvfEjjf(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLenum pname,
    GLfloat param) {
  self->glTexEnvf(target, pname, param);
}

//  void QOpenGLFunctions_2_0::glShadeModel(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glShadeModelEj(
    QOpenGLFunctions_2_0 *self,
    GLenum mode) {
  self->glShadeModel(mode);
}

//  void QOpenGLFunctions_2_0::glPolygonStipple(const GLubyte *mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_016glPolygonStippleEPKh(
    QOpenGLFunctions_2_0 *self,
    const GLubyte *mask) {
  self->glPolygonStipple(mask);
}

//  void QOpenGLFunctions_2_0::glMaterialiv(GLenum face, GLenum pname, const
//      GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glMaterialivEjjPKi(
    QOpenGLFunctions_2_0 *self,
    GLenum face,
    GLenum pname,
    const GLint *params) {
  self->glMaterialiv(face, pname, params);
}

//  void QOpenGLFunctions_2_0::glMateriali(GLenum face, GLenum pname, GLint
//      param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_011glMaterialiEjji(
    QOpenGLFunctions_2_0 *self,
    GLenum face,
    GLenum pname,
    GLint param) {
  self->glMateriali(face, pname, param);
}

//  void QOpenGLFunctions_2_0::glMaterialfv(GLenum face, GLenum pname, const
//      GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glMaterialfvEjjPKf(
    QOpenGLFunctions_2_0 *self,
    GLenum face,
    GLenum pname,
    const GLfloat *params) {
  self->glMaterialfv(face, pname, params);
}

//  void QOpenGLFunctions_2_0::glMaterialf(GLenum face, GLenum pname, GLfloat
//      param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_011glMaterialfEjjf(
    QOpenGLFunctions_2_0 *self,
    GLenum face,
    GLenum pname,
    GLfloat param) {
  self->glMaterialf(face, pname, param);
}

//  void QOpenGLFunctions_2_0::glLineStipple(GLint factor, GLushort pattern)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glLineStippleEit(
    QOpenGLFunctions_2_0 *self,
    GLint factor,
    GLushort pattern) {
  self->glLineStipple(factor, pattern);
}

//  void QOpenGLFunctions_2_0::glLightModeliv(GLenum pname, const GLint
//      *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_014glLightModelivEjPKi(
    QOpenGLFunctions_2_0 *self,
    GLenum pname,
    const GLint *params) {
  self->glLightModeliv(pname, params);
}

//  void QOpenGLFunctions_2_0::glLightModeli(GLenum pname, GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glLightModeliEji(
    QOpenGLFunctions_2_0 *self,
    GLenum pname,
    GLint param) {
  self->glLightModeli(pname, param);
}

//  void QOpenGLFunctions_2_0::glLightModelfv(GLenum pname, const GLfloat
//      *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_014glLightModelfvEjPKf(
    QOpenGLFunctions_2_0 *self,
    GLenum pname,
    const GLfloat *params) {
  self->glLightModelfv(pname, params);
}

//  void QOpenGLFunctions_2_0::glLightModelf(GLenum pname, GLfloat param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glLightModelfEjf(
    QOpenGLFunctions_2_0 *self,
    GLenum pname,
    GLfloat param) {
  self->glLightModelf(pname, param);
}

//  void QOpenGLFunctions_2_0::glLightiv(GLenum light, GLenum pname, const
//      GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_09glLightivEjjPKi(
    QOpenGLFunctions_2_0 *self,
    GLenum light,
    GLenum pname,
    const GLint *params) {
  self->glLightiv(light, pname, params);
}

//  void QOpenGLFunctions_2_0::glLighti(GLenum light, GLenum pname, GLint
//      param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_08glLightiEjji(
    QOpenGLFunctions_2_0 *self,
    GLenum light,
    GLenum pname,
    GLint param) {
  self->glLighti(light, pname, param);
}

//  void QOpenGLFunctions_2_0::glLightfv(GLenum light, GLenum pname, const
//      GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_09glLightfvEjjPKf(
    QOpenGLFunctions_2_0 *self,
    GLenum light,
    GLenum pname,
    const GLfloat *params) {
  self->glLightfv(light, pname, params);
}

//  void QOpenGLFunctions_2_0::glLightf(GLenum light, GLenum pname, GLfloat
//      param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_08glLightfEjjf(
    QOpenGLFunctions_2_0 *self,
    GLenum light,
    GLenum pname,
    GLfloat param) {
  self->glLightf(light, pname, param);
}

//  void QOpenGLFunctions_2_0::glFogiv(GLenum pname, const GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_07glFogivEjPKi(
    QOpenGLFunctions_2_0 *self,
    GLenum pname,
    const GLint *params) {
  self->glFogiv(pname, params);
}

//  void QOpenGLFunctions_2_0::glFogi(GLenum pname, GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_06glFogiEji(
    QOpenGLFunctions_2_0 *self,
    GLenum pname,
    GLint param) {
  self->glFogi(pname, param);
}

//  void QOpenGLFunctions_2_0::glFogfv(GLenum pname, const GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_07glFogfvEjPKf(
    QOpenGLFunctions_2_0 *self,
    GLenum pname,
    const GLfloat *params) {
  self->glFogfv(pname, params);
}

//  void QOpenGLFunctions_2_0::glFogf(GLenum pname, GLfloat param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_06glFogfEjf(
    QOpenGLFunctions_2_0 *self,
    GLenum pname,
    GLfloat param) {
  self->glFogf(pname, param);
}

//  void QOpenGLFunctions_2_0::glColorMaterial(GLenum face, GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_015glColorMaterialEjj(
    QOpenGLFunctions_2_0 *self,
    GLenum face,
    GLenum mode) {
  self->glColorMaterial(face, mode);
}

//  void QOpenGLFunctions_2_0::glClipPlane(GLenum plane, const GLdouble
//      *equation)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_011glClipPlaneEjPKd(
    QOpenGLFunctions_2_0 *self,
    GLenum plane,
    const GLdouble *equation) {
  self->glClipPlane(plane, equation);
}

//  void QOpenGLFunctions_2_0::glVertex4sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_011glVertex4svEPKs(
    QOpenGLFunctions_2_0 *self,
    const GLshort *v) {
  self->glVertex4sv(v);
}

//  void QOpenGLFunctions_2_0::glVertex4s(GLshort x, GLshort y, GLshort z,
//      GLshort w)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_010glVertex4sEssss(
    QOpenGLFunctions_2_0 *self,
    GLshort x,
    GLshort y,
    GLshort z,
    GLshort w) {
  self->glVertex4s(x, y, z, w);
}

//  void QOpenGLFunctions_2_0::glVertex4iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_011glVertex4ivEPKi(
    QOpenGLFunctions_2_0 *self,
    const GLint *v) {
  self->glVertex4iv(v);
}

//  void QOpenGLFunctions_2_0::glVertex4i(GLint x, GLint y, GLint z, GLint w)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_010glVertex4iEiiii(
    QOpenGLFunctions_2_0 *self,
    GLint x,
    GLint y,
    GLint z,
    GLint w) {
  self->glVertex4i(x, y, z, w);
}

//  void QOpenGLFunctions_2_0::glVertex4fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_011glVertex4fvEPKf(
    QOpenGLFunctions_2_0 *self,
    const GLfloat *v) {
  self->glVertex4fv(v);
}

//  void QOpenGLFunctions_2_0::glVertex4f(GLfloat x, GLfloat y, GLfloat z,
//      GLfloat w)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_010glVertex4fEffff(
    QOpenGLFunctions_2_0 *self,
    GLfloat x,
    GLfloat y,
    GLfloat z,
    GLfloat w) {
  self->glVertex4f(x, y, z, w);
}

//  void QOpenGLFunctions_2_0::glVertex4dv(const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_011glVertex4dvEPKd(
    QOpenGLFunctions_2_0 *self,
    const GLdouble *v) {
  self->glVertex4dv(v);
}

//  void QOpenGLFunctions_2_0::glVertex4d(GLdouble x, GLdouble y, GLdouble z,
//      GLdouble w)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_010glVertex4dEdddd(
    QOpenGLFunctions_2_0 *self,
    GLdouble x,
    GLdouble y,
    GLdouble z,
    GLdouble w) {
  self->glVertex4d(x, y, z, w);
}

//  void QOpenGLFunctions_2_0::glVertex3sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_011glVertex3svEPKs(
    QOpenGLFunctions_2_0 *self,
    const GLshort *v) {
  self->glVertex3sv(v);
}

//  void QOpenGLFunctions_2_0::glVertex3s(GLshort x, GLshort y, GLshort z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_010glVertex3sEsss(
    QOpenGLFunctions_2_0 *self,
    GLshort x,
    GLshort y,
    GLshort z) {
  self->glVertex3s(x, y, z);
}

//  void QOpenGLFunctions_2_0::glVertex3iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_011glVertex3ivEPKi(
    QOpenGLFunctions_2_0 *self,
    const GLint *v) {
  self->glVertex3iv(v);
}

//  void QOpenGLFunctions_2_0::glVertex3i(GLint x, GLint y, GLint z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_010glVertex3iEiii(
    QOpenGLFunctions_2_0 *self,
    GLint x,
    GLint y,
    GLint z) {
  self->glVertex3i(x, y, z);
}

//  void QOpenGLFunctions_2_0::glVertex3fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_011glVertex3fvEPKf(
    QOpenGLFunctions_2_0 *self,
    const GLfloat *v) {
  self->glVertex3fv(v);
}

//  void QOpenGLFunctions_2_0::glVertex3f(GLfloat x, GLfloat y, GLfloat z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_010glVertex3fEfff(
    QOpenGLFunctions_2_0 *self,
    GLfloat x,
    GLfloat y,
    GLfloat z) {
  self->glVertex3f(x, y, z);
}

//  void QOpenGLFunctions_2_0::glVertex3dv(const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_011glVertex3dvEPKd(
    QOpenGLFunctions_2_0 *self,
    const GLdouble *v) {
  self->glVertex3dv(v);
}

//  void QOpenGLFunctions_2_0::glVertex3d(GLdouble x, GLdouble y, GLdouble z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_010glVertex3dEddd(
    QOpenGLFunctions_2_0 *self,
    GLdouble x,
    GLdouble y,
    GLdouble z) {
  self->glVertex3d(x, y, z);
}

//  void QOpenGLFunctions_2_0::glVertex2sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_011glVertex2svEPKs(
    QOpenGLFunctions_2_0 *self,
    const GLshort *v) {
  self->glVertex2sv(v);
}

//  void QOpenGLFunctions_2_0::glVertex2s(GLshort x, GLshort y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_010glVertex2sEss(
    QOpenGLFunctions_2_0 *self,
    GLshort x,
    GLshort y) {
  self->glVertex2s(x, y);
}

//  void QOpenGLFunctions_2_0::glVertex2iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_011glVertex2ivEPKi(
    QOpenGLFunctions_2_0 *self,
    const GLint *v) {
  self->glVertex2iv(v);
}

//  void QOpenGLFunctions_2_0::glVertex2i(GLint x, GLint y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_010glVertex2iEii(
    QOpenGLFunctions_2_0 *self,
    GLint x,
    GLint y) {
  self->glVertex2i(x, y);
}

//  void QOpenGLFunctions_2_0::glVertex2fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_011glVertex2fvEPKf(
    QOpenGLFunctions_2_0 *self,
    const GLfloat *v) {
  self->glVertex2fv(v);
}

//  void QOpenGLFunctions_2_0::glVertex2f(GLfloat x, GLfloat y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_010glVertex2fEff(
    QOpenGLFunctions_2_0 *self,
    GLfloat x,
    GLfloat y) {
  self->glVertex2f(x, y);
}

//  void QOpenGLFunctions_2_0::glVertex2dv(const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_011glVertex2dvEPKd(
    QOpenGLFunctions_2_0 *self,
    const GLdouble *v) {
  self->glVertex2dv(v);
}

//  void QOpenGLFunctions_2_0::glVertex2d(GLdouble x, GLdouble y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_010glVertex2dEdd(
    QOpenGLFunctions_2_0 *self,
    GLdouble x,
    GLdouble y) {
  self->glVertex2d(x, y);
}

//  void QOpenGLFunctions_2_0::glTexCoord4sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glTexCoord4svEPKs(
    QOpenGLFunctions_2_0 *self,
    const GLshort *v) {
  self->glTexCoord4sv(v);
}

//  void QOpenGLFunctions_2_0::glTexCoord4s(GLshort s, GLshort t, GLshort r,
//      GLshort q)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glTexCoord4sEssss(
    QOpenGLFunctions_2_0 *self,
    GLshort s,
    GLshort t,
    GLshort r,
    GLshort q) {
  self->glTexCoord4s(s, t, r, q);
}

//  void QOpenGLFunctions_2_0::glTexCoord4iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glTexCoord4ivEPKi(
    QOpenGLFunctions_2_0 *self,
    const GLint *v) {
  self->glTexCoord4iv(v);
}

//  void QOpenGLFunctions_2_0::glTexCoord4i(GLint s, GLint t, GLint r, GLint
//      q)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glTexCoord4iEiiii(
    QOpenGLFunctions_2_0 *self,
    GLint s,
    GLint t,
    GLint r,
    GLint q) {
  self->glTexCoord4i(s, t, r, q);
}

//  void QOpenGLFunctions_2_0::glTexCoord4fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glTexCoord4fvEPKf(
    QOpenGLFunctions_2_0 *self,
    const GLfloat *v) {
  self->glTexCoord4fv(v);
}

//  void QOpenGLFunctions_2_0::glTexCoord4f(GLfloat s, GLfloat t, GLfloat r,
//      GLfloat q)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glTexCoord4fEffff(
    QOpenGLFunctions_2_0 *self,
    GLfloat s,
    GLfloat t,
    GLfloat r,
    GLfloat q) {
  self->glTexCoord4f(s, t, r, q);
}

//  void QOpenGLFunctions_2_0::glTexCoord4dv(const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glTexCoord4dvEPKd(
    QOpenGLFunctions_2_0 *self,
    const GLdouble *v) {
  self->glTexCoord4dv(v);
}

//  void QOpenGLFunctions_2_0::glTexCoord4d(GLdouble s, GLdouble t, GLdouble
//      r, GLdouble q)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glTexCoord4dEdddd(
    QOpenGLFunctions_2_0 *self,
    GLdouble s,
    GLdouble t,
    GLdouble r,
    GLdouble q) {
  self->glTexCoord4d(s, t, r, q);
}

//  void QOpenGLFunctions_2_0::glTexCoord3sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glTexCoord3svEPKs(
    QOpenGLFunctions_2_0 *self,
    const GLshort *v) {
  self->glTexCoord3sv(v);
}

//  void QOpenGLFunctions_2_0::glTexCoord3s(GLshort s, GLshort t, GLshort r)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glTexCoord3sEsss(
    QOpenGLFunctions_2_0 *self,
    GLshort s,
    GLshort t,
    GLshort r) {
  self->glTexCoord3s(s, t, r);
}

//  void QOpenGLFunctions_2_0::glTexCoord3iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glTexCoord3ivEPKi(
    QOpenGLFunctions_2_0 *self,
    const GLint *v) {
  self->glTexCoord3iv(v);
}

//  void QOpenGLFunctions_2_0::glTexCoord3i(GLint s, GLint t, GLint r)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glTexCoord3iEiii(
    QOpenGLFunctions_2_0 *self,
    GLint s,
    GLint t,
    GLint r) {
  self->glTexCoord3i(s, t, r);
}

//  void QOpenGLFunctions_2_0::glTexCoord3fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glTexCoord3fvEPKf(
    QOpenGLFunctions_2_0 *self,
    const GLfloat *v) {
  self->glTexCoord3fv(v);
}

//  void QOpenGLFunctions_2_0::glTexCoord3f(GLfloat s, GLfloat t, GLfloat r)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glTexCoord3fEfff(
    QOpenGLFunctions_2_0 *self,
    GLfloat s,
    GLfloat t,
    GLfloat r) {
  self->glTexCoord3f(s, t, r);
}

//  void QOpenGLFunctions_2_0::glTexCoord3dv(const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glTexCoord3dvEPKd(
    QOpenGLFunctions_2_0 *self,
    const GLdouble *v) {
  self->glTexCoord3dv(v);
}

//  void QOpenGLFunctions_2_0::glTexCoord3d(GLdouble s, GLdouble t, GLdouble
//      r)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glTexCoord3dEddd(
    QOpenGLFunctions_2_0 *self,
    GLdouble s,
    GLdouble t,
    GLdouble r) {
  self->glTexCoord3d(s, t, r);
}

//  void QOpenGLFunctions_2_0::glTexCoord2sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glTexCoord2svEPKs(
    QOpenGLFunctions_2_0 *self,
    const GLshort *v) {
  self->glTexCoord2sv(v);
}

//  void QOpenGLFunctions_2_0::glTexCoord2s(GLshort s, GLshort t)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glTexCoord2sEss(
    QOpenGLFunctions_2_0 *self,
    GLshort s,
    GLshort t) {
  self->glTexCoord2s(s, t);
}

//  void QOpenGLFunctions_2_0::glTexCoord2iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glTexCoord2ivEPKi(
    QOpenGLFunctions_2_0 *self,
    const GLint *v) {
  self->glTexCoord2iv(v);
}

//  void QOpenGLFunctions_2_0::glTexCoord2i(GLint s, GLint t)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glTexCoord2iEii(
    QOpenGLFunctions_2_0 *self,
    GLint s,
    GLint t) {
  self->glTexCoord2i(s, t);
}

//  void QOpenGLFunctions_2_0::glTexCoord2fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glTexCoord2fvEPKf(
    QOpenGLFunctions_2_0 *self,
    const GLfloat *v) {
  self->glTexCoord2fv(v);
}

//  void QOpenGLFunctions_2_0::glTexCoord2f(GLfloat s, GLfloat t)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glTexCoord2fEff(
    QOpenGLFunctions_2_0 *self,
    GLfloat s,
    GLfloat t) {
  self->glTexCoord2f(s, t);
}

//  void QOpenGLFunctions_2_0::glTexCoord2dv(const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glTexCoord2dvEPKd(
    QOpenGLFunctions_2_0 *self,
    const GLdouble *v) {
  self->glTexCoord2dv(v);
}

//  void QOpenGLFunctions_2_0::glTexCoord2d(GLdouble s, GLdouble t)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glTexCoord2dEdd(
    QOpenGLFunctions_2_0 *self,
    GLdouble s,
    GLdouble t) {
  self->glTexCoord2d(s, t);
}

//  void QOpenGLFunctions_2_0::glTexCoord1sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glTexCoord1svEPKs(
    QOpenGLFunctions_2_0 *self,
    const GLshort *v) {
  self->glTexCoord1sv(v);
}

//  void QOpenGLFunctions_2_0::glTexCoord1s(GLshort s)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glTexCoord1sEs(
    QOpenGLFunctions_2_0 *self,
    GLshort s) {
  self->glTexCoord1s(s);
}

//  void QOpenGLFunctions_2_0::glTexCoord1iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glTexCoord1ivEPKi(
    QOpenGLFunctions_2_0 *self,
    const GLint *v) {
  self->glTexCoord1iv(v);
}

//  void QOpenGLFunctions_2_0::glTexCoord1i(GLint s)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glTexCoord1iEi(
    QOpenGLFunctions_2_0 *self,
    GLint s) {
  self->glTexCoord1i(s);
}

//  void QOpenGLFunctions_2_0::glTexCoord1fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glTexCoord1fvEPKf(
    QOpenGLFunctions_2_0 *self,
    const GLfloat *v) {
  self->glTexCoord1fv(v);
}

//  void QOpenGLFunctions_2_0::glTexCoord1f(GLfloat s)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glTexCoord1fEf(
    QOpenGLFunctions_2_0 *self,
    GLfloat s) {
  self->glTexCoord1f(s);
}

//  void QOpenGLFunctions_2_0::glTexCoord1dv(const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glTexCoord1dvEPKd(
    QOpenGLFunctions_2_0 *self,
    const GLdouble *v) {
  self->glTexCoord1dv(v);
}

//  void QOpenGLFunctions_2_0::glTexCoord1d(GLdouble s)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glTexCoord1dEd(
    QOpenGLFunctions_2_0 *self,
    GLdouble s) {
  self->glTexCoord1d(s);
}

//  void QOpenGLFunctions_2_0::glRectsv(const GLshort *v1, const GLshort *v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_08glRectsvEPKsS1_(
    QOpenGLFunctions_2_0 *self,
    const GLshort *v1,
    const GLshort *v2) {
  self->glRectsv(v1, v2);
}

//  void QOpenGLFunctions_2_0::glRects(GLshort x1, GLshort y1, GLshort x2,
//      GLshort y2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_07glRectsEssss(
    QOpenGLFunctions_2_0 *self,
    GLshort x1,
    GLshort y1,
    GLshort x2,
    GLshort y2) {
  self->glRects(x1, y1, x2, y2);
}

//  void QOpenGLFunctions_2_0::glRectiv(const GLint *v1, const GLint *v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_08glRectivEPKiS1_(
    QOpenGLFunctions_2_0 *self,
    const GLint *v1,
    const GLint *v2) {
  self->glRectiv(v1, v2);
}

//  void QOpenGLFunctions_2_0::glRecti(GLint x1, GLint y1, GLint x2, GLint
//      y2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_07glRectiEiiii(
    QOpenGLFunctions_2_0 *self,
    GLint x1,
    GLint y1,
    GLint x2,
    GLint y2) {
  self->glRecti(x1, y1, x2, y2);
}

//  void QOpenGLFunctions_2_0::glRectfv(const GLfloat *v1, const GLfloat *v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_08glRectfvEPKfS1_(
    QOpenGLFunctions_2_0 *self,
    const GLfloat *v1,
    const GLfloat *v2) {
  self->glRectfv(v1, v2);
}

//  void QOpenGLFunctions_2_0::glRectf(GLfloat x1, GLfloat y1, GLfloat x2,
//      GLfloat y2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_07glRectfEffff(
    QOpenGLFunctions_2_0 *self,
    GLfloat x1,
    GLfloat y1,
    GLfloat x2,
    GLfloat y2) {
  self->glRectf(x1, y1, x2, y2);
}

//  void QOpenGLFunctions_2_0::glRectdv(const GLdouble *v1, const GLdouble
//      *v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_08glRectdvEPKdS1_(
    QOpenGLFunctions_2_0 *self,
    const GLdouble *v1,
    const GLdouble *v2) {
  self->glRectdv(v1, v2);
}

//  void QOpenGLFunctions_2_0::glRectd(GLdouble x1, GLdouble y1, GLdouble x2,
//      GLdouble y2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_07glRectdEdddd(
    QOpenGLFunctions_2_0 *self,
    GLdouble x1,
    GLdouble y1,
    GLdouble x2,
    GLdouble y2) {
  self->glRectd(x1, y1, x2, y2);
}

//  void QOpenGLFunctions_2_0::glRasterPos4sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_014glRasterPos4svEPKs(
    QOpenGLFunctions_2_0 *self,
    const GLshort *v) {
  self->glRasterPos4sv(v);
}

//  void QOpenGLFunctions_2_0::glRasterPos4s(GLshort x, GLshort y, GLshort z,
//      GLshort w)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glRasterPos4sEssss(
    QOpenGLFunctions_2_0 *self,
    GLshort x,
    GLshort y,
    GLshort z,
    GLshort w) {
  self->glRasterPos4s(x, y, z, w);
}

//  void QOpenGLFunctions_2_0::glRasterPos4iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_014glRasterPos4ivEPKi(
    QOpenGLFunctions_2_0 *self,
    const GLint *v) {
  self->glRasterPos4iv(v);
}

//  void QOpenGLFunctions_2_0::glRasterPos4i(GLint x, GLint y, GLint z, GLint
//      w)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glRasterPos4iEiiii(
    QOpenGLFunctions_2_0 *self,
    GLint x,
    GLint y,
    GLint z,
    GLint w) {
  self->glRasterPos4i(x, y, z, w);
}

//  void QOpenGLFunctions_2_0::glRasterPos4fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_014glRasterPos4fvEPKf(
    QOpenGLFunctions_2_0 *self,
    const GLfloat *v) {
  self->glRasterPos4fv(v);
}

//  void QOpenGLFunctions_2_0::glRasterPos4f(GLfloat x, GLfloat y, GLfloat z,
//      GLfloat w)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glRasterPos4fEffff(
    QOpenGLFunctions_2_0 *self,
    GLfloat x,
    GLfloat y,
    GLfloat z,
    GLfloat w) {
  self->glRasterPos4f(x, y, z, w);
}

//  void QOpenGLFunctions_2_0::glRasterPos4dv(const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_014glRasterPos4dvEPKd(
    QOpenGLFunctions_2_0 *self,
    const GLdouble *v) {
  self->glRasterPos4dv(v);
}

//  void QOpenGLFunctions_2_0::glRasterPos4d(GLdouble x, GLdouble y, GLdouble
//      z, GLdouble w)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glRasterPos4dEdddd(
    QOpenGLFunctions_2_0 *self,
    GLdouble x,
    GLdouble y,
    GLdouble z,
    GLdouble w) {
  self->glRasterPos4d(x, y, z, w);
}

//  void QOpenGLFunctions_2_0::glRasterPos3sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_014glRasterPos3svEPKs(
    QOpenGLFunctions_2_0 *self,
    const GLshort *v) {
  self->glRasterPos3sv(v);
}

//  void QOpenGLFunctions_2_0::glRasterPos3s(GLshort x, GLshort y, GLshort z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glRasterPos3sEsss(
    QOpenGLFunctions_2_0 *self,
    GLshort x,
    GLshort y,
    GLshort z) {
  self->glRasterPos3s(x, y, z);
}

//  void QOpenGLFunctions_2_0::glRasterPos3iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_014glRasterPos3ivEPKi(
    QOpenGLFunctions_2_0 *self,
    const GLint *v) {
  self->glRasterPos3iv(v);
}

//  void QOpenGLFunctions_2_0::glRasterPos3i(GLint x, GLint y, GLint z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glRasterPos3iEiii(
    QOpenGLFunctions_2_0 *self,
    GLint x,
    GLint y,
    GLint z) {
  self->glRasterPos3i(x, y, z);
}

//  void QOpenGLFunctions_2_0::glRasterPos3fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_014glRasterPos3fvEPKf(
    QOpenGLFunctions_2_0 *self,
    const GLfloat *v) {
  self->glRasterPos3fv(v);
}

//  void QOpenGLFunctions_2_0::glRasterPos3f(GLfloat x, GLfloat y, GLfloat z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glRasterPos3fEfff(
    QOpenGLFunctions_2_0 *self,
    GLfloat x,
    GLfloat y,
    GLfloat z) {
  self->glRasterPos3f(x, y, z);
}

//  void QOpenGLFunctions_2_0::glRasterPos3dv(const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_014glRasterPos3dvEPKd(
    QOpenGLFunctions_2_0 *self,
    const GLdouble *v) {
  self->glRasterPos3dv(v);
}

//  void QOpenGLFunctions_2_0::glRasterPos3d(GLdouble x, GLdouble y, GLdouble
//      z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glRasterPos3dEddd(
    QOpenGLFunctions_2_0 *self,
    GLdouble x,
    GLdouble y,
    GLdouble z) {
  self->glRasterPos3d(x, y, z);
}

//  void QOpenGLFunctions_2_0::glRasterPos2sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_014glRasterPos2svEPKs(
    QOpenGLFunctions_2_0 *self,
    const GLshort *v) {
  self->glRasterPos2sv(v);
}

//  void QOpenGLFunctions_2_0::glRasterPos2s(GLshort x, GLshort y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glRasterPos2sEss(
    QOpenGLFunctions_2_0 *self,
    GLshort x,
    GLshort y) {
  self->glRasterPos2s(x, y);
}

//  void QOpenGLFunctions_2_0::glRasterPos2iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_014glRasterPos2ivEPKi(
    QOpenGLFunctions_2_0 *self,
    const GLint *v) {
  self->glRasterPos2iv(v);
}

//  void QOpenGLFunctions_2_0::glRasterPos2i(GLint x, GLint y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glRasterPos2iEii(
    QOpenGLFunctions_2_0 *self,
    GLint x,
    GLint y) {
  self->glRasterPos2i(x, y);
}

//  void QOpenGLFunctions_2_0::glRasterPos2fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_014glRasterPos2fvEPKf(
    QOpenGLFunctions_2_0 *self,
    const GLfloat *v) {
  self->glRasterPos2fv(v);
}

//  void QOpenGLFunctions_2_0::glRasterPos2f(GLfloat x, GLfloat y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glRasterPos2fEff(
    QOpenGLFunctions_2_0 *self,
    GLfloat x,
    GLfloat y) {
  self->glRasterPos2f(x, y);
}

//  void QOpenGLFunctions_2_0::glRasterPos2dv(const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_014glRasterPos2dvEPKd(
    QOpenGLFunctions_2_0 *self,
    const GLdouble *v) {
  self->glRasterPos2dv(v);
}

//  void QOpenGLFunctions_2_0::glRasterPos2d(GLdouble x, GLdouble y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glRasterPos2dEdd(
    QOpenGLFunctions_2_0 *self,
    GLdouble x,
    GLdouble y) {
  self->glRasterPos2d(x, y);
}

//  void QOpenGLFunctions_2_0::glNormal3sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_011glNormal3svEPKs(
    QOpenGLFunctions_2_0 *self,
    const GLshort *v) {
  self->glNormal3sv(v);
}

//  void QOpenGLFunctions_2_0::glNormal3s(GLshort nx, GLshort ny, GLshort nz)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_010glNormal3sEsss(
    QOpenGLFunctions_2_0 *self,
    GLshort nx,
    GLshort ny,
    GLshort nz) {
  self->glNormal3s(nx, ny, nz);
}

//  void QOpenGLFunctions_2_0::glNormal3iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_011glNormal3ivEPKi(
    QOpenGLFunctions_2_0 *self,
    const GLint *v) {
  self->glNormal3iv(v);
}

//  void QOpenGLFunctions_2_0::glNormal3i(GLint nx, GLint ny, GLint nz)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_010glNormal3iEiii(
    QOpenGLFunctions_2_0 *self,
    GLint nx,
    GLint ny,
    GLint nz) {
  self->glNormal3i(nx, ny, nz);
}

//  void QOpenGLFunctions_2_0::glNormal3fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_011glNormal3fvEPKf(
    QOpenGLFunctions_2_0 *self,
    const GLfloat *v) {
  self->glNormal3fv(v);
}

//  void QOpenGLFunctions_2_0::glNormal3f(GLfloat nx, GLfloat ny, GLfloat nz)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_010glNormal3fEfff(
    QOpenGLFunctions_2_0 *self,
    GLfloat nx,
    GLfloat ny,
    GLfloat nz) {
  self->glNormal3f(nx, ny, nz);
}

//  void QOpenGLFunctions_2_0::glNormal3dv(const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_011glNormal3dvEPKd(
    QOpenGLFunctions_2_0 *self,
    const GLdouble *v) {
  self->glNormal3dv(v);
}

//  void QOpenGLFunctions_2_0::glNormal3d(GLdouble nx, GLdouble ny, GLdouble
//      nz)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_010glNormal3dEddd(
    QOpenGLFunctions_2_0 *self,
    GLdouble nx,
    GLdouble ny,
    GLdouble nz) {
  self->glNormal3d(nx, ny, nz);
}

//  void QOpenGLFunctions_2_0::glNormal3bv(const GLbyte *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_011glNormal3bvEPKa(
    QOpenGLFunctions_2_0 *self,
    const GLbyte *v) {
  self->glNormal3bv(v);
}

//  void QOpenGLFunctions_2_0::glNormal3b(GLbyte nx, GLbyte ny, GLbyte nz)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_010glNormal3bEaaa(
    QOpenGLFunctions_2_0 *self,
    GLbyte nx,
    GLbyte ny,
    GLbyte nz) {
  self->glNormal3b(nx, ny, nz);
}

//  void QOpenGLFunctions_2_0::glIndexsv(const GLshort *c)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_09glIndexsvEPKs(
    QOpenGLFunctions_2_0 *self,
    const GLshort *c) {
  self->glIndexsv(c);
}

//  void QOpenGLFunctions_2_0::glIndexs(GLshort c)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_08glIndexsEs(
    QOpenGLFunctions_2_0 *self,
    GLshort c) {
  self->glIndexs(c);
}

//  void QOpenGLFunctions_2_0::glIndexiv(const GLint *c)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_09glIndexivEPKi(
    QOpenGLFunctions_2_0 *self,
    const GLint *c) {
  self->glIndexiv(c);
}

//  void QOpenGLFunctions_2_0::glIndexi(GLint c)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_08glIndexiEi(
    QOpenGLFunctions_2_0 *self,
    GLint c) {
  self->glIndexi(c);
}

//  void QOpenGLFunctions_2_0::glIndexfv(const GLfloat *c)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_09glIndexfvEPKf(
    QOpenGLFunctions_2_0 *self,
    const GLfloat *c) {
  self->glIndexfv(c);
}

//  void QOpenGLFunctions_2_0::glIndexf(GLfloat c)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_08glIndexfEf(
    QOpenGLFunctions_2_0 *self,
    GLfloat c) {
  self->glIndexf(c);
}

//  void QOpenGLFunctions_2_0::glIndexdv(const GLdouble *c)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_09glIndexdvEPKd(
    QOpenGLFunctions_2_0 *self,
    const GLdouble *c) {
  self->glIndexdv(c);
}

//  void QOpenGLFunctions_2_0::glIndexd(GLdouble c)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_08glIndexdEd(
    QOpenGLFunctions_2_0 *self,
    GLdouble c) {
  self->glIndexd(c);
}

//  void QOpenGLFunctions_2_0::glEnd()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_05glEndEv(QOpenGLFunctions_2_0 *self) {
  self->glEnd();
}

//  void QOpenGLFunctions_2_0::glEdgeFlagv(const GLboolean *flag)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_011glEdgeFlagvEPKh(
    QOpenGLFunctions_2_0 *self,
    const GLboolean *flag) {
  self->glEdgeFlagv(flag);
}

//  void QOpenGLFunctions_2_0::glEdgeFlag(GLboolean flag)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_010glEdgeFlagEh(
    QOpenGLFunctions_2_0 *self,
    GLboolean flag) {
  self->glEdgeFlag(flag);
}

//  void QOpenGLFunctions_2_0::glColor4usv(const GLushort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_011glColor4usvEPKt(
    QOpenGLFunctions_2_0 *self,
    const GLushort *v) {
  self->glColor4usv(v);
}

//  void QOpenGLFunctions_2_0::glColor4us(GLushort red, GLushort green,
//      GLushort blue, GLushort alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_010glColor4usEtttt(
    QOpenGLFunctions_2_0 *self,
    GLushort red,
    GLushort green,
    GLushort blue,
    GLushort alpha) {
  self->glColor4us(red, green, blue, alpha);
}

//  void QOpenGLFunctions_2_0::glColor4uiv(const GLuint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_011glColor4uivEPKj(
    QOpenGLFunctions_2_0 *self,
    const GLuint *v) {
  self->glColor4uiv(v);
}

//  void QOpenGLFunctions_2_0::glColor4ui(GLuint red, GLuint green, GLuint
//      blue, GLuint alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_010glColor4uiEjjjj(
    QOpenGLFunctions_2_0 *self,
    GLuint red,
    GLuint green,
    GLuint blue,
    GLuint alpha) {
  self->glColor4ui(red, green, blue, alpha);
}

//  void QOpenGLFunctions_2_0::glColor4ubv(const GLubyte *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_011glColor4ubvEPKh(
    QOpenGLFunctions_2_0 *self,
    const GLubyte *v) {
  self->glColor4ubv(v);
}

//  void QOpenGLFunctions_2_0::glColor4ub(GLubyte red, GLubyte green, GLubyte
//      blue, GLubyte alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_010glColor4ubEhhhh(
    QOpenGLFunctions_2_0 *self,
    GLubyte red,
    GLubyte green,
    GLubyte blue,
    GLubyte alpha) {
  self->glColor4ub(red, green, blue, alpha);
}

//  void QOpenGLFunctions_2_0::glColor4sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_010glColor4svEPKs(
    QOpenGLFunctions_2_0 *self,
    const GLshort *v) {
  self->glColor4sv(v);
}

//  void QOpenGLFunctions_2_0::glColor4s(GLshort red, GLshort green, GLshort
//      blue, GLshort alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_09glColor4sEssss(
    QOpenGLFunctions_2_0 *self,
    GLshort red,
    GLshort green,
    GLshort blue,
    GLshort alpha) {
  self->glColor4s(red, green, blue, alpha);
}

//  void QOpenGLFunctions_2_0::glColor4iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_010glColor4ivEPKi(
    QOpenGLFunctions_2_0 *self,
    const GLint *v) {
  self->glColor4iv(v);
}

//  void QOpenGLFunctions_2_0::glColor4i(GLint red, GLint green, GLint blue,
//      GLint alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_09glColor4iEiiii(
    QOpenGLFunctions_2_0 *self,
    GLint red,
    GLint green,
    GLint blue,
    GLint alpha) {
  self->glColor4i(red, green, blue, alpha);
}

//  void QOpenGLFunctions_2_0::glColor4fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_010glColor4fvEPKf(
    QOpenGLFunctions_2_0 *self,
    const GLfloat *v) {
  self->glColor4fv(v);
}

//  void QOpenGLFunctions_2_0::glColor4f(GLfloat red, GLfloat green, GLfloat
//      blue, GLfloat alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_09glColor4fEffff(
    QOpenGLFunctions_2_0 *self,
    GLfloat red,
    GLfloat green,
    GLfloat blue,
    GLfloat alpha) {
  self->glColor4f(red, green, blue, alpha);
}

//  void QOpenGLFunctions_2_0::glColor4dv(const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_010glColor4dvEPKd(
    QOpenGLFunctions_2_0 *self,
    const GLdouble *v) {
  self->glColor4dv(v);
}

//  void QOpenGLFunctions_2_0::glColor4d(GLdouble red, GLdouble green,
//      GLdouble blue, GLdouble alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_09glColor4dEdddd(
    QOpenGLFunctions_2_0 *self,
    GLdouble red,
    GLdouble green,
    GLdouble blue,
    GLdouble alpha) {
  self->glColor4d(red, green, blue, alpha);
}

//  void QOpenGLFunctions_2_0::glColor4bv(const GLbyte *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_010glColor4bvEPKa(
    QOpenGLFunctions_2_0 *self,
    const GLbyte *v) {
  self->glColor4bv(v);
}

//  void QOpenGLFunctions_2_0::glColor4b(GLbyte red, GLbyte green, GLbyte
//      blue, GLbyte alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_09glColor4bEaaaa(
    QOpenGLFunctions_2_0 *self,
    GLbyte red,
    GLbyte green,
    GLbyte blue,
    GLbyte alpha) {
  self->glColor4b(red, green, blue, alpha);
}

//  void QOpenGLFunctions_2_0::glColor3usv(const GLushort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_011glColor3usvEPKt(
    QOpenGLFunctions_2_0 *self,
    const GLushort *v) {
  self->glColor3usv(v);
}

//  void QOpenGLFunctions_2_0::glColor3us(GLushort red, GLushort green,
//      GLushort blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_010glColor3usEttt(
    QOpenGLFunctions_2_0 *self,
    GLushort red,
    GLushort green,
    GLushort blue) {
  self->glColor3us(red, green, blue);
}

//  void QOpenGLFunctions_2_0::glColor3uiv(const GLuint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_011glColor3uivEPKj(
    QOpenGLFunctions_2_0 *self,
    const GLuint *v) {
  self->glColor3uiv(v);
}

//  void QOpenGLFunctions_2_0::glColor3ui(GLuint red, GLuint green, GLuint
//      blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_010glColor3uiEjjj(
    QOpenGLFunctions_2_0 *self,
    GLuint red,
    GLuint green,
    GLuint blue) {
  self->glColor3ui(red, green, blue);
}

//  void QOpenGLFunctions_2_0::glColor3ubv(const GLubyte *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_011glColor3ubvEPKh(
    QOpenGLFunctions_2_0 *self,
    const GLubyte *v) {
  self->glColor3ubv(v);
}

//  void QOpenGLFunctions_2_0::glColor3ub(GLubyte red, GLubyte green, GLubyte
//      blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_010glColor3ubEhhh(
    QOpenGLFunctions_2_0 *self,
    GLubyte red,
    GLubyte green,
    GLubyte blue) {
  self->glColor3ub(red, green, blue);
}

//  void QOpenGLFunctions_2_0::glColor3sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_010glColor3svEPKs(
    QOpenGLFunctions_2_0 *self,
    const GLshort *v) {
  self->glColor3sv(v);
}

//  void QOpenGLFunctions_2_0::glColor3s(GLshort red, GLshort green, GLshort
//      blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_09glColor3sEsss(
    QOpenGLFunctions_2_0 *self,
    GLshort red,
    GLshort green,
    GLshort blue) {
  self->glColor3s(red, green, blue);
}

//  void QOpenGLFunctions_2_0::glColor3iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_010glColor3ivEPKi(
    QOpenGLFunctions_2_0 *self,
    const GLint *v) {
  self->glColor3iv(v);
}

//  void QOpenGLFunctions_2_0::glColor3i(GLint red, GLint green, GLint blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_09glColor3iEiii(
    QOpenGLFunctions_2_0 *self,
    GLint red,
    GLint green,
    GLint blue) {
  self->glColor3i(red, green, blue);
}

//  void QOpenGLFunctions_2_0::glColor3fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_010glColor3fvEPKf(
    QOpenGLFunctions_2_0 *self,
    const GLfloat *v) {
  self->glColor3fv(v);
}

//  void QOpenGLFunctions_2_0::glColor3f(GLfloat red, GLfloat green, GLfloat
//      blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_09glColor3fEfff(
    QOpenGLFunctions_2_0 *self,
    GLfloat red,
    GLfloat green,
    GLfloat blue) {
  self->glColor3f(red, green, blue);
}

//  void QOpenGLFunctions_2_0::glColor3dv(const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_010glColor3dvEPKd(
    QOpenGLFunctions_2_0 *self,
    const GLdouble *v) {
  self->glColor3dv(v);
}

//  void QOpenGLFunctions_2_0::glColor3d(GLdouble red, GLdouble green,
//      GLdouble blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_09glColor3dEddd(
    QOpenGLFunctions_2_0 *self,
    GLdouble red,
    GLdouble green,
    GLdouble blue) {
  self->glColor3d(red, green, blue);
}

//  void QOpenGLFunctions_2_0::glColor3bv(const GLbyte *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_010glColor3bvEPKa(
    QOpenGLFunctions_2_0 *self,
    const GLbyte *v) {
  self->glColor3bv(v);
}

//  void QOpenGLFunctions_2_0::glColor3b(GLbyte red, GLbyte green, GLbyte
//      blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_09glColor3bEaaa(
    QOpenGLFunctions_2_0 *self,
    GLbyte red,
    GLbyte green,
    GLbyte blue) {
  self->glColor3b(red, green, blue);
}

//  void QOpenGLFunctions_2_0::glBitmap(GLsizei width, GLsizei height,
//      GLfloat xorig, GLfloat yorig, GLfloat xmove, GLfloat ymove, const
//      GLubyte *bitmap)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_08glBitmapEiiffffPKh(
    QOpenGLFunctions_2_0 *self,
    GLsizei width,
    GLsizei height,
    GLfloat xorig,
    GLfloat yorig,
    GLfloat xmove,
    GLfloat ymove,
    const GLubyte *bitmap) {
  self->glBitmap(width, height, xorig, yorig, xmove, ymove, bitmap);
}

//  void QOpenGLFunctions_2_0::glBegin(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_07glBeginEj(
    QOpenGLFunctions_2_0 *self,
    GLenum mode) {
  self->glBegin(mode);
}

//  void QOpenGLFunctions_2_0::glListBase(GLuint base)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_010glListBaseEj(
    QOpenGLFunctions_2_0 *self,
    GLuint base) {
  self->glListBase(base);
}

//  GLuint QOpenGLFunctions_2_0::glGenLists(GLsizei range)
extern "C" Q_DECL_EXPORT
GLuint ritual_ZN20QOpenGLFunctions_2_010glGenListsEi(
    QOpenGLFunctions_2_0 *self,
    GLsizei range) {
  return self->glGenLists(range);
}

//  void QOpenGLFunctions_2_0::glDeleteLists(GLuint list, GLsizei range)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glDeleteListsEji(
    QOpenGLFunctions_2_0 *self,
    GLuint list,
    GLsizei range) {
  self->glDeleteLists(list, range);
}

//  void QOpenGLFunctions_2_0::glCallLists(GLsizei n, GLenum type, const
//      GLvoid *lists)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_011glCallListsEijPKv(
    QOpenGLFunctions_2_0 *self,
    GLsizei n,
    GLenum type,
    const GLvoid *lists) {
  self->glCallLists(n, type, lists);
}

//  void QOpenGLFunctions_2_0::glCallList(GLuint list)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_010glCallListEj(
    QOpenGLFunctions_2_0 *self,
    GLuint list) {
  self->glCallList(list);
}

//  void QOpenGLFunctions_2_0::glEndList()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_09glEndListEv(
    QOpenGLFunctions_2_0 *self) {
  self->glEndList();
}

//  void QOpenGLFunctions_2_0::glNewList(GLuint list, GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_09glNewListEjj(
    QOpenGLFunctions_2_0 *self,
    GLuint list,
    GLenum mode) {
  self->glNewList(list, mode);
}

//  void QOpenGLFunctions_2_0::glPushClientAttrib(GLbitfield mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_018glPushClientAttribEj(
    QOpenGLFunctions_2_0 *self,
    GLbitfield mask) {
  self->glPushClientAttrib(mask);
}

//  void QOpenGLFunctions_2_0::glPopClientAttrib()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_017glPopClientAttribEv(
    QOpenGLFunctions_2_0 *self) {
  self->glPopClientAttrib();
}

//  void QOpenGLFunctions_2_0::glPrioritizeTextures(GLsizei n, const GLuint
//      *textures, const GLfloat *priorities)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_020glPrioritizeTexturesEiPKjPKf(
    QOpenGLFunctions_2_0 *self,
    GLsizei n,
    const GLuint *textures,
    const GLfloat *priorities) {
  self->glPrioritizeTextures(n, textures, priorities);
}

//  GLboolean QOpenGLFunctions_2_0::glAreTexturesResident(GLsizei n, const
//      GLuint *textures, GLboolean *residences)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN20QOpenGLFunctions_2_021glAreTexturesResidentEiPKjPh(
    QOpenGLFunctions_2_0 *self,
    GLsizei n,
    const GLuint *textures,
    GLboolean *residences) {
  return self->glAreTexturesResident(n, textures, residences);
}

//  void QOpenGLFunctions_2_0::glVertexPointer(GLint size, GLenum type,
//      GLsizei stride, const GLvoid *pointer)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_015glVertexPointerEijiPKv(
    QOpenGLFunctions_2_0 *self,
    GLint size,
    GLenum type,
    GLsizei stride,
    const GLvoid *pointer) {
  self->glVertexPointer(size, type, stride, pointer);
}

//  void QOpenGLFunctions_2_0::glTexCoordPointer(GLint size, GLenum type,
//      GLsizei stride, const GLvoid *pointer)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_017glTexCoordPointerEijiPKv(
    QOpenGLFunctions_2_0 *self,
    GLint size,
    GLenum type,
    GLsizei stride,
    const GLvoid *pointer) {
  self->glTexCoordPointer(size, type, stride, pointer);
}

//  void QOpenGLFunctions_2_0::glNormalPointer(GLenum type, GLsizei stride,
//      const GLvoid *pointer)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_015glNormalPointerEjiPKv(
    QOpenGLFunctions_2_0 *self,
    GLenum type,
    GLsizei stride,
    const GLvoid *pointer) {
  self->glNormalPointer(type, stride, pointer);
}

//  void QOpenGLFunctions_2_0::glInterleavedArrays(GLenum format, GLsizei
//      stride, const GLvoid *pointer)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_019glInterleavedArraysEjiPKv(
    QOpenGLFunctions_2_0 *self,
    GLenum format,
    GLsizei stride,
    const GLvoid *pointer) {
  self->glInterleavedArrays(format, stride, pointer);
}

//  void QOpenGLFunctions_2_0::glIndexPointer(GLenum type, GLsizei stride,
//      const GLvoid *pointer)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_014glIndexPointerEjiPKv(
    QOpenGLFunctions_2_0 *self,
    GLenum type,
    GLsizei stride,
    const GLvoid *pointer) {
  self->glIndexPointer(type, stride, pointer);
}

//  void QOpenGLFunctions_2_0::glEnableClientState(GLenum array)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_019glEnableClientStateEj(
    QOpenGLFunctions_2_0 *self,
    GLenum array) {
  self->glEnableClientState(array);
}

//  void QOpenGLFunctions_2_0::glEdgeFlagPointer(GLsizei stride, const GLvoid
//      *pointer)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_017glEdgeFlagPointerEiPKv(
    QOpenGLFunctions_2_0 *self,
    GLsizei stride,
    const GLvoid *pointer) {
  self->glEdgeFlagPointer(stride, pointer);
}

//  void QOpenGLFunctions_2_0::glDisableClientState(GLenum array)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_020glDisableClientStateEj(
    QOpenGLFunctions_2_0 *self,
    GLenum array) {
  self->glDisableClientState(array);
}

//  void QOpenGLFunctions_2_0::glColorPointer(GLint size, GLenum type,
//      GLsizei stride, const GLvoid *pointer)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_014glColorPointerEijiPKv(
    QOpenGLFunctions_2_0 *self,
    GLint size,
    GLenum type,
    GLsizei stride,
    const GLvoid *pointer) {
  self->glColorPointer(size, type, stride, pointer);
}

//  void QOpenGLFunctions_2_0::glArrayElement(GLint i)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_014glArrayElementEi(
    QOpenGLFunctions_2_0 *self,
    GLint i) {
  self->glArrayElement(i);
}

//  void QOpenGLFunctions_2_0::glResetMinmax(GLenum target)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glResetMinmaxEj(
    QOpenGLFunctions_2_0 *self,
    GLenum target) {
  self->glResetMinmax(target);
}

//  void QOpenGLFunctions_2_0::glResetHistogram(GLenum target)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_016glResetHistogramEj(
    QOpenGLFunctions_2_0 *self,
    GLenum target) {
  self->glResetHistogram(target);
}

//  void QOpenGLFunctions_2_0::glMinmax(GLenum target, GLenum internalformat,
//      GLboolean sink)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_08glMinmaxEjjh(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLenum internalformat,
    GLboolean sink) {
  self->glMinmax(target, internalformat, sink);
}

//  void QOpenGLFunctions_2_0::glHistogram(GLenum target, GLsizei width,
//      GLenum internalformat, GLboolean sink)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_011glHistogramEjijh(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLsizei width,
    GLenum internalformat,
    GLboolean sink) {
  self->glHistogram(target, width, internalformat, sink);
}

//  void QOpenGLFunctions_2_0::glGetMinmaxParameteriv(GLenum target, GLenum
//      pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_022glGetMinmaxParameterivEjjPi(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLenum pname,
    GLint *params) {
  self->glGetMinmaxParameteriv(target, pname, params);
}

//  void QOpenGLFunctions_2_0::glGetMinmaxParameterfv(GLenum target, GLenum
//      pname, GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_022glGetMinmaxParameterfvEjjPf(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLenum pname,
    GLfloat *params) {
  self->glGetMinmaxParameterfv(target, pname, params);
}

//  void QOpenGLFunctions_2_0::glGetMinmax(GLenum target, GLboolean reset,
//      GLenum format, GLenum type, GLvoid *values)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_011glGetMinmaxEjhjjPv(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLboolean reset,
    GLenum format,
    GLenum type,
    GLvoid *values) {
  self->glGetMinmax(target, reset, format, type, values);
}

//  void QOpenGLFunctions_2_0::glGetHistogramParameteriv(GLenum target,
//      GLenum pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_025glGetHistogramParameterivEjjPi(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLenum pname,
    GLint *params) {
  self->glGetHistogramParameteriv(target, pname, params);
}

//  void QOpenGLFunctions_2_0::glGetHistogramParameterfv(GLenum target,
//      GLenum pname, GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_025glGetHistogramParameterfvEjjPf(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLenum pname,
    GLfloat *params) {
  self->glGetHistogramParameterfv(target, pname, params);
}

//  void QOpenGLFunctions_2_0::glGetHistogram(GLenum target, GLboolean reset,
//      GLenum format, GLenum type, GLvoid *values)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_014glGetHistogramEjhjjPv(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLboolean reset,
    GLenum format,
    GLenum type,
    GLvoid *values) {
  self->glGetHistogram(target, reset, format, type, values);
}

//  void QOpenGLFunctions_2_0::glSeparableFilter2D(GLenum target, GLenum
//      internalformat, GLsizei width, GLsizei height, GLenum format, GLenum
//      type, const GLvoid *row, const GLvoid *column)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_019glSeparableFilter2DEjjiijjPKvS1_(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLenum internalformat,
    GLsizei width,
    GLsizei height,
    GLenum format,
    GLenum type,
    const GLvoid *row,
    const GLvoid *column) {
  self->glSeparableFilter2D(
      target,
      internalformat,
      width,
      height,
      format,
      type,
      row,
      column);
}

//  void QOpenGLFunctions_2_0::glGetSeparableFilter(GLenum target, GLenum
//      format, GLenum type, GLvoid *row, GLvoid *column, GLvoid *span)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_020glGetSeparableFilterEjjjPvS0_S0_(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLenum format,
    GLenum type,
    GLvoid *row,
    GLvoid *column,
    GLvoid *span) {
  self->glGetSeparableFilter(target, format, type, row, column, span);
}

//  void QOpenGLFunctions_2_0::glGetConvolutionParameteriv(GLenum target,
//      GLenum pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_027glGetConvolutionParameterivEjjPi(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLenum pname,
    GLint *params) {
  self->glGetConvolutionParameteriv(target, pname, params);
}

//  void QOpenGLFunctions_2_0::glGetConvolutionParameterfv(GLenum target,
//      GLenum pname, GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_027glGetConvolutionParameterfvEjjPf(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLenum pname,
    GLfloat *params) {
  self->glGetConvolutionParameterfv(target, pname, params);
}

//  void QOpenGLFunctions_2_0::glGetConvolutionFilter(GLenum target, GLenum
//      format, GLenum type, GLvoid *image)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_022glGetConvolutionFilterEjjjPv(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLenum format,
    GLenum type,
    GLvoid *image) {
  self->glGetConvolutionFilter(target, format, type, image);
}

//  void QOpenGLFunctions_2_0::glCopyConvolutionFilter2D(GLenum target,
//      GLenum internalformat, GLint x, GLint y, GLsizei width, GLsizei
//      height)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_025glCopyConvolutionFilter2DEjjiiii(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLenum internalformat,
    GLint x,
    GLint y,
    GLsizei width,
    GLsizei height) {
  self->glCopyConvolutionFilter2D(
      target,
      internalformat,
      x,
      y,
      width,
      height);
}

//  void QOpenGLFunctions_2_0::glCopyConvolutionFilter1D(GLenum target,
//      GLenum internalformat, GLint x, GLint y, GLsizei width)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_025glCopyConvolutionFilter1DEjjiii(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLenum internalformat,
    GLint x,
    GLint y,
    GLsizei width) {
  self->glCopyConvolutionFilter1D(target, internalformat, x, y, width);
}

//  void QOpenGLFunctions_2_0::glConvolutionParameteriv(GLenum target, GLenum
//      pname, const GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_024glConvolutionParameterivEjjPKi(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLenum pname,
    const GLint *params) {
  self->glConvolutionParameteriv(target, pname, params);
}

//  void QOpenGLFunctions_2_0::glConvolutionParameteri(GLenum target, GLenum
//      pname, GLint params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_023glConvolutionParameteriEjji(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLenum pname,
    GLint params) {
  self->glConvolutionParameteri(target, pname, params);
}

//  void QOpenGLFunctions_2_0::glConvolutionParameterfv(GLenum target, GLenum
//      pname, const GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_024glConvolutionParameterfvEjjPKf(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLenum pname,
    const GLfloat *params) {
  self->glConvolutionParameterfv(target, pname, params);
}

//  void QOpenGLFunctions_2_0::glConvolutionParameterf(GLenum target, GLenum
//      pname, GLfloat params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_023glConvolutionParameterfEjjf(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLenum pname,
    GLfloat params) {
  self->glConvolutionParameterf(target, pname, params);
}

//  void QOpenGLFunctions_2_0::glConvolutionFilter2D(GLenum target, GLenum
//      internalformat, GLsizei width, GLsizei height, GLenum format, GLenum
//      type, const GLvoid *image)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_021glConvolutionFilter2DEjjiijjPKv(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLenum internalformat,
    GLsizei width,
    GLsizei height,
    GLenum format,
    GLenum type,
    const GLvoid *image) {
  self->glConvolutionFilter2D(
      target,
      internalformat,
      width,
      height,
      format,
      type,
      image);
}

//  void QOpenGLFunctions_2_0::glConvolutionFilter1D(GLenum target, GLenum
//      internalformat, GLsizei width, GLenum format, GLenum type, const
//      GLvoid *image)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_021glConvolutionFilter1DEjjijjPKv(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLenum internalformat,
    GLsizei width,
    GLenum format,
    GLenum type,
    const GLvoid *image) {
  self->glConvolutionFilter1D(
      target,
      internalformat,
      width,
      format,
      type,
      image);
}

//  void QOpenGLFunctions_2_0::glCopyColorSubTable(GLenum target, GLsizei
//      start, GLint x, GLint y, GLsizei width)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_019glCopyColorSubTableEjiiii(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLsizei start,
    GLint x,
    GLint y,
    GLsizei width) {
  self->glCopyColorSubTable(target, start, x, y, width);
}

//  void QOpenGLFunctions_2_0::glColorSubTable(GLenum target, GLsizei start,
//      GLsizei count, GLenum format, GLenum type, const GLvoid *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_015glColorSubTableEjiijjPKv(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLsizei start,
    GLsizei count,
    GLenum format,
    GLenum type,
    const GLvoid *data) {
  self->glColorSubTable(target, start, count, format, type, data);
}

//  void QOpenGLFunctions_2_0::glGetColorTableParameteriv(GLenum target,
//      GLenum pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_026glGetColorTableParameterivEjjPi(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLenum pname,
    GLint *params) {
  self->glGetColorTableParameteriv(target, pname, params);
}

//  void QOpenGLFunctions_2_0::glGetColorTableParameterfv(GLenum target,
//      GLenum pname, GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_026glGetColorTableParameterfvEjjPf(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLenum pname,
    GLfloat *params) {
  self->glGetColorTableParameterfv(target, pname, params);
}

//  void QOpenGLFunctions_2_0::glGetColorTable(GLenum target, GLenum format,
//      GLenum type, GLvoid *table)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_015glGetColorTableEjjjPv(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLenum format,
    GLenum type,
    GLvoid *table) {
  self->glGetColorTable(target, format, type, table);
}

//  void QOpenGLFunctions_2_0::glCopyColorTable(GLenum target, GLenum
//      internalformat, GLint x, GLint y, GLsizei width)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_016glCopyColorTableEjjiii(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLenum internalformat,
    GLint x,
    GLint y,
    GLsizei width) {
  self->glCopyColorTable(target, internalformat, x, y, width);
}

//  void QOpenGLFunctions_2_0::glColorTableParameteriv(GLenum target, GLenum
//      pname, const GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_023glColorTableParameterivEjjPKi(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLenum pname,
    const GLint *params) {
  self->glColorTableParameteriv(target, pname, params);
}

//  void QOpenGLFunctions_2_0::glColorTableParameterfv(GLenum target, GLenum
//      pname, const GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_023glColorTableParameterfvEjjPKf(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLenum pname,
    const GLfloat *params) {
  self->glColorTableParameterfv(target, pname, params);
}

//  void QOpenGLFunctions_2_0::glColorTable(GLenum target, GLenum
//      internalformat, GLsizei width, GLenum format, GLenum type, const
//      GLvoid *table)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glColorTableEjjijjPKv(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLenum internalformat,
    GLsizei width,
    GLenum format,
    GLenum type,
    const GLvoid *table) {
  self->glColorTable(target, internalformat, width, format, type, table);
}

//  void QOpenGLFunctions_2_0::glMultTransposeMatrixd(const GLdouble *m)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_022glMultTransposeMatrixdEPKd(
    QOpenGLFunctions_2_0 *self,
    const GLdouble *m) {
  self->glMultTransposeMatrixd(m);
}

//  void QOpenGLFunctions_2_0::glMultTransposeMatrixf(const GLfloat *m)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_022glMultTransposeMatrixfEPKf(
    QOpenGLFunctions_2_0 *self,
    const GLfloat *m) {
  self->glMultTransposeMatrixf(m);
}

//  void QOpenGLFunctions_2_0::glLoadTransposeMatrixd(const GLdouble *m)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_022glLoadTransposeMatrixdEPKd(
    QOpenGLFunctions_2_0 *self,
    const GLdouble *m) {
  self->glLoadTransposeMatrixd(m);
}

//  void QOpenGLFunctions_2_0::glLoadTransposeMatrixf(const GLfloat *m)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_022glLoadTransposeMatrixfEPKf(
    QOpenGLFunctions_2_0 *self,
    const GLfloat *m) {
  self->glLoadTransposeMatrixf(m);
}

//  void QOpenGLFunctions_2_0::glMultiTexCoord4sv(GLenum target, const
//      GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_018glMultiTexCoord4svEjPKs(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    const GLshort *v) {
  self->glMultiTexCoord4sv(target, v);
}

//  void QOpenGLFunctions_2_0::glMultiTexCoord4s(GLenum target, GLshort s,
//      GLshort t, GLshort r, GLshort q)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_017glMultiTexCoord4sEjssss(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLshort s,
    GLshort t,
    GLshort r,
    GLshort q) {
  self->glMultiTexCoord4s(target, s, t, r, q);
}

//  void QOpenGLFunctions_2_0::glMultiTexCoord4iv(GLenum target, const GLint
//      *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_018glMultiTexCoord4ivEjPKi(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    const GLint *v) {
  self->glMultiTexCoord4iv(target, v);
}

//  void QOpenGLFunctions_2_0::glMultiTexCoord4i(GLenum target, GLint s,
//      GLint t, GLint r, GLint q)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_017glMultiTexCoord4iEjiiii(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLint s,
    GLint t,
    GLint r,
    GLint q) {
  self->glMultiTexCoord4i(target, s, t, r, q);
}

//  void QOpenGLFunctions_2_0::glMultiTexCoord4fv(GLenum target, const
//      GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_018glMultiTexCoord4fvEjPKf(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    const GLfloat *v) {
  self->glMultiTexCoord4fv(target, v);
}

//  void QOpenGLFunctions_2_0::glMultiTexCoord4f(GLenum target, GLfloat s,
//      GLfloat t, GLfloat r, GLfloat q)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_017glMultiTexCoord4fEjffff(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLfloat s,
    GLfloat t,
    GLfloat r,
    GLfloat q) {
  self->glMultiTexCoord4f(target, s, t, r, q);
}

//  void QOpenGLFunctions_2_0::glMultiTexCoord4dv(GLenum target, const
//      GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_018glMultiTexCoord4dvEjPKd(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    const GLdouble *v) {
  self->glMultiTexCoord4dv(target, v);
}

//  void QOpenGLFunctions_2_0::glMultiTexCoord4d(GLenum target, GLdouble s,
//      GLdouble t, GLdouble r, GLdouble q)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_017glMultiTexCoord4dEjdddd(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLdouble s,
    GLdouble t,
    GLdouble r,
    GLdouble q) {
  self->glMultiTexCoord4d(target, s, t, r, q);
}

//  void QOpenGLFunctions_2_0::glMultiTexCoord3sv(GLenum target, const
//      GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_018glMultiTexCoord3svEjPKs(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    const GLshort *v) {
  self->glMultiTexCoord3sv(target, v);
}

//  void QOpenGLFunctions_2_0::glMultiTexCoord3s(GLenum target, GLshort s,
//      GLshort t, GLshort r)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_017glMultiTexCoord3sEjsss(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLshort s,
    GLshort t,
    GLshort r) {
  self->glMultiTexCoord3s(target, s, t, r);
}

//  void QOpenGLFunctions_2_0::glMultiTexCoord3iv(GLenum target, const GLint
//      *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_018glMultiTexCoord3ivEjPKi(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    const GLint *v) {
  self->glMultiTexCoord3iv(target, v);
}

//  void QOpenGLFunctions_2_0::glMultiTexCoord3i(GLenum target, GLint s,
//      GLint t, GLint r)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_017glMultiTexCoord3iEjiii(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLint s,
    GLint t,
    GLint r) {
  self->glMultiTexCoord3i(target, s, t, r);
}

//  void QOpenGLFunctions_2_0::glMultiTexCoord3fv(GLenum target, const
//      GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_018glMultiTexCoord3fvEjPKf(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    const GLfloat *v) {
  self->glMultiTexCoord3fv(target, v);
}

//  void QOpenGLFunctions_2_0::glMultiTexCoord3f(GLenum target, GLfloat s,
//      GLfloat t, GLfloat r)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_017glMultiTexCoord3fEjfff(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLfloat s,
    GLfloat t,
    GLfloat r) {
  self->glMultiTexCoord3f(target, s, t, r);
}

//  void QOpenGLFunctions_2_0::glMultiTexCoord3dv(GLenum target, const
//      GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_018glMultiTexCoord3dvEjPKd(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    const GLdouble *v) {
  self->glMultiTexCoord3dv(target, v);
}

//  void QOpenGLFunctions_2_0::glMultiTexCoord3d(GLenum target, GLdouble s,
//      GLdouble t, GLdouble r)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_017glMultiTexCoord3dEjddd(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLdouble s,
    GLdouble t,
    GLdouble r) {
  self->glMultiTexCoord3d(target, s, t, r);
}

//  void QOpenGLFunctions_2_0::glMultiTexCoord2sv(GLenum target, const
//      GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_018glMultiTexCoord2svEjPKs(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    const GLshort *v) {
  self->glMultiTexCoord2sv(target, v);
}

//  void QOpenGLFunctions_2_0::glMultiTexCoord2s(GLenum target, GLshort s,
//      GLshort t)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_017glMultiTexCoord2sEjss(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLshort s,
    GLshort t) {
  self->glMultiTexCoord2s(target, s, t);
}

//  void QOpenGLFunctions_2_0::glMultiTexCoord2iv(GLenum target, const GLint
//      *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_018glMultiTexCoord2ivEjPKi(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    const GLint *v) {
  self->glMultiTexCoord2iv(target, v);
}

//  void QOpenGLFunctions_2_0::glMultiTexCoord2i(GLenum target, GLint s,
//      GLint t)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_017glMultiTexCoord2iEjii(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLint s,
    GLint t) {
  self->glMultiTexCoord2i(target, s, t);
}

//  void QOpenGLFunctions_2_0::glMultiTexCoord2fv(GLenum target, const
//      GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_018glMultiTexCoord2fvEjPKf(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    const GLfloat *v) {
  self->glMultiTexCoord2fv(target, v);
}

//  void QOpenGLFunctions_2_0::glMultiTexCoord2f(GLenum target, GLfloat s,
//      GLfloat t)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_017glMultiTexCoord2fEjff(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLfloat s,
    GLfloat t) {
  self->glMultiTexCoord2f(target, s, t);
}

//  void QOpenGLFunctions_2_0::glMultiTexCoord2dv(GLenum target, const
//      GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_018glMultiTexCoord2dvEjPKd(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    const GLdouble *v) {
  self->glMultiTexCoord2dv(target, v);
}

//  void QOpenGLFunctions_2_0::glMultiTexCoord2d(GLenum target, GLdouble s,
//      GLdouble t)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_017glMultiTexCoord2dEjdd(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLdouble s,
    GLdouble t) {
  self->glMultiTexCoord2d(target, s, t);
}

//  void QOpenGLFunctions_2_0::glMultiTexCoord1sv(GLenum target, const
//      GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_018glMultiTexCoord1svEjPKs(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    const GLshort *v) {
  self->glMultiTexCoord1sv(target, v);
}

//  void QOpenGLFunctions_2_0::glMultiTexCoord1s(GLenum target, GLshort s)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_017glMultiTexCoord1sEjs(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLshort s) {
  self->glMultiTexCoord1s(target, s);
}

//  void QOpenGLFunctions_2_0::glMultiTexCoord1iv(GLenum target, const GLint
//      *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_018glMultiTexCoord1ivEjPKi(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    const GLint *v) {
  self->glMultiTexCoord1iv(target, v);
}

//  void QOpenGLFunctions_2_0::glMultiTexCoord1i(GLenum target, GLint s)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_017glMultiTexCoord1iEji(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLint s) {
  self->glMultiTexCoord1i(target, s);
}

//  void QOpenGLFunctions_2_0::glMultiTexCoord1fv(GLenum target, const
//      GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_018glMultiTexCoord1fvEjPKf(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    const GLfloat *v) {
  self->glMultiTexCoord1fv(target, v);
}

//  void QOpenGLFunctions_2_0::glMultiTexCoord1f(GLenum target, GLfloat s)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_017glMultiTexCoord1fEjf(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLfloat s) {
  self->glMultiTexCoord1f(target, s);
}

//  void QOpenGLFunctions_2_0::glMultiTexCoord1dv(GLenum target, const
//      GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_018glMultiTexCoord1dvEjPKd(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    const GLdouble *v) {
  self->glMultiTexCoord1dv(target, v);
}

//  void QOpenGLFunctions_2_0::glMultiTexCoord1d(GLenum target, GLdouble s)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_017glMultiTexCoord1dEjd(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLdouble s) {
  self->glMultiTexCoord1d(target, s);
}

//  void QOpenGLFunctions_2_0::glClientActiveTexture(GLenum texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_021glClientActiveTextureEj(
    QOpenGLFunctions_2_0 *self,
    GLenum texture) {
  self->glClientActiveTexture(texture);
}

//  void QOpenGLFunctions_2_0::glWindowPos3sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_014glWindowPos3svEPKs(
    QOpenGLFunctions_2_0 *self,
    const GLshort *v) {
  self->glWindowPos3sv(v);
}

//  void QOpenGLFunctions_2_0::glWindowPos3s(GLshort x, GLshort y, GLshort z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glWindowPos3sEsss(
    QOpenGLFunctions_2_0 *self,
    GLshort x,
    GLshort y,
    GLshort z) {
  self->glWindowPos3s(x, y, z);
}

//  void QOpenGLFunctions_2_0::glWindowPos3iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_014glWindowPos3ivEPKi(
    QOpenGLFunctions_2_0 *self,
    const GLint *v) {
  self->glWindowPos3iv(v);
}

//  void QOpenGLFunctions_2_0::glWindowPos3i(GLint x, GLint y, GLint z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glWindowPos3iEiii(
    QOpenGLFunctions_2_0 *self,
    GLint x,
    GLint y,
    GLint z) {
  self->glWindowPos3i(x, y, z);
}

//  void QOpenGLFunctions_2_0::glWindowPos3fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_014glWindowPos3fvEPKf(
    QOpenGLFunctions_2_0 *self,
    const GLfloat *v) {
  self->glWindowPos3fv(v);
}

//  void QOpenGLFunctions_2_0::glWindowPos3f(GLfloat x, GLfloat y, GLfloat z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glWindowPos3fEfff(
    QOpenGLFunctions_2_0 *self,
    GLfloat x,
    GLfloat y,
    GLfloat z) {
  self->glWindowPos3f(x, y, z);
}

//  void QOpenGLFunctions_2_0::glWindowPos3dv(const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_014glWindowPos3dvEPKd(
    QOpenGLFunctions_2_0 *self,
    const GLdouble *v) {
  self->glWindowPos3dv(v);
}

//  void QOpenGLFunctions_2_0::glWindowPos3d(GLdouble x, GLdouble y, GLdouble
//      z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glWindowPos3dEddd(
    QOpenGLFunctions_2_0 *self,
    GLdouble x,
    GLdouble y,
    GLdouble z) {
  self->glWindowPos3d(x, y, z);
}

//  void QOpenGLFunctions_2_0::glWindowPos2sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_014glWindowPos2svEPKs(
    QOpenGLFunctions_2_0 *self,
    const GLshort *v) {
  self->glWindowPos2sv(v);
}

//  void QOpenGLFunctions_2_0::glWindowPos2s(GLshort x, GLshort y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glWindowPos2sEss(
    QOpenGLFunctions_2_0 *self,
    GLshort x,
    GLshort y) {
  self->glWindowPos2s(x, y);
}

//  void QOpenGLFunctions_2_0::glWindowPos2iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_014glWindowPos2ivEPKi(
    QOpenGLFunctions_2_0 *self,
    const GLint *v) {
  self->glWindowPos2iv(v);
}

//  void QOpenGLFunctions_2_0::glWindowPos2i(GLint x, GLint y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glWindowPos2iEii(
    QOpenGLFunctions_2_0 *self,
    GLint x,
    GLint y) {
  self->glWindowPos2i(x, y);
}

//  void QOpenGLFunctions_2_0::glWindowPos2fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_014glWindowPos2fvEPKf(
    QOpenGLFunctions_2_0 *self,
    const GLfloat *v) {
  self->glWindowPos2fv(v);
}

//  void QOpenGLFunctions_2_0::glWindowPos2f(GLfloat x, GLfloat y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glWindowPos2fEff(
    QOpenGLFunctions_2_0 *self,
    GLfloat x,
    GLfloat y) {
  self->glWindowPos2f(x, y);
}

//  void QOpenGLFunctions_2_0::glWindowPos2dv(const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_014glWindowPos2dvEPKd(
    QOpenGLFunctions_2_0 *self,
    const GLdouble *v) {
  self->glWindowPos2dv(v);
}

//  void QOpenGLFunctions_2_0::glWindowPos2d(GLdouble x, GLdouble y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glWindowPos2dEdd(
    QOpenGLFunctions_2_0 *self,
    GLdouble x,
    GLdouble y) {
  self->glWindowPos2d(x, y);
}

//  void QOpenGLFunctions_2_0::glSecondaryColorPointer(GLint size, GLenum
//      type, GLsizei stride, const GLvoid *pointer)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_023glSecondaryColorPointerEijiPKv(
    QOpenGLFunctions_2_0 *self,
    GLint size,
    GLenum type,
    GLsizei stride,
    const GLvoid *pointer) {
  self->glSecondaryColorPointer(size, type, stride, pointer);
}

//  void QOpenGLFunctions_2_0::glSecondaryColor3usv(const GLushort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_020glSecondaryColor3usvEPKt(
    QOpenGLFunctions_2_0 *self,
    const GLushort *v) {
  self->glSecondaryColor3usv(v);
}

//  void QOpenGLFunctions_2_0::glSecondaryColor3us(GLushort red, GLushort
//      green, GLushort blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_019glSecondaryColor3usEttt(
    QOpenGLFunctions_2_0 *self,
    GLushort red,
    GLushort green,
    GLushort blue) {
  self->glSecondaryColor3us(red, green, blue);
}

//  void QOpenGLFunctions_2_0::glSecondaryColor3uiv(const GLuint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_020glSecondaryColor3uivEPKj(
    QOpenGLFunctions_2_0 *self,
    const GLuint *v) {
  self->glSecondaryColor3uiv(v);
}

//  void QOpenGLFunctions_2_0::glSecondaryColor3ui(GLuint red, GLuint green,
//      GLuint blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_019glSecondaryColor3uiEjjj(
    QOpenGLFunctions_2_0 *self,
    GLuint red,
    GLuint green,
    GLuint blue) {
  self->glSecondaryColor3ui(red, green, blue);
}

//  void QOpenGLFunctions_2_0::glSecondaryColor3ubv(const GLubyte *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_020glSecondaryColor3ubvEPKh(
    QOpenGLFunctions_2_0 *self,
    const GLubyte *v) {
  self->glSecondaryColor3ubv(v);
}

//  void QOpenGLFunctions_2_0::glSecondaryColor3ub(GLubyte red, GLubyte
//      green, GLubyte blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_019glSecondaryColor3ubEhhh(
    QOpenGLFunctions_2_0 *self,
    GLubyte red,
    GLubyte green,
    GLubyte blue) {
  self->glSecondaryColor3ub(red, green, blue);
}

//  void QOpenGLFunctions_2_0::glSecondaryColor3sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_019glSecondaryColor3svEPKs(
    QOpenGLFunctions_2_0 *self,
    const GLshort *v) {
  self->glSecondaryColor3sv(v);
}

//  void QOpenGLFunctions_2_0::glSecondaryColor3s(GLshort red, GLshort green,
//      GLshort blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_018glSecondaryColor3sEsss(
    QOpenGLFunctions_2_0 *self,
    GLshort red,
    GLshort green,
    GLshort blue) {
  self->glSecondaryColor3s(red, green, blue);
}

//  void QOpenGLFunctions_2_0::glSecondaryColor3iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_019glSecondaryColor3ivEPKi(
    QOpenGLFunctions_2_0 *self,
    const GLint *v) {
  self->glSecondaryColor3iv(v);
}

//  void QOpenGLFunctions_2_0::glSecondaryColor3i(GLint red, GLint green,
//      GLint blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_018glSecondaryColor3iEiii(
    QOpenGLFunctions_2_0 *self,
    GLint red,
    GLint green,
    GLint blue) {
  self->glSecondaryColor3i(red, green, blue);
}

//  void QOpenGLFunctions_2_0::glSecondaryColor3fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_019glSecondaryColor3fvEPKf(
    QOpenGLFunctions_2_0 *self,
    const GLfloat *v) {
  self->glSecondaryColor3fv(v);
}

//  void QOpenGLFunctions_2_0::glSecondaryColor3f(GLfloat red, GLfloat green,
//      GLfloat blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_018glSecondaryColor3fEfff(
    QOpenGLFunctions_2_0 *self,
    GLfloat red,
    GLfloat green,
    GLfloat blue) {
  self->glSecondaryColor3f(red, green, blue);
}

//  void QOpenGLFunctions_2_0::glSecondaryColor3dv(const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_019glSecondaryColor3dvEPKd(
    QOpenGLFunctions_2_0 *self,
    const GLdouble *v) {
  self->glSecondaryColor3dv(v);
}

//  void QOpenGLFunctions_2_0::glSecondaryColor3d(GLdouble red, GLdouble
//      green, GLdouble blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_018glSecondaryColor3dEddd(
    QOpenGLFunctions_2_0 *self,
    GLdouble red,
    GLdouble green,
    GLdouble blue) {
  self->glSecondaryColor3d(red, green, blue);
}

//  void QOpenGLFunctions_2_0::glSecondaryColor3bv(const GLbyte *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_019glSecondaryColor3bvEPKa(
    QOpenGLFunctions_2_0 *self,
    const GLbyte *v) {
  self->glSecondaryColor3bv(v);
}

//  void QOpenGLFunctions_2_0::glSecondaryColor3b(GLbyte red, GLbyte green,
//      GLbyte blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_018glSecondaryColor3bEaaa(
    QOpenGLFunctions_2_0 *self,
    GLbyte red,
    GLbyte green,
    GLbyte blue) {
  self->glSecondaryColor3b(red, green, blue);
}

//  void QOpenGLFunctions_2_0::glFogCoordPointer(GLenum type, GLsizei stride,
//      const GLvoid *pointer)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_017glFogCoordPointerEjiPKv(
    QOpenGLFunctions_2_0 *self,
    GLenum type,
    GLsizei stride,
    const GLvoid *pointer) {
  self->glFogCoordPointer(type, stride, pointer);
}

//  void QOpenGLFunctions_2_0::glFogCoorddv(const GLdouble *coord)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glFogCoorddvEPKd(
    QOpenGLFunctions_2_0 *self,
    const GLdouble *coord) {
  self->glFogCoorddv(coord);
}

//  void QOpenGLFunctions_2_0::glFogCoordd(GLdouble coord)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_011glFogCoorddEd(
    QOpenGLFunctions_2_0 *self,
    GLdouble coord) {
  self->glFogCoordd(coord);
}

//  void QOpenGLFunctions_2_0::glFogCoordfv(const GLfloat *coord)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glFogCoordfvEPKf(
    QOpenGLFunctions_2_0 *self,
    const GLfloat *coord) {
  self->glFogCoordfv(coord);
}

//  void QOpenGLFunctions_2_0::glFogCoordf(GLfloat coord)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_011glFogCoordfEf(
    QOpenGLFunctions_2_0 *self,
    GLfloat coord) {
  self->glFogCoordf(coord);
}

//  void QOpenGLFunctions_2_0::glVertexAttrib4usv(GLuint index, const
//      GLushort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_018glVertexAttrib4usvEjPKt(
    QOpenGLFunctions_2_0 *self,
    GLuint index,
    const GLushort *v) {
  self->glVertexAttrib4usv(index, v);
}

//  void QOpenGLFunctions_2_0::glVertexAttrib4uiv(GLuint index, const GLuint
//      *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_018glVertexAttrib4uivEjPKj(
    QOpenGLFunctions_2_0 *self,
    GLuint index,
    const GLuint *v) {
  self->glVertexAttrib4uiv(index, v);
}

//  void QOpenGLFunctions_2_0::glVertexAttrib4ubv(GLuint index, const GLubyte
//      *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_018glVertexAttrib4ubvEjPKh(
    QOpenGLFunctions_2_0 *self,
    GLuint index,
    const GLubyte *v) {
  self->glVertexAttrib4ubv(index, v);
}

//  void QOpenGLFunctions_2_0::glVertexAttrib4sv(GLuint index, const GLshort
//      *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_017glVertexAttrib4svEjPKs(
    QOpenGLFunctions_2_0 *self,
    GLuint index,
    const GLshort *v) {
  self->glVertexAttrib4sv(index, v);
}

//  void QOpenGLFunctions_2_0::glVertexAttrib4s(GLuint index, GLshort x,
//      GLshort y, GLshort z, GLshort w)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_016glVertexAttrib4sEjssss(
    QOpenGLFunctions_2_0 *self,
    GLuint index,
    GLshort x,
    GLshort y,
    GLshort z,
    GLshort w) {
  self->glVertexAttrib4s(index, x, y, z, w);
}

//  void QOpenGLFunctions_2_0::glVertexAttrib4iv(GLuint index, const GLint
//      *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_017glVertexAttrib4ivEjPKi(
    QOpenGLFunctions_2_0 *self,
    GLuint index,
    const GLint *v) {
  self->glVertexAttrib4iv(index, v);
}

//  void QOpenGLFunctions_2_0::glVertexAttrib4fv(GLuint index, const GLfloat
//      *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_017glVertexAttrib4fvEjPKf(
    QOpenGLFunctions_2_0 *self,
    GLuint index,
    const GLfloat *v) {
  self->glVertexAttrib4fv(index, v);
}

//  void QOpenGLFunctions_2_0::glVertexAttrib4f(GLuint index, GLfloat x,
//      GLfloat y, GLfloat z, GLfloat w)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_016glVertexAttrib4fEjffff(
    QOpenGLFunctions_2_0 *self,
    GLuint index,
    GLfloat x,
    GLfloat y,
    GLfloat z,
    GLfloat w) {
  self->glVertexAttrib4f(index, x, y, z, w);
}

//  void QOpenGLFunctions_2_0::glVertexAttrib4dv(GLuint index, const GLdouble
//      *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_017glVertexAttrib4dvEjPKd(
    QOpenGLFunctions_2_0 *self,
    GLuint index,
    const GLdouble *v) {
  self->glVertexAttrib4dv(index, v);
}

//  void QOpenGLFunctions_2_0::glVertexAttrib4d(GLuint index, GLdouble x,
//      GLdouble y, GLdouble z, GLdouble w)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_016glVertexAttrib4dEjdddd(
    QOpenGLFunctions_2_0 *self,
    GLuint index,
    GLdouble x,
    GLdouble y,
    GLdouble z,
    GLdouble w) {
  self->glVertexAttrib4d(index, x, y, z, w);
}

//  void QOpenGLFunctions_2_0::glVertexAttrib4bv(GLuint index, const GLbyte
//      *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_017glVertexAttrib4bvEjPKa(
    QOpenGLFunctions_2_0 *self,
    GLuint index,
    const GLbyte *v) {
  self->glVertexAttrib4bv(index, v);
}

//  void QOpenGLFunctions_2_0::glVertexAttrib4Nusv(GLuint index, const
//      GLushort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_019glVertexAttrib4NusvEjPKt(
    QOpenGLFunctions_2_0 *self,
    GLuint index,
    const GLushort *v) {
  self->glVertexAttrib4Nusv(index, v);
}

//  void QOpenGLFunctions_2_0::glVertexAttrib4Nuiv(GLuint index, const GLuint
//      *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_019glVertexAttrib4NuivEjPKj(
    QOpenGLFunctions_2_0 *self,
    GLuint index,
    const GLuint *v) {
  self->glVertexAttrib4Nuiv(index, v);
}

//  void QOpenGLFunctions_2_0::glVertexAttrib4Nubv(GLuint index, const
//      GLubyte *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_019glVertexAttrib4NubvEjPKh(
    QOpenGLFunctions_2_0 *self,
    GLuint index,
    const GLubyte *v) {
  self->glVertexAttrib4Nubv(index, v);
}

//  void QOpenGLFunctions_2_0::glVertexAttrib4Nub(GLuint index, GLubyte x,
//      GLubyte y, GLubyte z, GLubyte w)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_018glVertexAttrib4NubEjhhhh(
    QOpenGLFunctions_2_0 *self,
    GLuint index,
    GLubyte x,
    GLubyte y,
    GLubyte z,
    GLubyte w) {
  self->glVertexAttrib4Nub(index, x, y, z, w);
}

//  void QOpenGLFunctions_2_0::glVertexAttrib4Nsv(GLuint index, const GLshort
//      *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_018glVertexAttrib4NsvEjPKs(
    QOpenGLFunctions_2_0 *self,
    GLuint index,
    const GLshort *v) {
  self->glVertexAttrib4Nsv(index, v);
}

//  void QOpenGLFunctions_2_0::glVertexAttrib4Niv(GLuint index, const GLint
//      *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_018glVertexAttrib4NivEjPKi(
    QOpenGLFunctions_2_0 *self,
    GLuint index,
    const GLint *v) {
  self->glVertexAttrib4Niv(index, v);
}

//  void QOpenGLFunctions_2_0::glVertexAttrib4Nbv(GLuint index, const GLbyte
//      *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_018glVertexAttrib4NbvEjPKa(
    QOpenGLFunctions_2_0 *self,
    GLuint index,
    const GLbyte *v) {
  self->glVertexAttrib4Nbv(index, v);
}

//  void QOpenGLFunctions_2_0::glVertexAttrib3sv(GLuint index, const GLshort
//      *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_017glVertexAttrib3svEjPKs(
    QOpenGLFunctions_2_0 *self,
    GLuint index,
    const GLshort *v) {
  self->glVertexAttrib3sv(index, v);
}

//  void QOpenGLFunctions_2_0::glVertexAttrib3s(GLuint index, GLshort x,
//      GLshort y, GLshort z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_016glVertexAttrib3sEjsss(
    QOpenGLFunctions_2_0 *self,
    GLuint index,
    GLshort x,
    GLshort y,
    GLshort z) {
  self->glVertexAttrib3s(index, x, y, z);
}

//  void QOpenGLFunctions_2_0::glVertexAttrib3fv(GLuint index, const GLfloat
//      *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_017glVertexAttrib3fvEjPKf(
    QOpenGLFunctions_2_0 *self,
    GLuint index,
    const GLfloat *v) {
  self->glVertexAttrib3fv(index, v);
}

//  void QOpenGLFunctions_2_0::glVertexAttrib3f(GLuint index, GLfloat x,
//      GLfloat y, GLfloat z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_016glVertexAttrib3fEjfff(
    QOpenGLFunctions_2_0 *self,
    GLuint index,
    GLfloat x,
    GLfloat y,
    GLfloat z) {
  self->glVertexAttrib3f(index, x, y, z);
}

//  void QOpenGLFunctions_2_0::glVertexAttrib3dv(GLuint index, const GLdouble
//      *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_017glVertexAttrib3dvEjPKd(
    QOpenGLFunctions_2_0 *self,
    GLuint index,
    const GLdouble *v) {
  self->glVertexAttrib3dv(index, v);
}

//  void QOpenGLFunctions_2_0::glVertexAttrib3d(GLuint index, GLdouble x,
//      GLdouble y, GLdouble z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_016glVertexAttrib3dEjddd(
    QOpenGLFunctions_2_0 *self,
    GLuint index,
    GLdouble x,
    GLdouble y,
    GLdouble z) {
  self->glVertexAttrib3d(index, x, y, z);
}

//  void QOpenGLFunctions_2_0::glVertexAttrib2sv(GLuint index, const GLshort
//      *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_017glVertexAttrib2svEjPKs(
    QOpenGLFunctions_2_0 *self,
    GLuint index,
    const GLshort *v) {
  self->glVertexAttrib2sv(index, v);
}

//  void QOpenGLFunctions_2_0::glVertexAttrib2s(GLuint index, GLshort x,
//      GLshort y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_016glVertexAttrib2sEjss(
    QOpenGLFunctions_2_0 *self,
    GLuint index,
    GLshort x,
    GLshort y) {
  self->glVertexAttrib2s(index, x, y);
}

//  void QOpenGLFunctions_2_0::glVertexAttrib2fv(GLuint index, const GLfloat
//      *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_017glVertexAttrib2fvEjPKf(
    QOpenGLFunctions_2_0 *self,
    GLuint index,
    const GLfloat *v) {
  self->glVertexAttrib2fv(index, v);
}

//  void QOpenGLFunctions_2_0::glVertexAttrib2f(GLuint index, GLfloat x,
//      GLfloat y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_016glVertexAttrib2fEjff(
    QOpenGLFunctions_2_0 *self,
    GLuint index,
    GLfloat x,
    GLfloat y) {
  self->glVertexAttrib2f(index, x, y);
}

//  void QOpenGLFunctions_2_0::glVertexAttrib2dv(GLuint index, const GLdouble
//      *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_017glVertexAttrib2dvEjPKd(
    QOpenGLFunctions_2_0 *self,
    GLuint index,
    const GLdouble *v) {
  self->glVertexAttrib2dv(index, v);
}

//  void QOpenGLFunctions_2_0::glVertexAttrib2d(GLuint index, GLdouble x,
//      GLdouble y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_016glVertexAttrib2dEjdd(
    QOpenGLFunctions_2_0 *self,
    GLuint index,
    GLdouble x,
    GLdouble y) {
  self->glVertexAttrib2d(index, x, y);
}

//  void QOpenGLFunctions_2_0::glVertexAttrib1sv(GLuint index, const GLshort
//      *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_017glVertexAttrib1svEjPKs(
    QOpenGLFunctions_2_0 *self,
    GLuint index,
    const GLshort *v) {
  self->glVertexAttrib1sv(index, v);
}

//  void QOpenGLFunctions_2_0::glVertexAttrib1s(GLuint index, GLshort x)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_016glVertexAttrib1sEjs(
    QOpenGLFunctions_2_0 *self,
    GLuint index,
    GLshort x) {
  self->glVertexAttrib1s(index, x);
}

//  void QOpenGLFunctions_2_0::glVertexAttrib1fv(GLuint index, const GLfloat
//      *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_017glVertexAttrib1fvEjPKf(
    QOpenGLFunctions_2_0 *self,
    GLuint index,
    const GLfloat *v) {
  self->glVertexAttrib1fv(index, v);
}

//  void QOpenGLFunctions_2_0::glVertexAttrib1f(GLuint index, GLfloat x)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_016glVertexAttrib1fEjf(
    QOpenGLFunctions_2_0 *self,
    GLuint index,
    GLfloat x) {
  self->glVertexAttrib1f(index, x);
}

//  void QOpenGLFunctions_2_0::glVertexAttrib1dv(GLuint index, const GLdouble
//      *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_017glVertexAttrib1dvEjPKd(
    QOpenGLFunctions_2_0 *self,
    GLuint index,
    const GLdouble *v) {
  self->glVertexAttrib1dv(index, v);
}

//  void QOpenGLFunctions_2_0::glVertexAttrib1d(GLuint index, GLdouble x)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_016glVertexAttrib1dEjd(
    QOpenGLFunctions_2_0 *self,
    GLuint index,
    GLdouble x) {
  self->glVertexAttrib1d(index, x);
}

//  bool QOpenGLFunctions_2_0::isContextCompatible(QOpenGLContext *context)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QOpenGLFunctions_2_019isContextCompatibleEP14QOpenGLContext(
    QOpenGLContext *context) {
  return QOpenGLFunctions_2_0::isContextCompatible(context);
}

//  QOpenGLVersionProfile QOpenGLFunctions_2_0::versionProfile()
extern "C" Q_DECL_EXPORT
QOpenGLVersionProfile *ritual_ZN20QOpenGLFunctions_2_014versionProfileEv() {
  return new QOpenGLVersionProfile(QOpenGLFunctions_2_0::versionProfile());
}

//  a Python function taken by a CuteQOpenGLFunctions_2_0, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QOpenGLFunctions_2_0(
    QOpenGLFunctions_2_0 *self,
    const char *key,
    void *call) {
  return static_cast<CuteQOpenGLFunctions_2_0 *>(self)->take(key, call);
}

//  bool QOpenGLFunctions_2_0::initializeOpenGLFunctions()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN20QOpenGLFunctions_2_025initializeOpenGLFunctionsEv(
    QOpenGLFunctions_2_0 *self) {
  return self->QOpenGLFunctions_2_0::initializeOpenGLFunctions();
}

#endif  // !defined(QT_NO_OPENGL) && !QT_CONFIG(opengles2)
#endif  // !QT_CONFIG(opengles2)
