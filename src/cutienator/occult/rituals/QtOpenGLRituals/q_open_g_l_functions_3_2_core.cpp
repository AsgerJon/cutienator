//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/qopenglfunctions_3_2_core.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/qtguiglobal.h>
#include <QtOpenGL/qtopenglglobal.h>
#if !QT_CONFIG(opengles2)
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

//  GLboolean QOpenGLFunctions_3_2_Core::glIsEnabled(GLenum cap)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN25QOpenGLFunctions_3_2_Core11glIsEnabledEj(
    QOpenGLFunctions_3_2_Core *self,
    GLenum cap) {
  return self->glIsEnabled(cap);
}

//  void QOpenGLFunctions_3_2_Core::glGetTexLevelParameteriv(GLenum target,
//      GLint level, GLenum pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core24glGetTexLevelParameterivEjijPi(
    QOpenGLFunctions_3_2_Core *self,
    GLenum target,
    GLint level,
    GLenum pname,
    GLint *params) {
  self->glGetTexLevelParameteriv(target, level, pname, params);
}

//  void QOpenGLFunctions_3_2_Core::glGetTexLevelParameterfv(GLenum target,
//      GLint level, GLenum pname, GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core24glGetTexLevelParameterfvEjijPf(
    QOpenGLFunctions_3_2_Core *self,
    GLenum target,
    GLint level,
    GLenum pname,
    GLfloat *params) {
  self->glGetTexLevelParameterfv(target, level, pname, params);
}

//  void QOpenGLFunctions_3_2_Core::glGetTexParameteriv(GLenum target, GLenum
//      pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core19glGetTexParameterivEjjPi(
    QOpenGLFunctions_3_2_Core *self,
    GLenum target,
    GLenum pname,
    GLint *params) {
  self->glGetTexParameteriv(target, pname, params);
}

//  void QOpenGLFunctions_3_2_Core::glGetTexParameterfv(GLenum target, GLenum
//      pname, GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core19glGetTexParameterfvEjjPf(
    QOpenGLFunctions_3_2_Core *self,
    GLenum target,
    GLenum pname,
    GLfloat *params) {
  self->glGetTexParameterfv(target, pname, params);
}

//  void QOpenGLFunctions_3_2_Core::glGetTexImage(GLenum target, GLint level,
//      GLenum format, GLenum type, GLvoid *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core13glGetTexImageEjijjPv(
    QOpenGLFunctions_3_2_Core *self,
    GLenum target,
    GLint level,
    GLenum format,
    GLenum type,
    GLvoid *pixels) {
  self->glGetTexImage(target, level, format, type, pixels);
}

//  const GLubyte *QOpenGLFunctions_3_2_Core::glGetString(GLenum name)
extern "C" Q_DECL_EXPORT
const GLubyte *ritual_ZN25QOpenGLFunctions_3_2_Core11glGetStringEj(
    QOpenGLFunctions_3_2_Core *self,
    GLenum name) {
  return self->glGetString(name);
}

//  void QOpenGLFunctions_3_2_Core::glGetIntegerv(GLenum pname, GLint
//      *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core13glGetIntegervEjPi(
    QOpenGLFunctions_3_2_Core *self,
    GLenum pname,
    GLint *params) {
  self->glGetIntegerv(pname, params);
}

//  void QOpenGLFunctions_3_2_Core::glGetFloatv(GLenum pname, GLfloat
//      *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core11glGetFloatvEjPf(
    QOpenGLFunctions_3_2_Core *self,
    GLenum pname,
    GLfloat *params) {
  self->glGetFloatv(pname, params);
}

//  GLenum QOpenGLFunctions_3_2_Core::glGetError()
extern "C" Q_DECL_EXPORT
GLenum ritual_ZN25QOpenGLFunctions_3_2_Core10glGetErrorEv(
    QOpenGLFunctions_3_2_Core *self) {
  return self->glGetError();
}

//  void QOpenGLFunctions_3_2_Core::glGetDoublev(GLenum pname, GLdouble
//      *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core12glGetDoublevEjPd(
    QOpenGLFunctions_3_2_Core *self,
    GLenum pname,
    GLdouble *params) {
  self->glGetDoublev(pname, params);
}

//  void QOpenGLFunctions_3_2_Core::glGetBooleanv(GLenum pname, GLboolean
//      *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core13glGetBooleanvEjPh(
    QOpenGLFunctions_3_2_Core *self,
    GLenum pname,
    GLboolean *params) {
  self->glGetBooleanv(pname, params);
}

//  void QOpenGLFunctions_3_2_Core::glReadPixels(GLint x, GLint y, GLsizei
//      width, GLsizei height, GLenum format, GLenum type, GLvoid *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core12glReadPixelsEiiiijjPv(
    QOpenGLFunctions_3_2_Core *self,
    GLint x,
    GLint y,
    GLsizei width,
    GLsizei height,
    GLenum format,
    GLenum type,
    GLvoid *pixels) {
  self->glReadPixels(x, y, width, height, format, type, pixels);
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

//  void QOpenGLFunctions_3_2_Core::glTexImage2D(GLenum target, GLint level,
//      GLint internalformat, GLsizei width, GLsizei height, GLint border,
//      GLenum format, GLenum type, const GLvoid *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core12glTexImage2DEjiiiiijjPKv(
    QOpenGLFunctions_3_2_Core *self,
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

//  void QOpenGLFunctions_3_2_Core::glTexImage1D(GLenum target, GLint level,
//      GLint internalformat, GLsizei width, GLint border, GLenum format,
//      GLenum type, const GLvoid *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core12glTexImage1DEjiiiijjPKv(
    QOpenGLFunctions_3_2_Core *self,
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

//  void QOpenGLFunctions_3_2_Core::glTexParameteriv(GLenum target, GLenum
//      pname, const GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core16glTexParameterivEjjPKi(
    QOpenGLFunctions_3_2_Core *self,
    GLenum target,
    GLenum pname,
    const GLint *params) {
  self->glTexParameteriv(target, pname, params);
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

//  void QOpenGLFunctions_3_2_Core::glTexParameterfv(GLenum target, GLenum
//      pname, const GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core16glTexParameterfvEjjPKf(
    QOpenGLFunctions_3_2_Core *self,
    GLenum target,
    GLenum pname,
    const GLfloat *params) {
  self->glTexParameterfv(target, pname, params);
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

//  GLboolean QOpenGLFunctions_3_2_Core::glIsTexture(GLuint texture)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN25QOpenGLFunctions_3_2_Core11glIsTextureEj(
    QOpenGLFunctions_3_2_Core *self,
    GLuint texture) {
  return self->glIsTexture(texture);
}

//  void QOpenGLFunctions_3_2_Core::glGenTextures(GLsizei n, GLuint
//      *textures)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core13glGenTexturesEiPj(
    QOpenGLFunctions_3_2_Core *self,
    GLsizei n,
    GLuint *textures) {
  self->glGenTextures(n, textures);
}

