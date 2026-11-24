//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/qopenglfunctions_2_1.h, Qt 6.12.0. Changes made here are lost.
#include <QtOpenGL/qtopenglglobal.h>
#if !defined(QT_NO_OPENGL) && !QT_CONFIG(opengles2)
#include <QtOpenGL/QtOpenGL>
#include <QtOpenGL/qopenglfunctions_2_1.h>
#include <QtOpenGL/qopenglversionprofile.h>
#include <cstring>

//  A QOpenGLFunctions_2_1 that Python can take functions over in. Every QOpenGLFunctions_2_1
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL) && !QT_CONFIG(opengles2)
typedef bool (*CuteQOpenGLFunctions_2_1Call0)(const void *, int *);
#endif  // !defined(QT_NO_OPENGL) && !QT_CONFIG(opengles2)
#endif  // !defined(QT_NO_OPENGL)
class CuteQOpenGLFunctions_2_1 : public QOpenGLFunctions_2_1 {
public:
  using QOpenGLFunctions_2_1::QOpenGLFunctions_2_1;
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
  //  bool QOpenGLFunctions_2_1::initializeOpenGLFunctions()
  bool initializeOpenGLFunctions() override {
    if (taken[0]) {
      int handled = 0;
      CuteQOpenGLFunctions_2_1Call0 call = reinterpret_cast<CuteQOpenGLFunctions_2_1Call0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QOpenGLFunctions_2_1::initializeOpenGLFunctions();
  }
#endif  // !defined(QT_NO_OPENGL) && !QT_CONFIG(opengles2)
#endif  // !defined(QT_NO_OPENGL)
};

//  QOpenGLFunctions_2_1::QOpenGLFunctions_2_1()
extern "C" Q_DECL_EXPORT
QOpenGLFunctions_2_1 *ritual_ZN20QOpenGLFunctions_2_1C1Ev() {
  return new CuteQOpenGLFunctions_2_1();
}

//  QOpenGLFunctions_2_1::~QOpenGLFunctions_2_1()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_1D1Ev(QOpenGLFunctions_2_1 *self) {
  delete self;
}

//  bool QOpenGLFunctions_2_1::initializeOpenGLFunctions()
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QOpenGLFunctions_2_125initializeOpenGLFunctionsEv(
    QOpenGLFunctions_2_1 *self) {
  return self->initializeOpenGLFunctions();
}

//  void QOpenGLFunctions_2_1::glViewport(GLint x, GLint y, GLsizei width,
//      GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_110glViewportEiiii(
    QOpenGLFunctions_2_1 *self,
    GLint x,
    GLint y,
    GLsizei width,
    GLsizei height) {
  self->glViewport(x, y, width, height);
}

//  void QOpenGLFunctions_2_1::glDepthRange(GLdouble nearVal, GLdouble
//      farVal)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_112glDepthRangeEdd(
    QOpenGLFunctions_2_1 *self,
    GLdouble nearVal,
    GLdouble farVal) {
  self->glDepthRange(nearVal, farVal);
}

//  void QOpenGLFunctions_2_1::glReadBuffer(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_112glReadBufferEj(
    QOpenGLFunctions_2_1 *self,
    GLenum mode) {
  self->glReadBuffer(mode);
}

//  void QOpenGLFunctions_2_1::glPixelStorei(GLenum pname, GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_113glPixelStoreiEji(
    QOpenGLFunctions_2_1 *self,
    GLenum pname,
    GLint param) {
  self->glPixelStorei(pname, param);
}

//  void QOpenGLFunctions_2_1::glPixelStoref(GLenum pname, GLfloat param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_113glPixelStorefEjf(
    QOpenGLFunctions_2_1 *self,
    GLenum pname,
    GLfloat param) {
  self->glPixelStoref(pname, param);
}

//  void QOpenGLFunctions_2_1::glDepthFunc(GLenum func)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_111glDepthFuncEj(
    QOpenGLFunctions_2_1 *self,
    GLenum func) {
  self->glDepthFunc(func);
}

//  void QOpenGLFunctions_2_1::glStencilOp(GLenum fail, GLenum zfail, GLenum
//      zpass)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_111glStencilOpEjjj(
    QOpenGLFunctions_2_1 *self,
    GLenum fail,
    GLenum zfail,
    GLenum zpass) {
  self->glStencilOp(fail, zfail, zpass);
}

//  void QOpenGLFunctions_2_1::glStencilFunc(GLenum func, GLint ref, GLuint
//      mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_113glStencilFuncEjij(
    QOpenGLFunctions_2_1 *self,
    GLenum func,
    GLint ref,
    GLuint mask) {
  self->glStencilFunc(func, ref, mask);
}

//  void QOpenGLFunctions_2_1::glLogicOp(GLenum opcode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_19glLogicOpEj(
    QOpenGLFunctions_2_1 *self,
    GLenum opcode) {
  self->glLogicOp(opcode);
}

//  void QOpenGLFunctions_2_1::glBlendFunc(GLenum sfactor, GLenum dfactor)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_111glBlendFuncEjj(
    QOpenGLFunctions_2_1 *self,
    GLenum sfactor,
    GLenum dfactor) {
  self->glBlendFunc(sfactor, dfactor);
}

//  void QOpenGLFunctions_2_1::glFlush()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_17glFlushEv(QOpenGLFunctions_2_1 *self) {
  self->glFlush();
}

//  void QOpenGLFunctions_2_1::glFinish()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_18glFinishEv(QOpenGLFunctions_2_1 *self) {
  self->glFinish();
}

//  void QOpenGLFunctions_2_1::glEnable(GLenum cap)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_18glEnableEj(
    QOpenGLFunctions_2_1 *self,
    GLenum cap) {
  self->glEnable(cap);
}

//  void QOpenGLFunctions_2_1::glDisable(GLenum cap)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_19glDisableEj(
    QOpenGLFunctions_2_1 *self,
    GLenum cap) {
  self->glDisable(cap);
}

//  void QOpenGLFunctions_2_1::glDepthMask(GLboolean flag)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_111glDepthMaskEh(
    QOpenGLFunctions_2_1 *self,
    GLboolean flag) {
  self->glDepthMask(flag);
}

//  void QOpenGLFunctions_2_1::glColorMask(GLboolean red, GLboolean green,
//      GLboolean blue, GLboolean alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_111glColorMaskEhhhh(
    QOpenGLFunctions_2_1 *self,
    GLboolean red,
    GLboolean green,
    GLboolean blue,
    GLboolean alpha) {
  self->glColorMask(red, green, blue, alpha);
}

//  void QOpenGLFunctions_2_1::glStencilMask(GLuint mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_113glStencilMaskEj(
    QOpenGLFunctions_2_1 *self,
    GLuint mask) {
  self->glStencilMask(mask);
}

//  void QOpenGLFunctions_2_1::glClearDepth(GLdouble depth)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_112glClearDepthEd(
    QOpenGLFunctions_2_1 *self,
    GLdouble depth) {
  self->glClearDepth(depth);
}

//  void QOpenGLFunctions_2_1::glClearStencil(GLint s)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_114glClearStencilEi(
    QOpenGLFunctions_2_1 *self,
    GLint s) {
  self->glClearStencil(s);
}

//  void QOpenGLFunctions_2_1::glClearColor(GLfloat red, GLfloat green,
//      GLfloat blue, GLfloat alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_112glClearColorEffff(
    QOpenGLFunctions_2_1 *self,
    GLfloat red,
    GLfloat green,
    GLfloat blue,
    GLfloat alpha) {
  self->glClearColor(red, green, blue, alpha);
}

//  void QOpenGLFunctions_2_1::glClear(GLbitfield mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_17glClearEj(
    QOpenGLFunctions_2_1 *self,
    GLbitfield mask) {
  self->glClear(mask);
}

//  void QOpenGLFunctions_2_1::glDrawBuffer(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_112glDrawBufferEj(
    QOpenGLFunctions_2_1 *self,
    GLenum mode) {
  self->glDrawBuffer(mode);
}

//  void QOpenGLFunctions_2_1::glTexParameteri(GLenum target, GLenum pname,
//      GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_115glTexParameteriEjji(
    QOpenGLFunctions_2_1 *self,
    GLenum target,
    GLenum pname,
    GLint param) {
  self->glTexParameteri(target, pname, param);
}

//  void QOpenGLFunctions_2_1::glTexParameterf(GLenum target, GLenum pname,
//      GLfloat param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_115glTexParameterfEjjf(
    QOpenGLFunctions_2_1 *self,
    GLenum target,
    GLenum pname,
    GLfloat param) {
  self->glTexParameterf(target, pname, param);
}

//  void QOpenGLFunctions_2_1::glScissor(GLint x, GLint y, GLsizei width,
//      GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_19glScissorEiiii(
    QOpenGLFunctions_2_1 *self,
    GLint x,
    GLint y,
    GLsizei width,
    GLsizei height) {
  self->glScissor(x, y, width, height);
}

//  void QOpenGLFunctions_2_1::glPolygonMode(GLenum face, GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_113glPolygonModeEjj(
    QOpenGLFunctions_2_1 *self,
    GLenum face,
    GLenum mode) {
  self->glPolygonMode(face, mode);
}

//  void QOpenGLFunctions_2_1::glPointSize(GLfloat size)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_111glPointSizeEf(
    QOpenGLFunctions_2_1 *self,
    GLfloat size) {
  self->glPointSize(size);
}

//  void QOpenGLFunctions_2_1::glLineWidth(GLfloat width)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_111glLineWidthEf(
    QOpenGLFunctions_2_1 *self,
    GLfloat width) {
  self->glLineWidth(width);
}

//  void QOpenGLFunctions_2_1::glHint(GLenum target, GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_16glHintEjj(
    QOpenGLFunctions_2_1 *self,
    GLenum target,
    GLenum mode) {
  self->glHint(target, mode);
}

//  void QOpenGLFunctions_2_1::glFrontFace(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_111glFrontFaceEj(
    QOpenGLFunctions_2_1 *self,
    GLenum mode) {
  self->glFrontFace(mode);
}

//  void QOpenGLFunctions_2_1::glCullFace(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_110glCullFaceEj(
    QOpenGLFunctions_2_1 *self,
    GLenum mode) {
  self->glCullFace(mode);
}

//  void QOpenGLFunctions_2_1::glIndexub(GLubyte c)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_19glIndexubEh(
    QOpenGLFunctions_2_1 *self,
    GLubyte c) {
  self->glIndexub(c);
}

