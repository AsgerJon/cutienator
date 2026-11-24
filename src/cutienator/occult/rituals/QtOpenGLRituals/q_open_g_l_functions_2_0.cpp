//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/qopenglfunctions_2_0.h, Qt 6.12.0. Changes made here are lost.
#include <QtOpenGL/qtopenglglobal.h>
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

//  void QOpenGLFunctions_2_0::glIndexub(GLubyte c)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_09glIndexubEh(
    QOpenGLFunctions_2_0 *self,
    GLubyte c) {
  self->glIndexub(c);
}

//  void QOpenGLFunctions_2_0::glBindTexture(GLenum target, GLuint texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glBindTextureEjj(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLuint texture) {
  self->glBindTexture(target, texture);
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

//  void QOpenGLFunctions_2_0::glPointParameteri(GLenum pname, GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_017glPointParameteriEji(
    QOpenGLFunctions_2_0 *self,
    GLenum pname,
    GLint param) {
  self->glPointParameteri(pname, param);
}

//  void QOpenGLFunctions_2_0::glPointParameterf(GLenum pname, GLfloat param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_017glPointParameterfEjf(
    QOpenGLFunctions_2_0 *self,
    GLenum pname,
    GLfloat param) {
  self->glPointParameterf(pname, param);
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

//  void QOpenGLFunctions_2_0::glBindBuffer(GLenum target, GLuint buffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glBindBufferEjj(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLuint buffer) {
  self->glBindBuffer(target, buffer);
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

//  void QOpenGLFunctions_2_0::glValidateProgram(GLuint program)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_017glValidateProgramEj(
    QOpenGLFunctions_2_0 *self,
    GLuint program) {
  self->glValidateProgram(program);
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

//  void QOpenGLFunctions_2_0::glLinkProgram(GLuint program)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glLinkProgramEj(
    QOpenGLFunctions_2_0 *self,
    GLuint program) {
  self->glLinkProgram(program);
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

//  void QOpenGLFunctions_2_0::glCompileShader(GLuint shader)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_015glCompileShaderEj(
    QOpenGLFunctions_2_0 *self,
    GLuint shader) {
  self->glCompileShader(shader);
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

//  void QOpenGLFunctions_2_0::glMatrixMode(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glMatrixModeEj(
    QOpenGLFunctions_2_0 *self,
    GLenum mode) {
  self->glMatrixMode(mode);
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

//  void QOpenGLFunctions_2_0::glEvalCoord2f(GLfloat u, GLfloat v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glEvalCoord2fEff(
    QOpenGLFunctions_2_0 *self,
    GLfloat u,
    GLfloat v) {
  self->glEvalCoord2f(u, v);
}

//  void QOpenGLFunctions_2_0::glEvalCoord2d(GLdouble u, GLdouble v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glEvalCoord2dEdd(
    QOpenGLFunctions_2_0 *self,
    GLdouble u,
    GLdouble v) {
  self->glEvalCoord2d(u, v);
}

//  void QOpenGLFunctions_2_0::glEvalCoord1f(GLfloat u)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glEvalCoord1fEf(
    QOpenGLFunctions_2_0 *self,
    GLfloat u) {
  self->glEvalCoord1f(u);
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

//  void QOpenGLFunctions_2_0::glLightModeli(GLenum pname, GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glLightModeliEji(
    QOpenGLFunctions_2_0 *self,
    GLenum pname,
    GLint param) {
  self->glLightModeli(pname, param);
}

