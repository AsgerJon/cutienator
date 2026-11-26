//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qopenglextrafunctions.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#if !defined(QT_NO_OPENGL)
#include <QtGui/qopenglextrafunctions.h>

//  QOpenGLExtraFunctionsPrivate *QOpenGLExtraFunctions::d_func()
extern "C" Q_DECL_EXPORT
QOpenGLExtraFunctionsPrivate *ritual_ZN21QOpenGLExtraFunctions6d_funcEv(
    QOpenGLExtraFunctions *self) {
  return self->d_func();
}

//  const QOpenGLExtraFunctionsPrivate *QOpenGLExtraFunctions::d_func() const
extern "C" Q_DECL_EXPORT
const QOpenGLExtraFunctionsPrivate *ritual_ZNK21QOpenGLExtraFunctions6d_funcEv(
    const QOpenGLExtraFunctions *self) {
  return self->d_func();
}

//  QOpenGLExtraFunctions::QOpenGLExtraFunctions()
extern "C" Q_DECL_EXPORT
QOpenGLExtraFunctions *ritual_ZN21QOpenGLExtraFunctionsC1Ev() {
  return new QOpenGLExtraFunctions();
}

//  QOpenGLExtraFunctions::QOpenGLExtraFunctions(QOpenGLContext *context)
extern "C" Q_DECL_EXPORT
QOpenGLExtraFunctions *ritual_ZN21QOpenGLExtraFunctionsC1EP14QOpenGLContext(
    QOpenGLContext *context) {
  return new QOpenGLExtraFunctions(context);
}

//  QOpenGLExtraFunctions::~QOpenGLExtraFunctions()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctionsD1Ev(QOpenGLExtraFunctions *self) {
  delete self;
}

//  void QOpenGLExtraFunctions::glReadBuffer(GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions12glReadBufferEj(
    QOpenGLExtraFunctions *self,
    GLenum mode) {
  self->glReadBuffer(mode);
}

//  void QOpenGLExtraFunctions::glDrawRangeElements(GLenum mode, GLuint
//      start, GLuint end, GLsizei count, GLenum type, const void *indices)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions19glDrawRangeElementsEjjjijPKv(
    QOpenGLExtraFunctions *self,
    GLenum mode,
    GLuint start,
    GLuint end,
    GLsizei count,
    GLenum type,
    const void *indices) {
  self->glDrawRangeElements(mode, start, end, count, type, indices);
}

//  void QOpenGLExtraFunctions::glTexImage3D(GLenum target, GLint level,
//      GLint internalformat, GLsizei width, GLsizei height, GLsizei depth,
//      GLint border, GLenum format, GLenum type, const void *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions12glTexImage3DEjiiiiiijjPKv(
    QOpenGLExtraFunctions *self,
    GLenum target,
    GLint level,
    GLint internalformat,
    GLsizei width,
    GLsizei height,
    GLsizei depth,
    GLint border,
    GLenum format,
    GLenum type,
    const void *pixels) {
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

//  void QOpenGLExtraFunctions::glTexSubImage3D(GLenum target, GLint level,
//      GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei
//      height, GLsizei depth, GLenum format, GLenum type, const void
//      *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions15glTexSubImage3DEjiiiiiiijjPKv(
    QOpenGLExtraFunctions *self,
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
    const void *pixels) {
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

//  void QOpenGLExtraFunctions::glCopyTexSubImage3D(GLenum target, GLint
//      level, GLint xoffset, GLint yoffset, GLint zoffset, GLint x, GLint y,
//      GLsizei width, GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions19glCopyTexSubImage3DEjiiiiiiii(
    QOpenGLExtraFunctions *self,
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

//  void QOpenGLExtraFunctions::glCompressedTexImage3D(GLenum target, GLint
//      level, GLenum internalformat, GLsizei width, GLsizei height, GLsizei
//      depth, GLint border, GLsizei imageSize, const void *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions22glCompressedTexImage3DEjijiiiiiPKv(
    QOpenGLExtraFunctions *self,
    GLenum target,
    GLint level,
    GLenum internalformat,
    GLsizei width,
    GLsizei height,
    GLsizei depth,
    GLint border,
    GLsizei imageSize,
    const void *data) {
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

//  void QOpenGLExtraFunctions::glCompressedTexSubImage3D(GLenum target,
//      GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei
//      width, GLsizei height, GLsizei depth, GLenum format, GLsizei
//      imageSize, const void *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions25glCompressedTexSubImage3DEjiiiiiiijiPKv(
    QOpenGLExtraFunctions *self,
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
    const void *data) {
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

//  void QOpenGLExtraFunctions::glGenQueries(GLsizei n, GLuint *ids)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions12glGenQueriesEiPj(
    QOpenGLExtraFunctions *self,
    GLsizei n,
    GLuint *ids) {
  self->glGenQueries(n, ids);
}

//  void QOpenGLExtraFunctions::glDeleteQueries(GLsizei n, const GLuint *ids)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions15glDeleteQueriesEiPKj(
    QOpenGLExtraFunctions *self,
    GLsizei n,
    const GLuint *ids) {
  self->glDeleteQueries(n, ids);
}

//  GLboolean QOpenGLExtraFunctions::glIsQuery(GLuint id)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN21QOpenGLExtraFunctions9glIsQueryEj(
    QOpenGLExtraFunctions *self,
    GLuint id) {
  return self->glIsQuery(id);
}

//  void QOpenGLExtraFunctions::glBeginQuery(GLenum target, GLuint id)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions12glBeginQueryEjj(
    QOpenGLExtraFunctions *self,
    GLenum target,
    GLuint id) {
  self->glBeginQuery(target, id);
}

//  void QOpenGLExtraFunctions::glEndQuery(GLenum target)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions10glEndQueryEj(
    QOpenGLExtraFunctions *self,
    GLenum target) {
  self->glEndQuery(target);
}

//  void QOpenGLExtraFunctions::glGetQueryiv(GLenum target, GLenum pname,
//      GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions12glGetQueryivEjjPi(
    QOpenGLExtraFunctions *self,
    GLenum target,
    GLenum pname,
    GLint *params) {
  self->glGetQueryiv(target, pname, params);
}

//  void QOpenGLExtraFunctions::glGetQueryObjectuiv(GLuint id, GLenum pname,
//      GLuint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions19glGetQueryObjectuivEjjPj(
    QOpenGLExtraFunctions *self,
    GLuint id,
    GLenum pname,
    GLuint *params) {
  self->glGetQueryObjectuiv(id, pname, params);
}

//  GLboolean QOpenGLExtraFunctions::glUnmapBuffer(GLenum target)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN21QOpenGLExtraFunctions13glUnmapBufferEj(
    QOpenGLExtraFunctions *self,
    GLenum target) {
  return self->glUnmapBuffer(target);
}

//  void QOpenGLExtraFunctions::glGetBufferPointerv(GLenum target, GLenum
//      pname, void **params)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions19glGetBufferPointervEjjPPv(
    QOpenGLExtraFunctions *self,
    GLenum target,
    GLenum pname,
    void **params) {
  self->glGetBufferPointerv(target, pname, params);
}

//  void QOpenGLExtraFunctions::glDrawBuffers(GLsizei n, const GLenum *bufs)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions13glDrawBuffersEiPKj(
    QOpenGLExtraFunctions *self,
    GLsizei n,
    const GLenum *bufs) {
  self->glDrawBuffers(n, bufs);
}

//  void QOpenGLExtraFunctions::glUniformMatrix2x3fv(GLint location, GLsizei
//      count, GLboolean transpose, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions20glUniformMatrix2x3fvEiihPKf(
    QOpenGLExtraFunctions *self,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLfloat *value) {
  self->glUniformMatrix2x3fv(location, count, transpose, value);
}

//  void QOpenGLExtraFunctions::glUniformMatrix3x2fv(GLint location, GLsizei
//      count, GLboolean transpose, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions20glUniformMatrix3x2fvEiihPKf(
    QOpenGLExtraFunctions *self,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLfloat *value) {
  self->glUniformMatrix3x2fv(location, count, transpose, value);
}

//  void QOpenGLExtraFunctions::glUniformMatrix2x4fv(GLint location, GLsizei
//      count, GLboolean transpose, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions20glUniformMatrix2x4fvEiihPKf(
    QOpenGLExtraFunctions *self,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLfloat *value) {
  self->glUniformMatrix2x4fv(location, count, transpose, value);
}

//  void QOpenGLExtraFunctions::glUniformMatrix4x2fv(GLint location, GLsizei
//      count, GLboolean transpose, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions20glUniformMatrix4x2fvEiihPKf(
    QOpenGLExtraFunctions *self,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLfloat *value) {
  self->glUniformMatrix4x2fv(location, count, transpose, value);
}

//  void QOpenGLExtraFunctions::glUniformMatrix3x4fv(GLint location, GLsizei
//      count, GLboolean transpose, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions20glUniformMatrix3x4fvEiihPKf(
    QOpenGLExtraFunctions *self,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLfloat *value) {
  self->glUniformMatrix3x4fv(location, count, transpose, value);
}

//  void QOpenGLExtraFunctions::glUniformMatrix4x3fv(GLint location, GLsizei
//      count, GLboolean transpose, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions20glUniformMatrix4x3fvEiihPKf(
    QOpenGLExtraFunctions *self,
    GLint location,
    GLsizei count,
    GLboolean transpose,
    const GLfloat *value) {
  self->glUniformMatrix4x3fv(location, count, transpose, value);
}

//  void QOpenGLExtraFunctions::glBlitFramebuffer(GLint srcX0, GLint srcY0,
//      GLint srcX1, GLint srcY1, GLint dstX0, GLint dstY0, GLint dstX1,
//      GLint dstY1, GLbitfield mask, GLenum filter)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions17glBlitFramebufferEiiiiiiiijj(
    QOpenGLExtraFunctions *self,
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

//  void QOpenGLExtraFunctions::glRenderbufferStorageMultisample(GLenum
//      target, GLsizei samples, GLenum internalformat, GLsizei width,
//      GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions32glRenderbufferStorageMultisampleEjijii(
    QOpenGLExtraFunctions *self,
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

