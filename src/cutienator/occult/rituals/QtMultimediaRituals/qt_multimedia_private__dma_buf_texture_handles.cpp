//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qdmabuftextureimporter_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtMultimedia/qtmultimediaglobal.h>
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#if QT_CONFIG(linux_dmabuf)
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qdmabuftextureimporter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <array>
#include <memory>

//  QtMultimediaPrivate::DmaBufTextureHandles::DmaBufTextureHandles(QRhi
//      &rhi, QOpenGLContext *glContext, int nPlanes, std::array<GLuint, 4>
//      textures, std::shared_ptr<void> parentKeepAlive)
extern "C" Q_DECL_EXPORT
QtMultimediaPrivate::DmaBufTextureHandles *ritual_ZN19QtMultimediaPrivate20DmaBufTextureHandlesC1ER4QRhiP14QOpenGLContextiSt5arrayIjLm4EESt10shared_ptrIvE(
    QRhi *rhi,
    QOpenGLContext *glContext,
    int nPlanes,
    const std::array<GLuint, 4> *textures,
    const std::shared_ptr<void> *parentKeepAlive) {
  return new QtMultimediaPrivate::DmaBufTextureHandles(
      *rhi,
      glContext,
      nPlanes,
      *textures,
      *parentKeepAlive);
}

//  QtMultimediaPrivate::DmaBufTextureHandles::~DmaBufTextureHandles()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QtMultimediaPrivate20DmaBufTextureHandlesD1Ev(
    QtMultimediaPrivate::DmaBufTextureHandles *self) {
  delete self;
}

//  quint64 QtMultimediaPrivate::DmaBufTextureHandles::textureHandle(QRhi
//      &a0, int plane)
extern "C" Q_DECL_EXPORT
quint64 ritual_ZN19QtMultimediaPrivate20DmaBufTextureHandles13textureHandleER4QRhii(
    QtMultimediaPrivate::DmaBufTextureHandles *self,
    QRhi *a0,
    int plane) {
  return self->textureHandle(*a0, plane);
}

#endif  // QT_CONFIG(linux_dmabuf)