//  void QOpenGLFunctions_2_0::glLightModelf(GLenum pname, GLfloat param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glLightModelfEjf(
    QOpenGLFunctions_2_0 *self,
    GLenum pname,
    GLfloat param) {
  self->glLightModelf(pname, param);
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

//  void QOpenGLFunctions_2_0::glFogi(GLenum pname, GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_06glFogiEji(
    QOpenGLFunctions_2_0 *self,
    GLenum pname,
    GLint param) {
  self->glFogi(pname, param);
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

//  void QOpenGLFunctions_2_0::glVertex3s(GLshort x, GLshort y, GLshort z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_010glVertex3sEsss(
    QOpenGLFunctions_2_0 *self,
    GLshort x,
    GLshort y,
    GLshort z) {
  self->glVertex3s(x, y, z);
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

//  void QOpenGLFunctions_2_0::glVertex3f(GLfloat x, GLfloat y, GLfloat z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_010glVertex3fEfff(
    QOpenGLFunctions_2_0 *self,
    GLfloat x,
    GLfloat y,
    GLfloat z) {
  self->glVertex3f(x, y, z);
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

//  void QOpenGLFunctions_2_0::glVertex2s(GLshort x, GLshort y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_010glVertex2sEss(
    QOpenGLFunctions_2_0 *self,
    GLshort x,
    GLshort y) {
  self->glVertex2s(x, y);
}

//  void QOpenGLFunctions_2_0::glVertex2i(GLint x, GLint y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_010glVertex2iEii(
    QOpenGLFunctions_2_0 *self,
    GLint x,
    GLint y) {
  self->glVertex2i(x, y);
}

//  void QOpenGLFunctions_2_0::glVertex2f(GLfloat x, GLfloat y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_010glVertex2fEff(
    QOpenGLFunctions_2_0 *self,
    GLfloat x,
    GLfloat y) {
  self->glVertex2f(x, y);
}

//  void QOpenGLFunctions_2_0::glVertex2d(GLdouble x, GLdouble y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_010glVertex2dEdd(
    QOpenGLFunctions_2_0 *self,
    GLdouble x,
    GLdouble y) {
  self->glVertex2d(x, y);
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

//  void QOpenGLFunctions_2_0::glTexCoord3s(GLshort s, GLshort t, GLshort r)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glTexCoord3sEsss(
    QOpenGLFunctions_2_0 *self,
    GLshort s,
    GLshort t,
    GLshort r) {
  self->glTexCoord3s(s, t, r);
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

//  void QOpenGLFunctions_2_0::glTexCoord3f(GLfloat s, GLfloat t, GLfloat r)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glTexCoord3fEfff(
    QOpenGLFunctions_2_0 *self,
    GLfloat s,
    GLfloat t,
    GLfloat r) {
  self->glTexCoord3f(s, t, r);
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

//  void QOpenGLFunctions_2_0::glTexCoord2s(GLshort s, GLshort t)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glTexCoord2sEss(
    QOpenGLFunctions_2_0 *self,
    GLshort s,
    GLshort t) {
  self->glTexCoord2s(s, t);
}

//  void QOpenGLFunctions_2_0::glTexCoord2i(GLint s, GLint t)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glTexCoord2iEii(
    QOpenGLFunctions_2_0 *self,
    GLint s,
    GLint t) {
  self->glTexCoord2i(s, t);
}

//  void QOpenGLFunctions_2_0::glTexCoord2f(GLfloat s, GLfloat t)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glTexCoord2fEff(
    QOpenGLFunctions_2_0 *self,
    GLfloat s,
    GLfloat t) {
  self->glTexCoord2f(s, t);
}

//  void QOpenGLFunctions_2_0::glTexCoord2d(GLdouble s, GLdouble t)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glTexCoord2dEdd(
    QOpenGLFunctions_2_0 *self,
    GLdouble s,
    GLdouble t) {
  self->glTexCoord2d(s, t);
}

//  void QOpenGLFunctions_2_0::glTexCoord1s(GLshort s)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glTexCoord1sEs(
    QOpenGLFunctions_2_0 *self,
    GLshort s) {
  self->glTexCoord1s(s);
}

//  void QOpenGLFunctions_2_0::glTexCoord1i(GLint s)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glTexCoord1iEi(
    QOpenGLFunctions_2_0 *self,
    GLint s) {
  self->glTexCoord1i(s);
}

//  void QOpenGLFunctions_2_0::glTexCoord1f(GLfloat s)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glTexCoord1fEf(
    QOpenGLFunctions_2_0 *self,
    GLfloat s) {
  self->glTexCoord1f(s);
}

