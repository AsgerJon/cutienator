//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qopenglfunctions.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#if !defined(QT_NO_OPENGL)
#include <QtGui/qopenglfunctions.h>

//  QOpenGLFunctions::QOpenGLFunctions()
extern "C" Q_DECL_EXPORT
QOpenGLFunctions *ritual_ZN16QOpenGLFunctionsC1Ev() {
  return new QOpenGLFunctions();
}

//  QOpenGLFunctions::QOpenGLFunctions(QOpenGLContext *context)
extern "C" Q_DECL_EXPORT
QOpenGLFunctions *ritual_ZN16QOpenGLFunctionsC1EP14QOpenGLContext(
    QOpenGLContext *context) {
  return new QOpenGLFunctions(context);
}

//  QOpenGLFunctions::~QOpenGLFunctions()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctionsD1Ev(QOpenGLFunctions *self) {
  delete self;
}

//  QOpenGLFunctions::OpenGLFeatures QOpenGLFunctions::openGLFeatures() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QOpenGLFunctions14openGLFeaturesEv(
    const QOpenGLFunctions *self) {
  return static_cast<int>(self->openGLFeatures().toInt());
}

//  bool QOpenGLFunctions::hasOpenGLFeature(QOpenGLFunctions::OpenGLFeature
//      feature) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QOpenGLFunctions16hasOpenGLFeatureENS_13OpenGLFeatureE(
    const QOpenGLFunctions *self,
    QOpenGLFunctions::OpenGLFeature feature) {
  return self->hasOpenGLFeature(feature);
}

//  void QOpenGLFunctions::initializeOpenGLFunctions()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions25initializeOpenGLFunctionsEv(
    QOpenGLFunctions *self) {
  self->initializeOpenGLFunctions();
}

//  void QOpenGLFunctions::glBindTexture(GLenum target, GLuint texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions13glBindTextureEjj(
    QOpenGLFunctions *self,
    GLenum target,
    GLuint texture) {
  self->glBindTexture(target, texture);
}

//  void QOpenGLFunctions::glBlendFunc(GLenum sfactor, GLenum dfactor)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions11glBlendFuncEjj(
    QOpenGLFunctions *self,
    GLenum sfactor,
    GLenum dfactor) {
  self->glBlendFunc(sfactor, dfactor);
}

//  void QOpenGLFunctions::glClear(GLbitfield mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions7glClearEj(
    QOpenGLFunctions *self,
    GLbitfield mask) {
  self->glClear(mask);
}

//  void QOpenGLFunctions::glClearColor(GLclampf red, GLclampf green,
//      GLclampf blue, GLclampf alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions12glClearColorEffff(
    QOpenGLFunctions *self,
    GLclampf red,
    GLclampf green,
    GLclampf blue,
    GLclampf alpha) {
  self->glClearColor(red, green, blue, alpha);
}

//  void QOpenGLFunctions::glClearStencil(GLint s)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions14glClearStencilEi(
    QOpenGLFunctions *self,
    GLint s) {
  self->glClearStencil(s);
}

//  void QOpenGLFunctions::glColorMask(GLboolean red, GLboolean green,
//      GLboolean blue, GLboolean alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions11glColorMaskEhhhh(
    QOpenGLFunctions *self,
    GLboolean red,
    GLboolean green,
    GLboolean blue,
    GLboolean alpha) {
  self->glColorMask(red, green, blue, alpha);
}

//  void QOpenGLFunctions::glCopyTexImage2D(GLenum target, GLint level,
//      GLenum internalformat, GLint x, GLint y, GLsizei width, GLsizei
//      height, GLint border)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions16glCopyTexImage2DEjijiiiii(
    QOpenGLFunctions *self,
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

//  void QOpenGLFunctions::glCopyTexSubImage2D(GLenum target, GLint level,
//      GLint xoffset, GLint yoffset, GLint x, GLint y, GLsizei width,
//      GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions19glCopyTexSubImage2DEjiiiiiii(
    QOpenGLFunctions *self,
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

//  void QOpenGLFunctions::glCullFace(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions10glCullFaceEj(
    QOpenGLFunctions *self,
    GLenum mode) {
  self->glCullFace(mode);
}

//  void QOpenGLFunctions::glDeleteTextures(GLsizei n, const GLuint
//      *textures)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions16glDeleteTexturesEiPKj(
    QOpenGLFunctions *self,
    GLsizei n,
    const GLuint *textures) {
  self->glDeleteTextures(n, textures);
}

//  void QOpenGLFunctions::glDepthFunc(GLenum func)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions11glDepthFuncEj(
    QOpenGLFunctions *self,
    GLenum func) {
  self->glDepthFunc(func);
}

//  void QOpenGLFunctions::glDepthMask(GLboolean flag)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions11glDepthMaskEh(
    QOpenGLFunctions *self,
    GLboolean flag) {
  self->glDepthMask(flag);
}

//  void QOpenGLFunctions::glDisable(GLenum cap)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions9glDisableEj(
    QOpenGLFunctions *self,
    GLenum cap) {
  self->glDisable(cap);
}

//  void QOpenGLFunctions::glDrawArrays(GLenum mode, GLint first, GLsizei
//      count)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions12glDrawArraysEjii(
    QOpenGLFunctions *self,
    GLenum mode,
    GLint first,
    GLsizei count) {
  self->glDrawArrays(mode, first, count);
}

//  void QOpenGLFunctions::glDrawElements(GLenum mode, GLsizei count, GLenum
//      type, const GLvoid *indices)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions14glDrawElementsEjijPKv(
    QOpenGLFunctions *self,
    GLenum mode,
    GLsizei count,
    GLenum type,
    const GLvoid *indices) {
  self->glDrawElements(mode, count, type, indices);
}

