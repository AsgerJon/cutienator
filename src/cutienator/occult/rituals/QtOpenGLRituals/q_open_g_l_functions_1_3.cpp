//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/qopenglfunctions_1_3.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtOpenGL/qtopenglglobal.h>
#if !QT_CONFIG(opengles2)
#if !defined(QT_NO_OPENGL) && !QT_CONFIG(opengles2)
#include <QtOpenGL/QtOpenGL>
#include <QtOpenGL/qopenglfunctions_1_3.h>
#include <QtOpenGL/qopenglversionprofile.h>
#include <cstring>

//  A QOpenGLFunctions_1_3 that Python can take functions over in. Every QOpenGLFunctions_1_3
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL) && !QT_CONFIG(opengles2)
typedef bool (*CuteQOpenGLFunctions_1_3Call0)(const void *, int *);
#endif  // !defined(QT_NO_OPENGL) && !QT_CONFIG(opengles2)
#endif  // !defined(QT_NO_OPENGL)
class CuteQOpenGLFunctions_1_3 : public QOpenGLFunctions_1_3 {
public:
  using QOpenGLFunctions_1_3::QOpenGLFunctions_1_3;
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
  //  bool QOpenGLFunctions_1_3::initializeOpenGLFunctions()
  bool initializeOpenGLFunctions() override {
    if (taken[0]) {
      int handled = 0;
      CuteQOpenGLFunctions_1_3Call0 call = reinterpret_cast<CuteQOpenGLFunctions_1_3Call0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QOpenGLFunctions_1_3::initializeOpenGLFunctions();
  }
#endif  // !defined(QT_NO_OPENGL) && !QT_CONFIG(opengles2)
#endif  // !defined(QT_NO_OPENGL)
};

//  QOpenGLFunctions_1_3::QOpenGLFunctions_1_3()
extern "C" Q_DECL_EXPORT
QOpenGLFunctions_1_3 *ritual_ZN20QOpenGLFunctions_1_3C1Ev() {
  return new CuteQOpenGLFunctions_1_3();
}

//  QOpenGLFunctions_1_3::~QOpenGLFunctions_1_3()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_3D1Ev(QOpenGLFunctions_1_3 *self) {
  delete self;
}

//  bool QOpenGLFunctions_1_3::initializeOpenGLFunctions()
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QOpenGLFunctions_1_325initializeOpenGLFunctionsEv(
    QOpenGLFunctions_1_3 *self) {
  return self->initializeOpenGLFunctions();
}

//  void QOpenGLFunctions_1_3::glViewport(GLint x, GLint y, GLsizei width,
//      GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_310glViewportEiiii(
    QOpenGLFunctions_1_3 *self,
    GLint x,
    GLint y,
    GLsizei width,
    GLsizei height) {
  self->glViewport(x, y, width, height);
}

//  void QOpenGLFunctions_1_3::glDepthRange(GLdouble nearVal, GLdouble
//      farVal)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_312glDepthRangeEdd(
    QOpenGLFunctions_1_3 *self,
    GLdouble nearVal,
    GLdouble farVal) {
  self->glDepthRange(nearVal, farVal);
}

//  GLboolean QOpenGLFunctions_1_3::glIsEnabled(GLenum cap)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN20QOpenGLFunctions_1_311glIsEnabledEj(
    QOpenGLFunctions_1_3 *self,
    GLenum cap) {
  return self->glIsEnabled(cap);
}

//  void QOpenGLFunctions_1_3::glGetTexLevelParameteriv(GLenum target, GLint
//      level, GLenum pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_324glGetTexLevelParameterivEjijPi(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    GLint level,
    GLenum pname,
    GLint *params) {
  self->glGetTexLevelParameteriv(target, level, pname, params);
}

//  void QOpenGLFunctions_1_3::glGetTexLevelParameterfv(GLenum target, GLint
//      level, GLenum pname, GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_324glGetTexLevelParameterfvEjijPf(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    GLint level,
    GLenum pname,
    GLfloat *params) {
  self->glGetTexLevelParameterfv(target, level, pname, params);
}

//  void QOpenGLFunctions_1_3::glGetTexParameteriv(GLenum target, GLenum
//      pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_319glGetTexParameterivEjjPi(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    GLenum pname,
    GLint *params) {
  self->glGetTexParameteriv(target, pname, params);
}

//  void QOpenGLFunctions_1_3::glGetTexParameterfv(GLenum target, GLenum
//      pname, GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_319glGetTexParameterfvEjjPf(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    GLenum pname,
    GLfloat *params) {
  self->glGetTexParameterfv(target, pname, params);
}

//  void QOpenGLFunctions_1_3::glGetTexImage(GLenum target, GLint level,
//      GLenum format, GLenum type, GLvoid *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_313glGetTexImageEjijjPv(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    GLint level,
    GLenum format,
    GLenum type,
    GLvoid *pixels) {
  self->glGetTexImage(target, level, format, type, pixels);
}

//  const GLubyte *QOpenGLFunctions_1_3::glGetString(GLenum name)
extern "C" Q_DECL_EXPORT
const GLubyte *ritual_ZN20QOpenGLFunctions_1_311glGetStringEj(
    QOpenGLFunctions_1_3 *self,
    GLenum name) {
  return self->glGetString(name);
}

//  void QOpenGLFunctions_1_3::glGetIntegerv(GLenum pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_313glGetIntegervEjPi(
    QOpenGLFunctions_1_3 *self,
    GLenum pname,
    GLint *params) {
  self->glGetIntegerv(pname, params);
}

//  void QOpenGLFunctions_1_3::glGetFloatv(GLenum pname, GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_311glGetFloatvEjPf(
    QOpenGLFunctions_1_3 *self,
    GLenum pname,
    GLfloat *params) {
  self->glGetFloatv(pname, params);
}

//  GLenum QOpenGLFunctions_1_3::glGetError()
extern "C" Q_DECL_EXPORT
GLenum ritual_ZN20QOpenGLFunctions_1_310glGetErrorEv(
    QOpenGLFunctions_1_3 *self) {
  return self->glGetError();
}

//  void QOpenGLFunctions_1_3::glGetDoublev(GLenum pname, GLdouble *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_312glGetDoublevEjPd(
    QOpenGLFunctions_1_3 *self,
    GLenum pname,
    GLdouble *params) {
  self->glGetDoublev(pname, params);
}

//  void QOpenGLFunctions_1_3::glGetBooleanv(GLenum pname, GLboolean *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_313glGetBooleanvEjPh(
    QOpenGLFunctions_1_3 *self,
    GLenum pname,
    GLboolean *params) {
  self->glGetBooleanv(pname, params);
}

//  void QOpenGLFunctions_1_3::glReadPixels(GLint x, GLint y, GLsizei width,
//      GLsizei height, GLenum format, GLenum type, GLvoid *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_312glReadPixelsEiiiijjPv(
    QOpenGLFunctions_1_3 *self,
    GLint x,
    GLint y,
    GLsizei width,
    GLsizei height,
    GLenum format,
    GLenum type,
    GLvoid *pixels) {
  self->glReadPixels(x, y, width, height, format, type, pixels);
}

//  void QOpenGLFunctions_1_3::glReadBuffer(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_312glReadBufferEj(
    QOpenGLFunctions_1_3 *self,
    GLenum mode) {
  self->glReadBuffer(mode);
}

//  void QOpenGLFunctions_1_3::glPixelStorei(GLenum pname, GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_313glPixelStoreiEji(
    QOpenGLFunctions_1_3 *self,
    GLenum pname,
    GLint param) {
  self->glPixelStorei(pname, param);
}

//  void QOpenGLFunctions_1_3::glPixelStoref(GLenum pname, GLfloat param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_313glPixelStorefEjf(
    QOpenGLFunctions_1_3 *self,
    GLenum pname,
    GLfloat param) {
  self->glPixelStoref(pname, param);
}

//  void QOpenGLFunctions_1_3::glDepthFunc(GLenum func)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_311glDepthFuncEj(
    QOpenGLFunctions_1_3 *self,
    GLenum func) {
  self->glDepthFunc(func);
}

//  void QOpenGLFunctions_1_3::glStencilOp(GLenum fail, GLenum zfail, GLenum
//      zpass)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_311glStencilOpEjjj(
    QOpenGLFunctions_1_3 *self,
    GLenum fail,
    GLenum zfail,
    GLenum zpass) {
  self->glStencilOp(fail, zfail, zpass);
}

//  void QOpenGLFunctions_1_3::glStencilFunc(GLenum func, GLint ref, GLuint
//      mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_313glStencilFuncEjij(
    QOpenGLFunctions_1_3 *self,
    GLenum func,
    GLint ref,
    GLuint mask) {
  self->glStencilFunc(func, ref, mask);
}

//  void QOpenGLFunctions_1_3::glLogicOp(GLenum opcode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_39glLogicOpEj(
    QOpenGLFunctions_1_3 *self,
    GLenum opcode) {
  self->glLogicOp(opcode);
}

//  void QOpenGLFunctions_1_3::glBlendFunc(GLenum sfactor, GLenum dfactor)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_311glBlendFuncEjj(
    QOpenGLFunctions_1_3 *self,
    GLenum sfactor,
    GLenum dfactor) {
  self->glBlendFunc(sfactor, dfactor);
}

//  void QOpenGLFunctions_1_3::glFlush()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_37glFlushEv(QOpenGLFunctions_1_3 *self) {
  self->glFlush();
}

//  void QOpenGLFunctions_1_3::glFinish()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_38glFinishEv(QOpenGLFunctions_1_3 *self) {
  self->glFinish();
}

//  void QOpenGLFunctions_1_3::glEnable(GLenum cap)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_38glEnableEj(
    QOpenGLFunctions_1_3 *self,
    GLenum cap) {
  self->glEnable(cap);
}

//  void QOpenGLFunctions_1_3::glDisable(GLenum cap)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_39glDisableEj(
    QOpenGLFunctions_1_3 *self,
    GLenum cap) {
  self->glDisable(cap);
}

//  void QOpenGLFunctions_1_3::glDepthMask(GLboolean flag)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_311glDepthMaskEh(
    QOpenGLFunctions_1_3 *self,
    GLboolean flag) {
  self->glDepthMask(flag);
}

//  void QOpenGLFunctions_1_3::glColorMask(GLboolean red, GLboolean green,
//      GLboolean blue, GLboolean alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_311glColorMaskEhhhh(
    QOpenGLFunctions_1_3 *self,
    GLboolean red,
    GLboolean green,
    GLboolean blue,
    GLboolean alpha) {
  self->glColorMask(red, green, blue, alpha);
}

//  void QOpenGLFunctions_1_3::glStencilMask(GLuint mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_313glStencilMaskEj(
    QOpenGLFunctions_1_3 *self,
    GLuint mask) {
  self->glStencilMask(mask);
}

//  void QOpenGLFunctions_1_3::glClearDepth(GLdouble depth)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_312glClearDepthEd(
    QOpenGLFunctions_1_3 *self,
    GLdouble depth) {
  self->glClearDepth(depth);
}

//  void QOpenGLFunctions_1_3::glClearStencil(GLint s)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_314glClearStencilEi(
    QOpenGLFunctions_1_3 *self,
    GLint s) {
  self->glClearStencil(s);
}

//  void QOpenGLFunctions_1_3::glClearColor(GLfloat red, GLfloat green,
//      GLfloat blue, GLfloat alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_312glClearColorEffff(
    QOpenGLFunctions_1_3 *self,
    GLfloat red,
    GLfloat green,
    GLfloat blue,
    GLfloat alpha) {
  self->glClearColor(red, green, blue, alpha);
}

//  void QOpenGLFunctions_1_3::glClear(GLbitfield mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_37glClearEj(
    QOpenGLFunctions_1_3 *self,
    GLbitfield mask) {
  self->glClear(mask);
}

//  void QOpenGLFunctions_1_3::glDrawBuffer(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_312glDrawBufferEj(
    QOpenGLFunctions_1_3 *self,
    GLenum mode) {
  self->glDrawBuffer(mode);
}

//  void QOpenGLFunctions_1_3::glTexImage2D(GLenum target, GLint level, GLint
//      internalformat, GLsizei width, GLsizei height, GLint border, GLenum
//      format, GLenum type, const GLvoid *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_312glTexImage2DEjiiiiijjPKv(
    QOpenGLFunctions_1_3 *self,
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

//  void QOpenGLFunctions_1_3::glTexImage1D(GLenum target, GLint level, GLint
//      internalformat, GLsizei width, GLint border, GLenum format, GLenum
//      type, const GLvoid *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_312glTexImage1DEjiiiijjPKv(
    QOpenGLFunctions_1_3 *self,
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

//  void QOpenGLFunctions_1_3::glTexParameteriv(GLenum target, GLenum pname,
//      const GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_316glTexParameterivEjjPKi(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    GLenum pname,
    const GLint *params) {
  self->glTexParameteriv(target, pname, params);
}

//  void QOpenGLFunctions_1_3::glTexParameteri(GLenum target, GLenum pname,
//      GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_315glTexParameteriEjji(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    GLenum pname,
    GLint param) {
  self->glTexParameteri(target, pname, param);
}

//  void QOpenGLFunctions_1_3::glTexParameterfv(GLenum target, GLenum pname,
//      const GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_316glTexParameterfvEjjPKf(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    GLenum pname,
    const GLfloat *params) {
  self->glTexParameterfv(target, pname, params);
}

//  void QOpenGLFunctions_1_3::glTexParameterf(GLenum target, GLenum pname,
//      GLfloat param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_315glTexParameterfEjjf(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    GLenum pname,
    GLfloat param) {
  self->glTexParameterf(target, pname, param);
}

//  void QOpenGLFunctions_1_3::glScissor(GLint x, GLint y, GLsizei width,
//      GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_39glScissorEiiii(
    QOpenGLFunctions_1_3 *self,
    GLint x,
    GLint y,
    GLsizei width,
    GLsizei height) {
  self->glScissor(x, y, width, height);
}

//  void QOpenGLFunctions_1_3::glPolygonMode(GLenum face, GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_313glPolygonModeEjj(
    QOpenGLFunctions_1_3 *self,
    GLenum face,
    GLenum mode) {
  self->glPolygonMode(face, mode);
}

//  void QOpenGLFunctions_1_3::glPointSize(GLfloat size)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_311glPointSizeEf(
    QOpenGLFunctions_1_3 *self,
    GLfloat size) {
  self->glPointSize(size);
}

//  void QOpenGLFunctions_1_3::glLineWidth(GLfloat width)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_311glLineWidthEf(
    QOpenGLFunctions_1_3 *self,
    GLfloat width) {
  self->glLineWidth(width);
}

//  void QOpenGLFunctions_1_3::glHint(GLenum target, GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_36glHintEjj(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    GLenum mode) {
  self->glHint(target, mode);
}

//  void QOpenGLFunctions_1_3::glFrontFace(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_311glFrontFaceEj(
    QOpenGLFunctions_1_3 *self,
    GLenum mode) {
  self->glFrontFace(mode);
}

//  void QOpenGLFunctions_1_3::glCullFace(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_310glCullFaceEj(
    QOpenGLFunctions_1_3 *self,
    GLenum mode) {
  self->glCullFace(mode);
}

//  void QOpenGLFunctions_1_3::glIndexubv(const GLubyte *c)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_310glIndexubvEPKh(
    QOpenGLFunctions_1_3 *self,
    const GLubyte *c) {
  self->glIndexubv(c);
}

