//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/qopenglfunctions_4_4_core.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtOpenGL/qtopenglglobal.h>
#if !defined(QT_NO_OPENGL) && !QT_CONFIG(opengles2)
#include <QtOpenGL/QtOpenGL>
#include <QtOpenGL/qopenglfunctions_4_4_core.h>
#include <QtOpenGL/qopenglversionprofile.h>
#include <cstring>

//  A QOpenGLFunctions_4_4_Core that Python can take functions over in. Every QOpenGLFunctions_4_4_Core
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL) && !QT_CONFIG(opengles2)
typedef bool (*CuteQOpenGLFunctions_4_4_CoreCall0)(const void *, int *);
#endif  // !defined(QT_NO_OPENGL) && !QT_CONFIG(opengles2)
#endif  // !defined(QT_NO_OPENGL)
class CuteQOpenGLFunctions_4_4_Core : public QOpenGLFunctions_4_4_Core {
public:
  using QOpenGLFunctions_4_4_Core::QOpenGLFunctions_4_4_Core;
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
  //  bool QOpenGLFunctions_4_4_Core::initializeOpenGLFunctions()
  bool initializeOpenGLFunctions() override {
    if (taken[0]) {
      int handled = 0;
      CuteQOpenGLFunctions_4_4_CoreCall0 call = reinterpret_cast<CuteQOpenGLFunctions_4_4_CoreCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QOpenGLFunctions_4_4_Core::initializeOpenGLFunctions();
  }
#endif  // !defined(QT_NO_OPENGL) && !QT_CONFIG(opengles2)
#endif  // !defined(QT_NO_OPENGL)
};

//  QOpenGLFunctions_4_4_Core::QOpenGLFunctions_4_4_Core()
extern "C" Q_DECL_EXPORT
QOpenGLFunctions_4_4_Core *ritual_ZN25QOpenGLFunctions_4_4_CoreC1Ev() {
  return new CuteQOpenGLFunctions_4_4_Core();
}

//  QOpenGLFunctions_4_4_Core::~QOpenGLFunctions_4_4_Core()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_CoreD1Ev(
    QOpenGLFunctions_4_4_Core *self) {
  delete self;
}

//  bool QOpenGLFunctions_4_4_Core::initializeOpenGLFunctions()
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QOpenGLFunctions_4_4_Core25initializeOpenGLFunctionsEv(
    QOpenGLFunctions_4_4_Core *self) {
  return self->initializeOpenGLFunctions();
}

//  void QOpenGLFunctions_4_4_Core::glViewport(GLint x, GLint y, GLsizei
//      width, GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core10glViewportEiiii(
    QOpenGLFunctions_4_4_Core *self,
    GLint x,
    GLint y,
    GLsizei width,
    GLsizei height) {
  self->glViewport(x, y, width, height);
}

//  void QOpenGLFunctions_4_4_Core::glDepthRange(GLdouble nearVal, GLdouble
//      farVal)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core12glDepthRangeEdd(
    QOpenGLFunctions_4_4_Core *self,
    GLdouble nearVal,
    GLdouble farVal) {
  self->glDepthRange(nearVal, farVal);
}

//  void QOpenGLFunctions_4_4_Core::glReadBuffer(GLenum src)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core12glReadBufferEj(
    QOpenGLFunctions_4_4_Core *self,
    GLenum src) {
  self->glReadBuffer(src);
}

//  void QOpenGLFunctions_4_4_Core::glPixelStorei(GLenum pname, GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core13glPixelStoreiEji(
    QOpenGLFunctions_4_4_Core *self,
    GLenum pname,
    GLint param) {
  self->glPixelStorei(pname, param);
}

//  void QOpenGLFunctions_4_4_Core::glPixelStoref(GLenum pname, GLfloat
//      param)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core13glPixelStorefEjf(
    QOpenGLFunctions_4_4_Core *self,
    GLenum pname,
    GLfloat param) {
  self->glPixelStoref(pname, param);
}

//  void QOpenGLFunctions_4_4_Core::glDepthFunc(GLenum func)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core11glDepthFuncEj(
    QOpenGLFunctions_4_4_Core *self,
    GLenum func) {
  self->glDepthFunc(func);
}

//  void QOpenGLFunctions_4_4_Core::glStencilOp(GLenum fail, GLenum zfail,
//      GLenum zpass)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core11glStencilOpEjjj(
    QOpenGLFunctions_4_4_Core *self,
    GLenum fail,
    GLenum zfail,
    GLenum zpass) {
  self->glStencilOp(fail, zfail, zpass);
}

//  void QOpenGLFunctions_4_4_Core::glStencilFunc(GLenum func, GLint ref,
//      GLuint mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core13glStencilFuncEjij(
    QOpenGLFunctions_4_4_Core *self,
    GLenum func,
    GLint ref,
    GLuint mask) {
  self->glStencilFunc(func, ref, mask);
}

//  void QOpenGLFunctions_4_4_Core::glLogicOp(GLenum opcode)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core9glLogicOpEj(
    QOpenGLFunctions_4_4_Core *self,
    GLenum opcode) {
  self->glLogicOp(opcode);
}

//  void QOpenGLFunctions_4_4_Core::glBlendFunc(GLenum sfactor, GLenum
//      dfactor)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core11glBlendFuncEjj(
    QOpenGLFunctions_4_4_Core *self,
    GLenum sfactor,
    GLenum dfactor) {
  self->glBlendFunc(sfactor, dfactor);
}

//  void QOpenGLFunctions_4_4_Core::glFlush()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core7glFlushEv(
    QOpenGLFunctions_4_4_Core *self) {
  self->glFlush();
}

//  void QOpenGLFunctions_4_4_Core::glFinish()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core8glFinishEv(
    QOpenGLFunctions_4_4_Core *self) {
  self->glFinish();
}

//  void QOpenGLFunctions_4_4_Core::glEnable(GLenum cap)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core8glEnableEj(
    QOpenGLFunctions_4_4_Core *self,
    GLenum cap) {
  self->glEnable(cap);
}

//  void QOpenGLFunctions_4_4_Core::glDisable(GLenum cap)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core9glDisableEj(
    QOpenGLFunctions_4_4_Core *self,
    GLenum cap) {
  self->glDisable(cap);
}

//  void QOpenGLFunctions_4_4_Core::glDepthMask(GLboolean flag)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core11glDepthMaskEh(
    QOpenGLFunctions_4_4_Core *self,
    GLboolean flag) {
  self->glDepthMask(flag);
}

//  void QOpenGLFunctions_4_4_Core::glColorMask(GLboolean red, GLboolean
//      green, GLboolean blue, GLboolean alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core11glColorMaskEhhhh(
    QOpenGLFunctions_4_4_Core *self,
    GLboolean red,
    GLboolean green,
    GLboolean blue,
    GLboolean alpha) {
  self->glColorMask(red, green, blue, alpha);
}

//  void QOpenGLFunctions_4_4_Core::glStencilMask(GLuint mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core13glStencilMaskEj(
    QOpenGLFunctions_4_4_Core *self,
    GLuint mask) {
  self->glStencilMask(mask);
}

//  void QOpenGLFunctions_4_4_Core::glClearDepth(GLdouble depth)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core12glClearDepthEd(
    QOpenGLFunctions_4_4_Core *self,
    GLdouble depth) {
  self->glClearDepth(depth);
}

//  void QOpenGLFunctions_4_4_Core::glClearStencil(GLint s)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core14glClearStencilEi(
    QOpenGLFunctions_4_4_Core *self,
    GLint s) {
  self->glClearStencil(s);
}

//  void QOpenGLFunctions_4_4_Core::glClearColor(GLfloat red, GLfloat green,
//      GLfloat blue, GLfloat alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core12glClearColorEffff(
    QOpenGLFunctions_4_4_Core *self,
    GLfloat red,
    GLfloat green,
    GLfloat blue,
    GLfloat alpha) {
  self->glClearColor(red, green, blue, alpha);
}

//  void QOpenGLFunctions_4_4_Core::glClear(GLbitfield mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core7glClearEj(
    QOpenGLFunctions_4_4_Core *self,
    GLbitfield mask) {
  self->glClear(mask);
}

//  void QOpenGLFunctions_4_4_Core::glDrawBuffer(GLenum buf)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core12glDrawBufferEj(
    QOpenGLFunctions_4_4_Core *self,
    GLenum buf) {
  self->glDrawBuffer(buf);
}

//  void QOpenGLFunctions_4_4_Core::glTexParameteri(GLenum target, GLenum
//      pname, GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core15glTexParameteriEjji(
    QOpenGLFunctions_4_4_Core *self,
    GLenum target,
    GLenum pname,
    GLint param) {
  self->glTexParameteri(target, pname, param);
}

//  void QOpenGLFunctions_4_4_Core::glTexParameterf(GLenum target, GLenum
//      pname, GLfloat param)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core15glTexParameterfEjjf(
    QOpenGLFunctions_4_4_Core *self,
    GLenum target,
    GLenum pname,
    GLfloat param) {
  self->glTexParameterf(target, pname, param);
}

//  void QOpenGLFunctions_4_4_Core::glScissor(GLint x, GLint y, GLsizei
//      width, GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core9glScissorEiiii(
    QOpenGLFunctions_4_4_Core *self,
    GLint x,
    GLint y,
    GLsizei width,
    GLsizei height) {
  self->glScissor(x, y, width, height);
}

//  void QOpenGLFunctions_4_4_Core::glPolygonMode(GLenum face, GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core13glPolygonModeEjj(
    QOpenGLFunctions_4_4_Core *self,
    GLenum face,
    GLenum mode) {
  self->glPolygonMode(face, mode);
}