//  void QOpenGLFunctions_3_2_Core::glDeleteTextures(GLsizei n, const GLuint
//      *textures)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core16glDeleteTexturesEiPKj(
    QOpenGLFunctions_3_2_Core *self,
    GLsizei n,
    const GLuint *textures) {
  self->glDeleteTextures(n, textures);
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

//  void QOpenGLFunctions_3_2_Core::glTexSubImage2D(GLenum target, GLint
//      level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height,
//      GLenum format, GLenum type, const GLvoid *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core15glTexSubImage2DEjiiiiijjPKv(
    QOpenGLFunctions_3_2_Core *self,
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

//  void QOpenGLFunctions_3_2_Core::glTexSubImage1D(GLenum target, GLint
//      level, GLint xoffset, GLsizei width, GLenum format, GLenum type,
//      const GLvoid *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core15glTexSubImage1DEjiiijjPKv(
    QOpenGLFunctions_3_2_Core *self,
    GLenum target,
    GLint level,
    GLint xoffset,
    GLsizei width,
    GLenum format,
    GLenum type,
    const GLvoid *pixels) {
  self->glTexSubImage1D(target, level, xoffset, width, format, type, pixels);
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

//  void QOpenGLFunctions_3_2_Core::glDrawElements(GLenum mode, GLsizei
//      count, GLenum type, const GLvoid *indices)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core14glDrawElementsEjijPKv(
    QOpenGLFunctions_3_2_Core *self,
    GLenum mode,
    GLsizei count,
    GLenum type,
    const GLvoid *indices) {
  self->glDrawElements(mode, count, type, indices);
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

//  void QOpenGLFunctions_3_2_Core::glTexSubImage3D(GLenum target, GLint
//      level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width,
//      GLsizei height, GLsizei depth, GLenum format, GLenum type, const
//      GLvoid *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core15glTexSubImage3DEjiiiiiiijjPKv(
    QOpenGLFunctions_3_2_Core *self,
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

//  void QOpenGLFunctions_3_2_Core::glTexImage3D(GLenum target, GLint level,
//      GLint internalformat, GLsizei width, GLsizei height, GLsizei depth,
//      GLint border, GLenum format, GLenum type, const GLvoid *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core12glTexImage3DEjiiiiiijjPKv(
    QOpenGLFunctions_3_2_Core *self,
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

//  void QOpenGLFunctions_3_2_Core::glDrawRangeElements(GLenum mode, GLuint
//      start, GLuint end, GLsizei count, GLenum type, const GLvoid *indices)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core19glDrawRangeElementsEjjjijPKv(
    QOpenGLFunctions_3_2_Core *self,
    GLenum mode,
    GLuint start,
    GLuint end,
    GLsizei count,
    GLenum type,
    const GLvoid *indices) {
  self->glDrawRangeElements(mode, start, end, count, type, indices);
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

//  void QOpenGLFunctions_3_2_Core::glGetCompressedTexImage(GLenum target,
//      GLint level, GLvoid *img)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core23glGetCompressedTexImageEjiPv(
    QOpenGLFunctions_3_2_Core *self,
    GLenum target,
    GLint level,
    GLvoid *img) {
  self->glGetCompressedTexImage(target, level, img);
}

//  void QOpenGLFunctions_3_2_Core::glCompressedTexSubImage1D(GLenum target,
//      GLint level, GLint xoffset, GLsizei width, GLenum format, GLsizei
//      imageSize, const GLvoid *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core25glCompressedTexSubImage1DEjiiijiPKv(
    QOpenGLFunctions_3_2_Core *self,
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

//  void QOpenGLFunctions_3_2_Core::glCompressedTexSubImage2D(GLenum target,
//      GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei
//      height, GLenum format, GLsizei imageSize, const GLvoid *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core25glCompressedTexSubImage2DEjiiiiijiPKv(
    QOpenGLFunctions_3_2_Core *self,
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

//  void QOpenGLFunctions_3_2_Core::glCompressedTexSubImage3D(GLenum target,
//      GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei
//      width, GLsizei height, GLsizei depth, GLenum format, GLsizei
//      imageSize, const GLvoid *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core25glCompressedTexSubImage3DEjiiiiiiijiPKv(
    QOpenGLFunctions_3_2_Core *self,
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

//  void QOpenGLFunctions_3_2_Core::glCompressedTexImage1D(GLenum target,
//      GLint level, GLenum internalformat, GLsizei width, GLint border,
//      GLsizei imageSize, const GLvoid *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core22glCompressedTexImage1DEjijiiiPKv(
    QOpenGLFunctions_3_2_Core *self,
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

//  void QOpenGLFunctions_3_2_Core::glCompressedTexImage2D(GLenum target,
//      GLint level, GLenum internalformat, GLsizei width, GLsizei height,
//      GLint border, GLsizei imageSize, const GLvoid *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core22glCompressedTexImage2DEjijiiiiPKv(
    QOpenGLFunctions_3_2_Core *self,
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

//  void QOpenGLFunctions_3_2_Core::glCompressedTexImage3D(GLenum target,
//      GLint level, GLenum internalformat, GLsizei width, GLsizei height,
//      GLsizei depth, GLint border, GLsizei imageSize, const GLvoid *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core22glCompressedTexImage3DEjijiiiiiPKv(
    QOpenGLFunctions_3_2_Core *self,
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

//  void QOpenGLFunctions_3_2_Core::glPointParameteriv(GLenum pname, const
//      GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core18glPointParameterivEjPKi(
    QOpenGLFunctions_3_2_Core *self,
    GLenum pname,
    const GLint *params) {
  self->glPointParameteriv(pname, params);
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

//  void QOpenGLFunctions_3_2_Core::glPointParameterfv(GLenum pname, const
//      GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core18glPointParameterfvEjPKf(
    QOpenGLFunctions_3_2_Core *self,
    GLenum pname,
    const GLfloat *params) {
  self->glPointParameterfv(pname, params);
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

//  void QOpenGLFunctions_3_2_Core::glMultiDrawElements(GLenum mode, const
//      GLsizei *count, GLenum type, const GLvoid *const *indices, GLsizei
//      drawcount)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core19glMultiDrawElementsEjPKijPKPKvi(
    QOpenGLFunctions_3_2_Core *self,
    GLenum mode,
    const GLsizei *count,
    GLenum type,
    const GLvoid *const *indices,
    GLsizei drawcount) {
  self->glMultiDrawElements(mode, count, type, indices, drawcount);
}

//  void QOpenGLFunctions_3_2_Core::glMultiDrawArrays(GLenum mode, const
//      GLint *first, const GLsizei *count, GLsizei drawcount)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core17glMultiDrawArraysEjPKiS1_i(
    QOpenGLFunctions_3_2_Core *self,
    GLenum mode,
    const GLint *first,
    const GLsizei *count,
    GLsizei drawcount) {
  self->glMultiDrawArrays(mode, first, count, drawcount);
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

//  void QOpenGLFunctions_3_2_Core::glGetBufferPointerv(GLenum target, GLenum
//      pname, GLvoid **params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core19glGetBufferPointervEjjPPv(
    QOpenGLFunctions_3_2_Core *self,
    GLenum target,
    GLenum pname,
    GLvoid **params) {
  self->glGetBufferPointerv(target, pname, params);
}

//  void QOpenGLFunctions_3_2_Core::glGetBufferParameteriv(GLenum target,
//      GLenum pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core22glGetBufferParameterivEjjPi(
    QOpenGLFunctions_3_2_Core *self,
    GLenum target,
    GLenum pname,
    GLint *params) {
  self->glGetBufferParameteriv(target, pname, params);
}