//  void QOpenGLFunctions_1_3::glIndexub(GLubyte c)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_39glIndexubEh(
    QOpenGLFunctions_1_3 *self,
    GLubyte c) {
  self->glIndexub(c);
}

//  GLboolean QOpenGLFunctions_1_3::glIsTexture(GLuint texture)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN20QOpenGLFunctions_1_311glIsTextureEj(
    QOpenGLFunctions_1_3 *self,
    GLuint texture) {
  return self->glIsTexture(texture);
}

//  void QOpenGLFunctions_1_3::glGenTextures(GLsizei n, GLuint *textures)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_313glGenTexturesEiPj(
    QOpenGLFunctions_1_3 *self,
    GLsizei n,
    GLuint *textures) {
  self->glGenTextures(n, textures);
}

//  void QOpenGLFunctions_1_3::glDeleteTextures(GLsizei n, const GLuint
//      *textures)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_316glDeleteTexturesEiPKj(
    QOpenGLFunctions_1_3 *self,
    GLsizei n,
    const GLuint *textures) {
  self->glDeleteTextures(n, textures);
}

//  void QOpenGLFunctions_1_3::glBindTexture(GLenum target, GLuint texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_313glBindTextureEjj(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    GLuint texture) {
  self->glBindTexture(target, texture);
}

//  void QOpenGLFunctions_1_3::glTexSubImage2D(GLenum target, GLint level,
//      GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum
//      format, GLenum type, const GLvoid *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_315glTexSubImage2DEjiiiiijjPKv(
    QOpenGLFunctions_1_3 *self,
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

//  void QOpenGLFunctions_1_3::glTexSubImage1D(GLenum target, GLint level,
//      GLint xoffset, GLsizei width, GLenum format, GLenum type, const
//      GLvoid *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_315glTexSubImage1DEjiiijjPKv(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    GLint level,
    GLint xoffset,
    GLsizei width,
    GLenum format,
    GLenum type,
    const GLvoid *pixels) {
  self->glTexSubImage1D(target, level, xoffset, width, format, type, pixels);
}

//  void QOpenGLFunctions_1_3::glCopyTexSubImage2D(GLenum target, GLint
//      level, GLint xoffset, GLint yoffset, GLint x, GLint y, GLsizei width,
//      GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_319glCopyTexSubImage2DEjiiiiiii(
    QOpenGLFunctions_1_3 *self,
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

//  void QOpenGLFunctions_1_3::glCopyTexSubImage1D(GLenum target, GLint
//      level, GLint xoffset, GLint x, GLint y, GLsizei width)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_319glCopyTexSubImage1DEjiiiii(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    GLint level,
    GLint xoffset,
    GLint x,
    GLint y,
    GLsizei width) {
  self->glCopyTexSubImage1D(target, level, xoffset, x, y, width);
}

//  void QOpenGLFunctions_1_3::glCopyTexImage2D(GLenum target, GLint level,
//      GLenum internalformat, GLint x, GLint y, GLsizei width, GLsizei
//      height, GLint border)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_316glCopyTexImage2DEjijiiiii(
    QOpenGLFunctions_1_3 *self,
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

//  void QOpenGLFunctions_1_3::glCopyTexImage1D(GLenum target, GLint level,
//      GLenum internalformat, GLint x, GLint y, GLsizei width, GLint border)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_316glCopyTexImage1DEjijiiii(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    GLint level,
    GLenum internalformat,
    GLint x,
    GLint y,
    GLsizei width,
    GLint border) {
  self->glCopyTexImage1D(target, level, internalformat, x, y, width, border);
}

//  void QOpenGLFunctions_1_3::glPolygonOffset(GLfloat factor, GLfloat units)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_315glPolygonOffsetEff(
    QOpenGLFunctions_1_3 *self,
    GLfloat factor,
    GLfloat units) {
  self->glPolygonOffset(factor, units);
}

//  void QOpenGLFunctions_1_3::glGetPointerv(GLenum pname, GLvoid **params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_313glGetPointervEjPPv(
    QOpenGLFunctions_1_3 *self,
    GLenum pname,
    GLvoid **params) {
  self->glGetPointerv(pname, params);
}

//  void QOpenGLFunctions_1_3::glDrawElements(GLenum mode, GLsizei count,
//      GLenum type, const GLvoid *indices)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_314glDrawElementsEjijPKv(
    QOpenGLFunctions_1_3 *self,
    GLenum mode,
    GLsizei count,
    GLenum type,
    const GLvoid *indices) {
  self->glDrawElements(mode, count, type, indices);
}

//  void QOpenGLFunctions_1_3::glDrawArrays(GLenum mode, GLint first, GLsizei
//      count)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_312glDrawArraysEjii(
    QOpenGLFunctions_1_3 *self,
    GLenum mode,
    GLint first,
    GLsizei count) {
  self->glDrawArrays(mode, first, count);
}

//  void QOpenGLFunctions_1_3::glCopyTexSubImage3D(GLenum target, GLint
//      level, GLint xoffset, GLint yoffset, GLint zoffset, GLint x, GLint y,
//      GLsizei width, GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_319glCopyTexSubImage3DEjiiiiiiii(
    QOpenGLFunctions_1_3 *self,
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

//  void QOpenGLFunctions_1_3::glTexSubImage3D(GLenum target, GLint level,
//      GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei
//      height, GLsizei depth, GLenum format, GLenum type, const GLvoid
//      *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_315glTexSubImage3DEjiiiiiiijjPKv(
    QOpenGLFunctions_1_3 *self,
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

//  void QOpenGLFunctions_1_3::glTexImage3D(GLenum target, GLint level, GLint
//      internalformat, GLsizei width, GLsizei height, GLsizei depth, GLint
//      border, GLenum format, GLenum type, const GLvoid *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_312glTexImage3DEjiiiiiijjPKv(
    QOpenGLFunctions_1_3 *self,
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

//  void QOpenGLFunctions_1_3::glDrawRangeElements(GLenum mode, GLuint start,
//      GLuint end, GLsizei count, GLenum type, const GLvoid *indices)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_319glDrawRangeElementsEjjjijPKv(
    QOpenGLFunctions_1_3 *self,
    GLenum mode,
    GLuint start,
    GLuint end,
    GLsizei count,
    GLenum type,
    const GLvoid *indices) {
  self->glDrawRangeElements(mode, start, end, count, type, indices);
}

//  void QOpenGLFunctions_1_3::glBlendEquation(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_315glBlendEquationEj(
    QOpenGLFunctions_1_3 *self,
    GLenum mode) {
  self->glBlendEquation(mode);
}

//  void QOpenGLFunctions_1_3::glBlendColor(GLfloat red, GLfloat green,
//      GLfloat blue, GLfloat alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_312glBlendColorEffff(
    QOpenGLFunctions_1_3 *self,
    GLfloat red,
    GLfloat green,
    GLfloat blue,
    GLfloat alpha) {
  self->glBlendColor(red, green, blue, alpha);
}

//  void QOpenGLFunctions_1_3::glGetCompressedTexImage(GLenum target, GLint
//      level, GLvoid *img)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_323glGetCompressedTexImageEjiPv(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    GLint level,
    GLvoid *img) {
  self->glGetCompressedTexImage(target, level, img);
}

//  void QOpenGLFunctions_1_3::glCompressedTexSubImage1D(GLenum target, GLint
//      level, GLint xoffset, GLsizei width, GLenum format, GLsizei
//      imageSize, const GLvoid *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_325glCompressedTexSubImage1DEjiiijiPKv(
    QOpenGLFunctions_1_3 *self,
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

//  void QOpenGLFunctions_1_3::glCompressedTexSubImage2D(GLenum target, GLint
//      level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height,
//      GLenum format, GLsizei imageSize, const GLvoid *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_325glCompressedTexSubImage2DEjiiiiijiPKv(
    QOpenGLFunctions_1_3 *self,
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

//  void QOpenGLFunctions_1_3::glCompressedTexSubImage3D(GLenum target, GLint
//      level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width,
//      GLsizei height, GLsizei depth, GLenum format, GLsizei imageSize,
//      const GLvoid *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_325glCompressedTexSubImage3DEjiiiiiiijiPKv(
    QOpenGLFunctions_1_3 *self,
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

//  void QOpenGLFunctions_1_3::glCompressedTexImage1D(GLenum target, GLint
//      level, GLenum internalformat, GLsizei width, GLint border, GLsizei
//      imageSize, const GLvoid *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_322glCompressedTexImage1DEjijiiiPKv(
    QOpenGLFunctions_1_3 *self,
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

//  void QOpenGLFunctions_1_3::glCompressedTexImage2D(GLenum target, GLint
//      level, GLenum internalformat, GLsizei width, GLsizei height, GLint
//      border, GLsizei imageSize, const GLvoid *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_322glCompressedTexImage2DEjijiiiiPKv(
    QOpenGLFunctions_1_3 *self,
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

//  void QOpenGLFunctions_1_3::glCompressedTexImage3D(GLenum target, GLint
//      level, GLenum internalformat, GLsizei width, GLsizei height, GLsizei
//      depth, GLint border, GLsizei imageSize, const GLvoid *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_322glCompressedTexImage3DEjijiiiiiPKv(
    QOpenGLFunctions_1_3 *self,
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

//  void QOpenGLFunctions_1_3::glSampleCoverage(GLfloat value, GLboolean
//      invert)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_316glSampleCoverageEfh(
    QOpenGLFunctions_1_3 *self,
    GLfloat value,
    GLboolean invert) {
  self->glSampleCoverage(value, invert);
}

//  void QOpenGLFunctions_1_3::glActiveTexture(GLenum texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_315glActiveTextureEj(
    QOpenGLFunctions_1_3 *self,
    GLenum texture) {
  self->glActiveTexture(texture);
}

//  void QOpenGLFunctions_1_3::glTranslatef(GLfloat x, GLfloat y, GLfloat z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_312glTranslatefEfff(
    QOpenGLFunctions_1_3 *self,
    GLfloat x,
    GLfloat y,
    GLfloat z) {
  self->glTranslatef(x, y, z);
}

//  void QOpenGLFunctions_1_3::glTranslated(GLdouble x, GLdouble y, GLdouble
//      z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_312glTranslatedEddd(
    QOpenGLFunctions_1_3 *self,
    GLdouble x,
    GLdouble y,
    GLdouble z) {
  self->glTranslated(x, y, z);
}

//  void QOpenGLFunctions_1_3::glScalef(GLfloat x, GLfloat y, GLfloat z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_38glScalefEfff(
    QOpenGLFunctions_1_3 *self,
    GLfloat x,
    GLfloat y,
    GLfloat z) {
  self->glScalef(x, y, z);
}

//  void QOpenGLFunctions_1_3::glScaled(GLdouble x, GLdouble y, GLdouble z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_38glScaledEddd(
    QOpenGLFunctions_1_3 *self,
    GLdouble x,
    GLdouble y,
    GLdouble z) {
  self->glScaled(x, y, z);
}

//  void QOpenGLFunctions_1_3::glRotatef(GLfloat angle, GLfloat x, GLfloat y,
//      GLfloat z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_39glRotatefEffff(
    QOpenGLFunctions_1_3 *self,
    GLfloat angle,
    GLfloat x,
    GLfloat y,
    GLfloat z) {
  self->glRotatef(angle, x, y, z);
}

//  void QOpenGLFunctions_1_3::glRotated(GLdouble angle, GLdouble x, GLdouble
//      y, GLdouble z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_39glRotatedEdddd(
    QOpenGLFunctions_1_3 *self,
    GLdouble angle,
    GLdouble x,
    GLdouble y,
    GLdouble z) {
  self->glRotated(angle, x, y, z);
}

//  void QOpenGLFunctions_1_3::glPushMatrix()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_312glPushMatrixEv(
    QOpenGLFunctions_1_3 *self) {
  self->glPushMatrix();
}

//  void QOpenGLFunctions_1_3::glPopMatrix()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_311glPopMatrixEv(
    QOpenGLFunctions_1_3 *self) {
  self->glPopMatrix();
}

//  void QOpenGLFunctions_1_3::glOrtho(GLdouble left, GLdouble right,
//      GLdouble bottom, GLdouble top, GLdouble zNear, GLdouble zFar)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_37glOrthoEdddddd(
    QOpenGLFunctions_1_3 *self,
    GLdouble left,
    GLdouble right,
    GLdouble bottom,
    GLdouble top,
    GLdouble zNear,
    GLdouble zFar) {
  self->glOrtho(left, right, bottom, top, zNear, zFar);
}

//  void QOpenGLFunctions_1_3::glMultMatrixd(const GLdouble *m)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_313glMultMatrixdEPKd(
    QOpenGLFunctions_1_3 *self,
    const GLdouble *m) {
  self->glMultMatrixd(m);
}

//  void QOpenGLFunctions_1_3::glMultMatrixf(const GLfloat *m)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_313glMultMatrixfEPKf(
    QOpenGLFunctions_1_3 *self,
    const GLfloat *m) {
  self->glMultMatrixf(m);
}

//  void QOpenGLFunctions_1_3::glMatrixMode(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_312glMatrixModeEj(
    QOpenGLFunctions_1_3 *self,
    GLenum mode) {
  self->glMatrixMode(mode);
}

//  void QOpenGLFunctions_1_3::glLoadMatrixd(const GLdouble *m)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_313glLoadMatrixdEPKd(
    QOpenGLFunctions_1_3 *self,
    const GLdouble *m) {
  self->glLoadMatrixd(m);
}

//  void QOpenGLFunctions_1_3::glLoadMatrixf(const GLfloat *m)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_313glLoadMatrixfEPKf(
    QOpenGLFunctions_1_3 *self,
    const GLfloat *m) {
  self->glLoadMatrixf(m);
}

//  void QOpenGLFunctions_1_3::glLoadIdentity()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_314glLoadIdentityEv(
    QOpenGLFunctions_1_3 *self) {
  self->glLoadIdentity();
}

//  void QOpenGLFunctions_1_3::glFrustum(GLdouble left, GLdouble right,
//      GLdouble bottom, GLdouble top, GLdouble zNear, GLdouble zFar)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_39glFrustumEdddddd(
    QOpenGLFunctions_1_3 *self,
    GLdouble left,
    GLdouble right,
    GLdouble bottom,
    GLdouble top,
    GLdouble zNear,
    GLdouble zFar) {
  self->glFrustum(left, right, bottom, top, zNear, zFar);
}

//  GLboolean QOpenGLFunctions_1_3::glIsList(GLuint list)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN20QOpenGLFunctions_1_38glIsListEj(
    QOpenGLFunctions_1_3 *self,
    GLuint list) {
  return self->glIsList(list);
}

//  void QOpenGLFunctions_1_3::glGetTexGeniv(GLenum coord, GLenum pname,
//      GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_313glGetTexGenivEjjPi(
    QOpenGLFunctions_1_3 *self,
    GLenum coord,
    GLenum pname,
    GLint *params) {
  self->glGetTexGeniv(coord, pname, params);
}

//  void QOpenGLFunctions_1_3::glGetTexGenfv(GLenum coord, GLenum pname,
//      GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_313glGetTexGenfvEjjPf(
    QOpenGLFunctions_1_3 *self,
    GLenum coord,
    GLenum pname,
    GLfloat *params) {
  self->glGetTexGenfv(coord, pname, params);
}

