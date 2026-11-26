//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/qopenglfunctions_1_0.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtOpenGL/qtopenglglobal.h>
#if !QT_CONFIG(opengles2)
#if !defined(QT_NO_OPENGL) && !QT_CONFIG(opengles2)
#include <QtOpenGL/QtOpenGL>
#include <QtOpenGL/qopenglfunctions_1_0.h>
#include <QtOpenGL/qopenglversionprofile.h>
#include <cstring>

//  A QOpenGLFunctions_1_0 that Python can take functions over in. Every QOpenGLFunctions_1_0
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL) && !QT_CONFIG(opengles2)
typedef bool (*CuteQOpenGLFunctions_1_0Call0)(const void *, int *);
#endif  // !defined(QT_NO_OPENGL) && !QT_CONFIG(opengles2)
#endif  // !defined(QT_NO_OPENGL)
class CuteQOpenGLFunctions_1_0 : public QOpenGLFunctions_1_0 {
public:
  using QOpenGLFunctions_1_0::QOpenGLFunctions_1_0;
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
  //  bool QOpenGLFunctions_1_0::initializeOpenGLFunctions()
  bool initializeOpenGLFunctions() override {
    if (taken[0]) {
      int handled = 0;
      CuteQOpenGLFunctions_1_0Call0 call = reinterpret_cast<CuteQOpenGLFunctions_1_0Call0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QOpenGLFunctions_1_0::initializeOpenGLFunctions();
  }
#endif  // !defined(QT_NO_OPENGL) && !QT_CONFIG(opengles2)
#endif  // !defined(QT_NO_OPENGL)
};

//  QOpenGLFunctions_1_0::QOpenGLFunctions_1_0()
extern "C" Q_DECL_EXPORT
QOpenGLFunctions_1_0 *ritual_ZN20QOpenGLFunctions_1_0C1Ev() {
  return new CuteQOpenGLFunctions_1_0();
}

//  QOpenGLFunctions_1_0::~QOpenGLFunctions_1_0()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_0D1Ev(QOpenGLFunctions_1_0 *self) {
  delete self;
}

//  bool QOpenGLFunctions_1_0::initializeOpenGLFunctions()
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QOpenGLFunctions_1_025initializeOpenGLFunctionsEv(
    QOpenGLFunctions_1_0 *self) {
  return self->initializeOpenGLFunctions();
}

//  void QOpenGLFunctions_1_0::glViewport(GLint x, GLint y, GLsizei width,
//      GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_010glViewportEiiii(
    QOpenGLFunctions_1_0 *self,
    GLint x,
    GLint y,
    GLsizei width,
    GLsizei height) {
  self->glViewport(x, y, width, height);
}

//  void QOpenGLFunctions_1_0::glDepthRange(GLdouble nearVal, GLdouble
//      farVal)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_012glDepthRangeEdd(
    QOpenGLFunctions_1_0 *self,
    GLdouble nearVal,
    GLdouble farVal) {
  self->glDepthRange(nearVal, farVal);
}

//  GLboolean QOpenGLFunctions_1_0::glIsEnabled(GLenum cap)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN20QOpenGLFunctions_1_011glIsEnabledEj(
    QOpenGLFunctions_1_0 *self,
    GLenum cap) {
  return self->glIsEnabled(cap);
}

//  void QOpenGLFunctions_1_0::glGetTexLevelParameteriv(GLenum target, GLint
//      level, GLenum pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_024glGetTexLevelParameterivEjijPi(
    QOpenGLFunctions_1_0 *self,
    GLenum target,
    GLint level,
    GLenum pname,
    GLint *params) {
  self->glGetTexLevelParameteriv(target, level, pname, params);
}

//  void QOpenGLFunctions_1_0::glGetTexLevelParameterfv(GLenum target, GLint
//      level, GLenum pname, GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_024glGetTexLevelParameterfvEjijPf(
    QOpenGLFunctions_1_0 *self,
    GLenum target,
    GLint level,
    GLenum pname,
    GLfloat *params) {
  self->glGetTexLevelParameterfv(target, level, pname, params);
}

//  void QOpenGLFunctions_1_0::glGetTexParameteriv(GLenum target, GLenum
//      pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_019glGetTexParameterivEjjPi(
    QOpenGLFunctions_1_0 *self,
    GLenum target,
    GLenum pname,
    GLint *params) {
  self->glGetTexParameteriv(target, pname, params);
}

//  void QOpenGLFunctions_1_0::glGetTexParameterfv(GLenum target, GLenum
//      pname, GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_019glGetTexParameterfvEjjPf(
    QOpenGLFunctions_1_0 *self,
    GLenum target,
    GLenum pname,
    GLfloat *params) {
  self->glGetTexParameterfv(target, pname, params);
}

//  void QOpenGLFunctions_1_0::glGetTexImage(GLenum target, GLint level,
//      GLenum format, GLenum type, GLvoid *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_013glGetTexImageEjijjPv(
    QOpenGLFunctions_1_0 *self,
    GLenum target,
    GLint level,
    GLenum format,
    GLenum type,
    GLvoid *pixels) {
  self->glGetTexImage(target, level, format, type, pixels);
}

//  const GLubyte *QOpenGLFunctions_1_0::glGetString(GLenum name)
extern "C" Q_DECL_EXPORT
const GLubyte *ritual_ZN20QOpenGLFunctions_1_011glGetStringEj(
    QOpenGLFunctions_1_0 *self,
    GLenum name) {
  return self->glGetString(name);
}

//  void QOpenGLFunctions_1_0::glGetIntegerv(GLenum pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_013glGetIntegervEjPi(
    QOpenGLFunctions_1_0 *self,
    GLenum pname,
    GLint *params) {
  self->glGetIntegerv(pname, params);
}

//  void QOpenGLFunctions_1_0::glGetFloatv(GLenum pname, GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_011glGetFloatvEjPf(
    QOpenGLFunctions_1_0 *self,
    GLenum pname,
    GLfloat *params) {
  self->glGetFloatv(pname, params);
}

//  GLenum QOpenGLFunctions_1_0::glGetError()
extern "C" Q_DECL_EXPORT
GLenum ritual_ZN20QOpenGLFunctions_1_010glGetErrorEv(
    QOpenGLFunctions_1_0 *self) {
  return self->glGetError();
}

//  void QOpenGLFunctions_1_0::glGetDoublev(GLenum pname, GLdouble *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_012glGetDoublevEjPd(
    QOpenGLFunctions_1_0 *self,
    GLenum pname,
    GLdouble *params) {
  self->glGetDoublev(pname, params);
}

//  void QOpenGLFunctions_1_0::glGetBooleanv(GLenum pname, GLboolean *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_013glGetBooleanvEjPh(
    QOpenGLFunctions_1_0 *self,
    GLenum pname,
    GLboolean *params) {
  self->glGetBooleanv(pname, params);
}

//  void QOpenGLFunctions_1_0::glReadPixels(GLint x, GLint y, GLsizei width,
//      GLsizei height, GLenum format, GLenum type, GLvoid *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_012glReadPixelsEiiiijjPv(
    QOpenGLFunctions_1_0 *self,
    GLint x,
    GLint y,
    GLsizei width,
    GLsizei height,
    GLenum format,
    GLenum type,
    GLvoid *pixels) {
  self->glReadPixels(x, y, width, height, format, type, pixels);
}

//  void QOpenGLFunctions_1_0::glReadBuffer(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_012glReadBufferEj(
    QOpenGLFunctions_1_0 *self,
    GLenum mode) {
  self->glReadBuffer(mode);
}

//  void QOpenGLFunctions_1_0::glPixelStorei(GLenum pname, GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_013glPixelStoreiEji(
    QOpenGLFunctions_1_0 *self,
    GLenum pname,
    GLint param) {
  self->glPixelStorei(pname, param);
}

//  void QOpenGLFunctions_1_0::glPixelStoref(GLenum pname, GLfloat param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_013glPixelStorefEjf(
    QOpenGLFunctions_1_0 *self,
    GLenum pname,
    GLfloat param) {
  self->glPixelStoref(pname, param);
}

//  void QOpenGLFunctions_1_0::glDepthFunc(GLenum func)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_011glDepthFuncEj(
    QOpenGLFunctions_1_0 *self,
    GLenum func) {
  self->glDepthFunc(func);
}

//  void QOpenGLFunctions_1_0::glStencilOp(GLenum fail, GLenum zfail, GLenum
//      zpass)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_011glStencilOpEjjj(
    QOpenGLFunctions_1_0 *self,
    GLenum fail,
    GLenum zfail,
    GLenum zpass) {
  self->glStencilOp(fail, zfail, zpass);
}

//  void QOpenGLFunctions_1_0::glStencilFunc(GLenum func, GLint ref, GLuint
//      mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_013glStencilFuncEjij(
    QOpenGLFunctions_1_0 *self,
    GLenum func,
    GLint ref,
    GLuint mask) {
  self->glStencilFunc(func, ref, mask);
}

//  void QOpenGLFunctions_1_0::glLogicOp(GLenum opcode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_09glLogicOpEj(
    QOpenGLFunctions_1_0 *self,
    GLenum opcode) {
  self->glLogicOp(opcode);
}

//  void QOpenGLFunctions_1_0::glBlendFunc(GLenum sfactor, GLenum dfactor)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_011glBlendFuncEjj(
    QOpenGLFunctions_1_0 *self,
    GLenum sfactor,
    GLenum dfactor) {
  self->glBlendFunc(sfactor, dfactor);
}

//  void QOpenGLFunctions_1_0::glFlush()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_07glFlushEv(QOpenGLFunctions_1_0 *self) {
  self->glFlush();
}

//  void QOpenGLFunctions_1_0::glFinish()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_08glFinishEv(QOpenGLFunctions_1_0 *self) {
  self->glFinish();
}

//  void QOpenGLFunctions_1_0::glEnable(GLenum cap)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_08glEnableEj(
    QOpenGLFunctions_1_0 *self,
    GLenum cap) {
  self->glEnable(cap);
}

//  void QOpenGLFunctions_1_0::glDisable(GLenum cap)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_09glDisableEj(
    QOpenGLFunctions_1_0 *self,
    GLenum cap) {
  self->glDisable(cap);
}

//  void QOpenGLFunctions_1_0::glDepthMask(GLboolean flag)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_011glDepthMaskEh(
    QOpenGLFunctions_1_0 *self,
    GLboolean flag) {
  self->glDepthMask(flag);
}

//  void QOpenGLFunctions_1_0::glColorMask(GLboolean red, GLboolean green,
//      GLboolean blue, GLboolean alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_011glColorMaskEhhhh(
    QOpenGLFunctions_1_0 *self,
    GLboolean red,
    GLboolean green,
    GLboolean blue,
    GLboolean alpha) {
  self->glColorMask(red, green, blue, alpha);
}

//  void QOpenGLFunctions_1_0::glStencilMask(GLuint mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_013glStencilMaskEj(
    QOpenGLFunctions_1_0 *self,
    GLuint mask) {
  self->glStencilMask(mask);
}

//  void QOpenGLFunctions_1_0::glClearDepth(GLdouble depth)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_012glClearDepthEd(
    QOpenGLFunctions_1_0 *self,
    GLdouble depth) {
  self->glClearDepth(depth);
}

