//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgrenderer_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgrenderer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSGRenderTarget::QSGRenderTarget()
extern "C" Q_DECL_EXPORT
QSGRenderTarget *ritual_ZN15QSGRenderTargetC1Ev() {
  return new QSGRenderTarget();
}

//  QSGRenderTarget::QSGRenderTarget(QRhiRenderTarget *rt,
//      QRhiRenderPassDescriptor *rpDesc, QRhiCommandBuffer *cb)
extern "C" Q_DECL_EXPORT
QSGRenderTarget *ritual_ZN15QSGRenderTargetC1EP16QRhiRenderTargetP24QRhiRenderPassDescriptorP17QRhiCommandBuffer(
    QRhiRenderTarget *rt,
    QRhiRenderPassDescriptor *rpDesc,
    QRhiCommandBuffer *cb) {
  return new QSGRenderTarget(rt, rpDesc, cb);
}

//  QSGRenderTarget::QSGRenderTarget(QPaintDevice *paintDevice)
extern "C" Q_DECL_EXPORT
QSGRenderTarget *ritual_ZN15QSGRenderTargetC1EP12QPaintDevice(
    QPaintDevice *paintDevice) {
  return new QSGRenderTarget(paintDevice);
}

//  QSGRenderTarget::~QSGRenderTarget()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSGRenderTargetD1Ev(QSGRenderTarget *self) {
  delete self;
}