//  void QOpenGLFunctions::glEnable(GLenum cap)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions8glEnableEj(
    QOpenGLFunctions *self,
    GLenum cap) {
  self->glEnable(cap);
}

//  void QOpenGLFunctions::glFinish()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions8glFinishEv(QOpenGLFunctions *self) {
  self->glFinish();
}

//  void QOpenGLFunctions::glFlush()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions7glFlushEv(QOpenGLFunctions *self) {
  self->glFlush();
}

//  void QOpenGLFunctions::glFrontFace(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions11glFrontFaceEj(
    QOpenGLFunctions *self,
    GLenum mode) {
  self->glFrontFace(mode);
}

//  void QOpenGLFunctions::glGenTextures(GLsizei n, GLuint *textures)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions13glGenTexturesEiPj(
    QOpenGLFunctions *self,
    GLsizei n,
    GLuint *textures) {
  self->glGenTextures(n, textures);
}

//  void QOpenGLFunctions::glGetBooleanv(GLenum pname, GLboolean *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions13glGetBooleanvEjPh(
    QOpenGLFunctions *self,
    GLenum pname,
    GLboolean *params) {
  self->glGetBooleanv(pname, params);
}

//  GLenum QOpenGLFunctions::glGetError()
extern "C" Q_DECL_EXPORT
GLenum ritual_ZN16QOpenGLFunctions10glGetErrorEv(QOpenGLFunctions *self) {
  return self->glGetError();
}

//  void QOpenGLFunctions::glGetFloatv(GLenum pname, GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions11glGetFloatvEjPf(
    QOpenGLFunctions *self,
    GLenum pname,
    GLfloat *params) {
  self->glGetFloatv(pname, params);
}

//  void QOpenGLFunctions::glGetIntegerv(GLenum pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions13glGetIntegervEjPi(
    QOpenGLFunctions *self,
    GLenum pname,
    GLint *params) {
  self->glGetIntegerv(pname, params);
}

//  const GLubyte *QOpenGLFunctions::glGetString(GLenum name)
extern "C" Q_DECL_EXPORT
const GLubyte *ritual_ZN16QOpenGLFunctions11glGetStringEj(
    QOpenGLFunctions *self,
    GLenum name) {
  return self->glGetString(name);
}

//  void QOpenGLFunctions::glGetTexParameterfv(GLenum target, GLenum pname,
//      GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions19glGetTexParameterfvEjjPf(
    QOpenGLFunctions *self,
    GLenum target,
    GLenum pname,
    GLfloat *params) {
  self->glGetTexParameterfv(target, pname, params);
}

//  void QOpenGLFunctions::glGetTexParameteriv(GLenum target, GLenum pname,
//      GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions19glGetTexParameterivEjjPi(
    QOpenGLFunctions *self,
    GLenum target,
    GLenum pname,
    GLint *params) {
  self->glGetTexParameteriv(target, pname, params);
}

//  void QOpenGLFunctions::glHint(GLenum target, GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions6glHintEjj(
    QOpenGLFunctions *self,
    GLenum target,
    GLenum mode) {
  self->glHint(target, mode);
}

//  GLboolean QOpenGLFunctions::glIsEnabled(GLenum cap)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN16QOpenGLFunctions11glIsEnabledEj(
    QOpenGLFunctions *self,
    GLenum cap) {
  return self->glIsEnabled(cap);
}

//  GLboolean QOpenGLFunctions::glIsTexture(GLuint texture)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN16QOpenGLFunctions11glIsTextureEj(
    QOpenGLFunctions *self,
    GLuint texture) {
  return self->glIsTexture(texture);
}

//  void QOpenGLFunctions::glLineWidth(GLfloat width)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions11glLineWidthEf(
    QOpenGLFunctions *self,
    GLfloat width) {
  self->glLineWidth(width);
}

//  void QOpenGLFunctions::glPixelStorei(GLenum pname, GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions13glPixelStoreiEji(
    QOpenGLFunctions *self,
    GLenum pname,
    GLint param) {
  self->glPixelStorei(pname, param);
}

//  void QOpenGLFunctions::glPolygonOffset(GLfloat factor, GLfloat units)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions15glPolygonOffsetEff(
    QOpenGLFunctions *self,
    GLfloat factor,
    GLfloat units) {
  self->glPolygonOffset(factor, units);
}

//  void QOpenGLFunctions::glReadPixels(GLint x, GLint y, GLsizei width,
//      GLsizei height, GLenum format, GLenum type, GLvoid *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions12glReadPixelsEiiiijjPv(
    QOpenGLFunctions *self,
    GLint x,
    GLint y,
    GLsizei width,
    GLsizei height,
    GLenum format,
    GLenum type,
    GLvoid *pixels) {
  self->glReadPixels(x, y, width, height, format, type, pixels);
}

//  void QOpenGLFunctions::glScissor(GLint x, GLint y, GLsizei width, GLsizei
//      height)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions9glScissorEiiii(
    QOpenGLFunctions *self,
    GLint x,
    GLint y,
    GLsizei width,
    GLsizei height) {
  self->glScissor(x, y, width, height);
}

//  void QOpenGLFunctions::glStencilFunc(GLenum func, GLint ref, GLuint mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions13glStencilFuncEjij(
    QOpenGLFunctions *self,
    GLenum func,
    GLint ref,
    GLuint mask) {
  self->glStencilFunc(func, ref, mask);
}

