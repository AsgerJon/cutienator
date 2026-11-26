//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/qopenglfunctions_3_1.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtOpenGL/qtopenglglobal.h>
#if !QT_CONFIG(opengles2)
#if !defined(QT_NO_OPENGL) && !QT_CONFIG(opengles2)
#include <QtOpenGL/QtOpenGL>
#include <QtOpenGL/qopenglfunctions_3_1.h>
#include <QtOpenGL/qopenglversionprofile.h>
#include <cstring>

//  A QOpenGLFunctions_3_1 that Python can take functions over in. Every QOpenGLFunctions_3_1
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL) && !QT_CONFIG(opengles2)
typedef bool (*CuteQOpenGLFunctions_3_1Call0)(const void *, int *);
#endif  // !defined(QT_NO_OPENGL) && !QT_CONFIG(opengles2)
#endif  // !defined(QT_NO_OPENGL)
class CuteQOpenGLFunctions_3_1 : public QOpenGLFunctions_3_1 {
public:
  using QOpenGLFunctions_3_1::QOpenGLFunctions_3_1;
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
  //  bool QOpenGLFunctions_3_1::initializeOpenGLFunctions()
  bool initializeOpenGLFunctions() override {
    if (taken[0]) {
      int handled = 0;
      CuteQOpenGLFunctions_3_1Call0 call = reinterpret_cast<CuteQOpenGLFunctions_3_1Call0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QOpenGLFunctions_3_1::initializeOpenGLFunctions();
  }
#endif  // !defined(QT_NO_OPENGL) && !QT_CONFIG(opengles2)
#endif  // !defined(QT_NO_OPENGL)
};

//  QOpenGLFunctions_3_1::QOpenGLFunctions_3_1()
extern "C" Q_DECL_EXPORT
QOpenGLFunctions_3_1 *ritual_ZN20QOpenGLFunctions_3_1C1Ev() {
  return new CuteQOpenGLFunctions_3_1();
}

//  QOpenGLFunctions_3_1::~QOpenGLFunctions_3_1()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_1D1Ev(QOpenGLFunctions_3_1 *self) {
  delete self;
}

//  bool QOpenGLFunctions_3_1::initializeOpenGLFunctions()
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QOpenGLFunctions_3_125initializeOpenGLFunctionsEv(
    QOpenGLFunctions_3_1 *self) {
  return self->initializeOpenGLFunctions();
}

//  void QOpenGLFunctions_3_1::glViewport(GLint x, GLint y, GLsizei width,
//      GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_110glViewportEiiii(
    QOpenGLFunctions_3_1 *self,
    GLint x,
    GLint y,
    GLsizei width,
    GLsizei height) {
  self->glViewport(x, y, width, height);
}

//  void QOpenGLFunctions_3_1::glDepthRange(GLdouble nearVal, GLdouble
//      farVal)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_112glDepthRangeEdd(
    QOpenGLFunctions_3_1 *self,
    GLdouble nearVal,
    GLdouble farVal) {
  self->glDepthRange(nearVal, farVal);
}

//  GLboolean QOpenGLFunctions_3_1::glIsEnabled(GLenum cap)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN20QOpenGLFunctions_3_111glIsEnabledEj(
    QOpenGLFunctions_3_1 *self,
    GLenum cap) {
  return self->glIsEnabled(cap);
}

//  void QOpenGLFunctions_3_1::glGetTexLevelParameteriv(GLenum target, GLint
//      level, GLenum pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_124glGetTexLevelParameterivEjijPi(
    QOpenGLFunctions_3_1 *self,
    GLenum target,
    GLint level,
    GLenum pname,
    GLint *params) {
  self->glGetTexLevelParameteriv(target, level, pname, params);
}

//  void QOpenGLFunctions_3_1::glGetTexLevelParameterfv(GLenum target, GLint
//      level, GLenum pname, GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_124glGetTexLevelParameterfvEjijPf(
    QOpenGLFunctions_3_1 *self,
    GLenum target,
    GLint level,
    GLenum pname,
    GLfloat *params) {
  self->glGetTexLevelParameterfv(target, level, pname, params);
}

//  void QOpenGLFunctions_3_1::glGetTexParameteriv(GLenum target, GLenum
//      pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_119glGetTexParameterivEjjPi(
    QOpenGLFunctions_3_1 *self,
    GLenum target,
    GLenum pname,
    GLint *params) {
  self->glGetTexParameteriv(target, pname, params);
}

//  void QOpenGLFunctions_3_1::glGetTexParameterfv(GLenum target, GLenum
//      pname, GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_119glGetTexParameterfvEjjPf(
    QOpenGLFunctions_3_1 *self,
    GLenum target,
    GLenum pname,
    GLfloat *params) {
  self->glGetTexParameterfv(target, pname, params);
}

//  void QOpenGLFunctions_3_1::glGetTexImage(GLenum target, GLint level,
//      GLenum format, GLenum type, GLvoid *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_113glGetTexImageEjijjPv(
    QOpenGLFunctions_3_1 *self,
    GLenum target,
    GLint level,
    GLenum format,
    GLenum type,
    GLvoid *pixels) {
  self->glGetTexImage(target, level, format, type, pixels);
}

//  const GLubyte *QOpenGLFunctions_3_1::glGetString(GLenum name)
extern "C" Q_DECL_EXPORT
const GLubyte *ritual_ZN20QOpenGLFunctions_3_111glGetStringEj(
    QOpenGLFunctions_3_1 *self,
    GLenum name) {
  return self->glGetString(name);
}

//  void QOpenGLFunctions_3_1::glGetIntegerv(GLenum pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_113glGetIntegervEjPi(
    QOpenGLFunctions_3_1 *self,
    GLenum pname,
    GLint *params) {
  self->glGetIntegerv(pname, params);
}

//  void QOpenGLFunctions_3_1::glGetFloatv(GLenum pname, GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_111glGetFloatvEjPf(
    QOpenGLFunctions_3_1 *self,
    GLenum pname,
    GLfloat *params) {
  self->glGetFloatv(pname, params);
}

//  GLenum QOpenGLFunctions_3_1::glGetError()
extern "C" Q_DECL_EXPORT
GLenum ritual_ZN20QOpenGLFunctions_3_110glGetErrorEv(
    QOpenGLFunctions_3_1 *self) {
  return self->glGetError();
}

//  void QOpenGLFunctions_3_1::glGetDoublev(GLenum pname, GLdouble *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_112glGetDoublevEjPd(
    QOpenGLFunctions_3_1 *self,
    GLenum pname,
    GLdouble *params) {
  self->glGetDoublev(pname, params);
}

//  void QOpenGLFunctions_3_1::glGetBooleanv(GLenum pname, GLboolean *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_113glGetBooleanvEjPh(
    QOpenGLFunctions_3_1 *self,
    GLenum pname,
    GLboolean *params) {
  self->glGetBooleanv(pname, params);
}

//  void QOpenGLFunctions_3_1::glReadPixels(GLint x, GLint y, GLsizei width,
//      GLsizei height, GLenum format, GLenum type, GLvoid *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_112glReadPixelsEiiiijjPv(
    QOpenGLFunctions_3_1 *self,
    GLint x,
    GLint y,
    GLsizei width,
    GLsizei height,
    GLenum format,
    GLenum type,
    GLvoid *pixels) {
  self->glReadPixels(x, y, width, height, format, type, pixels);
}

//  void QOpenGLFunctions_3_1::glReadBuffer(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_112glReadBufferEj(
    QOpenGLFunctions_3_1 *self,
    GLenum mode) {
  self->glReadBuffer(mode);
}

//  void QOpenGLFunctions_3_1::glPixelStorei(GLenum pname, GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_113glPixelStoreiEji(
    QOpenGLFunctions_3_1 *self,
    GLenum pname,
    GLint param) {
  self->glPixelStorei(pname, param);
}

//  void QOpenGLFunctions_3_1::glPixelStoref(GLenum pname, GLfloat param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_113glPixelStorefEjf(
    QOpenGLFunctions_3_1 *self,
    GLenum pname,
    GLfloat param) {
  self->glPixelStoref(pname, param);
}

//  void QOpenGLFunctions_3_1::glDepthFunc(GLenum func)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_111glDepthFuncEj(
    QOpenGLFunctions_3_1 *self,
    GLenum func) {
  self->glDepthFunc(func);
}

//  void QOpenGLFunctions_3_1::glStencilOp(GLenum fail, GLenum zfail, GLenum
//      zpass)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_111glStencilOpEjjj(
    QOpenGLFunctions_3_1 *self,
    GLenum fail,
    GLenum zfail,
    GLenum zpass) {
  self->glStencilOp(fail, zfail, zpass);
}

//  void QOpenGLFunctions_3_1::glStencilFunc(GLenum func, GLint ref, GLuint
//      mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_113glStencilFuncEjij(
    QOpenGLFunctions_3_1 *self,
    GLenum func,
    GLint ref,
    GLuint mask) {
  self->glStencilFunc(func, ref, mask);
}

//  void QOpenGLFunctions_3_1::glLogicOp(GLenum opcode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_19glLogicOpEj(
    QOpenGLFunctions_3_1 *self,
    GLenum opcode) {
  self->glLogicOp(opcode);
}

//  void QOpenGLFunctions_3_1::glBlendFunc(GLenum sfactor, GLenum dfactor)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_111glBlendFuncEjj(
    QOpenGLFunctions_3_1 *self,
    GLenum sfactor,
    GLenum dfactor) {
  self->glBlendFunc(sfactor, dfactor);
}

//  void QOpenGLFunctions_3_1::glFlush()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_17glFlushEv(QOpenGLFunctions_3_1 *self) {
  self->glFlush();
}

//  void QOpenGLFunctions_3_1::glFinish()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_18glFinishEv(QOpenGLFunctions_3_1 *self) {
  self->glFinish();
}

//  void QOpenGLFunctions_3_1::glEnable(GLenum cap)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_18glEnableEj(
    QOpenGLFunctions_3_1 *self,
    GLenum cap) {
  self->glEnable(cap);
}

//  void QOpenGLFunctions_3_1::glDisable(GLenum cap)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_19glDisableEj(
    QOpenGLFunctions_3_1 *self,
    GLenum cap) {
  self->glDisable(cap);
}

//  void QOpenGLFunctions_3_1::glDepthMask(GLboolean flag)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_111glDepthMaskEh(
    QOpenGLFunctions_3_1 *self,
    GLboolean flag) {
  self->glDepthMask(flag);
}

//  void QOpenGLFunctions_3_1::glColorMask(GLboolean red, GLboolean green,
//      GLboolean blue, GLboolean alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_111glColorMaskEhhhh(
    QOpenGLFunctions_3_1 *self,
    GLboolean red,
    GLboolean green,
    GLboolean blue,
    GLboolean alpha) {
  self->glColorMask(red, green, blue, alpha);
}