//  GLboolean QOpenGLFunctions_3_2_Core::glUnmapBuffer(GLenum target)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN25QOpenGLFunctions_3_2_Core13glUnmapBufferEj(
    QOpenGLFunctions_3_2_Core *self,
    GLenum target) {
  return self->glUnmapBuffer(target);
}

//  GLvoid *QOpenGLFunctions_3_2_Core::glMapBuffer(GLenum target, GLenum
//      access)
extern "C" Q_DECL_EXPORT
GLvoid *ritual_ZN25QOpenGLFunctions_3_2_Core11glMapBufferEjj(
    QOpenGLFunctions_3_2_Core *self,
    GLenum target,
    GLenum access) {
  return self->glMapBuffer(target, access);
}

//  void QOpenGLFunctions_3_2_Core::glGetBufferSubData(GLenum target,
//      GLintptr offset, GLsizeiptr size, GLvoid *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core18glGetBufferSubDataEjllPv(
    QOpenGLFunctions_3_2_Core *self,
    GLenum target,
    long long offset,
    long long size,
    GLvoid *data) {
  self->glGetBufferSubData(target, offset, size, data);
}

//  void QOpenGLFunctions_3_2_Core::glBufferSubData(GLenum target, GLintptr
//      offset, GLsizeiptr size, const GLvoid *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core15glBufferSubDataEjllPKv(
    QOpenGLFunctions_3_2_Core *self,
    GLenum target,
    long long offset,
    long long size,
    const GLvoid *data) {
  self->glBufferSubData(target, offset, size, data);
}

//  void QOpenGLFunctions_3_2_Core::glBufferData(GLenum target, GLsizeiptr
//      size, const GLvoid *data, GLenum usage)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core12glBufferDataEjlPKvj(
    QOpenGLFunctions_3_2_Core *self,
    GLenum target,
    long long size,
    const GLvoid *data,
    GLenum usage) {
  self->glBufferData(target, size, data, usage);
}

//  GLboolean QOpenGLFunctions_3_2_Core::glIsBuffer(GLuint buffer)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN25QOpenGLFunctions_3_2_Core10glIsBufferEj(
    QOpenGLFunctions_3_2_Core *self,
    GLuint buffer) {
  return self->glIsBuffer(buffer);
}

//  void QOpenGLFunctions_3_2_Core::glGenBuffers(GLsizei n, GLuint *buffers)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core12glGenBuffersEiPj(
    QOpenGLFunctions_3_2_Core *self,
    GLsizei n,
    GLuint *buffers) {
  self->glGenBuffers(n, buffers);
}

//  void QOpenGLFunctions_3_2_Core::glDeleteBuffers(GLsizei n, const GLuint
//      *buffers)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core15glDeleteBuffersEiPKj(
    QOpenGLFunctions_3_2_Core *self,
    GLsizei n,
    const GLuint *buffers) {
  self->glDeleteBuffers(n, buffers);
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

//  void QOpenGLFunctions_3_2_Core::glGetQueryObjectuiv(GLuint id, GLenum
//      pname, GLuint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core19glGetQueryObjectuivEjjPj(
    QOpenGLFunctions_3_2_Core *self,
    GLuint id,
    GLenum pname,
    GLuint *params) {
  self->glGetQueryObjectuiv(id, pname, params);
}

//  void QOpenGLFunctions_3_2_Core::glGetQueryObjectiv(GLuint id, GLenum
//      pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core18glGetQueryObjectivEjjPi(
    QOpenGLFunctions_3_2_Core *self,
    GLuint id,
    GLenum pname,
    GLint *params) {
  self->glGetQueryObjectiv(id, pname, params);
}

//  void QOpenGLFunctions_3_2_Core::glGetQueryiv(GLenum target, GLenum pname,
//      GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core12glGetQueryivEjjPi(
    QOpenGLFunctions_3_2_Core *self,
    GLenum target,
    GLenum pname,
    GLint *params) {
  self->glGetQueryiv(target, pname, params);
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

//  GLboolean QOpenGLFunctions_3_2_Core::glIsQuery(GLuint id)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN25QOpenGLFunctions_3_2_Core9glIsQueryEj(
    QOpenGLFunctions_3_2_Core *self,
    GLuint id) {
  return self->glIsQuery(id);
}

//  void QOpenGLFunctions_3_2_Core::glDeleteQueries(GLsizei n, const GLuint
//      *ids)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core15glDeleteQueriesEiPKj(
    QOpenGLFunctions_3_2_Core *self,
    GLsizei n,
    const GLuint *ids) {
  self->glDeleteQueries(n, ids);
}

//  void QOpenGLFunctions_3_2_Core::glGenQueries(GLsizei n, GLuint *ids)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core12glGenQueriesEiPj(
    QOpenGLFunctions_3_2_Core *self,
    GLsizei n,
    GLuint *ids) {
  self->glGenQueries(n, ids);
}

//  void QOpenGLFunctions_3_2_Core::glVertexAttribPointer(GLuint index, GLint
//      size, GLenum type, GLboolean normalized, GLsizei stride, const GLvoid
//      *pointer)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core21glVertexAttribPointerEjijhiPKv(
    QOpenGLFunctions_3_2_Core *self,
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

//  void QOpenGLFunctions_3_2_Core::glValidateProgram(GLuint program)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core17glValidateProgramEj(
    QOpenGLFunctions_3_2_Core *self,
    GLuint program) {
  self->glValidateProgram(program);
}

//  void QOpenGLFunctions_3_2_Core::glUniformMatrix4fv(GLint location,
//      GLsizei count, GLboolean transpose, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core18glUniformMatrix4fvEiihPKf(
    QOpenGLFunctions_3_2_Core *self,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLfloat *value) {
  self->glUniformMatrix4fv(location, count, transpose, value);
}

//  void QOpenGLFunctions_3_2_Core::glUniformMatrix3fv(GLint location,
//      GLsizei count, GLboolean transpose, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core18glUniformMatrix3fvEiihPKf(
    QOpenGLFunctions_3_2_Core *self,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLfloat *value) {
  self->glUniformMatrix3fv(location, count, transpose, value);
}

//  void QOpenGLFunctions_3_2_Core::glUniformMatrix2fv(GLint location,
//      GLsizei count, GLboolean transpose, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core18glUniformMatrix2fvEiihPKf(
    QOpenGLFunctions_3_2_Core *self,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLfloat *value) {
  self->glUniformMatrix2fv(location, count, transpose, value);
}

//  void QOpenGLFunctions_3_2_Core::glUniform4iv(GLint location, GLsizei
//      count, const GLint *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core12glUniform4ivEiiPKi(
    QOpenGLFunctions_3_2_Core *self,
    GLint location,
    GLsizei count,
    const GLint *value) {
  self->glUniform4iv(location, count, value);
}

//  void QOpenGLFunctions_3_2_Core::glUniform3iv(GLint location, GLsizei
//      count, const GLint *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core12glUniform3ivEiiPKi(
    QOpenGLFunctions_3_2_Core *self,
    GLint location,
    GLsizei count,
    const GLint *value) {
  self->glUniform3iv(location, count, value);
}

//  void QOpenGLFunctions_3_2_Core::glUniform2iv(GLint location, GLsizei
//      count, const GLint *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core12glUniform2ivEiiPKi(
    QOpenGLFunctions_3_2_Core *self,
    GLint location,
    GLsizei count,
    const GLint *value) {
  self->glUniform2iv(location, count, value);
}

