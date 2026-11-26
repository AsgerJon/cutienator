//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/qopenglfunctions_4_2_core.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/qtguiglobal.h>
#include <QtOpenGL/qtopenglglobal.h>
#if !QT_CONFIG(opengles2)
#if !defined(QT_NO_OPENGL) && !QT_CONFIG(opengles2)
#include <QtOpenGL/QtOpenGL>
#include <QtOpenGL/qopenglfunctions_4_2_core.h>
#include <QtOpenGL/qopenglversionprofile.h>
#include <cstring>

//  A QOpenGLFunctions_4_2_Core that Python can take functions over in. Every QOpenGLFunctions_4_2_Core
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL) && !QT_CONFIG(opengles2)
typedef bool (*CuteQOpenGLFunctions_4_2_CoreCall0)(const void *, int *);
#endif  // !defined(QT_NO_OPENGL) && !QT_CONFIG(opengles2)
#endif  // !defined(QT_NO_OPENGL)
class CuteQOpenGLFunctions_4_2_Core : public QOpenGLFunctions_4_2_Core {
public:
  using QOpenGLFunctions_4_2_Core::QOpenGLFunctions_4_2_Core;
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
  //  bool QOpenGLFunctions_4_2_Core::initializeOpenGLFunctions()
  bool initializeOpenGLFunctions() override {
    if (taken[0]) {
      int handled = 0;
      CuteQOpenGLFunctions_4_2_CoreCall0 call = reinterpret_cast<CuteQOpenGLFunctions_4_2_CoreCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QOpenGLFunctions_4_2_Core::initializeOpenGLFunctions();
  }
#endif  // !defined(QT_NO_OPENGL) && !QT_CONFIG(opengles2)
#endif  // !defined(QT_NO_OPENGL)
};

//  QOpenGLFunctions_4_2_Core::QOpenGLFunctions_4_2_Core()
extern "C" Q_DECL_EXPORT
QOpenGLFunctions_4_2_Core *ritual_ZN25QOpenGLFunctions_4_2_CoreC1Ev() {
  return new CuteQOpenGLFunctions_4_2_Core();
}

//  QOpenGLFunctions_4_2_Core::~QOpenGLFunctions_4_2_Core()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_CoreD1Ev(
    QOpenGLFunctions_4_2_Core *self) {
  delete self;
}

//  bool QOpenGLFunctions_4_2_Core::initializeOpenGLFunctions()
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QOpenGLFunctions_4_2_Core25initializeOpenGLFunctionsEv(
    QOpenGLFunctions_4_2_Core *self) {
  return self->initializeOpenGLFunctions();
}

//  void QOpenGLFunctions_4_2_Core::glViewport(GLint x, GLint y, GLsizei
//      width, GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core10glViewportEiiii(
    QOpenGLFunctions_4_2_Core *self,
    GLint x,
    GLint y,
    GLsizei width,
    GLsizei height) {
  self->glViewport(x, y, width, height);
}

//  void QOpenGLFunctions_4_2_Core::glDepthRange(GLdouble nearVal, GLdouble
//      farVal)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core12glDepthRangeEdd(
    QOpenGLFunctions_4_2_Core *self,
    GLdouble nearVal,
    GLdouble farVal) {
  self->glDepthRange(nearVal, farVal);
}

//  GLboolean QOpenGLFunctions_4_2_Core::glIsEnabled(GLenum cap)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN25QOpenGLFunctions_4_2_Core11glIsEnabledEj(
    QOpenGLFunctions_4_2_Core *self,
    GLenum cap) {
  return self->glIsEnabled(cap);
}

//  void QOpenGLFunctions_4_2_Core::glGetTexLevelParameteriv(GLenum target,
//      GLint level, GLenum pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core24glGetTexLevelParameterivEjijPi(
    QOpenGLFunctions_4_2_Core *self,
    GLenum target,
    GLint level,
    GLenum pname,
    GLint *params) {
  self->glGetTexLevelParameteriv(target, level, pname, params);
}

//  void QOpenGLFunctions_4_2_Core::glGetTexLevelParameterfv(GLenum target,
//      GLint level, GLenum pname, GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core24glGetTexLevelParameterfvEjijPf(
    QOpenGLFunctions_4_2_Core *self,
    GLenum target,
    GLint level,
    GLenum pname,
    GLfloat *params) {
  self->glGetTexLevelParameterfv(target, level, pname, params);
}

//  void QOpenGLFunctions_4_2_Core::glGetTexParameteriv(GLenum target, GLenum
//      pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core19glGetTexParameterivEjjPi(
    QOpenGLFunctions_4_2_Core *self,
    GLenum target,
    GLenum pname,
    GLint *params) {
  self->glGetTexParameteriv(target, pname, params);
}

//  void QOpenGLFunctions_4_2_Core::glGetTexParameterfv(GLenum target, GLenum
//      pname, GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core19glGetTexParameterfvEjjPf(
    QOpenGLFunctions_4_2_Core *self,
    GLenum target,
    GLenum pname,
    GLfloat *params) {
  self->glGetTexParameterfv(target, pname, params);
}

//  void QOpenGLFunctions_4_2_Core::glGetTexImage(GLenum target, GLint level,
//      GLenum format, GLenum type, GLvoid *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core13glGetTexImageEjijjPv(
    QOpenGLFunctions_4_2_Core *self,
    GLenum target,
    GLint level,
    GLenum format,
    GLenum type,
    GLvoid *pixels) {
  self->glGetTexImage(target, level, format, type, pixels);
}

//  const GLubyte *QOpenGLFunctions_4_2_Core::glGetString(GLenum name)
extern "C" Q_DECL_EXPORT
const GLubyte *ritual_ZN25QOpenGLFunctions_4_2_Core11glGetStringEj(
    QOpenGLFunctions_4_2_Core *self,
    GLenum name) {
  return self->glGetString(name);
}

//  void QOpenGLFunctions_4_2_Core::glGetIntegerv(GLenum pname, GLint
//      *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core13glGetIntegervEjPi(
    QOpenGLFunctions_4_2_Core *self,
    GLenum pname,
    GLint *params) {
  self->glGetIntegerv(pname, params);
}

//  void QOpenGLFunctions_4_2_Core::glGetFloatv(GLenum pname, GLfloat
//      *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core11glGetFloatvEjPf(
    QOpenGLFunctions_4_2_Core *self,
    GLenum pname,
    GLfloat *params) {
  self->glGetFloatv(pname, params);
}

//  GLenum QOpenGLFunctions_4_2_Core::glGetError()
extern "C" Q_DECL_EXPORT
GLenum ritual_ZN25QOpenGLFunctions_4_2_Core10glGetErrorEv(
    QOpenGLFunctions_4_2_Core *self) {
  return self->glGetError();
}

//  void QOpenGLFunctions_4_2_Core::glGetDoublev(GLenum pname, GLdouble
//      *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core12glGetDoublevEjPd(
    QOpenGLFunctions_4_2_Core *self,
    GLenum pname,
    GLdouble *params) {
  self->glGetDoublev(pname, params);
}

//  void QOpenGLFunctions_4_2_Core::glGetBooleanv(GLenum pname, GLboolean
//      *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core13glGetBooleanvEjPh(
    QOpenGLFunctions_4_2_Core *self,
    GLenum pname,
    GLboolean *params) {
  self->glGetBooleanv(pname, params);
}

//  void QOpenGLFunctions_4_2_Core::glReadPixels(GLint x, GLint y, GLsizei
//      width, GLsizei height, GLenum format, GLenum type, GLvoid *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core12glReadPixelsEiiiijjPv(
    QOpenGLFunctions_4_2_Core *self,
    GLint x,
    GLint y,
    GLsizei width,
    GLsizei height,
    GLenum format,
    GLenum type,
    GLvoid *pixels) {
  self->glReadPixels(x, y, width, height, format, type, pixels);
}

//  void QOpenGLFunctions_4_2_Core::glReadBuffer(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core12glReadBufferEj(
    QOpenGLFunctions_4_2_Core *self,
    GLenum mode) {
  self->glReadBuffer(mode);
}

//  void QOpenGLFunctions_4_2_Core::glPixelStorei(GLenum pname, GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core13glPixelStoreiEji(
    QOpenGLFunctions_4_2_Core *self,
    GLenum pname,
    GLint param) {
  self->glPixelStorei(pname, param);
}

//  void QOpenGLFunctions_4_2_Core::glPixelStoref(GLenum pname, GLfloat
//      param)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core13glPixelStorefEjf(
    QOpenGLFunctions_4_2_Core *self,
    GLenum pname,
    GLfloat param) {
  self->glPixelStoref(pname, param);
}

//  void QOpenGLFunctions_4_2_Core::glDepthFunc(GLenum func)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core11glDepthFuncEj(
    QOpenGLFunctions_4_2_Core *self,
    GLenum func) {
  self->glDepthFunc(func);
}

//  void QOpenGLFunctions_4_2_Core::glStencilOp(GLenum fail, GLenum zfail,
//      GLenum zpass)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core11glStencilOpEjjj(
    QOpenGLFunctions_4_2_Core *self,
    GLenum fail,
    GLenum zfail,
    GLenum zpass) {
  self->glStencilOp(fail, zfail, zpass);
}

//  void QOpenGLFunctions_4_2_Core::glStencilFunc(GLenum func, GLint ref,
//      GLuint mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core13glStencilFuncEjij(
    QOpenGLFunctions_4_2_Core *self,
    GLenum func,
    GLint ref,
    GLuint mask) {
  self->glStencilFunc(func, ref, mask);
}

//  void QOpenGLFunctions_4_2_Core::glLogicOp(GLenum opcode)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core9glLogicOpEj(
    QOpenGLFunctions_4_2_Core *self,
    GLenum opcode) {
  self->glLogicOp(opcode);
}

//  void QOpenGLFunctions_4_2_Core::glBlendFunc(GLenum sfactor, GLenum
//      dfactor)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core11glBlendFuncEjj(
    QOpenGLFunctions_4_2_Core *self,
    GLenum sfactor,
    GLenum dfactor) {
  self->glBlendFunc(sfactor, dfactor);
}

//  void QOpenGLFunctions_4_2_Core::glFlush()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core7glFlushEv(
    QOpenGLFunctions_4_2_Core *self) {
  self->glFlush();
}

//  void QOpenGLFunctions_4_2_Core::glFinish()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core8glFinishEv(
    QOpenGLFunctions_4_2_Core *self) {
  self->glFinish();
}

//  void QOpenGLFunctions_4_2_Core::glEnable(GLenum cap)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core8glEnableEj(
    QOpenGLFunctions_4_2_Core *self,
    GLenum cap) {
  self->glEnable(cap);
}

//  void QOpenGLFunctions_4_2_Core::glDisable(GLenum cap)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core9glDisableEj(
    QOpenGLFunctions_4_2_Core *self,
    GLenum cap) {
  self->glDisable(cap);
}

//  void QOpenGLFunctions_4_2_Core::glDepthMask(GLboolean flag)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core11glDepthMaskEh(
    QOpenGLFunctions_4_2_Core *self,
    GLboolean flag) {
  self->glDepthMask(flag);
}

//  void QOpenGLFunctions_4_2_Core::glColorMask(GLboolean red, GLboolean
//      green, GLboolean blue, GLboolean alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core11glColorMaskEhhhh(
    QOpenGLFunctions_4_2_Core *self,
    GLboolean red,
    GLboolean green,
    GLboolean blue,
    GLboolean alpha) {
  self->glColorMask(red, green, blue, alpha);
}

//  void QOpenGLFunctions_4_2_Core::glStencilMask(GLuint mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core13glStencilMaskEj(
    QOpenGLFunctions_4_2_Core *self,
    GLuint mask) {
  self->glStencilMask(mask);
}

//  void QOpenGLFunctions_4_2_Core::glClearDepth(GLdouble depth)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core12glClearDepthEd(
    QOpenGLFunctions_4_2_Core *self,
    GLdouble depth) {
  self->glClearDepth(depth);
}

//  void QOpenGLFunctions_4_2_Core::glClearStencil(GLint s)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core14glClearStencilEi(
    QOpenGLFunctions_4_2_Core *self,
    GLint s) {
  self->glClearStencil(s);
}

//  void QOpenGLFunctions_4_2_Core::glClearColor(GLfloat red, GLfloat green,
//      GLfloat blue, GLfloat alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core12glClearColorEffff(
    QOpenGLFunctions_4_2_Core *self,
    GLfloat red,
    GLfloat green,
    GLfloat blue,
    GLfloat alpha) {
  self->glClearColor(red, green, blue, alpha);
}

//  void QOpenGLFunctions_4_2_Core::glClear(GLbitfield mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core7glClearEj(
    QOpenGLFunctions_4_2_Core *self,
    GLbitfield mask) {
  self->glClear(mask);
}

//  void QOpenGLFunctions_4_2_Core::glDrawBuffer(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core12glDrawBufferEj(
    QOpenGLFunctions_4_2_Core *self,
    GLenum mode) {
  self->glDrawBuffer(mode);
}

//  void QOpenGLFunctions_4_2_Core::glTexImage2D(GLenum target, GLint level,
//      GLint internalformat, GLsizei width, GLsizei height, GLint border,
//      GLenum format, GLenum type, const GLvoid *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core12glTexImage2DEjiiiiijjPKv(
    QOpenGLFunctions_4_2_Core *self,
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

//  void QOpenGLFunctions_4_2_Core::glTexImage1D(GLenum target, GLint level,
//      GLint internalformat, GLsizei width, GLint border, GLenum format,
//      GLenum type, const GLvoid *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core12glTexImage1DEjiiiijjPKv(
    QOpenGLFunctions_4_2_Core *self,
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

//  void QOpenGLFunctions_4_2_Core::glTexParameteriv(GLenum target, GLenum
//      pname, const GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core16glTexParameterivEjjPKi(
    QOpenGLFunctions_4_2_Core *self,
    GLenum target,
    GLenum pname,
    const GLint *params) {
  self->glTexParameteriv(target, pname, params);
}

//  void QOpenGLFunctions_4_2_Core::glTexParameteri(GLenum target, GLenum
//      pname, GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core15glTexParameteriEjji(
    QOpenGLFunctions_4_2_Core *self,
    GLenum target,
    GLenum pname,
    GLint param) {
  self->glTexParameteri(target, pname, param);
}

//  void QOpenGLFunctions_4_2_Core::glTexParameterfv(GLenum target, GLenum
//      pname, const GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core16glTexParameterfvEjjPKf(
    QOpenGLFunctions_4_2_Core *self,
    GLenum target,
    GLenum pname,
    const GLfloat *params) {
  self->glTexParameterfv(target, pname, params);
}

//  void QOpenGLFunctions_4_2_Core::glTexParameterf(GLenum target, GLenum
//      pname, GLfloat param)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core15glTexParameterfEjjf(
    QOpenGLFunctions_4_2_Core *self,
    GLenum target,
    GLenum pname,
    GLfloat param) {
  self->glTexParameterf(target, pname, param);
}

//  void QOpenGLFunctions_4_2_Core::glScissor(GLint x, GLint y, GLsizei
//      width, GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core9glScissorEiiii(
    QOpenGLFunctions_4_2_Core *self,
    GLint x,
    GLint y,
    GLsizei width,
    GLsizei height) {
  self->glScissor(x, y, width, height);
}

//  void QOpenGLFunctions_4_2_Core::glPolygonMode(GLenum face, GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core13glPolygonModeEjj(
    QOpenGLFunctions_4_2_Core *self,
    GLenum face,
    GLenum mode) {
  self->glPolygonMode(face, mode);
}

//  void QOpenGLFunctions_4_2_Core::glPointSize(GLfloat size)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core11glPointSizeEf(
    QOpenGLFunctions_4_2_Core *self,
    GLfloat size) {
  self->glPointSize(size);
}

//  void QOpenGLFunctions_4_2_Core::glLineWidth(GLfloat width)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core11glLineWidthEf(
    QOpenGLFunctions_4_2_Core *self,
    GLfloat width) {
  self->glLineWidth(width);
}

//  void QOpenGLFunctions_4_2_Core::glHint(GLenum target, GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core6glHintEjj(
    QOpenGLFunctions_4_2_Core *self,
    GLenum target,
    GLenum mode) {
  self->glHint(target, mode);
}

//  void QOpenGLFunctions_4_2_Core::glFrontFace(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core11glFrontFaceEj(
    QOpenGLFunctions_4_2_Core *self,
    GLenum mode) {
  self->glFrontFace(mode);
}

//  void QOpenGLFunctions_4_2_Core::glCullFace(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core10glCullFaceEj(
    QOpenGLFunctions_4_2_Core *self,
    GLenum mode) {
  self->glCullFace(mode);
}

//  GLboolean QOpenGLFunctions_4_2_Core::glIsTexture(GLuint texture)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN25QOpenGLFunctions_4_2_Core11glIsTextureEj(
    QOpenGLFunctions_4_2_Core *self,
    GLuint texture) {
  return self->glIsTexture(texture);
}

//  void QOpenGLFunctions_4_2_Core::glGenTextures(GLsizei n, GLuint
//      *textures)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core13glGenTexturesEiPj(
    QOpenGLFunctions_4_2_Core *self,
    GLsizei n,
    GLuint *textures) {
  self->glGenTextures(n, textures);
}

//  void QOpenGLFunctions_4_2_Core::glDeleteTextures(GLsizei n, const GLuint
//      *textures)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core16glDeleteTexturesEiPKj(
    QOpenGLFunctions_4_2_Core *self,
    GLsizei n,
    const GLuint *textures) {
  self->glDeleteTextures(n, textures);
}

//  void QOpenGLFunctions_4_2_Core::glBindTexture(GLenum target, GLuint
//      texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core13glBindTextureEjj(
    QOpenGLFunctions_4_2_Core *self,
    GLenum target,
    GLuint texture) {
  self->glBindTexture(target, texture);
}

//  void QOpenGLFunctions_4_2_Core::glTexSubImage2D(GLenum target, GLint
//      level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height,
//      GLenum format, GLenum type, const GLvoid *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core15glTexSubImage2DEjiiiiijjPKv(
    QOpenGLFunctions_4_2_Core *self,
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

//  void QOpenGLFunctions_4_2_Core::glTexSubImage1D(GLenum target, GLint
//      level, GLint xoffset, GLsizei width, GLenum format, GLenum type,
//      const GLvoid *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core15glTexSubImage1DEjiiijjPKv(
    QOpenGLFunctions_4_2_Core *self,
    GLenum target,
    GLint level,
    GLint xoffset,
    GLsizei width,
    GLenum format,
    GLenum type,
    const GLvoid *pixels) {
  self->glTexSubImage1D(target, level, xoffset, width, format, type, pixels);
}

//  void QOpenGLFunctions_4_2_Core::glCopyTexSubImage2D(GLenum target, GLint
//      level, GLint xoffset, GLint yoffset, GLint x, GLint y, GLsizei width,
//      GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core19glCopyTexSubImage2DEjiiiiiii(
    QOpenGLFunctions_4_2_Core *self,
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

//  void QOpenGLFunctions_4_2_Core::glCopyTexSubImage1D(GLenum target, GLint
//      level, GLint xoffset, GLint x, GLint y, GLsizei width)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core19glCopyTexSubImage1DEjiiiii(
    QOpenGLFunctions_4_2_Core *self,
    GLenum target,
    GLint level,
    GLint xoffset,
    GLint x,
    GLint y,
    GLsizei width) {
  self->glCopyTexSubImage1D(target, level, xoffset, x, y, width);
}