//  void QOpenGLFunctions_2_1::glBindTexture(GLenum target, GLuint texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_113glBindTextureEjj(
    QOpenGLFunctions_2_1 *self,
    GLenum target,
    GLuint texture) {
  self->glBindTexture(target, texture);
}

//  void QOpenGLFunctions_2_1::glCopyTexSubImage2D(GLenum target, GLint
//      level, GLint xoffset, GLint yoffset, GLint x, GLint y, GLsizei width,
//      GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_119glCopyTexSubImage2DEjiiiiiii(
    QOpenGLFunctions_2_1 *self,
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

//  void QOpenGLFunctions_2_1::glCopyTexSubImage1D(GLenum target, GLint
//      level, GLint xoffset, GLint x, GLint y, GLsizei width)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_119glCopyTexSubImage1DEjiiiii(
    QOpenGLFunctions_2_1 *self,
    GLenum target,
    GLint level,
    GLint xoffset,
    GLint x,
    GLint y,
    GLsizei width) {
  self->glCopyTexSubImage1D(target, level, xoffset, x, y, width);
}

//  void QOpenGLFunctions_2_1::glCopyTexImage2D(GLenum target, GLint level,
//      GLenum internalformat, GLint x, GLint y, GLsizei width, GLsizei
//      height, GLint border)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_116glCopyTexImage2DEjijiiiii(
    QOpenGLFunctions_2_1 *self,
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

//  void QOpenGLFunctions_2_1::glCopyTexImage1D(GLenum target, GLint level,
//      GLenum internalformat, GLint x, GLint y, GLsizei width, GLint border)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_116glCopyTexImage1DEjijiiii(
    QOpenGLFunctions_2_1 *self,
    GLenum target,
    GLint level,
    GLenum internalformat,
    GLint x,
    GLint y,
    GLsizei width,
    GLint border) {
  self->glCopyTexImage1D(target, level, internalformat, x, y, width, border);
}

//  void QOpenGLFunctions_2_1::glPolygonOffset(GLfloat factor, GLfloat units)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_115glPolygonOffsetEff(
    QOpenGLFunctions_2_1 *self,
    GLfloat factor,
    GLfloat units) {
  self->glPolygonOffset(factor, units);
}

//  void QOpenGLFunctions_2_1::glDrawArrays(GLenum mode, GLint first, GLsizei
//      count)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_112glDrawArraysEjii(
    QOpenGLFunctions_2_1 *self,
    GLenum mode,
    GLint first,
    GLsizei count) {
  self->glDrawArrays(mode, first, count);
}

//  void QOpenGLFunctions_2_1::glCopyTexSubImage3D(GLenum target, GLint
//      level, GLint xoffset, GLint yoffset, GLint zoffset, GLint x, GLint y,
//      GLsizei width, GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_119glCopyTexSubImage3DEjiiiiiiii(
    QOpenGLFunctions_2_1 *self,
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

//  void QOpenGLFunctions_2_1::glBlendEquation(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_115glBlendEquationEj(
    QOpenGLFunctions_2_1 *self,
    GLenum mode) {
  self->glBlendEquation(mode);
}

//  void QOpenGLFunctions_2_1::glBlendColor(GLfloat red, GLfloat green,
//      GLfloat blue, GLfloat alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_112glBlendColorEffff(
    QOpenGLFunctions_2_1 *self,
    GLfloat red,
    GLfloat green,
    GLfloat blue,
    GLfloat alpha) {
  self->glBlendColor(red, green, blue, alpha);
}

//  void QOpenGLFunctions_2_1::glSampleCoverage(GLfloat value, GLboolean
//      invert)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_116glSampleCoverageEfh(
    QOpenGLFunctions_2_1 *self,
    GLfloat value,
    GLboolean invert) {
  self->glSampleCoverage(value, invert);
}

//  void QOpenGLFunctions_2_1::glActiveTexture(GLenum texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_115glActiveTextureEj(
    QOpenGLFunctions_2_1 *self,
    GLenum texture) {
  self->glActiveTexture(texture);
}

//  void QOpenGLFunctions_2_1::glPointParameteri(GLenum pname, GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_117glPointParameteriEji(
    QOpenGLFunctions_2_1 *self,
    GLenum pname,
    GLint param) {
  self->glPointParameteri(pname, param);
}

//  void QOpenGLFunctions_2_1::glPointParameterf(GLenum pname, GLfloat param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_117glPointParameterfEjf(
    QOpenGLFunctions_2_1 *self,
    GLenum pname,
    GLfloat param) {
  self->glPointParameterf(pname, param);
}

//  void QOpenGLFunctions_2_1::glBlendFuncSeparate(GLenum sfactorRGB, GLenum
//      dfactorRGB, GLenum sfactorAlpha, GLenum dfactorAlpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_119glBlendFuncSeparateEjjjj(
    QOpenGLFunctions_2_1 *self,
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

//  void QOpenGLFunctions_2_1::glBindBuffer(GLenum target, GLuint buffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_112glBindBufferEjj(
    QOpenGLFunctions_2_1 *self,
    GLenum target,
    GLuint buffer) {
  self->glBindBuffer(target, buffer);
}

//  void QOpenGLFunctions_2_1::glEndQuery(GLenum target)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_110glEndQueryEj(
    QOpenGLFunctions_2_1 *self,
    GLenum target) {
  self->glEndQuery(target);
}

//  void QOpenGLFunctions_2_1::glBeginQuery(GLenum target, GLuint id)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_112glBeginQueryEjj(
    QOpenGLFunctions_2_1 *self,
    GLenum target,
    GLuint id) {
  self->glBeginQuery(target, id);
}

//  void QOpenGLFunctions_2_1::glValidateProgram(GLuint program)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_117glValidateProgramEj(
    QOpenGLFunctions_2_1 *self,
    GLuint program) {
  self->glValidateProgram(program);
}

//  void QOpenGLFunctions_2_1::glUniform4i(GLint location, GLint v0, GLint
//      v1, GLint v2, GLint v3)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_111glUniform4iEiiiii(
    QOpenGLFunctions_2_1 *self,
    GLint location,
    GLint v0,
    GLint v1,
    GLint v2,
    GLint v3) {
  self->glUniform4i(location, v0, v1, v2, v3);
}

//  void QOpenGLFunctions_2_1::glUniform3i(GLint location, GLint v0, GLint
//      v1, GLint v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_111glUniform3iEiiii(
    QOpenGLFunctions_2_1 *self,
    GLint location,
    GLint v0,
    GLint v1,
    GLint v2) {
  self->glUniform3i(location, v0, v1, v2);
}

//  void QOpenGLFunctions_2_1::glUniform2i(GLint location, GLint v0, GLint
//      v1)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_111glUniform2iEiii(
    QOpenGLFunctions_2_1 *self,
    GLint location,
    GLint v0,
    GLint v1) {
  self->glUniform2i(location, v0, v1);
}

//  void QOpenGLFunctions_2_1::glUniform1i(GLint location, GLint v0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_111glUniform1iEii(
    QOpenGLFunctions_2_1 *self,
    GLint location,
    GLint v0) {
  self->glUniform1i(location, v0);
}

//  void QOpenGLFunctions_2_1::glUniform4f(GLint location, GLfloat v0,
//      GLfloat v1, GLfloat v2, GLfloat v3)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_111glUniform4fEiffff(
    QOpenGLFunctions_2_1 *self,
    GLint location,
    GLfloat v0,
    GLfloat v1,
    GLfloat v2,
    GLfloat v3) {
  self->glUniform4f(location, v0, v1, v2, v3);
}

//  void QOpenGLFunctions_2_1::glUniform3f(GLint location, GLfloat v0,
//      GLfloat v1, GLfloat v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_111glUniform3fEifff(
    QOpenGLFunctions_2_1 *self,
    GLint location,
    GLfloat v0,
    GLfloat v1,
    GLfloat v2) {
  self->glUniform3f(location, v0, v1, v2);
}

//  void QOpenGLFunctions_2_1::glUniform2f(GLint location, GLfloat v0,
//      GLfloat v1)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_111glUniform2fEiff(
    QOpenGLFunctions_2_1 *self,
    GLint location,
    GLfloat v0,
    GLfloat v1) {
  self->glUniform2f(location, v0, v1);
}

//  void QOpenGLFunctions_2_1::glUniform1f(GLint location, GLfloat v0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_111glUniform1fEif(
    QOpenGLFunctions_2_1 *self,
    GLint location,
    GLfloat v0) {
  self->glUniform1f(location, v0);
}

//  void QOpenGLFunctions_2_1::glUseProgram(GLuint program)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_112glUseProgramEj(
    QOpenGLFunctions_2_1 *self,
    GLuint program) {
  self->glUseProgram(program);
}

//  void QOpenGLFunctions_2_1::glLinkProgram(GLuint program)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_113glLinkProgramEj(
    QOpenGLFunctions_2_1 *self,
    GLuint program) {
  self->glLinkProgram(program);
}

//  void QOpenGLFunctions_2_1::glEnableVertexAttribArray(GLuint index)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_125glEnableVertexAttribArrayEj(
    QOpenGLFunctions_2_1 *self,
    GLuint index) {
  self->glEnableVertexAttribArray(index);
}

//  void QOpenGLFunctions_2_1::glDisableVertexAttribArray(GLuint index)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_126glDisableVertexAttribArrayEj(
    QOpenGLFunctions_2_1 *self,
    GLuint index) {
  self->glDisableVertexAttribArray(index);
}

//  void QOpenGLFunctions_2_1::glDetachShader(GLuint program, GLuint shader)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_114glDetachShaderEjj(
    QOpenGLFunctions_2_1 *self,
    GLuint program,
    GLuint shader) {
  self->glDetachShader(program, shader);
}

//  void QOpenGLFunctions_2_1::glDeleteShader(GLuint shader)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_114glDeleteShaderEj(
    QOpenGLFunctions_2_1 *self,
    GLuint shader) {
  self->glDeleteShader(shader);
}

//  void QOpenGLFunctions_2_1::glDeleteProgram(GLuint program)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_115glDeleteProgramEj(
    QOpenGLFunctions_2_1 *self,
    GLuint program) {
  self->glDeleteProgram(program);
}

//  void QOpenGLFunctions_2_1::glCompileShader(GLuint shader)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_115glCompileShaderEj(
    QOpenGLFunctions_2_1 *self,
    GLuint shader) {
  self->glCompileShader(shader);
}

//  void QOpenGLFunctions_2_1::glAttachShader(GLuint program, GLuint shader)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_114glAttachShaderEjj(
    QOpenGLFunctions_2_1 *self,
    GLuint program,
    GLuint shader) {
  self->glAttachShader(program, shader);
}