//  void QOpenGLFunctions_3_1::glStencilMask(GLuint mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_113glStencilMaskEj(
    QOpenGLFunctions_3_1 *self,
    GLuint mask) {
  self->glStencilMask(mask);
}

//  void QOpenGLFunctions_3_1::glClearDepth(GLdouble depth)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_112glClearDepthEd(
    QOpenGLFunctions_3_1 *self,
    GLdouble depth) {
  self->glClearDepth(depth);
}

//  void QOpenGLFunctions_3_1::glClearStencil(GLint s)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_114glClearStencilEi(
    QOpenGLFunctions_3_1 *self,
    GLint s) {
  self->glClearStencil(s);
}

//  void QOpenGLFunctions_3_1::glClearColor(GLfloat red, GLfloat green,
//      GLfloat blue, GLfloat alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_112glClearColorEffff(
    QOpenGLFunctions_3_1 *self,
    GLfloat red,
    GLfloat green,
    GLfloat blue,
    GLfloat alpha) {
  self->glClearColor(red, green, blue, alpha);
}

//  void QOpenGLFunctions_3_1::glClear(GLbitfield mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_17glClearEj(
    QOpenGLFunctions_3_1 *self,
    GLbitfield mask) {
  self->glClear(mask);
}

//  void QOpenGLFunctions_3_1::glDrawBuffer(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_112glDrawBufferEj(
    QOpenGLFunctions_3_1 *self,
    GLenum mode) {
  self->glDrawBuffer(mode);
}

//  void QOpenGLFunctions_3_1::glTexImage2D(GLenum target, GLint level, GLint
//      internalformat, GLsizei width, GLsizei height, GLint border, GLenum
//      format, GLenum type, const GLvoid *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_112glTexImage2DEjiiiiijjPKv(
    QOpenGLFunctions_3_1 *self,
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

//  void QOpenGLFunctions_3_1::glTexImage1D(GLenum target, GLint level, GLint
//      internalformat, GLsizei width, GLint border, GLenum format, GLenum
//      type, const GLvoid *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_112glTexImage1DEjiiiijjPKv(
    QOpenGLFunctions_3_1 *self,
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

//  void QOpenGLFunctions_3_1::glTexParameteriv(GLenum target, GLenum pname,
//      const GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_116glTexParameterivEjjPKi(
    QOpenGLFunctions_3_1 *self,
    GLenum target,
    GLenum pname,
    const GLint *params) {
  self->glTexParameteriv(target, pname, params);
}

//  void QOpenGLFunctions_3_1::glTexParameteri(GLenum target, GLenum pname,
//      GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_115glTexParameteriEjji(
    QOpenGLFunctions_3_1 *self,
    GLenum target,
    GLenum pname,
    GLint param) {
  self->glTexParameteri(target, pname, param);
}

//  void QOpenGLFunctions_3_1::glTexParameterfv(GLenum target, GLenum pname,
//      const GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_116glTexParameterfvEjjPKf(
    QOpenGLFunctions_3_1 *self,
    GLenum target,
    GLenum pname,
    const GLfloat *params) {
  self->glTexParameterfv(target, pname, params);
}

//  void QOpenGLFunctions_3_1::glTexParameterf(GLenum target, GLenum pname,
//      GLfloat param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_115glTexParameterfEjjf(
    QOpenGLFunctions_3_1 *self,
    GLenum target,
    GLenum pname,
    GLfloat param) {
  self->glTexParameterf(target, pname, param);
}

//  void QOpenGLFunctions_3_1::glScissor(GLint x, GLint y, GLsizei width,
//      GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_19glScissorEiiii(
    QOpenGLFunctions_3_1 *self,
    GLint x,
    GLint y,
    GLsizei width,
    GLsizei height) {
  self->glScissor(x, y, width, height);
}

//  void QOpenGLFunctions_3_1::glPolygonMode(GLenum face, GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_113glPolygonModeEjj(
    QOpenGLFunctions_3_1 *self,
    GLenum face,
    GLenum mode) {
  self->glPolygonMode(face, mode);
}

//  void QOpenGLFunctions_3_1::glPointSize(GLfloat size)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_111glPointSizeEf(
    QOpenGLFunctions_3_1 *self,
    GLfloat size) {
  self->glPointSize(size);
}

//  void QOpenGLFunctions_3_1::glLineWidth(GLfloat width)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_111glLineWidthEf(
    QOpenGLFunctions_3_1 *self,
    GLfloat width) {
  self->glLineWidth(width);
}

//  void QOpenGLFunctions_3_1::glHint(GLenum target, GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_16glHintEjj(
    QOpenGLFunctions_3_1 *self,
    GLenum target,
    GLenum mode) {
  self->glHint(target, mode);
}

//  void QOpenGLFunctions_3_1::glFrontFace(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_111glFrontFaceEj(
    QOpenGLFunctions_3_1 *self,
    GLenum mode) {
  self->glFrontFace(mode);
}

//  void QOpenGLFunctions_3_1::glCullFace(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_110glCullFaceEj(
    QOpenGLFunctions_3_1 *self,
    GLenum mode) {
  self->glCullFace(mode);
}

//  GLboolean QOpenGLFunctions_3_1::glIsTexture(GLuint texture)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN20QOpenGLFunctions_3_111glIsTextureEj(
    QOpenGLFunctions_3_1 *self,
    GLuint texture) {
  return self->glIsTexture(texture);
}

//  void QOpenGLFunctions_3_1::glGenTextures(GLsizei n, GLuint *textures)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_113glGenTexturesEiPj(
    QOpenGLFunctions_3_1 *self,
    GLsizei n,
    GLuint *textures) {
  self->glGenTextures(n, textures);
}

//  void QOpenGLFunctions_3_1::glDeleteTextures(GLsizei n, const GLuint
//      *textures)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_116glDeleteTexturesEiPKj(
    QOpenGLFunctions_3_1 *self,
    GLsizei n,
    const GLuint *textures) {
  self->glDeleteTextures(n, textures);
}

//  void QOpenGLFunctions_3_1::glBindTexture(GLenum target, GLuint texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_113glBindTextureEjj(
    QOpenGLFunctions_3_1 *self,
    GLenum target,
    GLuint texture) {
  self->glBindTexture(target, texture);
}

//  void QOpenGLFunctions_3_1::glTexSubImage2D(GLenum target, GLint level,
//      GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum
//      format, GLenum type, const GLvoid *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_115glTexSubImage2DEjiiiiijjPKv(
    QOpenGLFunctions_3_1 *self,
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

//  void QOpenGLFunctions_3_1::glTexSubImage1D(GLenum target, GLint level,
//      GLint xoffset, GLsizei width, GLenum format, GLenum type, const
//      GLvoid *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_115glTexSubImage1DEjiiijjPKv(
    QOpenGLFunctions_3_1 *self,
    GLenum target,
    GLint level,
    GLint xoffset,
    GLsizei width,
    GLenum format,
    GLenum type,
    const GLvoid *pixels) {
  self->glTexSubImage1D(target, level, xoffset, width, format, type, pixels);
}

//  void QOpenGLFunctions_3_1::glCopyTexSubImage2D(GLenum target, GLint
//      level, GLint xoffset, GLint yoffset, GLint x, GLint y, GLsizei width,
//      GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_119glCopyTexSubImage2DEjiiiiiii(
    QOpenGLFunctions_3_1 *self,
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

//  void QOpenGLFunctions_3_1::glCopyTexSubImage1D(GLenum target, GLint
//      level, GLint xoffset, GLint x, GLint y, GLsizei width)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_119glCopyTexSubImage1DEjiiiii(
    QOpenGLFunctions_3_1 *self,
    GLenum target,
    GLint level,
    GLint xoffset,
    GLint x,
    GLint y,
    GLsizei width) {
  self->glCopyTexSubImage1D(target, level, xoffset, x, y, width);
}

//  void QOpenGLFunctions_3_1::glCopyTexImage2D(GLenum target, GLint level,
//      GLenum internalformat, GLint x, GLint y, GLsizei width, GLsizei
//      height, GLint border)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_116glCopyTexImage2DEjijiiiii(
    QOpenGLFunctions_3_1 *self,
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

//  void QOpenGLFunctions_3_1::glCopyTexImage1D(GLenum target, GLint level,
//      GLenum internalformat, GLint x, GLint y, GLsizei width, GLint border)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_116glCopyTexImage1DEjijiiii(
    QOpenGLFunctions_3_1 *self,
    GLenum target,
    GLint level,
    GLenum internalformat,
    GLint x,
    GLint y,
    GLsizei width,
    GLint border) {
  self->glCopyTexImage1D(target, level, internalformat, x, y, width, border);
}

//  void QOpenGLFunctions_3_1::glPolygonOffset(GLfloat factor, GLfloat units)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_115glPolygonOffsetEff(
    QOpenGLFunctions_3_1 *self,
    GLfloat factor,
    GLfloat units) {
  self->glPolygonOffset(factor, units);
}

//  void QOpenGLFunctions_3_1::glDrawElements(GLenum mode, GLsizei count,
//      GLenum type, const GLvoid *indices)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_114glDrawElementsEjijPKv(
    QOpenGLFunctions_3_1 *self,
    GLenum mode,
    GLsizei count,
    GLenum type,
    const GLvoid *indices) {
  self->glDrawElements(mode, count, type, indices);
}

//  void QOpenGLFunctions_3_1::glDrawArrays(GLenum mode, GLint first, GLsizei
//      count)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_112glDrawArraysEjii(
    QOpenGLFunctions_3_1 *self,
    GLenum mode,
    GLint first,
    GLsizei count) {
  self->glDrawArrays(mode, first, count);
}

//  void QOpenGLFunctions_3_1::glCopyTexSubImage3D(GLenum target, GLint
//      level, GLint xoffset, GLint yoffset, GLint zoffset, GLint x, GLint y,
//      GLsizei width, GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_119glCopyTexSubImage3DEjiiiiiiii(
    QOpenGLFunctions_3_1 *self,
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

//  void QOpenGLFunctions_3_1::glTexSubImage3D(GLenum target, GLint level,
//      GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei
//      height, GLsizei depth, GLenum format, GLenum type, const GLvoid
//      *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_115glTexSubImage3DEjiiiiiiijjPKv(
    QOpenGLFunctions_3_1 *self,
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

//  void QOpenGLFunctions_3_1::glTexImage3D(GLenum target, GLint level, GLint
//      internalformat, GLsizei width, GLsizei height, GLsizei depth, GLint
//      border, GLenum format, GLenum type, const GLvoid *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_112glTexImage3DEjiiiiiijjPKv(
    QOpenGLFunctions_3_1 *self,
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