//  void QOpenGLFunctions_1_3::glGetTexGendv(GLenum coord, GLenum pname,
//      GLdouble *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_313glGetTexGendvEjjPd(
    QOpenGLFunctions_1_3 *self,
    GLenum coord,
    GLenum pname,
    GLdouble *params) {
  self->glGetTexGendv(coord, pname, params);
}

//  void QOpenGLFunctions_1_3::glGetTexEnviv(GLenum target, GLenum pname,
//      GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_313glGetTexEnvivEjjPi(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    GLenum pname,
    GLint *params) {
  self->glGetTexEnviv(target, pname, params);
}

//  void QOpenGLFunctions_1_3::glGetTexEnvfv(GLenum target, GLenum pname,
//      GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_313glGetTexEnvfvEjjPf(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    GLenum pname,
    GLfloat *params) {
  self->glGetTexEnvfv(target, pname, params);
}

//  void QOpenGLFunctions_1_3::glGetPolygonStipple(GLubyte *mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_319glGetPolygonStippleEPh(
    QOpenGLFunctions_1_3 *self,
    GLubyte *mask) {
  self->glGetPolygonStipple(mask);
}

//  void QOpenGLFunctions_1_3::glGetPixelMapusv(GLenum map, GLushort *values)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_316glGetPixelMapusvEjPt(
    QOpenGLFunctions_1_3 *self,
    GLenum map,
    GLushort *values) {
  self->glGetPixelMapusv(map, values);
}

//  void QOpenGLFunctions_1_3::glGetPixelMapuiv(GLenum map, GLuint *values)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_316glGetPixelMapuivEjPj(
    QOpenGLFunctions_1_3 *self,
    GLenum map,
    GLuint *values) {
  self->glGetPixelMapuiv(map, values);
}

//  void QOpenGLFunctions_1_3::glGetPixelMapfv(GLenum map, GLfloat *values)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_315glGetPixelMapfvEjPf(
    QOpenGLFunctions_1_3 *self,
    GLenum map,
    GLfloat *values) {
  self->glGetPixelMapfv(map, values);
}

//  void QOpenGLFunctions_1_3::glGetMaterialiv(GLenum face, GLenum pname,
//      GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_315glGetMaterialivEjjPi(
    QOpenGLFunctions_1_3 *self,
    GLenum face,
    GLenum pname,
    GLint *params) {
  self->glGetMaterialiv(face, pname, params);
}

//  void QOpenGLFunctions_1_3::glGetMaterialfv(GLenum face, GLenum pname,
//      GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_315glGetMaterialfvEjjPf(
    QOpenGLFunctions_1_3 *self,
    GLenum face,
    GLenum pname,
    GLfloat *params) {
  self->glGetMaterialfv(face, pname, params);
}

//  void QOpenGLFunctions_1_3::glGetMapiv(GLenum target, GLenum query, GLint
//      *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_310glGetMapivEjjPi(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    GLenum query,
    GLint *v) {
  self->glGetMapiv(target, query, v);
}

//  void QOpenGLFunctions_1_3::glGetMapfv(GLenum target, GLenum query,
//      GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_310glGetMapfvEjjPf(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    GLenum query,
    GLfloat *v) {
  self->glGetMapfv(target, query, v);
}

//  void QOpenGLFunctions_1_3::glGetMapdv(GLenum target, GLenum query,
//      GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_310glGetMapdvEjjPd(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    GLenum query,
    GLdouble *v) {
  self->glGetMapdv(target, query, v);
}

//  void QOpenGLFunctions_1_3::glGetLightiv(GLenum light, GLenum pname, GLint
//      *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_312glGetLightivEjjPi(
    QOpenGLFunctions_1_3 *self,
    GLenum light,
    GLenum pname,
    GLint *params) {
  self->glGetLightiv(light, pname, params);
}

//  void QOpenGLFunctions_1_3::glGetLightfv(GLenum light, GLenum pname,
//      GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_312glGetLightfvEjjPf(
    QOpenGLFunctions_1_3 *self,
    GLenum light,
    GLenum pname,
    GLfloat *params) {
  self->glGetLightfv(light, pname, params);
}

//  void QOpenGLFunctions_1_3::glGetClipPlane(GLenum plane, GLdouble
//      *equation)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_314glGetClipPlaneEjPd(
    QOpenGLFunctions_1_3 *self,
    GLenum plane,
    GLdouble *equation) {
  self->glGetClipPlane(plane, equation);
}

//  void QOpenGLFunctions_1_3::glDrawPixels(GLsizei width, GLsizei height,
//      GLenum format, GLenum type, const GLvoid *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_312glDrawPixelsEiijjPKv(
    QOpenGLFunctions_1_3 *self,
    GLsizei width,
    GLsizei height,
    GLenum format,
    GLenum type,
    const GLvoid *pixels) {
  self->glDrawPixels(width, height, format, type, pixels);
}

//  void QOpenGLFunctions_1_3::glCopyPixels(GLint x, GLint y, GLsizei width,
//      GLsizei height, GLenum type)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_312glCopyPixelsEiiiij(
    QOpenGLFunctions_1_3 *self,
    GLint x,
    GLint y,
    GLsizei width,
    GLsizei height,
    GLenum type) {
  self->glCopyPixels(x, y, width, height, type);
}

//  void QOpenGLFunctions_1_3::glPixelMapusv(GLenum map, GLint mapsize, const
//      GLushort *values)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_313glPixelMapusvEjiPKt(
    QOpenGLFunctions_1_3 *self,
    GLenum map,
    GLint mapsize,
    const GLushort *values) {
  self->glPixelMapusv(map, mapsize, values);
}

//  void QOpenGLFunctions_1_3::glPixelMapuiv(GLenum map, GLint mapsize, const
//      GLuint *values)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_313glPixelMapuivEjiPKj(
    QOpenGLFunctions_1_3 *self,
    GLenum map,
    GLint mapsize,
    const GLuint *values) {
  self->glPixelMapuiv(map, mapsize, values);
}

//  void QOpenGLFunctions_1_3::glPixelMapfv(GLenum map, GLint mapsize, const
//      GLfloat *values)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_312glPixelMapfvEjiPKf(
    QOpenGLFunctions_1_3 *self,
    GLenum map,
    GLint mapsize,
    const GLfloat *values) {
  self->glPixelMapfv(map, mapsize, values);
}

//  void QOpenGLFunctions_1_3::glPixelTransferi(GLenum pname, GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_316glPixelTransferiEji(
    QOpenGLFunctions_1_3 *self,
    GLenum pname,
    GLint param) {
  self->glPixelTransferi(pname, param);
}

//  void QOpenGLFunctions_1_3::glPixelTransferf(GLenum pname, GLfloat param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_316glPixelTransferfEjf(
    QOpenGLFunctions_1_3 *self,
    GLenum pname,
    GLfloat param) {
  self->glPixelTransferf(pname, param);
}

//  void QOpenGLFunctions_1_3::glPixelZoom(GLfloat xfactor, GLfloat yfactor)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_311glPixelZoomEff(
    QOpenGLFunctions_1_3 *self,
    GLfloat xfactor,
    GLfloat yfactor) {
  self->glPixelZoom(xfactor, yfactor);
}

//  void QOpenGLFunctions_1_3::glAlphaFunc(GLenum func, GLfloat ref)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_311glAlphaFuncEjf(
    QOpenGLFunctions_1_3 *self,
    GLenum func,
    GLfloat ref) {
  self->glAlphaFunc(func, ref);
}

//  void QOpenGLFunctions_1_3::glEvalPoint2(GLint i, GLint j)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_312glEvalPoint2Eii(
    QOpenGLFunctions_1_3 *self,
    GLint i,
    GLint j) {
  self->glEvalPoint2(i, j);
}

//  void QOpenGLFunctions_1_3::glEvalMesh2(GLenum mode, GLint i1, GLint i2,
//      GLint j1, GLint j2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_311glEvalMesh2Ejiiii(
    QOpenGLFunctions_1_3 *self,
    GLenum mode,
    GLint i1,
    GLint i2,
    GLint j1,
    GLint j2) {
  self->glEvalMesh2(mode, i1, i2, j1, j2);
}

//  void QOpenGLFunctions_1_3::glEvalPoint1(GLint i)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_312glEvalPoint1Ei(
    QOpenGLFunctions_1_3 *self,
    GLint i) {
  self->glEvalPoint1(i);
}

//  void QOpenGLFunctions_1_3::glEvalMesh1(GLenum mode, GLint i1, GLint i2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_311glEvalMesh1Ejii(
    QOpenGLFunctions_1_3 *self,
    GLenum mode,
    GLint i1,
    GLint i2) {
  self->glEvalMesh1(mode, i1, i2);
}

//  void QOpenGLFunctions_1_3::glEvalCoord2fv(const GLfloat *u)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_314glEvalCoord2fvEPKf(
    QOpenGLFunctions_1_3 *self,
    const GLfloat *u) {
  self->glEvalCoord2fv(u);
}

//  void QOpenGLFunctions_1_3::glEvalCoord2f(GLfloat u, GLfloat v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_313glEvalCoord2fEff(
    QOpenGLFunctions_1_3 *self,
    GLfloat u,
    GLfloat v) {
  self->glEvalCoord2f(u, v);
}

//  void QOpenGLFunctions_1_3::glEvalCoord2dv(const GLdouble *u)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_314glEvalCoord2dvEPKd(
    QOpenGLFunctions_1_3 *self,
    const GLdouble *u) {
  self->glEvalCoord2dv(u);
}

//  void QOpenGLFunctions_1_3::glEvalCoord2d(GLdouble u, GLdouble v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_313glEvalCoord2dEdd(
    QOpenGLFunctions_1_3 *self,
    GLdouble u,
    GLdouble v) {
  self->glEvalCoord2d(u, v);
}

//  void QOpenGLFunctions_1_3::glEvalCoord1fv(const GLfloat *u)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_314glEvalCoord1fvEPKf(
    QOpenGLFunctions_1_3 *self,
    const GLfloat *u) {
  self->glEvalCoord1fv(u);
}

//  void QOpenGLFunctions_1_3::glEvalCoord1f(GLfloat u)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_313glEvalCoord1fEf(
    QOpenGLFunctions_1_3 *self,
    GLfloat u) {
  self->glEvalCoord1f(u);
}

//  void QOpenGLFunctions_1_3::glEvalCoord1dv(const GLdouble *u)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_314glEvalCoord1dvEPKd(
    QOpenGLFunctions_1_3 *self,
    const GLdouble *u) {
  self->glEvalCoord1dv(u);
}

//  void QOpenGLFunctions_1_3::glEvalCoord1d(GLdouble u)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_313glEvalCoord1dEd(
    QOpenGLFunctions_1_3 *self,
    GLdouble u) {
  self->glEvalCoord1d(u);
}

//  void QOpenGLFunctions_1_3::glMapGrid2f(GLint un, GLfloat u1, GLfloat u2,
//      GLint vn, GLfloat v1, GLfloat v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_311glMapGrid2fEiffiff(
    QOpenGLFunctions_1_3 *self,
    GLint un,
    GLfloat u1,
    GLfloat u2,
    GLint vn,
    GLfloat v1,
    GLfloat v2) {
  self->glMapGrid2f(un, u1, u2, vn, v1, v2);
}

//  void QOpenGLFunctions_1_3::glMapGrid2d(GLint un, GLdouble u1, GLdouble
//      u2, GLint vn, GLdouble v1, GLdouble v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_311glMapGrid2dEiddidd(
    QOpenGLFunctions_1_3 *self,
    GLint un,
    GLdouble u1,
    GLdouble u2,
    GLint vn,
    GLdouble v1,
    GLdouble v2) {
  self->glMapGrid2d(un, u1, u2, vn, v1, v2);
}

//  void QOpenGLFunctions_1_3::glMapGrid1f(GLint un, GLfloat u1, GLfloat u2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_311glMapGrid1fEiff(
    QOpenGLFunctions_1_3 *self,
    GLint un,
    GLfloat u1,
    GLfloat u2) {
  self->glMapGrid1f(un, u1, u2);
}

//  void QOpenGLFunctions_1_3::glMapGrid1d(GLint un, GLdouble u1, GLdouble
//      u2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_311glMapGrid1dEidd(
    QOpenGLFunctions_1_3 *self,
    GLint un,
    GLdouble u1,
    GLdouble u2) {
  self->glMapGrid1d(un, u1, u2);
}

//  void QOpenGLFunctions_1_3::glMap2f(GLenum target, GLfloat u1, GLfloat u2,
//      GLint ustride, GLint uorder, GLfloat v1, GLfloat v2, GLint vstride,
//      GLint vorder, const GLfloat *points)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_37glMap2fEjffiiffiiPKf(
    QOpenGLFunctions_1_3 *self,
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

//  void QOpenGLFunctions_1_3::glMap2d(GLenum target, GLdouble u1, GLdouble
//      u2, GLint ustride, GLint uorder, GLdouble v1, GLdouble v2, GLint
//      vstride, GLint vorder, const GLdouble *points)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_37glMap2dEjddiiddiiPKd(
    QOpenGLFunctions_1_3 *self,
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

//  void QOpenGLFunctions_1_3::glMap1f(GLenum target, GLfloat u1, GLfloat u2,
//      GLint stride, GLint order, const GLfloat *points)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_37glMap1fEjffiiPKf(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    GLfloat u1,
    GLfloat u2,
    GLint stride,
    GLint order,
    const GLfloat *points) {
  self->glMap1f(target, u1, u2, stride, order, points);
}

//  void QOpenGLFunctions_1_3::glMap1d(GLenum target, GLdouble u1, GLdouble
//      u2, GLint stride, GLint order, const GLdouble *points)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_37glMap1dEjddiiPKd(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    GLdouble u1,
    GLdouble u2,
    GLint stride,
    GLint order,
    const GLdouble *points) {
  self->glMap1d(target, u1, u2, stride, order, points);
}

//  void QOpenGLFunctions_1_3::glPushAttrib(GLbitfield mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_312glPushAttribEj(
    QOpenGLFunctions_1_3 *self,
    GLbitfield mask) {
  self->glPushAttrib(mask);
}

//  void QOpenGLFunctions_1_3::glPopAttrib()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_311glPopAttribEv(
    QOpenGLFunctions_1_3 *self) {
  self->glPopAttrib();
}

//  void QOpenGLFunctions_1_3::glAccum(GLenum op, GLfloat value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_37glAccumEjf(
    QOpenGLFunctions_1_3 *self,
    GLenum op,
    GLfloat value) {
  self->glAccum(op, value);
}

//  void QOpenGLFunctions_1_3::glIndexMask(GLuint mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_311glIndexMaskEj(
    QOpenGLFunctions_1_3 *self,
    GLuint mask) {
  self->glIndexMask(mask);
}

//  void QOpenGLFunctions_1_3::glClearIndex(GLfloat c)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_312glClearIndexEf(
    QOpenGLFunctions_1_3 *self,
    GLfloat c) {
  self->glClearIndex(c);
}

//  void QOpenGLFunctions_1_3::glClearAccum(GLfloat red, GLfloat green,
//      GLfloat blue, GLfloat alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_312glClearAccumEffff(
    QOpenGLFunctions_1_3 *self,
    GLfloat red,
    GLfloat green,
    GLfloat blue,
    GLfloat alpha) {
  self->glClearAccum(red, green, blue, alpha);
}