//  void QOpenGLFunctions_1_0::glClearStencil(GLint s)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_014glClearStencilEi(
    QOpenGLFunctions_1_0 *self,
    GLint s) {
  self->glClearStencil(s);
}

//  void QOpenGLFunctions_1_0::glClearColor(GLfloat red, GLfloat green,
//      GLfloat blue, GLfloat alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_012glClearColorEffff(
    QOpenGLFunctions_1_0 *self,
    GLfloat red,
    GLfloat green,
    GLfloat blue,
    GLfloat alpha) {
  self->glClearColor(red, green, blue, alpha);
}

//  void QOpenGLFunctions_1_0::glClear(GLbitfield mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_07glClearEj(
    QOpenGLFunctions_1_0 *self,
    GLbitfield mask) {
  self->glClear(mask);
}

//  void QOpenGLFunctions_1_0::glDrawBuffer(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_012glDrawBufferEj(
    QOpenGLFunctions_1_0 *self,
    GLenum mode) {
  self->glDrawBuffer(mode);
}

//  void QOpenGLFunctions_1_0::glTexImage2D(GLenum target, GLint level, GLint
//      internalformat, GLsizei width, GLsizei height, GLint border, GLenum
//      format, GLenum type, const GLvoid *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_012glTexImage2DEjiiiiijjPKv(
    QOpenGLFunctions_1_0 *self,
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

//  void QOpenGLFunctions_1_0::glTexImage1D(GLenum target, GLint level, GLint
//      internalformat, GLsizei width, GLint border, GLenum format, GLenum
//      type, const GLvoid *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_012glTexImage1DEjiiiijjPKv(
    QOpenGLFunctions_1_0 *self,
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

//  void QOpenGLFunctions_1_0::glTexParameteriv(GLenum target, GLenum pname,
//      const GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_016glTexParameterivEjjPKi(
    QOpenGLFunctions_1_0 *self,
    GLenum target,
    GLenum pname,
    const GLint *params) {
  self->glTexParameteriv(target, pname, params);
}

//  void QOpenGLFunctions_1_0::glTexParameteri(GLenum target, GLenum pname,
//      GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_015glTexParameteriEjji(
    QOpenGLFunctions_1_0 *self,
    GLenum target,
    GLenum pname,
    GLint param) {
  self->glTexParameteri(target, pname, param);
}

//  void QOpenGLFunctions_1_0::glTexParameterfv(GLenum target, GLenum pname,
//      const GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_016glTexParameterfvEjjPKf(
    QOpenGLFunctions_1_0 *self,
    GLenum target,
    GLenum pname,
    const GLfloat *params) {
  self->glTexParameterfv(target, pname, params);
}

//  void QOpenGLFunctions_1_0::glTexParameterf(GLenum target, GLenum pname,
//      GLfloat param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_015glTexParameterfEjjf(
    QOpenGLFunctions_1_0 *self,
    GLenum target,
    GLenum pname,
    GLfloat param) {
  self->glTexParameterf(target, pname, param);
}

//  void QOpenGLFunctions_1_0::glScissor(GLint x, GLint y, GLsizei width,
//      GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_09glScissorEiiii(
    QOpenGLFunctions_1_0 *self,
    GLint x,
    GLint y,
    GLsizei width,
    GLsizei height) {
  self->glScissor(x, y, width, height);
}

//  void QOpenGLFunctions_1_0::glPolygonMode(GLenum face, GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_013glPolygonModeEjj(
    QOpenGLFunctions_1_0 *self,
    GLenum face,
    GLenum mode) {
  self->glPolygonMode(face, mode);
}

//  void QOpenGLFunctions_1_0::glPointSize(GLfloat size)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_011glPointSizeEf(
    QOpenGLFunctions_1_0 *self,
    GLfloat size) {
  self->glPointSize(size);
}

//  void QOpenGLFunctions_1_0::glLineWidth(GLfloat width)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_011glLineWidthEf(
    QOpenGLFunctions_1_0 *self,
    GLfloat width) {
  self->glLineWidth(width);
}

//  void QOpenGLFunctions_1_0::glHint(GLenum target, GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_06glHintEjj(
    QOpenGLFunctions_1_0 *self,
    GLenum target,
    GLenum mode) {
  self->glHint(target, mode);
}

//  void QOpenGLFunctions_1_0::glFrontFace(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_011glFrontFaceEj(
    QOpenGLFunctions_1_0 *self,
    GLenum mode) {
  self->glFrontFace(mode);
}

//  void QOpenGLFunctions_1_0::glCullFace(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_010glCullFaceEj(
    QOpenGLFunctions_1_0 *self,
    GLenum mode) {
  self->glCullFace(mode);
}

//  void QOpenGLFunctions_1_0::glTranslatef(GLfloat x, GLfloat y, GLfloat z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_012glTranslatefEfff(
    QOpenGLFunctions_1_0 *self,
    GLfloat x,
    GLfloat y,
    GLfloat z) {
  self->glTranslatef(x, y, z);
}

//  void QOpenGLFunctions_1_0::glTranslated(GLdouble x, GLdouble y, GLdouble
//      z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_012glTranslatedEddd(
    QOpenGLFunctions_1_0 *self,
    GLdouble x,
    GLdouble y,
    GLdouble z) {
  self->glTranslated(x, y, z);
}

//  void QOpenGLFunctions_1_0::glScalef(GLfloat x, GLfloat y, GLfloat z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_08glScalefEfff(
    QOpenGLFunctions_1_0 *self,
    GLfloat x,
    GLfloat y,
    GLfloat z) {
  self->glScalef(x, y, z);
}

//  void QOpenGLFunctions_1_0::glScaled(GLdouble x, GLdouble y, GLdouble z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_08glScaledEddd(
    QOpenGLFunctions_1_0 *self,
    GLdouble x,
    GLdouble y,
    GLdouble z) {
  self->glScaled(x, y, z);
}

//  void QOpenGLFunctions_1_0::glRotatef(GLfloat angle, GLfloat x, GLfloat y,
//      GLfloat z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_09glRotatefEffff(
    QOpenGLFunctions_1_0 *self,
    GLfloat angle,
    GLfloat x,
    GLfloat y,
    GLfloat z) {
  self->glRotatef(angle, x, y, z);
}

//  void QOpenGLFunctions_1_0::glRotated(GLdouble angle, GLdouble x, GLdouble
//      y, GLdouble z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_09glRotatedEdddd(
    QOpenGLFunctions_1_0 *self,
    GLdouble angle,
    GLdouble x,
    GLdouble y,
    GLdouble z) {
  self->glRotated(angle, x, y, z);
}

//  void QOpenGLFunctions_1_0::glPushMatrix()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_012glPushMatrixEv(
    QOpenGLFunctions_1_0 *self) {
  self->glPushMatrix();
}

//  void QOpenGLFunctions_1_0::glPopMatrix()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_011glPopMatrixEv(
    QOpenGLFunctions_1_0 *self) {
  self->glPopMatrix();
}

//  void QOpenGLFunctions_1_0::glOrtho(GLdouble left, GLdouble right,
//      GLdouble bottom, GLdouble top, GLdouble zNear, GLdouble zFar)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_07glOrthoEdddddd(
    QOpenGLFunctions_1_0 *self,
    GLdouble left,
    GLdouble right,
    GLdouble bottom,
    GLdouble top,
    GLdouble zNear,
    GLdouble zFar) {
  self->glOrtho(left, right, bottom, top, zNear, zFar);
}

//  void QOpenGLFunctions_1_0::glMultMatrixd(const GLdouble *m)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_013glMultMatrixdEPKd(
    QOpenGLFunctions_1_0 *self,
    const GLdouble *m) {
  self->glMultMatrixd(m);
}

//  void QOpenGLFunctions_1_0::glMultMatrixf(const GLfloat *m)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_013glMultMatrixfEPKf(
    QOpenGLFunctions_1_0 *self,
    const GLfloat *m) {
  self->glMultMatrixf(m);
}

//  void QOpenGLFunctions_1_0::glMatrixMode(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_012glMatrixModeEj(
    QOpenGLFunctions_1_0 *self,
    GLenum mode) {
  self->glMatrixMode(mode);
}

//  void QOpenGLFunctions_1_0::glLoadMatrixd(const GLdouble *m)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_013glLoadMatrixdEPKd(
    QOpenGLFunctions_1_0 *self,
    const GLdouble *m) {
  self->glLoadMatrixd(m);
}

//  void QOpenGLFunctions_1_0::glLoadMatrixf(const GLfloat *m)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_013glLoadMatrixfEPKf(
    QOpenGLFunctions_1_0 *self,
    const GLfloat *m) {
  self->glLoadMatrixf(m);
}

//  void QOpenGLFunctions_1_0::glLoadIdentity()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_014glLoadIdentityEv(
    QOpenGLFunctions_1_0 *self) {
  self->glLoadIdentity();
}

//  void QOpenGLFunctions_1_0::glFrustum(GLdouble left, GLdouble right,
//      GLdouble bottom, GLdouble top, GLdouble zNear, GLdouble zFar)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_09glFrustumEdddddd(
    QOpenGLFunctions_1_0 *self,
    GLdouble left,
    GLdouble right,
    GLdouble bottom,
    GLdouble top,
    GLdouble zNear,
    GLdouble zFar) {
  self->glFrustum(left, right, bottom, top, zNear, zFar);
}

//  GLboolean QOpenGLFunctions_1_0::glIsList(GLuint list)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN20QOpenGLFunctions_1_08glIsListEj(
    QOpenGLFunctions_1_0 *self,
    GLuint list) {
  return self->glIsList(list);
}

//  void QOpenGLFunctions_1_0::glGetTexGeniv(GLenum coord, GLenum pname,
//      GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_013glGetTexGenivEjjPi(
    QOpenGLFunctions_1_0 *self,
    GLenum coord,
    GLenum pname,
    GLint *params) {
  self->glGetTexGeniv(coord, pname, params);
}

//  void QOpenGLFunctions_1_0::glGetTexGenfv(GLenum coord, GLenum pname,
//      GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_013glGetTexGenfvEjjPf(
    QOpenGLFunctions_1_0 *self,
    GLenum coord,
    GLenum pname,
    GLfloat *params) {
  self->glGetTexGenfv(coord, pname, params);
}

//  void QOpenGLFunctions_1_0::glGetTexGendv(GLenum coord, GLenum pname,
//      GLdouble *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_013glGetTexGendvEjjPd(
    QOpenGLFunctions_1_0 *self,
    GLenum coord,
    GLenum pname,
    GLdouble *params) {
  self->glGetTexGendv(coord, pname, params);
}

//  void QOpenGLFunctions_1_0::glGetTexEnviv(GLenum target, GLenum pname,
//      GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_013glGetTexEnvivEjjPi(
    QOpenGLFunctions_1_0 *self,
    GLenum target,
    GLenum pname,
    GLint *params) {
  self->glGetTexEnviv(target, pname, params);
}

//  void QOpenGLFunctions_1_0::glGetTexEnvfv(GLenum target, GLenum pname,
//      GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_013glGetTexEnvfvEjjPf(
    QOpenGLFunctions_1_0 *self,
    GLenum target,
    GLenum pname,
    GLfloat *params) {
  self->glGetTexEnvfv(target, pname, params);
}