//  void QOpenGLFunctions_4_4_Core::glPointSize(GLfloat size)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core11glPointSizeEf(
    QOpenGLFunctions_4_4_Core *self,
    GLfloat size) {
  self->glPointSize(size);
}

//  void QOpenGLFunctions_4_4_Core::glLineWidth(GLfloat width)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core11glLineWidthEf(
    QOpenGLFunctions_4_4_Core *self,
    GLfloat width) {
  self->glLineWidth(width);
}

//  void QOpenGLFunctions_4_4_Core::glHint(GLenum target, GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core6glHintEjj(
    QOpenGLFunctions_4_4_Core *self,
    GLenum target,
    GLenum mode) {
  self->glHint(target, mode);
}

//  void QOpenGLFunctions_4_4_Core::glFrontFace(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core11glFrontFaceEj(
    QOpenGLFunctions_4_4_Core *self,
    GLenum mode) {
  self->glFrontFace(mode);
}

//  void QOpenGLFunctions_4_4_Core::glCullFace(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core10glCullFaceEj(
    QOpenGLFunctions_4_4_Core *self,
    GLenum mode) {
  self->glCullFace(mode);
}

//  void QOpenGLFunctions_4_4_Core::glBindTexture(GLenum target, GLuint
//      texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core13glBindTextureEjj(
    QOpenGLFunctions_4_4_Core *self,
    GLenum target,
    GLuint texture) {
  self->glBindTexture(target, texture);
}

//  void QOpenGLFunctions_4_4_Core::glCopyTexSubImage2D(GLenum target, GLint
//      level, GLint xoffset, GLint yoffset, GLint x, GLint y, GLsizei width,
//      GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core19glCopyTexSubImage2DEjiiiiiii(
    QOpenGLFunctions_4_4_Core *self,
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

//  void QOpenGLFunctions_4_4_Core::glCopyTexSubImage1D(GLenum target, GLint
//      level, GLint xoffset, GLint x, GLint y, GLsizei width)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core19glCopyTexSubImage1DEjiiiii(
    QOpenGLFunctions_4_4_Core *self,
    GLenum target,
    GLint level,
    GLint xoffset,
    GLint x,
    GLint y,
    GLsizei width) {
  self->glCopyTexSubImage1D(target, level, xoffset, x, y, width);
}

//  void QOpenGLFunctions_4_4_Core::glCopyTexImage2D(GLenum target, GLint
//      level, GLenum internalformat, GLint x, GLint y, GLsizei width,
//      GLsizei height, GLint border)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core16glCopyTexImage2DEjijiiiii(
    QOpenGLFunctions_4_4_Core *self,
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

//  void QOpenGLFunctions_4_4_Core::glCopyTexImage1D(GLenum target, GLint
//      level, GLenum internalformat, GLint x, GLint y, GLsizei width, GLint
//      border)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core16glCopyTexImage1DEjijiiii(
    QOpenGLFunctions_4_4_Core *self,
    GLenum target,
    GLint level,
    GLenum internalformat,
    GLint x,
    GLint y,
    GLsizei width,
    GLint border) {
  self->glCopyTexImage1D(target, level, internalformat, x, y, width, border);
}

//  void QOpenGLFunctions_4_4_Core::glPolygonOffset(GLfloat factor, GLfloat
//      units)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core15glPolygonOffsetEff(
    QOpenGLFunctions_4_4_Core *self,
    GLfloat factor,
    GLfloat units) {
  self->glPolygonOffset(factor, units);
}

//  void QOpenGLFunctions_4_4_Core::glDrawArrays(GLenum mode, GLint first,
//      GLsizei count)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core12glDrawArraysEjii(
    QOpenGLFunctions_4_4_Core *self,
    GLenum mode,
    GLint first,
    GLsizei count) {
  self->glDrawArrays(mode, first, count);
}

//  void QOpenGLFunctions_4_4_Core::glBlendColor(GLfloat red, GLfloat green,
//      GLfloat blue, GLfloat alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core12glBlendColorEffff(
    QOpenGLFunctions_4_4_Core *self,
    GLfloat red,
    GLfloat green,
    GLfloat blue,
    GLfloat alpha) {
  self->glBlendColor(red, green, blue, alpha);
}

//  void QOpenGLFunctions_4_4_Core::glBlendEquation(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core15glBlendEquationEj(
    QOpenGLFunctions_4_4_Core *self,
    GLenum mode) {
  self->glBlendEquation(mode);
}

//  void QOpenGLFunctions_4_4_Core::glCopyTexSubImage3D(GLenum target, GLint
//      level, GLint xoffset, GLint yoffset, GLint zoffset, GLint x, GLint y,
//      GLsizei width, GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core19glCopyTexSubImage3DEjiiiiiiii(
    QOpenGLFunctions_4_4_Core *self,
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

//  void QOpenGLFunctions_4_4_Core::glSampleCoverage(GLfloat value, GLboolean
//      invert)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core16glSampleCoverageEfh(
    QOpenGLFunctions_4_4_Core *self,
    GLfloat value,
    GLboolean invert) {
  self->glSampleCoverage(value, invert);
}

//  void QOpenGLFunctions_4_4_Core::glActiveTexture(GLenum texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core15glActiveTextureEj(
    QOpenGLFunctions_4_4_Core *self,
    GLenum texture) {
  self->glActiveTexture(texture);
}

//  void QOpenGLFunctions_4_4_Core::glPointParameteri(GLenum pname, GLint
//      param)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core17glPointParameteriEji(
    QOpenGLFunctions_4_4_Core *self,
    GLenum pname,
    GLint param) {
  self->glPointParameteri(pname, param);
}

//  void QOpenGLFunctions_4_4_Core::glPointParameterf(GLenum pname, GLfloat
//      param)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core17glPointParameterfEjf(
    QOpenGLFunctions_4_4_Core *self,
    GLenum pname,
    GLfloat param) {
  self->glPointParameterf(pname, param);
}

//  void QOpenGLFunctions_4_4_Core::glBlendFuncSeparate(GLenum sfactorRGB,
//      GLenum dfactorRGB, GLenum sfactorAlpha, GLenum dfactorAlpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core19glBlendFuncSeparateEjjjj(
    QOpenGLFunctions_4_4_Core *self,
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

//  void QOpenGLFunctions_4_4_Core::glBindBuffer(GLenum target, GLuint
//      buffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core12glBindBufferEjj(
    QOpenGLFunctions_4_4_Core *self,
    GLenum target,
    GLuint buffer) {
  self->glBindBuffer(target, buffer);
}

//  void QOpenGLFunctions_4_4_Core::glEndQuery(GLenum target)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core10glEndQueryEj(
    QOpenGLFunctions_4_4_Core *self,
    GLenum target) {
  self->glEndQuery(target);
}

//  void QOpenGLFunctions_4_4_Core::glBeginQuery(GLenum target, GLuint id)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core12glBeginQueryEjj(
    QOpenGLFunctions_4_4_Core *self,
    GLenum target,
    GLuint id) {
  self->glBeginQuery(target, id);
}

//  void QOpenGLFunctions_4_4_Core::glVertexAttrib4s(GLuint index, GLshort x,
//      GLshort y, GLshort z, GLshort w)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core16glVertexAttrib4sEjssss(
    QOpenGLFunctions_4_4_Core *self,
    GLuint index,
    GLshort x,
    GLshort y,
    GLshort z,
    GLshort w) {
  self->glVertexAttrib4s(index, x, y, z, w);
}

//  void QOpenGLFunctions_4_4_Core::glVertexAttrib4f(GLuint index, GLfloat x,
//      GLfloat y, GLfloat z, GLfloat w)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core16glVertexAttrib4fEjffff(
    QOpenGLFunctions_4_4_Core *self,
    GLuint index,
    GLfloat x,
    GLfloat y,
    GLfloat z,
    GLfloat w) {
  self->glVertexAttrib4f(index, x, y, z, w);
}

//  void QOpenGLFunctions_4_4_Core::glVertexAttrib4d(GLuint index, GLdouble
//      x, GLdouble y, GLdouble z, GLdouble w)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core16glVertexAttrib4dEjdddd(
    QOpenGLFunctions_4_4_Core *self,
    GLuint index,
    GLdouble x,
    GLdouble y,
    GLdouble z,
    GLdouble w) {
  self->glVertexAttrib4d(index, x, y, z, w);
}

//  void QOpenGLFunctions_4_4_Core::glVertexAttrib4Nub(GLuint index, GLubyte
//      x, GLubyte y, GLubyte z, GLubyte w)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core18glVertexAttrib4NubEjhhhh(
    QOpenGLFunctions_4_4_Core *self,
    GLuint index,
    GLubyte x,
    GLubyte y,
    GLubyte z,
    GLubyte w) {
  self->glVertexAttrib4Nub(index, x, y, z, w);
}

//  void QOpenGLFunctions_4_4_Core::glVertexAttrib3s(GLuint index, GLshort x,
//      GLshort y, GLshort z)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core16glVertexAttrib3sEjsss(
    QOpenGLFunctions_4_4_Core *self,
    GLuint index,
    GLshort x,
    GLshort y,
    GLshort z) {
  self->glVertexAttrib3s(index, x, y, z);
}

//  void QOpenGLFunctions_4_4_Core::glVertexAttrib3f(GLuint index, GLfloat x,
//      GLfloat y, GLfloat z)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core16glVertexAttrib3fEjfff(
    QOpenGLFunctions_4_4_Core *self,
    GLuint index,
    GLfloat x,
    GLfloat y,
    GLfloat z) {
  self->glVertexAttrib3f(index, x, y, z);
}

