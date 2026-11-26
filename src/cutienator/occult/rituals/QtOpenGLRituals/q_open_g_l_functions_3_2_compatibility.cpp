//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/qopenglfunctions_3_2_compatibility.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtOpenGL/qtopenglglobal.h>
#if !QT_CONFIG(opengles2)
#if !defined(QT_NO_OPENGL) && !QT_CONFIG(opengles2)
#include <QtOpenGL/QtOpenGL>
#include <QtOpenGL/qopenglfunctions_3_2_compatibility.h>
#include <QtOpenGL/qopenglversionprofile.h>
#include <cstring>

//  A QOpenGLFunctions_3_2_Compatibility that Python can take functions over in. Every QOpenGLFunctions_3_2_Compatibility
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL) && !QT_CONFIG(opengles2)
typedef bool (*CuteQOpenGLFunctions_3_2_CompatibilityCall0)(const void *, int *);
#endif  // !defined(QT_NO_OPENGL) && !QT_CONFIG(opengles2)
#endif  // !defined(QT_NO_OPENGL)
class CuteQOpenGLFunctions_3_2_Compatibility : public QOpenGLFunctions_3_2_Compatibility {
public:
  using QOpenGLFunctions_3_2_Compatibility::QOpenGLFunctions_3_2_Compatibility;
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
  //  bool QOpenGLFunctions_3_2_Compatibility::initializeOpenGLFunctions()
  bool initializeOpenGLFunctions() override {
    if (taken[0]) {
      int handled = 0;
      CuteQOpenGLFunctions_3_2_CompatibilityCall0 call = reinterpret_cast<CuteQOpenGLFunctions_3_2_CompatibilityCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QOpenGLFunctions_3_2_Compatibility::initializeOpenGLFunctions();
  }
#endif  // !defined(QT_NO_OPENGL) && !QT_CONFIG(opengles2)
#endif  // !defined(QT_NO_OPENGL)
};

//  QOpenGLFunctions_3_2_Compatibility::QOpenGLFunctions_3_2_Compatibility()
extern "C" Q_DECL_EXPORT
QOpenGLFunctions_3_2_Compatibility *ritual_ZN34QOpenGLFunctions_3_2_CompatibilityC1Ev() {
  return new CuteQOpenGLFunctions_3_2_Compatibility();
}

//  QOpenGLFunctions_3_2_Compatibility::~QOpenGLFunctions_3_2_Compatibility()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_CompatibilityD1Ev(
    QOpenGLFunctions_3_2_Compatibility *self) {
  delete self;
}

//  bool QOpenGLFunctions_3_2_Compatibility::initializeOpenGLFunctions()
extern "C" Q_DECL_EXPORT
bool ritual_ZN34QOpenGLFunctions_3_2_Compatibility25initializeOpenGLFunctionsEv(
    QOpenGLFunctions_3_2_Compatibility *self) {
  return self->initializeOpenGLFunctions();
}

//  void QOpenGLFunctions_3_2_Compatibility::glViewport(GLint x, GLint y,
//      GLsizei width, GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility10glViewportEiiii(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLint x,
    GLint y,
    GLsizei width,
    GLsizei height) {
  self->glViewport(x, y, width, height);
}

//  void QOpenGLFunctions_3_2_Compatibility::glDepthRange(GLdouble nearVal,
//      GLdouble farVal)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glDepthRangeEdd(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLdouble nearVal,
    GLdouble farVal) {
  self->glDepthRange(nearVal, farVal);
}

//  GLboolean QOpenGLFunctions_3_2_Compatibility::glIsEnabled(GLenum cap)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN34QOpenGLFunctions_3_2_Compatibility11glIsEnabledEj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum cap) {
  return self->glIsEnabled(cap);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGetTexLevelParameteriv(GLenum
//      target, GLint level, GLenum pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility24glGetTexLevelParameterivEjijPi(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLint level,
    GLenum pname,
    GLint *params) {
  self->glGetTexLevelParameteriv(target, level, pname, params);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGetTexLevelParameterfv(GLenum
//      target, GLint level, GLenum pname, GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility24glGetTexLevelParameterfvEjijPf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLint level,
    GLenum pname,
    GLfloat *params) {
  self->glGetTexLevelParameterfv(target, level, pname, params);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGetTexParameteriv(GLenum
//      target, GLenum pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility19glGetTexParameterivEjjPi(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLenum pname,
    GLint *params) {
  self->glGetTexParameteriv(target, pname, params);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGetTexParameterfv(GLenum
//      target, GLenum pname, GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility19glGetTexParameterfvEjjPf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLenum pname,
    GLfloat *params) {
  self->glGetTexParameterfv(target, pname, params);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGetTexImage(GLenum target,
//      GLint level, GLenum format, GLenum type, GLvoid *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glGetTexImageEjijjPv(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLint level,
    GLenum format,
    GLenum type,
    GLvoid *pixels) {
  self->glGetTexImage(target, level, format, type, pixels);
}

//  const GLubyte *QOpenGLFunctions_3_2_Compatibility::glGetString(GLenum
//      name)
extern "C" Q_DECL_EXPORT
const GLubyte *ritual_ZN34QOpenGLFunctions_3_2_Compatibility11glGetStringEj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum name) {
  return self->glGetString(name);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGetIntegerv(GLenum pname,
//      GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glGetIntegervEjPi(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum pname,
    GLint *params) {
  self->glGetIntegerv(pname, params);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGetFloatv(GLenum pname,
//      GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility11glGetFloatvEjPf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum pname,
    GLfloat *params) {
  self->glGetFloatv(pname, params);
}

//  GLenum QOpenGLFunctions_3_2_Compatibility::glGetError()
extern "C" Q_DECL_EXPORT
GLenum ritual_ZN34QOpenGLFunctions_3_2_Compatibility10glGetErrorEv(
    QOpenGLFunctions_3_2_Compatibility *self) {
  return self->glGetError();
}

//  void QOpenGLFunctions_3_2_Compatibility::glGetDoublev(GLenum pname,
//      GLdouble *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glGetDoublevEjPd(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum pname,
    GLdouble *params) {
  self->glGetDoublev(pname, params);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGetBooleanv(GLenum pname,
//      GLboolean *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glGetBooleanvEjPh(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum pname,
    GLboolean *params) {
  self->glGetBooleanv(pname, params);
}

//  void QOpenGLFunctions_3_2_Compatibility::glReadPixels(GLint x, GLint y,
//      GLsizei width, GLsizei height, GLenum format, GLenum type, GLvoid
//      *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glReadPixelsEiiiijjPv(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLint x,
    GLint y,
    GLsizei width,
    GLsizei height,
    GLenum format,
    GLenum type,
    GLvoid *pixels) {
  self->glReadPixels(x, y, width, height, format, type, pixels);
}

//  void QOpenGLFunctions_3_2_Compatibility::glReadBuffer(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glReadBufferEj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum mode) {
  self->glReadBuffer(mode);
}

//  void QOpenGLFunctions_3_2_Compatibility::glPixelStorei(GLenum pname,
//      GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glPixelStoreiEji(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum pname,
    GLint param) {
  self->glPixelStorei(pname, param);
}

//  void QOpenGLFunctions_3_2_Compatibility::glPixelStoref(GLenum pname,
//      GLfloat param)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glPixelStorefEjf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum pname,
    GLfloat param) {
  self->glPixelStoref(pname, param);
}

//  void QOpenGLFunctions_3_2_Compatibility::glDepthFunc(GLenum func)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility11glDepthFuncEj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum func) {
  self->glDepthFunc(func);
}

//  void QOpenGLFunctions_3_2_Compatibility::glStencilOp(GLenum fail, GLenum
//      zfail, GLenum zpass)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility11glStencilOpEjjj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum fail,
    GLenum zfail,
    GLenum zpass) {
  self->glStencilOp(fail, zfail, zpass);
}

//  void QOpenGLFunctions_3_2_Compatibility::glStencilFunc(GLenum func, GLint
//      ref, GLuint mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glStencilFuncEjij(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum func,
    GLint ref,
    GLuint mask) {
  self->glStencilFunc(func, ref, mask);
}

//  void QOpenGLFunctions_3_2_Compatibility::glLogicOp(GLenum opcode)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility9glLogicOpEj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum opcode) {
  self->glLogicOp(opcode);
}

//  void QOpenGLFunctions_3_2_Compatibility::glBlendFunc(GLenum sfactor,
//      GLenum dfactor)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility11glBlendFuncEjj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum sfactor,
    GLenum dfactor) {
  self->glBlendFunc(sfactor, dfactor);
}

//  void QOpenGLFunctions_3_2_Compatibility::glFlush()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility7glFlushEv(
    QOpenGLFunctions_3_2_Compatibility *self) {
  self->glFlush();
}

//  void QOpenGLFunctions_3_2_Compatibility::glFinish()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility8glFinishEv(
    QOpenGLFunctions_3_2_Compatibility *self) {
  self->glFinish();
}

//  void QOpenGLFunctions_3_2_Compatibility::glEnable(GLenum cap)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility8glEnableEj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum cap) {
  self->glEnable(cap);
}

//  void QOpenGLFunctions_3_2_Compatibility::glDisable(GLenum cap)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility9glDisableEj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum cap) {
  self->glDisable(cap);
}

//  void QOpenGLFunctions_3_2_Compatibility::glDepthMask(GLboolean flag)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility11glDepthMaskEh(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLboolean flag) {
  self->glDepthMask(flag);
}

//  void QOpenGLFunctions_3_2_Compatibility::glColorMask(GLboolean red,
//      GLboolean green, GLboolean blue, GLboolean alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility11glColorMaskEhhhh(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLboolean red,
    GLboolean green,
    GLboolean blue,
    GLboolean alpha) {
  self->glColorMask(red, green, blue, alpha);
}

//  void QOpenGLFunctions_3_2_Compatibility::glStencilMask(GLuint mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glStencilMaskEj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint mask) {
  self->glStencilMask(mask);
}

//  void QOpenGLFunctions_3_2_Compatibility::glClearDepth(GLdouble depth)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glClearDepthEd(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLdouble depth) {
  self->glClearDepth(depth);
}

//  void QOpenGLFunctions_3_2_Compatibility::glClearStencil(GLint s)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility14glClearStencilEi(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLint s) {
  self->glClearStencil(s);
}

//  void QOpenGLFunctions_3_2_Compatibility::glClearColor(GLfloat red,
//      GLfloat green, GLfloat blue, GLfloat alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glClearColorEffff(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLfloat red,
    GLfloat green,
    GLfloat blue,
    GLfloat alpha) {
  self->glClearColor(red, green, blue, alpha);
}

//  void QOpenGLFunctions_3_2_Compatibility::glClear(GLbitfield mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility7glClearEj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLbitfield mask) {
  self->glClear(mask);
}

//  void QOpenGLFunctions_3_2_Compatibility::glDrawBuffer(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glDrawBufferEj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum mode) {
  self->glDrawBuffer(mode);
}

//  void QOpenGLFunctions_3_2_Compatibility::glTexImage2D(GLenum target,
//      GLint level, GLint internalformat, GLsizei width, GLsizei height,
//      GLint border, GLenum format, GLenum type, const GLvoid *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glTexImage2DEjiiiiijjPKv(
    QOpenGLFunctions_3_2_Compatibility *self,
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

//  void QOpenGLFunctions_3_2_Compatibility::glTexImage1D(GLenum target,
//      GLint level, GLint internalformat, GLsizei width, GLint border,
//      GLenum format, GLenum type, const GLvoid *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glTexImage1DEjiiiijjPKv(
    QOpenGLFunctions_3_2_Compatibility *self,
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

//  void QOpenGLFunctions_3_2_Compatibility::glTexParameteriv(GLenum target,
//      GLenum pname, const GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility16glTexParameterivEjjPKi(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLenum pname,
    const GLint *params) {
  self->glTexParameteriv(target, pname, params);
}

//  void QOpenGLFunctions_3_2_Compatibility::glTexParameteri(GLenum target,
//      GLenum pname, GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility15glTexParameteriEjji(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLenum pname,
    GLint param) {
  self->glTexParameteri(target, pname, param);
}

//  void QOpenGLFunctions_3_2_Compatibility::glTexParameterfv(GLenum target,
//      GLenum pname, const GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility16glTexParameterfvEjjPKf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLenum pname,
    const GLfloat *params) {
  self->glTexParameterfv(target, pname, params);
}

//  void QOpenGLFunctions_3_2_Compatibility::glTexParameterf(GLenum target,
//      GLenum pname, GLfloat param)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility15glTexParameterfEjjf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLenum pname,
    GLfloat param) {
  self->glTexParameterf(target, pname, param);
}

//  void QOpenGLFunctions_3_2_Compatibility::glScissor(GLint x, GLint y,
//      GLsizei width, GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility9glScissorEiiii(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLint x,
    GLint y,
    GLsizei width,
    GLsizei height) {
  self->glScissor(x, y, width, height);
}

//  void QOpenGLFunctions_3_2_Compatibility::glPolygonMode(GLenum face,
//      GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glPolygonModeEjj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum face,
    GLenum mode) {
  self->glPolygonMode(face, mode);
}

//  void QOpenGLFunctions_3_2_Compatibility::glPointSize(GLfloat size)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility11glPointSizeEf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLfloat size) {
  self->glPointSize(size);
}

//  void QOpenGLFunctions_3_2_Compatibility::glLineWidth(GLfloat width)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility11glLineWidthEf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLfloat width) {
  self->glLineWidth(width);
}

//  void QOpenGLFunctions_3_2_Compatibility::glHint(GLenum target, GLenum
//      mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility6glHintEjj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLenum mode) {
  self->glHint(target, mode);
}

//  void QOpenGLFunctions_3_2_Compatibility::glFrontFace(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility11glFrontFaceEj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum mode) {
  self->glFrontFace(mode);
}

//  void QOpenGLFunctions_3_2_Compatibility::glCullFace(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility10glCullFaceEj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum mode) {
  self->glCullFace(mode);
}

//  void QOpenGLFunctions_3_2_Compatibility::glIndexubv(const GLubyte *c)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility10glIndexubvEPKh(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLubyte *c) {
  self->glIndexubv(c);
}

//  void QOpenGLFunctions_3_2_Compatibility::glIndexub(GLubyte c)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility9glIndexubEh(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLubyte c) {
  self->glIndexub(c);
}

//  GLboolean QOpenGLFunctions_3_2_Compatibility::glIsTexture(GLuint texture)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN34QOpenGLFunctions_3_2_Compatibility11glIsTextureEj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint texture) {
  return self->glIsTexture(texture);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGenTextures(GLsizei n, GLuint
//      *textures)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glGenTexturesEiPj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLsizei n,
    GLuint *textures) {
  self->glGenTextures(n, textures);
}

//  void QOpenGLFunctions_3_2_Compatibility::glDeleteTextures(GLsizei n,
//      const GLuint *textures)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility16glDeleteTexturesEiPKj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLsizei n,
    const GLuint *textures) {
  self->glDeleteTextures(n, textures);
}

//  void QOpenGLFunctions_3_2_Compatibility::glBindTexture(GLenum target,
//      GLuint texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glBindTextureEjj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLuint texture) {
  self->glBindTexture(target, texture);
}

//  void QOpenGLFunctions_3_2_Compatibility::glTexSubImage2D(GLenum target,
//      GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei
//      height, GLenum format, GLenum type, const GLvoid *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility15glTexSubImage2DEjiiiiijjPKv(
    QOpenGLFunctions_3_2_Compatibility *self,
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

//  void QOpenGLFunctions_3_2_Compatibility::glTexSubImage1D(GLenum target,
//      GLint level, GLint xoffset, GLsizei width, GLenum format, GLenum
//      type, const GLvoid *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility15glTexSubImage1DEjiiijjPKv(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLint level,
    GLint xoffset,
    GLsizei width,
    GLenum format,
    GLenum type,
    const GLvoid *pixels) {
  self->glTexSubImage1D(target, level, xoffset, width, format, type, pixels);
}

//  void QOpenGLFunctions_3_2_Compatibility::glCopyTexSubImage2D(GLenum
//      target, GLint level, GLint xoffset, GLint yoffset, GLint x, GLint y,
//      GLsizei width, GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility19glCopyTexSubImage2DEjiiiiiii(
    QOpenGLFunctions_3_2_Compatibility *self,
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

//  void QOpenGLFunctions_3_2_Compatibility::glCopyTexSubImage1D(GLenum
//      target, GLint level, GLint xoffset, GLint x, GLint y, GLsizei width)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility19glCopyTexSubImage1DEjiiiii(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLint level,
    GLint xoffset,
    GLint x,
    GLint y,
    GLsizei width) {
  self->glCopyTexSubImage1D(target, level, xoffset, x, y, width);
}

//  void QOpenGLFunctions_3_2_Compatibility::glCopyTexImage2D(GLenum target,
//      GLint level, GLenum internalformat, GLint x, GLint y, GLsizei width,
//      GLsizei height, GLint border)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility16glCopyTexImage2DEjijiiiii(
    QOpenGLFunctions_3_2_Compatibility *self,
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

//  void QOpenGLFunctions_3_2_Compatibility::glCopyTexImage1D(GLenum target,
//      GLint level, GLenum internalformat, GLint x, GLint y, GLsizei width,
//      GLint border)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility16glCopyTexImage1DEjijiiii(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLint level,
    GLenum internalformat,
    GLint x,
    GLint y,
    GLsizei width,
    GLint border) {
  self->glCopyTexImage1D(target, level, internalformat, x, y, width, border);
}

//  void QOpenGLFunctions_3_2_Compatibility::glPolygonOffset(GLfloat factor,
//      GLfloat units)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility15glPolygonOffsetEff(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLfloat factor,
    GLfloat units) {
  self->glPolygonOffset(factor, units);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGetPointerv(GLenum pname,
//      GLvoid **params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glGetPointervEjPPv(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum pname,
    GLvoid **params) {
  self->glGetPointerv(pname, params);
}

//  void QOpenGLFunctions_3_2_Compatibility::glDrawElements(GLenum mode,
//      GLsizei count, GLenum type, const GLvoid *indices)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility14glDrawElementsEjijPKv(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum mode,
    GLsizei count,
    GLenum type,
    const GLvoid *indices) {
  self->glDrawElements(mode, count, type, indices);
}

//  void QOpenGLFunctions_3_2_Compatibility::glDrawArrays(GLenum mode, GLint
//      first, GLsizei count)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glDrawArraysEjii(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum mode,
    GLint first,
    GLsizei count) {
  self->glDrawArrays(mode, first, count);
}

//  void QOpenGLFunctions_3_2_Compatibility::glCopyTexSubImage3D(GLenum
//      target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset,
//      GLint x, GLint y, GLsizei width, GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility19glCopyTexSubImage3DEjiiiiiiii(
    QOpenGLFunctions_3_2_Compatibility *self,
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

//  void QOpenGLFunctions_3_2_Compatibility::glTexSubImage3D(GLenum target,
//      GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei
//      width, GLsizei height, GLsizei depth, GLenum format, GLenum type,
//      const GLvoid *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility15glTexSubImage3DEjiiiiiiijjPKv(
    QOpenGLFunctions_3_2_Compatibility *self,
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

//  void QOpenGLFunctions_3_2_Compatibility::glTexImage3D(GLenum target,
//      GLint level, GLint internalformat, GLsizei width, GLsizei height,
//      GLsizei depth, GLint border, GLenum format, GLenum type, const GLvoid
//      *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glTexImage3DEjiiiiiijjPKv(
    QOpenGLFunctions_3_2_Compatibility *self,
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

//  void QOpenGLFunctions_3_2_Compatibility::glDrawRangeElements(GLenum mode,
//      GLuint start, GLuint end, GLsizei count, GLenum type, const GLvoid
//      *indices)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility19glDrawRangeElementsEjjjijPKv(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum mode,
    GLuint start,
    GLuint end,
    GLsizei count,
    GLenum type,
    const GLvoid *indices) {
  self->glDrawRangeElements(mode, start, end, count, type, indices);
}

//  void QOpenGLFunctions_3_2_Compatibility::glBlendEquation(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility15glBlendEquationEj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum mode) {
  self->glBlendEquation(mode);
}

//  void QOpenGLFunctions_3_2_Compatibility::glBlendColor(GLfloat red,
//      GLfloat green, GLfloat blue, GLfloat alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glBlendColorEffff(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLfloat red,
    GLfloat green,
    GLfloat blue,
    GLfloat alpha) {
  self->glBlendColor(red, green, blue, alpha);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGetCompressedTexImage(GLenum
//      target, GLint level, GLvoid *img)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility23glGetCompressedTexImageEjiPv(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLint level,
    GLvoid *img) {
  self->glGetCompressedTexImage(target, level, img);
}

//  void QOpenGLFunctions_3_2_Compatibility::glCompressedTexSubImage1D(GLenum
//      target, GLint level, GLint xoffset, GLsizei width, GLenum format,
//      GLsizei imageSize, const GLvoid *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility25glCompressedTexSubImage1DEjiiijiPKv(
    QOpenGLFunctions_3_2_Compatibility *self,
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

//  void QOpenGLFunctions_3_2_Compatibility::glCompressedTexSubImage2D(GLenum
//      target, GLint level, GLint xoffset, GLint yoffset, GLsizei width,
//      GLsizei height, GLenum format, GLsizei imageSize, const GLvoid *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility25glCompressedTexSubImage2DEjiiiiijiPKv(
    QOpenGLFunctions_3_2_Compatibility *self,
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

//  void QOpenGLFunctions_3_2_Compatibility::glCompressedTexSubImage3D(GLenum
//      target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset,
//      GLsizei width, GLsizei height, GLsizei depth, GLenum format, GLsizei
//      imageSize, const GLvoid *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility25glCompressedTexSubImage3DEjiiiiiiijiPKv(
    QOpenGLFunctions_3_2_Compatibility *self,
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

//  void QOpenGLFunctions_3_2_Compatibility::glCompressedTexImage1D(GLenum
//      target, GLint level, GLenum internalformat, GLsizei width, GLint
//      border, GLsizei imageSize, const GLvoid *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility22glCompressedTexImage1DEjijiiiPKv(
    QOpenGLFunctions_3_2_Compatibility *self,
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

//  void QOpenGLFunctions_3_2_Compatibility::glCompressedTexImage2D(GLenum
//      target, GLint level, GLenum internalformat, GLsizei width, GLsizei
//      height, GLint border, GLsizei imageSize, const GLvoid *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility22glCompressedTexImage2DEjijiiiiPKv(
    QOpenGLFunctions_3_2_Compatibility *self,
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

//  void QOpenGLFunctions_3_2_Compatibility::glCompressedTexImage3D(GLenum
//      target, GLint level, GLenum internalformat, GLsizei width, GLsizei
//      height, GLsizei depth, GLint border, GLsizei imageSize, const GLvoid
//      *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility22glCompressedTexImage3DEjijiiiiiPKv(
    QOpenGLFunctions_3_2_Compatibility *self,
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

//  void QOpenGLFunctions_3_2_Compatibility::glSampleCoverage(GLfloat value,
//      GLboolean invert)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility16glSampleCoverageEfh(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLfloat value,
    GLboolean invert) {
  self->glSampleCoverage(value, invert);
}