//  void QOpenGLFunctions::glStencilMask(GLuint mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions13glStencilMaskEj(
    QOpenGLFunctions *self,
    GLuint mask) {
  self->glStencilMask(mask);
}

//  void QOpenGLFunctions::glStencilOp(GLenum fail, GLenum zfail, GLenum
//      zpass)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions11glStencilOpEjjj(
    QOpenGLFunctions *self,
    GLenum fail,
    GLenum zfail,
    GLenum zpass) {
  self->glStencilOp(fail, zfail, zpass);
}

//  void QOpenGLFunctions::glTexImage2D(GLenum target, GLint level, GLint
//      internalformat, GLsizei width, GLsizei height, GLint border, GLenum
//      format, GLenum type, const GLvoid *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions12glTexImage2DEjiiiiijjPKv(
    QOpenGLFunctions *self,
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

//  void QOpenGLFunctions::glTexParameterf(GLenum target, GLenum pname,
//      GLfloat param)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions15glTexParameterfEjjf(
    QOpenGLFunctions *self,
    GLenum target,
    GLenum pname,
    GLfloat param) {
  self->glTexParameterf(target, pname, param);
}

//  void QOpenGLFunctions::glTexParameterfv(GLenum target, GLenum pname,
//      const GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions16glTexParameterfvEjjPKf(
    QOpenGLFunctions *self,
    GLenum target,
    GLenum pname,
    const GLfloat *params) {
  self->glTexParameterfv(target, pname, params);
}

//  void QOpenGLFunctions::glTexParameteri(GLenum target, GLenum pname, GLint
//      param)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions15glTexParameteriEjji(
    QOpenGLFunctions *self,
    GLenum target,
    GLenum pname,
    GLint param) {
  self->glTexParameteri(target, pname, param);
}

//  void QOpenGLFunctions::glTexParameteriv(GLenum target, GLenum pname,
//      const GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions16glTexParameterivEjjPKi(
    QOpenGLFunctions *self,
    GLenum target,
    GLenum pname,
    const GLint *params) {
  self->glTexParameteriv(target, pname, params);
}

//  void QOpenGLFunctions::glTexSubImage2D(GLenum target, GLint level, GLint
//      xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format,
//      GLenum type, const GLvoid *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions15glTexSubImage2DEjiiiiijjPKv(
    QOpenGLFunctions *self,
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

//  void QOpenGLFunctions::glViewport(GLint x, GLint y, GLsizei width,
//      GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions10glViewportEiiii(
    QOpenGLFunctions *self,
    GLint x,
    GLint y,
    GLsizei width,
    GLsizei height) {
  self->glViewport(x, y, width, height);
}

//  void QOpenGLFunctions::glActiveTexture(GLenum texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions15glActiveTextureEj(
    QOpenGLFunctions *self,
    GLenum texture) {
  self->glActiveTexture(texture);
}

//  void QOpenGLFunctions::glAttachShader(GLuint program, GLuint shader)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions14glAttachShaderEjj(
    QOpenGLFunctions *self,
    GLuint program,
    GLuint shader) {
  self->glAttachShader(program, shader);
}

//  void QOpenGLFunctions::glBindAttribLocation(GLuint program, GLuint index,
//      const char *name)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions20glBindAttribLocationEjjPKc(
    QOpenGLFunctions *self,
    GLuint program,
    GLuint index,
    const char *name) {
  self->glBindAttribLocation(program, index, name);
}

//  void QOpenGLFunctions::glBindBuffer(GLenum target, GLuint buffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions12glBindBufferEjj(
    QOpenGLFunctions *self,
    GLenum target,
    GLuint buffer) {
  self->glBindBuffer(target, buffer);
}

//  void QOpenGLFunctions::glBindFramebuffer(GLenum target, GLuint
//      framebuffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions17glBindFramebufferEjj(
    QOpenGLFunctions *self,
    GLenum target,
    GLuint framebuffer) {
  self->glBindFramebuffer(target, framebuffer);
}

//  void QOpenGLFunctions::glBindRenderbuffer(GLenum target, GLuint
//      renderbuffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions18glBindRenderbufferEjj(
    QOpenGLFunctions *self,
    GLenum target,
    GLuint renderbuffer) {
  self->glBindRenderbuffer(target, renderbuffer);
}

//  void QOpenGLFunctions::glBlendColor(GLclampf red, GLclampf green,
//      GLclampf blue, GLclampf alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions12glBlendColorEffff(
    QOpenGLFunctions *self,
    GLclampf red,
    GLclampf green,
    GLclampf blue,
    GLclampf alpha) {
  self->glBlendColor(red, green, blue, alpha);
}

//  void QOpenGLFunctions::glBlendEquation(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions15glBlendEquationEj(
    QOpenGLFunctions *self,
    GLenum mode) {
  self->glBlendEquation(mode);
}

//  void QOpenGLFunctions::glBlendEquationSeparate(GLenum modeRGB, GLenum
//      modeAlpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions23glBlendEquationSeparateEjj(
    QOpenGLFunctions *self,
    GLenum modeRGB,
    GLenum modeAlpha) {
  self->glBlendEquationSeparate(modeRGB, modeAlpha);
}

//  void QOpenGLFunctions::glBlendFuncSeparate(GLenum srcRGB, GLenum dstRGB,
//      GLenum srcAlpha, GLenum dstAlpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions19glBlendFuncSeparateEjjjj(
    QOpenGLFunctions *self,
    GLenum srcRGB,
    GLenum dstRGB,
    GLenum srcAlpha,
    GLenum dstAlpha) {
  self->glBlendFuncSeparate(srcRGB, dstRGB, srcAlpha, dstAlpha);
}

