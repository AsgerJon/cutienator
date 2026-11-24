//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/qopenglfunctions_1_1.h, Qt 6.12.0. Changes made here are lost.
#include <QtOpenGL/qtopenglglobal.h>
#if !defined(QT_NO_OPENGL) && !QT_CONFIG(opengles2)
#include <QtOpenGL/QtOpenGL>
#include <QtOpenGL/qopenglfunctions_1_1.h>
#include <QtOpenGL/qopenglversionprofile.h>
#include <cstring>

//  A QOpenGLFunctions_1_1 that Python can take functions over in. Every QOpenGLFunctions_1_1
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL) && !QT_CONFIG(opengles2)
typedef bool (*CuteQOpenGLFunctions_1_1Call0)(const void *, int *);
#endif  // !defined(QT_NO_OPENGL) && !QT_CONFIG(opengles2)
#endif  // !defined(QT_NO_OPENGL)
class CuteQOpenGLFunctions_1_1 : public QOpenGLFunctions_1_1 {
public:
  using QOpenGLFunctions_1_1::QOpenGLFunctions_1_1;
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
  //  bool QOpenGLFunctions_1_1::initializeOpenGLFunctions()
  bool initializeOpenGLFunctions() override {
    if (taken[0]) {
      int handled = 0;
      CuteQOpenGLFunctions_1_1Call0 call = reinterpret_cast<CuteQOpenGLFunctions_1_1Call0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QOpenGLFunctions_1_1::initializeOpenGLFunctions();
  }
#endif  // !defined(QT_NO_OPENGL) && !QT_CONFIG(opengles2)
#endif  // !defined(QT_NO_OPENGL)
};

//  QOpenGLFunctions_1_1::QOpenGLFunctions_1_1()
extern "C" Q_DECL_EXPORT
QOpenGLFunctions_1_1 *ritual_ZN20QOpenGLFunctions_1_1C1Ev() {
  return new CuteQOpenGLFunctions_1_1();
}

//  QOpenGLFunctions_1_1::~QOpenGLFunctions_1_1()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_1D1Ev(QOpenGLFunctions_1_1 *self) {
  delete self;
}

//  bool QOpenGLFunctions_1_1::initializeOpenGLFunctions()
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QOpenGLFunctions_1_125initializeOpenGLFunctionsEv(
    QOpenGLFunctions_1_1 *self) {
  return self->initializeOpenGLFunctions();
}

//  void QOpenGLFunctions_1_1::glViewport(GLint x, GLint y, GLsizei width,
//      GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_110glViewportEiiii(
    QOpenGLFunctions_1_1 *self,
    GLint x,
    GLint y,
    GLsizei width,
    GLsizei height) {
  self->glViewport(x, y, width, height);
}

//  void QOpenGLFunctions_1_1::glDepthRange(GLdouble nearVal, GLdouble
//      farVal)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_112glDepthRangeEdd(
    QOpenGLFunctions_1_1 *self,
    GLdouble nearVal,
    GLdouble farVal) {
  self->glDepthRange(nearVal, farVal);
}

//  void QOpenGLFunctions_1_1::glReadBuffer(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_112glReadBufferEj(
    QOpenGLFunctions_1_1 *self,
    GLenum mode) {
  self->glReadBuffer(mode);
}

//  void QOpenGLFunctions_1_1::glPixelStorei(GLenum pname, GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_113glPixelStoreiEji(
    QOpenGLFunctions_1_1 *self,
    GLenum pname,
    GLint param) {
  self->glPixelStorei(pname, param);
}

//  void QOpenGLFunctions_1_1::glPixelStoref(GLenum pname, GLfloat param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_113glPixelStorefEjf(
    QOpenGLFunctions_1_1 *self,
    GLenum pname,
    GLfloat param) {
  self->glPixelStoref(pname, param);
}

//  void QOpenGLFunctions_1_1::glDepthFunc(GLenum func)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_111glDepthFuncEj(
    QOpenGLFunctions_1_1 *self,
    GLenum func) {
  self->glDepthFunc(func);
}

//  void QOpenGLFunctions_1_1::glStencilOp(GLenum fail, GLenum zfail, GLenum
//      zpass)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_111glStencilOpEjjj(
    QOpenGLFunctions_1_1 *self,
    GLenum fail,
    GLenum zfail,
    GLenum zpass) {
  self->glStencilOp(fail, zfail, zpass);
}

//  void QOpenGLFunctions_1_1::glStencilFunc(GLenum func, GLint ref, GLuint
//      mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_113glStencilFuncEjij(
    QOpenGLFunctions_1_1 *self,
    GLenum func,
    GLint ref,
    GLuint mask) {
  self->glStencilFunc(func, ref, mask);
}

//  void QOpenGLFunctions_1_1::glLogicOp(GLenum opcode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_19glLogicOpEj(
    QOpenGLFunctions_1_1 *self,
    GLenum opcode) {
  self->glLogicOp(opcode);
}

//  void QOpenGLFunctions_1_1::glBlendFunc(GLenum sfactor, GLenum dfactor)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_111glBlendFuncEjj(
    QOpenGLFunctions_1_1 *self,
    GLenum sfactor,
    GLenum dfactor) {
  self->glBlendFunc(sfactor, dfactor);
}

//  void QOpenGLFunctions_1_1::glFlush()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_17glFlushEv(QOpenGLFunctions_1_1 *self) {
  self->glFlush();
}

//  void QOpenGLFunctions_1_1::glFinish()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_18glFinishEv(QOpenGLFunctions_1_1 *self) {
  self->glFinish();
}

//  void QOpenGLFunctions_1_1::glEnable(GLenum cap)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_18glEnableEj(
    QOpenGLFunctions_1_1 *self,
    GLenum cap) {
  self->glEnable(cap);
}

//  void QOpenGLFunctions_1_1::glDisable(GLenum cap)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_19glDisableEj(
    QOpenGLFunctions_1_1 *self,
    GLenum cap) {
  self->glDisable(cap);
}

//  void QOpenGLFunctions_1_1::glDepthMask(GLboolean flag)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_111glDepthMaskEh(
    QOpenGLFunctions_1_1 *self,
    GLboolean flag) {
  self->glDepthMask(flag);
}

//  void QOpenGLFunctions_1_1::glColorMask(GLboolean red, GLboolean green,
//      GLboolean blue, GLboolean alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_111glColorMaskEhhhh(
    QOpenGLFunctions_1_1 *self,
    GLboolean red,
    GLboolean green,
    GLboolean blue,
    GLboolean alpha) {
  self->glColorMask(red, green, blue, alpha);
}

//  void QOpenGLFunctions_1_1::glStencilMask(GLuint mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_113glStencilMaskEj(
    QOpenGLFunctions_1_1 *self,
    GLuint mask) {
  self->glStencilMask(mask);
}

//  void QOpenGLFunctions_1_1::glClearDepth(GLdouble depth)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_112glClearDepthEd(
    QOpenGLFunctions_1_1 *self,
    GLdouble depth) {
  self->glClearDepth(depth);
}