//  void QOpenGLFunctions_3_2_Compatibility::glActiveTexture(GLenum texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility15glActiveTextureEj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum texture) {
  self->glActiveTexture(texture);
}

//  void QOpenGLFunctions_3_2_Compatibility::glPointParameteriv(GLenum pname,
//      const GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility18glPointParameterivEjPKi(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum pname,
    const GLint *params) {
  self->glPointParameteriv(pname, params);
}

//  void QOpenGLFunctions_3_2_Compatibility::glPointParameteri(GLenum pname,
//      GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility17glPointParameteriEji(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum pname,
    GLint param) {
  self->glPointParameteri(pname, param);
}

//  void QOpenGLFunctions_3_2_Compatibility::glPointParameterfv(GLenum pname,
//      const GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility18glPointParameterfvEjPKf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum pname,
    const GLfloat *params) {
  self->glPointParameterfv(pname, params);
}

//  void QOpenGLFunctions_3_2_Compatibility::glPointParameterf(GLenum pname,
//      GLfloat param)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility17glPointParameterfEjf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum pname,
    GLfloat param) {
  self->glPointParameterf(pname, param);
}

//  void QOpenGLFunctions_3_2_Compatibility::glMultiDrawElements(GLenum mode,
//      const GLsizei *count, GLenum type, const GLvoid *const *indices,
//      GLsizei drawcount)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility19glMultiDrawElementsEjPKijPKPKvi(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum mode,
    const GLsizei *count,
    GLenum type,
    const GLvoid *const *indices,
    GLsizei drawcount) {
  self->glMultiDrawElements(mode, count, type, indices, drawcount);
}

//  void QOpenGLFunctions_3_2_Compatibility::glMultiDrawArrays(GLenum mode,
//      const GLint *first, const GLsizei *count, GLsizei drawcount)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility17glMultiDrawArraysEjPKiS1_i(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum mode,
    const GLint *first,
    const GLsizei *count,
    GLsizei drawcount) {
  self->glMultiDrawArrays(mode, first, count, drawcount);
}

//  void QOpenGLFunctions_3_2_Compatibility::glBlendFuncSeparate(GLenum
//      sfactorRGB, GLenum dfactorRGB, GLenum sfactorAlpha, GLenum
//      dfactorAlpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility19glBlendFuncSeparateEjjjj(
    QOpenGLFunctions_3_2_Compatibility *self,
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

//  void QOpenGLFunctions_3_2_Compatibility::glGetBufferPointerv(GLenum
//      target, GLenum pname, GLvoid **params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility19glGetBufferPointervEjjPPv(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLenum pname,
    GLvoid **params) {
  self->glGetBufferPointerv(target, pname, params);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGetBufferParameteriv(GLenum
//      target, GLenum pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility22glGetBufferParameterivEjjPi(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLenum pname,
    GLint *params) {
  self->glGetBufferParameteriv(target, pname, params);
}

//  GLboolean QOpenGLFunctions_3_2_Compatibility::glUnmapBuffer(GLenum
//      target)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glUnmapBufferEj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target) {
  return self->glUnmapBuffer(target);
}

//  GLvoid *QOpenGLFunctions_3_2_Compatibility::glMapBuffer(GLenum target,
//      GLenum access)
extern "C" Q_DECL_EXPORT
GLvoid *ritual_ZN34QOpenGLFunctions_3_2_Compatibility11glMapBufferEjj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLenum access) {
  return self->glMapBuffer(target, access);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGetBufferSubData(GLenum
//      target, GLintptr offset, GLsizeiptr size, GLvoid *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility18glGetBufferSubDataEjllPv(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    long long offset,
    long long size,
    GLvoid *data) {
  self->glGetBufferSubData(target, offset, size, data);
}

//  void QOpenGLFunctions_3_2_Compatibility::glBufferSubData(GLenum target,
//      GLintptr offset, GLsizeiptr size, const GLvoid *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility15glBufferSubDataEjllPKv(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    long long offset,
    long long size,
    const GLvoid *data) {
  self->glBufferSubData(target, offset, size, data);
}

//  void QOpenGLFunctions_3_2_Compatibility::glBufferData(GLenum target,
//      GLsizeiptr size, const GLvoid *data, GLenum usage)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glBufferDataEjlPKvj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    long long size,
    const GLvoid *data,
    GLenum usage) {
  self->glBufferData(target, size, data, usage);
}

//  GLboolean QOpenGLFunctions_3_2_Compatibility::glIsBuffer(GLuint buffer)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN34QOpenGLFunctions_3_2_Compatibility10glIsBufferEj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint buffer) {
  return self->glIsBuffer(buffer);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGenBuffers(GLsizei n, GLuint
//      *buffers)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glGenBuffersEiPj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLsizei n,
    GLuint *buffers) {
  self->glGenBuffers(n, buffers);
}

//  void QOpenGLFunctions_3_2_Compatibility::glDeleteBuffers(GLsizei n, const
//      GLuint *buffers)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility15glDeleteBuffersEiPKj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLsizei n,
    const GLuint *buffers) {
  self->glDeleteBuffers(n, buffers);
}

//  void QOpenGLFunctions_3_2_Compatibility::glBindBuffer(GLenum target,
//      GLuint buffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glBindBufferEjj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLuint buffer) {
  self->glBindBuffer(target, buffer);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGetQueryObjectuiv(GLuint id,
//      GLenum pname, GLuint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility19glGetQueryObjectuivEjjPj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint id,
    GLenum pname,
    GLuint *params) {
  self->glGetQueryObjectuiv(id, pname, params);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGetQueryObjectiv(GLuint id,
//      GLenum pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility18glGetQueryObjectivEjjPi(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint id,
    GLenum pname,
    GLint *params) {
  self->glGetQueryObjectiv(id, pname, params);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGetQueryiv(GLenum target,
//      GLenum pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glGetQueryivEjjPi(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLenum pname,
    GLint *params) {
  self->glGetQueryiv(target, pname, params);
}

//  void QOpenGLFunctions_3_2_Compatibility::glEndQuery(GLenum target)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility10glEndQueryEj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target) {
  self->glEndQuery(target);
}

//  void QOpenGLFunctions_3_2_Compatibility::glBeginQuery(GLenum target,
//      GLuint id)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glBeginQueryEjj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLuint id) {
  self->glBeginQuery(target, id);
}

//  GLboolean QOpenGLFunctions_3_2_Compatibility::glIsQuery(GLuint id)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN34QOpenGLFunctions_3_2_Compatibility9glIsQueryEj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint id) {
  return self->glIsQuery(id);
}

//  void QOpenGLFunctions_3_2_Compatibility::glDeleteQueries(GLsizei n, const
//      GLuint *ids)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility15glDeleteQueriesEiPKj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLsizei n,
    const GLuint *ids) {
  self->glDeleteQueries(n, ids);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGenQueries(GLsizei n, GLuint
//      *ids)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glGenQueriesEiPj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLsizei n,
    GLuint *ids) {
  self->glGenQueries(n, ids);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertexAttribPointer(GLuint
//      index, GLint size, GLenum type, GLboolean normalized, GLsizei stride,
//      const GLvoid *pointer)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility21glVertexAttribPointerEjijhiPKv(
    QOpenGLFunctions_3_2_Compatibility *self,
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

//  void QOpenGLFunctions_3_2_Compatibility::glValidateProgram(GLuint
//      program)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility17glValidateProgramEj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint program) {
  self->glValidateProgram(program);
}

//  void QOpenGLFunctions_3_2_Compatibility::glUniformMatrix4fv(GLint
//      location, GLsizei count, GLboolean transpose, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility18glUniformMatrix4fvEiihPKf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLfloat *value) {
  self->glUniformMatrix4fv(location, count, transpose, value);
}

//  void QOpenGLFunctions_3_2_Compatibility::glUniformMatrix3fv(GLint
//      location, GLsizei count, GLboolean transpose, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility18glUniformMatrix3fvEiihPKf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLfloat *value) {
  self->glUniformMatrix3fv(location, count, transpose, value);
}

//  void QOpenGLFunctions_3_2_Compatibility::glUniformMatrix2fv(GLint
//      location, GLsizei count, GLboolean transpose, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility18glUniformMatrix2fvEiihPKf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLfloat *value) {
  self->glUniformMatrix2fv(location, count, transpose, value);
}

//  void QOpenGLFunctions_3_2_Compatibility::glUniform4iv(GLint location,
//      GLsizei count, const GLint *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glUniform4ivEiiPKi(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLint location,
    GLsizei count,
    const GLint *value) {
  self->glUniform4iv(location, count, value);
}

//  void QOpenGLFunctions_3_2_Compatibility::glUniform3iv(GLint location,
//      GLsizei count, const GLint *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glUniform3ivEiiPKi(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLint location,
    GLsizei count,
    const GLint *value) {
  self->glUniform3iv(location, count, value);
}

//  void QOpenGLFunctions_3_2_Compatibility::glUniform2iv(GLint location,
//      GLsizei count, const GLint *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glUniform2ivEiiPKi(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLint location,
    GLsizei count,
    const GLint *value) {
  self->glUniform2iv(location, count, value);
}

//  void QOpenGLFunctions_3_2_Compatibility::glUniform1iv(GLint location,
//      GLsizei count, const GLint *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glUniform1ivEiiPKi(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLint location,
    GLsizei count,
    const GLint *value) {
  self->glUniform1iv(location, count, value);
}

//  void QOpenGLFunctions_3_2_Compatibility::glUniform4fv(GLint location,
//      GLsizei count, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glUniform4fvEiiPKf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLint location,
    GLsizei count,
    const GLfloat *value) {
  self->glUniform4fv(location, count, value);
}

//  void QOpenGLFunctions_3_2_Compatibility::glUniform3fv(GLint location,
//      GLsizei count, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glUniform3fvEiiPKf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLint location,
    GLsizei count,
    const GLfloat *value) {
  self->glUniform3fv(location, count, value);
}

//  void QOpenGLFunctions_3_2_Compatibility::glUniform2fv(GLint location,
//      GLsizei count, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glUniform2fvEiiPKf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLint location,
    GLsizei count,
    const GLfloat *value) {
  self->glUniform2fv(location, count, value);
}

//  void QOpenGLFunctions_3_2_Compatibility::glUniform1fv(GLint location,
//      GLsizei count, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glUniform1fvEiiPKf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLint location,
    GLsizei count,
    const GLfloat *value) {
  self->glUniform1fv(location, count, value);
}

//  void QOpenGLFunctions_3_2_Compatibility::glUniform4i(GLint location,
//      GLint v0, GLint v1, GLint v2, GLint v3)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility11glUniform4iEiiiii(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLint location,
    GLint v0,
    GLint v1,
    GLint v2,
    GLint v3) {
  self->glUniform4i(location, v0, v1, v2, v3);
}

//  void QOpenGLFunctions_3_2_Compatibility::glUniform3i(GLint location,
//      GLint v0, GLint v1, GLint v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility11glUniform3iEiiii(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLint location,
    GLint v0,
    GLint v1,
    GLint v2) {
  self->glUniform3i(location, v0, v1, v2);
}

//  void QOpenGLFunctions_3_2_Compatibility::glUniform2i(GLint location,
//      GLint v0, GLint v1)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility11glUniform2iEiii(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLint location,
    GLint v0,
    GLint v1) {
  self->glUniform2i(location, v0, v1);
}

//  void QOpenGLFunctions_3_2_Compatibility::glUniform1i(GLint location,
//      GLint v0)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility11glUniform1iEii(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLint location,
    GLint v0) {
  self->glUniform1i(location, v0);
}

//  void QOpenGLFunctions_3_2_Compatibility::glUniform4f(GLint location,
//      GLfloat v0, GLfloat v1, GLfloat v2, GLfloat v3)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility11glUniform4fEiffff(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLint location,
    GLfloat v0,
    GLfloat v1,
    GLfloat v2,
    GLfloat v3) {
  self->glUniform4f(location, v0, v1, v2, v3);
}

//  void QOpenGLFunctions_3_2_Compatibility::glUniform3f(GLint location,
//      GLfloat v0, GLfloat v1, GLfloat v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility11glUniform3fEifff(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLint location,
    GLfloat v0,
    GLfloat v1,
    GLfloat v2) {
  self->glUniform3f(location, v0, v1, v2);
}

//  void QOpenGLFunctions_3_2_Compatibility::glUniform2f(GLint location,
//      GLfloat v0, GLfloat v1)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility11glUniform2fEiff(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLint location,
    GLfloat v0,
    GLfloat v1) {
  self->glUniform2f(location, v0, v1);
}

//  void QOpenGLFunctions_3_2_Compatibility::glUniform1f(GLint location,
//      GLfloat v0)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility11glUniform1fEif(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLint location,
    GLfloat v0) {
  self->glUniform1f(location, v0);
}

//  void QOpenGLFunctions_3_2_Compatibility::glUseProgram(GLuint program)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glUseProgramEj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint program) {
  self->glUseProgram(program);
}

//  void QOpenGLFunctions_3_2_Compatibility::glShaderSource(GLuint shader,
//      GLsizei count, const GLchar *const *string, const GLint *length)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility14glShaderSourceEjiPKPKcPKi(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint shader,
    GLsizei count,
    const GLchar *const *string,
    const GLint *length) {
  self->glShaderSource(shader, count, string, length);
}

//  void QOpenGLFunctions_3_2_Compatibility::glLinkProgram(GLuint program)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glLinkProgramEj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint program) {
  self->glLinkProgram(program);
}

//  GLboolean QOpenGLFunctions_3_2_Compatibility::glIsShader(GLuint shader)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN34QOpenGLFunctions_3_2_Compatibility10glIsShaderEj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint shader) {
  return self->glIsShader(shader);
}

//  GLboolean QOpenGLFunctions_3_2_Compatibility::glIsProgram(GLuint program)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN34QOpenGLFunctions_3_2_Compatibility11glIsProgramEj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint program) {
  return self->glIsProgram(program);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGetVertexAttribPointerv(GLuint
//      index, GLenum pname, GLvoid **pointer)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility25glGetVertexAttribPointervEjjPPv(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint index,
    GLenum pname,
    GLvoid **pointer) {
  self->glGetVertexAttribPointerv(index, pname, pointer);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGetVertexAttribiv(GLuint
//      index, GLenum pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility19glGetVertexAttribivEjjPi(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint index,
    GLenum pname,
    GLint *params) {
  self->glGetVertexAttribiv(index, pname, params);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGetVertexAttribfv(GLuint
//      index, GLenum pname, GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility19glGetVertexAttribfvEjjPf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint index,
    GLenum pname,
    GLfloat *params) {
  self->glGetVertexAttribfv(index, pname, params);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGetVertexAttribdv(GLuint
//      index, GLenum pname, GLdouble *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility19glGetVertexAttribdvEjjPd(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint index,
    GLenum pname,
    GLdouble *params) {
  self->glGetVertexAttribdv(index, pname, params);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGetUniformiv(GLuint program,
//      GLint location, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility14glGetUniformivEjiPi(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint program,
    GLint location,
    GLint *params) {
  self->glGetUniformiv(program, location, params);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGetUniformfv(GLuint program,
//      GLint location, GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility14glGetUniformfvEjiPf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint program,
    GLint location,
    GLfloat *params) {
  self->glGetUniformfv(program, location, params);
}

//  GLint QOpenGLFunctions_3_2_Compatibility::glGetUniformLocation(GLuint
//      program, const GLchar *name)
extern "C" Q_DECL_EXPORT
GLint ritual_ZN34QOpenGLFunctions_3_2_Compatibility20glGetUniformLocationEjPKc(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint program,
    const GLchar *name) {
  return self->glGetUniformLocation(program, name);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGetShaderSource(GLuint shader,
//      GLsizei bufSize, GLsizei *length, GLchar *source)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility17glGetShaderSourceEjiPiPc(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint shader,
    GLsizei bufSize,
    GLsizei *length,
    GLchar *source) {
  self->glGetShaderSource(shader, bufSize, length, source);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGetShaderInfoLog(GLuint
//      shader, GLsizei bufSize, GLsizei *length, GLchar *infoLog)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility18glGetShaderInfoLogEjiPiPc(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint shader,
    GLsizei bufSize,
    GLsizei *length,
    GLchar *infoLog) {
  self->glGetShaderInfoLog(shader, bufSize, length, infoLog);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGetShaderiv(GLuint shader,
//      GLenum pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glGetShaderivEjjPi(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint shader,
    GLenum pname,
    GLint *params) {
  self->glGetShaderiv(shader, pname, params);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGetProgramInfoLog(GLuint
//      program, GLsizei bufSize, GLsizei *length, GLchar *infoLog)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility19glGetProgramInfoLogEjiPiPc(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint program,
    GLsizei bufSize,
    GLsizei *length,
    GLchar *infoLog) {
  self->glGetProgramInfoLog(program, bufSize, length, infoLog);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGetProgramiv(GLuint program,
//      GLenum pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility14glGetProgramivEjjPi(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint program,
    GLenum pname,
    GLint *params) {
  self->glGetProgramiv(program, pname, params);
}

//  GLint QOpenGLFunctions_3_2_Compatibility::glGetAttribLocation(GLuint
//      program, const GLchar *name)
extern "C" Q_DECL_EXPORT
GLint ritual_ZN34QOpenGLFunctions_3_2_Compatibility19glGetAttribLocationEjPKc(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint program,
    const GLchar *name) {
  return self->glGetAttribLocation(program, name);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGetAttachedShaders(GLuint
//      program, GLsizei maxCount, GLsizei *count, GLuint *obj)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility20glGetAttachedShadersEjiPiPj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint program,
    GLsizei maxCount,
    GLsizei *count,
    GLuint *obj) {
  self->glGetAttachedShaders(program, maxCount, count, obj);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGetActiveUniform(GLuint
//      program, GLuint index, GLsizei bufSize, GLsizei *length, GLint *size,
//      GLenum *type, GLchar *name)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility18glGetActiveUniformEjjiPiS0_PjPc(
    QOpenGLFunctions_3_2_Compatibility *self,
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

//  void QOpenGLFunctions_3_2_Compatibility::glGetActiveAttrib(GLuint
//      program, GLuint index, GLsizei bufSize, GLsizei *length, GLint *size,
//      GLenum *type, GLchar *name)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility17glGetActiveAttribEjjiPiS0_PjPc(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint program,
    GLuint index,
    GLsizei bufSize,
    GLsizei *length,
    GLint *size,
    GLenum *type,
    GLchar *name) {
  self->glGetActiveAttrib(program, index, bufSize, length, size, type, name);
}

//  void QOpenGLFunctions_3_2_Compatibility::glEnableVertexAttribArray(GLuint
//      index)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility25glEnableVertexAttribArrayEj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint index) {
  self->glEnableVertexAttribArray(index);
}

//  void
//      QOpenGLFunctions_3_2_Compatibility::glDisableVertexAttribArray(GLuint
//      index)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility26glDisableVertexAttribArrayEj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint index) {
  self->glDisableVertexAttribArray(index);
}

//  void QOpenGLFunctions_3_2_Compatibility::glDetachShader(GLuint program,
//      GLuint shader)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility14glDetachShaderEjj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint program,
    GLuint shader) {
  self->glDetachShader(program, shader);
}

//  void QOpenGLFunctions_3_2_Compatibility::glDeleteShader(GLuint shader)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility14glDeleteShaderEj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint shader) {
  self->glDeleteShader(shader);
}

//  void QOpenGLFunctions_3_2_Compatibility::glDeleteProgram(GLuint program)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility15glDeleteProgramEj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint program) {
  self->glDeleteProgram(program);
}

//  GLuint QOpenGLFunctions_3_2_Compatibility::glCreateShader(GLenum type)
extern "C" Q_DECL_EXPORT
GLuint ritual_ZN34QOpenGLFunctions_3_2_Compatibility14glCreateShaderEj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum type) {
  return self->glCreateShader(type);
}

//  GLuint QOpenGLFunctions_3_2_Compatibility::glCreateProgram()
extern "C" Q_DECL_EXPORT
GLuint ritual_ZN34QOpenGLFunctions_3_2_Compatibility15glCreateProgramEv(
    QOpenGLFunctions_3_2_Compatibility *self) {
  return self->glCreateProgram();
}

//  void QOpenGLFunctions_3_2_Compatibility::glCompileShader(GLuint shader)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility15glCompileShaderEj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint shader) {
  self->glCompileShader(shader);
}

//  void QOpenGLFunctions_3_2_Compatibility::glBindAttribLocation(GLuint
//      program, GLuint index, const GLchar *name)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility20glBindAttribLocationEjjPKc(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint program,
    GLuint index,
    const GLchar *name) {
  self->glBindAttribLocation(program, index, name);
}

//  void QOpenGLFunctions_3_2_Compatibility::glAttachShader(GLuint program,
//      GLuint shader)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility14glAttachShaderEjj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint program,
    GLuint shader) {
  self->glAttachShader(program, shader);
}

//  void QOpenGLFunctions_3_2_Compatibility::glStencilMaskSeparate(GLenum
//      face, GLuint mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility21glStencilMaskSeparateEjj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum face,
    GLuint mask) {
  self->glStencilMaskSeparate(face, mask);
}

//  void QOpenGLFunctions_3_2_Compatibility::glStencilFuncSeparate(GLenum
//      face, GLenum func, GLint ref, GLuint mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility21glStencilFuncSeparateEjjij(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum face,
    GLenum func,
    GLint ref,
    GLuint mask) {
  self->glStencilFuncSeparate(face, func, ref, mask);
}

//  void QOpenGLFunctions_3_2_Compatibility::glStencilOpSeparate(GLenum face,
//      GLenum sfail, GLenum dpfail, GLenum dppass)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility19glStencilOpSeparateEjjjj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum face,
    GLenum sfail,
    GLenum dpfail,
    GLenum dppass) {
  self->glStencilOpSeparate(face, sfail, dpfail, dppass);
}