//  void QOpenGLFunctions_4_4_Core::glVertexAttrib3d(GLuint index, GLdouble
//      x, GLdouble y, GLdouble z)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core16glVertexAttrib3dEjddd(
    QOpenGLFunctions_4_4_Core *self,
    GLuint index,
    GLdouble x,
    GLdouble y,
    GLdouble z) {
  self->glVertexAttrib3d(index, x, y, z);
}

//  void QOpenGLFunctions_4_4_Core::glVertexAttrib2s(GLuint index, GLshort x,
//      GLshort y)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core16glVertexAttrib2sEjss(
    QOpenGLFunctions_4_4_Core *self,
    GLuint index,
    GLshort x,
    GLshort y) {
  self->glVertexAttrib2s(index, x, y);
}

//  void QOpenGLFunctions_4_4_Core::glVertexAttrib2f(GLuint index, GLfloat x,
//      GLfloat y)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core16glVertexAttrib2fEjff(
    QOpenGLFunctions_4_4_Core *self,
    GLuint index,
    GLfloat x,
    GLfloat y) {
  self->glVertexAttrib2f(index, x, y);
}

//  void QOpenGLFunctions_4_4_Core::glVertexAttrib2d(GLuint index, GLdouble
//      x, GLdouble y)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core16glVertexAttrib2dEjdd(
    QOpenGLFunctions_4_4_Core *self,
    GLuint index,
    GLdouble x,
    GLdouble y) {
  self->glVertexAttrib2d(index, x, y);
}

//  void QOpenGLFunctions_4_4_Core::glVertexAttrib1s(GLuint index, GLshort x)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core16glVertexAttrib1sEjs(
    QOpenGLFunctions_4_4_Core *self,
    GLuint index,
    GLshort x) {
  self->glVertexAttrib1s(index, x);
}

//  void QOpenGLFunctions_4_4_Core::glVertexAttrib1f(GLuint index, GLfloat x)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core16glVertexAttrib1fEjf(
    QOpenGLFunctions_4_4_Core *self,
    GLuint index,
    GLfloat x) {
  self->glVertexAttrib1f(index, x);
}

//  void QOpenGLFunctions_4_4_Core::glVertexAttrib1d(GLuint index, GLdouble
//      x)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core16glVertexAttrib1dEjd(
    QOpenGLFunctions_4_4_Core *self,
    GLuint index,
    GLdouble x) {
  self->glVertexAttrib1d(index, x);
}

//  void QOpenGLFunctions_4_4_Core::glValidateProgram(GLuint program)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core17glValidateProgramEj(
    QOpenGLFunctions_4_4_Core *self,
    GLuint program) {
  self->glValidateProgram(program);
}

//  void QOpenGLFunctions_4_4_Core::glUniform4i(GLint location, GLint v0,
//      GLint v1, GLint v2, GLint v3)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core11glUniform4iEiiiii(
    QOpenGLFunctions_4_4_Core *self,
    GLint location,
    GLint v0,
    GLint v1,
    GLint v2,
    GLint v3) {
  self->glUniform4i(location, v0, v1, v2, v3);
}

//  void QOpenGLFunctions_4_4_Core::glUniform3i(GLint location, GLint v0,
//      GLint v1, GLint v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core11glUniform3iEiiii(
    QOpenGLFunctions_4_4_Core *self,
    GLint location,
    GLint v0,
    GLint v1,
    GLint v2) {
  self->glUniform3i(location, v0, v1, v2);
}

//  void QOpenGLFunctions_4_4_Core::glUniform2i(GLint location, GLint v0,
//      GLint v1)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core11glUniform2iEiii(
    QOpenGLFunctions_4_4_Core *self,
    GLint location,
    GLint v0,
    GLint v1) {
  self->glUniform2i(location, v0, v1);
}

//  void QOpenGLFunctions_4_4_Core::glUniform1i(GLint location, GLint v0)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core11glUniform1iEii(
    QOpenGLFunctions_4_4_Core *self,
    GLint location,
    GLint v0) {
  self->glUniform1i(location, v0);
}

//  void QOpenGLFunctions_4_4_Core::glUniform4f(GLint location, GLfloat v0,
//      GLfloat v1, GLfloat v2, GLfloat v3)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core11glUniform4fEiffff(
    QOpenGLFunctions_4_4_Core *self,
    GLint location,
    GLfloat v0,
    GLfloat v1,
    GLfloat v2,
    GLfloat v3) {
  self->glUniform4f(location, v0, v1, v2, v3);
}

//  void QOpenGLFunctions_4_4_Core::glUniform3f(GLint location, GLfloat v0,
//      GLfloat v1, GLfloat v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core11glUniform3fEifff(
    QOpenGLFunctions_4_4_Core *self,
    GLint location,
    GLfloat v0,
    GLfloat v1,
    GLfloat v2) {
  self->glUniform3f(location, v0, v1, v2);
}

//  void QOpenGLFunctions_4_4_Core::glUniform2f(GLint location, GLfloat v0,
//      GLfloat v1)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core11glUniform2fEiff(
    QOpenGLFunctions_4_4_Core *self,
    GLint location,
    GLfloat v0,
    GLfloat v1) {
  self->glUniform2f(location, v0, v1);
}

//  void QOpenGLFunctions_4_4_Core::glUniform1f(GLint location, GLfloat v0)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core11glUniform1fEif(
    QOpenGLFunctions_4_4_Core *self,
    GLint location,
    GLfloat v0) {
  self->glUniform1f(location, v0);
}

//  void QOpenGLFunctions_4_4_Core::glUseProgram(GLuint program)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core12glUseProgramEj(
    QOpenGLFunctions_4_4_Core *self,
    GLuint program) {
  self->glUseProgram(program);
}

//  void QOpenGLFunctions_4_4_Core::glLinkProgram(GLuint program)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core13glLinkProgramEj(
    QOpenGLFunctions_4_4_Core *self,
    GLuint program) {
  self->glLinkProgram(program);
}

//  void QOpenGLFunctions_4_4_Core::glEnableVertexAttribArray(GLuint index)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core25glEnableVertexAttribArrayEj(
    QOpenGLFunctions_4_4_Core *self,
    GLuint index) {
  self->glEnableVertexAttribArray(index);
}

//  void QOpenGLFunctions_4_4_Core::glDisableVertexAttribArray(GLuint index)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core26glDisableVertexAttribArrayEj(
    QOpenGLFunctions_4_4_Core *self,
    GLuint index) {
  self->glDisableVertexAttribArray(index);
}

//  void QOpenGLFunctions_4_4_Core::glDetachShader(GLuint program, GLuint
//      shader)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core14glDetachShaderEjj(
    QOpenGLFunctions_4_4_Core *self,
    GLuint program,
    GLuint shader) {
  self->glDetachShader(program, shader);
}

//  void QOpenGLFunctions_4_4_Core::glDeleteShader(GLuint shader)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core14glDeleteShaderEj(
    QOpenGLFunctions_4_4_Core *self,
    GLuint shader) {
  self->glDeleteShader(shader);
}

//  void QOpenGLFunctions_4_4_Core::glDeleteProgram(GLuint program)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core15glDeleteProgramEj(
    QOpenGLFunctions_4_4_Core *self,
    GLuint program) {
  self->glDeleteProgram(program);
}

//  void QOpenGLFunctions_4_4_Core::glCompileShader(GLuint shader)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core15glCompileShaderEj(
    QOpenGLFunctions_4_4_Core *self,
    GLuint shader) {
  self->glCompileShader(shader);
}

//  void QOpenGLFunctions_4_4_Core::glAttachShader(GLuint program, GLuint
//      shader)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core14glAttachShaderEjj(
    QOpenGLFunctions_4_4_Core *self,
    GLuint program,
    GLuint shader) {
  self->glAttachShader(program, shader);
}

//  void QOpenGLFunctions_4_4_Core::glStencilMaskSeparate(GLenum face, GLuint
//      mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core21glStencilMaskSeparateEjj(
    QOpenGLFunctions_4_4_Core *self,
    GLenum face,
    GLuint mask) {
  self->glStencilMaskSeparate(face, mask);
}

//  void QOpenGLFunctions_4_4_Core::glStencilFuncSeparate(GLenum face, GLenum
//      func, GLint ref, GLuint mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core21glStencilFuncSeparateEjjij(
    QOpenGLFunctions_4_4_Core *self,
    GLenum face,
    GLenum func,
    GLint ref,
    GLuint mask) {
  self->glStencilFuncSeparate(face, func, ref, mask);
}

//  void QOpenGLFunctions_4_4_Core::glStencilOpSeparate(GLenum face, GLenum
//      sfail, GLenum dpfail, GLenum dppass)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core19glStencilOpSeparateEjjjj(
    QOpenGLFunctions_4_4_Core *self,
    GLenum face,
    GLenum sfail,
    GLenum dpfail,
    GLenum dppass) {
  self->glStencilOpSeparate(face, sfail, dpfail, dppass);
}

//  void QOpenGLFunctions_4_4_Core::glBlendEquationSeparate(GLenum modeRGB,
//      GLenum modeAlpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core23glBlendEquationSeparateEjj(
    QOpenGLFunctions_4_4_Core *self,
    GLenum modeRGB,
    GLenum modeAlpha) {
  self->glBlendEquationSeparate(modeRGB, modeAlpha);
}

//  void QOpenGLFunctions_4_4_Core::glBindVertexArray(GLuint array)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core17glBindVertexArrayEj(
    QOpenGLFunctions_4_4_Core *self,
    GLuint array) {
  self->glBindVertexArray(array);
}

//  void QOpenGLFunctions_4_4_Core::glFramebufferTextureLayer(GLenum target,
//      GLenum attachment, GLuint texture, GLint level, GLint layer)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core25glFramebufferTextureLayerEjjjii(
    QOpenGLFunctions_4_4_Core *self,
    GLenum target,
    GLenum attachment,
    GLuint texture,
    GLint level,
    GLint layer) {
  self->glFramebufferTextureLayer(target, attachment, texture, level, layer);
}