//  void QOpenGLFunctions_1_1::glClearStencil(GLint s)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_114glClearStencilEi(
    QOpenGLFunctions_1_1 *self,
    GLint s) {
  self->glClearStencil(s);
}

//  void QOpenGLFunctions_1_1::glClearColor(GLfloat red, GLfloat green,
//      GLfloat blue, GLfloat alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_112glClearColorEffff(
    QOpenGLFunctions_1_1 *self,
    GLfloat red,
    GLfloat green,
    GLfloat blue,
    GLfloat alpha) {
  self->glClearColor(red, green, blue, alpha);
}

//  void QOpenGLFunctions_1_1::glClear(GLbitfield mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_17glClearEj(
    QOpenGLFunctions_1_1 *self,
    GLbitfield mask) {
  self->glClear(mask);
}

//  void QOpenGLFunctions_1_1::glDrawBuffer(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_112glDrawBufferEj(
    QOpenGLFunctions_1_1 *self,
    GLenum mode) {
  self->glDrawBuffer(mode);
}

//  void QOpenGLFunctions_1_1::glTexParameteri(GLenum target, GLenum pname,
//      GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_115glTexParameteriEjji(
    QOpenGLFunctions_1_1 *self,
    GLenum target,
    GLenum pname,
    GLint param) {
  self->glTexParameteri(target, pname, param);
}

//  void QOpenGLFunctions_1_1::glTexParameterf(GLenum target, GLenum pname,
//      GLfloat param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_115glTexParameterfEjjf(
    QOpenGLFunctions_1_1 *self,
    GLenum target,
    GLenum pname,
    GLfloat param) {
  self->glTexParameterf(target, pname, param);
}

//  void QOpenGLFunctions_1_1::glScissor(GLint x, GLint y, GLsizei width,
//      GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_19glScissorEiiii(
    QOpenGLFunctions_1_1 *self,
    GLint x,
    GLint y,
    GLsizei width,
    GLsizei height) {
  self->glScissor(x, y, width, height);
}

//  void QOpenGLFunctions_1_1::glPolygonMode(GLenum face, GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_113glPolygonModeEjj(
    QOpenGLFunctions_1_1 *self,
    GLenum face,
    GLenum mode) {
  self->glPolygonMode(face, mode);
}

//  void QOpenGLFunctions_1_1::glPointSize(GLfloat size)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_111glPointSizeEf(
    QOpenGLFunctions_1_1 *self,
    GLfloat size) {
  self->glPointSize(size);
}

//  void QOpenGLFunctions_1_1::glLineWidth(GLfloat width)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_111glLineWidthEf(
    QOpenGLFunctions_1_1 *self,
    GLfloat width) {
  self->glLineWidth(width);
}

//  void QOpenGLFunctions_1_1::glHint(GLenum target, GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_16glHintEjj(
    QOpenGLFunctions_1_1 *self,
    GLenum target,
    GLenum mode) {
  self->glHint(target, mode);
}

//  void QOpenGLFunctions_1_1::glFrontFace(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_111glFrontFaceEj(
    QOpenGLFunctions_1_1 *self,
    GLenum mode) {
  self->glFrontFace(mode);
}

//  void QOpenGLFunctions_1_1::glCullFace(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_110glCullFaceEj(
    QOpenGLFunctions_1_1 *self,
    GLenum mode) {
  self->glCullFace(mode);
}

//  void QOpenGLFunctions_1_1::glIndexub(GLubyte c)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_19glIndexubEh(
    QOpenGLFunctions_1_1 *self,
    GLubyte c) {
  self->glIndexub(c);
}

//  void QOpenGLFunctions_1_1::glBindTexture(GLenum target, GLuint texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_113glBindTextureEjj(
    QOpenGLFunctions_1_1 *self,
    GLenum target,
    GLuint texture) {
  self->glBindTexture(target, texture);
}

//  void QOpenGLFunctions_1_1::glCopyTexSubImage2D(GLenum target, GLint
//      level, GLint xoffset, GLint yoffset, GLint x, GLint y, GLsizei width,
//      GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_119glCopyTexSubImage2DEjiiiiiii(
    QOpenGLFunctions_1_1 *self,
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

//  void QOpenGLFunctions_1_1::glCopyTexSubImage1D(GLenum target, GLint
//      level, GLint xoffset, GLint x, GLint y, GLsizei width)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_119glCopyTexSubImage1DEjiiiii(
    QOpenGLFunctions_1_1 *self,
    GLenum target,
    GLint level,
    GLint xoffset,
    GLint x,
    GLint y,
    GLsizei width) {
  self->glCopyTexSubImage1D(target, level, xoffset, x, y, width);
}

//  void QOpenGLFunctions_1_1::glCopyTexImage2D(GLenum target, GLint level,
//      GLenum internalformat, GLint x, GLint y, GLsizei width, GLsizei
//      height, GLint border)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_116glCopyTexImage2DEjijiiiii(
    QOpenGLFunctions_1_1 *self,
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

//  void QOpenGLFunctions_1_1::glCopyTexImage1D(GLenum target, GLint level,
//      GLenum internalformat, GLint x, GLint y, GLsizei width, GLint border)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_116glCopyTexImage1DEjijiiii(
    QOpenGLFunctions_1_1 *self,
    GLenum target,
    GLint level,
    GLenum internalformat,
    GLint x,
    GLint y,
    GLsizei width,
    GLint border) {
  self->glCopyTexImage1D(target, level, internalformat, x, y, width, border);
}

//  void QOpenGLFunctions_1_1::glPolygonOffset(GLfloat factor, GLfloat units)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_115glPolygonOffsetEff(
    QOpenGLFunctions_1_1 *self,
    GLfloat factor,
    GLfloat units) {
  self->glPolygonOffset(factor, units);
}

//  void QOpenGLFunctions_1_1::glDrawArrays(GLenum mode, GLint first, GLsizei
//      count)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_112glDrawArraysEjii(
    QOpenGLFunctions_1_1 *self,
    GLenum mode,
    GLint first,
    GLsizei count) {
  self->glDrawArrays(mode, first, count);
}

//  void QOpenGLFunctions_1_1::glTranslatef(GLfloat x, GLfloat y, GLfloat z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_112glTranslatefEfff(
    QOpenGLFunctions_1_1 *self,
    GLfloat x,
    GLfloat y,
    GLfloat z) {
  self->glTranslatef(x, y, z);
}

//  void QOpenGLFunctions_1_1::glTranslated(GLdouble x, GLdouble y, GLdouble
//      z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_112glTranslatedEddd(
    QOpenGLFunctions_1_1 *self,
    GLdouble x,
    GLdouble y,
    GLdouble z) {
  self->glTranslated(x, y, z);
}