//  void QOpenGLFunctions_1_3::glPushName(GLuint name)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_310glPushNameEj(
    QOpenGLFunctions_1_3 *self,
    GLuint name) {
  self->glPushName(name);
}

//  void QOpenGLFunctions_1_3::glPopName()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_39glPopNameEv(
    QOpenGLFunctions_1_3 *self) {
  self->glPopName();
}

//  void QOpenGLFunctions_1_3::glPassThrough(GLfloat token)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_313glPassThroughEf(
    QOpenGLFunctions_1_3 *self,
    GLfloat token) {
  self->glPassThrough(token);
}

//  void QOpenGLFunctions_1_3::glLoadName(GLuint name)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_310glLoadNameEj(
    QOpenGLFunctions_1_3 *self,
    GLuint name) {
  self->glLoadName(name);
}

//  void QOpenGLFunctions_1_3::glInitNames()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_311glInitNamesEv(
    QOpenGLFunctions_1_3 *self) {
  self->glInitNames();
}

//  GLint QOpenGLFunctions_1_3::glRenderMode(GLenum mode)
extern "C" Q_DECL_EXPORT
GLint ritual_ZN20QOpenGLFunctions_1_312glRenderModeEj(
    QOpenGLFunctions_1_3 *self,
    GLenum mode) {
  return self->glRenderMode(mode);
}

//  void QOpenGLFunctions_1_3::glSelectBuffer(GLsizei size, GLuint *buffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_314glSelectBufferEiPj(
    QOpenGLFunctions_1_3 *self,
    GLsizei size,
    GLuint *buffer) {
  self->glSelectBuffer(size, buffer);
}

//  void QOpenGLFunctions_1_3::glFeedbackBuffer(GLsizei size, GLenum type,
//      GLfloat *buffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_316glFeedbackBufferEijPf(
    QOpenGLFunctions_1_3 *self,
    GLsizei size,
    GLenum type,
    GLfloat *buffer) {
  self->glFeedbackBuffer(size, type, buffer);
}

//  void QOpenGLFunctions_1_3::glTexGeniv(GLenum coord, GLenum pname, const
//      GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_310glTexGenivEjjPKi(
    QOpenGLFunctions_1_3 *self,
    GLenum coord,
    GLenum pname,
    const GLint *params) {
  self->glTexGeniv(coord, pname, params);
}

//  void QOpenGLFunctions_1_3::glTexGeni(GLenum coord, GLenum pname, GLint
//      param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_39glTexGeniEjji(
    QOpenGLFunctions_1_3 *self,
    GLenum coord,
    GLenum pname,
    GLint param) {
  self->glTexGeni(coord, pname, param);
}

//  void QOpenGLFunctions_1_3::glTexGenfv(GLenum coord, GLenum pname, const
//      GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_310glTexGenfvEjjPKf(
    QOpenGLFunctions_1_3 *self,
    GLenum coord,
    GLenum pname,
    const GLfloat *params) {
  self->glTexGenfv(coord, pname, params);
}

//  void QOpenGLFunctions_1_3::glTexGenf(GLenum coord, GLenum pname, GLfloat
//      param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_39glTexGenfEjjf(
    QOpenGLFunctions_1_3 *self,
    GLenum coord,
    GLenum pname,
    GLfloat param) {
  self->glTexGenf(coord, pname, param);
}

//  void QOpenGLFunctions_1_3::glTexGendv(GLenum coord, GLenum pname, const
//      GLdouble *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_310glTexGendvEjjPKd(
    QOpenGLFunctions_1_3 *self,
    GLenum coord,
    GLenum pname,
    const GLdouble *params) {
  self->glTexGendv(coord, pname, params);
}

//  void QOpenGLFunctions_1_3::glTexGend(GLenum coord, GLenum pname, GLdouble
//      param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_39glTexGendEjjd(
    QOpenGLFunctions_1_3 *self,
    GLenum coord,
    GLenum pname,
    GLdouble param) {
  self->glTexGend(coord, pname, param);
}

//  void QOpenGLFunctions_1_3::glTexEnviv(GLenum target, GLenum pname, const
//      GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_310glTexEnvivEjjPKi(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    GLenum pname,
    const GLint *params) {
  self->glTexEnviv(target, pname, params);
}

//  void QOpenGLFunctions_1_3::glTexEnvi(GLenum target, GLenum pname, GLint
//      param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_39glTexEnviEjji(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    GLenum pname,
    GLint param) {
  self->glTexEnvi(target, pname, param);
}

//  void QOpenGLFunctions_1_3::glTexEnvfv(GLenum target, GLenum pname, const
//      GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_310glTexEnvfvEjjPKf(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    GLenum pname,
    const GLfloat *params) {
  self->glTexEnvfv(target, pname, params);
}

//  void QOpenGLFunctions_1_3::glTexEnvf(GLenum target, GLenum pname, GLfloat
//      param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_39glTexEnvfEjjf(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    GLenum pname,
    GLfloat param) {
  self->glTexEnvf(target, pname, param);
}

//  void QOpenGLFunctions_1_3::glShadeModel(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_312glShadeModelEj(
    QOpenGLFunctions_1_3 *self,
    GLenum mode) {
  self->glShadeModel(mode);
}

//  void QOpenGLFunctions_1_3::glPolygonStipple(const GLubyte *mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_316glPolygonStippleEPKh(
    QOpenGLFunctions_1_3 *self,
    const GLubyte *mask) {
  self->glPolygonStipple(mask);
}

//  void QOpenGLFunctions_1_3::glMaterialiv(GLenum face, GLenum pname, const
//      GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_312glMaterialivEjjPKi(
    QOpenGLFunctions_1_3 *self,
    GLenum face,
    GLenum pname,
    const GLint *params) {
  self->glMaterialiv(face, pname, params);
}

//  void QOpenGLFunctions_1_3::glMateriali(GLenum face, GLenum pname, GLint
//      param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_311glMaterialiEjji(
    QOpenGLFunctions_1_3 *self,
    GLenum face,
    GLenum pname,
    GLint param) {
  self->glMateriali(face, pname, param);
}

//  void QOpenGLFunctions_1_3::glMaterialfv(GLenum face, GLenum pname, const
//      GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_312glMaterialfvEjjPKf(
    QOpenGLFunctions_1_3 *self,
    GLenum face,
    GLenum pname,
    const GLfloat *params) {
  self->glMaterialfv(face, pname, params);
}

//  void QOpenGLFunctions_1_3::glMaterialf(GLenum face, GLenum pname, GLfloat
//      param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_311glMaterialfEjjf(
    QOpenGLFunctions_1_3 *self,
    GLenum face,
    GLenum pname,
    GLfloat param) {
  self->glMaterialf(face, pname, param);
}

//  void QOpenGLFunctions_1_3::glLineStipple(GLint factor, GLushort pattern)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_313glLineStippleEit(
    QOpenGLFunctions_1_3 *self,
    GLint factor,
    GLushort pattern) {
  self->glLineStipple(factor, pattern);
}

//  void QOpenGLFunctions_1_3::glLightModeliv(GLenum pname, const GLint
//      *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_314glLightModelivEjPKi(
    QOpenGLFunctions_1_3 *self,
    GLenum pname,
    const GLint *params) {
  self->glLightModeliv(pname, params);
}

//  void QOpenGLFunctions_1_3::glLightModeli(GLenum pname, GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_313glLightModeliEji(
    QOpenGLFunctions_1_3 *self,
    GLenum pname,
    GLint param) {
  self->glLightModeli(pname, param);
}

//  void QOpenGLFunctions_1_3::glLightModelfv(GLenum pname, const GLfloat
//      *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_314glLightModelfvEjPKf(
    QOpenGLFunctions_1_3 *self,
    GLenum pname,
    const GLfloat *params) {
  self->glLightModelfv(pname, params);
}

//  void QOpenGLFunctions_1_3::glLightModelf(GLenum pname, GLfloat param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_313glLightModelfEjf(
    QOpenGLFunctions_1_3 *self,
    GLenum pname,
    GLfloat param) {
  self->glLightModelf(pname, param);
}

//  void QOpenGLFunctions_1_3::glLightiv(GLenum light, GLenum pname, const
//      GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_39glLightivEjjPKi(
    QOpenGLFunctions_1_3 *self,
    GLenum light,
    GLenum pname,
    const GLint *params) {
  self->glLightiv(light, pname, params);
}

//  void QOpenGLFunctions_1_3::glLighti(GLenum light, GLenum pname, GLint
//      param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_38glLightiEjji(
    QOpenGLFunctions_1_3 *self,
    GLenum light,
    GLenum pname,
    GLint param) {
  self->glLighti(light, pname, param);
}

//  void QOpenGLFunctions_1_3::glLightfv(GLenum light, GLenum pname, const
//      GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_39glLightfvEjjPKf(
    QOpenGLFunctions_1_3 *self,
    GLenum light,
    GLenum pname,
    const GLfloat *params) {
  self->glLightfv(light, pname, params);
}

//  void QOpenGLFunctions_1_3::glLightf(GLenum light, GLenum pname, GLfloat
//      param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_38glLightfEjjf(
    QOpenGLFunctions_1_3 *self,
    GLenum light,
    GLenum pname,
    GLfloat param) {
  self->glLightf(light, pname, param);
}

//  void QOpenGLFunctions_1_3::glFogiv(GLenum pname, const GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_37glFogivEjPKi(
    QOpenGLFunctions_1_3 *self,
    GLenum pname,
    const GLint *params) {
  self->glFogiv(pname, params);
}

//  void QOpenGLFunctions_1_3::glFogi(GLenum pname, GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_36glFogiEji(
    QOpenGLFunctions_1_3 *self,
    GLenum pname,
    GLint param) {
  self->glFogi(pname, param);
}

//  void QOpenGLFunctions_1_3::glFogfv(GLenum pname, const GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_37glFogfvEjPKf(
    QOpenGLFunctions_1_3 *self,
    GLenum pname,
    const GLfloat *params) {
  self->glFogfv(pname, params);
}

//  void QOpenGLFunctions_1_3::glFogf(GLenum pname, GLfloat param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_36glFogfEjf(
    QOpenGLFunctions_1_3 *self,
    GLenum pname,
    GLfloat param) {
  self->glFogf(pname, param);
}

//  void QOpenGLFunctions_1_3::glColorMaterial(GLenum face, GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_315glColorMaterialEjj(
    QOpenGLFunctions_1_3 *self,
    GLenum face,
    GLenum mode) {
  self->glColorMaterial(face, mode);
}

//  void QOpenGLFunctions_1_3::glClipPlane(GLenum plane, const GLdouble
//      *equation)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_311glClipPlaneEjPKd(
    QOpenGLFunctions_1_3 *self,
    GLenum plane,
    const GLdouble *equation) {
  self->glClipPlane(plane, equation);
}

//  void QOpenGLFunctions_1_3::glVertex4sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_311glVertex4svEPKs(
    QOpenGLFunctions_1_3 *self,
    const GLshort *v) {
  self->glVertex4sv(v);
}

//  void QOpenGLFunctions_1_3::glVertex4s(GLshort x, GLshort y, GLshort z,
//      GLshort w)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_310glVertex4sEssss(
    QOpenGLFunctions_1_3 *self,
    GLshort x,
    GLshort y,
    GLshort z,
    GLshort w) {
  self->glVertex4s(x, y, z, w);
}

//  void QOpenGLFunctions_1_3::glVertex4iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_311glVertex4ivEPKi(
    QOpenGLFunctions_1_3 *self,
    const GLint *v) {
  self->glVertex4iv(v);
}

//  void QOpenGLFunctions_1_3::glVertex4i(GLint x, GLint y, GLint z, GLint w)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_310glVertex4iEiiii(
    QOpenGLFunctions_1_3 *self,
    GLint x,
    GLint y,
    GLint z,
    GLint w) {
  self->glVertex4i(x, y, z, w);
}

//  void QOpenGLFunctions_1_3::glVertex4fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_311glVertex4fvEPKf(
    QOpenGLFunctions_1_3 *self,
    const GLfloat *v) {
  self->glVertex4fv(v);
}

//  void QOpenGLFunctions_1_3::glVertex4f(GLfloat x, GLfloat y, GLfloat z,
//      GLfloat w)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_310glVertex4fEffff(
    QOpenGLFunctions_1_3 *self,
    GLfloat x,
    GLfloat y,
    GLfloat z,
    GLfloat w) {
  self->glVertex4f(x, y, z, w);
}

//  void QOpenGLFunctions_1_3::glVertex4dv(const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_311glVertex4dvEPKd(
    QOpenGLFunctions_1_3 *self,
    const GLdouble *v) {
  self->glVertex4dv(v);
}

//  void QOpenGLFunctions_1_3::glVertex4d(GLdouble x, GLdouble y, GLdouble z,
//      GLdouble w)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_310glVertex4dEdddd(
    QOpenGLFunctions_1_3 *self,
    GLdouble x,
    GLdouble y,
    GLdouble z,
    GLdouble w) {
  self->glVertex4d(x, y, z, w);
}

//  void QOpenGLFunctions_1_3::glVertex3sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_311glVertex3svEPKs(
    QOpenGLFunctions_1_3 *self,
    const GLshort *v) {
  self->glVertex3sv(v);
}

//  void QOpenGLFunctions_1_3::glVertex3s(GLshort x, GLshort y, GLshort z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_310glVertex3sEsss(
    QOpenGLFunctions_1_3 *self,
    GLshort x,
    GLshort y,
    GLshort z) {
  self->glVertex3s(x, y, z);
}

//  void QOpenGLFunctions_1_3::glVertex3iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_311glVertex3ivEPKi(
    QOpenGLFunctions_1_3 *self,
    const GLint *v) {
  self->glVertex3iv(v);
}

//  void QOpenGLFunctions_1_3::glVertex3i(GLint x, GLint y, GLint z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_310glVertex3iEiii(
    QOpenGLFunctions_1_3 *self,
    GLint x,
    GLint y,
    GLint z) {
  self->glVertex3i(x, y, z);
}

//  void QOpenGLFunctions_1_3::glVertex3fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_311glVertex3fvEPKf(
    QOpenGLFunctions_1_3 *self,
    const GLfloat *v) {
  self->glVertex3fv(v);
}

//  void QOpenGLFunctions_1_3::glVertex3f(GLfloat x, GLfloat y, GLfloat z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_310glVertex3fEfff(
    QOpenGLFunctions_1_3 *self,
    GLfloat x,
    GLfloat y,
    GLfloat z) {
  self->glVertex3f(x, y, z);
}

//  void QOpenGLFunctions_1_3::glVertex3dv(const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_311glVertex3dvEPKd(
    QOpenGLFunctions_1_3 *self,
    const GLdouble *v) {
  self->glVertex3dv(v);
}

//  void QOpenGLFunctions_1_3::glVertex3d(GLdouble x, GLdouble y, GLdouble z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_310glVertex3dEddd(
    QOpenGLFunctions_1_3 *self,
    GLdouble x,
    GLdouble y,
    GLdouble z) {
  self->glVertex3d(x, y, z);
}

//  void QOpenGLFunctions_1_3::glVertex2sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_311glVertex2svEPKs(
    QOpenGLFunctions_1_3 *self,
    const GLshort *v) {
  self->glVertex2sv(v);
}

//  void QOpenGLFunctions_1_3::glVertex2s(GLshort x, GLshort y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_310glVertex2sEss(
    QOpenGLFunctions_1_3 *self,
    GLshort x,
    GLshort y) {
  self->glVertex2s(x, y);
}