//  void QOpenGLFunctions_3_2_Compatibility::glDrawBuffers(GLsizei n, const
//      GLenum *bufs)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glDrawBuffersEiPKj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLsizei n,
    const GLenum *bufs) {
  self->glDrawBuffers(n, bufs);
}

//  void QOpenGLFunctions_3_2_Compatibility::glBlendEquationSeparate(GLenum
//      modeRGB, GLenum modeAlpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility23glBlendEquationSeparateEjj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum modeRGB,
    GLenum modeAlpha) {
  self->glBlendEquationSeparate(modeRGB, modeAlpha);
}

//  void QOpenGLFunctions_3_2_Compatibility::glUniformMatrix4x3fv(GLint
//      location, GLsizei count, GLboolean transpose, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility20glUniformMatrix4x3fvEiihPKf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLfloat *value) {
  self->glUniformMatrix4x3fv(location, count, transpose, value);
}

//  void QOpenGLFunctions_3_2_Compatibility::glUniformMatrix3x4fv(GLint
//      location, GLsizei count, GLboolean transpose, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility20glUniformMatrix3x4fvEiihPKf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLfloat *value) {
  self->glUniformMatrix3x4fv(location, count, transpose, value);
}

//  void QOpenGLFunctions_3_2_Compatibility::glUniformMatrix4x2fv(GLint
//      location, GLsizei count, GLboolean transpose, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility20glUniformMatrix4x2fvEiihPKf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLfloat *value) {
  self->glUniformMatrix4x2fv(location, count, transpose, value);
}

//  void QOpenGLFunctions_3_2_Compatibility::glUniformMatrix2x4fv(GLint
//      location, GLsizei count, GLboolean transpose, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility20glUniformMatrix2x4fvEiihPKf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLfloat *value) {
  self->glUniformMatrix2x4fv(location, count, transpose, value);
}

//  void QOpenGLFunctions_3_2_Compatibility::glUniformMatrix3x2fv(GLint
//      location, GLsizei count, GLboolean transpose, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility20glUniformMatrix3x2fvEiihPKf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLfloat *value) {
  self->glUniformMatrix3x2fv(location, count, transpose, value);
}

//  void QOpenGLFunctions_3_2_Compatibility::glUniformMatrix2x3fv(GLint
//      location, GLsizei count, GLboolean transpose, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility20glUniformMatrix2x3fvEiihPKf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLfloat *value) {
  self->glUniformMatrix2x3fv(location, count, transpose, value);
}

//  GLboolean QOpenGLFunctions_3_2_Compatibility::glIsVertexArray(GLuint
//      array)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN34QOpenGLFunctions_3_2_Compatibility15glIsVertexArrayEj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint array) {
  return self->glIsVertexArray(array);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGenVertexArrays(GLsizei n,
//      GLuint *arrays)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility17glGenVertexArraysEiPj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLsizei n,
    GLuint *arrays) {
  self->glGenVertexArrays(n, arrays);
}

//  void QOpenGLFunctions_3_2_Compatibility::glDeleteVertexArrays(GLsizei n,
//      const GLuint *arrays)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility20glDeleteVertexArraysEiPKj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLsizei n,
    const GLuint *arrays) {
  self->glDeleteVertexArrays(n, arrays);
}

//  void QOpenGLFunctions_3_2_Compatibility::glBindVertexArray(GLuint array)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility17glBindVertexArrayEj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint array) {
  self->glBindVertexArray(array);
}

//  void QOpenGLFunctions_3_2_Compatibility::glFlushMappedBufferRange(GLenum
//      target, GLintptr offset, GLsizeiptr length)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility24glFlushMappedBufferRangeEjll(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    long long offset,
    long long length) {
  self->glFlushMappedBufferRange(target, offset, length);
}

//  GLvoid *QOpenGLFunctions_3_2_Compatibility::glMapBufferRange(GLenum
//      target, GLintptr offset, GLsizeiptr length, GLbitfield access)
extern "C" Q_DECL_EXPORT
GLvoid *ritual_ZN34QOpenGLFunctions_3_2_Compatibility16glMapBufferRangeEjllj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    long long offset,
    long long length,
    GLbitfield access) {
  return self->glMapBufferRange(target, offset, length, access);
}

//  void QOpenGLFunctions_3_2_Compatibility::glFramebufferTextureLayer(GLenum
//      target, GLenum attachment, GLuint texture, GLint level, GLint layer)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility25glFramebufferTextureLayerEjjjii(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLenum attachment,
    GLuint texture,
    GLint level,
    GLint layer) {
  self->glFramebufferTextureLayer(target, attachment, texture, level, layer);
}

//  void QOpenGLFunctions_3_2_Compatibility::glRenderbufferStorageMultisample
//      (GLenum target, GLsizei samples, GLenum internalformat, GLsizei
//      width, GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility32glRenderbufferStorageMultisampleEjijii(
    QOpenGLFunctions_3_2_Compatibility *self,
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

//  void QOpenGLFunctions_3_2_Compatibility::glBlitFramebuffer(GLint srcX0,
//      GLint srcY0, GLint srcX1, GLint srcY1, GLint dstX0, GLint dstY0,
//      GLint dstX1, GLint dstY1, GLbitfield mask, GLenum filter)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility17glBlitFramebufferEiiiiiiiijj(
    QOpenGLFunctions_3_2_Compatibility *self,
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

//  void QOpenGLFunctions_3_2_Compatibility::glGenerateMipmap(GLenum target)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility16glGenerateMipmapEj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target) {
  self->glGenerateMipmap(target);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGetFramebufferAttachmentParame
//      teriv(GLenum target, GLenum attachment, GLenum pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility37glGetFramebufferAttachmentParameterivEjjjPi(
    QOpenGLFunctions_3_2_Compatibility *self,
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

//  void QOpenGLFunctions_3_2_Compatibility::glFramebufferRenderbuffer(GLenum
//      target, GLenum attachment, GLenum renderbuffertarget, GLuint
//      renderbuffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility25glFramebufferRenderbufferEjjjj(
    QOpenGLFunctions_3_2_Compatibility *self,
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

//  void QOpenGLFunctions_3_2_Compatibility::glFramebufferTexture3D(GLenum
//      target, GLenum attachment, GLenum textarget, GLuint texture, GLint
//      level, GLint zoffset)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility22glFramebufferTexture3DEjjjjii(
    QOpenGLFunctions_3_2_Compatibility *self,
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

//  void QOpenGLFunctions_3_2_Compatibility::glFramebufferTexture2D(GLenum
//      target, GLenum attachment, GLenum textarget, GLuint texture, GLint
//      level)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility22glFramebufferTexture2DEjjjji(
    QOpenGLFunctions_3_2_Compatibility *self,
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

//  void QOpenGLFunctions_3_2_Compatibility::glFramebufferTexture1D(GLenum
//      target, GLenum attachment, GLenum textarget, GLuint texture, GLint
//      level)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility22glFramebufferTexture1DEjjjji(
    QOpenGLFunctions_3_2_Compatibility *self,
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

//  GLenum
//      QOpenGLFunctions_3_2_Compatibility::glCheckFramebufferStatus(GLenum
//      target)
extern "C" Q_DECL_EXPORT
GLenum ritual_ZN34QOpenGLFunctions_3_2_Compatibility24glCheckFramebufferStatusEj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target) {
  return self->glCheckFramebufferStatus(target);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGenFramebuffers(GLsizei n,
//      GLuint *framebuffers)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility17glGenFramebuffersEiPj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLsizei n,
    GLuint *framebuffers) {
  self->glGenFramebuffers(n, framebuffers);
}

//  void QOpenGLFunctions_3_2_Compatibility::glDeleteFramebuffers(GLsizei n,
//      const GLuint *framebuffers)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility20glDeleteFramebuffersEiPKj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLsizei n,
    const GLuint *framebuffers) {
  self->glDeleteFramebuffers(n, framebuffers);
}

//  void QOpenGLFunctions_3_2_Compatibility::glBindFramebuffer(GLenum target,
//      GLuint framebuffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility17glBindFramebufferEjj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLuint framebuffer) {
  self->glBindFramebuffer(target, framebuffer);
}

//  GLboolean QOpenGLFunctions_3_2_Compatibility::glIsFramebuffer(GLuint
//      framebuffer)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN34QOpenGLFunctions_3_2_Compatibility15glIsFramebufferEj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint framebuffer) {
  return self->glIsFramebuffer(framebuffer);
}

//  void
//      QOpenGLFunctions_3_2_Compatibility::glGetRenderbufferParameteriv(GLen
//      um target, GLenum pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility28glGetRenderbufferParameterivEjjPi(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLenum pname,
    GLint *params) {
  self->glGetRenderbufferParameteriv(target, pname, params);
}

//  void QOpenGLFunctions_3_2_Compatibility::glRenderbufferStorage(GLenum
//      target, GLenum internalformat, GLsizei width, GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility21glRenderbufferStorageEjjii(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLenum internalformat,
    GLsizei width,
    GLsizei height) {
  self->glRenderbufferStorage(target, internalformat, width, height);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGenRenderbuffers(GLsizei n,
//      GLuint *renderbuffers)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility18glGenRenderbuffersEiPj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLsizei n,
    GLuint *renderbuffers) {
  self->glGenRenderbuffers(n, renderbuffers);
}

//  void QOpenGLFunctions_3_2_Compatibility::glDeleteRenderbuffers(GLsizei n,
//      const GLuint *renderbuffers)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility21glDeleteRenderbuffersEiPKj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLsizei n,
    const GLuint *renderbuffers) {
  self->glDeleteRenderbuffers(n, renderbuffers);
}

//  void QOpenGLFunctions_3_2_Compatibility::glBindRenderbuffer(GLenum
//      target, GLuint renderbuffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility18glBindRenderbufferEjj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLuint renderbuffer) {
  self->glBindRenderbuffer(target, renderbuffer);
}

//  GLboolean QOpenGLFunctions_3_2_Compatibility::glIsRenderbuffer(GLuint
//      renderbuffer)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN34QOpenGLFunctions_3_2_Compatibility16glIsRenderbufferEj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint renderbuffer) {
  return self->glIsRenderbuffer(renderbuffer);
}

//  const GLubyte *QOpenGLFunctions_3_2_Compatibility::glGetStringi(GLenum
//      name, GLuint index)
extern "C" Q_DECL_EXPORT
const GLubyte *ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glGetStringiEjj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum name,
    GLuint index) {
  return self->glGetStringi(name, index);
}

//  void QOpenGLFunctions_3_2_Compatibility::glClearBufferfi(GLenum buffer,
//      GLint drawbuffer, GLfloat depth, GLint stencil)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility15glClearBufferfiEjifi(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum buffer,
    GLint drawbuffer,
    GLfloat depth,
    GLint stencil) {
  self->glClearBufferfi(buffer, drawbuffer, depth, stencil);
}

//  void QOpenGLFunctions_3_2_Compatibility::glClearBufferfv(GLenum buffer,
//      GLint drawbuffer, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility15glClearBufferfvEjiPKf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum buffer,
    GLint drawbuffer,
    const GLfloat *value) {
  self->glClearBufferfv(buffer, drawbuffer, value);
}

//  void QOpenGLFunctions_3_2_Compatibility::glClearBufferuiv(GLenum buffer,
//      GLint drawbuffer, const GLuint *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility16glClearBufferuivEjiPKj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum buffer,
    GLint drawbuffer,
    const GLuint *value) {
  self->glClearBufferuiv(buffer, drawbuffer, value);
}

//  void QOpenGLFunctions_3_2_Compatibility::glClearBufferiv(GLenum buffer,
//      GLint drawbuffer, const GLint *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility15glClearBufferivEjiPKi(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum buffer,
    GLint drawbuffer,
    const GLint *value) {
  self->glClearBufferiv(buffer, drawbuffer, value);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGetTexParameterIuiv(GLenum
//      target, GLenum pname, GLuint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility21glGetTexParameterIuivEjjPj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLenum pname,
    GLuint *params) {
  self->glGetTexParameterIuiv(target, pname, params);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGetTexParameterIiv(GLenum
//      target, GLenum pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility20glGetTexParameterIivEjjPi(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLenum pname,
    GLint *params) {
  self->glGetTexParameterIiv(target, pname, params);
}

//  void QOpenGLFunctions_3_2_Compatibility::glTexParameterIuiv(GLenum
//      target, GLenum pname, const GLuint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility18glTexParameterIuivEjjPKj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLenum pname,
    const GLuint *params) {
  self->glTexParameterIuiv(target, pname, params);
}

//  void QOpenGLFunctions_3_2_Compatibility::glTexParameterIiv(GLenum target,
//      GLenum pname, const GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility17glTexParameterIivEjjPKi(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLenum pname,
    const GLint *params) {
  self->glTexParameterIiv(target, pname, params);
}

//  void QOpenGLFunctions_3_2_Compatibility::glUniform4uiv(GLint location,
//      GLsizei count, const GLuint *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glUniform4uivEiiPKj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLint location,
    GLsizei count,
    const GLuint *value) {
  self->glUniform4uiv(location, count, value);
}

//  void QOpenGLFunctions_3_2_Compatibility::glUniform3uiv(GLint location,
//      GLsizei count, const GLuint *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glUniform3uivEiiPKj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLint location,
    GLsizei count,
    const GLuint *value) {
  self->glUniform3uiv(location, count, value);
}

//  void QOpenGLFunctions_3_2_Compatibility::glUniform2uiv(GLint location,
//      GLsizei count, const GLuint *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glUniform2uivEiiPKj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLint location,
    GLsizei count,
    const GLuint *value) {
  self->glUniform2uiv(location, count, value);
}

//  void QOpenGLFunctions_3_2_Compatibility::glUniform1uiv(GLint location,
//      GLsizei count, const GLuint *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glUniform1uivEiiPKj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLint location,
    GLsizei count,
    const GLuint *value) {
  self->glUniform1uiv(location, count, value);
}

//  void QOpenGLFunctions_3_2_Compatibility::glUniform4ui(GLint location,
//      GLuint v0, GLuint v1, GLuint v2, GLuint v3)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glUniform4uiEijjjj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLint location,
    GLuint v0,
    GLuint v1,
    GLuint v2,
    GLuint v3) {
  self->glUniform4ui(location, v0, v1, v2, v3);
}

//  void QOpenGLFunctions_3_2_Compatibility::glUniform3ui(GLint location,
//      GLuint v0, GLuint v1, GLuint v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glUniform3uiEijjj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLint location,
    GLuint v0,
    GLuint v1,
    GLuint v2) {
  self->glUniform3ui(location, v0, v1, v2);
}

//  void QOpenGLFunctions_3_2_Compatibility::glUniform2ui(GLint location,
//      GLuint v0, GLuint v1)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glUniform2uiEijj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLint location,
    GLuint v0,
    GLuint v1) {
  self->glUniform2ui(location, v0, v1);
}

//  void QOpenGLFunctions_3_2_Compatibility::glUniform1ui(GLint location,
//      GLuint v0)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glUniform1uiEij(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLint location,
    GLuint v0) {
  self->glUniform1ui(location, v0);
}

//  GLint QOpenGLFunctions_3_2_Compatibility::glGetFragDataLocation(GLuint
//      program, const GLchar *name)
extern "C" Q_DECL_EXPORT
GLint ritual_ZN34QOpenGLFunctions_3_2_Compatibility21glGetFragDataLocationEjPKc(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint program,
    const GLchar *name) {
  return self->glGetFragDataLocation(program, name);
}

//  void QOpenGLFunctions_3_2_Compatibility::glBindFragDataLocation(GLuint
//      program, GLuint color, const GLchar *name)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility22glBindFragDataLocationEjjPKc(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint program,
    GLuint color,
    const GLchar *name) {
  self->glBindFragDataLocation(program, color, name);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGetUniformuiv(GLuint program,
//      GLint location, GLuint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility15glGetUniformuivEjiPj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint program,
    GLint location,
    GLuint *params) {
  self->glGetUniformuiv(program, location, params);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGetVertexAttribIuiv(GLuint
//      index, GLenum pname, GLuint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility21glGetVertexAttribIuivEjjPj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint index,
    GLenum pname,
    GLuint *params) {
  self->glGetVertexAttribIuiv(index, pname, params);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGetVertexAttribIiv(GLuint
//      index, GLenum pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility20glGetVertexAttribIivEjjPi(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint index,
    GLenum pname,
    GLint *params) {
  self->glGetVertexAttribIiv(index, pname, params);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertexAttribIPointer(GLuint
//      index, GLint size, GLenum type, GLsizei stride, const GLvoid
//      *pointer)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility22glVertexAttribIPointerEjijiPKv(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint index,
    GLint size,
    GLenum type,
    GLsizei stride,
    const GLvoid *pointer) {
  self->glVertexAttribIPointer(index, size, type, stride, pointer);
}

//  void QOpenGLFunctions_3_2_Compatibility::glEndConditionalRender()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility22glEndConditionalRenderEv(
    QOpenGLFunctions_3_2_Compatibility *self) {
  self->glEndConditionalRender();
}

//  void QOpenGLFunctions_3_2_Compatibility::glBeginConditionalRender(GLuint
//      id, GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility24glBeginConditionalRenderEjj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint id,
    GLenum mode) {
  self->glBeginConditionalRender(id, mode);
}

//  void QOpenGLFunctions_3_2_Compatibility::glClampColor(GLenum target,
//      GLenum clamp)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glClampColorEjj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLenum clamp) {
  self->glClampColor(target, clamp);
}

//  void
//      QOpenGLFunctions_3_2_Compatibility::glGetTransformFeedbackVarying(GLu
//      int program, GLuint index, GLsizei bufSize, GLsizei *length, GLsizei
//      *size, GLenum *type, GLchar *name)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility29glGetTransformFeedbackVaryingEjjiPiS0_PjPc(
    QOpenGLFunctions_3_2_Compatibility *self,
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

//  void
//      QOpenGLFunctions_3_2_Compatibility::glTransformFeedbackVaryings(GLuin
//      t program, GLsizei count, const GLchar *const *varyings, GLenum
//      bufferMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility27glTransformFeedbackVaryingsEjiPKPKcj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint program,
    GLsizei count,
    const GLchar *const *varyings,
    GLenum bufferMode) {
  self->glTransformFeedbackVaryings(program, count, varyings, bufferMode);
}

//  void QOpenGLFunctions_3_2_Compatibility::glBindBufferBase(GLenum target,
//      GLuint index, GLuint buffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility16glBindBufferBaseEjjj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLuint index,
    GLuint buffer) {
  self->glBindBufferBase(target, index, buffer);
}

//  void QOpenGLFunctions_3_2_Compatibility::glBindBufferRange(GLenum target,
//      GLuint index, GLuint buffer, GLintptr offset, GLsizeiptr size)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility17glBindBufferRangeEjjjll(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLuint index,
    GLuint buffer,
    long long offset,
    long long size) {
  self->glBindBufferRange(target, index, buffer, offset, size);
}

//  void QOpenGLFunctions_3_2_Compatibility::glEndTransformFeedback()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility22glEndTransformFeedbackEv(
    QOpenGLFunctions_3_2_Compatibility *self) {
  self->glEndTransformFeedback();
}

//  void QOpenGLFunctions_3_2_Compatibility::glBeginTransformFeedback(GLenum
//      primitiveMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility24glBeginTransformFeedbackEj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum primitiveMode) {
  self->glBeginTransformFeedback(primitiveMode);
}

//  GLboolean QOpenGLFunctions_3_2_Compatibility::glIsEnabledi(GLenum target,
//      GLuint index)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glIsEnablediEjj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLuint index) {
  return self->glIsEnabledi(target, index);
}

//  void QOpenGLFunctions_3_2_Compatibility::glDisablei(GLenum target, GLuint
//      index)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility10glDisableiEjj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLuint index) {
  self->glDisablei(target, index);
}

//  void QOpenGLFunctions_3_2_Compatibility::glEnablei(GLenum target, GLuint
//      index)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility9glEnableiEjj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLuint index) {
  self->glEnablei(target, index);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGetIntegeri_v(GLenum target,
//      GLuint index, GLint *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility15glGetIntegeri_vEjjPi(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLuint index,
    GLint *data) {
  self->glGetIntegeri_v(target, index, data);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGetBooleani_v(GLenum target,
//      GLuint index, GLboolean *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility15glGetBooleani_vEjjPh(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLuint index,
    GLboolean *data) {
  self->glGetBooleani_v(target, index, data);
}

//  void QOpenGLFunctions_3_2_Compatibility::glColorMaski(GLuint index,
//      GLboolean r, GLboolean g, GLboolean b, GLboolean a)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glColorMaskiEjhhhh(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint index,
    GLboolean r,
    GLboolean g,
    GLboolean b,
    GLboolean a) {
  self->glColorMaski(index, r, g, b, a);
}

//  void QOpenGLFunctions_3_2_Compatibility::glCopyBufferSubData(GLenum
//      readTarget, GLenum writeTarget, GLintptr readOffset, GLintptr
//      writeOffset, GLsizeiptr size)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility19glCopyBufferSubDataEjjlll(
    QOpenGLFunctions_3_2_Compatibility *self,
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

//  void QOpenGLFunctions_3_2_Compatibility::glUniformBlockBinding(GLuint
//      program, GLuint uniformBlockIndex, GLuint uniformBlockBinding)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility21glUniformBlockBindingEjjj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint program,
    GLuint uniformBlockIndex,
    GLuint uniformBlockBinding) {
  self->glUniformBlockBinding(
      program,
      uniformBlockIndex,
      uniformBlockBinding);
}

//  void
//      QOpenGLFunctions_3_2_Compatibility::glGetActiveUniformBlockName(GLuin
//      t program, GLuint uniformBlockIndex, GLsizei bufSize, GLsizei
//      *length, GLchar *uniformBlockName)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility27glGetActiveUniformBlockNameEjjiPiPc(
    QOpenGLFunctions_3_2_Compatibility *self,
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

