//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/qopenglfunctions_3_2_core.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtOpenGL/qtopenglglobal.h>
#if !defined(QT_NO_OPENGL) && !QT_CONFIG(opengles2)
#include <QtOpenGL/QtOpenGL>
#include <QtOpenGL/qopenglfunctions_3_2_core.h>
#include <QtOpenGL/qopenglversionprofile.h>
#include <cstring>

//  A QOpenGLFunctions_3_2_Core that Python can take functions over in. Every QOpenGLFunctions_3_2_Core
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL) && !QT_CONFIG(opengles2)
typedef bool (*CuteQOpenGLFunctions_3_2_CoreCall0)(const void *, int *);
#endif  // !defined(QT_NO_OPENGL) && !QT_CONFIG(opengles2)
#endif  // !defined(QT_NO_OPENGL)
class CuteQOpenGLFunctions_3_2_Core : public QOpenGLFunctions_3_2_Core {
public:
  using QOpenGLFunctions_3_2_Core::QOpenGLFunctions_3_2_Core;
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
  //  bool QOpenGLFunctions_3_2_Core::initializeOpenGLFunctions()
  bool initializeOpenGLFunctions() override {
    if (taken[0]) {
      int handled = 0;
      CuteQOpenGLFunctions_3_2_CoreCall0 call = reinterpret_cast<CuteQOpenGLFunctions_3_2_CoreCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QOpenGLFunctions_3_2_Core::initializeOpenGLFunctions();
  }
#endif  // !defined(QT_NO_OPENGL) && !QT_CONFIG(opengles2)
#endif  // !defined(QT_NO_OPENGL)
};

//  QOpenGLFunctions_3_2_Core::QOpenGLFunctions_3_2_Core()
extern "C" Q_DECL_EXPORT
QOpenGLFunctions_3_2_Core *ritual_ZN25QOpenGLFunctions_3_2_CoreC1Ev() {
  return new CuteQOpenGLFunctions_3_2_Core();
}

//  QOpenGLFunctions_3_2_Core::~QOpenGLFunctions_3_2_Core()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_CoreD1Ev(
    QOpenGLFunctions_3_2_Core *self) {
  delete self;
}

//  bool QOpenGLFunctions_3_2_Core::initializeOpenGLFunctions()
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QOpenGLFunctions_3_2_Core25initializeOpenGLFunctionsEv(
    QOpenGLFunctions_3_2_Core *self) {
  return self->initializeOpenGLFunctions();
}

//  void QOpenGLFunctions_3_2_Core::glViewport(GLint x, GLint y, GLsizei
//      width, GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core10glViewportEiiii(
    QOpenGLFunctions_3_2_Core *self,
    GLint x,
    GLint y,
    GLsizei width,
    GLsizei height) {
  self->glViewport(x, y, width, height);
}

//  void QOpenGLFunctions_3_2_Core::glDepthRange(GLdouble nearVal, GLdouble
//      farVal)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core12glDepthRangeEdd(
    QOpenGLFunctions_3_2_Core *self,
    GLdouble nearVal,
    GLdouble farVal) {
  self->glDepthRange(nearVal, farVal);
}

//  void QOpenGLFunctions_3_2_Core::glReadBuffer(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core12glReadBufferEj(
    QOpenGLFunctions_3_2_Core *self,
    GLenum mode) {
  self->glReadBuffer(mode);
}

//  void QOpenGLFunctions_3_2_Core::glPixelStorei(GLenum pname, GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core13glPixelStoreiEji(
    QOpenGLFunctions_3_2_Core *self,
    GLenum pname,
    GLint param) {
  self->glPixelStorei(pname, param);
}

//  void QOpenGLFunctions_3_2_Core::glPixelStoref(GLenum pname, GLfloat
//      param)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core13glPixelStorefEjf(
    QOpenGLFunctions_3_2_Core *self,
    GLenum pname,
    GLfloat param) {
  self->glPixelStoref(pname, param);
}

//  void QOpenGLFunctions_3_2_Core::glDepthFunc(GLenum func)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core11glDepthFuncEj(
    QOpenGLFunctions_3_2_Core *self,
    GLenum func) {
  self->glDepthFunc(func);
}

//  void QOpenGLFunctions_3_2_Core::glStencilOp(GLenum fail, GLenum zfail,
//      GLenum zpass)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core11glStencilOpEjjj(
    QOpenGLFunctions_3_2_Core *self,
    GLenum fail,
    GLenum zfail,
    GLenum zpass) {
  self->glStencilOp(fail, zfail, zpass);
}

