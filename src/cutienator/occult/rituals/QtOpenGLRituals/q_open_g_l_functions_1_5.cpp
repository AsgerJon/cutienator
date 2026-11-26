//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/qopenglfunctions_1_5.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtOpenGL/qtopenglglobal.h>
#if !QT_CONFIG(opengles2)
#if !defined(QT_NO_OPENGL) && !QT_CONFIG(opengles2)
#include <QtOpenGL/QtOpenGL>
#include <QtOpenGL/qopenglfunctions_1_5.h>
#include <QtOpenGL/qopenglversionprofile.h>
#include <cstring>

//  A QOpenGLFunctions_1_5 that Python can take functions over in. Every QOpenGLFunctions_1_5
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL) && !QT_CONFIG(opengles2)
typedef bool (*CuteQOpenGLFunctions_1_5Call0)(const void *, int *);
#endif  // !defined(QT_NO_OPENGL) && !QT_CONFIG(opengles2)
#endif  // !defined(QT_NO_OPENGL)
class CuteQOpenGLFunctions_1_5 : public QOpenGLFunctions_1_5 {
public:
  using QOpenGLFunctions_1_5::QOpenGLFunctions_1_5;
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
  //  bool QOpenGLFunctions_1_5::initializeOpenGLFunctions()
  bool initializeOpenGLFunctions() override {
    if (taken[0]) {
      int handled = 0;
      CuteQOpenGLFunctions_1_5Call0 call = reinterpret_cast<CuteQOpenGLFunctions_1_5Call0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QOpenGLFunctions_1_5::initializeOpenGLFunctions();
  }
#endif  // !defined(QT_NO_OPENGL) && !QT_CONFIG(opengles2)
#endif  // !defined(QT_NO_OPENGL)
};

//  QOpenGLFunctions_1_5::QOpenGLFunctions_1_5()
extern "C" Q_DECL_EXPORT
QOpenGLFunctions_1_5 *ritual_ZN20QOpenGLFunctions_1_5C1Ev() {
  return new CuteQOpenGLFunctions_1_5();
}

//  QOpenGLFunctions_1_5::~QOpenGLFunctions_1_5()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_5D1Ev(QOpenGLFunctions_1_5 *self) {
  delete self;
}

//  bool QOpenGLFunctions_1_5::initializeOpenGLFunctions()
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QOpenGLFunctions_1_525initializeOpenGLFunctionsEv(
    QOpenGLFunctions_1_5 *self) {
  return self->initializeOpenGLFunctions();
}

//  void QOpenGLFunctions_1_5::glViewport(GLint x, GLint y, GLsizei width,
//      GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_510glViewportEiiii(
    QOpenGLFunctions_1_5 *self,
    GLint x,
    GLint y,
    GLsizei width,
    GLsizei height) {
  self->glViewport(x, y, width, height);
}

//  void QOpenGLFunctions_1_5::glDepthRange(GLdouble nearVal, GLdouble
//      farVal)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_512glDepthRangeEdd(
    QOpenGLFunctions_1_5 *self,
    GLdouble nearVal,
    GLdouble farVal) {
  self->glDepthRange(nearVal, farVal);
}

//  GLboolean QOpenGLFunctions_1_5::glIsEnabled(GLenum cap)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN20QOpenGLFunctions_1_511glIsEnabledEj(
    QOpenGLFunctions_1_5 *self,
    GLenum cap) {
  return self->glIsEnabled(cap);
}

//  void QOpenGLFunctions_1_5::glGetTexLevelParameteriv(GLenum target, GLint
//      level, GLenum pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_524glGetTexLevelParameterivEjijPi(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLint level,
    GLenum pname,
    GLint *params) {
  self->glGetTexLevelParameteriv(target, level, pname, params);
}

//  void QOpenGLFunctions_1_5::glGetTexLevelParameterfv(GLenum target, GLint
//      level, GLenum pname, GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_524glGetTexLevelParameterfvEjijPf(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLint level,
    GLenum pname,
    GLfloat *params) {
  self->glGetTexLevelParameterfv(target, level, pname, params);
}

//  void QOpenGLFunctions_1_5::glGetTexParameteriv(GLenum target, GLenum
//      pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_519glGetTexParameterivEjjPi(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLenum pname,
    GLint *params) {
  self->glGetTexParameteriv(target, pname, params);
}

//  void QOpenGLFunctions_1_5::glGetTexParameterfv(GLenum target, GLenum
//      pname, GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_519glGetTexParameterfvEjjPf(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLenum pname,
    GLfloat *params) {
  self->glGetTexParameterfv(target, pname, params);
}

//  void QOpenGLFunctions_1_5::glGetTexImage(GLenum target, GLint level,
//      GLenum format, GLenum type, GLvoid *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glGetTexImageEjijjPv(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLint level,
    GLenum format,
    GLenum type,
    GLvoid *pixels) {
  self->glGetTexImage(target, level, format, type, pixels);
}

//  const GLubyte *QOpenGLFunctions_1_5::glGetString(GLenum name)
extern "C" Q_DECL_EXPORT
const GLubyte *ritual_ZN20QOpenGLFunctions_1_511glGetStringEj(
    QOpenGLFunctions_1_5 *self,
    GLenum name) {
  return self->glGetString(name);
}

//  void QOpenGLFunctions_1_5::glGetIntegerv(GLenum pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glGetIntegervEjPi(
    QOpenGLFunctions_1_5 *self,
    GLenum pname,
    GLint *params) {
  self->glGetIntegerv(pname, params);
}

//  void QOpenGLFunctions_1_5::glGetFloatv(GLenum pname, GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_511glGetFloatvEjPf(
    QOpenGLFunctions_1_5 *self,
    GLenum pname,
    GLfloat *params) {
  self->glGetFloatv(pname, params);
}

//  GLenum QOpenGLFunctions_1_5::glGetError()
extern "C" Q_DECL_EXPORT
GLenum ritual_ZN20QOpenGLFunctions_1_510glGetErrorEv(
    QOpenGLFunctions_1_5 *self) {
  return self->glGetError();
}

//  void QOpenGLFunctions_1_5::glGetDoublev(GLenum pname, GLdouble *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_512glGetDoublevEjPd(
    QOpenGLFunctions_1_5 *self,
    GLenum pname,
    GLdouble *params) {
  self->glGetDoublev(pname, params);
}

//  void QOpenGLFunctions_1_5::glGetBooleanv(GLenum pname, GLboolean *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glGetBooleanvEjPh(
    QOpenGLFunctions_1_5 *self,
    GLenum pname,
    GLboolean *params) {
  self->glGetBooleanv(pname, params);
}

//  void QOpenGLFunctions_1_5::glReadPixels(GLint x, GLint y, GLsizei width,
//      GLsizei height, GLenum format, GLenum type, GLvoid *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_512glReadPixelsEiiiijjPv(
    QOpenGLFunctions_1_5 *self,
    GLint x,
    GLint y,
    GLsizei width,
    GLsizei height,
    GLenum format,
    GLenum type,
    GLvoid *pixels) {
  self->glReadPixels(x, y, width, height, format, type, pixels);
}

//  void QOpenGLFunctions_1_5::glReadBuffer(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_512glReadBufferEj(
    QOpenGLFunctions_1_5 *self,
    GLenum mode) {
  self->glReadBuffer(mode);
}

//  void QOpenGLFunctions_1_5::glPixelStorei(GLenum pname, GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glPixelStoreiEji(
    QOpenGLFunctions_1_5 *self,
    GLenum pname,
    GLint param) {
  self->glPixelStorei(pname, param);
}

//  void QOpenGLFunctions_1_5::glPixelStoref(GLenum pname, GLfloat param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glPixelStorefEjf(
    QOpenGLFunctions_1_5 *self,
    GLenum pname,
    GLfloat param) {
  self->glPixelStoref(pname, param);
}

//  void QOpenGLFunctions_1_5::glDepthFunc(GLenum func)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_511glDepthFuncEj(
    QOpenGLFunctions_1_5 *self,
    GLenum func) {
  self->glDepthFunc(func);
}

//  void QOpenGLFunctions_1_5::glStencilOp(GLenum fail, GLenum zfail, GLenum
//      zpass)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_511glStencilOpEjjj(
    QOpenGLFunctions_1_5 *self,
    GLenum fail,
    GLenum zfail,
    GLenum zpass) {
  self->glStencilOp(fail, zfail, zpass);
}

//  void QOpenGLFunctions_1_5::glStencilFunc(GLenum func, GLint ref, GLuint
//      mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glStencilFuncEjij(
    QOpenGLFunctions_1_5 *self,
    GLenum func,
    GLint ref,
    GLuint mask) {
  self->glStencilFunc(func, ref, mask);
}

//  void QOpenGLFunctions_1_5::glLogicOp(GLenum opcode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_59glLogicOpEj(
    QOpenGLFunctions_1_5 *self,
    GLenum opcode) {
  self->glLogicOp(opcode);
}

//  void QOpenGLFunctions_1_5::glBlendFunc(GLenum sfactor, GLenum dfactor)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_511glBlendFuncEjj(
    QOpenGLFunctions_1_5 *self,
    GLenum sfactor,
    GLenum dfactor) {
  self->glBlendFunc(sfactor, dfactor);
}

//  void QOpenGLFunctions_1_5::glFlush()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_57glFlushEv(QOpenGLFunctions_1_5 *self) {
  self->glFlush();
}

//  void QOpenGLFunctions_1_5::glFinish()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_58glFinishEv(QOpenGLFunctions_1_5 *self) {
  self->glFinish();
}

//  void QOpenGLFunctions_1_5::glEnable(GLenum cap)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_58glEnableEj(
    QOpenGLFunctions_1_5 *self,
    GLenum cap) {
  self->glEnable(cap);
}

//  void QOpenGLFunctions_1_5::glDisable(GLenum cap)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_59glDisableEj(
    QOpenGLFunctions_1_5 *self,
    GLenum cap) {
  self->glDisable(cap);
}

//  void QOpenGLFunctions_1_5::glDepthMask(GLboolean flag)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_511glDepthMaskEh(
    QOpenGLFunctions_1_5 *self,
    GLboolean flag) {
  self->glDepthMask(flag);
}

//  void QOpenGLFunctions_1_5::glColorMask(GLboolean red, GLboolean green,
//      GLboolean blue, GLboolean alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_511glColorMaskEhhhh(
    QOpenGLFunctions_1_5 *self,
    GLboolean red,
    GLboolean green,
    GLboolean blue,
    GLboolean alpha) {
  self->glColorMask(red, green, blue, alpha);
}

//  void QOpenGLFunctions_1_5::glStencilMask(GLuint mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glStencilMaskEj(
    QOpenGLFunctions_1_5 *self,
    GLuint mask) {
  self->glStencilMask(mask);
}

//  void QOpenGLFunctions_1_5::glClearDepth(GLdouble depth)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_512glClearDepthEd(
    QOpenGLFunctions_1_5 *self,
    GLdouble depth) {
  self->glClearDepth(depth);
}

//  void QOpenGLFunctions_1_5::glClearStencil(GLint s)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_514glClearStencilEi(
    QOpenGLFunctions_1_5 *self,
    GLint s) {
  self->glClearStencil(s);
}

//  void QOpenGLFunctions_1_5::glClearColor(GLfloat red, GLfloat green,
//      GLfloat blue, GLfloat alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_512glClearColorEffff(
    QOpenGLFunctions_1_5 *self,
    GLfloat red,
    GLfloat green,
    GLfloat blue,
    GLfloat alpha) {
  self->glClearColor(red, green, blue, alpha);
}

//  void QOpenGLFunctions_1_5::glClear(GLbitfield mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_57glClearEj(
    QOpenGLFunctions_1_5 *self,
    GLbitfield mask) {
  self->glClear(mask);
}

//  void QOpenGLFunctions_1_5::glDrawBuffer(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_512glDrawBufferEj(
    QOpenGLFunctions_1_5 *self,
    GLenum mode) {
  self->glDrawBuffer(mode);
}

//  void QOpenGLFunctions_1_5::glTexImage2D(GLenum target, GLint level, GLint
//      internalformat, GLsizei width, GLsizei height, GLint border, GLenum
//      format, GLenum type, const GLvoid *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_512glTexImage2DEjiiiiijjPKv(
    QOpenGLFunctions_1_5 *self,
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

//  void QOpenGLFunctions_1_5::glTexImage1D(GLenum target, GLint level, GLint
//      internalformat, GLsizei width, GLint border, GLenum format, GLenum
//      type, const GLvoid *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_512glTexImage1DEjiiiijjPKv(
    QOpenGLFunctions_1_5 *self,
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

//  void QOpenGLFunctions_1_5::glTexParameteriv(GLenum target, GLenum pname,
//      const GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_516glTexParameterivEjjPKi(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLenum pname,
    const GLint *params) {
  self->glTexParameteriv(target, pname, params);
}

//  void QOpenGLFunctions_1_5::glTexParameteri(GLenum target, GLenum pname,
//      GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_515glTexParameteriEjji(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLenum pname,
    GLint param) {
  self->glTexParameteri(target, pname, param);
}

//  void QOpenGLFunctions_1_5::glTexParameterfv(GLenum target, GLenum pname,
//      const GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_516glTexParameterfvEjjPKf(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLenum pname,
    const GLfloat *params) {
  self->glTexParameterfv(target, pname, params);
}

//  void QOpenGLFunctions_1_5::glTexParameterf(GLenum target, GLenum pname,
//      GLfloat param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_515glTexParameterfEjjf(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLenum pname,
    GLfloat param) {
  self->glTexParameterf(target, pname, param);
}

//  void QOpenGLFunctions_1_5::glScissor(GLint x, GLint y, GLsizei width,
//      GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_59glScissorEiiii(
    QOpenGLFunctions_1_5 *self,
    GLint x,
    GLint y,
    GLsizei width,
    GLsizei height) {
  self->glScissor(x, y, width, height);
}

//  void QOpenGLFunctions_1_5::glPolygonMode(GLenum face, GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glPolygonModeEjj(
    QOpenGLFunctions_1_5 *self,
    GLenum face,
    GLenum mode) {
  self->glPolygonMode(face, mode);
}

//  void QOpenGLFunctions_1_5::glPointSize(GLfloat size)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_511glPointSizeEf(
    QOpenGLFunctions_1_5 *self,
    GLfloat size) {
  self->glPointSize(size);
}

//  void QOpenGLFunctions_1_5::glLineWidth(GLfloat width)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_511glLineWidthEf(
    QOpenGLFunctions_1_5 *self,
    GLfloat width) {
  self->glLineWidth(width);
}

//  void QOpenGLFunctions_1_5::glHint(GLenum target, GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_56glHintEjj(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLenum mode) {
  self->glHint(target, mode);
}

//  void QOpenGLFunctions_1_5::glFrontFace(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_511glFrontFaceEj(
    QOpenGLFunctions_1_5 *self,
    GLenum mode) {
  self->glFrontFace(mode);
}

//  void QOpenGLFunctions_1_5::glCullFace(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_510glCullFaceEj(
    QOpenGLFunctions_1_5 *self,
    GLenum mode) {
  self->glCullFace(mode);
}

//  void QOpenGLFunctions_1_5::glIndexubv(const GLubyte *c)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_510glIndexubvEPKh(
    QOpenGLFunctions_1_5 *self,
    const GLubyte *c) {
  self->glIndexubv(c);
}

//  void QOpenGLFunctions_1_5::glIndexub(GLubyte c)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_59glIndexubEh(
    QOpenGLFunctions_1_5 *self,
    GLubyte c) {
  self->glIndexub(c);
}

//  GLboolean QOpenGLFunctions_1_5::glIsTexture(GLuint texture)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN20QOpenGLFunctions_1_511glIsTextureEj(
    QOpenGLFunctions_1_5 *self,
    GLuint texture) {
  return self->glIsTexture(texture);
}

//  void QOpenGLFunctions_1_5::glGenTextures(GLsizei n, GLuint *textures)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glGenTexturesEiPj(
    QOpenGLFunctions_1_5 *self,
    GLsizei n,
    GLuint *textures) {
  self->glGenTextures(n, textures);
}

//  void QOpenGLFunctions_1_5::glDeleteTextures(GLsizei n, const GLuint
//      *textures)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_516glDeleteTexturesEiPKj(
    QOpenGLFunctions_1_5 *self,
    GLsizei n,
    const GLuint *textures) {
  self->glDeleteTextures(n, textures);
}

//  void QOpenGLFunctions_1_5::glBindTexture(GLenum target, GLuint texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glBindTextureEjj(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLuint texture) {
  self->glBindTexture(target, texture);
}

//  void QOpenGLFunctions_1_5::glTexSubImage2D(GLenum target, GLint level,
//      GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum
//      format, GLenum type, const GLvoid *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_515glTexSubImage2DEjiiiiijjPKv(
    QOpenGLFunctions_1_5 *self,
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

//  void QOpenGLFunctions_1_5::glTexSubImage1D(GLenum target, GLint level,
//      GLint xoffset, GLsizei width, GLenum format, GLenum type, const
//      GLvoid *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_515glTexSubImage1DEjiiijjPKv(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLint level,
    GLint xoffset,
    GLsizei width,
    GLenum format,
    GLenum type,
    const GLvoid *pixels) {
  self->glTexSubImage1D(target, level, xoffset, width, format, type, pixels);
}

//  void QOpenGLFunctions_1_5::glCopyTexSubImage2D(GLenum target, GLint
//      level, GLint xoffset, GLint yoffset, GLint x, GLint y, GLsizei width,
//      GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_519glCopyTexSubImage2DEjiiiiiii(
    QOpenGLFunctions_1_5 *self,
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