//  void QOpenGLFunctions_1_1::glScalef(GLfloat x, GLfloat y, GLfloat z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_18glScalefEfff(
    QOpenGLFunctions_1_1 *self,
    GLfloat x,
    GLfloat y,
    GLfloat z) {
  self->glScalef(x, y, z);
}

//  void QOpenGLFunctions_1_1::glScaled(GLdouble x, GLdouble y, GLdouble z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_18glScaledEddd(
    QOpenGLFunctions_1_1 *self,
    GLdouble x,
    GLdouble y,
    GLdouble z) {
  self->glScaled(x, y, z);
}

//  void QOpenGLFunctions_1_1::glRotatef(GLfloat angle, GLfloat x, GLfloat y,
//      GLfloat z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_19glRotatefEffff(
    QOpenGLFunctions_1_1 *self,
    GLfloat angle,
    GLfloat x,
    GLfloat y,
    GLfloat z) {
  self->glRotatef(angle, x, y, z);
}

//  void QOpenGLFunctions_1_1::glRotated(GLdouble angle, GLdouble x, GLdouble
//      y, GLdouble z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_19glRotatedEdddd(
    QOpenGLFunctions_1_1 *self,
    GLdouble angle,
    GLdouble x,
    GLdouble y,
    GLdouble z) {
  self->glRotated(angle, x, y, z);
}

//  void QOpenGLFunctions_1_1::glPushMatrix()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_112glPushMatrixEv(
    QOpenGLFunctions_1_1 *self) {
  self->glPushMatrix();
}

//  void QOpenGLFunctions_1_1::glPopMatrix()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_111glPopMatrixEv(
    QOpenGLFunctions_1_1 *self) {
  self->glPopMatrix();
}

//  void QOpenGLFunctions_1_1::glOrtho(GLdouble left, GLdouble right,
//      GLdouble bottom, GLdouble top, GLdouble zNear, GLdouble zFar)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_17glOrthoEdddddd(
    QOpenGLFunctions_1_1 *self,
    GLdouble left,
    GLdouble right,
    GLdouble bottom,
    GLdouble top,
    GLdouble zNear,
    GLdouble zFar) {
  self->glOrtho(left, right, bottom, top, zNear, zFar);
}

//  void QOpenGLFunctions_1_1::glMatrixMode(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_112glMatrixModeEj(
    QOpenGLFunctions_1_1 *self,
    GLenum mode) {
  self->glMatrixMode(mode);
}

//  void QOpenGLFunctions_1_1::glLoadIdentity()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_114glLoadIdentityEv(
    QOpenGLFunctions_1_1 *self) {
  self->glLoadIdentity();
}

//  void QOpenGLFunctions_1_1::glFrustum(GLdouble left, GLdouble right,
//      GLdouble bottom, GLdouble top, GLdouble zNear, GLdouble zFar)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_19glFrustumEdddddd(
    QOpenGLFunctions_1_1 *self,
    GLdouble left,
    GLdouble right,
    GLdouble bottom,
    GLdouble top,
    GLdouble zNear,
    GLdouble zFar) {
  self->glFrustum(left, right, bottom, top, zNear, zFar);
}

//  void QOpenGLFunctions_1_1::glCopyPixels(GLint x, GLint y, GLsizei width,
//      GLsizei height, GLenum type)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_112glCopyPixelsEiiiij(
    QOpenGLFunctions_1_1 *self,
    GLint x,
    GLint y,
    GLsizei width,
    GLsizei height,
    GLenum type) {
  self->glCopyPixels(x, y, width, height, type);
}

//  void QOpenGLFunctions_1_1::glPixelTransferi(GLenum pname, GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_116glPixelTransferiEji(
    QOpenGLFunctions_1_1 *self,
    GLenum pname,
    GLint param) {
  self->glPixelTransferi(pname, param);
}

//  void QOpenGLFunctions_1_1::glPixelTransferf(GLenum pname, GLfloat param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_116glPixelTransferfEjf(
    QOpenGLFunctions_1_1 *self,
    GLenum pname,
    GLfloat param) {
  self->glPixelTransferf(pname, param);
}

//  void QOpenGLFunctions_1_1::glPixelZoom(GLfloat xfactor, GLfloat yfactor)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_111glPixelZoomEff(
    QOpenGLFunctions_1_1 *self,
    GLfloat xfactor,
    GLfloat yfactor) {
  self->glPixelZoom(xfactor, yfactor);
}

//  void QOpenGLFunctions_1_1::glAlphaFunc(GLenum func, GLfloat ref)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_111glAlphaFuncEjf(
    QOpenGLFunctions_1_1 *self,
    GLenum func,
    GLfloat ref) {
  self->glAlphaFunc(func, ref);
}

//  void QOpenGLFunctions_1_1::glEvalPoint2(GLint i, GLint j)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_112glEvalPoint2Eii(
    QOpenGLFunctions_1_1 *self,
    GLint i,
    GLint j) {
  self->glEvalPoint2(i, j);
}

//  void QOpenGLFunctions_1_1::glEvalMesh2(GLenum mode, GLint i1, GLint i2,
//      GLint j1, GLint j2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_111glEvalMesh2Ejiiii(
    QOpenGLFunctions_1_1 *self,
    GLenum mode,
    GLint i1,
    GLint i2,
    GLint j1,
    GLint j2) {
  self->glEvalMesh2(mode, i1, i2, j1, j2);
}

//  void QOpenGLFunctions_1_1::glEvalPoint1(GLint i)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_112glEvalPoint1Ei(
    QOpenGLFunctions_1_1 *self,
    GLint i) {
  self->glEvalPoint1(i);
}

//  void QOpenGLFunctions_1_1::glEvalMesh1(GLenum mode, GLint i1, GLint i2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_111glEvalMesh1Ejii(
    QOpenGLFunctions_1_1 *self,
    GLenum mode,
    GLint i1,
    GLint i2) {
  self->glEvalMesh1(mode, i1, i2);
}

//  void QOpenGLFunctions_1_1::glEvalCoord2f(GLfloat u, GLfloat v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_113glEvalCoord2fEff(
    QOpenGLFunctions_1_1 *self,
    GLfloat u,
    GLfloat v) {
  self->glEvalCoord2f(u, v);
}

//  void QOpenGLFunctions_1_1::glEvalCoord2d(GLdouble u, GLdouble v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_113glEvalCoord2dEdd(
    QOpenGLFunctions_1_1 *self,
    GLdouble u,
    GLdouble v) {
  self->glEvalCoord2d(u, v);
}

//  void QOpenGLFunctions_1_1::glEvalCoord1f(GLfloat u)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_113glEvalCoord1fEf(
    QOpenGLFunctions_1_1 *self,
    GLfloat u) {
  self->glEvalCoord1f(u);
}

//  void QOpenGLFunctions_1_1::glEvalCoord1d(GLdouble u)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_113glEvalCoord1dEd(
    QOpenGLFunctions_1_1 *self,
    GLdouble u) {
  self->glEvalCoord1d(u);
}