//  void QOpenGLFunctions_3_1::glDrawRangeElements(GLenum mode, GLuint start,
//      GLuint end, GLsizei count, GLenum type, const GLvoid *indices)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_119glDrawRangeElementsEjjjijPKv(
    QOpenGLFunctions_3_1 *self,
    GLenum mode,
    GLuint start,
    GLuint end,
    GLsizei count,
    GLenum type,
    const GLvoid *indices) {
  self->glDrawRangeElements(mode, start, end, count, type, indices);
}

//  void QOpenGLFunctions_3_1::glBlendEquation(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_115glBlendEquationEj(
    QOpenGLFunctions_3_1 *self,
    GLenum mode) {
  self->glBlendEquation(mode);
}

//  void QOpenGLFunctions_3_1::glBlendColor(GLfloat red, GLfloat green,
//      GLfloat blue, GLfloat alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_112glBlendColorEffff(
    QOpenGLFunctions_3_1 *self,
    GLfloat red,
    GLfloat green,
    GLfloat blue,
    GLfloat alpha) {
  self->glBlendColor(red, green, blue, alpha);
}

//  void QOpenGLFunctions_3_1::glGetCompressedTexImage(GLenum target, GLint
//      level, GLvoid *img)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_123glGetCompressedTexImageEjiPv(
    QOpenGLFunctions_3_1 *self,
    GLenum target,
    GLint level,
    GLvoid *img) {
  self->glGetCompressedTexImage(target, level, img);
}

//  void QOpenGLFunctions_3_1::glCompressedTexSubImage1D(GLenum target, GLint
//      level, GLint xoffset, GLsizei width, GLenum format, GLsizei
//      imageSize, const GLvoid *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_125glCompressedTexSubImage1DEjiiijiPKv(
    QOpenGLFunctions_3_1 *self,
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

//  void QOpenGLFunctions_3_1::glCompressedTexSubImage2D(GLenum target, GLint
//      level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height,
//      GLenum format, GLsizei imageSize, const GLvoid *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_125glCompressedTexSubImage2DEjiiiiijiPKv(
    QOpenGLFunctions_3_1 *self,
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

//  void QOpenGLFunctions_3_1::glCompressedTexSubImage3D(GLenum target, GLint
//      level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width,
//      GLsizei height, GLsizei depth, GLenum format, GLsizei imageSize,
//      const GLvoid *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_125glCompressedTexSubImage3DEjiiiiiiijiPKv(
    QOpenGLFunctions_3_1 *self,
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

//  void QOpenGLFunctions_3_1::glCompressedTexImage1D(GLenum target, GLint
//      level, GLenum internalformat, GLsizei width, GLint border, GLsizei
//      imageSize, const GLvoid *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_122glCompressedTexImage1DEjijiiiPKv(
    QOpenGLFunctions_3_1 *self,
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

//  void QOpenGLFunctions_3_1::glCompressedTexImage2D(GLenum target, GLint
//      level, GLenum internalformat, GLsizei width, GLsizei height, GLint
//      border, GLsizei imageSize, const GLvoid *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_122glCompressedTexImage2DEjijiiiiPKv(
    QOpenGLFunctions_3_1 *self,
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

//  void QOpenGLFunctions_3_1::glCompressedTexImage3D(GLenum target, GLint
//      level, GLenum internalformat, GLsizei width, GLsizei height, GLsizei
//      depth, GLint border, GLsizei imageSize, const GLvoid *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_122glCompressedTexImage3DEjijiiiiiPKv(
    QOpenGLFunctions_3_1 *self,
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

//  void QOpenGLFunctions_3_1::glSampleCoverage(GLfloat value, GLboolean
//      invert)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_116glSampleCoverageEfh(
    QOpenGLFunctions_3_1 *self,
    GLfloat value,
    GLboolean invert) {
  self->glSampleCoverage(value, invert);
}

//  void QOpenGLFunctions_3_1::glActiveTexture(GLenum texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_115glActiveTextureEj(
    QOpenGLFunctions_3_1 *self,
    GLenum texture) {
  self->glActiveTexture(texture);
}

//  void QOpenGLFunctions_3_1::glPointParameteriv(GLenum pname, const GLint
//      *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_118glPointParameterivEjPKi(
    QOpenGLFunctions_3_1 *self,
    GLenum pname,
    const GLint *params) {
  self->glPointParameteriv(pname, params);
}

//  void QOpenGLFunctions_3_1::glPointParameteri(GLenum pname, GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_117glPointParameteriEji(
    QOpenGLFunctions_3_1 *self,
    GLenum pname,
    GLint param) {
  self->glPointParameteri(pname, param);
}

//  void QOpenGLFunctions_3_1::glPointParameterfv(GLenum pname, const GLfloat
//      *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_118glPointParameterfvEjPKf(
    QOpenGLFunctions_3_1 *self,
    GLenum pname,
    const GLfloat *params) {
  self->glPointParameterfv(pname, params);
}

//  void QOpenGLFunctions_3_1::glPointParameterf(GLenum pname, GLfloat param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_117glPointParameterfEjf(
    QOpenGLFunctions_3_1 *self,
    GLenum pname,
    GLfloat param) {
  self->glPointParameterf(pname, param);
}

//  void QOpenGLFunctions_3_1::glMultiDrawElements(GLenum mode, const GLsizei
//      *count, GLenum type, const GLvoid *const *indices, GLsizei drawcount)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_119glMultiDrawElementsEjPKijPKPKvi(
    QOpenGLFunctions_3_1 *self,
    GLenum mode,
    const GLsizei *count,
    GLenum type,
    const GLvoid *const *indices,
    GLsizei drawcount) {
  self->glMultiDrawElements(mode, count, type, indices, drawcount);
}

//  void QOpenGLFunctions_3_1::glMultiDrawArrays(GLenum mode, const GLint
//      *first, const GLsizei *count, GLsizei drawcount)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_117glMultiDrawArraysEjPKiS1_i(
    QOpenGLFunctions_3_1 *self,
    GLenum mode,
    const GLint *first,
    const GLsizei *count,
    GLsizei drawcount) {
  self->glMultiDrawArrays(mode, first, count, drawcount);
}

//  void QOpenGLFunctions_3_1::glBlendFuncSeparate(GLenum sfactorRGB, GLenum
//      dfactorRGB, GLenum sfactorAlpha, GLenum dfactorAlpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_119glBlendFuncSeparateEjjjj(
    QOpenGLFunctions_3_1 *self,
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

//  void QOpenGLFunctions_3_1::glGetBufferPointerv(GLenum target, GLenum
//      pname, GLvoid **params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_119glGetBufferPointervEjjPPv(
    QOpenGLFunctions_3_1 *self,
    GLenum target,
    GLenum pname,
    GLvoid **params) {
  self->glGetBufferPointerv(target, pname, params);
}

//  void QOpenGLFunctions_3_1::glGetBufferParameteriv(GLenum target, GLenum
//      pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_122glGetBufferParameterivEjjPi(
    QOpenGLFunctions_3_1 *self,
    GLenum target,
    GLenum pname,
    GLint *params) {
  self->glGetBufferParameteriv(target, pname, params);
}

//  GLboolean QOpenGLFunctions_3_1::glUnmapBuffer(GLenum target)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN20QOpenGLFunctions_3_113glUnmapBufferEj(
    QOpenGLFunctions_3_1 *self,
    GLenum target) {
  return self->glUnmapBuffer(target);
}

//  GLvoid *QOpenGLFunctions_3_1::glMapBuffer(GLenum target, GLenum access)
extern "C" Q_DECL_EXPORT
GLvoid *ritual_ZN20QOpenGLFunctions_3_111glMapBufferEjj(
    QOpenGLFunctions_3_1 *self,
    GLenum target,
    GLenum access) {
  return self->glMapBuffer(target, access);
}

//  void QOpenGLFunctions_3_1::glGetBufferSubData(GLenum target, GLintptr
//      offset, GLsizeiptr size, GLvoid *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_118glGetBufferSubDataEjllPv(
    QOpenGLFunctions_3_1 *self,
    GLenum target,
    long long offset,
    long long size,
    GLvoid *data) {
  self->glGetBufferSubData(target, offset, size, data);
}

//  void QOpenGLFunctions_3_1::glBufferSubData(GLenum target, GLintptr
//      offset, GLsizeiptr size, const GLvoid *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_115glBufferSubDataEjllPKv(
    QOpenGLFunctions_3_1 *self,
    GLenum target,
    long long offset,
    long long size,
    const GLvoid *data) {
  self->glBufferSubData(target, offset, size, data);
}

//  void QOpenGLFunctions_3_1::glBufferData(GLenum target, GLsizeiptr size,
//      const GLvoid *data, GLenum usage)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_112glBufferDataEjlPKvj(
    QOpenGLFunctions_3_1 *self,
    GLenum target,
    long long size,
    const GLvoid *data,
    GLenum usage) {
  self->glBufferData(target, size, data, usage);
}

//  GLboolean QOpenGLFunctions_3_1::glIsBuffer(GLuint buffer)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN20QOpenGLFunctions_3_110glIsBufferEj(
    QOpenGLFunctions_3_1 *self,
    GLuint buffer) {
  return self->glIsBuffer(buffer);
}

//  void QOpenGLFunctions_3_1::glGenBuffers(GLsizei n, GLuint *buffers)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_112glGenBuffersEiPj(
    QOpenGLFunctions_3_1 *self,
    GLsizei n,
    GLuint *buffers) {
  self->glGenBuffers(n, buffers);
}

//  void QOpenGLFunctions_3_1::glDeleteBuffers(GLsizei n, const GLuint
//      *buffers)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_115glDeleteBuffersEiPKj(
    QOpenGLFunctions_3_1 *self,
    GLsizei n,
    const GLuint *buffers) {
  self->glDeleteBuffers(n, buffers);
}

//  void QOpenGLFunctions_3_1::glBindBuffer(GLenum target, GLuint buffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_112glBindBufferEjj(
    QOpenGLFunctions_3_1 *self,
    GLenum target,
    GLuint buffer) {
  self->glBindBuffer(target, buffer);
}

//  void QOpenGLFunctions_3_1::glGetQueryObjectuiv(GLuint id, GLenum pname,
//      GLuint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_119glGetQueryObjectuivEjjPj(
    QOpenGLFunctions_3_1 *self,
    GLuint id,
    GLenum pname,
    GLuint *params) {
  self->glGetQueryObjectuiv(id, pname, params);
}

//  void QOpenGLFunctions_3_1::glGetQueryObjectiv(GLuint id, GLenum pname,
//      GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_118glGetQueryObjectivEjjPi(
    QOpenGLFunctions_3_1 *self,
    GLuint id,
    GLenum pname,
    GLint *params) {
  self->glGetQueryObjectiv(id, pname, params);
}