//  void QOpenGLFunctions_3_2_Compatibility::glGetActiveUniformBlockiv(GLuint
//      program, GLuint uniformBlockIndex, GLenum pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility25glGetActiveUniformBlockivEjjjPi(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint program,
    GLuint uniformBlockIndex,
    GLenum pname,
    GLint *params) {
  self->glGetActiveUniformBlockiv(program, uniformBlockIndex, pname, params);
}

//  GLuint QOpenGLFunctions_3_2_Compatibility::glGetUniformBlockIndex(GLuint
//      program, const GLchar *uniformBlockName)
extern "C" Q_DECL_EXPORT
GLuint ritual_ZN34QOpenGLFunctions_3_2_Compatibility22glGetUniformBlockIndexEjPKc(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint program,
    const GLchar *uniformBlockName) {
  return self->glGetUniformBlockIndex(program, uniformBlockName);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGetActiveUniformName(GLuint
//      program, GLuint uniformIndex, GLsizei bufSize, GLsizei *length,
//      GLchar *uniformName)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility22glGetActiveUniformNameEjjiPiPc(
    QOpenGLFunctions_3_2_Compatibility *self,
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

//  void QOpenGLFunctions_3_2_Compatibility::glGetActiveUniformsiv(GLuint
//      program, GLsizei uniformCount, const GLuint *uniformIndices, GLenum
//      pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility21glGetActiveUniformsivEjiPKjjPi(
    QOpenGLFunctions_3_2_Compatibility *self,
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

//  void QOpenGLFunctions_3_2_Compatibility::glGetUniformIndices(GLuint
//      program, GLsizei uniformCount, const GLchar *const *uniformNames,
//      GLuint *uniformIndices)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility19glGetUniformIndicesEjiPKPKcPj(
    QOpenGLFunctions_3_2_Compatibility *self,
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

//  void QOpenGLFunctions_3_2_Compatibility::glPrimitiveRestartIndex(GLuint
//      index)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility23glPrimitiveRestartIndexEj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint index) {
  self->glPrimitiveRestartIndex(index);
}

//  void QOpenGLFunctions_3_2_Compatibility::glTexBuffer(GLenum target,
//      GLenum internalformat, GLuint buffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility11glTexBufferEjjj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLenum internalformat,
    GLuint buffer) {
  self->glTexBuffer(target, internalformat, buffer);
}

//  void QOpenGLFunctions_3_2_Compatibility::glDrawElementsInstanced(GLenum
//      mode, GLsizei count, GLenum type, const GLvoid *indices, GLsizei
//      instancecount)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility23glDrawElementsInstancedEjijPKvi(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum mode,
    GLsizei count,
    GLenum type,
    const GLvoid *indices,
    GLsizei instancecount) {
  self->glDrawElementsInstanced(mode, count, type, indices, instancecount);
}

//  void QOpenGLFunctions_3_2_Compatibility::glDrawArraysInstanced(GLenum
//      mode, GLint first, GLsizei count, GLsizei instancecount)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility21glDrawArraysInstancedEjiii(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum mode,
    GLint first,
    GLsizei count,
    GLsizei instancecount) {
  self->glDrawArraysInstanced(mode, first, count, instancecount);
}

//  void QOpenGLFunctions_3_2_Compatibility::glSampleMaski(GLuint index,
//      GLbitfield mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glSampleMaskiEjj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint index,
    GLbitfield mask) {
  self->glSampleMaski(index, mask);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGetMultisamplefv(GLenum pname,
//      GLuint index, GLfloat *val)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility18glGetMultisamplefvEjjPf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum pname,
    GLuint index,
    GLfloat *val) {
  self->glGetMultisamplefv(pname, index, val);
}

//  void QOpenGLFunctions_3_2_Compatibility::glTexImage3DMultisample(GLenum
//      target, GLsizei samples, GLint internalformat, GLsizei width, GLsizei
//      height, GLsizei depth, GLboolean fixedsamplelocations)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility23glTexImage3DMultisampleEjiiiiih(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLsizei samples,
    GLint internalformat,
    GLsizei width,
    GLsizei height,
    GLsizei depth,
    GLboolean fixedsamplelocations) {
  self->glTexImage3DMultisample(
      target,
      samples,
      internalformat,
      width,
      height,
      depth,
      fixedsamplelocations);
}

//  void QOpenGLFunctions_3_2_Compatibility::glTexImage2DMultisample(GLenum
//      target, GLsizei samples, GLint internalformat, GLsizei width, GLsizei
//      height, GLboolean fixedsamplelocations)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility23glTexImage2DMultisampleEjiiiih(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLsizei samples,
    GLint internalformat,
    GLsizei width,
    GLsizei height,
    GLboolean fixedsamplelocations) {
  self->glTexImage2DMultisample(
      target,
      samples,
      internalformat,
      width,
      height,
      fixedsamplelocations);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGetSynciv(GLsync sync, GLenum
//      pname, GLsizei bufSize, GLsizei *length, GLint *values)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility11glGetSyncivEP8__GLsyncjiPiS2_(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLsync sync,
    GLenum pname,
    GLsizei bufSize,
    GLsizei *length,
    GLint *values) {
  self->glGetSynciv(sync, pname, bufSize, length, values);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGetInteger64v(GLenum pname,
//      GLint64 *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility15glGetInteger64vEjPl(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum pname,
    GLint64 *params) {
  self->glGetInteger64v(pname, params);
}

//  void QOpenGLFunctions_3_2_Compatibility::glWaitSync(GLsync sync,
//      GLbitfield flags, GLuint64 timeout)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility10glWaitSyncEP8__GLsyncjm(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLsync sync,
    GLbitfield flags,
    unsigned long long timeout) {
  self->glWaitSync(sync, flags, timeout);
}

//  GLenum QOpenGLFunctions_3_2_Compatibility::glClientWaitSync(GLsync sync,
//      GLbitfield flags, GLuint64 timeout)
extern "C" Q_DECL_EXPORT
GLenum ritual_ZN34QOpenGLFunctions_3_2_Compatibility16glClientWaitSyncEP8__GLsyncjm(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLsync sync,
    GLbitfield flags,
    unsigned long long timeout) {
  return self->glClientWaitSync(sync, flags, timeout);
}

//  void QOpenGLFunctions_3_2_Compatibility::glDeleteSync(GLsync sync)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glDeleteSyncEP8__GLsync(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLsync sync) {
  self->glDeleteSync(sync);
}

//  GLboolean QOpenGLFunctions_3_2_Compatibility::glIsSync(GLsync sync)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN34QOpenGLFunctions_3_2_Compatibility8glIsSyncEP8__GLsync(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLsync sync) {
  return self->glIsSync(sync);
}

//  GLsync QOpenGLFunctions_3_2_Compatibility::glFenceSync(GLenum condition,
//      GLbitfield flags)
extern "C" Q_DECL_EXPORT
GLsync ritual_ZN34QOpenGLFunctions_3_2_Compatibility11glFenceSyncEjj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum condition,
    GLbitfield flags) {
  return self->glFenceSync(condition, flags);
}

//  void QOpenGLFunctions_3_2_Compatibility::glProvokingVertex(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility17glProvokingVertexEj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum mode) {
  self->glProvokingVertex(mode);
}

//  void
//      QOpenGLFunctions_3_2_Compatibility::glMultiDrawElementsBaseVertex(GLe
//      num mode, const GLsizei *count, GLenum type, const GLvoid *const
//      *indices, GLsizei drawcount, const GLint *basevertex)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility29glMultiDrawElementsBaseVertexEjPKijPKPKviS1_(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum mode,
    const GLsizei *count,
    GLenum type,
    const GLvoid *const *indices,
    GLsizei drawcount,
    const GLint *basevertex) {
  self->glMultiDrawElementsBaseVertex(
      mode,
      count,
      type,
      indices,
      drawcount,
      basevertex);
}

//  void QOpenGLFunctions_3_2_Compatibility::glDrawElementsInstancedBaseVerte
//      x(GLenum mode, GLsizei count, GLenum type, const GLvoid *indices,
//      GLsizei instancecount, GLint basevertex)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility33glDrawElementsInstancedBaseVertexEjijPKvii(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum mode,
    GLsizei count,
    GLenum type,
    const GLvoid *indices,
    GLsizei instancecount,
    GLint basevertex) {
  self->glDrawElementsInstancedBaseVertex(
      mode,
      count,
      type,
      indices,
      instancecount,
      basevertex);
}

//  void
//      QOpenGLFunctions_3_2_Compatibility::glDrawRangeElementsBaseVertex(GLe
//      num mode, GLuint start, GLuint end, GLsizei count, GLenum type, const
//      GLvoid *indices, GLint basevertex)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility29glDrawRangeElementsBaseVertexEjjjijPKvi(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum mode,
    GLuint start,
    GLuint end,
    GLsizei count,
    GLenum type,
    const GLvoid *indices,
    GLint basevertex) {
  self->glDrawRangeElementsBaseVertex(
      mode,
      start,
      end,
      count,
      type,
      indices,
      basevertex);
}

//  void QOpenGLFunctions_3_2_Compatibility::glDrawElementsBaseVertex(GLenum
//      mode, GLsizei count, GLenum type, const GLvoid *indices, GLint
//      basevertex)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility24glDrawElementsBaseVertexEjijPKvi(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum mode,
    GLsizei count,
    GLenum type,
    const GLvoid *indices,
    GLint basevertex) {
  self->glDrawElementsBaseVertex(mode, count, type, indices, basevertex);
}

//  void QOpenGLFunctions_3_2_Compatibility::glFramebufferTexture(GLenum
//      target, GLenum attachment, GLuint texture, GLint level)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility20glFramebufferTextureEjjji(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLenum attachment,
    GLuint texture,
    GLint level) {
  self->glFramebufferTexture(target, attachment, texture, level);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGetBufferParameteri64v(GLenum
//      target, GLenum pname, GLint64 *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility24glGetBufferParameteri64vEjjPl(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLenum pname,
    GLint64 *params) {
  self->glGetBufferParameteri64v(target, pname, params);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGetInteger64i_v(GLenum target,
//      GLuint index, GLint64 *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility17glGetInteger64i_vEjjPl(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLuint index,
    GLint64 *data) {
  self->glGetInteger64i_v(target, index, data);
}

//  void QOpenGLFunctions_3_2_Compatibility::glTranslatef(GLfloat x, GLfloat
//      y, GLfloat z)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glTranslatefEfff(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLfloat x,
    GLfloat y,
    GLfloat z) {
  self->glTranslatef(x, y, z);
}

//  void QOpenGLFunctions_3_2_Compatibility::glTranslated(GLdouble x,
//      GLdouble y, GLdouble z)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glTranslatedEddd(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLdouble x,
    GLdouble y,
    GLdouble z) {
  self->glTranslated(x, y, z);
}

//  void QOpenGLFunctions_3_2_Compatibility::glScalef(GLfloat x, GLfloat y,
//      GLfloat z)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility8glScalefEfff(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLfloat x,
    GLfloat y,
    GLfloat z) {
  self->glScalef(x, y, z);
}

//  void QOpenGLFunctions_3_2_Compatibility::glScaled(GLdouble x, GLdouble y,
//      GLdouble z)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility8glScaledEddd(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLdouble x,
    GLdouble y,
    GLdouble z) {
  self->glScaled(x, y, z);
}

//  void QOpenGLFunctions_3_2_Compatibility::glRotatef(GLfloat angle, GLfloat
//      x, GLfloat y, GLfloat z)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility9glRotatefEffff(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLfloat angle,
    GLfloat x,
    GLfloat y,
    GLfloat z) {
  self->glRotatef(angle, x, y, z);
}

//  void QOpenGLFunctions_3_2_Compatibility::glRotated(GLdouble angle,
//      GLdouble x, GLdouble y, GLdouble z)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility9glRotatedEdddd(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLdouble angle,
    GLdouble x,
    GLdouble y,
    GLdouble z) {
  self->glRotated(angle, x, y, z);
}

//  void QOpenGLFunctions_3_2_Compatibility::glPushMatrix()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glPushMatrixEv(
    QOpenGLFunctions_3_2_Compatibility *self) {
  self->glPushMatrix();
}

//  void QOpenGLFunctions_3_2_Compatibility::glPopMatrix()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility11glPopMatrixEv(
    QOpenGLFunctions_3_2_Compatibility *self) {
  self->glPopMatrix();
}

//  void QOpenGLFunctions_3_2_Compatibility::glOrtho(GLdouble left, GLdouble
//      right, GLdouble bottom, GLdouble top, GLdouble zNear, GLdouble zFar)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility7glOrthoEdddddd(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLdouble left,
    GLdouble right,
    GLdouble bottom,
    GLdouble top,
    GLdouble zNear,
    GLdouble zFar) {
  self->glOrtho(left, right, bottom, top, zNear, zFar);
}

//  void QOpenGLFunctions_3_2_Compatibility::glMultMatrixd(const GLdouble *m)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glMultMatrixdEPKd(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLdouble *m) {
  self->glMultMatrixd(m);
}

//  void QOpenGLFunctions_3_2_Compatibility::glMultMatrixf(const GLfloat *m)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glMultMatrixfEPKf(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLfloat *m) {
  self->glMultMatrixf(m);
}

//  void QOpenGLFunctions_3_2_Compatibility::glMatrixMode(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glMatrixModeEj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum mode) {
  self->glMatrixMode(mode);
}

//  void QOpenGLFunctions_3_2_Compatibility::glLoadMatrixd(const GLdouble *m)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glLoadMatrixdEPKd(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLdouble *m) {
  self->glLoadMatrixd(m);
}

//  void QOpenGLFunctions_3_2_Compatibility::glLoadMatrixf(const GLfloat *m)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glLoadMatrixfEPKf(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLfloat *m) {
  self->glLoadMatrixf(m);
}

//  void QOpenGLFunctions_3_2_Compatibility::glLoadIdentity()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility14glLoadIdentityEv(
    QOpenGLFunctions_3_2_Compatibility *self) {
  self->glLoadIdentity();
}

//  void QOpenGLFunctions_3_2_Compatibility::glFrustum(GLdouble left,
//      GLdouble right, GLdouble bottom, GLdouble top, GLdouble zNear,
//      GLdouble zFar)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility9glFrustumEdddddd(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLdouble left,
    GLdouble right,
    GLdouble bottom,
    GLdouble top,
    GLdouble zNear,
    GLdouble zFar) {
  self->glFrustum(left, right, bottom, top, zNear, zFar);
}

//  GLboolean QOpenGLFunctions_3_2_Compatibility::glIsList(GLuint list)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN34QOpenGLFunctions_3_2_Compatibility8glIsListEj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint list) {
  return self->glIsList(list);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGetTexGeniv(GLenum coord,
//      GLenum pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glGetTexGenivEjjPi(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum coord,
    GLenum pname,
    GLint *params) {
  self->glGetTexGeniv(coord, pname, params);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGetTexGenfv(GLenum coord,
//      GLenum pname, GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glGetTexGenfvEjjPf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum coord,
    GLenum pname,
    GLfloat *params) {
  self->glGetTexGenfv(coord, pname, params);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGetTexGendv(GLenum coord,
//      GLenum pname, GLdouble *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glGetTexGendvEjjPd(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum coord,
    GLenum pname,
    GLdouble *params) {
  self->glGetTexGendv(coord, pname, params);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGetTexEnviv(GLenum target,
//      GLenum pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glGetTexEnvivEjjPi(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLenum pname,
    GLint *params) {
  self->glGetTexEnviv(target, pname, params);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGetTexEnvfv(GLenum target,
//      GLenum pname, GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glGetTexEnvfvEjjPf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLenum pname,
    GLfloat *params) {
  self->glGetTexEnvfv(target, pname, params);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGetPolygonStipple(GLubyte
//      *mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility19glGetPolygonStippleEPh(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLubyte *mask) {
  self->glGetPolygonStipple(mask);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGetPixelMapusv(GLenum map,
//      GLushort *values)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility16glGetPixelMapusvEjPt(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum map,
    GLushort *values) {
  self->glGetPixelMapusv(map, values);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGetPixelMapuiv(GLenum map,
//      GLuint *values)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility16glGetPixelMapuivEjPj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum map,
    GLuint *values) {
  self->glGetPixelMapuiv(map, values);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGetPixelMapfv(GLenum map,
//      GLfloat *values)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility15glGetPixelMapfvEjPf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum map,
    GLfloat *values) {
  self->glGetPixelMapfv(map, values);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGetMaterialiv(GLenum face,
//      GLenum pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility15glGetMaterialivEjjPi(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum face,
    GLenum pname,
    GLint *params) {
  self->glGetMaterialiv(face, pname, params);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGetMaterialfv(GLenum face,
//      GLenum pname, GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility15glGetMaterialfvEjjPf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum face,
    GLenum pname,
    GLfloat *params) {
  self->glGetMaterialfv(face, pname, params);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGetMapiv(GLenum target, GLenum
//      query, GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility10glGetMapivEjjPi(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLenum query,
    GLint *v) {
  self->glGetMapiv(target, query, v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGetMapfv(GLenum target, GLenum
//      query, GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility10glGetMapfvEjjPf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLenum query,
    GLfloat *v) {
  self->glGetMapfv(target, query, v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGetMapdv(GLenum target, GLenum
//      query, GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility10glGetMapdvEjjPd(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLenum query,
    GLdouble *v) {
  self->glGetMapdv(target, query, v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGetLightiv(GLenum light,
//      GLenum pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glGetLightivEjjPi(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum light,
    GLenum pname,
    GLint *params) {
  self->glGetLightiv(light, pname, params);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGetLightfv(GLenum light,
//      GLenum pname, GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glGetLightfvEjjPf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum light,
    GLenum pname,
    GLfloat *params) {
  self->glGetLightfv(light, pname, params);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGetClipPlane(GLenum plane,
//      GLdouble *equation)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility14glGetClipPlaneEjPd(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum plane,
    GLdouble *equation) {
  self->glGetClipPlane(plane, equation);
}

//  void QOpenGLFunctions_3_2_Compatibility::glDrawPixels(GLsizei width,
//      GLsizei height, GLenum format, GLenum type, const GLvoid *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glDrawPixelsEiijjPKv(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLsizei width,
    GLsizei height,
    GLenum format,
    GLenum type,
    const GLvoid *pixels) {
  self->glDrawPixels(width, height, format, type, pixels);
}

//  void QOpenGLFunctions_3_2_Compatibility::glCopyPixels(GLint x, GLint y,
//      GLsizei width, GLsizei height, GLenum type)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glCopyPixelsEiiiij(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLint x,
    GLint y,
    GLsizei width,
    GLsizei height,
    GLenum type) {
  self->glCopyPixels(x, y, width, height, type);
}

//  void QOpenGLFunctions_3_2_Compatibility::glPixelMapusv(GLenum map, GLint
//      mapsize, const GLushort *values)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glPixelMapusvEjiPKt(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum map,
    GLint mapsize,
    const GLushort *values) {
  self->glPixelMapusv(map, mapsize, values);
}

//  void QOpenGLFunctions_3_2_Compatibility::glPixelMapuiv(GLenum map, GLint
//      mapsize, const GLuint *values)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glPixelMapuivEjiPKj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum map,
    GLint mapsize,
    const GLuint *values) {
  self->glPixelMapuiv(map, mapsize, values);
}

//  void QOpenGLFunctions_3_2_Compatibility::glPixelMapfv(GLenum map, GLint
//      mapsize, const GLfloat *values)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glPixelMapfvEjiPKf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum map,
    GLint mapsize,
    const GLfloat *values) {
  self->glPixelMapfv(map, mapsize, values);
}

//  void QOpenGLFunctions_3_2_Compatibility::glPixelTransferi(GLenum pname,
//      GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility16glPixelTransferiEji(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum pname,
    GLint param) {
  self->glPixelTransferi(pname, param);
}

//  void QOpenGLFunctions_3_2_Compatibility::glPixelTransferf(GLenum pname,
//      GLfloat param)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility16glPixelTransferfEjf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum pname,
    GLfloat param) {
  self->glPixelTransferf(pname, param);
}

//  void QOpenGLFunctions_3_2_Compatibility::glPixelZoom(GLfloat xfactor,
//      GLfloat yfactor)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility11glPixelZoomEff(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLfloat xfactor,
    GLfloat yfactor) {
  self->glPixelZoom(xfactor, yfactor);
}

//  void QOpenGLFunctions_3_2_Compatibility::glAlphaFunc(GLenum func, GLfloat
//      ref)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility11glAlphaFuncEjf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum func,
    GLfloat ref) {
  self->glAlphaFunc(func, ref);
}

//  void QOpenGLFunctions_3_2_Compatibility::glEvalPoint2(GLint i, GLint j)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glEvalPoint2Eii(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLint i,
    GLint j) {
  self->glEvalPoint2(i, j);
}

//  void QOpenGLFunctions_3_2_Compatibility::glEvalMesh2(GLenum mode, GLint
//      i1, GLint i2, GLint j1, GLint j2)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility11glEvalMesh2Ejiiii(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum mode,
    GLint i1,
    GLint i2,
    GLint j1,
    GLint j2) {
  self->glEvalMesh2(mode, i1, i2, j1, j2);
}

//  void QOpenGLFunctions_3_2_Compatibility::glEvalPoint1(GLint i)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glEvalPoint1Ei(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLint i) {
  self->glEvalPoint1(i);
}

//  void QOpenGLFunctions_3_2_Compatibility::glEvalMesh1(GLenum mode, GLint
//      i1, GLint i2)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility11glEvalMesh1Ejii(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum mode,
    GLint i1,
    GLint i2) {
  self->glEvalMesh1(mode, i1, i2);
}

//  void QOpenGLFunctions_3_2_Compatibility::glEvalCoord2fv(const GLfloat *u)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility14glEvalCoord2fvEPKf(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLfloat *u) {
  self->glEvalCoord2fv(u);
}

//  void QOpenGLFunctions_3_2_Compatibility::glEvalCoord2f(GLfloat u, GLfloat
//      v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glEvalCoord2fEff(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLfloat u,
    GLfloat v) {
  self->glEvalCoord2f(u, v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glEvalCoord2dv(const GLdouble
//      *u)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility14glEvalCoord2dvEPKd(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLdouble *u) {
  self->glEvalCoord2dv(u);
}

//  void QOpenGLFunctions_3_2_Compatibility::glEvalCoord2d(GLdouble u,
//      GLdouble v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glEvalCoord2dEdd(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLdouble u,
    GLdouble v) {
  self->glEvalCoord2d(u, v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glEvalCoord1fv(const GLfloat *u)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility14glEvalCoord1fvEPKf(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLfloat *u) {
  self->glEvalCoord1fv(u);
}

//  void QOpenGLFunctions_3_2_Compatibility::glEvalCoord1f(GLfloat u)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glEvalCoord1fEf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLfloat u) {
  self->glEvalCoord1f(u);
}

//  void QOpenGLFunctions_3_2_Compatibility::glEvalCoord1dv(const GLdouble
//      *u)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility14glEvalCoord1dvEPKd(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLdouble *u) {
  self->glEvalCoord1dv(u);
}

//  void QOpenGLFunctions_3_2_Compatibility::glEvalCoord1d(GLdouble u)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glEvalCoord1dEd(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLdouble u) {
  self->glEvalCoord1d(u);
}

//  void QOpenGLFunctions_3_2_Compatibility::glMapGrid2f(GLint un, GLfloat
//      u1, GLfloat u2, GLint vn, GLfloat v1, GLfloat v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility11glMapGrid2fEiffiff(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLint un,
    GLfloat u1,
    GLfloat u2,
    GLint vn,
    GLfloat v1,
    GLfloat v2) {
  self->glMapGrid2f(un, u1, u2, vn, v1, v2);
}

//  void QOpenGLFunctions_3_2_Compatibility::glMapGrid2d(GLint un, GLdouble
//      u1, GLdouble u2, GLint vn, GLdouble v1, GLdouble v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility11glMapGrid2dEiddidd(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLint un,
    GLdouble u1,
    GLdouble u2,
    GLint vn,
    GLdouble v1,
    GLdouble v2) {
  self->glMapGrid2d(un, u1, u2, vn, v1, v2);
}

//  void QOpenGLFunctions_3_2_Compatibility::glMapGrid1f(GLint un, GLfloat
//      u1, GLfloat u2)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility11glMapGrid1fEiff(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLint un,
    GLfloat u1,
    GLfloat u2) {
  self->glMapGrid1f(un, u1, u2);
}

//  void QOpenGLFunctions_3_2_Compatibility::glMapGrid1d(GLint un, GLdouble
//      u1, GLdouble u2)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility11glMapGrid1dEidd(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLint un,
    GLdouble u1,
    GLdouble u2) {
  self->glMapGrid1d(un, u1, u2);
}