//  void QOpenGLFunctions_1_1::glMapGrid2f(GLint un, GLfloat u1, GLfloat u2,
//      GLint vn, GLfloat v1, GLfloat v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_111glMapGrid2fEiffiff(
    QOpenGLFunctions_1_1 *self,
    GLint un,
    GLfloat u1,
    GLfloat u2,
    GLint vn,
    GLfloat v1,
    GLfloat v2) {
  self->glMapGrid2f(un, u1, u2, vn, v1, v2);
}

//  void QOpenGLFunctions_1_1::glMapGrid2d(GLint un, GLdouble u1, GLdouble
//      u2, GLint vn, GLdouble v1, GLdouble v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_111glMapGrid2dEiddidd(
    QOpenGLFunctions_1_1 *self,
    GLint un,
    GLdouble u1,
    GLdouble u2,
    GLint vn,
    GLdouble v1,
    GLdouble v2) {
  self->glMapGrid2d(un, u1, u2, vn, v1, v2);
}

//  void QOpenGLFunctions_1_1::glMapGrid1f(GLint un, GLfloat u1, GLfloat u2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_111glMapGrid1fEiff(
    QOpenGLFunctions_1_1 *self,
    GLint un,
    GLfloat u1,
    GLfloat u2) {
  self->glMapGrid1f(un, u1, u2);
}

//  void QOpenGLFunctions_1_1::glMapGrid1d(GLint un, GLdouble u1, GLdouble
//      u2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_111glMapGrid1dEidd(
    QOpenGLFunctions_1_1 *self,
    GLint un,
    GLdouble u1,
    GLdouble u2) {
  self->glMapGrid1d(un, u1, u2);
}

//  void QOpenGLFunctions_1_1::glPushAttrib(GLbitfield mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_112glPushAttribEj(
    QOpenGLFunctions_1_1 *self,
    GLbitfield mask) {
  self->glPushAttrib(mask);
}

//  void QOpenGLFunctions_1_1::glPopAttrib()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_111glPopAttribEv(
    QOpenGLFunctions_1_1 *self) {
  self->glPopAttrib();
}

//  void QOpenGLFunctions_1_1::glAccum(GLenum op, GLfloat value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_17glAccumEjf(
    QOpenGLFunctions_1_1 *self,
    GLenum op,
    GLfloat value) {
  self->glAccum(op, value);
}

//  void QOpenGLFunctions_1_1::glIndexMask(GLuint mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_111glIndexMaskEj(
    QOpenGLFunctions_1_1 *self,
    GLuint mask) {
  self->glIndexMask(mask);
}

//  void QOpenGLFunctions_1_1::glClearIndex(GLfloat c)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_112glClearIndexEf(
    QOpenGLFunctions_1_1 *self,
    GLfloat c) {
  self->glClearIndex(c);
}

//  void QOpenGLFunctions_1_1::glClearAccum(GLfloat red, GLfloat green,
//      GLfloat blue, GLfloat alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_112glClearAccumEffff(
    QOpenGLFunctions_1_1 *self,
    GLfloat red,
    GLfloat green,
    GLfloat blue,
    GLfloat alpha) {
  self->glClearAccum(red, green, blue, alpha);
}

//  void QOpenGLFunctions_1_1::glPushName(GLuint name)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_110glPushNameEj(
    QOpenGLFunctions_1_1 *self,
    GLuint name) {
  self->glPushName(name);
}

//  void QOpenGLFunctions_1_1::glPopName()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_19glPopNameEv(
    QOpenGLFunctions_1_1 *self) {
  self->glPopName();
}

//  void QOpenGLFunctions_1_1::glPassThrough(GLfloat token)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_113glPassThroughEf(
    QOpenGLFunctions_1_1 *self,
    GLfloat token) {
  self->glPassThrough(token);
}

//  void QOpenGLFunctions_1_1::glLoadName(GLuint name)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_110glLoadNameEj(
    QOpenGLFunctions_1_1 *self,
    GLuint name) {
  self->glLoadName(name);
}

//  void QOpenGLFunctions_1_1::glInitNames()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_111glInitNamesEv(
    QOpenGLFunctions_1_1 *self) {
  self->glInitNames();
}

//  void QOpenGLFunctions_1_1::glTexGeni(GLenum coord, GLenum pname, GLint
//      param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_19glTexGeniEjji(
    QOpenGLFunctions_1_1 *self,
    GLenum coord,
    GLenum pname,
    GLint param) {
  self->glTexGeni(coord, pname, param);
}

//  void QOpenGLFunctions_1_1::glTexGenf(GLenum coord, GLenum pname, GLfloat
//      param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_19glTexGenfEjjf(
    QOpenGLFunctions_1_1 *self,
    GLenum coord,
    GLenum pname,
    GLfloat param) {
  self->glTexGenf(coord, pname, param);
}

//  void QOpenGLFunctions_1_1::glTexGend(GLenum coord, GLenum pname, GLdouble
//      param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_19glTexGendEjjd(
    QOpenGLFunctions_1_1 *self,
    GLenum coord,
    GLenum pname,
    GLdouble param) {
  self->glTexGend(coord, pname, param);
}

//  void QOpenGLFunctions_1_1::glTexEnvi(GLenum target, GLenum pname, GLint
//      param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_19glTexEnviEjji(
    QOpenGLFunctions_1_1 *self,
    GLenum target,
    GLenum pname,
    GLint param) {
  self->glTexEnvi(target, pname, param);
}

//  void QOpenGLFunctions_1_1::glTexEnvf(GLenum target, GLenum pname, GLfloat
//      param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_19glTexEnvfEjjf(
    QOpenGLFunctions_1_1 *self,
    GLenum target,
    GLenum pname,
    GLfloat param) {
  self->glTexEnvf(target, pname, param);
}

//  void QOpenGLFunctions_1_1::glShadeModel(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_112glShadeModelEj(
    QOpenGLFunctions_1_1 *self,
    GLenum mode) {
  self->glShadeModel(mode);
}

//  void QOpenGLFunctions_1_1::glMateriali(GLenum face, GLenum pname, GLint
//      param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_111glMaterialiEjji(
    QOpenGLFunctions_1_1 *self,
    GLenum face,
    GLenum pname,
    GLint param) {
  self->glMateriali(face, pname, param);
}

//  void QOpenGLFunctions_1_1::glMaterialf(GLenum face, GLenum pname, GLfloat
//      param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_111glMaterialfEjjf(
    QOpenGLFunctions_1_1 *self,
    GLenum face,
    GLenum pname,
    GLfloat param) {
  self->glMaterialf(face, pname, param);
}

//  void QOpenGLFunctions_1_1::glLineStipple(GLint factor, GLushort pattern)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_113glLineStippleEit(
    QOpenGLFunctions_1_1 *self,
    GLint factor,
    GLushort pattern) {
  self->glLineStipple(factor, pattern);
}

