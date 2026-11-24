//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/qopenglfunctions_4_1_compatibility.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtOpenGL/qtopenglglobal.h>
#if !defined(QT_NO_OPENGL) && !QT_CONFIG(opengles2)
#include <QtOpenGL/QtOpenGL>
#include <QtOpenGL/qopenglfunctions_4_1_compatibility.h>
#include <QtOpenGL/qopenglversionprofile.h>
#include <cstring>

//  A QOpenGLFunctions_4_1_Compatibility that Python can take functions over in. Every QOpenGLFunctions_4_1_Compatibility
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL) && !QT_CONFIG(opengles2)
typedef bool (*CuteQOpenGLFunctions_4_1_CompatibilityCall0)(const void *, int *);
#endif  // !defined(QT_NO_OPENGL) && !QT_CONFIG(opengles2)
#endif  // !defined(QT_NO_OPENGL)
class CuteQOpenGLFunctions_4_1_Compatibility : public QOpenGLFunctions_4_1_Compatibility {
public:
  using QOpenGLFunctions_4_1_Compatibility::QOpenGLFunctions_4_1_Compatibility;
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
  //  bool QOpenGLFunctions_4_1_Compatibility::initializeOpenGLFunctions()
  bool initializeOpenGLFunctions() override {
    if (taken[0]) {
      int handled = 0;
      CuteQOpenGLFunctions_4_1_CompatibilityCall0 call = reinterpret_cast<CuteQOpenGLFunctions_4_1_CompatibilityCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QOpenGLFunctions_4_1_Compatibility::initializeOpenGLFunctions();
  }
#endif  // !defined(QT_NO_OPENGL) && !QT_CONFIG(opengles2)
#endif  // !defined(QT_NO_OPENGL)
};

//  QOpenGLFunctions_4_1_Compatibility::QOpenGLFunctions_4_1_Compatibility()
extern "C" Q_DECL_EXPORT
QOpenGLFunctions_4_1_Compatibility *ritual_ZN34QOpenGLFunctions_4_1_CompatibilityC1Ev() {
  return new CuteQOpenGLFunctions_4_1_Compatibility();
}

//  QOpenGLFunctions_4_1_Compatibility::~QOpenGLFunctions_4_1_Compatibility()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_CompatibilityD1Ev(
    QOpenGLFunctions_4_1_Compatibility *self) {
  delete self;
}

//  bool QOpenGLFunctions_4_1_Compatibility::initializeOpenGLFunctions()
extern "C" Q_DECL_EXPORT
bool ritual_ZN34QOpenGLFunctions_4_1_Compatibility25initializeOpenGLFunctionsEv(
    QOpenGLFunctions_4_1_Compatibility *self) {
  return self->initializeOpenGLFunctions();
}

//  void QOpenGLFunctions_4_1_Compatibility::glViewport(GLint x, GLint y,
//      GLsizei width, GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility10glViewportEiiii(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLint x,
    GLint y,
    GLsizei width,
    GLsizei height) {
  self->glViewport(x, y, width, height);
}

//  void QOpenGLFunctions_4_1_Compatibility::glDepthRange(GLdouble nearVal,
//      GLdouble farVal)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility12glDepthRangeEdd(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLdouble nearVal,
    GLdouble farVal) {
  self->glDepthRange(nearVal, farVal);
}

//  void QOpenGLFunctions_4_1_Compatibility::glReadBuffer(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility12glReadBufferEj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum mode) {
  self->glReadBuffer(mode);
}

//  void QOpenGLFunctions_4_1_Compatibility::glPixelStorei(GLenum pname,
//      GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility13glPixelStoreiEji(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum pname,
    GLint param) {
  self->glPixelStorei(pname, param);
}

//  void QOpenGLFunctions_4_1_Compatibility::glPixelStoref(GLenum pname,
//      GLfloat param)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility13glPixelStorefEjf(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum pname,
    GLfloat param) {
  self->glPixelStoref(pname, param);
}

//  void QOpenGLFunctions_4_1_Compatibility::glDepthFunc(GLenum func)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility11glDepthFuncEj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum func) {
  self->glDepthFunc(func);
}

//  void QOpenGLFunctions_4_1_Compatibility::glStencilOp(GLenum fail, GLenum
//      zfail, GLenum zpass)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility11glStencilOpEjjj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum fail,
    GLenum zfail,
    GLenum zpass) {
  self->glStencilOp(fail, zfail, zpass);
}

//  void QOpenGLFunctions_4_1_Compatibility::glStencilFunc(GLenum func, GLint
//      ref, GLuint mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility13glStencilFuncEjij(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum func,
    GLint ref,
    GLuint mask) {
  self->glStencilFunc(func, ref, mask);
}

//  void QOpenGLFunctions_4_1_Compatibility::glLogicOp(GLenum opcode)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility9glLogicOpEj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum opcode) {
  self->glLogicOp(opcode);
}

//  void QOpenGLFunctions_4_1_Compatibility::glBlendFunc(GLenum sfactor,
//      GLenum dfactor)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility11glBlendFuncEjj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum sfactor,
    GLenum dfactor) {
  self->glBlendFunc(sfactor, dfactor);
}

//  void QOpenGLFunctions_4_1_Compatibility::glFlush()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility7glFlushEv(
    QOpenGLFunctions_4_1_Compatibility *self) {
  self->glFlush();
}

//  void QOpenGLFunctions_4_1_Compatibility::glFinish()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility8glFinishEv(
    QOpenGLFunctions_4_1_Compatibility *self) {
  self->glFinish();
}

//  void QOpenGLFunctions_4_1_Compatibility::glEnable(GLenum cap)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility8glEnableEj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum cap) {
  self->glEnable(cap);
}

//  void QOpenGLFunctions_4_1_Compatibility::glDisable(GLenum cap)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility9glDisableEj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum cap) {
  self->glDisable(cap);
}

//  void QOpenGLFunctions_4_1_Compatibility::glDepthMask(GLboolean flag)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility11glDepthMaskEh(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLboolean flag) {
  self->glDepthMask(flag);
}

//  void QOpenGLFunctions_4_1_Compatibility::glColorMask(GLboolean red,
//      GLboolean green, GLboolean blue, GLboolean alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility11glColorMaskEhhhh(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLboolean red,
    GLboolean green,
    GLboolean blue,
    GLboolean alpha) {
  self->glColorMask(red, green, blue, alpha);
}

//  void QOpenGLFunctions_4_1_Compatibility::glStencilMask(GLuint mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility13glStencilMaskEj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint mask) {
  self->glStencilMask(mask);
}

//  void QOpenGLFunctions_4_1_Compatibility::glClearDepth(GLdouble depth)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility12glClearDepthEd(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLdouble depth) {
  self->glClearDepth(depth);
}

//  void QOpenGLFunctions_4_1_Compatibility::glClearStencil(GLint s)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility14glClearStencilEi(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLint s) {
  self->glClearStencil(s);
}

//  void QOpenGLFunctions_4_1_Compatibility::glClearColor(GLfloat red,
//      GLfloat green, GLfloat blue, GLfloat alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility12glClearColorEffff(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLfloat red,
    GLfloat green,
    GLfloat blue,
    GLfloat alpha) {
  self->glClearColor(red, green, blue, alpha);
}

//  void QOpenGLFunctions_4_1_Compatibility::glClear(GLbitfield mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility7glClearEj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLbitfield mask) {
  self->glClear(mask);
}

//  void QOpenGLFunctions_4_1_Compatibility::glDrawBuffer(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility12glDrawBufferEj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum mode) {
  self->glDrawBuffer(mode);
}

//  void QOpenGLFunctions_4_1_Compatibility::glTexParameteri(GLenum target,
//      GLenum pname, GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility15glTexParameteriEjji(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum target,
    GLenum pname,
    GLint param) {
  self->glTexParameteri(target, pname, param);
}

//  void QOpenGLFunctions_4_1_Compatibility::glTexParameterf(GLenum target,
//      GLenum pname, GLfloat param)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility15glTexParameterfEjjf(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum target,
    GLenum pname,
    GLfloat param) {
  self->glTexParameterf(target, pname, param);
}

//  void QOpenGLFunctions_4_1_Compatibility::glScissor(GLint x, GLint y,
//      GLsizei width, GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility9glScissorEiiii(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLint x,
    GLint y,
    GLsizei width,
    GLsizei height) {
  self->glScissor(x, y, width, height);
}

//  void QOpenGLFunctions_4_1_Compatibility::glPolygonMode(GLenum face,
//      GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility13glPolygonModeEjj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum face,
    GLenum mode) {
  self->glPolygonMode(face, mode);
}

//  void QOpenGLFunctions_4_1_Compatibility::glPointSize(GLfloat size)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility11glPointSizeEf(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLfloat size) {
  self->glPointSize(size);
}

//  void QOpenGLFunctions_4_1_Compatibility::glLineWidth(GLfloat width)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility11glLineWidthEf(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLfloat width) {
  self->glLineWidth(width);
}

//  void QOpenGLFunctions_4_1_Compatibility::glHint(GLenum target, GLenum
//      mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility6glHintEjj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum target,
    GLenum mode) {
  self->glHint(target, mode);
}

//  void QOpenGLFunctions_4_1_Compatibility::glFrontFace(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility11glFrontFaceEj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum mode) {
  self->glFrontFace(mode);
}

//  void QOpenGLFunctions_4_1_Compatibility::glCullFace(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility10glCullFaceEj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum mode) {
  self->glCullFace(mode);
}

//  void QOpenGLFunctions_4_1_Compatibility::glIndexub(GLubyte c)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility9glIndexubEh(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLubyte c) {
  self->glIndexub(c);
}

//  void QOpenGLFunctions_4_1_Compatibility::glBindTexture(GLenum target,
//      GLuint texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility13glBindTextureEjj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum target,
    GLuint texture) {
  self->glBindTexture(target, texture);
}

//  void QOpenGLFunctions_4_1_Compatibility::glCopyTexSubImage2D(GLenum
//      target, GLint level, GLint xoffset, GLint yoffset, GLint x, GLint y,
//      GLsizei width, GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility19glCopyTexSubImage2DEjiiiiiii(
    QOpenGLFunctions_4_1_Compatibility *self,
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

//  void QOpenGLFunctions_4_1_Compatibility::glCopyTexSubImage1D(GLenum
//      target, GLint level, GLint xoffset, GLint x, GLint y, GLsizei width)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility19glCopyTexSubImage1DEjiiiii(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum target,
    GLint level,
    GLint xoffset,
    GLint x,
    GLint y,
    GLsizei width) {
  self->glCopyTexSubImage1D(target, level, xoffset, x, y, width);
}

//  void QOpenGLFunctions_4_1_Compatibility::glCopyTexImage2D(GLenum target,
//      GLint level, GLenum internalformat, GLint x, GLint y, GLsizei width,
//      GLsizei height, GLint border)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility16glCopyTexImage2DEjijiiiii(
    QOpenGLFunctions_4_1_Compatibility *self,
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

//  void QOpenGLFunctions_4_1_Compatibility::glCopyTexImage1D(GLenum target,
//      GLint level, GLenum internalformat, GLint x, GLint y, GLsizei width,
//      GLint border)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility16glCopyTexImage1DEjijiiii(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum target,
    GLint level,
    GLenum internalformat,
    GLint x,
    GLint y,
    GLsizei width,
    GLint border) {
  self->glCopyTexImage1D(target, level, internalformat, x, y, width, border);
}

//  void QOpenGLFunctions_4_1_Compatibility::glPolygonOffset(GLfloat factor,
//      GLfloat units)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility15glPolygonOffsetEff(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLfloat factor,
    GLfloat units) {
  self->glPolygonOffset(factor, units);
}

//  void QOpenGLFunctions_4_1_Compatibility::glDrawArrays(GLenum mode, GLint
//      first, GLsizei count)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility12glDrawArraysEjii(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum mode,
    GLint first,
    GLsizei count) {
  self->glDrawArrays(mode, first, count);
}

//  void QOpenGLFunctions_4_1_Compatibility::glCopyTexSubImage3D(GLenum
//      target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset,
//      GLint x, GLint y, GLsizei width, GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility19glCopyTexSubImage3DEjiiiiiiii(
    QOpenGLFunctions_4_1_Compatibility *self,
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

//  void QOpenGLFunctions_4_1_Compatibility::glBlendEquation(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility15glBlendEquationEj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum mode) {
  self->glBlendEquation(mode);
}

//  void QOpenGLFunctions_4_1_Compatibility::glBlendColor(GLfloat red,
//      GLfloat green, GLfloat blue, GLfloat alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility12glBlendColorEffff(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLfloat red,
    GLfloat green,
    GLfloat blue,
    GLfloat alpha) {
  self->glBlendColor(red, green, blue, alpha);
}

//  void QOpenGLFunctions_4_1_Compatibility::glSampleCoverage(GLfloat value,
//      GLboolean invert)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility16glSampleCoverageEfh(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLfloat value,
    GLboolean invert) {
  self->glSampleCoverage(value, invert);
}

//  void QOpenGLFunctions_4_1_Compatibility::glActiveTexture(GLenum texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility15glActiveTextureEj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum texture) {
  self->glActiveTexture(texture);
}

//  void QOpenGLFunctions_4_1_Compatibility::glPointParameteri(GLenum pname,
//      GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility17glPointParameteriEji(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum pname,
    GLint param) {
  self->glPointParameteri(pname, param);
}

//  void QOpenGLFunctions_4_1_Compatibility::glPointParameterf(GLenum pname,
//      GLfloat param)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility17glPointParameterfEjf(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum pname,
    GLfloat param) {
  self->glPointParameterf(pname, param);
}