//  void QOpenGLFunctions::glBufferData(GLenum target, qopengl_GLsizeiptr
//      size, const void *data, GLenum usage)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions12glBufferDataEjlPKvj(
    QOpenGLFunctions *self,
    GLenum target,
    long long size,
    const void *data,
    GLenum usage) {
  self->glBufferData(target, size, data, usage);
}

//  void QOpenGLFunctions::glBufferSubData(GLenum target, qopengl_GLintptr
//      offset, qopengl_GLsizeiptr size, const void *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions15glBufferSubDataEjllPKv(
    QOpenGLFunctions *self,
    GLenum target,
    long long offset,
    long long size,
    const void *data) {
  self->glBufferSubData(target, offset, size, data);
}

//  GLenum QOpenGLFunctions::glCheckFramebufferStatus(GLenum target)
extern "C" Q_DECL_EXPORT
GLenum ritual_ZN16QOpenGLFunctions24glCheckFramebufferStatusEj(
    QOpenGLFunctions *self,
    GLenum target) {
  return self->glCheckFramebufferStatus(target);
}

//  void QOpenGLFunctions::glClearDepthf(GLclampf depth)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions13glClearDepthfEf(
    QOpenGLFunctions *self,
    GLclampf depth) {
  self->glClearDepthf(depth);
}

//  void QOpenGLFunctions::glCompileShader(GLuint shader)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions15glCompileShaderEj(
    QOpenGLFunctions *self,
    GLuint shader) {
  self->glCompileShader(shader);
}

//  void QOpenGLFunctions::glCompressedTexImage2D(GLenum target, GLint level,
//      GLenum internalformat, GLsizei width, GLsizei height, GLint border,
//      GLsizei imageSize, const void *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions22glCompressedTexImage2DEjijiiiiPKv(
    QOpenGLFunctions *self,
    GLenum target,
    GLint level,
    GLenum internalformat,
    GLsizei width,
    GLsizei height,
    GLint border,
    GLsizei imageSize,
    const void *data) {
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

//  void QOpenGLFunctions::glCompressedTexSubImage2D(GLenum target, GLint
//      level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height,
//      GLenum format, GLsizei imageSize, const void *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions25glCompressedTexSubImage2DEjiiiiijiPKv(
    QOpenGLFunctions *self,
    GLenum target,
    GLint level,
    GLint xoffset,
    GLint yoffset,
    GLsizei width,
    GLsizei height,
    GLenum format,
    GLsizei imageSize,
    const void *data) {
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

//  GLuint QOpenGLFunctions::glCreateProgram()
extern "C" Q_DECL_EXPORT
GLuint ritual_ZN16QOpenGLFunctions15glCreateProgramEv(
    QOpenGLFunctions *self) {
  return self->glCreateProgram();
}

//  GLuint QOpenGLFunctions::glCreateShader(GLenum type)
extern "C" Q_DECL_EXPORT
GLuint ritual_ZN16QOpenGLFunctions14glCreateShaderEj(
    QOpenGLFunctions *self,
    GLenum type) {
  return self->glCreateShader(type);
}

//  void QOpenGLFunctions::glDeleteBuffers(GLsizei n, const GLuint *buffers)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions15glDeleteBuffersEiPKj(
    QOpenGLFunctions *self,
    GLsizei n,
    const GLuint *buffers) {
  self->glDeleteBuffers(n, buffers);
}

//  void QOpenGLFunctions::glDeleteFramebuffers(GLsizei n, const GLuint
//      *framebuffers)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions20glDeleteFramebuffersEiPKj(
    QOpenGLFunctions *self,
    GLsizei n,
    const GLuint *framebuffers) {
  self->glDeleteFramebuffers(n, framebuffers);
}

//  void QOpenGLFunctions::glDeleteProgram(GLuint program)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions15glDeleteProgramEj(
    QOpenGLFunctions *self,
    GLuint program) {
  self->glDeleteProgram(program);
}

//  void QOpenGLFunctions::glDeleteRenderbuffers(GLsizei n, const GLuint
//      *renderbuffers)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions21glDeleteRenderbuffersEiPKj(
    QOpenGLFunctions *self,
    GLsizei n,
    const GLuint *renderbuffers) {
  self->glDeleteRenderbuffers(n, renderbuffers);
}

//  void QOpenGLFunctions::glDeleteShader(GLuint shader)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions14glDeleteShaderEj(
    QOpenGLFunctions *self,
    GLuint shader) {
  self->glDeleteShader(shader);
}

//  void QOpenGLFunctions::glDepthRangef(GLclampf zNear, GLclampf zFar)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions13glDepthRangefEff(
    QOpenGLFunctions *self,
    GLclampf zNear,
    GLclampf zFar) {
  self->glDepthRangef(zNear, zFar);
}

//  void QOpenGLFunctions::glDetachShader(GLuint program, GLuint shader)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions14glDetachShaderEjj(
    QOpenGLFunctions *self,
    GLuint program,
    GLuint shader) {
  self->glDetachShader(program, shader);
}

//  void QOpenGLFunctions::glDisableVertexAttribArray(GLuint index)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions26glDisableVertexAttribArrayEj(
    QOpenGLFunctions *self,
    GLuint index) {
  self->glDisableVertexAttribArray(index);
}

//  void QOpenGLFunctions::glEnableVertexAttribArray(GLuint index)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions25glEnableVertexAttribArrayEj(
    QOpenGLFunctions *self,
    GLuint index) {
  self->glEnableVertexAttribArray(index);
}