//  void QOpenGLFunctions_3_2_Core::glStencilFunc(GLenum func, GLint ref,
//      GLuint mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core13glStencilFuncEjij(
    QOpenGLFunctions_3_2_Core *self,
    GLenum func,
    GLint ref,
    GLuint mask) {
  self->glStencilFunc(func, ref, mask);
}

//  void QOpenGLFunctions_3_2_Core::glLogicOp(GLenum opcode)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core9glLogicOpEj(
    QOpenGLFunctions_3_2_Core *self,
    GLenum opcode) {
  self->glLogicOp(opcode);
}

//  void QOpenGLFunctions_3_2_Core::glBlendFunc(GLenum sfactor, GLenum
//      dfactor)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core11glBlendFuncEjj(
    QOpenGLFunctions_3_2_Core *self,
    GLenum sfactor,
    GLenum dfactor) {
  self->glBlendFunc(sfactor, dfactor);
}

//  void QOpenGLFunctions_3_2_Core::glFlush()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core7glFlushEv(
    QOpenGLFunctions_3_2_Core *self) {
  self->glFlush();
}

//  void QOpenGLFunctions_3_2_Core::glFinish()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core8glFinishEv(
    QOpenGLFunctions_3_2_Core *self) {
  self->glFinish();
}

//  void QOpenGLFunctions_3_2_Core::glEnable(GLenum cap)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core8glEnableEj(
    QOpenGLFunctions_3_2_Core *self,
    GLenum cap) {
  self->glEnable(cap);
}

//  void QOpenGLFunctions_3_2_Core::glDisable(GLenum cap)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core9glDisableEj(
    QOpenGLFunctions_3_2_Core *self,
    GLenum cap) {
  self->glDisable(cap);
}

//  void QOpenGLFunctions_3_2_Core::glDepthMask(GLboolean flag)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core11glDepthMaskEh(
    QOpenGLFunctions_3_2_Core *self,
    GLboolean flag) {
  self->glDepthMask(flag);
}

//  void QOpenGLFunctions_3_2_Core::glColorMask(GLboolean red, GLboolean
//      green, GLboolean blue, GLboolean alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core11glColorMaskEhhhh(
    QOpenGLFunctions_3_2_Core *self,
    GLboolean red,
    GLboolean green,
    GLboolean blue,
    GLboolean alpha) {
  self->glColorMask(red, green, blue, alpha);
}

//  void QOpenGLFunctions_3_2_Core::glStencilMask(GLuint mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core13glStencilMaskEj(
    QOpenGLFunctions_3_2_Core *self,
    GLuint mask) {
  self->glStencilMask(mask);
}

//  void QOpenGLFunctions_3_2_Core::glClearDepth(GLdouble depth)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core12glClearDepthEd(
    QOpenGLFunctions_3_2_Core *self,
    GLdouble depth) {
  self->glClearDepth(depth);
}

//  void QOpenGLFunctions_3_2_Core::glClearStencil(GLint s)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core14glClearStencilEi(
    QOpenGLFunctions_3_2_Core *self,
    GLint s) {
  self->glClearStencil(s);
}

//  void QOpenGLFunctions_3_2_Core::glClearColor(GLfloat red, GLfloat green,
//      GLfloat blue, GLfloat alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core12glClearColorEffff(
    QOpenGLFunctions_3_2_Core *self,
    GLfloat red,
    GLfloat green,
    GLfloat blue,
    GLfloat alpha) {
  self->glClearColor(red, green, blue, alpha);
}

//  void QOpenGLFunctions_3_2_Core::glClear(GLbitfield mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core7glClearEj(
    QOpenGLFunctions_3_2_Core *self,
    GLbitfield mask) {
  self->glClear(mask);
}

//  void QOpenGLFunctions_3_2_Core::glDrawBuffer(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core12glDrawBufferEj(
    QOpenGLFunctions_3_2_Core *self,
    GLenum mode) {
  self->glDrawBuffer(mode);
}

//  void QOpenGLFunctions_3_2_Core::glTexParameteri(GLenum target, GLenum
//      pname, GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core15glTexParameteriEjji(
    QOpenGLFunctions_3_2_Core *self,
    GLenum target,
    GLenum pname,
    GLint param) {
  self->glTexParameteri(target, pname, param);
}

//  void QOpenGLFunctions_3_2_Core::glTexParameterf(GLenum target, GLenum
//      pname, GLfloat param)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core15glTexParameterfEjjf(
    QOpenGLFunctions_3_2_Core *self,
    GLenum target,
    GLenum pname,
    GLfloat param) {
  self->glTexParameterf(target, pname, param);
}