//  void QOpenGLFunctions_4_1_Compatibility::glBlendFuncSeparate(GLenum
//      sfactorRGB, GLenum dfactorRGB, GLenum sfactorAlpha, GLenum
//      dfactorAlpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility19glBlendFuncSeparateEjjjj(
    QOpenGLFunctions_4_1_Compatibility *self,
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

//  void QOpenGLFunctions_4_1_Compatibility::glBindBuffer(GLenum target,
//      GLuint buffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility12glBindBufferEjj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum target,
    GLuint buffer) {
  self->glBindBuffer(target, buffer);
}

//  void QOpenGLFunctions_4_1_Compatibility::glEndQuery(GLenum target)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility10glEndQueryEj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum target) {
  self->glEndQuery(target);
}

//  void QOpenGLFunctions_4_1_Compatibility::glBeginQuery(GLenum target,
//      GLuint id)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility12glBeginQueryEjj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum target,
    GLuint id) {
  self->glBeginQuery(target, id);
}

//  void QOpenGLFunctions_4_1_Compatibility::glValidateProgram(GLuint
//      program)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility17glValidateProgramEj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint program) {
  self->glValidateProgram(program);
}

//  void QOpenGLFunctions_4_1_Compatibility::glUniform4i(GLint location,
//      GLint v0, GLint v1, GLint v2, GLint v3)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility11glUniform4iEiiiii(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLint location,
    GLint v0,
    GLint v1,
    GLint v2,
    GLint v3) {
  self->glUniform4i(location, v0, v1, v2, v3);
}

//  void QOpenGLFunctions_4_1_Compatibility::glUniform3i(GLint location,
//      GLint v0, GLint v1, GLint v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility11glUniform3iEiiii(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLint location,
    GLint v0,
    GLint v1,
    GLint v2) {
  self->glUniform3i(location, v0, v1, v2);
}

//  void QOpenGLFunctions_4_1_Compatibility::glUniform2i(GLint location,
//      GLint v0, GLint v1)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility11glUniform2iEiii(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLint location,
    GLint v0,
    GLint v1) {
  self->glUniform2i(location, v0, v1);
}

//  void QOpenGLFunctions_4_1_Compatibility::glUniform1i(GLint location,
//      GLint v0)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility11glUniform1iEii(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLint location,
    GLint v0) {
  self->glUniform1i(location, v0);
}

//  void QOpenGLFunctions_4_1_Compatibility::glUniform4f(GLint location,
//      GLfloat v0, GLfloat v1, GLfloat v2, GLfloat v3)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility11glUniform4fEiffff(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLint location,
    GLfloat v0,
    GLfloat v1,
    GLfloat v2,
    GLfloat v3) {
  self->glUniform4f(location, v0, v1, v2, v3);
}

//  void QOpenGLFunctions_4_1_Compatibility::glUniform3f(GLint location,
//      GLfloat v0, GLfloat v1, GLfloat v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility11glUniform3fEifff(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLint location,
    GLfloat v0,
    GLfloat v1,
    GLfloat v2) {
  self->glUniform3f(location, v0, v1, v2);
}

//  void QOpenGLFunctions_4_1_Compatibility::glUniform2f(GLint location,
//      GLfloat v0, GLfloat v1)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility11glUniform2fEiff(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLint location,
    GLfloat v0,
    GLfloat v1) {
  self->glUniform2f(location, v0, v1);
}

//  void QOpenGLFunctions_4_1_Compatibility::glUniform1f(GLint location,
//      GLfloat v0)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility11glUniform1fEif(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLint location,
    GLfloat v0) {
  self->glUniform1f(location, v0);
}

//  void QOpenGLFunctions_4_1_Compatibility::glUseProgram(GLuint program)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility12glUseProgramEj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint program) {
  self->glUseProgram(program);
}

//  void QOpenGLFunctions_4_1_Compatibility::glLinkProgram(GLuint program)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility13glLinkProgramEj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint program) {
  self->glLinkProgram(program);
}

//  void QOpenGLFunctions_4_1_Compatibility::glEnableVertexAttribArray(GLuint
//      index)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility25glEnableVertexAttribArrayEj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint index) {
  self->glEnableVertexAttribArray(index);
}

//  void
//      QOpenGLFunctions_4_1_Compatibility::glDisableVertexAttribArray(GLuint
//      index)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility26glDisableVertexAttribArrayEj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint index) {
  self->glDisableVertexAttribArray(index);
}

//  void QOpenGLFunctions_4_1_Compatibility::glDetachShader(GLuint program,
//      GLuint shader)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility14glDetachShaderEjj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint program,
    GLuint shader) {
  self->glDetachShader(program, shader);
}

//  void QOpenGLFunctions_4_1_Compatibility::glDeleteShader(GLuint shader)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility14glDeleteShaderEj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint shader) {
  self->glDeleteShader(shader);
}

//  void QOpenGLFunctions_4_1_Compatibility::glDeleteProgram(GLuint program)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility15glDeleteProgramEj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint program) {
  self->glDeleteProgram(program);
}

//  void QOpenGLFunctions_4_1_Compatibility::glCompileShader(GLuint shader)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility15glCompileShaderEj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint shader) {
  self->glCompileShader(shader);
}

//  void QOpenGLFunctions_4_1_Compatibility::glAttachShader(GLuint program,
//      GLuint shader)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility14glAttachShaderEjj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint program,
    GLuint shader) {
  self->glAttachShader(program, shader);
}

//  void QOpenGLFunctions_4_1_Compatibility::glStencilMaskSeparate(GLenum
//      face, GLuint mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility21glStencilMaskSeparateEjj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum face,
    GLuint mask) {
  self->glStencilMaskSeparate(face, mask);
}

//  void QOpenGLFunctions_4_1_Compatibility::glStencilFuncSeparate(GLenum
//      face, GLenum func, GLint ref, GLuint mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility21glStencilFuncSeparateEjjij(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum face,
    GLenum func,
    GLint ref,
    GLuint mask) {
  self->glStencilFuncSeparate(face, func, ref, mask);
}

//  void QOpenGLFunctions_4_1_Compatibility::glStencilOpSeparate(GLenum face,
//      GLenum sfail, GLenum dpfail, GLenum dppass)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility19glStencilOpSeparateEjjjj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum face,
    GLenum sfail,
    GLenum dpfail,
    GLenum dppass) {
  self->glStencilOpSeparate(face, sfail, dpfail, dppass);
}

//  void QOpenGLFunctions_4_1_Compatibility::glBlendEquationSeparate(GLenum
//      modeRGB, GLenum modeAlpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility23glBlendEquationSeparateEjj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum modeRGB,
    GLenum modeAlpha) {
  self->glBlendEquationSeparate(modeRGB, modeAlpha);
}

//  void QOpenGLFunctions_4_1_Compatibility::glBindVertexArray(GLuint array)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility17glBindVertexArrayEj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint array) {
  self->glBindVertexArray(array);
}

//  void QOpenGLFunctions_4_1_Compatibility::glFramebufferTextureLayer(GLenum
//      target, GLenum attachment, GLuint texture, GLint level, GLint layer)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility25glFramebufferTextureLayerEjjjii(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum target,
    GLenum attachment,
    GLuint texture,
    GLint level,
    GLint layer) {
  self->glFramebufferTextureLayer(target, attachment, texture, level, layer);
}

//  void QOpenGLFunctions_4_1_Compatibility::glRenderbufferStorageMultisample
//      (GLenum target, GLsizei samples, GLenum internalformat, GLsizei
//      width, GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility32glRenderbufferStorageMultisampleEjijii(
    QOpenGLFunctions_4_1_Compatibility *self,
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

//  void QOpenGLFunctions_4_1_Compatibility::glBlitFramebuffer(GLint srcX0,
//      GLint srcY0, GLint srcX1, GLint srcY1, GLint dstX0, GLint dstY0,
//      GLint dstX1, GLint dstY1, GLbitfield mask, GLenum filter)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility17glBlitFramebufferEiiiiiiiijj(
    QOpenGLFunctions_4_1_Compatibility *self,
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

//  void QOpenGLFunctions_4_1_Compatibility::glGenerateMipmap(GLenum target)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility16glGenerateMipmapEj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum target) {
  self->glGenerateMipmap(target);
}

//  void QOpenGLFunctions_4_1_Compatibility::glFramebufferRenderbuffer(GLenum
//      target, GLenum attachment, GLenum renderbuffertarget, GLuint
//      renderbuffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility25glFramebufferRenderbufferEjjjj(
    QOpenGLFunctions_4_1_Compatibility *self,
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

//  void QOpenGLFunctions_4_1_Compatibility::glFramebufferTexture3D(GLenum
//      target, GLenum attachment, GLenum textarget, GLuint texture, GLint
//      level, GLint zoffset)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility22glFramebufferTexture3DEjjjjii(
    QOpenGLFunctions_4_1_Compatibility *self,
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

//  void QOpenGLFunctions_4_1_Compatibility::glFramebufferTexture2D(GLenum
//      target, GLenum attachment, GLenum textarget, GLuint texture, GLint
//      level)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility22glFramebufferTexture2DEjjjji(
    QOpenGLFunctions_4_1_Compatibility *self,
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

//  void QOpenGLFunctions_4_1_Compatibility::glFramebufferTexture1D(GLenum
//      target, GLenum attachment, GLenum textarget, GLuint texture, GLint
//      level)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility22glFramebufferTexture1DEjjjji(
    QOpenGLFunctions_4_1_Compatibility *self,
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

//  void QOpenGLFunctions_4_1_Compatibility::glBindFramebuffer(GLenum target,
//      GLuint framebuffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility17glBindFramebufferEjj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum target,
    GLuint framebuffer) {
  self->glBindFramebuffer(target, framebuffer);
}

//  void QOpenGLFunctions_4_1_Compatibility::glRenderbufferStorage(GLenum
//      target, GLenum internalformat, GLsizei width, GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility21glRenderbufferStorageEjjii(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum target,
    GLenum internalformat,
    GLsizei width,
    GLsizei height) {
  self->glRenderbufferStorage(target, internalformat, width, height);
}

//  void QOpenGLFunctions_4_1_Compatibility::glBindRenderbuffer(GLenum
//      target, GLuint renderbuffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility18glBindRenderbufferEjj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum target,
    GLuint renderbuffer) {
  self->glBindRenderbuffer(target, renderbuffer);
}

//  void QOpenGLFunctions_4_1_Compatibility::glClearBufferfi(GLenum buffer,
//      GLint drawbuffer, GLfloat depth, GLint stencil)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility15glClearBufferfiEjifi(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum buffer,
    GLint drawbuffer,
    GLfloat depth,
    GLint stencil) {
  self->glClearBufferfi(buffer, drawbuffer, depth, stencil);
}

//  void QOpenGLFunctions_4_1_Compatibility::glUniform4ui(GLint location,
//      GLuint v0, GLuint v1, GLuint v2, GLuint v3)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility12glUniform4uiEijjjj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLint location,
    GLuint v0,
    GLuint v1,
    GLuint v2,
    GLuint v3) {
  self->glUniform4ui(location, v0, v1, v2, v3);
}

//  void QOpenGLFunctions_4_1_Compatibility::glUniform3ui(GLint location,
//      GLuint v0, GLuint v1, GLuint v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility12glUniform3uiEijjj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLint location,
    GLuint v0,
    GLuint v1,
    GLuint v2) {
  self->glUniform3ui(location, v0, v1, v2);
}

//  void QOpenGLFunctions_4_1_Compatibility::glUniform2ui(GLint location,
//      GLuint v0, GLuint v1)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility12glUniform2uiEijj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLint location,
    GLuint v0,
    GLuint v1) {
  self->glUniform2ui(location, v0, v1);
}

//  void QOpenGLFunctions_4_1_Compatibility::glUniform1ui(GLint location,
//      GLuint v0)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility12glUniform1uiEij(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLint location,
    GLuint v0) {
  self->glUniform1ui(location, v0);
}

//  void QOpenGLFunctions_4_1_Compatibility::glEndConditionalRender()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility22glEndConditionalRenderEv(
    QOpenGLFunctions_4_1_Compatibility *self) {
  self->glEndConditionalRender();
}

//  void QOpenGLFunctions_4_1_Compatibility::glBeginConditionalRender(GLuint
//      id, GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility24glBeginConditionalRenderEjj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint id,
    GLenum mode) {
  self->glBeginConditionalRender(id, mode);
}

//  void QOpenGLFunctions_4_1_Compatibility::glClampColor(GLenum target,
//      GLenum clamp)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility12glClampColorEjj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum target,
    GLenum clamp) {
  self->glClampColor(target, clamp);
}

//  void QOpenGLFunctions_4_1_Compatibility::glBindBufferBase(GLenum target,
//      GLuint index, GLuint buffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility16glBindBufferBaseEjjj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum target,
    GLuint index,
    GLuint buffer) {
  self->glBindBufferBase(target, index, buffer);
}

//  void QOpenGLFunctions_4_1_Compatibility::glEndTransformFeedback()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility22glEndTransformFeedbackEv(
    QOpenGLFunctions_4_1_Compatibility *self) {
  self->glEndTransformFeedback();
}

//  void QOpenGLFunctions_4_1_Compatibility::glBeginTransformFeedback(GLenum
//      primitiveMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility24glBeginTransformFeedbackEj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum primitiveMode) {
  self->glBeginTransformFeedback(primitiveMode);
}

//  void QOpenGLFunctions_4_1_Compatibility::glDisablei(GLenum target, GLuint
//      index)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility10glDisableiEjj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum target,
    GLuint index) {
  self->glDisablei(target, index);
}

//  void QOpenGLFunctions_4_1_Compatibility::glEnablei(GLenum target, GLuint
//      index)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility9glEnableiEjj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum target,
    GLuint index) {
  self->glEnablei(target, index);
}