//  void QOpenGLFunctions_2_1::glStencilMaskSeparate(GLenum face, GLuint
//      mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_121glStencilMaskSeparateEjj(
    QOpenGLFunctions_2_1 *self,
    GLenum face,
    GLuint mask) {
  self->glStencilMaskSeparate(face, mask);
}

//  void QOpenGLFunctions_2_1::glStencilFuncSeparate(GLenum face, GLenum
//      func, GLint ref, GLuint mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_121glStencilFuncSeparateEjjij(
    QOpenGLFunctions_2_1 *self,
    GLenum face,
    GLenum func,
    GLint ref,
    GLuint mask) {
  self->glStencilFuncSeparate(face, func, ref, mask);
}

//  void QOpenGLFunctions_2_1::glStencilOpSeparate(GLenum face, GLenum sfail,
//      GLenum dpfail, GLenum dppass)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_119glStencilOpSeparateEjjjj(
    QOpenGLFunctions_2_1 *self,
    GLenum face,
    GLenum sfail,
    GLenum dpfail,
    GLenum dppass) {
  self->glStencilOpSeparate(face, sfail, dpfail, dppass);
}

//  void QOpenGLFunctions_2_1::glBlendEquationSeparate(GLenum modeRGB, GLenum
//      modeAlpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_123glBlendEquationSeparateEjj(
    QOpenGLFunctions_2_1 *self,
    GLenum modeRGB,
    GLenum modeAlpha) {
  self->glBlendEquationSeparate(modeRGB, modeAlpha);
}

//  void QOpenGLFunctions_2_1::glTranslatef(GLfloat x, GLfloat y, GLfloat z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_112glTranslatefEfff(
    QOpenGLFunctions_2_1 *self,
    GLfloat x,
    GLfloat y,
    GLfloat z) {
  self->glTranslatef(x, y, z);
}

//  void QOpenGLFunctions_2_1::glTranslated(GLdouble x, GLdouble y, GLdouble
//      z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_112glTranslatedEddd(
    QOpenGLFunctions_2_1 *self,
    GLdouble x,
    GLdouble y,
    GLdouble z) {
  self->glTranslated(x, y, z);
}

//  void QOpenGLFunctions_2_1::glScalef(GLfloat x, GLfloat y, GLfloat z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_18glScalefEfff(
    QOpenGLFunctions_2_1 *self,
    GLfloat x,
    GLfloat y,
    GLfloat z) {
  self->glScalef(x, y, z);
}

//  void QOpenGLFunctions_2_1::glScaled(GLdouble x, GLdouble y, GLdouble z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_18glScaledEddd(
    QOpenGLFunctions_2_1 *self,
    GLdouble x,
    GLdouble y,
    GLdouble z) {
  self->glScaled(x, y, z);
}

//  void QOpenGLFunctions_2_1::glRotatef(GLfloat angle, GLfloat x, GLfloat y,
//      GLfloat z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_19glRotatefEffff(
    QOpenGLFunctions_2_1 *self,
    GLfloat angle,
    GLfloat x,
    GLfloat y,
    GLfloat z) {
  self->glRotatef(angle, x, y, z);
}

//  void QOpenGLFunctions_2_1::glRotated(GLdouble angle, GLdouble x, GLdouble
//      y, GLdouble z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_19glRotatedEdddd(
    QOpenGLFunctions_2_1 *self,
    GLdouble angle,
    GLdouble x,
    GLdouble y,
    GLdouble z) {
  self->glRotated(angle, x, y, z);
}

//  void QOpenGLFunctions_2_1::glPushMatrix()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_112glPushMatrixEv(
    QOpenGLFunctions_2_1 *self) {
  self->glPushMatrix();
}

//  void QOpenGLFunctions_2_1::glPopMatrix()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_111glPopMatrixEv(
    QOpenGLFunctions_2_1 *self) {
  self->glPopMatrix();
}

//  void QOpenGLFunctions_2_1::glOrtho(GLdouble left, GLdouble right,
//      GLdouble bottom, GLdouble top, GLdouble zNear, GLdouble zFar)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_17glOrthoEdddddd(
    QOpenGLFunctions_2_1 *self,
    GLdouble left,
    GLdouble right,
    GLdouble bottom,
    GLdouble top,
    GLdouble zNear,
    GLdouble zFar) {
  self->glOrtho(left, right, bottom, top, zNear, zFar);
}

//  void QOpenGLFunctions_2_1::glMatrixMode(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_112glMatrixModeEj(
    QOpenGLFunctions_2_1 *self,
    GLenum mode) {
  self->glMatrixMode(mode);
}

//  void QOpenGLFunctions_2_1::glLoadIdentity()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_114glLoadIdentityEv(
    QOpenGLFunctions_2_1 *self) {
  self->glLoadIdentity();
}

//  void QOpenGLFunctions_2_1::glFrustum(GLdouble left, GLdouble right,
//      GLdouble bottom, GLdouble top, GLdouble zNear, GLdouble zFar)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_19glFrustumEdddddd(
    QOpenGLFunctions_2_1 *self,
    GLdouble left,
    GLdouble right,
    GLdouble bottom,
    GLdouble top,
    GLdouble zNear,
    GLdouble zFar) {
  self->glFrustum(left, right, bottom, top, zNear, zFar);
}

//  void QOpenGLFunctions_2_1::glCopyPixels(GLint x, GLint y, GLsizei width,
//      GLsizei height, GLenum type)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_112glCopyPixelsEiiiij(
    QOpenGLFunctions_2_1 *self,
    GLint x,
    GLint y,
    GLsizei width,
    GLsizei height,
    GLenum type) {
  self->glCopyPixels(x, y, width, height, type);
}

//  void QOpenGLFunctions_2_1::glPixelTransferi(GLenum pname, GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_116glPixelTransferiEji(
    QOpenGLFunctions_2_1 *self,
    GLenum pname,
    GLint param) {
  self->glPixelTransferi(pname, param);
}

//  void QOpenGLFunctions_2_1::glPixelTransferf(GLenum pname, GLfloat param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_116glPixelTransferfEjf(
    QOpenGLFunctions_2_1 *self,
    GLenum pname,
    GLfloat param) {
  self->glPixelTransferf(pname, param);
}

//  void QOpenGLFunctions_2_1::glPixelZoom(GLfloat xfactor, GLfloat yfactor)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_111glPixelZoomEff(
    QOpenGLFunctions_2_1 *self,
    GLfloat xfactor,
    GLfloat yfactor) {
  self->glPixelZoom(xfactor, yfactor);
}

//  void QOpenGLFunctions_2_1::glAlphaFunc(GLenum func, GLfloat ref)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_111glAlphaFuncEjf(
    QOpenGLFunctions_2_1 *self,
    GLenum func,
    GLfloat ref) {
  self->glAlphaFunc(func, ref);
}

//  void QOpenGLFunctions_2_1::glEvalPoint2(GLint i, GLint j)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_112glEvalPoint2Eii(
    QOpenGLFunctions_2_1 *self,
    GLint i,
    GLint j) {
  self->glEvalPoint2(i, j);
}

//  void QOpenGLFunctions_2_1::glEvalMesh2(GLenum mode, GLint i1, GLint i2,
//      GLint j1, GLint j2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_111glEvalMesh2Ejiiii(
    QOpenGLFunctions_2_1 *self,
    GLenum mode,
    GLint i1,
    GLint i2,
    GLint j1,
    GLint j2) {
  self->glEvalMesh2(mode, i1, i2, j1, j2);
}

//  void QOpenGLFunctions_2_1::glEvalPoint1(GLint i)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_112glEvalPoint1Ei(
    QOpenGLFunctions_2_1 *self,
    GLint i) {
  self->glEvalPoint1(i);
}

//  void QOpenGLFunctions_2_1::glEvalMesh1(GLenum mode, GLint i1, GLint i2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_111glEvalMesh1Ejii(
    QOpenGLFunctions_2_1 *self,
    GLenum mode,
    GLint i1,
    GLint i2) {
  self->glEvalMesh1(mode, i1, i2);
}

//  void QOpenGLFunctions_2_1::glEvalCoord2f(GLfloat u, GLfloat v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_113glEvalCoord2fEff(
    QOpenGLFunctions_2_1 *self,
    GLfloat u,
    GLfloat v) {
  self->glEvalCoord2f(u, v);
}

//  void QOpenGLFunctions_2_1::glEvalCoord2d(GLdouble u, GLdouble v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_113glEvalCoord2dEdd(
    QOpenGLFunctions_2_1 *self,
    GLdouble u,
    GLdouble v) {
  self->glEvalCoord2d(u, v);
}

//  void QOpenGLFunctions_2_1::glEvalCoord1f(GLfloat u)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_113glEvalCoord1fEf(
    QOpenGLFunctions_2_1 *self,
    GLfloat u) {
  self->glEvalCoord1f(u);
}

//  void QOpenGLFunctions_2_1::glEvalCoord1d(GLdouble u)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_113glEvalCoord1dEd(
    QOpenGLFunctions_2_1 *self,
    GLdouble u) {
  self->glEvalCoord1d(u);
}

//  void QOpenGLFunctions_2_1::glMapGrid2f(GLint un, GLfloat u1, GLfloat u2,
//      GLint vn, GLfloat v1, GLfloat v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_111glMapGrid2fEiffiff(
    QOpenGLFunctions_2_1 *self,
    GLint un,
    GLfloat u1,
    GLfloat u2,
    GLint vn,
    GLfloat v1,
    GLfloat v2) {
  self->glMapGrid2f(un, u1, u2, vn, v1, v2);
}

//  void QOpenGLFunctions_2_1::glMapGrid2d(GLint un, GLdouble u1, GLdouble
//      u2, GLint vn, GLdouble v1, GLdouble v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_111glMapGrid2dEiddidd(
    QOpenGLFunctions_2_1 *self,
    GLint un,
    GLdouble u1,
    GLdouble u2,
    GLint vn,
    GLdouble v1,
    GLdouble v2) {
  self->glMapGrid2d(un, u1, u2, vn, v1, v2);
}

//  void QOpenGLFunctions_2_1::glMapGrid1f(GLint un, GLfloat u1, GLfloat u2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_111glMapGrid1fEiff(
    QOpenGLFunctions_2_1 *self,
    GLint un,
    GLfloat u1,
    GLfloat u2) {
  self->glMapGrid1f(un, u1, u2);
}

//  void QOpenGLFunctions_2_1::glMapGrid1d(GLint un, GLdouble u1, GLdouble
//      u2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_111glMapGrid1dEidd(
    QOpenGLFunctions_2_1 *self,
    GLint un,
    GLdouble u1,
    GLdouble u2) {
  self->glMapGrid1d(un, u1, u2);
}