//  void QOpenGLFunctions_1_1::glLightModeli(GLenum pname, GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_113glLightModeliEji(
    QOpenGLFunctions_1_1 *self,
    GLenum pname,
    GLint param) {
  self->glLightModeli(pname, param);
}

//  void QOpenGLFunctions_1_1::glLightModelf(GLenum pname, GLfloat param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_113glLightModelfEjf(
    QOpenGLFunctions_1_1 *self,
    GLenum pname,
    GLfloat param) {
  self->glLightModelf(pname, param);
}

//  void QOpenGLFunctions_1_1::glLighti(GLenum light, GLenum pname, GLint
//      param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_18glLightiEjji(
    QOpenGLFunctions_1_1 *self,
    GLenum light,
    GLenum pname,
    GLint param) {
  self->glLighti(light, pname, param);
}

//  void QOpenGLFunctions_1_1::glLightf(GLenum light, GLenum pname, GLfloat
//      param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_18glLightfEjjf(
    QOpenGLFunctions_1_1 *self,
    GLenum light,
    GLenum pname,
    GLfloat param) {
  self->glLightf(light, pname, param);
}

//  void QOpenGLFunctions_1_1::glFogi(GLenum pname, GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_16glFogiEji(
    QOpenGLFunctions_1_1 *self,
    GLenum pname,
    GLint param) {
  self->glFogi(pname, param);
}

//  void QOpenGLFunctions_1_1::glFogf(GLenum pname, GLfloat param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_16glFogfEjf(
    QOpenGLFunctions_1_1 *self,
    GLenum pname,
    GLfloat param) {
  self->glFogf(pname, param);
}

//  void QOpenGLFunctions_1_1::glColorMaterial(GLenum face, GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_115glColorMaterialEjj(
    QOpenGLFunctions_1_1 *self,
    GLenum face,
    GLenum mode) {
  self->glColorMaterial(face, mode);
}

//  void QOpenGLFunctions_1_1::glVertex4s(GLshort x, GLshort y, GLshort z,
//      GLshort w)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_110glVertex4sEssss(
    QOpenGLFunctions_1_1 *self,
    GLshort x,
    GLshort y,
    GLshort z,
    GLshort w) {
  self->glVertex4s(x, y, z, w);
}

//  void QOpenGLFunctions_1_1::glVertex4i(GLint x, GLint y, GLint z, GLint w)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_110glVertex4iEiiii(
    QOpenGLFunctions_1_1 *self,
    GLint x,
    GLint y,
    GLint z,
    GLint w) {
  self->glVertex4i(x, y, z, w);
}

//  void QOpenGLFunctions_1_1::glVertex4f(GLfloat x, GLfloat y, GLfloat z,
//      GLfloat w)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_110glVertex4fEffff(
    QOpenGLFunctions_1_1 *self,
    GLfloat x,
    GLfloat y,
    GLfloat z,
    GLfloat w) {
  self->glVertex4f(x, y, z, w);
}

//  void QOpenGLFunctions_1_1::glVertex4d(GLdouble x, GLdouble y, GLdouble z,
//      GLdouble w)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_110glVertex4dEdddd(
    QOpenGLFunctions_1_1 *self,
    GLdouble x,
    GLdouble y,
    GLdouble z,
    GLdouble w) {
  self->glVertex4d(x, y, z, w);
}

//  void QOpenGLFunctions_1_1::glVertex3s(GLshort x, GLshort y, GLshort z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_110glVertex3sEsss(
    QOpenGLFunctions_1_1 *self,
    GLshort x,
    GLshort y,
    GLshort z) {
  self->glVertex3s(x, y, z);
}

//  void QOpenGLFunctions_1_1::glVertex3i(GLint x, GLint y, GLint z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_110glVertex3iEiii(
    QOpenGLFunctions_1_1 *self,
    GLint x,
    GLint y,
    GLint z) {
  self->glVertex3i(x, y, z);
}

//  void QOpenGLFunctions_1_1::glVertex3f(GLfloat x, GLfloat y, GLfloat z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_110glVertex3fEfff(
    QOpenGLFunctions_1_1 *self,
    GLfloat x,
    GLfloat y,
    GLfloat z) {
  self->glVertex3f(x, y, z);
}

//  void QOpenGLFunctions_1_1::glVertex3d(GLdouble x, GLdouble y, GLdouble z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_110glVertex3dEddd(
    QOpenGLFunctions_1_1 *self,
    GLdouble x,
    GLdouble y,
    GLdouble z) {
  self->glVertex3d(x, y, z);
}

//  void QOpenGLFunctions_1_1::glVertex2s(GLshort x, GLshort y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_110glVertex2sEss(
    QOpenGLFunctions_1_1 *self,
    GLshort x,
    GLshort y) {
  self->glVertex2s(x, y);
}

//  void QOpenGLFunctions_1_1::glVertex2i(GLint x, GLint y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_110glVertex2iEii(
    QOpenGLFunctions_1_1 *self,
    GLint x,
    GLint y) {
  self->glVertex2i(x, y);
}

//  void QOpenGLFunctions_1_1::glVertex2f(GLfloat x, GLfloat y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_110glVertex2fEff(
    QOpenGLFunctions_1_1 *self,
    GLfloat x,
    GLfloat y) {
  self->glVertex2f(x, y);
}

//  void QOpenGLFunctions_1_1::glVertex2d(GLdouble x, GLdouble y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_110glVertex2dEdd(
    QOpenGLFunctions_1_1 *self,
    GLdouble x,
    GLdouble y) {
  self->glVertex2d(x, y);
}

//  void QOpenGLFunctions_1_1::glTexCoord4s(GLshort s, GLshort t, GLshort r,
//      GLshort q)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_112glTexCoord4sEssss(
    QOpenGLFunctions_1_1 *self,
    GLshort s,
    GLshort t,
    GLshort r,
    GLshort q) {
  self->glTexCoord4s(s, t, r, q);
}

//  void QOpenGLFunctions_1_1::glTexCoord4i(GLint s, GLint t, GLint r, GLint
//      q)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_112glTexCoord4iEiiii(
    QOpenGLFunctions_1_1 *self,
    GLint s,
    GLint t,
    GLint r,
    GLint q) {
  self->glTexCoord4i(s, t, r, q);
}

//  void QOpenGLFunctions_1_1::glTexCoord4f(GLfloat s, GLfloat t, GLfloat r,
//      GLfloat q)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_112glTexCoord4fEffff(
    QOpenGLFunctions_1_1 *self,
    GLfloat s,
    GLfloat t,
    GLfloat r,
    GLfloat q) {
  self->glTexCoord4f(s, t, r, q);
}

//  void QOpenGLFunctions_1_1::glTexCoord4d(GLdouble s, GLdouble t, GLdouble
//      r, GLdouble q)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_112glTexCoord4dEdddd(
    QOpenGLFunctions_1_1 *self,
    GLdouble s,
    GLdouble t,
    GLdouble r,
    GLdouble q) {
  self->glTexCoord4d(s, t, r, q);
}

