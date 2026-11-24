//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/6.12.0/QtOpenGL/private/qopenglframebufferobject_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtOpenGL/QtOpenGL>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtOpenGL/6.12.0/QtOpenGL/private/qopenglframebufferobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QOpenGLFramebufferObjectFormatPrivate::QOpenGLFramebufferObjectFormatPriv
//      ate()
extern "C" Q_DECL_EXPORT
QOpenGLFramebufferObjectFormatPrivate *ritual_ZN37QOpenGLFramebufferObjectFormatPrivateC1Ev() {
  return new QOpenGLFramebufferObjectFormatPrivate();
}

//  QOpenGLFramebufferObjectFormatPrivate::QOpenGLFramebufferObjectFormatPriv
//      ate(const QOpenGLFramebufferObjectFormatPrivate *other)
extern "C" Q_DECL_EXPORT
QOpenGLFramebufferObjectFormatPrivate *ritual_ZN37QOpenGLFramebufferObjectFormatPrivateC1EPKS_(
    const QOpenGLFramebufferObjectFormatPrivate *other) {
  return new QOpenGLFramebufferObjectFormatPrivate(other);
}

//  bool QOpenGLFramebufferObjectFormatPrivate::equals(const
//      QOpenGLFramebufferObjectFormatPrivate *other)
extern "C" Q_DECL_EXPORT
bool ritual_ZN37QOpenGLFramebufferObjectFormatPrivate6equalsEPKS_(
    QOpenGLFramebufferObjectFormatPrivate *self,
    const QOpenGLFramebufferObjectFormatPrivate *other) {
  return self->equals(other);
}

//  QOpenGLFramebufferObjectFormatPrivate::~QOpenGLFramebufferObjectFormatPri
//      vate()
extern "C" Q_DECL_EXPORT
void ritual_ZN37QOpenGLFramebufferObjectFormatPrivateD1Ev(
    QOpenGLFramebufferObjectFormatPrivate *self) {
  delete self;
}