//  void QOpenGLExtraFunctions::glFramebufferTextureLayer(GLenum target,
//      GLenum attachment, GLuint texture, GLint level, GLint layer)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions25glFramebufferTextureLayerEjjjii(
    QOpenGLExtraFunctions *self,
    GLenum target,
    GLenum attachment,
    GLuint texture,
    GLint level,
    GLint layer) {
  self->glFramebufferTextureLayer(target, attachment, texture, level, layer);
}

//  void *QOpenGLExtraFunctions::glMapBufferRange(GLenum target, GLintptr
//      offset, GLsizeiptr length, GLbitfield access)
extern "C" Q_DECL_EXPORT
void *ritual_ZN21QOpenGLExtraFunctions16glMapBufferRangeEjllj(
    QOpenGLExtraFunctions *self,
    GLenum target,
    long long offset,
    long long length,
    GLbitfield access) {
  return self->glMapBufferRange(target, offset, length, access);
}

//  void QOpenGLExtraFunctions::glFlushMappedBufferRange(GLenum target,
//      GLintptr offset, GLsizeiptr length)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions24glFlushMappedBufferRangeEjll(
    QOpenGLExtraFunctions *self,
    GLenum target,
    long long offset,
    long long length) {
  self->glFlushMappedBufferRange(target, offset, length);
}

//  void QOpenGLExtraFunctions::glBindVertexArray(GLuint array)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions17glBindVertexArrayEj(
    QOpenGLExtraFunctions *self,
    GLuint array) {
  self->glBindVertexArray(array);
}

//  void QOpenGLExtraFunctions::glDeleteVertexArrays(GLsizei n, const GLuint
//      *arrays)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions20glDeleteVertexArraysEiPKj(
    QOpenGLExtraFunctions *self,
    GLsizei n,
    const GLuint *arrays) {
  self->glDeleteVertexArrays(n, arrays);
}

//  void QOpenGLExtraFunctions::glGenVertexArrays(GLsizei n, GLuint *arrays)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions17glGenVertexArraysEiPj(
    QOpenGLExtraFunctions *self,
    GLsizei n,
    GLuint *arrays) {
  self->glGenVertexArrays(n, arrays);
}

//  GLboolean QOpenGLExtraFunctions::glIsVertexArray(GLuint array)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN21QOpenGLExtraFunctions15glIsVertexArrayEj(
    QOpenGLExtraFunctions *self,
    GLuint array) {
  return self->glIsVertexArray(array);
}

//  void QOpenGLExtraFunctions::glGetIntegeri_v(GLenum target, GLuint index,
//      GLint *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions15glGetIntegeri_vEjjPi(
    QOpenGLExtraFunctions *self,
    GLenum target,
    GLuint index,
    GLint *data) {
  self->glGetIntegeri_v(target, index, data);
}

//  void QOpenGLExtraFunctions::glBeginTransformFeedback(GLenum
//      primitiveMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions24glBeginTransformFeedbackEj(
    QOpenGLExtraFunctions *self,
    GLenum primitiveMode) {
  self->glBeginTransformFeedback(primitiveMode);
}

//  void QOpenGLExtraFunctions::glEndTransformFeedback()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions22glEndTransformFeedbackEv(
    QOpenGLExtraFunctions *self) {
  self->glEndTransformFeedback();
}

//  void QOpenGLExtraFunctions::glBindBufferRange(GLenum target, GLuint
//      index, GLuint buffer, GLintptr offset, GLsizeiptr size)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions17glBindBufferRangeEjjjll(
    QOpenGLExtraFunctions *self,
    GLenum target,
    GLuint index,
    GLuint buffer,
    long long offset,
    long long size) {
  self->glBindBufferRange(target, index, buffer, offset, size);
}

//  void QOpenGLExtraFunctions::glBindBufferBase(GLenum target, GLuint index,
//      GLuint buffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions16glBindBufferBaseEjjj(
    QOpenGLExtraFunctions *self,
    GLenum target,
    GLuint index,
    GLuint buffer) {
  self->glBindBufferBase(target, index, buffer);
}

//  void QOpenGLExtraFunctions::glTransformFeedbackVaryings(GLuint program,
//      GLsizei count, const GLchar *const *varyings, GLenum bufferMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions27glTransformFeedbackVaryingsEjiPKPKcj(
    QOpenGLExtraFunctions *self,
    GLuint program,
    GLsizei count,
    const GLchar *const *varyings,
    GLenum bufferMode) {
  self->glTransformFeedbackVaryings(program, count, varyings, bufferMode);
}

//  void QOpenGLExtraFunctions::glGetTransformFeedbackVarying(GLuint program,
//      GLuint index, GLsizei bufSize, GLsizei *length, GLsizei *size, GLenum
//      *type, GLchar *name)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions29glGetTransformFeedbackVaryingEjjiPiS0_PjPc(
    QOpenGLExtraFunctions *self,
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

//  void QOpenGLExtraFunctions::glVertexAttribIPointer(GLuint index, GLint
//      size, GLenum type, GLsizei stride, const void *pointer)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions22glVertexAttribIPointerEjijiPKv(
    QOpenGLExtraFunctions *self,
    GLuint index,
    GLint size,
    GLenum type,
    GLsizei stride,
    const void *pointer) {
  self->glVertexAttribIPointer(index, size, type, stride, pointer);
}

//  void QOpenGLExtraFunctions::glGetVertexAttribIiv(GLuint index, GLenum
//      pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions20glGetVertexAttribIivEjjPi(
    QOpenGLExtraFunctions *self,
    GLuint index,
    GLenum pname,
    GLint *params) {
  self->glGetVertexAttribIiv(index, pname, params);
}

//  void QOpenGLExtraFunctions::glGetVertexAttribIuiv(GLuint index, GLenum
//      pname, GLuint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions21glGetVertexAttribIuivEjjPj(
    QOpenGLExtraFunctions *self,
    GLuint index,
    GLenum pname,
    GLuint *params) {
  self->glGetVertexAttribIuiv(index, pname, params);
}

//  void QOpenGLExtraFunctions::glVertexAttribI4i(GLuint index, GLint x,
//      GLint y, GLint z, GLint w)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions17glVertexAttribI4iEjiiii(
    QOpenGLExtraFunctions *self,
    GLuint index,
    GLint x,
    GLint y,
    GLint z,
    GLint w) {
  self->glVertexAttribI4i(index, x, y, z, w);
}

//  void QOpenGLExtraFunctions::glVertexAttribI4ui(GLuint index, GLuint x,
//      GLuint y, GLuint z, GLuint w)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions18glVertexAttribI4uiEjjjjj(
    QOpenGLExtraFunctions *self,
    GLuint index,
    GLuint x,
    GLuint y,
    GLuint z,
    GLuint w) {
  self->glVertexAttribI4ui(index, x, y, z, w);
}

//  void QOpenGLExtraFunctions::glVertexAttribI4iv(GLuint index, const GLint
//      *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions18glVertexAttribI4ivEjPKi(
    QOpenGLExtraFunctions *self,
    GLuint index,
    const GLint *v) {
  self->glVertexAttribI4iv(index, v);
}

//  void QOpenGLExtraFunctions::glVertexAttribI4uiv(GLuint index, const
//      GLuint *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions19glVertexAttribI4uivEjPKj(
    QOpenGLExtraFunctions *self,
    GLuint index,
    const GLuint *v) {
  self->glVertexAttribI4uiv(index, v);
}

//  void QOpenGLExtraFunctions::glGetUniformuiv(GLuint program, GLint
//      location, GLuint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions15glGetUniformuivEjiPj(
    QOpenGLExtraFunctions *self,
    GLuint program,
    GLint location,
    GLuint *params) {
  self->glGetUniformuiv(program, location, params);
}

//  GLint QOpenGLExtraFunctions::glGetFragDataLocation(GLuint program, const
//      GLchar *name)
extern "C" Q_DECL_EXPORT
GLint ritual_ZN21QOpenGLExtraFunctions21glGetFragDataLocationEjPKc(
    QOpenGLExtraFunctions *self,
    GLuint program,
    const GLchar *name) {
  return self->glGetFragDataLocation(program, name);
}

//  void QOpenGLExtraFunctions::glUniform1ui(GLint location, GLuint v0)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions12glUniform1uiEij(
    QOpenGLExtraFunctions *self,
    GLint location,
    GLuint v0) {
  self->glUniform1ui(location, v0);
}

//  void QOpenGLExtraFunctions::glUniform2ui(GLint location, GLuint v0,
//      GLuint v1)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions12glUniform2uiEijj(
    QOpenGLExtraFunctions *self,
    GLint location,
    GLuint v0,
    GLuint v1) {
  self->glUniform2ui(location, v0, v1);
}

//  void QOpenGLExtraFunctions::glUniform3ui(GLint location, GLuint v0,
//      GLuint v1, GLuint v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions12glUniform3uiEijjj(
    QOpenGLExtraFunctions *self,
    GLint location,
    GLuint v0,
    GLuint v1,
    GLuint v2) {
  self->glUniform3ui(location, v0, v1, v2);
}

//  void QOpenGLExtraFunctions::glUniform4ui(GLint location, GLuint v0,
//      GLuint v1, GLuint v2, GLuint v3)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions12glUniform4uiEijjjj(
    QOpenGLExtraFunctions *self,
    GLint location,
    GLuint v0,
    GLuint v1,
    GLuint v2,
    GLuint v3) {
  self->glUniform4ui(location, v0, v1, v2, v3);
}

//  void QOpenGLExtraFunctions::glUniform1uiv(GLint location, GLsizei count,
//      const GLuint *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions13glUniform1uivEiiPKj(
    QOpenGLExtraFunctions *self,
    GLint location,
    GLsizei count,
    const GLuint *value) {
  self->glUniform1uiv(location, count, value);
}

//  void QOpenGLExtraFunctions::glUniform2uiv(GLint location, GLsizei count,
//      const GLuint *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions13glUniform2uivEiiPKj(
    QOpenGLExtraFunctions *self,
    GLint location,
    GLsizei count,
    const GLuint *value) {
  self->glUniform2uiv(location, count, value);
}