//  void QOpenGLFunctions_2_1::glPushAttrib(GLbitfield mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_112glPushAttribEj(
    QOpenGLFunctions_2_1 *self,
    GLbitfield mask) {
  self->glPushAttrib(mask);
}

//  void QOpenGLFunctions_2_1::glPopAttrib()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_111glPopAttribEv(
    QOpenGLFunctions_2_1 *self) {
  self->glPopAttrib();
}

//  void QOpenGLFunctions_2_1::glAccum(GLenum op, GLfloat value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_17glAccumEjf(
    QOpenGLFunctions_2_1 *self,
    GLenum op,
    GLfloat value) {
  self->glAccum(op, value);
}

//  void QOpenGLFunctions_2_1::glIndexMask(GLuint mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_111glIndexMaskEj(
    QOpenGLFunctions_2_1 *self,
    GLuint mask) {
  self->glIndexMask(mask);
}

//  void QOpenGLFunctions_2_1::glClearIndex(GLfloat c)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_112glClearIndexEf(
    QOpenGLFunctions_2_1 *self,
    GLfloat c) {
  self->glClearIndex(c);
}

//  void QOpenGLFunctions_2_1::glClearAccum(GLfloat red, GLfloat green,
//      GLfloat blue, GLfloat alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_112glClearAccumEffff(
    QOpenGLFunctions_2_1 *self,
    GLfloat red,
    GLfloat green,
    GLfloat blue,
    GLfloat alpha) {
  self->glClearAccum(red, green, blue, alpha);
}

//  void QOpenGLFunctions_2_1::glPushName(GLuint name)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_110glPushNameEj(
    QOpenGLFunctions_2_1 *self,
    GLuint name) {
  self->glPushName(name);
}

//  void QOpenGLFunctions_2_1::glPopName()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_19glPopNameEv(
    QOpenGLFunctions_2_1 *self) {
  self->glPopName();
}

//  void QOpenGLFunctions_2_1::glPassThrough(GLfloat token)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_113glPassThroughEf(
    QOpenGLFunctions_2_1 *self,
    GLfloat token) {
  self->glPassThrough(token);
}

//  void QOpenGLFunctions_2_1::glLoadName(GLuint name)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_110glLoadNameEj(
    QOpenGLFunctions_2_1 *self,
    GLuint name) {
  self->glLoadName(name);
}

//  void QOpenGLFunctions_2_1::glInitNames()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_111glInitNamesEv(
    QOpenGLFunctions_2_1 *self) {
  self->glInitNames();
}

//  void QOpenGLFunctions_2_1::glTexGeni(GLenum coord, GLenum pname, GLint
//      param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_19glTexGeniEjji(
    QOpenGLFunctions_2_1 *self,
    GLenum coord,
    GLenum pname,
    GLint param) {
  self->glTexGeni(coord, pname, param);
}

//  void QOpenGLFunctions_2_1::glTexGenf(GLenum coord, GLenum pname, GLfloat
//      param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_19glTexGenfEjjf(
    QOpenGLFunctions_2_1 *self,
    GLenum coord,
    GLenum pname,
    GLfloat param) {
  self->glTexGenf(coord, pname, param);
}

//  void QOpenGLFunctions_2_1::glTexGend(GLenum coord, GLenum pname, GLdouble
//      param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_19glTexGendEjjd(
    QOpenGLFunctions_2_1 *self,
    GLenum coord,
    GLenum pname,
    GLdouble param) {
  self->glTexGend(coord, pname, param);
}

//  void QOpenGLFunctions_2_1::glTexEnvi(GLenum target, GLenum pname, GLint
//      param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_19glTexEnviEjji(
    QOpenGLFunctions_2_1 *self,
    GLenum target,
    GLenum pname,
    GLint param) {
  self->glTexEnvi(target, pname, param);
}

//  void QOpenGLFunctions_2_1::glTexEnvf(GLenum target, GLenum pname, GLfloat
//      param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_19glTexEnvfEjjf(
    QOpenGLFunctions_2_1 *self,
    GLenum target,
    GLenum pname,
    GLfloat param) {
  self->glTexEnvf(target, pname, param);
}

//  void QOpenGLFunctions_2_1::glShadeModel(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_112glShadeModelEj(
    QOpenGLFunctions_2_1 *self,
    GLenum mode) {
  self->glShadeModel(mode);
}

//  void QOpenGLFunctions_2_1::glMateriali(GLenum face, GLenum pname, GLint
//      param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_111glMaterialiEjji(
    QOpenGLFunctions_2_1 *self,
    GLenum face,
    GLenum pname,
    GLint param) {
  self->glMateriali(face, pname, param);
}

//  void QOpenGLFunctions_2_1::glMaterialf(GLenum face, GLenum pname, GLfloat
//      param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_111glMaterialfEjjf(
    QOpenGLFunctions_2_1 *self,
    GLenum face,
    GLenum pname,
    GLfloat param) {
  self->glMaterialf(face, pname, param);
}

//  void QOpenGLFunctions_2_1::glLineStipple(GLint factor, GLushort pattern)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_113glLineStippleEit(
    QOpenGLFunctions_2_1 *self,
    GLint factor,
    GLushort pattern) {
  self->glLineStipple(factor, pattern);
}

//  void QOpenGLFunctions_2_1::glLightModeli(GLenum pname, GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_113glLightModeliEji(
    QOpenGLFunctions_2_1 *self,
    GLenum pname,
    GLint param) {
  self->glLightModeli(pname, param);
}

//  void QOpenGLFunctions_2_1::glLightModelf(GLenum pname, GLfloat param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_113glLightModelfEjf(
    QOpenGLFunctions_2_1 *self,
    GLenum pname,
    GLfloat param) {
  self->glLightModelf(pname, param);
}

//  void QOpenGLFunctions_2_1::glLighti(GLenum light, GLenum pname, GLint
//      param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_18glLightiEjji(
    QOpenGLFunctions_2_1 *self,
    GLenum light,
    GLenum pname,
    GLint param) {
  self->glLighti(light, pname, param);
}

//  void QOpenGLFunctions_2_1::glLightf(GLenum light, GLenum pname, GLfloat
//      param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_18glLightfEjjf(
    QOpenGLFunctions_2_1 *self,
    GLenum light,
    GLenum pname,
    GLfloat param) {
  self->glLightf(light, pname, param);
}

//  void QOpenGLFunctions_2_1::glFogi(GLenum pname, GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_16glFogiEji(
    QOpenGLFunctions_2_1 *self,
    GLenum pname,
    GLint param) {
  self->glFogi(pname, param);
}

//  void QOpenGLFunctions_2_1::glFogf(GLenum pname, GLfloat param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_16glFogfEjf(
    QOpenGLFunctions_2_1 *self,
    GLenum pname,
    GLfloat param) {
  self->glFogf(pname, param);
}

//  void QOpenGLFunctions_2_1::glColorMaterial(GLenum face, GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_115glColorMaterialEjj(
    QOpenGLFunctions_2_1 *self,
    GLenum face,
    GLenum mode) {
  self->glColorMaterial(face, mode);
}

//  void QOpenGLFunctions_2_1::glVertex4s(GLshort x, GLshort y, GLshort z,
//      GLshort w)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_110glVertex4sEssss(
    QOpenGLFunctions_2_1 *self,
    GLshort x,
    GLshort y,
    GLshort z,
    GLshort w) {
  self->glVertex4s(x, y, z, w);
}

//  void QOpenGLFunctions_2_1::glVertex4i(GLint x, GLint y, GLint z, GLint w)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_110glVertex4iEiiii(
    QOpenGLFunctions_2_1 *self,
    GLint x,
    GLint y,
    GLint z,
    GLint w) {
  self->glVertex4i(x, y, z, w);
}

//  void QOpenGLFunctions_2_1::glVertex4f(GLfloat x, GLfloat y, GLfloat z,
//      GLfloat w)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_110glVertex4fEffff(
    QOpenGLFunctions_2_1 *self,
    GLfloat x,
    GLfloat y,
    GLfloat z,
    GLfloat w) {
  self->glVertex4f(x, y, z, w);
}

//  void QOpenGLFunctions_2_1::glVertex4d(GLdouble x, GLdouble y, GLdouble z,
//      GLdouble w)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_110glVertex4dEdddd(
    QOpenGLFunctions_2_1 *self,
    GLdouble x,
    GLdouble y,
    GLdouble z,
    GLdouble w) {
  self->glVertex4d(x, y, z, w);
}

//  void QOpenGLFunctions_2_1::glVertex3s(GLshort x, GLshort y, GLshort z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_110glVertex3sEsss(
    QOpenGLFunctions_2_1 *self,
    GLshort x,
    GLshort y,
    GLshort z) {
  self->glVertex3s(x, y, z);
}

//  void QOpenGLFunctions_2_1::glVertex3i(GLint x, GLint y, GLint z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_110glVertex3iEiii(
    QOpenGLFunctions_2_1 *self,
    GLint x,
    GLint y,
    GLint z) {
  self->glVertex3i(x, y, z);
}

//  void QOpenGLFunctions_2_1::glVertex3f(GLfloat x, GLfloat y, GLfloat z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_110glVertex3fEfff(
    QOpenGLFunctions_2_1 *self,
    GLfloat x,
    GLfloat y,
    GLfloat z) {
  self->glVertex3f(x, y, z);
}

//  void QOpenGLFunctions_2_1::glVertex3d(GLdouble x, GLdouble y, GLdouble z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_110glVertex3dEddd(
    QOpenGLFunctions_2_1 *self,
    GLdouble x,
    GLdouble y,
    GLdouble z) {
  self->glVertex3d(x, y, z);
}

//  void QOpenGLFunctions_2_1::glVertex2s(GLshort x, GLshort y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_110glVertex2sEss(
    QOpenGLFunctions_2_1 *self,
    GLshort x,
    GLshort y) {
  self->glVertex2s(x, y);
}

//  void QOpenGLFunctions_2_1::glVertex2i(GLint x, GLint y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_110glVertex2iEii(
    QOpenGLFunctions_2_1 *self,
    GLint x,
    GLint y) {
  self->glVertex2i(x, y);
}

//  void QOpenGLFunctions_2_1::glVertex2f(GLfloat x, GLfloat y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_110glVertex2fEff(
    QOpenGLFunctions_2_1 *self,
    GLfloat x,
    GLfloat y) {
  self->glVertex2f(x, y);
}