//  void QOpenGLFunctions_3_1::glGetQueryiv(GLenum target, GLenum pname,
//      GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_112glGetQueryivEjjPi(
    QOpenGLFunctions_3_1 *self,
    GLenum target,
    GLenum pname,
    GLint *params) {
  self->glGetQueryiv(target, pname, params);
}

//  void QOpenGLFunctions_3_1::glEndQuery(GLenum target)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_110glEndQueryEj(
    QOpenGLFunctions_3_1 *self,
    GLenum target) {
  self->glEndQuery(target);
}

//  void QOpenGLFunctions_3_1::glBeginQuery(GLenum target, GLuint id)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_112glBeginQueryEjj(
    QOpenGLFunctions_3_1 *self,
    GLenum target,
    GLuint id) {
  self->glBeginQuery(target, id);
}

//  GLboolean QOpenGLFunctions_3_1::glIsQuery(GLuint id)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN20QOpenGLFunctions_3_19glIsQueryEj(
    QOpenGLFunctions_3_1 *self,
    GLuint id) {
  return self->glIsQuery(id);
}

//  void QOpenGLFunctions_3_1::glDeleteQueries(GLsizei n, const GLuint *ids)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_115glDeleteQueriesEiPKj(
    QOpenGLFunctions_3_1 *self,
    GLsizei n,
    const GLuint *ids) {
  self->glDeleteQueries(n, ids);
}

//  void QOpenGLFunctions_3_1::glGenQueries(GLsizei n, GLuint *ids)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_112glGenQueriesEiPj(
    QOpenGLFunctions_3_1 *self,
    GLsizei n,
    GLuint *ids) {
  self->glGenQueries(n, ids);
}

//  void QOpenGLFunctions_3_1::glVertexAttribPointer(GLuint index, GLint
//      size, GLenum type, GLboolean normalized, GLsizei stride, const GLvoid
//      *pointer)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_121glVertexAttribPointerEjijhiPKv(
    QOpenGLFunctions_3_1 *self,
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

//  void QOpenGLFunctions_3_1::glValidateProgram(GLuint program)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_117glValidateProgramEj(
    QOpenGLFunctions_3_1 *self,
    GLuint program) {
  self->glValidateProgram(program);
}

//  void QOpenGLFunctions_3_1::glUniformMatrix4fv(GLint location, GLsizei
//      count, GLboolean transpose, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_118glUniformMatrix4fvEiihPKf(
    QOpenGLFunctions_3_1 *self,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLfloat *value) {
  self->glUniformMatrix4fv(location, count, transpose, value);
}

//  void QOpenGLFunctions_3_1::glUniformMatrix3fv(GLint location, GLsizei
//      count, GLboolean transpose, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_118glUniformMatrix3fvEiihPKf(
    QOpenGLFunctions_3_1 *self,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLfloat *value) {
  self->glUniformMatrix3fv(location, count, transpose, value);
}

//  void QOpenGLFunctions_3_1::glUniformMatrix2fv(GLint location, GLsizei
//      count, GLboolean transpose, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_118glUniformMatrix2fvEiihPKf(
    QOpenGLFunctions_3_1 *self,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLfloat *value) {
  self->glUniformMatrix2fv(location, count, transpose, value);
}

//  void QOpenGLFunctions_3_1::glUniform4iv(GLint location, GLsizei count,
//      const GLint *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_112glUniform4ivEiiPKi(
    QOpenGLFunctions_3_1 *self,
    GLint location,
    GLsizei count,
    const GLint *value) {
  self->glUniform4iv(location, count, value);
}

//  void QOpenGLFunctions_3_1::glUniform3iv(GLint location, GLsizei count,
//      const GLint *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_112glUniform3ivEiiPKi(
    QOpenGLFunctions_3_1 *self,
    GLint location,
    GLsizei count,
    const GLint *value) {
  self->glUniform3iv(location, count, value);
}

//  void QOpenGLFunctions_3_1::glUniform2iv(GLint location, GLsizei count,
//      const GLint *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_112glUniform2ivEiiPKi(
    QOpenGLFunctions_3_1 *self,
    GLint location,
    GLsizei count,
    const GLint *value) {
  self->glUniform2iv(location, count, value);
}

//  void QOpenGLFunctions_3_1::glUniform1iv(GLint location, GLsizei count,
//      const GLint *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_112glUniform1ivEiiPKi(
    QOpenGLFunctions_3_1 *self,
    GLint location,
    GLsizei count,
    const GLint *value) {
  self->glUniform1iv(location, count, value);
}

//  void QOpenGLFunctions_3_1::glUniform4fv(GLint location, GLsizei count,
//      const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_112glUniform4fvEiiPKf(
    QOpenGLFunctions_3_1 *self,
    GLint location,
    GLsizei count,
    const GLfloat *value) {
  self->glUniform4fv(location, count, value);
}

//  void QOpenGLFunctions_3_1::glUniform3fv(GLint location, GLsizei count,
//      const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_112glUniform3fvEiiPKf(
    QOpenGLFunctions_3_1 *self,
    GLint location,
    GLsizei count,
    const GLfloat *value) {
  self->glUniform3fv(location, count, value);
}

//  void QOpenGLFunctions_3_1::glUniform2fv(GLint location, GLsizei count,
//      const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_112glUniform2fvEiiPKf(
    QOpenGLFunctions_3_1 *self,
    GLint location,
    GLsizei count,
    const GLfloat *value) {
  self->glUniform2fv(location, count, value);
}

//  void QOpenGLFunctions_3_1::glUniform1fv(GLint location, GLsizei count,
//      const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_112glUniform1fvEiiPKf(
    QOpenGLFunctions_3_1 *self,
    GLint location,
    GLsizei count,
    const GLfloat *value) {
  self->glUniform1fv(location, count, value);
}

//  void QOpenGLFunctions_3_1::glUniform4i(GLint location, GLint v0, GLint
//      v1, GLint v2, GLint v3)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_111glUniform4iEiiiii(
    QOpenGLFunctions_3_1 *self,
    GLint location,
    GLint v0,
    GLint v1,
    GLint v2,
    GLint v3) {
  self->glUniform4i(location, v0, v1, v2, v3);
}

//  void QOpenGLFunctions_3_1::glUniform3i(GLint location, GLint v0, GLint
//      v1, GLint v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_111glUniform3iEiiii(
    QOpenGLFunctions_3_1 *self,
    GLint location,
    GLint v0,
    GLint v1,
    GLint v2) {
  self->glUniform3i(location, v0, v1, v2);
}

//  void QOpenGLFunctions_3_1::glUniform2i(GLint location, GLint v0, GLint
//      v1)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_111glUniform2iEiii(
    QOpenGLFunctions_3_1 *self,
    GLint location,
    GLint v0,
    GLint v1) {
  self->glUniform2i(location, v0, v1);
}

//  void QOpenGLFunctions_3_1::glUniform1i(GLint location, GLint v0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_111glUniform1iEii(
    QOpenGLFunctions_3_1 *self,
    GLint location,
    GLint v0) {
  self->glUniform1i(location, v0);
}

//  void QOpenGLFunctions_3_1::glUniform4f(GLint location, GLfloat v0,
//      GLfloat v1, GLfloat v2, GLfloat v3)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_111glUniform4fEiffff(
    QOpenGLFunctions_3_1 *self,
    GLint location,
    GLfloat v0,
    GLfloat v1,
    GLfloat v2,
    GLfloat v3) {
  self->glUniform4f(location, v0, v1, v2, v3);
}

//  void QOpenGLFunctions_3_1::glUniform3f(GLint location, GLfloat v0,
//      GLfloat v1, GLfloat v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_111glUniform3fEifff(
    QOpenGLFunctions_3_1 *self,
    GLint location,
    GLfloat v0,
    GLfloat v1,
    GLfloat v2) {
  self->glUniform3f(location, v0, v1, v2);
}

//  void QOpenGLFunctions_3_1::glUniform2f(GLint location, GLfloat v0,
//      GLfloat v1)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_111glUniform2fEiff(
    QOpenGLFunctions_3_1 *self,
    GLint location,
    GLfloat v0,
    GLfloat v1) {
  self->glUniform2f(location, v0, v1);
}

//  void QOpenGLFunctions_3_1::glUniform1f(GLint location, GLfloat v0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_111glUniform1fEif(
    QOpenGLFunctions_3_1 *self,
    GLint location,
    GLfloat v0) {
  self->glUniform1f(location, v0);
}

//  void QOpenGLFunctions_3_1::glUseProgram(GLuint program)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_112glUseProgramEj(
    QOpenGLFunctions_3_1 *self,
    GLuint program) {
  self->glUseProgram(program);
}

//  void QOpenGLFunctions_3_1::glShaderSource(GLuint shader, GLsizei count,
//      const GLchar *const *string, const GLint *length)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_114glShaderSourceEjiPKPKcPKi(
    QOpenGLFunctions_3_1 *self,
    GLuint shader,
    GLsizei count,
    const GLchar *const *string,
    const GLint *length) {
  self->glShaderSource(shader, count, string, length);
}

//  void QOpenGLFunctions_3_1::glLinkProgram(GLuint program)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_113glLinkProgramEj(
    QOpenGLFunctions_3_1 *self,
    GLuint program) {
  self->glLinkProgram(program);
}

//  GLboolean QOpenGLFunctions_3_1::glIsShader(GLuint shader)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN20QOpenGLFunctions_3_110glIsShaderEj(
    QOpenGLFunctions_3_1 *self,
    GLuint shader) {
  return self->glIsShader(shader);
}

//  GLboolean QOpenGLFunctions_3_1::glIsProgram(GLuint program)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN20QOpenGLFunctions_3_111glIsProgramEj(
    QOpenGLFunctions_3_1 *self,
    GLuint program) {
  return self->glIsProgram(program);
}

//  void QOpenGLFunctions_3_1::glGetVertexAttribPointerv(GLuint index, GLenum
//      pname, GLvoid **pointer)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_125glGetVertexAttribPointervEjjPPv(
    QOpenGLFunctions_3_1 *self,
    GLuint index,
    GLenum pname,
    GLvoid **pointer) {
  self->glGetVertexAttribPointerv(index, pname, pointer);
}

//  void QOpenGLFunctions_3_1::glGetVertexAttribiv(GLuint index, GLenum
//      pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_119glGetVertexAttribivEjjPi(
    QOpenGLFunctions_3_1 *self,
    GLuint index,
    GLenum pname,
    GLint *params) {
  self->glGetVertexAttribiv(index, pname, params);
}