//  void QOpenGLFunctions::glFramebufferRenderbuffer(GLenum target, GLenum
//      attachment, GLenum renderbuffertarget, GLuint renderbuffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions25glFramebufferRenderbufferEjjjj(
    QOpenGLFunctions *self,
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

//  void QOpenGLFunctions::glFramebufferTexture2D(GLenum target, GLenum
//      attachment, GLenum textarget, GLuint texture, GLint level)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions22glFramebufferTexture2DEjjjji(
    QOpenGLFunctions *self,
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

//  void QOpenGLFunctions::glGenBuffers(GLsizei n, GLuint *buffers)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions12glGenBuffersEiPj(
    QOpenGLFunctions *self,
    GLsizei n,
    GLuint *buffers) {
  self->glGenBuffers(n, buffers);
}

//  void QOpenGLFunctions::glGenerateMipmap(GLenum target)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions16glGenerateMipmapEj(
    QOpenGLFunctions *self,
    GLenum target) {
  self->glGenerateMipmap(target);
}

//  void QOpenGLFunctions::glGenFramebuffers(GLsizei n, GLuint *framebuffers)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions17glGenFramebuffersEiPj(
    QOpenGLFunctions *self,
    GLsizei n,
    GLuint *framebuffers) {
  self->glGenFramebuffers(n, framebuffers);
}

//  void QOpenGLFunctions::glGenRenderbuffers(GLsizei n, GLuint
//      *renderbuffers)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions18glGenRenderbuffersEiPj(
    QOpenGLFunctions *self,
    GLsizei n,
    GLuint *renderbuffers) {
  self->glGenRenderbuffers(n, renderbuffers);
}

//  void QOpenGLFunctions::glGetActiveAttrib(GLuint program, GLuint index,
//      GLsizei bufsize, GLsizei *length, GLint *size, GLenum *type, char
//      *name)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions17glGetActiveAttribEjjiPiS0_PjPc(
    QOpenGLFunctions *self,
    GLuint program,
    GLuint index,
    GLsizei bufsize,
    GLsizei *length,
    GLint *size,
    GLenum *type,
    char *name) {
  self->glGetActiveAttrib(program, index, bufsize, length, size, type, name);
}

//  void QOpenGLFunctions::glGetActiveUniform(GLuint program, GLuint index,
//      GLsizei bufsize, GLsizei *length, GLint *size, GLenum *type, char
//      *name)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions18glGetActiveUniformEjjiPiS0_PjPc(
    QOpenGLFunctions *self,
    GLuint program,
    GLuint index,
    GLsizei bufsize,
    GLsizei *length,
    GLint *size,
    GLenum *type,
    char *name) {
  self->glGetActiveUniform(
      program,
      index,
      bufsize,
      length,
      size,
      type,
      name);
}

//  void QOpenGLFunctions::glGetAttachedShaders(GLuint program, GLsizei
//      maxcount, GLsizei *count, GLuint *shaders)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions20glGetAttachedShadersEjiPiPj(
    QOpenGLFunctions *self,
    GLuint program,
    GLsizei maxcount,
    GLsizei *count,
    GLuint *shaders) {
  self->glGetAttachedShaders(program, maxcount, count, shaders);
}

//  GLint QOpenGLFunctions::glGetAttribLocation(GLuint program, const char
//      *name)
extern "C" Q_DECL_EXPORT
GLint ritual_ZN16QOpenGLFunctions19glGetAttribLocationEjPKc(
    QOpenGLFunctions *self,
    GLuint program,
    const char *name) {
  return self->glGetAttribLocation(program, name);
}

//  void QOpenGLFunctions::glGetBufferParameteriv(GLenum target, GLenum
//      pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions22glGetBufferParameterivEjjPi(
    QOpenGLFunctions *self,
    GLenum target,
    GLenum pname,
    GLint *params) {
  self->glGetBufferParameteriv(target, pname, params);
}

//  void QOpenGLFunctions::glGetFramebufferAttachmentParameteriv(GLenum
//      target, GLenum attachment, GLenum pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions37glGetFramebufferAttachmentParameterivEjjjPi(
    QOpenGLFunctions *self,
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

//  void QOpenGLFunctions::glGetProgramiv(GLuint program, GLenum pname, GLint
//      *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions14glGetProgramivEjjPi(
    QOpenGLFunctions *self,
    GLuint program,
    GLenum pname,
    GLint *params) {
  self->glGetProgramiv(program, pname, params);
}

//  void QOpenGLFunctions::glGetProgramInfoLog(GLuint program, GLsizei
//      bufsize, GLsizei *length, char *infolog)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions19glGetProgramInfoLogEjiPiPc(
    QOpenGLFunctions *self,
    GLuint program,
    GLsizei bufsize,
    GLsizei *length,
    char *infolog) {
  self->glGetProgramInfoLog(program, bufsize, length, infolog);
}

//  void QOpenGLFunctions::glGetRenderbufferParameteriv(GLenum target, GLenum
//      pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions28glGetRenderbufferParameterivEjjPi(
    QOpenGLFunctions *self,
    GLenum target,
    GLenum pname,
    GLint *params) {
  self->glGetRenderbufferParameteriv(target, pname, params);
}

//  void QOpenGLFunctions::glGetShaderiv(GLuint shader, GLenum pname, GLint
//      *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions13glGetShaderivEjjPi(
    QOpenGLFunctions *self,
    GLuint shader,
    GLenum pname,
    GLint *params) {
  self->glGetShaderiv(shader, pname, params);
}