//  void QOpenGLFunctions_1_3::glVertex2iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_311glVertex2ivEPKi(
    QOpenGLFunctions_1_3 *self,
    const GLint *v) {
  self->glVertex2iv(v);
}

//  void QOpenGLFunctions_1_3::glVertex2i(GLint x, GLint y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_310glVertex2iEii(
    QOpenGLFunctions_1_3 *self,
    GLint x,
    GLint y) {
  self->glVertex2i(x, y);
}

//  void QOpenGLFunctions_1_3::glVertex2fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_311glVertex2fvEPKf(
    QOpenGLFunctions_1_3 *self,
    const GLfloat *v) {
  self->glVertex2fv(v);
}

//  void QOpenGLFunctions_1_3::glVertex2f(GLfloat x, GLfloat y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_310glVertex2fEff(
    QOpenGLFunctions_1_3 *self,
    GLfloat x,
    GLfloat y) {
  self->glVertex2f(x, y);
}

//  void QOpenGLFunctions_1_3::glVertex2dv(const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_311glVertex2dvEPKd(
    QOpenGLFunctions_1_3 *self,
    const GLdouble *v) {
  self->glVertex2dv(v);
}

//  void QOpenGLFunctions_1_3::glVertex2d(GLdouble x, GLdouble y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_310glVertex2dEdd(
    QOpenGLFunctions_1_3 *self,
    GLdouble x,
    GLdouble y) {
  self->glVertex2d(x, y);
}

//  void QOpenGLFunctions_1_3::glTexCoord4sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_313glTexCoord4svEPKs(
    QOpenGLFunctions_1_3 *self,
    const GLshort *v) {
  self->glTexCoord4sv(v);
}

//  void QOpenGLFunctions_1_3::glTexCoord4s(GLshort s, GLshort t, GLshort r,
//      GLshort q)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_312glTexCoord4sEssss(
    QOpenGLFunctions_1_3 *self,
    GLshort s,
    GLshort t,
    GLshort r,
    GLshort q) {
  self->glTexCoord4s(s, t, r, q);
}

//  void QOpenGLFunctions_1_3::glTexCoord4iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_313glTexCoord4ivEPKi(
    QOpenGLFunctions_1_3 *self,
    const GLint *v) {
  self->glTexCoord4iv(v);
}

//  void QOpenGLFunctions_1_3::glTexCoord4i(GLint s, GLint t, GLint r, GLint
//      q)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_312glTexCoord4iEiiii(
    QOpenGLFunctions_1_3 *self,
    GLint s,
    GLint t,
    GLint r,
    GLint q) {
  self->glTexCoord4i(s, t, r, q);
}

//  void QOpenGLFunctions_1_3::glTexCoord4fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_313glTexCoord4fvEPKf(
    QOpenGLFunctions_1_3 *self,
    const GLfloat *v) {
  self->glTexCoord4fv(v);
}

//  void QOpenGLFunctions_1_3::glTexCoord4f(GLfloat s, GLfloat t, GLfloat r,
//      GLfloat q)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_312glTexCoord4fEffff(
    QOpenGLFunctions_1_3 *self,
    GLfloat s,
    GLfloat t,
    GLfloat r,
    GLfloat q) {
  self->glTexCoord4f(s, t, r, q);
}

//  void QOpenGLFunctions_1_3::glTexCoord4dv(const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_313glTexCoord4dvEPKd(
    QOpenGLFunctions_1_3 *self,
    const GLdouble *v) {
  self->glTexCoord4dv(v);
}

//  void QOpenGLFunctions_1_3::glTexCoord4d(GLdouble s, GLdouble t, GLdouble
//      r, GLdouble q)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_312glTexCoord4dEdddd(
    QOpenGLFunctions_1_3 *self,
    GLdouble s,
    GLdouble t,
    GLdouble r,
    GLdouble q) {
  self->glTexCoord4d(s, t, r, q);
}

//  void QOpenGLFunctions_1_3::glTexCoord3sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_313glTexCoord3svEPKs(
    QOpenGLFunctions_1_3 *self,
    const GLshort *v) {
  self->glTexCoord3sv(v);
}

//  void QOpenGLFunctions_1_3::glTexCoord3s(GLshort s, GLshort t, GLshort r)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_312glTexCoord3sEsss(
    QOpenGLFunctions_1_3 *self,
    GLshort s,
    GLshort t,
    GLshort r) {
  self->glTexCoord3s(s, t, r);
}

//  void QOpenGLFunctions_1_3::glTexCoord3iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_313glTexCoord3ivEPKi(
    QOpenGLFunctions_1_3 *self,
    const GLint *v) {
  self->glTexCoord3iv(v);
}

//  void QOpenGLFunctions_1_3::glTexCoord3i(GLint s, GLint t, GLint r)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_312glTexCoord3iEiii(
    QOpenGLFunctions_1_3 *self,
    GLint s,
    GLint t,
    GLint r) {
  self->glTexCoord3i(s, t, r);
}

//  void QOpenGLFunctions_1_3::glTexCoord3fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_313glTexCoord3fvEPKf(
    QOpenGLFunctions_1_3 *self,
    const GLfloat *v) {
  self->glTexCoord3fv(v);
}

//  void QOpenGLFunctions_1_3::glTexCoord3f(GLfloat s, GLfloat t, GLfloat r)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_312glTexCoord3fEfff(
    QOpenGLFunctions_1_3 *self,
    GLfloat s,
    GLfloat t,
    GLfloat r) {
  self->glTexCoord3f(s, t, r);
}

//  void QOpenGLFunctions_1_3::glTexCoord3dv(const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_313glTexCoord3dvEPKd(
    QOpenGLFunctions_1_3 *self,
    const GLdouble *v) {
  self->glTexCoord3dv(v);
}

//  void QOpenGLFunctions_1_3::glTexCoord3d(GLdouble s, GLdouble t, GLdouble
//      r)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_312glTexCoord3dEddd(
    QOpenGLFunctions_1_3 *self,
    GLdouble s,
    GLdouble t,
    GLdouble r) {
  self->glTexCoord3d(s, t, r);
}

//  void QOpenGLFunctions_1_3::glTexCoord2sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_313glTexCoord2svEPKs(
    QOpenGLFunctions_1_3 *self,
    const GLshort *v) {
  self->glTexCoord2sv(v);
}

//  void QOpenGLFunctions_1_3::glTexCoord2s(GLshort s, GLshort t)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_312glTexCoord2sEss(
    QOpenGLFunctions_1_3 *self,
    GLshort s,
    GLshort t) {
  self->glTexCoord2s(s, t);
}

//  void QOpenGLFunctions_1_3::glTexCoord2iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_313glTexCoord2ivEPKi(
    QOpenGLFunctions_1_3 *self,
    const GLint *v) {
  self->glTexCoord2iv(v);
}

//  void QOpenGLFunctions_1_3::glTexCoord2i(GLint s, GLint t)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_312glTexCoord2iEii(
    QOpenGLFunctions_1_3 *self,
    GLint s,
    GLint t) {
  self->glTexCoord2i(s, t);
}

//  void QOpenGLFunctions_1_3::glTexCoord2fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_313glTexCoord2fvEPKf(
    QOpenGLFunctions_1_3 *self,
    const GLfloat *v) {
  self->glTexCoord2fv(v);
}

//  void QOpenGLFunctions_1_3::glTexCoord2f(GLfloat s, GLfloat t)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_312glTexCoord2fEff(
    QOpenGLFunctions_1_3 *self,
    GLfloat s,
    GLfloat t) {
  self->glTexCoord2f(s, t);
}

//  void QOpenGLFunctions_1_3::glTexCoord2dv(const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_313glTexCoord2dvEPKd(
    QOpenGLFunctions_1_3 *self,
    const GLdouble *v) {
  self->glTexCoord2dv(v);
}

//  void QOpenGLFunctions_1_3::glTexCoord2d(GLdouble s, GLdouble t)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_312glTexCoord2dEdd(
    QOpenGLFunctions_1_3 *self,
    GLdouble s,
    GLdouble t) {
  self->glTexCoord2d(s, t);
}

//  void QOpenGLFunctions_1_3::glTexCoord1sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_313glTexCoord1svEPKs(
    QOpenGLFunctions_1_3 *self,
    const GLshort *v) {
  self->glTexCoord1sv(v);
}

//  void QOpenGLFunctions_1_3::glTexCoord1s(GLshort s)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_312glTexCoord1sEs(
    QOpenGLFunctions_1_3 *self,
    GLshort s) {
  self->glTexCoord1s(s);
}

//  void QOpenGLFunctions_1_3::glTexCoord1iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_313glTexCoord1ivEPKi(
    QOpenGLFunctions_1_3 *self,
    const GLint *v) {
  self->glTexCoord1iv(v);
}

//  void QOpenGLFunctions_1_3::glTexCoord1i(GLint s)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_312glTexCoord1iEi(
    QOpenGLFunctions_1_3 *self,
    GLint s) {
  self->glTexCoord1i(s);
}

//  void QOpenGLFunctions_1_3::glTexCoord1fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_313glTexCoord1fvEPKf(
    QOpenGLFunctions_1_3 *self,
    const GLfloat *v) {
  self->glTexCoord1fv(v);
}

//  void QOpenGLFunctions_1_3::glTexCoord1f(GLfloat s)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_312glTexCoord1fEf(
    QOpenGLFunctions_1_3 *self,
    GLfloat s) {
  self->glTexCoord1f(s);
}

//  void QOpenGLFunctions_1_3::glTexCoord1dv(const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_313glTexCoord1dvEPKd(
    QOpenGLFunctions_1_3 *self,
    const GLdouble *v) {
  self->glTexCoord1dv(v);
}

//  void QOpenGLFunctions_1_3::glTexCoord1d(GLdouble s)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_312glTexCoord1dEd(
    QOpenGLFunctions_1_3 *self,
    GLdouble s) {
  self->glTexCoord1d(s);
}

//  void QOpenGLFunctions_1_3::glRectsv(const GLshort *v1, const GLshort *v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_38glRectsvEPKsS1_(
    QOpenGLFunctions_1_3 *self,
    const GLshort *v1,
    const GLshort *v2) {
  self->glRectsv(v1, v2);
}

//  void QOpenGLFunctions_1_3::glRects(GLshort x1, GLshort y1, GLshort x2,
//      GLshort y2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_37glRectsEssss(
    QOpenGLFunctions_1_3 *self,
    GLshort x1,
    GLshort y1,
    GLshort x2,
    GLshort y2) {
  self->glRects(x1, y1, x2, y2);
}

//  void QOpenGLFunctions_1_3::glRectiv(const GLint *v1, const GLint *v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_38glRectivEPKiS1_(
    QOpenGLFunctions_1_3 *self,
    const GLint *v1,
    const GLint *v2) {
  self->glRectiv(v1, v2);
}

//  void QOpenGLFunctions_1_3::glRecti(GLint x1, GLint y1, GLint x2, GLint
//      y2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_37glRectiEiiii(
    QOpenGLFunctions_1_3 *self,
    GLint x1,
    GLint y1,
    GLint x2,
    GLint y2) {
  self->glRecti(x1, y1, x2, y2);
}

//  void QOpenGLFunctions_1_3::glRectfv(const GLfloat *v1, const GLfloat *v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_38glRectfvEPKfS1_(
    QOpenGLFunctions_1_3 *self,
    const GLfloat *v1,
    const GLfloat *v2) {
  self->glRectfv(v1, v2);
}

//  void QOpenGLFunctions_1_3::glRectf(GLfloat x1, GLfloat y1, GLfloat x2,
//      GLfloat y2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_37glRectfEffff(
    QOpenGLFunctions_1_3 *self,
    GLfloat x1,
    GLfloat y1,
    GLfloat x2,
    GLfloat y2) {
  self->glRectf(x1, y1, x2, y2);
}

//  void QOpenGLFunctions_1_3::glRectdv(const GLdouble *v1, const GLdouble
//      *v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_38glRectdvEPKdS1_(
    QOpenGLFunctions_1_3 *self,
    const GLdouble *v1,
    const GLdouble *v2) {
  self->glRectdv(v1, v2);
}

//  void QOpenGLFunctions_1_3::glRectd(GLdouble x1, GLdouble y1, GLdouble x2,
//      GLdouble y2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_37glRectdEdddd(
    QOpenGLFunctions_1_3 *self,
    GLdouble x1,
    GLdouble y1,
    GLdouble x2,
    GLdouble y2) {
  self->glRectd(x1, y1, x2, y2);
}

//  void QOpenGLFunctions_1_3::glRasterPos4sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_314glRasterPos4svEPKs(
    QOpenGLFunctions_1_3 *self,
    const GLshort *v) {
  self->glRasterPos4sv(v);
}

//  void QOpenGLFunctions_1_3::glRasterPos4s(GLshort x, GLshort y, GLshort z,
//      GLshort w)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_313glRasterPos4sEssss(
    QOpenGLFunctions_1_3 *self,
    GLshort x,
    GLshort y,
    GLshort z,
    GLshort w) {
  self->glRasterPos4s(x, y, z, w);
}

//  void QOpenGLFunctions_1_3::glRasterPos4iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_314glRasterPos4ivEPKi(
    QOpenGLFunctions_1_3 *self,
    const GLint *v) {
  self->glRasterPos4iv(v);
}

//  void QOpenGLFunctions_1_3::glRasterPos4i(GLint x, GLint y, GLint z, GLint
//      w)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_313glRasterPos4iEiiii(
    QOpenGLFunctions_1_3 *self,
    GLint x,
    GLint y,
    GLint z,
    GLint w) {
  self->glRasterPos4i(x, y, z, w);
}

//  void QOpenGLFunctions_1_3::glRasterPos4fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_314glRasterPos4fvEPKf(
    QOpenGLFunctions_1_3 *self,
    const GLfloat *v) {
  self->glRasterPos4fv(v);
}

//  void QOpenGLFunctions_1_3::glRasterPos4f(GLfloat x, GLfloat y, GLfloat z,
//      GLfloat w)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_313glRasterPos4fEffff(
    QOpenGLFunctions_1_3 *self,
    GLfloat x,
    GLfloat y,
    GLfloat z,
    GLfloat w) {
  self->glRasterPos4f(x, y, z, w);
}

//  void QOpenGLFunctions_1_3::glRasterPos4dv(const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_314glRasterPos4dvEPKd(
    QOpenGLFunctions_1_3 *self,
    const GLdouble *v) {
  self->glRasterPos4dv(v);
}

//  void QOpenGLFunctions_1_3::glRasterPos4d(GLdouble x, GLdouble y, GLdouble
//      z, GLdouble w)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_313glRasterPos4dEdddd(
    QOpenGLFunctions_1_3 *self,
    GLdouble x,
    GLdouble y,
    GLdouble z,
    GLdouble w) {
  self->glRasterPos4d(x, y, z, w);
}

//  void QOpenGLFunctions_1_3::glRasterPos3sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_314glRasterPos3svEPKs(
    QOpenGLFunctions_1_3 *self,
    const GLshort *v) {
  self->glRasterPos3sv(v);
}

//  void QOpenGLFunctions_1_3::glRasterPos3s(GLshort x, GLshort y, GLshort z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_313glRasterPos3sEsss(
    QOpenGLFunctions_1_3 *self,
    GLshort x,
    GLshort y,
    GLshort z) {
  self->glRasterPos3s(x, y, z);
}