//  void QOpenGLExtraFunctions::glUniform3uiv(GLint location, GLsizei count,
//      const GLuint *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions13glUniform3uivEiiPKj(
    QOpenGLExtraFunctions *self,
    GLint location,
    GLsizei count,
    const GLuint *value) {
  self->glUniform3uiv(location, count, value);
}

//  void QOpenGLExtraFunctions::glUniform4uiv(GLint location, GLsizei count,
//      const GLuint *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions13glUniform4uivEiiPKj(
    QOpenGLExtraFunctions *self,
    GLint location,
    GLsizei count,
    const GLuint *value) {
  self->glUniform4uiv(location, count, value);
}

//  void QOpenGLExtraFunctions::glClearBufferiv(GLenum buffer, GLint
//      drawbuffer, const GLint *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions15glClearBufferivEjiPKi(
    QOpenGLExtraFunctions *self,
    GLenum buffer,
    GLint drawbuffer,
    const GLint *value) {
  self->glClearBufferiv(buffer, drawbuffer, value);
}

//  void QOpenGLExtraFunctions::glClearBufferuiv(GLenum buffer, GLint
//      drawbuffer, const GLuint *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions16glClearBufferuivEjiPKj(
    QOpenGLExtraFunctions *self,
    GLenum buffer,
    GLint drawbuffer,
    const GLuint *value) {
  self->glClearBufferuiv(buffer, drawbuffer, value);
}

//  void QOpenGLExtraFunctions::glClearBufferfv(GLenum buffer, GLint
//      drawbuffer, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions15glClearBufferfvEjiPKf(
    QOpenGLExtraFunctions *self,
    GLenum buffer,
    GLint drawbuffer,
    const GLfloat *value) {
  self->glClearBufferfv(buffer, drawbuffer, value);
}

//  void QOpenGLExtraFunctions::glClearBufferfi(GLenum buffer, GLint
//      drawbuffer, GLfloat depth, GLint stencil)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions15glClearBufferfiEjifi(
    QOpenGLExtraFunctions *self,
    GLenum buffer,
    GLint drawbuffer,
    GLfloat depth,
    GLint stencil) {
  self->glClearBufferfi(buffer, drawbuffer, depth, stencil);
}

//  const GLubyte *QOpenGLExtraFunctions::glGetStringi(GLenum name, GLuint
//      index)
extern "C" Q_DECL_EXPORT
const GLubyte *ritual_ZN21QOpenGLExtraFunctions12glGetStringiEjj(
    QOpenGLExtraFunctions *self,
    GLenum name,
    GLuint index) {
  return self->glGetStringi(name, index);
}

//  void QOpenGLExtraFunctions::glCopyBufferSubData(GLenum readTarget, GLenum
//      writeTarget, GLintptr readOffset, GLintptr writeOffset, GLsizeiptr
//      size)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions19glCopyBufferSubDataEjjlll(
    QOpenGLExtraFunctions *self,
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

//  void QOpenGLExtraFunctions::glGetUniformIndices(GLuint program, GLsizei
//      uniformCount, const GLchar *const *uniformNames, GLuint
//      *uniformIndices)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions19glGetUniformIndicesEjiPKPKcPj(
    QOpenGLExtraFunctions *self,
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

//  void QOpenGLExtraFunctions::glGetActiveUniformsiv(GLuint program, GLsizei
//      uniformCount, const GLuint *uniformIndices, GLenum pname, GLint
//      *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions21glGetActiveUniformsivEjiPKjjPi(
    QOpenGLExtraFunctions *self,
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

//  GLuint QOpenGLExtraFunctions::glGetUniformBlockIndex(GLuint program,
//      const GLchar *uniformBlockName)
extern "C" Q_DECL_EXPORT
GLuint ritual_ZN21QOpenGLExtraFunctions22glGetUniformBlockIndexEjPKc(
    QOpenGLExtraFunctions *self,
    GLuint program,
    const GLchar *uniformBlockName) {
  return self->glGetUniformBlockIndex(program, uniformBlockName);
}

//  void QOpenGLExtraFunctions::glGetActiveUniformBlockiv(GLuint program,
//      GLuint uniformBlockIndex, GLenum pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions25glGetActiveUniformBlockivEjjjPi(
    QOpenGLExtraFunctions *self,
    GLuint program,
    GLuint uniformBlockIndex,
    GLenum pname,
    GLint *params) {
  self->glGetActiveUniformBlockiv(program, uniformBlockIndex, pname, params);
}

//  void QOpenGLExtraFunctions::glGetActiveUniformBlockName(GLuint program,
//      GLuint uniformBlockIndex, GLsizei bufSize, GLsizei *length, GLchar
//      *uniformBlockName)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions27glGetActiveUniformBlockNameEjjiPiPc(
    QOpenGLExtraFunctions *self,
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

//  void QOpenGLExtraFunctions::glUniformBlockBinding(GLuint program, GLuint
//      uniformBlockIndex, GLuint uniformBlockBinding)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions21glUniformBlockBindingEjjj(
    QOpenGLExtraFunctions *self,
    GLuint program,
    GLuint uniformBlockIndex,
    GLuint uniformBlockBinding) {
  self->glUniformBlockBinding(
      program,
      uniformBlockIndex,
      uniformBlockBinding);
}

//  void QOpenGLExtraFunctions::glDrawArraysInstanced(GLenum mode, GLint
//      first, GLsizei count, GLsizei instancecount)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions21glDrawArraysInstancedEjiii(
    QOpenGLExtraFunctions *self,
    GLenum mode,
    GLint first,
    GLsizei count,
    GLsizei instancecount) {
  self->glDrawArraysInstanced(mode, first, count, instancecount);
}

//  void QOpenGLExtraFunctions::glDrawElementsInstanced(GLenum mode, GLsizei
//      count, GLenum type, const void *indices, GLsizei instancecount)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions23glDrawElementsInstancedEjijPKvi(
    QOpenGLExtraFunctions *self,
    GLenum mode,
    GLsizei count,
    GLenum type,
    const void *indices,
    GLsizei instancecount) {
  self->glDrawElementsInstanced(mode, count, type, indices, instancecount);
}

//  GLsync QOpenGLExtraFunctions::glFenceSync(GLenum condition, GLbitfield
//      flags)
extern "C" Q_DECL_EXPORT
GLsync ritual_ZN21QOpenGLExtraFunctions11glFenceSyncEjj(
    QOpenGLExtraFunctions *self,
    GLenum condition,
    GLbitfield flags) {
  return self->glFenceSync(condition, flags);
}

//  GLboolean QOpenGLExtraFunctions::glIsSync(GLsync sync)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN21QOpenGLExtraFunctions8glIsSyncEP8__GLsync(
    QOpenGLExtraFunctions *self,
    GLsync sync) {
  return self->glIsSync(sync);
}

//  void QOpenGLExtraFunctions::glDeleteSync(GLsync sync)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions12glDeleteSyncEP8__GLsync(
    QOpenGLExtraFunctions *self,
    GLsync sync) {
  self->glDeleteSync(sync);
}

//  GLenum QOpenGLExtraFunctions::glClientWaitSync(GLsync sync, GLbitfield
//      flags, GLuint64 timeout)
extern "C" Q_DECL_EXPORT
GLenum ritual_ZN21QOpenGLExtraFunctions16glClientWaitSyncEP8__GLsyncjm(
    QOpenGLExtraFunctions *self,
    GLsync sync,
    GLbitfield flags,
    unsigned long long timeout) {
  return self->glClientWaitSync(sync, flags, timeout);
}

//  void QOpenGLExtraFunctions::glWaitSync(GLsync sync, GLbitfield flags,
//      GLuint64 timeout)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions10glWaitSyncEP8__GLsyncjm(
    QOpenGLExtraFunctions *self,
    GLsync sync,
    GLbitfield flags,
    unsigned long long timeout) {
  self->glWaitSync(sync, flags, timeout);
}

//  void QOpenGLExtraFunctions::glGetInteger64v(GLenum pname, GLint64 *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions15glGetInteger64vEjPl(
    QOpenGLExtraFunctions *self,
    GLenum pname,
    GLint64 *data) {
  self->glGetInteger64v(pname, data);
}

//  void QOpenGLExtraFunctions::glGetSynciv(GLsync sync, GLenum pname,
//      GLsizei bufSize, GLsizei *length, GLint *values)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions11glGetSyncivEP8__GLsyncjiPiS2_(
    QOpenGLExtraFunctions *self,
    GLsync sync,
    GLenum pname,
    GLsizei bufSize,
    GLsizei *length,
    GLint *values) {
  self->glGetSynciv(sync, pname, bufSize, length, values);
}

//  void QOpenGLExtraFunctions::glGetInteger64i_v(GLenum target, GLuint
//      index, GLint64 *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions17glGetInteger64i_vEjjPl(
    QOpenGLExtraFunctions *self,
    GLenum target,
    GLuint index,
    GLint64 *data) {
  self->glGetInteger64i_v(target, index, data);
}

//  void QOpenGLExtraFunctions::glGetBufferParameteri64v(GLenum target,
//      GLenum pname, GLint64 *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions24glGetBufferParameteri64vEjjPl(
    QOpenGLExtraFunctions *self,
    GLenum target,
    GLenum pname,
    GLint64 *params) {
  self->glGetBufferParameteri64v(target, pname, params);
}

//  void QOpenGLExtraFunctions::glGenSamplers(GLsizei count, GLuint
//      *samplers)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions13glGenSamplersEiPj(
    QOpenGLExtraFunctions *self,
    GLsizei count,
    GLuint *samplers) {
  self->glGenSamplers(count, samplers);
}

//  void QOpenGLExtraFunctions::glDeleteSamplers(GLsizei count, const GLuint
//      *samplers)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions16glDeleteSamplersEiPKj(
    QOpenGLExtraFunctions *self,
    GLsizei count,
    const GLuint *samplers) {
  self->glDeleteSamplers(count, samplers);
}

//  GLboolean QOpenGLExtraFunctions::glIsSampler(GLuint sampler)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN21QOpenGLExtraFunctions11glIsSamplerEj(
    QOpenGLExtraFunctions *self,
    GLuint sampler) {
  return self->glIsSampler(sampler);
}