//  void QOpenGLFunctions_4_4_Core::glRenderbufferStorageMultisample(GLenum
//      target, GLsizei samples, GLenum internalformat, GLsizei width,
//      GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core32glRenderbufferStorageMultisampleEjijii(
    QOpenGLFunctions_4_4_Core *self,
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

//  void QOpenGLFunctions_4_4_Core::glBlitFramebuffer(GLint srcX0, GLint
//      srcY0, GLint srcX1, GLint srcY1, GLint dstX0, GLint dstY0, GLint
//      dstX1, GLint dstY1, GLbitfield mask, GLenum filter)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core17glBlitFramebufferEiiiiiiiijj(
    QOpenGLFunctions_4_4_Core *self,
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

//  void QOpenGLFunctions_4_4_Core::glGenerateMipmap(GLenum target)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core16glGenerateMipmapEj(
    QOpenGLFunctions_4_4_Core *self,
    GLenum target) {
  self->glGenerateMipmap(target);
}

//  void QOpenGLFunctions_4_4_Core::glFramebufferRenderbuffer(GLenum target,
//      GLenum attachment, GLenum renderbuffertarget, GLuint renderbuffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core25glFramebufferRenderbufferEjjjj(
    QOpenGLFunctions_4_4_Core *self,
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

//  void QOpenGLFunctions_4_4_Core::glFramebufferTexture3D(GLenum target,
//      GLenum attachment, GLenum textarget, GLuint texture, GLint level,
//      GLint zoffset)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core22glFramebufferTexture3DEjjjjii(
    QOpenGLFunctions_4_4_Core *self,
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

//  void QOpenGLFunctions_4_4_Core::glFramebufferTexture2D(GLenum target,
//      GLenum attachment, GLenum textarget, GLuint texture, GLint level)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core22glFramebufferTexture2DEjjjji(
    QOpenGLFunctions_4_4_Core *self,
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

//  void QOpenGLFunctions_4_4_Core::glFramebufferTexture1D(GLenum target,
//      GLenum attachment, GLenum textarget, GLuint texture, GLint level)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core22glFramebufferTexture1DEjjjji(
    QOpenGLFunctions_4_4_Core *self,
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

//  void QOpenGLFunctions_4_4_Core::glBindFramebuffer(GLenum target, GLuint
//      framebuffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core17glBindFramebufferEjj(
    QOpenGLFunctions_4_4_Core *self,
    GLenum target,
    GLuint framebuffer) {
  self->glBindFramebuffer(target, framebuffer);
}

//  void QOpenGLFunctions_4_4_Core::glRenderbufferStorage(GLenum target,
//      GLenum internalformat, GLsizei width, GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core21glRenderbufferStorageEjjii(
    QOpenGLFunctions_4_4_Core *self,
    GLenum target,
    GLenum internalformat,
    GLsizei width,
    GLsizei height) {
  self->glRenderbufferStorage(target, internalformat, width, height);
}

//  void QOpenGLFunctions_4_4_Core::glBindRenderbuffer(GLenum target, GLuint
//      renderbuffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core18glBindRenderbufferEjj(
    QOpenGLFunctions_4_4_Core *self,
    GLenum target,
    GLuint renderbuffer) {
  self->glBindRenderbuffer(target, renderbuffer);
}

//  void QOpenGLFunctions_4_4_Core::glClearBufferfi(GLenum buffer, GLint
//      drawbuffer, GLfloat depth, GLint stencil)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core15glClearBufferfiEjifi(
    QOpenGLFunctions_4_4_Core *self,
    GLenum buffer,
    GLint drawbuffer,
    GLfloat depth,
    GLint stencil) {
  self->glClearBufferfi(buffer, drawbuffer, depth, stencil);
}

//  void QOpenGLFunctions_4_4_Core::glUniform4ui(GLint location, GLuint v0,
//      GLuint v1, GLuint v2, GLuint v3)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core12glUniform4uiEijjjj(
    QOpenGLFunctions_4_4_Core *self,
    GLint location,
    GLuint v0,
    GLuint v1,
    GLuint v2,
    GLuint v3) {
  self->glUniform4ui(location, v0, v1, v2, v3);
}

//  void QOpenGLFunctions_4_4_Core::glUniform3ui(GLint location, GLuint v0,
//      GLuint v1, GLuint v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core12glUniform3uiEijjj(
    QOpenGLFunctions_4_4_Core *self,
    GLint location,
    GLuint v0,
    GLuint v1,
    GLuint v2) {
  self->glUniform3ui(location, v0, v1, v2);
}

//  void QOpenGLFunctions_4_4_Core::glUniform2ui(GLint location, GLuint v0,
//      GLuint v1)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core12glUniform2uiEijj(
    QOpenGLFunctions_4_4_Core *self,
    GLint location,
    GLuint v0,
    GLuint v1) {
  self->glUniform2ui(location, v0, v1);
}

//  void QOpenGLFunctions_4_4_Core::glUniform1ui(GLint location, GLuint v0)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core12glUniform1uiEij(
    QOpenGLFunctions_4_4_Core *self,
    GLint location,
    GLuint v0) {
  self->glUniform1ui(location, v0);
}

//  void QOpenGLFunctions_4_4_Core::glVertexAttribI4ui(GLuint index, GLuint
//      x, GLuint y, GLuint z, GLuint w)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core18glVertexAttribI4uiEjjjjj(
    QOpenGLFunctions_4_4_Core *self,
    GLuint index,
    GLuint x,
    GLuint y,
    GLuint z,
    GLuint w) {
  self->glVertexAttribI4ui(index, x, y, z, w);
}

//  void QOpenGLFunctions_4_4_Core::glVertexAttribI3ui(GLuint index, GLuint
//      x, GLuint y, GLuint z)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core18glVertexAttribI3uiEjjjj(
    QOpenGLFunctions_4_4_Core *self,
    GLuint index,
    GLuint x,
    GLuint y,
    GLuint z) {
  self->glVertexAttribI3ui(index, x, y, z);
}

//  void QOpenGLFunctions_4_4_Core::glVertexAttribI2ui(GLuint index, GLuint
//      x, GLuint y)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core18glVertexAttribI2uiEjjj(
    QOpenGLFunctions_4_4_Core *self,
    GLuint index,
    GLuint x,
    GLuint y) {
  self->glVertexAttribI2ui(index, x, y);
}

//  void QOpenGLFunctions_4_4_Core::glVertexAttribI1ui(GLuint index, GLuint
//      x)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core18glVertexAttribI1uiEjj(
    QOpenGLFunctions_4_4_Core *self,
    GLuint index,
    GLuint x) {
  self->glVertexAttribI1ui(index, x);
}

//  void QOpenGLFunctions_4_4_Core::glVertexAttribI4i(GLuint index, GLint x,
//      GLint y, GLint z, GLint w)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core17glVertexAttribI4iEjiiii(
    QOpenGLFunctions_4_4_Core *self,
    GLuint index,
    GLint x,
    GLint y,
    GLint z,
    GLint w) {
  self->glVertexAttribI4i(index, x, y, z, w);
}

//  void QOpenGLFunctions_4_4_Core::glVertexAttribI3i(GLuint index, GLint x,
//      GLint y, GLint z)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core17glVertexAttribI3iEjiii(
    QOpenGLFunctions_4_4_Core *self,
    GLuint index,
    GLint x,
    GLint y,
    GLint z) {
  self->glVertexAttribI3i(index, x, y, z);
}

//  void QOpenGLFunctions_4_4_Core::glVertexAttribI2i(GLuint index, GLint x,
//      GLint y)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core17glVertexAttribI2iEjii(
    QOpenGLFunctions_4_4_Core *self,
    GLuint index,
    GLint x,
    GLint y) {
  self->glVertexAttribI2i(index, x, y);
}

//  void QOpenGLFunctions_4_4_Core::glVertexAttribI1i(GLuint index, GLint x)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core17glVertexAttribI1iEji(
    QOpenGLFunctions_4_4_Core *self,
    GLuint index,
    GLint x) {
  self->glVertexAttribI1i(index, x);
}

//  void QOpenGLFunctions_4_4_Core::glEndConditionalRender()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core22glEndConditionalRenderEv(
    QOpenGLFunctions_4_4_Core *self) {
  self->glEndConditionalRender();
}

//  void QOpenGLFunctions_4_4_Core::glBeginConditionalRender(GLuint id,
//      GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core24glBeginConditionalRenderEjj(
    QOpenGLFunctions_4_4_Core *self,
    GLuint id,
    GLenum mode) {
  self->glBeginConditionalRender(id, mode);
}

//  void QOpenGLFunctions_4_4_Core::glClampColor(GLenum target, GLenum clamp)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core12glClampColorEjj(
    QOpenGLFunctions_4_4_Core *self,
    GLenum target,
    GLenum clamp) {
  self->glClampColor(target, clamp);
}

//  void QOpenGLFunctions_4_4_Core::glBindBufferBase(GLenum target, GLuint
//      index, GLuint buffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core16glBindBufferBaseEjjj(
    QOpenGLFunctions_4_4_Core *self,
    GLenum target,
    GLuint index,
    GLuint buffer) {
  self->glBindBufferBase(target, index, buffer);
}

//  void QOpenGLFunctions_4_4_Core::glEndTransformFeedback()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core22glEndTransformFeedbackEv(
    QOpenGLFunctions_4_4_Core *self) {
  self->glEndTransformFeedback();
}