//  void QOpenGLFunctions_3_2_Core::glScissor(GLint x, GLint y, GLsizei
//      width, GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core9glScissorEiiii(
    QOpenGLFunctions_3_2_Core *self,
    GLint x,
    GLint y,
    GLsizei width,
    GLsizei height) {
  self->glScissor(x, y, width, height);
}

//  void QOpenGLFunctions_3_2_Core::glPolygonMode(GLenum face, GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core13glPolygonModeEjj(
    QOpenGLFunctions_3_2_Core *self,
    GLenum face,
    GLenum mode) {
  self->glPolygonMode(face, mode);
}

//  void QOpenGLFunctions_3_2_Core::glPointSize(GLfloat size)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core11glPointSizeEf(
    QOpenGLFunctions_3_2_Core *self,
    GLfloat size) {
  self->glPointSize(size);
}

//  void QOpenGLFunctions_3_2_Core::glLineWidth(GLfloat width)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core11glLineWidthEf(
    QOpenGLFunctions_3_2_Core *self,
    GLfloat width) {
  self->glLineWidth(width);
}

//  void QOpenGLFunctions_3_2_Core::glHint(GLenum target, GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core6glHintEjj(
    QOpenGLFunctions_3_2_Core *self,
    GLenum target,
    GLenum mode) {
  self->glHint(target, mode);
}

//  void QOpenGLFunctions_3_2_Core::glFrontFace(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core11glFrontFaceEj(
    QOpenGLFunctions_3_2_Core *self,
    GLenum mode) {
  self->glFrontFace(mode);
}

//  void QOpenGLFunctions_3_2_Core::glCullFace(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core10glCullFaceEj(
    QOpenGLFunctions_3_2_Core *self,
    GLenum mode) {
  self->glCullFace(mode);
}

//  void QOpenGLFunctions_3_2_Core::glBindTexture(GLenum target, GLuint
//      texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core13glBindTextureEjj(
    QOpenGLFunctions_3_2_Core *self,
    GLenum target,
    GLuint texture) {
  self->glBindTexture(target, texture);
}

//  void QOpenGLFunctions_3_2_Core::glCopyTexSubImage2D(GLenum target, GLint
//      level, GLint xoffset, GLint yoffset, GLint x, GLint y, GLsizei width,
//      GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core19glCopyTexSubImage2DEjiiiiiii(
    QOpenGLFunctions_3_2_Core *self,
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

//  void QOpenGLFunctions_3_2_Core::glCopyTexSubImage1D(GLenum target, GLint
//      level, GLint xoffset, GLint x, GLint y, GLsizei width)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core19glCopyTexSubImage1DEjiiiii(
    QOpenGLFunctions_3_2_Core *self,
    GLenum target,
    GLint level,
    GLint xoffset,
    GLint x,
    GLint y,
    GLsizei width) {
  self->glCopyTexSubImage1D(target, level, xoffset, x, y, width);
}

//  void QOpenGLFunctions_3_2_Core::glCopyTexImage2D(GLenum target, GLint
//      level, GLenum internalformat, GLint x, GLint y, GLsizei width,
//      GLsizei height, GLint border)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core16glCopyTexImage2DEjijiiiii(
    QOpenGLFunctions_3_2_Core *self,
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

//  void QOpenGLFunctions_3_2_Core::glCopyTexImage1D(GLenum target, GLint
//      level, GLenum internalformat, GLint x, GLint y, GLsizei width, GLint
//      border)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core16glCopyTexImage1DEjijiiii(
    QOpenGLFunctions_3_2_Core *self,
    GLenum target,
    GLint level,
    GLenum internalformat,
    GLint x,
    GLint y,
    GLsizei width,
    GLint border) {
  self->glCopyTexImage1D(target, level, internalformat, x, y, width, border);
}

//  void QOpenGLFunctions_3_2_Core::glPolygonOffset(GLfloat factor, GLfloat
//      units)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core15glPolygonOffsetEff(
    QOpenGLFunctions_3_2_Core *self,
    GLfloat factor,
    GLfloat units) {
  self->glPolygonOffset(factor, units);
}

//  void QOpenGLFunctions_3_2_Core::glDrawArrays(GLenum mode, GLint first,
//      GLsizei count)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core12glDrawArraysEjii(
    QOpenGLFunctions_3_2_Core *self,
    GLenum mode,
    GLint first,
    GLsizei count) {
  self->glDrawArrays(mode, first, count);
}

//  void QOpenGLFunctions_3_2_Core::glCopyTexSubImage3D(GLenum target, GLint
//      level, GLint xoffset, GLint yoffset, GLint zoffset, GLint x, GLint y,
//      GLsizei width, GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core19glCopyTexSubImage3DEjiiiiiiii(
    QOpenGLFunctions_3_2_Core *self,
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