//  void QOpenGLFunctions_3_1::glGetVertexAttribfv(GLuint index, GLenum
//      pname, GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_119glGetVertexAttribfvEjjPf(
    QOpenGLFunctions_3_1 *self,
    GLuint index,
    GLenum pname,
    GLfloat *params) {
  self->glGetVertexAttribfv(index, pname, params);
}

//  void QOpenGLFunctions_3_1::glGetVertexAttribdv(GLuint index, GLenum
//      pname, GLdouble *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_119glGetVertexAttribdvEjjPd(
    QOpenGLFunctions_3_1 *self,
    GLuint index,
    GLenum pname,
    GLdouble *params) {
  self->glGetVertexAttribdv(index, pname, params);
}

//  void QOpenGLFunctions_3_1::glGetUniformiv(GLuint program, GLint location,
//      GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_114glGetUniformivEjiPi(
    QOpenGLFunctions_3_1 *self,
    GLuint program,
    GLint location,
    GLint *params) {
  self->glGetUniformiv(program, location, params);
}

//  void QOpenGLFunctions_3_1::glGetUniformfv(GLuint program, GLint location,
//      GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_114glGetUniformfvEjiPf(
    QOpenGLFunctions_3_1 *self,
    GLuint program,
    GLint location,
    GLfloat *params) {
  self->glGetUniformfv(program, location, params);
}

//  GLint QOpenGLFunctions_3_1::glGetUniformLocation(GLuint program, const
//      GLchar *name)
extern "C" Q_DECL_EXPORT
GLint ritual_ZN20QOpenGLFunctions_3_120glGetUniformLocationEjPKc(
    QOpenGLFunctions_3_1 *self,
    GLuint program,
    const GLchar *name) {
  return self->glGetUniformLocation(program, name);
}

//  void QOpenGLFunctions_3_1::glGetShaderSource(GLuint shader, GLsizei
//      bufSize, GLsizei *length, GLchar *source)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_117glGetShaderSourceEjiPiPc(
    QOpenGLFunctions_3_1 *self,
    GLuint shader,
    GLsizei bufSize,
    GLsizei *length,
    GLchar *source) {
  self->glGetShaderSource(shader, bufSize, length, source);
}

//  void QOpenGLFunctions_3_1::glGetShaderInfoLog(GLuint shader, GLsizei
//      bufSize, GLsizei *length, GLchar *infoLog)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_118glGetShaderInfoLogEjiPiPc(
    QOpenGLFunctions_3_1 *self,
    GLuint shader,
    GLsizei bufSize,
    GLsizei *length,
    GLchar *infoLog) {
  self->glGetShaderInfoLog(shader, bufSize, length, infoLog);
}

//  void QOpenGLFunctions_3_1::glGetShaderiv(GLuint shader, GLenum pname,
//      GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_113glGetShaderivEjjPi(
    QOpenGLFunctions_3_1 *self,
    GLuint shader,
    GLenum pname,
    GLint *params) {
  self->glGetShaderiv(shader, pname, params);
}

//  void QOpenGLFunctions_3_1::glGetProgramInfoLog(GLuint program, GLsizei
//      bufSize, GLsizei *length, GLchar *infoLog)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_119glGetProgramInfoLogEjiPiPc(
    QOpenGLFunctions_3_1 *self,
    GLuint program,
    GLsizei bufSize,
    GLsizei *length,
    GLchar *infoLog) {
  self->glGetProgramInfoLog(program, bufSize, length, infoLog);
}

//  void QOpenGLFunctions_3_1::glGetProgramiv(GLuint program, GLenum pname,
//      GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_114glGetProgramivEjjPi(
    QOpenGLFunctions_3_1 *self,
    GLuint program,
    GLenum pname,
    GLint *params) {
  self->glGetProgramiv(program, pname, params);
}

//  GLint QOpenGLFunctions_3_1::glGetAttribLocation(GLuint program, const
//      GLchar *name)
extern "C" Q_DECL_EXPORT
GLint ritual_ZN20QOpenGLFunctions_3_119glGetAttribLocationEjPKc(
    QOpenGLFunctions_3_1 *self,
    GLuint program,
    const GLchar *name) {
  return self->glGetAttribLocation(program, name);
}

//  void QOpenGLFunctions_3_1::glGetAttachedShaders(GLuint program, GLsizei
//      maxCount, GLsizei *count, GLuint *obj)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_120glGetAttachedShadersEjiPiPj(
    QOpenGLFunctions_3_1 *self,
    GLuint program,
    GLsizei maxCount,
    GLsizei *count,
    GLuint *obj) {
  self->glGetAttachedShaders(program, maxCount, count, obj);
}

//  void QOpenGLFunctions_3_1::glGetActiveUniform(GLuint program, GLuint
//      index, GLsizei bufSize, GLsizei *length, GLint *size, GLenum *type,
//      GLchar *name)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_118glGetActiveUniformEjjiPiS0_PjPc(
    QOpenGLFunctions_3_1 *self,
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

//  void QOpenGLFunctions_3_1::glGetActiveAttrib(GLuint program, GLuint
//      index, GLsizei bufSize, GLsizei *length, GLint *size, GLenum *type,
//      GLchar *name)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_117glGetActiveAttribEjjiPiS0_PjPc(
    QOpenGLFunctions_3_1 *self,
    GLuint program,
    GLuint index,
    GLsizei bufSize,
    GLsizei *length,
    GLint *size,
    GLenum *type,
    GLchar *name) {
  self->glGetActiveAttrib(program, index, bufSize, length, size, type, name);
}

//  void QOpenGLFunctions_3_1::glEnableVertexAttribArray(GLuint index)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_125glEnableVertexAttribArrayEj(
    QOpenGLFunctions_3_1 *self,
    GLuint index) {
  self->glEnableVertexAttribArray(index);
}

//  void QOpenGLFunctions_3_1::glDisableVertexAttribArray(GLuint index)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_126glDisableVertexAttribArrayEj(
    QOpenGLFunctions_3_1 *self,
    GLuint index) {
  self->glDisableVertexAttribArray(index);
}

//  void QOpenGLFunctions_3_1::glDetachShader(GLuint program, GLuint shader)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_114glDetachShaderEjj(
    QOpenGLFunctions_3_1 *self,
    GLuint program,
    GLuint shader) {
  self->glDetachShader(program, shader);
}

//  void QOpenGLFunctions_3_1::glDeleteShader(GLuint shader)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_114glDeleteShaderEj(
    QOpenGLFunctions_3_1 *self,
    GLuint shader) {
  self->glDeleteShader(shader);
}

//  void QOpenGLFunctions_3_1::glDeleteProgram(GLuint program)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_115glDeleteProgramEj(
    QOpenGLFunctions_3_1 *self,
    GLuint program) {
  self->glDeleteProgram(program);
}

//  GLuint QOpenGLFunctions_3_1::glCreateShader(GLenum type)
extern "C" Q_DECL_EXPORT
GLuint ritual_ZN20QOpenGLFunctions_3_114glCreateShaderEj(
    QOpenGLFunctions_3_1 *self,
    GLenum type) {
  return self->glCreateShader(type);
}

//  GLuint QOpenGLFunctions_3_1::glCreateProgram()
extern "C" Q_DECL_EXPORT
GLuint ritual_ZN20QOpenGLFunctions_3_115glCreateProgramEv(
    QOpenGLFunctions_3_1 *self) {
  return self->glCreateProgram();
}

//  void QOpenGLFunctions_3_1::glCompileShader(GLuint shader)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_115glCompileShaderEj(
    QOpenGLFunctions_3_1 *self,
    GLuint shader) {
  self->glCompileShader(shader);
}

//  void QOpenGLFunctions_3_1::glBindAttribLocation(GLuint program, GLuint
//      index, const GLchar *name)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_120glBindAttribLocationEjjPKc(
    QOpenGLFunctions_3_1 *self,
    GLuint program,
    GLuint index,
    const GLchar *name) {
  self->glBindAttribLocation(program, index, name);
}

//  void QOpenGLFunctions_3_1::glAttachShader(GLuint program, GLuint shader)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_114glAttachShaderEjj(
    QOpenGLFunctions_3_1 *self,
    GLuint program,
    GLuint shader) {
  self->glAttachShader(program, shader);
}

//  void QOpenGLFunctions_3_1::glStencilMaskSeparate(GLenum face, GLuint
//      mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_121glStencilMaskSeparateEjj(
    QOpenGLFunctions_3_1 *self,
    GLenum face,
    GLuint mask) {
  self->glStencilMaskSeparate(face, mask);
}

//  void QOpenGLFunctions_3_1::glStencilFuncSeparate(GLenum face, GLenum
//      func, GLint ref, GLuint mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_121glStencilFuncSeparateEjjij(
    QOpenGLFunctions_3_1 *self,
    GLenum face,
    GLenum func,
    GLint ref,
    GLuint mask) {
  self->glStencilFuncSeparate(face, func, ref, mask);
}

//  void QOpenGLFunctions_3_1::glStencilOpSeparate(GLenum face, GLenum sfail,
//      GLenum dpfail, GLenum dppass)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_119glStencilOpSeparateEjjjj(
    QOpenGLFunctions_3_1 *self,
    GLenum face,
    GLenum sfail,
    GLenum dpfail,
    GLenum dppass) {
  self->glStencilOpSeparate(face, sfail, dpfail, dppass);
}

//  void QOpenGLFunctions_3_1::glDrawBuffers(GLsizei n, const GLenum *bufs)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_113glDrawBuffersEiPKj(
    QOpenGLFunctions_3_1 *self,
    GLsizei n,
    const GLenum *bufs) {
  self->glDrawBuffers(n, bufs);
}

//  void QOpenGLFunctions_3_1::glBlendEquationSeparate(GLenum modeRGB, GLenum
//      modeAlpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_123glBlendEquationSeparateEjj(
    QOpenGLFunctions_3_1 *self,
    GLenum modeRGB,
    GLenum modeAlpha) {
  self->glBlendEquationSeparate(modeRGB, modeAlpha);
}

//  void QOpenGLFunctions_3_1::glUniformMatrix4x3fv(GLint location, GLsizei
//      count, GLboolean transpose, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_120glUniformMatrix4x3fvEiihPKf(
    QOpenGLFunctions_3_1 *self,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLfloat *value) {
  self->glUniformMatrix4x3fv(location, count, transpose, value);
}

//  void QOpenGLFunctions_3_1::glUniformMatrix3x4fv(GLint location, GLsizei
//      count, GLboolean transpose, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_120glUniformMatrix3x4fvEiihPKf(
    QOpenGLFunctions_3_1 *self,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLfloat *value) {
  self->glUniformMatrix3x4fv(location, count, transpose, value);
}