//  void QOpenGLFunctions::glGetShaderInfoLog(GLuint shader, GLsizei bufsize,
//      GLsizei *length, char *infolog)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions18glGetShaderInfoLogEjiPiPc(
    QOpenGLFunctions *self,
    GLuint shader,
    GLsizei bufsize,
    GLsizei *length,
    char *infolog) {
  self->glGetShaderInfoLog(shader, bufsize, length, infolog);
}

//  void QOpenGLFunctions::glGetShaderPrecisionFormat(GLenum shadertype,
//      GLenum precisiontype, GLint *range, GLint *precision)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions26glGetShaderPrecisionFormatEjjPiS0_(
    QOpenGLFunctions *self,
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

//  void QOpenGLFunctions::glGetShaderSource(GLuint shader, GLsizei bufsize,
//      GLsizei *length, char *source)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions17glGetShaderSourceEjiPiPc(
    QOpenGLFunctions *self,
    GLuint shader,
    GLsizei bufsize,
    GLsizei *length,
    char *source) {
  self->glGetShaderSource(shader, bufsize, length, source);
}

//  void QOpenGLFunctions::glGetUniformfv(GLuint program, GLint location,
//      GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions14glGetUniformfvEjiPf(
    QOpenGLFunctions *self,
    GLuint program,
    GLint location,
    GLfloat *params) {
  self->glGetUniformfv(program, location, params);
}

//  void QOpenGLFunctions::glGetUniformiv(GLuint program, GLint location,
//      GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions14glGetUniformivEjiPi(
    QOpenGLFunctions *self,
    GLuint program,
    GLint location,
    GLint *params) {
  self->glGetUniformiv(program, location, params);
}

//  GLint QOpenGLFunctions::glGetUniformLocation(GLuint program, const char
//      *name)
extern "C" Q_DECL_EXPORT
GLint ritual_ZN16QOpenGLFunctions20glGetUniformLocationEjPKc(
    QOpenGLFunctions *self,
    GLuint program,
    const char *name) {
  return self->glGetUniformLocation(program, name);
}

//  void QOpenGLFunctions::glGetVertexAttribfv(GLuint index, GLenum pname,
//      GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions19glGetVertexAttribfvEjjPf(
    QOpenGLFunctions *self,
    GLuint index,
    GLenum pname,
    GLfloat *params) {
  self->glGetVertexAttribfv(index, pname, params);
}

//  void QOpenGLFunctions::glGetVertexAttribiv(GLuint index, GLenum pname,
//      GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions19glGetVertexAttribivEjjPi(
    QOpenGLFunctions *self,
    GLuint index,
    GLenum pname,
    GLint *params) {
  self->glGetVertexAttribiv(index, pname, params);
}

//  void QOpenGLFunctions::glGetVertexAttribPointerv(GLuint index, GLenum
//      pname, void **pointer)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions25glGetVertexAttribPointervEjjPPv(
    QOpenGLFunctions *self,
    GLuint index,
    GLenum pname,
    void **pointer) {
  self->glGetVertexAttribPointerv(index, pname, pointer);
}

//  GLboolean QOpenGLFunctions::glIsBuffer(GLuint buffer)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN16QOpenGLFunctions10glIsBufferEj(
    QOpenGLFunctions *self,
    GLuint buffer) {
  return self->glIsBuffer(buffer);
}

//  GLboolean QOpenGLFunctions::glIsFramebuffer(GLuint framebuffer)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN16QOpenGLFunctions15glIsFramebufferEj(
    QOpenGLFunctions *self,
    GLuint framebuffer) {
  return self->glIsFramebuffer(framebuffer);
}

//  GLboolean QOpenGLFunctions::glIsProgram(GLuint program)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN16QOpenGLFunctions11glIsProgramEj(
    QOpenGLFunctions *self,
    GLuint program) {
  return self->glIsProgram(program);
}

//  GLboolean QOpenGLFunctions::glIsRenderbuffer(GLuint renderbuffer)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN16QOpenGLFunctions16glIsRenderbufferEj(
    QOpenGLFunctions *self,
    GLuint renderbuffer) {
  return self->glIsRenderbuffer(renderbuffer);
}

//  GLboolean QOpenGLFunctions::glIsShader(GLuint shader)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN16QOpenGLFunctions10glIsShaderEj(
    QOpenGLFunctions *self,
    GLuint shader) {
  return self->glIsShader(shader);
}

//  void QOpenGLFunctions::glLinkProgram(GLuint program)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions13glLinkProgramEj(
    QOpenGLFunctions *self,
    GLuint program) {
  self->glLinkProgram(program);
}

//  void QOpenGLFunctions::glReleaseShaderCompiler()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions23glReleaseShaderCompilerEv(
    QOpenGLFunctions *self) {
  self->glReleaseShaderCompiler();
}

//  void QOpenGLFunctions::glRenderbufferStorage(GLenum target, GLenum
//      internalformat, GLsizei width, GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions21glRenderbufferStorageEjjii(
    QOpenGLFunctions *self,
    GLenum target,
    GLenum internalformat,
    GLsizei width,
    GLsizei height) {
  self->glRenderbufferStorage(target, internalformat, width, height);
}

//  void QOpenGLFunctions::glSampleCoverage(GLclampf value, GLboolean invert)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions16glSampleCoverageEfh(
    QOpenGLFunctions *self,
    GLclampf value,
    GLboolean invert) {
  self->glSampleCoverage(value, invert);
}

//  void QOpenGLFunctions::glShaderBinary(GLint n, const GLuint *shaders,
//      GLenum binaryformat, const void *binary, GLint length)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions14glShaderBinaryEiPKjjPKvi(
    QOpenGLFunctions *self,
    GLint n,
    const GLuint *shaders,
    GLenum binaryformat,
    const void *binary,
    GLint length) {
  self->glShaderBinary(n, shaders, binaryformat, binary, length);
}