//  void QOpenGLFunctions_3_2_Core::glBlendEquation(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core15glBlendEquationEj(
    QOpenGLFunctions_3_2_Core *self,
    GLenum mode) {
  self->glBlendEquation(mode);
}

//  void QOpenGLFunctions_3_2_Core::glBlendColor(GLfloat red, GLfloat green,
//      GLfloat blue, GLfloat alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core12glBlendColorEffff(
    QOpenGLFunctions_3_2_Core *self,
    GLfloat red,
    GLfloat green,
    GLfloat blue,
    GLfloat alpha) {
  self->glBlendColor(red, green, blue, alpha);
}

//  void QOpenGLFunctions_3_2_Core::glSampleCoverage(GLfloat value, GLboolean
//      invert)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core16glSampleCoverageEfh(
    QOpenGLFunctions_3_2_Core *self,
    GLfloat value,
    GLboolean invert) {
  self->glSampleCoverage(value, invert);
}

//  void QOpenGLFunctions_3_2_Core::glActiveTexture(GLenum texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core15glActiveTextureEj(
    QOpenGLFunctions_3_2_Core *self,
    GLenum texture) {
  self->glActiveTexture(texture);
}

//  void QOpenGLFunctions_3_2_Core::glPointParameteri(GLenum pname, GLint
//      param)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core17glPointParameteriEji(
    QOpenGLFunctions_3_2_Core *self,
    GLenum pname,
    GLint param) {
  self->glPointParameteri(pname, param);
}

//  void QOpenGLFunctions_3_2_Core::glPointParameterf(GLenum pname, GLfloat
//      param)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core17glPointParameterfEjf(
    QOpenGLFunctions_3_2_Core *self,
    GLenum pname,
    GLfloat param) {
  self->glPointParameterf(pname, param);
}

//  void QOpenGLFunctions_3_2_Core::glBlendFuncSeparate(GLenum sfactorRGB,
//      GLenum dfactorRGB, GLenum sfactorAlpha, GLenum dfactorAlpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core19glBlendFuncSeparateEjjjj(
    QOpenGLFunctions_3_2_Core *self,
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

//  void QOpenGLFunctions_3_2_Core::glBindBuffer(GLenum target, GLuint
//      buffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core12glBindBufferEjj(
    QOpenGLFunctions_3_2_Core *self,
    GLenum target,
    GLuint buffer) {
  self->glBindBuffer(target, buffer);
}

//  void QOpenGLFunctions_3_2_Core::glEndQuery(GLenum target)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core10glEndQueryEj(
    QOpenGLFunctions_3_2_Core *self,
    GLenum target) {
  self->glEndQuery(target);
}

//  void QOpenGLFunctions_3_2_Core::glBeginQuery(GLenum target, GLuint id)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core12glBeginQueryEjj(
    QOpenGLFunctions_3_2_Core *self,
    GLenum target,
    GLuint id) {
  self->glBeginQuery(target, id);
}

//  void QOpenGLFunctions_3_2_Core::glValidateProgram(GLuint program)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core17glValidateProgramEj(
    QOpenGLFunctions_3_2_Core *self,
    GLuint program) {
  self->glValidateProgram(program);
}

//  void QOpenGLFunctions_3_2_Core::glUniform4i(GLint location, GLint v0,
//      GLint v1, GLint v2, GLint v3)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core11glUniform4iEiiiii(
    QOpenGLFunctions_3_2_Core *self,
    GLint location,
    GLint v0,
    GLint v1,
    GLint v2,
    GLint v3) {
  self->glUniform4i(location, v0, v1, v2, v3);
}

//  void QOpenGLFunctions_3_2_Core::glUniform3i(GLint location, GLint v0,
//      GLint v1, GLint v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core11glUniform3iEiiii(
    QOpenGLFunctions_3_2_Core *self,
    GLint location,
    GLint v0,
    GLint v1,
    GLint v2) {
  self->glUniform3i(location, v0, v1, v2);
}

//  void QOpenGLFunctions_3_2_Core::glUniform2i(GLint location, GLint v0,
//      GLint v1)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core11glUniform2iEiii(
    QOpenGLFunctions_3_2_Core *self,
    GLint location,
    GLint v0,
    GLint v1) {
  self->glUniform2i(location, v0, v1);
}

//  void QOpenGLFunctions_3_2_Core::glUniform1i(GLint location, GLint v0)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core11glUniform1iEii(
    QOpenGLFunctions_3_2_Core *self,
    GLint location,
    GLint v0) {
  self->glUniform1i(location, v0);
}