//  void QOpenGLFunctions_4_4_Core::glBeginTransformFeedback(GLenum
//      primitiveMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core24glBeginTransformFeedbackEj(
    QOpenGLFunctions_4_4_Core *self,
    GLenum primitiveMode) {
  self->glBeginTransformFeedback(primitiveMode);
}

//  void QOpenGLFunctions_4_4_Core::glDisablei(GLenum target, GLuint index)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core10glDisableiEjj(
    QOpenGLFunctions_4_4_Core *self,
    GLenum target,
    GLuint index) {
  self->glDisablei(target, index);
}

//  void QOpenGLFunctions_4_4_Core::glEnablei(GLenum target, GLuint index)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core9glEnableiEjj(
    QOpenGLFunctions_4_4_Core *self,
    GLenum target,
    GLuint index) {
  self->glEnablei(target, index);
}

//  void QOpenGLFunctions_4_4_Core::glColorMaski(GLuint index, GLboolean r,
//      GLboolean g, GLboolean b, GLboolean a)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core12glColorMaskiEjhhhh(
    QOpenGLFunctions_4_4_Core *self,
    GLuint index,
    GLboolean r,
    GLboolean g,
    GLboolean b,
    GLboolean a) {
  self->glColorMaski(index, r, g, b, a);
}

//  void QOpenGLFunctions_4_4_Core::glUniformBlockBinding(GLuint program,
//      GLuint uniformBlockIndex, GLuint uniformBlockBinding)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core21glUniformBlockBindingEjjj(
    QOpenGLFunctions_4_4_Core *self,
    GLuint program,
    GLuint uniformBlockIndex,
    GLuint uniformBlockBinding) {
  self->glUniformBlockBinding(
      program,
      uniformBlockIndex,
      uniformBlockBinding);
}

//  void QOpenGLFunctions_4_4_Core::glPrimitiveRestartIndex(GLuint index)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core23glPrimitiveRestartIndexEj(
    QOpenGLFunctions_4_4_Core *self,
    GLuint index) {
  self->glPrimitiveRestartIndex(index);
}

//  void QOpenGLFunctions_4_4_Core::glTexBuffer(GLenum target, GLenum
//      internalformat, GLuint buffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core11glTexBufferEjjj(
    QOpenGLFunctions_4_4_Core *self,
    GLenum target,
    GLenum internalformat,
    GLuint buffer) {
  self->glTexBuffer(target, internalformat, buffer);
}

//  void QOpenGLFunctions_4_4_Core::glDrawArraysInstanced(GLenum mode, GLint
//      first, GLsizei count, GLsizei instancecount)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core21glDrawArraysInstancedEjiii(
    QOpenGLFunctions_4_4_Core *self,
    GLenum mode,
    GLint first,
    GLsizei count,
    GLsizei instancecount) {
  self->glDrawArraysInstanced(mode, first, count, instancecount);
}

//  void QOpenGLFunctions_4_4_Core::glSampleMaski(GLuint maskNumber,
//      GLbitfield mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core13glSampleMaskiEjj(
    QOpenGLFunctions_4_4_Core *self,
    GLuint maskNumber,
    GLbitfield mask) {
  self->glSampleMaski(maskNumber, mask);
}

//  void QOpenGLFunctions_4_4_Core::glTexImage3DMultisample(GLenum target,
//      GLsizei samples, GLenum internalformat, GLsizei width, GLsizei
//      height, GLsizei depth, GLboolean fixedsamplelocations)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core23glTexImage3DMultisampleEjijiiih(
    QOpenGLFunctions_4_4_Core *self,
    GLenum target,
    GLsizei samples,
    GLenum internalformat,
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

//  void QOpenGLFunctions_4_4_Core::glTexImage2DMultisample(GLenum target,
//      GLsizei samples, GLenum internalformat, GLsizei width, GLsizei
//      height, GLboolean fixedsamplelocations)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core23glTexImage2DMultisampleEjijiih(
    QOpenGLFunctions_4_4_Core *self,
    GLenum target,
    GLsizei samples,
    GLenum internalformat,
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

//  void QOpenGLFunctions_4_4_Core::glFramebufferTexture(GLenum target,
//      GLenum attachment, GLuint texture, GLint level)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core20glFramebufferTextureEjjji(
    QOpenGLFunctions_4_4_Core *self,
    GLenum target,
    GLenum attachment,
    GLuint texture,
    GLint level) {
  self->glFramebufferTexture(target, attachment, texture, level);
}

//  void QOpenGLFunctions_4_4_Core::glProvokingVertex(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core17glProvokingVertexEj(
    QOpenGLFunctions_4_4_Core *self,
    GLenum mode) {
  self->glProvokingVertex(mode);
}

//  void QOpenGLFunctions_4_4_Core::glVertexAttribP4ui(GLuint index, GLenum
//      type, GLboolean normalized, GLuint value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core18glVertexAttribP4uiEjjhj(
    QOpenGLFunctions_4_4_Core *self,
    GLuint index,
    GLenum type,
    GLboolean normalized,
    GLuint value) {
  self->glVertexAttribP4ui(index, type, normalized, value);
}

//  void QOpenGLFunctions_4_4_Core::glVertexAttribP3ui(GLuint index, GLenum
//      type, GLboolean normalized, GLuint value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core18glVertexAttribP3uiEjjhj(
    QOpenGLFunctions_4_4_Core *self,
    GLuint index,
    GLenum type,
    GLboolean normalized,
    GLuint value) {
  self->glVertexAttribP3ui(index, type, normalized, value);
}

//  void QOpenGLFunctions_4_4_Core::glVertexAttribP2ui(GLuint index, GLenum
//      type, GLboolean normalized, GLuint value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core18glVertexAttribP2uiEjjhj(
    QOpenGLFunctions_4_4_Core *self,
    GLuint index,
    GLenum type,
    GLboolean normalized,
    GLuint value) {
  self->glVertexAttribP2ui(index, type, normalized, value);
}

//  void QOpenGLFunctions_4_4_Core::glVertexAttribP1ui(GLuint index, GLenum
//      type, GLboolean normalized, GLuint value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core18glVertexAttribP1uiEjjhj(
    QOpenGLFunctions_4_4_Core *self,
    GLuint index,
    GLenum type,
    GLboolean normalized,
    GLuint value) {
  self->glVertexAttribP1ui(index, type, normalized, value);
}

//  void QOpenGLFunctions_4_4_Core::glVertexAttribDivisor(GLuint index,
//      GLuint divisor)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core21glVertexAttribDivisorEjj(
    QOpenGLFunctions_4_4_Core *self,
    GLuint index,
    GLuint divisor) {
  self->glVertexAttribDivisor(index, divisor);
}

//  void QOpenGLFunctions_4_4_Core::glQueryCounter(GLuint id, GLenum target)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core14glQueryCounterEjj(
    QOpenGLFunctions_4_4_Core *self,
    GLuint id,
    GLenum target) {
  self->glQueryCounter(id, target);
}

//  void QOpenGLFunctions_4_4_Core::glSamplerParameterf(GLuint sampler,
//      GLenum pname, GLfloat param)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core19glSamplerParameterfEjjf(
    QOpenGLFunctions_4_4_Core *self,
    GLuint sampler,
    GLenum pname,
    GLfloat param) {
  self->glSamplerParameterf(sampler, pname, param);
}

//  void QOpenGLFunctions_4_4_Core::glSamplerParameteri(GLuint sampler,
//      GLenum pname, GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core19glSamplerParameteriEjji(
    QOpenGLFunctions_4_4_Core *self,
    GLuint sampler,
    GLenum pname,
    GLint param) {
  self->glSamplerParameteri(sampler, pname, param);
}

//  void QOpenGLFunctions_4_4_Core::glBindSampler(GLuint unit, GLuint
//      sampler)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core13glBindSamplerEjj(
    QOpenGLFunctions_4_4_Core *self,
    GLuint unit,
    GLuint sampler) {
  self->glBindSampler(unit, sampler);
}

//  void QOpenGLFunctions_4_4_Core::glEndQueryIndexed(GLenum target, GLuint
//      index)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core17glEndQueryIndexedEjj(
    QOpenGLFunctions_4_4_Core *self,
    GLenum target,
    GLuint index) {
  self->glEndQueryIndexed(target, index);
}

//  void QOpenGLFunctions_4_4_Core::glBeginQueryIndexed(GLenum target, GLuint
//      index, GLuint id)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core19glBeginQueryIndexedEjjj(
    QOpenGLFunctions_4_4_Core *self,
    GLenum target,
    GLuint index,
    GLuint id) {
  self->glBeginQueryIndexed(target, index, id);
}

//  void QOpenGLFunctions_4_4_Core::glDrawTransformFeedbackStream(GLenum
//      mode, GLuint id, GLuint stream)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core29glDrawTransformFeedbackStreamEjjj(
    QOpenGLFunctions_4_4_Core *self,
    GLenum mode,
    GLuint id,
    GLuint stream) {
  self->glDrawTransformFeedbackStream(mode, id, stream);
}

//  void QOpenGLFunctions_4_4_Core::glDrawTransformFeedback(GLenum mode,
//      GLuint id)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core23glDrawTransformFeedbackEjj(
    QOpenGLFunctions_4_4_Core *self,
    GLenum mode,
    GLuint id) {
  self->glDrawTransformFeedback(mode, id);
}

//  void QOpenGLFunctions_4_4_Core::glResumeTransformFeedback()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core25glResumeTransformFeedbackEv(
    QOpenGLFunctions_4_4_Core *self) {
  self->glResumeTransformFeedback();
}

//  void QOpenGLFunctions_4_4_Core::glPauseTransformFeedback()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core24glPauseTransformFeedbackEv(
    QOpenGLFunctions_4_4_Core *self) {
  self->glPauseTransformFeedback();
}