//  void QOpenGLFunctions_1_1::glTexCoord3s(GLshort s, GLshort t, GLshort r)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_112glTexCoord3sEsss(
    QOpenGLFunctions_1_1 *self,
    GLshort s,
    GLshort t,
    GLshort r) {
  self->glTexCoord3s(s, t, r);
}

//  void QOpenGLFunctions_1_1::glTexCoord3i(GLint s, GLint t, GLint r)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_112glTexCoord3iEiii(
    QOpenGLFunctions_1_1 *self,
    GLint s,
    GLint t,
    GLint r) {
  self->glTexCoord3i(s, t, r);
}

//  void QOpenGLFunctions_1_1::glTexCoord3f(GLfloat s, GLfloat t, GLfloat r)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_112glTexCoord3fEfff(
    QOpenGLFunctions_1_1 *self,
    GLfloat s,
    GLfloat t,
    GLfloat r) {
  self->glTexCoord3f(s, t, r);
}

//  void QOpenGLFunctions_1_1::glTexCoord3d(GLdouble s, GLdouble t, GLdouble
//      r)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_112glTexCoord3dEddd(
    QOpenGLFunctions_1_1 *self,
    GLdouble s,
    GLdouble t,
    GLdouble r) {
  self->glTexCoord3d(s, t, r);
}

//  void QOpenGLFunctions_1_1::glTexCoord2s(GLshort s, GLshort t)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_112glTexCoord2sEss(
    QOpenGLFunctions_1_1 *self,
    GLshort s,
    GLshort t) {
  self->glTexCoord2s(s, t);
}

//  void QOpenGLFunctions_1_1::glTexCoord2i(GLint s, GLint t)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_112glTexCoord2iEii(
    QOpenGLFunctions_1_1 *self,
    GLint s,
    GLint t) {
  self->glTexCoord2i(s, t);
}

//  void QOpenGLFunctions_1_1::glTexCoord2f(GLfloat s, GLfloat t)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_112glTexCoord2fEff(
    QOpenGLFunctions_1_1 *self,
    GLfloat s,
    GLfloat t) {
  self->glTexCoord2f(s, t);
}

//  void QOpenGLFunctions_1_1::glTexCoord2d(GLdouble s, GLdouble t)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_112glTexCoord2dEdd(
    QOpenGLFunctions_1_1 *self,
    GLdouble s,
    GLdouble t) {
  self->glTexCoord2d(s, t);
}

//  void QOpenGLFunctions_1_1::glTexCoord1s(GLshort s)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_112glTexCoord1sEs(
    QOpenGLFunctions_1_1 *self,
    GLshort s) {
  self->glTexCoord1s(s);
}

//  void QOpenGLFunctions_1_1::glTexCoord1i(GLint s)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_112glTexCoord1iEi(
    QOpenGLFunctions_1_1 *self,
    GLint s) {
  self->glTexCoord1i(s);
}

//  void QOpenGLFunctions_1_1::glTexCoord1f(GLfloat s)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_112glTexCoord1fEf(
    QOpenGLFunctions_1_1 *self,
    GLfloat s) {
  self->glTexCoord1f(s);
}

//  void QOpenGLFunctions_1_1::glTexCoord1d(GLdouble s)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_112glTexCoord1dEd(
    QOpenGLFunctions_1_1 *self,
    GLdouble s) {
  self->glTexCoord1d(s);
}

//  void QOpenGLFunctions_1_1::glRects(GLshort x1, GLshort y1, GLshort x2,
//      GLshort y2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_17glRectsEssss(
    QOpenGLFunctions_1_1 *self,
    GLshort x1,
    GLshort y1,
    GLshort x2,
    GLshort y2) {
  self->glRects(x1, y1, x2, y2);
}

//  void QOpenGLFunctions_1_1::glRecti(GLint x1, GLint y1, GLint x2, GLint
//      y2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_17glRectiEiiii(
    QOpenGLFunctions_1_1 *self,
    GLint x1,
    GLint y1,
    GLint x2,
    GLint y2) {
  self->glRecti(x1, y1, x2, y2);
}

//  void QOpenGLFunctions_1_1::glRectf(GLfloat x1, GLfloat y1, GLfloat x2,
//      GLfloat y2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_17glRectfEffff(
    QOpenGLFunctions_1_1 *self,
    GLfloat x1,
    GLfloat y1,
    GLfloat x2,
    GLfloat y2) {
  self->glRectf(x1, y1, x2, y2);
}

//  void QOpenGLFunctions_1_1::glRectd(GLdouble x1, GLdouble y1, GLdouble x2,
//      GLdouble y2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_17glRectdEdddd(
    QOpenGLFunctions_1_1 *self,
    GLdouble x1,
    GLdouble y1,
    GLdouble x2,
    GLdouble y2) {
  self->glRectd(x1, y1, x2, y2);
}

//  void QOpenGLFunctions_1_1::glRasterPos4s(GLshort x, GLshort y, GLshort z,
//      GLshort w)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_113glRasterPos4sEssss(
    QOpenGLFunctions_1_1 *self,
    GLshort x,
    GLshort y,
    GLshort z,
    GLshort w) {
  self->glRasterPos4s(x, y, z, w);
}

//  void QOpenGLFunctions_1_1::glRasterPos4i(GLint x, GLint y, GLint z, GLint
//      w)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_113glRasterPos4iEiiii(
    QOpenGLFunctions_1_1 *self,
    GLint x,
    GLint y,
    GLint z,
    GLint w) {
  self->glRasterPos4i(x, y, z, w);
}

//  void QOpenGLFunctions_1_1::glRasterPos4f(GLfloat x, GLfloat y, GLfloat z,
//      GLfloat w)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_113glRasterPos4fEffff(
    QOpenGLFunctions_1_1 *self,
    GLfloat x,
    GLfloat y,
    GLfloat z,
    GLfloat w) {
  self->glRasterPos4f(x, y, z, w);
}

//  void QOpenGLFunctions_1_1::glRasterPos4d(GLdouble x, GLdouble y, GLdouble
//      z, GLdouble w)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_113glRasterPos4dEdddd(
    QOpenGLFunctions_1_1 *self,
    GLdouble x,
    GLdouble y,
    GLdouble z,
    GLdouble w) {
  self->glRasterPos4d(x, y, z, w);
}

//  void QOpenGLFunctions_1_1::glRasterPos3s(GLshort x, GLshort y, GLshort z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_113glRasterPos3sEsss(
    QOpenGLFunctions_1_1 *self,
    GLshort x,
    GLshort y,
    GLshort z) {
  self->glRasterPos3s(x, y, z);
}

//  void QOpenGLFunctions_1_1::glRasterPos3i(GLint x, GLint y, GLint z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_113glRasterPos3iEiii(
    QOpenGLFunctions_1_1 *self,
    GLint x,
    GLint y,
    GLint z) {
  self->glRasterPos3i(x, y, z);
}