//  void QOpenGLFunctions_4_2_Core::glCopyTexImage2D(GLenum target, GLint
//      level, GLenum internalformat, GLint x, GLint y, GLsizei width,
//      GLsizei height, GLint border)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core16glCopyTexImage2DEjijiiiii(
    QOpenGLFunctions_4_2_Core *self,
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

//  void QOpenGLFunctions_4_2_Core::glCopyTexImage1D(GLenum target, GLint
//      level, GLenum internalformat, GLint x, GLint y, GLsizei width, GLint
//      border)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core16glCopyTexImage1DEjijiiii(
    QOpenGLFunctions_4_2_Core *self,
    GLenum target,
    GLint level,
    GLenum internalformat,
    GLint x,
    GLint y,
    GLsizei width,
    GLint border) {
  self->glCopyTexImage1D(target, level, internalformat, x, y, width, border);
}

//  void QOpenGLFunctions_4_2_Core::glPolygonOffset(GLfloat factor, GLfloat
//      units)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core15glPolygonOffsetEff(
    QOpenGLFunctions_4_2_Core *self,
    GLfloat factor,
    GLfloat units) {
  self->glPolygonOffset(factor, units);
}

//  void QOpenGLFunctions_4_2_Core::glDrawElements(GLenum mode, GLsizei
//      count, GLenum type, const GLvoid *indices)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core14glDrawElementsEjijPKv(
    QOpenGLFunctions_4_2_Core *self,
    GLenum mode,
    GLsizei count,
    GLenum type,
    const GLvoid *indices) {
  self->glDrawElements(mode, count, type, indices);
}

//  void QOpenGLFunctions_4_2_Core::glDrawArrays(GLenum mode, GLint first,
//      GLsizei count)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core12glDrawArraysEjii(
    QOpenGLFunctions_4_2_Core *self,
    GLenum mode,
    GLint first,
    GLsizei count) {
  self->glDrawArrays(mode, first, count);
}

//  void QOpenGLFunctions_4_2_Core::glCopyTexSubImage3D(GLenum target, GLint
//      level, GLint xoffset, GLint yoffset, GLint zoffset, GLint x, GLint y,
//      GLsizei width, GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core19glCopyTexSubImage3DEjiiiiiiii(
    QOpenGLFunctions_4_2_Core *self,
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

//  void QOpenGLFunctions_4_2_Core::glTexSubImage3D(GLenum target, GLint
//      level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width,
//      GLsizei height, GLsizei depth, GLenum format, GLenum type, const
//      GLvoid *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core15glTexSubImage3DEjiiiiiiijjPKv(
    QOpenGLFunctions_4_2_Core *self,
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

//  void QOpenGLFunctions_4_2_Core::glTexImage3D(GLenum target, GLint level,
//      GLint internalformat, GLsizei width, GLsizei height, GLsizei depth,
//      GLint border, GLenum format, GLenum type, const GLvoid *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core12glTexImage3DEjiiiiiijjPKv(
    QOpenGLFunctions_4_2_Core *self,
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

//  void QOpenGLFunctions_4_2_Core::glDrawRangeElements(GLenum mode, GLuint
//      start, GLuint end, GLsizei count, GLenum type, const GLvoid *indices)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core19glDrawRangeElementsEjjjijPKv(
    QOpenGLFunctions_4_2_Core *self,
    GLenum mode,
    GLuint start,
    GLuint end,
    GLsizei count,
    GLenum type,
    const GLvoid *indices) {
  self->glDrawRangeElements(mode, start, end, count, type, indices);
}

//  void QOpenGLFunctions_4_2_Core::glBlendEquation(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core15glBlendEquationEj(
    QOpenGLFunctions_4_2_Core *self,
    GLenum mode) {
  self->glBlendEquation(mode);
}

//  void QOpenGLFunctions_4_2_Core::glBlendColor(GLfloat red, GLfloat green,
//      GLfloat blue, GLfloat alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core12glBlendColorEffff(
    QOpenGLFunctions_4_2_Core *self,
    GLfloat red,
    GLfloat green,
    GLfloat blue,
    GLfloat alpha) {
  self->glBlendColor(red, green, blue, alpha);
}

//  void QOpenGLFunctions_4_2_Core::glGetCompressedTexImage(GLenum target,
//      GLint level, GLvoid *img)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core23glGetCompressedTexImageEjiPv(
    QOpenGLFunctions_4_2_Core *self,
    GLenum target,
    GLint level,
    GLvoid *img) {
  self->glGetCompressedTexImage(target, level, img);
}

//  void QOpenGLFunctions_4_2_Core::glCompressedTexSubImage1D(GLenum target,
//      GLint level, GLint xoffset, GLsizei width, GLenum format, GLsizei
//      imageSize, const GLvoid *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core25glCompressedTexSubImage1DEjiiijiPKv(
    QOpenGLFunctions_4_2_Core *self,
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

//  void QOpenGLFunctions_4_2_Core::glCompressedTexSubImage2D(GLenum target,
//      GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei
//      height, GLenum format, GLsizei imageSize, const GLvoid *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core25glCompressedTexSubImage2DEjiiiiijiPKv(
    QOpenGLFunctions_4_2_Core *self,
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

//  void QOpenGLFunctions_4_2_Core::glCompressedTexSubImage3D(GLenum target,
//      GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei
//      width, GLsizei height, GLsizei depth, GLenum format, GLsizei
//      imageSize, const GLvoid *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core25glCompressedTexSubImage3DEjiiiiiiijiPKv(
    QOpenGLFunctions_4_2_Core *self,
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

//  void QOpenGLFunctions_4_2_Core::glCompressedTexImage1D(GLenum target,
//      GLint level, GLenum internalformat, GLsizei width, GLint border,
//      GLsizei imageSize, const GLvoid *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core22glCompressedTexImage1DEjijiiiPKv(
    QOpenGLFunctions_4_2_Core *self,
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

//  void QOpenGLFunctions_4_2_Core::glCompressedTexImage2D(GLenum target,
//      GLint level, GLenum internalformat, GLsizei width, GLsizei height,
//      GLint border, GLsizei imageSize, const GLvoid *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core22glCompressedTexImage2DEjijiiiiPKv(
    QOpenGLFunctions_4_2_Core *self,
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

//  void QOpenGLFunctions_4_2_Core::glCompressedTexImage3D(GLenum target,
//      GLint level, GLenum internalformat, GLsizei width, GLsizei height,
//      GLsizei depth, GLint border, GLsizei imageSize, const GLvoid *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core22glCompressedTexImage3DEjijiiiiiPKv(
    QOpenGLFunctions_4_2_Core *self,
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

//  void QOpenGLFunctions_4_2_Core::glSampleCoverage(GLfloat value, GLboolean
//      invert)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core16glSampleCoverageEfh(
    QOpenGLFunctions_4_2_Core *self,
    GLfloat value,
    GLboolean invert) {
  self->glSampleCoverage(value, invert);
}

//  void QOpenGLFunctions_4_2_Core::glActiveTexture(GLenum texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core15glActiveTextureEj(
    QOpenGLFunctions_4_2_Core *self,
    GLenum texture) {
  self->glActiveTexture(texture);
}

//  void QOpenGLFunctions_4_2_Core::glPointParameteriv(GLenum pname, const
//      GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core18glPointParameterivEjPKi(
    QOpenGLFunctions_4_2_Core *self,
    GLenum pname,
    const GLint *params) {
  self->glPointParameteriv(pname, params);
}

//  void QOpenGLFunctions_4_2_Core::glPointParameteri(GLenum pname, GLint
//      param)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core17glPointParameteriEji(
    QOpenGLFunctions_4_2_Core *self,
    GLenum pname,
    GLint param) {
  self->glPointParameteri(pname, param);
}

//  void QOpenGLFunctions_4_2_Core::glPointParameterfv(GLenum pname, const
//      GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core18glPointParameterfvEjPKf(
    QOpenGLFunctions_4_2_Core *self,
    GLenum pname,
    const GLfloat *params) {
  self->glPointParameterfv(pname, params);
}

//  void QOpenGLFunctions_4_2_Core::glPointParameterf(GLenum pname, GLfloat
//      param)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core17glPointParameterfEjf(
    QOpenGLFunctions_4_2_Core *self,
    GLenum pname,
    GLfloat param) {
  self->glPointParameterf(pname, param);
}

//  void QOpenGLFunctions_4_2_Core::glMultiDrawElements(GLenum mode, const
//      GLsizei *count, GLenum type, const GLvoid *const *indices, GLsizei
//      drawcount)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core19glMultiDrawElementsEjPKijPKPKvi(
    QOpenGLFunctions_4_2_Core *self,
    GLenum mode,
    const GLsizei *count,
    GLenum type,
    const GLvoid *const *indices,
    GLsizei drawcount) {
  self->glMultiDrawElements(mode, count, type, indices, drawcount);
}

//  void QOpenGLFunctions_4_2_Core::glMultiDrawArrays(GLenum mode, const
//      GLint *first, const GLsizei *count, GLsizei drawcount)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core17glMultiDrawArraysEjPKiS1_i(
    QOpenGLFunctions_4_2_Core *self,
    GLenum mode,
    const GLint *first,
    const GLsizei *count,
    GLsizei drawcount) {
  self->glMultiDrawArrays(mode, first, count, drawcount);
}

//  void QOpenGLFunctions_4_2_Core::glBlendFuncSeparate(GLenum sfactorRGB,
//      GLenum dfactorRGB, GLenum sfactorAlpha, GLenum dfactorAlpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core19glBlendFuncSeparateEjjjj(
    QOpenGLFunctions_4_2_Core *self,
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

//  void QOpenGLFunctions_4_2_Core::glGetBufferPointerv(GLenum target, GLenum
//      pname, GLvoid **params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core19glGetBufferPointervEjjPPv(
    QOpenGLFunctions_4_2_Core *self,
    GLenum target,
    GLenum pname,
    GLvoid **params) {
  self->glGetBufferPointerv(target, pname, params);
}

//  void QOpenGLFunctions_4_2_Core::glGetBufferParameteriv(GLenum target,
//      GLenum pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core22glGetBufferParameterivEjjPi(
    QOpenGLFunctions_4_2_Core *self,
    GLenum target,
    GLenum pname,
    GLint *params) {
  self->glGetBufferParameteriv(target, pname, params);
}

//  GLboolean QOpenGLFunctions_4_2_Core::glUnmapBuffer(GLenum target)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN25QOpenGLFunctions_4_2_Core13glUnmapBufferEj(
    QOpenGLFunctions_4_2_Core *self,
    GLenum target) {
  return self->glUnmapBuffer(target);
}

//  GLvoid *QOpenGLFunctions_4_2_Core::glMapBuffer(GLenum target, GLenum
//      access)
extern "C" Q_DECL_EXPORT
GLvoid *ritual_ZN25QOpenGLFunctions_4_2_Core11glMapBufferEjj(
    QOpenGLFunctions_4_2_Core *self,
    GLenum target,
    GLenum access) {
  return self->glMapBuffer(target, access);
}

//  void QOpenGLFunctions_4_2_Core::glGetBufferSubData(GLenum target,
//      GLintptr offset, GLsizeiptr size, GLvoid *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core18glGetBufferSubDataEjllPv(
    QOpenGLFunctions_4_2_Core *self,
    GLenum target,
    long long offset,
    long long size,
    GLvoid *data) {
  self->glGetBufferSubData(target, offset, size, data);
}

//  void QOpenGLFunctions_4_2_Core::glBufferSubData(GLenum target, GLintptr
//      offset, GLsizeiptr size, const GLvoid *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core15glBufferSubDataEjllPKv(
    QOpenGLFunctions_4_2_Core *self,
    GLenum target,
    long long offset,
    long long size,
    const GLvoid *data) {
  self->glBufferSubData(target, offset, size, data);
}

//  void QOpenGLFunctions_4_2_Core::glBufferData(GLenum target, GLsizeiptr
//      size, const GLvoid *data, GLenum usage)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core12glBufferDataEjlPKvj(
    QOpenGLFunctions_4_2_Core *self,
    GLenum target,
    long long size,
    const GLvoid *data,
    GLenum usage) {
  self->glBufferData(target, size, data, usage);
}

//  GLboolean QOpenGLFunctions_4_2_Core::glIsBuffer(GLuint buffer)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN25QOpenGLFunctions_4_2_Core10glIsBufferEj(
    QOpenGLFunctions_4_2_Core *self,
    GLuint buffer) {
  return self->glIsBuffer(buffer);
}

//  void QOpenGLFunctions_4_2_Core::glGenBuffers(GLsizei n, GLuint *buffers)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core12glGenBuffersEiPj(
    QOpenGLFunctions_4_2_Core *self,
    GLsizei n,
    GLuint *buffers) {
  self->glGenBuffers(n, buffers);
}

//  void QOpenGLFunctions_4_2_Core::glDeleteBuffers(GLsizei n, const GLuint
//      *buffers)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core15glDeleteBuffersEiPKj(
    QOpenGLFunctions_4_2_Core *self,
    GLsizei n,
    const GLuint *buffers) {
  self->glDeleteBuffers(n, buffers);
}

//  void QOpenGLFunctions_4_2_Core::glBindBuffer(GLenum target, GLuint
//      buffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core12glBindBufferEjj(
    QOpenGLFunctions_4_2_Core *self,
    GLenum target,
    GLuint buffer) {
  self->glBindBuffer(target, buffer);
}

//  void QOpenGLFunctions_4_2_Core::glGetQueryObjectuiv(GLuint id, GLenum
//      pname, GLuint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core19glGetQueryObjectuivEjjPj(
    QOpenGLFunctions_4_2_Core *self,
    GLuint id,
    GLenum pname,
    GLuint *params) {
  self->glGetQueryObjectuiv(id, pname, params);
}

//  void QOpenGLFunctions_4_2_Core::glGetQueryObjectiv(GLuint id, GLenum
//      pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core18glGetQueryObjectivEjjPi(
    QOpenGLFunctions_4_2_Core *self,
    GLuint id,
    GLenum pname,
    GLint *params) {
  self->glGetQueryObjectiv(id, pname, params);
}

//  void QOpenGLFunctions_4_2_Core::glGetQueryiv(GLenum target, GLenum pname,
//      GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core12glGetQueryivEjjPi(
    QOpenGLFunctions_4_2_Core *self,
    GLenum target,
    GLenum pname,
    GLint *params) {
  self->glGetQueryiv(target, pname, params);
}

//  void QOpenGLFunctions_4_2_Core::glEndQuery(GLenum target)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core10glEndQueryEj(
    QOpenGLFunctions_4_2_Core *self,
    GLenum target) {
  self->glEndQuery(target);
}

//  void QOpenGLFunctions_4_2_Core::glBeginQuery(GLenum target, GLuint id)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core12glBeginQueryEjj(
    QOpenGLFunctions_4_2_Core *self,
    GLenum target,
    GLuint id) {
  self->glBeginQuery(target, id);
}

//  GLboolean QOpenGLFunctions_4_2_Core::glIsQuery(GLuint id)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN25QOpenGLFunctions_4_2_Core9glIsQueryEj(
    QOpenGLFunctions_4_2_Core *self,
    GLuint id) {
  return self->glIsQuery(id);
}

//  void QOpenGLFunctions_4_2_Core::glDeleteQueries(GLsizei n, const GLuint
//      *ids)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core15glDeleteQueriesEiPKj(
    QOpenGLFunctions_4_2_Core *self,
    GLsizei n,
    const GLuint *ids) {
  self->glDeleteQueries(n, ids);
}

//  void QOpenGLFunctions_4_2_Core::glGenQueries(GLsizei n, GLuint *ids)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core12glGenQueriesEiPj(
    QOpenGLFunctions_4_2_Core *self,
    GLsizei n,
    GLuint *ids) {
  self->glGenQueries(n, ids);
}

//  void QOpenGLFunctions_4_2_Core::glVertexAttribPointer(GLuint index, GLint
//      size, GLenum type, GLboolean normalized, GLsizei stride, const GLvoid
//      *pointer)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core21glVertexAttribPointerEjijhiPKv(
    QOpenGLFunctions_4_2_Core *self,
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

//  void QOpenGLFunctions_4_2_Core::glValidateProgram(GLuint program)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core17glValidateProgramEj(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program) {
  self->glValidateProgram(program);
}

//  void QOpenGLFunctions_4_2_Core::glUniformMatrix4fv(GLint location,
//      GLsizei count, GLboolean transpose, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core18glUniformMatrix4fvEiihPKf(
    QOpenGLFunctions_4_2_Core *self,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLfloat *value) {
  self->glUniformMatrix4fv(location, count, transpose, value);
}

//  void QOpenGLFunctions_4_2_Core::glUniformMatrix3fv(GLint location,
//      GLsizei count, GLboolean transpose, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core18glUniformMatrix3fvEiihPKf(
    QOpenGLFunctions_4_2_Core *self,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLfloat *value) {
  self->glUniformMatrix3fv(location, count, transpose, value);
}

//  void QOpenGLFunctions_4_2_Core::glUniformMatrix2fv(GLint location,
//      GLsizei count, GLboolean transpose, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core18glUniformMatrix2fvEiihPKf(
    QOpenGLFunctions_4_2_Core *self,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLfloat *value) {
  self->glUniformMatrix2fv(location, count, transpose, value);
}

//  void QOpenGLFunctions_4_2_Core::glUniform4iv(GLint location, GLsizei
//      count, const GLint *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core12glUniform4ivEiiPKi(
    QOpenGLFunctions_4_2_Core *self,
    GLint location,
    GLsizei count,
    const GLint *value) {
  self->glUniform4iv(location, count, value);
}

//  void QOpenGLFunctions_4_2_Core::glUniform3iv(GLint location, GLsizei
//      count, const GLint *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core12glUniform3ivEiiPKi(
    QOpenGLFunctions_4_2_Core *self,
    GLint location,
    GLsizei count,
    const GLint *value) {
  self->glUniform3iv(location, count, value);
}

//  void QOpenGLFunctions_4_2_Core::glUniform2iv(GLint location, GLsizei
//      count, const GLint *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core12glUniform2ivEiiPKi(
    QOpenGLFunctions_4_2_Core *self,
    GLint location,
    GLsizei count,
    const GLint *value) {
  self->glUniform2iv(location, count, value);
}

//  void QOpenGLFunctions_4_2_Core::glUniform1iv(GLint location, GLsizei
//      count, const GLint *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core12glUniform1ivEiiPKi(
    QOpenGLFunctions_4_2_Core *self,
    GLint location,
    GLsizei count,
    const GLint *value) {
  self->glUniform1iv(location, count, value);
}

//  void QOpenGLFunctions_4_2_Core::glUniform4fv(GLint location, GLsizei
//      count, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core12glUniform4fvEiiPKf(
    QOpenGLFunctions_4_2_Core *self,
    GLint location,
    GLsizei count,
    const GLfloat *value) {
  self->glUniform4fv(location, count, value);
}

//  void QOpenGLFunctions_4_2_Core::glUniform3fv(GLint location, GLsizei
//      count, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core12glUniform3fvEiiPKf(
    QOpenGLFunctions_4_2_Core *self,
    GLint location,
    GLsizei count,
    const GLfloat *value) {
  self->glUniform3fv(location, count, value);
}

