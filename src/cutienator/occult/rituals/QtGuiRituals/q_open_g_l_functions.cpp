//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qopenglfunctions.h, Qt 6.12.0. Changes made here are lost.
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

//  void QOpenGLFunctions::glHint(GLenum target, GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions6glHintEjj(
    QOpenGLFunctions *self,
    GLenum target,
    GLenum mode) {
  self->glHint(target, mode);
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

//  void QOpenGLFunctions::glDeleteProgram(GLuint program)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions15glDeleteProgramEj(
    QOpenGLFunctions *self,
    GLuint program) {
  self->glDeleteProgram(program);
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

//  void QOpenGLFunctions::glGenerateMipmap(GLenum target)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions16glGenerateMipmapEj(
    QOpenGLFunctions *self,
    GLenum target) {
  self->glGenerateMipmap(target);
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

//  void QOpenGLFunctions::glUniform1i(GLint location, GLint x)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions11glUniform1iEii(
    QOpenGLFunctions *self,
    GLint location,
    GLint x) {
  self->glUniform1i(location, x);
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

//  void QOpenGLFunctions::glUniform2i(GLint location, GLint x, GLint y)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpenGLFunctions11glUniform2iEiii(
    QOpenGLFunctions *self,
    GLint location,
    GLint x,
    GLint y) {
  self->glUniform2i(location, x, y);
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