//  void QOpenGLFunctions_1_1::glRasterPos3f(GLfloat x, GLfloat y, GLfloat z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_113glRasterPos3fEfff(
    QOpenGLFunctions_1_1 *self,
    GLfloat x,
    GLfloat y,
    GLfloat z) {
  self->glRasterPos3f(x, y, z);
}

//  void QOpenGLFunctions_1_1::glRasterPos3d(GLdouble x, GLdouble y, GLdouble
//      z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_113glRasterPos3dEddd(
    QOpenGLFunctions_1_1 *self,
    GLdouble x,
    GLdouble y,
    GLdouble z) {
  self->glRasterPos3d(x, y, z);
}

//  void QOpenGLFunctions_1_1::glRasterPos2s(GLshort x, GLshort y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_113glRasterPos2sEss(
    QOpenGLFunctions_1_1 *self,
    GLshort x,
    GLshort y) {
  self->glRasterPos2s(x, y);
}

//  void QOpenGLFunctions_1_1::glRasterPos2i(GLint x, GLint y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_113glRasterPos2iEii(
    QOpenGLFunctions_1_1 *self,
    GLint x,
    GLint y) {
  self->glRasterPos2i(x, y);
}

//  void QOpenGLFunctions_1_1::glRasterPos2f(GLfloat x, GLfloat y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_113glRasterPos2fEff(
    QOpenGLFunctions_1_1 *self,
    GLfloat x,
    GLfloat y) {
  self->glRasterPos2f(x, y);
}

//  void QOpenGLFunctions_1_1::glRasterPos2d(GLdouble x, GLdouble y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_113glRasterPos2dEdd(
    QOpenGLFunctions_1_1 *self,
    GLdouble x,
    GLdouble y) {
  self->glRasterPos2d(x, y);
}

//  void QOpenGLFunctions_1_1::glNormal3s(GLshort nx, GLshort ny, GLshort nz)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_110glNormal3sEsss(
    QOpenGLFunctions_1_1 *self,
    GLshort nx,
    GLshort ny,
    GLshort nz) {
  self->glNormal3s(nx, ny, nz);
}

//  void QOpenGLFunctions_1_1::glNormal3i(GLint nx, GLint ny, GLint nz)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_110glNormal3iEiii(
    QOpenGLFunctions_1_1 *self,
    GLint nx,
    GLint ny,
    GLint nz) {
  self->glNormal3i(nx, ny, nz);
}

//  void QOpenGLFunctions_1_1::glNormal3f(GLfloat nx, GLfloat ny, GLfloat nz)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_110glNormal3fEfff(
    QOpenGLFunctions_1_1 *self,
    GLfloat nx,
    GLfloat ny,
    GLfloat nz) {
  self->glNormal3f(nx, ny, nz);
}

//  void QOpenGLFunctions_1_1::glNormal3d(GLdouble nx, GLdouble ny, GLdouble
//      nz)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_110glNormal3dEddd(
    QOpenGLFunctions_1_1 *self,
    GLdouble nx,
    GLdouble ny,
    GLdouble nz) {
  self->glNormal3d(nx, ny, nz);
}

//  void QOpenGLFunctions_1_1::glNormal3b(GLbyte nx, GLbyte ny, GLbyte nz)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_110glNormal3bEaaa(
    QOpenGLFunctions_1_1 *self,
    GLbyte nx,
    GLbyte ny,
    GLbyte nz) {
  self->glNormal3b(nx, ny, nz);
}

//  void QOpenGLFunctions_1_1::glIndexs(GLshort c)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_18glIndexsEs(
    QOpenGLFunctions_1_1 *self,
    GLshort c) {
  self->glIndexs(c);
}

//  void QOpenGLFunctions_1_1::glIndexi(GLint c)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_18glIndexiEi(
    QOpenGLFunctions_1_1 *self,
    GLint c) {
  self->glIndexi(c);
}

//  void QOpenGLFunctions_1_1::glIndexf(GLfloat c)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_18glIndexfEf(
    QOpenGLFunctions_1_1 *self,
    GLfloat c) {
  self->glIndexf(c);
}

//  void QOpenGLFunctions_1_1::glIndexd(GLdouble c)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_18glIndexdEd(
    QOpenGLFunctions_1_1 *self,
    GLdouble c) {
  self->glIndexd(c);
}

//  void QOpenGLFunctions_1_1::glEnd()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_15glEndEv(QOpenGLFunctions_1_1 *self) {
  self->glEnd();
}

//  void QOpenGLFunctions_1_1::glEdgeFlag(GLboolean flag)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_110glEdgeFlagEh(
    QOpenGLFunctions_1_1 *self,
    GLboolean flag) {
  self->glEdgeFlag(flag);
}

//  void QOpenGLFunctions_1_1::glColor4us(GLushort red, GLushort green,
//      GLushort blue, GLushort alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_110glColor4usEtttt(
    QOpenGLFunctions_1_1 *self,
    GLushort red,
    GLushort green,
    GLushort blue,
    GLushort alpha) {
  self->glColor4us(red, green, blue, alpha);
}

//  void QOpenGLFunctions_1_1::glColor4ui(GLuint red, GLuint green, GLuint
//      blue, GLuint alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_110glColor4uiEjjjj(
    QOpenGLFunctions_1_1 *self,
    GLuint red,
    GLuint green,
    GLuint blue,
    GLuint alpha) {
  self->glColor4ui(red, green, blue, alpha);
}

//  void QOpenGLFunctions_1_1::glColor4ub(GLubyte red, GLubyte green, GLubyte
//      blue, GLubyte alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_110glColor4ubEhhhh(
    QOpenGLFunctions_1_1 *self,
    GLubyte red,
    GLubyte green,
    GLubyte blue,
    GLubyte alpha) {
  self->glColor4ub(red, green, blue, alpha);
}

//  void QOpenGLFunctions_1_1::glColor4s(GLshort red, GLshort green, GLshort
//      blue, GLshort alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_19glColor4sEssss(
    QOpenGLFunctions_1_1 *self,
    GLshort red,
    GLshort green,
    GLshort blue,
    GLshort alpha) {
  self->glColor4s(red, green, blue, alpha);
}

//  void QOpenGLFunctions_1_1::glColor4i(GLint red, GLint green, GLint blue,
//      GLint alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_19glColor4iEiiii(
    QOpenGLFunctions_1_1 *self,
    GLint red,
    GLint green,
    GLint blue,
    GLint alpha) {
  self->glColor4i(red, green, blue, alpha);
}

//  void QOpenGLFunctions_1_1::glColor4f(GLfloat red, GLfloat green, GLfloat
//      blue, GLfloat alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_19glColor4fEffff(
    QOpenGLFunctions_1_1 *self,
    GLfloat red,
    GLfloat green,
    GLfloat blue,
    GLfloat alpha) {
  self->glColor4f(red, green, blue, alpha);
}