//  void QOpenGLFunctions::glShaderSource(GLuint shader, GLsizei count, const
//      char **string, const GLint *length)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions14glShaderSourceEjiPPKcPKi(
    QOpenGLFunctions *self,
    GLuint shader,
    GLsizei count,
    const char **string,
    const GLint *length) {
  self->glShaderSource(shader, count, string, length);
}

//  void QOpenGLFunctions::glStencilFuncSeparate(GLenum face, GLenum func,
//      GLint ref, GLuint mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions21glStencilFuncSeparateEjjij(
    QOpenGLFunctions *self,
    GLenum face,
    GLenum func,
    GLint ref,
    GLuint mask) {
  self->glStencilFuncSeparate(face, func, ref, mask);
}

//  void QOpenGLFunctions::glStencilMaskSeparate(GLenum face, GLuint mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions21glStencilMaskSeparateEjj(
    QOpenGLFunctions *self,
    GLenum face,
    GLuint mask) {
  self->glStencilMaskSeparate(face, mask);
}

//  void QOpenGLFunctions::glStencilOpSeparate(GLenum face, GLenum fail,
//      GLenum zfail, GLenum zpass)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions19glStencilOpSeparateEjjjj(
    QOpenGLFunctions *self,
    GLenum face,
    GLenum fail,
    GLenum zfail,
    GLenum zpass) {
  self->glStencilOpSeparate(face, fail, zfail, zpass);
}

//  void QOpenGLFunctions::glUniform1f(GLint location, GLfloat x)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions11glUniform1fEif(
    QOpenGLFunctions *self,
    GLint location,
    GLfloat x) {
  self->glUniform1f(location, x);
}

//  void QOpenGLFunctions::glUniform1fv(GLint location, GLsizei count, const
//      GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions12glUniform1fvEiiPKf(
    QOpenGLFunctions *self,
    GLint location,
    GLsizei count,
    const GLfloat *v) {
  self->glUniform1fv(location, count, v);
}

//  void QOpenGLFunctions::glUniform1i(GLint location, GLint x)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions11glUniform1iEii(
    QOpenGLFunctions *self,
    GLint location,
    GLint x) {
  self->glUniform1i(location, x);
}

//  void QOpenGLFunctions::glUniform1iv(GLint location, GLsizei count, const
//      GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions12glUniform1ivEiiPKi(
    QOpenGLFunctions *self,
    GLint location,
    GLsizei count,
    const GLint *v) {
  self->glUniform1iv(location, count, v);
}

//  void QOpenGLFunctions::glUniform2f(GLint location, GLfloat x, GLfloat y)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions11glUniform2fEiff(
    QOpenGLFunctions *self,
    GLint location,
    GLfloat x,
    GLfloat y) {
  self->glUniform2f(location, x, y);
}

//  void QOpenGLFunctions::glUniform2fv(GLint location, GLsizei count, const
//      GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions12glUniform2fvEiiPKf(
    QOpenGLFunctions *self,
    GLint location,
    GLsizei count,
    const GLfloat *v) {
  self->glUniform2fv(location, count, v);
}

//  void QOpenGLFunctions::glUniform2i(GLint location, GLint x, GLint y)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions11glUniform2iEiii(
    QOpenGLFunctions *self,
    GLint location,
    GLint x,
    GLint y) {
  self->glUniform2i(location, x, y);
}

//  void QOpenGLFunctions::glUniform2iv(GLint location, GLsizei count, const
//      GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions12glUniform2ivEiiPKi(
    QOpenGLFunctions *self,
    GLint location,
    GLsizei count,
    const GLint *v) {
  self->glUniform2iv(location, count, v);
}

//  void QOpenGLFunctions::glUniform3f(GLint location, GLfloat x, GLfloat y,
//      GLfloat z)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions11glUniform3fEifff(
    QOpenGLFunctions *self,
    GLint location,
    GLfloat x,
    GLfloat y,
    GLfloat z) {
  self->glUniform3f(location, x, y, z);
}

//  void QOpenGLFunctions::glUniform3fv(GLint location, GLsizei count, const
//      GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions12glUniform3fvEiiPKf(
    QOpenGLFunctions *self,
    GLint location,
    GLsizei count,
    const GLfloat *v) {
  self->glUniform3fv(location, count, v);
}

//  void QOpenGLFunctions::glUniform3i(GLint location, GLint x, GLint y,
//      GLint z)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions11glUniform3iEiiii(
    QOpenGLFunctions *self,
    GLint location,
    GLint x,
    GLint y,
    GLint z) {
  self->glUniform3i(location, x, y, z);
}

//  void QOpenGLFunctions::glUniform3iv(GLint location, GLsizei count, const
//      GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions12glUniform3ivEiiPKi(
    QOpenGLFunctions *self,
    GLint location,
    GLsizei count,
    const GLint *v) {
  self->glUniform3iv(location, count, v);
}

//  void QOpenGLFunctions::glUniform4f(GLint location, GLfloat x, GLfloat y,
//      GLfloat z, GLfloat w)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions11glUniform4fEiffff(
    QOpenGLFunctions *self,
    GLint location,
    GLfloat x,
    GLfloat y,
    GLfloat z,
    GLfloat w) {
  self->glUniform4f(location, x, y, z, w);
}

//  void QOpenGLFunctions::glUniform4fv(GLint location, GLsizei count, const
//      GLfloat *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions12glUniform4fvEiiPKf(
    QOpenGLFunctions *self,
    GLint location,
    GLsizei count,
    const GLfloat *v) {
  self->glUniform4fv(location, count, v);
}