//  void QOpenGLFunctions_1_0::glGetPolygonStipple(GLubyte *mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_019glGetPolygonStippleEPh(
    QOpenGLFunctions_1_0 *self,
    GLubyte *mask) {
  self->glGetPolygonStipple(mask);
}

//  void QOpenGLFunctions_1_0::glGetPixelMapusv(GLenum map, GLushort *values)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_016glGetPixelMapusvEjPt(
    QOpenGLFunctions_1_0 *self,
    GLenum map,
    GLushort *values) {
  self->glGetPixelMapusv(map, values);
}

//  void QOpenGLFunctions_1_0::glGetPixelMapuiv(GLenum map, GLuint *values)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_016glGetPixelMapuivEjPj(
    QOpenGLFunctions_1_0 *self,
    GLenum map,
    GLuint *values) {
  self->glGetPixelMapuiv(map, values);
}

//  void QOpenGLFunctions_1_0::glGetPixelMapfv(GLenum map, GLfloat *values)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_015glGetPixelMapfvEjPf(
    QOpenGLFunctions_1_0 *self,
    GLenum map,
    GLfloat *values) {
  self->glGetPixelMapfv(map, values);
}

//  void QOpenGLFunctions_1_0::glGetMaterialiv(GLenum face, GLenum pname,
//      GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_015glGetMaterialivEjjPi(
    QOpenGLFunctions_1_0 *self,
    GLenum face,
    GLenum pname,
    GLint *params) {
  self->glGetMaterialiv(face, pname, params);
}

//  void QOpenGLFunctions_1_0::glGetMaterialfv(GLenum face, GLenum pname,
//      GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_015glGetMaterialfvEjjPf(
    QOpenGLFunctions_1_0 *self,
    GLenum face,
    GLenum pname,
    GLfloat *params) {
  self->glGetMaterialfv(face, pname, params);
}

//  void QOpenGLFunctions_1_0::glGetMapiv(GLenum target, GLenum query, GLint
//      *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_010glGetMapivEjjPi(
    QOpenGLFunctions_1_0 *self,
    GLenum target,
    GLenum query,
    GLint *v) {
  self->glGetMapiv(target, query, v);
}

//  void QOpenGLFunctions_1_0::glGetMapfv(GLenum target, GLenum query,
//      GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_010glGetMapfvEjjPf(
    QOpenGLFunctions_1_0 *self,
    GLenum target,
    GLenum query,
    GLfloat *v) {
  self->glGetMapfv(target, query, v);
}

//  void QOpenGLFunctions_1_0::glGetMapdv(GLenum target, GLenum query,
//      GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_010glGetMapdvEjjPd(
    QOpenGLFunctions_1_0 *self,
    GLenum target,
    GLenum query,
    GLdouble *v) {
  self->glGetMapdv(target, query, v);
}

//  void QOpenGLFunctions_1_0::glGetLightiv(GLenum light, GLenum pname, GLint
//      *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_012glGetLightivEjjPi(
    QOpenGLFunctions_1_0 *self,
    GLenum light,
    GLenum pname,
    GLint *params) {
  self->glGetLightiv(light, pname, params);
}

//  void QOpenGLFunctions_1_0::glGetLightfv(GLenum light, GLenum pname,
//      GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_012glGetLightfvEjjPf(
    QOpenGLFunctions_1_0 *self,
    GLenum light,
    GLenum pname,
    GLfloat *params) {
  self->glGetLightfv(light, pname, params);
}

//  void QOpenGLFunctions_1_0::glGetClipPlane(GLenum plane, GLdouble
//      *equation)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_014glGetClipPlaneEjPd(
    QOpenGLFunctions_1_0 *self,
    GLenum plane,
    GLdouble *equation) {
  self->glGetClipPlane(plane, equation);
}

//  void QOpenGLFunctions_1_0::glDrawPixels(GLsizei width, GLsizei height,
//      GLenum format, GLenum type, const GLvoid *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_012glDrawPixelsEiijjPKv(
    QOpenGLFunctions_1_0 *self,
    GLsizei width,
    GLsizei height,
    GLenum format,
    GLenum type,
    const GLvoid *pixels) {
  self->glDrawPixels(width, height, format, type, pixels);
}

//  void QOpenGLFunctions_1_0::glCopyPixels(GLint x, GLint y, GLsizei width,
//      GLsizei height, GLenum type)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_012glCopyPixelsEiiiij(
    QOpenGLFunctions_1_0 *self,
    GLint x,
    GLint y,
    GLsizei width,
    GLsizei height,
    GLenum type) {
  self->glCopyPixels(x, y, width, height, type);
}

//  void QOpenGLFunctions_1_0::glPixelMapusv(GLenum map, GLint mapsize, const
//      GLushort *values)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_013glPixelMapusvEjiPKt(
    QOpenGLFunctions_1_0 *self,
    GLenum map,
    GLint mapsize,
    const GLushort *values) {
  self->glPixelMapusv(map, mapsize, values);
}

//  void QOpenGLFunctions_1_0::glPixelMapuiv(GLenum map, GLint mapsize, const
//      GLuint *values)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_013glPixelMapuivEjiPKj(
    QOpenGLFunctions_1_0 *self,
    GLenum map,
    GLint mapsize,
    const GLuint *values) {
  self->glPixelMapuiv(map, mapsize, values);
}

//  void QOpenGLFunctions_1_0::glPixelMapfv(GLenum map, GLint mapsize, const
//      GLfloat *values)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_012glPixelMapfvEjiPKf(
    QOpenGLFunctions_1_0 *self,
    GLenum map,
    GLint mapsize,
    const GLfloat *values) {
  self->glPixelMapfv(map, mapsize, values);
}

//  void QOpenGLFunctions_1_0::glPixelTransferi(GLenum pname, GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_016glPixelTransferiEji(
    QOpenGLFunctions_1_0 *self,
    GLenum pname,
    GLint param) {
  self->glPixelTransferi(pname, param);
}

//  void QOpenGLFunctions_1_0::glPixelTransferf(GLenum pname, GLfloat param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_016glPixelTransferfEjf(
    QOpenGLFunctions_1_0 *self,
    GLenum pname,
    GLfloat param) {
  self->glPixelTransferf(pname, param);
}

//  void QOpenGLFunctions_1_0::glPixelZoom(GLfloat xfactor, GLfloat yfactor)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_011glPixelZoomEff(
    QOpenGLFunctions_1_0 *self,
    GLfloat xfactor,
    GLfloat yfactor) {
  self->glPixelZoom(xfactor, yfactor);
}

//  void QOpenGLFunctions_1_0::glAlphaFunc(GLenum func, GLfloat ref)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_011glAlphaFuncEjf(
    QOpenGLFunctions_1_0 *self,
    GLenum func,
    GLfloat ref) {
  self->glAlphaFunc(func, ref);
}

//  void QOpenGLFunctions_1_0::glEvalPoint2(GLint i, GLint j)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_012glEvalPoint2Eii(
    QOpenGLFunctions_1_0 *self,
    GLint i,
    GLint j) {
  self->glEvalPoint2(i, j);
}

//  void QOpenGLFunctions_1_0::glEvalMesh2(GLenum mode, GLint i1, GLint i2,
//      GLint j1, GLint j2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_011glEvalMesh2Ejiiii(
    QOpenGLFunctions_1_0 *self,
    GLenum mode,
    GLint i1,
    GLint i2,
    GLint j1,
    GLint j2) {
  self->glEvalMesh2(mode, i1, i2, j1, j2);
}

//  void QOpenGLFunctions_1_0::glEvalPoint1(GLint i)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_012glEvalPoint1Ei(
    QOpenGLFunctions_1_0 *self,
    GLint i) {
  self->glEvalPoint1(i);
}

//  void QOpenGLFunctions_1_0::glEvalMesh1(GLenum mode, GLint i1, GLint i2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_011glEvalMesh1Ejii(
    QOpenGLFunctions_1_0 *self,
    GLenum mode,
    GLint i1,
    GLint i2) {
  self->glEvalMesh1(mode, i1, i2);
}

//  void QOpenGLFunctions_1_0::glEvalCoord2fv(const GLfloat *u)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_014glEvalCoord2fvEPKf(
    QOpenGLFunctions_1_0 *self,
    const GLfloat *u) {
  self->glEvalCoord2fv(u);
}

//  void QOpenGLFunctions_1_0::glEvalCoord2f(GLfloat u, GLfloat v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_013glEvalCoord2fEff(
    QOpenGLFunctions_1_0 *self,
    GLfloat u,
    GLfloat v) {
  self->glEvalCoord2f(u, v);
}

//  void QOpenGLFunctions_1_0::glEvalCoord2dv(const GLdouble *u)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_014glEvalCoord2dvEPKd(
    QOpenGLFunctions_1_0 *self,
    const GLdouble *u) {
  self->glEvalCoord2dv(u);
}

//  void QOpenGLFunctions_1_0::glEvalCoord2d(GLdouble u, GLdouble v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_013glEvalCoord2dEdd(
    QOpenGLFunctions_1_0 *self,
    GLdouble u,
    GLdouble v) {
  self->glEvalCoord2d(u, v);
}

//  void QOpenGLFunctions_1_0::glEvalCoord1fv(const GLfloat *u)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_014glEvalCoord1fvEPKf(
    QOpenGLFunctions_1_0 *self,
    const GLfloat *u) {
  self->glEvalCoord1fv(u);
}

//  void QOpenGLFunctions_1_0::glEvalCoord1f(GLfloat u)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_013glEvalCoord1fEf(
    QOpenGLFunctions_1_0 *self,
    GLfloat u) {
  self->glEvalCoord1f(u);
}

//  void QOpenGLFunctions_1_0::glEvalCoord1dv(const GLdouble *u)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_014glEvalCoord1dvEPKd(
    QOpenGLFunctions_1_0 *self,
    const GLdouble *u) {
  self->glEvalCoord1dv(u);
}

//  void QOpenGLFunctions_1_0::glEvalCoord1d(GLdouble u)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_013glEvalCoord1dEd(
    QOpenGLFunctions_1_0 *self,
    GLdouble u) {
  self->glEvalCoord1d(u);
}

//  void QOpenGLFunctions_1_0::glMapGrid2f(GLint un, GLfloat u1, GLfloat u2,
//      GLint vn, GLfloat v1, GLfloat v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_011glMapGrid2fEiffiff(
    QOpenGLFunctions_1_0 *self,
    GLint un,
    GLfloat u1,
    GLfloat u2,
    GLint vn,
    GLfloat v1,
    GLfloat v2) {
  self->glMapGrid2f(un, u1, u2, vn, v1, v2);
}

//  void QOpenGLFunctions_1_0::glMapGrid2d(GLint un, GLdouble u1, GLdouble
//      u2, GLint vn, GLdouble v1, GLdouble v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_011glMapGrid2dEiddidd(
    QOpenGLFunctions_1_0 *self,
    GLint un,
    GLdouble u1,
    GLdouble u2,
    GLint vn,
    GLdouble v1,
    GLdouble v2) {
  self->glMapGrid2d(un, u1, u2, vn, v1, v2);
}

//  void QOpenGLFunctions_1_0::glMapGrid1f(GLint un, GLfloat u1, GLfloat u2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_011glMapGrid1fEiff(
    QOpenGLFunctions_1_0 *self,
    GLint un,
    GLfloat u1,
    GLfloat u2) {
  self->glMapGrid1f(un, u1, u2);
}