//  void QOpenGLFunctions_3_2_Core::glUniform1iv(GLint location, GLsizei
//      count, const GLint *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core12glUniform1ivEiiPKi(
    QOpenGLFunctions_3_2_Core *self,
    GLint location,
    GLsizei count,
    const GLint *value) {
  self->glUniform1iv(location, count, value);
}

//  void QOpenGLFunctions_3_2_Core::glUniform4fv(GLint location, GLsizei
//      count, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core12glUniform4fvEiiPKf(
    QOpenGLFunctions_3_2_Core *self,
    GLint location,
    GLsizei count,
    const GLfloat *value) {
  self->glUniform4fv(location, count, value);
}

//  void QOpenGLFunctions_3_2_Core::glUniform3fv(GLint location, GLsizei
//      count, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core12glUniform3fvEiiPKf(
    QOpenGLFunctions_3_2_Core *self,
    GLint location,
    GLsizei count,
    const GLfloat *value) {
  self->glUniform3fv(location, count, value);
}

//  void QOpenGLFunctions_3_2_Core::glUniform2fv(GLint location, GLsizei
//      count, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core12glUniform2fvEiiPKf(
    QOpenGLFunctions_3_2_Core *self,
    GLint location,
    GLsizei count,
    const GLfloat *value) {
  self->glUniform2fv(location, count, value);
}

//  void QOpenGLFunctions_3_2_Core::glUniform1fv(GLint location, GLsizei
//      count, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core12glUniform1fvEiiPKf(
    QOpenGLFunctions_3_2_Core *self,
    GLint location,
    GLsizei count,
    const GLfloat *value) {
  self->glUniform1fv(location, count, value);
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

//  void QOpenGLFunctions_3_2_Core::glShaderSource(GLuint shader, GLsizei
//      count, const GLchar *const *string, const GLint *length)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core14glShaderSourceEjiPKPKcPKi(
    QOpenGLFunctions_3_2_Core *self,
    GLuint shader,
    GLsizei count,
    const GLchar *const *string,
    const GLint *length) {
  self->glShaderSource(shader, count, string, length);
}

//  void QOpenGLFunctions_3_2_Core::glLinkProgram(GLuint program)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core13glLinkProgramEj(
    QOpenGLFunctions_3_2_Core *self,
    GLuint program) {
  self->glLinkProgram(program);
}

//  GLboolean QOpenGLFunctions_3_2_Core::glIsShader(GLuint shader)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN25QOpenGLFunctions_3_2_Core10glIsShaderEj(
    QOpenGLFunctions_3_2_Core *self,
    GLuint shader) {
  return self->glIsShader(shader);
}

//  GLboolean QOpenGLFunctions_3_2_Core::glIsProgram(GLuint program)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN25QOpenGLFunctions_3_2_Core11glIsProgramEj(
    QOpenGLFunctions_3_2_Core *self,
    GLuint program) {
  return self->glIsProgram(program);
}

//  void QOpenGLFunctions_3_2_Core::glGetVertexAttribPointerv(GLuint index,
//      GLenum pname, GLvoid **pointer)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core25glGetVertexAttribPointervEjjPPv(
    QOpenGLFunctions_3_2_Core *self,
    GLuint index,
    GLenum pname,
    GLvoid **pointer) {
  self->glGetVertexAttribPointerv(index, pname, pointer);
}

//  void QOpenGLFunctions_3_2_Core::glGetVertexAttribiv(GLuint index, GLenum
//      pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core19glGetVertexAttribivEjjPi(
    QOpenGLFunctions_3_2_Core *self,
    GLuint index,
    GLenum pname,
    GLint *params) {
  self->glGetVertexAttribiv(index, pname, params);
}

//  void QOpenGLFunctions_3_2_Core::glGetVertexAttribfv(GLuint index, GLenum
//      pname, GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core19glGetVertexAttribfvEjjPf(
    QOpenGLFunctions_3_2_Core *self,
    GLuint index,
    GLenum pname,
    GLfloat *params) {
  self->glGetVertexAttribfv(index, pname, params);
}

//  void QOpenGLFunctions_3_2_Core::glGetVertexAttribdv(GLuint index, GLenum
//      pname, GLdouble *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core19glGetVertexAttribdvEjjPd(
    QOpenGLFunctions_3_2_Core *self,
    GLuint index,
    GLenum pname,
    GLdouble *params) {
  self->glGetVertexAttribdv(index, pname, params);
}

//  void QOpenGLFunctions_3_2_Core::glGetUniformiv(GLuint program, GLint
//      location, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core14glGetUniformivEjiPi(
    QOpenGLFunctions_3_2_Core *self,
    GLuint program,
    GLint location,
    GLint *params) {
  self->glGetUniformiv(program, location, params);
}

//  void QOpenGLFunctions_3_2_Core::glGetUniformfv(GLuint program, GLint
//      location, GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core14glGetUniformfvEjiPf(
    QOpenGLFunctions_3_2_Core *self,
    GLuint program,
    GLint location,
    GLfloat *params) {
  self->glGetUniformfv(program, location, params);
}

//  GLint QOpenGLFunctions_3_2_Core::glGetUniformLocation(GLuint program,
//      const GLchar *name)
extern "C" Q_DECL_EXPORT
GLint ritual_ZN25QOpenGLFunctions_3_2_Core20glGetUniformLocationEjPKc(
    QOpenGLFunctions_3_2_Core *self,
    GLuint program,
    const GLchar *name) {
  return self->glGetUniformLocation(program, name);
}

//  void QOpenGLFunctions_3_2_Core::glGetShaderSource(GLuint shader, GLsizei
//      bufSize, GLsizei *length, GLchar *source)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core17glGetShaderSourceEjiPiPc(
    QOpenGLFunctions_3_2_Core *self,
    GLuint shader,
    GLsizei bufSize,
    GLsizei *length,
    GLchar *source) {
  self->glGetShaderSource(shader, bufSize, length, source);
}

//  void QOpenGLFunctions_3_2_Core::glGetShaderInfoLog(GLuint shader, GLsizei
//      bufSize, GLsizei *length, GLchar *infoLog)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core18glGetShaderInfoLogEjiPiPc(
    QOpenGLFunctions_3_2_Core *self,
    GLuint shader,
    GLsizei bufSize,
    GLsizei *length,
    GLchar *infoLog) {
  self->glGetShaderInfoLog(shader, bufSize, length, infoLog);
}

//  void QOpenGLFunctions_3_2_Core::glGetShaderiv(GLuint shader, GLenum
//      pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core13glGetShaderivEjjPi(
    QOpenGLFunctions_3_2_Core *self,
    GLuint shader,
    GLenum pname,
    GLint *params) {
  self->glGetShaderiv(shader, pname, params);
}

//  void QOpenGLFunctions_3_2_Core::glGetProgramInfoLog(GLuint program,
//      GLsizei bufSize, GLsizei *length, GLchar *infoLog)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core19glGetProgramInfoLogEjiPiPc(
    QOpenGLFunctions_3_2_Core *self,
    GLuint program,
    GLsizei bufSize,
    GLsizei *length,
    GLchar *infoLog) {
  self->glGetProgramInfoLog(program, bufSize, length, infoLog);
}