//  void QOpenGLFunctions_3_2_Compatibility::glMap2f(GLenum target, GLfloat
//      u1, GLfloat u2, GLint ustride, GLint uorder, GLfloat v1, GLfloat v2,
//      GLint vstride, GLint vorder, const GLfloat *points)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility7glMap2fEjffiiffiiPKf(
    QOpenGLFunctions_3_2_Compatibility *self,
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

//  void QOpenGLFunctions_3_2_Compatibility::glMap2d(GLenum target, GLdouble
//      u1, GLdouble u2, GLint ustride, GLint uorder, GLdouble v1, GLdouble
//      v2, GLint vstride, GLint vorder, const GLdouble *points)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility7glMap2dEjddiiddiiPKd(
    QOpenGLFunctions_3_2_Compatibility *self,
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

//  void QOpenGLFunctions_3_2_Compatibility::glMap1f(GLenum target, GLfloat
//      u1, GLfloat u2, GLint stride, GLint order, const GLfloat *points)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility7glMap1fEjffiiPKf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLfloat u1,
    GLfloat u2,
    GLint stride,
    GLint order,
    const GLfloat *points) {
  self->glMap1f(target, u1, u2, stride, order, points);
}

//  void QOpenGLFunctions_3_2_Compatibility::glMap1d(GLenum target, GLdouble
//      u1, GLdouble u2, GLint stride, GLint order, const GLdouble *points)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility7glMap1dEjddiiPKd(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLdouble u1,
    GLdouble u2,
    GLint stride,
    GLint order,
    const GLdouble *points) {
  self->glMap1d(target, u1, u2, stride, order, points);
}

//  void QOpenGLFunctions_3_2_Compatibility::glPushAttrib(GLbitfield mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glPushAttribEj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLbitfield mask) {
  self->glPushAttrib(mask);
}

//  void QOpenGLFunctions_3_2_Compatibility::glPopAttrib()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility11glPopAttribEv(
    QOpenGLFunctions_3_2_Compatibility *self) {
  self->glPopAttrib();
}

//  void QOpenGLFunctions_3_2_Compatibility::glAccum(GLenum op, GLfloat
//      value)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility7glAccumEjf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum op,
    GLfloat value) {
  self->glAccum(op, value);
}

//  void QOpenGLFunctions_3_2_Compatibility::glIndexMask(GLuint mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility11glIndexMaskEj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint mask) {
  self->glIndexMask(mask);
}

//  void QOpenGLFunctions_3_2_Compatibility::glClearIndex(GLfloat c)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glClearIndexEf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLfloat c) {
  self->glClearIndex(c);
}

//  void QOpenGLFunctions_3_2_Compatibility::glClearAccum(GLfloat red,
//      GLfloat green, GLfloat blue, GLfloat alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glClearAccumEffff(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLfloat red,
    GLfloat green,
    GLfloat blue,
    GLfloat alpha) {
  self->glClearAccum(red, green, blue, alpha);
}

//  void QOpenGLFunctions_3_2_Compatibility::glPushName(GLuint name)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility10glPushNameEj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint name) {
  self->glPushName(name);
}

//  void QOpenGLFunctions_3_2_Compatibility::glPopName()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility9glPopNameEv(
    QOpenGLFunctions_3_2_Compatibility *self) {
  self->glPopName();
}

//  void QOpenGLFunctions_3_2_Compatibility::glPassThrough(GLfloat token)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glPassThroughEf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLfloat token) {
  self->glPassThrough(token);
}

//  void QOpenGLFunctions_3_2_Compatibility::glLoadName(GLuint name)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility10glLoadNameEj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint name) {
  self->glLoadName(name);
}

//  void QOpenGLFunctions_3_2_Compatibility::glInitNames()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility11glInitNamesEv(
    QOpenGLFunctions_3_2_Compatibility *self) {
  self->glInitNames();
}

//  GLint QOpenGLFunctions_3_2_Compatibility::glRenderMode(GLenum mode)
extern "C" Q_DECL_EXPORT
GLint ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glRenderModeEj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum mode) {
  return self->glRenderMode(mode);
}

//  void QOpenGLFunctions_3_2_Compatibility::glSelectBuffer(GLsizei size,
//      GLuint *buffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility14glSelectBufferEiPj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLsizei size,
    GLuint *buffer) {
  self->glSelectBuffer(size, buffer);
}

//  void QOpenGLFunctions_3_2_Compatibility::glFeedbackBuffer(GLsizei size,
//      GLenum type, GLfloat *buffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility16glFeedbackBufferEijPf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLsizei size,
    GLenum type,
    GLfloat *buffer) {
  self->glFeedbackBuffer(size, type, buffer);
}

//  void QOpenGLFunctions_3_2_Compatibility::glTexGeniv(GLenum coord, GLenum
//      pname, const GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility10glTexGenivEjjPKi(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum coord,
    GLenum pname,
    const GLint *params) {
  self->glTexGeniv(coord, pname, params);
}

//  void QOpenGLFunctions_3_2_Compatibility::glTexGeni(GLenum coord, GLenum
//      pname, GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility9glTexGeniEjji(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum coord,
    GLenum pname,
    GLint param) {
  self->glTexGeni(coord, pname, param);
}

//  void QOpenGLFunctions_3_2_Compatibility::glTexGenfv(GLenum coord, GLenum
//      pname, const GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility10glTexGenfvEjjPKf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum coord,
    GLenum pname,
    const GLfloat *params) {
  self->glTexGenfv(coord, pname, params);
}

//  void QOpenGLFunctions_3_2_Compatibility::glTexGenf(GLenum coord, GLenum
//      pname, GLfloat param)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility9glTexGenfEjjf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum coord,
    GLenum pname,
    GLfloat param) {
  self->glTexGenf(coord, pname, param);
}

//  void QOpenGLFunctions_3_2_Compatibility::glTexGendv(GLenum coord, GLenum
//      pname, const GLdouble *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility10glTexGendvEjjPKd(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum coord,
    GLenum pname,
    const GLdouble *params) {
  self->glTexGendv(coord, pname, params);
}

//  void QOpenGLFunctions_3_2_Compatibility::glTexGend(GLenum coord, GLenum
//      pname, GLdouble param)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility9glTexGendEjjd(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum coord,
    GLenum pname,
    GLdouble param) {
  self->glTexGend(coord, pname, param);
}

//  void QOpenGLFunctions_3_2_Compatibility::glTexEnviv(GLenum target, GLenum
//      pname, const GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility10glTexEnvivEjjPKi(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLenum pname,
    const GLint *params) {
  self->glTexEnviv(target, pname, params);
}

//  void QOpenGLFunctions_3_2_Compatibility::glTexEnvi(GLenum target, GLenum
//      pname, GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility9glTexEnviEjji(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLenum pname,
    GLint param) {
  self->glTexEnvi(target, pname, param);
}

//  void QOpenGLFunctions_3_2_Compatibility::glTexEnvfv(GLenum target, GLenum
//      pname, const GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility10glTexEnvfvEjjPKf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLenum pname,
    const GLfloat *params) {
  self->glTexEnvfv(target, pname, params);
}

//  void QOpenGLFunctions_3_2_Compatibility::glTexEnvf(GLenum target, GLenum
//      pname, GLfloat param)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility9glTexEnvfEjjf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLenum pname,
    GLfloat param) {
  self->glTexEnvf(target, pname, param);
}

//  void QOpenGLFunctions_3_2_Compatibility::glShadeModel(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glShadeModelEj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum mode) {
  self->glShadeModel(mode);
}

//  void QOpenGLFunctions_3_2_Compatibility::glPolygonStipple(const GLubyte
//      *mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility16glPolygonStippleEPKh(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLubyte *mask) {
  self->glPolygonStipple(mask);
}

//  void QOpenGLFunctions_3_2_Compatibility::glMaterialiv(GLenum face, GLenum
//      pname, const GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glMaterialivEjjPKi(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum face,
    GLenum pname,
    const GLint *params) {
  self->glMaterialiv(face, pname, params);
}

//  void QOpenGLFunctions_3_2_Compatibility::glMateriali(GLenum face, GLenum
//      pname, GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility11glMaterialiEjji(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum face,
    GLenum pname,
    GLint param) {
  self->glMateriali(face, pname, param);
}

//  void QOpenGLFunctions_3_2_Compatibility::glMaterialfv(GLenum face, GLenum
//      pname, const GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glMaterialfvEjjPKf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum face,
    GLenum pname,
    const GLfloat *params) {
  self->glMaterialfv(face, pname, params);
}

//  void QOpenGLFunctions_3_2_Compatibility::glMaterialf(GLenum face, GLenum
//      pname, GLfloat param)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility11glMaterialfEjjf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum face,
    GLenum pname,
    GLfloat param) {
  self->glMaterialf(face, pname, param);
}

//  void QOpenGLFunctions_3_2_Compatibility::glLineStipple(GLint factor,
//      GLushort pattern)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glLineStippleEit(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLint factor,
    GLushort pattern) {
  self->glLineStipple(factor, pattern);
}

//  void QOpenGLFunctions_3_2_Compatibility::glLightModeliv(GLenum pname,
//      const GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility14glLightModelivEjPKi(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum pname,
    const GLint *params) {
  self->glLightModeliv(pname, params);
}

//  void QOpenGLFunctions_3_2_Compatibility::glLightModeli(GLenum pname,
//      GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glLightModeliEji(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum pname,
    GLint param) {
  self->glLightModeli(pname, param);
}

//  void QOpenGLFunctions_3_2_Compatibility::glLightModelfv(GLenum pname,
//      const GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility14glLightModelfvEjPKf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum pname,
    const GLfloat *params) {
  self->glLightModelfv(pname, params);
}

//  void QOpenGLFunctions_3_2_Compatibility::glLightModelf(GLenum pname,
//      GLfloat param)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glLightModelfEjf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum pname,
    GLfloat param) {
  self->glLightModelf(pname, param);
}

//  void QOpenGLFunctions_3_2_Compatibility::glLightiv(GLenum light, GLenum
//      pname, const GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility9glLightivEjjPKi(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum light,
    GLenum pname,
    const GLint *params) {
  self->glLightiv(light, pname, params);
}

//  void QOpenGLFunctions_3_2_Compatibility::glLighti(GLenum light, GLenum
//      pname, GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility8glLightiEjji(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum light,
    GLenum pname,
    GLint param) {
  self->glLighti(light, pname, param);
}

//  void QOpenGLFunctions_3_2_Compatibility::glLightfv(GLenum light, GLenum
//      pname, const GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility9glLightfvEjjPKf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum light,
    GLenum pname,
    const GLfloat *params) {
  self->glLightfv(light, pname, params);
}

//  void QOpenGLFunctions_3_2_Compatibility::glLightf(GLenum light, GLenum
//      pname, GLfloat param)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility8glLightfEjjf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum light,
    GLenum pname,
    GLfloat param) {
  self->glLightf(light, pname, param);
}

//  void QOpenGLFunctions_3_2_Compatibility::glFogiv(GLenum pname, const
//      GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility7glFogivEjPKi(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum pname,
    const GLint *params) {
  self->glFogiv(pname, params);
}

//  void QOpenGLFunctions_3_2_Compatibility::glFogi(GLenum pname, GLint
//      param)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility6glFogiEji(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum pname,
    GLint param) {
  self->glFogi(pname, param);
}

//  void QOpenGLFunctions_3_2_Compatibility::glFogfv(GLenum pname, const
//      GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility7glFogfvEjPKf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum pname,
    const GLfloat *params) {
  self->glFogfv(pname, params);
}

//  void QOpenGLFunctions_3_2_Compatibility::glFogf(GLenum pname, GLfloat
//      param)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility6glFogfEjf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum pname,
    GLfloat param) {
  self->glFogf(pname, param);
}

//  void QOpenGLFunctions_3_2_Compatibility::glColorMaterial(GLenum face,
//      GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility15glColorMaterialEjj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum face,
    GLenum mode) {
  self->glColorMaterial(face, mode);
}