//  void QOpenGLFunctions_1_3::glRasterPos3iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_314glRasterPos3ivEPKi(
    QOpenGLFunctions_1_3 *self,
    const GLint *v) {
  self->glRasterPos3iv(v);
}

//  void QOpenGLFunctions_1_3::glRasterPos3i(GLint x, GLint y, GLint z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_313glRasterPos3iEiii(
    QOpenGLFunctions_1_3 *self,
    GLint x,
    GLint y,
    GLint z) {
  self->glRasterPos3i(x, y, z);
}

//  void QOpenGLFunctions_1_3::glRasterPos3fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_314glRasterPos3fvEPKf(
    QOpenGLFunctions_1_3 *self,
    const GLfloat *v) {
  self->glRasterPos3fv(v);
}

//  void QOpenGLFunctions_1_3::glRasterPos3f(GLfloat x, GLfloat y, GLfloat z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_313glRasterPos3fEfff(
    QOpenGLFunctions_1_3 *self,
    GLfloat x,
    GLfloat y,
    GLfloat z) {
  self->glRasterPos3f(x, y, z);
}

//  void QOpenGLFunctions_1_3::glRasterPos3dv(const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_314glRasterPos3dvEPKd(
    QOpenGLFunctions_1_3 *self,
    const GLdouble *v) {
  self->glRasterPos3dv(v);
}

//  void QOpenGLFunctions_1_3::glRasterPos3d(GLdouble x, GLdouble y, GLdouble
//      z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_313glRasterPos3dEddd(
    QOpenGLFunctions_1_3 *self,
    GLdouble x,
    GLdouble y,
    GLdouble z) {
  self->glRasterPos3d(x, y, z);
}

//  void QOpenGLFunctions_1_3::glRasterPos2sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_314glRasterPos2svEPKs(
    QOpenGLFunctions_1_3 *self,
    const GLshort *v) {
  self->glRasterPos2sv(v);
}

//  void QOpenGLFunctions_1_3::glRasterPos2s(GLshort x, GLshort y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_313glRasterPos2sEss(
    QOpenGLFunctions_1_3 *self,
    GLshort x,
    GLshort y) {
  self->glRasterPos2s(x, y);
}

//  void QOpenGLFunctions_1_3::glRasterPos2iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_314glRasterPos2ivEPKi(
    QOpenGLFunctions_1_3 *self,
    const GLint *v) {
  self->glRasterPos2iv(v);
}

//  void QOpenGLFunctions_1_3::glRasterPos2i(GLint x, GLint y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_313glRasterPos2iEii(
    QOpenGLFunctions_1_3 *self,
    GLint x,
    GLint y) {
  self->glRasterPos2i(x, y);
}

//  void QOpenGLFunctions_1_3::glRasterPos2fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_314glRasterPos2fvEPKf(
    QOpenGLFunctions_1_3 *self,
    const GLfloat *v) {
  self->glRasterPos2fv(v);
}

//  void QOpenGLFunctions_1_3::glRasterPos2f(GLfloat x, GLfloat y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_313glRasterPos2fEff(
    QOpenGLFunctions_1_3 *self,
    GLfloat x,
    GLfloat y) {
  self->glRasterPos2f(x, y);
}

//  void QOpenGLFunctions_1_3::glRasterPos2dv(const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_314glRasterPos2dvEPKd(
    QOpenGLFunctions_1_3 *self,
    const GLdouble *v) {
  self->glRasterPos2dv(v);
}

//  void QOpenGLFunctions_1_3::glRasterPos2d(GLdouble x, GLdouble y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_313glRasterPos2dEdd(
    QOpenGLFunctions_1_3 *self,
    GLdouble x,
    GLdouble y) {
  self->glRasterPos2d(x, y);
}

//  void QOpenGLFunctions_1_3::glNormal3sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_311glNormal3svEPKs(
    QOpenGLFunctions_1_3 *self,
    const GLshort *v) {
  self->glNormal3sv(v);
}

//  void QOpenGLFunctions_1_3::glNormal3s(GLshort nx, GLshort ny, GLshort nz)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_310glNormal3sEsss(
    QOpenGLFunctions_1_3 *self,
    GLshort nx,
    GLshort ny,
    GLshort nz) {
  self->glNormal3s(nx, ny, nz);
}

//  void QOpenGLFunctions_1_3::glNormal3iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_311glNormal3ivEPKi(
    QOpenGLFunctions_1_3 *self,
    const GLint *v) {
  self->glNormal3iv(v);
}

//  void QOpenGLFunctions_1_3::glNormal3i(GLint nx, GLint ny, GLint nz)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_310glNormal3iEiii(
    QOpenGLFunctions_1_3 *self,
    GLint nx,
    GLint ny,
    GLint nz) {
  self->glNormal3i(nx, ny, nz);
}

//  void QOpenGLFunctions_1_3::glNormal3fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_311glNormal3fvEPKf(
    QOpenGLFunctions_1_3 *self,
    const GLfloat *v) {
  self->glNormal3fv(v);
}

//  void QOpenGLFunctions_1_3::glNormal3f(GLfloat nx, GLfloat ny, GLfloat nz)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_310glNormal3fEfff(
    QOpenGLFunctions_1_3 *self,
    GLfloat nx,
    GLfloat ny,
    GLfloat nz) {
  self->glNormal3f(nx, ny, nz);
}

//  void QOpenGLFunctions_1_3::glNormal3dv(const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_311glNormal3dvEPKd(
    QOpenGLFunctions_1_3 *self,
    const GLdouble *v) {
  self->glNormal3dv(v);
}

//  void QOpenGLFunctions_1_3::glNormal3d(GLdouble nx, GLdouble ny, GLdouble
//      nz)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_310glNormal3dEddd(
    QOpenGLFunctions_1_3 *self,
    GLdouble nx,
    GLdouble ny,
    GLdouble nz) {
  self->glNormal3d(nx, ny, nz);
}

//  void QOpenGLFunctions_1_3::glNormal3bv(const GLbyte *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_311glNormal3bvEPKa(
    QOpenGLFunctions_1_3 *self,
    const GLbyte *v) {
  self->glNormal3bv(v);
}

//  void QOpenGLFunctions_1_3::glNormal3b(GLbyte nx, GLbyte ny, GLbyte nz)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_310glNormal3bEaaa(
    QOpenGLFunctions_1_3 *self,
    GLbyte nx,
    GLbyte ny,
    GLbyte nz) {
  self->glNormal3b(nx, ny, nz);
}

//  void QOpenGLFunctions_1_3::glIndexsv(const GLshort *c)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_39glIndexsvEPKs(
    QOpenGLFunctions_1_3 *self,
    const GLshort *c) {
  self->glIndexsv(c);
}

//  void QOpenGLFunctions_1_3::glIndexs(GLshort c)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_38glIndexsEs(
    QOpenGLFunctions_1_3 *self,
    GLshort c) {
  self->glIndexs(c);
}

//  void QOpenGLFunctions_1_3::glIndexiv(const GLint *c)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_39glIndexivEPKi(
    QOpenGLFunctions_1_3 *self,
    const GLint *c) {
  self->glIndexiv(c);
}

//  void QOpenGLFunctions_1_3::glIndexi(GLint c)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_38glIndexiEi(
    QOpenGLFunctions_1_3 *self,
    GLint c) {
  self->glIndexi(c);
}

//  void QOpenGLFunctions_1_3::glIndexfv(const GLfloat *c)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_39glIndexfvEPKf(
    QOpenGLFunctions_1_3 *self,
    const GLfloat *c) {
  self->glIndexfv(c);
}

//  void QOpenGLFunctions_1_3::glIndexf(GLfloat c)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_38glIndexfEf(
    QOpenGLFunctions_1_3 *self,
    GLfloat c) {
  self->glIndexf(c);
}

//  void QOpenGLFunctions_1_3::glIndexdv(const GLdouble *c)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_39glIndexdvEPKd(
    QOpenGLFunctions_1_3 *self,
    const GLdouble *c) {
  self->glIndexdv(c);
}

//  void QOpenGLFunctions_1_3::glIndexd(GLdouble c)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_38glIndexdEd(
    QOpenGLFunctions_1_3 *self,
    GLdouble c) {
  self->glIndexd(c);
}

//  void QOpenGLFunctions_1_3::glEnd()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_35glEndEv(QOpenGLFunctions_1_3 *self) {
  self->glEnd();
}

//  void QOpenGLFunctions_1_3::glEdgeFlagv(const GLboolean *flag)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_311glEdgeFlagvEPKh(
    QOpenGLFunctions_1_3 *self,
    const GLboolean *flag) {
  self->glEdgeFlagv(flag);
}

//  void QOpenGLFunctions_1_3::glEdgeFlag(GLboolean flag)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_310glEdgeFlagEh(
    QOpenGLFunctions_1_3 *self,
    GLboolean flag) {
  self->glEdgeFlag(flag);
}

//  void QOpenGLFunctions_1_3::glColor4usv(const GLushort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_311glColor4usvEPKt(
    QOpenGLFunctions_1_3 *self,
    const GLushort *v) {
  self->glColor4usv(v);
}

//  void QOpenGLFunctions_1_3::glColor4us(GLushort red, GLushort green,
//      GLushort blue, GLushort alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_310glColor4usEtttt(
    QOpenGLFunctions_1_3 *self,
    GLushort red,
    GLushort green,
    GLushort blue,
    GLushort alpha) {
  self->glColor4us(red, green, blue, alpha);
}

//  void QOpenGLFunctions_1_3::glColor4uiv(const GLuint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_311glColor4uivEPKj(
    QOpenGLFunctions_1_3 *self,
    const GLuint *v) {
  self->glColor4uiv(v);
}

//  void QOpenGLFunctions_1_3::glColor4ui(GLuint red, GLuint green, GLuint
//      blue, GLuint alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_310glColor4uiEjjjj(
    QOpenGLFunctions_1_3 *self,
    GLuint red,
    GLuint green,
    GLuint blue,
    GLuint alpha) {
  self->glColor4ui(red, green, blue, alpha);
}

//  void QOpenGLFunctions_1_3::glColor4ubv(const GLubyte *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_311glColor4ubvEPKh(
    QOpenGLFunctions_1_3 *self,
    const GLubyte *v) {
  self->glColor4ubv(v);
}

//  void QOpenGLFunctions_1_3::glColor4ub(GLubyte red, GLubyte green, GLubyte
//      blue, GLubyte alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_310glColor4ubEhhhh(
    QOpenGLFunctions_1_3 *self,
    GLubyte red,
    GLubyte green,
    GLubyte blue,
    GLubyte alpha) {
  self->glColor4ub(red, green, blue, alpha);
}

//  void QOpenGLFunctions_1_3::glColor4sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_310glColor4svEPKs(
    QOpenGLFunctions_1_3 *self,
    const GLshort *v) {
  self->glColor4sv(v);
}

//  void QOpenGLFunctions_1_3::glColor4s(GLshort red, GLshort green, GLshort
//      blue, GLshort alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_39glColor4sEssss(
    QOpenGLFunctions_1_3 *self,
    GLshort red,
    GLshort green,
    GLshort blue,
    GLshort alpha) {
  self->glColor4s(red, green, blue, alpha);
}

//  void QOpenGLFunctions_1_3::glColor4iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_310glColor4ivEPKi(
    QOpenGLFunctions_1_3 *self,
    const GLint *v) {
  self->glColor4iv(v);
}

//  void QOpenGLFunctions_1_3::glColor4i(GLint red, GLint green, GLint blue,
//      GLint alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_39glColor4iEiiii(
    QOpenGLFunctions_1_3 *self,
    GLint red,
    GLint green,
    GLint blue,
    GLint alpha) {
  self->glColor4i(red, green, blue, alpha);
}

//  void QOpenGLFunctions_1_3::glColor4fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_310glColor4fvEPKf(
    QOpenGLFunctions_1_3 *self,
    const GLfloat *v) {
  self->glColor4fv(v);
}

//  void QOpenGLFunctions_1_3::glColor4f(GLfloat red, GLfloat green, GLfloat
//      blue, GLfloat alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_39glColor4fEffff(
    QOpenGLFunctions_1_3 *self,
    GLfloat red,
    GLfloat green,
    GLfloat blue,
    GLfloat alpha) {
  self->glColor4f(red, green, blue, alpha);
}

//  void QOpenGLFunctions_1_3::glColor4dv(const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_310glColor4dvEPKd(
    QOpenGLFunctions_1_3 *self,
    const GLdouble *v) {
  self->glColor4dv(v);
}

//  void QOpenGLFunctions_1_3::glColor4d(GLdouble red, GLdouble green,
//      GLdouble blue, GLdouble alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_39glColor4dEdddd(
    QOpenGLFunctions_1_3 *self,
    GLdouble red,
    GLdouble green,
    GLdouble blue,
    GLdouble alpha) {
  self->glColor4d(red, green, blue, alpha);
}

//  void QOpenGLFunctions_1_3::glColor4bv(const GLbyte *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_310glColor4bvEPKa(
    QOpenGLFunctions_1_3 *self,
    const GLbyte *v) {
  self->glColor4bv(v);
}

//  void QOpenGLFunctions_1_3::glColor4b(GLbyte red, GLbyte green, GLbyte
//      blue, GLbyte alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_39glColor4bEaaaa(
    QOpenGLFunctions_1_3 *self,
    GLbyte red,
    GLbyte green,
    GLbyte blue,
    GLbyte alpha) {
  self->glColor4b(red, green, blue, alpha);
}

//  void QOpenGLFunctions_1_3::glColor3usv(const GLushort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_311glColor3usvEPKt(
    QOpenGLFunctions_1_3 *self,
    const GLushort *v) {
  self->glColor3usv(v);
}

//  void QOpenGLFunctions_1_3::glColor3us(GLushort red, GLushort green,
//      GLushort blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_310glColor3usEttt(
    QOpenGLFunctions_1_3 *self,
    GLushort red,
    GLushort green,
    GLushort blue) {
  self->glColor3us(red, green, blue);
}

//  void QOpenGLFunctions_1_3::glColor3uiv(const GLuint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_311glColor3uivEPKj(
    QOpenGLFunctions_1_3 *self,
    const GLuint *v) {
  self->glColor3uiv(v);
}

//  void QOpenGLFunctions_1_3::glColor3ui(GLuint red, GLuint green, GLuint
//      blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_310glColor3uiEjjj(
    QOpenGLFunctions_1_3 *self,
    GLuint red,
    GLuint green,
    GLuint blue) {
  self->glColor3ui(red, green, blue);
}

//  void QOpenGLFunctions_1_3::glColor3ubv(const GLubyte *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_311glColor3ubvEPKh(
    QOpenGLFunctions_1_3 *self,
    const GLubyte *v) {
  self->glColor3ubv(v);
}

//  void QOpenGLFunctions_1_3::glColor3ub(GLubyte red, GLubyte green, GLubyte
//      blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_310glColor3ubEhhh(
    QOpenGLFunctions_1_3 *self,
    GLubyte red,
    GLubyte green,
    GLubyte blue) {
  self->glColor3ub(red, green, blue);
}

//  void QOpenGLFunctions_1_3::glColor3sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_310glColor3svEPKs(
    QOpenGLFunctions_1_3 *self,
    const GLshort *v) {
  self->glColor3sv(v);
}