//  void QOpenGLFunctions_2_0::glTexCoord1d(GLdouble s)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_012glTexCoord1dEd(
    QOpenGLFunctions_2_0 *self,
    GLdouble s) {
  self->glTexCoord1d(s);
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

//  void QOpenGLFunctions_2_0::glRasterPos3s(GLshort x, GLshort y, GLshort z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glRasterPos3sEsss(
    QOpenGLFunctions_2_0 *self,
    GLshort x,
    GLshort y,
    GLshort z) {
  self->glRasterPos3s(x, y, z);
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

//  void QOpenGLFunctions_2_0::glRasterPos3f(GLfloat x, GLfloat y, GLfloat z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glRasterPos3fEfff(
    QOpenGLFunctions_2_0 *self,
    GLfloat x,
    GLfloat y,
    GLfloat z) {
  self->glRasterPos3f(x, y, z);
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

//  void QOpenGLFunctions_2_0::glRasterPos2s(GLshort x, GLshort y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glRasterPos2sEss(
    QOpenGLFunctions_2_0 *self,
    GLshort x,
    GLshort y) {
  self->glRasterPos2s(x, y);
}

//  void QOpenGLFunctions_2_0::glRasterPos2i(GLint x, GLint y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glRasterPos2iEii(
    QOpenGLFunctions_2_0 *self,
    GLint x,
    GLint y) {
  self->glRasterPos2i(x, y);
}

//  void QOpenGLFunctions_2_0::glRasterPos2f(GLfloat x, GLfloat y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glRasterPos2fEff(
    QOpenGLFunctions_2_0 *self,
    GLfloat x,
    GLfloat y) {
  self->glRasterPos2f(x, y);
}

//  void QOpenGLFunctions_2_0::glRasterPos2d(GLdouble x, GLdouble y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glRasterPos2dEdd(
    QOpenGLFunctions_2_0 *self,
    GLdouble x,
    GLdouble y) {
  self->glRasterPos2d(x, y);
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

//  void QOpenGLFunctions_2_0::glNormal3i(GLint nx, GLint ny, GLint nz)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_010glNormal3iEiii(
    QOpenGLFunctions_2_0 *self,
    GLint nx,
    GLint ny,
    GLint nz) {
  self->glNormal3i(nx, ny, nz);
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

//  void QOpenGLFunctions_2_0::glNormal3b(GLbyte nx, GLbyte ny, GLbyte nz)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_010glNormal3bEaaa(
    QOpenGLFunctions_2_0 *self,
    GLbyte nx,
    GLbyte ny,
    GLbyte nz) {
  self->glNormal3b(nx, ny, nz);
}

//  void QOpenGLFunctions_2_0::glIndexs(GLshort c)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_08glIndexsEs(
    QOpenGLFunctions_2_0 *self,
    GLshort c) {
  self->glIndexs(c);
}

//  void QOpenGLFunctions_2_0::glIndexi(GLint c)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_08glIndexiEi(
    QOpenGLFunctions_2_0 *self,
    GLint c) {
  self->glIndexi(c);
}

//  void QOpenGLFunctions_2_0::glIndexf(GLfloat c)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_08glIndexfEf(
    QOpenGLFunctions_2_0 *self,
    GLfloat c) {
  self->glIndexf(c);
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

//  void QOpenGLFunctions_2_0::glEdgeFlag(GLboolean flag)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_010glEdgeFlagEh(
    QOpenGLFunctions_2_0 *self,
    GLboolean flag) {
  self->glEdgeFlag(flag);
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

//  void QOpenGLFunctions_2_0::glColor3i(GLint red, GLint green, GLint blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_09glColor3iEiii(
    QOpenGLFunctions_2_0 *self,
    GLint red,
    GLint green,
    GLint blue) {
  self->glColor3i(red, green, blue);
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

//  void QOpenGLFunctions_2_0::glDeleteLists(GLuint list, GLsizei range)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glDeleteListsEji(
    QOpenGLFunctions_2_0 *self,
    GLuint list,
    GLsizei range) {
  self->glDeleteLists(list, range);
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

//  void QOpenGLFunctions_2_0::glEnableClientState(GLenum array)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_019glEnableClientStateEj(
    QOpenGLFunctions_2_0 *self,
    GLenum array) {
  self->glEnableClientState(array);
}