//  void QOpenGLFunctions_3_2_Compatibility::glClipPlane(GLenum plane, const
//      GLdouble *equation)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility11glClipPlaneEjPKd(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum plane,
    const GLdouble *equation) {
  self->glClipPlane(plane, equation);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertex4sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility11glVertex4svEPKs(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLshort *v) {
  self->glVertex4sv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertex4s(GLshort x, GLshort y,
//      GLshort z, GLshort w)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility10glVertex4sEssss(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLshort x,
    GLshort y,
    GLshort z,
    GLshort w) {
  self->glVertex4s(x, y, z, w);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertex4iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility11glVertex4ivEPKi(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLint *v) {
  self->glVertex4iv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertex4i(GLint x, GLint y,
//      GLint z, GLint w)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility10glVertex4iEiiii(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLint x,
    GLint y,
    GLint z,
    GLint w) {
  self->glVertex4i(x, y, z, w);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertex4fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility11glVertex4fvEPKf(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLfloat *v) {
  self->glVertex4fv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertex4f(GLfloat x, GLfloat y,
//      GLfloat z, GLfloat w)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility10glVertex4fEffff(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLfloat x,
    GLfloat y,
    GLfloat z,
    GLfloat w) {
  self->glVertex4f(x, y, z, w);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertex4dv(const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility11glVertex4dvEPKd(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLdouble *v) {
  self->glVertex4dv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertex4d(GLdouble x, GLdouble
//      y, GLdouble z, GLdouble w)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility10glVertex4dEdddd(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLdouble x,
    GLdouble y,
    GLdouble z,
    GLdouble w) {
  self->glVertex4d(x, y, z, w);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertex3sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility11glVertex3svEPKs(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLshort *v) {
  self->glVertex3sv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertex3s(GLshort x, GLshort y,
//      GLshort z)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility10glVertex3sEsss(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLshort x,
    GLshort y,
    GLshort z) {
  self->glVertex3s(x, y, z);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertex3iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility11glVertex3ivEPKi(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLint *v) {
  self->glVertex3iv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertex3i(GLint x, GLint y,
//      GLint z)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility10glVertex3iEiii(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLint x,
    GLint y,
    GLint z) {
  self->glVertex3i(x, y, z);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertex3fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility11glVertex3fvEPKf(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLfloat *v) {
  self->glVertex3fv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertex3f(GLfloat x, GLfloat y,
//      GLfloat z)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility10glVertex3fEfff(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLfloat x,
    GLfloat y,
    GLfloat z) {
  self->glVertex3f(x, y, z);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertex3dv(const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility11glVertex3dvEPKd(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLdouble *v) {
  self->glVertex3dv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertex3d(GLdouble x, GLdouble
//      y, GLdouble z)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility10glVertex3dEddd(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLdouble x,
    GLdouble y,
    GLdouble z) {
  self->glVertex3d(x, y, z);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertex2sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility11glVertex2svEPKs(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLshort *v) {
  self->glVertex2sv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertex2s(GLshort x, GLshort y)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility10glVertex2sEss(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLshort x,
    GLshort y) {
  self->glVertex2s(x, y);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertex2iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility11glVertex2ivEPKi(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLint *v) {
  self->glVertex2iv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertex2i(GLint x, GLint y)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility10glVertex2iEii(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLint x,
    GLint y) {
  self->glVertex2i(x, y);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertex2fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility11glVertex2fvEPKf(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLfloat *v) {
  self->glVertex2fv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertex2f(GLfloat x, GLfloat y)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility10glVertex2fEff(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLfloat x,
    GLfloat y) {
  self->glVertex2f(x, y);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertex2dv(const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility11glVertex2dvEPKd(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLdouble *v) {
  self->glVertex2dv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertex2d(GLdouble x, GLdouble
//      y)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility10glVertex2dEdd(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLdouble x,
    GLdouble y) {
  self->glVertex2d(x, y);
}

//  void QOpenGLFunctions_3_2_Compatibility::glTexCoord4sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glTexCoord4svEPKs(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLshort *v) {
  self->glTexCoord4sv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glTexCoord4s(GLshort s, GLshort
//      t, GLshort r, GLshort q)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glTexCoord4sEssss(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLshort s,
    GLshort t,
    GLshort r,
    GLshort q) {
  self->glTexCoord4s(s, t, r, q);
}

//  void QOpenGLFunctions_3_2_Compatibility::glTexCoord4iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glTexCoord4ivEPKi(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLint *v) {
  self->glTexCoord4iv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glTexCoord4i(GLint s, GLint t,
//      GLint r, GLint q)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glTexCoord4iEiiii(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLint s,
    GLint t,
    GLint r,
    GLint q) {
  self->glTexCoord4i(s, t, r, q);
}

//  void QOpenGLFunctions_3_2_Compatibility::glTexCoord4fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glTexCoord4fvEPKf(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLfloat *v) {
  self->glTexCoord4fv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glTexCoord4f(GLfloat s, GLfloat
//      t, GLfloat r, GLfloat q)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glTexCoord4fEffff(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLfloat s,
    GLfloat t,
    GLfloat r,
    GLfloat q) {
  self->glTexCoord4f(s, t, r, q);
}

//  void QOpenGLFunctions_3_2_Compatibility::glTexCoord4dv(const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glTexCoord4dvEPKd(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLdouble *v) {
  self->glTexCoord4dv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glTexCoord4d(GLdouble s,
//      GLdouble t, GLdouble r, GLdouble q)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glTexCoord4dEdddd(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLdouble s,
    GLdouble t,
    GLdouble r,
    GLdouble q) {
  self->glTexCoord4d(s, t, r, q);
}

//  void QOpenGLFunctions_3_2_Compatibility::glTexCoord3sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glTexCoord3svEPKs(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLshort *v) {
  self->glTexCoord3sv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glTexCoord3s(GLshort s, GLshort
//      t, GLshort r)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glTexCoord3sEsss(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLshort s,
    GLshort t,
    GLshort r) {
  self->glTexCoord3s(s, t, r);
}

//  void QOpenGLFunctions_3_2_Compatibility::glTexCoord3iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glTexCoord3ivEPKi(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLint *v) {
  self->glTexCoord3iv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glTexCoord3i(GLint s, GLint t,
//      GLint r)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glTexCoord3iEiii(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLint s,
    GLint t,
    GLint r) {
  self->glTexCoord3i(s, t, r);
}

//  void QOpenGLFunctions_3_2_Compatibility::glTexCoord3fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glTexCoord3fvEPKf(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLfloat *v) {
  self->glTexCoord3fv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glTexCoord3f(GLfloat s, GLfloat
//      t, GLfloat r)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glTexCoord3fEfff(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLfloat s,
    GLfloat t,
    GLfloat r) {
  self->glTexCoord3f(s, t, r);
}

//  void QOpenGLFunctions_3_2_Compatibility::glTexCoord3dv(const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glTexCoord3dvEPKd(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLdouble *v) {
  self->glTexCoord3dv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glTexCoord3d(GLdouble s,
//      GLdouble t, GLdouble r)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glTexCoord3dEddd(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLdouble s,
    GLdouble t,
    GLdouble r) {
  self->glTexCoord3d(s, t, r);
}

//  void QOpenGLFunctions_3_2_Compatibility::glTexCoord2sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glTexCoord2svEPKs(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLshort *v) {
  self->glTexCoord2sv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glTexCoord2s(GLshort s, GLshort
//      t)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glTexCoord2sEss(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLshort s,
    GLshort t) {
  self->glTexCoord2s(s, t);
}

//  void QOpenGLFunctions_3_2_Compatibility::glTexCoord2iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glTexCoord2ivEPKi(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLint *v) {
  self->glTexCoord2iv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glTexCoord2i(GLint s, GLint t)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glTexCoord2iEii(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLint s,
    GLint t) {
  self->glTexCoord2i(s, t);
}

//  void QOpenGLFunctions_3_2_Compatibility::glTexCoord2fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glTexCoord2fvEPKf(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLfloat *v) {
  self->glTexCoord2fv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glTexCoord2f(GLfloat s, GLfloat
//      t)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glTexCoord2fEff(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLfloat s,
    GLfloat t) {
  self->glTexCoord2f(s, t);
}

//  void QOpenGLFunctions_3_2_Compatibility::glTexCoord2dv(const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glTexCoord2dvEPKd(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLdouble *v) {
  self->glTexCoord2dv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glTexCoord2d(GLdouble s,
//      GLdouble t)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glTexCoord2dEdd(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLdouble s,
    GLdouble t) {
  self->glTexCoord2d(s, t);
}

//  void QOpenGLFunctions_3_2_Compatibility::glTexCoord1sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glTexCoord1svEPKs(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLshort *v) {
  self->glTexCoord1sv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glTexCoord1s(GLshort s)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glTexCoord1sEs(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLshort s) {
  self->glTexCoord1s(s);
}

//  void QOpenGLFunctions_3_2_Compatibility::glTexCoord1iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glTexCoord1ivEPKi(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLint *v) {
  self->glTexCoord1iv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glTexCoord1i(GLint s)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glTexCoord1iEi(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLint s) {
  self->glTexCoord1i(s);
}

//  void QOpenGLFunctions_3_2_Compatibility::glTexCoord1fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glTexCoord1fvEPKf(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLfloat *v) {
  self->glTexCoord1fv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glTexCoord1f(GLfloat s)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glTexCoord1fEf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLfloat s) {
  self->glTexCoord1f(s);
}

//  void QOpenGLFunctions_3_2_Compatibility::glTexCoord1dv(const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glTexCoord1dvEPKd(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLdouble *v) {
  self->glTexCoord1dv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glTexCoord1d(GLdouble s)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glTexCoord1dEd(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLdouble s) {
  self->glTexCoord1d(s);
}

//  void QOpenGLFunctions_3_2_Compatibility::glRectsv(const GLshort *v1,
//      const GLshort *v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility8glRectsvEPKsS1_(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLshort *v1,
    const GLshort *v2) {
  self->glRectsv(v1, v2);
}

//  void QOpenGLFunctions_3_2_Compatibility::glRects(GLshort x1, GLshort y1,
//      GLshort x2, GLshort y2)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility7glRectsEssss(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLshort x1,
    GLshort y1,
    GLshort x2,
    GLshort y2) {
  self->glRects(x1, y1, x2, y2);
}

//  void QOpenGLFunctions_3_2_Compatibility::glRectiv(const GLint *v1, const
//      GLint *v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility8glRectivEPKiS1_(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLint *v1,
    const GLint *v2) {
  self->glRectiv(v1, v2);
}

//  void QOpenGLFunctions_3_2_Compatibility::glRecti(GLint x1, GLint y1,
//      GLint x2, GLint y2)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility7glRectiEiiii(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLint x1,
    GLint y1,
    GLint x2,
    GLint y2) {
  self->glRecti(x1, y1, x2, y2);
}

//  void QOpenGLFunctions_3_2_Compatibility::glRectfv(const GLfloat *v1,
//      const GLfloat *v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility8glRectfvEPKfS1_(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLfloat *v1,
    const GLfloat *v2) {
  self->glRectfv(v1, v2);
}

//  void QOpenGLFunctions_3_2_Compatibility::glRectf(GLfloat x1, GLfloat y1,
//      GLfloat x2, GLfloat y2)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility7glRectfEffff(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLfloat x1,
    GLfloat y1,
    GLfloat x2,
    GLfloat y2) {
  self->glRectf(x1, y1, x2, y2);
}

//  void QOpenGLFunctions_3_2_Compatibility::glRectdv(const GLdouble *v1,
//      const GLdouble *v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility8glRectdvEPKdS1_(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLdouble *v1,
    const GLdouble *v2) {
  self->glRectdv(v1, v2);
}

//  void QOpenGLFunctions_3_2_Compatibility::glRectd(GLdouble x1, GLdouble
//      y1, GLdouble x2, GLdouble y2)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility7glRectdEdddd(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLdouble x1,
    GLdouble y1,
    GLdouble x2,
    GLdouble y2) {
  self->glRectd(x1, y1, x2, y2);
}

//  void QOpenGLFunctions_3_2_Compatibility::glRasterPos4sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility14glRasterPos4svEPKs(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLshort *v) {
  self->glRasterPos4sv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glRasterPos4s(GLshort x, GLshort
//      y, GLshort z, GLshort w)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glRasterPos4sEssss(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLshort x,
    GLshort y,
    GLshort z,
    GLshort w) {
  self->glRasterPos4s(x, y, z, w);
}

//  void QOpenGLFunctions_3_2_Compatibility::glRasterPos4iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility14glRasterPos4ivEPKi(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLint *v) {
  self->glRasterPos4iv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glRasterPos4i(GLint x, GLint y,
//      GLint z, GLint w)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glRasterPos4iEiiii(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLint x,
    GLint y,
    GLint z,
    GLint w) {
  self->glRasterPos4i(x, y, z, w);
}

//  void QOpenGLFunctions_3_2_Compatibility::glRasterPos4fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility14glRasterPos4fvEPKf(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLfloat *v) {
  self->glRasterPos4fv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glRasterPos4f(GLfloat x, GLfloat
//      y, GLfloat z, GLfloat w)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glRasterPos4fEffff(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLfloat x,
    GLfloat y,
    GLfloat z,
    GLfloat w) {
  self->glRasterPos4f(x, y, z, w);
}

//  void QOpenGLFunctions_3_2_Compatibility::glRasterPos4dv(const GLdouble
//      *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility14glRasterPos4dvEPKd(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLdouble *v) {
  self->glRasterPos4dv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glRasterPos4d(GLdouble x,
//      GLdouble y, GLdouble z, GLdouble w)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glRasterPos4dEdddd(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLdouble x,
    GLdouble y,
    GLdouble z,
    GLdouble w) {
  self->glRasterPos4d(x, y, z, w);
}

//  void QOpenGLFunctions_3_2_Compatibility::glRasterPos3sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility14glRasterPos3svEPKs(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLshort *v) {
  self->glRasterPos3sv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glRasterPos3s(GLshort x, GLshort
//      y, GLshort z)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glRasterPos3sEsss(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLshort x,
    GLshort y,
    GLshort z) {
  self->glRasterPos3s(x, y, z);
}

//  void QOpenGLFunctions_3_2_Compatibility::glRasterPos3iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility14glRasterPos3ivEPKi(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLint *v) {
  self->glRasterPos3iv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glRasterPos3i(GLint x, GLint y,
//      GLint z)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glRasterPos3iEiii(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLint x,
    GLint y,
    GLint z) {
  self->glRasterPos3i(x, y, z);
}

//  void QOpenGLFunctions_3_2_Compatibility::glRasterPos3fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility14glRasterPos3fvEPKf(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLfloat *v) {
  self->glRasterPos3fv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glRasterPos3f(GLfloat x, GLfloat
//      y, GLfloat z)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glRasterPos3fEfff(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLfloat x,
    GLfloat y,
    GLfloat z) {
  self->glRasterPos3f(x, y, z);
}

//  void QOpenGLFunctions_3_2_Compatibility::glRasterPos3dv(const GLdouble
//      *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility14glRasterPos3dvEPKd(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLdouble *v) {
  self->glRasterPos3dv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glRasterPos3d(GLdouble x,
//      GLdouble y, GLdouble z)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glRasterPos3dEddd(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLdouble x,
    GLdouble y,
    GLdouble z) {
  self->glRasterPos3d(x, y, z);
}

//  void QOpenGLFunctions_3_2_Compatibility::glRasterPos2sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility14glRasterPos2svEPKs(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLshort *v) {
  self->glRasterPos2sv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glRasterPos2s(GLshort x, GLshort
//      y)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glRasterPos2sEss(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLshort x,
    GLshort y) {
  self->glRasterPos2s(x, y);
}

//  void QOpenGLFunctions_3_2_Compatibility::glRasterPos2iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility14glRasterPos2ivEPKi(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLint *v) {
  self->glRasterPos2iv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glRasterPos2i(GLint x, GLint y)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glRasterPos2iEii(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLint x,
    GLint y) {
  self->glRasterPos2i(x, y);
}

//  void QOpenGLFunctions_3_2_Compatibility::glRasterPos2fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility14glRasterPos2fvEPKf(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLfloat *v) {
  self->glRasterPos2fv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glRasterPos2f(GLfloat x, GLfloat
//      y)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glRasterPos2fEff(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLfloat x,
    GLfloat y) {
  self->glRasterPos2f(x, y);
}

//  void QOpenGLFunctions_3_2_Compatibility::glRasterPos2dv(const GLdouble
//      *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility14glRasterPos2dvEPKd(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLdouble *v) {
  self->glRasterPos2dv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glRasterPos2d(GLdouble x,
//      GLdouble y)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glRasterPos2dEdd(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLdouble x,
    GLdouble y) {
  self->glRasterPos2d(x, y);
}

//  void QOpenGLFunctions_3_2_Compatibility::glNormal3sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility11glNormal3svEPKs(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLshort *v) {
  self->glNormal3sv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glNormal3s(GLshort nx, GLshort
//      ny, GLshort nz)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility10glNormal3sEsss(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLshort nx,
    GLshort ny,
    GLshort nz) {
  self->glNormal3s(nx, ny, nz);
}

//  void QOpenGLFunctions_3_2_Compatibility::glNormal3iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility11glNormal3ivEPKi(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLint *v) {
  self->glNormal3iv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glNormal3i(GLint nx, GLint ny,
//      GLint nz)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility10glNormal3iEiii(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLint nx,
    GLint ny,
    GLint nz) {
  self->glNormal3i(nx, ny, nz);
}

//  void QOpenGLFunctions_3_2_Compatibility::glNormal3fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility11glNormal3fvEPKf(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLfloat *v) {
  self->glNormal3fv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glNormal3f(GLfloat nx, GLfloat
//      ny, GLfloat nz)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility10glNormal3fEfff(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLfloat nx,
    GLfloat ny,
    GLfloat nz) {
  self->glNormal3f(nx, ny, nz);
}

//  void QOpenGLFunctions_3_2_Compatibility::glNormal3dv(const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility11glNormal3dvEPKd(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLdouble *v) {
  self->glNormal3dv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glNormal3d(GLdouble nx, GLdouble
//      ny, GLdouble nz)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility10glNormal3dEddd(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLdouble nx,
    GLdouble ny,
    GLdouble nz) {
  self->glNormal3d(nx, ny, nz);
}

//  void QOpenGLFunctions_3_2_Compatibility::glNormal3bv(const GLbyte *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility11glNormal3bvEPKa(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLbyte *v) {
  self->glNormal3bv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glNormal3b(GLbyte nx, GLbyte ny,
//      GLbyte nz)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility10glNormal3bEaaa(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLbyte nx,
    GLbyte ny,
    GLbyte nz) {
  self->glNormal3b(nx, ny, nz);
}

//  void QOpenGLFunctions_3_2_Compatibility::glIndexsv(const GLshort *c)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility9glIndexsvEPKs(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLshort *c) {
  self->glIndexsv(c);
}

//  void QOpenGLFunctions_3_2_Compatibility::glIndexs(GLshort c)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility8glIndexsEs(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLshort c) {
  self->glIndexs(c);
}

//  void QOpenGLFunctions_3_2_Compatibility::glIndexiv(const GLint *c)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility9glIndexivEPKi(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLint *c) {
  self->glIndexiv(c);
}

//  void QOpenGLFunctions_3_2_Compatibility::glIndexi(GLint c)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility8glIndexiEi(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLint c) {
  self->glIndexi(c);
}

//  void QOpenGLFunctions_3_2_Compatibility::glIndexfv(const GLfloat *c)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility9glIndexfvEPKf(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLfloat *c) {
  self->glIndexfv(c);
}

//  void QOpenGLFunctions_3_2_Compatibility::glIndexf(GLfloat c)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility8glIndexfEf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLfloat c) {
  self->glIndexf(c);
}

//  void QOpenGLFunctions_3_2_Compatibility::glIndexdv(const GLdouble *c)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility9glIndexdvEPKd(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLdouble *c) {
  self->glIndexdv(c);
}

//  void QOpenGLFunctions_3_2_Compatibility::glIndexd(GLdouble c)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility8glIndexdEd(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLdouble c) {
  self->glIndexd(c);
}

//  void QOpenGLFunctions_3_2_Compatibility::glEnd()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility5glEndEv(
    QOpenGLFunctions_3_2_Compatibility *self) {
  self->glEnd();
}

//  void QOpenGLFunctions_3_2_Compatibility::glEdgeFlagv(const GLboolean
//      *flag)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility11glEdgeFlagvEPKh(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLboolean *flag) {
  self->glEdgeFlagv(flag);
}

//  void QOpenGLFunctions_3_2_Compatibility::glEdgeFlag(GLboolean flag)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility10glEdgeFlagEh(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLboolean flag) {
  self->glEdgeFlag(flag);
}

//  void QOpenGLFunctions_3_2_Compatibility::glColor4usv(const GLushort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility11glColor4usvEPKt(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLushort *v) {
  self->glColor4usv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glColor4us(GLushort red,
//      GLushort green, GLushort blue, GLushort alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility10glColor4usEtttt(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLushort red,
    GLushort green,
    GLushort blue,
    GLushort alpha) {
  self->glColor4us(red, green, blue, alpha);
}

//  void QOpenGLFunctions_3_2_Compatibility::glColor4uiv(const GLuint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility11glColor4uivEPKj(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLuint *v) {
  self->glColor4uiv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glColor4ui(GLuint red, GLuint
//      green, GLuint blue, GLuint alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility10glColor4uiEjjjj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint red,
    GLuint green,
    GLuint blue,
    GLuint alpha) {
  self->glColor4ui(red, green, blue, alpha);
}

//  void QOpenGLFunctions_3_2_Compatibility::glColor4ubv(const GLubyte *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility11glColor4ubvEPKh(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLubyte *v) {
  self->glColor4ubv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glColor4ub(GLubyte red, GLubyte
//      green, GLubyte blue, GLubyte alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility10glColor4ubEhhhh(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLubyte red,
    GLubyte green,
    GLubyte blue,
    GLubyte alpha) {
  self->glColor4ub(red, green, blue, alpha);
}

//  void QOpenGLFunctions_3_2_Compatibility::glColor4sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility10glColor4svEPKs(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLshort *v) {
  self->glColor4sv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glColor4s(GLshort red, GLshort
//      green, GLshort blue, GLshort alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility9glColor4sEssss(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLshort red,
    GLshort green,
    GLshort blue,
    GLshort alpha) {
  self->glColor4s(red, green, blue, alpha);
}

//  void QOpenGLFunctions_3_2_Compatibility::glColor4iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility10glColor4ivEPKi(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLint *v) {
  self->glColor4iv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glColor4i(GLint red, GLint
//      green, GLint blue, GLint alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility9glColor4iEiiii(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLint red,
    GLint green,
    GLint blue,
    GLint alpha) {
  self->glColor4i(red, green, blue, alpha);
}

//  void QOpenGLFunctions_3_2_Compatibility::glColor4fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility10glColor4fvEPKf(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLfloat *v) {
  self->glColor4fv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glColor4f(GLfloat red, GLfloat
//      green, GLfloat blue, GLfloat alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility9glColor4fEffff(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLfloat red,
    GLfloat green,
    GLfloat blue,
    GLfloat alpha) {
  self->glColor4f(red, green, blue, alpha);
}

//  void QOpenGLFunctions_3_2_Compatibility::glColor4dv(const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility10glColor4dvEPKd(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLdouble *v) {
  self->glColor4dv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glColor4d(GLdouble red, GLdouble
//      green, GLdouble blue, GLdouble alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility9glColor4dEdddd(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLdouble red,
    GLdouble green,
    GLdouble blue,
    GLdouble alpha) {
  self->glColor4d(red, green, blue, alpha);
}

//  void QOpenGLFunctions_3_2_Compatibility::glColor4bv(const GLbyte *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility10glColor4bvEPKa(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLbyte *v) {
  self->glColor4bv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glColor4b(GLbyte red, GLbyte
//      green, GLbyte blue, GLbyte alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility9glColor4bEaaaa(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLbyte red,
    GLbyte green,
    GLbyte blue,
    GLbyte alpha) {
  self->glColor4b(red, green, blue, alpha);
}

//  void QOpenGLFunctions_3_2_Compatibility::glColor3usv(const GLushort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility11glColor3usvEPKt(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLushort *v) {
  self->glColor3usv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glColor3us(GLushort red,
//      GLushort green, GLushort blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility10glColor3usEttt(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLushort red,
    GLushort green,
    GLushort blue) {
  self->glColor3us(red, green, blue);
}

//  void QOpenGLFunctions_3_2_Compatibility::glColor3uiv(const GLuint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility11glColor3uivEPKj(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLuint *v) {
  self->glColor3uiv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glColor3ui(GLuint red, GLuint
//      green, GLuint blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility10glColor3uiEjjj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint red,
    GLuint green,
    GLuint blue) {
  self->glColor3ui(red, green, blue);
}

//  void QOpenGLFunctions_3_2_Compatibility::glColor3ubv(const GLubyte *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility11glColor3ubvEPKh(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLubyte *v) {
  self->glColor3ubv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glColor3ub(GLubyte red, GLubyte
//      green, GLubyte blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility10glColor3ubEhhh(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLubyte red,
    GLubyte green,
    GLubyte blue) {
  self->glColor3ub(red, green, blue);
}

//  void QOpenGLFunctions_3_2_Compatibility::glColor3sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility10glColor3svEPKs(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLshort *v) {
  self->glColor3sv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glColor3s(GLshort red, GLshort
//      green, GLshort blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility9glColor3sEsss(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLshort red,
    GLshort green,
    GLshort blue) {
  self->glColor3s(red, green, blue);
}

//  void QOpenGLFunctions_3_2_Compatibility::glColor3iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility10glColor3ivEPKi(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLint *v) {
  self->glColor3iv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glColor3i(GLint red, GLint
//      green, GLint blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility9glColor3iEiii(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLint red,
    GLint green,
    GLint blue) {
  self->glColor3i(red, green, blue);
}

//  void QOpenGLFunctions_3_2_Compatibility::glColor3fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility10glColor3fvEPKf(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLfloat *v) {
  self->glColor3fv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glColor3f(GLfloat red, GLfloat
//      green, GLfloat blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility9glColor3fEfff(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLfloat red,
    GLfloat green,
    GLfloat blue) {
  self->glColor3f(red, green, blue);
}

//  void QOpenGLFunctions_3_2_Compatibility::glColor3dv(const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility10glColor3dvEPKd(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLdouble *v) {
  self->glColor3dv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glColor3d(GLdouble red, GLdouble
//      green, GLdouble blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility9glColor3dEddd(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLdouble red,
    GLdouble green,
    GLdouble blue) {
  self->glColor3d(red, green, blue);
}

//  void QOpenGLFunctions_3_2_Compatibility::glColor3bv(const GLbyte *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility10glColor3bvEPKa(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLbyte *v) {
  self->glColor3bv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glColor3b(GLbyte red, GLbyte
//      green, GLbyte blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility9glColor3bEaaa(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLbyte red,
    GLbyte green,
    GLbyte blue) {
  self->glColor3b(red, green, blue);
}

//  void QOpenGLFunctions_3_2_Compatibility::glBitmap(GLsizei width, GLsizei
//      height, GLfloat xorig, GLfloat yorig, GLfloat xmove, GLfloat ymove,
//      const GLubyte *bitmap)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility8glBitmapEiiffffPKh(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLsizei width,
    GLsizei height,
    GLfloat xorig,
    GLfloat yorig,
    GLfloat xmove,
    GLfloat ymove,
    const GLubyte *bitmap) {
  self->glBitmap(width, height, xorig, yorig, xmove, ymove, bitmap);
}

//  void QOpenGLFunctions_3_2_Compatibility::glBegin(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility7glBeginEj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum mode) {
  self->glBegin(mode);
}

//  void QOpenGLFunctions_3_2_Compatibility::glListBase(GLuint base)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility10glListBaseEj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint base) {
  self->glListBase(base);
}

//  GLuint QOpenGLFunctions_3_2_Compatibility::glGenLists(GLsizei range)
extern "C" Q_DECL_EXPORT
GLuint ritual_ZN34QOpenGLFunctions_3_2_Compatibility10glGenListsEi(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLsizei range) {
  return self->glGenLists(range);
}

//  void QOpenGLFunctions_3_2_Compatibility::glDeleteLists(GLuint list,
//      GLsizei range)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glDeleteListsEji(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint list,
    GLsizei range) {
  self->glDeleteLists(list, range);
}

//  void QOpenGLFunctions_3_2_Compatibility::glCallLists(GLsizei n, GLenum
//      type, const GLvoid *lists)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility11glCallListsEijPKv(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLsizei n,
    GLenum type,
    const GLvoid *lists) {
  self->glCallLists(n, type, lists);
}

//  void QOpenGLFunctions_3_2_Compatibility::glCallList(GLuint list)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility10glCallListEj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint list) {
  self->glCallList(list);
}

//  void QOpenGLFunctions_3_2_Compatibility::glEndList()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility9glEndListEv(
    QOpenGLFunctions_3_2_Compatibility *self) {
  self->glEndList();
}

//  void QOpenGLFunctions_3_2_Compatibility::glNewList(GLuint list, GLenum
//      mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility9glNewListEjj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint list,
    GLenum mode) {
  self->glNewList(list, mode);
}

//  void QOpenGLFunctions_3_2_Compatibility::glPushClientAttrib(GLbitfield
//      mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility18glPushClientAttribEj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLbitfield mask) {
  self->glPushClientAttrib(mask);
}

//  void QOpenGLFunctions_3_2_Compatibility::glPopClientAttrib()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility17glPopClientAttribEv(
    QOpenGLFunctions_3_2_Compatibility *self) {
  self->glPopClientAttrib();
}

