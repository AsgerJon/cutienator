//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/qopenglfunctions_1_5.h, Qt 6.12.0. Changes made here are lost.
#include <QtOpenGL/qtopenglglobal.h>
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

//  void QOpenGLFunctions_1_5::glIndexub(GLubyte c)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_59glIndexubEh(
    QOpenGLFunctions_1_5 *self,
    GLubyte c) {
  self->glIndexub(c);
}

//  void QOpenGLFunctions_1_5::glBindTexture(GLenum target, GLuint texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glBindTextureEjj(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLuint texture) {
  self->glBindTexture(target, texture);
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

//  void QOpenGLFunctions_1_5::glPointParameteri(GLenum pname, GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_517glPointParameteriEji(
    QOpenGLFunctions_1_5 *self,
    GLenum pname,
    GLint param) {
  self->glPointParameteri(pname, param);
}

//  void QOpenGLFunctions_1_5::glPointParameterf(GLenum pname, GLfloat param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_517glPointParameterfEjf(
    QOpenGLFunctions_1_5 *self,
    GLenum pname,
    GLfloat param) {
  self->glPointParameterf(pname, param);
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

//  void QOpenGLFunctions_1_5::glBindBuffer(GLenum target, GLuint buffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_512glBindBufferEjj(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLuint buffer) {
  self->glBindBuffer(target, buffer);
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

//  void QOpenGLFunctions_1_5::glMatrixMode(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_512glMatrixModeEj(
    QOpenGLFunctions_1_5 *self,
    GLenum mode) {
  self->glMatrixMode(mode);
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

//  void QOpenGLFunctions_1_5::glEvalCoord2f(GLfloat u, GLfloat v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glEvalCoord2fEff(
    QOpenGLFunctions_1_5 *self,
    GLfloat u,
    GLfloat v) {
  self->glEvalCoord2f(u, v);
}

//  void QOpenGLFunctions_1_5::glEvalCoord2d(GLdouble u, GLdouble v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glEvalCoord2dEdd(
    QOpenGLFunctions_1_5 *self,
    GLdouble u,
    GLdouble v) {
  self->glEvalCoord2d(u, v);
}

//  void QOpenGLFunctions_1_5::glEvalCoord1f(GLfloat u)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glEvalCoord1fEf(
    QOpenGLFunctions_1_5 *self,
    GLfloat u) {
  self->glEvalCoord1f(u);
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

//  void QOpenGLFunctions_1_5::glLightModeli(GLenum pname, GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glLightModeliEji(
    QOpenGLFunctions_1_5 *self,
    GLenum pname,
    GLint param) {
  self->glLightModeli(pname, param);
}

//  void QOpenGLFunctions_1_5::glLightModelf(GLenum pname, GLfloat param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glLightModelfEjf(
    QOpenGLFunctions_1_5 *self,
    GLenum pname,
    GLfloat param) {
  self->glLightModelf(pname, param);
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

//  void QOpenGLFunctions_1_5::glFogi(GLenum pname, GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_56glFogiEji(
    QOpenGLFunctions_1_5 *self,
    GLenum pname,
    GLint param) {
  self->glFogi(pname, param);
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

//  void QOpenGLFunctions_1_5::glVertex3s(GLshort x, GLshort y, GLshort z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_510glVertex3sEsss(
    QOpenGLFunctions_1_5 *self,
    GLshort x,
    GLshort y,
    GLshort z) {
  self->glVertex3s(x, y, z);
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

//  void QOpenGLFunctions_1_5::glVertex3f(GLfloat x, GLfloat y, GLfloat z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_510glVertex3fEfff(
    QOpenGLFunctions_1_5 *self,
    GLfloat x,
    GLfloat y,
    GLfloat z) {
  self->glVertex3f(x, y, z);
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

//  void QOpenGLFunctions_1_5::glVertex2s(GLshort x, GLshort y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_510glVertex2sEss(
    QOpenGLFunctions_1_5 *self,
    GLshort x,
    GLshort y) {
  self->glVertex2s(x, y);
}

//  void QOpenGLFunctions_1_5::glVertex2i(GLint x, GLint y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_510glVertex2iEii(
    QOpenGLFunctions_1_5 *self,
    GLint x,
    GLint y) {
  self->glVertex2i(x, y);
}

//  void QOpenGLFunctions_1_5::glVertex2f(GLfloat x, GLfloat y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_510glVertex2fEff(
    QOpenGLFunctions_1_5 *self,
    GLfloat x,
    GLfloat y) {
  self->glVertex2f(x, y);
}