//  void QOpenGLFunctions_4_2_Core::glUniform2fv(GLint location, GLsizei
//      count, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core12glUniform2fvEiiPKf(
    QOpenGLFunctions_4_2_Core *self,
    GLint location,
    GLsizei count,
    const GLfloat *value) {
  self->glUniform2fv(location, count, value);
}

//  void QOpenGLFunctions_4_2_Core::glUniform1fv(GLint location, GLsizei
//      count, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core12glUniform1fvEiiPKf(
    QOpenGLFunctions_4_2_Core *self,
    GLint location,
    GLsizei count,
    const GLfloat *value) {
  self->glUniform1fv(location, count, value);
}

//  void QOpenGLFunctions_4_2_Core::glUniform4i(GLint location, GLint v0,
//      GLint v1, GLint v2, GLint v3)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core11glUniform4iEiiiii(
    QOpenGLFunctions_4_2_Core *self,
    GLint location,
    GLint v0,
    GLint v1,
    GLint v2,
    GLint v3) {
  self->glUniform4i(location, v0, v1, v2, v3);
}

//  void QOpenGLFunctions_4_2_Core::glUniform3i(GLint location, GLint v0,
//      GLint v1, GLint v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core11glUniform3iEiiii(
    QOpenGLFunctions_4_2_Core *self,
    GLint location,
    GLint v0,
    GLint v1,
    GLint v2) {
  self->glUniform3i(location, v0, v1, v2);
}

//  void QOpenGLFunctions_4_2_Core::glUniform2i(GLint location, GLint v0,
//      GLint v1)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core11glUniform2iEiii(
    QOpenGLFunctions_4_2_Core *self,
    GLint location,
    GLint v0,
    GLint v1) {
  self->glUniform2i(location, v0, v1);
}

//  void QOpenGLFunctions_4_2_Core::glUniform1i(GLint location, GLint v0)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core11glUniform1iEii(
    QOpenGLFunctions_4_2_Core *self,
    GLint location,
    GLint v0) {
  self->glUniform1i(location, v0);
}

//  void QOpenGLFunctions_4_2_Core::glUniform4f(GLint location, GLfloat v0,
//      GLfloat v1, GLfloat v2, GLfloat v3)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core11glUniform4fEiffff(
    QOpenGLFunctions_4_2_Core *self,
    GLint location,
    GLfloat v0,
    GLfloat v1,
    GLfloat v2,
    GLfloat v3) {
  self->glUniform4f(location, v0, v1, v2, v3);
}

//  void QOpenGLFunctions_4_2_Core::glUniform3f(GLint location, GLfloat v0,
//      GLfloat v1, GLfloat v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core11glUniform3fEifff(
    QOpenGLFunctions_4_2_Core *self,
    GLint location,
    GLfloat v0,
    GLfloat v1,
    GLfloat v2) {
  self->glUniform3f(location, v0, v1, v2);
}

//  void QOpenGLFunctions_4_2_Core::glUniform2f(GLint location, GLfloat v0,
//      GLfloat v1)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core11glUniform2fEiff(
    QOpenGLFunctions_4_2_Core *self,
    GLint location,
    GLfloat v0,
    GLfloat v1) {
  self->glUniform2f(location, v0, v1);
}

//  void QOpenGLFunctions_4_2_Core::glUniform1f(GLint location, GLfloat v0)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core11glUniform1fEif(
    QOpenGLFunctions_4_2_Core *self,
    GLint location,
    GLfloat v0) {
  self->glUniform1f(location, v0);
}

//  void QOpenGLFunctions_4_2_Core::glUseProgram(GLuint program)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core12glUseProgramEj(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program) {
  self->glUseProgram(program);
}

//  void QOpenGLFunctions_4_2_Core::glShaderSource(GLuint shader, GLsizei
//      count, const GLchar *const *string, const GLint *length)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core14glShaderSourceEjiPKPKcPKi(
    QOpenGLFunctions_4_2_Core *self,
    GLuint shader,
    GLsizei count,
    const GLchar *const *string,
    const GLint *length) {
  self->glShaderSource(shader, count, string, length);
}

//  void QOpenGLFunctions_4_2_Core::glLinkProgram(GLuint program)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core13glLinkProgramEj(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program) {
  self->glLinkProgram(program);
}

//  GLboolean QOpenGLFunctions_4_2_Core::glIsShader(GLuint shader)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN25QOpenGLFunctions_4_2_Core10glIsShaderEj(
    QOpenGLFunctions_4_2_Core *self,
    GLuint shader) {
  return self->glIsShader(shader);
}

//  GLboolean QOpenGLFunctions_4_2_Core::glIsProgram(GLuint program)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN25QOpenGLFunctions_4_2_Core11glIsProgramEj(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program) {
  return self->glIsProgram(program);
}

//  void QOpenGLFunctions_4_2_Core::glGetVertexAttribPointerv(GLuint index,
//      GLenum pname, GLvoid **pointer)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core25glGetVertexAttribPointervEjjPPv(
    QOpenGLFunctions_4_2_Core *self,
    GLuint index,
    GLenum pname,
    GLvoid **pointer) {
  self->glGetVertexAttribPointerv(index, pname, pointer);
}

//  void QOpenGLFunctions_4_2_Core::glGetVertexAttribiv(GLuint index, GLenum
//      pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core19glGetVertexAttribivEjjPi(
    QOpenGLFunctions_4_2_Core *self,
    GLuint index,
    GLenum pname,
    GLint *params) {
  self->glGetVertexAttribiv(index, pname, params);
}

//  void QOpenGLFunctions_4_2_Core::glGetVertexAttribfv(GLuint index, GLenum
//      pname, GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core19glGetVertexAttribfvEjjPf(
    QOpenGLFunctions_4_2_Core *self,
    GLuint index,
    GLenum pname,
    GLfloat *params) {
  self->glGetVertexAttribfv(index, pname, params);
}

//  void QOpenGLFunctions_4_2_Core::glGetVertexAttribdv(GLuint index, GLenum
//      pname, GLdouble *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core19glGetVertexAttribdvEjjPd(
    QOpenGLFunctions_4_2_Core *self,
    GLuint index,
    GLenum pname,
    GLdouble *params) {
  self->glGetVertexAttribdv(index, pname, params);
}

//  void QOpenGLFunctions_4_2_Core::glGetUniformiv(GLuint program, GLint
//      location, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core14glGetUniformivEjiPi(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLint location,
    GLint *params) {
  self->glGetUniformiv(program, location, params);
}

//  void QOpenGLFunctions_4_2_Core::glGetUniformfv(GLuint program, GLint
//      location, GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core14glGetUniformfvEjiPf(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLint location,
    GLfloat *params) {
  self->glGetUniformfv(program, location, params);
}

//  GLint QOpenGLFunctions_4_2_Core::glGetUniformLocation(GLuint program,
//      const GLchar *name)
extern "C" Q_DECL_EXPORT
GLint ritual_ZN25QOpenGLFunctions_4_2_Core20glGetUniformLocationEjPKc(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    const GLchar *name) {
  return self->glGetUniformLocation(program, name);
}

//  void QOpenGLFunctions_4_2_Core::glGetShaderSource(GLuint shader, GLsizei
//      bufSize, GLsizei *length, GLchar *source)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core17glGetShaderSourceEjiPiPc(
    QOpenGLFunctions_4_2_Core *self,
    GLuint shader,
    GLsizei bufSize,
    GLsizei *length,
    GLchar *source) {
  self->glGetShaderSource(shader, bufSize, length, source);
}

//  void QOpenGLFunctions_4_2_Core::glGetShaderInfoLog(GLuint shader, GLsizei
//      bufSize, GLsizei *length, GLchar *infoLog)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core18glGetShaderInfoLogEjiPiPc(
    QOpenGLFunctions_4_2_Core *self,
    GLuint shader,
    GLsizei bufSize,
    GLsizei *length,
    GLchar *infoLog) {
  self->glGetShaderInfoLog(shader, bufSize, length, infoLog);
}

//  void QOpenGLFunctions_4_2_Core::glGetShaderiv(GLuint shader, GLenum
//      pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core13glGetShaderivEjjPi(
    QOpenGLFunctions_4_2_Core *self,
    GLuint shader,
    GLenum pname,
    GLint *params) {
  self->glGetShaderiv(shader, pname, params);
}

//  void QOpenGLFunctions_4_2_Core::glGetProgramInfoLog(GLuint program,
//      GLsizei bufSize, GLsizei *length, GLchar *infoLog)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core19glGetProgramInfoLogEjiPiPc(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLsizei bufSize,
    GLsizei *length,
    GLchar *infoLog) {
  self->glGetProgramInfoLog(program, bufSize, length, infoLog);
}

//  void QOpenGLFunctions_4_2_Core::glGetProgramiv(GLuint program, GLenum
//      pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core14glGetProgramivEjjPi(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLenum pname,
    GLint *params) {
  self->glGetProgramiv(program, pname, params);
}

//  GLint QOpenGLFunctions_4_2_Core::glGetAttribLocation(GLuint program,
//      const GLchar *name)
extern "C" Q_DECL_EXPORT
GLint ritual_ZN25QOpenGLFunctions_4_2_Core19glGetAttribLocationEjPKc(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    const GLchar *name) {
  return self->glGetAttribLocation(program, name);
}

//  void QOpenGLFunctions_4_2_Core::glGetAttachedShaders(GLuint program,
//      GLsizei maxCount, GLsizei *count, GLuint *obj)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core20glGetAttachedShadersEjiPiPj(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLsizei maxCount,
    GLsizei *count,
    GLuint *obj) {
  self->glGetAttachedShaders(program, maxCount, count, obj);
}

//  void QOpenGLFunctions_4_2_Core::glGetActiveUniform(GLuint program, GLuint
//      index, GLsizei bufSize, GLsizei *length, GLint *size, GLenum *type,
//      GLchar *name)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core18glGetActiveUniformEjjiPiS0_PjPc(
    QOpenGLFunctions_4_2_Core *self,
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

//  void QOpenGLFunctions_4_2_Core::glGetActiveAttrib(GLuint program, GLuint
//      index, GLsizei bufSize, GLsizei *length, GLint *size, GLenum *type,
//      GLchar *name)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core17glGetActiveAttribEjjiPiS0_PjPc(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLuint index,
    GLsizei bufSize,
    GLsizei *length,
    GLint *size,
    GLenum *type,
    GLchar *name) {
  self->glGetActiveAttrib(program, index, bufSize, length, size, type, name);
}

//  void QOpenGLFunctions_4_2_Core::glEnableVertexAttribArray(GLuint index)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core25glEnableVertexAttribArrayEj(
    QOpenGLFunctions_4_2_Core *self,
    GLuint index) {
  self->glEnableVertexAttribArray(index);
}

//  void QOpenGLFunctions_4_2_Core::glDisableVertexAttribArray(GLuint index)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core26glDisableVertexAttribArrayEj(
    QOpenGLFunctions_4_2_Core *self,
    GLuint index) {
  self->glDisableVertexAttribArray(index);
}

//  void QOpenGLFunctions_4_2_Core::glDetachShader(GLuint program, GLuint
//      shader)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core14glDetachShaderEjj(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLuint shader) {
  self->glDetachShader(program, shader);
}

//  void QOpenGLFunctions_4_2_Core::glDeleteShader(GLuint shader)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core14glDeleteShaderEj(
    QOpenGLFunctions_4_2_Core *self,
    GLuint shader) {
  self->glDeleteShader(shader);
}

//  void QOpenGLFunctions_4_2_Core::glDeleteProgram(GLuint program)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core15glDeleteProgramEj(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program) {
  self->glDeleteProgram(program);
}

//  GLuint QOpenGLFunctions_4_2_Core::glCreateShader(GLenum type)
extern "C" Q_DECL_EXPORT
GLuint ritual_ZN25QOpenGLFunctions_4_2_Core14glCreateShaderEj(
    QOpenGLFunctions_4_2_Core *self,
    GLenum type) {
  return self->glCreateShader(type);
}

//  GLuint QOpenGLFunctions_4_2_Core::glCreateProgram()
extern "C" Q_DECL_EXPORT
GLuint ritual_ZN25QOpenGLFunctions_4_2_Core15glCreateProgramEv(
    QOpenGLFunctions_4_2_Core *self) {
  return self->glCreateProgram();
}

//  void QOpenGLFunctions_4_2_Core::glCompileShader(GLuint shader)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core15glCompileShaderEj(
    QOpenGLFunctions_4_2_Core *self,
    GLuint shader) {
  self->glCompileShader(shader);
}

//  void QOpenGLFunctions_4_2_Core::glBindAttribLocation(GLuint program,
//      GLuint index, const GLchar *name)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core20glBindAttribLocationEjjPKc(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLuint index,
    const GLchar *name) {
  self->glBindAttribLocation(program, index, name);
}

//  void QOpenGLFunctions_4_2_Core::glAttachShader(GLuint program, GLuint
//      shader)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core14glAttachShaderEjj(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLuint shader) {
  self->glAttachShader(program, shader);
}

//  void QOpenGLFunctions_4_2_Core::glStencilMaskSeparate(GLenum face, GLuint
//      mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core21glStencilMaskSeparateEjj(
    QOpenGLFunctions_4_2_Core *self,
    GLenum face,
    GLuint mask) {
  self->glStencilMaskSeparate(face, mask);
}

//  void QOpenGLFunctions_4_2_Core::glStencilFuncSeparate(GLenum face, GLenum
//      func, GLint ref, GLuint mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core21glStencilFuncSeparateEjjij(
    QOpenGLFunctions_4_2_Core *self,
    GLenum face,
    GLenum func,
    GLint ref,
    GLuint mask) {
  self->glStencilFuncSeparate(face, func, ref, mask);
}

//  void QOpenGLFunctions_4_2_Core::glStencilOpSeparate(GLenum face, GLenum
//      sfail, GLenum dpfail, GLenum dppass)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core19glStencilOpSeparateEjjjj(
    QOpenGLFunctions_4_2_Core *self,
    GLenum face,
    GLenum sfail,
    GLenum dpfail,
    GLenum dppass) {
  self->glStencilOpSeparate(face, sfail, dpfail, dppass);
}

//  void QOpenGLFunctions_4_2_Core::glDrawBuffers(GLsizei n, const GLenum
//      *bufs)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core13glDrawBuffersEiPKj(
    QOpenGLFunctions_4_2_Core *self,
    GLsizei n,
    const GLenum *bufs) {
  self->glDrawBuffers(n, bufs);
}

//  void QOpenGLFunctions_4_2_Core::glBlendEquationSeparate(GLenum modeRGB,
//      GLenum modeAlpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core23glBlendEquationSeparateEjj(
    QOpenGLFunctions_4_2_Core *self,
    GLenum modeRGB,
    GLenum modeAlpha) {
  self->glBlendEquationSeparate(modeRGB, modeAlpha);
}

//  void QOpenGLFunctions_4_2_Core::glUniformMatrix4x3fv(GLint location,
//      GLsizei count, GLboolean transpose, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core20glUniformMatrix4x3fvEiihPKf(
    QOpenGLFunctions_4_2_Core *self,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLfloat *value) {
  self->glUniformMatrix4x3fv(location, count, transpose, value);
}

//  void QOpenGLFunctions_4_2_Core::glUniformMatrix3x4fv(GLint location,
//      GLsizei count, GLboolean transpose, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core20glUniformMatrix3x4fvEiihPKf(
    QOpenGLFunctions_4_2_Core *self,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLfloat *value) {
  self->glUniformMatrix3x4fv(location, count, transpose, value);
}

//  void QOpenGLFunctions_4_2_Core::glUniformMatrix4x2fv(GLint location,
//      GLsizei count, GLboolean transpose, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core20glUniformMatrix4x2fvEiihPKf(
    QOpenGLFunctions_4_2_Core *self,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLfloat *value) {
  self->glUniformMatrix4x2fv(location, count, transpose, value);
}

//  void QOpenGLFunctions_4_2_Core::glUniformMatrix2x4fv(GLint location,
//      GLsizei count, GLboolean transpose, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core20glUniformMatrix2x4fvEiihPKf(
    QOpenGLFunctions_4_2_Core *self,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLfloat *value) {
  self->glUniformMatrix2x4fv(location, count, transpose, value);
}

//  void QOpenGLFunctions_4_2_Core::glUniformMatrix3x2fv(GLint location,
//      GLsizei count, GLboolean transpose, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core20glUniformMatrix3x2fvEiihPKf(
    QOpenGLFunctions_4_2_Core *self,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLfloat *value) {
  self->glUniformMatrix3x2fv(location, count, transpose, value);
}

//  void QOpenGLFunctions_4_2_Core::glUniformMatrix2x3fv(GLint location,
//      GLsizei count, GLboolean transpose, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core20glUniformMatrix2x3fvEiihPKf(
    QOpenGLFunctions_4_2_Core *self,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLfloat *value) {
  self->glUniformMatrix2x3fv(location, count, transpose, value);
}

//  GLboolean QOpenGLFunctions_4_2_Core::glIsVertexArray(GLuint array)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN25QOpenGLFunctions_4_2_Core15glIsVertexArrayEj(
    QOpenGLFunctions_4_2_Core *self,
    GLuint array) {
  return self->glIsVertexArray(array);
}

//  void QOpenGLFunctions_4_2_Core::glGenVertexArrays(GLsizei n, GLuint
//      *arrays)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core17glGenVertexArraysEiPj(
    QOpenGLFunctions_4_2_Core *self,
    GLsizei n,
    GLuint *arrays) {
  self->glGenVertexArrays(n, arrays);
}

//  void QOpenGLFunctions_4_2_Core::glDeleteVertexArrays(GLsizei n, const
//      GLuint *arrays)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core20glDeleteVertexArraysEiPKj(
    QOpenGLFunctions_4_2_Core *self,
    GLsizei n,
    const GLuint *arrays) {
  self->glDeleteVertexArrays(n, arrays);
}

//  void QOpenGLFunctions_4_2_Core::glBindVertexArray(GLuint array)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core17glBindVertexArrayEj(
    QOpenGLFunctions_4_2_Core *self,
    GLuint array) {
  self->glBindVertexArray(array);
}

//  void QOpenGLFunctions_4_2_Core::glFlushMappedBufferRange(GLenum target,
//      GLintptr offset, GLsizeiptr length)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core24glFlushMappedBufferRangeEjll(
    QOpenGLFunctions_4_2_Core *self,
    GLenum target,
    long long offset,
    long long length) {
  self->glFlushMappedBufferRange(target, offset, length);
}

//  GLvoid *QOpenGLFunctions_4_2_Core::glMapBufferRange(GLenum target,
//      GLintptr offset, GLsizeiptr length, GLbitfield access)
extern "C" Q_DECL_EXPORT
GLvoid *ritual_ZN25QOpenGLFunctions_4_2_Core16glMapBufferRangeEjllj(
    QOpenGLFunctions_4_2_Core *self,
    GLenum target,
    long long offset,
    long long length,
    GLbitfield access) {
  return self->glMapBufferRange(target, offset, length, access);
}