//  void QOpenGLFunctions_4_1_Compatibility::glColorMaski(GLuint index,
//      GLboolean r, GLboolean g, GLboolean b, GLboolean a)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility12glColorMaskiEjhhhh(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint index,
    GLboolean r,
    GLboolean g,
    GLboolean b,
    GLboolean a) {
  self->glColorMaski(index, r, g, b, a);
}

//  void QOpenGLFunctions_4_1_Compatibility::glUniformBlockBinding(GLuint
//      program, GLuint uniformBlockIndex, GLuint uniformBlockBinding)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility21glUniformBlockBindingEjjj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint program,
    GLuint uniformBlockIndex,
    GLuint uniformBlockBinding) {
  self->glUniformBlockBinding(
      program,
      uniformBlockIndex,
      uniformBlockBinding);
}

//  void QOpenGLFunctions_4_1_Compatibility::glPrimitiveRestartIndex(GLuint
//      index)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility23glPrimitiveRestartIndexEj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint index) {
  self->glPrimitiveRestartIndex(index);
}

//  void QOpenGLFunctions_4_1_Compatibility::glTexBuffer(GLenum target,
//      GLenum internalformat, GLuint buffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility11glTexBufferEjjj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum target,
    GLenum internalformat,
    GLuint buffer) {
  self->glTexBuffer(target, internalformat, buffer);
}

//  void QOpenGLFunctions_4_1_Compatibility::glDrawArraysInstanced(GLenum
//      mode, GLint first, GLsizei count, GLsizei instancecount)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility21glDrawArraysInstancedEjiii(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum mode,
    GLint first,
    GLsizei count,
    GLsizei instancecount) {
  self->glDrawArraysInstanced(mode, first, count, instancecount);
}

//  void QOpenGLFunctions_4_1_Compatibility::glSampleMaski(GLuint index,
//      GLbitfield mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility13glSampleMaskiEjj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint index,
    GLbitfield mask) {
  self->glSampleMaski(index, mask);
}

//  void QOpenGLFunctions_4_1_Compatibility::glTexImage3DMultisample(GLenum
//      target, GLsizei samples, GLint internalformat, GLsizei width, GLsizei
//      height, GLsizei depth, GLboolean fixedsamplelocations)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility23glTexImage3DMultisampleEjiiiiih(
    QOpenGLFunctions_4_1_Compatibility *self,
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

//  void QOpenGLFunctions_4_1_Compatibility::glTexImage2DMultisample(GLenum
//      target, GLsizei samples, GLint internalformat, GLsizei width, GLsizei
//      height, GLboolean fixedsamplelocations)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility23glTexImage2DMultisampleEjiiiih(
    QOpenGLFunctions_4_1_Compatibility *self,
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

//  void QOpenGLFunctions_4_1_Compatibility::glProvokingVertex(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility17glProvokingVertexEj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum mode) {
  self->glProvokingVertex(mode);
}

//  void QOpenGLFunctions_4_1_Compatibility::glFramebufferTexture(GLenum
//      target, GLenum attachment, GLuint texture, GLint level)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility20glFramebufferTextureEjjji(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum target,
    GLenum attachment,
    GLuint texture,
    GLint level) {
  self->glFramebufferTexture(target, attachment, texture, level);
}

//  void QOpenGLFunctions_4_1_Compatibility::glVertexAttribP4ui(GLuint index,
//      GLenum type, GLboolean normalized, GLuint value)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility18glVertexAttribP4uiEjjhj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint index,
    GLenum type,
    GLboolean normalized,
    GLuint value) {
  self->glVertexAttribP4ui(index, type, normalized, value);
}

//  void QOpenGLFunctions_4_1_Compatibility::glVertexAttribP3ui(GLuint index,
//      GLenum type, GLboolean normalized, GLuint value)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility18glVertexAttribP3uiEjjhj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint index,
    GLenum type,
    GLboolean normalized,
    GLuint value) {
  self->glVertexAttribP3ui(index, type, normalized, value);
}

//  void QOpenGLFunctions_4_1_Compatibility::glVertexAttribP2ui(GLuint index,
//      GLenum type, GLboolean normalized, GLuint value)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility18glVertexAttribP2uiEjjhj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint index,
    GLenum type,
    GLboolean normalized,
    GLuint value) {
  self->glVertexAttribP2ui(index, type, normalized, value);
}

//  void QOpenGLFunctions_4_1_Compatibility::glVertexAttribP1ui(GLuint index,
//      GLenum type, GLboolean normalized, GLuint value)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility18glVertexAttribP1uiEjjhj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint index,
    GLenum type,
    GLboolean normalized,
    GLuint value) {
  self->glVertexAttribP1ui(index, type, normalized, value);
}

//  void QOpenGLFunctions_4_1_Compatibility::glSecondaryColorP3ui(GLenum
//      type, GLuint color)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility20glSecondaryColorP3uiEjj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum type,
    GLuint color) {
  self->glSecondaryColorP3ui(type, color);
}

//  void QOpenGLFunctions_4_1_Compatibility::glColorP4ui(GLenum type, GLuint
//      color)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility11glColorP4uiEjj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum type,
    GLuint color) {
  self->glColorP4ui(type, color);
}

//  void QOpenGLFunctions_4_1_Compatibility::glColorP3ui(GLenum type, GLuint
//      color)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility11glColorP3uiEjj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum type,
    GLuint color) {
  self->glColorP3ui(type, color);
}

//  void QOpenGLFunctions_4_1_Compatibility::glNormalP3ui(GLenum type, GLuint
//      coords)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility12glNormalP3uiEjj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum type,
    GLuint coords) {
  self->glNormalP3ui(type, coords);
}

//  void QOpenGLFunctions_4_1_Compatibility::glMultiTexCoordP4ui(GLenum
//      texture, GLenum type, GLuint coords)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility19glMultiTexCoordP4uiEjjj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum texture,
    GLenum type,
    GLuint coords) {
  self->glMultiTexCoordP4ui(texture, type, coords);
}

//  void QOpenGLFunctions_4_1_Compatibility::glMultiTexCoordP3ui(GLenum
//      texture, GLenum type, GLuint coords)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility19glMultiTexCoordP3uiEjjj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum texture,
    GLenum type,
    GLuint coords) {
  self->glMultiTexCoordP3ui(texture, type, coords);
}

//  void QOpenGLFunctions_4_1_Compatibility::glMultiTexCoordP2ui(GLenum
//      texture, GLenum type, GLuint coords)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility19glMultiTexCoordP2uiEjjj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum texture,
    GLenum type,
    GLuint coords) {
  self->glMultiTexCoordP2ui(texture, type, coords);
}

//  void QOpenGLFunctions_4_1_Compatibility::glMultiTexCoordP1ui(GLenum
//      texture, GLenum type, GLuint coords)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility19glMultiTexCoordP1uiEjjj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum texture,
    GLenum type,
    GLuint coords) {
  self->glMultiTexCoordP1ui(texture, type, coords);
}

//  void QOpenGLFunctions_4_1_Compatibility::glTexCoordP4ui(GLenum type,
//      GLuint coords)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility14glTexCoordP4uiEjj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum type,
    GLuint coords) {
  self->glTexCoordP4ui(type, coords);
}

//  void QOpenGLFunctions_4_1_Compatibility::glTexCoordP3ui(GLenum type,
//      GLuint coords)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility14glTexCoordP3uiEjj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum type,
    GLuint coords) {
  self->glTexCoordP3ui(type, coords);
}

//  void QOpenGLFunctions_4_1_Compatibility::glTexCoordP2ui(GLenum type,
//      GLuint coords)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility14glTexCoordP2uiEjj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum type,
    GLuint coords) {
  self->glTexCoordP2ui(type, coords);
}

//  void QOpenGLFunctions_4_1_Compatibility::glTexCoordP1ui(GLenum type,
//      GLuint coords)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility14glTexCoordP1uiEjj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum type,
    GLuint coords) {
  self->glTexCoordP1ui(type, coords);
}

//  void QOpenGLFunctions_4_1_Compatibility::glVertexP4ui(GLenum type, GLuint
//      value)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility12glVertexP4uiEjj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum type,
    GLuint value) {
  self->glVertexP4ui(type, value);
}

//  void QOpenGLFunctions_4_1_Compatibility::glVertexP3ui(GLenum type, GLuint
//      value)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility12glVertexP3uiEjj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum type,
    GLuint value) {
  self->glVertexP3ui(type, value);
}

//  void QOpenGLFunctions_4_1_Compatibility::glVertexP2ui(GLenum type, GLuint
//      value)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility12glVertexP2uiEjj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum type,
    GLuint value) {
  self->glVertexP2ui(type, value);
}

//  void QOpenGLFunctions_4_1_Compatibility::glQueryCounter(GLuint id, GLenum
//      target)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility14glQueryCounterEjj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint id,
    GLenum target) {
  self->glQueryCounter(id, target);
}

//  void QOpenGLFunctions_4_1_Compatibility::glSamplerParameterf(GLuint
//      sampler, GLenum pname, GLfloat param)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility19glSamplerParameterfEjjf(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint sampler,
    GLenum pname,
    GLfloat param) {
  self->glSamplerParameterf(sampler, pname, param);
}

//  void QOpenGLFunctions_4_1_Compatibility::glSamplerParameteri(GLuint
//      sampler, GLenum pname, GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility19glSamplerParameteriEjji(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint sampler,
    GLenum pname,
    GLint param) {
  self->glSamplerParameteri(sampler, pname, param);
}

//  void QOpenGLFunctions_4_1_Compatibility::glBindSampler(GLuint unit,
//      GLuint sampler)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility13glBindSamplerEjj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint unit,
    GLuint sampler) {
  self->glBindSampler(unit, sampler);
}

//  void QOpenGLFunctions_4_1_Compatibility::glVertexAttribDivisor(GLuint
//      index, GLuint divisor)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility21glVertexAttribDivisorEjj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint index,
    GLuint divisor) {
  self->glVertexAttribDivisor(index, divisor);
}

//  void QOpenGLFunctions_4_1_Compatibility::glEndQueryIndexed(GLenum target,
//      GLuint index)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility17glEndQueryIndexedEjj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum target,
    GLuint index) {
  self->glEndQueryIndexed(target, index);
}

//  void QOpenGLFunctions_4_1_Compatibility::glBeginQueryIndexed(GLenum
//      target, GLuint index, GLuint id)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility19glBeginQueryIndexedEjjj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum target,
    GLuint index,
    GLuint id) {
  self->glBeginQueryIndexed(target, index, id);
}

//  void
//      QOpenGLFunctions_4_1_Compatibility::glDrawTransformFeedbackStream(GLe
//      num mode, GLuint id, GLuint stream)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility29glDrawTransformFeedbackStreamEjjj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum mode,
    GLuint id,
    GLuint stream) {
  self->glDrawTransformFeedbackStream(mode, id, stream);
}

//  void QOpenGLFunctions_4_1_Compatibility::glDrawTransformFeedback(GLenum
//      mode, GLuint id)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility23glDrawTransformFeedbackEjj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum mode,
    GLuint id) {
  self->glDrawTransformFeedback(mode, id);
}

//  void QOpenGLFunctions_4_1_Compatibility::glResumeTransformFeedback()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility25glResumeTransformFeedbackEv(
    QOpenGLFunctions_4_1_Compatibility *self) {
  self->glResumeTransformFeedback();
}

//  void QOpenGLFunctions_4_1_Compatibility::glPauseTransformFeedback()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility24glPauseTransformFeedbackEv(
    QOpenGLFunctions_4_1_Compatibility *self) {
  self->glPauseTransformFeedback();
}

//  void QOpenGLFunctions_4_1_Compatibility::glBindTransformFeedback(GLenum
//      target, GLuint id)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility23glBindTransformFeedbackEjj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum target,
    GLuint id) {
  self->glBindTransformFeedback(target, id);
}

//  void QOpenGLFunctions_4_1_Compatibility::glPatchParameteri(GLenum pname,
//      GLint value)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility17glPatchParameteriEji(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum pname,
    GLint value) {
  self->glPatchParameteri(pname, value);
}

//  void QOpenGLFunctions_4_1_Compatibility::glUniform4d(GLint location,
//      GLdouble x, GLdouble y, GLdouble z, GLdouble w)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility11glUniform4dEidddd(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLint location,
    GLdouble x,
    GLdouble y,
    GLdouble z,
    GLdouble w) {
  self->glUniform4d(location, x, y, z, w);
}

//  void QOpenGLFunctions_4_1_Compatibility::glUniform3d(GLint location,
//      GLdouble x, GLdouble y, GLdouble z)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility11glUniform3dEiddd(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLint location,
    GLdouble x,
    GLdouble y,
    GLdouble z) {
  self->glUniform3d(location, x, y, z);
}

//  void QOpenGLFunctions_4_1_Compatibility::glUniform2d(GLint location,
//      GLdouble x, GLdouble y)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility11glUniform2dEidd(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLint location,
    GLdouble x,
    GLdouble y) {
  self->glUniform2d(location, x, y);
}

//  void QOpenGLFunctions_4_1_Compatibility::glUniform1d(GLint location,
//      GLdouble x)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility11glUniform1dEid(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLint location,
    GLdouble x) {
  self->glUniform1d(location, x);
}

//  void QOpenGLFunctions_4_1_Compatibility::glBlendFuncSeparatei(GLuint buf,
//      GLenum srcRGB, GLenum dstRGB, GLenum srcAlpha, GLenum dstAlpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility20glBlendFuncSeparateiEjjjjj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint buf,
    GLenum srcRGB,
    GLenum dstRGB,
    GLenum srcAlpha,
    GLenum dstAlpha) {
  self->glBlendFuncSeparatei(buf, srcRGB, dstRGB, srcAlpha, dstAlpha);
}