//  void QOpenGLFunctions_2_1::glVertex2d(GLdouble x, GLdouble y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_110glVertex2dEdd(
    QOpenGLFunctions_2_1 *self,
    GLdouble x,
    GLdouble y) {
  self->glVertex2d(x, y);
}

//  void QOpenGLFunctions_2_1::glTexCoord4s(GLshort s, GLshort t, GLshort r,
//      GLshort q)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_112glTexCoord4sEssss(
    QOpenGLFunctions_2_1 *self,
    GLshort s,
    GLshort t,
    GLshort r,
    GLshort q) {
  self->glTexCoord4s(s, t, r, q);
}

//  void QOpenGLFunctions_2_1::glTexCoord4i(GLint s, GLint t, GLint r, GLint
//      q)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_112glTexCoord4iEiiii(
    QOpenGLFunctions_2_1 *self,
    GLint s,
    GLint t,
    GLint r,
    GLint q) {
  self->glTexCoord4i(s, t, r, q);
}

//  void QOpenGLFunctions_2_1::glTexCoord4f(GLfloat s, GLfloat t, GLfloat r,
//      GLfloat q)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_112glTexCoord4fEffff(
    QOpenGLFunctions_2_1 *self,
    GLfloat s,
    GLfloat t,
    GLfloat r,
    GLfloat q) {
  self->glTexCoord4f(s, t, r, q);
}

//  void QOpenGLFunctions_2_1::glTexCoord4d(GLdouble s, GLdouble t, GLdouble
//      r, GLdouble q)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_112glTexCoord4dEdddd(
    QOpenGLFunctions_2_1 *self,
    GLdouble s,
    GLdouble t,
    GLdouble r,
    GLdouble q) {
  self->glTexCoord4d(s, t, r, q);
}

//  void QOpenGLFunctions_2_1::glTexCoord3s(GLshort s, GLshort t, GLshort r)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_112glTexCoord3sEsss(
    QOpenGLFunctions_2_1 *self,
    GLshort s,
    GLshort t,
    GLshort r) {
  self->glTexCoord3s(s, t, r);
}

//  void QOpenGLFunctions_2_1::glTexCoord3i(GLint s, GLint t, GLint r)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_112glTexCoord3iEiii(
    QOpenGLFunctions_2_1 *self,
    GLint s,
    GLint t,
    GLint r) {
  self->glTexCoord3i(s, t, r);
}

//  void QOpenGLFunctions_2_1::glTexCoord3f(GLfloat s, GLfloat t, GLfloat r)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_112glTexCoord3fEfff(
    QOpenGLFunctions_2_1 *self,
    GLfloat s,
    GLfloat t,
    GLfloat r) {
  self->glTexCoord3f(s, t, r);
}

//  void QOpenGLFunctions_2_1::glTexCoord3d(GLdouble s, GLdouble t, GLdouble
//      r)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_112glTexCoord3dEddd(
    QOpenGLFunctions_2_1 *self,
    GLdouble s,
    GLdouble t,
    GLdouble r) {
  self->glTexCoord3d(s, t, r);
}

//  void QOpenGLFunctions_2_1::glTexCoord2s(GLshort s, GLshort t)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_112glTexCoord2sEss(
    QOpenGLFunctions_2_1 *self,
    GLshort s,
    GLshort t) {
  self->glTexCoord2s(s, t);
}

//  void QOpenGLFunctions_2_1::glTexCoord2i(GLint s, GLint t)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_112glTexCoord2iEii(
    QOpenGLFunctions_2_1 *self,
    GLint s,
    GLint t) {
  self->glTexCoord2i(s, t);
}

//  void QOpenGLFunctions_2_1::glTexCoord2f(GLfloat s, GLfloat t)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_112glTexCoord2fEff(
    QOpenGLFunctions_2_1 *self,
    GLfloat s,
    GLfloat t) {
  self->glTexCoord2f(s, t);
}

//  void QOpenGLFunctions_2_1::glTexCoord2d(GLdouble s, GLdouble t)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_112glTexCoord2dEdd(
    QOpenGLFunctions_2_1 *self,
    GLdouble s,
    GLdouble t) {
  self->glTexCoord2d(s, t);
}

//  void QOpenGLFunctions_2_1::glTexCoord1s(GLshort s)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_112glTexCoord1sEs(
    QOpenGLFunctions_2_1 *self,
    GLshort s) {
  self->glTexCoord1s(s);
}

//  void QOpenGLFunctions_2_1::glTexCoord1i(GLint s)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_112glTexCoord1iEi(
    QOpenGLFunctions_2_1 *self,
    GLint s) {
  self->glTexCoord1i(s);
}

//  void QOpenGLFunctions_2_1::glTexCoord1f(GLfloat s)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_112glTexCoord1fEf(
    QOpenGLFunctions_2_1 *self,
    GLfloat s) {
  self->glTexCoord1f(s);
}

//  void QOpenGLFunctions_2_1::glTexCoord1d(GLdouble s)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_112glTexCoord1dEd(
    QOpenGLFunctions_2_1 *self,
    GLdouble s) {
  self->glTexCoord1d(s);
}

//  void QOpenGLFunctions_2_1::glRects(GLshort x1, GLshort y1, GLshort x2,
//      GLshort y2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_17glRectsEssss(
    QOpenGLFunctions_2_1 *self,
    GLshort x1,
    GLshort y1,
    GLshort x2,
    GLshort y2) {
  self->glRects(x1, y1, x2, y2);
}

//  void QOpenGLFunctions_2_1::glRecti(GLint x1, GLint y1, GLint x2, GLint
//      y2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_17glRectiEiiii(
    QOpenGLFunctions_2_1 *self,
    GLint x1,
    GLint y1,
    GLint x2,
    GLint y2) {
  self->glRecti(x1, y1, x2, y2);
}

//  void QOpenGLFunctions_2_1::glRectf(GLfloat x1, GLfloat y1, GLfloat x2,
//      GLfloat y2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_17glRectfEffff(
    QOpenGLFunctions_2_1 *self,
    GLfloat x1,
    GLfloat y1,
    GLfloat x2,
    GLfloat y2) {
  self->glRectf(x1, y1, x2, y2);
}

//  void QOpenGLFunctions_2_1::glRectd(GLdouble x1, GLdouble y1, GLdouble x2,
//      GLdouble y2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_17glRectdEdddd(
    QOpenGLFunctions_2_1 *self,
    GLdouble x1,
    GLdouble y1,
    GLdouble x2,
    GLdouble y2) {
  self->glRectd(x1, y1, x2, y2);
}

//  void QOpenGLFunctions_2_1::glRasterPos4s(GLshort x, GLshort y, GLshort z,
//      GLshort w)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_113glRasterPos4sEssss(
    QOpenGLFunctions_2_1 *self,
    GLshort x,
    GLshort y,
    GLshort z,
    GLshort w) {
  self->glRasterPos4s(x, y, z, w);
}

//  void QOpenGLFunctions_2_1::glRasterPos4i(GLint x, GLint y, GLint z, GLint
//      w)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_113glRasterPos4iEiiii(
    QOpenGLFunctions_2_1 *self,
    GLint x,
    GLint y,
    GLint z,
    GLint w) {
  self->glRasterPos4i(x, y, z, w);
}

//  void QOpenGLFunctions_2_1::glRasterPos4f(GLfloat x, GLfloat y, GLfloat z,
//      GLfloat w)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_113glRasterPos4fEffff(
    QOpenGLFunctions_2_1 *self,
    GLfloat x,
    GLfloat y,
    GLfloat z,
    GLfloat w) {
  self->glRasterPos4f(x, y, z, w);
}

//  void QOpenGLFunctions_2_1::glRasterPos4d(GLdouble x, GLdouble y, GLdouble
//      z, GLdouble w)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_113glRasterPos4dEdddd(
    QOpenGLFunctions_2_1 *self,
    GLdouble x,
    GLdouble y,
    GLdouble z,
    GLdouble w) {
  self->glRasterPos4d(x, y, z, w);
}

//  void QOpenGLFunctions_2_1::glRasterPos3s(GLshort x, GLshort y, GLshort z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_113glRasterPos3sEsss(
    QOpenGLFunctions_2_1 *self,
    GLshort x,
    GLshort y,
    GLshort z) {
  self->glRasterPos3s(x, y, z);
}

//  void QOpenGLFunctions_2_1::glRasterPos3i(GLint x, GLint y, GLint z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_113glRasterPos3iEiii(
    QOpenGLFunctions_2_1 *self,
    GLint x,
    GLint y,
    GLint z) {
  self->glRasterPos3i(x, y, z);
}

//  void QOpenGLFunctions_2_1::glRasterPos3f(GLfloat x, GLfloat y, GLfloat z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_113glRasterPos3fEfff(
    QOpenGLFunctions_2_1 *self,
    GLfloat x,
    GLfloat y,
    GLfloat z) {
  self->glRasterPos3f(x, y, z);
}

//  void QOpenGLFunctions_2_1::glRasterPos3d(GLdouble x, GLdouble y, GLdouble
//      z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_113glRasterPos3dEddd(
    QOpenGLFunctions_2_1 *self,
    GLdouble x,
    GLdouble y,
    GLdouble z) {
  self->glRasterPos3d(x, y, z);
}

//  void QOpenGLFunctions_2_1::glRasterPos2s(GLshort x, GLshort y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_113glRasterPos2sEss(
    QOpenGLFunctions_2_1 *self,
    GLshort x,
    GLshort y) {
  self->glRasterPos2s(x, y);
}

//  void QOpenGLFunctions_2_1::glRasterPos2i(GLint x, GLint y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_113glRasterPos2iEii(
    QOpenGLFunctions_2_1 *self,
    GLint x,
    GLint y) {
  self->glRasterPos2i(x, y);
}

//  void QOpenGLFunctions_2_1::glRasterPos2f(GLfloat x, GLfloat y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_113glRasterPos2fEff(
    QOpenGLFunctions_2_1 *self,
    GLfloat x,
    GLfloat y) {
  self->glRasterPos2f(x, y);
}

//  void QOpenGLFunctions_2_1::glRasterPos2d(GLdouble x, GLdouble y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_113glRasterPos2dEdd(
    QOpenGLFunctions_2_1 *self,
    GLdouble x,
    GLdouble y) {
  self->glRasterPos2d(x, y);
}

//  void QOpenGLFunctions_2_1::glNormal3s(GLshort nx, GLshort ny, GLshort nz)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_110glNormal3sEsss(
    QOpenGLFunctions_2_1 *self,
    GLshort nx,
    GLshort ny,
    GLshort nz) {
  self->glNormal3s(nx, ny, nz);
}