//  void QOpenGLFunctions_4_2_Core::glFramebufferTextureLayer(GLenum target,
//      GLenum attachment, GLuint texture, GLint level, GLint layer)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core25glFramebufferTextureLayerEjjjii(
    QOpenGLFunctions_4_2_Core *self,
    GLenum target,
    GLenum attachment,
    GLuint texture,
    GLint level,
    GLint layer) {
  self->glFramebufferTextureLayer(target, attachment, texture, level, layer);
}

//  void QOpenGLFunctions_4_2_Core::glRenderbufferStorageMultisample(GLenum
//      target, GLsizei samples, GLenum internalformat, GLsizei width,
//      GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core32glRenderbufferStorageMultisampleEjijii(
    QOpenGLFunctions_4_2_Core *self,
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

//  void QOpenGLFunctions_4_2_Core::glBlitFramebuffer(GLint srcX0, GLint
//      srcY0, GLint srcX1, GLint srcY1, GLint dstX0, GLint dstY0, GLint
//      dstX1, GLint dstY1, GLbitfield mask, GLenum filter)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core17glBlitFramebufferEiiiiiiiijj(
    QOpenGLFunctions_4_2_Core *self,
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

//  void QOpenGLFunctions_4_2_Core::glGenerateMipmap(GLenum target)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core16glGenerateMipmapEj(
    QOpenGLFunctions_4_2_Core *self,
    GLenum target) {
  self->glGenerateMipmap(target);
}

//  void
//      QOpenGLFunctions_4_2_Core::glGetFramebufferAttachmentParameteriv(GLen
//      um target, GLenum attachment, GLenum pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core37glGetFramebufferAttachmentParameterivEjjjPi(
    QOpenGLFunctions_4_2_Core *self,
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

//  void QOpenGLFunctions_4_2_Core::glFramebufferRenderbuffer(GLenum target,
//      GLenum attachment, GLenum renderbuffertarget, GLuint renderbuffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core25glFramebufferRenderbufferEjjjj(
    QOpenGLFunctions_4_2_Core *self,
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

//  void QOpenGLFunctions_4_2_Core::glFramebufferTexture3D(GLenum target,
//      GLenum attachment, GLenum textarget, GLuint texture, GLint level,
//      GLint zoffset)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core22glFramebufferTexture3DEjjjjii(
    QOpenGLFunctions_4_2_Core *self,
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

//  void QOpenGLFunctions_4_2_Core::glFramebufferTexture2D(GLenum target,
//      GLenum attachment, GLenum textarget, GLuint texture, GLint level)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core22glFramebufferTexture2DEjjjji(
    QOpenGLFunctions_4_2_Core *self,
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

//  void QOpenGLFunctions_4_2_Core::glFramebufferTexture1D(GLenum target,
//      GLenum attachment, GLenum textarget, GLuint texture, GLint level)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core22glFramebufferTexture1DEjjjji(
    QOpenGLFunctions_4_2_Core *self,
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

//  GLenum QOpenGLFunctions_4_2_Core::glCheckFramebufferStatus(GLenum target)
extern "C" Q_DECL_EXPORT
GLenum ritual_ZN25QOpenGLFunctions_4_2_Core24glCheckFramebufferStatusEj(
    QOpenGLFunctions_4_2_Core *self,
    GLenum target) {
  return self->glCheckFramebufferStatus(target);
}

//  void QOpenGLFunctions_4_2_Core::glGenFramebuffers(GLsizei n, GLuint
//      *framebuffers)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core17glGenFramebuffersEiPj(
    QOpenGLFunctions_4_2_Core *self,
    GLsizei n,
    GLuint *framebuffers) {
  self->glGenFramebuffers(n, framebuffers);
}

//  void QOpenGLFunctions_4_2_Core::glDeleteFramebuffers(GLsizei n, const
//      GLuint *framebuffers)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core20glDeleteFramebuffersEiPKj(
    QOpenGLFunctions_4_2_Core *self,
    GLsizei n,
    const GLuint *framebuffers) {
  self->glDeleteFramebuffers(n, framebuffers);
}

//  void QOpenGLFunctions_4_2_Core::glBindFramebuffer(GLenum target, GLuint
//      framebuffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core17glBindFramebufferEjj(
    QOpenGLFunctions_4_2_Core *self,
    GLenum target,
    GLuint framebuffer) {
  self->glBindFramebuffer(target, framebuffer);
}

//  GLboolean QOpenGLFunctions_4_2_Core::glIsFramebuffer(GLuint framebuffer)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN25QOpenGLFunctions_4_2_Core15glIsFramebufferEj(
    QOpenGLFunctions_4_2_Core *self,
    GLuint framebuffer) {
  return self->glIsFramebuffer(framebuffer);
}

//  void QOpenGLFunctions_4_2_Core::glGetRenderbufferParameteriv(GLenum
//      target, GLenum pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core28glGetRenderbufferParameterivEjjPi(
    QOpenGLFunctions_4_2_Core *self,
    GLenum target,
    GLenum pname,
    GLint *params) {
  self->glGetRenderbufferParameteriv(target, pname, params);
}

//  void QOpenGLFunctions_4_2_Core::glRenderbufferStorage(GLenum target,
//      GLenum internalformat, GLsizei width, GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core21glRenderbufferStorageEjjii(
    QOpenGLFunctions_4_2_Core *self,
    GLenum target,
    GLenum internalformat,
    GLsizei width,
    GLsizei height) {
  self->glRenderbufferStorage(target, internalformat, width, height);
}

//  void QOpenGLFunctions_4_2_Core::glGenRenderbuffers(GLsizei n, GLuint
//      *renderbuffers)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core18glGenRenderbuffersEiPj(
    QOpenGLFunctions_4_2_Core *self,
    GLsizei n,
    GLuint *renderbuffers) {
  self->glGenRenderbuffers(n, renderbuffers);
}

//  void QOpenGLFunctions_4_2_Core::glDeleteRenderbuffers(GLsizei n, const
//      GLuint *renderbuffers)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core21glDeleteRenderbuffersEiPKj(
    QOpenGLFunctions_4_2_Core *self,
    GLsizei n,
    const GLuint *renderbuffers) {
  self->glDeleteRenderbuffers(n, renderbuffers);
}

//  void QOpenGLFunctions_4_2_Core::glBindRenderbuffer(GLenum target, GLuint
//      renderbuffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core18glBindRenderbufferEjj(
    QOpenGLFunctions_4_2_Core *self,
    GLenum target,
    GLuint renderbuffer) {
  self->glBindRenderbuffer(target, renderbuffer);
}

//  GLboolean QOpenGLFunctions_4_2_Core::glIsRenderbuffer(GLuint
//      renderbuffer)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN25QOpenGLFunctions_4_2_Core16glIsRenderbufferEj(
    QOpenGLFunctions_4_2_Core *self,
    GLuint renderbuffer) {
  return self->glIsRenderbuffer(renderbuffer);
}

//  const GLubyte *QOpenGLFunctions_4_2_Core::glGetStringi(GLenum name,
//      GLuint index)
extern "C" Q_DECL_EXPORT
const GLubyte *ritual_ZN25QOpenGLFunctions_4_2_Core12glGetStringiEjj(
    QOpenGLFunctions_4_2_Core *self,
    GLenum name,
    GLuint index) {
  return self->glGetStringi(name, index);
}

//  void QOpenGLFunctions_4_2_Core::glClearBufferfi(GLenum buffer, GLint
//      drawbuffer, GLfloat depth, GLint stencil)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core15glClearBufferfiEjifi(
    QOpenGLFunctions_4_2_Core *self,
    GLenum buffer,
    GLint drawbuffer,
    GLfloat depth,
    GLint stencil) {
  self->glClearBufferfi(buffer, drawbuffer, depth, stencil);
}

//  void QOpenGLFunctions_4_2_Core::glClearBufferfv(GLenum buffer, GLint
//      drawbuffer, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core15glClearBufferfvEjiPKf(
    QOpenGLFunctions_4_2_Core *self,
    GLenum buffer,
    GLint drawbuffer,
    const GLfloat *value) {
  self->glClearBufferfv(buffer, drawbuffer, value);
}

//  void QOpenGLFunctions_4_2_Core::glClearBufferuiv(GLenum buffer, GLint
//      drawbuffer, const GLuint *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core16glClearBufferuivEjiPKj(
    QOpenGLFunctions_4_2_Core *self,
    GLenum buffer,
    GLint drawbuffer,
    const GLuint *value) {
  self->glClearBufferuiv(buffer, drawbuffer, value);
}

//  void QOpenGLFunctions_4_2_Core::glClearBufferiv(GLenum buffer, GLint
//      drawbuffer, const GLint *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core15glClearBufferivEjiPKi(
    QOpenGLFunctions_4_2_Core *self,
    GLenum buffer,
    GLint drawbuffer,
    const GLint *value) {
  self->glClearBufferiv(buffer, drawbuffer, value);
}

//  void QOpenGLFunctions_4_2_Core::glGetTexParameterIuiv(GLenum target,
//      GLenum pname, GLuint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core21glGetTexParameterIuivEjjPj(
    QOpenGLFunctions_4_2_Core *self,
    GLenum target,
    GLenum pname,
    GLuint *params) {
  self->glGetTexParameterIuiv(target, pname, params);
}

//  void QOpenGLFunctions_4_2_Core::glGetTexParameterIiv(GLenum target,
//      GLenum pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core20glGetTexParameterIivEjjPi(
    QOpenGLFunctions_4_2_Core *self,
    GLenum target,
    GLenum pname,
    GLint *params) {
  self->glGetTexParameterIiv(target, pname, params);
}

//  void QOpenGLFunctions_4_2_Core::glTexParameterIuiv(GLenum target, GLenum
//      pname, const GLuint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core18glTexParameterIuivEjjPKj(
    QOpenGLFunctions_4_2_Core *self,
    GLenum target,
    GLenum pname,
    const GLuint *params) {
  self->glTexParameterIuiv(target, pname, params);
}

//  void QOpenGLFunctions_4_2_Core::glTexParameterIiv(GLenum target, GLenum
//      pname, const GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core17glTexParameterIivEjjPKi(
    QOpenGLFunctions_4_2_Core *self,
    GLenum target,
    GLenum pname,
    const GLint *params) {
  self->glTexParameterIiv(target, pname, params);
}

//  void QOpenGLFunctions_4_2_Core::glUniform4uiv(GLint location, GLsizei
//      count, const GLuint *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core13glUniform4uivEiiPKj(
    QOpenGLFunctions_4_2_Core *self,
    GLint location,
    GLsizei count,
    const GLuint *value) {
  self->glUniform4uiv(location, count, value);
}

//  void QOpenGLFunctions_4_2_Core::glUniform3uiv(GLint location, GLsizei
//      count, const GLuint *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core13glUniform3uivEiiPKj(
    QOpenGLFunctions_4_2_Core *self,
    GLint location,
    GLsizei count,
    const GLuint *value) {
  self->glUniform3uiv(location, count, value);
}

//  void QOpenGLFunctions_4_2_Core::glUniform2uiv(GLint location, GLsizei
//      count, const GLuint *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core13glUniform2uivEiiPKj(
    QOpenGLFunctions_4_2_Core *self,
    GLint location,
    GLsizei count,
    const GLuint *value) {
  self->glUniform2uiv(location, count, value);
}

//  void QOpenGLFunctions_4_2_Core::glUniform1uiv(GLint location, GLsizei
//      count, const GLuint *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core13glUniform1uivEiiPKj(
    QOpenGLFunctions_4_2_Core *self,
    GLint location,
    GLsizei count,
    const GLuint *value) {
  self->glUniform1uiv(location, count, value);
}

//  void QOpenGLFunctions_4_2_Core::glUniform4ui(GLint location, GLuint v0,
//      GLuint v1, GLuint v2, GLuint v3)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core12glUniform4uiEijjjj(
    QOpenGLFunctions_4_2_Core *self,
    GLint location,
    GLuint v0,
    GLuint v1,
    GLuint v2,
    GLuint v3) {
  self->glUniform4ui(location, v0, v1, v2, v3);
}

//  void QOpenGLFunctions_4_2_Core::glUniform3ui(GLint location, GLuint v0,
//      GLuint v1, GLuint v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core12glUniform3uiEijjj(
    QOpenGLFunctions_4_2_Core *self,
    GLint location,
    GLuint v0,
    GLuint v1,
    GLuint v2) {
  self->glUniform3ui(location, v0, v1, v2);
}

//  void QOpenGLFunctions_4_2_Core::glUniform2ui(GLint location, GLuint v0,
//      GLuint v1)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core12glUniform2uiEijj(
    QOpenGLFunctions_4_2_Core *self,
    GLint location,
    GLuint v0,
    GLuint v1) {
  self->glUniform2ui(location, v0, v1);
}

//  void QOpenGLFunctions_4_2_Core::glUniform1ui(GLint location, GLuint v0)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core12glUniform1uiEij(
    QOpenGLFunctions_4_2_Core *self,
    GLint location,
    GLuint v0) {
  self->glUniform1ui(location, v0);
}

//  GLint QOpenGLFunctions_4_2_Core::glGetFragDataLocation(GLuint program,
//      const GLchar *name)
extern "C" Q_DECL_EXPORT
GLint ritual_ZN25QOpenGLFunctions_4_2_Core21glGetFragDataLocationEjPKc(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    const GLchar *name) {
  return self->glGetFragDataLocation(program, name);
}

//  void QOpenGLFunctions_4_2_Core::glBindFragDataLocation(GLuint program,
//      GLuint color, const GLchar *name)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core22glBindFragDataLocationEjjPKc(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLuint color,
    const GLchar *name) {
  self->glBindFragDataLocation(program, color, name);
}

//  void QOpenGLFunctions_4_2_Core::glGetUniformuiv(GLuint program, GLint
//      location, GLuint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core15glGetUniformuivEjiPj(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLint location,
    GLuint *params) {
  self->glGetUniformuiv(program, location, params);
}

//  void QOpenGLFunctions_4_2_Core::glGetVertexAttribIuiv(GLuint index,
//      GLenum pname, GLuint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core21glGetVertexAttribIuivEjjPj(
    QOpenGLFunctions_4_2_Core *self,
    GLuint index,
    GLenum pname,
    GLuint *params) {
  self->glGetVertexAttribIuiv(index, pname, params);
}

//  void QOpenGLFunctions_4_2_Core::glGetVertexAttribIiv(GLuint index, GLenum
//      pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core20glGetVertexAttribIivEjjPi(
    QOpenGLFunctions_4_2_Core *self,
    GLuint index,
    GLenum pname,
    GLint *params) {
  self->glGetVertexAttribIiv(index, pname, params);
}

//  void QOpenGLFunctions_4_2_Core::glVertexAttribIPointer(GLuint index,
//      GLint size, GLenum type, GLsizei stride, const GLvoid *pointer)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core22glVertexAttribIPointerEjijiPKv(
    QOpenGLFunctions_4_2_Core *self,
    GLuint index,
    GLint size,
    GLenum type,
    GLsizei stride,
    const GLvoid *pointer) {
  self->glVertexAttribIPointer(index, size, type, stride, pointer);
}

//  void QOpenGLFunctions_4_2_Core::glEndConditionalRender()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core22glEndConditionalRenderEv(
    QOpenGLFunctions_4_2_Core *self) {
  self->glEndConditionalRender();
}

//  void QOpenGLFunctions_4_2_Core::glBeginConditionalRender(GLuint id,
//      GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core24glBeginConditionalRenderEjj(
    QOpenGLFunctions_4_2_Core *self,
    GLuint id,
    GLenum mode) {
  self->glBeginConditionalRender(id, mode);
}

//  void QOpenGLFunctions_4_2_Core::glClampColor(GLenum target, GLenum clamp)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core12glClampColorEjj(
    QOpenGLFunctions_4_2_Core *self,
    GLenum target,
    GLenum clamp) {
  self->glClampColor(target, clamp);
}

//  void QOpenGLFunctions_4_2_Core::glGetTransformFeedbackVarying(GLuint
//      program, GLuint index, GLsizei bufSize, GLsizei *length, GLsizei
//      *size, GLenum *type, GLchar *name)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core29glGetTransformFeedbackVaryingEjjiPiS0_PjPc(
    QOpenGLFunctions_4_2_Core *self,
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

//  void QOpenGLFunctions_4_2_Core::glTransformFeedbackVaryings(GLuint
//      program, GLsizei count, const GLchar *const *varyings, GLenum
//      bufferMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core27glTransformFeedbackVaryingsEjiPKPKcj(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLsizei count,
    const GLchar *const *varyings,
    GLenum bufferMode) {
  self->glTransformFeedbackVaryings(program, count, varyings, bufferMode);
}

//  void QOpenGLFunctions_4_2_Core::glBindBufferBase(GLenum target, GLuint
//      index, GLuint buffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core16glBindBufferBaseEjjj(
    QOpenGLFunctions_4_2_Core *self,
    GLenum target,
    GLuint index,
    GLuint buffer) {
  self->glBindBufferBase(target, index, buffer);
}

//  void QOpenGLFunctions_4_2_Core::glBindBufferRange(GLenum target, GLuint
//      index, GLuint buffer, GLintptr offset, GLsizeiptr size)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core17glBindBufferRangeEjjjll(
    QOpenGLFunctions_4_2_Core *self,
    GLenum target,
    GLuint index,
    GLuint buffer,
    long long offset,
    long long size) {
  self->glBindBufferRange(target, index, buffer, offset, size);
}

//  void QOpenGLFunctions_4_2_Core::glEndTransformFeedback()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core22glEndTransformFeedbackEv(
    QOpenGLFunctions_4_2_Core *self) {
  self->glEndTransformFeedback();
}

//  void QOpenGLFunctions_4_2_Core::glBeginTransformFeedback(GLenum
//      primitiveMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core24glBeginTransformFeedbackEj(
    QOpenGLFunctions_4_2_Core *self,
    GLenum primitiveMode) {
  self->glBeginTransformFeedback(primitiveMode);
}

//  GLboolean QOpenGLFunctions_4_2_Core::glIsEnabledi(GLenum target, GLuint
//      index)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN25QOpenGLFunctions_4_2_Core12glIsEnablediEjj(
    QOpenGLFunctions_4_2_Core *self,
    GLenum target,
    GLuint index) {
  return self->glIsEnabledi(target, index);
}

//  void QOpenGLFunctions_4_2_Core::glDisablei(GLenum target, GLuint index)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core10glDisableiEjj(
    QOpenGLFunctions_4_2_Core *self,
    GLenum target,
    GLuint index) {
  self->glDisablei(target, index);
}

//  void QOpenGLFunctions_4_2_Core::glEnablei(GLenum target, GLuint index)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core9glEnableiEjj(
    QOpenGLFunctions_4_2_Core *self,
    GLenum target,
    GLuint index) {
  self->glEnablei(target, index);
}

//  void QOpenGLFunctions_4_2_Core::glGetIntegeri_v(GLenum target, GLuint
//      index, GLint *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core15glGetIntegeri_vEjjPi(
    QOpenGLFunctions_4_2_Core *self,
    GLenum target,
    GLuint index,
    GLint *data) {
  self->glGetIntegeri_v(target, index, data);
}

//  void QOpenGLFunctions_4_2_Core::glGetBooleani_v(GLenum target, GLuint
//      index, GLboolean *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core15glGetBooleani_vEjjPh(
    QOpenGLFunctions_4_2_Core *self,
    GLenum target,
    GLuint index,
    GLboolean *data) {
  self->glGetBooleani_v(target, index, data);
}