//  void QOpenGLFunctions_4_1_Compatibility::glBlendFunci(GLuint buf, GLenum
//      src, GLenum dst)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility12glBlendFunciEjjj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint buf,
    GLenum src,
    GLenum dst) {
  self->glBlendFunci(buf, src, dst);
}

//  void QOpenGLFunctions_4_1_Compatibility::glBlendEquationSeparatei(GLuint
//      buf, GLenum modeRGB, GLenum modeAlpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility24glBlendEquationSeparateiEjjj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint buf,
    GLenum modeRGB,
    GLenum modeAlpha) {
  self->glBlendEquationSeparatei(buf, modeRGB, modeAlpha);
}

//  void QOpenGLFunctions_4_1_Compatibility::glBlendEquationi(GLuint buf,
//      GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility16glBlendEquationiEjj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint buf,
    GLenum mode) {
  self->glBlendEquationi(buf, mode);
}

//  void QOpenGLFunctions_4_1_Compatibility::glMinSampleShading(GLfloat
//      value)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility18glMinSampleShadingEf(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLfloat value) {
  self->glMinSampleShading(value);
}

//  void QOpenGLFunctions_4_1_Compatibility::glDepthRangeIndexed(GLuint
//      index, GLdouble n, GLdouble f)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility19glDepthRangeIndexedEjdd(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint index,
    GLdouble n,
    GLdouble f) {
  self->glDepthRangeIndexed(index, n, f);
}

//  void QOpenGLFunctions_4_1_Compatibility::glScissorIndexed(GLuint index,
//      GLint left, GLint bottom, GLsizei width, GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility16glScissorIndexedEjiiii(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint index,
    GLint left,
    GLint bottom,
    GLsizei width,
    GLsizei height) {
  self->glScissorIndexed(index, left, bottom, width, height);
}

//  void QOpenGLFunctions_4_1_Compatibility::glViewportIndexedf(GLuint index,
//      GLfloat x, GLfloat y, GLfloat w, GLfloat h)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility18glViewportIndexedfEjffff(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint index,
    GLfloat x,
    GLfloat y,
    GLfloat w,
    GLfloat h) {
  self->glViewportIndexedf(index, x, y, w, h);
}

//  void QOpenGLFunctions_4_1_Compatibility::glVertexAttribL4d(GLuint index,
//      GLdouble x, GLdouble y, GLdouble z, GLdouble w)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility17glVertexAttribL4dEjdddd(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint index,
    GLdouble x,
    GLdouble y,
    GLdouble z,
    GLdouble w) {
  self->glVertexAttribL4d(index, x, y, z, w);
}

//  void QOpenGLFunctions_4_1_Compatibility::glVertexAttribL3d(GLuint index,
//      GLdouble x, GLdouble y, GLdouble z)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility17glVertexAttribL3dEjddd(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint index,
    GLdouble x,
    GLdouble y,
    GLdouble z) {
  self->glVertexAttribL3d(index, x, y, z);
}

//  void QOpenGLFunctions_4_1_Compatibility::glVertexAttribL2d(GLuint index,
//      GLdouble x, GLdouble y)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility17glVertexAttribL2dEjdd(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint index,
    GLdouble x,
    GLdouble y) {
  self->glVertexAttribL2d(index, x, y);
}

//  void QOpenGLFunctions_4_1_Compatibility::glVertexAttribL1d(GLuint index,
//      GLdouble x)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility17glVertexAttribL1dEjd(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint index,
    GLdouble x) {
  self->glVertexAttribL1d(index, x);
}

//  void QOpenGLFunctions_4_1_Compatibility::glValidateProgramPipeline(GLuint
//      pipeline)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility25glValidateProgramPipelineEj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint pipeline) {
  self->glValidateProgramPipeline(pipeline);
}

//  void QOpenGLFunctions_4_1_Compatibility::glProgramUniform4ui(GLuint
//      program, GLint location, GLuint v0, GLuint v1, GLuint v2, GLuint v3)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility19glProgramUniform4uiEjijjjj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint program,
    GLint location,
    GLuint v0,
    GLuint v1,
    GLuint v2,
    GLuint v3) {
  self->glProgramUniform4ui(program, location, v0, v1, v2, v3);
}

//  void QOpenGLFunctions_4_1_Compatibility::glProgramUniform4d(GLuint
//      program, GLint location, GLdouble v0, GLdouble v1, GLdouble v2,
//      GLdouble v3)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility18glProgramUniform4dEjidddd(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint program,
    GLint location,
    GLdouble v0,
    GLdouble v1,
    GLdouble v2,
    GLdouble v3) {
  self->glProgramUniform4d(program, location, v0, v1, v2, v3);
}

//  void QOpenGLFunctions_4_1_Compatibility::glProgramUniform4f(GLuint
//      program, GLint location, GLfloat v0, GLfloat v1, GLfloat v2, GLfloat
//      v3)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility18glProgramUniform4fEjiffff(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint program,
    GLint location,
    GLfloat v0,
    GLfloat v1,
    GLfloat v2,
    GLfloat v3) {
  self->glProgramUniform4f(program, location, v0, v1, v2, v3);
}

//  void QOpenGLFunctions_4_1_Compatibility::glProgramUniform4i(GLuint
//      program, GLint location, GLint v0, GLint v1, GLint v2, GLint v3)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility18glProgramUniform4iEjiiiii(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint program,
    GLint location,
    GLint v0,
    GLint v1,
    GLint v2,
    GLint v3) {
  self->glProgramUniform4i(program, location, v0, v1, v2, v3);
}

//  void QOpenGLFunctions_4_1_Compatibility::glProgramUniform3ui(GLuint
//      program, GLint location, GLuint v0, GLuint v1, GLuint v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility19glProgramUniform3uiEjijjj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint program,
    GLint location,
    GLuint v0,
    GLuint v1,
    GLuint v2) {
  self->glProgramUniform3ui(program, location, v0, v1, v2);
}

//  void QOpenGLFunctions_4_1_Compatibility::glProgramUniform3d(GLuint
//      program, GLint location, GLdouble v0, GLdouble v1, GLdouble v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility18glProgramUniform3dEjiddd(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint program,
    GLint location,
    GLdouble v0,
    GLdouble v1,
    GLdouble v2) {
  self->glProgramUniform3d(program, location, v0, v1, v2);
}

//  void QOpenGLFunctions_4_1_Compatibility::glProgramUniform3f(GLuint
//      program, GLint location, GLfloat v0, GLfloat v1, GLfloat v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility18glProgramUniform3fEjifff(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint program,
    GLint location,
    GLfloat v0,
    GLfloat v1,
    GLfloat v2) {
  self->glProgramUniform3f(program, location, v0, v1, v2);
}

//  void QOpenGLFunctions_4_1_Compatibility::glProgramUniform3i(GLuint
//      program, GLint location, GLint v0, GLint v1, GLint v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility18glProgramUniform3iEjiiii(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint program,
    GLint location,
    GLint v0,
    GLint v1,
    GLint v2) {
  self->glProgramUniform3i(program, location, v0, v1, v2);
}

//  void QOpenGLFunctions_4_1_Compatibility::glProgramUniform2ui(GLuint
//      program, GLint location, GLuint v0, GLuint v1)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility19glProgramUniform2uiEjijj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint program,
    GLint location,
    GLuint v0,
    GLuint v1) {
  self->glProgramUniform2ui(program, location, v0, v1);
}

//  void QOpenGLFunctions_4_1_Compatibility::glProgramUniform2d(GLuint
//      program, GLint location, GLdouble v0, GLdouble v1)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility18glProgramUniform2dEjidd(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint program,
    GLint location,
    GLdouble v0,
    GLdouble v1) {
  self->glProgramUniform2d(program, location, v0, v1);
}

//  void QOpenGLFunctions_4_1_Compatibility::glProgramUniform2f(GLuint
//      program, GLint location, GLfloat v0, GLfloat v1)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility18glProgramUniform2fEjiff(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint program,
    GLint location,
    GLfloat v0,
    GLfloat v1) {
  self->glProgramUniform2f(program, location, v0, v1);
}

//  void QOpenGLFunctions_4_1_Compatibility::glProgramUniform2i(GLuint
//      program, GLint location, GLint v0, GLint v1)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility18glProgramUniform2iEjiii(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint program,
    GLint location,
    GLint v0,
    GLint v1) {
  self->glProgramUniform2i(program, location, v0, v1);
}

//  void QOpenGLFunctions_4_1_Compatibility::glProgramUniform1ui(GLuint
//      program, GLint location, GLuint v0)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility19glProgramUniform1uiEjij(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint program,
    GLint location,
    GLuint v0) {
  self->glProgramUniform1ui(program, location, v0);
}

//  void QOpenGLFunctions_4_1_Compatibility::glProgramUniform1d(GLuint
//      program, GLint location, GLdouble v0)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility18glProgramUniform1dEjid(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint program,
    GLint location,
    GLdouble v0) {
  self->glProgramUniform1d(program, location, v0);
}

//  void QOpenGLFunctions_4_1_Compatibility::glProgramUniform1f(GLuint
//      program, GLint location, GLfloat v0)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility18glProgramUniform1fEjif(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint program,
    GLint location,
    GLfloat v0) {
  self->glProgramUniform1f(program, location, v0);
}

//  void QOpenGLFunctions_4_1_Compatibility::glProgramUniform1i(GLuint
//      program, GLint location, GLint v0)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility18glProgramUniform1iEjii(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint program,
    GLint location,
    GLint v0) {
  self->glProgramUniform1i(program, location, v0);
}

//  void QOpenGLFunctions_4_1_Compatibility::glBindProgramPipeline(GLuint
//      pipeline)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility21glBindProgramPipelineEj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint pipeline) {
  self->glBindProgramPipeline(pipeline);
}

//  void QOpenGLFunctions_4_1_Compatibility::glActiveShaderProgram(GLuint
//      pipeline, GLuint program)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility21glActiveShaderProgramEjj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint pipeline,
    GLuint program) {
  self->glActiveShaderProgram(pipeline, program);
}

//  void QOpenGLFunctions_4_1_Compatibility::glUseProgramStages(GLuint
//      pipeline, GLbitfield stages, GLuint program)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility18glUseProgramStagesEjjj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint pipeline,
    GLbitfield stages,
    GLuint program) {
  self->glUseProgramStages(pipeline, stages, program);
}

//  void QOpenGLFunctions_4_1_Compatibility::glProgramParameteri(GLuint
//      program, GLenum pname, GLint value)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility19glProgramParameteriEjji(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint program,
    GLenum pname,
    GLint value) {
  self->glProgramParameteri(program, pname, value);
}

//  void QOpenGLFunctions_4_1_Compatibility::glClearDepthf(GLfloat dd)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility13glClearDepthfEf(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLfloat dd) {
  self->glClearDepthf(dd);
}

//  void QOpenGLFunctions_4_1_Compatibility::glDepthRangef(GLfloat n, GLfloat
//      f)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility13glDepthRangefEff(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLfloat n,
    GLfloat f) {
  self->glDepthRangef(n, f);
}

//  void QOpenGLFunctions_4_1_Compatibility::glReleaseShaderCompiler()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility23glReleaseShaderCompilerEv(
    QOpenGLFunctions_4_1_Compatibility *self) {
  self->glReleaseShaderCompiler();
}

//  void QOpenGLFunctions_4_1_Compatibility::glTranslatef(GLfloat x, GLfloat
//      y, GLfloat z)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility12glTranslatefEfff(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLfloat x,
    GLfloat y,
    GLfloat z) {
  self->glTranslatef(x, y, z);
}

//  void QOpenGLFunctions_4_1_Compatibility::glTranslated(GLdouble x,
//      GLdouble y, GLdouble z)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility12glTranslatedEddd(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLdouble x,
    GLdouble y,
    GLdouble z) {
  self->glTranslated(x, y, z);
}

//  void QOpenGLFunctions_4_1_Compatibility::glScalef(GLfloat x, GLfloat y,
//      GLfloat z)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility8glScalefEfff(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLfloat x,
    GLfloat y,
    GLfloat z) {
  self->glScalef(x, y, z);
}

//  void QOpenGLFunctions_4_1_Compatibility::glScaled(GLdouble x, GLdouble y,
//      GLdouble z)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility8glScaledEddd(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLdouble x,
    GLdouble y,
    GLdouble z) {
  self->glScaled(x, y, z);
}

//  void QOpenGLFunctions_4_1_Compatibility::glRotatef(GLfloat angle, GLfloat
//      x, GLfloat y, GLfloat z)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility9glRotatefEffff(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLfloat angle,
    GLfloat x,
    GLfloat y,
    GLfloat z) {
  self->glRotatef(angle, x, y, z);
}

//  void QOpenGLFunctions_4_1_Compatibility::glRotated(GLdouble angle,
//      GLdouble x, GLdouble y, GLdouble z)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility9glRotatedEdddd(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLdouble angle,
    GLdouble x,
    GLdouble y,
    GLdouble z) {
  self->glRotated(angle, x, y, z);
}

//  void QOpenGLFunctions_4_1_Compatibility::glPushMatrix()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility12glPushMatrixEv(
    QOpenGLFunctions_4_1_Compatibility *self) {
  self->glPushMatrix();
}

//  void QOpenGLFunctions_4_1_Compatibility::glPopMatrix()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility11glPopMatrixEv(
    QOpenGLFunctions_4_1_Compatibility *self) {
  self->glPopMatrix();
}

//  void QOpenGLFunctions_4_1_Compatibility::glOrtho(GLdouble left, GLdouble
//      right, GLdouble bottom, GLdouble top, GLdouble zNear, GLdouble zFar)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility7glOrthoEdddddd(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLdouble left,
    GLdouble right,
    GLdouble bottom,
    GLdouble top,
    GLdouble zNear,
    GLdouble zFar) {
  self->glOrtho(left, right, bottom, top, zNear, zFar);
}