//  void QOpenGLFunctions_1_5::glCopyTexSubImage1D(GLenum target, GLint
//      level, GLint xoffset, GLint x, GLint y, GLsizei width)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_519glCopyTexSubImage1DEjiiiii(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLint level,
    GLint xoffset,
    GLint x,
    GLint y,
    GLsizei width) {
  self->glCopyTexSubImage1D(target, level, xoffset, x, y, width);
}

//  void QOpenGLFunctions_1_5::glCopyTexImage2D(GLenum target, GLint level,
//      GLenum internalformat, GLint x, GLint y, GLsizei width, GLsizei
//      height, GLint border)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_516glCopyTexImage2DEjijiiiii(
    QOpenGLFunctions_1_5 *self,
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

//  void QOpenGLFunctions_1_5::glCopyTexImage1D(GLenum target, GLint level,
//      GLenum internalformat, GLint x, GLint y, GLsizei width, GLint border)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_516glCopyTexImage1DEjijiiii(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLint level,
    GLenum internalformat,
    GLint x,
    GLint y,
    GLsizei width,
    GLint border) {
  self->glCopyTexImage1D(target, level, internalformat, x, y, width, border);
}

//  void QOpenGLFunctions_1_5::glPolygonOffset(GLfloat factor, GLfloat units)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_515glPolygonOffsetEff(
    QOpenGLFunctions_1_5 *self,
    GLfloat factor,
    GLfloat units) {
  self->glPolygonOffset(factor, units);
}

//  void QOpenGLFunctions_1_5::glGetPointerv(GLenum pname, GLvoid **params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glGetPointervEjPPv(
    QOpenGLFunctions_1_5 *self,
    GLenum pname,
    GLvoid **params) {
  self->glGetPointerv(pname, params);
}

//  void QOpenGLFunctions_1_5::glDrawElements(GLenum mode, GLsizei count,
//      GLenum type, const GLvoid *indices)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_514glDrawElementsEjijPKv(
    QOpenGLFunctions_1_5 *self,
    GLenum mode,
    GLsizei count,
    GLenum type,
    const GLvoid *indices) {
  self->glDrawElements(mode, count, type, indices);
}

//  void QOpenGLFunctions_1_5::glDrawArrays(GLenum mode, GLint first, GLsizei
//      count)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_512glDrawArraysEjii(
    QOpenGLFunctions_1_5 *self,
    GLenum mode,
    GLint first,
    GLsizei count) {
  self->glDrawArrays(mode, first, count);
}

//  void QOpenGLFunctions_1_5::glCopyTexSubImage3D(GLenum target, GLint
//      level, GLint xoffset, GLint yoffset, GLint zoffset, GLint x, GLint y,
//      GLsizei width, GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_519glCopyTexSubImage3DEjiiiiiiii(
    QOpenGLFunctions_1_5 *self,
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

//  void QOpenGLFunctions_1_5::glTexSubImage3D(GLenum target, GLint level,
//      GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei
//      height, GLsizei depth, GLenum format, GLenum type, const GLvoid
//      *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_515glTexSubImage3DEjiiiiiiijjPKv(
    QOpenGLFunctions_1_5 *self,
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

//  void QOpenGLFunctions_1_5::glTexImage3D(GLenum target, GLint level, GLint
//      internalformat, GLsizei width, GLsizei height, GLsizei depth, GLint
//      border, GLenum format, GLenum type, const GLvoid *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_512glTexImage3DEjiiiiiijjPKv(
    QOpenGLFunctions_1_5 *self,
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

//  void QOpenGLFunctions_1_5::glDrawRangeElements(GLenum mode, GLuint start,
//      GLuint end, GLsizei count, GLenum type, const GLvoid *indices)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_519glDrawRangeElementsEjjjijPKv(
    QOpenGLFunctions_1_5 *self,
    GLenum mode,
    GLuint start,
    GLuint end,
    GLsizei count,
    GLenum type,
    const GLvoid *indices) {
  self->glDrawRangeElements(mode, start, end, count, type, indices);
}

//  void QOpenGLFunctions_1_5::glBlendEquation(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_515glBlendEquationEj(
    QOpenGLFunctions_1_5 *self,
    GLenum mode) {
  self->glBlendEquation(mode);
}

//  void QOpenGLFunctions_1_5::glBlendColor(GLfloat red, GLfloat green,
//      GLfloat blue, GLfloat alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_512glBlendColorEffff(
    QOpenGLFunctions_1_5 *self,
    GLfloat red,
    GLfloat green,
    GLfloat blue,
    GLfloat alpha) {
  self->glBlendColor(red, green, blue, alpha);
}

//  void QOpenGLFunctions_1_5::glGetCompressedTexImage(GLenum target, GLint
//      level, GLvoid *img)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_523glGetCompressedTexImageEjiPv(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLint level,
    GLvoid *img) {
  self->glGetCompressedTexImage(target, level, img);
}

//  void QOpenGLFunctions_1_5::glCompressedTexSubImage1D(GLenum target, GLint
//      level, GLint xoffset, GLsizei width, GLenum format, GLsizei
//      imageSize, const GLvoid *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_525glCompressedTexSubImage1DEjiiijiPKv(
    QOpenGLFunctions_1_5 *self,
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

//  void QOpenGLFunctions_1_5::glCompressedTexSubImage2D(GLenum target, GLint
//      level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height,
//      GLenum format, GLsizei imageSize, const GLvoid *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_525glCompressedTexSubImage2DEjiiiiijiPKv(
    QOpenGLFunctions_1_5 *self,
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

//  void QOpenGLFunctions_1_5::glCompressedTexSubImage3D(GLenum target, GLint
//      level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width,
//      GLsizei height, GLsizei depth, GLenum format, GLsizei imageSize,
//      const GLvoid *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_525glCompressedTexSubImage3DEjiiiiiiijiPKv(
    QOpenGLFunctions_1_5 *self,
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

//  void QOpenGLFunctions_1_5::glCompressedTexImage1D(GLenum target, GLint
//      level, GLenum internalformat, GLsizei width, GLint border, GLsizei
//      imageSize, const GLvoid *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_522glCompressedTexImage1DEjijiiiPKv(
    QOpenGLFunctions_1_5 *self,
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

//  void QOpenGLFunctions_1_5::glCompressedTexImage2D(GLenum target, GLint
//      level, GLenum internalformat, GLsizei width, GLsizei height, GLint
//      border, GLsizei imageSize, const GLvoid *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_522glCompressedTexImage2DEjijiiiiPKv(
    QOpenGLFunctions_1_5 *self,
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

//  void QOpenGLFunctions_1_5::glCompressedTexImage3D(GLenum target, GLint
//      level, GLenum internalformat, GLsizei width, GLsizei height, GLsizei
//      depth, GLint border, GLsizei imageSize, const GLvoid *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_522glCompressedTexImage3DEjijiiiiiPKv(
    QOpenGLFunctions_1_5 *self,
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

//  void QOpenGLFunctions_1_5::glSampleCoverage(GLfloat value, GLboolean
//      invert)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_516glSampleCoverageEfh(
    QOpenGLFunctions_1_5 *self,
    GLfloat value,
    GLboolean invert) {
  self->glSampleCoverage(value, invert);
}

//  void QOpenGLFunctions_1_5::glActiveTexture(GLenum texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_515glActiveTextureEj(
    QOpenGLFunctions_1_5 *self,
    GLenum texture) {
  self->glActiveTexture(texture);
}

//  void QOpenGLFunctions_1_5::glPointParameteriv(GLenum pname, const GLint
//      *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_518glPointParameterivEjPKi(
    QOpenGLFunctions_1_5 *self,
    GLenum pname,
    const GLint *params) {
  self->glPointParameteriv(pname, params);
}

//  void QOpenGLFunctions_1_5::glPointParameteri(GLenum pname, GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_517glPointParameteriEji(
    QOpenGLFunctions_1_5 *self,
    GLenum pname,
    GLint param) {
  self->glPointParameteri(pname, param);
}

//  void QOpenGLFunctions_1_5::glPointParameterfv(GLenum pname, const GLfloat
//      *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_518glPointParameterfvEjPKf(
    QOpenGLFunctions_1_5 *self,
    GLenum pname,
    const GLfloat *params) {
  self->glPointParameterfv(pname, params);
}

//  void QOpenGLFunctions_1_5::glPointParameterf(GLenum pname, GLfloat param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_517glPointParameterfEjf(
    QOpenGLFunctions_1_5 *self,
    GLenum pname,
    GLfloat param) {
  self->glPointParameterf(pname, param);
}

//  void QOpenGLFunctions_1_5::glMultiDrawElements(GLenum mode, const GLsizei
//      *count, GLenum type, const GLvoid *const *indices, GLsizei drawcount)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_519glMultiDrawElementsEjPKijPKPKvi(
    QOpenGLFunctions_1_5 *self,
    GLenum mode,
    const GLsizei *count,
    GLenum type,
    const GLvoid *const *indices,
    GLsizei drawcount) {
  self->glMultiDrawElements(mode, count, type, indices, drawcount);
}

//  void QOpenGLFunctions_1_5::glMultiDrawArrays(GLenum mode, const GLint
//      *first, const GLsizei *count, GLsizei drawcount)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_517glMultiDrawArraysEjPKiS1_i(
    QOpenGLFunctions_1_5 *self,
    GLenum mode,
    const GLint *first,
    const GLsizei *count,
    GLsizei drawcount) {
  self->glMultiDrawArrays(mode, first, count, drawcount);
}

//  void QOpenGLFunctions_1_5::glBlendFuncSeparate(GLenum sfactorRGB, GLenum
//      dfactorRGB, GLenum sfactorAlpha, GLenum dfactorAlpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_519glBlendFuncSeparateEjjjj(
    QOpenGLFunctions_1_5 *self,
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

//  void QOpenGLFunctions_1_5::glGetBufferPointerv(GLenum target, GLenum
//      pname, GLvoid **params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_519glGetBufferPointervEjjPPv(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLenum pname,
    GLvoid **params) {
  self->glGetBufferPointerv(target, pname, params);
}

//  void QOpenGLFunctions_1_5::glGetBufferParameteriv(GLenum target, GLenum
//      pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_522glGetBufferParameterivEjjPi(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLenum pname,
    GLint *params) {
  self->glGetBufferParameteriv(target, pname, params);
}

//  GLboolean QOpenGLFunctions_1_5::glUnmapBuffer(GLenum target)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN20QOpenGLFunctions_1_513glUnmapBufferEj(
    QOpenGLFunctions_1_5 *self,
    GLenum target) {
  return self->glUnmapBuffer(target);
}

//  GLvoid *QOpenGLFunctions_1_5::glMapBuffer(GLenum target, GLenum access)
extern "C" Q_DECL_EXPORT
GLvoid *ritual_ZN20QOpenGLFunctions_1_511glMapBufferEjj(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLenum access) {
  return self->glMapBuffer(target, access);
}

//  void QOpenGLFunctions_1_5::glGetBufferSubData(GLenum target, GLintptr
//      offset, GLsizeiptr size, GLvoid *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_518glGetBufferSubDataEjllPv(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    long long offset,
    long long size,
    GLvoid *data) {
  self->glGetBufferSubData(target, offset, size, data);
}

//  void QOpenGLFunctions_1_5::glBufferSubData(GLenum target, GLintptr
//      offset, GLsizeiptr size, const GLvoid *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_515glBufferSubDataEjllPKv(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    long long offset,
    long long size,
    const GLvoid *data) {
  self->glBufferSubData(target, offset, size, data);
}

//  void QOpenGLFunctions_1_5::glBufferData(GLenum target, GLsizeiptr size,
//      const GLvoid *data, GLenum usage)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_512glBufferDataEjlPKvj(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    long long size,
    const GLvoid *data,
    GLenum usage) {
  self->glBufferData(target, size, data, usage);
}

//  GLboolean QOpenGLFunctions_1_5::glIsBuffer(GLuint buffer)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN20QOpenGLFunctions_1_510glIsBufferEj(
    QOpenGLFunctions_1_5 *self,
    GLuint buffer) {
  return self->glIsBuffer(buffer);
}

//  void QOpenGLFunctions_1_5::glGenBuffers(GLsizei n, GLuint *buffers)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_512glGenBuffersEiPj(
    QOpenGLFunctions_1_5 *self,
    GLsizei n,
    GLuint *buffers) {
  self->glGenBuffers(n, buffers);
}

//  void QOpenGLFunctions_1_5::glDeleteBuffers(GLsizei n, const GLuint
//      *buffers)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_515glDeleteBuffersEiPKj(
    QOpenGLFunctions_1_5 *self,
    GLsizei n,
    const GLuint *buffers) {
  self->glDeleteBuffers(n, buffers);
}

//  void QOpenGLFunctions_1_5::glBindBuffer(GLenum target, GLuint buffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_512glBindBufferEjj(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLuint buffer) {
  self->glBindBuffer(target, buffer);
}

//  void QOpenGLFunctions_1_5::glGetQueryObjectuiv(GLuint id, GLenum pname,
//      GLuint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_519glGetQueryObjectuivEjjPj(
    QOpenGLFunctions_1_5 *self,
    GLuint id,
    GLenum pname,
    GLuint *params) {
  self->glGetQueryObjectuiv(id, pname, params);
}

//  void QOpenGLFunctions_1_5::glGetQueryObjectiv(GLuint id, GLenum pname,
//      GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_518glGetQueryObjectivEjjPi(
    QOpenGLFunctions_1_5 *self,
    GLuint id,
    GLenum pname,
    GLint *params) {
  self->glGetQueryObjectiv(id, pname, params);
}

//  void QOpenGLFunctions_1_5::glGetQueryiv(GLenum target, GLenum pname,
//      GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_512glGetQueryivEjjPi(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLenum pname,
    GLint *params) {
  self->glGetQueryiv(target, pname, params);
}

//  void QOpenGLFunctions_1_5::glEndQuery(GLenum target)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_510glEndQueryEj(
    QOpenGLFunctions_1_5 *self,
    GLenum target) {
  self->glEndQuery(target);
}

//  void QOpenGLFunctions_1_5::glBeginQuery(GLenum target, GLuint id)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_512glBeginQueryEjj(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLuint id) {
  self->glBeginQuery(target, id);
}

//  GLboolean QOpenGLFunctions_1_5::glIsQuery(GLuint id)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN20QOpenGLFunctions_1_59glIsQueryEj(
    QOpenGLFunctions_1_5 *self,
    GLuint id) {
  return self->glIsQuery(id);
}

//  void QOpenGLFunctions_1_5::glDeleteQueries(GLsizei n, const GLuint *ids)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_515glDeleteQueriesEiPKj(
    QOpenGLFunctions_1_5 *self,
    GLsizei n,
    const GLuint *ids) {
  self->glDeleteQueries(n, ids);
}

//  void QOpenGLFunctions_1_5::glGenQueries(GLsizei n, GLuint *ids)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_512glGenQueriesEiPj(
    QOpenGLFunctions_1_5 *self,
    GLsizei n,
    GLuint *ids) {
  self->glGenQueries(n, ids);
}

//  void QOpenGLFunctions_1_5::glTranslatef(GLfloat x, GLfloat y, GLfloat z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_512glTranslatefEfff(
    QOpenGLFunctions_1_5 *self,
    GLfloat x,
    GLfloat y,
    GLfloat z) {
  self->glTranslatef(x, y, z);
}

//  void QOpenGLFunctions_1_5::glTranslated(GLdouble x, GLdouble y, GLdouble
//      z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_512glTranslatedEddd(
    QOpenGLFunctions_1_5 *self,
    GLdouble x,
    GLdouble y,
    GLdouble z) {
  self->glTranslated(x, y, z);
}

//  void QOpenGLFunctions_1_5::glScalef(GLfloat x, GLfloat y, GLfloat z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_58glScalefEfff(
    QOpenGLFunctions_1_5 *self,
    GLfloat x,
    GLfloat y,
    GLfloat z) {
  self->glScalef(x, y, z);
}

//  void QOpenGLFunctions_1_5::glScaled(GLdouble x, GLdouble y, GLdouble z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_58glScaledEddd(
    QOpenGLFunctions_1_5 *self,
    GLdouble x,
    GLdouble y,
    GLdouble z) {
  self->glScaled(x, y, z);
}

//  void QOpenGLFunctions_1_5::glRotatef(GLfloat angle, GLfloat x, GLfloat y,
//      GLfloat z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_59glRotatefEffff(
    QOpenGLFunctions_1_5 *self,
    GLfloat angle,
    GLfloat x,
    GLfloat y,
    GLfloat z) {
  self->glRotatef(angle, x, y, z);
}

//  void QOpenGLFunctions_1_5::glRotated(GLdouble angle, GLdouble x, GLdouble
//      y, GLdouble z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_59glRotatedEdddd(
    QOpenGLFunctions_1_5 *self,
    GLdouble angle,
    GLdouble x,
    GLdouble y,
    GLdouble z) {
  self->glRotated(angle, x, y, z);
}

//  void QOpenGLFunctions_1_5::glPushMatrix()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_512glPushMatrixEv(
    QOpenGLFunctions_1_5 *self) {
  self->glPushMatrix();
}

//  void QOpenGLFunctions_1_5::glPopMatrix()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_511glPopMatrixEv(
    QOpenGLFunctions_1_5 *self) {
  self->glPopMatrix();
}