//  void QOpenGLFunctions_4_2_Core::glColorMaski(GLuint index, GLboolean r,
//      GLboolean g, GLboolean b, GLboolean a)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core12glColorMaskiEjhhhh(
    QOpenGLFunctions_4_2_Core *self,
    GLuint index,
    GLboolean r,
    GLboolean g,
    GLboolean b,
    GLboolean a) {
  self->glColorMaski(index, r, g, b, a);
}

//  void QOpenGLFunctions_4_2_Core::glCopyBufferSubData(GLenum readTarget,
//      GLenum writeTarget, GLintptr readOffset, GLintptr writeOffset,
//      GLsizeiptr size)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core19glCopyBufferSubDataEjjlll(
    QOpenGLFunctions_4_2_Core *self,
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

//  void QOpenGLFunctions_4_2_Core::glUniformBlockBinding(GLuint program,
//      GLuint uniformBlockIndex, GLuint uniformBlockBinding)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core21glUniformBlockBindingEjjj(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLuint uniformBlockIndex,
    GLuint uniformBlockBinding) {
  self->glUniformBlockBinding(
      program,
      uniformBlockIndex,
      uniformBlockBinding);
}

//  void QOpenGLFunctions_4_2_Core::glGetActiveUniformBlockName(GLuint
//      program, GLuint uniformBlockIndex, GLsizei bufSize, GLsizei *length,
//      GLchar *uniformBlockName)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core27glGetActiveUniformBlockNameEjjiPiPc(
    QOpenGLFunctions_4_2_Core *self,
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

//  void QOpenGLFunctions_4_2_Core::glGetActiveUniformBlockiv(GLuint program,
//      GLuint uniformBlockIndex, GLenum pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core25glGetActiveUniformBlockivEjjjPi(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLuint uniformBlockIndex,
    GLenum pname,
    GLint *params) {
  self->glGetActiveUniformBlockiv(program, uniformBlockIndex, pname, params);
}

//  GLuint QOpenGLFunctions_4_2_Core::glGetUniformBlockIndex(GLuint program,
//      const GLchar *uniformBlockName)
extern "C" Q_DECL_EXPORT
GLuint ritual_ZN25QOpenGLFunctions_4_2_Core22glGetUniformBlockIndexEjPKc(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    const GLchar *uniformBlockName) {
  return self->glGetUniformBlockIndex(program, uniformBlockName);
}

//  void QOpenGLFunctions_4_2_Core::glGetActiveUniformName(GLuint program,
//      GLuint uniformIndex, GLsizei bufSize, GLsizei *length, GLchar
//      *uniformName)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core22glGetActiveUniformNameEjjiPiPc(
    QOpenGLFunctions_4_2_Core *self,
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

//  void QOpenGLFunctions_4_2_Core::glGetActiveUniformsiv(GLuint program,
//      GLsizei uniformCount, const GLuint *uniformIndices, GLenum pname,
//      GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core21glGetActiveUniformsivEjiPKjjPi(
    QOpenGLFunctions_4_2_Core *self,
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

//  void QOpenGLFunctions_4_2_Core::glGetUniformIndices(GLuint program,
//      GLsizei uniformCount, const GLchar *const *uniformNames, GLuint
//      *uniformIndices)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core19glGetUniformIndicesEjiPKPKcPj(
    QOpenGLFunctions_4_2_Core *self,
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

//  void QOpenGLFunctions_4_2_Core::glPrimitiveRestartIndex(GLuint index)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core23glPrimitiveRestartIndexEj(
    QOpenGLFunctions_4_2_Core *self,
    GLuint index) {
  self->glPrimitiveRestartIndex(index);
}

//  void QOpenGLFunctions_4_2_Core::glTexBuffer(GLenum target, GLenum
//      internalformat, GLuint buffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core11glTexBufferEjjj(
    QOpenGLFunctions_4_2_Core *self,
    GLenum target,
    GLenum internalformat,
    GLuint buffer) {
  self->glTexBuffer(target, internalformat, buffer);
}

//  void QOpenGLFunctions_4_2_Core::glDrawElementsInstanced(GLenum mode,
//      GLsizei count, GLenum type, const GLvoid *indices, GLsizei
//      instancecount)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core23glDrawElementsInstancedEjijPKvi(
    QOpenGLFunctions_4_2_Core *self,
    GLenum mode,
    GLsizei count,
    GLenum type,
    const GLvoid *indices,
    GLsizei instancecount) {
  self->glDrawElementsInstanced(mode, count, type, indices, instancecount);
}

//  void QOpenGLFunctions_4_2_Core::glDrawArraysInstanced(GLenum mode, GLint
//      first, GLsizei count, GLsizei instancecount)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core21glDrawArraysInstancedEjiii(
    QOpenGLFunctions_4_2_Core *self,
    GLenum mode,
    GLint first,
    GLsizei count,
    GLsizei instancecount) {
  self->glDrawArraysInstanced(mode, first, count, instancecount);
}

//  void QOpenGLFunctions_4_2_Core::glSampleMaski(GLuint index, GLbitfield
//      mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core13glSampleMaskiEjj(
    QOpenGLFunctions_4_2_Core *self,
    GLuint index,
    GLbitfield mask) {
  self->glSampleMaski(index, mask);
}

//  void QOpenGLFunctions_4_2_Core::glGetMultisamplefv(GLenum pname, GLuint
//      index, GLfloat *val)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core18glGetMultisamplefvEjjPf(
    QOpenGLFunctions_4_2_Core *self,
    GLenum pname,
    GLuint index,
    GLfloat *val) {
  self->glGetMultisamplefv(pname, index, val);
}

//  void QOpenGLFunctions_4_2_Core::glTexImage3DMultisample(GLenum target,
//      GLsizei samples, GLint internalformat, GLsizei width, GLsizei height,
//      GLsizei depth, GLboolean fixedsamplelocations)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core23glTexImage3DMultisampleEjiiiiih(
    QOpenGLFunctions_4_2_Core *self,
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

//  void QOpenGLFunctions_4_2_Core::glTexImage2DMultisample(GLenum target,
//      GLsizei samples, GLint internalformat, GLsizei width, GLsizei height,
//      GLboolean fixedsamplelocations)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core23glTexImage2DMultisampleEjiiiih(
    QOpenGLFunctions_4_2_Core *self,
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

//  void QOpenGLFunctions_4_2_Core::glGetSynciv(GLsync sync, GLenum pname,
//      GLsizei bufSize, GLsizei *length, GLint *values)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core11glGetSyncivEP8__GLsyncjiPiS2_(
    QOpenGLFunctions_4_2_Core *self,
    GLsync sync,
    GLenum pname,
    GLsizei bufSize,
    GLsizei *length,
    GLint *values) {
  self->glGetSynciv(sync, pname, bufSize, length, values);
}

//  void QOpenGLFunctions_4_2_Core::glGetInteger64v(GLenum pname, GLint64
//      *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core15glGetInteger64vEjPl(
    QOpenGLFunctions_4_2_Core *self,
    GLenum pname,
    GLint64 *params) {
  self->glGetInteger64v(pname, params);
}

//  void QOpenGLFunctions_4_2_Core::glWaitSync(GLsync sync, GLbitfield flags,
//      GLuint64 timeout)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core10glWaitSyncEP8__GLsyncjm(
    QOpenGLFunctions_4_2_Core *self,
    GLsync sync,
    GLbitfield flags,
    unsigned long long timeout) {
  self->glWaitSync(sync, flags, timeout);
}

//  GLenum QOpenGLFunctions_4_2_Core::glClientWaitSync(GLsync sync,
//      GLbitfield flags, GLuint64 timeout)
extern "C" Q_DECL_EXPORT
GLenum ritual_ZN25QOpenGLFunctions_4_2_Core16glClientWaitSyncEP8__GLsyncjm(
    QOpenGLFunctions_4_2_Core *self,
    GLsync sync,
    GLbitfield flags,
    unsigned long long timeout) {
  return self->glClientWaitSync(sync, flags, timeout);
}

//  void QOpenGLFunctions_4_2_Core::glDeleteSync(GLsync sync)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core12glDeleteSyncEP8__GLsync(
    QOpenGLFunctions_4_2_Core *self,
    GLsync sync) {
  self->glDeleteSync(sync);
}

//  GLboolean QOpenGLFunctions_4_2_Core::glIsSync(GLsync sync)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN25QOpenGLFunctions_4_2_Core8glIsSyncEP8__GLsync(
    QOpenGLFunctions_4_2_Core *self,
    GLsync sync) {
  return self->glIsSync(sync);
}

//  GLsync QOpenGLFunctions_4_2_Core::glFenceSync(GLenum condition,
//      GLbitfield flags)
extern "C" Q_DECL_EXPORT
GLsync ritual_ZN25QOpenGLFunctions_4_2_Core11glFenceSyncEjj(
    QOpenGLFunctions_4_2_Core *self,
    GLenum condition,
    GLbitfield flags) {
  return self->glFenceSync(condition, flags);
}

//  void QOpenGLFunctions_4_2_Core::glProvokingVertex(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core17glProvokingVertexEj(
    QOpenGLFunctions_4_2_Core *self,
    GLenum mode) {
  self->glProvokingVertex(mode);
}

//  void QOpenGLFunctions_4_2_Core::glMultiDrawElementsBaseVertex(GLenum
//      mode, const GLsizei *count, GLenum type, const GLvoid *const
//      *indices, GLsizei drawcount, const GLint *basevertex)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core29glMultiDrawElementsBaseVertexEjPKijPKPKviS1_(
    QOpenGLFunctions_4_2_Core *self,
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

//  void QOpenGLFunctions_4_2_Core::glDrawElementsInstancedBaseVertex(GLenum
//      mode, GLsizei count, GLenum type, const GLvoid *indices, GLsizei
//      instancecount, GLint basevertex)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core33glDrawElementsInstancedBaseVertexEjijPKvii(
    QOpenGLFunctions_4_2_Core *self,
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

//  void QOpenGLFunctions_4_2_Core::glDrawRangeElementsBaseVertex(GLenum
//      mode, GLuint start, GLuint end, GLsizei count, GLenum type, const
//      GLvoid *indices, GLint basevertex)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core29glDrawRangeElementsBaseVertexEjjjijPKvi(
    QOpenGLFunctions_4_2_Core *self,
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

//  void QOpenGLFunctions_4_2_Core::glDrawElementsBaseVertex(GLenum mode,
//      GLsizei count, GLenum type, const GLvoid *indices, GLint basevertex)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core24glDrawElementsBaseVertexEjijPKvi(
    QOpenGLFunctions_4_2_Core *self,
    GLenum mode,
    GLsizei count,
    GLenum type,
    const GLvoid *indices,
    GLint basevertex) {
  self->glDrawElementsBaseVertex(mode, count, type, indices, basevertex);
}

//  void QOpenGLFunctions_4_2_Core::glFramebufferTexture(GLenum target,
//      GLenum attachment, GLuint texture, GLint level)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core20glFramebufferTextureEjjji(
    QOpenGLFunctions_4_2_Core *self,
    GLenum target,
    GLenum attachment,
    GLuint texture,
    GLint level) {
  self->glFramebufferTexture(target, attachment, texture, level);
}

//  void QOpenGLFunctions_4_2_Core::glGetBufferParameteri64v(GLenum target,
//      GLenum pname, GLint64 *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core24glGetBufferParameteri64vEjjPl(
    QOpenGLFunctions_4_2_Core *self,
    GLenum target,
    GLenum pname,
    GLint64 *params) {
  self->glGetBufferParameteri64v(target, pname, params);
}

//  void QOpenGLFunctions_4_2_Core::glGetInteger64i_v(GLenum target, GLuint
//      index, GLint64 *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core17glGetInteger64i_vEjjPl(
    QOpenGLFunctions_4_2_Core *self,
    GLenum target,
    GLuint index,
    GLint64 *data) {
  self->glGetInteger64i_v(target, index, data);
}

//  void QOpenGLFunctions_4_2_Core::glVertexAttribP4uiv(GLuint index, GLenum
//      type, GLboolean normalized, const GLuint *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core19glVertexAttribP4uivEjjhPKj(
    QOpenGLFunctions_4_2_Core *self,
    GLuint index,
    GLenum type,
    GLboolean normalized,
    const GLuint *value) {
  self->glVertexAttribP4uiv(index, type, normalized, value);
}

//  void QOpenGLFunctions_4_2_Core::glVertexAttribP4ui(GLuint index, GLenum
//      type, GLboolean normalized, GLuint value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core18glVertexAttribP4uiEjjhj(
    QOpenGLFunctions_4_2_Core *self,
    GLuint index,
    GLenum type,
    GLboolean normalized,
    GLuint value) {
  self->glVertexAttribP4ui(index, type, normalized, value);
}

//  void QOpenGLFunctions_4_2_Core::glVertexAttribP3uiv(GLuint index, GLenum
//      type, GLboolean normalized, const GLuint *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core19glVertexAttribP3uivEjjhPKj(
    QOpenGLFunctions_4_2_Core *self,
    GLuint index,
    GLenum type,
    GLboolean normalized,
    const GLuint *value) {
  self->glVertexAttribP3uiv(index, type, normalized, value);
}

//  void QOpenGLFunctions_4_2_Core::glVertexAttribP3ui(GLuint index, GLenum
//      type, GLboolean normalized, GLuint value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core18glVertexAttribP3uiEjjhj(
    QOpenGLFunctions_4_2_Core *self,
    GLuint index,
    GLenum type,
    GLboolean normalized,
    GLuint value) {
  self->glVertexAttribP3ui(index, type, normalized, value);
}

//  void QOpenGLFunctions_4_2_Core::glVertexAttribP2uiv(GLuint index, GLenum
//      type, GLboolean normalized, const GLuint *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core19glVertexAttribP2uivEjjhPKj(
    QOpenGLFunctions_4_2_Core *self,
    GLuint index,
    GLenum type,
    GLboolean normalized,
    const GLuint *value) {
  self->glVertexAttribP2uiv(index, type, normalized, value);
}

//  void QOpenGLFunctions_4_2_Core::glVertexAttribP2ui(GLuint index, GLenum
//      type, GLboolean normalized, GLuint value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core18glVertexAttribP2uiEjjhj(
    QOpenGLFunctions_4_2_Core *self,
    GLuint index,
    GLenum type,
    GLboolean normalized,
    GLuint value) {
  self->glVertexAttribP2ui(index, type, normalized, value);
}

//  void QOpenGLFunctions_4_2_Core::glVertexAttribP1uiv(GLuint index, GLenum
//      type, GLboolean normalized, const GLuint *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core19glVertexAttribP1uivEjjhPKj(
    QOpenGLFunctions_4_2_Core *self,
    GLuint index,
    GLenum type,
    GLboolean normalized,
    const GLuint *value) {
  self->glVertexAttribP1uiv(index, type, normalized, value);
}

//  void QOpenGLFunctions_4_2_Core::glVertexAttribP1ui(GLuint index, GLenum
//      type, GLboolean normalized, GLuint value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core18glVertexAttribP1uiEjjhj(
    QOpenGLFunctions_4_2_Core *self,
    GLuint index,
    GLenum type,
    GLboolean normalized,
    GLuint value) {
  self->glVertexAttribP1ui(index, type, normalized, value);
}

//  void QOpenGLFunctions_4_2_Core::glGetQueryObjectui64v(GLuint id, GLenum
//      pname, GLuint64 *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core21glGetQueryObjectui64vEjjPm(
    QOpenGLFunctions_4_2_Core *self,
    GLuint id,
    GLenum pname,
    GLuint64 *params) {
  self->glGetQueryObjectui64v(id, pname, params);
}

//  void QOpenGLFunctions_4_2_Core::glGetQueryObjecti64v(GLuint id, GLenum
//      pname, GLint64 *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core20glGetQueryObjecti64vEjjPl(
    QOpenGLFunctions_4_2_Core *self,
    GLuint id,
    GLenum pname,
    GLint64 *params) {
  self->glGetQueryObjecti64v(id, pname, params);
}

//  void QOpenGLFunctions_4_2_Core::glQueryCounter(GLuint id, GLenum target)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core14glQueryCounterEjj(
    QOpenGLFunctions_4_2_Core *self,
    GLuint id,
    GLenum target) {
  self->glQueryCounter(id, target);
}

//  void QOpenGLFunctions_4_2_Core::glGetSamplerParameterIuiv(GLuint sampler,
//      GLenum pname, GLuint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core25glGetSamplerParameterIuivEjjPj(
    QOpenGLFunctions_4_2_Core *self,
    GLuint sampler,
    GLenum pname,
    GLuint *params) {
  self->glGetSamplerParameterIuiv(sampler, pname, params);
}

//  void QOpenGLFunctions_4_2_Core::glGetSamplerParameterfv(GLuint sampler,
//      GLenum pname, GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core23glGetSamplerParameterfvEjjPf(
    QOpenGLFunctions_4_2_Core *self,
    GLuint sampler,
    GLenum pname,
    GLfloat *params) {
  self->glGetSamplerParameterfv(sampler, pname, params);
}

//  void QOpenGLFunctions_4_2_Core::glGetSamplerParameterIiv(GLuint sampler,
//      GLenum pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core24glGetSamplerParameterIivEjjPi(
    QOpenGLFunctions_4_2_Core *self,
    GLuint sampler,
    GLenum pname,
    GLint *params) {
  self->glGetSamplerParameterIiv(sampler, pname, params);
}

//  void QOpenGLFunctions_4_2_Core::glGetSamplerParameteriv(GLuint sampler,
//      GLenum pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core23glGetSamplerParameterivEjjPi(
    QOpenGLFunctions_4_2_Core *self,
    GLuint sampler,
    GLenum pname,
    GLint *params) {
  self->glGetSamplerParameteriv(sampler, pname, params);
}

//  void QOpenGLFunctions_4_2_Core::glSamplerParameterIuiv(GLuint sampler,
//      GLenum pname, const GLuint *param)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core22glSamplerParameterIuivEjjPKj(
    QOpenGLFunctions_4_2_Core *self,
    GLuint sampler,
    GLenum pname,
    const GLuint *param) {
  self->glSamplerParameterIuiv(sampler, pname, param);
}

//  void QOpenGLFunctions_4_2_Core::glSamplerParameterIiv(GLuint sampler,
//      GLenum pname, const GLint *param)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core21glSamplerParameterIivEjjPKi(
    QOpenGLFunctions_4_2_Core *self,
    GLuint sampler,
    GLenum pname,
    const GLint *param) {
  self->glSamplerParameterIiv(sampler, pname, param);
}

//  void QOpenGLFunctions_4_2_Core::glSamplerParameterfv(GLuint sampler,
//      GLenum pname, const GLfloat *param)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core20glSamplerParameterfvEjjPKf(
    QOpenGLFunctions_4_2_Core *self,
    GLuint sampler,
    GLenum pname,
    const GLfloat *param) {
  self->glSamplerParameterfv(sampler, pname, param);
}

//  void QOpenGLFunctions_4_2_Core::glSamplerParameterf(GLuint sampler,
//      GLenum pname, GLfloat param)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core19glSamplerParameterfEjjf(
    QOpenGLFunctions_4_2_Core *self,
    GLuint sampler,
    GLenum pname,
    GLfloat param) {
  self->glSamplerParameterf(sampler, pname, param);
}