//  void QOpenGLFunctions_4_1_Compatibility::glMatrixMode(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility12glMatrixModeEj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum mode) {
  self->glMatrixMode(mode);
}

//  void QOpenGLFunctions_4_1_Compatibility::glLoadIdentity()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility14glLoadIdentityEv(
    QOpenGLFunctions_4_1_Compatibility *self) {
  self->glLoadIdentity();
}

//  void QOpenGLFunctions_4_1_Compatibility::glFrustum(GLdouble left,
//      GLdouble right, GLdouble bottom, GLdouble top, GLdouble zNear,
//      GLdouble zFar)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility9glFrustumEdddddd(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLdouble left,
    GLdouble right,
    GLdouble bottom,
    GLdouble top,
    GLdouble zNear,
    GLdouble zFar) {
  self->glFrustum(left, right, bottom, top, zNear, zFar);
}

//  void QOpenGLFunctions_4_1_Compatibility::glCopyPixels(GLint x, GLint y,
//      GLsizei width, GLsizei height, GLenum type)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility12glCopyPixelsEiiiij(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLint x,
    GLint y,
    GLsizei width,
    GLsizei height,
    GLenum type) {
  self->glCopyPixels(x, y, width, height, type);
}

//  void QOpenGLFunctions_4_1_Compatibility::glPixelTransferi(GLenum pname,
//      GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility16glPixelTransferiEji(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum pname,
    GLint param) {
  self->glPixelTransferi(pname, param);
}

//  void QOpenGLFunctions_4_1_Compatibility::glPixelTransferf(GLenum pname,
//      GLfloat param)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility16glPixelTransferfEjf(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum pname,
    GLfloat param) {
  self->glPixelTransferf(pname, param);
}

//  void QOpenGLFunctions_4_1_Compatibility::glPixelZoom(GLfloat xfactor,
//      GLfloat yfactor)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility11glPixelZoomEff(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLfloat xfactor,
    GLfloat yfactor) {
  self->glPixelZoom(xfactor, yfactor);
}

//  void QOpenGLFunctions_4_1_Compatibility::glAlphaFunc(GLenum func, GLfloat
//      ref)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility11glAlphaFuncEjf(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum func,
    GLfloat ref) {
  self->glAlphaFunc(func, ref);
}

//  void QOpenGLFunctions_4_1_Compatibility::glEvalPoint2(GLint i, GLint j)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility12glEvalPoint2Eii(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLint i,
    GLint j) {
  self->glEvalPoint2(i, j);
}

//  void QOpenGLFunctions_4_1_Compatibility::glEvalMesh2(GLenum mode, GLint
//      i1, GLint i2, GLint j1, GLint j2)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility11glEvalMesh2Ejiiii(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum mode,
    GLint i1,
    GLint i2,
    GLint j1,
    GLint j2) {
  self->glEvalMesh2(mode, i1, i2, j1, j2);
}

//  void QOpenGLFunctions_4_1_Compatibility::glEvalPoint1(GLint i)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility12glEvalPoint1Ei(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLint i) {
  self->glEvalPoint1(i);
}

//  void QOpenGLFunctions_4_1_Compatibility::glEvalMesh1(GLenum mode, GLint
//      i1, GLint i2)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility11glEvalMesh1Ejii(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum mode,
    GLint i1,
    GLint i2) {
  self->glEvalMesh1(mode, i1, i2);
}

//  void QOpenGLFunctions_4_1_Compatibility::glEvalCoord2f(GLfloat u, GLfloat
//      v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility13glEvalCoord2fEff(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLfloat u,
    GLfloat v) {
  self->glEvalCoord2f(u, v);
}

//  void QOpenGLFunctions_4_1_Compatibility::glEvalCoord2d(GLdouble u,
//      GLdouble v)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility13glEvalCoord2dEdd(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLdouble u,
    GLdouble v) {
  self->glEvalCoord2d(u, v);
}

//  void QOpenGLFunctions_4_1_Compatibility::glEvalCoord1f(GLfloat u)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility13glEvalCoord1fEf(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLfloat u) {
  self->glEvalCoord1f(u);
}

//  void QOpenGLFunctions_4_1_Compatibility::glEvalCoord1d(GLdouble u)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility13glEvalCoord1dEd(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLdouble u) {
  self->glEvalCoord1d(u);
}

//  void QOpenGLFunctions_4_1_Compatibility::glMapGrid2f(GLint un, GLfloat
//      u1, GLfloat u2, GLint vn, GLfloat v1, GLfloat v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility11glMapGrid2fEiffiff(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLint un,
    GLfloat u1,
    GLfloat u2,
    GLint vn,
    GLfloat v1,
    GLfloat v2) {
  self->glMapGrid2f(un, u1, u2, vn, v1, v2);
}

//  void QOpenGLFunctions_4_1_Compatibility::glMapGrid2d(GLint un, GLdouble
//      u1, GLdouble u2, GLint vn, GLdouble v1, GLdouble v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility11glMapGrid2dEiddidd(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLint un,
    GLdouble u1,
    GLdouble u2,
    GLint vn,
    GLdouble v1,
    GLdouble v2) {
  self->glMapGrid2d(un, u1, u2, vn, v1, v2);
}

//  void QOpenGLFunctions_4_1_Compatibility::glMapGrid1f(GLint un, GLfloat
//      u1, GLfloat u2)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility11glMapGrid1fEiff(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLint un,
    GLfloat u1,
    GLfloat u2) {
  self->glMapGrid1f(un, u1, u2);
}

//  void QOpenGLFunctions_4_1_Compatibility::glMapGrid1d(GLint un, GLdouble
//      u1, GLdouble u2)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility11glMapGrid1dEidd(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLint un,
    GLdouble u1,
    GLdouble u2) {
  self->glMapGrid1d(un, u1, u2);
}

//  void QOpenGLFunctions_4_1_Compatibility::glPushAttrib(GLbitfield mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility12glPushAttribEj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLbitfield mask) {
  self->glPushAttrib(mask);
}

//  void QOpenGLFunctions_4_1_Compatibility::glPopAttrib()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility11glPopAttribEv(
    QOpenGLFunctions_4_1_Compatibility *self) {
  self->glPopAttrib();
}

//  void QOpenGLFunctions_4_1_Compatibility::glAccum(GLenum op, GLfloat
//      value)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility7glAccumEjf(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum op,
    GLfloat value) {
  self->glAccum(op, value);
}

//  void QOpenGLFunctions_4_1_Compatibility::glIndexMask(GLuint mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility11glIndexMaskEj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint mask) {
  self->glIndexMask(mask);
}

//  void QOpenGLFunctions_4_1_Compatibility::glClearIndex(GLfloat c)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility12glClearIndexEf(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLfloat c) {
  self->glClearIndex(c);
}

//  void QOpenGLFunctions_4_1_Compatibility::glClearAccum(GLfloat red,
//      GLfloat green, GLfloat blue, GLfloat alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility12glClearAccumEffff(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLfloat red,
    GLfloat green,
    GLfloat blue,
    GLfloat alpha) {
  self->glClearAccum(red, green, blue, alpha);
}

//  void QOpenGLFunctions_4_1_Compatibility::glPushName(GLuint name)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility10glPushNameEj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint name) {
  self->glPushName(name);
}

//  void QOpenGLFunctions_4_1_Compatibility::glPopName()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility9glPopNameEv(
    QOpenGLFunctions_4_1_Compatibility *self) {
  self->glPopName();
}

//  void QOpenGLFunctions_4_1_Compatibility::glPassThrough(GLfloat token)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility13glPassThroughEf(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLfloat token) {
  self->glPassThrough(token);
}

//  void QOpenGLFunctions_4_1_Compatibility::glLoadName(GLuint name)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility10glLoadNameEj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint name) {
  self->glLoadName(name);
}

//  void QOpenGLFunctions_4_1_Compatibility::glInitNames()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility11glInitNamesEv(
    QOpenGLFunctions_4_1_Compatibility *self) {
  self->glInitNames();
}

//  void QOpenGLFunctions_4_1_Compatibility::glTexGeni(GLenum coord, GLenum
//      pname, GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility9glTexGeniEjji(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum coord,
    GLenum pname,
    GLint param) {
  self->glTexGeni(coord, pname, param);
}

//  void QOpenGLFunctions_4_1_Compatibility::glTexGenf(GLenum coord, GLenum
//      pname, GLfloat param)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility9glTexGenfEjjf(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum coord,
    GLenum pname,
    GLfloat param) {
  self->glTexGenf(coord, pname, param);
}

//  void QOpenGLFunctions_4_1_Compatibility::glTexGend(GLenum coord, GLenum
//      pname, GLdouble param)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility9glTexGendEjjd(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum coord,
    GLenum pname,
    GLdouble param) {
  self->glTexGend(coord, pname, param);
}

//  void QOpenGLFunctions_4_1_Compatibility::glTexEnvi(GLenum target, GLenum
//      pname, GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility9glTexEnviEjji(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum target,
    GLenum pname,
    GLint param) {
  self->glTexEnvi(target, pname, param);
}

//  void QOpenGLFunctions_4_1_Compatibility::glTexEnvf(GLenum target, GLenum
//      pname, GLfloat param)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility9glTexEnvfEjjf(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum target,
    GLenum pname,
    GLfloat param) {
  self->glTexEnvf(target, pname, param);
}

//  void QOpenGLFunctions_4_1_Compatibility::glShadeModel(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility12glShadeModelEj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum mode) {
  self->glShadeModel(mode);
}

//  void QOpenGLFunctions_4_1_Compatibility::glMateriali(GLenum face, GLenum
//      pname, GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility11glMaterialiEjji(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum face,
    GLenum pname,
    GLint param) {
  self->glMateriali(face, pname, param);
}

//  void QOpenGLFunctions_4_1_Compatibility::glMaterialf(GLenum face, GLenum
//      pname, GLfloat param)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility11glMaterialfEjjf(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum face,
    GLenum pname,
    GLfloat param) {
  self->glMaterialf(face, pname, param);
}

//  void QOpenGLFunctions_4_1_Compatibility::glLineStipple(GLint factor,
//      GLushort pattern)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility13glLineStippleEit(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLint factor,
    GLushort pattern) {
  self->glLineStipple(factor, pattern);
}

//  void QOpenGLFunctions_4_1_Compatibility::glLightModeli(GLenum pname,
//      GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility13glLightModeliEji(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum pname,
    GLint param) {
  self->glLightModeli(pname, param);
}

//  void QOpenGLFunctions_4_1_Compatibility::glLightModelf(GLenum pname,
//      GLfloat param)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility13glLightModelfEjf(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum pname,
    GLfloat param) {
  self->glLightModelf(pname, param);
}

//  void QOpenGLFunctions_4_1_Compatibility::glLighti(GLenum light, GLenum
//      pname, GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility8glLightiEjji(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum light,
    GLenum pname,
    GLint param) {
  self->glLighti(light, pname, param);
}

//  void QOpenGLFunctions_4_1_Compatibility::glLightf(GLenum light, GLenum
//      pname, GLfloat param)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility8glLightfEjjf(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum light,
    GLenum pname,
    GLfloat param) {
  self->glLightf(light, pname, param);
}

//  void QOpenGLFunctions_4_1_Compatibility::glFogi(GLenum pname, GLint
//      param)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility6glFogiEji(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum pname,
    GLint param) {
  self->glFogi(pname, param);
}

//  void QOpenGLFunctions_4_1_Compatibility::glFogf(GLenum pname, GLfloat
//      param)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility6glFogfEjf(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum pname,
    GLfloat param) {
  self->glFogf(pname, param);
}

//  void QOpenGLFunctions_4_1_Compatibility::glColorMaterial(GLenum face,
//      GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility15glColorMaterialEjj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum face,
    GLenum mode) {
  self->glColorMaterial(face, mode);
}

//  void QOpenGLFunctions_4_1_Compatibility::glVertex4s(GLshort x, GLshort y,
//      GLshort z, GLshort w)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility10glVertex4sEssss(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLshort x,
    GLshort y,
    GLshort z,
    GLshort w) {
  self->glVertex4s(x, y, z, w);
}

//  void QOpenGLFunctions_4_1_Compatibility::glVertex4i(GLint x, GLint y,
//      GLint z, GLint w)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility10glVertex4iEiiii(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLint x,
    GLint y,
    GLint z,
    GLint w) {
  self->glVertex4i(x, y, z, w);
}

//  void QOpenGLFunctions_4_1_Compatibility::glVertex4f(GLfloat x, GLfloat y,
//      GLfloat z, GLfloat w)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility10glVertex4fEffff(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLfloat x,
    GLfloat y,
    GLfloat z,
    GLfloat w) {
  self->glVertex4f(x, y, z, w);
}

//  void QOpenGLFunctions_4_1_Compatibility::glVertex4d(GLdouble x, GLdouble
//      y, GLdouble z, GLdouble w)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility10glVertex4dEdddd(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLdouble x,
    GLdouble y,
    GLdouble z,
    GLdouble w) {
  self->glVertex4d(x, y, z, w);
}

//  void QOpenGLFunctions_4_1_Compatibility::glVertex3s(GLshort x, GLshort y,
//      GLshort z)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility10glVertex3sEsss(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLshort x,
    GLshort y,
    GLshort z) {
  self->glVertex3s(x, y, z);
}

//  void QOpenGLFunctions_4_1_Compatibility::glVertex3i(GLint x, GLint y,
//      GLint z)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility10glVertex3iEiii(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLint x,
    GLint y,
    GLint z) {
  self->glVertex3i(x, y, z);
}

//  void QOpenGLFunctions_4_1_Compatibility::glVertex3f(GLfloat x, GLfloat y,
//      GLfloat z)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility10glVertex3fEfff(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLfloat x,
    GLfloat y,
    GLfloat z) {
  self->glVertex3f(x, y, z);
}