//  void QOpenGLFunctions_3_1::glUniformMatrix4x2fv(GLint location, GLsizei
//      count, GLboolean transpose, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_120glUniformMatrix4x2fvEiihPKf(
    QOpenGLFunctions_3_1 *self,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLfloat *value) {
  self->glUniformMatrix4x2fv(location, count, transpose, value);
}

//  void QOpenGLFunctions_3_1::glUniformMatrix2x4fv(GLint location, GLsizei
//      count, GLboolean transpose, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_120glUniformMatrix2x4fvEiihPKf(
    QOpenGLFunctions_3_1 *self,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLfloat *value) {
  self->glUniformMatrix2x4fv(location, count, transpose, value);
}

//  void QOpenGLFunctions_3_1::glUniformMatrix3x2fv(GLint location, GLsizei
//      count, GLboolean transpose, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_120glUniformMatrix3x2fvEiihPKf(
    QOpenGLFunctions_3_1 *self,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLfloat *value) {
  self->glUniformMatrix3x2fv(location, count, transpose, value);
}

//  void QOpenGLFunctions_3_1::glUniformMatrix2x3fv(GLint location, GLsizei
//      count, GLboolean transpose, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_120glUniformMatrix2x3fvEiihPKf(
    QOpenGLFunctions_3_1 *self,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLfloat *value) {
  self->glUniformMatrix2x3fv(location, count, transpose, value);
}

//  GLboolean QOpenGLFunctions_3_1::glIsVertexArray(GLuint array)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN20QOpenGLFunctions_3_115glIsVertexArrayEj(
    QOpenGLFunctions_3_1 *self,
    GLuint array) {
  return self->glIsVertexArray(array);
}

//  void QOpenGLFunctions_3_1::glGenVertexArrays(GLsizei n, GLuint *arrays)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_117glGenVertexArraysEiPj(
    QOpenGLFunctions_3_1 *self,
    GLsizei n,
    GLuint *arrays) {
  self->glGenVertexArrays(n, arrays);
}

//  void QOpenGLFunctions_3_1::glDeleteVertexArrays(GLsizei n, const GLuint
//      *arrays)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_120glDeleteVertexArraysEiPKj(
    QOpenGLFunctions_3_1 *self,
    GLsizei n,
    const GLuint *arrays) {
  self->glDeleteVertexArrays(n, arrays);
}

//  void QOpenGLFunctions_3_1::glBindVertexArray(GLuint array)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_117glBindVertexArrayEj(
    QOpenGLFunctions_3_1 *self,
    GLuint array) {
  self->glBindVertexArray(array);
}

//  void QOpenGLFunctions_3_1::glFlushMappedBufferRange(GLenum target,
//      GLintptr offset, GLsizeiptr length)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_124glFlushMappedBufferRangeEjll(
    QOpenGLFunctions_3_1 *self,
    GLenum target,
    long long offset,
    long long length) {
  self->glFlushMappedBufferRange(target, offset, length);
}

//  GLvoid *QOpenGLFunctions_3_1::glMapBufferRange(GLenum target, GLintptr
//      offset, GLsizeiptr length, GLbitfield access)
extern "C" Q_DECL_EXPORT
GLvoid *ritual_ZN20QOpenGLFunctions_3_116glMapBufferRangeEjllj(
    QOpenGLFunctions_3_1 *self,
    GLenum target,
    long long offset,
    long long length,
    GLbitfield access) {
  return self->glMapBufferRange(target, offset, length, access);
}

//  void QOpenGLFunctions_3_1::glFramebufferTextureLayer(GLenum target,
//      GLenum attachment, GLuint texture, GLint level, GLint layer)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_125glFramebufferTextureLayerEjjjii(
    QOpenGLFunctions_3_1 *self,
    GLenum target,
    GLenum attachment,
    GLuint texture,
    GLint level,
    GLint layer) {
  self->glFramebufferTextureLayer(target, attachment, texture, level, layer);
}

//  void QOpenGLFunctions_3_1::glRenderbufferStorageMultisample(GLenum
//      target, GLsizei samples, GLenum internalformat, GLsizei width,
//      GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_132glRenderbufferStorageMultisampleEjijii(
    QOpenGLFunctions_3_1 *self,
    GLenum target,
    GLsizei samples,
    GLenum internalformat,
    GLsizei width,
    GLsizei height) {
  self->glRenderbufferStorageMultisample(
      target,
      samples,
      internalformat,
      width,
      height);
}

//  void QOpenGLFunctions_3_1::glBlitFramebuffer(GLint srcX0, GLint srcY0,
//      GLint srcX1, GLint srcY1, GLint dstX0, GLint dstY0, GLint dstX1,
//      GLint dstY1, GLbitfield mask, GLenum filter)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_117glBlitFramebufferEiiiiiiiijj(
    QOpenGLFunctions_3_1 *self,
    GLint srcX0,
    GLint srcY0,
    GLint srcX1,
    GLint srcY1,
    GLint dstX0,
    GLint dstY0,
    GLint dstX1,
    GLint dstY1,
    GLbitfield mask,
    GLenum filter) {
  self->glBlitFramebuffer(
      srcX0,
      srcY0,
      srcX1,
      srcY1,
      dstX0,
      dstY0,
      dstX1,
      dstY1,
      mask,
      filter);
}

//  void QOpenGLFunctions_3_1::glGenerateMipmap(GLenum target)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_116glGenerateMipmapEj(
    QOpenGLFunctions_3_1 *self,
    GLenum target) {
  self->glGenerateMipmap(target);
}

//  void QOpenGLFunctions_3_1::glGetFramebufferAttachmentParameteriv(GLenum
//      target, GLenum attachment, GLenum pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_137glGetFramebufferAttachmentParameterivEjjjPi(
    QOpenGLFunctions_3_1 *self,
    GLenum target,
    GLenum attachment,
    GLenum pname,
    GLint *params) {
  self->glGetFramebufferAttachmentParameteriv(
      target,
      attachment,
      pname,
      params);
}

//  void QOpenGLFunctions_3_1::glFramebufferRenderbuffer(GLenum target,
//      GLenum attachment, GLenum renderbuffertarget, GLuint renderbuffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_125glFramebufferRenderbufferEjjjj(
    QOpenGLFunctions_3_1 *self,
    GLenum target,
    GLenum attachment,
    GLenum renderbuffertarget,
    GLuint renderbuffer) {
  self->glFramebufferRenderbuffer(
      target,
      attachment,
      renderbuffertarget,
      renderbuffer);
}

//  void QOpenGLFunctions_3_1::glFramebufferTexture3D(GLenum target, GLenum
//      attachment, GLenum textarget, GLuint texture, GLint level, GLint
//      zoffset)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_122glFramebufferTexture3DEjjjjii(
    QOpenGLFunctions_3_1 *self,
    GLenum target,
    GLenum attachment,
    GLenum textarget,
    GLuint texture,
    GLint level,
    GLint zoffset) {
  self->glFramebufferTexture3D(
      target,
      attachment,
      textarget,
      texture,
      level,
      zoffset);
}

//  void QOpenGLFunctions_3_1::glFramebufferTexture2D(GLenum target, GLenum
//      attachment, GLenum textarget, GLuint texture, GLint level)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_122glFramebufferTexture2DEjjjji(
    QOpenGLFunctions_3_1 *self,
    GLenum target,
    GLenum attachment,
    GLenum textarget,
    GLuint texture,
    GLint level) {
  self->glFramebufferTexture2D(
      target,
      attachment,
      textarget,
      texture,
      level);
}

//  void QOpenGLFunctions_3_1::glFramebufferTexture1D(GLenum target, GLenum
//      attachment, GLenum textarget, GLuint texture, GLint level)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_122glFramebufferTexture1DEjjjji(
    QOpenGLFunctions_3_1 *self,
    GLenum target,
    GLenum attachment,
    GLenum textarget,
    GLuint texture,
    GLint level) {
  self->glFramebufferTexture1D(
      target,
      attachment,
      textarget,
      texture,
      level);
}

//  GLenum QOpenGLFunctions_3_1::glCheckFramebufferStatus(GLenum target)
extern "C" Q_DECL_EXPORT
GLenum ritual_ZN20QOpenGLFunctions_3_124glCheckFramebufferStatusEj(
    QOpenGLFunctions_3_1 *self,
    GLenum target) {
  return self->glCheckFramebufferStatus(target);
}

//  void QOpenGLFunctions_3_1::glGenFramebuffers(GLsizei n, GLuint
//      *framebuffers)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_117glGenFramebuffersEiPj(
    QOpenGLFunctions_3_1 *self,
    GLsizei n,
    GLuint *framebuffers) {
  self->glGenFramebuffers(n, framebuffers);
}

//  void QOpenGLFunctions_3_1::glDeleteFramebuffers(GLsizei n, const GLuint
//      *framebuffers)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_120glDeleteFramebuffersEiPKj(
    QOpenGLFunctions_3_1 *self,
    GLsizei n,
    const GLuint *framebuffers) {
  self->glDeleteFramebuffers(n, framebuffers);
}

//  void QOpenGLFunctions_3_1::glBindFramebuffer(GLenum target, GLuint
//      framebuffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_117glBindFramebufferEjj(
    QOpenGLFunctions_3_1 *self,
    GLenum target,
    GLuint framebuffer) {
  self->glBindFramebuffer(target, framebuffer);
}

//  GLboolean QOpenGLFunctions_3_1::glIsFramebuffer(GLuint framebuffer)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN20QOpenGLFunctions_3_115glIsFramebufferEj(
    QOpenGLFunctions_3_1 *self,
    GLuint framebuffer) {
  return self->glIsFramebuffer(framebuffer);
}

//  void QOpenGLFunctions_3_1::glGetRenderbufferParameteriv(GLenum target,
//      GLenum pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_128glGetRenderbufferParameterivEjjPi(
    QOpenGLFunctions_3_1 *self,
    GLenum target,
    GLenum pname,
    GLint *params) {
  self->glGetRenderbufferParameteriv(target, pname, params);
}

//  void QOpenGLFunctions_3_1::glRenderbufferStorage(GLenum target, GLenum
//      internalformat, GLsizei width, GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_121glRenderbufferStorageEjjii(
    QOpenGLFunctions_3_1 *self,
    GLenum target,
    GLenum internalformat,
    GLsizei width,
    GLsizei height) {
  self->glRenderbufferStorage(target, internalformat, width, height);
}

//  void QOpenGLFunctions_3_1::glGenRenderbuffers(GLsizei n, GLuint
//      *renderbuffers)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_118glGenRenderbuffersEiPj(
    QOpenGLFunctions_3_1 *self,
    GLsizei n,
    GLuint *renderbuffers) {
  self->glGenRenderbuffers(n, renderbuffers);
}