//  void QOpenGLFunctions_4_2_Core::glSamplerParameteriv(GLuint sampler,
//      GLenum pname, const GLint *param)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core20glSamplerParameterivEjjPKi(
    QOpenGLFunctions_4_2_Core *self,
    GLuint sampler,
    GLenum pname,
    const GLint *param) {
  self->glSamplerParameteriv(sampler, pname, param);
}

//  void QOpenGLFunctions_4_2_Core::glSamplerParameteri(GLuint sampler,
//      GLenum pname, GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core19glSamplerParameteriEjji(
    QOpenGLFunctions_4_2_Core *self,
    GLuint sampler,
    GLenum pname,
    GLint param) {
  self->glSamplerParameteri(sampler, pname, param);
}

//  void QOpenGLFunctions_4_2_Core::glBindSampler(GLuint unit, GLuint
//      sampler)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core13glBindSamplerEjj(
    QOpenGLFunctions_4_2_Core *self,
    GLuint unit,
    GLuint sampler) {
  self->glBindSampler(unit, sampler);
}

//  GLboolean QOpenGLFunctions_4_2_Core::glIsSampler(GLuint sampler)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN25QOpenGLFunctions_4_2_Core11glIsSamplerEj(
    QOpenGLFunctions_4_2_Core *self,
    GLuint sampler) {
  return self->glIsSampler(sampler);
}

//  void QOpenGLFunctions_4_2_Core::glDeleteSamplers(GLsizei count, const
//      GLuint *samplers)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core16glDeleteSamplersEiPKj(
    QOpenGLFunctions_4_2_Core *self,
    GLsizei count,
    const GLuint *samplers) {
  self->glDeleteSamplers(count, samplers);
}

//  void QOpenGLFunctions_4_2_Core::glGenSamplers(GLsizei count, GLuint
//      *samplers)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core13glGenSamplersEiPj(
    QOpenGLFunctions_4_2_Core *self,
    GLsizei count,
    GLuint *samplers) {
  self->glGenSamplers(count, samplers);
}

//  GLint QOpenGLFunctions_4_2_Core::glGetFragDataIndex(GLuint program, const
//      GLchar *name)
extern "C" Q_DECL_EXPORT
GLint ritual_ZN25QOpenGLFunctions_4_2_Core18glGetFragDataIndexEjPKc(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    const GLchar *name) {
  return self->glGetFragDataIndex(program, name);
}

//  void QOpenGLFunctions_4_2_Core::glBindFragDataLocationIndexed(GLuint
//      program, GLuint colorNumber, GLuint index, const GLchar *name)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core29glBindFragDataLocationIndexedEjjjPKc(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLuint colorNumber,
    GLuint index,
    const GLchar *name) {
  self->glBindFragDataLocationIndexed(program, colorNumber, index, name);
}

//  void QOpenGLFunctions_4_2_Core::glVertexAttribDivisor(GLuint index,
//      GLuint divisor)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core21glVertexAttribDivisorEjj(
    QOpenGLFunctions_4_2_Core *self,
    GLuint index,
    GLuint divisor) {
  self->glVertexAttribDivisor(index, divisor);
}

//  void QOpenGLFunctions_4_2_Core::glGetQueryIndexediv(GLenum target, GLuint
//      index, GLenum pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core19glGetQueryIndexedivEjjjPi(
    QOpenGLFunctions_4_2_Core *self,
    GLenum target,
    GLuint index,
    GLenum pname,
    GLint *params) {
  self->glGetQueryIndexediv(target, index, pname, params);
}

//  void QOpenGLFunctions_4_2_Core::glEndQueryIndexed(GLenum target, GLuint
//      index)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core17glEndQueryIndexedEjj(
    QOpenGLFunctions_4_2_Core *self,
    GLenum target,
    GLuint index) {
  self->glEndQueryIndexed(target, index);
}

//  void QOpenGLFunctions_4_2_Core::glBeginQueryIndexed(GLenum target, GLuint
//      index, GLuint id)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core19glBeginQueryIndexedEjjj(
    QOpenGLFunctions_4_2_Core *self,
    GLenum target,
    GLuint index,
    GLuint id) {
  self->glBeginQueryIndexed(target, index, id);
}

//  void QOpenGLFunctions_4_2_Core::glDrawTransformFeedbackStream(GLenum
//      mode, GLuint id, GLuint stream)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core29glDrawTransformFeedbackStreamEjjj(
    QOpenGLFunctions_4_2_Core *self,
    GLenum mode,
    GLuint id,
    GLuint stream) {
  self->glDrawTransformFeedbackStream(mode, id, stream);
}

//  void QOpenGLFunctions_4_2_Core::glDrawTransformFeedback(GLenum mode,
//      GLuint id)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core23glDrawTransformFeedbackEjj(
    QOpenGLFunctions_4_2_Core *self,
    GLenum mode,
    GLuint id) {
  self->glDrawTransformFeedback(mode, id);
}

//  void QOpenGLFunctions_4_2_Core::glResumeTransformFeedback()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core25glResumeTransformFeedbackEv(
    QOpenGLFunctions_4_2_Core *self) {
  self->glResumeTransformFeedback();
}

//  void QOpenGLFunctions_4_2_Core::glPauseTransformFeedback()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core24glPauseTransformFeedbackEv(
    QOpenGLFunctions_4_2_Core *self) {
  self->glPauseTransformFeedback();
}

//  GLboolean QOpenGLFunctions_4_2_Core::glIsTransformFeedback(GLuint id)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN25QOpenGLFunctions_4_2_Core21glIsTransformFeedbackEj(
    QOpenGLFunctions_4_2_Core *self,
    GLuint id) {
  return self->glIsTransformFeedback(id);
}

//  void QOpenGLFunctions_4_2_Core::glGenTransformFeedbacks(GLsizei n, GLuint
//      *ids)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core23glGenTransformFeedbacksEiPj(
    QOpenGLFunctions_4_2_Core *self,
    GLsizei n,
    GLuint *ids) {
  self->glGenTransformFeedbacks(n, ids);
}

//  void QOpenGLFunctions_4_2_Core::glDeleteTransformFeedbacks(GLsizei n,
//      const GLuint *ids)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core26glDeleteTransformFeedbacksEiPKj(
    QOpenGLFunctions_4_2_Core *self,
    GLsizei n,
    const GLuint *ids) {
  self->glDeleteTransformFeedbacks(n, ids);
}

//  void QOpenGLFunctions_4_2_Core::glBindTransformFeedback(GLenum target,
//      GLuint id)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core23glBindTransformFeedbackEjj(
    QOpenGLFunctions_4_2_Core *self,
    GLenum target,
    GLuint id) {
  self->glBindTransformFeedback(target, id);
}

//  void QOpenGLFunctions_4_2_Core::glPatchParameterfv(GLenum pname, const
//      GLfloat *values)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core18glPatchParameterfvEjPKf(
    QOpenGLFunctions_4_2_Core *self,
    GLenum pname,
    const GLfloat *values) {
  self->glPatchParameterfv(pname, values);
}

//  void QOpenGLFunctions_4_2_Core::glPatchParameteri(GLenum pname, GLint
//      value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core17glPatchParameteriEji(
    QOpenGLFunctions_4_2_Core *self,
    GLenum pname,
    GLint value) {
  self->glPatchParameteri(pname, value);
}

//  void QOpenGLFunctions_4_2_Core::glGetProgramStageiv(GLuint program,
//      GLenum shadertype, GLenum pname, GLint *values)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core19glGetProgramStageivEjjjPi(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLenum shadertype,
    GLenum pname,
    GLint *values) {
  self->glGetProgramStageiv(program, shadertype, pname, values);
}

//  void QOpenGLFunctions_4_2_Core::glGetUniformSubroutineuiv(GLenum
//      shadertype, GLint location, GLuint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core25glGetUniformSubroutineuivEjiPj(
    QOpenGLFunctions_4_2_Core *self,
    GLenum shadertype,
    GLint location,
    GLuint *params) {
  self->glGetUniformSubroutineuiv(shadertype, location, params);
}

//  void QOpenGLFunctions_4_2_Core::glUniformSubroutinesuiv(GLenum
//      shadertype, GLsizei count, const GLuint *indices)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core23glUniformSubroutinesuivEjiPKj(
    QOpenGLFunctions_4_2_Core *self,
    GLenum shadertype,
    GLsizei count,
    const GLuint *indices) {
  self->glUniformSubroutinesuiv(shadertype, count, indices);
}

//  void QOpenGLFunctions_4_2_Core::glGetActiveSubroutineName(GLuint program,
//      GLenum shadertype, GLuint index, GLsizei bufsize, GLsizei *length,
//      GLchar *name)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core25glGetActiveSubroutineNameEjjjiPiPc(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLenum shadertype,
    GLuint index,
    GLsizei bufsize,
    GLsizei *length,
    GLchar *name) {
  self->glGetActiveSubroutineName(
      program,
      shadertype,
      index,
      bufsize,
      length,
      name);
}

//  void QOpenGLFunctions_4_2_Core::glGetActiveSubroutineUniformName(GLuint
//      program, GLenum shadertype, GLuint index, GLsizei bufsize, GLsizei
//      *length, GLchar *name)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core32glGetActiveSubroutineUniformNameEjjjiPiPc(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLenum shadertype,
    GLuint index,
    GLsizei bufsize,
    GLsizei *length,
    GLchar *name) {
  self->glGetActiveSubroutineUniformName(
      program,
      shadertype,
      index,
      bufsize,
      length,
      name);
}

//  void QOpenGLFunctions_4_2_Core::glGetActiveSubroutineUniformiv(GLuint
//      program, GLenum shadertype, GLuint index, GLenum pname, GLint
//      *values)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core30glGetActiveSubroutineUniformivEjjjjPi(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLenum shadertype,
    GLuint index,
    GLenum pname,
    GLint *values) {
  self->glGetActiveSubroutineUniformiv(
      program,
      shadertype,
      index,
      pname,
      values);
}

//  GLuint QOpenGLFunctions_4_2_Core::glGetSubroutineIndex(GLuint program,
//      GLenum shadertype, const GLchar *name)
extern "C" Q_DECL_EXPORT
GLuint ritual_ZN25QOpenGLFunctions_4_2_Core20glGetSubroutineIndexEjjPKc(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLenum shadertype,
    const GLchar *name) {
  return self->glGetSubroutineIndex(program, shadertype, name);
}

//  GLint QOpenGLFunctions_4_2_Core::glGetSubroutineUniformLocation(GLuint
//      program, GLenum shadertype, const GLchar *name)
extern "C" Q_DECL_EXPORT
GLint ritual_ZN25QOpenGLFunctions_4_2_Core30glGetSubroutineUniformLocationEjjPKc(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLenum shadertype,
    const GLchar *name) {
  return self->glGetSubroutineUniformLocation(program, shadertype, name);
}

//  void QOpenGLFunctions_4_2_Core::glGetUniformdv(GLuint program, GLint
//      location, GLdouble *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core14glGetUniformdvEjiPd(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLint location,
    GLdouble *params) {
  self->glGetUniformdv(program, location, params);
}

//  void QOpenGLFunctions_4_2_Core::glUniformMatrix4x3dv(GLint location,
//      GLsizei count, GLboolean transpose, const GLdouble *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core20glUniformMatrix4x3dvEiihPKd(
    QOpenGLFunctions_4_2_Core *self,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLdouble *value) {
  self->glUniformMatrix4x3dv(location, count, transpose, value);
}

//  void QOpenGLFunctions_4_2_Core::glUniformMatrix4x2dv(GLint location,
//      GLsizei count, GLboolean transpose, const GLdouble *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core20glUniformMatrix4x2dvEiihPKd(
    QOpenGLFunctions_4_2_Core *self,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLdouble *value) {
  self->glUniformMatrix4x2dv(location, count, transpose, value);
}

//  void QOpenGLFunctions_4_2_Core::glUniformMatrix3x4dv(GLint location,
//      GLsizei count, GLboolean transpose, const GLdouble *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core20glUniformMatrix3x4dvEiihPKd(
    QOpenGLFunctions_4_2_Core *self,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLdouble *value) {
  self->glUniformMatrix3x4dv(location, count, transpose, value);
}

//  void QOpenGLFunctions_4_2_Core::glUniformMatrix3x2dv(GLint location,
//      GLsizei count, GLboolean transpose, const GLdouble *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core20glUniformMatrix3x2dvEiihPKd(
    QOpenGLFunctions_4_2_Core *self,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLdouble *value) {
  self->glUniformMatrix3x2dv(location, count, transpose, value);
}

//  void QOpenGLFunctions_4_2_Core::glUniformMatrix2x4dv(GLint location,
//      GLsizei count, GLboolean transpose, const GLdouble *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core20glUniformMatrix2x4dvEiihPKd(
    QOpenGLFunctions_4_2_Core *self,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLdouble *value) {
  self->glUniformMatrix2x4dv(location, count, transpose, value);
}

//  void QOpenGLFunctions_4_2_Core::glUniformMatrix2x3dv(GLint location,
//      GLsizei count, GLboolean transpose, const GLdouble *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core20glUniformMatrix2x3dvEiihPKd(
    QOpenGLFunctions_4_2_Core *self,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLdouble *value) {
  self->glUniformMatrix2x3dv(location, count, transpose, value);
}

//  void QOpenGLFunctions_4_2_Core::glUniformMatrix4dv(GLint location,
//      GLsizei count, GLboolean transpose, const GLdouble *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core18glUniformMatrix4dvEiihPKd(
    QOpenGLFunctions_4_2_Core *self,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLdouble *value) {
  self->glUniformMatrix4dv(location, count, transpose, value);
}

//  void QOpenGLFunctions_4_2_Core::glUniformMatrix3dv(GLint location,
//      GLsizei count, GLboolean transpose, const GLdouble *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core18glUniformMatrix3dvEiihPKd(
    QOpenGLFunctions_4_2_Core *self,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLdouble *value) {
  self->glUniformMatrix3dv(location, count, transpose, value);
}

//  void QOpenGLFunctions_4_2_Core::glUniformMatrix2dv(GLint location,
//      GLsizei count, GLboolean transpose, const GLdouble *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core18glUniformMatrix2dvEiihPKd(
    QOpenGLFunctions_4_2_Core *self,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLdouble *value) {
  self->glUniformMatrix2dv(location, count, transpose, value);
}

//  void QOpenGLFunctions_4_2_Core::glUniform4dv(GLint location, GLsizei
//      count, const GLdouble *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core12glUniform4dvEiiPKd(
    QOpenGLFunctions_4_2_Core *self,
    GLint location,
    GLsizei count,
    const GLdouble *value) {
  self->glUniform4dv(location, count, value);
}

//  void QOpenGLFunctions_4_2_Core::glUniform3dv(GLint location, GLsizei
//      count, const GLdouble *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core12glUniform3dvEiiPKd(
    QOpenGLFunctions_4_2_Core *self,
    GLint location,
    GLsizei count,
    const GLdouble *value) {
  self->glUniform3dv(location, count, value);
}

//  void QOpenGLFunctions_4_2_Core::glUniform2dv(GLint location, GLsizei
//      count, const GLdouble *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core12glUniform2dvEiiPKd(
    QOpenGLFunctions_4_2_Core *self,
    GLint location,
    GLsizei count,
    const GLdouble *value) {
  self->glUniform2dv(location, count, value);
}

//  void QOpenGLFunctions_4_2_Core::glUniform1dv(GLint location, GLsizei
//      count, const GLdouble *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core12glUniform1dvEiiPKd(
    QOpenGLFunctions_4_2_Core *self,
    GLint location,
    GLsizei count,
    const GLdouble *value) {
  self->glUniform1dv(location, count, value);
}

//  void QOpenGLFunctions_4_2_Core::glUniform4d(GLint location, GLdouble x,
//      GLdouble y, GLdouble z, GLdouble w)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core11glUniform4dEidddd(
    QOpenGLFunctions_4_2_Core *self,
    GLint location,
    GLdouble x,
    GLdouble y,
    GLdouble z,
    GLdouble w) {
  self->glUniform4d(location, x, y, z, w);
}

//  void QOpenGLFunctions_4_2_Core::glUniform3d(GLint location, GLdouble x,
//      GLdouble y, GLdouble z)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core11glUniform3dEiddd(
    QOpenGLFunctions_4_2_Core *self,
    GLint location,
    GLdouble x,
    GLdouble y,
    GLdouble z) {
  self->glUniform3d(location, x, y, z);
}

//  void QOpenGLFunctions_4_2_Core::glUniform2d(GLint location, GLdouble x,
//      GLdouble y)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core11glUniform2dEidd(
    QOpenGLFunctions_4_2_Core *self,
    GLint location,
    GLdouble x,
    GLdouble y) {
  self->glUniform2d(location, x, y);
}

//  void QOpenGLFunctions_4_2_Core::glUniform1d(GLint location, GLdouble x)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core11glUniform1dEid(
    QOpenGLFunctions_4_2_Core *self,
    GLint location,
    GLdouble x) {
  self->glUniform1d(location, x);
}

//  void QOpenGLFunctions_4_2_Core::glDrawElementsIndirect(GLenum mode,
//      GLenum type, const GLvoid *indirect)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core22glDrawElementsIndirectEjjPKv(
    QOpenGLFunctions_4_2_Core *self,
    GLenum mode,
    GLenum type,
    const GLvoid *indirect) {
  self->glDrawElementsIndirect(mode, type, indirect);
}

//  void QOpenGLFunctions_4_2_Core::glDrawArraysIndirect(GLenum mode, const
//      GLvoid *indirect)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core20glDrawArraysIndirectEjPKv(
    QOpenGLFunctions_4_2_Core *self,
    GLenum mode,
    const GLvoid *indirect) {
  self->glDrawArraysIndirect(mode, indirect);
}

//  void QOpenGLFunctions_4_2_Core::glBlendFuncSeparatei(GLuint buf, GLenum
//      srcRGB, GLenum dstRGB, GLenum srcAlpha, GLenum dstAlpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core20glBlendFuncSeparateiEjjjjj(
    QOpenGLFunctions_4_2_Core *self,
    GLuint buf,
    GLenum srcRGB,
    GLenum dstRGB,
    GLenum srcAlpha,
    GLenum dstAlpha) {
  self->glBlendFuncSeparatei(buf, srcRGB, dstRGB, srcAlpha, dstAlpha);
}

//  void QOpenGLFunctions_4_2_Core::glBlendFunci(GLuint buf, GLenum src,
//      GLenum dst)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core12glBlendFunciEjjj(
    QOpenGLFunctions_4_2_Core *self,
    GLuint buf,
    GLenum src,
    GLenum dst) {
  self->glBlendFunci(buf, src, dst);
}

//  void QOpenGLFunctions_4_2_Core::glBlendEquationSeparatei(GLuint buf,
//      GLenum modeRGB, GLenum modeAlpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core24glBlendEquationSeparateiEjjj(
    QOpenGLFunctions_4_2_Core *self,
    GLuint buf,
    GLenum modeRGB,
    GLenum modeAlpha) {
  self->glBlendEquationSeparatei(buf, modeRGB, modeAlpha);
}

