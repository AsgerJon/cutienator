//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/6.12.0/QtOpenGL/private/qopenglframebufferobject_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtOpenGL/QtOpenGL>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtOpenGL/6.12.0/QtOpenGL/private/qopenglframebufferobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>

//  QOpenGLFramebufferObjectPrivate::ColorAttachment::ColorAttachment()
extern "C" Q_DECL_EXPORT
QOpenGLFramebufferObjectPrivate::ColorAttachment *ritual_ZN31QOpenGLFramebufferObjectPrivate15ColorAttachmentC1Ev() {
  return new QOpenGLFramebufferObjectPrivate::ColorAttachment();
}

//  QOpenGLFramebufferObjectPrivate::ColorAttachment::ColorAttachment(const
//      QSize &size, GLenum internalFormat)
extern "C" Q_DECL_EXPORT
QOpenGLFramebufferObjectPrivate::ColorAttachment *ritual_ZN31QOpenGLFramebufferObjectPrivate15ColorAttachmentC1ERK5QSizej(
    const QSize *size,
    GLenum internalFormat) {
  return new QOpenGLFramebufferObjectPrivate::ColorAttachment(
      *size,
      internalFormat);
}

//  QOpenGLFramebufferObjectPrivate::ColorAttachment::~ColorAttachment()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QOpenGLFramebufferObjectPrivate15ColorAttachmentD1Ev(
    QOpenGLFramebufferObjectPrivate::ColorAttachment *self) {
  delete self;
}