//  void QOpenGLExtraFunctions::glBindSampler(GLuint unit, GLuint sampler)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions13glBindSamplerEjj(
    QOpenGLExtraFunctions *self,
    GLuint unit,
    GLuint sampler) {
  self->glBindSampler(unit, sampler);
}

//  void QOpenGLExtraFunctions::glSamplerParameteri(GLuint sampler, GLenum
//      pname, GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions19glSamplerParameteriEjji(
    QOpenGLExtraFunctions *self,
    GLuint sampler,
    GLenum pname,
    GLint param) {
  self->glSamplerParameteri(sampler, pname, param);
}

//  void QOpenGLExtraFunctions::glSamplerParameteriv(GLuint sampler, GLenum
//      pname, const GLint *param)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions20glSamplerParameterivEjjPKi(
    QOpenGLExtraFunctions *self,
    GLuint sampler,
    GLenum pname,
    const GLint *param) {
  self->glSamplerParameteriv(sampler, pname, param);
}

//  void QOpenGLExtraFunctions::glSamplerParameterf(GLuint sampler, GLenum
//      pname, GLfloat param)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions19glSamplerParameterfEjjf(
    QOpenGLExtraFunctions *self,
    GLuint sampler,
    GLenum pname,
    GLfloat param) {
  self->glSamplerParameterf(sampler, pname, param);
}

//  void QOpenGLExtraFunctions::glSamplerParameterfv(GLuint sampler, GLenum
//      pname, const GLfloat *param)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions20glSamplerParameterfvEjjPKf(
    QOpenGLExtraFunctions *self,
    GLuint sampler,
    GLenum pname,
    const GLfloat *param) {
  self->glSamplerParameterfv(sampler, pname, param);
}

//  void QOpenGLExtraFunctions::glGetSamplerParameteriv(GLuint sampler,
//      GLenum pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions23glGetSamplerParameterivEjjPi(
    QOpenGLExtraFunctions *self,
    GLuint sampler,
    GLenum pname,
    GLint *params) {
  self->glGetSamplerParameteriv(sampler, pname, params);
}

//  void QOpenGLExtraFunctions::glGetSamplerParameterfv(GLuint sampler,
//      GLenum pname, GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions23glGetSamplerParameterfvEjjPf(
    QOpenGLExtraFunctions *self,
    GLuint sampler,
    GLenum pname,
    GLfloat *params) {
  self->glGetSamplerParameterfv(sampler, pname, params);
}

//  void QOpenGLExtraFunctions::glVertexAttribDivisor(GLuint index, GLuint
//      divisor)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions21glVertexAttribDivisorEjj(
    QOpenGLExtraFunctions *self,
    GLuint index,
    GLuint divisor) {
  self->glVertexAttribDivisor(index, divisor);
}

//  void QOpenGLExtraFunctions::glBindTransformFeedback(GLenum target, GLuint
//      id)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions23glBindTransformFeedbackEjj(
    QOpenGLExtraFunctions *self,
    GLenum target,
    GLuint id) {
  self->glBindTransformFeedback(target, id);
}

//  void QOpenGLExtraFunctions::glDeleteTransformFeedbacks(GLsizei n, const
//      GLuint *ids)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions26glDeleteTransformFeedbacksEiPKj(
    QOpenGLExtraFunctions *self,
    GLsizei n,
    const GLuint *ids) {
  self->glDeleteTransformFeedbacks(n, ids);
}

//  void QOpenGLExtraFunctions::glGenTransformFeedbacks(GLsizei n, GLuint
//      *ids)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions23glGenTransformFeedbacksEiPj(
    QOpenGLExtraFunctions *self,
    GLsizei n,
    GLuint *ids) {
  self->glGenTransformFeedbacks(n, ids);
}

//  GLboolean QOpenGLExtraFunctions::glIsTransformFeedback(GLuint id)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN21QOpenGLExtraFunctions21glIsTransformFeedbackEj(
    QOpenGLExtraFunctions *self,
    GLuint id) {
  return self->glIsTransformFeedback(id);
}

//  void QOpenGLExtraFunctions::glPauseTransformFeedback()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions24glPauseTransformFeedbackEv(
    QOpenGLExtraFunctions *self) {
  self->glPauseTransformFeedback();
}

//  void QOpenGLExtraFunctions::glResumeTransformFeedback()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions25glResumeTransformFeedbackEv(
    QOpenGLExtraFunctions *self) {
  self->glResumeTransformFeedback();
}

//  void QOpenGLExtraFunctions::glGetProgramBinary(GLuint program, GLsizei
//      bufSize, GLsizei *length, GLenum *binaryFormat, void *binary)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions18glGetProgramBinaryEjiPiPjPv(
    QOpenGLExtraFunctions *self,
    GLuint program,
    GLsizei bufSize,
    GLsizei *length,
    GLenum *binaryFormat,
    void *binary) {
  self->glGetProgramBinary(program, bufSize, length, binaryFormat, binary);
}

//  void QOpenGLExtraFunctions::glProgramBinary(GLuint program, GLenum
//      binaryFormat, const void *binary, GLsizei length)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions15glProgramBinaryEjjPKvi(
    QOpenGLExtraFunctions *self,
    GLuint program,
    GLenum binaryFormat,
    const void *binary,
    GLsizei length) {
  self->glProgramBinary(program, binaryFormat, binary, length);
}

//  void QOpenGLExtraFunctions::glProgramParameteri(GLuint program, GLenum
//      pname, GLint value)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions19glProgramParameteriEjji(
    QOpenGLExtraFunctions *self,
    GLuint program,
    GLenum pname,
    GLint value) {
  self->glProgramParameteri(program, pname, value);
}

//  void QOpenGLExtraFunctions::glInvalidateFramebuffer(GLenum target,
//      GLsizei numAttachments, const GLenum *attachments)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions23glInvalidateFramebufferEjiPKj(
    QOpenGLExtraFunctions *self,
    GLenum target,
    GLsizei numAttachments,
    const GLenum *attachments) {
  self->glInvalidateFramebuffer(target, numAttachments, attachments);
}

//  void QOpenGLExtraFunctions::glInvalidateSubFramebuffer(GLenum target,
//      GLsizei numAttachments, const GLenum *attachments, GLint x, GLint y,
//      GLsizei width, GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions26glInvalidateSubFramebufferEjiPKjiiii(
    QOpenGLExtraFunctions *self,
    GLenum target,
    GLsizei numAttachments,
    const GLenum *attachments,
    GLint x,
    GLint y,
    GLsizei width,
    GLsizei height) {
  self->glInvalidateSubFramebuffer(
      target,
      numAttachments,
      attachments,
      x,
      y,
      width,
      height);
}

//  void QOpenGLExtraFunctions::glTexStorage2D(GLenum target, GLsizei levels,
//      GLenum internalformat, GLsizei width, GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions14glTexStorage2DEjijii(
    QOpenGLExtraFunctions *self,
    GLenum target,
    GLsizei levels,
    GLenum internalformat,
    GLsizei width,
    GLsizei height) {
  self->glTexStorage2D(target, levels, internalformat, width, height);
}

//  void QOpenGLExtraFunctions::glTexStorage3D(GLenum target, GLsizei levels,
//      GLenum internalformat, GLsizei width, GLsizei height, GLsizei depth)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions14glTexStorage3DEjijiii(
    QOpenGLExtraFunctions *self,
    GLenum target,
    GLsizei levels,
    GLenum internalformat,
    GLsizei width,
    GLsizei height,
    GLsizei depth) {
  self->glTexStorage3D(target, levels, internalformat, width, height, depth);
}

//  void QOpenGLExtraFunctions::glGetInternalformativ(GLenum target, GLenum
//      internalformat, GLenum pname, GLsizei bufSize, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions21glGetInternalformativEjjjiPi(
    QOpenGLExtraFunctions *self,
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

//  void QOpenGLExtraFunctions::glDispatchCompute(GLuint num_groups_x, GLuint
//      num_groups_y, GLuint num_groups_z)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions17glDispatchComputeEjjj(
    QOpenGLExtraFunctions *self,
    GLuint num_groups_x,
    GLuint num_groups_y,
    GLuint num_groups_z) {
  self->glDispatchCompute(num_groups_x, num_groups_y, num_groups_z);
}

//  void QOpenGLExtraFunctions::glDispatchComputeIndirect(GLintptr indirect)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions25glDispatchComputeIndirectEl(
    QOpenGLExtraFunctions *self,
    long long indirect) {
  self->glDispatchComputeIndirect(indirect);
}

//  void QOpenGLExtraFunctions::glDrawArraysIndirect(GLenum mode, const void
//      *indirect)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions20glDrawArraysIndirectEjPKv(
    QOpenGLExtraFunctions *self,
    GLenum mode,
    const void *indirect) {
  self->glDrawArraysIndirect(mode, indirect);
}

//  void QOpenGLExtraFunctions::glDrawElementsIndirect(GLenum mode, GLenum
//      type, const void *indirect)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions22glDrawElementsIndirectEjjPKv(
    QOpenGLExtraFunctions *self,
    GLenum mode,
    GLenum type,
    const void *indirect) {
  self->glDrawElementsIndirect(mode, type, indirect);
}

//  void QOpenGLExtraFunctions::glFramebufferParameteri(GLenum target, GLenum
//      pname, GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions23glFramebufferParameteriEjji(
    QOpenGLExtraFunctions *self,
    GLenum target,
    GLenum pname,
    GLint param) {
  self->glFramebufferParameteri(target, pname, param);
}

//  void QOpenGLExtraFunctions::glGetFramebufferParameteriv(GLenum target,
//      GLenum pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions27glGetFramebufferParameterivEjjPi(
    QOpenGLExtraFunctions *self,
    GLenum target,
    GLenum pname,
    GLint *params) {
  self->glGetFramebufferParameteriv(target, pname, params);
}