//  void QOpenGLFunctions_2_0::glDisableClientState(GLenum array)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_020glDisableClientStateEj(
    QOpenGLFunctions_2_0 *self,
    GLenum array) {
  self->glDisableClientState(array);
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

//  void QOpenGLFunctions_2_0::glMultiTexCoord1s(GLenum target, GLshort s)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_017glMultiTexCoord1sEjs(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLshort s) {
  self->glMultiTexCoord1s(target, s);
}

//  void QOpenGLFunctions_2_0::glMultiTexCoord1i(GLenum target, GLint s)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_017glMultiTexCoord1iEji(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLint s) {
  self->glMultiTexCoord1i(target, s);
}

//  void QOpenGLFunctions_2_0::glMultiTexCoord1f(GLenum target, GLfloat s)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_017glMultiTexCoord1fEjf(
    QOpenGLFunctions_2_0 *self,
    GLenum target,
    GLfloat s) {
  self->glMultiTexCoord1f(target, s);
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

//  void QOpenGLFunctions_2_0::glWindowPos3s(GLshort x, GLshort y, GLshort z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glWindowPos3sEsss(
    QOpenGLFunctions_2_0 *self,
    GLshort x,
    GLshort y,
    GLshort z) {
  self->glWindowPos3s(x, y, z);
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

//  void QOpenGLFunctions_2_0::glWindowPos3f(GLfloat x, GLfloat y, GLfloat z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glWindowPos3fEfff(
    QOpenGLFunctions_2_0 *self,
    GLfloat x,
    GLfloat y,
    GLfloat z) {
  self->glWindowPos3f(x, y, z);
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

//  void QOpenGLFunctions_2_0::glWindowPos2s(GLshort x, GLshort y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glWindowPos2sEss(
    QOpenGLFunctions_2_0 *self,
    GLshort x,
    GLshort y) {
  self->glWindowPos2s(x, y);
}

//  void QOpenGLFunctions_2_0::glWindowPos2i(GLint x, GLint y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glWindowPos2iEii(
    QOpenGLFunctions_2_0 *self,
    GLint x,
    GLint y) {
  self->glWindowPos2i(x, y);
}

//  void QOpenGLFunctions_2_0::glWindowPos2f(GLfloat x, GLfloat y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glWindowPos2fEff(
    QOpenGLFunctions_2_0 *self,
    GLfloat x,
    GLfloat y) {
  self->glWindowPos2f(x, y);
}

//  void QOpenGLFunctions_2_0::glWindowPos2d(GLdouble x, GLdouble y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_013glWindowPos2dEdd(
    QOpenGLFunctions_2_0 *self,
    GLdouble x,
    GLdouble y) {
  self->glWindowPos2d(x, y);
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

//  void QOpenGLFunctions_2_0::glFogCoordd(GLdouble coord)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_011glFogCoorddEd(
    QOpenGLFunctions_2_0 *self,
    GLdouble coord) {
  self->glFogCoordd(coord);
}

//  void QOpenGLFunctions_2_0::glFogCoordf(GLfloat coord)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_011glFogCoordfEf(
    QOpenGLFunctions_2_0 *self,
    GLfloat coord) {
  self->glFogCoordf(coord);
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

//  void QOpenGLFunctions_2_0::glVertexAttrib1s(GLuint index, GLshort x)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_016glVertexAttrib1sEjs(
    QOpenGLFunctions_2_0 *self,
    GLuint index,
    GLshort x) {
  self->glVertexAttrib1s(index, x);
}

//  void QOpenGLFunctions_2_0::glVertexAttrib1f(GLuint index, GLfloat x)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_2_016glVertexAttrib1fEjf(
    QOpenGLFunctions_2_0 *self,
    GLuint index,
    GLfloat x) {
  self->glVertexAttrib1f(index, x);
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