//  void QOpenGLFunctions_1_5::glVertex2d(GLdouble x, GLdouble y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_510glVertex2dEdd(
    QOpenGLFunctions_1_5 *self,
    GLdouble x,
    GLdouble y) {
  self->glVertex2d(x, y);
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

//  void QOpenGLFunctions_1_5::glTexCoord3s(GLshort s, GLshort t, GLshort r)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_512glTexCoord3sEsss(
    QOpenGLFunctions_1_5 *self,
    GLshort s,
    GLshort t,
    GLshort r) {
  self->glTexCoord3s(s, t, r);
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

//  void QOpenGLFunctions_1_5::glTexCoord3f(GLfloat s, GLfloat t, GLfloat r)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_512glTexCoord3fEfff(
    QOpenGLFunctions_1_5 *self,
    GLfloat s,
    GLfloat t,
    GLfloat r) {
  self->glTexCoord3f(s, t, r);
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

//  void QOpenGLFunctions_1_5::glTexCoord2s(GLshort s, GLshort t)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_512glTexCoord2sEss(
    QOpenGLFunctions_1_5 *self,
    GLshort s,
    GLshort t) {
  self->glTexCoord2s(s, t);
}

//  void QOpenGLFunctions_1_5::glTexCoord2i(GLint s, GLint t)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_512glTexCoord2iEii(
    QOpenGLFunctions_1_5 *self,
    GLint s,
    GLint t) {
  self->glTexCoord2i(s, t);
}

//  void QOpenGLFunctions_1_5::glTexCoord2f(GLfloat s, GLfloat t)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_512glTexCoord2fEff(
    QOpenGLFunctions_1_5 *self,
    GLfloat s,
    GLfloat t) {
  self->glTexCoord2f(s, t);
}

//  void QOpenGLFunctions_1_5::glTexCoord2d(GLdouble s, GLdouble t)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_512glTexCoord2dEdd(
    QOpenGLFunctions_1_5 *self,
    GLdouble s,
    GLdouble t) {
  self->glTexCoord2d(s, t);
}

//  void QOpenGLFunctions_1_5::glTexCoord1s(GLshort s)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_512glTexCoord1sEs(
    QOpenGLFunctions_1_5 *self,
    GLshort s) {
  self->glTexCoord1s(s);
}

//  void QOpenGLFunctions_1_5::glTexCoord1i(GLint s)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_512glTexCoord1iEi(
    QOpenGLFunctions_1_5 *self,
    GLint s) {
  self->glTexCoord1i(s);
}

//  void QOpenGLFunctions_1_5::glTexCoord1f(GLfloat s)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_512glTexCoord1fEf(
    QOpenGLFunctions_1_5 *self,
    GLfloat s) {
  self->glTexCoord1f(s);
}

//  void QOpenGLFunctions_1_5::glTexCoord1d(GLdouble s)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_512glTexCoord1dEd(
    QOpenGLFunctions_1_5 *self,
    GLdouble s) {
  self->glTexCoord1d(s);
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

//  void QOpenGLFunctions_1_5::glRasterPos3s(GLshort x, GLshort y, GLshort z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glRasterPos3sEsss(
    QOpenGLFunctions_1_5 *self,
    GLshort x,
    GLshort y,
    GLshort z) {
  self->glRasterPos3s(x, y, z);
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

//  void QOpenGLFunctions_1_5::glRasterPos3f(GLfloat x, GLfloat y, GLfloat z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glRasterPos3fEfff(
    QOpenGLFunctions_1_5 *self,
    GLfloat x,
    GLfloat y,
    GLfloat z) {
  self->glRasterPos3f(x, y, z);
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

//  void QOpenGLFunctions_1_5::glRasterPos2s(GLshort x, GLshort y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glRasterPos2sEss(
    QOpenGLFunctions_1_5 *self,
    GLshort x,
    GLshort y) {
  self->glRasterPos2s(x, y);
}

//  void QOpenGLFunctions_1_5::glRasterPos2i(GLint x, GLint y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glRasterPos2iEii(
    QOpenGLFunctions_1_5 *self,
    GLint x,
    GLint y) {
  self->glRasterPos2i(x, y);
}

//  void QOpenGLFunctions_1_5::glRasterPos2f(GLfloat x, GLfloat y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glRasterPos2fEff(
    QOpenGLFunctions_1_5 *self,
    GLfloat x,
    GLfloat y) {
  self->glRasterPos2f(x, y);
}

//  void QOpenGLFunctions_1_5::glRasterPos2d(GLdouble x, GLdouble y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glRasterPos2dEdd(
    QOpenGLFunctions_1_5 *self,
    GLdouble x,
    GLdouble y) {
  self->glRasterPos2d(x, y);
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

//  void QOpenGLFunctions_1_5::glNormal3i(GLint nx, GLint ny, GLint nz)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_510glNormal3iEiii(
    QOpenGLFunctions_1_5 *self,
    GLint nx,
    GLint ny,
    GLint nz) {
  self->glNormal3i(nx, ny, nz);
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

//  void QOpenGLFunctions_1_5::glNormal3b(GLbyte nx, GLbyte ny, GLbyte nz)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_510glNormal3bEaaa(
    QOpenGLFunctions_1_5 *self,
    GLbyte nx,
    GLbyte ny,
    GLbyte nz) {
  self->glNormal3b(nx, ny, nz);
}