//  void QOpenGLFunctions_1_0::glMapGrid1d(GLint un, GLdouble u1, GLdouble
//      u2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_011glMapGrid1dEidd(
    QOpenGLFunctions_1_0 *self,
    GLint un,
    GLdouble u1,
    GLdouble u2) {
  self->glMapGrid1d(un, u1, u2);
}

//  void QOpenGLFunctions_1_0::glMap2f(GLenum target, GLfloat u1, GLfloat u2,
//      GLint ustride, GLint uorder, GLfloat v1, GLfloat v2, GLint vstride,
//      GLint vorder, const GLfloat *points)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_07glMap2fEjffiiffiiPKf(
    QOpenGLFunctions_1_0 *self,
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

//  void QOpenGLFunctions_1_0::glMap2d(GLenum target, GLdouble u1, GLdouble
//      u2, GLint ustride, GLint uorder, GLdouble v1, GLdouble v2, GLint
//      vstride, GLint vorder, const GLdouble *points)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_07glMap2dEjddiiddiiPKd(
    QOpenGLFunctions_1_0 *self,
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

//  void QOpenGLFunctions_1_0::glMap1f(GLenum target, GLfloat u1, GLfloat u2,
//      GLint stride, GLint order, const GLfloat *points)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_07glMap1fEjffiiPKf(
    QOpenGLFunctions_1_0 *self,
    GLenum target,
    GLfloat u1,
    GLfloat u2,
    GLint stride,
    GLint order,
    const GLfloat *points) {
  self->glMap1f(target, u1, u2, stride, order, points);
}

//  void QOpenGLFunctions_1_0::glMap1d(GLenum target, GLdouble u1, GLdouble
//      u2, GLint stride, GLint order, const GLdouble *points)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_07glMap1dEjddiiPKd(
    QOpenGLFunctions_1_0 *self,
    GLenum target,
    GLdouble u1,
    GLdouble u2,
    GLint stride,
    GLint order,
    const GLdouble *points) {
  self->glMap1d(target, u1, u2, stride, order, points);
}

//  void QOpenGLFunctions_1_0::glPushAttrib(GLbitfield mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_012glPushAttribEj(
    QOpenGLFunctions_1_0 *self,
    GLbitfield mask) {
  self->glPushAttrib(mask);
}

//  void QOpenGLFunctions_1_0::glPopAttrib()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_011glPopAttribEv(
    QOpenGLFunctions_1_0 *self) {
  self->glPopAttrib();
}

//  void QOpenGLFunctions_1_0::glAccum(GLenum op, GLfloat value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_07glAccumEjf(
    QOpenGLFunctions_1_0 *self,
    GLenum op,
    GLfloat value) {
  self->glAccum(op, value);
}

//  void QOpenGLFunctions_1_0::glIndexMask(GLuint mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_011glIndexMaskEj(
    QOpenGLFunctions_1_0 *self,
    GLuint mask) {
  self->glIndexMask(mask);
}

//  void QOpenGLFunctions_1_0::glClearIndex(GLfloat c)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_012glClearIndexEf(
    QOpenGLFunctions_1_0 *self,
    GLfloat c) {
  self->glClearIndex(c);
}

//  void QOpenGLFunctions_1_0::glClearAccum(GLfloat red, GLfloat green,
//      GLfloat blue, GLfloat alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_012glClearAccumEffff(
    QOpenGLFunctions_1_0 *self,
    GLfloat red,
    GLfloat green,
    GLfloat blue,
    GLfloat alpha) {
  self->glClearAccum(red, green, blue, alpha);
}

//  void QOpenGLFunctions_1_0::glPushName(GLuint name)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_010glPushNameEj(
    QOpenGLFunctions_1_0 *self,
    GLuint name) {
  self->glPushName(name);
}

//  void QOpenGLFunctions_1_0::glPopName()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_09glPopNameEv(
    QOpenGLFunctions_1_0 *self) {
  self->glPopName();
}

//  void QOpenGLFunctions_1_0::glPassThrough(GLfloat token)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_013glPassThroughEf(
    QOpenGLFunctions_1_0 *self,
    GLfloat token) {
  self->glPassThrough(token);
}

//  void QOpenGLFunctions_1_0::glLoadName(GLuint name)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_010glLoadNameEj(
    QOpenGLFunctions_1_0 *self,
    GLuint name) {
  self->glLoadName(name);
}

//  void QOpenGLFunctions_1_0::glInitNames()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_011glInitNamesEv(
    QOpenGLFunctions_1_0 *self) {
  self->glInitNames();
}

//  GLint QOpenGLFunctions_1_0::glRenderMode(GLenum mode)
extern "C" Q_DECL_EXPORT
GLint ritual_ZN20QOpenGLFunctions_1_012glRenderModeEj(
    QOpenGLFunctions_1_0 *self,
    GLenum mode) {
  return self->glRenderMode(mode);
}

//  void QOpenGLFunctions_1_0::glSelectBuffer(GLsizei size, GLuint *buffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_014glSelectBufferEiPj(
    QOpenGLFunctions_1_0 *self,
    GLsizei size,
    GLuint *buffer) {
  self->glSelectBuffer(size, buffer);
}

//  void QOpenGLFunctions_1_0::glFeedbackBuffer(GLsizei size, GLenum type,
//      GLfloat *buffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_016glFeedbackBufferEijPf(
    QOpenGLFunctions_1_0 *self,
    GLsizei size,
    GLenum type,
    GLfloat *buffer) {
  self->glFeedbackBuffer(size, type, buffer);
}

//  void QOpenGLFunctions_1_0::glTexGeniv(GLenum coord, GLenum pname, const
//      GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_010glTexGenivEjjPKi(
    QOpenGLFunctions_1_0 *self,
    GLenum coord,
    GLenum pname,
    const GLint *params) {
  self->glTexGeniv(coord, pname, params);
}

//  void QOpenGLFunctions_1_0::glTexGeni(GLenum coord, GLenum pname, GLint
//      param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_09glTexGeniEjji(
    QOpenGLFunctions_1_0 *self,
    GLenum coord,
    GLenum pname,
    GLint param) {
  self->glTexGeni(coord, pname, param);
}

//  void QOpenGLFunctions_1_0::glTexGenfv(GLenum coord, GLenum pname, const
//      GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_010glTexGenfvEjjPKf(
    QOpenGLFunctions_1_0 *self,
    GLenum coord,
    GLenum pname,
    const GLfloat *params) {
  self->glTexGenfv(coord, pname, params);
}

//  void QOpenGLFunctions_1_0::glTexGenf(GLenum coord, GLenum pname, GLfloat
//      param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_09glTexGenfEjjf(
    QOpenGLFunctions_1_0 *self,
    GLenum coord,
    GLenum pname,
    GLfloat param) {
  self->glTexGenf(coord, pname, param);
}

//  void QOpenGLFunctions_1_0::glTexGendv(GLenum coord, GLenum pname, const
//      GLdouble *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_010glTexGendvEjjPKd(
    QOpenGLFunctions_1_0 *self,
    GLenum coord,
    GLenum pname,
    const GLdouble *params) {
  self->glTexGendv(coord, pname, params);
}

//  void QOpenGLFunctions_1_0::glTexGend(GLenum coord, GLenum pname, GLdouble
//      param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_09glTexGendEjjd(
    QOpenGLFunctions_1_0 *self,
    GLenum coord,
    GLenum pname,
    GLdouble param) {
  self->glTexGend(coord, pname, param);
}

//  void QOpenGLFunctions_1_0::glTexEnviv(GLenum target, GLenum pname, const
//      GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_010glTexEnvivEjjPKi(
    QOpenGLFunctions_1_0 *self,
    GLenum target,
    GLenum pname,
    const GLint *params) {
  self->glTexEnviv(target, pname, params);
}

//  void QOpenGLFunctions_1_0::glTexEnvi(GLenum target, GLenum pname, GLint
//      param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_09glTexEnviEjji(
    QOpenGLFunctions_1_0 *self,
    GLenum target,
    GLenum pname,
    GLint param) {
  self->glTexEnvi(target, pname, param);
}

//  void QOpenGLFunctions_1_0::glTexEnvfv(GLenum target, GLenum pname, const
//      GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_010glTexEnvfvEjjPKf(
    QOpenGLFunctions_1_0 *self,
    GLenum target,
    GLenum pname,
    const GLfloat *params) {
  self->glTexEnvfv(target, pname, params);
}

//  void QOpenGLFunctions_1_0::glTexEnvf(GLenum target, GLenum pname, GLfloat
//      param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_09glTexEnvfEjjf(
    QOpenGLFunctions_1_0 *self,
    GLenum target,
    GLenum pname,
    GLfloat param) {
  self->glTexEnvf(target, pname, param);
}

//  void QOpenGLFunctions_1_0::glShadeModel(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_012glShadeModelEj(
    QOpenGLFunctions_1_0 *self,
    GLenum mode) {
  self->glShadeModel(mode);
}

//  void QOpenGLFunctions_1_0::glPolygonStipple(const GLubyte *mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_016glPolygonStippleEPKh(
    QOpenGLFunctions_1_0 *self,
    const GLubyte *mask) {
  self->glPolygonStipple(mask);
}

//  void QOpenGLFunctions_1_0::glMaterialiv(GLenum face, GLenum pname, const
//      GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_012glMaterialivEjjPKi(
    QOpenGLFunctions_1_0 *self,
    GLenum face,
    GLenum pname,
    const GLint *params) {
  self->glMaterialiv(face, pname, params);
}

//  void QOpenGLFunctions_1_0::glMateriali(GLenum face, GLenum pname, GLint
//      param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_011glMaterialiEjji(
    QOpenGLFunctions_1_0 *self,
    GLenum face,
    GLenum pname,
    GLint param) {
  self->glMateriali(face, pname, param);
}

//  void QOpenGLFunctions_1_0::glMaterialfv(GLenum face, GLenum pname, const
//      GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_012glMaterialfvEjjPKf(
    QOpenGLFunctions_1_0 *self,
    GLenum face,
    GLenum pname,
    const GLfloat *params) {
  self->glMaterialfv(face, pname, params);
}

//  void QOpenGLFunctions_1_0::glMaterialf(GLenum face, GLenum pname, GLfloat
//      param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_011glMaterialfEjjf(
    QOpenGLFunctions_1_0 *self,
    GLenum face,
    GLenum pname,
    GLfloat param) {
  self->glMaterialf(face, pname, param);
}

//  void QOpenGLFunctions_1_0::glLineStipple(GLint factor, GLushort pattern)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_013glLineStippleEit(
    QOpenGLFunctions_1_0 *self,
    GLint factor,
    GLushort pattern) {
  self->glLineStipple(factor, pattern);
}

//  void QOpenGLFunctions_1_0::glLightModeliv(GLenum pname, const GLint
//      *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_014glLightModelivEjPKi(
    QOpenGLFunctions_1_0 *self,
    GLenum pname,
    const GLint *params) {
  self->glLightModeliv(pname, params);
}

//  void QOpenGLFunctions_1_0::glLightModeli(GLenum pname, GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_013glLightModeliEji(
    QOpenGLFunctions_1_0 *self,
    GLenum pname,
    GLint param) {
  self->glLightModeli(pname, param);
}