//  void QOpenGLFunctions_1_5::glOrtho(GLdouble left, GLdouble right,
//      GLdouble bottom, GLdouble top, GLdouble zNear, GLdouble zFar)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_57glOrthoEdddddd(
    QOpenGLFunctions_1_5 *self,
    GLdouble left,
    GLdouble right,
    GLdouble bottom,
    GLdouble top,
    GLdouble zNear,
    GLdouble zFar) {
  self->glOrtho(left, right, bottom, top, zNear, zFar);
}

//  void QOpenGLFunctions_1_5::glMultMatrixd(const GLdouble *m)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glMultMatrixdEPKd(
    QOpenGLFunctions_1_5 *self,
    const GLdouble *m) {
  self->glMultMatrixd(m);
}

//  void QOpenGLFunctions_1_5::glMultMatrixf(const GLfloat *m)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glMultMatrixfEPKf(
    QOpenGLFunctions_1_5 *self,
    const GLfloat *m) {
  self->glMultMatrixf(m);
}

//  void QOpenGLFunctions_1_5::glMatrixMode(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_512glMatrixModeEj(
    QOpenGLFunctions_1_5 *self,
    GLenum mode) {
  self->glMatrixMode(mode);
}

//  void QOpenGLFunctions_1_5::glLoadMatrixd(const GLdouble *m)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glLoadMatrixdEPKd(
    QOpenGLFunctions_1_5 *self,
    const GLdouble *m) {
  self->glLoadMatrixd(m);
}

//  void QOpenGLFunctions_1_5::glLoadMatrixf(const GLfloat *m)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glLoadMatrixfEPKf(
    QOpenGLFunctions_1_5 *self,
    const GLfloat *m) {
  self->glLoadMatrixf(m);
}

//  void QOpenGLFunctions_1_5::glLoadIdentity()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_514glLoadIdentityEv(
    QOpenGLFunctions_1_5 *self) {
  self->glLoadIdentity();
}

//  void QOpenGLFunctions_1_5::glFrustum(GLdouble left, GLdouble right,
//      GLdouble bottom, GLdouble top, GLdouble zNear, GLdouble zFar)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_59glFrustumEdddddd(
    QOpenGLFunctions_1_5 *self,
    GLdouble left,
    GLdouble right,
    GLdouble bottom,
    GLdouble top,
    GLdouble zNear,
    GLdouble zFar) {
  self->glFrustum(left, right, bottom, top, zNear, zFar);
}

//  GLboolean QOpenGLFunctions_1_5::glIsList(GLuint list)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN20QOpenGLFunctions_1_58glIsListEj(
    QOpenGLFunctions_1_5 *self,
    GLuint list) {
  return self->glIsList(list);
}

//  void QOpenGLFunctions_1_5::glGetTexGeniv(GLenum coord, GLenum pname,
//      GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glGetTexGenivEjjPi(
    QOpenGLFunctions_1_5 *self,
    GLenum coord,
    GLenum pname,
    GLint *params) {
  self->glGetTexGeniv(coord, pname, params);
}

//  void QOpenGLFunctions_1_5::glGetTexGenfv(GLenum coord, GLenum pname,
//      GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glGetTexGenfvEjjPf(
    QOpenGLFunctions_1_5 *self,
    GLenum coord,
    GLenum pname,
    GLfloat *params) {
  self->glGetTexGenfv(coord, pname, params);
}

//  void QOpenGLFunctions_1_5::glGetTexGendv(GLenum coord, GLenum pname,
//      GLdouble *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glGetTexGendvEjjPd(
    QOpenGLFunctions_1_5 *self,
    GLenum coord,
    GLenum pname,
    GLdouble *params) {
  self->glGetTexGendv(coord, pname, params);
}

//  void QOpenGLFunctions_1_5::glGetTexEnviv(GLenum target, GLenum pname,
//      GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glGetTexEnvivEjjPi(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLenum pname,
    GLint *params) {
  self->glGetTexEnviv(target, pname, params);
}

//  void QOpenGLFunctions_1_5::glGetTexEnvfv(GLenum target, GLenum pname,
//      GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glGetTexEnvfvEjjPf(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLenum pname,
    GLfloat *params) {
  self->glGetTexEnvfv(target, pname, params);
}

//  void QOpenGLFunctions_1_5::glGetPolygonStipple(GLubyte *mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_519glGetPolygonStippleEPh(
    QOpenGLFunctions_1_5 *self,
    GLubyte *mask) {
  self->glGetPolygonStipple(mask);
}

//  void QOpenGLFunctions_1_5::glGetPixelMapusv(GLenum map, GLushort *values)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_516glGetPixelMapusvEjPt(
    QOpenGLFunctions_1_5 *self,
    GLenum map,
    GLushort *values) {
  self->glGetPixelMapusv(map, values);
}

//  void QOpenGLFunctions_1_5::glGetPixelMapuiv(GLenum map, GLuint *values)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_516glGetPixelMapuivEjPj(
    QOpenGLFunctions_1_5 *self,
    GLenum map,
    GLuint *values) {
  self->glGetPixelMapuiv(map, values);
}

//  void QOpenGLFunctions_1_5::glGetPixelMapfv(GLenum map, GLfloat *values)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_515glGetPixelMapfvEjPf(
    QOpenGLFunctions_1_5 *self,
    GLenum map,
    GLfloat *values) {
  self->glGetPixelMapfv(map, values);
}

//  void QOpenGLFunctions_1_5::glGetMaterialiv(GLenum face, GLenum pname,
//      GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_515glGetMaterialivEjjPi(
    QOpenGLFunctions_1_5 *self,
    GLenum face,
    GLenum pname,
    GLint *params) {
  self->glGetMaterialiv(face, pname, params);
}

//  void QOpenGLFunctions_1_5::glGetMaterialfv(GLenum face, GLenum pname,
//      GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_515glGetMaterialfvEjjPf(
    QOpenGLFunctions_1_5 *self,
    GLenum face,
    GLenum pname,
    GLfloat *params) {
  self->glGetMaterialfv(face, pname, params);
}

//  void QOpenGLFunctions_1_5::glGetMapiv(GLenum target, GLenum query, GLint
//      *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_510glGetMapivEjjPi(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLenum query,
    GLint *v) {
  self->glGetMapiv(target, query, v);
}

//  void QOpenGLFunctions_1_5::glGetMapfv(GLenum target, GLenum query,
//      GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_510glGetMapfvEjjPf(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLenum query,
    GLfloat *v) {
  self->glGetMapfv(target, query, v);
}

//  void QOpenGLFunctions_1_5::glGetMapdv(GLenum target, GLenum query,
//      GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_510glGetMapdvEjjPd(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLenum query,
    GLdouble *v) {
  self->glGetMapdv(target, query, v);
}

//  void QOpenGLFunctions_1_5::glGetLightiv(GLenum light, GLenum pname, GLint
//      *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_512glGetLightivEjjPi(
    QOpenGLFunctions_1_5 *self,
    GLenum light,
    GLenum pname,
    GLint *params) {
  self->glGetLightiv(light, pname, params);
}

//  void QOpenGLFunctions_1_5::glGetLightfv(GLenum light, GLenum pname,
//      GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_512glGetLightfvEjjPf(
    QOpenGLFunctions_1_5 *self,
    GLenum light,
    GLenum pname,
    GLfloat *params) {
  self->glGetLightfv(light, pname, params);
}

//  void QOpenGLFunctions_1_5::glGetClipPlane(GLenum plane, GLdouble
//      *equation)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_514glGetClipPlaneEjPd(
    QOpenGLFunctions_1_5 *self,
    GLenum plane,
    GLdouble *equation) {
  self->glGetClipPlane(plane, equation);
}

//  void QOpenGLFunctions_1_5::glDrawPixels(GLsizei width, GLsizei height,
//      GLenum format, GLenum type, const GLvoid *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_512glDrawPixelsEiijjPKv(
    QOpenGLFunctions_1_5 *self,
    GLsizei width,
    GLsizei height,
    GLenum format,
    GLenum type,
    const GLvoid *pixels) {
  self->glDrawPixels(width, height, format, type, pixels);
}

//  void QOpenGLFunctions_1_5::glCopyPixels(GLint x, GLint y, GLsizei width,
//      GLsizei height, GLenum type)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_512glCopyPixelsEiiiij(
    QOpenGLFunctions_1_5 *self,
    GLint x,
    GLint y,
    GLsizei width,
    GLsizei height,
    GLenum type) {
  self->glCopyPixels(x, y, width, height, type);
}

//  void QOpenGLFunctions_1_5::glPixelMapusv(GLenum map, GLint mapsize, const
//      GLushort *values)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glPixelMapusvEjiPKt(
    QOpenGLFunctions_1_5 *self,
    GLenum map,
    GLint mapsize,
    const GLushort *values) {
  self->glPixelMapusv(map, mapsize, values);
}

//  void QOpenGLFunctions_1_5::glPixelMapuiv(GLenum map, GLint mapsize, const
//      GLuint *values)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glPixelMapuivEjiPKj(
    QOpenGLFunctions_1_5 *self,
    GLenum map,
    GLint mapsize,
    const GLuint *values) {
  self->glPixelMapuiv(map, mapsize, values);
}

//  void QOpenGLFunctions_1_5::glPixelMapfv(GLenum map, GLint mapsize, const
//      GLfloat *values)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_512glPixelMapfvEjiPKf(
    QOpenGLFunctions_1_5 *self,
    GLenum map,
    GLint mapsize,
    const GLfloat *values) {
  self->glPixelMapfv(map, mapsize, values);
}

//  void QOpenGLFunctions_1_5::glPixelTransferi(GLenum pname, GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_516glPixelTransferiEji(
    QOpenGLFunctions_1_5 *self,
    GLenum pname,
    GLint param) {
  self->glPixelTransferi(pname, param);
}

//  void QOpenGLFunctions_1_5::glPixelTransferf(GLenum pname, GLfloat param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_516glPixelTransferfEjf(
    QOpenGLFunctions_1_5 *self,
    GLenum pname,
    GLfloat param) {
  self->glPixelTransferf(pname, param);
}

//  void QOpenGLFunctions_1_5::glPixelZoom(GLfloat xfactor, GLfloat yfactor)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_511glPixelZoomEff(
    QOpenGLFunctions_1_5 *self,
    GLfloat xfactor,
    GLfloat yfactor) {
  self->glPixelZoom(xfactor, yfactor);
}

//  void QOpenGLFunctions_1_5::glAlphaFunc(GLenum func, GLfloat ref)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_511glAlphaFuncEjf(
    QOpenGLFunctions_1_5 *self,
    GLenum func,
    GLfloat ref) {
  self->glAlphaFunc(func, ref);
}

//  void QOpenGLFunctions_1_5::glEvalPoint2(GLint i, GLint j)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_512glEvalPoint2Eii(
    QOpenGLFunctions_1_5 *self,
    GLint i,
    GLint j) {
  self->glEvalPoint2(i, j);
}

//  void QOpenGLFunctions_1_5::glEvalMesh2(GLenum mode, GLint i1, GLint i2,
//      GLint j1, GLint j2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_511glEvalMesh2Ejiiii(
    QOpenGLFunctions_1_5 *self,
    GLenum mode,
    GLint i1,
    GLint i2,
    GLint j1,
    GLint j2) {
  self->glEvalMesh2(mode, i1, i2, j1, j2);
}

//  void QOpenGLFunctions_1_5::glEvalPoint1(GLint i)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_512glEvalPoint1Ei(
    QOpenGLFunctions_1_5 *self,
    GLint i) {
  self->glEvalPoint1(i);
}

//  void QOpenGLFunctions_1_5::glEvalMesh1(GLenum mode, GLint i1, GLint i2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_511glEvalMesh1Ejii(
    QOpenGLFunctions_1_5 *self,
    GLenum mode,
    GLint i1,
    GLint i2) {
  self->glEvalMesh1(mode, i1, i2);
}

//  void QOpenGLFunctions_1_5::glEvalCoord2fv(const GLfloat *u)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_514glEvalCoord2fvEPKf(
    QOpenGLFunctions_1_5 *self,
    const GLfloat *u) {
  self->glEvalCoord2fv(u);
}

//  void QOpenGLFunctions_1_5::glEvalCoord2f(GLfloat u, GLfloat v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glEvalCoord2fEff(
    QOpenGLFunctions_1_5 *self,
    GLfloat u,
    GLfloat v) {
  self->glEvalCoord2f(u, v);
}

//  void QOpenGLFunctions_1_5::glEvalCoord2dv(const GLdouble *u)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_514glEvalCoord2dvEPKd(
    QOpenGLFunctions_1_5 *self,
    const GLdouble *u) {
  self->glEvalCoord2dv(u);
}

//  void QOpenGLFunctions_1_5::glEvalCoord2d(GLdouble u, GLdouble v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glEvalCoord2dEdd(
    QOpenGLFunctions_1_5 *self,
    GLdouble u,
    GLdouble v) {
  self->glEvalCoord2d(u, v);
}

//  void QOpenGLFunctions_1_5::glEvalCoord1fv(const GLfloat *u)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_514glEvalCoord1fvEPKf(
    QOpenGLFunctions_1_5 *self,
    const GLfloat *u) {
  self->glEvalCoord1fv(u);
}

//  void QOpenGLFunctions_1_5::glEvalCoord1f(GLfloat u)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glEvalCoord1fEf(
    QOpenGLFunctions_1_5 *self,
    GLfloat u) {
  self->glEvalCoord1f(u);
}

//  void QOpenGLFunctions_1_5::glEvalCoord1dv(const GLdouble *u)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_514glEvalCoord1dvEPKd(
    QOpenGLFunctions_1_5 *self,
    const GLdouble *u) {
  self->glEvalCoord1dv(u);
}

//  void QOpenGLFunctions_1_5::glEvalCoord1d(GLdouble u)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glEvalCoord1dEd(
    QOpenGLFunctions_1_5 *self,
    GLdouble u) {
  self->glEvalCoord1d(u);
}

//  void QOpenGLFunctions_1_5::glMapGrid2f(GLint un, GLfloat u1, GLfloat u2,
//      GLint vn, GLfloat v1, GLfloat v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_511glMapGrid2fEiffiff(
    QOpenGLFunctions_1_5 *self,
    GLint un,
    GLfloat u1,
    GLfloat u2,
    GLint vn,
    GLfloat v1,
    GLfloat v2) {
  self->glMapGrid2f(un, u1, u2, vn, v1, v2);
}

//  void QOpenGLFunctions_1_5::glMapGrid2d(GLint un, GLdouble u1, GLdouble
//      u2, GLint vn, GLdouble v1, GLdouble v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_511glMapGrid2dEiddidd(
    QOpenGLFunctions_1_5 *self,
    GLint un,
    GLdouble u1,
    GLdouble u2,
    GLint vn,
    GLdouble v1,
    GLdouble v2) {
  self->glMapGrid2d(un, u1, u2, vn, v1, v2);
}

//  void QOpenGLFunctions_1_5::glMapGrid1f(GLint un, GLfloat u1, GLfloat u2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_511glMapGrid1fEiff(
    QOpenGLFunctions_1_5 *self,
    GLint un,
    GLfloat u1,
    GLfloat u2) {
  self->glMapGrid1f(un, u1, u2);
}

//  void QOpenGLFunctions_1_5::glMapGrid1d(GLint un, GLdouble u1, GLdouble
//      u2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_511glMapGrid1dEidd(
    QOpenGLFunctions_1_5 *self,
    GLint un,
    GLdouble u1,
    GLdouble u2) {
  self->glMapGrid1d(un, u1, u2);
}

//  void QOpenGLFunctions_1_5::glMap2f(GLenum target, GLfloat u1, GLfloat u2,
//      GLint ustride, GLint uorder, GLfloat v1, GLfloat v2, GLint vstride,
//      GLint vorder, const GLfloat *points)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_57glMap2fEjffiiffiiPKf(
    QOpenGLFunctions_1_5 *self,
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

//  void QOpenGLFunctions_1_5::glMap2d(GLenum target, GLdouble u1, GLdouble
//      u2, GLint ustride, GLint uorder, GLdouble v1, GLdouble v2, GLint
//      vstride, GLint vorder, const GLdouble *points)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_57glMap2dEjddiiddiiPKd(
    QOpenGLFunctions_1_5 *self,
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

//  void QOpenGLFunctions_1_5::glMap1f(GLenum target, GLfloat u1, GLfloat u2,
//      GLint stride, GLint order, const GLfloat *points)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_57glMap1fEjffiiPKf(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLfloat u1,
    GLfloat u2,
    GLint stride,
    GLint order,
    const GLfloat *points) {
  self->glMap1f(target, u1, u2, stride, order, points);
}

//  void QOpenGLFunctions_1_5::glMap1d(GLenum target, GLdouble u1, GLdouble
//      u2, GLint stride, GLint order, const GLdouble *points)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_57glMap1dEjddiiPKd(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLdouble u1,
    GLdouble u2,
    GLint stride,
    GLint order,
    const GLdouble *points) {
  self->glMap1d(target, u1, u2, stride, order, points);
}

//  void QOpenGLFunctions_1_5::glPushAttrib(GLbitfield mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_512glPushAttribEj(
    QOpenGLFunctions_1_5 *self,
    GLbitfield mask) {
  self->glPushAttrib(mask);
}

//  void QOpenGLFunctions_1_5::glPopAttrib()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_511glPopAttribEv(
    QOpenGLFunctions_1_5 *self) {
  self->glPopAttrib();
}

//  void QOpenGLFunctions_1_5::glAccum(GLenum op, GLfloat value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_57glAccumEjf(
    QOpenGLFunctions_1_5 *self,
    GLenum op,
    GLfloat value) {
  self->glAccum(op, value);
}