//  void QOpenGLFunctions_2_1::glNormal3i(GLint nx, GLint ny, GLint nz)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_110glNormal3iEiii(
    QOpenGLFunctions_2_1 *self,
    GLint nx,
    GLint ny,
    GLint nz) {
  self->glNormal3i(nx, ny, nz);
}

//  void QOpenGLFunctions_2_1::glNormal3f(GLfloat nx, GLfloat ny, GLfloat nz)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_110glNormal3fEfff(
    QOpenGLFunctions_2_1 *self,
    GLfloat nx,
    GLfloat ny,
    GLfloat nz) {
  self->glNormal3f(nx, ny, nz);
}

//  void QOpenGLFunctions_2_1::glNormal3d(GLdouble nx, GLdouble ny, GLdouble
//      nz)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_110glNormal3dEddd(
    QOpenGLFunctions_2_1 *self,
    GLdouble nx,
    GLdouble ny,
    GLdouble nz) {
  self->glNormal3d(nx, ny, nz);
}

//  void QOpenGLFunctions_2_1::glNormal3b(GLbyte nx, GLbyte ny, GLbyte nz)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_110glNormal3bEaaa(
    QOpenGLFunctions_2_1 *self,
    GLbyte nx,
    GLbyte ny,
    GLbyte nz) {
  self->glNormal3b(nx, ny, nz);
}

//  void QOpenGLFunctions_2_1::glIndexs(GLshort c)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_18glIndexsEs(
    QOpenGLFunctions_2_1 *self,
    GLshort c) {
  self->glIndexs(c);
}

//  void QOpenGLFunctions_2_1::glIndexi(GLint c)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_18glIndexiEi(
    QOpenGLFunctions_2_1 *self,
    GLint c) {
  self->glIndexi(c);
}

//  void QOpenGLFunctions_2_1::glIndexf(GLfloat c)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_18glIndexfEf(
    QOpenGLFunctions_2_1 *self,
    GLfloat c) {
  self->glIndexf(c);
}

//  void QOpenGLFunctions_2_1::glIndexd(GLdouble c)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_18glIndexdEd(
    QOpenGLFunctions_2_1 *self,
    GLdouble c) {
  self->glIndexd(c);
}

//  void QOpenGLFunctions_2_1::glEnd()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_15glEndEv(QOpenGLFunctions_2_1 *self) {
  self->glEnd();
}

//  void QOpenGLFunctions_2_1::glEdgeFlag(GLboolean flag)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_110glEdgeFlagEh(
    QOpenGLFunctions_2_1 *self,
    GLboolean flag) {
  self->glEdgeFlag(flag);
}

//  void QOpenGLFunctions_2_1::glColor4us(GLushort red, GLushort green,
//      GLushort blue, GLushort alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_110glColor4usEtttt(
    QOpenGLFunctions_2_1 *self,
    GLushort red,
    GLushort green,
    GLushort blue,
    GLushort alpha) {
  self->glColor4us(red, green, blue, alpha);
}

//  void QOpenGLFunctions_2_1::glColor4ui(GLuint red, GLuint green, GLuint
//      blue, GLuint alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_110glColor4uiEjjjj(
    QOpenGLFunctions_2_1 *self,
    GLuint red,
    GLuint green,
    GLuint blue,
    GLuint alpha) {
  self->glColor4ui(red, green, blue, alpha);
}

//  void QOpenGLFunctions_2_1::glColor4ub(GLubyte red, GLubyte green, GLubyte
//      blue, GLubyte alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_110glColor4ubEhhhh(
    QOpenGLFunctions_2_1 *self,
    GLubyte red,
    GLubyte green,
    GLubyte blue,
    GLubyte alpha) {
  self->glColor4ub(red, green, blue, alpha);
}

//  void QOpenGLFunctions_2_1::glColor4s(GLshort red, GLshort green, GLshort
//      blue, GLshort alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_19glColor4sEssss(
    QOpenGLFunctions_2_1 *self,
    GLshort red,
    GLshort green,
    GLshort blue,
    GLshort alpha) {
  self->glColor4s(red, green, blue, alpha);
}

//  void QOpenGLFunctions_2_1::glColor4i(GLint red, GLint green, GLint blue,
//      GLint alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_19glColor4iEiiii(
    QOpenGLFunctions_2_1 *self,
    GLint red,
    GLint green,
    GLint blue,
    GLint alpha) {
  self->glColor4i(red, green, blue, alpha);
}

//  void QOpenGLFunctions_2_1::glColor4f(GLfloat red, GLfloat green, GLfloat
//      blue, GLfloat alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_19glColor4fEffff(
    QOpenGLFunctions_2_1 *self,
    GLfloat red,
    GLfloat green,
    GLfloat blue,
    GLfloat alpha) {
  self->glColor4f(red, green, blue, alpha);
}

//  void QOpenGLFunctions_2_1::glColor4d(GLdouble red, GLdouble green,
//      GLdouble blue, GLdouble alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_19glColor4dEdddd(
    QOpenGLFunctions_2_1 *self,
    GLdouble red,
    GLdouble green,
    GLdouble blue,
    GLdouble alpha) {
  self->glColor4d(red, green, blue, alpha);
}

//  void QOpenGLFunctions_2_1::glColor4b(GLbyte red, GLbyte green, GLbyte
//      blue, GLbyte alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_19glColor4bEaaaa(
    QOpenGLFunctions_2_1 *self,
    GLbyte red,
    GLbyte green,
    GLbyte blue,
    GLbyte alpha) {
  self->glColor4b(red, green, blue, alpha);
}

//  void QOpenGLFunctions_2_1::glColor3us(GLushort red, GLushort green,
//      GLushort blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_110glColor3usEttt(
    QOpenGLFunctions_2_1 *self,
    GLushort red,
    GLushort green,
    GLushort blue) {
  self->glColor3us(red, green, blue);
}

//  void QOpenGLFunctions_2_1::glColor3ui(GLuint red, GLuint green, GLuint
//      blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_110glColor3uiEjjj(
    QOpenGLFunctions_2_1 *self,
    GLuint red,
    GLuint green,
    GLuint blue) {
  self->glColor3ui(red, green, blue);
}

//  void QOpenGLFunctions_2_1::glColor3ub(GLubyte red, GLubyte green, GLubyte
//      blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_110glColor3ubEhhh(
    QOpenGLFunctions_2_1 *self,
    GLubyte red,
    GLubyte green,
    GLubyte blue) {
  self->glColor3ub(red, green, blue);
}

//  void QOpenGLFunctions_2_1::glColor3s(GLshort red, GLshort green, GLshort
//      blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_19glColor3sEsss(
    QOpenGLFunctions_2_1 *self,
    GLshort red,
    GLshort green,
    GLshort blue) {
  self->glColor3s(red, green, blue);
}

//  void QOpenGLFunctions_2_1::glColor3i(GLint red, GLint green, GLint blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_19glColor3iEiii(
    QOpenGLFunctions_2_1 *self,
    GLint red,
    GLint green,
    GLint blue) {
  self->glColor3i(red, green, blue);
}

//  void QOpenGLFunctions_2_1::glColor3f(GLfloat red, GLfloat green, GLfloat
//      blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_19glColor3fEfff(
    QOpenGLFunctions_2_1 *self,
    GLfloat red,
    GLfloat green,
    GLfloat blue) {
  self->glColor3f(red, green, blue);
}

//  void QOpenGLFunctions_2_1::glColor3d(GLdouble red, GLdouble green,
//      GLdouble blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_19glColor3dEddd(
    QOpenGLFunctions_2_1 *self,
    GLdouble red,
    GLdouble green,
    GLdouble blue) {
  self->glColor3d(red, green, blue);
}

//  void QOpenGLFunctions_2_1::glColor3b(GLbyte red, GLbyte green, GLbyte
//      blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_19glColor3bEaaa(
    QOpenGLFunctions_2_1 *self,
    GLbyte red,
    GLbyte green,
    GLbyte blue) {
  self->glColor3b(red, green, blue);
}

//  void QOpenGLFunctions_2_1::glBegin(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_17glBeginEj(
    QOpenGLFunctions_2_1 *self,
    GLenum mode) {
  self->glBegin(mode);
}

//  void QOpenGLFunctions_2_1::glListBase(GLuint base)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_110glListBaseEj(
    QOpenGLFunctions_2_1 *self,
    GLuint base) {
  self->glListBase(base);
}

//  void QOpenGLFunctions_2_1::glDeleteLists(GLuint list, GLsizei range)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_113glDeleteListsEji(
    QOpenGLFunctions_2_1 *self,
    GLuint list,
    GLsizei range) {
  self->glDeleteLists(list, range);
}

//  void QOpenGLFunctions_2_1::glCallList(GLuint list)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_110glCallListEj(
    QOpenGLFunctions_2_1 *self,
    GLuint list) {
  self->glCallList(list);
}

//  void QOpenGLFunctions_2_1::glEndList()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_19glEndListEv(
    QOpenGLFunctions_2_1 *self) {
  self->glEndList();
}

//  void QOpenGLFunctions_2_1::glNewList(GLuint list, GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_19glNewListEjj(
    QOpenGLFunctions_2_1 *self,
    GLuint list,
    GLenum mode) {
  self->glNewList(list, mode);
}

//  void QOpenGLFunctions_2_1::glPushClientAttrib(GLbitfield mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_118glPushClientAttribEj(
    QOpenGLFunctions_2_1 *self,
    GLbitfield mask) {
  self->glPushClientAttrib(mask);
}

//  void QOpenGLFunctions_2_1::glPopClientAttrib()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_117glPopClientAttribEv(
    QOpenGLFunctions_2_1 *self) {
  self->glPopClientAttrib();
}

//  void QOpenGLFunctions_2_1::glEnableClientState(GLenum array)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_119glEnableClientStateEj(
    QOpenGLFunctions_2_1 *self,
    GLenum array) {
  self->glEnableClientState(array);
}

//  void QOpenGLFunctions_2_1::glDisableClientState(GLenum array)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_120glDisableClientStateEj(
    QOpenGLFunctions_2_1 *self,
    GLenum array) {
  self->glDisableClientState(array);
}

//  void QOpenGLFunctions_2_1::glArrayElement(GLint i)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_114glArrayElementEi(
    QOpenGLFunctions_2_1 *self,
    GLint i) {
  self->glArrayElement(i);
}

//  void QOpenGLFunctions_2_1::glResetMinmax(GLenum target)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_113glResetMinmaxEj(
    QOpenGLFunctions_2_1 *self,
    GLenum target) {
  self->glResetMinmax(target);
}