//  void QOpenGLFunctions_3_1::glDeleteRenderbuffers(GLsizei n, const GLuint
//      *renderbuffers)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_121glDeleteRenderbuffersEiPKj(
    QOpenGLFunctions_3_1 *self,
    GLsizei n,
    const GLuint *renderbuffers) {
  self->glDeleteRenderbuffers(n, renderbuffers);
}

//  void QOpenGLFunctions_3_1::glBindRenderbuffer(GLenum target, GLuint
//      renderbuffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_118glBindRenderbufferEjj(
    QOpenGLFunctions_3_1 *self,
    GLenum target,
    GLuint renderbuffer) {
  self->glBindRenderbuffer(target, renderbuffer);
}

//  GLboolean QOpenGLFunctions_3_1::glIsRenderbuffer(GLuint renderbuffer)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN20QOpenGLFunctions_3_116glIsRenderbufferEj(
    QOpenGLFunctions_3_1 *self,
    GLuint renderbuffer) {
  return self->glIsRenderbuffer(renderbuffer);
}

//  const GLubyte *QOpenGLFunctions_3_1::glGetStringi(GLenum name, GLuint
//      index)
extern "C" Q_DECL_EXPORT
const GLubyte *ritual_ZN20QOpenGLFunctions_3_112glGetStringiEjj(
    QOpenGLFunctions_3_1 *self,
    GLenum name,
    GLuint index) {
  return self->glGetStringi(name, index);
}

//  void QOpenGLFunctions_3_1::glClearBufferfi(GLenum buffer, GLint
//      drawbuffer, GLfloat depth, GLint stencil)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_115glClearBufferfiEjifi(
    QOpenGLFunctions_3_1 *self,
    GLenum buffer,
    GLint drawbuffer,
    GLfloat depth,
    GLint stencil) {
  self->glClearBufferfi(buffer, drawbuffer, depth, stencil);
}

//  void QOpenGLFunctions_3_1::glClearBufferfv(GLenum buffer, GLint
//      drawbuffer, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_115glClearBufferfvEjiPKf(
    QOpenGLFunctions_3_1 *self,
    GLenum buffer,
    GLint drawbuffer,
    const GLfloat *value) {
  self->glClearBufferfv(buffer, drawbuffer, value);
}

//  void QOpenGLFunctions_3_1::glClearBufferuiv(GLenum buffer, GLint
//      drawbuffer, const GLuint *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_116glClearBufferuivEjiPKj(
    QOpenGLFunctions_3_1 *self,
    GLenum buffer,
    GLint drawbuffer,
    const GLuint *value) {
  self->glClearBufferuiv(buffer, drawbuffer, value);
}

//  void QOpenGLFunctions_3_1::glClearBufferiv(GLenum buffer, GLint
//      drawbuffer, const GLint *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_115glClearBufferivEjiPKi(
    QOpenGLFunctions_3_1 *self,
    GLenum buffer,
    GLint drawbuffer,
    const GLint *value) {
  self->glClearBufferiv(buffer, drawbuffer, value);
}

//  void QOpenGLFunctions_3_1::glGetTexParameterIuiv(GLenum target, GLenum
//      pname, GLuint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_121glGetTexParameterIuivEjjPj(
    QOpenGLFunctions_3_1 *self,
    GLenum target,
    GLenum pname,
    GLuint *params) {
  self->glGetTexParameterIuiv(target, pname, params);
}

//  void QOpenGLFunctions_3_1::glGetTexParameterIiv(GLenum target, GLenum
//      pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_120glGetTexParameterIivEjjPi(
    QOpenGLFunctions_3_1 *self,
    GLenum target,
    GLenum pname,
    GLint *params) {
  self->glGetTexParameterIiv(target, pname, params);
}

//  void QOpenGLFunctions_3_1::glTexParameterIuiv(GLenum target, GLenum
//      pname, const GLuint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_118glTexParameterIuivEjjPKj(
    QOpenGLFunctions_3_1 *self,
    GLenum target,
    GLenum pname,
    const GLuint *params) {
  self->glTexParameterIuiv(target, pname, params);
}

//  void QOpenGLFunctions_3_1::glTexParameterIiv(GLenum target, GLenum pname,
//      const GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_117glTexParameterIivEjjPKi(
    QOpenGLFunctions_3_1 *self,
    GLenum target,
    GLenum pname,
    const GLint *params) {
  self->glTexParameterIiv(target, pname, params);
}

//  void QOpenGLFunctions_3_1::glUniform4uiv(GLint location, GLsizei count,
//      const GLuint *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_113glUniform4uivEiiPKj(
    QOpenGLFunctions_3_1 *self,
    GLint location,
    GLsizei count,
    const GLuint *value) {
  self->glUniform4uiv(location, count, value);
}

//  void QOpenGLFunctions_3_1::glUniform3uiv(GLint location, GLsizei count,
//      const GLuint *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_113glUniform3uivEiiPKj(
    QOpenGLFunctions_3_1 *self,
    GLint location,
    GLsizei count,
    const GLuint *value) {
  self->glUniform3uiv(location, count, value);
}

//  void QOpenGLFunctions_3_1::glUniform2uiv(GLint location, GLsizei count,
//      const GLuint *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_113glUniform2uivEiiPKj(
    QOpenGLFunctions_3_1 *self,
    GLint location,
    GLsizei count,
    const GLuint *value) {
  self->glUniform2uiv(location, count, value);
}

//  void QOpenGLFunctions_3_1::glUniform1uiv(GLint location, GLsizei count,
//      const GLuint *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_113glUniform1uivEiiPKj(
    QOpenGLFunctions_3_1 *self,
    GLint location,
    GLsizei count,
    const GLuint *value) {
  self->glUniform1uiv(location, count, value);
}

//  void QOpenGLFunctions_3_1::glUniform4ui(GLint location, GLuint v0, GLuint
//      v1, GLuint v2, GLuint v3)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_112glUniform4uiEijjjj(
    QOpenGLFunctions_3_1 *self,
    GLint location,
    GLuint v0,
    GLuint v1,
    GLuint v2,
    GLuint v3) {
  self->glUniform4ui(location, v0, v1, v2, v3);
}

//  void QOpenGLFunctions_3_1::glUniform3ui(GLint location, GLuint v0, GLuint
//      v1, GLuint v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_112glUniform3uiEijjj(
    QOpenGLFunctions_3_1 *self,
    GLint location,
    GLuint v0,
    GLuint v1,
    GLuint v2) {
  self->glUniform3ui(location, v0, v1, v2);
}

//  void QOpenGLFunctions_3_1::glUniform2ui(GLint location, GLuint v0, GLuint
//      v1)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_112glUniform2uiEijj(
    QOpenGLFunctions_3_1 *self,
    GLint location,
    GLuint v0,
    GLuint v1) {
  self->glUniform2ui(location, v0, v1);
}

//  void QOpenGLFunctions_3_1::glUniform1ui(GLint location, GLuint v0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_112glUniform1uiEij(
    QOpenGLFunctions_3_1 *self,
    GLint location,
    GLuint v0) {
  self->glUniform1ui(location, v0);
}

//  GLint QOpenGLFunctions_3_1::glGetFragDataLocation(GLuint program, const
//      GLchar *name)
extern "C" Q_DECL_EXPORT
GLint ritual_ZN20QOpenGLFunctions_3_121glGetFragDataLocationEjPKc(
    QOpenGLFunctions_3_1 *self,
    GLuint program,
    const GLchar *name) {
  return self->glGetFragDataLocation(program, name);
}

//  void QOpenGLFunctions_3_1::glBindFragDataLocation(GLuint program, GLuint
//      color, const GLchar *name)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_122glBindFragDataLocationEjjPKc(
    QOpenGLFunctions_3_1 *self,
    GLuint program,
    GLuint color,
    const GLchar *name) {
  self->glBindFragDataLocation(program, color, name);
}

//  void QOpenGLFunctions_3_1::glGetUniformuiv(GLuint program, GLint
//      location, GLuint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_115glGetUniformuivEjiPj(
    QOpenGLFunctions_3_1 *self,
    GLuint program,
    GLint location,
    GLuint *params) {
  self->glGetUniformuiv(program, location, params);
}

//  void QOpenGLFunctions_3_1::glGetVertexAttribIuiv(GLuint index, GLenum
//      pname, GLuint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_121glGetVertexAttribIuivEjjPj(
    QOpenGLFunctions_3_1 *self,
    GLuint index,
    GLenum pname,
    GLuint *params) {
  self->glGetVertexAttribIuiv(index, pname, params);
}

//  void QOpenGLFunctions_3_1::glGetVertexAttribIiv(GLuint index, GLenum
//      pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_120glGetVertexAttribIivEjjPi(
    QOpenGLFunctions_3_1 *self,
    GLuint index,
    GLenum pname,
    GLint *params) {
  self->glGetVertexAttribIiv(index, pname, params);
}

//  void QOpenGLFunctions_3_1::glVertexAttribIPointer(GLuint index, GLint
//      size, GLenum type, GLsizei stride, const GLvoid *pointer)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_122glVertexAttribIPointerEjijiPKv(
    QOpenGLFunctions_3_1 *self,
    GLuint index,
    GLint size,
    GLenum type,
    GLsizei stride,
    const GLvoid *pointer) {
  self->glVertexAttribIPointer(index, size, type, stride, pointer);
}

//  void QOpenGLFunctions_3_1::glEndConditionalRender()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_122glEndConditionalRenderEv(
    QOpenGLFunctions_3_1 *self) {
  self->glEndConditionalRender();
}

//  void QOpenGLFunctions_3_1::glBeginConditionalRender(GLuint id, GLenum
//      mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_124glBeginConditionalRenderEjj(
    QOpenGLFunctions_3_1 *self,
    GLuint id,
    GLenum mode) {
  self->glBeginConditionalRender(id, mode);
}

//  void QOpenGLFunctions_3_1::glClampColor(GLenum target, GLenum clamp)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_112glClampColorEjj(
    QOpenGLFunctions_3_1 *self,
    GLenum target,
    GLenum clamp) {
  self->glClampColor(target, clamp);
}

//  void QOpenGLFunctions_3_1::glGetTransformFeedbackVarying(GLuint program,
//      GLuint index, GLsizei bufSize, GLsizei *length, GLsizei *size, GLenum
//      *type, GLchar *name)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_129glGetTransformFeedbackVaryingEjjiPiS0_PjPc(
    QOpenGLFunctions_3_1 *self,
    GLuint program,
    GLuint index,
    GLsizei bufSize,
    GLsizei *length,
    GLsizei *size,
    GLenum *type,
    GLchar *name) {
  self->glGetTransformFeedbackVarying(
      program,
      index,
      bufSize,
      length,
      size,
      type,
      name);
}