//  void QOpenGLFunctions_3_2_Core::glGetProgramiv(GLuint program, GLenum
//      pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core14glGetProgramivEjjPi(
    QOpenGLFunctions_3_2_Core *self,
    GLuint program,
    GLenum pname,
    GLint *params) {
  self->glGetProgramiv(program, pname, params);
}

//  GLint QOpenGLFunctions_3_2_Core::glGetAttribLocation(GLuint program,
//      const GLchar *name)
extern "C" Q_DECL_EXPORT
GLint ritual_ZN25QOpenGLFunctions_3_2_Core19glGetAttribLocationEjPKc(
    QOpenGLFunctions_3_2_Core *self,
    GLuint program,
    const GLchar *name) {
  return self->glGetAttribLocation(program, name);
}

//  void QOpenGLFunctions_3_2_Core::glGetAttachedShaders(GLuint program,
//      GLsizei maxCount, GLsizei *count, GLuint *obj)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core20glGetAttachedShadersEjiPiPj(
    QOpenGLFunctions_3_2_Core *self,
    GLuint program,
    GLsizei maxCount,
    GLsizei *count,
    GLuint *obj) {
  self->glGetAttachedShaders(program, maxCount, count, obj);
}

//  void QOpenGLFunctions_3_2_Core::glGetActiveUniform(GLuint program, GLuint
//      index, GLsizei bufSize, GLsizei *length, GLint *size, GLenum *type,
//      GLchar *name)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core18glGetActiveUniformEjjiPiS0_PjPc(
    QOpenGLFunctions_3_2_Core *self,
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

//  void QOpenGLFunctions_3_2_Core::glGetActiveAttrib(GLuint program, GLuint
//      index, GLsizei bufSize, GLsizei *length, GLint *size, GLenum *type,
//      GLchar *name)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core17glGetActiveAttribEjjiPiS0_PjPc(
    QOpenGLFunctions_3_2_Core *self,
    GLuint program,
    GLuint index,
    GLsizei bufSize,
    GLsizei *length,
    GLint *size,
    GLenum *type,
    GLchar *name) {
  self->glGetActiveAttrib(program, index, bufSize, length, size, type, name);
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

//  GLuint QOpenGLFunctions_3_2_Core::glCreateShader(GLenum type)
extern "C" Q_DECL_EXPORT
GLuint ritual_ZN25QOpenGLFunctions_3_2_Core14glCreateShaderEj(
    QOpenGLFunctions_3_2_Core *self,
    GLenum type) {
  return self->glCreateShader(type);
}

//  GLuint QOpenGLFunctions_3_2_Core::glCreateProgram()
extern "C" Q_DECL_EXPORT
GLuint ritual_ZN25QOpenGLFunctions_3_2_Core15glCreateProgramEv(
    QOpenGLFunctions_3_2_Core *self) {
  return self->glCreateProgram();
}

//  void QOpenGLFunctions_3_2_Core::glCompileShader(GLuint shader)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core15glCompileShaderEj(
    QOpenGLFunctions_3_2_Core *self,
    GLuint shader) {
  self->glCompileShader(shader);
}

//  void QOpenGLFunctions_3_2_Core::glBindAttribLocation(GLuint program,
//      GLuint index, const GLchar *name)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core20glBindAttribLocationEjjPKc(
    QOpenGLFunctions_3_2_Core *self,
    GLuint program,
    GLuint index,
    const GLchar *name) {
  self->glBindAttribLocation(program, index, name);
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

//  void QOpenGLFunctions_3_2_Core::glDrawBuffers(GLsizei n, const GLenum
//      *bufs)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core13glDrawBuffersEiPKj(
    QOpenGLFunctions_3_2_Core *self,
    GLsizei n,
    const GLenum *bufs) {
  self->glDrawBuffers(n, bufs);
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

//  void QOpenGLFunctions_3_2_Core::glUniformMatrix4x3fv(GLint location,
//      GLsizei count, GLboolean transpose, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core20glUniformMatrix4x3fvEiihPKf(
    QOpenGLFunctions_3_2_Core *self,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLfloat *value) {
  self->glUniformMatrix4x3fv(location, count, transpose, value);
}

//  void QOpenGLFunctions_3_2_Core::glUniformMatrix3x4fv(GLint location,
//      GLsizei count, GLboolean transpose, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core20glUniformMatrix3x4fvEiihPKf(
    QOpenGLFunctions_3_2_Core *self,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLfloat *value) {
  self->glUniformMatrix3x4fv(location, count, transpose, value);
}

//  void QOpenGLFunctions_3_2_Core::glUniformMatrix4x2fv(GLint location,
//      GLsizei count, GLboolean transpose, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core20glUniformMatrix4x2fvEiihPKf(
    QOpenGLFunctions_3_2_Core *self,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLfloat *value) {
  self->glUniformMatrix4x2fv(location, count, transpose, value);
}

//  void QOpenGLFunctions_3_2_Core::glUniformMatrix2x4fv(GLint location,
//      GLsizei count, GLboolean transpose, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core20glUniformMatrix2x4fvEiihPKf(
    QOpenGLFunctions_3_2_Core *self,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLfloat *value) {
  self->glUniformMatrix2x4fv(location, count, transpose, value);
}

//  void QOpenGLFunctions_3_2_Core::glUniformMatrix3x2fv(GLint location,
//      GLsizei count, GLboolean transpose, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core20glUniformMatrix3x2fvEiihPKf(
    QOpenGLFunctions_3_2_Core *self,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLfloat *value) {
  self->glUniformMatrix3x2fv(location, count, transpose, value);
}

//  void QOpenGLFunctions_3_2_Core::glUniformMatrix2x3fv(GLint location,
//      GLsizei count, GLboolean transpose, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core20glUniformMatrix2x3fvEiihPKf(
    QOpenGLFunctions_3_2_Core *self,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLfloat *value) {
  self->glUniformMatrix2x3fv(location, count, transpose, value);
}

//  GLboolean QOpenGLFunctions_3_2_Core::glIsVertexArray(GLuint array)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN25QOpenGLFunctions_3_2_Core15glIsVertexArrayEj(
    QOpenGLFunctions_3_2_Core *self,
    GLuint array) {
  return self->glIsVertexArray(array);
}

//  void QOpenGLFunctions_3_2_Core::glGenVertexArrays(GLsizei n, GLuint
//      *arrays)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core17glGenVertexArraysEiPj(
    QOpenGLFunctions_3_2_Core *self,
    GLsizei n,
    GLuint *arrays) {
  self->glGenVertexArrays(n, arrays);
}

//  void QOpenGLFunctions_3_2_Core::glDeleteVertexArrays(GLsizei n, const
//      GLuint *arrays)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core20glDeleteVertexArraysEiPKj(
    QOpenGLFunctions_3_2_Core *self,
    GLsizei n,
    const GLuint *arrays) {
  self->glDeleteVertexArrays(n, arrays);
}

//  void QOpenGLFunctions_3_2_Core::glBindVertexArray(GLuint array)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core17glBindVertexArrayEj(
    QOpenGLFunctions_3_2_Core *self,
    GLuint array) {
  self->glBindVertexArray(array);
}

//  void QOpenGLFunctions_3_2_Core::glFlushMappedBufferRange(GLenum target,
//      GLintptr offset, GLsizeiptr length)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core24glFlushMappedBufferRangeEjll(
    QOpenGLFunctions_3_2_Core *self,
    GLenum target,
    long long offset,
    long long length) {
  self->glFlushMappedBufferRange(target, offset, length);
}

