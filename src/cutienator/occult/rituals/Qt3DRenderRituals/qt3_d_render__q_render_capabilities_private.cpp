//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/qrendercapabilities_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/qrendercapabilities_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  Qt3DRender::QRenderCapabilitiesPrivate::QRenderCapabilitiesPrivate()
extern "C" Q_DECL_EXPORT
Qt3DRender::QRenderCapabilitiesPrivate *ritual_ZN10Qt3DRender26QRenderCapabilitiesPrivateC1Ev() {
  return new Qt3DRender::QRenderCapabilitiesPrivate();
}

//  QRenderCapabilities *Qt3DRender::QRenderCapabilitiesPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QRenderCapabilities *ritual_ZN10Qt3DRender26QRenderCapabilitiesPrivate6q_funcEv(
    Qt3DRender::QRenderCapabilitiesPrivate *self) {
  return self->q_func();
}

//  const QRenderCapabilities
//      *Qt3DRender::QRenderCapabilitiesPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QRenderCapabilities *ritual_ZNK10Qt3DRender26QRenderCapabilitiesPrivate6q_funcEv(
    const Qt3DRender::QRenderCapabilitiesPrivate *self) {
  return self->q_func();
}

//  const QRenderCapabilitiesPrivate
//      *Qt3DRender::QRenderCapabilitiesPrivate::get(const
//      QRenderCapabilities *q)
extern "C" Q_DECL_EXPORT
const Qt3DRender::QRenderCapabilitiesPrivate *ritual_ZN10Qt3DRender26QRenderCapabilitiesPrivate3getEPKNS_19QRenderCapabilitiesE(
    const Qt3DRender::QRenderCapabilities *q) {
  return Qt3DRender::QRenderCapabilitiesPrivate::get(q);
}

//  QString Qt3DRender::QRenderCapabilitiesPrivate::toString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10Qt3DRender26QRenderCapabilitiesPrivate8toStringEv(
    const Qt3DRender::QRenderCapabilitiesPrivate *self) {
  return new QString(self->toString());
}