//  void QOpenGLFunctions_4_4_Core::glBindTransformFeedback(GLenum target,
//      GLuint id)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core23glBindTransformFeedbackEjj(
    QOpenGLFunctions_4_4_Core *self,
    GLenum target,
    GLuint id) {
  self->glBindTransformFeedback(target, id);
}

//  void QOpenGLFunctions_4_4_Core::glPatchParameteri(GLenum pname, GLint
//      value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core17glPatchParameteriEji(
    QOpenGLFunctions_4_4_Core *self,
    GLenum pname,
    GLint value) {
  self->glPatchParameteri(pname, value);
}

//  void QOpenGLFunctions_4_4_Core::glUniform4d(GLint location, GLdouble x,
//      GLdouble y, GLdouble z, GLdouble w)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core11glUniform4dEidddd(
    QOpenGLFunctions_4_4_Core *self,
    GLint location,
    GLdouble x,
    GLdouble y,
    GLdouble z,
    GLdouble w) {
  self->glUniform4d(location, x, y, z, w);
}

//  void QOpenGLFunctions_4_4_Core::glUniform3d(GLint location, GLdouble x,
//      GLdouble y, GLdouble z)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core11glUniform3dEiddd(
    QOpenGLFunctions_4_4_Core *self,
    GLint location,
    GLdouble x,
    GLdouble y,
    GLdouble z) {
  self->glUniform3d(location, x, y, z);
}

//  void QOpenGLFunctions_4_4_Core::glUniform2d(GLint location, GLdouble x,
//      GLdouble y)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core11glUniform2dEidd(
    QOpenGLFunctions_4_4_Core *self,
    GLint location,
    GLdouble x,
    GLdouble y) {
  self->glUniform2d(location, x, y);
}

//  void QOpenGLFunctions_4_4_Core::glUniform1d(GLint location, GLdouble x)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core11glUniform1dEid(
    QOpenGLFunctions_4_4_Core *self,
    GLint location,
    GLdouble x) {
  self->glUniform1d(location, x);
}

//  void QOpenGLFunctions_4_4_Core::glBlendFuncSeparatei(GLuint buf, GLenum
//      srcRGB, GLenum dstRGB, GLenum srcAlpha, GLenum dstAlpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core20glBlendFuncSeparateiEjjjjj(
    QOpenGLFunctions_4_4_Core *self,
    GLuint buf,
    GLenum srcRGB,
    GLenum dstRGB,
    GLenum srcAlpha,
    GLenum dstAlpha) {
  self->glBlendFuncSeparatei(buf, srcRGB, dstRGB, srcAlpha, dstAlpha);
}

//  void QOpenGLFunctions_4_4_Core::glBlendFunci(GLuint buf, GLenum src,
//      GLenum dst)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core12glBlendFunciEjjj(
    QOpenGLFunctions_4_4_Core *self,
    GLuint buf,
    GLenum src,
    GLenum dst) {
  self->glBlendFunci(buf, src, dst);
}

//  void QOpenGLFunctions_4_4_Core::glBlendEquationSeparatei(GLuint buf,
//      GLenum modeRGB, GLenum modeAlpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core24glBlendEquationSeparateiEjjj(
    QOpenGLFunctions_4_4_Core *self,
    GLuint buf,
    GLenum modeRGB,
    GLenum modeAlpha) {
  self->glBlendEquationSeparatei(buf, modeRGB, modeAlpha);
}

//  void QOpenGLFunctions_4_4_Core::glBlendEquationi(GLuint buf, GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core16glBlendEquationiEjj(
    QOpenGLFunctions_4_4_Core *self,
    GLuint buf,
    GLenum mode) {
  self->glBlendEquationi(buf, mode);
}

//  void QOpenGLFunctions_4_4_Core::glMinSampleShading(GLfloat value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core18glMinSampleShadingEf(
    QOpenGLFunctions_4_4_Core *self,
    GLfloat value) {
  self->glMinSampleShading(value);
}

//  void QOpenGLFunctions_4_4_Core::glDepthRangeIndexed(GLuint index,
//      GLdouble n, GLdouble f)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core19glDepthRangeIndexedEjdd(
    QOpenGLFunctions_4_4_Core *self,
    GLuint index,
    GLdouble n,
    GLdouble f) {
  self->glDepthRangeIndexed(index, n, f);
}

//  void QOpenGLFunctions_4_4_Core::glScissorIndexed(GLuint index, GLint
//      left, GLint bottom, GLsizei width, GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core16glScissorIndexedEjiiii(
    QOpenGLFunctions_4_4_Core *self,
    GLuint index,
    GLint left,
    GLint bottom,
    GLsizei width,
    GLsizei height) {
  self->glScissorIndexed(index, left, bottom, width, height);
}

//  void QOpenGLFunctions_4_4_Core::glViewportIndexedf(GLuint index, GLfloat
//      x, GLfloat y, GLfloat w, GLfloat h)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core18glViewportIndexedfEjffff(
    QOpenGLFunctions_4_4_Core *self,
    GLuint index,
    GLfloat x,
    GLfloat y,
    GLfloat w,
    GLfloat h) {
  self->glViewportIndexedf(index, x, y, w, h);
}

//  void QOpenGLFunctions_4_4_Core::glVertexAttribL4d(GLuint index, GLdouble
//      x, GLdouble y, GLdouble z, GLdouble w)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core17glVertexAttribL4dEjdddd(
    QOpenGLFunctions_4_4_Core *self,
    GLuint index,
    GLdouble x,
    GLdouble y,
    GLdouble z,
    GLdouble w) {
  self->glVertexAttribL4d(index, x, y, z, w);
}

//  void QOpenGLFunctions_4_4_Core::glVertexAttribL3d(GLuint index, GLdouble
//      x, GLdouble y, GLdouble z)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core17glVertexAttribL3dEjddd(
    QOpenGLFunctions_4_4_Core *self,
    GLuint index,
    GLdouble x,
    GLdouble y,
    GLdouble z) {
  self->glVertexAttribL3d(index, x, y, z);
}

//  void QOpenGLFunctions_4_4_Core::glVertexAttribL2d(GLuint index, GLdouble
//      x, GLdouble y)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core17glVertexAttribL2dEjdd(
    QOpenGLFunctions_4_4_Core *self,
    GLuint index,
    GLdouble x,
    GLdouble y) {
  self->glVertexAttribL2d(index, x, y);
}

//  void QOpenGLFunctions_4_4_Core::glVertexAttribL1d(GLuint index, GLdouble
//      x)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core17glVertexAttribL1dEjd(
    QOpenGLFunctions_4_4_Core *self,
    GLuint index,
    GLdouble x) {
  self->glVertexAttribL1d(index, x);
}

//  void QOpenGLFunctions_4_4_Core::glValidateProgramPipeline(GLuint
//      pipeline)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core25glValidateProgramPipelineEj(
    QOpenGLFunctions_4_4_Core *self,
    GLuint pipeline) {
  self->glValidateProgramPipeline(pipeline);
}

//  void QOpenGLFunctions_4_4_Core::glProgramUniform4ui(GLuint program, GLint
//      location, GLuint v0, GLuint v1, GLuint v2, GLuint v3)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core19glProgramUniform4uiEjijjjj(
    QOpenGLFunctions_4_4_Core *self,
    GLuint program,
    GLint location,
    GLuint v0,
    GLuint v1,
    GLuint v2,
    GLuint v3) {
  self->glProgramUniform4ui(program, location, v0, v1, v2, v3);
}

//  void QOpenGLFunctions_4_4_Core::glProgramUniform4d(GLuint program, GLint
//      location, GLdouble v0, GLdouble v1, GLdouble v2, GLdouble v3)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core18glProgramUniform4dEjidddd(
    QOpenGLFunctions_4_4_Core *self,
    GLuint program,
    GLint location,
    GLdouble v0,
    GLdouble v1,
    GLdouble v2,
    GLdouble v3) {
  self->glProgramUniform4d(program, location, v0, v1, v2, v3);
}

//  void QOpenGLFunctions_4_4_Core::glProgramUniform4f(GLuint program, GLint
//      location, GLfloat v0, GLfloat v1, GLfloat v2, GLfloat v3)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core18glProgramUniform4fEjiffff(
    QOpenGLFunctions_4_4_Core *self,
    GLuint program,
    GLint location,
    GLfloat v0,
    GLfloat v1,
    GLfloat v2,
    GLfloat v3) {
  self->glProgramUniform4f(program, location, v0, v1, v2, v3);
}

//  void QOpenGLFunctions_4_4_Core::glProgramUniform4i(GLuint program, GLint
//      location, GLint v0, GLint v1, GLint v2, GLint v3)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core18glProgramUniform4iEjiiiii(
    QOpenGLFunctions_4_4_Core *self,
    GLuint program,
    GLint location,
    GLint v0,
    GLint v1,
    GLint v2,
    GLint v3) {
  self->glProgramUniform4i(program, location, v0, v1, v2, v3);
}

//  void QOpenGLFunctions_4_4_Core::glProgramUniform3ui(GLuint program, GLint
//      location, GLuint v0, GLuint v1, GLuint v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core19glProgramUniform3uiEjijjj(
    QOpenGLFunctions_4_4_Core *self,
    GLuint program,
    GLint location,
    GLuint v0,
    GLuint v1,
    GLuint v2) {
  self->glProgramUniform3ui(program, location, v0, v1, v2);
}

//  void QOpenGLFunctions_4_4_Core::glProgramUniform3d(GLuint program, GLint
//      location, GLdouble v0, GLdouble v1, GLdouble v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core18glProgramUniform3dEjiddd(
    QOpenGLFunctions_4_4_Core *self,
    GLuint program,
    GLint location,
    GLdouble v0,
    GLdouble v1,
    GLdouble v2) {
  self->glProgramUniform3d(program, location, v0, v1, v2);
}