//  void QOpenGLFunctions_3_2_Core::glUniform4f(GLint location, GLfloat v0,
//      GLfloat v1, GLfloat v2, GLfloat v3)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core11glUniform4fEiffff(
    QOpenGLFunctions_3_2_Core *self,
    GLint location,
    GLfloat v0,
    GLfloat v1,
    GLfloat v2,
    GLfloat v3) {
  self->glUniform4f(location, v0, v1, v2, v3);
}

//  void QOpenGLFunctions_3_2_Core::glUniform3f(GLint location, GLfloat v0,
//      GLfloat v1, GLfloat v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core11glUniform3fEifff(
    QOpenGLFunctions_3_2_Core *self,
    GLint location,
    GLfloat v0,
    GLfloat v1,
    GLfloat v2) {
  self->glUniform3f(location, v0, v1, v2);
}

//  void QOpenGLFunctions_3_2_Core::glUniform2f(GLint location, GLfloat v0,
//      GLfloat v1)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core11glUniform2fEiff(
    QOpenGLFunctions_3_2_Core *self,
    GLint location,
    GLfloat v0,
    GLfloat v1) {
  self->glUniform2f(location, v0, v1);
}

//  void QOpenGLFunctions_3_2_Core::glUniform1f(GLint location, GLfloat v0)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core11glUniform1fEif(
    QOpenGLFunctions_3_2_Core *self,
    GLint location,
    GLfloat v0) {
  self->glUniform1f(location, v0);
}

//  void QOpenGLFunctions_3_2_Core::glUseProgram(GLuint program)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core12glUseProgramEj(
    QOpenGLFunctions_3_2_Core *self,
    GLuint program) {
  self->glUseProgram(program);
}

//  void QOpenGLFunctions_3_2_Core::glLinkProgram(GLuint program)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core13glLinkProgramEj(
    QOpenGLFunctions_3_2_Core *self,
    GLuint program) {
  self->glLinkProgram(program);
}

//  void QOpenGLFunctions_3_2_Core::glEnableVertexAttribArray(GLuint index)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core25glEnableVertexAttribArrayEj(
    QOpenGLFunctions_3_2_Core *self,
    GLuint index) {
  self->glEnableVertexAttribArray(index);
}

//  void QOpenGLFunctions_3_2_Core::glDisableVertexAttribArray(GLuint index)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core26glDisableVertexAttribArrayEj(
    QOpenGLFunctions_3_2_Core *self,
    GLuint index) {
  self->glDisableVertexAttribArray(index);
}

//  void QOpenGLFunctions_3_2_Core::glDetachShader(GLuint program, GLuint
//      shader)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core14glDetachShaderEjj(
    QOpenGLFunctions_3_2_Core *self,
    GLuint program,
    GLuint shader) {
  self->glDetachShader(program, shader);
}

//  void QOpenGLFunctions_3_2_Core::glDeleteShader(GLuint shader)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core14glDeleteShaderEj(
    QOpenGLFunctions_3_2_Core *self,
    GLuint shader) {
  self->glDeleteShader(shader);
}

//  void QOpenGLFunctions_3_2_Core::glDeleteProgram(GLuint program)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core15glDeleteProgramEj(
    QOpenGLFunctions_3_2_Core *self,
    GLuint program) {
  self->glDeleteProgram(program);
}

//  void QOpenGLFunctions_3_2_Core::glCompileShader(GLuint shader)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core15glCompileShaderEj(
    QOpenGLFunctions_3_2_Core *self,
    GLuint shader) {
  self->glCompileShader(shader);
}

//  void QOpenGLFunctions_3_2_Core::glAttachShader(GLuint program, GLuint
//      shader)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core14glAttachShaderEjj(
    QOpenGLFunctions_3_2_Core *self,
    GLuint program,
    GLuint shader) {
  self->glAttachShader(program, shader);
}

//  void QOpenGLFunctions_3_2_Core::glStencilMaskSeparate(GLenum face, GLuint
//      mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core21glStencilMaskSeparateEjj(
    QOpenGLFunctions_3_2_Core *self,
    GLenum face,
    GLuint mask) {
  self->glStencilMaskSeparate(face, mask);
}

//  void QOpenGLFunctions_3_2_Core::glStencilFuncSeparate(GLenum face, GLenum
//      func, GLint ref, GLuint mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core21glStencilFuncSeparateEjjij(
    QOpenGLFunctions_3_2_Core *self,
    GLenum face,
    GLenum func,
    GLint ref,
    GLuint mask) {
  self->glStencilFuncSeparate(face, func, ref, mask);
}