//  void QOpenGLExtraFunctions::glGetProgramInterfaceiv(GLuint program,
//      GLenum programInterface, GLenum pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions23glGetProgramInterfaceivEjjjPi(
    QOpenGLExtraFunctions *self,
    GLuint program,
    GLenum programInterface,
    GLenum pname,
    GLint *params) {
  self->glGetProgramInterfaceiv(program, programInterface, pname, params);
}

//  GLuint QOpenGLExtraFunctions::glGetProgramResourceIndex(GLuint program,
//      GLenum programInterface, const GLchar *name)
extern "C" Q_DECL_EXPORT
GLuint ritual_ZN21QOpenGLExtraFunctions25glGetProgramResourceIndexEjjPKc(
    QOpenGLExtraFunctions *self,
    GLuint program,
    GLenum programInterface,
    const GLchar *name) {
  return self->glGetProgramResourceIndex(program, programInterface, name);
}

//  void QOpenGLExtraFunctions::glGetProgramResourceName(GLuint program,
//      GLenum programInterface, GLuint index, GLsizei bufSize, GLsizei
//      *length, GLchar *name)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions24glGetProgramResourceNameEjjjiPiPc(
    QOpenGLExtraFunctions *self,
    GLuint program,
    GLenum programInterface,
    GLuint index,
    GLsizei bufSize,
    GLsizei *length,
    GLchar *name) {
  self->glGetProgramResourceName(
      program,
      programInterface,
      index,
      bufSize,
      length,
      name);
}

//  void QOpenGLExtraFunctions::glGetProgramResourceiv(GLuint program, GLenum
//      programInterface, GLuint index, GLsizei propCount, const GLenum
//      *props, GLsizei bufSize, GLsizei *length, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions22glGetProgramResourceivEjjjiPKjiPiS2_(
    QOpenGLExtraFunctions *self,
    GLuint program,
    GLenum programInterface,
    GLuint index,
    GLsizei propCount,
    const GLenum *props,
    GLsizei bufSize,
    GLsizei *length,
    GLint *params) {
  self->glGetProgramResourceiv(
      program,
      programInterface,
      index,
      propCount,
      props,
      bufSize,
      length,
      params);
}

//  GLint QOpenGLExtraFunctions::glGetProgramResourceLocation(GLuint program,
//      GLenum programInterface, const GLchar *name)
extern "C" Q_DECL_EXPORT
GLint ritual_ZN21QOpenGLExtraFunctions28glGetProgramResourceLocationEjjPKc(
    QOpenGLExtraFunctions *self,
    GLuint program,
    GLenum programInterface,
    const GLchar *name) {
  return self->glGetProgramResourceLocation(program, programInterface, name);
}

//  void QOpenGLExtraFunctions::glUseProgramStages(GLuint pipeline,
//      GLbitfield stages, GLuint program)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions18glUseProgramStagesEjjj(
    QOpenGLExtraFunctions *self,
    GLuint pipeline,
    GLbitfield stages,
    GLuint program) {
  self->glUseProgramStages(pipeline, stages, program);
}

//  void QOpenGLExtraFunctions::glActiveShaderProgram(GLuint pipeline, GLuint
//      program)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions21glActiveShaderProgramEjj(
    QOpenGLExtraFunctions *self,
    GLuint pipeline,
    GLuint program) {
  self->glActiveShaderProgram(pipeline, program);
}

//  GLuint QOpenGLExtraFunctions::glCreateShaderProgramv(GLenum type, GLsizei
//      count, const GLchar *const *strings)
extern "C" Q_DECL_EXPORT
GLuint ritual_ZN21QOpenGLExtraFunctions22glCreateShaderProgramvEjiPKPKc(
    QOpenGLExtraFunctions *self,
    GLenum type,
    GLsizei count,
    const GLchar *const *strings) {
  return self->glCreateShaderProgramv(type, count, strings);
}

//  void QOpenGLExtraFunctions::glBindProgramPipeline(GLuint pipeline)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions21glBindProgramPipelineEj(
    QOpenGLExtraFunctions *self,
    GLuint pipeline) {
  self->glBindProgramPipeline(pipeline);
}

//  void QOpenGLExtraFunctions::glDeleteProgramPipelines(GLsizei n, const
//      GLuint *pipelines)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions24glDeleteProgramPipelinesEiPKj(
    QOpenGLExtraFunctions *self,
    GLsizei n,
    const GLuint *pipelines) {
  self->glDeleteProgramPipelines(n, pipelines);
}

//  void QOpenGLExtraFunctions::glGenProgramPipelines(GLsizei n, GLuint
//      *pipelines)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions21glGenProgramPipelinesEiPj(
    QOpenGLExtraFunctions *self,
    GLsizei n,
    GLuint *pipelines) {
  self->glGenProgramPipelines(n, pipelines);
}

//  GLboolean QOpenGLExtraFunctions::glIsProgramPipeline(GLuint pipeline)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN21QOpenGLExtraFunctions19glIsProgramPipelineEj(
    QOpenGLExtraFunctions *self,
    GLuint pipeline) {
  return self->glIsProgramPipeline(pipeline);
}

//  void QOpenGLExtraFunctions::glGetProgramPipelineiv(GLuint pipeline,
//      GLenum pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions22glGetProgramPipelineivEjjPi(
    QOpenGLExtraFunctions *self,
    GLuint pipeline,
    GLenum pname,
    GLint *params) {
  self->glGetProgramPipelineiv(pipeline, pname, params);
}

//  void QOpenGLExtraFunctions::glProgramUniform1i(GLuint program, GLint
//      location, GLint v0)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions18glProgramUniform1iEjii(
    QOpenGLExtraFunctions *self,
    GLuint program,
    GLint location,
    GLint v0) {
  self->glProgramUniform1i(program, location, v0);
}

//  void QOpenGLExtraFunctions::glProgramUniform2i(GLuint program, GLint
//      location, GLint v0, GLint v1)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions18glProgramUniform2iEjiii(
    QOpenGLExtraFunctions *self,
    GLuint program,
    GLint location,
    GLint v0,
    GLint v1) {
  self->glProgramUniform2i(program, location, v0, v1);
}

//  void QOpenGLExtraFunctions::glProgramUniform3i(GLuint program, GLint
//      location, GLint v0, GLint v1, GLint v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions18glProgramUniform3iEjiiii(
    QOpenGLExtraFunctions *self,
    GLuint program,
    GLint location,
    GLint v0,
    GLint v1,
    GLint v2) {
  self->glProgramUniform3i(program, location, v0, v1, v2);
}

//  void QOpenGLExtraFunctions::glProgramUniform4i(GLuint program, GLint
//      location, GLint v0, GLint v1, GLint v2, GLint v3)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions18glProgramUniform4iEjiiiii(
    QOpenGLExtraFunctions *self,
    GLuint program,
    GLint location,
    GLint v0,
    GLint v1,
    GLint v2,
    GLint v3) {
  self->glProgramUniform4i(program, location, v0, v1, v2, v3);
}

//  void QOpenGLExtraFunctions::glProgramUniform1ui(GLuint program, GLint
//      location, GLuint v0)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions19glProgramUniform1uiEjij(
    QOpenGLExtraFunctions *self,
    GLuint program,
    GLint location,
    GLuint v0) {
  self->glProgramUniform1ui(program, location, v0);
}

//  void QOpenGLExtraFunctions::glProgramUniform2ui(GLuint program, GLint
//      location, GLuint v0, GLuint v1)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions19glProgramUniform2uiEjijj(
    QOpenGLExtraFunctions *self,
    GLuint program,
    GLint location,
    GLuint v0,
    GLuint v1) {
  self->glProgramUniform2ui(program, location, v0, v1);
}

//  void QOpenGLExtraFunctions::glProgramUniform3ui(GLuint program, GLint
//      location, GLuint v0, GLuint v1, GLuint v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions19glProgramUniform3uiEjijjj(
    QOpenGLExtraFunctions *self,
    GLuint program,
    GLint location,
    GLuint v0,
    GLuint v1,
    GLuint v2) {
  self->glProgramUniform3ui(program, location, v0, v1, v2);
}

//  void QOpenGLExtraFunctions::glProgramUniform4ui(GLuint program, GLint
//      location, GLuint v0, GLuint v1, GLuint v2, GLuint v3)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions19glProgramUniform4uiEjijjjj(
    QOpenGLExtraFunctions *self,
    GLuint program,
    GLint location,
    GLuint v0,
    GLuint v1,
    GLuint v2,
    GLuint v3) {
  self->glProgramUniform4ui(program, location, v0, v1, v2, v3);
}

//  void QOpenGLExtraFunctions::glProgramUniform1f(GLuint program, GLint
//      location, GLfloat v0)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions18glProgramUniform1fEjif(
    QOpenGLExtraFunctions *self,
    GLuint program,
    GLint location,
    GLfloat v0) {
  self->glProgramUniform1f(program, location, v0);
}

//  void QOpenGLExtraFunctions::glProgramUniform2f(GLuint program, GLint
//      location, GLfloat v0, GLfloat v1)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions18glProgramUniform2fEjiff(
    QOpenGLExtraFunctions *self,
    GLuint program,
    GLint location,
    GLfloat v0,
    GLfloat v1) {
  self->glProgramUniform2f(program, location, v0, v1);
}

//  void QOpenGLExtraFunctions::glProgramUniform3f(GLuint program, GLint
//      location, GLfloat v0, GLfloat v1, GLfloat v2)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions18glProgramUniform3fEjifff(
    QOpenGLExtraFunctions *self,
    GLuint program,
    GLint location,
    GLfloat v0,
    GLfloat v1,
    GLfloat v2) {
  self->glProgramUniform3f(program, location, v0, v1, v2);
}

//  void QOpenGLExtraFunctions::glProgramUniform4f(GLuint program, GLint
//      location, GLfloat v0, GLfloat v1, GLfloat v2, GLfloat v3)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions18glProgramUniform4fEjiffff(
    QOpenGLExtraFunctions *self,
    GLuint program,
    GLint location,
    GLfloat v0,
    GLfloat v1,
    GLfloat v2,
    GLfloat v3) {
  self->glProgramUniform4f(program, location, v0, v1, v2, v3);
}