//  void QOpenGLFunctions_4_1_Compatibility::glVertex3d(GLdouble x, GLdouble
//      y, GLdouble z)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility10glVertex3dEddd(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLdouble x,
    GLdouble y,
    GLdouble z) {
  self->glVertex3d(x, y, z);
}

//  void QOpenGLFunctions_4_1_Compatibility::glVertex2s(GLshort x, GLshort y)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility10glVertex2sEss(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLshort x,
    GLshort y) {
  self->glVertex2s(x, y);
}

//  void QOpenGLFunctions_4_1_Compatibility::glVertex2i(GLint x, GLint y)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility10glVertex2iEii(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLint x,
    GLint y) {
  self->glVertex2i(x, y);
}

//  void QOpenGLFunctions_4_1_Compatibility::glVertex2f(GLfloat x, GLfloat y)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility10glVertex2fEff(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLfloat x,
    GLfloat y) {
  self->glVertex2f(x, y);
}

//  void QOpenGLFunctions_4_1_Compatibility::glVertex2d(GLdouble x, GLdouble
//      y)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility10glVertex2dEdd(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLdouble x,
    GLdouble y) {
  self->glVertex2d(x, y);
}

//  void QOpenGLFunctions_4_1_Compatibility::glTexCoord4s(GLshort s, GLshort
//      t, GLshort r, GLshort q)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility12glTexCoord4sEssss(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLshort s,
    GLshort t,
    GLshort r,
    GLshort q) {
  self->glTexCoord4s(s, t, r, q);
}

//  void QOpenGLFunctions_4_1_Compatibility::glTexCoord4i(GLint s, GLint t,
//      GLint r, GLint q)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility12glTexCoord4iEiiii(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLint s,
    GLint t,
    GLint r,
    GLint q) {
  self->glTexCoord4i(s, t, r, q);
}

//  void QOpenGLFunctions_4_1_Compatibility::glTexCoord4f(GLfloat s, GLfloat
//      t, GLfloat r, GLfloat q)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility12glTexCoord4fEffff(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLfloat s,
    GLfloat t,
    GLfloat r,
    GLfloat q) {
  self->glTexCoord4f(s, t, r, q);
}

//  void QOpenGLFunctions_4_1_Compatibility::glTexCoord4d(GLdouble s,
//      GLdouble t, GLdouble r, GLdouble q)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility12glTexCoord4dEdddd(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLdouble s,
    GLdouble t,
    GLdouble r,
    GLdouble q) {
  self->glTexCoord4d(s, t, r, q);
}

//  void QOpenGLFunctions_4_1_Compatibility::glTexCoord3s(GLshort s, GLshort
//      t, GLshort r)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility12glTexCoord3sEsss(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLshort s,
    GLshort t,
    GLshort r) {
  self->glTexCoord3s(s, t, r);
}

//  void QOpenGLFunctions_4_1_Compatibility::glTexCoord3i(GLint s, GLint t,
//      GLint r)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility12glTexCoord3iEiii(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLint s,
    GLint t,
    GLint r) {
  self->glTexCoord3i(s, t, r);
}

//  void QOpenGLFunctions_4_1_Compatibility::glTexCoord3f(GLfloat s, GLfloat
//      t, GLfloat r)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility12glTexCoord3fEfff(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLfloat s,
    GLfloat t,
    GLfloat r) {
  self->glTexCoord3f(s, t, r);
}

//  void QOpenGLFunctions_4_1_Compatibility::glTexCoord3d(GLdouble s,
//      GLdouble t, GLdouble r)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility12glTexCoord3dEddd(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLdouble s,
    GLdouble t,
    GLdouble r) {
  self->glTexCoord3d(s, t, r);
}

//  void QOpenGLFunctions_4_1_Compatibility::glTexCoord2s(GLshort s, GLshort
//      t)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility12glTexCoord2sEss(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLshort s,
    GLshort t) {
  self->glTexCoord2s(s, t);
}

//  void QOpenGLFunctions_4_1_Compatibility::glTexCoord2i(GLint s, GLint t)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility12glTexCoord2iEii(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLint s,
    GLint t) {
  self->glTexCoord2i(s, t);
}

//  void QOpenGLFunctions_4_1_Compatibility::glTexCoord2f(GLfloat s, GLfloat
//      t)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility12glTexCoord2fEff(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLfloat s,
    GLfloat t) {
  self->glTexCoord2f(s, t);
}

//  void QOpenGLFunctions_4_1_Compatibility::glTexCoord2d(GLdouble s,
//      GLdouble t)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility12glTexCoord2dEdd(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLdouble s,
    GLdouble t) {
  self->glTexCoord2d(s, t);
}

//  void QOpenGLFunctions_4_1_Compatibility::glTexCoord1s(GLshort s)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility12glTexCoord1sEs(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLshort s) {
  self->glTexCoord1s(s);
}

//  void QOpenGLFunctions_4_1_Compatibility::glTexCoord1i(GLint s)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility12glTexCoord1iEi(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLint s) {
  self->glTexCoord1i(s);
}

//  void QOpenGLFunctions_4_1_Compatibility::glTexCoord1f(GLfloat s)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility12glTexCoord1fEf(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLfloat s) {
  self->glTexCoord1f(s);
}

//  void QOpenGLFunctions_4_1_Compatibility::glTexCoord1d(GLdouble s)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility12glTexCoord1dEd(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLdouble s) {
  self->glTexCoord1d(s);
}

//  void QOpenGLFunctions_4_1_Compatibility::glRects(GLshort x1, GLshort y1,
//      GLshort x2, GLshort y2)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility7glRectsEssss(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLshort x1,
    GLshort y1,
    GLshort x2,
    GLshort y2) {
  self->glRects(x1, y1, x2, y2);
}

//  void QOpenGLFunctions_4_1_Compatibility::glRecti(GLint x1, GLint y1,
//      GLint x2, GLint y2)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility7glRectiEiiii(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLint x1,
    GLint y1,
    GLint x2,
    GLint y2) {
  self->glRecti(x1, y1, x2, y2);
}

//  void QOpenGLFunctions_4_1_Compatibility::glRectf(GLfloat x1, GLfloat y1,
//      GLfloat x2, GLfloat y2)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility7glRectfEffff(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLfloat x1,
    GLfloat y1,
    GLfloat x2,
    GLfloat y2) {
  self->glRectf(x1, y1, x2, y2);
}

//  void QOpenGLFunctions_4_1_Compatibility::glRectd(GLdouble x1, GLdouble
//      y1, GLdouble x2, GLdouble y2)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility7glRectdEdddd(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLdouble x1,
    GLdouble y1,
    GLdouble x2,
    GLdouble y2) {
  self->glRectd(x1, y1, x2, y2);
}

//  void QOpenGLFunctions_4_1_Compatibility::glRasterPos4s(GLshort x, GLshort
//      y, GLshort z, GLshort w)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility13glRasterPos4sEssss(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLshort x,
    GLshort y,
    GLshort z,
    GLshort w) {
  self->glRasterPos4s(x, y, z, w);
}

//  void QOpenGLFunctions_4_1_Compatibility::glRasterPos4i(GLint x, GLint y,
//      GLint z, GLint w)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility13glRasterPos4iEiiii(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLint x,
    GLint y,
    GLint z,
    GLint w) {
  self->glRasterPos4i(x, y, z, w);
}

//  void QOpenGLFunctions_4_1_Compatibility::glRasterPos4f(GLfloat x, GLfloat
//      y, GLfloat z, GLfloat w)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility13glRasterPos4fEffff(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLfloat x,
    GLfloat y,
    GLfloat z,
    GLfloat w) {
  self->glRasterPos4f(x, y, z, w);
}

//  void QOpenGLFunctions_4_1_Compatibility::glRasterPos4d(GLdouble x,
//      GLdouble y, GLdouble z, GLdouble w)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility13glRasterPos4dEdddd(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLdouble x,
    GLdouble y,
    GLdouble z,
    GLdouble w) {
  self->glRasterPos4d(x, y, z, w);
}

//  void QOpenGLFunctions_4_1_Compatibility::glRasterPos3s(GLshort x, GLshort
//      y, GLshort z)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility13glRasterPos3sEsss(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLshort x,
    GLshort y,
    GLshort z) {
  self->glRasterPos3s(x, y, z);
}

//  void QOpenGLFunctions_4_1_Compatibility::glRasterPos3i(GLint x, GLint y,
//      GLint z)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility13glRasterPos3iEiii(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLint x,
    GLint y,
    GLint z) {
  self->glRasterPos3i(x, y, z);
}

//  void QOpenGLFunctions_4_1_Compatibility::glRasterPos3f(GLfloat x, GLfloat
//      y, GLfloat z)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility13glRasterPos3fEfff(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLfloat x,
    GLfloat y,
    GLfloat z) {
  self->glRasterPos3f(x, y, z);
}

//  void QOpenGLFunctions_4_1_Compatibility::glRasterPos3d(GLdouble x,
//      GLdouble y, GLdouble z)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility13glRasterPos3dEddd(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLdouble x,
    GLdouble y,
    GLdouble z) {
  self->glRasterPos3d(x, y, z);
}

//  void QOpenGLFunctions_4_1_Compatibility::glRasterPos2s(GLshort x, GLshort
//      y)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility13glRasterPos2sEss(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLshort x,
    GLshort y) {
  self->glRasterPos2s(x, y);
}

//  void QOpenGLFunctions_4_1_Compatibility::glRasterPos2i(GLint x, GLint y)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility13glRasterPos2iEii(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLint x,
    GLint y) {
  self->glRasterPos2i(x, y);
}

//  void QOpenGLFunctions_4_1_Compatibility::glRasterPos2f(GLfloat x, GLfloat
//      y)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility13glRasterPos2fEff(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLfloat x,
    GLfloat y) {
  self->glRasterPos2f(x, y);
}

//  void QOpenGLFunctions_4_1_Compatibility::glRasterPos2d(GLdouble x,
//      GLdouble y)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility13glRasterPos2dEdd(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLdouble x,
    GLdouble y) {
  self->glRasterPos2d(x, y);
}

//  void QOpenGLFunctions_4_1_Compatibility::glNormal3s(GLshort nx, GLshort
//      ny, GLshort nz)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility10glNormal3sEsss(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLshort nx,
    GLshort ny,
    GLshort nz) {
  self->glNormal3s(nx, ny, nz);
}

//  void QOpenGLFunctions_4_1_Compatibility::glNormal3i(GLint nx, GLint ny,
//      GLint nz)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility10glNormal3iEiii(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLint nx,
    GLint ny,
    GLint nz) {
  self->glNormal3i(nx, ny, nz);
}

//  void QOpenGLFunctions_4_1_Compatibility::glNormal3f(GLfloat nx, GLfloat
//      ny, GLfloat nz)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility10glNormal3fEfff(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLfloat nx,
    GLfloat ny,
    GLfloat nz) {
  self->glNormal3f(nx, ny, nz);
}

//  void QOpenGLFunctions_4_1_Compatibility::glNormal3d(GLdouble nx, GLdouble
//      ny, GLdouble nz)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility10glNormal3dEddd(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLdouble nx,
    GLdouble ny,
    GLdouble nz) {
  self->glNormal3d(nx, ny, nz);
}

//  void QOpenGLFunctions_4_1_Compatibility::glNormal3b(GLbyte nx, GLbyte ny,
//      GLbyte nz)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility10glNormal3bEaaa(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLbyte nx,
    GLbyte ny,
    GLbyte nz) {
  self->glNormal3b(nx, ny, nz);
}

//  void QOpenGLFunctions_4_1_Compatibility::glIndexs(GLshort c)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility8glIndexsEs(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLshort c) {
  self->glIndexs(c);
}

//  void QOpenGLFunctions_4_1_Compatibility::glIndexi(GLint c)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility8glIndexiEi(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLint c) {
  self->glIndexi(c);
}

//  void QOpenGLFunctions_4_1_Compatibility::glIndexf(GLfloat c)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility8glIndexfEf(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLfloat c) {
  self->glIndexf(c);
}

//  void QOpenGLFunctions_4_1_Compatibility::glIndexd(GLdouble c)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility8glIndexdEd(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLdouble c) {
  self->glIndexd(c);
}

//  void QOpenGLFunctions_4_1_Compatibility::glEnd()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility5glEndEv(
    QOpenGLFunctions_4_1_Compatibility *self) {
  self->glEnd();
}

//  void QOpenGLFunctions_4_1_Compatibility::glEdgeFlag(GLboolean flag)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility10glEdgeFlagEh(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLboolean flag) {
  self->glEdgeFlag(flag);
}

//  void QOpenGLFunctions_4_1_Compatibility::glColor4us(GLushort red,
//      GLushort green, GLushort blue, GLushort alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility10glColor4usEtttt(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLushort red,
    GLushort green,
    GLushort blue,
    GLushort alpha) {
  self->glColor4us(red, green, blue, alpha);
}

//  void QOpenGLFunctions_4_1_Compatibility::glColor4ui(GLuint red, GLuint
//      green, GLuint blue, GLuint alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility10glColor4uiEjjjj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint red,
    GLuint green,
    GLuint blue,
    GLuint alpha) {
  self->glColor4ui(red, green, blue, alpha);
}

//  void QOpenGLFunctions_4_1_Compatibility::glColor4ub(GLubyte red, GLubyte
//      green, GLubyte blue, GLubyte alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility10glColor4ubEhhhh(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLubyte red,
    GLubyte green,
    GLubyte blue,
    GLubyte alpha) {
  self->glColor4ub(red, green, blue, alpha);
}