//  void QOpenGLFunctions_1_1::glColor4d(GLdouble red, GLdouble green,
//      GLdouble blue, GLdouble alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_19glColor4dEdddd(
    QOpenGLFunctions_1_1 *self,
    GLdouble red,
    GLdouble green,
    GLdouble blue,
    GLdouble alpha) {
  self->glColor4d(red, green, blue, alpha);
}

//  void QOpenGLFunctions_1_1::glColor4b(GLbyte red, GLbyte green, GLbyte
//      blue, GLbyte alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_19glColor4bEaaaa(
    QOpenGLFunctions_1_1 *self,
    GLbyte red,
    GLbyte green,
    GLbyte blue,
    GLbyte alpha) {
  self->glColor4b(red, green, blue, alpha);
}

//  void QOpenGLFunctions_1_1::glColor3us(GLushort red, GLushort green,
//      GLushort blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_110glColor3usEttt(
    QOpenGLFunctions_1_1 *self,
    GLushort red,
    GLushort green,
    GLushort blue) {
  self->glColor3us(red, green, blue);
}

//  void QOpenGLFunctions_1_1::glColor3ui(GLuint red, GLuint green, GLuint
//      blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_110glColor3uiEjjj(
    QOpenGLFunctions_1_1 *self,
    GLuint red,
    GLuint green,
    GLuint blue) {
  self->glColor3ui(red, green, blue);
}

//  void QOpenGLFunctions_1_1::glColor3ub(GLubyte red, GLubyte green, GLubyte
//      blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_110glColor3ubEhhh(
    QOpenGLFunctions_1_1 *self,
    GLubyte red,
    GLubyte green,
    GLubyte blue) {
  self->glColor3ub(red, green, blue);
}

//  void QOpenGLFunctions_1_1::glColor3s(GLshort red, GLshort green, GLshort
//      blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_19glColor3sEsss(
    QOpenGLFunctions_1_1 *self,
    GLshort red,
    GLshort green,
    GLshort blue) {
  self->glColor3s(red, green, blue);
}

//  void QOpenGLFunctions_1_1::glColor3i(GLint red, GLint green, GLint blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_19glColor3iEiii(
    QOpenGLFunctions_1_1 *self,
    GLint red,
    GLint green,
    GLint blue) {
  self->glColor3i(red, green, blue);
}

//  void QOpenGLFunctions_1_1::glColor3f(GLfloat red, GLfloat green, GLfloat
//      blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_19glColor3fEfff(
    QOpenGLFunctions_1_1 *self,
    GLfloat red,
    GLfloat green,
    GLfloat blue) {
  self->glColor3f(red, green, blue);
}

//  void QOpenGLFunctions_1_1::glColor3d(GLdouble red, GLdouble green,
//      GLdouble blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_19glColor3dEddd(
    QOpenGLFunctions_1_1 *self,
    GLdouble red,
    GLdouble green,
    GLdouble blue) {
  self->glColor3d(red, green, blue);
}

//  void QOpenGLFunctions_1_1::glColor3b(GLbyte red, GLbyte green, GLbyte
//      blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_19glColor3bEaaa(
    QOpenGLFunctions_1_1 *self,
    GLbyte red,
    GLbyte green,
    GLbyte blue) {
  self->glColor3b(red, green, blue);
}

//  void QOpenGLFunctions_1_1::glBegin(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_17glBeginEj(
    QOpenGLFunctions_1_1 *self,
    GLenum mode) {
  self->glBegin(mode);
}

//  void QOpenGLFunctions_1_1::glListBase(GLuint base)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_110glListBaseEj(
    QOpenGLFunctions_1_1 *self,
    GLuint base) {
  self->glListBase(base);
}

//  void QOpenGLFunctions_1_1::glDeleteLists(GLuint list, GLsizei range)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_113glDeleteListsEji(
    QOpenGLFunctions_1_1 *self,
    GLuint list,
    GLsizei range) {
  self->glDeleteLists(list, range);
}

//  void QOpenGLFunctions_1_1::glCallList(GLuint list)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_110glCallListEj(
    QOpenGLFunctions_1_1 *self,
    GLuint list) {
  self->glCallList(list);
}

//  void QOpenGLFunctions_1_1::glEndList()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_19glEndListEv(
    QOpenGLFunctions_1_1 *self) {
  self->glEndList();
}

//  void QOpenGLFunctions_1_1::glNewList(GLuint list, GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_19glNewListEjj(
    QOpenGLFunctions_1_1 *self,
    GLuint list,
    GLenum mode) {
  self->glNewList(list, mode);
}

//  void QOpenGLFunctions_1_1::glPushClientAttrib(GLbitfield mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_118glPushClientAttribEj(
    QOpenGLFunctions_1_1 *self,
    GLbitfield mask) {
  self->glPushClientAttrib(mask);
}

//  void QOpenGLFunctions_1_1::glPopClientAttrib()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_117glPopClientAttribEv(
    QOpenGLFunctions_1_1 *self) {
  self->glPopClientAttrib();
}

//  void QOpenGLFunctions_1_1::glEnableClientState(GLenum array)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_119glEnableClientStateEj(
    QOpenGLFunctions_1_1 *self,
    GLenum array) {
  self->glEnableClientState(array);
}

//  void QOpenGLFunctions_1_1::glDisableClientState(GLenum array)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_120glDisableClientStateEj(
    QOpenGLFunctions_1_1 *self,
    GLenum array) {
  self->glDisableClientState(array);
}

//  void QOpenGLFunctions_1_1::glArrayElement(GLint i)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_114glArrayElementEi(
    QOpenGLFunctions_1_1 *self,
    GLint i) {
  self->glArrayElement(i);
}

//  bool QOpenGLFunctions_1_1::isContextCompatible(QOpenGLContext *context)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QOpenGLFunctions_1_119isContextCompatibleEP14QOpenGLContext(
    QOpenGLContext *context) {
  return QOpenGLFunctions_1_1::isContextCompatible(context);
}

//  QOpenGLVersionProfile QOpenGLFunctions_1_1::versionProfile()
extern "C" Q_DECL_EXPORT
QOpenGLVersionProfile *ritual_ZN20QOpenGLFunctions_1_114versionProfileEv() {
  return new QOpenGLVersionProfile(QOpenGLFunctions_1_1::versionProfile());
}

//  a Python function taken by a CuteQOpenGLFunctions_1_1, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QOpenGLFunctions_1_1(
    QOpenGLFunctions_1_1 *self,
    const char *key,
    void *call) {
  return static_cast<CuteQOpenGLFunctions_1_1 *>(self)->take(key, call);
}

//  bool QOpenGLFunctions_1_1::initializeOpenGLFunctions()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN20QOpenGLFunctions_1_125initializeOpenGLFunctionsEv(
    QOpenGLFunctions_1_1 *self) {
  return self->QOpenGLFunctions_1_1::initializeOpenGLFunctions();
}

#endif  // !defined(QT_NO_OPENGL) && !QT_CONFIG(opengles2)