//  void QOpenGLExtraFunctions::glProgramUniform1iv(GLuint program, GLint
//      location, GLsizei count, const GLint *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions19glProgramUniform1ivEjiiPKi(
    QOpenGLExtraFunctions *self,
    GLuint program,
    GLint location,
    GLsizei count,
    const GLint *value) {
  self->glProgramUniform1iv(program, location, count, value);
}

//  void QOpenGLExtraFunctions::glProgramUniform2iv(GLuint program, GLint
//      location, GLsizei count, const GLint *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions19glProgramUniform2ivEjiiPKi(
    QOpenGLExtraFunctions *self,
    GLuint program,
    GLint location,
    GLsizei count,
    const GLint *value) {
  self->glProgramUniform2iv(program, location, count, value);
}

//  void QOpenGLExtraFunctions::glProgramUniform3iv(GLuint program, GLint
//      location, GLsizei count, const GLint *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions19glProgramUniform3ivEjiiPKi(
    QOpenGLExtraFunctions *self,
    GLuint program,
    GLint location,
    GLsizei count,
    const GLint *value) {
  self->glProgramUniform3iv(program, location, count, value);
}

//  void QOpenGLExtraFunctions::glProgramUniform4iv(GLuint program, GLint
//      location, GLsizei count, const GLint *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions19glProgramUniform4ivEjiiPKi(
    QOpenGLExtraFunctions *self,
    GLuint program,
    GLint location,
    GLsizei count,
    const GLint *value) {
  self->glProgramUniform4iv(program, location, count, value);
}

//  void QOpenGLExtraFunctions::glProgramUniform1uiv(GLuint program, GLint
//      location, GLsizei count, const GLuint *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions20glProgramUniform1uivEjiiPKj(
    QOpenGLExtraFunctions *self,
    GLuint program,
    GLint location,
    GLsizei count,
    const GLuint *value) {
  self->glProgramUniform1uiv(program, location, count, value);
}

//  void QOpenGLExtraFunctions::glProgramUniform2uiv(GLuint program, GLint
//      location, GLsizei count, const GLuint *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions20glProgramUniform2uivEjiiPKj(
    QOpenGLExtraFunctions *self,
    GLuint program,
    GLint location,
    GLsizei count,
    const GLuint *value) {
  self->glProgramUniform2uiv(program, location, count, value);
}

//  void QOpenGLExtraFunctions::glProgramUniform3uiv(GLuint program, GLint
//      location, GLsizei count, const GLuint *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions20glProgramUniform3uivEjiiPKj(
    QOpenGLExtraFunctions *self,
    GLuint program,
    GLint location,
    GLsizei count,
    const GLuint *value) {
  self->glProgramUniform3uiv(program, location, count, value);
}

//  void QOpenGLExtraFunctions::glProgramUniform4uiv(GLuint program, GLint
//      location, GLsizei count, const GLuint *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions20glProgramUniform4uivEjiiPKj(
    QOpenGLExtraFunctions *self,
    GLuint program,
    GLint location,
    GLsizei count,
    const GLuint *value) {
  self->glProgramUniform4uiv(program, location, count, value);
}

//  void QOpenGLExtraFunctions::glProgramUniform1fv(GLuint program, GLint
//      location, GLsizei count, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions19glProgramUniform1fvEjiiPKf(
    QOpenGLExtraFunctions *self,
    GLuint program,
    GLint location,
    GLsizei count,
    const GLfloat *value) {
  self->glProgramUniform1fv(program, location, count, value);
}

//  void QOpenGLExtraFunctions::glProgramUniform2fv(GLuint program, GLint
//      location, GLsizei count, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions19glProgramUniform2fvEjiiPKf(
    QOpenGLExtraFunctions *self,
    GLuint program,
    GLint location,
    GLsizei count,
    const GLfloat *value) {
  self->glProgramUniform2fv(program, location, count, value);
}

//  void QOpenGLExtraFunctions::glProgramUniform3fv(GLuint program, GLint
//      location, GLsizei count, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions19glProgramUniform3fvEjiiPKf(
    QOpenGLExtraFunctions *self,
    GLuint program,
    GLint location,
    GLsizei count,
    const GLfloat *value) {
  self->glProgramUniform3fv(program, location, count, value);
}

//  void QOpenGLExtraFunctions::glProgramUniform4fv(GLuint program, GLint
//      location, GLsizei count, const GLfloat *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions19glProgramUniform4fvEjiiPKf(
    QOpenGLExtraFunctions *self,
    GLuint program,
    GLint location,
    GLsizei count,
    const GLfloat *value) {
  self->glProgramUniform4fv(program, location, count, value);
}

//  void QOpenGLExtraFunctions::glProgramUniformMatrix2fv(GLuint program,
//      GLint location, GLsizei count, GLboolean transpose, const GLfloat
//      *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions25glProgramUniformMatrix2fvEjiihPKf(
    QOpenGLExtraFunctions *self,
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

//  void QOpenGLExtraFunctions::glProgramUniformMatrix3fv(GLuint program,
//      GLint location, GLsizei count, GLboolean transpose, const GLfloat
//      *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions25glProgramUniformMatrix3fvEjiihPKf(
    QOpenGLExtraFunctions *self,
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

//  void QOpenGLExtraFunctions::glProgramUniformMatrix4fv(GLuint program,
//      GLint location, GLsizei count, GLboolean transpose, const GLfloat
//      *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions25glProgramUniformMatrix4fvEjiihPKf(
    QOpenGLExtraFunctions *self,
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

//  void QOpenGLExtraFunctions::glProgramUniformMatrix2x3fv(GLuint program,
//      GLint location, GLsizei count, GLboolean transpose, const GLfloat
//      *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions27glProgramUniformMatrix2x3fvEjiihPKf(
    QOpenGLExtraFunctions *self,
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

//  void QOpenGLExtraFunctions::glProgramUniformMatrix3x2fv(GLuint program,
//      GLint location, GLsizei count, GLboolean transpose, const GLfloat
//      *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions27glProgramUniformMatrix3x2fvEjiihPKf(
    QOpenGLExtraFunctions *self,
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

//  void QOpenGLExtraFunctions::glProgramUniformMatrix2x4fv(GLuint program,
//      GLint location, GLsizei count, GLboolean transpose, const GLfloat
//      *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions27glProgramUniformMatrix2x4fvEjiihPKf(
    QOpenGLExtraFunctions *self,
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

//  void QOpenGLExtraFunctions::glProgramUniformMatrix4x2fv(GLuint program,
//      GLint location, GLsizei count, GLboolean transpose, const GLfloat
//      *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions27glProgramUniformMatrix4x2fvEjiihPKf(
    QOpenGLExtraFunctions *self,
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

//  void QOpenGLExtraFunctions::glProgramUniformMatrix3x4fv(GLuint program,
//      GLint location, GLsizei count, GLboolean transpose, const GLfloat
//      *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions27glProgramUniformMatrix3x4fvEjiihPKf(
    QOpenGLExtraFunctions *self,
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

//  void QOpenGLExtraFunctions::glProgramUniformMatrix4x3fv(GLuint program,
//      GLint location, GLsizei count, GLboolean transpose, const GLfloat
//      *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions27glProgramUniformMatrix4x3fvEjiihPKf(
    QOpenGLExtraFunctions *self,
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

//  void QOpenGLExtraFunctions::glValidateProgramPipeline(GLuint pipeline)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions25glValidateProgramPipelineEj(
    QOpenGLExtraFunctions *self,
    GLuint pipeline) {
  self->glValidateProgramPipeline(pipeline);
}

//  void QOpenGLExtraFunctions::glGetProgramPipelineInfoLog(GLuint pipeline,
//      GLsizei bufSize, GLsizei *length, GLchar *infoLog)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions27glGetProgramPipelineInfoLogEjiPiPc(
    QOpenGLExtraFunctions *self,
    GLuint pipeline,
    GLsizei bufSize,
    GLsizei *length,
    GLchar *infoLog) {
  self->glGetProgramPipelineInfoLog(pipeline, bufSize, length, infoLog);
}

//  void QOpenGLExtraFunctions::glBindImageTexture(GLuint unit, GLuint
//      texture, GLint level, GLboolean layered, GLint layer, GLenum access,
//      GLenum format)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions18glBindImageTextureEjjihijj(
    QOpenGLExtraFunctions *self,
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

//  void QOpenGLExtraFunctions::glGetBooleani_v(GLenum target, GLuint index,
//      GLboolean *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions15glGetBooleani_vEjjPh(
    QOpenGLExtraFunctions *self,
    GLenum target,
    GLuint index,
    GLboolean *data) {
  self->glGetBooleani_v(target, index, data);
}

//  void QOpenGLExtraFunctions::glMemoryBarrier(GLbitfield barriers)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions15glMemoryBarrierEj(
    QOpenGLExtraFunctions *self,
    GLbitfield barriers) {
  self->glMemoryBarrier(barriers);
}

//  void QOpenGLExtraFunctions::glMemoryBarrierByRegion(GLbitfield barriers)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions23glMemoryBarrierByRegionEj(
    QOpenGLExtraFunctions *self,
    GLbitfield barriers) {
  self->glMemoryBarrierByRegion(barriers);
}

//  void QOpenGLExtraFunctions::glTexStorage2DMultisample(GLenum target,
//      GLsizei samples, GLenum internalformat, GLsizei width, GLsizei
//      height, GLboolean fixedsamplelocations)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions25glTexStorage2DMultisampleEjijiih(
    QOpenGLExtraFunctions *self,
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

//  void QOpenGLExtraFunctions::glGetMultisamplefv(GLenum pname, GLuint
//      index, GLfloat *val)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions18glGetMultisamplefvEjjPf(
    QOpenGLExtraFunctions *self,
    GLenum pname,
    GLuint index,
    GLfloat *val) {
  self->glGetMultisamplefv(pname, index, val);
}

//  void QOpenGLExtraFunctions::glSampleMaski(GLuint maskNumber, GLbitfield
//      mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions13glSampleMaskiEjj(
    QOpenGLExtraFunctions *self,
    GLuint maskNumber,
    GLbitfield mask) {
  self->glSampleMaski(maskNumber, mask);
}