//  void QOpenGLFunctions_4_1_Compatibility::glColor4s(GLshort red, GLshort
//      green, GLshort blue, GLshort alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility9glColor4sEssss(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLshort red,
    GLshort green,
    GLshort blue,
    GLshort alpha) {
  self->glColor4s(red, green, blue, alpha);
}

//  void QOpenGLFunctions_4_1_Compatibility::glColor4i(GLint red, GLint
//      green, GLint blue, GLint alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility9glColor4iEiiii(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLint red,
    GLint green,
    GLint blue,
    GLint alpha) {
  self->glColor4i(red, green, blue, alpha);
}

//  void QOpenGLFunctions_4_1_Compatibility::glColor4f(GLfloat red, GLfloat
//      green, GLfloat blue, GLfloat alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility9glColor4fEffff(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLfloat red,
    GLfloat green,
    GLfloat blue,
    GLfloat alpha) {
  self->glColor4f(red, green, blue, alpha);
}

//  void QOpenGLFunctions_4_1_Compatibility::glColor4d(GLdouble red, GLdouble
//      green, GLdouble blue, GLdouble alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility9glColor4dEdddd(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLdouble red,
    GLdouble green,
    GLdouble blue,
    GLdouble alpha) {
  self->glColor4d(red, green, blue, alpha);
}

//  void QOpenGLFunctions_4_1_Compatibility::glColor4b(GLbyte red, GLbyte
//      green, GLbyte blue, GLbyte alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility9glColor4bEaaaa(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLbyte red,
    GLbyte green,
    GLbyte blue,
    GLbyte alpha) {
  self->glColor4b(red, green, blue, alpha);
}

//  void QOpenGLFunctions_4_1_Compatibility::glColor3us(GLushort red,
//      GLushort green, GLushort blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility10glColor3usEttt(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLushort red,
    GLushort green,
    GLushort blue) {
  self->glColor3us(red, green, blue);
}

//  void QOpenGLFunctions_4_1_Compatibility::glColor3ui(GLuint red, GLuint
//      green, GLuint blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility10glColor3uiEjjj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint red,
    GLuint green,
    GLuint blue) {
  self->glColor3ui(red, green, blue);
}

//  void QOpenGLFunctions_4_1_Compatibility::glColor3ub(GLubyte red, GLubyte
//      green, GLubyte blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility10glColor3ubEhhh(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLubyte red,
    GLubyte green,
    GLubyte blue) {
  self->glColor3ub(red, green, blue);
}

//  void QOpenGLFunctions_4_1_Compatibility::glColor3s(GLshort red, GLshort
//      green, GLshort blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility9glColor3sEsss(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLshort red,
    GLshort green,
    GLshort blue) {
  self->glColor3s(red, green, blue);
}

//  void QOpenGLFunctions_4_1_Compatibility::glColor3i(GLint red, GLint
//      green, GLint blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility9glColor3iEiii(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLint red,
    GLint green,
    GLint blue) {
  self->glColor3i(red, green, blue);
}

//  void QOpenGLFunctions_4_1_Compatibility::glColor3f(GLfloat red, GLfloat
//      green, GLfloat blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility9glColor3fEfff(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLfloat red,
    GLfloat green,
    GLfloat blue) {
  self->glColor3f(red, green, blue);
}

//  void QOpenGLFunctions_4_1_Compatibility::glColor3d(GLdouble red, GLdouble
//      green, GLdouble blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility9glColor3dEddd(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLdouble red,
    GLdouble green,
    GLdouble blue) {
  self->glColor3d(red, green, blue);
}

//  void QOpenGLFunctions_4_1_Compatibility::glColor3b(GLbyte red, GLbyte
//      green, GLbyte blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility9glColor3bEaaa(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLbyte red,
    GLbyte green,
    GLbyte blue) {
  self->glColor3b(red, green, blue);
}

//  void QOpenGLFunctions_4_1_Compatibility::glBegin(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility7glBeginEj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum mode) {
  self->glBegin(mode);
}

//  void QOpenGLFunctions_4_1_Compatibility::glListBase(GLuint base)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility10glListBaseEj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint base) {
  self->glListBase(base);
}

//  void QOpenGLFunctions_4_1_Compatibility::glDeleteLists(GLuint list,
//      GLsizei range)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility13glDeleteListsEji(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint list,
    GLsizei range) {
  self->glDeleteLists(list, range);
}

//  void QOpenGLFunctions_4_1_Compatibility::glCallList(GLuint list)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility10glCallListEj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint list) {
  self->glCallList(list);
}

//  void QOpenGLFunctions_4_1_Compatibility::glEndList()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility9glEndListEv(
    QOpenGLFunctions_4_1_Compatibility *self) {
  self->glEndList();
}

//  void QOpenGLFunctions_4_1_Compatibility::glNewList(GLuint list, GLenum
//      mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility9glNewListEjj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint list,
    GLenum mode) {
  self->glNewList(list, mode);
}

//  void QOpenGLFunctions_4_1_Compatibility::glPushClientAttrib(GLbitfield
//      mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility18glPushClientAttribEj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLbitfield mask) {
  self->glPushClientAttrib(mask);
}

//  void QOpenGLFunctions_4_1_Compatibility::glPopClientAttrib()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility17glPopClientAttribEv(
    QOpenGLFunctions_4_1_Compatibility *self) {
  self->glPopClientAttrib();
}

//  void QOpenGLFunctions_4_1_Compatibility::glEnableClientState(GLenum
//      array)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility19glEnableClientStateEj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum array) {
  self->glEnableClientState(array);
}

//  void QOpenGLFunctions_4_1_Compatibility::glDisableClientState(GLenum
//      array)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility20glDisableClientStateEj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum array) {
  self->glDisableClientState(array);
}

//  void QOpenGLFunctions_4_1_Compatibility::glArrayElement(GLint i)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility14glArrayElementEi(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLint i) {
  self->glArrayElement(i);
}

//  void QOpenGLFunctions_4_1_Compatibility::glResetMinmax(GLenum target)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility13glResetMinmaxEj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum target) {
  self->glResetMinmax(target);
}

//  void QOpenGLFunctions_4_1_Compatibility::glResetHistogram(GLenum target)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility16glResetHistogramEj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum target) {
  self->glResetHistogram(target);
}

//  void QOpenGLFunctions_4_1_Compatibility::glMinmax(GLenum target, GLenum
//      internalformat, GLboolean sink)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility8glMinmaxEjjh(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum target,
    GLenum internalformat,
    GLboolean sink) {
  self->glMinmax(target, internalformat, sink);
}

//  void QOpenGLFunctions_4_1_Compatibility::glHistogram(GLenum target,
//      GLsizei width, GLenum internalformat, GLboolean sink)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility11glHistogramEjijh(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum target,
    GLsizei width,
    GLenum internalformat,
    GLboolean sink) {
  self->glHistogram(target, width, internalformat, sink);
}

//  void QOpenGLFunctions_4_1_Compatibility::glCopyConvolutionFilter2D(GLenum
//      target, GLenum internalformat, GLint x, GLint y, GLsizei width,
//      GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility25glCopyConvolutionFilter2DEjjiiii(
    QOpenGLFunctions_4_1_Compatibility *self,
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

//  void QOpenGLFunctions_4_1_Compatibility::glCopyConvolutionFilter1D(GLenum
//      target, GLenum internalformat, GLint x, GLint y, GLsizei width)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility25glCopyConvolutionFilter1DEjjiii(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum target,
    GLenum internalformat,
    GLint x,
    GLint y,
    GLsizei width) {
  self->glCopyConvolutionFilter1D(target, internalformat, x, y, width);
}

//  void QOpenGLFunctions_4_1_Compatibility::glConvolutionParameteri(GLenum
//      target, GLenum pname, GLint params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility23glConvolutionParameteriEjji(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum target,
    GLenum pname,
    GLint params) {
  self->glConvolutionParameteri(target, pname, params);
}

//  void QOpenGLFunctions_4_1_Compatibility::glConvolutionParameterf(GLenum
//      target, GLenum pname, GLfloat params)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility23glConvolutionParameterfEjjf(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum target,
    GLenum pname,
    GLfloat params) {
  self->glConvolutionParameterf(target, pname, params);
}

//  void QOpenGLFunctions_4_1_Compatibility::glCopyColorSubTable(GLenum
//      target, GLsizei start, GLint x, GLint y, GLsizei width)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility19glCopyColorSubTableEjiiii(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum target,
    GLsizei start,
    GLint x,
    GLint y,
    GLsizei width) {
  self->glCopyColorSubTable(target, start, x, y, width);
}

//  void QOpenGLFunctions_4_1_Compatibility::glCopyColorTable(GLenum target,
//      GLenum internalformat, GLint x, GLint y, GLsizei width)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility16glCopyColorTableEjjiii(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum target,
    GLenum internalformat,
    GLint x,
    GLint y,
    GLsizei width) {
  self->glCopyColorTable(target, internalformat, x, y, width);
}

//  void QOpenGLFunctions_4_1_Compatibility::glMultiTexCoord4s(GLenum target,
//      GLshort s, GLshort t, GLshort r, GLshort q)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility17glMultiTexCoord4sEjssss(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum target,
    GLshort s,
    GLshort t,
    GLshort r,
    GLshort q) {
  self->glMultiTexCoord4s(target, s, t, r, q);
}

//  void QOpenGLFunctions_4_1_Compatibility::glMultiTexCoord4i(GLenum target,
//      GLint s, GLint t, GLint r, GLint q)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility17glMultiTexCoord4iEjiiii(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum target,
    GLint s,
    GLint t,
    GLint r,
    GLint q) {
  self->glMultiTexCoord4i(target, s, t, r, q);
}

//  void QOpenGLFunctions_4_1_Compatibility::glMultiTexCoord4f(GLenum target,
//      GLfloat s, GLfloat t, GLfloat r, GLfloat q)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility17glMultiTexCoord4fEjffff(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum target,
    GLfloat s,
    GLfloat t,
    GLfloat r,
    GLfloat q) {
  self->glMultiTexCoord4f(target, s, t, r, q);
}

//  void QOpenGLFunctions_4_1_Compatibility::glMultiTexCoord4d(GLenum target,
//      GLdouble s, GLdouble t, GLdouble r, GLdouble q)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility17glMultiTexCoord4dEjdddd(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum target,
    GLdouble s,
    GLdouble t,
    GLdouble r,
    GLdouble q) {
  self->glMultiTexCoord4d(target, s, t, r, q);
}

//  void QOpenGLFunctions_4_1_Compatibility::glMultiTexCoord3s(GLenum target,
//      GLshort s, GLshort t, GLshort r)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility17glMultiTexCoord3sEjsss(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum target,
    GLshort s,
    GLshort t,
    GLshort r) {
  self->glMultiTexCoord3s(target, s, t, r);
}

//  void QOpenGLFunctions_4_1_Compatibility::glMultiTexCoord3i(GLenum target,
//      GLint s, GLint t, GLint r)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility17glMultiTexCoord3iEjiii(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum target,
    GLint s,
    GLint t,
    GLint r) {
  self->glMultiTexCoord3i(target, s, t, r);
}

//  void QOpenGLFunctions_4_1_Compatibility::glMultiTexCoord3f(GLenum target,
//      GLfloat s, GLfloat t, GLfloat r)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility17glMultiTexCoord3fEjfff(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum target,
    GLfloat s,
    GLfloat t,
    GLfloat r) {
  self->glMultiTexCoord3f(target, s, t, r);
}

//  void QOpenGLFunctions_4_1_Compatibility::glMultiTexCoord3d(GLenum target,
//      GLdouble s, GLdouble t, GLdouble r)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility17glMultiTexCoord3dEjddd(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum target,
    GLdouble s,
    GLdouble t,
    GLdouble r) {
  self->glMultiTexCoord3d(target, s, t, r);
}

//  void QOpenGLFunctions_4_1_Compatibility::glMultiTexCoord2s(GLenum target,
//      GLshort s, GLshort t)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility17glMultiTexCoord2sEjss(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum target,
    GLshort s,
    GLshort t) {
  self->glMultiTexCoord2s(target, s, t);
}

//  void QOpenGLFunctions_4_1_Compatibility::glMultiTexCoord2i(GLenum target,
//      GLint s, GLint t)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility17glMultiTexCoord2iEjii(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum target,
    GLint s,
    GLint t) {
  self->glMultiTexCoord2i(target, s, t);
}

//  void QOpenGLFunctions_4_1_Compatibility::glMultiTexCoord2f(GLenum target,
//      GLfloat s, GLfloat t)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility17glMultiTexCoord2fEjff(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum target,
    GLfloat s,
    GLfloat t) {
  self->glMultiTexCoord2f(target, s, t);
}

//  void QOpenGLFunctions_4_1_Compatibility::glMultiTexCoord2d(GLenum target,
//      GLdouble s, GLdouble t)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility17glMultiTexCoord2dEjdd(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum target,
    GLdouble s,
    GLdouble t) {
  self->glMultiTexCoord2d(target, s, t);
}

//  void QOpenGLFunctions_4_1_Compatibility::glMultiTexCoord1s(GLenum target,
//      GLshort s)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility17glMultiTexCoord1sEjs(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum target,
    GLshort s) {
  self->glMultiTexCoord1s(target, s);
}

//  void QOpenGLFunctions_4_1_Compatibility::glMultiTexCoord1i(GLenum target,
//      GLint s)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility17glMultiTexCoord1iEji(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum target,
    GLint s) {
  self->glMultiTexCoord1i(target, s);
}

//  void QOpenGLFunctions_4_1_Compatibility::glMultiTexCoord1f(GLenum target,
//      GLfloat s)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility17glMultiTexCoord1fEjf(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum target,
    GLfloat s) {
  self->glMultiTexCoord1f(target, s);
}