//  void QOpenGLFunctions_1_3::glColor3s(GLshort red, GLshort green, GLshort
//      blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_39glColor3sEsss(
    QOpenGLFunctions_1_3 *self,
    GLshort red,
    GLshort green,
    GLshort blue) {
  self->glColor3s(red, green, blue);
}

//  void QOpenGLFunctions_1_3::glColor3iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_310glColor3ivEPKi(
    QOpenGLFunctions_1_3 *self,
    const GLint *v) {
  self->glColor3iv(v);
}

//  void QOpenGLFunctions_1_3::glColor3i(GLint red, GLint green, GLint blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_39glColor3iEiii(
    QOpenGLFunctions_1_3 *self,
    GLint red,
    GLint green,
    GLint blue) {
  self->glColor3i(red, green, blue);
}

//  void QOpenGLFunctions_1_3::glColor3fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_310glColor3fvEPKf(
    QOpenGLFunctions_1_3 *self,
    const GLfloat *v) {
  self->glColor3fv(v);
}

//  void QOpenGLFunctions_1_3::glColor3f(GLfloat red, GLfloat green, GLfloat
//      blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_39glColor3fEfff(
    QOpenGLFunctions_1_3 *self,
    GLfloat red,
    GLfloat green,
    GLfloat blue) {
  self->glColor3f(red, green, blue);
}

//  void QOpenGLFunctions_1_3::glColor3dv(const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_310glColor3dvEPKd(
    QOpenGLFunctions_1_3 *self,
    const GLdouble *v) {
  self->glColor3dv(v);
}

//  void QOpenGLFunctions_1_3::glColor3d(GLdouble red, GLdouble green,
//      GLdouble blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_39glColor3dEddd(
    QOpenGLFunctions_1_3 *self,
    GLdouble red,
    GLdouble green,
    GLdouble blue) {
  self->glColor3d(red, green, blue);
}

//  void QOpenGLFunctions_1_3::glColor3bv(const GLbyte *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_310glColor3bvEPKa(
    QOpenGLFunctions_1_3 *self,
    const GLbyte *v) {
  self->glColor3bv(v);
}

//  void QOpenGLFunctions_1_3::glColor3b(GLbyte red, GLbyte green, GLbyte
//      blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_39glColor3bEaaa(
    QOpenGLFunctions_1_3 *self,
    GLbyte red,
    GLbyte green,
    GLbyte blue) {
  self->glColor3b(red, green, blue);
}

//  void QOpenGLFunctions_1_3::glBitmap(GLsizei width, GLsizei height,
//      GLfloat xorig, GLfloat yorig, GLfloat xmove, GLfloat ymove, const
//      GLubyte *bitmap)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_38glBitmapEiiffffPKh(
    QOpenGLFunctions_1_3 *self,
    GLsizei width,
    GLsizei height,
    GLfloat xorig,
    GLfloat yorig,
    GLfloat xmove,
    GLfloat ymove,
    const GLubyte *bitmap) {
  self->glBitmap(width, height, xorig, yorig, xmove, ymove, bitmap);
}

//  void QOpenGLFunctions_1_3::glBegin(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_37glBeginEj(
    QOpenGLFunctions_1_3 *self,
    GLenum mode) {
  self->glBegin(mode);
}

//  void QOpenGLFunctions_1_3::glListBase(GLuint base)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_310glListBaseEj(
    QOpenGLFunctions_1_3 *self,
    GLuint base) {
  self->glListBase(base);
}

//  GLuint QOpenGLFunctions_1_3::glGenLists(GLsizei range)
extern "C" Q_DECL_EXPORT
GLuint ritual_ZN20QOpenGLFunctions_1_310glGenListsEi(
    QOpenGLFunctions_1_3 *self,
    GLsizei range) {
  return self->glGenLists(range);
}

//  void QOpenGLFunctions_1_3::glDeleteLists(GLuint list, GLsizei range)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_313glDeleteListsEji(
    QOpenGLFunctions_1_3 *self,
    GLuint list,
    GLsizei range) {
  self->glDeleteLists(list, range);
}

//  void QOpenGLFunctions_1_3::glCallLists(GLsizei n, GLenum type, const
//      GLvoid *lists)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_311glCallListsEijPKv(
    QOpenGLFunctions_1_3 *self,
    GLsizei n,
    GLenum type,
    const GLvoid *lists) {
  self->glCallLists(n, type, lists);
}

//  void QOpenGLFunctions_1_3::glCallList(GLuint list)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_310glCallListEj(
    QOpenGLFunctions_1_3 *self,
    GLuint list) {
  self->glCallList(list);
}

//  void QOpenGLFunctions_1_3::glEndList()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_39glEndListEv(
    QOpenGLFunctions_1_3 *self) {
  self->glEndList();
}

//  void QOpenGLFunctions_1_3::glNewList(GLuint list, GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_39glNewListEjj(
    QOpenGLFunctions_1_3 *self,
    GLuint list,
    GLenum mode) {
  self->glNewList(list, mode);
}

//  void QOpenGLFunctions_1_3::glPushClientAttrib(GLbitfield mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_318glPushClientAttribEj(
    QOpenGLFunctions_1_3 *self,
    GLbitfield mask) {
  self->glPushClientAttrib(mask);
}

//  void QOpenGLFunctions_1_3::glPopClientAttrib()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_317glPopClientAttribEv(
    QOpenGLFunctions_1_3 *self) {
  self->glPopClientAttrib();
}

//  void QOpenGLFunctions_1_3::glPrioritizeTextures(GLsizei n, const GLuint
//      *textures, const GLfloat *priorities)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_320glPrioritizeTexturesEiPKjPKf(
    QOpenGLFunctions_1_3 *self,
    GLsizei n,
    const GLuint *textures,
    const GLfloat *priorities) {
  self->glPrioritizeTextures(n, textures, priorities);
}

//  GLboolean QOpenGLFunctions_1_3::glAreTexturesResident(GLsizei n, const
//      GLuint *textures, GLboolean *residences)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN20QOpenGLFunctions_1_321glAreTexturesResidentEiPKjPh(
    QOpenGLFunctions_1_3 *self,
    GLsizei n,
    const GLuint *textures,
    GLboolean *residences) {
  return self->glAreTexturesResident(n, textures, residences);
}

//  void QOpenGLFunctions_1_3::glVertexPointer(GLint size, GLenum type,
//      GLsizei stride, const GLvoid *pointer)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_315glVertexPointerEijiPKv(
    QOpenGLFunctions_1_3 *self,
    GLint size,
    GLenum type,
    GLsizei stride,
    const GLvoid *pointer) {
  self->glVertexPointer(size, type, stride, pointer);
}

//  void QOpenGLFunctions_1_3::glTexCoordPointer(GLint size, GLenum type,
//      GLsizei stride, const GLvoid *pointer)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_317glTexCoordPointerEijiPKv(
    QOpenGLFunctions_1_3 *self,
    GLint size,
    GLenum type,
    GLsizei stride,
    const GLvoid *pointer) {
  self->glTexCoordPointer(size, type, stride, pointer);
}

//  void QOpenGLFunctions_1_3::glNormalPointer(GLenum type, GLsizei stride,
//      const GLvoid *pointer)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_315glNormalPointerEjiPKv(
    QOpenGLFunctions_1_3 *self,
    GLenum type,
    GLsizei stride,
    const GLvoid *pointer) {
  self->glNormalPointer(type, stride, pointer);
}

//  void QOpenGLFunctions_1_3::glInterleavedArrays(GLenum format, GLsizei
//      stride, const GLvoid *pointer)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_319glInterleavedArraysEjiPKv(
    QOpenGLFunctions_1_3 *self,
    GLenum format,
    GLsizei stride,
    const GLvoid *pointer) {
  self->glInterleavedArrays(format, stride, pointer);
}

//  void QOpenGLFunctions_1_3::glIndexPointer(GLenum type, GLsizei stride,
//      const GLvoid *pointer)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_314glIndexPointerEjiPKv(
    QOpenGLFunctions_1_3 *self,
    GLenum type,
    GLsizei stride,
    const GLvoid *pointer) {
  self->glIndexPointer(type, stride, pointer);
}

//  void QOpenGLFunctions_1_3::glEnableClientState(GLenum array)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_319glEnableClientStateEj(
    QOpenGLFunctions_1_3 *self,
    GLenum array) {
  self->glEnableClientState(array);
}

//  void QOpenGLFunctions_1_3::glEdgeFlagPointer(GLsizei stride, const GLvoid
//      *pointer)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_317glEdgeFlagPointerEiPKv(
    QOpenGLFunctions_1_3 *self,
    GLsizei stride,
    const GLvoid *pointer) {
  self->glEdgeFlagPointer(stride, pointer);
}

//  void QOpenGLFunctions_1_3::glDisableClientState(GLenum array)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_320glDisableClientStateEj(
    QOpenGLFunctions_1_3 *self,
    GLenum array) {
  self->glDisableClientState(array);
}

//  void QOpenGLFunctions_1_3::glColorPointer(GLint size, GLenum type,
//      GLsizei stride, const GLvoid *pointer)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_314glColorPointerEijiPKv(
    QOpenGLFunctions_1_3 *self,
    GLint size,
    GLenum type,
    GLsizei stride,
    const GLvoid *pointer) {
  self->glColorPointer(size, type, stride, pointer);
}

//  void QOpenGLFunctions_1_3::glArrayElement(GLint i)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_314glArrayElementEi(
    QOpenGLFunctions_1_3 *self,
    GLint i) {
  self->glArrayElement(i);
}

//  void QOpenGLFunctions_1_3::glResetMinmax(GLenum target)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_313glResetMinmaxEj(
    QOpenGLFunctions_1_3 *self,
    GLenum target) {
  self->glResetMinmax(target);
}

//  void QOpenGLFunctions_1_3::glResetHistogram(GLenum target)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_316glResetHistogramEj(
    QOpenGLFunctions_1_3 *self,
    GLenum target) {
  self->glResetHistogram(target);
}

//  void QOpenGLFunctions_1_3::glMinmax(GLenum target, GLenum internalformat,
//      GLboolean sink)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_38glMinmaxEjjh(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    GLenum internalformat,
    GLboolean sink) {
  self->glMinmax(target, internalformat, sink);
}

//  void QOpenGLFunctions_1_3::glHistogram(GLenum target, GLsizei width,
//      GLenum internalformat, GLboolean sink)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_311glHistogramEjijh(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    GLsizei width,
    GLenum internalformat,
    GLboolean sink) {
  self->glHistogram(target, width, internalformat, sink);
}

//  void QOpenGLFunctions_1_3::glGetMinmaxParameteriv(GLenum target, GLenum
//      pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_322glGetMinmaxParameterivEjjPi(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    GLenum pname,
    GLint *params) {
  self->glGetMinmaxParameteriv(target, pname, params);
}

//  void QOpenGLFunctions_1_3::glGetMinmaxParameterfv(GLenum target, GLenum
//      pname, GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_322glGetMinmaxParameterfvEjjPf(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    GLenum pname,
    GLfloat *params) {
  self->glGetMinmaxParameterfv(target, pname, params);
}

//  void QOpenGLFunctions_1_3::glGetMinmax(GLenum target, GLboolean reset,
//      GLenum format, GLenum type, GLvoid *values)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_311glGetMinmaxEjhjjPv(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    GLboolean reset,
    GLenum format,
    GLenum type,
    GLvoid *values) {
  self->glGetMinmax(target, reset, format, type, values);
}

//  void QOpenGLFunctions_1_3::glGetHistogramParameteriv(GLenum target,
//      GLenum pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_325glGetHistogramParameterivEjjPi(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    GLenum pname,
    GLint *params) {
  self->glGetHistogramParameteriv(target, pname, params);
}

//  void QOpenGLFunctions_1_3::glGetHistogramParameterfv(GLenum target,
//      GLenum pname, GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_325glGetHistogramParameterfvEjjPf(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    GLenum pname,
    GLfloat *params) {
  self->glGetHistogramParameterfv(target, pname, params);
}

//  void QOpenGLFunctions_1_3::glGetHistogram(GLenum target, GLboolean reset,
//      GLenum format, GLenum type, GLvoid *values)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_314glGetHistogramEjhjjPv(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    GLboolean reset,
    GLenum format,
    GLenum type,
    GLvoid *values) {
  self->glGetHistogram(target, reset, format, type, values);
}

//  void QOpenGLFunctions_1_3::glSeparableFilter2D(GLenum target, GLenum
//      internalformat, GLsizei width, GLsizei height, GLenum format, GLenum
//      type, const GLvoid *row, const GLvoid *column)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_319glSeparableFilter2DEjjiijjPKvS1_(
    QOpenGLFunctions_1_3 *self,
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

//  void QOpenGLFunctions_1_3::glGetSeparableFilter(GLenum target, GLenum
//      format, GLenum type, GLvoid *row, GLvoid *column, GLvoid *span)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_320glGetSeparableFilterEjjjPvS0_S0_(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    GLenum format,
    GLenum type,
    GLvoid *row,
    GLvoid *column,
    GLvoid *span) {
  self->glGetSeparableFilter(target, format, type, row, column, span);
}

//  void QOpenGLFunctions_1_3::glGetConvolutionParameteriv(GLenum target,
//      GLenum pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_327glGetConvolutionParameterivEjjPi(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    GLenum pname,
    GLint *params) {
  self->glGetConvolutionParameteriv(target, pname, params);
}

//  void QOpenGLFunctions_1_3::glGetConvolutionParameterfv(GLenum target,
//      GLenum pname, GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_327glGetConvolutionParameterfvEjjPf(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    GLenum pname,
    GLfloat *params) {
  self->glGetConvolutionParameterfv(target, pname, params);
}

//  void QOpenGLFunctions_1_3::glGetConvolutionFilter(GLenum target, GLenum
//      format, GLenum type, GLvoid *image)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_322glGetConvolutionFilterEjjjPv(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    GLenum format,
    GLenum type,
    GLvoid *image) {
  self->glGetConvolutionFilter(target, format, type, image);
}

//  void QOpenGLFunctions_1_3::glCopyConvolutionFilter2D(GLenum target,
//      GLenum internalformat, GLint x, GLint y, GLsizei width, GLsizei
//      height)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_325glCopyConvolutionFilter2DEjjiiii(
    QOpenGLFunctions_1_3 *self,
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

//  void QOpenGLFunctions_1_3::glCopyConvolutionFilter1D(GLenum target,
//      GLenum internalformat, GLint x, GLint y, GLsizei width)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_325glCopyConvolutionFilter1DEjjiii(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    GLenum internalformat,
    GLint x,
    GLint y,
    GLsizei width) {
  self->glCopyConvolutionFilter1D(target, internalformat, x, y, width);
}

//  void QOpenGLFunctions_1_3::glConvolutionParameteriv(GLenum target, GLenum
//      pname, const GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_324glConvolutionParameterivEjjPKi(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    GLenum pname,
    const GLint *params) {
  self->glConvolutionParameteriv(target, pname, params);
}

//  void QOpenGLFunctions_1_3::glConvolutionParameteri(GLenum target, GLenum
//      pname, GLint params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_323glConvolutionParameteriEjji(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    GLenum pname,
    GLint params) {
  self->glConvolutionParameteri(target, pname, params);
}