//  void QOpenGLFunctions_3_2_Core::glStencilOpSeparate(GLenum face, GLenum
//      sfail, GLenum dpfail, GLenum dppass)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core19glStencilOpSeparateEjjjj(
    QOpenGLFunctions_3_2_Core *self,
    GLenum face,
    GLenum sfail,
    GLenum dpfail,
    GLenum dppass) {
  self->glStencilOpSeparate(face, sfail, dpfail, dppass);
}

//  void QOpenGLFunctions_3_2_Core::glBlendEquationSeparate(GLenum modeRGB,
//      GLenum modeAlpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core23glBlendEquationSeparateEjj(
    QOpenGLFunctions_3_2_Core *self,
    GLenum modeRGB,
    GLenum modeAlpha) {
  self->glBlendEquationSeparate(modeRGB, modeAlpha);
}

//  void QOpenGLFunctions_3_2_Core::glBindVertexArray(GLuint array)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core17glBindVertexArrayEj(
    QOpenGLFunctions_3_2_Core *self,
    GLuint array) {
  self->glBindVertexArray(array);
}

//  void QOpenGLFunctions_3_2_Core::glFramebufferTextureLayer(GLenum target,
//      GLenum attachment, GLuint texture, GLint level, GLint layer)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core25glFramebufferTextureLayerEjjjii(
    QOpenGLFunctions_3_2_Core *self,
    GLenum target,
    GLenum attachment,
    GLuint texture,
    GLint level,
    GLint layer) {
  self->glFramebufferTextureLayer(target, attachment, texture, level, layer);
}

//  void QOpenGLFunctions_3_2_Core::glRenderbufferStorageMultisample(GLenum
//      target, GLsizei samples, GLenum internalformat, GLsizei width,
//      GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core32glRenderbufferStorageMultisampleEjijii(
    QOpenGLFunctions_3_2_Core *self,
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

//  void QOpenGLFunctions_3_2_Core::glBlitFramebuffer(GLint srcX0, GLint
//      srcY0, GLint srcX1, GLint srcY1, GLint dstX0, GLint dstY0, GLint
//      dstX1, GLint dstY1, GLbitfield mask, GLenum filter)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core17glBlitFramebufferEiiiiiiiijj(
    QOpenGLFunctions_3_2_Core *self,
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

//  void QOpenGLFunctions_3_2_Core::glGenerateMipmap(GLenum target)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core16glGenerateMipmapEj(
    QOpenGLFunctions_3_2_Core *self,
    GLenum target) {
  self->glGenerateMipmap(target);
}

//  void QOpenGLFunctions_3_2_Core::glFramebufferRenderbuffer(GLenum target,
//      GLenum attachment, GLenum renderbuffertarget, GLuint renderbuffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core25glFramebufferRenderbufferEjjjj(
    QOpenGLFunctions_3_2_Core *self,
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

//  void QOpenGLFunctions_3_2_Core::glFramebufferTexture3D(GLenum target,
//      GLenum attachment, GLenum textarget, GLuint texture, GLint level,
//      GLint zoffset)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core22glFramebufferTexture3DEjjjjii(
    QOpenGLFunctions_3_2_Core *self,
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

//  void QOpenGLFunctions_3_2_Core::glFramebufferTexture2D(GLenum target,
//      GLenum attachment, GLenum textarget, GLuint texture, GLint level)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core22glFramebufferTexture2DEjjjji(
    QOpenGLFunctions_3_2_Core *self,
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

//  void QOpenGLFunctions_3_2_Core::glFramebufferTexture1D(GLenum target,
//      GLenum attachment, GLenum textarget, GLuint texture, GLint level)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core22glFramebufferTexture1DEjjjji(
    QOpenGLFunctions_3_2_Core *self,
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

//  void QOpenGLFunctions_3_2_Core::glBindFramebuffer(GLenum target, GLuint
//      framebuffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core17glBindFramebufferEjj(
    QOpenGLFunctions_3_2_Core *self,
    GLenum target,
    GLuint framebuffer) {
  self->glBindFramebuffer(target, framebuffer);
}

//  void QOpenGLFunctions_3_2_Core::glRenderbufferStorage(GLenum target,
//      GLenum internalformat, GLsizei width, GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core21glRenderbufferStorageEjjii(
    QOpenGLFunctions_3_2_Core *self,
    GLenum target,
    GLenum internalformat,
    GLsizei width,
    GLsizei height) {
  self->glRenderbufferStorage(target, internalformat, width, height);
}

//  void QOpenGLFunctions_3_2_Core::glBindRenderbuffer(GLenum target, GLuint
//      renderbuffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core18glBindRenderbufferEjj(
    QOpenGLFunctions_3_2_Core *self,
    GLenum target,
    GLuint renderbuffer) {
  self->glBindRenderbuffer(target, renderbuffer);
}