//  void QOpenGLFunctions_4_1_Compatibility::glMultiTexCoord1d(GLenum target,
//      GLdouble s)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility17glMultiTexCoord1dEjd(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum target,
    GLdouble s) {
  self->glMultiTexCoord1d(target, s);
}

//  void QOpenGLFunctions_4_1_Compatibility::glClientActiveTexture(GLenum
//      texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility21glClientActiveTextureEj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLenum texture) {
  self->glClientActiveTexture(texture);
}

//  void QOpenGLFunctions_4_1_Compatibility::glWindowPos3s(GLshort x, GLshort
//      y, GLshort z)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility13glWindowPos3sEsss(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLshort x,
    GLshort y,
    GLshort z) {
  self->glWindowPos3s(x, y, z);
}

//  void QOpenGLFunctions_4_1_Compatibility::glWindowPos3i(GLint x, GLint y,
//      GLint z)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility13glWindowPos3iEiii(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLint x,
    GLint y,
    GLint z) {
  self->glWindowPos3i(x, y, z);
}

//  void QOpenGLFunctions_4_1_Compatibility::glWindowPos3f(GLfloat x, GLfloat
//      y, GLfloat z)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility13glWindowPos3fEfff(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLfloat x,
    GLfloat y,
    GLfloat z) {
  self->glWindowPos3f(x, y, z);
}

//  void QOpenGLFunctions_4_1_Compatibility::glWindowPos3d(GLdouble x,
//      GLdouble y, GLdouble z)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility13glWindowPos3dEddd(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLdouble x,
    GLdouble y,
    GLdouble z) {
  self->glWindowPos3d(x, y, z);
}

//  void QOpenGLFunctions_4_1_Compatibility::glWindowPos2s(GLshort x, GLshort
//      y)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility13glWindowPos2sEss(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLshort x,
    GLshort y) {
  self->glWindowPos2s(x, y);
}

//  void QOpenGLFunctions_4_1_Compatibility::glWindowPos2i(GLint x, GLint y)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility13glWindowPos2iEii(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLint x,
    GLint y) {
  self->glWindowPos2i(x, y);
}

//  void QOpenGLFunctions_4_1_Compatibility::glWindowPos2f(GLfloat x, GLfloat
//      y)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility13glWindowPos2fEff(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLfloat x,
    GLfloat y) {
  self->glWindowPos2f(x, y);
}

//  void QOpenGLFunctions_4_1_Compatibility::glWindowPos2d(GLdouble x,
//      GLdouble y)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility13glWindowPos2dEdd(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLdouble x,
    GLdouble y) {
  self->glWindowPos2d(x, y);
}

//  void QOpenGLFunctions_4_1_Compatibility::glSecondaryColor3us(GLushort
//      red, GLushort green, GLushort blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility19glSecondaryColor3usEttt(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLushort red,
    GLushort green,
    GLushort blue) {
  self->glSecondaryColor3us(red, green, blue);
}

//  void QOpenGLFunctions_4_1_Compatibility::glSecondaryColor3ui(GLuint red,
//      GLuint green, GLuint blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility19glSecondaryColor3uiEjjj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint red,
    GLuint green,
    GLuint blue) {
  self->glSecondaryColor3ui(red, green, blue);
}

//  void QOpenGLFunctions_4_1_Compatibility::glSecondaryColor3ub(GLubyte red,
//      GLubyte green, GLubyte blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility19glSecondaryColor3ubEhhh(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLubyte red,
    GLubyte green,
    GLubyte blue) {
  self->glSecondaryColor3ub(red, green, blue);
}

//  void QOpenGLFunctions_4_1_Compatibility::glSecondaryColor3s(GLshort red,
//      GLshort green, GLshort blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility18glSecondaryColor3sEsss(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLshort red,
    GLshort green,
    GLshort blue) {
  self->glSecondaryColor3s(red, green, blue);
}

//  void QOpenGLFunctions_4_1_Compatibility::glSecondaryColor3i(GLint red,
//      GLint green, GLint blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility18glSecondaryColor3iEiii(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLint red,
    GLint green,
    GLint blue) {
  self->glSecondaryColor3i(red, green, blue);
}

//  void QOpenGLFunctions_4_1_Compatibility::glSecondaryColor3f(GLfloat red,
//      GLfloat green, GLfloat blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility18glSecondaryColor3fEfff(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLfloat red,
    GLfloat green,
    GLfloat blue) {
  self->glSecondaryColor3f(red, green, blue);
}

//  void QOpenGLFunctions_4_1_Compatibility::glSecondaryColor3d(GLdouble red,
//      GLdouble green, GLdouble blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility18glSecondaryColor3dEddd(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLdouble red,
    GLdouble green,
    GLdouble blue) {
  self->glSecondaryColor3d(red, green, blue);
}

//  void QOpenGLFunctions_4_1_Compatibility::glSecondaryColor3b(GLbyte red,
//      GLbyte green, GLbyte blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility18glSecondaryColor3bEaaa(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLbyte red,
    GLbyte green,
    GLbyte blue) {
  self->glSecondaryColor3b(red, green, blue);
}

//  void QOpenGLFunctions_4_1_Compatibility::glFogCoordd(GLdouble coord)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility11glFogCoorddEd(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLdouble coord) {
  self->glFogCoordd(coord);
}

//  void QOpenGLFunctions_4_1_Compatibility::glFogCoordf(GLfloat coord)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility11glFogCoordfEf(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLfloat coord) {
  self->glFogCoordf(coord);
}

//  void QOpenGLFunctions_4_1_Compatibility::glVertexAttrib4s(GLuint index,
//      GLshort x, GLshort y, GLshort z, GLshort w)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility16glVertexAttrib4sEjssss(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint index,
    GLshort x,
    GLshort y,
    GLshort z,
    GLshort w) {
  self->glVertexAttrib4s(index, x, y, z, w);
}

//  void QOpenGLFunctions_4_1_Compatibility::glVertexAttrib4f(GLuint index,
//      GLfloat x, GLfloat y, GLfloat z, GLfloat w)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility16glVertexAttrib4fEjffff(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint index,
    GLfloat x,
    GLfloat y,
    GLfloat z,
    GLfloat w) {
  self->glVertexAttrib4f(index, x, y, z, w);
}

//  void QOpenGLFunctions_4_1_Compatibility::glVertexAttrib4d(GLuint index,
//      GLdouble x, GLdouble y, GLdouble z, GLdouble w)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility16glVertexAttrib4dEjdddd(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint index,
    GLdouble x,
    GLdouble y,
    GLdouble z,
    GLdouble w) {
  self->glVertexAttrib4d(index, x, y, z, w);
}

//  void QOpenGLFunctions_4_1_Compatibility::glVertexAttrib4Nub(GLuint index,
//      GLubyte x, GLubyte y, GLubyte z, GLubyte w)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility18glVertexAttrib4NubEjhhhh(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint index,
    GLubyte x,
    GLubyte y,
    GLubyte z,
    GLubyte w) {
  self->glVertexAttrib4Nub(index, x, y, z, w);
}

//  void QOpenGLFunctions_4_1_Compatibility::glVertexAttrib3s(GLuint index,
//      GLshort x, GLshort y, GLshort z)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility16glVertexAttrib3sEjsss(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint index,
    GLshort x,
    GLshort y,
    GLshort z) {
  self->glVertexAttrib3s(index, x, y, z);
}

//  void QOpenGLFunctions_4_1_Compatibility::glVertexAttrib3f(GLuint index,
//      GLfloat x, GLfloat y, GLfloat z)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility16glVertexAttrib3fEjfff(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint index,
    GLfloat x,
    GLfloat y,
    GLfloat z) {
  self->glVertexAttrib3f(index, x, y, z);
}

//  void QOpenGLFunctions_4_1_Compatibility::glVertexAttrib3d(GLuint index,
//      GLdouble x, GLdouble y, GLdouble z)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility16glVertexAttrib3dEjddd(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint index,
    GLdouble x,
    GLdouble y,
    GLdouble z) {
  self->glVertexAttrib3d(index, x, y, z);
}

//  void QOpenGLFunctions_4_1_Compatibility::glVertexAttrib2s(GLuint index,
//      GLshort x, GLshort y)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility16glVertexAttrib2sEjss(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint index,
    GLshort x,
    GLshort y) {
  self->glVertexAttrib2s(index, x, y);
}

//  void QOpenGLFunctions_4_1_Compatibility::glVertexAttrib2f(GLuint index,
//      GLfloat x, GLfloat y)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility16glVertexAttrib2fEjff(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint index,
    GLfloat x,
    GLfloat y) {
  self->glVertexAttrib2f(index, x, y);
}

//  void QOpenGLFunctions_4_1_Compatibility::glVertexAttrib2d(GLuint index,
//      GLdouble x, GLdouble y)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility16glVertexAttrib2dEjdd(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint index,
    GLdouble x,
    GLdouble y) {
  self->glVertexAttrib2d(index, x, y);
}

//  void QOpenGLFunctions_4_1_Compatibility::glVertexAttrib1s(GLuint index,
//      GLshort x)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility16glVertexAttrib1sEjs(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint index,
    GLshort x) {
  self->glVertexAttrib1s(index, x);
}

//  void QOpenGLFunctions_4_1_Compatibility::glVertexAttrib1f(GLuint index,
//      GLfloat x)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility16glVertexAttrib1fEjf(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint index,
    GLfloat x) {
  self->glVertexAttrib1f(index, x);
}

//  void QOpenGLFunctions_4_1_Compatibility::glVertexAttrib1d(GLuint index,
//      GLdouble x)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility16glVertexAttrib1dEjd(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint index,
    GLdouble x) {
  self->glVertexAttrib1d(index, x);
}

//  void QOpenGLFunctions_4_1_Compatibility::glVertexAttribI4ui(GLuint index,
//      GLuint x, GLuint y, GLuint z, GLuint w)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility18glVertexAttribI4uiEjjjjj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint index,
    GLuint x,
    GLuint y,
    GLuint z,
    GLuint w) {
  self->glVertexAttribI4ui(index, x, y, z, w);
}

//  void QOpenGLFunctions_4_1_Compatibility::glVertexAttribI3ui(GLuint index,
//      GLuint x, GLuint y, GLuint z)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility18glVertexAttribI3uiEjjjj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint index,
    GLuint x,
    GLuint y,
    GLuint z) {
  self->glVertexAttribI3ui(index, x, y, z);
}

//  void QOpenGLFunctions_4_1_Compatibility::glVertexAttribI2ui(GLuint index,
//      GLuint x, GLuint y)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility18glVertexAttribI2uiEjjj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint index,
    GLuint x,
    GLuint y) {
  self->glVertexAttribI2ui(index, x, y);
}

//  void QOpenGLFunctions_4_1_Compatibility::glVertexAttribI1ui(GLuint index,
//      GLuint x)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility18glVertexAttribI1uiEjj(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint index,
    GLuint x) {
  self->glVertexAttribI1ui(index, x);
}

//  void QOpenGLFunctions_4_1_Compatibility::glVertexAttribI4i(GLuint index,
//      GLint x, GLint y, GLint z, GLint w)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility17glVertexAttribI4iEjiiii(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint index,
    GLint x,
    GLint y,
    GLint z,
    GLint w) {
  self->glVertexAttribI4i(index, x, y, z, w);
}

//  void QOpenGLFunctions_4_1_Compatibility::glVertexAttribI3i(GLuint index,
//      GLint x, GLint y, GLint z)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility17glVertexAttribI3iEjiii(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint index,
    GLint x,
    GLint y,
    GLint z) {
  self->glVertexAttribI3i(index, x, y, z);
}

//  void QOpenGLFunctions_4_1_Compatibility::glVertexAttribI2i(GLuint index,
//      GLint x, GLint y)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility17glVertexAttribI2iEjii(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint index,
    GLint x,
    GLint y) {
  self->glVertexAttribI2i(index, x, y);
}

//  void QOpenGLFunctions_4_1_Compatibility::glVertexAttribI1i(GLuint index,
//      GLint x)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QOpenGLFunctions_4_1_Compatibility17glVertexAttribI1iEji(
    QOpenGLFunctions_4_1_Compatibility *self,
    GLuint index,
    GLint x) {
  self->glVertexAttribI1i(index, x);
}

//  bool
//      QOpenGLFunctions_4_1_Compatibility::isContextCompatible(QOpenGLContex
//      t *context)
extern "C" Q_DECL_EXPORT
bool ritual_ZN34QOpenGLFunctions_4_1_Compatibility19isContextCompatibleEP14QOpenGLContext(
    QOpenGLContext *context) {
  return QOpenGLFunctions_4_1_Compatibility::isContextCompatible(context);
}

//  QOpenGLVersionProfile
//      QOpenGLFunctions_4_1_Compatibility::versionProfile()
extern "C" Q_DECL_EXPORT
QOpenGLVersionProfile *ritual_ZN34QOpenGLFunctions_4_1_Compatibility14versionProfileEv() {
  return new QOpenGLVersionProfile(
      QOpenGLFunctions_4_1_Compatibility::versionProfile());
}

//  a Python function taken by a CuteQOpenGLFunctions_4_1_Compatibility, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QOpenGLFunctions_4_1_Compatibility(
    QOpenGLFunctions_4_1_Compatibility *self,
    const char *key,
    void *call) {
  return static_cast<CuteQOpenGLFunctions_4_1_Compatibility *>(self)->take(key, call);
}

//  bool QOpenGLFunctions_4_1_Compatibility::initializeOpenGLFunctions()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN34QOpenGLFunctions_4_1_Compatibility25initializeOpenGLFunctionsEv(
    QOpenGLFunctions_4_1_Compatibility *self) {
  return self->QOpenGLFunctions_4_1_Compatibility::initializeOpenGLFunctions();
}

#endif  // !defined(QT_NO_OPENGL) && !QT_CONFIG(opengles2)