//  void QOpenGLFunctions_1_3::glConvolutionParameterfv(GLenum target, GLenum
//      pname, const GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_324glConvolutionParameterfvEjjPKf(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    GLenum pname,
    const GLfloat *params) {
  self->glConvolutionParameterfv(target, pname, params);
}

//  void QOpenGLFunctions_1_3::glConvolutionParameterf(GLenum target, GLenum
//      pname, GLfloat params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_323glConvolutionParameterfEjjf(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    GLenum pname,
    GLfloat params) {
  self->glConvolutionParameterf(target, pname, params);
}

//  void QOpenGLFunctions_1_3::glConvolutionFilter2D(GLenum target, GLenum
//      internalformat, GLsizei width, GLsizei height, GLenum format, GLenum
//      type, const GLvoid *image)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_321glConvolutionFilter2DEjjiijjPKv(
    QOpenGLFunctions_1_3 *self,
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

//  void QOpenGLFunctions_1_3::glConvolutionFilter1D(GLenum target, GLenum
//      internalformat, GLsizei width, GLenum format, GLenum type, const
//      GLvoid *image)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_321glConvolutionFilter1DEjjijjPKv(
    QOpenGLFunctions_1_3 *self,
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

//  void QOpenGLFunctions_1_3::glCopyColorSubTable(GLenum target, GLsizei
//      start, GLint x, GLint y, GLsizei width)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_319glCopyColorSubTableEjiiii(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    GLsizei start,
    GLint x,
    GLint y,
    GLsizei width) {
  self->glCopyColorSubTable(target, start, x, y, width);
}

//  void QOpenGLFunctions_1_3::glColorSubTable(GLenum target, GLsizei start,
//      GLsizei count, GLenum format, GLenum type, const GLvoid *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_315glColorSubTableEjiijjPKv(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    GLsizei start,
    GLsizei count,
    GLenum format,
    GLenum type,
    const GLvoid *data) {
  self->glColorSubTable(target, start, count, format, type, data);
}

//  void QOpenGLFunctions_1_3::glGetColorTableParameteriv(GLenum target,
//      GLenum pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_326glGetColorTableParameterivEjjPi(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    GLenum pname,
    GLint *params) {
  self->glGetColorTableParameteriv(target, pname, params);
}

//  void QOpenGLFunctions_1_3::glGetColorTableParameterfv(GLenum target,
//      GLenum pname, GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_326glGetColorTableParameterfvEjjPf(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    GLenum pname,
    GLfloat *params) {
  self->glGetColorTableParameterfv(target, pname, params);
}

//  void QOpenGLFunctions_1_3::glGetColorTable(GLenum target, GLenum format,
//      GLenum type, GLvoid *table)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_315glGetColorTableEjjjPv(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    GLenum format,
    GLenum type,
    GLvoid *table) {
  self->glGetColorTable(target, format, type, table);
}

//  void QOpenGLFunctions_1_3::glCopyColorTable(GLenum target, GLenum
//      internalformat, GLint x, GLint y, GLsizei width)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_316glCopyColorTableEjjiii(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    GLenum internalformat,
    GLint x,
    GLint y,
    GLsizei width) {
  self->glCopyColorTable(target, internalformat, x, y, width);
}

//  void QOpenGLFunctions_1_3::glColorTableParameteriv(GLenum target, GLenum
//      pname, const GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_323glColorTableParameterivEjjPKi(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    GLenum pname,
    const GLint *params) {
  self->glColorTableParameteriv(target, pname, params);
}

//  void QOpenGLFunctions_1_3::glColorTableParameterfv(GLenum target, GLenum
//      pname, const GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_323glColorTableParameterfvEjjPKf(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    GLenum pname,
    const GLfloat *params) {
  self->glColorTableParameterfv(target, pname, params);
}

//  void QOpenGLFunctions_1_3::glColorTable(GLenum target, GLenum
//      internalformat, GLsizei width, GLenum format, GLenum type, const
//      GLvoid *table)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_312glColorTableEjjijjPKv(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    GLenum internalformat,
    GLsizei width,
    GLenum format,
    GLenum type,
    const GLvoid *table) {
  self->glColorTable(target, internalformat, width, format, type, table);
}

//  void QOpenGLFunctions_1_3::glMultTransposeMatrixd(const GLdouble *m)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_322glMultTransposeMatrixdEPKd(
    QOpenGLFunctions_1_3 *self,
    const GLdouble *m) {
  self->glMultTransposeMatrixd(m);
}

//  void QOpenGLFunctions_1_3::glMultTransposeMatrixf(const GLfloat *m)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_322glMultTransposeMatrixfEPKf(
    QOpenGLFunctions_1_3 *self,
    const GLfloat *m) {
  self->glMultTransposeMatrixf(m);
}

//  void QOpenGLFunctions_1_3::glLoadTransposeMatrixd(const GLdouble *m)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_322glLoadTransposeMatrixdEPKd(
    QOpenGLFunctions_1_3 *self,
    const GLdouble *m) {
  self->glLoadTransposeMatrixd(m);
}

//  void QOpenGLFunctions_1_3::glLoadTransposeMatrixf(const GLfloat *m)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_322glLoadTransposeMatrixfEPKf(
    QOpenGLFunctions_1_3 *self,
    const GLfloat *m) {
  self->glLoadTransposeMatrixf(m);
}

//  void QOpenGLFunctions_1_3::glMultiTexCoord4sv(GLenum target, const
//      GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_318glMultiTexCoord4svEjPKs(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    const GLshort *v) {
  self->glMultiTexCoord4sv(target, v);
}

//  void QOpenGLFunctions_1_3::glMultiTexCoord4s(GLenum target, GLshort s,
//      GLshort t, GLshort r, GLshort q)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_317glMultiTexCoord4sEjssss(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    GLshort s,
    GLshort t,
    GLshort r,
    GLshort q) {
  self->glMultiTexCoord4s(target, s, t, r, q);
}

//  void QOpenGLFunctions_1_3::glMultiTexCoord4iv(GLenum target, const GLint
//      *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_318glMultiTexCoord4ivEjPKi(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    const GLint *v) {
  self->glMultiTexCoord4iv(target, v);
}

//  void QOpenGLFunctions_1_3::glMultiTexCoord4i(GLenum target, GLint s,
//      GLint t, GLint r, GLint q)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_317glMultiTexCoord4iEjiiii(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    GLint s,
    GLint t,
    GLint r,
    GLint q) {
  self->glMultiTexCoord4i(target, s, t, r, q);
}

//  void QOpenGLFunctions_1_3::glMultiTexCoord4fv(GLenum target, const
//      GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_318glMultiTexCoord4fvEjPKf(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    const GLfloat *v) {
  self->glMultiTexCoord4fv(target, v);
}

//  void QOpenGLFunctions_1_3::glMultiTexCoord4f(GLenum target, GLfloat s,
//      GLfloat t, GLfloat r, GLfloat q)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_317glMultiTexCoord4fEjffff(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    GLfloat s,
    GLfloat t,
    GLfloat r,
    GLfloat q) {
  self->glMultiTexCoord4f(target, s, t, r, q);
}

//  void QOpenGLFunctions_1_3::glMultiTexCoord4dv(GLenum target, const
//      GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_318glMultiTexCoord4dvEjPKd(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    const GLdouble *v) {
  self->glMultiTexCoord4dv(target, v);
}

//  void QOpenGLFunctions_1_3::glMultiTexCoord4d(GLenum target, GLdouble s,
//      GLdouble t, GLdouble r, GLdouble q)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_317glMultiTexCoord4dEjdddd(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    GLdouble s,
    GLdouble t,
    GLdouble r,
    GLdouble q) {
  self->glMultiTexCoord4d(target, s, t, r, q);
}

//  void QOpenGLFunctions_1_3::glMultiTexCoord3sv(GLenum target, const
//      GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_318glMultiTexCoord3svEjPKs(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    const GLshort *v) {
  self->glMultiTexCoord3sv(target, v);
}

//  void QOpenGLFunctions_1_3::glMultiTexCoord3s(GLenum target, GLshort s,
//      GLshort t, GLshort r)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_317glMultiTexCoord3sEjsss(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    GLshort s,
    GLshort t,
    GLshort r) {
  self->glMultiTexCoord3s(target, s, t, r);
}

//  void QOpenGLFunctions_1_3::glMultiTexCoord3iv(GLenum target, const GLint
//      *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_318glMultiTexCoord3ivEjPKi(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    const GLint *v) {
  self->glMultiTexCoord3iv(target, v);
}

//  void QOpenGLFunctions_1_3::glMultiTexCoord3i(GLenum target, GLint s,
//      GLint t, GLint r)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_317glMultiTexCoord3iEjiii(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    GLint s,
    GLint t,
    GLint r) {
  self->glMultiTexCoord3i(target, s, t, r);
}

//  void QOpenGLFunctions_1_3::glMultiTexCoord3fv(GLenum target, const
//      GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_318glMultiTexCoord3fvEjPKf(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    const GLfloat *v) {
  self->glMultiTexCoord3fv(target, v);
}

//  void QOpenGLFunctions_1_3::glMultiTexCoord3f(GLenum target, GLfloat s,
//      GLfloat t, GLfloat r)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_317glMultiTexCoord3fEjfff(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    GLfloat s,
    GLfloat t,
    GLfloat r) {
  self->glMultiTexCoord3f(target, s, t, r);
}

//  void QOpenGLFunctions_1_3::glMultiTexCoord3dv(GLenum target, const
//      GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_318glMultiTexCoord3dvEjPKd(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    const GLdouble *v) {
  self->glMultiTexCoord3dv(target, v);
}

//  void QOpenGLFunctions_1_3::glMultiTexCoord3d(GLenum target, GLdouble s,
//      GLdouble t, GLdouble r)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_317glMultiTexCoord3dEjddd(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    GLdouble s,
    GLdouble t,
    GLdouble r) {
  self->glMultiTexCoord3d(target, s, t, r);
}

//  void QOpenGLFunctions_1_3::glMultiTexCoord2sv(GLenum target, const
//      GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_318glMultiTexCoord2svEjPKs(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    const GLshort *v) {
  self->glMultiTexCoord2sv(target, v);
}

//  void QOpenGLFunctions_1_3::glMultiTexCoord2s(GLenum target, GLshort s,
//      GLshort t)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_317glMultiTexCoord2sEjss(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    GLshort s,
    GLshort t) {
  self->glMultiTexCoord2s(target, s, t);
}

//  void QOpenGLFunctions_1_3::glMultiTexCoord2iv(GLenum target, const GLint
//      *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_318glMultiTexCoord2ivEjPKi(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    const GLint *v) {
  self->glMultiTexCoord2iv(target, v);
}

//  void QOpenGLFunctions_1_3::glMultiTexCoord2i(GLenum target, GLint s,
//      GLint t)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_317glMultiTexCoord2iEjii(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    GLint s,
    GLint t) {
  self->glMultiTexCoord2i(target, s, t);
}

//  void QOpenGLFunctions_1_3::glMultiTexCoord2fv(GLenum target, const
//      GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_318glMultiTexCoord2fvEjPKf(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    const GLfloat *v) {
  self->glMultiTexCoord2fv(target, v);
}

//  void QOpenGLFunctions_1_3::glMultiTexCoord2f(GLenum target, GLfloat s,
//      GLfloat t)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_317glMultiTexCoord2fEjff(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    GLfloat s,
    GLfloat t) {
  self->glMultiTexCoord2f(target, s, t);
}

//  void QOpenGLFunctions_1_3::glMultiTexCoord2dv(GLenum target, const
//      GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_318glMultiTexCoord2dvEjPKd(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    const GLdouble *v) {
  self->glMultiTexCoord2dv(target, v);
}

//  void QOpenGLFunctions_1_3::glMultiTexCoord2d(GLenum target, GLdouble s,
//      GLdouble t)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_317glMultiTexCoord2dEjdd(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    GLdouble s,
    GLdouble t) {
  self->glMultiTexCoord2d(target, s, t);
}

//  void QOpenGLFunctions_1_3::glMultiTexCoord1sv(GLenum target, const
//      GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_318glMultiTexCoord1svEjPKs(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    const GLshort *v) {
  self->glMultiTexCoord1sv(target, v);
}

//  void QOpenGLFunctions_1_3::glMultiTexCoord1s(GLenum target, GLshort s)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_317glMultiTexCoord1sEjs(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    GLshort s) {
  self->glMultiTexCoord1s(target, s);
}

//  void QOpenGLFunctions_1_3::glMultiTexCoord1iv(GLenum target, const GLint
//      *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_318glMultiTexCoord1ivEjPKi(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    const GLint *v) {
  self->glMultiTexCoord1iv(target, v);
}

//  void QOpenGLFunctions_1_3::glMultiTexCoord1i(GLenum target, GLint s)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_317glMultiTexCoord1iEji(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    GLint s) {
  self->glMultiTexCoord1i(target, s);
}

//  void QOpenGLFunctions_1_3::glMultiTexCoord1fv(GLenum target, const
//      GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_318glMultiTexCoord1fvEjPKf(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    const GLfloat *v) {
  self->glMultiTexCoord1fv(target, v);
}

//  void QOpenGLFunctions_1_3::glMultiTexCoord1f(GLenum target, GLfloat s)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_317glMultiTexCoord1fEjf(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    GLfloat s) {
  self->glMultiTexCoord1f(target, s);
}

//  void QOpenGLFunctions_1_3::glMultiTexCoord1dv(GLenum target, const
//      GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_318glMultiTexCoord1dvEjPKd(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    const GLdouble *v) {
  self->glMultiTexCoord1dv(target, v);
}

//  void QOpenGLFunctions_1_3::glMultiTexCoord1d(GLenum target, GLdouble s)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_317glMultiTexCoord1dEjd(
    QOpenGLFunctions_1_3 *self,
    GLenum target,
    GLdouble s) {
  self->glMultiTexCoord1d(target, s);
}

//  void QOpenGLFunctions_1_3::glClientActiveTexture(GLenum texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_321glClientActiveTextureEj(
    QOpenGLFunctions_1_3 *self,
    GLenum texture) {
  self->glClientActiveTexture(texture);
}

//  bool QOpenGLFunctions_1_3::isContextCompatible(QOpenGLContext *context)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QOpenGLFunctions_1_319isContextCompatibleEP14QOpenGLContext(
    QOpenGLContext *context) {
  return QOpenGLFunctions_1_3::isContextCompatible(context);
}

//  QOpenGLVersionProfile QOpenGLFunctions_1_3::versionProfile()
extern "C" Q_DECL_EXPORT
QOpenGLVersionProfile *ritual_ZN20QOpenGLFunctions_1_314versionProfileEv() {
  return new QOpenGLVersionProfile(QOpenGLFunctions_1_3::versionProfile());
}

//  a Python function taken by a CuteQOpenGLFunctions_1_3, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QOpenGLFunctions_1_3(
    QOpenGLFunctions_1_3 *self,
    const char *key,
    void *call) {
  return static_cast<CuteQOpenGLFunctions_1_3 *>(self)->take(key, call);
}

//  bool QOpenGLFunctions_1_3::initializeOpenGLFunctions()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN20QOpenGLFunctions_1_325initializeOpenGLFunctionsEv(
    QOpenGLFunctions_1_3 *self) {
  return self->QOpenGLFunctions_1_3::initializeOpenGLFunctions();
}

#endif  // !defined(QT_NO_OPENGL) && !QT_CONFIG(opengles2)
#endif  // !QT_CONFIG(opengles2)