//  void QOpenGLFunctions_2_1::glResetHistogram(GLenum target)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_116glResetHistogramEj(
    QOpenGLFunctions_2_1 *self,
    GLenum target) {
  self->glResetHistogram(target);
}

//  void QOpenGLFunctions_2_1::glMinmax(GLenum target, GLenum internalformat,
//      GLboolean sink)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_18glMinmaxEjjh(
    QOpenGLFunctions_2_1 *self,
    GLenum target,
    GLenum internalformat,
    GLboolean sink) {
  self->glMinmax(target, internalformat, sink);
}

//  void QOpenGLFunctions_2_1::glHistogram(GLenum target, GLsizei width,
//      GLenum internalformat, GLboolean sink)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_111glHistogramEjijh(
    QOpenGLFunctions_2_1 *self,
    GLenum target,
    GLsizei width,
    GLenum internalformat,
    GLboolean sink) {
  self->glHistogram(target, width, internalformat, sink);
}

//  void QOpenGLFunctions_2_1::glCopyConvolutionFilter2D(GLenum target,
//      GLenum internalformat, GLint x, GLint y, GLsizei width, GLsizei
//      height)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_125glCopyConvolutionFilter2DEjjiiii(
    QOpenGLFunctions_2_1 *self,
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

//  void QOpenGLFunctions_2_1::glCopyConvolutionFilter1D(GLenum target,
//      GLenum internalformat, GLint x, GLint y, GLsizei width)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_125glCopyConvolutionFilter1DEjjiii(
    QOpenGLFunctions_2_1 *self,
    GLenum target,
    GLenum internalformat,
    GLint x,
    GLint y,
    GLsizei width) {
  self->glCopyConvolutionFilter1D(target, internalformat, x, y, width);
}

//  void QOpenGLFunctions_2_1::glConvolutionParameteri(GLenum target, GLenum
//      pname, GLint params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_123glConvolutionParameteriEjji(
    QOpenGLFunctions_2_1 *self,
    GLenum target,
    GLenum pname,
    GLint params) {
  self->glConvolutionParameteri(target, pname, params);
}

//  void QOpenGLFunctions_2_1::glConvolutionParameterf(GLenum target, GLenum
//      pname, GLfloat params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_123glConvolutionParameterfEjjf(
    QOpenGLFunctions_2_1 *self,
    GLenum target,
    GLenum pname,
    GLfloat params) {
  self->glConvolutionParameterf(target, pname, params);
}

//  void QOpenGLFunctions_2_1::glCopyColorSubTable(GLenum target, GLsizei
//      start, GLint x, GLint y, GLsizei width)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_119glCopyColorSubTableEjiiii(
    QOpenGLFunctions_2_1 *self,
    GLenum target,
    GLsizei start,
    GLint x,
    GLint y,
    GLsizei width) {
  self->glCopyColorSubTable(target, start, x, y, width);
}

//  void QOpenGLFunctions_2_1::glCopyColorTable(GLenum target, GLenum
//      internalformat, GLint x, GLint y, GLsizei width)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_116glCopyColorTableEjjiii(
    QOpenGLFunctions_2_1 *self,
    GLenum target,
    GLenum internalformat,
    GLint x,
    GLint y,
    GLsizei width) {
  self->glCopyColorTable(target, internalformat, x, y, width);
}

//  void QOpenGLFunctions_2_1::glMultiTexCoord4s(GLenum target, GLshort s,
//      GLshort t, GLshort r, GLshort q)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_117glMultiTexCoord4sEjssss(
    QOpenGLFunctions_2_1 *self,
    GLenum target,
    GLshort s,
    GLshort t,
    GLshort r,
    GLshort q) {
  self->glMultiTexCoord4s(target, s, t, r, q);
}

//  void QOpenGLFunctions_2_1::glMultiTexCoord4i(GLenum target, GLint s,
//      GLint t, GLint r, GLint q)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_117glMultiTexCoord4iEjiiii(
    QOpenGLFunctions_2_1 *self,
    GLenum target,
    GLint s,
    GLint t,
    GLint r,
    GLint q) {
  self->glMultiTexCoord4i(target, s, t, r, q);
}

//  void QOpenGLFunctions_2_1::glMultiTexCoord4f(GLenum target, GLfloat s,
//      GLfloat t, GLfloat r, GLfloat q)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_117glMultiTexCoord4fEjffff(
    QOpenGLFunctions_2_1 *self,
    GLenum target,
    GLfloat s,
    GLfloat t,
    GLfloat r,
    GLfloat q) {
  self->glMultiTexCoord4f(target, s, t, r, q);
}

//  void QOpenGLFunctions_2_1::glMultiTexCoord4d(GLenum target, GLdouble s,
//      GLdouble t, GLdouble r, GLdouble q)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_117glMultiTexCoord4dEjdddd(
    QOpenGLFunctions_2_1 *self,
    GLenum target,
    GLdouble s,
    GLdouble t,
    GLdouble r,
    GLdouble q) {
  self->glMultiTexCoord4d(target, s, t, r, q);
}

//  void QOpenGLFunctions_2_1::glMultiTexCoord3s(GLenum target, GLshort s,
//      GLshort t, GLshort r)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_117glMultiTexCoord3sEjsss(
    QOpenGLFunctions_2_1 *self,
    GLenum target,
    GLshort s,
    GLshort t,
    GLshort r) {
  self->glMultiTexCoord3s(target, s, t, r);
}

//  void QOpenGLFunctions_2_1::glMultiTexCoord3i(GLenum target, GLint s,
//      GLint t, GLint r)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_117glMultiTexCoord3iEjiii(
    QOpenGLFunctions_2_1 *self,
    GLenum target,
    GLint s,
    GLint t,
    GLint r) {
  self->glMultiTexCoord3i(target, s, t, r);
}

//  void QOpenGLFunctions_2_1::glMultiTexCoord3f(GLenum target, GLfloat s,
//      GLfloat t, GLfloat r)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_117glMultiTexCoord3fEjfff(
    QOpenGLFunctions_2_1 *self,
    GLenum target,
    GLfloat s,
    GLfloat t,
    GLfloat r) {
  self->glMultiTexCoord3f(target, s, t, r);
}

//  void QOpenGLFunctions_2_1::glMultiTexCoord3d(GLenum target, GLdouble s,
//      GLdouble t, GLdouble r)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_117glMultiTexCoord3dEjddd(
    QOpenGLFunctions_2_1 *self,
    GLenum target,
    GLdouble s,
    GLdouble t,
    GLdouble r) {
  self->glMultiTexCoord3d(target, s, t, r);
}

//  void QOpenGLFunctions_2_1::glMultiTexCoord2s(GLenum target, GLshort s,
//      GLshort t)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_117glMultiTexCoord2sEjss(
    QOpenGLFunctions_2_1 *self,
    GLenum target,
    GLshort s,
    GLshort t) {
  self->glMultiTexCoord2s(target, s, t);
}

//  void QOpenGLFunctions_2_1::glMultiTexCoord2i(GLenum target, GLint s,
//      GLint t)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_117glMultiTexCoord2iEjii(
    QOpenGLFunctions_2_1 *self,
    GLenum target,
    GLint s,
    GLint t) {
  self->glMultiTexCoord2i(target, s, t);
}

//  void QOpenGLFunctions_2_1::glMultiTexCoord2f(GLenum target, GLfloat s,
//      GLfloat t)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_117glMultiTexCoord2fEjff(
    QOpenGLFunctions_2_1 *self,
    GLenum target,
    GLfloat s,
    GLfloat t) {
  self->glMultiTexCoord2f(target, s, t);
}

//  void QOpenGLFunctions_2_1::glMultiTexCoord2d(GLenum target, GLdouble s,
//      GLdouble t)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_117glMultiTexCoord2dEjdd(
    QOpenGLFunctions_2_1 *self,
    GLenum target,
    GLdouble s,
    GLdouble t) {
  self->glMultiTexCoord2d(target, s, t);
}

//  void QOpenGLFunctions_2_1::glMultiTexCoord1s(GLenum target, GLshort s)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_117glMultiTexCoord1sEjs(
    QOpenGLFunctions_2_1 *self,
    GLenum target,
    GLshort s) {
  self->glMultiTexCoord1s(target, s);
}

//  void QOpenGLFunctions_2_1::glMultiTexCoord1i(GLenum target, GLint s)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_117glMultiTexCoord1iEji(
    QOpenGLFunctions_2_1 *self,
    GLenum target,
    GLint s) {
  self->glMultiTexCoord1i(target, s);
}

//  void QOpenGLFunctions_2_1::glMultiTexCoord1f(GLenum target, GLfloat s)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_117glMultiTexCoord1fEjf(
    QOpenGLFunctions_2_1 *self,
    GLenum target,
    GLfloat s) {
  self->glMultiTexCoord1f(target, s);
}

//  void QOpenGLFunctions_2_1::glMultiTexCoord1d(GLenum target, GLdouble s)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_117glMultiTexCoord1dEjd(
    QOpenGLFunctions_2_1 *self,
    GLenum target,
    GLdouble s) {
  self->glMultiTexCoord1d(target, s);
}

//  void QOpenGLFunctions_2_1::glClientActiveTexture(GLenum texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_121glClientActiveTextureEj(
    QOpenGLFunctions_2_1 *self,
    GLenum texture) {
  self->glClientActiveTexture(texture);
}

//  void QOpenGLFunctions_2_1::glWindowPos3s(GLshort x, GLshort y, GLshort z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_113glWindowPos3sEsss(
    QOpenGLFunctions_2_1 *self,
    GLshort x,
    GLshort y,
    GLshort z) {
  self->glWindowPos3s(x, y, z);
}

//  void QOpenGLFunctions_2_1::glWindowPos3i(GLint x, GLint y, GLint z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_113glWindowPos3iEiii(
    QOpenGLFunctions_2_1 *self,
    GLint x,
    GLint y,
    GLint z) {
  self->glWindowPos3i(x, y, z);
}

//  void QOpenGLFunctions_2_1::glWindowPos3f(GLfloat x, GLfloat y, GLfloat z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_113glWindowPos3fEfff(
    QOpenGLFunctions_2_1 *self,
    GLfloat x,
    GLfloat y,
    GLfloat z) {
  self->glWindowPos3f(x, y, z);
}

//  void QOpenGLFunctions_2_1::glWindowPos3d(GLdouble x, GLdouble y, GLdouble
//      z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_113glWindowPos3dEddd(
    QOpenGLFunctions_2_1 *self,
    GLdouble x,
    GLdouble y,
    GLdouble z) {
  self->glWindowPos3d(x, y, z);
}