//  GLvoid *QOpenGLFunctions_3_2_Core::glMapBufferRange(GLenum target,
//      GLintptr offset, GLsizeiptr length, GLbitfield access)
extern "C" Q_DECL_EXPORT
GLvoid *ritual_ZN25QOpenGLFunctions_3_2_Core16glMapBufferRangeEjllj(
    QOpenGLFunctions_3_2_Core *self,
    GLenum target,
    long long offset,
    long long length,
    GLbitfield access) {
  return self->glMapBufferRange(target, offset, length, access);
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

//  void
//      QOpenGLFunctions_3_2_Core::glGetFramebufferAttachmentParameteriv(GLen
//      um target, GLenum attachment, GLenum pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core37glGetFramebufferAttachmentParameterivEjjjPi(
    QOpenGLFunctions_3_2_Core *self,
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

//  GLenum QOpenGLFunctions_3_2_Core::glCheckFramebufferStatus(GLenum target)
extern "C" Q_DECL_EXPORT
GLenum ritual_ZN25QOpenGLFunctions_3_2_Core24glCheckFramebufferStatusEj(
    QOpenGLFunctions_3_2_Core *self,
    GLenum target) {
  return self->glCheckFramebufferStatus(target);
}

//  void QOpenGLFunctions_3_2_Core::glGenFramebuffers(GLsizei n, GLuint
//      *framebuffers)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core17glGenFramebuffersEiPj(
    QOpenGLFunctions_3_2_Core *self,
    GLsizei n,
    GLuint *framebuffers) {
  self->glGenFramebuffers(n, framebuffers);
}

//  void QOpenGLFunctions_3_2_Core::glDeleteFramebuffers(GLsizei n, const
//      GLuint *framebuffers)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core20glDeleteFramebuffersEiPKj(
    QOpenGLFunctions_3_2_Core *self,
    GLsizei n,
    const GLuint *framebuffers) {
  self->glDeleteFramebuffers(n, framebuffers);
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

//  GLboolean QOpenGLFunctions_3_2_Core::glIsFramebuffer(GLuint framebuffer)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN25QOpenGLFunctions_3_2_Core15glIsFramebufferEj(
    QOpenGLFunctions_3_2_Core *self,
    GLuint framebuffer) {
  return self->glIsFramebuffer(framebuffer);
}

//  void QOpenGLFunctions_3_2_Core::glGetRenderbufferParameteriv(GLenum
//      target, GLenum pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core28glGetRenderbufferParameterivEjjPi(
    QOpenGLFunctions_3_2_Core *self,
    GLenum target,
    GLenum pname,
    GLint *params) {
  self->glGetRenderbufferParameteriv(target, pname, params);
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

//  void QOpenGLFunctions_3_2_Core::glGenRenderbuffers(GLsizei n, GLuint
//      *renderbuffers)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core18glGenRenderbuffersEiPj(
    QOpenGLFunctions_3_2_Core *self,
    GLsizei n,
    GLuint *renderbuffers) {
  self->glGenRenderbuffers(n, renderbuffers);
}

//  void QOpenGLFunctions_3_2_Core::glDeleteRenderbuffers(GLsizei n, const
//      GLuint *renderbuffers)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core21glDeleteRenderbuffersEiPKj(
    QOpenGLFunctions_3_2_Core *self,
    GLsizei n,
    const GLuint *renderbuffers) {
  self->glDeleteRenderbuffers(n, renderbuffers);
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

//  GLboolean QOpenGLFunctions_3_2_Core::glIsRenderbuffer(GLuint
//      renderbuffer)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN25QOpenGLFunctions_3_2_Core16glIsRenderbufferEj(
    QOpenGLFunctions_3_2_Core *self,
    GLuint renderbuffer) {
  return self->glIsRenderbuffer(renderbuffer);
}

//  const GLubyte *QOpenGLFunctions_3_2_Core::glGetStringi(GLenum name,
//      GLuint index)
extern "C" Q_DECL_EXPORT
const GLubyte *ritual_ZN25QOpenGLFunctions_3_2_Core12glGetStringiEjj(
    QOpenGLFunctions_3_2_Core *self,
    GLenum name,
    GLuint index) {
  return self->glGetStringi(name, index);
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

//  void QOpenGLFunctions_3_2_Core::glClearBufferfv(GLenum buffer, GLint
//      drawbuffer, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core15glClearBufferfvEjiPKf(
    QOpenGLFunctions_3_2_Core *self,
    GLenum buffer,
    GLint drawbuffer,
    const GLfloat *value) {
  self->glClearBufferfv(buffer, drawbuffer, value);
}

//  void QOpenGLFunctions_3_2_Core::glClearBufferuiv(GLenum buffer, GLint
//      drawbuffer, const GLuint *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core16glClearBufferuivEjiPKj(
    QOpenGLFunctions_3_2_Core *self,
    GLenum buffer,
    GLint drawbuffer,
    const GLuint *value) {
  self->glClearBufferuiv(buffer, drawbuffer, value);
}

//  void QOpenGLFunctions_3_2_Core::glClearBufferiv(GLenum buffer, GLint
//      drawbuffer, const GLint *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core15glClearBufferivEjiPKi(
    QOpenGLFunctions_3_2_Core *self,
    GLenum buffer,
    GLint drawbuffer,
    const GLint *value) {
  self->glClearBufferiv(buffer, drawbuffer, value);
}

//  void QOpenGLFunctions_3_2_Core::glGetTexParameterIuiv(GLenum target,
//      GLenum pname, GLuint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core21glGetTexParameterIuivEjjPj(
    QOpenGLFunctions_3_2_Core *self,
    GLenum target,
    GLenum pname,
    GLuint *params) {
  self->glGetTexParameterIuiv(target, pname, params);
}

//  void QOpenGLFunctions_3_2_Core::glGetTexParameterIiv(GLenum target,
//      GLenum pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core20glGetTexParameterIivEjjPi(
    QOpenGLFunctions_3_2_Core *self,
    GLenum target,
    GLenum pname,
    GLint *params) {
  self->glGetTexParameterIiv(target, pname, params);
}

//  void QOpenGLFunctions_3_2_Core::glTexParameterIuiv(GLenum target, GLenum
//      pname, const GLuint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core18glTexParameterIuivEjjPKj(
    QOpenGLFunctions_3_2_Core *self,
    GLenum target,
    GLenum pname,
    const GLuint *params) {
  self->glTexParameterIuiv(target, pname, params);
}

//  void QOpenGLFunctions_3_2_Core::glTexParameterIiv(GLenum target, GLenum
//      pname, const GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core17glTexParameterIivEjjPKi(
    QOpenGLFunctions_3_2_Core *self,
    GLenum target,
    GLenum pname,
    const GLint *params) {
  self->glTexParameterIiv(target, pname, params);
}

//  void QOpenGLFunctions_3_2_Core::glUniform4uiv(GLint location, GLsizei
//      count, const GLuint *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core13glUniform4uivEiiPKj(
    QOpenGLFunctions_3_2_Core *self,
    GLint location,
    GLsizei count,
    const GLuint *value) {
  self->glUniform4uiv(location, count, value);
}

