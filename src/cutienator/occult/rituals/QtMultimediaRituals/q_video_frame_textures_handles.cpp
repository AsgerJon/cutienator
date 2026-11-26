//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qhwvideobuffer_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qhwvideobuffer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QVideoFrameTexturesHandles::~QVideoFrameTexturesHandles()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QVideoFrameTexturesHandlesD1Ev(
    QVideoFrameTexturesHandles *self) {
  delete self;
}

//  quint64 QVideoFrameTexturesHandles::textureHandle(QRhi &a0, int a1)
extern "C" Q_DECL_EXPORT
quint64 ritual_ZN26QVideoFrameTexturesHandles13textureHandleER4QRhii(
    QVideoFrameTexturesHandles *self,
    QRhi *a0,
    int a1) {
  return self->textureHandle(*a0, a1);
}