//  void QOpenGLFunctions::glUniform4i(GLint location, GLint x, GLint y,
//      GLint z, GLint w)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions11glUniform4iEiiiii(
    QOpenGLFunctions *self,
    GLint location,
    GLint x,
    GLint y,
    GLint z,
    GLint w) {
  self->glUniform4i(location, x, y, z, w);
}

//  void QOpenGLFunctions::glUniform4iv(GLint location, GLsizei count, const
//      GLint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions12glUniform4ivEiiPKi(
    QOpenGLFunctions *self,
    GLint location,
    GLsizei count,
    const GLint *v) {
  self->glUniform4iv(location, count, v);
}

//  void QOpenGLFunctions::glUniformMatrix2fv(GLint location, GLsizei count,
//      GLboolean transpose, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions18glUniformMatrix2fvEiihPKf(
    QOpenGLFunctions *self,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLfloat *value) {
  self->glUniformMatrix2fv(location, count, transpose, value);
}

//  void QOpenGLFunctions::glUniformMatrix3fv(GLint location, GLsizei count,
//      GLboolean transpose, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions18glUniformMatrix3fvEiihPKf(
    QOpenGLFunctions *self,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLfloat *value) {
  self->glUniformMatrix3fv(location, count, transpose, value);
}

//  void QOpenGLFunctions::glUniformMatrix4fv(GLint location, GLsizei count,
//      GLboolean transpose, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions18glUniformMatrix4fvEiihPKf(
    QOpenGLFunctions *self,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLfloat *value) {
  self->glUniformMatrix4fv(location, count, transpose, value);
}

//  void QOpenGLFunctions::glUseProgram(GLuint program)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions12glUseProgramEj(
    QOpenGLFunctions *self,
    GLuint program) {
  self->glUseProgram(program);
}

//  void QOpenGLFunctions::glValidateProgram(GLuint program)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions17glValidateProgramEj(
    QOpenGLFunctions *self,
    GLuint program) {
  self->glValidateProgram(program);
}

//  void QOpenGLFunctions::glVertexAttrib1f(GLuint indx, GLfloat x)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions16glVertexAttrib1fEjf(
    QOpenGLFunctions *self,
    GLuint indx,
    GLfloat x) {
  self->glVertexAttrib1f(indx, x);
}

//  void QOpenGLFunctions::glVertexAttrib1fv(GLuint indx, const GLfloat
//      *values)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions17glVertexAttrib1fvEjPKf(
    QOpenGLFunctions *self,
    GLuint indx,
    const GLfloat *values) {
  self->glVertexAttrib1fv(indx, values);
}

//  void QOpenGLFunctions::glVertexAttrib2f(GLuint indx, GLfloat x, GLfloat
//      y)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions16glVertexAttrib2fEjff(
    QOpenGLFunctions *self,
    GLuint indx,
    GLfloat x,
    GLfloat y) {
  self->glVertexAttrib2f(indx, x, y);
}

//  void QOpenGLFunctions::glVertexAttrib2fv(GLuint indx, const GLfloat
//      *values)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions17glVertexAttrib2fvEjPKf(
    QOpenGLFunctions *self,
    GLuint indx,
    const GLfloat *values) {
  self->glVertexAttrib2fv(indx, values);
}

//  void QOpenGLFunctions::glVertexAttrib3f(GLuint indx, GLfloat x, GLfloat
//      y, GLfloat z)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions16glVertexAttrib3fEjfff(
    QOpenGLFunctions *self,
    GLuint indx,
    GLfloat x,
    GLfloat y,
    GLfloat z) {
  self->glVertexAttrib3f(indx, x, y, z);
}

//  void QOpenGLFunctions::glVertexAttrib3fv(GLuint indx, const GLfloat
//      *values)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions17glVertexAttrib3fvEjPKf(
    QOpenGLFunctions *self,
    GLuint indx,
    const GLfloat *values) {
  self->glVertexAttrib3fv(indx, values);
}

//  void QOpenGLFunctions::glVertexAttrib4f(GLuint indx, GLfloat x, GLfloat
//      y, GLfloat z, GLfloat w)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions16glVertexAttrib4fEjffff(
    QOpenGLFunctions *self,
    GLuint indx,
    GLfloat x,
    GLfloat y,
    GLfloat z,
    GLfloat w) {
  self->glVertexAttrib4f(indx, x, y, z, w);
}

//  void QOpenGLFunctions::glVertexAttrib4fv(GLuint indx, const GLfloat
//      *values)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions17glVertexAttrib4fvEjPKf(
    QOpenGLFunctions *self,
    GLuint indx,
    const GLfloat *values) {
  self->glVertexAttrib4fv(indx, values);
}

//  void QOpenGLFunctions::glVertexAttribPointer(GLuint indx, GLint size,
//      GLenum type, GLboolean normalized, GLsizei stride, const void *ptr)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions21glVertexAttribPointerEjijhiPKv(
    QOpenGLFunctions *self,
    GLuint indx,
    GLint size,
    GLenum type,
    GLboolean normalized,
    GLsizei stride,
    const void *ptr) {
  self->glVertexAttribPointer(indx, size, type, normalized, stride, ptr);
}

//  bool QOpenGLFunctions::isInitialized(const QOpenGLFunctionsPrivate *d)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QOpenGLFunctions13isInitializedEPK23QOpenGLFunctionsPrivate(
    const QOpenGLFunctionsPrivate *d) {
  return QOpenGLFunctions::isInitialized(d);
}

#endif  // !defined(QT_NO_OPENGL)