//  void QOpenGLFunctions_1_5::glIndexMask(GLuint mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_511glIndexMaskEj(
    QOpenGLFunctions_1_5 *self,
    GLuint mask) {
  self->glIndexMask(mask);
}

//  void QOpenGLFunctions_1_5::glClearIndex(GLfloat c)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_512glClearIndexEf(
    QOpenGLFunctions_1_5 *self,
    GLfloat c) {
  self->glClearIndex(c);
}

//  void QOpenGLFunctions_1_5::glClearAccum(GLfloat red, GLfloat green,
//      GLfloat blue, GLfloat alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_512glClearAccumEffff(
    QOpenGLFunctions_1_5 *self,
    GLfloat red,
    GLfloat green,
    GLfloat blue,
    GLfloat alpha) {
  self->glClearAccum(red, green, blue, alpha);
}

//  void QOpenGLFunctions_1_5::glPushName(GLuint name)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_510glPushNameEj(
    QOpenGLFunctions_1_5 *self,
    GLuint name) {
  self->glPushName(name);
}

//  void QOpenGLFunctions_1_5::glPopName()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_59glPopNameEv(
    QOpenGLFunctions_1_5 *self) {
  self->glPopName();
}

//  void QOpenGLFunctions_1_5::glPassThrough(GLfloat token)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glPassThroughEf(
    QOpenGLFunctions_1_5 *self,
    GLfloat token) {
  self->glPassThrough(token);
}

//  void QOpenGLFunctions_1_5::glLoadName(GLuint name)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_510glLoadNameEj(
    QOpenGLFunctions_1_5 *self,
    GLuint name) {
  self->glLoadName(name);
}

//  void QOpenGLFunctions_1_5::glInitNames()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_511glInitNamesEv(
    QOpenGLFunctions_1_5 *self) {
  self->glInitNames();
}

//  GLint QOpenGLFunctions_1_5::glRenderMode(GLenum mode)
extern "C" Q_DECL_EXPORT
GLint ritual_ZN20QOpenGLFunctions_1_512glRenderModeEj(
    QOpenGLFunctions_1_5 *self,
    GLenum mode) {
  return self->glRenderMode(mode);
}

//  void QOpenGLFunctions_1_5::glSelectBuffer(GLsizei size, GLuint *buffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_514glSelectBufferEiPj(
    QOpenGLFunctions_1_5 *self,
    GLsizei size,
    GLuint *buffer) {
  self->glSelectBuffer(size, buffer);
}

//  void QOpenGLFunctions_1_5::glFeedbackBuffer(GLsizei size, GLenum type,
//      GLfloat *buffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_516glFeedbackBufferEijPf(
    QOpenGLFunctions_1_5 *self,
    GLsizei size,
    GLenum type,
    GLfloat *buffer) {
  self->glFeedbackBuffer(size, type, buffer);
}

//  void QOpenGLFunctions_1_5::glTexGeniv(GLenum coord, GLenum pname, const
//      GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_510glTexGenivEjjPKi(
    QOpenGLFunctions_1_5 *self,
    GLenum coord,
    GLenum pname,
    const GLint *params) {
  self->glTexGeniv(coord, pname, params);
}

//  void QOpenGLFunctions_1_5::glTexGeni(GLenum coord, GLenum pname, GLint
//      param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_59glTexGeniEjji(
    QOpenGLFunctions_1_5 *self,
    GLenum coord,
    GLenum pname,
    GLint param) {
  self->glTexGeni(coord, pname, param);
}

//  void QOpenGLFunctions_1_5::glTexGenfv(GLenum coord, GLenum pname, const
//      GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_510glTexGenfvEjjPKf(
    QOpenGLFunctions_1_5 *self,
    GLenum coord,
    GLenum pname,
    const GLfloat *params) {
  self->glTexGenfv(coord, pname, params);
}

//  void QOpenGLFunctions_1_5::glTexGenf(GLenum coord, GLenum pname, GLfloat
//      param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_59glTexGenfEjjf(
    QOpenGLFunctions_1_5 *self,
    GLenum coord,
    GLenum pname,
    GLfloat param) {
  self->glTexGenf(coord, pname, param);
}

//  void QOpenGLFunctions_1_5::glTexGendv(GLenum coord, GLenum pname, const
//      GLdouble *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_510glTexGendvEjjPKd(
    QOpenGLFunctions_1_5 *self,
    GLenum coord,
    GLenum pname,
    const GLdouble *params) {
  self->glTexGendv(coord, pname, params);
}

//  void QOpenGLFunctions_1_5::glTexGend(GLenum coord, GLenum pname, GLdouble
//      param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_59glTexGendEjjd(
    QOpenGLFunctions_1_5 *self,
    GLenum coord,
    GLenum pname,
    GLdouble param) {
  self->glTexGend(coord, pname, param);
}

//  void QOpenGLFunctions_1_5::glTexEnviv(GLenum target, GLenum pname, const
//      GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_510glTexEnvivEjjPKi(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLenum pname,
    const GLint *params) {
  self->glTexEnviv(target, pname, params);
}

//  void QOpenGLFunctions_1_5::glTexEnvi(GLenum target, GLenum pname, GLint
//      param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_59glTexEnviEjji(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLenum pname,
    GLint param) {
  self->glTexEnvi(target, pname, param);
}

//  void QOpenGLFunctions_1_5::glTexEnvfv(GLenum target, GLenum pname, const
//      GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_510glTexEnvfvEjjPKf(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLenum pname,
    const GLfloat *params) {
  self->glTexEnvfv(target, pname, params);
}

//  void QOpenGLFunctions_1_5::glTexEnvf(GLenum target, GLenum pname, GLfloat
//      param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_59glTexEnvfEjjf(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLenum pname,
    GLfloat param) {
  self->glTexEnvf(target, pname, param);
}

//  void QOpenGLFunctions_1_5::glShadeModel(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_512glShadeModelEj(
    QOpenGLFunctions_1_5 *self,
    GLenum mode) {
  self->glShadeModel(mode);
}

//  void QOpenGLFunctions_1_5::glPolygonStipple(const GLubyte *mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_516glPolygonStippleEPKh(
    QOpenGLFunctions_1_5 *self,
    const GLubyte *mask) {
  self->glPolygonStipple(mask);
}

//  void QOpenGLFunctions_1_5::glMaterialiv(GLenum face, GLenum pname, const
//      GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_512glMaterialivEjjPKi(
    QOpenGLFunctions_1_5 *self,
    GLenum face,
    GLenum pname,
    const GLint *params) {
  self->glMaterialiv(face, pname, params);
}

//  void QOpenGLFunctions_1_5::glMateriali(GLenum face, GLenum pname, GLint
//      param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_511glMaterialiEjji(
    QOpenGLFunctions_1_5 *self,
    GLenum face,
    GLenum pname,
    GLint param) {
  self->glMateriali(face, pname, param);
}

//  void QOpenGLFunctions_1_5::glMaterialfv(GLenum face, GLenum pname, const
//      GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_512glMaterialfvEjjPKf(
    QOpenGLFunctions_1_5 *self,
    GLenum face,
    GLenum pname,
    const GLfloat *params) {
  self->glMaterialfv(face, pname, params);
}

//  void QOpenGLFunctions_1_5::glMaterialf(GLenum face, GLenum pname, GLfloat
//      param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_511glMaterialfEjjf(
    QOpenGLFunctions_1_5 *self,
    GLenum face,
    GLenum pname,
    GLfloat param) {
  self->glMaterialf(face, pname, param);
}

//  void QOpenGLFunctions_1_5::glLineStipple(GLint factor, GLushort pattern)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glLineStippleEit(
    QOpenGLFunctions_1_5 *self,
    GLint factor,
    GLushort pattern) {
  self->glLineStipple(factor, pattern);
}

//  void QOpenGLFunctions_1_5::glLightModeliv(GLenum pname, const GLint
//      *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_514glLightModelivEjPKi(
    QOpenGLFunctions_1_5 *self,
    GLenum pname,
    const GLint *params) {
  self->glLightModeliv(pname, params);
}

//  void QOpenGLFunctions_1_5::glLightModeli(GLenum pname, GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glLightModeliEji(
    QOpenGLFunctions_1_5 *self,
    GLenum pname,
    GLint param) {
  self->glLightModeli(pname, param);
}

//  void QOpenGLFunctions_1_5::glLightModelfv(GLenum pname, const GLfloat
//      *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_514glLightModelfvEjPKf(
    QOpenGLFunctions_1_5 *self,
    GLenum pname,
    const GLfloat *params) {
  self->glLightModelfv(pname, params);
}

//  void QOpenGLFunctions_1_5::glLightModelf(GLenum pname, GLfloat param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glLightModelfEjf(
    QOpenGLFunctions_1_5 *self,
    GLenum pname,
    GLfloat param) {
  self->glLightModelf(pname, param);
}

//  void QOpenGLFunctions_1_5::glLightiv(GLenum light, GLenum pname, const
//      GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_59glLightivEjjPKi(
    QOpenGLFunctions_1_5 *self,
    GLenum light,
    GLenum pname,
    const GLint *params) {
  self->glLightiv(light, pname, params);
}

//  void QOpenGLFunctions_1_5::glLighti(GLenum light, GLenum pname, GLint
//      param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_58glLightiEjji(
    QOpenGLFunctions_1_5 *self,
    GLenum light,
    GLenum pname,
    GLint param) {
  self->glLighti(light, pname, param);
}

//  void QOpenGLFunctions_1_5::glLightfv(GLenum light, GLenum pname, const
//      GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_59glLightfvEjjPKf(
    QOpenGLFunctions_1_5 *self,
    GLenum light,
    GLenum pname,
    const GLfloat *params) {
  self->glLightfv(light, pname, params);
}

//  void QOpenGLFunctions_1_5::glLightf(GLenum light, GLenum pname, GLfloat
//      param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_58glLightfEjjf(
    QOpenGLFunctions_1_5 *self,
    GLenum light,
    GLenum pname,
    GLfloat param) {
  self->glLightf(light, pname, param);
}

//  void QOpenGLFunctions_1_5::glFogiv(GLenum pname, const GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_57glFogivEjPKi(
    QOpenGLFunctions_1_5 *self,
    GLenum pname,
    const GLint *params) {
  self->glFogiv(pname, params);
}

//  void QOpenGLFunctions_1_5::glFogi(GLenum pname, GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_56glFogiEji(
    QOpenGLFunctions_1_5 *self,
    GLenum pname,
    GLint param) {
  self->glFogi(pname, param);
}

//  void QOpenGLFunctions_1_5::glFogfv(GLenum pname, const GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_57glFogfvEjPKf(
    QOpenGLFunctions_1_5 *self,
    GLenum pname,
    const GLfloat *params) {
  self->glFogfv(pname, params);
}

//  void QOpenGLFunctions_1_5::glFogf(GLenum pname, GLfloat param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_56glFogfEjf(
    QOpenGLFunctions_1_5 *self,
    GLenum pname,
    GLfloat param) {
  self->glFogf(pname, param);
}

//  void QOpenGLFunctions_1_5::glColorMaterial(GLenum face, GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_515glColorMaterialEjj(
    QOpenGLFunctions_1_5 *self,
    GLenum face,
    GLenum mode) {
  self->glColorMaterial(face, mode);
}

//  void QOpenGLFunctions_1_5::glClipPlane(GLenum plane, const GLdouble
//      *equation)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_511glClipPlaneEjPKd(
    QOpenGLFunctions_1_5 *self,
    GLenum plane,
    const GLdouble *equation) {
  self->glClipPlane(plane, equation);
}

//  void QOpenGLFunctions_1_5::glVertex4sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_511glVertex4svEPKs(
    QOpenGLFunctions_1_5 *self,
    const GLshort *v) {
  self->glVertex4sv(v);
}

//  void QOpenGLFunctions_1_5::glVertex4s(GLshort x, GLshort y, GLshort z,
//      GLshort w)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_510glVertex4sEssss(
    QOpenGLFunctions_1_5 *self,
    GLshort x,
    GLshort y,
    GLshort z,
    GLshort w) {
  self->glVertex4s(x, y, z, w);
}

//  void QOpenGLFunctions_1_5::glVertex4iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_511glVertex4ivEPKi(
    QOpenGLFunctions_1_5 *self,
    const GLint *v) {
  self->glVertex4iv(v);
}

//  void QOpenGLFunctions_1_5::glVertex4i(GLint x, GLint y, GLint z, GLint w)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_510glVertex4iEiiii(
    QOpenGLFunctions_1_5 *self,
    GLint x,
    GLint y,
    GLint z,
    GLint w) {
  self->glVertex4i(x, y, z, w);
}

//  void QOpenGLFunctions_1_5::glVertex4fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_511glVertex4fvEPKf(
    QOpenGLFunctions_1_5 *self,
    const GLfloat *v) {
  self->glVertex4fv(v);
}

//  void QOpenGLFunctions_1_5::glVertex4f(GLfloat x, GLfloat y, GLfloat z,
//      GLfloat w)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_510glVertex4fEffff(
    QOpenGLFunctions_1_5 *self,
    GLfloat x,
    GLfloat y,
    GLfloat z,
    GLfloat w) {
  self->glVertex4f(x, y, z, w);
}

//  void QOpenGLFunctions_1_5::glVertex4dv(const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_511glVertex4dvEPKd(
    QOpenGLFunctions_1_5 *self,
    const GLdouble *v) {
  self->glVertex4dv(v);
}

//  void QOpenGLFunctions_1_5::glVertex4d(GLdouble x, GLdouble y, GLdouble z,
//      GLdouble w)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_510glVertex4dEdddd(
    QOpenGLFunctions_1_5 *self,
    GLdouble x,
    GLdouble y,
    GLdouble z,
    GLdouble w) {
  self->glVertex4d(x, y, z, w);
}

//  void QOpenGLFunctions_1_5::glVertex3sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_511glVertex3svEPKs(
    QOpenGLFunctions_1_5 *self,
    const GLshort *v) {
  self->glVertex3sv(v);
}

//  void QOpenGLFunctions_1_5::glVertex3s(GLshort x, GLshort y, GLshort z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_510glVertex3sEsss(
    QOpenGLFunctions_1_5 *self,
    GLshort x,
    GLshort y,
    GLshort z) {
  self->glVertex3s(x, y, z);
}

//  void QOpenGLFunctions_1_5::glVertex3iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_511glVertex3ivEPKi(
    QOpenGLFunctions_1_5 *self,
    const GLint *v) {
  self->glVertex3iv(v);
}

//  void QOpenGLFunctions_1_5::glVertex3i(GLint x, GLint y, GLint z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_510glVertex3iEiii(
    QOpenGLFunctions_1_5 *self,
    GLint x,
    GLint y,
    GLint z) {
  self->glVertex3i(x, y, z);
}

//  void QOpenGLFunctions_1_5::glVertex3fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_511glVertex3fvEPKf(
    QOpenGLFunctions_1_5 *self,
    const GLfloat *v) {
  self->glVertex3fv(v);
}

//  void QOpenGLFunctions_1_5::glVertex3f(GLfloat x, GLfloat y, GLfloat z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_510glVertex3fEfff(
    QOpenGLFunctions_1_5 *self,
    GLfloat x,
    GLfloat y,
    GLfloat z) {
  self->glVertex3f(x, y, z);
}

//  void QOpenGLFunctions_1_5::glVertex3dv(const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_511glVertex3dvEPKd(
    QOpenGLFunctions_1_5 *self,
    const GLdouble *v) {
  self->glVertex3dv(v);
}

//  void QOpenGLFunctions_1_5::glVertex3d(GLdouble x, GLdouble y, GLdouble z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_510glVertex3dEddd(
    QOpenGLFunctions_1_5 *self,
    GLdouble x,
    GLdouble y,
    GLdouble z) {
  self->glVertex3d(x, y, z);
}

//  void QOpenGLFunctions_1_5::glVertex2sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_511glVertex2svEPKs(
    QOpenGLFunctions_1_5 *self,
    const GLshort *v) {
  self->glVertex2sv(v);
}

//  void QOpenGLFunctions_1_5::glVertex2s(GLshort x, GLshort y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_510glVertex2sEss(
    QOpenGLFunctions_1_5 *self,
    GLshort x,
    GLshort y) {
  self->glVertex2s(x, y);
}

//  void QOpenGLFunctions_1_5::glVertex2iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_511glVertex2ivEPKi(
    QOpenGLFunctions_1_5 *self,
    const GLint *v) {
  self->glVertex2iv(v);
}

//  void QOpenGLFunctions_1_5::glVertex2i(GLint x, GLint y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_510glVertex2iEii(
    QOpenGLFunctions_1_5 *self,
    GLint x,
    GLint y) {
  self->glVertex2i(x, y);
}

//  void QOpenGLFunctions_1_5::glVertex2fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_511glVertex2fvEPKf(
    QOpenGLFunctions_1_5 *self,
    const GLfloat *v) {
  self->glVertex2fv(v);
}

//  void QOpenGLFunctions_1_5::glVertex2f(GLfloat x, GLfloat y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_510glVertex2fEff(
    QOpenGLFunctions_1_5 *self,
    GLfloat x,
    GLfloat y) {
  self->glVertex2f(x, y);
}

//  void QOpenGLFunctions_1_5::glVertex2dv(const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_511glVertex2dvEPKd(
    QOpenGLFunctions_1_5 *self,
    const GLdouble *v) {
  self->glVertex2dv(v);
}

//  void QOpenGLFunctions_1_5::glVertex2d(GLdouble x, GLdouble y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_510glVertex2dEdd(
    QOpenGLFunctions_1_5 *self,
    GLdouble x,
    GLdouble y) {
  self->glVertex2d(x, y);
}