//  void QOpenGLFunctions_3_1::glTransformFeedbackVaryings(GLuint program,
//      GLsizei count, const GLchar *const *varyings, GLenum bufferMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_127glTransformFeedbackVaryingsEjiPKPKcj(
    QOpenGLFunctions_3_1 *self,
    GLuint program,
    GLsizei count,
    const GLchar *const *varyings,
    GLenum bufferMode) {
  self->glTransformFeedbackVaryings(program, count, varyings, bufferMode);
}

//  void QOpenGLFunctions_3_1::glBindBufferBase(GLenum target, GLuint index,
//      GLuint buffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_116glBindBufferBaseEjjj(
    QOpenGLFunctions_3_1 *self,
    GLenum target,
    GLuint index,
    GLuint buffer) {
  self->glBindBufferBase(target, index, buffer);
}

//  void QOpenGLFunctions_3_1::glBindBufferRange(GLenum target, GLuint index,
//      GLuint buffer, GLintptr offset, GLsizeiptr size)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_117glBindBufferRangeEjjjll(
    QOpenGLFunctions_3_1 *self,
    GLenum target,
    GLuint index,
    GLuint buffer,
    long long offset,
    long long size) {
  self->glBindBufferRange(target, index, buffer, offset, size);
}

//  void QOpenGLFunctions_3_1::glEndTransformFeedback()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_122glEndTransformFeedbackEv(
    QOpenGLFunctions_3_1 *self) {
  self->glEndTransformFeedback();
}

//  void QOpenGLFunctions_3_1::glBeginTransformFeedback(GLenum primitiveMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_124glBeginTransformFeedbackEj(
    QOpenGLFunctions_3_1 *self,
    GLenum primitiveMode) {
  self->glBeginTransformFeedback(primitiveMode);
}

//  GLboolean QOpenGLFunctions_3_1::glIsEnabledi(GLenum target, GLuint index)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN20QOpenGLFunctions_3_112glIsEnablediEjj(
    QOpenGLFunctions_3_1 *self,
    GLenum target,
    GLuint index) {
  return self->glIsEnabledi(target, index);
}

//  void QOpenGLFunctions_3_1::glDisablei(GLenum target, GLuint index)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_110glDisableiEjj(
    QOpenGLFunctions_3_1 *self,
    GLenum target,
    GLuint index) {
  self->glDisablei(target, index);
}

//  void QOpenGLFunctions_3_1::glEnablei(GLenum target, GLuint index)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_19glEnableiEjj(
    QOpenGLFunctions_3_1 *self,
    GLenum target,
    GLuint index) {
  self->glEnablei(target, index);
}

//  void QOpenGLFunctions_3_1::glGetIntegeri_v(GLenum target, GLuint index,
//      GLint *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_115glGetIntegeri_vEjjPi(
    QOpenGLFunctions_3_1 *self,
    GLenum target,
    GLuint index,
    GLint *data) {
  self->glGetIntegeri_v(target, index, data);
}

//  void QOpenGLFunctions_3_1::glGetBooleani_v(GLenum target, GLuint index,
//      GLboolean *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_115glGetBooleani_vEjjPh(
    QOpenGLFunctions_3_1 *self,
    GLenum target,
    GLuint index,
    GLboolean *data) {
  self->glGetBooleani_v(target, index, data);
}

//  void QOpenGLFunctions_3_1::glColorMaski(GLuint index, GLboolean r,
//      GLboolean g, GLboolean b, GLboolean a)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_112glColorMaskiEjhhhh(
    QOpenGLFunctions_3_1 *self,
    GLuint index,
    GLboolean r,
    GLboolean g,
    GLboolean b,
    GLboolean a) {
  self->glColorMaski(index, r, g, b, a);
}

//  void QOpenGLFunctions_3_1::glCopyBufferSubData(GLenum readTarget, GLenum
//      writeTarget, GLintptr readOffset, GLintptr writeOffset, GLsizeiptr
//      size)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_119glCopyBufferSubDataEjjlll(
    QOpenGLFunctions_3_1 *self,
    GLenum readTarget,
    GLenum writeTarget,
    long long readOffset,
    long long writeOffset,
    long long size) {
  self->glCopyBufferSubData(
      readTarget,
      writeTarget,
      readOffset,
      writeOffset,
      size);
}

//  void QOpenGLFunctions_3_1::glUniformBlockBinding(GLuint program, GLuint
//      uniformBlockIndex, GLuint uniformBlockBinding)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_121glUniformBlockBindingEjjj(
    QOpenGLFunctions_3_1 *self,
    GLuint program,
    GLuint uniformBlockIndex,
    GLuint uniformBlockBinding) {
  self->glUniformBlockBinding(
      program,
      uniformBlockIndex,
      uniformBlockBinding);
}

//  void QOpenGLFunctions_3_1::glGetActiveUniformBlockName(GLuint program,
//      GLuint uniformBlockIndex, GLsizei bufSize, GLsizei *length, GLchar
//      *uniformBlockName)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_127glGetActiveUniformBlockNameEjjiPiPc(
    QOpenGLFunctions_3_1 *self,
    GLuint program,
    GLuint uniformBlockIndex,
    GLsizei bufSize,
    GLsizei *length,
    GLchar *uniformBlockName) {
  self->glGetActiveUniformBlockName(
      program,
      uniformBlockIndex,
      bufSize,
      length,
      uniformBlockName);
}

//  void QOpenGLFunctions_3_1::glGetActiveUniformBlockiv(GLuint program,
//      GLuint uniformBlockIndex, GLenum pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_125glGetActiveUniformBlockivEjjjPi(
    QOpenGLFunctions_3_1 *self,
    GLuint program,
    GLuint uniformBlockIndex,
    GLenum pname,
    GLint *params) {
  self->glGetActiveUniformBlockiv(program, uniformBlockIndex, pname, params);
}

//  GLuint QOpenGLFunctions_3_1::glGetUniformBlockIndex(GLuint program, const
//      GLchar *uniformBlockName)
extern "C" Q_DECL_EXPORT
GLuint ritual_ZN20QOpenGLFunctions_3_122glGetUniformBlockIndexEjPKc(
    QOpenGLFunctions_3_1 *self,
    GLuint program,
    const GLchar *uniformBlockName) {
  return self->glGetUniformBlockIndex(program, uniformBlockName);
}

//  void QOpenGLFunctions_3_1::glGetActiveUniformName(GLuint program, GLuint
//      uniformIndex, GLsizei bufSize, GLsizei *length, GLchar *uniformName)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_122glGetActiveUniformNameEjjiPiPc(
    QOpenGLFunctions_3_1 *self,
    GLuint program,
    GLuint uniformIndex,
    GLsizei bufSize,
    GLsizei *length,
    GLchar *uniformName) {
  self->glGetActiveUniformName(
      program,
      uniformIndex,
      bufSize,
      length,
      uniformName);
}

//  void QOpenGLFunctions_3_1::glGetActiveUniformsiv(GLuint program, GLsizei
//      uniformCount, const GLuint *uniformIndices, GLenum pname, GLint
//      *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_121glGetActiveUniformsivEjiPKjjPi(
    QOpenGLFunctions_3_1 *self,
    GLuint program,
    GLsizei uniformCount,
    const GLuint *uniformIndices,
    GLenum pname,
    GLint *params) {
  self->glGetActiveUniformsiv(
      program,
      uniformCount,
      uniformIndices,
      pname,
      params);
}

//  void QOpenGLFunctions_3_1::glGetUniformIndices(GLuint program, GLsizei
//      uniformCount, const GLchar *const *uniformNames, GLuint
//      *uniformIndices)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_119glGetUniformIndicesEjiPKPKcPj(
    QOpenGLFunctions_3_1 *self,
    GLuint program,
    GLsizei uniformCount,
    const GLchar *const *uniformNames,
    GLuint *uniformIndices) {
  self->glGetUniformIndices(
      program,
      uniformCount,
      uniformNames,
      uniformIndices);
}

//  void QOpenGLFunctions_3_1::glPrimitiveRestartIndex(GLuint index)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_123glPrimitiveRestartIndexEj(
    QOpenGLFunctions_3_1 *self,
    GLuint index) {
  self->glPrimitiveRestartIndex(index);
}

//  void QOpenGLFunctions_3_1::glTexBuffer(GLenum target, GLenum
//      internalformat, GLuint buffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_111glTexBufferEjjj(
    QOpenGLFunctions_3_1 *self,
    GLenum target,
    GLenum internalformat,
    GLuint buffer) {
  self->glTexBuffer(target, internalformat, buffer);
}

//  void QOpenGLFunctions_3_1::glDrawElementsInstanced(GLenum mode, GLsizei
//      count, GLenum type, const GLvoid *indices, GLsizei instancecount)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_123glDrawElementsInstancedEjijPKvi(
    QOpenGLFunctions_3_1 *self,
    GLenum mode,
    GLsizei count,
    GLenum type,
    const GLvoid *indices,
    GLsizei instancecount) {
  self->glDrawElementsInstanced(mode, count, type, indices, instancecount);
}

//  void QOpenGLFunctions_3_1::glDrawArraysInstanced(GLenum mode, GLint
//      first, GLsizei count, GLsizei instancecount)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_121glDrawArraysInstancedEjiii(
    QOpenGLFunctions_3_1 *self,
    GLenum mode,
    GLint first,
    GLsizei count,
    GLsizei instancecount) {
  self->glDrawArraysInstanced(mode, first, count, instancecount);
}

//  bool QOpenGLFunctions_3_1::isContextCompatible(QOpenGLContext *context)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QOpenGLFunctions_3_119isContextCompatibleEP14QOpenGLContext(
    QOpenGLContext *context) {
  return QOpenGLFunctions_3_1::isContextCompatible(context);
}

//  QOpenGLVersionProfile QOpenGLFunctions_3_1::versionProfile()
extern "C" Q_DECL_EXPORT
QOpenGLVersionProfile *ritual_ZN20QOpenGLFunctions_3_114versionProfileEv() {
  return new QOpenGLVersionProfile(QOpenGLFunctions_3_1::versionProfile());
}

//  a Python function taken by a CuteQOpenGLFunctions_3_1, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QOpenGLFunctions_3_1(
    QOpenGLFunctions_3_1 *self,
    const char *key,
    void *call) {
  return static_cast<CuteQOpenGLFunctions_3_1 *>(self)->take(key, call);
}

//  bool QOpenGLFunctions_3_1::initializeOpenGLFunctions()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN20QOpenGLFunctions_3_125initializeOpenGLFunctionsEv(
    QOpenGLFunctions_3_1 *self) {
  return self->QOpenGLFunctions_3_1::initializeOpenGLFunctions();
}

#endif  // !defined(QT_NO_OPENGL) && !QT_CONFIG(opengles2)
#endif  // !QT_CONFIG(opengles2)
