//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qrhivaluemapper_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qrhivaluemapper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QRhiCallback::~QRhiCallback()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QRhiCallbackD1Ev(QRhiCallback *self) {
  delete self;
}

//  void QRhiCallback::registerCallback(QRhi &rhi)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QRhiCallback16registerCallbackER4QRhi(
    QRhiCallback *self,
    QRhi *rhi) {
  self->registerCallback(*rhi);
}

//  void QRhiCallback::onRhiCleanup(QRhi &rhi)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QRhiCallback12onRhiCleanupER4QRhi(
    QRhiCallback *self,
    QRhi *rhi) {
  self->onRhiCleanup(*rhi);
}