//  void QOpenGLFunctions_3_2_Core::glUniform3uiv(GLint location, GLsizei
//      count, const GLuint *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core13glUniform3uivEiiPKj(
    QOpenGLFunctions_3_2_Core *self,
    GLint location,
    GLsizei count,
    const GLuint *value) {
  self->glUniform3uiv(location, count, value);
}

//  void QOpenGLFunctions_3_2_Core::glUniform2uiv(GLint location, GLsizei
//      count, const GLuint *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core13glUniform2uivEiiPKj(
    QOpenGLFunctions_3_2_Core *self,
    GLint location,
    GLsizei count,
    const GLuint *value) {
  self->glUniform2uiv(location, count, value);
}

//  void QOpenGLFunctions_3_2_Core::glUniform1uiv(GLint location, GLsizei
//      count, const GLuint *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core13glUniform1uivEiiPKj(
    QOpenGLFunctions_3_2_Core *self,
    GLint location,
    GLsizei count,
    const GLuint *value) {
  self->glUniform1uiv(location, count, value);
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

//  GLint QOpenGLFunctions_3_2_Core::glGetFragDataLocation(GLuint program,
//      const GLchar *name)
extern "C" Q_DECL_EXPORT
GLint ritual_ZN25QOpenGLFunctions_3_2_Core21glGetFragDataLocationEjPKc(
    QOpenGLFunctions_3_2_Core *self,
    GLuint program,
    const GLchar *name) {
  return self->glGetFragDataLocation(program, name);
}

//  void QOpenGLFunctions_3_2_Core::glBindFragDataLocation(GLuint program,
//      GLuint color, const GLchar *name)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core22glBindFragDataLocationEjjPKc(
    QOpenGLFunctions_3_2_Core *self,
    GLuint program,
    GLuint color,
    const GLchar *name) {
  self->glBindFragDataLocation(program, color, name);
}

//  void QOpenGLFunctions_3_2_Core::glGetUniformuiv(GLuint program, GLint
//      location, GLuint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core15glGetUniformuivEjiPj(
    QOpenGLFunctions_3_2_Core *self,
    GLuint program,
    GLint location,
    GLuint *params) {
  self->glGetUniformuiv(program, location, params);
}

//  void QOpenGLFunctions_3_2_Core::glGetVertexAttribIuiv(GLuint index,
//      GLenum pname, GLuint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core21glGetVertexAttribIuivEjjPj(
    QOpenGLFunctions_3_2_Core *self,
    GLuint index,
    GLenum pname,
    GLuint *params) {
  self->glGetVertexAttribIuiv(index, pname, params);
}

//  void QOpenGLFunctions_3_2_Core::glGetVertexAttribIiv(GLuint index, GLenum
//      pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core20glGetVertexAttribIivEjjPi(
    QOpenGLFunctions_3_2_Core *self,
    GLuint index,
    GLenum pname,
    GLint *params) {
  self->glGetVertexAttribIiv(index, pname, params);
}

//  void QOpenGLFunctions_3_2_Core::glVertexAttribIPointer(GLuint index,
//      GLint size, GLenum type, GLsizei stride, const GLvoid *pointer)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core22glVertexAttribIPointerEjijiPKv(
    QOpenGLFunctions_3_2_Core *self,
    GLuint index,
    GLint size,
    GLenum type,
    GLsizei stride,
    const GLvoid *pointer) {
  self->glVertexAttribIPointer(index, size, type, stride, pointer);
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

//  void QOpenGLFunctions_3_2_Core::glGetTransformFeedbackVarying(GLuint
//      program, GLuint index, GLsizei bufSize, GLsizei *length, GLsizei
//      *size, GLenum *type, GLchar *name)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core29glGetTransformFeedbackVaryingEjjiPiS0_PjPc(
    QOpenGLFunctions_3_2_Core *self,
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

//  void QOpenGLFunctions_3_2_Core::glTransformFeedbackVaryings(GLuint
//      program, GLsizei count, const GLchar *const *varyings, GLenum
//      bufferMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core27glTransformFeedbackVaryingsEjiPKPKcj(
    QOpenGLFunctions_3_2_Core *self,
    GLuint program,
    GLsizei count,
    const GLchar *const *varyings,
    GLenum bufferMode) {
  self->glTransformFeedbackVaryings(program, count, varyings, bufferMode);
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

//  void QOpenGLFunctions_3_2_Core::glBindBufferRange(GLenum target, GLuint
//      index, GLuint buffer, GLintptr offset, GLsizeiptr size)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core17glBindBufferRangeEjjjll(
    QOpenGLFunctions_3_2_Core *self,
    GLenum target,
    GLuint index,
    GLuint buffer,
    long long offset,
    long long size) {
  self->glBindBufferRange(target, index, buffer, offset, size);
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

//  GLboolean QOpenGLFunctions_3_2_Core::glIsEnabledi(GLenum target, GLuint
//      index)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN25QOpenGLFunctions_3_2_Core12glIsEnablediEjj(
    QOpenGLFunctions_3_2_Core *self,
    GLenum target,
    GLuint index) {
  return self->glIsEnabledi(target, index);
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

//  void QOpenGLFunctions_3_2_Core::glGetIntegeri_v(GLenum target, GLuint
//      index, GLint *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core15glGetIntegeri_vEjjPi(
    QOpenGLFunctions_3_2_Core *self,
    GLenum target,
    GLuint index,
    GLint *data) {
  self->glGetIntegeri_v(target, index, data);
}

//  void QOpenGLFunctions_3_2_Core::glGetBooleani_v(GLenum target, GLuint
//      index, GLboolean *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core15glGetBooleani_vEjjPh(
    QOpenGLFunctions_3_2_Core *self,
    GLenum target,
    GLuint index,
    GLboolean *data) {
  self->glGetBooleani_v(target, index, data);
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

//  void QOpenGLFunctions_3_2_Core::glCopyBufferSubData(GLenum readTarget,
//      GLenum writeTarget, GLintptr readOffset, GLintptr writeOffset,
//      GLsizeiptr size)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core19glCopyBufferSubDataEjjlll(
    QOpenGLFunctions_3_2_Core *self,
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

//  void QOpenGLFunctions_3_2_Core::glGetActiveUniformBlockName(GLuint
//      program, GLuint uniformBlockIndex, GLsizei bufSize, GLsizei *length,
//      GLchar *uniformBlockName)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core27glGetActiveUniformBlockNameEjjiPiPc(
    QOpenGLFunctions_3_2_Core *self,
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

//  void QOpenGLFunctions_3_2_Core::glGetActiveUniformBlockiv(GLuint program,
//      GLuint uniformBlockIndex, GLenum pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core25glGetActiveUniformBlockivEjjjPi(
    QOpenGLFunctions_3_2_Core *self,
    GLuint program,
    GLuint uniformBlockIndex,
    GLenum pname,
    GLint *params) {
  self->glGetActiveUniformBlockiv(program, uniformBlockIndex, pname, params);
}

//  GLuint QOpenGLFunctions_3_2_Core::glGetUniformBlockIndex(GLuint program,
//      const GLchar *uniformBlockName)
extern "C" Q_DECL_EXPORT
GLuint ritual_ZN25QOpenGLFunctions_3_2_Core22glGetUniformBlockIndexEjPKc(
    QOpenGLFunctions_3_2_Core *self,
    GLuint program,
    const GLchar *uniformBlockName) {
  return self->glGetUniformBlockIndex(program, uniformBlockName);
}