//  void QOpenGLFunctions_1_5::glTexCoord4sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glTexCoord4svEPKs(
    QOpenGLFunctions_1_5 *self,
    const GLshort *v) {
  self->glTexCoord4sv(v);
}

//  void QOpenGLFunctions_1_5::glTexCoord4s(GLshort s, GLshort t, GLshort r,
//      GLshort q)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_512glTexCoord4sEssss(
    QOpenGLFunctions_1_5 *self,
    GLshort s,
    GLshort t,
    GLshort r,
    GLshort q) {
  self->glTexCoord4s(s, t, r, q);
}

//  void QOpenGLFunctions_1_5::glTexCoord4iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glTexCoord4ivEPKi(
    QOpenGLFunctions_1_5 *self,
    const GLint *v) {
  self->glTexCoord4iv(v);
}

//  void QOpenGLFunctions_1_5::glTexCoord4i(GLint s, GLint t, GLint r, GLint
//      q)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_512glTexCoord4iEiiii(
    QOpenGLFunctions_1_5 *self,
    GLint s,
    GLint t,
    GLint r,
    GLint q) {
  self->glTexCoord4i(s, t, r, q);
}

//  void QOpenGLFunctions_1_5::glTexCoord4fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glTexCoord4fvEPKf(
    QOpenGLFunctions_1_5 *self,
    const GLfloat *v) {
  self->glTexCoord4fv(v);
}

//  void QOpenGLFunctions_1_5::glTexCoord4f(GLfloat s, GLfloat t, GLfloat r,
//      GLfloat q)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_512glTexCoord4fEffff(
    QOpenGLFunctions_1_5 *self,
    GLfloat s,
    GLfloat t,
    GLfloat r,
    GLfloat q) {
  self->glTexCoord4f(s, t, r, q);
}

//  void QOpenGLFunctions_1_5::glTexCoord4dv(const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glTexCoord4dvEPKd(
    QOpenGLFunctions_1_5 *self,
    const GLdouble *v) {
  self->glTexCoord4dv(v);
}

//  void QOpenGLFunctions_1_5::glTexCoord4d(GLdouble s, GLdouble t, GLdouble
//      r, GLdouble q)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_512glTexCoord4dEdddd(
    QOpenGLFunctions_1_5 *self,
    GLdouble s,
    GLdouble t,
    GLdouble r,
    GLdouble q) {
  self->glTexCoord4d(s, t, r, q);
}

//  void QOpenGLFunctions_1_5::glTexCoord3sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glTexCoord3svEPKs(
    QOpenGLFunctions_1_5 *self,
    const GLshort *v) {
  self->glTexCoord3sv(v);
}

//  void QOpenGLFunctions_1_5::glTexCoord3s(GLshort s, GLshort t, GLshort r)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_512glTexCoord3sEsss(
    QOpenGLFunctions_1_5 *self,
    GLshort s,
    GLshort t,
    GLshort r) {
  self->glTexCoord3s(s, t, r);
}

//  void QOpenGLFunctions_1_5::glTexCoord3iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glTexCoord3ivEPKi(
    QOpenGLFunctions_1_5 *self,
    const GLint *v) {
  self->glTexCoord3iv(v);
}

//  void QOpenGLFunctions_1_5::glTexCoord3i(GLint s, GLint t, GLint r)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_512glTexCoord3iEiii(
    QOpenGLFunctions_1_5 *self,
    GLint s,
    GLint t,
    GLint r) {
  self->glTexCoord3i(s, t, r);
}

//  void QOpenGLFunctions_1_5::glTexCoord3fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glTexCoord3fvEPKf(
    QOpenGLFunctions_1_5 *self,
    const GLfloat *v) {
  self->glTexCoord3fv(v);
}

//  void QOpenGLFunctions_1_5::glTexCoord3f(GLfloat s, GLfloat t, GLfloat r)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_512glTexCoord3fEfff(
    QOpenGLFunctions_1_5 *self,
    GLfloat s,
    GLfloat t,
    GLfloat r) {
  self->glTexCoord3f(s, t, r);
}

//  void QOpenGLFunctions_1_5::glTexCoord3dv(const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glTexCoord3dvEPKd(
    QOpenGLFunctions_1_5 *self,
    const GLdouble *v) {
  self->glTexCoord3dv(v);
}

//  void QOpenGLFunctions_1_5::glTexCoord3d(GLdouble s, GLdouble t, GLdouble
//      r)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_512glTexCoord3dEddd(
    QOpenGLFunctions_1_5 *self,
    GLdouble s,
    GLdouble t,
    GLdouble r) {
  self->glTexCoord3d(s, t, r);
}

//  void QOpenGLFunctions_1_5::glTexCoord2sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glTexCoord2svEPKs(
    QOpenGLFunctions_1_5 *self,
    const GLshort *v) {
  self->glTexCoord2sv(v);
}

//  void QOpenGLFunctions_1_5::glTexCoord2s(GLshort s, GLshort t)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_512glTexCoord2sEss(
    QOpenGLFunctions_1_5 *self,
    GLshort s,
    GLshort t) {
  self->glTexCoord2s(s, t);
}

//  void QOpenGLFunctions_1_5::glTexCoord2iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glTexCoord2ivEPKi(
    QOpenGLFunctions_1_5 *self,
    const GLint *v) {
  self->glTexCoord2iv(v);
}

//  void QOpenGLFunctions_1_5::glTexCoord2i(GLint s, GLint t)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_512glTexCoord2iEii(
    QOpenGLFunctions_1_5 *self,
    GLint s,
    GLint t) {
  self->glTexCoord2i(s, t);
}

//  void QOpenGLFunctions_1_5::glTexCoord2fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glTexCoord2fvEPKf(
    QOpenGLFunctions_1_5 *self,
    const GLfloat *v) {
  self->glTexCoord2fv(v);
}

//  void QOpenGLFunctions_1_5::glTexCoord2f(GLfloat s, GLfloat t)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_512glTexCoord2fEff(
    QOpenGLFunctions_1_5 *self,
    GLfloat s,
    GLfloat t) {
  self->glTexCoord2f(s, t);
}

//  void QOpenGLFunctions_1_5::glTexCoord2dv(const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glTexCoord2dvEPKd(
    QOpenGLFunctions_1_5 *self,
    const GLdouble *v) {
  self->glTexCoord2dv(v);
}

//  void QOpenGLFunctions_1_5::glTexCoord2d(GLdouble s, GLdouble t)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_512glTexCoord2dEdd(
    QOpenGLFunctions_1_5 *self,
    GLdouble s,
    GLdouble t) {
  self->glTexCoord2d(s, t);
}

//  void QOpenGLFunctions_1_5::glTexCoord1sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glTexCoord1svEPKs(
    QOpenGLFunctions_1_5 *self,
    const GLshort *v) {
  self->glTexCoord1sv(v);
}

//  void QOpenGLFunctions_1_5::glTexCoord1s(GLshort s)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_512glTexCoord1sEs(
    QOpenGLFunctions_1_5 *self,
    GLshort s) {
  self->glTexCoord1s(s);
}

//  void QOpenGLFunctions_1_5::glTexCoord1iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glTexCoord1ivEPKi(
    QOpenGLFunctions_1_5 *self,
    const GLint *v) {
  self->glTexCoord1iv(v);
}

//  void QOpenGLFunctions_1_5::glTexCoord1i(GLint s)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_512glTexCoord1iEi(
    QOpenGLFunctions_1_5 *self,
    GLint s) {
  self->glTexCoord1i(s);
}

//  void QOpenGLFunctions_1_5::glTexCoord1fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glTexCoord1fvEPKf(
    QOpenGLFunctions_1_5 *self,
    const GLfloat *v) {
  self->glTexCoord1fv(v);
}

//  void QOpenGLFunctions_1_5::glTexCoord1f(GLfloat s)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_512glTexCoord1fEf(
    QOpenGLFunctions_1_5 *self,
    GLfloat s) {
  self->glTexCoord1f(s);
}

//  void QOpenGLFunctions_1_5::glTexCoord1dv(const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glTexCoord1dvEPKd(
    QOpenGLFunctions_1_5 *self,
    const GLdouble *v) {
  self->glTexCoord1dv(v);
}

//  void QOpenGLFunctions_1_5::glTexCoord1d(GLdouble s)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_512glTexCoord1dEd(
    QOpenGLFunctions_1_5 *self,
    GLdouble s) {
  self->glTexCoord1d(s);
}

//  void QOpenGLFunctions_1_5::glRectsv(const GLshort *v1, const GLshort *v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_58glRectsvEPKsS1_(
    QOpenGLFunctions_1_5 *self,
    const GLshort *v1,
    const GLshort *v2) {
  self->glRectsv(v1, v2);
}

//  void QOpenGLFunctions_1_5::glRects(GLshort x1, GLshort y1, GLshort x2,
//      GLshort y2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_57glRectsEssss(
    QOpenGLFunctions_1_5 *self,
    GLshort x1,
    GLshort y1,
    GLshort x2,
    GLshort y2) {
  self->glRects(x1, y1, x2, y2);
}

//  void QOpenGLFunctions_1_5::glRectiv(const GLint *v1, const GLint *v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_58glRectivEPKiS1_(
    QOpenGLFunctions_1_5 *self,
    const GLint *v1,
    const GLint *v2) {
  self->glRectiv(v1, v2);
}

//  void QOpenGLFunctions_1_5::glRecti(GLint x1, GLint y1, GLint x2, GLint
//      y2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_57glRectiEiiii(
    QOpenGLFunctions_1_5 *self,
    GLint x1,
    GLint y1,
    GLint x2,
    GLint y2) {
  self->glRecti(x1, y1, x2, y2);
}

//  void QOpenGLFunctions_1_5::glRectfv(const GLfloat *v1, const GLfloat *v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_58glRectfvEPKfS1_(
    QOpenGLFunctions_1_5 *self,
    const GLfloat *v1,
    const GLfloat *v2) {
  self->glRectfv(v1, v2);
}

//  void QOpenGLFunctions_1_5::glRectf(GLfloat x1, GLfloat y1, GLfloat x2,
//      GLfloat y2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_57glRectfEffff(
    QOpenGLFunctions_1_5 *self,
    GLfloat x1,
    GLfloat y1,
    GLfloat x2,
    GLfloat y2) {
  self->glRectf(x1, y1, x2, y2);
}

//  void QOpenGLFunctions_1_5::glRectdv(const GLdouble *v1, const GLdouble
//      *v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_58glRectdvEPKdS1_(
    QOpenGLFunctions_1_5 *self,
    const GLdouble *v1,
    const GLdouble *v2) {
  self->glRectdv(v1, v2);
}

//  void QOpenGLFunctions_1_5::glRectd(GLdouble x1, GLdouble y1, GLdouble x2,
//      GLdouble y2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_57glRectdEdddd(
    QOpenGLFunctions_1_5 *self,
    GLdouble x1,
    GLdouble y1,
    GLdouble x2,
    GLdouble y2) {
  self->glRectd(x1, y1, x2, y2);
}

//  void QOpenGLFunctions_1_5::glRasterPos4sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_514glRasterPos4svEPKs(
    QOpenGLFunctions_1_5 *self,
    const GLshort *v) {
  self->glRasterPos4sv(v);
}

//  void QOpenGLFunctions_1_5::glRasterPos4s(GLshort x, GLshort y, GLshort z,
//      GLshort w)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glRasterPos4sEssss(
    QOpenGLFunctions_1_5 *self,
    GLshort x,
    GLshort y,
    GLshort z,
    GLshort w) {
  self->glRasterPos4s(x, y, z, w);
}

//  void QOpenGLFunctions_1_5::glRasterPos4iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_514glRasterPos4ivEPKi(
    QOpenGLFunctions_1_5 *self,
    const GLint *v) {
  self->glRasterPos4iv(v);
}

//  void QOpenGLFunctions_1_5::glRasterPos4i(GLint x, GLint y, GLint z, GLint
//      w)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glRasterPos4iEiiii(
    QOpenGLFunctions_1_5 *self,
    GLint x,
    GLint y,
    GLint z,
    GLint w) {
  self->glRasterPos4i(x, y, z, w);
}

//  void QOpenGLFunctions_1_5::glRasterPos4fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_514glRasterPos4fvEPKf(
    QOpenGLFunctions_1_5 *self,
    const GLfloat *v) {
  self->glRasterPos4fv(v);
}

//  void QOpenGLFunctions_1_5::glRasterPos4f(GLfloat x, GLfloat y, GLfloat z,
//      GLfloat w)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glRasterPos4fEffff(
    QOpenGLFunctions_1_5 *self,
    GLfloat x,
    GLfloat y,
    GLfloat z,
    GLfloat w) {
  self->glRasterPos4f(x, y, z, w);
}

//  void QOpenGLFunctions_1_5::glRasterPos4dv(const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_514glRasterPos4dvEPKd(
    QOpenGLFunctions_1_5 *self,
    const GLdouble *v) {
  self->glRasterPos4dv(v);
}

//  void QOpenGLFunctions_1_5::glRasterPos4d(GLdouble x, GLdouble y, GLdouble
//      z, GLdouble w)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glRasterPos4dEdddd(
    QOpenGLFunctions_1_5 *self,
    GLdouble x,
    GLdouble y,
    GLdouble z,
    GLdouble w) {
  self->glRasterPos4d(x, y, z, w);
}

//  void QOpenGLFunctions_1_5::glRasterPos3sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_514glRasterPos3svEPKs(
    QOpenGLFunctions_1_5 *self,
    const GLshort *v) {
  self->glRasterPos3sv(v);
}

//  void QOpenGLFunctions_1_5::glRasterPos3s(GLshort x, GLshort y, GLshort z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glRasterPos3sEsss(
    QOpenGLFunctions_1_5 *self,
    GLshort x,
    GLshort y,
    GLshort z) {
  self->glRasterPos3s(x, y, z);
}

//  void QOpenGLFunctions_1_5::glRasterPos3iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_514glRasterPos3ivEPKi(
    QOpenGLFunctions_1_5 *self,
    const GLint *v) {
  self->glRasterPos3iv(v);
}

//  void QOpenGLFunctions_1_5::glRasterPos3i(GLint x, GLint y, GLint z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glRasterPos3iEiii(
    QOpenGLFunctions_1_5 *self,
    GLint x,
    GLint y,
    GLint z) {
  self->glRasterPos3i(x, y, z);
}

//  void QOpenGLFunctions_1_5::glRasterPos3fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_514glRasterPos3fvEPKf(
    QOpenGLFunctions_1_5 *self,
    const GLfloat *v) {
  self->glRasterPos3fv(v);
}

//  void QOpenGLFunctions_1_5::glRasterPos3f(GLfloat x, GLfloat y, GLfloat z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glRasterPos3fEfff(
    QOpenGLFunctions_1_5 *self,
    GLfloat x,
    GLfloat y,
    GLfloat z) {
  self->glRasterPos3f(x, y, z);
}

//  void QOpenGLFunctions_1_5::glRasterPos3dv(const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_514glRasterPos3dvEPKd(
    QOpenGLFunctions_1_5 *self,
    const GLdouble *v) {
  self->glRasterPos3dv(v);
}

//  void QOpenGLFunctions_1_5::glRasterPos3d(GLdouble x, GLdouble y, GLdouble
//      z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glRasterPos3dEddd(
    QOpenGLFunctions_1_5 *self,
    GLdouble x,
    GLdouble y,
    GLdouble z) {
  self->glRasterPos3d(x, y, z);
}

//  void QOpenGLFunctions_1_5::glRasterPos2sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_514glRasterPos2svEPKs(
    QOpenGLFunctions_1_5 *self,
    const GLshort *v) {
  self->glRasterPos2sv(v);
}

//  void QOpenGLFunctions_1_5::glRasterPos2s(GLshort x, GLshort y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glRasterPos2sEss(
    QOpenGLFunctions_1_5 *self,
    GLshort x,
    GLshort y) {
  self->glRasterPos2s(x, y);
}

//  void QOpenGLFunctions_1_5::glRasterPos2iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_514glRasterPos2ivEPKi(
    QOpenGLFunctions_1_5 *self,
    const GLint *v) {
  self->glRasterPos2iv(v);
}

//  void QOpenGLFunctions_1_5::glRasterPos2i(GLint x, GLint y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glRasterPos2iEii(
    QOpenGLFunctions_1_5 *self,
    GLint x,
    GLint y) {
  self->glRasterPos2i(x, y);
}

//  void QOpenGLFunctions_1_5::glRasterPos2fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_514glRasterPos2fvEPKf(
    QOpenGLFunctions_1_5 *self,
    const GLfloat *v) {
  self->glRasterPos2fv(v);
}

//  void QOpenGLFunctions_1_5::glRasterPos2f(GLfloat x, GLfloat y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glRasterPos2fEff(
    QOpenGLFunctions_1_5 *self,
    GLfloat x,
    GLfloat y) {
  self->glRasterPos2f(x, y);
}

//  void QOpenGLFunctions_1_5::glRasterPos2dv(const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_514glRasterPos2dvEPKd(
    QOpenGLFunctions_1_5 *self,
    const GLdouble *v) {
  self->glRasterPos2dv(v);
}

//  void QOpenGLFunctions_1_5::glRasterPos2d(GLdouble x, GLdouble y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glRasterPos2dEdd(
    QOpenGLFunctions_1_5 *self,
    GLdouble x,
    GLdouble y) {
  self->glRasterPos2d(x, y);
}