//  void QOpenGLFunctions_4_4_Core::glProgramUniform3f(GLuint program, GLint
//      location, GLfloat v0, GLfloat v1, GLfloat v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core18glProgramUniform3fEjifff(
    QOpenGLFunctions_4_4_Core *self,
    GLuint program,
    GLint location,
    GLfloat v0,
    GLfloat v1,
    GLfloat v2) {
  self->glProgramUniform3f(program, location, v0, v1, v2);
}

//  void QOpenGLFunctions_4_4_Core::glProgramUniform3i(GLuint program, GLint
//      location, GLint v0, GLint v1, GLint v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core18glProgramUniform3iEjiiii(
    QOpenGLFunctions_4_4_Core *self,
    GLuint program,
    GLint location,
    GLint v0,
    GLint v1,
    GLint v2) {
  self->glProgramUniform3i(program, location, v0, v1, v2);
}

//  void QOpenGLFunctions_4_4_Core::glProgramUniform2ui(GLuint program, GLint
//      location, GLuint v0, GLuint v1)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core19glProgramUniform2uiEjijj(
    QOpenGLFunctions_4_4_Core *self,
    GLuint program,
    GLint location,
    GLuint v0,
    GLuint v1) {
  self->glProgramUniform2ui(program, location, v0, v1);
}

//  void QOpenGLFunctions_4_4_Core::glProgramUniform2d(GLuint program, GLint
//      location, GLdouble v0, GLdouble v1)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core18glProgramUniform2dEjidd(
    QOpenGLFunctions_4_4_Core *self,
    GLuint program,
    GLint location,
    GLdouble v0,
    GLdouble v1) {
  self->glProgramUniform2d(program, location, v0, v1);
}

//  void QOpenGLFunctions_4_4_Core::glProgramUniform2f(GLuint program, GLint
//      location, GLfloat v0, GLfloat v1)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core18glProgramUniform2fEjiff(
    QOpenGLFunctions_4_4_Core *self,
    GLuint program,
    GLint location,
    GLfloat v0,
    GLfloat v1) {
  self->glProgramUniform2f(program, location, v0, v1);
}

//  void QOpenGLFunctions_4_4_Core::glProgramUniform2i(GLuint program, GLint
//      location, GLint v0, GLint v1)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core18glProgramUniform2iEjiii(
    QOpenGLFunctions_4_4_Core *self,
    GLuint program,
    GLint location,
    GLint v0,
    GLint v1) {
  self->glProgramUniform2i(program, location, v0, v1);
}

//  void QOpenGLFunctions_4_4_Core::glProgramUniform1ui(GLuint program, GLint
//      location, GLuint v0)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core19glProgramUniform1uiEjij(
    QOpenGLFunctions_4_4_Core *self,
    GLuint program,
    GLint location,
    GLuint v0) {
  self->glProgramUniform1ui(program, location, v0);
}

//  void QOpenGLFunctions_4_4_Core::glProgramUniform1d(GLuint program, GLint
//      location, GLdouble v0)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core18glProgramUniform1dEjid(
    QOpenGLFunctions_4_4_Core *self,
    GLuint program,
    GLint location,
    GLdouble v0) {
  self->glProgramUniform1d(program, location, v0);
}

//  void QOpenGLFunctions_4_4_Core::glProgramUniform1f(GLuint program, GLint
//      location, GLfloat v0)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core18glProgramUniform1fEjif(
    QOpenGLFunctions_4_4_Core *self,
    GLuint program,
    GLint location,
    GLfloat v0) {
  self->glProgramUniform1f(program, location, v0);
}

//  void QOpenGLFunctions_4_4_Core::glProgramUniform1i(GLuint program, GLint
//      location, GLint v0)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core18glProgramUniform1iEjii(
    QOpenGLFunctions_4_4_Core *self,
    GLuint program,
    GLint location,
    GLint v0) {
  self->glProgramUniform1i(program, location, v0);
}

//  void QOpenGLFunctions_4_4_Core::glBindProgramPipeline(GLuint pipeline)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core21glBindProgramPipelineEj(
    QOpenGLFunctions_4_4_Core *self,
    GLuint pipeline) {
  self->glBindProgramPipeline(pipeline);
}

//  void QOpenGLFunctions_4_4_Core::glActiveShaderProgram(GLuint pipeline,
//      GLuint program)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core21glActiveShaderProgramEjj(
    QOpenGLFunctions_4_4_Core *self,
    GLuint pipeline,
    GLuint program) {
  self->glActiveShaderProgram(pipeline, program);
}

//  void QOpenGLFunctions_4_4_Core::glUseProgramStages(GLuint pipeline,
//      GLbitfield stages, GLuint program)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core18glUseProgramStagesEjjj(
    QOpenGLFunctions_4_4_Core *self,
    GLuint pipeline,
    GLbitfield stages,
    GLuint program) {
  self->glUseProgramStages(pipeline, stages, program);
}

//  void QOpenGLFunctions_4_4_Core::glProgramParameteri(GLuint program,
//      GLenum pname, GLint value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core19glProgramParameteriEjji(
    QOpenGLFunctions_4_4_Core *self,
    GLuint program,
    GLenum pname,
    GLint value) {
  self->glProgramParameteri(program, pname, value);
}

//  void QOpenGLFunctions_4_4_Core::glClearDepthf(GLfloat dd)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core13glClearDepthfEf(
    QOpenGLFunctions_4_4_Core *self,
    GLfloat dd) {
  self->glClearDepthf(dd);
}

//  void QOpenGLFunctions_4_4_Core::glDepthRangef(GLfloat n, GLfloat f)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core13glDepthRangefEff(
    QOpenGLFunctions_4_4_Core *self,
    GLfloat n,
    GLfloat f) {
  self->glDepthRangef(n, f);
}

//  void QOpenGLFunctions_4_4_Core::glReleaseShaderCompiler()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core23glReleaseShaderCompilerEv(
    QOpenGLFunctions_4_4_Core *self) {
  self->glReleaseShaderCompiler();
}

//  void
//      QOpenGLFunctions_4_4_Core::glDrawTransformFeedbackStreamInstanced(GLe
//      num mode, GLuint id, GLuint stream, GLsizei instancecount)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core38glDrawTransformFeedbackStreamInstancedEjjji(
    QOpenGLFunctions_4_4_Core *self,
    GLenum mode,
    GLuint id,
    GLuint stream,
    GLsizei instancecount) {
  self->glDrawTransformFeedbackStreamInstanced(
      mode,
      id,
      stream,
      instancecount);
}

//  void QOpenGLFunctions_4_4_Core::glDrawTransformFeedbackInstanced(GLenum
//      mode, GLuint id, GLsizei instancecount)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core32glDrawTransformFeedbackInstancedEjji(
    QOpenGLFunctions_4_4_Core *self,
    GLenum mode,
    GLuint id,
    GLsizei instancecount) {
  self->glDrawTransformFeedbackInstanced(mode, id, instancecount);
}

//  void QOpenGLFunctions_4_4_Core::glTexStorage3D(GLenum target, GLsizei
//      levels, GLenum internalformat, GLsizei width, GLsizei height, GLsizei
//      depth)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core14glTexStorage3DEjijiii(
    QOpenGLFunctions_4_4_Core *self,
    GLenum target,
    GLsizei levels,
    GLenum internalformat,
    GLsizei width,
    GLsizei height,
    GLsizei depth) {
  self->glTexStorage3D(target, levels, internalformat, width, height, depth);
}

//  void QOpenGLFunctions_4_4_Core::glTexStorage2D(GLenum target, GLsizei
//      levels, GLenum internalformat, GLsizei width, GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core14glTexStorage2DEjijii(
    QOpenGLFunctions_4_4_Core *self,
    GLenum target,
    GLsizei levels,
    GLenum internalformat,
    GLsizei width,
    GLsizei height) {
  self->glTexStorage2D(target, levels, internalformat, width, height);
}

//  void QOpenGLFunctions_4_4_Core::glTexStorage1D(GLenum target, GLsizei
//      levels, GLenum internalformat, GLsizei width)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core14glTexStorage1DEjiji(
    QOpenGLFunctions_4_4_Core *self,
    GLenum target,
    GLsizei levels,
    GLenum internalformat,
    GLsizei width) {
  self->glTexStorage1D(target, levels, internalformat, width);
}

//  void QOpenGLFunctions_4_4_Core::glMemoryBarrier(GLbitfield barriers)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core15glMemoryBarrierEj(
    QOpenGLFunctions_4_4_Core *self,
    GLbitfield barriers) {
  self->glMemoryBarrier(barriers);
}

//  void QOpenGLFunctions_4_4_Core::glBindImageTexture(GLuint unit, GLuint
//      texture, GLint level, GLboolean layered, GLint layer, GLenum access,
//      GLenum format)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core18glBindImageTextureEjjihijj(
    QOpenGLFunctions_4_4_Core *self,
    GLuint unit,
    GLuint texture,
    GLint level,
    GLboolean layered,
    GLint layer,
    GLenum access,
    GLenum format) {
  self->glBindImageTexture(
      unit,
      texture,
      level,
      layered,
      layer,
      access,
      format);
}

//  void QOpenGLFunctions_4_4_Core::glDrawArraysInstancedBaseInstance(GLenum
//      mode, GLint first, GLsizei count, GLsizei instancecount, GLuint
//      baseinstance)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core33glDrawArraysInstancedBaseInstanceEjiiij(
    QOpenGLFunctions_4_4_Core *self,
    GLenum mode,
    GLint first,
    GLsizei count,
    GLsizei instancecount,
    GLuint baseinstance) {
  self->glDrawArraysInstancedBaseInstance(
      mode,
      first,
      count,
      instancecount,
      baseinstance);
}