//  void QOpenGLFunctions_3_2_Core::glGetActiveUniformName(GLuint program,
//      GLuint uniformIndex, GLsizei bufSize, GLsizei *length, GLchar
//      *uniformName)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core22glGetActiveUniformNameEjjiPiPc(
    QOpenGLFunctions_3_2_Core *self,
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

//  void QOpenGLFunctions_3_2_Core::glGetActiveUniformsiv(GLuint program,
//      GLsizei uniformCount, const GLuint *uniformIndices, GLenum pname,
//      GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core21glGetActiveUniformsivEjiPKjjPi(
    QOpenGLFunctions_3_2_Core *self,
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

//  void QOpenGLFunctions_3_2_Core::glGetUniformIndices(GLuint program,
//      GLsizei uniformCount, const GLchar *const *uniformNames, GLuint
//      *uniformIndices)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core19glGetUniformIndicesEjiPKPKcPj(
    QOpenGLFunctions_3_2_Core *self,
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

//  void QOpenGLFunctions_3_2_Core::glDrawElementsInstanced(GLenum mode,
//      GLsizei count, GLenum type, const GLvoid *indices, GLsizei
//      instancecount)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core23glDrawElementsInstancedEjijPKvi(
    QOpenGLFunctions_3_2_Core *self,
    GLenum mode,
    GLsizei count,
    GLenum type,
    const GLvoid *indices,
    GLsizei instancecount) {
  self->glDrawElementsInstanced(mode, count, type, indices, instancecount);
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

//  void QOpenGLFunctions_3_2_Core::glGetMultisamplefv(GLenum pname, GLuint
//      index, GLfloat *val)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core18glGetMultisamplefvEjjPf(
    QOpenGLFunctions_3_2_Core *self,
    GLenum pname,
    GLuint index,
    GLfloat *val) {
  self->glGetMultisamplefv(pname, index, val);
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

//  void QOpenGLFunctions_3_2_Core::glGetSynciv(GLsync sync, GLenum pname,
//      GLsizei bufSize, GLsizei *length, GLint *values)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core11glGetSyncivEP8__GLsyncjiPiS2_(
    QOpenGLFunctions_3_2_Core *self,
    GLsync sync,
    GLenum pname,
    GLsizei bufSize,
    GLsizei *length,
    GLint *values) {
  self->glGetSynciv(sync, pname, bufSize, length, values);
}

//  void QOpenGLFunctions_3_2_Core::glGetInteger64v(GLenum pname, GLint64
//      *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core15glGetInteger64vEjPl(
    QOpenGLFunctions_3_2_Core *self,
    GLenum pname,
    GLint64 *params) {
  self->glGetInteger64v(pname, params);
}

//  void QOpenGLFunctions_3_2_Core::glWaitSync(GLsync sync, GLbitfield flags,
//      GLuint64 timeout)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core10glWaitSyncEP8__GLsyncjm(
    QOpenGLFunctions_3_2_Core *self,
    GLsync sync,
    GLbitfield flags,
    unsigned long long timeout) {
  self->glWaitSync(sync, flags, timeout);
}

//  GLenum QOpenGLFunctions_3_2_Core::glClientWaitSync(GLsync sync,
//      GLbitfield flags, GLuint64 timeout)
extern "C" Q_DECL_EXPORT
GLenum ritual_ZN25QOpenGLFunctions_3_2_Core16glClientWaitSyncEP8__GLsyncjm(
    QOpenGLFunctions_3_2_Core *self,
    GLsync sync,
    GLbitfield flags,
    unsigned long long timeout) {
  return self->glClientWaitSync(sync, flags, timeout);
}

//  void QOpenGLFunctions_3_2_Core::glDeleteSync(GLsync sync)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core12glDeleteSyncEP8__GLsync(
    QOpenGLFunctions_3_2_Core *self,
    GLsync sync) {
  self->glDeleteSync(sync);
}

//  GLboolean QOpenGLFunctions_3_2_Core::glIsSync(GLsync sync)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN25QOpenGLFunctions_3_2_Core8glIsSyncEP8__GLsync(
    QOpenGLFunctions_3_2_Core *self,
    GLsync sync) {
  return self->glIsSync(sync);
}

//  GLsync QOpenGLFunctions_3_2_Core::glFenceSync(GLenum condition,
//      GLbitfield flags)
extern "C" Q_DECL_EXPORT
GLsync ritual_ZN25QOpenGLFunctions_3_2_Core11glFenceSyncEjj(
    QOpenGLFunctions_3_2_Core *self,
    GLenum condition,
    GLbitfield flags) {
  return self->glFenceSync(condition, flags);
}

//  void QOpenGLFunctions_3_2_Core::glProvokingVertex(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core17glProvokingVertexEj(
    QOpenGLFunctions_3_2_Core *self,
    GLenum mode) {
  self->glProvokingVertex(mode);
}

//  void QOpenGLFunctions_3_2_Core::glMultiDrawElementsBaseVertex(GLenum
//      mode, const GLsizei *count, GLenum type, const GLvoid *const
//      *indices, GLsizei drawcount, const GLint *basevertex)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core29glMultiDrawElementsBaseVertexEjPKijPKPKviS1_(
    QOpenGLFunctions_3_2_Core *self,
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

//  void QOpenGLFunctions_3_2_Core::glDrawElementsInstancedBaseVertex(GLenum
//      mode, GLsizei count, GLenum type, const GLvoid *indices, GLsizei
//      instancecount, GLint basevertex)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core33glDrawElementsInstancedBaseVertexEjijPKvii(
    QOpenGLFunctions_3_2_Core *self,
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

//  void QOpenGLFunctions_3_2_Core::glDrawRangeElementsBaseVertex(GLenum
//      mode, GLuint start, GLuint end, GLsizei count, GLenum type, const
//      GLvoid *indices, GLint basevertex)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core29glDrawRangeElementsBaseVertexEjjjijPKvi(
    QOpenGLFunctions_3_2_Core *self,
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

//  void QOpenGLFunctions_3_2_Core::glDrawElementsBaseVertex(GLenum mode,
//      GLsizei count, GLenum type, const GLvoid *indices, GLint basevertex)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core24glDrawElementsBaseVertexEjijPKvi(
    QOpenGLFunctions_3_2_Core *self,
    GLenum mode,
    GLsizei count,
    GLenum type,
    const GLvoid *indices,
    GLint basevertex) {
  self->glDrawElementsBaseVertex(mode, count, type, indices, basevertex);
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

//  void QOpenGLFunctions_3_2_Core::glGetBufferParameteri64v(GLenum target,
//      GLenum pname, GLint64 *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core24glGetBufferParameteri64vEjjPl(
    QOpenGLFunctions_3_2_Core *self,
    GLenum target,
    GLenum pname,
    GLint64 *params) {
  self->glGetBufferParameteri64v(target, pname, params);
}

//  void QOpenGLFunctions_3_2_Core::glGetInteger64i_v(GLenum target, GLuint
//      index, GLint64 *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_3_2_Core17glGetInteger64i_vEjjPl(
    QOpenGLFunctions_3_2_Core *self,
    GLenum target,
    GLuint index,
    GLint64 *data) {
  self->glGetInteger64i_v(target, index, data);
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
#endif  // !QT_CONFIG(opengles2)