//  void QOpenGLExtraFunctions::glGetTexLevelParameteriv(GLenum target, GLint
//      level, GLenum pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions24glGetTexLevelParameterivEjijPi(
    QOpenGLExtraFunctions *self,
    GLenum target,
    GLint level,
    GLenum pname,
    GLint *params) {
  self->glGetTexLevelParameteriv(target, level, pname, params);
}

//  void QOpenGLExtraFunctions::glGetTexLevelParameterfv(GLenum target, GLint
//      level, GLenum pname, GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions24glGetTexLevelParameterfvEjijPf(
    QOpenGLExtraFunctions *self,
    GLenum target,
    GLint level,
    GLenum pname,
    GLfloat *params) {
  self->glGetTexLevelParameterfv(target, level, pname, params);
}

//  void QOpenGLExtraFunctions::glBindVertexBuffer(GLuint bindingindex,
//      GLuint buffer, GLintptr offset, GLsizei stride)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions18glBindVertexBufferEjjli(
    QOpenGLExtraFunctions *self,
    GLuint bindingindex,
    GLuint buffer,
    long long offset,
    GLsizei stride) {
  self->glBindVertexBuffer(bindingindex, buffer, offset, stride);
}

//  void QOpenGLExtraFunctions::glVertexAttribFormat(GLuint attribindex,
//      GLint size, GLenum type, GLboolean normalized, GLuint relativeoffset)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions20glVertexAttribFormatEjijhj(
    QOpenGLExtraFunctions *self,
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

//  void QOpenGLExtraFunctions::glVertexAttribIFormat(GLuint attribindex,
//      GLint size, GLenum type, GLuint relativeoffset)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions21glVertexAttribIFormatEjijj(
    QOpenGLExtraFunctions *self,
    GLuint attribindex,
    GLint size,
    GLenum type,
    GLuint relativeoffset) {
  self->glVertexAttribIFormat(attribindex, size, type, relativeoffset);
}

//  void QOpenGLExtraFunctions::glVertexAttribBinding(GLuint attribindex,
//      GLuint bindingindex)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions21glVertexAttribBindingEjj(
    QOpenGLExtraFunctions *self,
    GLuint attribindex,
    GLuint bindingindex) {
  self->glVertexAttribBinding(attribindex, bindingindex);
}

//  void QOpenGLExtraFunctions::glVertexBindingDivisor(GLuint bindingindex,
//      GLuint divisor)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions22glVertexBindingDivisorEjj(
    QOpenGLExtraFunctions *self,
    GLuint bindingindex,
    GLuint divisor) {
  self->glVertexBindingDivisor(bindingindex, divisor);
}

//  void QOpenGLExtraFunctions::glBlendBarrier()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions14glBlendBarrierEv(
    QOpenGLExtraFunctions *self) {
  self->glBlendBarrier();
}

//  void QOpenGLExtraFunctions::glCopyImageSubData(GLuint srcName, GLenum
//      srcTarget, GLint srcLevel, GLint srcX, GLint srcY, GLint srcZ, GLuint
//      dstName, GLenum dstTarget, GLint dstLevel, GLint dstX, GLint dstY,
//      GLint dstZ, GLsizei srcWidth, GLsizei srcHeight, GLsizei srcDepth)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions18glCopyImageSubDataEjjiiiijjiiiiiii(
    QOpenGLExtraFunctions *self,
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

//  void QOpenGLExtraFunctions::glDebugMessageControl(GLenum source, GLenum
//      type, GLenum severity, GLsizei count, const GLuint *ids, GLboolean
//      enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions21glDebugMessageControlEjjjiPKjh(
    QOpenGLExtraFunctions *self,
    GLenum source,
    GLenum type,
    GLenum severity,
    GLsizei count,
    const GLuint *ids,
    GLboolean enabled) {
  self->glDebugMessageControl(source, type, severity, count, ids, enabled);
}

//  void QOpenGLExtraFunctions::glDebugMessageInsert(GLenum source, GLenum
//      type, GLuint id, GLenum severity, GLsizei length, const GLchar *buf)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions20glDebugMessageInsertEjjjjiPKc(
    QOpenGLExtraFunctions *self,
    GLenum source,
    GLenum type,
    GLuint id,
    GLenum severity,
    GLsizei length,
    const GLchar *buf) {
  self->glDebugMessageInsert(source, type, id, severity, length, buf);
}

//  void QOpenGLExtraFunctions::glDebugMessageCallback(GLDEBUGPROC callback,
//      const void *userParam)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions22glDebugMessageCallbackEPFvjjjjiPKcPKvES3_(
    QOpenGLExtraFunctions *self,
    void *callback,
    const void *userParam) {
  self->glDebugMessageCallback(
      reinterpret_cast<GLDEBUGPROC>(callback),
      userParam);
}

//  GLuint QOpenGLExtraFunctions::glGetDebugMessageLog(GLuint count, GLsizei
//      bufSize, GLenum *sources, GLenum *types, GLuint *ids, GLenum
//      *severities, GLsizei *lengths, GLchar *messageLog)
extern "C" Q_DECL_EXPORT
GLuint ritual_ZN21QOpenGLExtraFunctions20glGetDebugMessageLogEjiPjS0_S0_S0_PiPc(
    QOpenGLExtraFunctions *self,
    GLuint count,
    GLsizei bufSize,
    GLenum *sources,
    GLenum *types,
    GLuint *ids,
    GLenum *severities,
    GLsizei *lengths,
    GLchar *messageLog) {
  return self->glGetDebugMessageLog(
      count,
      bufSize,
      sources,
      types,
      ids,
      severities,
      lengths,
      messageLog);
}

//  void QOpenGLExtraFunctions::glPushDebugGroup(GLenum source, GLuint id,
//      GLsizei length, const GLchar *message)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions16glPushDebugGroupEjjiPKc(
    QOpenGLExtraFunctions *self,
    GLenum source,
    GLuint id,
    GLsizei length,
    const GLchar *message) {
  self->glPushDebugGroup(source, id, length, message);
}

//  void QOpenGLExtraFunctions::glPopDebugGroup()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions15glPopDebugGroupEv(
    QOpenGLExtraFunctions *self) {
  self->glPopDebugGroup();
}

//  void QOpenGLExtraFunctions::glObjectLabel(GLenum identifier, GLuint name,
//      GLsizei length, const GLchar *label)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions13glObjectLabelEjjiPKc(
    QOpenGLExtraFunctions *self,
    GLenum identifier,
    GLuint name,
    GLsizei length,
    const GLchar *label) {
  self->glObjectLabel(identifier, name, length, label);
}

//  void QOpenGLExtraFunctions::glGetObjectLabel(GLenum identifier, GLuint
//      name, GLsizei bufSize, GLsizei *length, GLchar *label)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions16glGetObjectLabelEjjiPiPc(
    QOpenGLExtraFunctions *self,
    GLenum identifier,
    GLuint name,
    GLsizei bufSize,
    GLsizei *length,
    GLchar *label) {
  self->glGetObjectLabel(identifier, name, bufSize, length, label);
}

//  void QOpenGLExtraFunctions::glObjectPtrLabel(const void *ptr, GLsizei
//      length, const GLchar *label)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions16glObjectPtrLabelEPKviPKc(
    QOpenGLExtraFunctions *self,
    const void *ptr,
    GLsizei length,
    const GLchar *label) {
  self->glObjectPtrLabel(ptr, length, label);
}

//  void QOpenGLExtraFunctions::glGetObjectPtrLabel(const void *ptr, GLsizei
//      bufSize, GLsizei *length, GLchar *label)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions19glGetObjectPtrLabelEPKviPiPc(
    QOpenGLExtraFunctions *self,
    const void *ptr,
    GLsizei bufSize,
    GLsizei *length,
    GLchar *label) {
  self->glGetObjectPtrLabel(ptr, bufSize, length, label);
}

//  void QOpenGLExtraFunctions::glGetPointerv(GLenum pname, void **params)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions13glGetPointervEjPPv(
    QOpenGLExtraFunctions *self,
    GLenum pname,
    void **params) {
  self->glGetPointerv(pname, params);
}

//  void QOpenGLExtraFunctions::glEnablei(GLenum target, GLuint index)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions9glEnableiEjj(
    QOpenGLExtraFunctions *self,
    GLenum target,
    GLuint index) {
  self->glEnablei(target, index);
}

//  void QOpenGLExtraFunctions::glDisablei(GLenum target, GLuint index)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions10glDisableiEjj(
    QOpenGLExtraFunctions *self,
    GLenum target,
    GLuint index) {
  self->glDisablei(target, index);
}

//  void QOpenGLExtraFunctions::glBlendEquationi(GLuint buf, GLenum mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions16glBlendEquationiEjj(
    QOpenGLExtraFunctions *self,
    GLuint buf,
    GLenum mode) {
  self->glBlendEquationi(buf, mode);
}

//  void QOpenGLExtraFunctions::glBlendEquationSeparatei(GLuint buf, GLenum
//      modeRGB, GLenum modeAlpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions24glBlendEquationSeparateiEjjj(
    QOpenGLExtraFunctions *self,
    GLuint buf,
    GLenum modeRGB,
    GLenum modeAlpha) {
  self->glBlendEquationSeparatei(buf, modeRGB, modeAlpha);
}

//  void QOpenGLExtraFunctions::glBlendFunci(GLuint buf, GLenum src, GLenum
//      dst)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions12glBlendFunciEjjj(
    QOpenGLExtraFunctions *self,
    GLuint buf,
    GLenum src,
    GLenum dst) {
  self->glBlendFunci(buf, src, dst);
}

//  void QOpenGLExtraFunctions::glBlendFuncSeparatei(GLuint buf, GLenum
//      srcRGB, GLenum dstRGB, GLenum srcAlpha, GLenum dstAlpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions20glBlendFuncSeparateiEjjjjj(
    QOpenGLExtraFunctions *self,
    GLuint buf,
    GLenum srcRGB,
    GLenum dstRGB,
    GLenum srcAlpha,
    GLenum dstAlpha) {
  self->glBlendFuncSeparatei(buf, srcRGB, dstRGB, srcAlpha, dstAlpha);
}