//  void QOpenGLFunctions_4_2_Core::glBlendEquationi(GLuint buf, GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core16glBlendEquationiEjj(
    QOpenGLFunctions_4_2_Core *self,
    GLuint buf,
    GLenum mode) {
  self->glBlendEquationi(buf, mode);
}

//  void QOpenGLFunctions_4_2_Core::glMinSampleShading(GLfloat value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core18glMinSampleShadingEf(
    QOpenGLFunctions_4_2_Core *self,
    GLfloat value) {
  self->glMinSampleShading(value);
}

//  void QOpenGLFunctions_4_2_Core::glGetDoublei_v(GLenum target, GLuint
//      index, GLdouble *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core14glGetDoublei_vEjjPd(
    QOpenGLFunctions_4_2_Core *self,
    GLenum target,
    GLuint index,
    GLdouble *data) {
  self->glGetDoublei_v(target, index, data);
}

//  void QOpenGLFunctions_4_2_Core::glGetFloati_v(GLenum target, GLuint
//      index, GLfloat *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core13glGetFloati_vEjjPf(
    QOpenGLFunctions_4_2_Core *self,
    GLenum target,
    GLuint index,
    GLfloat *data) {
  self->glGetFloati_v(target, index, data);
}

//  void QOpenGLFunctions_4_2_Core::glDepthRangeIndexed(GLuint index,
//      GLdouble n, GLdouble f)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core19glDepthRangeIndexedEjdd(
    QOpenGLFunctions_4_2_Core *self,
    GLuint index,
    GLdouble n,
    GLdouble f) {
  self->glDepthRangeIndexed(index, n, f);
}

//  void QOpenGLFunctions_4_2_Core::glDepthRangeArrayv(GLuint first, GLsizei
//      count, const GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core18glDepthRangeArrayvEjiPKd(
    QOpenGLFunctions_4_2_Core *self,
    GLuint first,
    GLsizei count,
    const GLdouble *v) {
  self->glDepthRangeArrayv(first, count, v);
}

//  void QOpenGLFunctions_4_2_Core::glScissorIndexedv(GLuint index, const
//      GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core17glScissorIndexedvEjPKi(
    QOpenGLFunctions_4_2_Core *self,
    GLuint index,
    const GLint *v) {
  self->glScissorIndexedv(index, v);
}

//  void QOpenGLFunctions_4_2_Core::glScissorIndexed(GLuint index, GLint
//      left, GLint bottom, GLsizei width, GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core16glScissorIndexedEjiiii(
    QOpenGLFunctions_4_2_Core *self,
    GLuint index,
    GLint left,
    GLint bottom,
    GLsizei width,
    GLsizei height) {
  self->glScissorIndexed(index, left, bottom, width, height);
}

//  void QOpenGLFunctions_4_2_Core::glScissorArrayv(GLuint first, GLsizei
//      count, const GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core15glScissorArrayvEjiPKi(
    QOpenGLFunctions_4_2_Core *self,
    GLuint first,
    GLsizei count,
    const GLint *v) {
  self->glScissorArrayv(first, count, v);
}

//  void QOpenGLFunctions_4_2_Core::glViewportIndexedfv(GLuint index, const
//      GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core19glViewportIndexedfvEjPKf(
    QOpenGLFunctions_4_2_Core *self,
    GLuint index,
    const GLfloat *v) {
  self->glViewportIndexedfv(index, v);
}

//  void QOpenGLFunctions_4_2_Core::glViewportIndexedf(GLuint index, GLfloat
//      x, GLfloat y, GLfloat w, GLfloat h)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core18glViewportIndexedfEjffff(
    QOpenGLFunctions_4_2_Core *self,
    GLuint index,
    GLfloat x,
    GLfloat y,
    GLfloat w,
    GLfloat h) {
  self->glViewportIndexedf(index, x, y, w, h);
}

//  void QOpenGLFunctions_4_2_Core::glViewportArrayv(GLuint first, GLsizei
//      count, const GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core16glViewportArrayvEjiPKf(
    QOpenGLFunctions_4_2_Core *self,
    GLuint first,
    GLsizei count,
    const GLfloat *v) {
  self->glViewportArrayv(first, count, v);
}

//  void QOpenGLFunctions_4_2_Core::glGetVertexAttribLdv(GLuint index, GLenum
//      pname, GLdouble *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core20glGetVertexAttribLdvEjjPd(
    QOpenGLFunctions_4_2_Core *self,
    GLuint index,
    GLenum pname,
    GLdouble *params) {
  self->glGetVertexAttribLdv(index, pname, params);
}

//  void QOpenGLFunctions_4_2_Core::glVertexAttribLPointer(GLuint index,
//      GLint size, GLenum type, GLsizei stride, const GLvoid *pointer)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core22glVertexAttribLPointerEjijiPKv(
    QOpenGLFunctions_4_2_Core *self,
    GLuint index,
    GLint size,
    GLenum type,
    GLsizei stride,
    const GLvoid *pointer) {
  self->glVertexAttribLPointer(index, size, type, stride, pointer);
}

//  void QOpenGLFunctions_4_2_Core::glVertexAttribL4dv(GLuint index, const
//      GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core18glVertexAttribL4dvEjPKd(
    QOpenGLFunctions_4_2_Core *self,
    GLuint index,
    const GLdouble *v) {
  self->glVertexAttribL4dv(index, v);
}

//  void QOpenGLFunctions_4_2_Core::glVertexAttribL3dv(GLuint index, const
//      GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core18glVertexAttribL3dvEjPKd(
    QOpenGLFunctions_4_2_Core *self,
    GLuint index,
    const GLdouble *v) {
  self->glVertexAttribL3dv(index, v);
}

//  void QOpenGLFunctions_4_2_Core::glVertexAttribL2dv(GLuint index, const
//      GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core18glVertexAttribL2dvEjPKd(
    QOpenGLFunctions_4_2_Core *self,
    GLuint index,
    const GLdouble *v) {
  self->glVertexAttribL2dv(index, v);
}

//  void QOpenGLFunctions_4_2_Core::glVertexAttribL1dv(GLuint index, const
//      GLdouble *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core18glVertexAttribL1dvEjPKd(
    QOpenGLFunctions_4_2_Core *self,
    GLuint index,
    const GLdouble *v) {
  self->glVertexAttribL1dv(index, v);
}

//  void QOpenGLFunctions_4_2_Core::glVertexAttribL4d(GLuint index, GLdouble
//      x, GLdouble y, GLdouble z, GLdouble w)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core17glVertexAttribL4dEjdddd(
    QOpenGLFunctions_4_2_Core *self,
    GLuint index,
    GLdouble x,
    GLdouble y,
    GLdouble z,
    GLdouble w) {
  self->glVertexAttribL4d(index, x, y, z, w);
}

//  void QOpenGLFunctions_4_2_Core::glVertexAttribL3d(GLuint index, GLdouble
//      x, GLdouble y, GLdouble z)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core17glVertexAttribL3dEjddd(
    QOpenGLFunctions_4_2_Core *self,
    GLuint index,
    GLdouble x,
    GLdouble y,
    GLdouble z) {
  self->glVertexAttribL3d(index, x, y, z);
}

//  void QOpenGLFunctions_4_2_Core::glVertexAttribL2d(GLuint index, GLdouble
//      x, GLdouble y)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core17glVertexAttribL2dEjdd(
    QOpenGLFunctions_4_2_Core *self,
    GLuint index,
    GLdouble x,
    GLdouble y) {
  self->glVertexAttribL2d(index, x, y);
}

//  void QOpenGLFunctions_4_2_Core::glVertexAttribL1d(GLuint index, GLdouble
//      x)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core17glVertexAttribL1dEjd(
    QOpenGLFunctions_4_2_Core *self,
    GLuint index,
    GLdouble x) {
  self->glVertexAttribL1d(index, x);
}

//  void QOpenGLFunctions_4_2_Core::glGetProgramPipelineInfoLog(GLuint
//      pipeline, GLsizei bufSize, GLsizei *length, GLchar *infoLog)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core27glGetProgramPipelineInfoLogEjiPiPc(
    QOpenGLFunctions_4_2_Core *self,
    GLuint pipeline,
    GLsizei bufSize,
    GLsizei *length,
    GLchar *infoLog) {
  self->glGetProgramPipelineInfoLog(pipeline, bufSize, length, infoLog);
}

//  void QOpenGLFunctions_4_2_Core::glValidateProgramPipeline(GLuint
//      pipeline)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core25glValidateProgramPipelineEj(
    QOpenGLFunctions_4_2_Core *self,
    GLuint pipeline) {
  self->glValidateProgramPipeline(pipeline);
}

//  void QOpenGLFunctions_4_2_Core::glProgramUniformMatrix4x3dv(GLuint
//      program, GLint location, GLsizei count, GLboolean transpose, const
//      GLdouble *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core27glProgramUniformMatrix4x3dvEjiihPKd(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLdouble *value) {
  self->glProgramUniformMatrix4x3dv(
      program,
      location,
      count,
      transpose,
      value);
}

//  void QOpenGLFunctions_4_2_Core::glProgramUniformMatrix3x4dv(GLuint
//      program, GLint location, GLsizei count, GLboolean transpose, const
//      GLdouble *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core27glProgramUniformMatrix3x4dvEjiihPKd(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLdouble *value) {
  self->glProgramUniformMatrix3x4dv(
      program,
      location,
      count,
      transpose,
      value);
}

//  void QOpenGLFunctions_4_2_Core::glProgramUniformMatrix4x2dv(GLuint
//      program, GLint location, GLsizei count, GLboolean transpose, const
//      GLdouble *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core27glProgramUniformMatrix4x2dvEjiihPKd(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLdouble *value) {
  self->glProgramUniformMatrix4x2dv(
      program,
      location,
      count,
      transpose,
      value);
}

//  void QOpenGLFunctions_4_2_Core::glProgramUniformMatrix2x4dv(GLuint
//      program, GLint location, GLsizei count, GLboolean transpose, const
//      GLdouble *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core27glProgramUniformMatrix2x4dvEjiihPKd(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLdouble *value) {
  self->glProgramUniformMatrix2x4dv(
      program,
      location,
      count,
      transpose,
      value);
}

//  void QOpenGLFunctions_4_2_Core::glProgramUniformMatrix3x2dv(GLuint
//      program, GLint location, GLsizei count, GLboolean transpose, const
//      GLdouble *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core27glProgramUniformMatrix3x2dvEjiihPKd(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLdouble *value) {
  self->glProgramUniformMatrix3x2dv(
      program,
      location,
      count,
      transpose,
      value);
}

//  void QOpenGLFunctions_4_2_Core::glProgramUniformMatrix2x3dv(GLuint
//      program, GLint location, GLsizei count, GLboolean transpose, const
//      GLdouble *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core27glProgramUniformMatrix2x3dvEjiihPKd(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLdouble *value) {
  self->glProgramUniformMatrix2x3dv(
      program,
      location,
      count,
      transpose,
      value);
}

//  void QOpenGLFunctions_4_2_Core::glProgramUniformMatrix4x3fv(GLuint
//      program, GLint location, GLsizei count, GLboolean transpose, const
//      GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core27glProgramUniformMatrix4x3fvEjiihPKf(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLfloat *value) {
  self->glProgramUniformMatrix4x3fv(
      program,
      location,
      count,
      transpose,
      value);
}

//  void QOpenGLFunctions_4_2_Core::glProgramUniformMatrix3x4fv(GLuint
//      program, GLint location, GLsizei count, GLboolean transpose, const
//      GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core27glProgramUniformMatrix3x4fvEjiihPKf(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLfloat *value) {
  self->glProgramUniformMatrix3x4fv(
      program,
      location,
      count,
      transpose,
      value);
}

//  void QOpenGLFunctions_4_2_Core::glProgramUniformMatrix4x2fv(GLuint
//      program, GLint location, GLsizei count, GLboolean transpose, const
//      GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core27glProgramUniformMatrix4x2fvEjiihPKf(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLfloat *value) {
  self->glProgramUniformMatrix4x2fv(
      program,
      location,
      count,
      transpose,
      value);
}

//  void QOpenGLFunctions_4_2_Core::glProgramUniformMatrix2x4fv(GLuint
//      program, GLint location, GLsizei count, GLboolean transpose, const
//      GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core27glProgramUniformMatrix2x4fvEjiihPKf(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLfloat *value) {
  self->glProgramUniformMatrix2x4fv(
      program,
      location,
      count,
      transpose,
      value);
}

//  void QOpenGLFunctions_4_2_Core::glProgramUniformMatrix3x2fv(GLuint
//      program, GLint location, GLsizei count, GLboolean transpose, const
//      GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core27glProgramUniformMatrix3x2fvEjiihPKf(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLfloat *value) {
  self->glProgramUniformMatrix3x2fv(
      program,
      location,
      count,
      transpose,
      value);
}

//  void QOpenGLFunctions_4_2_Core::glProgramUniformMatrix2x3fv(GLuint
//      program, GLint location, GLsizei count, GLboolean transpose, const
//      GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core27glProgramUniformMatrix2x3fvEjiihPKf(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLfloat *value) {
  self->glProgramUniformMatrix2x3fv(
      program,
      location,
      count,
      transpose,
      value);
}

//  void QOpenGLFunctions_4_2_Core::glProgramUniformMatrix4dv(GLuint program,
//      GLint location, GLsizei count, GLboolean transpose, const GLdouble
//      *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core25glProgramUniformMatrix4dvEjiihPKd(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLdouble *value) {
  self->glProgramUniformMatrix4dv(
      program,
      location,
      count,
      transpose,
      value);
}

//  void QOpenGLFunctions_4_2_Core::glProgramUniformMatrix3dv(GLuint program,
//      GLint location, GLsizei count, GLboolean transpose, const GLdouble
//      *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core25glProgramUniformMatrix3dvEjiihPKd(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLdouble *value) {
  self->glProgramUniformMatrix3dv(
      program,
      location,
      count,
      transpose,
      value);
}

//  void QOpenGLFunctions_4_2_Core::glProgramUniformMatrix2dv(GLuint program,
//      GLint location, GLsizei count, GLboolean transpose, const GLdouble
//      *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core25glProgramUniformMatrix2dvEjiihPKd(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLdouble *value) {
  self->glProgramUniformMatrix2dv(
      program,
      location,
      count,
      transpose,
      value);
}

//  void QOpenGLFunctions_4_2_Core::glProgramUniformMatrix4fv(GLuint program,
//      GLint location, GLsizei count, GLboolean transpose, const GLfloat
//      *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core25glProgramUniformMatrix4fvEjiihPKf(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLfloat *value) {
  self->glProgramUniformMatrix4fv(
      program,
      location,
      count,
      transpose,
      value);
}

//  void QOpenGLFunctions_4_2_Core::glProgramUniformMatrix3fv(GLuint program,
//      GLint location, GLsizei count, GLboolean transpose, const GLfloat
//      *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core25glProgramUniformMatrix3fvEjiihPKf(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLfloat *value) {
  self->glProgramUniformMatrix3fv(
      program,
      location,
      count,
      transpose,
      value);
}

//  void QOpenGLFunctions_4_2_Core::glProgramUniformMatrix2fv(GLuint program,
//      GLint location, GLsizei count, GLboolean transpose, const GLfloat
//      *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core25glProgramUniformMatrix2fvEjiihPKf(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLfloat *value) {
  self->glProgramUniformMatrix2fv(
      program,
      location,
      count,
      transpose,
      value);
}

//  void QOpenGLFunctions_4_2_Core::glProgramUniform4uiv(GLuint program,
//      GLint location, GLsizei count, const GLuint *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core20glProgramUniform4uivEjiiPKj(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLint location,
    GLsizei count,
    const GLuint *value) {
  self->glProgramUniform4uiv(program, location, count, value);
}

//  void QOpenGLFunctions_4_2_Core::glProgramUniform4ui(GLuint program, GLint
//      location, GLuint v0, GLuint v1, GLuint v2, GLuint v3)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core19glProgramUniform4uiEjijjjj(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLint location,
    GLuint v0,
    GLuint v1,
    GLuint v2,
    GLuint v3) {
  self->glProgramUniform4ui(program, location, v0, v1, v2, v3);
}

//  void QOpenGLFunctions_4_2_Core::glProgramUniform4dv(GLuint program, GLint
//      location, GLsizei count, const GLdouble *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core19glProgramUniform4dvEjiiPKd(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLint location,
    GLsizei count,
    const GLdouble *value) {
  self->glProgramUniform4dv(program, location, count, value);
}

//  void QOpenGLFunctions_4_2_Core::glProgramUniform4d(GLuint program, GLint
//      location, GLdouble v0, GLdouble v1, GLdouble v2, GLdouble v3)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core18glProgramUniform4dEjidddd(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLint location,
    GLdouble v0,
    GLdouble v1,
    GLdouble v2,
    GLdouble v3) {
  self->glProgramUniform4d(program, location, v0, v1, v2, v3);
}

//  void QOpenGLFunctions_4_2_Core::glProgramUniform4fv(GLuint program, GLint
//      location, GLsizei count, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core19glProgramUniform4fvEjiiPKf(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLint location,
    GLsizei count,
    const GLfloat *value) {
  self->glProgramUniform4fv(program, location, count, value);
}

//  void QOpenGLFunctions_4_2_Core::glProgramUniform4f(GLuint program, GLint
//      location, GLfloat v0, GLfloat v1, GLfloat v2, GLfloat v3)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core18glProgramUniform4fEjiffff(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLint location,
    GLfloat v0,
    GLfloat v1,
    GLfloat v2,
    GLfloat v3) {
  self->glProgramUniform4f(program, location, v0, v1, v2, v3);
}

//  void QOpenGLFunctions_4_2_Core::glProgramUniform4iv(GLuint program, GLint
//      location, GLsizei count, const GLint *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core19glProgramUniform4ivEjiiPKi(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLint location,
    GLsizei count,
    const GLint *value) {
  self->glProgramUniform4iv(program, location, count, value);
}

//  void QOpenGLFunctions_4_2_Core::glProgramUniform4i(GLuint program, GLint
//      location, GLint v0, GLint v1, GLint v2, GLint v3)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core18glProgramUniform4iEjiiiii(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLint location,
    GLint v0,
    GLint v1,
    GLint v2,
    GLint v3) {
  self->glProgramUniform4i(program, location, v0, v1, v2, v3);
}

//  void QOpenGLFunctions_4_2_Core::glProgramUniform3uiv(GLuint program,
//      GLint location, GLsizei count, const GLuint *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core20glProgramUniform3uivEjiiPKj(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLint location,
    GLsizei count,
    const GLuint *value) {
  self->glProgramUniform3uiv(program, location, count, value);
}

//  void QOpenGLFunctions_4_2_Core::glProgramUniform3ui(GLuint program, GLint
//      location, GLuint v0, GLuint v1, GLuint v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core19glProgramUniform3uiEjijjj(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLint location,
    GLuint v0,
    GLuint v1,
    GLuint v2) {
  self->glProgramUniform3ui(program, location, v0, v1, v2);
}

//  void QOpenGLFunctions_4_2_Core::glProgramUniform3dv(GLuint program, GLint
//      location, GLsizei count, const GLdouble *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core19glProgramUniform3dvEjiiPKd(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLint location,
    GLsizei count,
    const GLdouble *value) {
  self->glProgramUniform3dv(program, location, count, value);
}