//  void QOpenGLFunctions_2_1::glWindowPos2s(GLshort x, GLshort y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_113glWindowPos2sEss(
    QOpenGLFunctions_2_1 *self,
    GLshort x,
    GLshort y) {
  self->glWindowPos2s(x, y);
}

//  void QOpenGLFunctions_2_1::glWindowPos2i(GLint x, GLint y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_113glWindowPos2iEii(
    QOpenGLFunctions_2_1 *self,
    GLint x,
    GLint y) {
  self->glWindowPos2i(x, y);
}

//  void QOpenGLFunctions_2_1::glWindowPos2f(GLfloat x, GLfloat y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_113glWindowPos2fEff(
    QOpenGLFunctions_2_1 *self,
    GLfloat x,
    GLfloat y) {
  self->glWindowPos2f(x, y);
}

//  void QOpenGLFunctions_2_1::glWindowPos2d(GLdouble x, GLdouble y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_113glWindowPos2dEdd(
    QOpenGLFunctions_2_1 *self,
    GLdouble x,
    GLdouble y) {
  self->glWindowPos2d(x, y);
}

//  void QOpenGLFunctions_2_1::glSecondaryColor3us(GLushort red, GLushort
//      green, GLushort blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_119glSecondaryColor3usEttt(
    QOpenGLFunctions_2_1 *self,
    GLushort red,
    GLushort green,
    GLushort blue) {
  self->glSecondaryColor3us(red, green, blue);
}

//  void QOpenGLFunctions_2_1::glSecondaryColor3ui(GLuint red, GLuint green,
//      GLuint blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_119glSecondaryColor3uiEjjj(
    QOpenGLFunctions_2_1 *self,
    GLuint red,
    GLuint green,
    GLuint blue) {
  self->glSecondaryColor3ui(red, green, blue);
}

//  void QOpenGLFunctions_2_1::glSecondaryColor3ub(GLubyte red, GLubyte
//      green, GLubyte blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_119glSecondaryColor3ubEhhh(
    QOpenGLFunctions_2_1 *self,
    GLubyte red,
    GLubyte green,
    GLubyte blue) {
  self->glSecondaryColor3ub(red, green, blue);
}

//  void QOpenGLFunctions_2_1::glSecondaryColor3s(GLshort red, GLshort green,
//      GLshort blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_118glSecondaryColor3sEsss(
    QOpenGLFunctions_2_1 *self,
    GLshort red,
    GLshort green,
    GLshort blue) {
  self->glSecondaryColor3s(red, green, blue);
}

//  void QOpenGLFunctions_2_1::glSecondaryColor3i(GLint red, GLint green,
//      GLint blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_118glSecondaryColor3iEiii(
    QOpenGLFunctions_2_1 *self,
    GLint red,
    GLint green,
    GLint blue) {
  self->glSecondaryColor3i(red, green, blue);
}

//  void QOpenGLFunctions_2_1::glSecondaryColor3f(GLfloat red, GLfloat green,
//      GLfloat blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_118glSecondaryColor3fEfff(
    QOpenGLFunctions_2_1 *self,
    GLfloat red,
    GLfloat green,
    GLfloat blue) {
  self->glSecondaryColor3f(red, green, blue);
}

//  void QOpenGLFunctions_2_1::glSecondaryColor3d(GLdouble red, GLdouble
//      green, GLdouble blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_118glSecondaryColor3dEddd(
    QOpenGLFunctions_2_1 *self,
    GLdouble red,
    GLdouble green,
    GLdouble blue) {
  self->glSecondaryColor3d(red, green, blue);
}

//  void QOpenGLFunctions_2_1::glSecondaryColor3b(GLbyte red, GLbyte green,
//      GLbyte blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_118glSecondaryColor3bEaaa(
    QOpenGLFunctions_2_1 *self,
    GLbyte red,
    GLbyte green,
    GLbyte blue) {
  self->glSecondaryColor3b(red, green, blue);
}

//  void QOpenGLFunctions_2_1::glFogCoordd(GLdouble coord)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_111glFogCoorddEd(
    QOpenGLFunctions_2_1 *self,
    GLdouble coord) {
  self->glFogCoordd(coord);
}

//  void QOpenGLFunctions_2_1::glFogCoordf(GLfloat coord)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_111glFogCoordfEf(
    QOpenGLFunctions_2_1 *self,
    GLfloat coord) {
  self->glFogCoordf(coord);
}

//  void QOpenGLFunctions_2_1::glVertexAttrib4s(GLuint index, GLshort x,
//      GLshort y, GLshort z, GLshort w)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_116glVertexAttrib4sEjssss(
    QOpenGLFunctions_2_1 *self,
    GLuint index,
    GLshort x,
    GLshort y,
    GLshort z,
    GLshort w) {
  self->glVertexAttrib4s(index, x, y, z, w);
}

//  void QOpenGLFunctions_2_1::glVertexAttrib4f(GLuint index, GLfloat x,
//      GLfloat y, GLfloat z, GLfloat w)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_116glVertexAttrib4fEjffff(
    QOpenGLFunctions_2_1 *self,
    GLuint index,
    GLfloat x,
    GLfloat y,
    GLfloat z,
    GLfloat w) {
  self->glVertexAttrib4f(index, x, y, z, w);
}

//  void QOpenGLFunctions_2_1::glVertexAttrib4d(GLuint index, GLdouble x,
//      GLdouble y, GLdouble z, GLdouble w)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_116glVertexAttrib4dEjdddd(
    QOpenGLFunctions_2_1 *self,
    GLuint index,
    GLdouble x,
    GLdouble y,
    GLdouble z,
    GLdouble w) {
  self->glVertexAttrib4d(index, x, y, z, w);
}

//  void QOpenGLFunctions_2_1::glVertexAttrib4Nub(GLuint index, GLubyte x,
//      GLubyte y, GLubyte z, GLubyte w)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_118glVertexAttrib4NubEjhhhh(
    QOpenGLFunctions_2_1 *self,
    GLuint index,
    GLubyte x,
    GLubyte y,
    GLubyte z,
    GLubyte w) {
  self->glVertexAttrib4Nub(index, x, y, z, w);
}

//  void QOpenGLFunctions_2_1::glVertexAttrib3s(GLuint index, GLshort x,
//      GLshort y, GLshort z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_116glVertexAttrib3sEjsss(
    QOpenGLFunctions_2_1 *self,
    GLuint index,
    GLshort x,
    GLshort y,
    GLshort z) {
  self->glVertexAttrib3s(index, x, y, z);
}

//  void QOpenGLFunctions_2_1::glVertexAttrib3f(GLuint index, GLfloat x,
//      GLfloat y, GLfloat z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_116glVertexAttrib3fEjfff(
    QOpenGLFunctions_2_1 *self,
    GLuint index,
    GLfloat x,
    GLfloat y,
    GLfloat z) {
  self->glVertexAttrib3f(index, x, y, z);
}

//  void QOpenGLFunctions_2_1::glVertexAttrib3d(GLuint index, GLdouble x,
//      GLdouble y, GLdouble z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_116glVertexAttrib3dEjddd(
    QOpenGLFunctions_2_1 *self,
    GLuint index,
    GLdouble x,
    GLdouble y,
    GLdouble z) {
  self->glVertexAttrib3d(index, x, y, z);
}

//  void QOpenGLFunctions_2_1::glVertexAttrib2s(GLuint index, GLshort x,
//      GLshort y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_116glVertexAttrib2sEjss(
    QOpenGLFunctions_2_1 *self,
    GLuint index,
    GLshort x,
    GLshort y) {
  self->glVertexAttrib2s(index, x, y);
}

//  void QOpenGLFunctions_2_1::glVertexAttrib2f(GLuint index, GLfloat x,
//      GLfloat y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_116glVertexAttrib2fEjff(
    QOpenGLFunctions_2_1 *self,
    GLuint index,
    GLfloat x,
    GLfloat y) {
  self->glVertexAttrib2f(index, x, y);
}

//  void QOpenGLFunctions_2_1::glVertexAttrib2d(GLuint index, GLdouble x,
//      GLdouble y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_116glVertexAttrib2dEjdd(
    QOpenGLFunctions_2_1 *self,
    GLuint index,
    GLdouble x,
    GLdouble y) {
  self->glVertexAttrib2d(index, x, y);
}

//  void QOpenGLFunctions_2_1::glVertexAttrib1s(GLuint index, GLshort x)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_116glVertexAttrib1sEjs(
    QOpenGLFunctions_2_1 *self,
    GLuint index,
    GLshort x) {
  self->glVertexAttrib1s(index, x);
}

//  void QOpenGLFunctions_2_1::glVertexAttrib1f(GLuint index, GLfloat x)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_116glVertexAttrib1fEjf(
    QOpenGLFunctions_2_1 *self,
    GLuint index,
    GLfloat x) {
  self->glVertexAttrib1f(index, x);
}

//  void QOpenGLFunctions_2_1::glVertexAttrib1d(GLuint index, GLdouble x)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_116glVertexAttrib1dEjd(
    QOpenGLFunctions_2_1 *self,
    GLuint index,
    GLdouble x) {
  self->glVertexAttrib1d(index, x);
}

//  bool QOpenGLFunctions_2_1::isContextCompatible(QOpenGLContext *context)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QOpenGLFunctions_2_119isContextCompatibleEP14QOpenGLContext(
    QOpenGLContext *context) {
  return QOpenGLFunctions_2_1::isContextCompatible(context);
}

//  QOpenGLVersionProfile QOpenGLFunctions_2_1::versionProfile()
extern "C" Q_DECL_EXPORT
QOpenGLVersionProfile *ritual_ZN20QOpenGLFunctions_2_114versionProfileEv() {
  return new QOpenGLVersionProfile(QOpenGLFunctions_2_1::versionProfile());
}

//  a Python function taken by a CuteQOpenGLFunctions_2_1, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QOpenGLFunctions_2_1(
    QOpenGLFunctions_2_1 *self,
    const char *key,
    void *call) {
  return static_cast<CuteQOpenGLFunctions_2_1 *>(self)->take(key, call);
}

//  bool QOpenGLFunctions_2_1::initializeOpenGLFunctions()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN20QOpenGLFunctions_2_125initializeOpenGLFunctionsEv(
    QOpenGLFunctions_2_1 *self) {
  return self->QOpenGLFunctions_2_1::initializeOpenGLFunctions();
}

#endif  // !defined(QT_NO_OPENGL) && !QT_CONFIG(opengles2)