//  void QOpenGLFunctions_1_5::glIndexs(GLshort c)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_58glIndexsEs(
    QOpenGLFunctions_1_5 *self,
    GLshort c) {
  self->glIndexs(c);
}

//  void QOpenGLFunctions_1_5::glIndexi(GLint c)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_58glIndexiEi(
    QOpenGLFunctions_1_5 *self,
    GLint c) {
  self->glIndexi(c);
}

//  void QOpenGLFunctions_1_5::glIndexf(GLfloat c)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_58glIndexfEf(
    QOpenGLFunctions_1_5 *self,
    GLfloat c) {
  self->glIndexf(c);
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

//  void QOpenGLFunctions_1_5::glEdgeFlag(GLboolean flag)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_510glEdgeFlagEh(
    QOpenGLFunctions_1_5 *self,
    GLboolean flag) {
  self->glEdgeFlag(flag);
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

//  void QOpenGLFunctions_1_5::glColor3i(GLint red, GLint green, GLint blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_59glColor3iEiii(
    QOpenGLFunctions_1_5 *self,
    GLint red,
    GLint green,
    GLint blue) {
  self->glColor3i(red, green, blue);
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

//  void QOpenGLFunctions_1_5::glDeleteLists(GLuint list, GLsizei range)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glDeleteListsEji(
    QOpenGLFunctions_1_5 *self,
    GLuint list,
    GLsizei range) {
  self->glDeleteLists(list, range);
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

//  void QOpenGLFunctions_1_5::glEnableClientState(GLenum array)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_519glEnableClientStateEj(
    QOpenGLFunctions_1_5 *self,
    GLenum array) {
  self->glEnableClientState(array);
}

//  void QOpenGLFunctions_1_5::glDisableClientState(GLenum array)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_520glDisableClientStateEj(
    QOpenGLFunctions_1_5 *self,
    GLenum array) {
  self->glDisableClientState(array);
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

//  void QOpenGLFunctions_1_5::glMultiTexCoord1s(GLenum target, GLshort s)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_517glMultiTexCoord1sEjs(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLshort s) {
  self->glMultiTexCoord1s(target, s);
}

//  void QOpenGLFunctions_1_5::glMultiTexCoord1i(GLenum target, GLint s)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_517glMultiTexCoord1iEji(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLint s) {
  self->glMultiTexCoord1i(target, s);
}

//  void QOpenGLFunctions_1_5::glMultiTexCoord1f(GLenum target, GLfloat s)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_517glMultiTexCoord1fEjf(
    QOpenGLFunctions_1_5 *self,
    GLenum target,
    GLfloat s) {
  self->glMultiTexCoord1f(target, s);
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

//  void QOpenGLFunctions_1_5::glWindowPos3s(GLshort x, GLshort y, GLshort z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glWindowPos3sEsss(
    QOpenGLFunctions_1_5 *self,
    GLshort x,
    GLshort y,
    GLshort z) {
  self->glWindowPos3s(x, y, z);
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

//  void QOpenGLFunctions_1_5::glWindowPos3f(GLfloat x, GLfloat y, GLfloat z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glWindowPos3fEfff(
    QOpenGLFunctions_1_5 *self,
    GLfloat x,
    GLfloat y,
    GLfloat z) {
  self->glWindowPos3f(x, y, z);
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

//  void QOpenGLFunctions_1_5::glWindowPos2s(GLshort x, GLshort y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glWindowPos2sEss(
    QOpenGLFunctions_1_5 *self,
    GLshort x,
    GLshort y) {
  self->glWindowPos2s(x, y);
}

//  void QOpenGLFunctions_1_5::glWindowPos2i(GLint x, GLint y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glWindowPos2iEii(
    QOpenGLFunctions_1_5 *self,
    GLint x,
    GLint y) {
  self->glWindowPos2i(x, y);
}

//  void QOpenGLFunctions_1_5::glWindowPos2f(GLfloat x, GLfloat y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glWindowPos2fEff(
    QOpenGLFunctions_1_5 *self,
    GLfloat x,
    GLfloat y) {
  self->glWindowPos2f(x, y);
}

//  void QOpenGLFunctions_1_5::glWindowPos2d(GLdouble x, GLdouble y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_513glWindowPos2dEdd(
    QOpenGLFunctions_1_5 *self,
    GLdouble x,
    GLdouble y) {
  self->glWindowPos2d(x, y);
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

//  void QOpenGLFunctions_1_5::glFogCoordd(GLdouble coord)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_511glFogCoorddEd(
    QOpenGLFunctions_1_5 *self,
    GLdouble coord) {
  self->glFogCoordd(coord);
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