//  void QOpenGLFunctions_1_0::glLightModelfv(GLenum pname, const GLfloat
//      *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_014glLightModelfvEjPKf(
    QOpenGLFunctions_1_0 *self,
    GLenum pname,
    const GLfloat *params) {
  self->glLightModelfv(pname, params);
}

//  void QOpenGLFunctions_1_0::glLightModelf(GLenum pname, GLfloat param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_013glLightModelfEjf(
    QOpenGLFunctions_1_0 *self,
    GLenum pname,
    GLfloat param) {
  self->glLightModelf(pname, param);
}

//  void QOpenGLFunctions_1_0::glLightiv(GLenum light, GLenum pname, const
//      GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_09glLightivEjjPKi(
    QOpenGLFunctions_1_0 *self,
    GLenum light,
    GLenum pname,
    const GLint *params) {
  self->glLightiv(light, pname, params);
}

//  void QOpenGLFunctions_1_0::glLighti(GLenum light, GLenum pname, GLint
//      param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_08glLightiEjji(
    QOpenGLFunctions_1_0 *self,
    GLenum light,
    GLenum pname,
    GLint param) {
  self->glLighti(light, pname, param);
}

//  void QOpenGLFunctions_1_0::glLightfv(GLenum light, GLenum pname, const
//      GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_09glLightfvEjjPKf(
    QOpenGLFunctions_1_0 *self,
    GLenum light,
    GLenum pname,
    const GLfloat *params) {
  self->glLightfv(light, pname, params);
}

//  void QOpenGLFunctions_1_0::glLightf(GLenum light, GLenum pname, GLfloat
//      param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_08glLightfEjjf(
    QOpenGLFunctions_1_0 *self,
    GLenum light,
    GLenum pname,
    GLfloat param) {
  self->glLightf(light, pname, param);
}

//  void QOpenGLFunctions_1_0::glFogiv(GLenum pname, const GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_07glFogivEjPKi(
    QOpenGLFunctions_1_0 *self,
    GLenum pname,
    const GLint *params) {
  self->glFogiv(pname, params);
}

//  void QOpenGLFunctions_1_0::glFogi(GLenum pname, GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_06glFogiEji(
    QOpenGLFunctions_1_0 *self,
    GLenum pname,
    GLint param) {
  self->glFogi(pname, param);
}

//  void QOpenGLFunctions_1_0::glFogfv(GLenum pname, const GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_07glFogfvEjPKf(
    QOpenGLFunctions_1_0 *self,
    GLenum pname,
    const GLfloat *params) {
  self->glFogfv(pname, params);
}

//  void QOpenGLFunctions_1_0::glFogf(GLenum pname, GLfloat param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_06glFogfEjf(
    QOpenGLFunctions_1_0 *self,
    GLenum pname,
    GLfloat param) {
  self->glFogf(pname, param);
}

//  void QOpenGLFunctions_1_0::glColorMaterial(GLenum face, GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_015glColorMaterialEjj(
    QOpenGLFunctions_1_0 *self,
    GLenum face,
    GLenum mode) {
  self->glColorMaterial(face, mode);
}

//  void QOpenGLFunctions_1_0::glClipPlane(GLenum plane, const GLdouble
//      *equation)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_011glClipPlaneEjPKd(
    QOpenGLFunctions_1_0 *self,
    GLenum plane,
    const GLdouble *equation) {
  self->glClipPlane(plane, equation);
}

//  void QOpenGLFunctions_1_0::glVertex4sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_011glVertex4svEPKs(
    QOpenGLFunctions_1_0 *self,
    const GLshort *v) {
  self->glVertex4sv(v);
}

//  void QOpenGLFunctions_1_0::glVertex4s(GLshort x, GLshort y, GLshort z,
//      GLshort w)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_010glVertex4sEssss(
    QOpenGLFunctions_1_0 *self,
    GLshort x,
    GLshort y,
    GLshort z,
    GLshort w) {
  self->glVertex4s(x, y, z, w);
}

//  void QOpenGLFunctions_1_0::glVertex4iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_011glVertex4ivEPKi(
    QOpenGLFunctions_1_0 *self,
    const GLint *v) {
  self->glVertex4iv(v);
}

//  void QOpenGLFunctions_1_0::glVertex4i(GLint x, GLint y, GLint z, GLint w)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_010glVertex4iEiiii(
    QOpenGLFunctions_1_0 *self,
    GLint x,
    GLint y,
    GLint z,
    GLint w) {
  self->glVertex4i(x, y, z, w);
}

//  void QOpenGLFunctions_1_0::glVertex4fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_011glVertex4fvEPKf(
    QOpenGLFunctions_1_0 *self,
    const GLfloat *v) {
  self->glVertex4fv(v);
}

//  void QOpenGLFunctions_1_0::glVertex4f(GLfloat x, GLfloat y, GLfloat z,
//      GLfloat w)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_010glVertex4fEffff(
    QOpenGLFunctions_1_0 *self,
    GLfloat x,
    GLfloat y,
    GLfloat z,
    GLfloat w) {
  self->glVertex4f(x, y, z, w);
}

//  void QOpenGLFunctions_1_0::glVertex4dv(const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_011glVertex4dvEPKd(
    QOpenGLFunctions_1_0 *self,
    const GLdouble *v) {
  self->glVertex4dv(v);
}

//  void QOpenGLFunctions_1_0::glVertex4d(GLdouble x, GLdouble y, GLdouble z,
//      GLdouble w)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_010glVertex4dEdddd(
    QOpenGLFunctions_1_0 *self,
    GLdouble x,
    GLdouble y,
    GLdouble z,
    GLdouble w) {
  self->glVertex4d(x, y, z, w);
}

//  void QOpenGLFunctions_1_0::glVertex3sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_011glVertex3svEPKs(
    QOpenGLFunctions_1_0 *self,
    const GLshort *v) {
  self->glVertex3sv(v);
}

//  void QOpenGLFunctions_1_0::glVertex3s(GLshort x, GLshort y, GLshort z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_010glVertex3sEsss(
    QOpenGLFunctions_1_0 *self,
    GLshort x,
    GLshort y,
    GLshort z) {
  self->glVertex3s(x, y, z);
}

//  void QOpenGLFunctions_1_0::glVertex3iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_011glVertex3ivEPKi(
    QOpenGLFunctions_1_0 *self,
    const GLint *v) {
  self->glVertex3iv(v);
}

//  void QOpenGLFunctions_1_0::glVertex3i(GLint x, GLint y, GLint z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_010glVertex3iEiii(
    QOpenGLFunctions_1_0 *self,
    GLint x,
    GLint y,
    GLint z) {
  self->glVertex3i(x, y, z);
}

//  void QOpenGLFunctions_1_0::glVertex3fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_011glVertex3fvEPKf(
    QOpenGLFunctions_1_0 *self,
    const GLfloat *v) {
  self->glVertex3fv(v);
}

//  void QOpenGLFunctions_1_0::glVertex3f(GLfloat x, GLfloat y, GLfloat z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_010glVertex3fEfff(
    QOpenGLFunctions_1_0 *self,
    GLfloat x,
    GLfloat y,
    GLfloat z) {
  self->glVertex3f(x, y, z);
}

//  void QOpenGLFunctions_1_0::glVertex3dv(const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_011glVertex3dvEPKd(
    QOpenGLFunctions_1_0 *self,
    const GLdouble *v) {
  self->glVertex3dv(v);
}

//  void QOpenGLFunctions_1_0::glVertex3d(GLdouble x, GLdouble y, GLdouble z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_010glVertex3dEddd(
    QOpenGLFunctions_1_0 *self,
    GLdouble x,
    GLdouble y,
    GLdouble z) {
  self->glVertex3d(x, y, z);
}

//  void QOpenGLFunctions_1_0::glVertex2sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_011glVertex2svEPKs(
    QOpenGLFunctions_1_0 *self,
    const GLshort *v) {
  self->glVertex2sv(v);
}

//  void QOpenGLFunctions_1_0::glVertex2s(GLshort x, GLshort y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_010glVertex2sEss(
    QOpenGLFunctions_1_0 *self,
    GLshort x,
    GLshort y) {
  self->glVertex2s(x, y);
}

//  void QOpenGLFunctions_1_0::glVertex2iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_011glVertex2ivEPKi(
    QOpenGLFunctions_1_0 *self,
    const GLint *v) {
  self->glVertex2iv(v);
}

//  void QOpenGLFunctions_1_0::glVertex2i(GLint x, GLint y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_010glVertex2iEii(
    QOpenGLFunctions_1_0 *self,
    GLint x,
    GLint y) {
  self->glVertex2i(x, y);
}

//  void QOpenGLFunctions_1_0::glVertex2fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_011glVertex2fvEPKf(
    QOpenGLFunctions_1_0 *self,
    const GLfloat *v) {
  self->glVertex2fv(v);
}

//  void QOpenGLFunctions_1_0::glVertex2f(GLfloat x, GLfloat y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_010glVertex2fEff(
    QOpenGLFunctions_1_0 *self,
    GLfloat x,
    GLfloat y) {
  self->glVertex2f(x, y);
}

//  void QOpenGLFunctions_1_0::glVertex2dv(const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_011glVertex2dvEPKd(
    QOpenGLFunctions_1_0 *self,
    const GLdouble *v) {
  self->glVertex2dv(v);
}

//  void QOpenGLFunctions_1_0::glVertex2d(GLdouble x, GLdouble y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_010glVertex2dEdd(
    QOpenGLFunctions_1_0 *self,
    GLdouble x,
    GLdouble y) {
  self->glVertex2d(x, y);
}

//  void QOpenGLFunctions_1_0::glTexCoord4sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_013glTexCoord4svEPKs(
    QOpenGLFunctions_1_0 *self,
    const GLshort *v) {
  self->glTexCoord4sv(v);
}

//  void QOpenGLFunctions_1_0::glTexCoord4s(GLshort s, GLshort t, GLshort r,
//      GLshort q)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_012glTexCoord4sEssss(
    QOpenGLFunctions_1_0 *self,
    GLshort s,
    GLshort t,
    GLshort r,
    GLshort q) {
  self->glTexCoord4s(s, t, r, q);
}

//  void QOpenGLFunctions_1_0::glTexCoord4iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_013glTexCoord4ivEPKi(
    QOpenGLFunctions_1_0 *self,
    const GLint *v) {
  self->glTexCoord4iv(v);
}

//  void QOpenGLFunctions_1_0::glTexCoord4i(GLint s, GLint t, GLint r, GLint
//      q)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_012glTexCoord4iEiiii(
    QOpenGLFunctions_1_0 *self,
    GLint s,
    GLint t,
    GLint r,
    GLint q) {
  self->glTexCoord4i(s, t, r, q);
}

//  void QOpenGLFunctions_1_0::glTexCoord4fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_013glTexCoord4fvEPKf(
    QOpenGLFunctions_1_0 *self,
    const GLfloat *v) {
  self->glTexCoord4fv(v);
}

//  void QOpenGLFunctions_1_0::glTexCoord4f(GLfloat s, GLfloat t, GLfloat r,
//      GLfloat q)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_012glTexCoord4fEffff(
    QOpenGLFunctions_1_0 *self,
    GLfloat s,
    GLfloat t,
    GLfloat r,
    GLfloat q) {
  self->glTexCoord4f(s, t, r, q);
}