//  void QOpenGLFunctions_3_2_Compatibility::glPrioritizeTextures(GLsizei n,
//      const GLuint *textures, const GLfloat *priorities)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility20glPrioritizeTexturesEiPKjPKf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLsizei n,
    const GLuint *textures,
    const GLfloat *priorities) {
  self->glPrioritizeTextures(n, textures, priorities);
}

//  GLboolean
//      QOpenGLFunctions_3_2_Compatibility::glAreTexturesResident(GLsizei n,
//      const GLuint *textures, GLboolean *residences)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN34QOpenGLFunctions_3_2_Compatibility21glAreTexturesResidentEiPKjPh(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLsizei n,
    const GLuint *textures,
    GLboolean *residences) {
  return self->glAreTexturesResident(n, textures, residences);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertexPointer(GLint size,
//      GLenum type, GLsizei stride, const GLvoid *pointer)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility15glVertexPointerEijiPKv(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLint size,
    GLenum type,
    GLsizei stride,
    const GLvoid *pointer) {
  self->glVertexPointer(size, type, stride, pointer);
}

//  void QOpenGLFunctions_3_2_Compatibility::glTexCoordPointer(GLint size,
//      GLenum type, GLsizei stride, const GLvoid *pointer)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility17glTexCoordPointerEijiPKv(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLint size,
    GLenum type,
    GLsizei stride,
    const GLvoid *pointer) {
  self->glTexCoordPointer(size, type, stride, pointer);
}

//  void QOpenGLFunctions_3_2_Compatibility::glNormalPointer(GLenum type,
//      GLsizei stride, const GLvoid *pointer)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility15glNormalPointerEjiPKv(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum type,
    GLsizei stride,
    const GLvoid *pointer) {
  self->glNormalPointer(type, stride, pointer);
}

//  void QOpenGLFunctions_3_2_Compatibility::glInterleavedArrays(GLenum
//      format, GLsizei stride, const GLvoid *pointer)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility19glInterleavedArraysEjiPKv(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum format,
    GLsizei stride,
    const GLvoid *pointer) {
  self->glInterleavedArrays(format, stride, pointer);
}

//  void QOpenGLFunctions_3_2_Compatibility::glIndexPointer(GLenum type,
//      GLsizei stride, const GLvoid *pointer)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility14glIndexPointerEjiPKv(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum type,
    GLsizei stride,
    const GLvoid *pointer) {
  self->glIndexPointer(type, stride, pointer);
}

//  void QOpenGLFunctions_3_2_Compatibility::glEnableClientState(GLenum
//      array)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility19glEnableClientStateEj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum array) {
  self->glEnableClientState(array);
}

//  void QOpenGLFunctions_3_2_Compatibility::glEdgeFlagPointer(GLsizei
//      stride, const GLvoid *pointer)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility17glEdgeFlagPointerEiPKv(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLsizei stride,
    const GLvoid *pointer) {
  self->glEdgeFlagPointer(stride, pointer);
}

//  void QOpenGLFunctions_3_2_Compatibility::glDisableClientState(GLenum
//      array)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility20glDisableClientStateEj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum array) {
  self->glDisableClientState(array);
}

//  void QOpenGLFunctions_3_2_Compatibility::glColorPointer(GLint size,
//      GLenum type, GLsizei stride, const GLvoid *pointer)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility14glColorPointerEijiPKv(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLint size,
    GLenum type,
    GLsizei stride,
    const GLvoid *pointer) {
  self->glColorPointer(size, type, stride, pointer);
}

//  void QOpenGLFunctions_3_2_Compatibility::glArrayElement(GLint i)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility14glArrayElementEi(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLint i) {
  self->glArrayElement(i);
}

//  void QOpenGLFunctions_3_2_Compatibility::glResetMinmax(GLenum target)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glResetMinmaxEj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target) {
  self->glResetMinmax(target);
}

//  void QOpenGLFunctions_3_2_Compatibility::glResetHistogram(GLenum target)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility16glResetHistogramEj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target) {
  self->glResetHistogram(target);
}

//  void QOpenGLFunctions_3_2_Compatibility::glMinmax(GLenum target, GLenum
//      internalformat, GLboolean sink)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility8glMinmaxEjjh(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLenum internalformat,
    GLboolean sink) {
  self->glMinmax(target, internalformat, sink);
}

//  void QOpenGLFunctions_3_2_Compatibility::glHistogram(GLenum target,
//      GLsizei width, GLenum internalformat, GLboolean sink)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility11glHistogramEjijh(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLsizei width,
    GLenum internalformat,
    GLboolean sink) {
  self->glHistogram(target, width, internalformat, sink);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGetMinmaxParameteriv(GLenum
//      target, GLenum pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility22glGetMinmaxParameterivEjjPi(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLenum pname,
    GLint *params) {
  self->glGetMinmaxParameteriv(target, pname, params);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGetMinmaxParameterfv(GLenum
//      target, GLenum pname, GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility22glGetMinmaxParameterfvEjjPf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLenum pname,
    GLfloat *params) {
  self->glGetMinmaxParameterfv(target, pname, params);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGetMinmax(GLenum target,
//      GLboolean reset, GLenum format, GLenum type, GLvoid *values)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility11glGetMinmaxEjhjjPv(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLboolean reset,
    GLenum format,
    GLenum type,
    GLvoid *values) {
  self->glGetMinmax(target, reset, format, type, values);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGetHistogramParameteriv(GLenum
//      target, GLenum pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility25glGetHistogramParameterivEjjPi(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLenum pname,
    GLint *params) {
  self->glGetHistogramParameteriv(target, pname, params);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGetHistogramParameterfv(GLenum
//      target, GLenum pname, GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility25glGetHistogramParameterfvEjjPf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLenum pname,
    GLfloat *params) {
  self->glGetHistogramParameterfv(target, pname, params);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGetHistogram(GLenum target,
//      GLboolean reset, GLenum format, GLenum type, GLvoid *values)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility14glGetHistogramEjhjjPv(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLboolean reset,
    GLenum format,
    GLenum type,
    GLvoid *values) {
  self->glGetHistogram(target, reset, format, type, values);
}

//  void QOpenGLFunctions_3_2_Compatibility::glSeparableFilter2D(GLenum
//      target, GLenum internalformat, GLsizei width, GLsizei height, GLenum
//      format, GLenum type, const GLvoid *row, const GLvoid *column)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility19glSeparableFilter2DEjjiijjPKvS1_(
    QOpenGLFunctions_3_2_Compatibility *self,
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

//  void QOpenGLFunctions_3_2_Compatibility::glGetSeparableFilter(GLenum
//      target, GLenum format, GLenum type, GLvoid *row, GLvoid *column,
//      GLvoid *span)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility20glGetSeparableFilterEjjjPvS0_S0_(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLenum format,
    GLenum type,
    GLvoid *row,
    GLvoid *column,
    GLvoid *span) {
  self->glGetSeparableFilter(target, format, type, row, column, span);
}

//  void
//      QOpenGLFunctions_3_2_Compatibility::glGetConvolutionParameteriv(GLenu
//      m target, GLenum pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility27glGetConvolutionParameterivEjjPi(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLenum pname,
    GLint *params) {
  self->glGetConvolutionParameteriv(target, pname, params);
}

//  void
//      QOpenGLFunctions_3_2_Compatibility::glGetConvolutionParameterfv(GLenu
//      m target, GLenum pname, GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility27glGetConvolutionParameterfvEjjPf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLenum pname,
    GLfloat *params) {
  self->glGetConvolutionParameterfv(target, pname, params);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGetConvolutionFilter(GLenum
//      target, GLenum format, GLenum type, GLvoid *image)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility22glGetConvolutionFilterEjjjPv(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLenum format,
    GLenum type,
    GLvoid *image) {
  self->glGetConvolutionFilter(target, format, type, image);
}

//  void QOpenGLFunctions_3_2_Compatibility::glCopyConvolutionFilter2D(GLenum
//      target, GLenum internalformat, GLint x, GLint y, GLsizei width,
//      GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility25glCopyConvolutionFilter2DEjjiiii(
    QOpenGLFunctions_3_2_Compatibility *self,
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

//  void QOpenGLFunctions_3_2_Compatibility::glCopyConvolutionFilter1D(GLenum
//      target, GLenum internalformat, GLint x, GLint y, GLsizei width)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility25glCopyConvolutionFilter1DEjjiii(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLenum internalformat,
    GLint x,
    GLint y,
    GLsizei width) {
  self->glCopyConvolutionFilter1D(target, internalformat, x, y, width);
}

//  void QOpenGLFunctions_3_2_Compatibility::glConvolutionParameteriv(GLenum
//      target, GLenum pname, const GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility24glConvolutionParameterivEjjPKi(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLenum pname,
    const GLint *params) {
  self->glConvolutionParameteriv(target, pname, params);
}

//  void QOpenGLFunctions_3_2_Compatibility::glConvolutionParameteri(GLenum
//      target, GLenum pname, GLint params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility23glConvolutionParameteriEjji(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLenum pname,
    GLint params) {
  self->glConvolutionParameteri(target, pname, params);
}

//  void QOpenGLFunctions_3_2_Compatibility::glConvolutionParameterfv(GLenum
//      target, GLenum pname, const GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility24glConvolutionParameterfvEjjPKf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLenum pname,
    const GLfloat *params) {
  self->glConvolutionParameterfv(target, pname, params);
}

//  void QOpenGLFunctions_3_2_Compatibility::glConvolutionParameterf(GLenum
//      target, GLenum pname, GLfloat params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility23glConvolutionParameterfEjjf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLenum pname,
    GLfloat params) {
  self->glConvolutionParameterf(target, pname, params);
}

//  void QOpenGLFunctions_3_2_Compatibility::glConvolutionFilter2D(GLenum
//      target, GLenum internalformat, GLsizei width, GLsizei height, GLenum
//      format, GLenum type, const GLvoid *image)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility21glConvolutionFilter2DEjjiijjPKv(
    QOpenGLFunctions_3_2_Compatibility *self,
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

//  void QOpenGLFunctions_3_2_Compatibility::glConvolutionFilter1D(GLenum
//      target, GLenum internalformat, GLsizei width, GLenum format, GLenum
//      type, const GLvoid *image)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility21glConvolutionFilter1DEjjijjPKv(
    QOpenGLFunctions_3_2_Compatibility *self,
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

//  void QOpenGLFunctions_3_2_Compatibility::glCopyColorSubTable(GLenum
//      target, GLsizei start, GLint x, GLint y, GLsizei width)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility19glCopyColorSubTableEjiiii(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLsizei start,
    GLint x,
    GLint y,
    GLsizei width) {
  self->glCopyColorSubTable(target, start, x, y, width);
}

//  void QOpenGLFunctions_3_2_Compatibility::glColorSubTable(GLenum target,
//      GLsizei start, GLsizei count, GLenum format, GLenum type, const
//      GLvoid *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility15glColorSubTableEjiijjPKv(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLsizei start,
    GLsizei count,
    GLenum format,
    GLenum type,
    const GLvoid *data) {
  self->glColorSubTable(target, start, count, format, type, data);
}

//  void
//      QOpenGLFunctions_3_2_Compatibility::glGetColorTableParameteriv(GLenum
//      target, GLenum pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility26glGetColorTableParameterivEjjPi(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLenum pname,
    GLint *params) {
  self->glGetColorTableParameteriv(target, pname, params);
}

//  void
//      QOpenGLFunctions_3_2_Compatibility::glGetColorTableParameterfv(GLenum
//      target, GLenum pname, GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility26glGetColorTableParameterfvEjjPf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLenum pname,
    GLfloat *params) {
  self->glGetColorTableParameterfv(target, pname, params);
}

//  void QOpenGLFunctions_3_2_Compatibility::glGetColorTable(GLenum target,
//      GLenum format, GLenum type, GLvoid *table)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility15glGetColorTableEjjjPv(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLenum format,
    GLenum type,
    GLvoid *table) {
  self->glGetColorTable(target, format, type, table);
}

//  void QOpenGLFunctions_3_2_Compatibility::glCopyColorTable(GLenum target,
//      GLenum internalformat, GLint x, GLint y, GLsizei width)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility16glCopyColorTableEjjiii(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLenum internalformat,
    GLint x,
    GLint y,
    GLsizei width) {
  self->glCopyColorTable(target, internalformat, x, y, width);
}

//  void QOpenGLFunctions_3_2_Compatibility::glColorTableParameteriv(GLenum
//      target, GLenum pname, const GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility23glColorTableParameterivEjjPKi(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLenum pname,
    const GLint *params) {
  self->glColorTableParameteriv(target, pname, params);
}

//  void QOpenGLFunctions_3_2_Compatibility::glColorTableParameterfv(GLenum
//      target, GLenum pname, const GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility23glColorTableParameterfvEjjPKf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLenum pname,
    const GLfloat *params) {
  self->glColorTableParameterfv(target, pname, params);
}

//  void QOpenGLFunctions_3_2_Compatibility::glColorTable(GLenum target,
//      GLenum internalformat, GLsizei width, GLenum format, GLenum type,
//      const GLvoid *table)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glColorTableEjjijjPKv(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLenum internalformat,
    GLsizei width,
    GLenum format,
    GLenum type,
    const GLvoid *table) {
  self->glColorTable(target, internalformat, width, format, type, table);
}

//  void QOpenGLFunctions_3_2_Compatibility::glMultTransposeMatrixd(const
//      GLdouble *m)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility22glMultTransposeMatrixdEPKd(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLdouble *m) {
  self->glMultTransposeMatrixd(m);
}

//  void QOpenGLFunctions_3_2_Compatibility::glMultTransposeMatrixf(const
//      GLfloat *m)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility22glMultTransposeMatrixfEPKf(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLfloat *m) {
  self->glMultTransposeMatrixf(m);
}

//  void QOpenGLFunctions_3_2_Compatibility::glLoadTransposeMatrixd(const
//      GLdouble *m)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility22glLoadTransposeMatrixdEPKd(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLdouble *m) {
  self->glLoadTransposeMatrixd(m);
}

//  void QOpenGLFunctions_3_2_Compatibility::glLoadTransposeMatrixf(const
//      GLfloat *m)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility22glLoadTransposeMatrixfEPKf(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLfloat *m) {
  self->glLoadTransposeMatrixf(m);
}