//  void QOpenGLExtraFunctions::glColorMaski(GLuint index, GLboolean r,
//      GLboolean g, GLboolean b, GLboolean a)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions12glColorMaskiEjhhhh(
    QOpenGLExtraFunctions *self,
    GLuint index,
    GLboolean r,
    GLboolean g,
    GLboolean b,
    GLboolean a) {
  self->glColorMaski(index, r, g, b, a);
}

//  GLboolean QOpenGLExtraFunctions::glIsEnabledi(GLenum target, GLuint
//      index)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN21QOpenGLExtraFunctions12glIsEnablediEjj(
    QOpenGLExtraFunctions *self,
    GLenum target,
    GLuint index) {
  return self->glIsEnabledi(target, index);
}

//  void QOpenGLExtraFunctions::glDrawElementsBaseVertex(GLenum mode, GLsizei
//      count, GLenum type, const void *indices, GLint basevertex)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions24glDrawElementsBaseVertexEjijPKvi(
    QOpenGLExtraFunctions *self,
    GLenum mode,
    GLsizei count,
    GLenum type,
    const void *indices,
    GLint basevertex) {
  self->glDrawElementsBaseVertex(mode, count, type, indices, basevertex);
}

//  void QOpenGLExtraFunctions::glDrawRangeElementsBaseVertex(GLenum mode,
//      GLuint start, GLuint end, GLsizei count, GLenum type, const void
//      *indices, GLint basevertex)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions29glDrawRangeElementsBaseVertexEjjjijPKvi(
    QOpenGLExtraFunctions *self,
    GLenum mode,
    GLuint start,
    GLuint end,
    GLsizei count,
    GLenum type,
    const void *indices,
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

//  void QOpenGLExtraFunctions::glDrawElementsInstancedBaseVertex(GLenum
//      mode, GLsizei count, GLenum type, const void *indices, GLsizei
//      instancecount, GLint basevertex)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions33glDrawElementsInstancedBaseVertexEjijPKvii(
    QOpenGLExtraFunctions *self,
    GLenum mode,
    GLsizei count,
    GLenum type,
    const void *indices,
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

//  void QOpenGLExtraFunctions::glFramebufferTexture(GLenum target, GLenum
//      attachment, GLuint texture, GLint level)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions20glFramebufferTextureEjjji(
    QOpenGLExtraFunctions *self,
    GLenum target,
    GLenum attachment,
    GLuint texture,
    GLint level) {
  self->glFramebufferTexture(target, attachment, texture, level);
}

//  void QOpenGLExtraFunctions::glPrimitiveBoundingBox(GLfloat minX, GLfloat
//      minY, GLfloat minZ, GLfloat minW, GLfloat maxX, GLfloat maxY, GLfloat
//      maxZ, GLfloat maxW)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions22glPrimitiveBoundingBoxEffffffff(
    QOpenGLExtraFunctions *self,
    GLfloat minX,
    GLfloat minY,
    GLfloat minZ,
    GLfloat minW,
    GLfloat maxX,
    GLfloat maxY,
    GLfloat maxZ,
    GLfloat maxW) {
  self->glPrimitiveBoundingBox(
      minX,
      minY,
      minZ,
      minW,
      maxX,
      maxY,
      maxZ,
      maxW);
}

//  GLenum QOpenGLExtraFunctions::glGetGraphicsResetStatus()
extern "C" Q_DECL_EXPORT
GLenum ritual_ZN21QOpenGLExtraFunctions24glGetGraphicsResetStatusEv(
    QOpenGLExtraFunctions *self) {
  return self->glGetGraphicsResetStatus();
}

//  void QOpenGLExtraFunctions::glReadnPixels(GLint x, GLint y, GLsizei
//      width, GLsizei height, GLenum format, GLenum type, GLsizei bufSize,
//      void *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions13glReadnPixelsEiiiijjiPv(
    QOpenGLExtraFunctions *self,
    GLint x,
    GLint y,
    GLsizei width,
    GLsizei height,
    GLenum format,
    GLenum type,
    GLsizei bufSize,
    void *data) {
  self->glReadnPixels(x, y, width, height, format, type, bufSize, data);
}

//  void QOpenGLExtraFunctions::glGetnUniformfv(GLuint program, GLint
//      location, GLsizei bufSize, GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions15glGetnUniformfvEjiiPf(
    QOpenGLExtraFunctions *self,
    GLuint program,
    GLint location,
    GLsizei bufSize,
    GLfloat *params) {
  self->glGetnUniformfv(program, location, bufSize, params);
}

//  void QOpenGLExtraFunctions::glGetnUniformiv(GLuint program, GLint
//      location, GLsizei bufSize, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions15glGetnUniformivEjiiPi(
    QOpenGLExtraFunctions *self,
    GLuint program,
    GLint location,
    GLsizei bufSize,
    GLint *params) {
  self->glGetnUniformiv(program, location, bufSize, params);
}

//  void QOpenGLExtraFunctions::glGetnUniformuiv(GLuint program, GLint
//      location, GLsizei bufSize, GLuint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions16glGetnUniformuivEjiiPj(
    QOpenGLExtraFunctions *self,
    GLuint program,
    GLint location,
    GLsizei bufSize,
    GLuint *params) {
  self->glGetnUniformuiv(program, location, bufSize, params);
}

//  void QOpenGLExtraFunctions::glMinSampleShading(GLfloat value)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions18glMinSampleShadingEf(
    QOpenGLExtraFunctions *self,
    GLfloat value) {
  self->glMinSampleShading(value);
}

//  void QOpenGLExtraFunctions::glPatchParameteri(GLenum pname, GLint value)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions17glPatchParameteriEji(
    QOpenGLExtraFunctions *self,
    GLenum pname,
    GLint value) {
  self->glPatchParameteri(pname, value);
}

//  void QOpenGLExtraFunctions::glTexParameterIiv(GLenum target, GLenum
//      pname, const GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions17glTexParameterIivEjjPKi(
    QOpenGLExtraFunctions *self,
    GLenum target,
    GLenum pname,
    const GLint *params) {
  self->glTexParameterIiv(target, pname, params);
}

//  void QOpenGLExtraFunctions::glTexParameterIuiv(GLenum target, GLenum
//      pname, const GLuint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions18glTexParameterIuivEjjPKj(
    QOpenGLExtraFunctions *self,
    GLenum target,
    GLenum pname,
    const GLuint *params) {
  self->glTexParameterIuiv(target, pname, params);
}

//  void QOpenGLExtraFunctions::glGetTexParameterIiv(GLenum target, GLenum
//      pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions20glGetTexParameterIivEjjPi(
    QOpenGLExtraFunctions *self,
    GLenum target,
    GLenum pname,
    GLint *params) {
  self->glGetTexParameterIiv(target, pname, params);
}

//  void QOpenGLExtraFunctions::glGetTexParameterIuiv(GLenum target, GLenum
//      pname, GLuint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions21glGetTexParameterIuivEjjPj(
    QOpenGLExtraFunctions *self,
    GLenum target,
    GLenum pname,
    GLuint *params) {
  self->glGetTexParameterIuiv(target, pname, params);
}

//  void QOpenGLExtraFunctions::glSamplerParameterIiv(GLuint sampler, GLenum
//      pname, const GLint *param)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions21glSamplerParameterIivEjjPKi(
    QOpenGLExtraFunctions *self,
    GLuint sampler,
    GLenum pname,
    const GLint *param) {
  self->glSamplerParameterIiv(sampler, pname, param);
}

//  void QOpenGLExtraFunctions::glSamplerParameterIuiv(GLuint sampler, GLenum
//      pname, const GLuint *param)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions22glSamplerParameterIuivEjjPKj(
    QOpenGLExtraFunctions *self,
    GLuint sampler,
    GLenum pname,
    const GLuint *param) {
  self->glSamplerParameterIuiv(sampler, pname, param);
}

//  void QOpenGLExtraFunctions::glGetSamplerParameterIiv(GLuint sampler,
//      GLenum pname, GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions24glGetSamplerParameterIivEjjPi(
    QOpenGLExtraFunctions *self,
    GLuint sampler,
    GLenum pname,
    GLint *params) {
  self->glGetSamplerParameterIiv(sampler, pname, params);
}

//  void QOpenGLExtraFunctions::glGetSamplerParameterIuiv(GLuint sampler,
//      GLenum pname, GLuint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions25glGetSamplerParameterIuivEjjPj(
    QOpenGLExtraFunctions *self,
    GLuint sampler,
    GLenum pname,
    GLuint *params) {
  self->glGetSamplerParameterIuiv(sampler, pname, params);
}

//  void QOpenGLExtraFunctions::glTexBuffer(GLenum target, GLenum
//      internalformat, GLuint buffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions11glTexBufferEjjj(
    QOpenGLExtraFunctions *self,
    GLenum target,
    GLenum internalformat,
    GLuint buffer) {
  self->glTexBuffer(target, internalformat, buffer);
}

//  void QOpenGLExtraFunctions::glTexBufferRange(GLenum target, GLenum
//      internalformat, GLuint buffer, GLintptr offset, GLsizeiptr size)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions16glTexBufferRangeEjjjll(
    QOpenGLExtraFunctions *self,
    GLenum target,
    GLenum internalformat,
    GLuint buffer,
    long long offset,
    long long size) {
  self->glTexBufferRange(target, internalformat, buffer, offset, size);
}

//  void QOpenGLExtraFunctions::glTexStorage3DMultisample(GLenum target,
//      GLsizei samples, GLenum internalformat, GLsizei width, GLsizei
//      height, GLsizei depth, GLboolean fixedsamplelocations)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions25glTexStorage3DMultisampleEjijiiih(
    QOpenGLExtraFunctions *self,
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

//  bool QOpenGLExtraFunctions::isInitialized(const
//      QOpenGLExtraFunctionsPrivate *d)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QOpenGLExtraFunctions13isInitializedEPK28QOpenGLExtraFunctionsPrivate(
    const QOpenGLExtraFunctionsPrivate *d) {
  return QOpenGLExtraFunctions::isInitialized(d);
}

#endif  // !defined(QT_NO_OPENGL)