//  void QOpenGLFunctions_1_0::glTexCoord4dv(const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_013glTexCoord4dvEPKd(
    QOpenGLFunctions_1_0 *self,
    const GLdouble *v) {
  self->glTexCoord4dv(v);
}

//  void QOpenGLFunctions_1_0::glTexCoord4d(GLdouble s, GLdouble t, GLdouble
//      r, GLdouble q)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_012glTexCoord4dEdddd(
    QOpenGLFunctions_1_0 *self,
    GLdouble s,
    GLdouble t,
    GLdouble r,
    GLdouble q) {
  self->glTexCoord4d(s, t, r, q);
}

//  void QOpenGLFunctions_1_0::glTexCoord3sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_013glTexCoord3svEPKs(
    QOpenGLFunctions_1_0 *self,
    const GLshort *v) {
  self->glTexCoord3sv(v);
}

//  void QOpenGLFunctions_1_0::glTexCoord3s(GLshort s, GLshort t, GLshort r)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_012glTexCoord3sEsss(
    QOpenGLFunctions_1_0 *self,
    GLshort s,
    GLshort t,
    GLshort r) {
  self->glTexCoord3s(s, t, r);
}

//  void QOpenGLFunctions_1_0::glTexCoord3iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_013glTexCoord3ivEPKi(
    QOpenGLFunctions_1_0 *self,
    const GLint *v) {
  self->glTexCoord3iv(v);
}

//  void QOpenGLFunctions_1_0::glTexCoord3i(GLint s, GLint t, GLint r)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_012glTexCoord3iEiii(
    QOpenGLFunctions_1_0 *self,
    GLint s,
    GLint t,
    GLint r) {
  self->glTexCoord3i(s, t, r);
}

//  void QOpenGLFunctions_1_0::glTexCoord3fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_013glTexCoord3fvEPKf(
    QOpenGLFunctions_1_0 *self,
    const GLfloat *v) {
  self->glTexCoord3fv(v);
}

//  void QOpenGLFunctions_1_0::glTexCoord3f(GLfloat s, GLfloat t, GLfloat r)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_012glTexCoord3fEfff(
    QOpenGLFunctions_1_0 *self,
    GLfloat s,
    GLfloat t,
    GLfloat r) {
  self->glTexCoord3f(s, t, r);
}

//  void QOpenGLFunctions_1_0::glTexCoord3dv(const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_013glTexCoord3dvEPKd(
    QOpenGLFunctions_1_0 *self,
    const GLdouble *v) {
  self->glTexCoord3dv(v);
}

//  void QOpenGLFunctions_1_0::glTexCoord3d(GLdouble s, GLdouble t, GLdouble
//      r)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_012glTexCoord3dEddd(
    QOpenGLFunctions_1_0 *self,
    GLdouble s,
    GLdouble t,
    GLdouble r) {
  self->glTexCoord3d(s, t, r);
}

//  void QOpenGLFunctions_1_0::glTexCoord2sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_013glTexCoord2svEPKs(
    QOpenGLFunctions_1_0 *self,
    const GLshort *v) {
  self->glTexCoord2sv(v);
}

//  void QOpenGLFunctions_1_0::glTexCoord2s(GLshort s, GLshort t)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_012glTexCoord2sEss(
    QOpenGLFunctions_1_0 *self,
    GLshort s,
    GLshort t) {
  self->glTexCoord2s(s, t);
}

//  void QOpenGLFunctions_1_0::glTexCoord2iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_013glTexCoord2ivEPKi(
    QOpenGLFunctions_1_0 *self,
    const GLint *v) {
  self->glTexCoord2iv(v);
}

//  void QOpenGLFunctions_1_0::glTexCoord2i(GLint s, GLint t)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_012glTexCoord2iEii(
    QOpenGLFunctions_1_0 *self,
    GLint s,
    GLint t) {
  self->glTexCoord2i(s, t);
}

//  void QOpenGLFunctions_1_0::glTexCoord2fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_013glTexCoord2fvEPKf(
    QOpenGLFunctions_1_0 *self,
    const GLfloat *v) {
  self->glTexCoord2fv(v);
}

//  void QOpenGLFunctions_1_0::glTexCoord2f(GLfloat s, GLfloat t)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_012glTexCoord2fEff(
    QOpenGLFunctions_1_0 *self,
    GLfloat s,
    GLfloat t) {
  self->glTexCoord2f(s, t);
}

//  void QOpenGLFunctions_1_0::glTexCoord2dv(const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_013glTexCoord2dvEPKd(
    QOpenGLFunctions_1_0 *self,
    const GLdouble *v) {
  self->glTexCoord2dv(v);
}

//  void QOpenGLFunctions_1_0::glTexCoord2d(GLdouble s, GLdouble t)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_012glTexCoord2dEdd(
    QOpenGLFunctions_1_0 *self,
    GLdouble s,
    GLdouble t) {
  self->glTexCoord2d(s, t);
}

//  void QOpenGLFunctions_1_0::glTexCoord1sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_013glTexCoord1svEPKs(
    QOpenGLFunctions_1_0 *self,
    const GLshort *v) {
  self->glTexCoord1sv(v);
}

//  void QOpenGLFunctions_1_0::glTexCoord1s(GLshort s)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_012glTexCoord1sEs(
    QOpenGLFunctions_1_0 *self,
    GLshort s) {
  self->glTexCoord1s(s);
}

//  void QOpenGLFunctions_1_0::glTexCoord1iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_013glTexCoord1ivEPKi(
    QOpenGLFunctions_1_0 *self,
    const GLint *v) {
  self->glTexCoord1iv(v);
}

//  void QOpenGLFunctions_1_0::glTexCoord1i(GLint s)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_012glTexCoord1iEi(
    QOpenGLFunctions_1_0 *self,
    GLint s) {
  self->glTexCoord1i(s);
}

//  void QOpenGLFunctions_1_0::glTexCoord1fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_013glTexCoord1fvEPKf(
    QOpenGLFunctions_1_0 *self,
    const GLfloat *v) {
  self->glTexCoord1fv(v);
}

//  void QOpenGLFunctions_1_0::glTexCoord1f(GLfloat s)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_012glTexCoord1fEf(
    QOpenGLFunctions_1_0 *self,
    GLfloat s) {
  self->glTexCoord1f(s);
}

//  void QOpenGLFunctions_1_0::glTexCoord1dv(const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_013glTexCoord1dvEPKd(
    QOpenGLFunctions_1_0 *self,
    const GLdouble *v) {
  self->glTexCoord1dv(v);
}

//  void QOpenGLFunctions_1_0::glTexCoord1d(GLdouble s)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_012glTexCoord1dEd(
    QOpenGLFunctions_1_0 *self,
    GLdouble s) {
  self->glTexCoord1d(s);
}

//  void QOpenGLFunctions_1_0::glRectsv(const GLshort *v1, const GLshort *v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_08glRectsvEPKsS1_(
    QOpenGLFunctions_1_0 *self,
    const GLshort *v1,
    const GLshort *v2) {
  self->glRectsv(v1, v2);
}

//  void QOpenGLFunctions_1_0::glRects(GLshort x1, GLshort y1, GLshort x2,
//      GLshort y2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_07glRectsEssss(
    QOpenGLFunctions_1_0 *self,
    GLshort x1,
    GLshort y1,
    GLshort x2,
    GLshort y2) {
  self->glRects(x1, y1, x2, y2);
}

//  void QOpenGLFunctions_1_0::glRectiv(const GLint *v1, const GLint *v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_08glRectivEPKiS1_(
    QOpenGLFunctions_1_0 *self,
    const GLint *v1,
    const GLint *v2) {
  self->glRectiv(v1, v2);
}

//  void QOpenGLFunctions_1_0::glRecti(GLint x1, GLint y1, GLint x2, GLint
//      y2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_07glRectiEiiii(
    QOpenGLFunctions_1_0 *self,
    GLint x1,
    GLint y1,
    GLint x2,
    GLint y2) {
  self->glRecti(x1, y1, x2, y2);
}

//  void QOpenGLFunctions_1_0::glRectfv(const GLfloat *v1, const GLfloat *v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_08glRectfvEPKfS1_(
    QOpenGLFunctions_1_0 *self,
    const GLfloat *v1,
    const GLfloat *v2) {
  self->glRectfv(v1, v2);
}

//  void QOpenGLFunctions_1_0::glRectf(GLfloat x1, GLfloat y1, GLfloat x2,
//      GLfloat y2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_07glRectfEffff(
    QOpenGLFunctions_1_0 *self,
    GLfloat x1,
    GLfloat y1,
    GLfloat x2,
    GLfloat y2) {
  self->glRectf(x1, y1, x2, y2);
}

//  void QOpenGLFunctions_1_0::glRectdv(const GLdouble *v1, const GLdouble
//      *v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_08glRectdvEPKdS1_(
    QOpenGLFunctions_1_0 *self,
    const GLdouble *v1,
    const GLdouble *v2) {
  self->glRectdv(v1, v2);
}

//  void QOpenGLFunctions_1_0::glRectd(GLdouble x1, GLdouble y1, GLdouble x2,
//      GLdouble y2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_07glRectdEdddd(
    QOpenGLFunctions_1_0 *self,
    GLdouble x1,
    GLdouble y1,
    GLdouble x2,
    GLdouble y2) {
  self->glRectd(x1, y1, x2, y2);
}

//  void QOpenGLFunctions_1_0::glRasterPos4sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_014glRasterPos4svEPKs(
    QOpenGLFunctions_1_0 *self,
    const GLshort *v) {
  self->glRasterPos4sv(v);
}

//  void QOpenGLFunctions_1_0::glRasterPos4s(GLshort x, GLshort y, GLshort z,
//      GLshort w)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_013glRasterPos4sEssss(
    QOpenGLFunctions_1_0 *self,
    GLshort x,
    GLshort y,
    GLshort z,
    GLshort w) {
  self->glRasterPos4s(x, y, z, w);
}

//  void QOpenGLFunctions_1_0::glRasterPos4iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_014glRasterPos4ivEPKi(
    QOpenGLFunctions_1_0 *self,
    const GLint *v) {
  self->glRasterPos4iv(v);
}

//  void QOpenGLFunctions_1_0::glRasterPos4i(GLint x, GLint y, GLint z, GLint
//      w)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_013glRasterPos4iEiiii(
    QOpenGLFunctions_1_0 *self,
    GLint x,
    GLint y,
    GLint z,
    GLint w) {
  self->glRasterPos4i(x, y, z, w);
}

//  void QOpenGLFunctions_1_0::glRasterPos4fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_014glRasterPos4fvEPKf(
    QOpenGLFunctions_1_0 *self,
    const GLfloat *v) {
  self->glRasterPos4fv(v);
}

//  void QOpenGLFunctions_1_0::glRasterPos4f(GLfloat x, GLfloat y, GLfloat z,
//      GLfloat w)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_013glRasterPos4fEffff(
    QOpenGLFunctions_1_0 *self,
    GLfloat x,
    GLfloat y,
    GLfloat z,
    GLfloat w) {
  self->glRasterPos4f(x, y, z, w);
}

//  void QOpenGLFunctions_1_0::glRasterPos4dv(const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_014glRasterPos4dvEPKd(
    QOpenGLFunctions_1_0 *self,
    const GLdouble *v) {
  self->glRasterPos4dv(v);
}

