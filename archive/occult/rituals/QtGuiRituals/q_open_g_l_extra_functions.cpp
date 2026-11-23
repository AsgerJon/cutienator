//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qopenglextrafunctions.h, Qt 6.12.0. Changes made here are lost.
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

//  void QOpenGLExtraFunctions::glBindVertexArray(GLuint array)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions17glBindVertexArrayEj(
    QOpenGLExtraFunctions *self,
    GLuint array) {
  self->glBindVertexArray(array);
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

//  void QOpenGLExtraFunctions::glBindProgramPipeline(GLuint pipeline)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions21glBindProgramPipelineEj(
    QOpenGLExtraFunctions *self,
    GLuint pipeline) {
  self->glBindProgramPipeline(pipeline);
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

//  void QOpenGLExtraFunctions::glValidateProgramPipeline(GLuint pipeline)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions25glValidateProgramPipelineEj(
    QOpenGLExtraFunctions *self,
    GLuint pipeline) {
  self->glValidateProgramPipeline(pipeline);
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

//  void QOpenGLExtraFunctions::glSampleMaski(GLuint maskNumber, GLbitfield
//      mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions13glSampleMaskiEjj(
    QOpenGLExtraFunctions *self,
    GLuint maskNumber,
    GLbitfield mask) {
  self->glSampleMaski(maskNumber, mask);
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

//  void QOpenGLExtraFunctions::glPopDebugGroup()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLExtraFunctions15glPopDebugGroupEv(
    QOpenGLExtraFunctions *self) {
  self->glPopDebugGroup();
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
