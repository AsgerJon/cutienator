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

//  QtMultimediaPrivate::DmaBufEglContext::DmaBufEglContext(QRhi *rhi)
extern "C" Q_DECL_EXPORT
QtMultimediaPrivate::DmaBufEglContext *ritual_ZN19QtMultimediaPrivate16DmaBufEglContextC1EP4QRhi(
    QRhi *rhi) {
  return new QtMultimediaPrivate::DmaBufEglContext(rhi);
}

//  bool QtMultimediaPrivate::DmaBufEglContext::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QtMultimediaPrivate16DmaBufEglContext7isValidEv(
    const QtMultimediaPrivate::DmaBufEglContext *self) {
  return self->isValid();
}

//  void QtMultimediaPrivate::DmaBufEglContext::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QtMultimediaPrivate16DmaBufEglContext10invalidateEv(
    QtMultimediaPrivate::DmaBufEglContext *self) {
  self->invalidate();
}

//  QOpenGLContext *QtMultimediaPrivate::DmaBufEglContext::glContext() const
extern "C" Q_DECL_EXPORT
QOpenGLContext *ritual_ZNK19QtMultimediaPrivate16DmaBufEglContext9glContextEv(
    const QtMultimediaPrivate::DmaBufEglContext *self) {
  return self->glContext();
}

//  EGLDisplay QtMultimediaPrivate::DmaBufEglContext::eglDisplay() const
extern "C" Q_DECL_EXPORT
EGLDisplay ritual_ZNK19QtMultimediaPrivate16DmaBufEglContext10eglDisplayEv(
    const QtMultimediaPrivate::DmaBufEglContext *self) {
  return self->eglDisplay();
}

//  QtMultimediaPrivate::DmaBufEglContext::~DmaBufEglContext()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QtMultimediaPrivate16DmaBufEglContextD1Ev(
    QtMultimediaPrivate::DmaBufEglContext *self) {
  delete self;
}

#endif  // QT_CONFIG(linux_dmabuf)