//  void QOpenGLFunctions_1_0::glRasterPos4d(GLdouble x, GLdouble y, GLdouble
//      z, GLdouble w)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_013glRasterPos4dEdddd(
    QOpenGLFunctions_1_0 *self,
    GLdouble x,
    GLdouble y,
    GLdouble z,
    GLdouble w) {
  self->glRasterPos4d(x, y, z, w);
}

//  void QOpenGLFunctions_1_0::glRasterPos3sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_014glRasterPos3svEPKs(
    QOpenGLFunctions_1_0 *self,
    const GLshort *v) {
  self->glRasterPos3sv(v);
}

//  void QOpenGLFunctions_1_0::glRasterPos3s(GLshort x, GLshort y, GLshort z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_013glRasterPos3sEsss(
    QOpenGLFunctions_1_0 *self,
    GLshort x,
    GLshort y,
    GLshort z) {
  self->glRasterPos3s(x, y, z);
}

//  void QOpenGLFunctions_1_0::glRasterPos3iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_014glRasterPos3ivEPKi(
    QOpenGLFunctions_1_0 *self,
    const GLint *v) {
  self->glRasterPos3iv(v);
}

//  void QOpenGLFunctions_1_0::glRasterPos3i(GLint x, GLint y, GLint z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_013glRasterPos3iEiii(
    QOpenGLFunctions_1_0 *self,
    GLint x,
    GLint y,
    GLint z) {
  self->glRasterPos3i(x, y, z);
}

//  void QOpenGLFunctions_1_0::glRasterPos3fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_014glRasterPos3fvEPKf(
    QOpenGLFunctions_1_0 *self,
    const GLfloat *v) {
  self->glRasterPos3fv(v);
}

//  void QOpenGLFunctions_1_0::glRasterPos3f(GLfloat x, GLfloat y, GLfloat z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_013glRasterPos3fEfff(
    QOpenGLFunctions_1_0 *self,
    GLfloat x,
    GLfloat y,
    GLfloat z) {
  self->glRasterPos3f(x, y, z);
}

//  void QOpenGLFunctions_1_0::glRasterPos3dv(const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_014glRasterPos3dvEPKd(
    QOpenGLFunctions_1_0 *self,
    const GLdouble *v) {
  self->glRasterPos3dv(v);
}

//  void QOpenGLFunctions_1_0::glRasterPos3d(GLdouble x, GLdouble y, GLdouble
//      z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_013glRasterPos3dEddd(
    QOpenGLFunctions_1_0 *self,
    GLdouble x,
    GLdouble y,
    GLdouble z) {
  self->glRasterPos3d(x, y, z);
}

//  void QOpenGLFunctions_1_0::glRasterPos2sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_014glRasterPos2svEPKs(
    QOpenGLFunctions_1_0 *self,
    const GLshort *v) {
  self->glRasterPos2sv(v);
}

//  void QOpenGLFunctions_1_0::glRasterPos2s(GLshort x, GLshort y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_013glRasterPos2sEss(
    QOpenGLFunctions_1_0 *self,
    GLshort x,
    GLshort y) {
  self->glRasterPos2s(x, y);
}

//  void QOpenGLFunctions_1_0::glRasterPos2iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_014glRasterPos2ivEPKi(
    QOpenGLFunctions_1_0 *self,
    const GLint *v) {
  self->glRasterPos2iv(v);
}

//  void QOpenGLFunctions_1_0::glRasterPos2i(GLint x, GLint y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_013glRasterPos2iEii(
    QOpenGLFunctions_1_0 *self,
    GLint x,
    GLint y) {
  self->glRasterPos2i(x, y);
}

//  void QOpenGLFunctions_1_0::glRasterPos2fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_014glRasterPos2fvEPKf(
    QOpenGLFunctions_1_0 *self,
    const GLfloat *v) {
  self->glRasterPos2fv(v);
}

//  void QOpenGLFunctions_1_0::glRasterPos2f(GLfloat x, GLfloat y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_013glRasterPos2fEff(
    QOpenGLFunctions_1_0 *self,
    GLfloat x,
    GLfloat y) {
  self->glRasterPos2f(x, y);
}

//  void QOpenGLFunctions_1_0::glRasterPos2dv(const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_014glRasterPos2dvEPKd(
    QOpenGLFunctions_1_0 *self,
    const GLdouble *v) {
  self->glRasterPos2dv(v);
}

//  void QOpenGLFunctions_1_0::glRasterPos2d(GLdouble x, GLdouble y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_013glRasterPos2dEdd(
    QOpenGLFunctions_1_0 *self,
    GLdouble x,
    GLdouble y) {
  self->glRasterPos2d(x, y);
}

//  void QOpenGLFunctions_1_0::glNormal3sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_011glNormal3svEPKs(
    QOpenGLFunctions_1_0 *self,
    const GLshort *v) {
  self->glNormal3sv(v);
}

//  void QOpenGLFunctions_1_0::glNormal3s(GLshort nx, GLshort ny, GLshort nz)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_010glNormal3sEsss(
    QOpenGLFunctions_1_0 *self,
    GLshort nx,
    GLshort ny,
    GLshort nz) {
  self->glNormal3s(nx, ny, nz);
}

//  void QOpenGLFunctions_1_0::glNormal3iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_011glNormal3ivEPKi(
    QOpenGLFunctions_1_0 *self,
    const GLint *v) {
  self->glNormal3iv(v);
}

//  void QOpenGLFunctions_1_0::glNormal3i(GLint nx, GLint ny, GLint nz)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_010glNormal3iEiii(
    QOpenGLFunctions_1_0 *self,
    GLint nx,
    GLint ny,
    GLint nz) {
  self->glNormal3i(nx, ny, nz);
}

//  void QOpenGLFunctions_1_0::glNormal3fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_011glNormal3fvEPKf(
    QOpenGLFunctions_1_0 *self,
    const GLfloat *v) {
  self->glNormal3fv(v);
}

//  void QOpenGLFunctions_1_0::glNormal3f(GLfloat nx, GLfloat ny, GLfloat nz)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_010glNormal3fEfff(
    QOpenGLFunctions_1_0 *self,
    GLfloat nx,
    GLfloat ny,
    GLfloat nz) {
  self->glNormal3f(nx, ny, nz);
}

//  void QOpenGLFunctions_1_0::glNormal3dv(const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_011glNormal3dvEPKd(
    QOpenGLFunctions_1_0 *self,
    const GLdouble *v) {
  self->glNormal3dv(v);
}

//  void QOpenGLFunctions_1_0::glNormal3d(GLdouble nx, GLdouble ny, GLdouble
//      nz)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_010glNormal3dEddd(
    QOpenGLFunctions_1_0 *self,
    GLdouble nx,
    GLdouble ny,
    GLdouble nz) {
  self->glNormal3d(nx, ny, nz);
}

//  void QOpenGLFunctions_1_0::glNormal3bv(const GLbyte *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_011glNormal3bvEPKa(
    QOpenGLFunctions_1_0 *self,
    const GLbyte *v) {
  self->glNormal3bv(v);
}

//  void QOpenGLFunctions_1_0::glNormal3b(GLbyte nx, GLbyte ny, GLbyte nz)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_010glNormal3bEaaa(
    QOpenGLFunctions_1_0 *self,
    GLbyte nx,
    GLbyte ny,
    GLbyte nz) {
  self->glNormal3b(nx, ny, nz);
}

//  void QOpenGLFunctions_1_0::glIndexsv(const GLshort *c)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_09glIndexsvEPKs(
    QOpenGLFunctions_1_0 *self,
    const GLshort *c) {
  self->glIndexsv(c);
}

//  void QOpenGLFunctions_1_0::glIndexs(GLshort c)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_08glIndexsEs(
    QOpenGLFunctions_1_0 *self,
    GLshort c) {
  self->glIndexs(c);
}

//  void QOpenGLFunctions_1_0::glIndexiv(const GLint *c)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_09glIndexivEPKi(
    QOpenGLFunctions_1_0 *self,
    const GLint *c) {
  self->glIndexiv(c);
}

//  void QOpenGLFunctions_1_0::glIndexi(GLint c)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_08glIndexiEi(
    QOpenGLFunctions_1_0 *self,
    GLint c) {
  self->glIndexi(c);
}

//  void QOpenGLFunctions_1_0::glIndexfv(const GLfloat *c)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_09glIndexfvEPKf(
    QOpenGLFunctions_1_0 *self,
    const GLfloat *c) {
  self->glIndexfv(c);
}

//  void QOpenGLFunctions_1_0::glIndexf(GLfloat c)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_08glIndexfEf(
    QOpenGLFunctions_1_0 *self,
    GLfloat c) {
  self->glIndexf(c);
}

//  void QOpenGLFunctions_1_0::glIndexdv(const GLdouble *c)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_09glIndexdvEPKd(
    QOpenGLFunctions_1_0 *self,
    const GLdouble *c) {
  self->glIndexdv(c);
}

//  void QOpenGLFunctions_1_0::glIndexd(GLdouble c)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_08glIndexdEd(
    QOpenGLFunctions_1_0 *self,
    GLdouble c) {
  self->glIndexd(c);
}

//  void QOpenGLFunctions_1_0::glEnd()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_05glEndEv(QOpenGLFunctions_1_0 *self) {
  self->glEnd();
}

//  void QOpenGLFunctions_1_0::glEdgeFlagv(const GLboolean *flag)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_011glEdgeFlagvEPKh(
    QOpenGLFunctions_1_0 *self,
    const GLboolean *flag) {
  self->glEdgeFlagv(flag);
}

//  void QOpenGLFunctions_1_0::glEdgeFlag(GLboolean flag)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_010glEdgeFlagEh(
    QOpenGLFunctions_1_0 *self,
    GLboolean flag) {
  self->glEdgeFlag(flag);
}

//  void QOpenGLFunctions_1_0::glColor4usv(const GLushort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_011glColor4usvEPKt(
    QOpenGLFunctions_1_0 *self,
    const GLushort *v) {
  self->glColor4usv(v);
}

//  void QOpenGLFunctions_1_0::glColor4us(GLushort red, GLushort green,
//      GLushort blue, GLushort alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_010glColor4usEtttt(
    QOpenGLFunctions_1_0 *self,
    GLushort red,
    GLushort green,
    GLushort blue,
    GLushort alpha) {
  self->glColor4us(red, green, blue, alpha);
}

//  void QOpenGLFunctions_1_0::glColor4uiv(const GLuint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_011glColor4uivEPKj(
    QOpenGLFunctions_1_0 *self,
    const GLuint *v) {
  self->glColor4uiv(v);
}

//  void QOpenGLFunctions_1_0::glColor4ui(GLuint red, GLuint green, GLuint
//      blue, GLuint alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_010glColor4uiEjjjj(
    QOpenGLFunctions_1_0 *self,
    GLuint red,
    GLuint green,
    GLuint blue,
    GLuint alpha) {
  self->glColor4ui(red, green, blue, alpha);
}

//  void QOpenGLFunctions_1_0::glColor4ubv(const GLubyte *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_011glColor4ubvEPKh(
    QOpenGLFunctions_1_0 *self,
    const GLubyte *v) {
  self->glColor4ubv(v);
}