//  void QOpenGLFunctions_3_2_Core::glClearBufferfi(GLenum buffer, GLint
//      drawbuffer, GLfloat depth, GLint stencil)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core15glClearBufferfiEjifi(
    QOpenGLFunctions_3_2_Core *self,
    GLenum buffer,
    GLint drawbuffer,
    GLfloat depth,
    GLint stencil) {
  self->glClearBufferfi(buffer, drawbuffer, depth, stencil);
}

//  void QOpenGLFunctions_3_2_Core::glUniform4ui(GLint location, GLuint v0,
//      GLuint v1, GLuint v2, GLuint v3)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core12glUniform4uiEijjjj(
    QOpenGLFunctions_3_2_Core *self,
    GLint location,
    GLuint v0,
    GLuint v1,
    GLuint v2,
    GLuint v3) {
  self->glUniform4ui(location, v0, v1, v2, v3);
}

//  void QOpenGLFunctions_3_2_Core::glUniform3ui(GLint location, GLuint v0,
//      GLuint v1, GLuint v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core12glUniform3uiEijjj(
    QOpenGLFunctions_3_2_Core *self,
    GLint location,
    GLuint v0,
    GLuint v1,
    GLuint v2) {
  self->glUniform3ui(location, v0, v1, v2);
}

//  void QOpenGLFunctions_3_2_Core::glUniform2ui(GLint location, GLuint v0,
//      GLuint v1)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core12glUniform2uiEijj(
    QOpenGLFunctions_3_2_Core *self,
    GLint location,
    GLuint v0,
    GLuint v1) {
  self->glUniform2ui(location, v0, v1);
}

//  void QOpenGLFunctions_3_2_Core::glUniform1ui(GLint location, GLuint v0)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core12glUniform1uiEij(
    QOpenGLFunctions_3_2_Core *self,
    GLint location,
    GLuint v0) {
  self->glUniform1ui(location, v0);
}

//  void QOpenGLFunctions_3_2_Core::glEndConditionalRender()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core22glEndConditionalRenderEv(
    QOpenGLFunctions_3_2_Core *self) {
  self->glEndConditionalRender();
}

//  void QOpenGLFunctions_3_2_Core::glBeginConditionalRender(GLuint id,
//      GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core24glBeginConditionalRenderEjj(
    QOpenGLFunctions_3_2_Core *self,
    GLuint id,
    GLenum mode) {
  self->glBeginConditionalRender(id, mode);
}

//  void QOpenGLFunctions_3_2_Core::glClampColor(GLenum target, GLenum clamp)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core12glClampColorEjj(
    QOpenGLFunctions_3_2_Core *self,
    GLenum target,
    GLenum clamp) {
  self->glClampColor(target, clamp);
}

//  void QOpenGLFunctions_3_2_Core::glBindBufferBase(GLenum target, GLuint
//      index, GLuint buffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core16glBindBufferBaseEjjj(
    QOpenGLFunctions_3_2_Core *self,
    GLenum target,
    GLuint index,
    GLuint buffer) {
  self->glBindBufferBase(target, index, buffer);
}

//  void QOpenGLFunctions_3_2_Core::glEndTransformFeedback()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core22glEndTransformFeedbackEv(
    QOpenGLFunctions_3_2_Core *self) {
  self->glEndTransformFeedback();
}

//  void QOpenGLFunctions_3_2_Core::glBeginTransformFeedback(GLenum
//      primitiveMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core24glBeginTransformFeedbackEj(
    QOpenGLFunctions_3_2_Core *self,
    GLenum primitiveMode) {
  self->glBeginTransformFeedback(primitiveMode);
}

//  void QOpenGLFunctions_3_2_Core::glDisablei(GLenum target, GLuint index)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core10glDisableiEjj(
    QOpenGLFunctions_3_2_Core *self,
    GLenum target,
    GLuint index) {
  self->glDisablei(target, index);
}

//  void QOpenGLFunctions_3_2_Core::glEnablei(GLenum target, GLuint index)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core9glEnableiEjj(
    QOpenGLFunctions_3_2_Core *self,
    GLenum target,
    GLuint index) {
  self->glEnablei(target, index);
}

//  void QOpenGLFunctions_3_2_Core::glColorMaski(GLuint index, GLboolean r,
//      GLboolean g, GLboolean b, GLboolean a)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core12glColorMaskiEjhhhh(
    QOpenGLFunctions_3_2_Core *self,
    GLuint index,
    GLboolean r,
    GLboolean g,
    GLboolean b,
    GLboolean a) {
  self->glColorMaski(index, r, g, b, a);
}