//  void QOpenGLFunctions_1_5::glNormal3sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_511glNormal3svEPKs(
    QOpenGLFunctions_1_5 *self,
    const GLshort *v) {
  self->glNormal3sv(v);
}

//  void QOpenGLFunctions_1_5::glNormal3s(GLshort nx, GLshort ny, GLshort nz)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_510glNormal3sEsss(
    QOpenGLFunctions_1_5 *self,
    GLshort nx,
    GLshort ny,
    GLshort nz) {
  self->glNormal3s(nx, ny, nz);
}

//  void QOpenGLFunctions_1_5::glNormal3iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_511glNormal3ivEPKi(
    QOpenGLFunctions_1_5 *self,
    const GLint *v) {
  self->glNormal3iv(v);
}

//  void QOpenGLFunctions_1_5::glNormal3i(GLint nx, GLint ny, GLint nz)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_510glNormal3iEiii(
    QOpenGLFunctions_1_5 *self,
    GLint nx,
    GLint ny,
    GLint nz) {
  self->glNormal3i(nx, ny, nz);
}

//  void QOpenGLFunctions_1_5::glNormal3fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_511glNormal3fvEPKf(
    QOpenGLFunctions_1_5 *self,
    const GLfloat *v) {
  self->glNormal3fv(v);
}

//  void QOpenGLFunctions_1_5::glNormal3f(GLfloat nx, GLfloat ny, GLfloat nz)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_510glNormal3fEfff(
    QOpenGLFunctions_1_5 *self,
    GLfloat nx,
    GLfloat ny,
    GLfloat nz) {
  self->glNormal3f(nx, ny, nz);
}

//  void QOpenGLFunctions_1_5::glNormal3dv(const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_511glNormal3dvEPKd(
    QOpenGLFunctions_1_5 *self,
    const GLdouble *v) {
  self->glNormal3dv(v);
}

//  void QOpenGLFunctions_1_5::glNormal3d(GLdouble nx, GLdouble ny, GLdouble
//      nz)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_510glNormal3dEddd(
    QOpenGLFunctions_1_5 *self,
    GLdouble nx,
    GLdouble ny,
    GLdouble nz) {
  self->glNormal3d(nx, ny, nz);
}

//  void QOpenGLFunctions_1_5::glNormal3bv(const GLbyte *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_511glNormal3bvEPKa(
    QOpenGLFunctions_1_5 *self,
    const GLbyte *v) {
  self->glNormal3bv(v);
}

//  void QOpenGLFunctions_1_5::glNormal3b(GLbyte nx, GLbyte ny, GLbyte nz)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_510glNormal3bEaaa(
    QOpenGLFunctions_1_5 *self,
    GLbyte nx,
    GLbyte ny,
    GLbyte nz) {
  self->glNormal3b(nx, ny, nz);
}

//  void QOpenGLFunctions_1_5::glIndexsv(const GLshort *c)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_59glIndexsvEPKs(
    QOpenGLFunctions_1_5 *self,
    const GLshort *c) {
  self->glIndexsv(c);
}

//  void QOpenGLFunctions_1_5::glIndexs(GLshort c)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_58glIndexsEs(
    QOpenGLFunctions_1_5 *self,
    GLshort c) {
  self->glIndexs(c);
}

//  void QOpenGLFunctions_1_5::glIndexiv(const GLint *c)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_59glIndexivEPKi(
    QOpenGLFunctions_1_5 *self,
    const GLint *c) {
  self->glIndexiv(c);
}

//  void QOpenGLFunctions_1_5::glIndexi(GLint c)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_58glIndexiEi(
    QOpenGLFunctions_1_5 *self,
    GLint c) {
  self->glIndexi(c);
}

//  void QOpenGLFunctions_1_5::glIndexfv(const GLfloat *c)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_59glIndexfvEPKf(
    QOpenGLFunctions_1_5 *self,
    const GLfloat *c) {
  self->glIndexfv(c);
}

//  void QOpenGLFunctions_1_5::glIndexf(GLfloat c)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_58glIndexfEf(
    QOpenGLFunctions_1_5 *self,
    GLfloat c) {
  self->glIndexf(c);
}

//  void QOpenGLFunctions_1_5::glIndexdv(const GLdouble *c)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_59glIndexdvEPKd(
    QOpenGLFunctions_1_5 *self,
    const GLdouble *c) {
  self->glIndexdv(c);
}

//  void QOpenGLFunctions_1_5::glIndexd(GLdouble c)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_58glIndexdEd(
    QOpenGLFunctions_1_5 *self,
    GLdouble c) {
  self->glIndexd(c);
}

//  void QOpenGLFunctions_1_5::glEnd()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_55glEndEv(QOpenGLFunctions_1_5 *self) {
  self->glEnd();
}

//  void QOpenGLFunctions_1_5::glEdgeFlagv(const GLboolean *flag)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_511glEdgeFlagvEPKh(
    QOpenGLFunctions_1_5 *self,
    const GLboolean *flag) {
  self->glEdgeFlagv(flag);
}

//  void QOpenGLFunctions_1_5::glEdgeFlag(GLboolean flag)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_510glEdgeFlagEh(
    QOpenGLFunctions_1_5 *self,
    GLboolean flag) {
  self->glEdgeFlag(flag);
}

//  void QOpenGLFunctions_1_5::glColor4usv(const GLushort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_511glColor4usvEPKt(
    QOpenGLFunctions_1_5 *self,
    const GLushort *v) {
  self->glColor4usv(v);
}

//  void QOpenGLFunctions_1_5::glColor4us(GLushort red, GLushort green,
//      GLushort blue, GLushort alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_510glColor4usEtttt(
    QOpenGLFunctions_1_5 *self,
    GLushort red,
    GLushort green,
    GLushort blue,
    GLushort alpha) {
  self->glColor4us(red, green, blue, alpha);
}

//  void QOpenGLFunctions_1_5::glColor4uiv(const GLuint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_511glColor4uivEPKj(
    QOpenGLFunctions_1_5 *self,
    const GLuint *v) {
  self->glColor4uiv(v);
}

//  void QOpenGLFunctions_1_5::glColor4ui(GLuint red, GLuint green, GLuint
//      blue, GLuint alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_510glColor4uiEjjjj(
    QOpenGLFunctions_1_5 *self,
    GLuint red,
    GLuint green,
    GLuint blue,
    GLuint alpha) {
  self->glColor4ui(red, green, blue, alpha);
}

//  void QOpenGLFunctions_1_5::glColor4ubv(const GLubyte *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_511glColor4ubvEPKh(
    QOpenGLFunctions_1_5 *self,
    const GLubyte *v) {
  self->glColor4ubv(v);
}

//  void QOpenGLFunctions_1_5::glColor4ub(GLubyte red, GLubyte green, GLubyte
//      blue, GLubyte alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_510glColor4ubEhhhh(
    QOpenGLFunctions_1_5 *self,
    GLubyte red,
    GLubyte green,
    GLubyte blue,
    GLubyte alpha) {
  self->glColor4ub(red, green, blue, alpha);
}

//  void QOpenGLFunctions_1_5::glColor4sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_510glColor4svEPKs(
    QOpenGLFunctions_1_5 *self,
    const GLshort *v) {
  self->glColor4sv(v);
}

//  void QOpenGLFunctions_1_5::glColor4s(GLshort red, GLshort green, GLshort
//      blue, GLshort alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_59glColor4sEssss(
    QOpenGLFunctions_1_5 *self,
    GLshort red,
    GLshort green,
    GLshort blue,
    GLshort alpha) {
  self->glColor4s(red, green, blue, alpha);
}

//  void QOpenGLFunctions_1_5::glColor4iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_510glColor4ivEPKi(
    QOpenGLFunctions_1_5 *self,
    const GLint *v) {
  self->glColor4iv(v);
}

//  void QOpenGLFunctions_1_5::glColor4i(GLint red, GLint green, GLint blue,
//      GLint alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_59glColor4iEiiii(
    QOpenGLFunctions_1_5 *self,
    GLint red,
    GLint green,
    GLint blue,
    GLint alpha) {
  self->glColor4i(red, green, blue, alpha);
}

//  void QOpenGLFunctions_1_5::glColor4fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_510glColor4fvEPKf(
    QOpenGLFunctions_1_5 *self,
    const GLfloat *v) {
  self->glColor4fv(v);
}

//  void QOpenGLFunctions_1_5::glColor4f(GLfloat red, GLfloat green, GLfloat
//      blue, GLfloat alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_59glColor4fEffff(
    QOpenGLFunctions_1_5 *self,
    GLfloat red,
    GLfloat green,
    GLfloat blue,
    GLfloat alpha) {
  self->glColor4f(red, green, blue, alpha);
}

//  void QOpenGLFunctions_1_5::glColor4dv(const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_510glColor4dvEPKd(
    QOpenGLFunctions_1_5 *self,
    const GLdouble *v) {
  self->glColor4dv(v);
}

//  void QOpenGLFunctions_1_5::glColor4d(GLdouble red, GLdouble green,
//      GLdouble blue, GLdouble alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_59glColor4dEdddd(
    QOpenGLFunctions_1_5 *self,
    GLdouble red,
    GLdouble green,
    GLdouble blue,
    GLdouble alpha) {
  self->glColor4d(red, green, blue, alpha);
}

//  void QOpenGLFunctions_1_5::glColor4bv(const GLbyte *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_510glColor4bvEPKa(
    QOpenGLFunctions_1_5 *self,
    const GLbyte *v) {
  self->glColor4bv(v);
}

//  void QOpenGLFunctions_1_5::glColor4b(GLbyte red, GLbyte green, GLbyte
//      blue, GLbyte alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_59glColor4bEaaaa(
    QOpenGLFunctions_1_5 *self,
    GLbyte red,
    GLbyte green,
    GLbyte blue,
    GLbyte alpha) {
  self->glColor4b(red, green, blue, alpha);
}

//  void QOpenGLFunctions_1_5::glColor3usv(const GLushort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_511glColor3usvEPKt(
    QOpenGLFunctions_1_5 *self,
    const GLushort *v) {
  self->glColor3usv(v);
}

//  void QOpenGLFunctions_1_5::glColor3us(GLushort red, GLushort green,
//      GLushort blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_510glColor3usEttt(
    QOpenGLFunctions_1_5 *self,
    GLushort red,
    GLushort green,
    GLushort blue) {
  self->glColor3us(red, green, blue);
}

//  void QOpenGLFunctions_1_5::glColor3uiv(const GLuint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_511glColor3uivEPKj(
    QOpenGLFunctions_1_5 *self,
    const GLuint *v) {
  self->glColor3uiv(v);
}

//  void QOpenGLFunctions_1_5::glColor3ui(GLuint red, GLuint green, GLuint
//      blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_510glColor3uiEjjj(
    QOpenGLFunctions_1_5 *self,
    GLuint red,
    GLuint green,
    GLuint blue) {
  self->glColor3ui(red, green, blue);
}

//  void QOpenGLFunctions_1_5::glColor3ubv(const GLubyte *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_511glColor3ubvEPKh(
    QOpenGLFunctions_1_5 *self,
    const GLubyte *v) {
  self->glColor3ubv(v);
}

//  void QOpenGLFunctions_1_5::glColor3ub(GLubyte red, GLubyte green, GLubyte
//      blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_510glColor3ubEhhh(
    QOpenGLFunctions_1_5 *self,
    GLubyte red,
    GLubyte green,
    GLubyte blue) {
  self->glColor3ub(red, green, blue);
}

//  void QOpenGLFunctions_1_5::glColor3sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_510glColor3svEPKs(
    QOpenGLFunctions_1_5 *self,
    const GLshort *v) {
  self->glColor3sv(v);
}

//  void QOpenGLFunctions_1_5::glColor3s(GLshort red, GLshort green, GLshort
//      blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_59glColor3sEsss(
    QOpenGLFunctions_1_5 *self,
    GLshort red,
    GLshort green,
    GLshort blue) {
  self->glColor3s(red, green, blue);
}

//  void QOpenGLFunctions_1_5::glColor3iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_510glColor3ivEPKi(
    QOpenGLFunctions_1_5 *self,
    const GLint *v) {
  self->glColor3iv(v);
}

//  void QOpenGLFunctions_1_5::glColor3i(GLint red, GLint green, GLint blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_59glColor3iEiii(
    QOpenGLFunctions_1_5 *self,
    GLint red,
    GLint green,
    GLint blue) {
  self->glColor3i(red, green, blue);
}

//  void QOpenGLFunctions_1_5::glColor3fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_510glColor3fvEPKf(
    QOpenGLFunctions_1_5 *self,
    const GLfloat *v) {
  self->glColor3fv(v);
}

//  void QOpenGLFunctions_1_5::glColor3f(GLfloat red, GLfloat green, GLfloat
//      blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_59glColor3fEfff(
    QOpenGLFunctions_1_5 *self,
    GLfloat red,
    GLfloat green,
    GLfloat blue) {
  self->glColor3f(red, green, blue);
}

//  void QOpenGLFunctions_1_5::glColor3dv(const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_510glColor3dvEPKd(
    QOpenGLFunctions_1_5 *self,
    const GLdouble *v) {
  self->glColor3dv(v);
}

//  void QOpenGLFunctions_1_5::glColor3d(GLdouble red, GLdouble green,
//      GLdouble blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_59glColor3dEddd(
    QOpenGLFunctions_1_5 *self,
    GLdouble red,
    GLdouble green,
    GLdouble blue) {
  self->glColor3d(red, green, blue);
}

//  void QOpenGLFunctions_1_5::glColor3bv(const GLbyte *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_510glColor3bvEPKa(
    QOpenGLFunctions_1_5 *self,
    const GLbyte *v) {
  self->glColor3bv(v);
}

//  void QOpenGLFunctions_1_5::glColor3b(GLbyte red, GLbyte green, GLbyte
//      blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_59glColor3bEaaa(
    QOpenGLFunctions_1_5 *self,
    GLbyte red,
    GLbyte green,
    GLbyte blue) {
  self->glColor3b(red, green, blue);
}

//  void QOpenGLFunctions_1_5::glBitmap(GLsizei width, GLsizei height,
//      GLfloat xorig, GLfloat yorig, GLfloat xmove, GLfloat ymove, const
//      GLubyte *bitmap)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_58glBitmapEiiffffPKh(
    QOpenGLFunctions_1_5 *self,
    GLsizei width,
    GLsizei height,
    GLfloat xorig,
    GLfloat yorig,
    GLfloat xmove,
    GLfloat ymove,
    const GLubyte *bitmap) {
  self->glBitmap(width, height, xorig, yorig, xmove, ymove, bitmap);
}

//  void QOpenGLFunctions_1_5::glBegin(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_57glBeginEj(
    QOpenGLFunctions_1_5 *self,
    GLenum mode) {
  self->glBegin(mode);
}

//  void QOpenGLFunctions_1_5::glListBase(GLuint base)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_510glListBaseEj(
    QOpenGLFunctions_1_5 *self,
    GLuint base) {
  self->glListBase(base);
}

//  GLuint QOpenGLFunctions_1_5::glGenLists(GLsizei range)
extern "C" Q_DECL_EXPORT
GLuint ritual_ZN20QOpenGLFunctions_1_510glGenListsEi(
    QOpenGLFunctions_1_5 *self,
    GLsizei range) {
  return self->glGenLists(range);
}

//  void QOpenGLFunctions_1_5::glDeleteLists(GLuint list, GLsizei range)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glDeleteListsEji(
    QOpenGLFunctions_1_5 *self,
    GLuint list,
    GLsizei range) {
  self->glDeleteLists(list, range);
}

//  void QOpenGLFunctions_1_5::glCallLists(GLsizei n, GLenum type, const
//      GLvoid *lists)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_511glCallListsEijPKv(
    QOpenGLFunctions_1_5 *self,
    GLsizei n,
    GLenum type,
    const GLvoid *lists) {
  self->glCallLists(n, type, lists);
}

//  void QOpenGLFunctions_1_5::glCallList(GLuint list)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_510glCallListEj(
    QOpenGLFunctions_1_5 *self,
    GLuint list) {
  self->glCallList(list);
}

//  void QOpenGLFunctions_1_5::glEndList()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_59glEndListEv(
    QOpenGLFunctions_1_5 *self) {
  self->glEndList();
}

//  void QOpenGLFunctions_1_5::glNewList(GLuint list, GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_59glNewListEjj(
    QOpenGLFunctions_1_5 *self,
    GLuint list,
    GLenum mode) {
  self->glNewList(list, mode);
}

//  void QOpenGLFunctions_1_5::glPushClientAttrib(GLbitfield mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_518glPushClientAttribEj(
    QOpenGLFunctions_1_5 *self,
    GLbitfield mask) {
  self->glPushClientAttrib(mask);
}

//  void QOpenGLFunctions_1_5::glPopClientAttrib()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_517glPopClientAttribEv(
    QOpenGLFunctions_1_5 *self) {
  self->glPopClientAttrib();
}

//  void QOpenGLFunctions_1_5::glPrioritizeTextures(GLsizei n, const GLuint
//      *textures, const GLfloat *priorities)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_520glPrioritizeTexturesEiPKjPKf(
    QOpenGLFunctions_1_5 *self,
    GLsizei n,
    const GLuint *textures,
    const GLfloat *priorities) {
  self->glPrioritizeTextures(n, textures, priorities);
}

//  GLboolean QOpenGLFunctions_1_5::glAreTexturesResident(GLsizei n, const
//      GLuint *textures, GLboolean *residences)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN20QOpenGLFunctions_1_521glAreTexturesResidentEiPKjPh(
    QOpenGLFunctions_1_5 *self,
    GLsizei n,
    const GLuint *textures,
    GLboolean *residences) {
  return self->glAreTexturesResident(n, textures, residences);
}