//  void QOpenGLFunctions_4_4_Core::glPopDebugGroup()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core15glPopDebugGroupEv(
    QOpenGLFunctions_4_4_Core *self) {
  self->glPopDebugGroup();
}

//  void QOpenGLFunctions_4_4_Core::glVertexBindingDivisor(GLuint
//      bindingindex, GLuint divisor)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core22glVertexBindingDivisorEjj(
    QOpenGLFunctions_4_4_Core *self,
    GLuint bindingindex,
    GLuint divisor) {
  self->glVertexBindingDivisor(bindingindex, divisor);
}

//  void QOpenGLFunctions_4_4_Core::glVertexAttribBinding(GLuint attribindex,
//      GLuint bindingindex)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core21glVertexAttribBindingEjj(
    QOpenGLFunctions_4_4_Core *self,
    GLuint attribindex,
    GLuint bindingindex) {
  self->glVertexAttribBinding(attribindex, bindingindex);
}

//  void QOpenGLFunctions_4_4_Core::glVertexAttribLFormat(GLuint attribindex,
//      GLint size, GLenum type, GLuint relativeoffset)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core21glVertexAttribLFormatEjijj(
    QOpenGLFunctions_4_4_Core *self,
    GLuint attribindex,
    GLint size,
    GLenum type,
    GLuint relativeoffset) {
  self->glVertexAttribLFormat(attribindex, size, type, relativeoffset);
}

//  void QOpenGLFunctions_4_4_Core::glVertexAttribIFormat(GLuint attribindex,
//      GLint size, GLenum type, GLuint relativeoffset)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core21glVertexAttribIFormatEjijj(
    QOpenGLFunctions_4_4_Core *self,
    GLuint attribindex,
    GLint size,
    GLenum type,
    GLuint relativeoffset) {
  self->glVertexAttribIFormat(attribindex, size, type, relativeoffset);
}

//  void QOpenGLFunctions_4_4_Core::glVertexAttribFormat(GLuint attribindex,
//      GLint size, GLenum type, GLboolean normalized, GLuint relativeoffset)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core20glVertexAttribFormatEjijhj(
    QOpenGLFunctions_4_4_Core *self,
    GLuint attribindex,
    GLint size,
    GLenum type,
    GLboolean normalized,
    GLuint relativeoffset) {
  self->glVertexAttribFormat(
      attribindex,
      size,
      type,
      normalized,
      relativeoffset);
}

//  void QOpenGLFunctions_4_4_Core::glTextureView(GLuint texture, GLenum
//      target, GLuint origtexture, GLenum internalformat, GLuint minlevel,
//      GLuint numlevels, GLuint minlayer, GLuint numlayers)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core13glTextureViewEjjjjjjjj(
    QOpenGLFunctions_4_4_Core *self,
    GLuint texture,
    GLenum target,
    GLuint origtexture,
    GLenum internalformat,
    GLuint minlevel,
    GLuint numlevels,
    GLuint minlayer,
    GLuint numlayers) {
  self->glTextureView(
      texture,
      target,
      origtexture,
      internalformat,
      minlevel,
      numlevels,
      minlayer,
      numlayers);
}

//  void QOpenGLFunctions_4_4_Core::glTexStorage3DMultisample(GLenum target,
//      GLsizei samples, GLenum internalformat, GLsizei width, GLsizei
//      height, GLsizei depth, GLboolean fixedsamplelocations)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core25glTexStorage3DMultisampleEjijiiih(
    QOpenGLFunctions_4_4_Core *self,
    GLenum target,
    GLsizei samples,
    GLenum internalformat,
    GLsizei width,
    GLsizei height,
    GLsizei depth,
    GLboolean fixedsamplelocations) {
  self->glTexStorage3DMultisample(
      target,
      samples,
      internalformat,
      width,
      height,
      depth,
      fixedsamplelocations);
}

//  void QOpenGLFunctions_4_4_Core::glTexStorage2DMultisample(GLenum target,
//      GLsizei samples, GLenum internalformat, GLsizei width, GLsizei
//      height, GLboolean fixedsamplelocations)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core25glTexStorage2DMultisampleEjijiih(
    QOpenGLFunctions_4_4_Core *self,
    GLenum target,
    GLsizei samples,
    GLenum internalformat,
    GLsizei width,
    GLsizei height,
    GLboolean fixedsamplelocations) {
  self->glTexStorage2DMultisample(
      target,
      samples,
      internalformat,
      width,
      height,
      fixedsamplelocations);
}

//  void QOpenGLFunctions_4_4_Core::glShaderStorageBlockBinding(GLuint
//      program, GLuint storageBlockIndex, GLuint storageBlockBinding)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core27glShaderStorageBlockBindingEjjj(
    QOpenGLFunctions_4_4_Core *self,
    GLuint program,
    GLuint storageBlockIndex,
    GLuint storageBlockBinding) {
  self->glShaderStorageBlockBinding(
      program,
      storageBlockIndex,
      storageBlockBinding);
}

//  void QOpenGLFunctions_4_4_Core::glInvalidateBufferData(GLuint buffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core22glInvalidateBufferDataEj(
    QOpenGLFunctions_4_4_Core *self,
    GLuint buffer) {
  self->glInvalidateBufferData(buffer);
}

//  void QOpenGLFunctions_4_4_Core::glInvalidateTexImage(GLuint texture,
//      GLint level)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core20glInvalidateTexImageEji(
    QOpenGLFunctions_4_4_Core *self,
    GLuint texture,
    GLint level) {
  self->glInvalidateTexImage(texture, level);
}

//  void QOpenGLFunctions_4_4_Core::glInvalidateTexSubImage(GLuint texture,
//      GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei
//      width, GLsizei height, GLsizei depth)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core23glInvalidateTexSubImageEjiiiiiii(
    QOpenGLFunctions_4_4_Core *self,
    GLuint texture,
    GLint level,
    GLint xoffset,
    GLint yoffset,
    GLint zoffset,
    GLsizei width,
    GLsizei height,
    GLsizei depth) {
  self->glInvalidateTexSubImage(
      texture,
      level,
      xoffset,
      yoffset,
      zoffset,
      width,
      height,
      depth);
}

//  void QOpenGLFunctions_4_4_Core::glFramebufferParameteri(GLenum target,
//      GLenum pname, GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core23glFramebufferParameteriEjji(
    QOpenGLFunctions_4_4_Core *self,
    GLenum target,
    GLenum pname,
    GLint param) {
  self->glFramebufferParameteri(target, pname, param);
}

//  void QOpenGLFunctions_4_4_Core::glCopyImageSubData(GLuint srcName, GLenum
//      srcTarget, GLint srcLevel, GLint srcX, GLint srcY, GLint srcZ, GLuint
//      dstName, GLenum dstTarget, GLint dstLevel, GLint dstX, GLint dstY,
//      GLint dstZ, GLsizei srcWidth, GLsizei srcHeight, GLsizei srcDepth)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core18glCopyImageSubDataEjjiiiijjiiiiiii(
    QOpenGLFunctions_4_4_Core *self,
    GLuint srcName,
    GLenum srcTarget,
    GLint srcLevel,
    GLint srcX,
    GLint srcY,
    GLint srcZ,
    GLuint dstName,
    GLenum dstTarget,
    GLint dstLevel,
    GLint dstX,
    GLint dstY,
    GLint dstZ,
    GLsizei srcWidth,
    GLsizei srcHeight,
    GLsizei srcDepth) {
  self->glCopyImageSubData(
      srcName,
      srcTarget,
      srcLevel,
      srcX,
      srcY,
      srcZ,
      dstName,
      dstTarget,
      dstLevel,
      dstX,
      dstY,
      dstZ,
      srcWidth,
      srcHeight,
      srcDepth);
}

//  void QOpenGLFunctions_4_4_Core::glDispatchCompute(GLuint num_groups_x,
//      GLuint num_groups_y, GLuint num_groups_z)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_4_Core17glDispatchComputeEjjj(
    QOpenGLFunctions_4_4_Core *self,
    GLuint num_groups_x,
    GLuint num_groups_y,
    GLuint num_groups_z) {
  self->glDispatchCompute(num_groups_x, num_groups_y, num_groups_z);
}

//  bool QOpenGLFunctions_4_4_Core::isContextCompatible(QOpenGLContext
//      *context)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QOpenGLFunctions_4_4_Core19isContextCompatibleEP14QOpenGLContext(
    QOpenGLContext *context) {
  return QOpenGLFunctions_4_4_Core::isContextCompatible(context);
}

//  QOpenGLVersionProfile QOpenGLFunctions_4_4_Core::versionProfile()
extern "C" Q_DECL_EXPORT
QOpenGLVersionProfile *ritual_ZN25QOpenGLFunctions_4_4_Core14versionProfileEv() {
  return new QOpenGLVersionProfile(
      QOpenGLFunctions_4_4_Core::versionProfile());
}

//  a Python function taken by a CuteQOpenGLFunctions_4_4_Core, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QOpenGLFunctions_4_4_Core(
    QOpenGLFunctions_4_4_Core *self,
    const char *key,
    void *call) {
  return static_cast<CuteQOpenGLFunctions_4_4_Core *>(self)->take(key, call);
}

//  bool QOpenGLFunctions_4_4_Core::initializeOpenGLFunctions()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN25QOpenGLFunctions_4_4_Core25initializeOpenGLFunctionsEv(
    QOpenGLFunctions_4_4_Core *self) {
  return self->QOpenGLFunctions_4_4_Core::initializeOpenGLFunctions();
}

#endif  // !defined(QT_NO_OPENGL) && !QT_CONFIG(opengles2)