//  void QOpenGLFunctions_1_0::glColor4ub(GLubyte red, GLubyte green, GLubyte
//      blue, GLubyte alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_010glColor4ubEhhhh(
    QOpenGLFunctions_1_0 *self,
    GLubyte red,
    GLubyte green,
    GLubyte blue,
    GLubyte alpha) {
  self->glColor4ub(red, green, blue, alpha);
}

//  void QOpenGLFunctions_1_0::glColor4sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_010glColor4svEPKs(
    QOpenGLFunctions_1_0 *self,
    const GLshort *v) {
  self->glColor4sv(v);
}

//  void QOpenGLFunctions_1_0::glColor4s(GLshort red, GLshort green, GLshort
//      blue, GLshort alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_09glColor4sEssss(
    QOpenGLFunctions_1_0 *self,
    GLshort red,
    GLshort green,
    GLshort blue,
    GLshort alpha) {
  self->glColor4s(red, green, blue, alpha);
}

//  void QOpenGLFunctions_1_0::glColor4iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_010glColor4ivEPKi(
    QOpenGLFunctions_1_0 *self,
    const GLint *v) {
  self->glColor4iv(v);
}

//  void QOpenGLFunctions_1_0::glColor4i(GLint red, GLint green, GLint blue,
//      GLint alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_09glColor4iEiiii(
    QOpenGLFunctions_1_0 *self,
    GLint red,
    GLint green,
    GLint blue,
    GLint alpha) {
  self->glColor4i(red, green, blue, alpha);
}

//  void QOpenGLFunctions_1_0::glColor4fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_010glColor4fvEPKf(
    QOpenGLFunctions_1_0 *self,
    const GLfloat *v) {
  self->glColor4fv(v);
}

//  void QOpenGLFunctions_1_0::glColor4f(GLfloat red, GLfloat green, GLfloat
//      blue, GLfloat alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_09glColor4fEffff(
    QOpenGLFunctions_1_0 *self,
    GLfloat red,
    GLfloat green,
    GLfloat blue,
    GLfloat alpha) {
  self->glColor4f(red, green, blue, alpha);
}

//  void QOpenGLFunctions_1_0::glColor4dv(const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_010glColor4dvEPKd(
    QOpenGLFunctions_1_0 *self,
    const GLdouble *v) {
  self->glColor4dv(v);
}

//  void QOpenGLFunctions_1_0::glColor4d(GLdouble red, GLdouble green,
//      GLdouble blue, GLdouble alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_09glColor4dEdddd(
    QOpenGLFunctions_1_0 *self,
    GLdouble red,
    GLdouble green,
    GLdouble blue,
    GLdouble alpha) {
  self->glColor4d(red, green, blue, alpha);
}

//  void QOpenGLFunctions_1_0::glColor4bv(const GLbyte *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_010glColor4bvEPKa(
    QOpenGLFunctions_1_0 *self,
    const GLbyte *v) {
  self->glColor4bv(v);
}

//  void QOpenGLFunctions_1_0::glColor4b(GLbyte red, GLbyte green, GLbyte
//      blue, GLbyte alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_09glColor4bEaaaa(
    QOpenGLFunctions_1_0 *self,
    GLbyte red,
    GLbyte green,
    GLbyte blue,
    GLbyte alpha) {
  self->glColor4b(red, green, blue, alpha);
}

//  void QOpenGLFunctions_1_0::glColor3usv(const GLushort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_011glColor3usvEPKt(
    QOpenGLFunctions_1_0 *self,
    const GLushort *v) {
  self->glColor3usv(v);
}

//  void QOpenGLFunctions_1_0::glColor3us(GLushort red, GLushort green,
//      GLushort blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_010glColor3usEttt(
    QOpenGLFunctions_1_0 *self,
    GLushort red,
    GLushort green,
    GLushort blue) {
  self->glColor3us(red, green, blue);
}

//  void QOpenGLFunctions_1_0::glColor3uiv(const GLuint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_011glColor3uivEPKj(
    QOpenGLFunctions_1_0 *self,
    const GLuint *v) {
  self->glColor3uiv(v);
}

//  void QOpenGLFunctions_1_0::glColor3ui(GLuint red, GLuint green, GLuint
//      blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_010glColor3uiEjjj(
    QOpenGLFunctions_1_0 *self,
    GLuint red,
    GLuint green,
    GLuint blue) {
  self->glColor3ui(red, green, blue);
}

//  void QOpenGLFunctions_1_0::glColor3ubv(const GLubyte *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_011glColor3ubvEPKh(
    QOpenGLFunctions_1_0 *self,
    const GLubyte *v) {
  self->glColor3ubv(v);
}

//  void QOpenGLFunctions_1_0::glColor3ub(GLubyte red, GLubyte green, GLubyte
//      blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_010glColor3ubEhhh(
    QOpenGLFunctions_1_0 *self,
    GLubyte red,
    GLubyte green,
    GLubyte blue) {
  self->glColor3ub(red, green, blue);
}

//  void QOpenGLFunctions_1_0::glColor3sv(const GLshort *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_010glColor3svEPKs(
    QOpenGLFunctions_1_0 *self,
    const GLshort *v) {
  self->glColor3sv(v);
}

//  void QOpenGLFunctions_1_0::glColor3s(GLshort red, GLshort green, GLshort
//      blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_09glColor3sEsss(
    QOpenGLFunctions_1_0 *self,
    GLshort red,
    GLshort green,
    GLshort blue) {
  self->glColor3s(red, green, blue);
}

//  void QOpenGLFunctions_1_0::glColor3iv(const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_010glColor3ivEPKi(
    QOpenGLFunctions_1_0 *self,
    const GLint *v) {
  self->glColor3iv(v);
}

//  void QOpenGLFunctions_1_0::glColor3i(GLint red, GLint green, GLint blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_09glColor3iEiii(
    QOpenGLFunctions_1_0 *self,
    GLint red,
    GLint green,
    GLint blue) {
  self->glColor3i(red, green, blue);
}

//  void QOpenGLFunctions_1_0::glColor3fv(const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_010glColor3fvEPKf(
    QOpenGLFunctions_1_0 *self,
    const GLfloat *v) {
  self->glColor3fv(v);
}

//  void QOpenGLFunctions_1_0::glColor3f(GLfloat red, GLfloat green, GLfloat
//      blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_09glColor3fEfff(
    QOpenGLFunctions_1_0 *self,
    GLfloat red,
    GLfloat green,
    GLfloat blue) {
  self->glColor3f(red, green, blue);
}

//  void QOpenGLFunctions_1_0::glColor3dv(const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_010glColor3dvEPKd(
    QOpenGLFunctions_1_0 *self,
    const GLdouble *v) {
  self->glColor3dv(v);
}

//  void QOpenGLFunctions_1_0::glColor3d(GLdouble red, GLdouble green,
//      GLdouble blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_09glColor3dEddd(
    QOpenGLFunctions_1_0 *self,
    GLdouble red,
    GLdouble green,
    GLdouble blue) {
  self->glColor3d(red, green, blue);
}

//  void QOpenGLFunctions_1_0::glColor3bv(const GLbyte *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_010glColor3bvEPKa(
    QOpenGLFunctions_1_0 *self,
    const GLbyte *v) {
  self->glColor3bv(v);
}

//  void QOpenGLFunctions_1_0::glColor3b(GLbyte red, GLbyte green, GLbyte
//      blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_09glColor3bEaaa(
    QOpenGLFunctions_1_0 *self,
    GLbyte red,
    GLbyte green,
    GLbyte blue) {
  self->glColor3b(red, green, blue);
}

//  void QOpenGLFunctions_1_0::glBitmap(GLsizei width, GLsizei height,
//      GLfloat xorig, GLfloat yorig, GLfloat xmove, GLfloat ymove, const
//      GLubyte *bitmap)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_08glBitmapEiiffffPKh(
    QOpenGLFunctions_1_0 *self,
    GLsizei width,
    GLsizei height,
    GLfloat xorig,
    GLfloat yorig,
    GLfloat xmove,
    GLfloat ymove,
    const GLubyte *bitmap) {
  self->glBitmap(width, height, xorig, yorig, xmove, ymove, bitmap);
}

//  void QOpenGLFunctions_1_0::glBegin(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_07glBeginEj(
    QOpenGLFunctions_1_0 *self,
    GLenum mode) {
  self->glBegin(mode);
}

//  void QOpenGLFunctions_1_0::glListBase(GLuint base)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_010glListBaseEj(
    QOpenGLFunctions_1_0 *self,
    GLuint base) {
  self->glListBase(base);
}

//  GLuint QOpenGLFunctions_1_0::glGenLists(GLsizei range)
extern "C" Q_DECL_EXPORT
GLuint ritual_ZN20QOpenGLFunctions_1_010glGenListsEi(
    QOpenGLFunctions_1_0 *self,
    GLsizei range) {
  return self->glGenLists(range);
}

//  void QOpenGLFunctions_1_0::glDeleteLists(GLuint list, GLsizei range)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_013glDeleteListsEji(
    QOpenGLFunctions_1_0 *self,
    GLuint list,
    GLsizei range) {
  self->glDeleteLists(list, range);
}

//  void QOpenGLFunctions_1_0::glCallLists(GLsizei n, GLenum type, const
//      GLvoid *lists)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_011glCallListsEijPKv(
    QOpenGLFunctions_1_0 *self,
    GLsizei n,
    GLenum type,
    const GLvoid *lists) {
  self->glCallLists(n, type, lists);
}

//  void QOpenGLFunctions_1_0::glCallList(GLuint list)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_010glCallListEj(
    QOpenGLFunctions_1_0 *self,
    GLuint list) {
  self->glCallList(list);
}

//  void QOpenGLFunctions_1_0::glEndList()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_09glEndListEv(
    QOpenGLFunctions_1_0 *self) {
  self->glEndList();
}

//  void QOpenGLFunctions_1_0::glNewList(GLuint list, GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLFunctions_1_09glNewListEjj(
    QOpenGLFunctions_1_0 *self,
    GLuint list,
    GLenum mode) {
  self->glNewList(list, mode);
}

//  bool QOpenGLFunctions_1_0::isContextCompatible(QOpenGLContext *context)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QOpenGLFunctions_1_019isContextCompatibleEP14QOpenGLContext(
    QOpenGLContext *context) {
  return QOpenGLFunctions_1_0::isContextCompatible(context);
}

//  QOpenGLVersionProfile QOpenGLFunctions_1_0::versionProfile()
extern "C" Q_DECL_EXPORT
QOpenGLVersionProfile *ritual_ZN20QOpenGLFunctions_1_014versionProfileEv() {
  return new QOpenGLVersionProfile(QOpenGLFunctions_1_0::versionProfile());
}

//  a Python function taken by a CuteQOpenGLFunctions_1_0, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QOpenGLFunctions_1_0(
    QOpenGLFunctions_1_0 *self,
    const char *key,
    void *call) {
  return static_cast<CuteQOpenGLFunctions_1_0 *>(self)->take(key, call);
}

//  bool QOpenGLFunctions_1_0::initializeOpenGLFunctions()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN20QOpenGLFunctions_1_025initializeOpenGLFunctionsEv(
    QOpenGLFunctions_1_0 *self) {
  return self->QOpenGLFunctions_1_0::initializeOpenGLFunctions();
}

#endif  // !defined(QT_NO_OPENGL) && !QT_CONFIG(opengles2)
#endif  // !QT_CONFIG(opengles2)