//  void QOpenGLFunctions_1_5::glVertexPointer(GLint size, GLenum type,
//      GLsizei stride, const GLvoid *pointer)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_515glVertexPointerEijiPKv(
    QOpenGLFunctions_1_5 *self,
    GLint size,
    GLenum type,
    GLsizei stride,
    const GLvoid *pointer) {
  self->glVertexPointer(size, type, stride, pointer);
}

//  void QOpenGLFunctions_1_5::glTexCoordPointer(GLint size, GLenum type,
//      GLsizei stride, const GLvoid *pointer)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_517glTexCoordPointerEijiPKv(
    QOpenGLFunctions_1_5 *self,
    GLint size,
    GLenum type,
    GLsizei stride,
    const GLvoid *pointer) {
  self->glTexCoordPointer(size, type, stride, pointer);
}

//  void QOpenGLFunctions_1_5::glNormalPointer(GLenum type, GLsizei stride,
//      const GLvoid *pointer)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_515glNormalPointerEjiPKv(
    QOpenGLFunctions_1_5 *self,
    GLenum type,
    GLsizei stride,
    const GLvoid *pointer) {
  self->glNormalPointer(type, stride, pointer);
}

//  void QOpenGLFunctions_1_5::glInterleavedArrays(GLenum format, GLsizei
//      stride, const GLvoid *pointer)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_519glInterleavedArraysEjiPKv(
    QOpenGLFunctions_1_5 *self,
    GLenum format,
    GLsizei stride,
    const GLvoid *pointer) {
  self->glInterleavedArrays(format, stride, pointer);
}

//  void QOpenGLFunctions_1_5::glIndexPointer(GLenum type, GLsizei stride,
//      const GLvoid *pointer)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_514glIndexPointerEjiPKv(
    QOpenGLFunctions_1_5 *self,
    GLenum type,
    GLsizei stride,
    const GLvoid *pointer) {
  self->glIndexPointer(type, stride, pointer);
}

//  void QOpenGLFunctions_1_5::glEnableClientState(GLenum array)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_519glEnableClientStateEj(
    QOpenGLFunctions_1_5 *self,
    GLenum array) {
  self->glEnableClientState(array);
}

//  void QOpenGLFunctions_1_5::glEdgeFlagPointer(GLsizei stride, const GLvoid
//      *pointer)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_517glEdgeFlagPointerEiPKv(
    QOpenGLFunctions_1_5 *self,
    GLsizei stride,
    const GLvoid *pointer) {
  self->glEdgeFlagPointer(stride, pointer);
}

//  void QOpenGLFunctions_1_5::glDisableClientState(GLenum array)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_520glDisableClientStateEj(
    QOpenGLFunctions_1_5 *self,
    GLenum array) {
  self->glDisableClientState(array);
}

//  void QOpenGLFunctions_1_5::glColorPointer(GLint size, GLenum type,
//      GLsizei stride, const GLvoid *pointer)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_514glColorPointerEijiPKv(
    QOpenGLFunctions_1_5 *self,
    GLint size,
    GLenum type,
    GLsizei stride,
    const GLvoid *pointer) {
  self->glColorPointer(size, type, stride, pointer);
}

//  void QOpenGLFunctions_1_5::glArrayElement(GLint i)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_514glArrayElementEi(
    QOpenGLFunctions_1_5 *self,
    GLint i) {
  self->glArrayElement(i);
}

//  void QOpenGLFunctions_1_5::glResetMinmax(GLenum target)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glResetMinmaxEj(
    QOpenGLFunctions_1_5 *self,
    GLenum target) {
  self->glResetMinmax(target);
}

//  void QOpenGLFunctions_1_5::glResetHistogram(GLenum target)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_516glResetHistogramEj(
    QOpenGLFunctions_1_5 *self,
    GLenum target) {
  self->glResetHistogram(target);
}

//  void QOpenGLFunctions_1_5::glMinmax(GLenum target, GLenum internalformat,
//      GLboolean sink)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_58glMinmaxEjjh(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLenum internalformat,
    GLboolean sink) {
  self->glMinmax(target, internalformat, sink);
}

//  void QOpenGLFunctions_1_5::glHistogram(GLenum target, GLsizei width,
//      GLenum internalformat, GLboolean sink)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_511glHistogramEjijh(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLsizei width,
    GLenum internalformat,
    GLboolean sink) {
  self->glHistogram(target, width, internalformat, sink);
}

//  void QOpenGLFunctions_1_5::glGetMinmaxParameteriv(GLenum target, GLenum
//      pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_522glGetMinmaxParameterivEjjPi(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLenum pname,
    GLint *params) {
  self->glGetMinmaxParameteriv(target, pname, params);
}

//  void QOpenGLFunctions_1_5::glGetMinmaxParameterfv(GLenum target, GLenum
//      pname, GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_522glGetMinmaxParameterfvEjjPf(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLenum pname,
    GLfloat *params) {
  self->glGetMinmaxParameterfv(target, pname, params);
}

//  void QOpenGLFunctions_1_5::glGetMinmax(GLenum target, GLboolean reset,
//      GLenum format, GLenum type, GLvoid *values)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_511glGetMinmaxEjhjjPv(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLboolean reset,
    GLenum format,
    GLenum type,
    GLvoid *values) {
  self->glGetMinmax(target, reset, format, type, values);
}

//  void QOpenGLFunctions_1_5::glGetHistogramParameteriv(GLenum target,
//      GLenum pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_525glGetHistogramParameterivEjjPi(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLenum pname,
    GLint *params) {
  self->glGetHistogramParameteriv(target, pname, params);
}

//  void QOpenGLFunctions_1_5::glGetHistogramParameterfv(GLenum target,
//      GLenum pname, GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_525glGetHistogramParameterfvEjjPf(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLenum pname,
    GLfloat *params) {
  self->glGetHistogramParameterfv(target, pname, params);
}

//  void QOpenGLFunctions_1_5::glGetHistogram(GLenum target, GLboolean reset,
//      GLenum format, GLenum type, GLvoid *values)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_514glGetHistogramEjhjjPv(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLboolean reset,
    GLenum format,
    GLenum type,
    GLvoid *values) {
  self->glGetHistogram(target, reset, format, type, values);
}

//  void QOpenGLFunctions_1_5::glSeparableFilter2D(GLenum target, GLenum
//      internalformat, GLsizei width, GLsizei height, GLenum format, GLenum
//      type, const GLvoid *row, const GLvoid *column)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_519glSeparableFilter2DEjjiijjPKvS1_(
    QOpenGLFunctions_1_5 *self,
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

//  void QOpenGLFunctions_1_5::glGetSeparableFilter(GLenum target, GLenum
//      format, GLenum type, GLvoid *row, GLvoid *column, GLvoid *span)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_520glGetSeparableFilterEjjjPvS0_S0_(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLenum format,
    GLenum type,
    GLvoid *row,
    GLvoid *column,
    GLvoid *span) {
  self->glGetSeparableFilter(target, format, type, row, column, span);
}

//  void QOpenGLFunctions_1_5::glGetConvolutionParameteriv(GLenum target,
//      GLenum pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_527glGetConvolutionParameterivEjjPi(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLenum pname,
    GLint *params) {
  self->glGetConvolutionParameteriv(target, pname, params);
}

//  void QOpenGLFunctions_1_5::glGetConvolutionParameterfv(GLenum target,
//      GLenum pname, GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_527glGetConvolutionParameterfvEjjPf(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLenum pname,
    GLfloat *params) {
  self->glGetConvolutionParameterfv(target, pname, params);
}

//  void QOpenGLFunctions_1_5::glGetConvolutionFilter(GLenum target, GLenum
//      format, GLenum type, GLvoid *image)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_522glGetConvolutionFilterEjjjPv(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLenum format,
    GLenum type,
    GLvoid *image) {
  self->glGetConvolutionFilter(target, format, type, image);
}

//  void QOpenGLFunctions_1_5::glCopyConvolutionFilter2D(GLenum target,
//      GLenum internalformat, GLint x, GLint y, GLsizei width, GLsizei
//      height)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_525glCopyConvolutionFilter2DEjjiiii(
    QOpenGLFunctions_1_5 *self,
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

//  void QOpenGLFunctions_1_5::glCopyConvolutionFilter1D(GLenum target,
//      GLenum internalformat, GLint x, GLint y, GLsizei width)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_525glCopyConvolutionFilter1DEjjiii(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLenum internalformat,
    GLint x,
    GLint y,
    GLsizei width) {
  self->glCopyConvolutionFilter1D(target, internalformat, x, y, width);
}

//  void QOpenGLFunctions_1_5::glConvolutionParameteriv(GLenum target, GLenum
//      pname, const GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_524glConvolutionParameterivEjjPKi(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLenum pname,
    const GLint *params) {
  self->glConvolutionParameteriv(target, pname, params);
}

//  void QOpenGLFunctions_1_5::glConvolutionParameteri(GLenum target, GLenum
//      pname, GLint params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_523glConvolutionParameteriEjji(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLenum pname,
    GLint params) {
  self->glConvolutionParameteri(target, pname, params);
}

//  void QOpenGLFunctions_1_5::glConvolutionParameterfv(GLenum target, GLenum
//      pname, const GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_524glConvolutionParameterfvEjjPKf(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLenum pname,
    const GLfloat *params) {
  self->glConvolutionParameterfv(target, pname, params);
}

//  void QOpenGLFunctions_1_5::glConvolutionParameterf(GLenum target, GLenum
//      pname, GLfloat params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_523glConvolutionParameterfEjjf(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLenum pname,
    GLfloat params) {
  self->glConvolutionParameterf(target, pname, params);
}

//  void QOpenGLFunctions_1_5::glConvolutionFilter2D(GLenum target, GLenum
//      internalformat, GLsizei width, GLsizei height, GLenum format, GLenum
//      type, const GLvoid *image)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_521glConvolutionFilter2DEjjiijjPKv(
    QOpenGLFunctions_1_5 *self,
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

//  void QOpenGLFunctions_1_5::glConvolutionFilter1D(GLenum target, GLenum
//      internalformat, GLsizei width, GLenum format, GLenum type, const
//      GLvoid *image)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_521glConvolutionFilter1DEjjijjPKv(
    QOpenGLFunctions_1_5 *self,
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

//  void QOpenGLFunctions_1_5::glCopyColorSubTable(GLenum target, GLsizei
//      start, GLint x, GLint y, GLsizei width)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_519glCopyColorSubTableEjiiii(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLsizei start,
    GLint x,
    GLint y,
    GLsizei width) {
  self->glCopyColorSubTable(target, start, x, y, width);
}

//  void QOpenGLFunctions_1_5::glColorSubTable(GLenum target, GLsizei start,
//      GLsizei count, GLenum format, GLenum type, const GLvoid *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_515glColorSubTableEjiijjPKv(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLsizei start,
    GLsizei count,
    GLenum format,
    GLenum type,
    const GLvoid *data) {
  self->glColorSubTable(target, start, count, format, type, data);
}

//  void QOpenGLFunctions_1_5::glGetColorTableParameteriv(GLenum target,
//      GLenum pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_526glGetColorTableParameterivEjjPi(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLenum pname,
    GLint *params) {
  self->glGetColorTableParameteriv(target, pname, params);
}

//  void QOpenGLFunctions_1_5::glGetColorTableParameterfv(GLenum target,
//      GLenum pname, GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_526glGetColorTableParameterfvEjjPf(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLenum pname,
    GLfloat *params) {
  self->glGetColorTableParameterfv(target, pname, params);
}

//  void QOpenGLFunctions_1_5::glGetColorTable(GLenum target, GLenum format,
//      GLenum type, GLvoid *table)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_515glGetColorTableEjjjPv(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLenum format,
    GLenum type,
    GLvoid *table) {
  self->glGetColorTable(target, format, type, table);
}

//  void QOpenGLFunctions_1_5::glCopyColorTable(GLenum target, GLenum
//      internalformat, GLint x, GLint y, GLsizei width)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_516glCopyColorTableEjjiii(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLenum internalformat,
    GLint x,
    GLint y,
    GLsizei width) {
  self->glCopyColorTable(target, internalformat, x, y, width);
}

//  void QOpenGLFunctions_1_5::glColorTableParameteriv(GLenum target, GLenum
//      pname, const GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_523glColorTableParameterivEjjPKi(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLenum pname,
    const GLint *params) {
  self->glColorTableParameteriv(target, pname, params);
}

//  void QOpenGLFunctions_1_5::glColorTableParameterfv(GLenum target, GLenum
//      pname, const GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_523glColorTableParameterfvEjjPKf(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLenum pname,
    const GLfloat *params) {
  self->glColorTableParameterfv(target, pname, params);
}

//  void QOpenGLFunctions_1_5::glColorTable(GLenum target, GLenum
//      internalformat, GLsizei width, GLenum format, GLenum type, const
//      GLvoid *table)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_512glColorTableEjjijjPKv(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLenum internalformat,
    GLsizei width,
    GLenum format,
    GLenum type,
    const GLvoid *table) {
  self->glColorTable(target, internalformat, width, format, type, table);
}

//  void QOpenGLFunctions_1_5::glMultTransposeMatrixd(const GLdouble *m)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_522glMultTransposeMatrixdEPKd(
    QOpenGLFunctions_1_5 *self,
    const GLdouble *m) {
  self->glMultTransposeMatrixd(m);
}

//  void QOpenGLFunctions_1_5::glMultTransposeMatrixf(const GLfloat *m)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_522glMultTransposeMatrixfEPKf(
    QOpenGLFunctions_1_5 *self,
    const GLfloat *m) {
  self->glMultTransposeMatrixf(m);
}

//  void QOpenGLFunctions_1_5::glLoadTransposeMatrixd(const GLdouble *m)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_522glLoadTransposeMatrixdEPKd(
    QOpenGLFunctions_1_5 *self,
    const GLdouble *m) {
  self->glLoadTransposeMatrixd(m);
}

//  void QOpenGLFunctions_1_5::glLoadTransposeMatrixf(const GLfloat *m)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_522glLoadTransposeMatrixfEPKf(
    QOpenGLFunctions_1_5 *self,
    const GLfloat *m) {
  self->glLoadTransposeMatrixf(m);
}

//  void QOpenGLFunctions_1_5::glMultiTexCoord4sv(GLenum target, const
//      GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_518glMultiTexCoord4svEjPKs(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    const GLshort *v) {
  self->glMultiTexCoord4sv(target, v);
}

//  void QOpenGLFunctions_1_5::glMultiTexCoord4s(GLenum target, GLshort s,
//      GLshort t, GLshort r, GLshort q)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_517glMultiTexCoord4sEjssss(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLshort s,
    GLshort t,
    GLshort r,
    GLshort q) {
  self->glMultiTexCoord4s(target, s, t, r, q);
}

//  void QOpenGLFunctions_1_5::glMultiTexCoord4iv(GLenum target, const GLint
//      *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_518glMultiTexCoord4ivEjPKi(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    const GLint *v) {
  self->glMultiTexCoord4iv(target, v);
}

//  void QOpenGLFunctions_1_5::glMultiTexCoord4i(GLenum target, GLint s,
//      GLint t, GLint r, GLint q)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_517glMultiTexCoord4iEjiiii(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLint s,
    GLint t,
    GLint r,
    GLint q) {
  self->glMultiTexCoord4i(target, s, t, r, q);
}

//  void QOpenGLFunctions_1_5::glMultiTexCoord4fv(GLenum target, const
//      GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_518glMultiTexCoord4fvEjPKf(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    const GLfloat *v) {
  self->glMultiTexCoord4fv(target, v);
}

//  void QOpenGLFunctions_1_5::glMultiTexCoord4f(GLenum target, GLfloat s,
//      GLfloat t, GLfloat r, GLfloat q)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_517glMultiTexCoord4fEjffff(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLfloat s,
    GLfloat t,
    GLfloat r,
    GLfloat q) {
  self->glMultiTexCoord4f(target, s, t, r, q);
}

//  void QOpenGLFunctions_1_5::glMultiTexCoord4dv(GLenum target, const
//      GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_518glMultiTexCoord4dvEjPKd(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    const GLdouble *v) {
  self->glMultiTexCoord4dv(target, v);
}

//  void QOpenGLFunctions_1_5::glMultiTexCoord4d(GLenum target, GLdouble s,
//      GLdouble t, GLdouble r, GLdouble q)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_517glMultiTexCoord4dEjdddd(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLdouble s,
    GLdouble t,
    GLdouble r,
    GLdouble q) {
  self->glMultiTexCoord4d(target, s, t, r, q);
}

//  void QOpenGLFunctions_1_5::glMultiTexCoord3sv(GLenum target, const
//      GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_518glMultiTexCoord3svEjPKs(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    const GLshort *v) {
  self->glMultiTexCoord3sv(target, v);
}

//  void QOpenGLFunctions_1_5::glMultiTexCoord3s(GLenum target, GLshort s,
//      GLshort t, GLshort r)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_517glMultiTexCoord3sEjsss(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLshort s,
    GLshort t,
    GLshort r) {
  self->glMultiTexCoord3s(target, s, t, r);
}

//  void QOpenGLFunctions_1_5::glMultiTexCoord3iv(GLenum target, const GLint
//      *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_518glMultiTexCoord3ivEjPKi(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    const GLint *v) {
  self->glMultiTexCoord3iv(target, v);
}

