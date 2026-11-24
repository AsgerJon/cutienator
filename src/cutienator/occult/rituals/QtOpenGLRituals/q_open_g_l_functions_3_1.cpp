//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/qopenglfunctions_3_1.h, Qt 6.12.0. Changes made here are lost.
#include <QtOpenGL/qtopenglglobal.h>
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

//  void QOpenGLFunctions_3_1::glBindTexture(GLenum target, GLuint texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_113glBindTextureEjj(
    QOpenGLFunctions_3_1 *self,
    GLenum target,
    GLuint texture) {
  self->glBindTexture(target, texture);
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

//  void QOpenGLFunctions_3_1::glPointParameteri(GLenum pname, GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_117glPointParameteriEji(
    QOpenGLFunctions_3_1 *self,
    GLenum pname,
    GLint param) {
  self->glPointParameteri(pname, param);
}

//  void QOpenGLFunctions_3_1::glPointParameterf(GLenum pname, GLfloat param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_117glPointParameterfEjf(
    QOpenGLFunctions_3_1 *self,
    GLenum pname,
    GLfloat param) {
  self->glPointParameterf(pname, param);
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

//  void QOpenGLFunctions_3_1::glBindBuffer(GLenum target, GLuint buffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_112glBindBufferEjj(
    QOpenGLFunctions_3_1 *self,
    GLenum target,
    GLuint buffer) {
  self->glBindBuffer(target, buffer);
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

//  void QOpenGLFunctions_3_1::glValidateProgram(GLuint program)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_117glValidateProgramEj(
    QOpenGLFunctions_3_1 *self,
    GLuint program) {
  self->glValidateProgram(program);
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

//  void QOpenGLFunctions_3_1::glLinkProgram(GLuint program)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_113glLinkProgramEj(
    QOpenGLFunctions_3_1 *self,
    GLuint program) {
  self->glLinkProgram(program);
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

//  void QOpenGLFunctions_3_1::glCompileShader(GLuint shader)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_115glCompileShaderEj(
    QOpenGLFunctions_3_1 *self,
    GLuint shader) {
  self->glCompileShader(shader);
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

//  void QOpenGLFunctions_3_1::glBlendEquationSeparate(GLenum modeRGB, GLenum
//      modeAlpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_123glBlendEquationSeparateEjj(
    QOpenGLFunctions_3_1 *self,
    GLenum modeRGB,
    GLenum modeAlpha) {
  self->glBlendEquationSeparate(modeRGB, modeAlpha);
}

//  void QOpenGLFunctions_3_1::glBindVertexArray(GLuint array)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_117glBindVertexArrayEj(
    QOpenGLFunctions_3_1 *self,
    GLuint array) {
  self->glBindVertexArray(array);
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

//  void QOpenGLFunctions_3_1::glBindFramebuffer(GLenum target, GLuint
//      framebuffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_117glBindFramebufferEjj(
    QOpenGLFunctions_3_1 *self,
    GLenum target,
    GLuint framebuffer) {
  self->glBindFramebuffer(target, framebuffer);
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

//  void QOpenGLFunctions_3_1::glBindRenderbuffer(GLenum target, GLuint
//      renderbuffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_3_118glBindRenderbufferEjj(
    QOpenGLFunctions_3_1 *self,
    GLenum target,
    GLuint renderbuffer) {
  self->glBindRenderbuffer(target, renderbuffer);
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