//  void QOpenGLFunctions_3_2_Compatibility::glMultiTexCoord4sv(GLenum
//      target, const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility18glMultiTexCoord4svEjPKs(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    const GLshort *v) {
  self->glMultiTexCoord4sv(target, v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glMultiTexCoord4s(GLenum target,
//      GLshort s, GLshort t, GLshort r, GLshort q)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility17glMultiTexCoord4sEjssss(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLshort s,
    GLshort t,
    GLshort r,
    GLshort q) {
  self->glMultiTexCoord4s(target, s, t, r, q);
}

//  void QOpenGLFunctions_3_2_Compatibility::glMultiTexCoord4iv(GLenum
//      target, const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility18glMultiTexCoord4ivEjPKi(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    const GLint *v) {
  self->glMultiTexCoord4iv(target, v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glMultiTexCoord4i(GLenum target,
//      GLint s, GLint t, GLint r, GLint q)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility17glMultiTexCoord4iEjiiii(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLint s,
    GLint t,
    GLint r,
    GLint q) {
  self->glMultiTexCoord4i(target, s, t, r, q);
}

//  void QOpenGLFunctions_3_2_Compatibility::glMultiTexCoord4fv(GLenum
//      target, const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility18glMultiTexCoord4fvEjPKf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    const GLfloat *v) {
  self->glMultiTexCoord4fv(target, v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glMultiTexCoord4f(GLenum target,
//      GLfloat s, GLfloat t, GLfloat r, GLfloat q)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility17glMultiTexCoord4fEjffff(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLfloat s,
    GLfloat t,
    GLfloat r,
    GLfloat q) {
  self->glMultiTexCoord4f(target, s, t, r, q);
}

//  void QOpenGLFunctions_3_2_Compatibility::glMultiTexCoord4dv(GLenum
//      target, const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility18glMultiTexCoord4dvEjPKd(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    const GLdouble *v) {
  self->glMultiTexCoord4dv(target, v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glMultiTexCoord4d(GLenum target,
//      GLdouble s, GLdouble t, GLdouble r, GLdouble q)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility17glMultiTexCoord4dEjdddd(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLdouble s,
    GLdouble t,
    GLdouble r,
    GLdouble q) {
  self->glMultiTexCoord4d(target, s, t, r, q);
}

//  void QOpenGLFunctions_3_2_Compatibility::glMultiTexCoord3sv(GLenum
//      target, const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility18glMultiTexCoord3svEjPKs(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    const GLshort *v) {
  self->glMultiTexCoord3sv(target, v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glMultiTexCoord3s(GLenum target,
//      GLshort s, GLshort t, GLshort r)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility17glMultiTexCoord3sEjsss(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLshort s,
    GLshort t,
    GLshort r) {
  self->glMultiTexCoord3s(target, s, t, r);
}

//  void QOpenGLFunctions_3_2_Compatibility::glMultiTexCoord3iv(GLenum
//      target, const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility18glMultiTexCoord3ivEjPKi(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    const GLint *v) {
  self->glMultiTexCoord3iv(target, v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glMultiTexCoord3i(GLenum target,
//      GLint s, GLint t, GLint r)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility17glMultiTexCoord3iEjiii(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLint s,
    GLint t,
    GLint r) {
  self->glMultiTexCoord3i(target, s, t, r);
}

//  void QOpenGLFunctions_3_2_Compatibility::glMultiTexCoord3fv(GLenum
//      target, const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility18glMultiTexCoord3fvEjPKf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    const GLfloat *v) {
  self->glMultiTexCoord3fv(target, v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glMultiTexCoord3f(GLenum target,
//      GLfloat s, GLfloat t, GLfloat r)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility17glMultiTexCoord3fEjfff(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLfloat s,
    GLfloat t,
    GLfloat r) {
  self->glMultiTexCoord3f(target, s, t, r);
}

//  void QOpenGLFunctions_3_2_Compatibility::glMultiTexCoord3dv(GLenum
//      target, const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility18glMultiTexCoord3dvEjPKd(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    const GLdouble *v) {
  self->glMultiTexCoord3dv(target, v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glMultiTexCoord3d(GLenum target,
//      GLdouble s, GLdouble t, GLdouble r)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility17glMultiTexCoord3dEjddd(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLdouble s,
    GLdouble t,
    GLdouble r) {
  self->glMultiTexCoord3d(target, s, t, r);
}

//  void QOpenGLFunctions_3_2_Compatibility::glMultiTexCoord2sv(GLenum
//      target, const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility18glMultiTexCoord2svEjPKs(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    const GLshort *v) {
  self->glMultiTexCoord2sv(target, v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glMultiTexCoord2s(GLenum target,
//      GLshort s, GLshort t)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility17glMultiTexCoord2sEjss(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLshort s,
    GLshort t) {
  self->glMultiTexCoord2s(target, s, t);
}

//  void QOpenGLFunctions_3_2_Compatibility::glMultiTexCoord2iv(GLenum
//      target, const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility18glMultiTexCoord2ivEjPKi(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    const GLint *v) {
  self->glMultiTexCoord2iv(target, v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glMultiTexCoord2i(GLenum target,
//      GLint s, GLint t)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility17glMultiTexCoord2iEjii(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLint s,
    GLint t) {
  self->glMultiTexCoord2i(target, s, t);
}

//  void QOpenGLFunctions_3_2_Compatibility::glMultiTexCoord2fv(GLenum
//      target, const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility18glMultiTexCoord2fvEjPKf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    const GLfloat *v) {
  self->glMultiTexCoord2fv(target, v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glMultiTexCoord2f(GLenum target,
//      GLfloat s, GLfloat t)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility17glMultiTexCoord2fEjff(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLfloat s,
    GLfloat t) {
  self->glMultiTexCoord2f(target, s, t);
}

//  void QOpenGLFunctions_3_2_Compatibility::glMultiTexCoord2dv(GLenum
//      target, const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility18glMultiTexCoord2dvEjPKd(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    const GLdouble *v) {
  self->glMultiTexCoord2dv(target, v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glMultiTexCoord2d(GLenum target,
//      GLdouble s, GLdouble t)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility17glMultiTexCoord2dEjdd(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLdouble s,
    GLdouble t) {
  self->glMultiTexCoord2d(target, s, t);
}

//  void QOpenGLFunctions_3_2_Compatibility::glMultiTexCoord1sv(GLenum
//      target, const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility18glMultiTexCoord1svEjPKs(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    const GLshort *v) {
  self->glMultiTexCoord1sv(target, v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glMultiTexCoord1s(GLenum target,
//      GLshort s)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility17glMultiTexCoord1sEjs(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLshort s) {
  self->glMultiTexCoord1s(target, s);
}

//  void QOpenGLFunctions_3_2_Compatibility::glMultiTexCoord1iv(GLenum
//      target, const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility18glMultiTexCoord1ivEjPKi(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    const GLint *v) {
  self->glMultiTexCoord1iv(target, v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glMultiTexCoord1i(GLenum target,
//      GLint s)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility17glMultiTexCoord1iEji(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLint s) {
  self->glMultiTexCoord1i(target, s);
}

//  void QOpenGLFunctions_3_2_Compatibility::glMultiTexCoord1fv(GLenum
//      target, const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility18glMultiTexCoord1fvEjPKf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    const GLfloat *v) {
  self->glMultiTexCoord1fv(target, v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glMultiTexCoord1f(GLenum target,
//      GLfloat s)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility17glMultiTexCoord1fEjf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLfloat s) {
  self->glMultiTexCoord1f(target, s);
}

//  void QOpenGLFunctions_3_2_Compatibility::glMultiTexCoord1dv(GLenum
//      target, const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility18glMultiTexCoord1dvEjPKd(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    const GLdouble *v) {
  self->glMultiTexCoord1dv(target, v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glMultiTexCoord1d(GLenum target,
//      GLdouble s)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility17glMultiTexCoord1dEjd(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum target,
    GLdouble s) {
  self->glMultiTexCoord1d(target, s);
}

//  void QOpenGLFunctions_3_2_Compatibility::glClientActiveTexture(GLenum
//      texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility21glClientActiveTextureEj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum texture) {
  self->glClientActiveTexture(texture);
}

//  void QOpenGLFunctions_3_2_Compatibility::glWindowPos3sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility14glWindowPos3svEPKs(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLshort *v) {
  self->glWindowPos3sv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glWindowPos3s(GLshort x, GLshort
//      y, GLshort z)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glWindowPos3sEsss(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLshort x,
    GLshort y,
    GLshort z) {
  self->glWindowPos3s(x, y, z);
}

//  void QOpenGLFunctions_3_2_Compatibility::glWindowPos3iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility14glWindowPos3ivEPKi(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLint *v) {
  self->glWindowPos3iv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glWindowPos3i(GLint x, GLint y,
//      GLint z)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glWindowPos3iEiii(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLint x,
    GLint y,
    GLint z) {
  self->glWindowPos3i(x, y, z);
}

//  void QOpenGLFunctions_3_2_Compatibility::glWindowPos3fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility14glWindowPos3fvEPKf(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLfloat *v) {
  self->glWindowPos3fv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glWindowPos3f(GLfloat x, GLfloat
//      y, GLfloat z)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glWindowPos3fEfff(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLfloat x,
    GLfloat y,
    GLfloat z) {
  self->glWindowPos3f(x, y, z);
}

//  void QOpenGLFunctions_3_2_Compatibility::glWindowPos3dv(const GLdouble
//      *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility14glWindowPos3dvEPKd(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLdouble *v) {
  self->glWindowPos3dv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glWindowPos3d(GLdouble x,
//      GLdouble y, GLdouble z)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glWindowPos3dEddd(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLdouble x,
    GLdouble y,
    GLdouble z) {
  self->glWindowPos3d(x, y, z);
}

//  void QOpenGLFunctions_3_2_Compatibility::glWindowPos2sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility14glWindowPos2svEPKs(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLshort *v) {
  self->glWindowPos2sv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glWindowPos2s(GLshort x, GLshort
//      y)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glWindowPos2sEss(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLshort x,
    GLshort y) {
  self->glWindowPos2s(x, y);
}

//  void QOpenGLFunctions_3_2_Compatibility::glWindowPos2iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility14glWindowPos2ivEPKi(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLint *v) {
  self->glWindowPos2iv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glWindowPos2i(GLint x, GLint y)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glWindowPos2iEii(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLint x,
    GLint y) {
  self->glWindowPos2i(x, y);
}

//  void QOpenGLFunctions_3_2_Compatibility::glWindowPos2fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility14glWindowPos2fvEPKf(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLfloat *v) {
  self->glWindowPos2fv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glWindowPos2f(GLfloat x, GLfloat
//      y)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glWindowPos2fEff(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLfloat x,
    GLfloat y) {
  self->glWindowPos2f(x, y);
}

//  void QOpenGLFunctions_3_2_Compatibility::glWindowPos2dv(const GLdouble
//      *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility14glWindowPos2dvEPKd(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLdouble *v) {
  self->glWindowPos2dv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glWindowPos2d(GLdouble x,
//      GLdouble y)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility13glWindowPos2dEdd(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLdouble x,
    GLdouble y) {
  self->glWindowPos2d(x, y);
}

//  void QOpenGLFunctions_3_2_Compatibility::glSecondaryColorPointer(GLint
//      size, GLenum type, GLsizei stride, const GLvoid *pointer)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility23glSecondaryColorPointerEijiPKv(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLint size,
    GLenum type,
    GLsizei stride,
    const GLvoid *pointer) {
  self->glSecondaryColorPointer(size, type, stride, pointer);
}

//  void QOpenGLFunctions_3_2_Compatibility::glSecondaryColor3usv(const
//      GLushort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility20glSecondaryColor3usvEPKt(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLushort *v) {
  self->glSecondaryColor3usv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glSecondaryColor3us(GLushort
//      red, GLushort green, GLushort blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility19glSecondaryColor3usEttt(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLushort red,
    GLushort green,
    GLushort blue) {
  self->glSecondaryColor3us(red, green, blue);
}

//  void QOpenGLFunctions_3_2_Compatibility::glSecondaryColor3uiv(const
//      GLuint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility20glSecondaryColor3uivEPKj(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLuint *v) {
  self->glSecondaryColor3uiv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glSecondaryColor3ui(GLuint red,
//      GLuint green, GLuint blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility19glSecondaryColor3uiEjjj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint red,
    GLuint green,
    GLuint blue) {
  self->glSecondaryColor3ui(red, green, blue);
}

//  void QOpenGLFunctions_3_2_Compatibility::glSecondaryColor3ubv(const
//      GLubyte *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility20glSecondaryColor3ubvEPKh(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLubyte *v) {
  self->glSecondaryColor3ubv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glSecondaryColor3ub(GLubyte red,
//      GLubyte green, GLubyte blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility19glSecondaryColor3ubEhhh(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLubyte red,
    GLubyte green,
    GLubyte blue) {
  self->glSecondaryColor3ub(red, green, blue);
}

//  void QOpenGLFunctions_3_2_Compatibility::glSecondaryColor3sv(const
//      GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility19glSecondaryColor3svEPKs(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLshort *v) {
  self->glSecondaryColor3sv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glSecondaryColor3s(GLshort red,
//      GLshort green, GLshort blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility18glSecondaryColor3sEsss(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLshort red,
    GLshort green,
    GLshort blue) {
  self->glSecondaryColor3s(red, green, blue);
}

//  void QOpenGLFunctions_3_2_Compatibility::glSecondaryColor3iv(const GLint
//      *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility19glSecondaryColor3ivEPKi(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLint *v) {
  self->glSecondaryColor3iv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glSecondaryColor3i(GLint red,
//      GLint green, GLint blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility18glSecondaryColor3iEiii(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLint red,
    GLint green,
    GLint blue) {
  self->glSecondaryColor3i(red, green, blue);
}

//  void QOpenGLFunctions_3_2_Compatibility::glSecondaryColor3fv(const
//      GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility19glSecondaryColor3fvEPKf(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLfloat *v) {
  self->glSecondaryColor3fv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glSecondaryColor3f(GLfloat red,
//      GLfloat green, GLfloat blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility18glSecondaryColor3fEfff(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLfloat red,
    GLfloat green,
    GLfloat blue) {
  self->glSecondaryColor3f(red, green, blue);
}

//  void QOpenGLFunctions_3_2_Compatibility::glSecondaryColor3dv(const
//      GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility19glSecondaryColor3dvEPKd(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLdouble *v) {
  self->glSecondaryColor3dv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glSecondaryColor3d(GLdouble red,
//      GLdouble green, GLdouble blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility18glSecondaryColor3dEddd(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLdouble red,
    GLdouble green,
    GLdouble blue) {
  self->glSecondaryColor3d(red, green, blue);
}

//  void QOpenGLFunctions_3_2_Compatibility::glSecondaryColor3bv(const GLbyte
//      *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility19glSecondaryColor3bvEPKa(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLbyte *v) {
  self->glSecondaryColor3bv(v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glSecondaryColor3b(GLbyte red,
//      GLbyte green, GLbyte blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility18glSecondaryColor3bEaaa(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLbyte red,
    GLbyte green,
    GLbyte blue) {
  self->glSecondaryColor3b(red, green, blue);
}

//  void QOpenGLFunctions_3_2_Compatibility::glFogCoordPointer(GLenum type,
//      GLsizei stride, const GLvoid *pointer)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility17glFogCoordPointerEjiPKv(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLenum type,
    GLsizei stride,
    const GLvoid *pointer) {
  self->glFogCoordPointer(type, stride, pointer);
}

//  void QOpenGLFunctions_3_2_Compatibility::glFogCoorddv(const GLdouble
//      *coord)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glFogCoorddvEPKd(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLdouble *coord) {
  self->glFogCoorddv(coord);
}

//  void QOpenGLFunctions_3_2_Compatibility::glFogCoordd(GLdouble coord)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility11glFogCoorddEd(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLdouble coord) {
  self->glFogCoordd(coord);
}

//  void QOpenGLFunctions_3_2_Compatibility::glFogCoordfv(const GLfloat
//      *coord)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility12glFogCoordfvEPKf(
    QOpenGLFunctions_3_2_Compatibility *self,
    const GLfloat *coord) {
  self->glFogCoordfv(coord);
}

//  void QOpenGLFunctions_3_2_Compatibility::glFogCoordf(GLfloat coord)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility11glFogCoordfEf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLfloat coord) {
  self->glFogCoordf(coord);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertexAttrib4usv(GLuint index,
//      const GLushort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility18glVertexAttrib4usvEjPKt(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint index,
    const GLushort *v) {
  self->glVertexAttrib4usv(index, v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertexAttrib4uiv(GLuint index,
//      const GLuint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility18glVertexAttrib4uivEjPKj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint index,
    const GLuint *v) {
  self->glVertexAttrib4uiv(index, v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertexAttrib4ubv(GLuint index,
//      const GLubyte *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility18glVertexAttrib4ubvEjPKh(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint index,
    const GLubyte *v) {
  self->glVertexAttrib4ubv(index, v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertexAttrib4sv(GLuint index,
//      const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility17glVertexAttrib4svEjPKs(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint index,
    const GLshort *v) {
  self->glVertexAttrib4sv(index, v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertexAttrib4s(GLuint index,
//      GLshort x, GLshort y, GLshort z, GLshort w)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility16glVertexAttrib4sEjssss(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint index,
    GLshort x,
    GLshort y,
    GLshort z,
    GLshort w) {
  self->glVertexAttrib4s(index, x, y, z, w);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertexAttrib4iv(GLuint index,
//      const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility17glVertexAttrib4ivEjPKi(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint index,
    const GLint *v) {
  self->glVertexAttrib4iv(index, v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertexAttrib4fv(GLuint index,
//      const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility17glVertexAttrib4fvEjPKf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint index,
    const GLfloat *v) {
  self->glVertexAttrib4fv(index, v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertexAttrib4f(GLuint index,
//      GLfloat x, GLfloat y, GLfloat z, GLfloat w)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility16glVertexAttrib4fEjffff(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint index,
    GLfloat x,
    GLfloat y,
    GLfloat z,
    GLfloat w) {
  self->glVertexAttrib4f(index, x, y, z, w);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertexAttrib4dv(GLuint index,
//      const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility17glVertexAttrib4dvEjPKd(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint index,
    const GLdouble *v) {
  self->glVertexAttrib4dv(index, v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertexAttrib4d(GLuint index,
//      GLdouble x, GLdouble y, GLdouble z, GLdouble w)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility16glVertexAttrib4dEjdddd(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint index,
    GLdouble x,
    GLdouble y,
    GLdouble z,
    GLdouble w) {
  self->glVertexAttrib4d(index, x, y, z, w);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertexAttrib4bv(GLuint index,
//      const GLbyte *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility17glVertexAttrib4bvEjPKa(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint index,
    const GLbyte *v) {
  self->glVertexAttrib4bv(index, v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertexAttrib4Nusv(GLuint
//      index, const GLushort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility19glVertexAttrib4NusvEjPKt(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint index,
    const GLushort *v) {
  self->glVertexAttrib4Nusv(index, v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertexAttrib4Nuiv(GLuint
//      index, const GLuint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility19glVertexAttrib4NuivEjPKj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint index,
    const GLuint *v) {
  self->glVertexAttrib4Nuiv(index, v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertexAttrib4Nubv(GLuint
//      index, const GLubyte *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility19glVertexAttrib4NubvEjPKh(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint index,
    const GLubyte *v) {
  self->glVertexAttrib4Nubv(index, v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertexAttrib4Nub(GLuint index,
//      GLubyte x, GLubyte y, GLubyte z, GLubyte w)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility18glVertexAttrib4NubEjhhhh(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint index,
    GLubyte x,
    GLubyte y,
    GLubyte z,
    GLubyte w) {
  self->glVertexAttrib4Nub(index, x, y, z, w);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertexAttrib4Nsv(GLuint index,
//      const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility18glVertexAttrib4NsvEjPKs(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint index,
    const GLshort *v) {
  self->glVertexAttrib4Nsv(index, v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertexAttrib4Niv(GLuint index,
//      const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility18glVertexAttrib4NivEjPKi(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint index,
    const GLint *v) {
  self->glVertexAttrib4Niv(index, v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertexAttrib4Nbv(GLuint index,
//      const GLbyte *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility18glVertexAttrib4NbvEjPKa(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint index,
    const GLbyte *v) {
  self->glVertexAttrib4Nbv(index, v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertexAttrib3sv(GLuint index,
//      const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility17glVertexAttrib3svEjPKs(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint index,
    const GLshort *v) {
  self->glVertexAttrib3sv(index, v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertexAttrib3s(GLuint index,
//      GLshort x, GLshort y, GLshort z)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility16glVertexAttrib3sEjsss(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint index,
    GLshort x,
    GLshort y,
    GLshort z) {
  self->glVertexAttrib3s(index, x, y, z);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertexAttrib3fv(GLuint index,
//      const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility17glVertexAttrib3fvEjPKf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint index,
    const GLfloat *v) {
  self->glVertexAttrib3fv(index, v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertexAttrib3f(GLuint index,
//      GLfloat x, GLfloat y, GLfloat z)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility16glVertexAttrib3fEjfff(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint index,
    GLfloat x,
    GLfloat y,
    GLfloat z) {
  self->glVertexAttrib3f(index, x, y, z);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertexAttrib3dv(GLuint index,
//      const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility17glVertexAttrib3dvEjPKd(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint index,
    const GLdouble *v) {
  self->glVertexAttrib3dv(index, v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertexAttrib3d(GLuint index,
//      GLdouble x, GLdouble y, GLdouble z)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility16glVertexAttrib3dEjddd(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint index,
    GLdouble x,
    GLdouble y,
    GLdouble z) {
  self->glVertexAttrib3d(index, x, y, z);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertexAttrib2sv(GLuint index,
//      const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility17glVertexAttrib2svEjPKs(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint index,
    const GLshort *v) {
  self->glVertexAttrib2sv(index, v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertexAttrib2s(GLuint index,
//      GLshort x, GLshort y)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility16glVertexAttrib2sEjss(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint index,
    GLshort x,
    GLshort y) {
  self->glVertexAttrib2s(index, x, y);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertexAttrib2fv(GLuint index,
//      const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility17glVertexAttrib2fvEjPKf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint index,
    const GLfloat *v) {
  self->glVertexAttrib2fv(index, v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertexAttrib2f(GLuint index,
//      GLfloat x, GLfloat y)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility16glVertexAttrib2fEjff(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint index,
    GLfloat x,
    GLfloat y) {
  self->glVertexAttrib2f(index, x, y);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertexAttrib2dv(GLuint index,
//      const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility17glVertexAttrib2dvEjPKd(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint index,
    const GLdouble *v) {
  self->glVertexAttrib2dv(index, v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertexAttrib2d(GLuint index,
//      GLdouble x, GLdouble y)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility16glVertexAttrib2dEjdd(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint index,
    GLdouble x,
    GLdouble y) {
  self->glVertexAttrib2d(index, x, y);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertexAttrib1sv(GLuint index,
//      const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility17glVertexAttrib1svEjPKs(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint index,
    const GLshort *v) {
  self->glVertexAttrib1sv(index, v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertexAttrib1s(GLuint index,
//      GLshort x)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility16glVertexAttrib1sEjs(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint index,
    GLshort x) {
  self->glVertexAttrib1s(index, x);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertexAttrib1fv(GLuint index,
//      const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility17glVertexAttrib1fvEjPKf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint index,
    const GLfloat *v) {
  self->glVertexAttrib1fv(index, v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertexAttrib1f(GLuint index,
//      GLfloat x)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility16glVertexAttrib1fEjf(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint index,
    GLfloat x) {
  self->glVertexAttrib1f(index, x);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertexAttrib1dv(GLuint index,
//      const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility17glVertexAttrib1dvEjPKd(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint index,
    const GLdouble *v) {
  self->glVertexAttrib1dv(index, v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertexAttrib1d(GLuint index,
//      GLdouble x)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility16glVertexAttrib1dEjd(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint index,
    GLdouble x) {
  self->glVertexAttrib1d(index, x);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertexAttribI4usv(GLuint
//      index, const GLushort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility19glVertexAttribI4usvEjPKt(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint index,
    const GLushort *v) {
  self->glVertexAttribI4usv(index, v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertexAttribI4ubv(GLuint
//      index, const GLubyte *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility19glVertexAttribI4ubvEjPKh(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint index,
    const GLubyte *v) {
  self->glVertexAttribI4ubv(index, v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertexAttribI4sv(GLuint index,
//      const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility18glVertexAttribI4svEjPKs(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint index,
    const GLshort *v) {
  self->glVertexAttribI4sv(index, v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertexAttribI4bv(GLuint index,
//      const GLbyte *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility18glVertexAttribI4bvEjPKa(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint index,
    const GLbyte *v) {
  self->glVertexAttribI4bv(index, v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertexAttribI4uiv(GLuint
//      index, const GLuint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility19glVertexAttribI4uivEjPKj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint index,
    const GLuint *v) {
  self->glVertexAttribI4uiv(index, v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertexAttribI3uiv(GLuint
//      index, const GLuint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility19glVertexAttribI3uivEjPKj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint index,
    const GLuint *v) {
  self->glVertexAttribI3uiv(index, v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertexAttribI2uiv(GLuint
//      index, const GLuint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility19glVertexAttribI2uivEjPKj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint index,
    const GLuint *v) {
  self->glVertexAttribI2uiv(index, v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertexAttribI1uiv(GLuint
//      index, const GLuint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility19glVertexAttribI1uivEjPKj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint index,
    const GLuint *v) {
  self->glVertexAttribI1uiv(index, v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertexAttribI4iv(GLuint index,
//      const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility18glVertexAttribI4ivEjPKi(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint index,
    const GLint *v) {
  self->glVertexAttribI4iv(index, v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertexAttribI3iv(GLuint index,
//      const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility18glVertexAttribI3ivEjPKi(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint index,
    const GLint *v) {
  self->glVertexAttribI3iv(index, v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertexAttribI2iv(GLuint index,
//      const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility18glVertexAttribI2ivEjPKi(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint index,
    const GLint *v) {
  self->glVertexAttribI2iv(index, v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertexAttribI1iv(GLuint index,
//      const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility18glVertexAttribI1ivEjPKi(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint index,
    const GLint *v) {
  self->glVertexAttribI1iv(index, v);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertexAttribI4ui(GLuint index,
//      GLuint x, GLuint y, GLuint z, GLuint w)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility18glVertexAttribI4uiEjjjjj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint index,
    GLuint x,
    GLuint y,
    GLuint z,
    GLuint w) {
  self->glVertexAttribI4ui(index, x, y, z, w);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertexAttribI3ui(GLuint index,
//      GLuint x, GLuint y, GLuint z)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility18glVertexAttribI3uiEjjjj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint index,
    GLuint x,
    GLuint y,
    GLuint z) {
  self->glVertexAttribI3ui(index, x, y, z);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertexAttribI2ui(GLuint index,
//      GLuint x, GLuint y)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility18glVertexAttribI2uiEjjj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint index,
    GLuint x,
    GLuint y) {
  self->glVertexAttribI2ui(index, x, y);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertexAttribI1ui(GLuint index,
//      GLuint x)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility18glVertexAttribI1uiEjj(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint index,
    GLuint x) {
  self->glVertexAttribI1ui(index, x);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertexAttribI4i(GLuint index,
//      GLint x, GLint y, GLint z, GLint w)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility17glVertexAttribI4iEjiiii(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint index,
    GLint x,
    GLint y,
    GLint z,
    GLint w) {
  self->glVertexAttribI4i(index, x, y, z, w);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertexAttribI3i(GLuint index,
//      GLint x, GLint y, GLint z)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility17glVertexAttribI3iEjiii(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint index,
    GLint x,
    GLint y,
    GLint z) {
  self->glVertexAttribI3i(index, x, y, z);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertexAttribI2i(GLuint index,
//      GLint x, GLint y)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility17glVertexAttribI2iEjii(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint index,
    GLint x,
    GLint y) {
  self->glVertexAttribI2i(index, x, y);
}

//  void QOpenGLFunctions_3_2_Compatibility::glVertexAttribI1i(GLuint index,
//      GLint x)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_3_2_Compatibility17glVertexAttribI1iEji(
    QOpenGLFunctions_3_2_Compatibility *self,
    GLuint index,
    GLint x) {
  self->glVertexAttribI1i(index, x);
}

//  bool
//      QOpenGLFunctions_3_2_Compatibility::isContextCompatible(QOpenGLContex
//      t *context)
extern "C" Q_DECL_EXPORT
bool ritual_ZN34QOpenGLFunctions_3_2_Compatibility19isContextCompatibleEP14QOpenGLContext(
    QOpenGLContext *context) {
  return QOpenGLFunctions_3_2_Compatibility::isContextCompatible(context);
}

//  QOpenGLVersionProfile
//      QOpenGLFunctions_3_2_Compatibility::versionProfile()
extern "C" Q_DECL_EXPORT
QOpenGLVersionProfile *ritual_ZN34QOpenGLFunctions_3_2_Compatibility14versionProfileEv() {
  return new QOpenGLVersionProfile(
      QOpenGLFunctions_3_2_Compatibility::versionProfile());
}

//  a Python function taken by a CuteQOpenGLFunctions_3_2_Compatibility, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QOpenGLFunctions_3_2_Compatibility(
    QOpenGLFunctions_3_2_Compatibility *self,
    const char *key,
    void *call) {
  return static_cast<CuteQOpenGLFunctions_3_2_Compatibility *>(self)->take(key, call);
}

//  bool QOpenGLFunctions_3_2_Compatibility::initializeOpenGLFunctions()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN34QOpenGLFunctions_3_2_Compatibility25initializeOpenGLFunctionsEv(
    QOpenGLFunctions_3_2_Compatibility *self) {
  return self->QOpenGLFunctions_3_2_Compatibility::initializeOpenGLFunctions();
}

#endif  // !defined(QT_NO_OPENGL) && !QT_CONFIG(opengles2)
#endif  // !QT_CONFIG(opengles2)
