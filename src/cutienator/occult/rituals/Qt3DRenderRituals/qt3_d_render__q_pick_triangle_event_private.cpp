//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/qpicktriangleevent_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/qpicktriangleevent_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt3DRender::QPickTriangleEventPrivate::QPickTriangleEventPrivate()
extern "C" Q_DECL_EXPORT
Qt3DRender::QPickTriangleEventPrivate *ritual_ZN10Qt3DRender25QPickTriangleEventPrivateC1Ev() {
  return new Qt3DRender::QPickTriangleEventPrivate();
}

//  const QPickTriangleEventPrivate
//      *Qt3DRender::QPickTriangleEventPrivate::get(const QPickTriangleEvent
//      *ev)
extern "C" Q_DECL_EXPORT
const Qt3DRender::QPickTriangleEventPrivate *ritual_ZN10Qt3DRender25QPickTriangleEventPrivate3getEPKNS_18QPickTriangleEventE(
    const Qt3DRender::QPickTriangleEvent *ev) {
  return Qt3DRender::QPickTriangleEventPrivate::get(ev);
}

//  QPickTriangleEvent *Qt3DRender::QPickTriangleEventPrivate::clone() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QPickTriangleEvent *ritual_ZNK10Qt3DRender25QPickTriangleEventPrivate5cloneEv(
    const Qt3DRender::QPickTriangleEventPrivate *self) {
  return self->clone();
}