//  void QOpenGLFunctions_1_5::glMultiTexCoord3i(GLenum target, GLint s,
//      GLint t, GLint r)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_517glMultiTexCoord3iEjiii(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLint s,
    GLint t,
    GLint r) {
  self->glMultiTexCoord3i(target, s, t, r);
}

//  void QOpenGLFunctions_1_5::glMultiTexCoord3fv(GLenum target, const
//      GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_518glMultiTexCoord3fvEjPKf(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    const GLfloat *v) {
  self->glMultiTexCoord3fv(target, v);
}

//  void QOpenGLFunctions_1_5::glMultiTexCoord3f(GLenum target, GLfloat s,
//      GLfloat t, GLfloat r)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_517glMultiTexCoord3fEjfff(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLfloat s,
    GLfloat t,
    GLfloat r) {
  self->glMultiTexCoord3f(target, s, t, r);
}

//  void QOpenGLFunctions_1_5::glMultiTexCoord3dv(GLenum target, const
//      GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_518glMultiTexCoord3dvEjPKd(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    const GLdouble *v) {
  self->glMultiTexCoord3dv(target, v);
}

//  void QOpenGLFunctions_1_5::glMultiTexCoord3d(GLenum target, GLdouble s,
//      GLdouble t, GLdouble r)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_517glMultiTexCoord3dEjddd(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLdouble s,
    GLdouble t,
    GLdouble r) {
  self->glMultiTexCoord3d(target, s, t, r);
}

//  void QOpenGLFunctions_1_5::glMultiTexCoord2sv(GLenum target, const
//      GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_518glMultiTexCoord2svEjPKs(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    const GLshort *v) {
  self->glMultiTexCoord2sv(target, v);
}

//  void QOpenGLFunctions_1_5::glMultiTexCoord2s(GLenum target, GLshort s,
//      GLshort t)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_517glMultiTexCoord2sEjss(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLshort s,
    GLshort t) {
  self->glMultiTexCoord2s(target, s, t);
}

//  void QOpenGLFunctions_1_5::glMultiTexCoord2iv(GLenum target, const GLint
//      *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_518glMultiTexCoord2ivEjPKi(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    const GLint *v) {
  self->glMultiTexCoord2iv(target, v);
}

//  void QOpenGLFunctions_1_5::glMultiTexCoord2i(GLenum target, GLint s,
//      GLint t)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_517glMultiTexCoord2iEjii(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLint s,
    GLint t) {
  self->glMultiTexCoord2i(target, s, t);
}

//  void QOpenGLFunctions_1_5::glMultiTexCoord2fv(GLenum target, const
//      GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_518glMultiTexCoord2fvEjPKf(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    const GLfloat *v) {
  self->glMultiTexCoord2fv(target, v);
}

//  void QOpenGLFunctions_1_5::glMultiTexCoord2f(GLenum target, GLfloat s,
//      GLfloat t)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_517glMultiTexCoord2fEjff(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLfloat s,
    GLfloat t) {
  self->glMultiTexCoord2f(target, s, t);
}

//  void QOpenGLFunctions_1_5::glMultiTexCoord2dv(GLenum target, const
//      GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_518glMultiTexCoord2dvEjPKd(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    const GLdouble *v) {
  self->glMultiTexCoord2dv(target, v);
}

//  void QOpenGLFunctions_1_5::glMultiTexCoord2d(GLenum target, GLdouble s,
//      GLdouble t)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_517glMultiTexCoord2dEjdd(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLdouble s,
    GLdouble t) {
  self->glMultiTexCoord2d(target, s, t);
}

//  void QOpenGLFunctions_1_5::glMultiTexCoord1sv(GLenum target, const
//      GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_518glMultiTexCoord1svEjPKs(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    const GLshort *v) {
  self->glMultiTexCoord1sv(target, v);
}

//  void QOpenGLFunctions_1_5::glMultiTexCoord1s(GLenum target, GLshort s)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_517glMultiTexCoord1sEjs(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLshort s) {
  self->glMultiTexCoord1s(target, s);
}

//  void QOpenGLFunctions_1_5::glMultiTexCoord1iv(GLenum target, const GLint
//      *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_518glMultiTexCoord1ivEjPKi(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    const GLint *v) {
  self->glMultiTexCoord1iv(target, v);
}

//  void QOpenGLFunctions_1_5::glMultiTexCoord1i(GLenum target, GLint s)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_517glMultiTexCoord1iEji(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLint s) {
  self->glMultiTexCoord1i(target, s);
}

//  void QOpenGLFunctions_1_5::glMultiTexCoord1fv(GLenum target, const
//      GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_518glMultiTexCoord1fvEjPKf(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    const GLfloat *v) {
  self->glMultiTexCoord1fv(target, v);
}

//  void QOpenGLFunctions_1_5::glMultiTexCoord1f(GLenum target, GLfloat s)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_517glMultiTexCoord1fEjf(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLfloat s) {
  self->glMultiTexCoord1f(target, s);
}

//  void QOpenGLFunctions_1_5::glMultiTexCoord1dv(GLenum target, const
//      GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_518glMultiTexCoord1dvEjPKd(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    const GLdouble *v) {
  self->glMultiTexCoord1dv(target, v);
}

//  void QOpenGLFunctions_1_5::glMultiTexCoord1d(GLenum target, GLdouble s)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_517glMultiTexCoord1dEjd(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLdouble s) {
  self->glMultiTexCoord1d(target, s);
}

//  void QOpenGLFunctions_1_5::glClientActiveTexture(GLenum texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_521glClientActiveTextureEj(
    QOpenGLFunctions_1_5 *self,
    GLenum texture) {
  self->glClientActiveTexture(texture);
}

//  void QOpenGLFunctions_1_5::glWindowPos3sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_514glWindowPos3svEPKs(
    QOpenGLFunctions_1_5 *self,
    const GLshort *v) {
  self->glWindowPos3sv(v);
}

//  void QOpenGLFunctions_1_5::glWindowPos3s(GLshort x, GLshort y, GLshort z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glWindowPos3sEsss(
    QOpenGLFunctions_1_5 *self,
    GLshort x,
    GLshort y,
    GLshort z) {
  self->glWindowPos3s(x, y, z);
}

//  void QOpenGLFunctions_1_5::glWindowPos3iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_514glWindowPos3ivEPKi(
    QOpenGLFunctions_1_5 *self,
    const GLint *v) {
  self->glWindowPos3iv(v);
}

//  void QOpenGLFunctions_1_5::glWindowPos3i(GLint x, GLint y, GLint z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glWindowPos3iEiii(
    QOpenGLFunctions_1_5 *self,
    GLint x,
    GLint y,
    GLint z) {
  self->glWindowPos3i(x, y, z);
}

//  void QOpenGLFunctions_1_5::glWindowPos3fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_514glWindowPos3fvEPKf(
    QOpenGLFunctions_1_5 *self,
    const GLfloat *v) {
  self->glWindowPos3fv(v);
}

//  void QOpenGLFunctions_1_5::glWindowPos3f(GLfloat x, GLfloat y, GLfloat z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glWindowPos3fEfff(
    QOpenGLFunctions_1_5 *self,
    GLfloat x,
    GLfloat y,
    GLfloat z) {
  self->glWindowPos3f(x, y, z);
}

//  void QOpenGLFunctions_1_5::glWindowPos3dv(const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_514glWindowPos3dvEPKd(
    QOpenGLFunctions_1_5 *self,
    const GLdouble *v) {
  self->glWindowPos3dv(v);
}

//  void QOpenGLFunctions_1_5::glWindowPos3d(GLdouble x, GLdouble y, GLdouble
//      z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glWindowPos3dEddd(
    QOpenGLFunctions_1_5 *self,
    GLdouble x,
    GLdouble y,
    GLdouble z) {
  self->glWindowPos3d(x, y, z);
}

//  void QOpenGLFunctions_1_5::glWindowPos2sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_514glWindowPos2svEPKs(
    QOpenGLFunctions_1_5 *self,
    const GLshort *v) {
  self->glWindowPos2sv(v);
}

//  void QOpenGLFunctions_1_5::glWindowPos2s(GLshort x, GLshort y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glWindowPos2sEss(
    QOpenGLFunctions_1_5 *self,
    GLshort x,
    GLshort y) {
  self->glWindowPos2s(x, y);
}

//  void QOpenGLFunctions_1_5::glWindowPos2iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_514glWindowPos2ivEPKi(
    QOpenGLFunctions_1_5 *self,
    const GLint *v) {
  self->glWindowPos2iv(v);
}

//  void QOpenGLFunctions_1_5::glWindowPos2i(GLint x, GLint y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glWindowPos2iEii(
    QOpenGLFunctions_1_5 *self,
    GLint x,
    GLint y) {
  self->glWindowPos2i(x, y);
}

//  void QOpenGLFunctions_1_5::glWindowPos2fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_514glWindowPos2fvEPKf(
    QOpenGLFunctions_1_5 *self,
    const GLfloat *v) {
  self->glWindowPos2fv(v);
}

//  void QOpenGLFunctions_1_5::glWindowPos2f(GLfloat x, GLfloat y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glWindowPos2fEff(
    QOpenGLFunctions_1_5 *self,
    GLfloat x,
    GLfloat y) {
  self->glWindowPos2f(x, y);
}

//  void QOpenGLFunctions_1_5::glWindowPos2dv(const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_514glWindowPos2dvEPKd(
    QOpenGLFunctions_1_5 *self,
    const GLdouble *v) {
  self->glWindowPos2dv(v);
}

//  void QOpenGLFunctions_1_5::glWindowPos2d(GLdouble x, GLdouble y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glWindowPos2dEdd(
    QOpenGLFunctions_1_5 *self,
    GLdouble x,
    GLdouble y) {
  self->glWindowPos2d(x, y);
}

//  void QOpenGLFunctions_1_5::glSecondaryColorPointer(GLint size, GLenum
//      type, GLsizei stride, const GLvoid *pointer)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_523glSecondaryColorPointerEijiPKv(
    QOpenGLFunctions_1_5 *self,
    GLint size,
    GLenum type,
    GLsizei stride,
    const GLvoid *pointer) {
  self->glSecondaryColorPointer(size, type, stride, pointer);
}

//  void QOpenGLFunctions_1_5::glSecondaryColor3usv(const GLushort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_520glSecondaryColor3usvEPKt(
    QOpenGLFunctions_1_5 *self,
    const GLushort *v) {
  self->glSecondaryColor3usv(v);
}

//  void QOpenGLFunctions_1_5::glSecondaryColor3us(GLushort red, GLushort
//      green, GLushort blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_519glSecondaryColor3usEttt(
    QOpenGLFunctions_1_5 *self,
    GLushort red,
    GLushort green,
    GLushort blue) {
  self->glSecondaryColor3us(red, green, blue);
}

//  void QOpenGLFunctions_1_5::glSecondaryColor3uiv(const GLuint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_520glSecondaryColor3uivEPKj(
    QOpenGLFunctions_1_5 *self,
    const GLuint *v) {
  self->glSecondaryColor3uiv(v);
}

//  void QOpenGLFunctions_1_5::glSecondaryColor3ui(GLuint red, GLuint green,
//      GLuint blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_519glSecondaryColor3uiEjjj(
    QOpenGLFunctions_1_5 *self,
    GLuint red,
    GLuint green,
    GLuint blue) {
  self->glSecondaryColor3ui(red, green, blue);
}

//  void QOpenGLFunctions_1_5::glSecondaryColor3ubv(const GLubyte *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_520glSecondaryColor3ubvEPKh(
    QOpenGLFunctions_1_5 *self,
    const GLubyte *v) {
  self->glSecondaryColor3ubv(v);
}

//  void QOpenGLFunctions_1_5::glSecondaryColor3ub(GLubyte red, GLubyte
//      green, GLubyte blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_519glSecondaryColor3ubEhhh(
    QOpenGLFunctions_1_5 *self,
    GLubyte red,
    GLubyte green,
    GLubyte blue) {
  self->glSecondaryColor3ub(red, green, blue);
}

//  void QOpenGLFunctions_1_5::glSecondaryColor3sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_519glSecondaryColor3svEPKs(
    QOpenGLFunctions_1_5 *self,
    const GLshort *v) {
  self->glSecondaryColor3sv(v);
}

//  void QOpenGLFunctions_1_5::glSecondaryColor3s(GLshort red, GLshort green,
//      GLshort blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_518glSecondaryColor3sEsss(
    QOpenGLFunctions_1_5 *self,
    GLshort red,
    GLshort green,
    GLshort blue) {
  self->glSecondaryColor3s(red, green, blue);
}

//  void QOpenGLFunctions_1_5::glSecondaryColor3iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_519glSecondaryColor3ivEPKi(
    QOpenGLFunctions_1_5 *self,
    const GLint *v) {
  self->glSecondaryColor3iv(v);
}

//  void QOpenGLFunctions_1_5::glSecondaryColor3i(GLint red, GLint green,
//      GLint blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_518glSecondaryColor3iEiii(
    QOpenGLFunctions_1_5 *self,
    GLint red,
    GLint green,
    GLint blue) {
  self->glSecondaryColor3i(red, green, blue);
}

//  void QOpenGLFunctions_1_5::glSecondaryColor3fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_519glSecondaryColor3fvEPKf(
    QOpenGLFunctions_1_5 *self,
    const GLfloat *v) {
  self->glSecondaryColor3fv(v);
}

//  void QOpenGLFunctions_1_5::glSecondaryColor3f(GLfloat red, GLfloat green,
//      GLfloat blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_518glSecondaryColor3fEfff(
    QOpenGLFunctions_1_5 *self,
    GLfloat red,
    GLfloat green,
    GLfloat blue) {
  self->glSecondaryColor3f(red, green, blue);
}

//  void QOpenGLFunctions_1_5::glSecondaryColor3dv(const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_519glSecondaryColor3dvEPKd(
    QOpenGLFunctions_1_5 *self,
    const GLdouble *v) {
  self->glSecondaryColor3dv(v);
}

//  void QOpenGLFunctions_1_5::glSecondaryColor3d(GLdouble red, GLdouble
//      green, GLdouble blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_518glSecondaryColor3dEddd(
    QOpenGLFunctions_1_5 *self,
    GLdouble red,
    GLdouble green,
    GLdouble blue) {
  self->glSecondaryColor3d(red, green, blue);
}

//  void QOpenGLFunctions_1_5::glSecondaryColor3bv(const GLbyte *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_519glSecondaryColor3bvEPKa(
    QOpenGLFunctions_1_5 *self,
    const GLbyte *v) {
  self->glSecondaryColor3bv(v);
}

//  void QOpenGLFunctions_1_5::glSecondaryColor3b(GLbyte red, GLbyte green,
//      GLbyte blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_518glSecondaryColor3bEaaa(
    QOpenGLFunctions_1_5 *self,
    GLbyte red,
    GLbyte green,
    GLbyte blue) {
  self->glSecondaryColor3b(red, green, blue);
}

//  void QOpenGLFunctions_1_5::glFogCoordPointer(GLenum type, GLsizei stride,
//      const GLvoid *pointer)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_517glFogCoordPointerEjiPKv(
    QOpenGLFunctions_1_5 *self,
    GLenum type,
    GLsizei stride,
    const GLvoid *pointer) {
  self->glFogCoordPointer(type, stride, pointer);
}

//  void QOpenGLFunctions_1_5::glFogCoorddv(const GLdouble *coord)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_512glFogCoorddvEPKd(
    QOpenGLFunctions_1_5 *self,
    const GLdouble *coord) {
  self->glFogCoorddv(coord);
}

//  void QOpenGLFunctions_1_5::glFogCoordd(GLdouble coord)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_511glFogCoorddEd(
    QOpenGLFunctions_1_5 *self,
    GLdouble coord) {
  self->glFogCoordd(coord);
}

//  void QOpenGLFunctions_1_5::glFogCoordfv(const GLfloat *coord)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_512glFogCoordfvEPKf(
    QOpenGLFunctions_1_5 *self,
    const GLfloat *coord) {
  self->glFogCoordfv(coord);
}

//  void QOpenGLFunctions_1_5::glFogCoordf(GLfloat coord)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_511glFogCoordfEf(
    QOpenGLFunctions_1_5 *self,
    GLfloat coord) {
  self->glFogCoordf(coord);
}

//  bool QOpenGLFunctions_1_5::isContextCompatible(QOpenGLContext *context)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QOpenGLFunctions_1_519isContextCompatibleEP14QOpenGLContext(
    QOpenGLContext *context) {
  return QOpenGLFunctions_1_5::isContextCompatible(context);
}

//  QOpenGLVersionProfile QOpenGLFunctions_1_5::versionProfile()
extern "C" Q_DECL_EXPORT
QOpenGLVersionProfile *ritual_ZN20QOpenGLFunctions_1_514versionProfileEv() {
  return new QOpenGLVersionProfile(QOpenGLFunctions_1_5::versionProfile());
}

//  a Python function taken by a CuteQOpenGLFunctions_1_5, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QOpenGLFunctions_1_5(
    QOpenGLFunctions_1_5 *self,
    const char *key,
    void *call) {
  return static_cast<CuteQOpenGLFunctions_1_5 *>(self)->take(key, call);
}

//  bool QOpenGLFunctions_1_5::initializeOpenGLFunctions()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN20QOpenGLFunctions_1_525initializeOpenGLFunctionsEv(
    QOpenGLFunctions_1_5 *self) {
  return self->QOpenGLFunctions_1_5::initializeOpenGLFunctions();
}

#endif  // !defined(QT_NO_OPENGL) && !QT_CONFIG(opengles2)
#endif  // !QT_CONFIG(opengles2)