//  void QOpenGLFunctions_4_2_Core::glProgramUniform3d(GLuint program, GLint
//      location, GLdouble v0, GLdouble v1, GLdouble v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core18glProgramUniform3dEjiddd(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLint location,
    GLdouble v0,
    GLdouble v1,
    GLdouble v2) {
  self->glProgramUniform3d(program, location, v0, v1, v2);
}

//  void QOpenGLFunctions_4_2_Core::glProgramUniform3fv(GLuint program, GLint
//      location, GLsizei count, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core19glProgramUniform3fvEjiiPKf(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLint location,
    GLsizei count,
    const GLfloat *value) {
  self->glProgramUniform3fv(program, location, count, value);
}

//  void QOpenGLFunctions_4_2_Core::glProgramUniform3f(GLuint program, GLint
//      location, GLfloat v0, GLfloat v1, GLfloat v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core18glProgramUniform3fEjifff(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLint location,
    GLfloat v0,
    GLfloat v1,
    GLfloat v2) {
  self->glProgramUniform3f(program, location, v0, v1, v2);
}

//  void QOpenGLFunctions_4_2_Core::glProgramUniform3iv(GLuint program, GLint
//      location, GLsizei count, const GLint *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core19glProgramUniform3ivEjiiPKi(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLint location,
    GLsizei count,
    const GLint *value) {
  self->glProgramUniform3iv(program, location, count, value);
}

//  void QOpenGLFunctions_4_2_Core::glProgramUniform3i(GLuint program, GLint
//      location, GLint v0, GLint v1, GLint v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core18glProgramUniform3iEjiiii(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLint location,
    GLint v0,
    GLint v1,
    GLint v2) {
  self->glProgramUniform3i(program, location, v0, v1, v2);
}

//  void QOpenGLFunctions_4_2_Core::glProgramUniform2uiv(GLuint program,
//      GLint location, GLsizei count, const GLuint *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core20glProgramUniform2uivEjiiPKj(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLint location,
    GLsizei count,
    const GLuint *value) {
  self->glProgramUniform2uiv(program, location, count, value);
}

//  void QOpenGLFunctions_4_2_Core::glProgramUniform2ui(GLuint program, GLint
//      location, GLuint v0, GLuint v1)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core19glProgramUniform2uiEjijj(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLint location,
    GLuint v0,
    GLuint v1) {
  self->glProgramUniform2ui(program, location, v0, v1);
}

//  void QOpenGLFunctions_4_2_Core::glProgramUniform2dv(GLuint program, GLint
//      location, GLsizei count, const GLdouble *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core19glProgramUniform2dvEjiiPKd(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLint location,
    GLsizei count,
    const GLdouble *value) {
  self->glProgramUniform2dv(program, location, count, value);
}

//  void QOpenGLFunctions_4_2_Core::glProgramUniform2d(GLuint program, GLint
//      location, GLdouble v0, GLdouble v1)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core18glProgramUniform2dEjidd(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLint location,
    GLdouble v0,
    GLdouble v1) {
  self->glProgramUniform2d(program, location, v0, v1);
}

//  void QOpenGLFunctions_4_2_Core::glProgramUniform2fv(GLuint program, GLint
//      location, GLsizei count, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core19glProgramUniform2fvEjiiPKf(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLint location,
    GLsizei count,
    const GLfloat *value) {
  self->glProgramUniform2fv(program, location, count, value);
}

//  void QOpenGLFunctions_4_2_Core::glProgramUniform2f(GLuint program, GLint
//      location, GLfloat v0, GLfloat v1)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core18glProgramUniform2fEjiff(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLint location,
    GLfloat v0,
    GLfloat v1) {
  self->glProgramUniform2f(program, location, v0, v1);
}

//  void QOpenGLFunctions_4_2_Core::glProgramUniform2iv(GLuint program, GLint
//      location, GLsizei count, const GLint *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core19glProgramUniform2ivEjiiPKi(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLint location,
    GLsizei count,
    const GLint *value) {
  self->glProgramUniform2iv(program, location, count, value);
}

//  void QOpenGLFunctions_4_2_Core::glProgramUniform2i(GLuint program, GLint
//      location, GLint v0, GLint v1)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core18glProgramUniform2iEjiii(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLint location,
    GLint v0,
    GLint v1) {
  self->glProgramUniform2i(program, location, v0, v1);
}

//  void QOpenGLFunctions_4_2_Core::glProgramUniform1uiv(GLuint program,
//      GLint location, GLsizei count, const GLuint *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core20glProgramUniform1uivEjiiPKj(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLint location,
    GLsizei count,
    const GLuint *value) {
  self->glProgramUniform1uiv(program, location, count, value);
}

//  void QOpenGLFunctions_4_2_Core::glProgramUniform1ui(GLuint program, GLint
//      location, GLuint v0)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core19glProgramUniform1uiEjij(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLint location,
    GLuint v0) {
  self->glProgramUniform1ui(program, location, v0);
}

//  void QOpenGLFunctions_4_2_Core::glProgramUniform1dv(GLuint program, GLint
//      location, GLsizei count, const GLdouble *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core19glProgramUniform1dvEjiiPKd(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLint location,
    GLsizei count,
    const GLdouble *value) {
  self->glProgramUniform1dv(program, location, count, value);
}

//  void QOpenGLFunctions_4_2_Core::glProgramUniform1d(GLuint program, GLint
//      location, GLdouble v0)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core18glProgramUniform1dEjid(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLint location,
    GLdouble v0) {
  self->glProgramUniform1d(program, location, v0);
}

//  void QOpenGLFunctions_4_2_Core::glProgramUniform1fv(GLuint program, GLint
//      location, GLsizei count, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core19glProgramUniform1fvEjiiPKf(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLint location,
    GLsizei count,
    const GLfloat *value) {
  self->glProgramUniform1fv(program, location, count, value);
}

//  void QOpenGLFunctions_4_2_Core::glProgramUniform1f(GLuint program, GLint
//      location, GLfloat v0)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core18glProgramUniform1fEjif(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLint location,
    GLfloat v0) {
  self->glProgramUniform1f(program, location, v0);
}

//  void QOpenGLFunctions_4_2_Core::glProgramUniform1iv(GLuint program, GLint
//      location, GLsizei count, const GLint *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core19glProgramUniform1ivEjiiPKi(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLint location,
    GLsizei count,
    const GLint *value) {
  self->glProgramUniform1iv(program, location, count, value);
}

//  void QOpenGLFunctions_4_2_Core::glProgramUniform1i(GLuint program, GLint
//      location, GLint v0)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core18glProgramUniform1iEjii(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLint location,
    GLint v0) {
  self->glProgramUniform1i(program, location, v0);
}

//  void QOpenGLFunctions_4_2_Core::glGetProgramPipelineiv(GLuint pipeline,
//      GLenum pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core22glGetProgramPipelineivEjjPi(
    QOpenGLFunctions_4_2_Core *self,
    GLuint pipeline,
    GLenum pname,
    GLint *params) {
  self->glGetProgramPipelineiv(pipeline, pname, params);
}

//  GLboolean QOpenGLFunctions_4_2_Core::glIsProgramPipeline(GLuint pipeline)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN25QOpenGLFunctions_4_2_Core19glIsProgramPipelineEj(
    QOpenGLFunctions_4_2_Core *self,
    GLuint pipeline) {
  return self->glIsProgramPipeline(pipeline);
}

//  void QOpenGLFunctions_4_2_Core::glGenProgramPipelines(GLsizei n, GLuint
//      *pipelines)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core21glGenProgramPipelinesEiPj(
    QOpenGLFunctions_4_2_Core *self,
    GLsizei n,
    GLuint *pipelines) {
  self->glGenProgramPipelines(n, pipelines);
}

//  void QOpenGLFunctions_4_2_Core::glDeleteProgramPipelines(GLsizei n, const
//      GLuint *pipelines)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core24glDeleteProgramPipelinesEiPKj(
    QOpenGLFunctions_4_2_Core *self,
    GLsizei n,
    const GLuint *pipelines) {
  self->glDeleteProgramPipelines(n, pipelines);
}

//  void QOpenGLFunctions_4_2_Core::glBindProgramPipeline(GLuint pipeline)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core21glBindProgramPipelineEj(
    QOpenGLFunctions_4_2_Core *self,
    GLuint pipeline) {
  self->glBindProgramPipeline(pipeline);
}

//  GLuint QOpenGLFunctions_4_2_Core::glCreateShaderProgramv(GLenum type,
//      GLsizei count, const GLchar *const *strings)
extern "C" Q_DECL_EXPORT
GLuint ritual_ZN25QOpenGLFunctions_4_2_Core22glCreateShaderProgramvEjiPKPKc(
    QOpenGLFunctions_4_2_Core *self,
    GLenum type,
    GLsizei count,
    const GLchar *const *strings) {
  return self->glCreateShaderProgramv(type, count, strings);
}

//  void QOpenGLFunctions_4_2_Core::glActiveShaderProgram(GLuint pipeline,
//      GLuint program)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core21glActiveShaderProgramEjj(
    QOpenGLFunctions_4_2_Core *self,
    GLuint pipeline,
    GLuint program) {
  self->glActiveShaderProgram(pipeline, program);
}

//  void QOpenGLFunctions_4_2_Core::glUseProgramStages(GLuint pipeline,
//      GLbitfield stages, GLuint program)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core18glUseProgramStagesEjjj(
    QOpenGLFunctions_4_2_Core *self,
    GLuint pipeline,
    GLbitfield stages,
    GLuint program) {
  self->glUseProgramStages(pipeline, stages, program);
}

//  void QOpenGLFunctions_4_2_Core::glProgramParameteri(GLuint program,
//      GLenum pname, GLint value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core19glProgramParameteriEjji(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLenum pname,
    GLint value) {
  self->glProgramParameteri(program, pname, value);
}

//  void QOpenGLFunctions_4_2_Core::glProgramBinary(GLuint program, GLenum
//      binaryFormat, const GLvoid *binary, GLsizei length)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core15glProgramBinaryEjjPKvi(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLenum binaryFormat,
    const GLvoid *binary,
    GLsizei length) {
  self->glProgramBinary(program, binaryFormat, binary, length);
}

//  void QOpenGLFunctions_4_2_Core::glGetProgramBinary(GLuint program,
//      GLsizei bufSize, GLsizei *length, GLenum *binaryFormat, GLvoid
//      *binary)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core18glGetProgramBinaryEjiPiPjPv(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLsizei bufSize,
    GLsizei *length,
    GLenum *binaryFormat,
    GLvoid *binary) {
  self->glGetProgramBinary(program, bufSize, length, binaryFormat, binary);
}

//  void QOpenGLFunctions_4_2_Core::glClearDepthf(GLfloat dd)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core13glClearDepthfEf(
    QOpenGLFunctions_4_2_Core *self,
    GLfloat dd) {
  self->glClearDepthf(dd);
}

//  void QOpenGLFunctions_4_2_Core::glDepthRangef(GLfloat n, GLfloat f)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core13glDepthRangefEff(
    QOpenGLFunctions_4_2_Core *self,
    GLfloat n,
    GLfloat f) {
  self->glDepthRangef(n, f);
}

//  void QOpenGLFunctions_4_2_Core::glGetShaderPrecisionFormat(GLenum
//      shadertype, GLenum precisiontype, GLint *range, GLint *precision)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core26glGetShaderPrecisionFormatEjjPiS0_(
    QOpenGLFunctions_4_2_Core *self,
    GLenum shadertype,
    GLenum precisiontype,
    GLint *range,
    GLint *precision) {
  self->glGetShaderPrecisionFormat(
      shadertype,
      precisiontype,
      range,
      precision);
}

//  void QOpenGLFunctions_4_2_Core::glShaderBinary(GLsizei count, const
//      GLuint *shaders, GLenum binaryformat, const GLvoid *binary, GLsizei
//      length)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core14glShaderBinaryEiPKjjPKvi(
    QOpenGLFunctions_4_2_Core *self,
    GLsizei count,
    const GLuint *shaders,
    GLenum binaryformat,
    const GLvoid *binary,
    GLsizei length) {
  self->glShaderBinary(count, shaders, binaryformat, binary, length);
}

//  void QOpenGLFunctions_4_2_Core::glReleaseShaderCompiler()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core23glReleaseShaderCompilerEv(
    QOpenGLFunctions_4_2_Core *self) {
  self->glReleaseShaderCompiler();
}

//  void QOpenGLFunctions_4_2_Core::glTexStorage3D(GLenum target, GLsizei
//      levels, GLenum internalformat, GLsizei width, GLsizei height, GLsizei
//      depth)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core14glTexStorage3DEjijiii(
    QOpenGLFunctions_4_2_Core *self,
    GLenum target,
    GLsizei levels,
    GLenum internalformat,
    GLsizei width,
    GLsizei height,
    GLsizei depth) {
  self->glTexStorage3D(target, levels, internalformat, width, height, depth);
}

//  void QOpenGLFunctions_4_2_Core::glTexStorage2D(GLenum target, GLsizei
//      levels, GLenum internalformat, GLsizei width, GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core14glTexStorage2DEjijii(
    QOpenGLFunctions_4_2_Core *self,
    GLenum target,
    GLsizei levels,
    GLenum internalformat,
    GLsizei width,
    GLsizei height) {
  self->glTexStorage2D(target, levels, internalformat, width, height);
}

//  void QOpenGLFunctions_4_2_Core::glTexStorage1D(GLenum target, GLsizei
//      levels, GLenum internalformat, GLsizei width)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core14glTexStorage1DEjiji(
    QOpenGLFunctions_4_2_Core *self,
    GLenum target,
    GLsizei levels,
    GLenum internalformat,
    GLsizei width) {
  self->glTexStorage1D(target, levels, internalformat, width);
}

//  void QOpenGLFunctions_4_2_Core::glMemoryBarrier(GLbitfield barriers)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core15glMemoryBarrierEj(
    QOpenGLFunctions_4_2_Core *self,
    GLbitfield barriers) {
  self->glMemoryBarrier(barriers);
}

//  void QOpenGLFunctions_4_2_Core::glBindImageTexture(GLuint unit, GLuint
//      texture, GLint level, GLboolean layered, GLint layer, GLenum access,
//      GLenum format)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core18glBindImageTextureEjjihijj(
    QOpenGLFunctions_4_2_Core *self,
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

//  void QOpenGLFunctions_4_2_Core::glGetActiveAtomicCounterBufferiv(GLuint
//      program, GLuint bufferIndex, GLenum pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core32glGetActiveAtomicCounterBufferivEjjjPi(
    QOpenGLFunctions_4_2_Core *self,
    GLuint program,
    GLuint bufferIndex,
    GLenum pname,
    GLint *params) {
  self->glGetActiveAtomicCounterBufferiv(
      program,
      bufferIndex,
      pname,
      params);
}

//  void QOpenGLFunctions_4_2_Core::glGetInternalformativ(GLenum target,
//      GLenum internalformat, GLenum pname, GLsizei bufSize, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core21glGetInternalformativEjjjiPi(
    QOpenGLFunctions_4_2_Core *self,
    GLenum target,
    GLenum internalformat,
    GLenum pname,
    GLsizei bufSize,
    GLint *params) {
  self->glGetInternalformativ(
      target,
      internalformat,
      pname,
      bufSize,
      params);
}

//  void
//      QOpenGLFunctions_4_2_Core::glDrawTransformFeedbackStreamInstanced(GLe
//      num mode, GLuint id, GLuint stream, GLsizei instancecount)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core38glDrawTransformFeedbackStreamInstancedEjjji(
    QOpenGLFunctions_4_2_Core *self,
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

//  void QOpenGLFunctions_4_2_Core::glDrawTransformFeedbackInstanced(GLenum
//      mode, GLuint id, GLsizei instancecount)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core32glDrawTransformFeedbackInstancedEjji(
    QOpenGLFunctions_4_2_Core *self,
    GLenum mode,
    GLuint id,
    GLsizei instancecount) {
  self->glDrawTransformFeedbackInstanced(mode, id, instancecount);
}

//  void QOpenGLFunctions_4_2_Core::glDrawElementsInstancedBaseVertexBaseInst
//      ance(GLenum mode, GLsizei count, GLenum type, const void *indices,
//      GLsizei instancecount, GLint basevertex, GLuint baseinstance)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core45glDrawElementsInstancedBaseVertexBaseInstanceEjijPKviij(
    QOpenGLFunctions_4_2_Core *self,
    GLenum mode,
    GLsizei count,
    GLenum type,
    const void *indices,
    GLsizei instancecount,
    GLint basevertex,
    GLuint baseinstance) {
  self->glDrawElementsInstancedBaseVertexBaseInstance(
      mode,
      count,
      type,
      indices,
      instancecount,
      basevertex,
      baseinstance);
}

//  void
//      QOpenGLFunctions_4_2_Core::glDrawElementsInstancedBaseInstance(GLenum
//      mode, GLsizei count, GLenum type, const void *indices, GLsizei
//      instancecount, GLuint baseinstance)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core35glDrawElementsInstancedBaseInstanceEjijPKvij(
    QOpenGLFunctions_4_2_Core *self,
    GLenum mode,
    GLsizei count,
    GLenum type,
    const void *indices,
    GLsizei instancecount,
    GLuint baseinstance) {
  self->glDrawElementsInstancedBaseInstance(
      mode,
      count,
      type,
      indices,
      instancecount,
      baseinstance);
}

//  void QOpenGLFunctions_4_2_Core::glDrawArraysInstancedBaseInstance(GLenum
//      mode, GLint first, GLsizei count, GLsizei instancecount, GLuint
//      baseinstance)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLFunctions_4_2_Core33glDrawArraysInstancedBaseInstanceEjiiij(
    QOpenGLFunctions_4_2_Core *self,
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

//  bool QOpenGLFunctions_4_2_Core::isContextCompatible(QOpenGLContext
//      *context)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QOpenGLFunctions_4_2_Core19isContextCompatibleEP14QOpenGLContext(
    QOpenGLContext *context) {
  return QOpenGLFunctions_4_2_Core::isContextCompatible(context);
}

//  QOpenGLVersionProfile QOpenGLFunctions_4_2_Core::versionProfile()
extern "C" Q_DECL_EXPORT
QOpenGLVersionProfile *ritual_ZN25QOpenGLFunctions_4_2_Core14versionProfileEv() {
  return new QOpenGLVersionProfile(
      QOpenGLFunctions_4_2_Core::versionProfile());
}

//  a Python function taken by a CuteQOpenGLFunctions_4_2_Core, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QOpenGLFunctions_4_2_Core(
    QOpenGLFunctions_4_2_Core *self,
    const char *key,
    void *call) {
  return static_cast<CuteQOpenGLFunctions_4_2_Core *>(self)->take(key, call);
}

//  bool QOpenGLFunctions_4_2_Core::initializeOpenGLFunctions()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN25QOpenGLFunctions_4_2_Core25initializeOpenGLFunctionsEv(
    QOpenGLFunctions_4_2_Core *self) {
  return self->QOpenGLFunctions_4_2_Core::initializeOpenGLFunctions();
}

#endif  // !defined(QT_NO_OPENGL) && !QT_CONFIG(opengles2)
#endif  // !QT_CONFIG(opengles2)
