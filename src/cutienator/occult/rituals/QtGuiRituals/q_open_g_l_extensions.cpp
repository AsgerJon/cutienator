//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qopenglextensions_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(opengl)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qopenglextensions_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QOpenGLExtensionsPrivate *QOpenGLExtensions::d_func()
extern "C" Q_DECL_EXPORT
QOpenGLExtensionsPrivate *ritual_ZN17QOpenGLExtensions6d_funcEv(
    QOpenGLExtensions *self) {
  return self->d_func();
}

//  const QOpenGLExtensionsPrivate *QOpenGLExtensions::d_func() const
extern "C" Q_DECL_EXPORT
const QOpenGLExtensionsPrivate *ritual_ZNK17QOpenGLExtensions6d_funcEv(
    const QOpenGLExtensions *self) {
  return self->d_func();
}

//  QOpenGLExtensions::QOpenGLExtensions()
extern "C" Q_DECL_EXPORT
QOpenGLExtensions *ritual_ZN17QOpenGLExtensionsC1Ev() {
  return new QOpenGLExtensions();
}

//  QOpenGLExtensions::QOpenGLExtensions(QOpenGLContext *context)
extern "C" Q_DECL_EXPORT
QOpenGLExtensions *ritual_ZN17QOpenGLExtensionsC1EP14QOpenGLContext(
    QOpenGLContext *context) {
  return new QOpenGLExtensions(context);
}

//  QOpenGLExtensions::~QOpenGLExtensions()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QOpenGLExtensionsD1Ev(QOpenGLExtensions *self) {
  delete self;
}

//  OpenGLExtensions QOpenGLExtensions::openGLExtensions()
extern "C" Q_DECL_EXPORT
int ritual_ZN17QOpenGLExtensions16openGLExtensionsEv(
    QOpenGLExtensions *self) {
  return static_cast<int>(self->openGLExtensions().toInt());
}

//  bool
//      QOpenGLExtensions::hasOpenGLExtension(QOpenGLExtensions::OpenGLExtens
//      ion extension) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QOpenGLExtensions18hasOpenGLExtensionENS_15OpenGLExtensionE(
    const QOpenGLExtensions *self,
    QOpenGLExtensions::OpenGLExtension extension) {
  return self->hasOpenGLExtension(extension);
}

//  GLvoid *QOpenGLExtensions::glMapBuffer(GLenum target, GLenum access)
extern "C" Q_DECL_EXPORT
GLvoid *ritual_ZN17QOpenGLExtensions11glMapBufferEjj(
    QOpenGLExtensions *self,
    GLenum target,
    GLenum access) {
  return self->glMapBuffer(target, access);
}

//  void QOpenGLExtensions::glGetBufferSubData(GLenum target,
//      qopengl_GLintptr offset, qopengl_GLsizeiptr size, GLvoid *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QOpenGLExtensions18glGetBufferSubDataEjllPv(
    QOpenGLExtensions *self,
    GLenum target,
    long long offset,
    long long size,
    GLvoid *data) {
  self->glGetBufferSubData(target, offset, size, data);
}

//  void QOpenGLExtensions::flushShared()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QOpenGLExtensions11flushSharedEv(QOpenGLExtensions *self) {
  self->flushShared();
}

//  void QOpenGLExtensions::discardFramebuffer(GLenum target, GLsizei
//      numAttachments, const GLenum *attachments)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QOpenGLExtensions18discardFramebufferEjiPKj(
    QOpenGLExtensions *self,
    GLenum target,
    GLsizei numAttachments,
    const GLenum *attachments) {
  self->discardFramebuffer(target, numAttachments, attachments);
}

//  QOpenGLExtensionsPrivate *QOpenGLExtensions::d() const
extern "C" Q_DECL_EXPORT
QOpenGLExtensionsPrivate *ritual_ZNK17QOpenGLExtensions1dEv(
    const QOpenGLExtensions *self) {
  return self->d();
}

//  bool QOpenGLExtensions::isInitialized(const QOpenGLFunctionsPrivate *d)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QOpenGLExtensions13isInitializedEPK23QOpenGLFunctionsPrivate(
    const QOpenGLFunctionsPrivate *d) {
  return QOpenGLExtensions::isInitialized(d);
}

#endif  // QT_CONFIG(opengl)