//  void QOpenGLFunctions_3_2_Core::glUniformBlockBinding(GLuint program,
//      GLuint uniformBlockIndex, GLuint uniformBlockBinding)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core21glUniformBlockBindingEjjj(
    QOpenGLFunctions_3_2_Core *self,
    GLuint program,
    GLuint uniformBlockIndex,
    GLuint uniformBlockBinding) {
  self->glUniformBlockBinding(
      program,
      uniformBlockIndex,
      uniformBlockBinding);
}

//  void QOpenGLFunctions_3_2_Core::glPrimitiveRestartIndex(GLuint index)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core23glPrimitiveRestartIndexEj(
    QOpenGLFunctions_3_2_Core *self,
    GLuint index) {
  self->glPrimitiveRestartIndex(index);
}

//  void QOpenGLFunctions_3_2_Core::glTexBuffer(GLenum target, GLenum
//      internalformat, GLuint buffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core11glTexBufferEjjj(
    QOpenGLFunctions_3_2_Core *self,
    GLenum target,
    GLenum internalformat,
    GLuint buffer) {
  self->glTexBuffer(target, internalformat, buffer);
}

//  void QOpenGLFunctions_3_2_Core::glDrawArraysInstanced(GLenum mode, GLint
//      first, GLsizei count, GLsizei instancecount)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core21glDrawArraysInstancedEjiii(
    QOpenGLFunctions_3_2_Core *self,
    GLenum mode,
    GLint first,
    GLsizei count,
    GLsizei instancecount) {
  self->glDrawArraysInstanced(mode, first, count, instancecount);
}

//  void QOpenGLFunctions_3_2_Core::glSampleMaski(GLuint index, GLbitfield
//      mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core13glSampleMaskiEjj(
    QOpenGLFunctions_3_2_Core *self,
    GLuint index,
    GLbitfield mask) {
  self->glSampleMaski(index, mask);
}

//  void QOpenGLFunctions_3_2_Core::glTexImage3DMultisample(GLenum target,
//      GLsizei samples, GLint internalformat, GLsizei width, GLsizei height,
//      GLsizei depth, GLboolean fixedsamplelocations)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core23glTexImage3DMultisampleEjiiiiih(
    QOpenGLFunctions_3_2_Core *self,
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

//  void QOpenGLFunctions_3_2_Core::glTexImage2DMultisample(GLenum target,
//      GLsizei samples, GLint internalformat, GLsizei width, GLsizei height,
//      GLboolean fixedsamplelocations)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core23glTexImage2DMultisampleEjiiiih(
    QOpenGLFunctions_3_2_Core *self,
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

//  void QOpenGLFunctions_3_2_Core::glProvokingVertex(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core17glProvokingVertexEj(
    QOpenGLFunctions_3_2_Core *self,
    GLenum mode) {
  self->glProvokingVertex(mode);
}

//  void QOpenGLFunctions_3_2_Core::glFramebufferTexture(GLenum target,
//      GLenum attachment, GLuint texture, GLint level)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core20glFramebufferTextureEjjji(
    QOpenGLFunctions_3_2_Core *self,
    GLenum target,
    GLenum attachment,
    GLuint texture,
    GLint level) {
  self->glFramebufferTexture(target, attachment, texture, level);
}

//  bool QOpenGLFunctions_3_2_Core::isContextCompatible(QOpenGLContext
//      *context)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QOpenGLFunctions_3_2_Core19isContextCompatibleEP14QOpenGLContext(
    QOpenGLContext *context) {
  return QOpenGLFunctions_3_2_Core::isContextCompatible(context);
}

//  QOpenGLVersionProfile QOpenGLFunctions_3_2_Core::versionProfile()
extern "C" Q_DECL_EXPORT
QOpenGLVersionProfile *ritual_ZN25QOpenGLFunctions_3_2_Core14versionProfileEv() {
  return new QOpenGLVersionProfile(
      QOpenGLFunctions_3_2_Core::versionProfile());
}

//  a Python function taken by a CuteQOpenGLFunctions_3_2_Core, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QOpenGLFunctions_3_2_Core(
    QOpenGLFunctions_3_2_Core *self,
    const char *key,
    void *call) {
  return static_cast<CuteQOpenGLFunctions_3_2_Core *>(self)->take(key, call);
}

//  bool QOpenGLFunctions_3_2_Core::initializeOpenGLFunctions()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN25QOpenGLFunctions_3_2_Core25initializeOpenGLFunctionsEv(
    QOpenGLFunctions_3_2_Core *self) {
  return self->QOpenGLFunctions_3_2_Core::initializeOpenGLFunctions();
}

#endif  // !defined(QT_NO_OPENGL) && !QT_CONFIG(opengles2)
