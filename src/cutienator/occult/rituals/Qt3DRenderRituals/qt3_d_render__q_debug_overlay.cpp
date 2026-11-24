//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/qdebugoverlay.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DRender/qdebugoverlay.h>
#include <QtCore/qstring.h>

//  const QMetaObject *Qt3DRender::QDebugOverlay::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender13QDebugOverlay10metaObjectEv(
    const Qt3DRender::QDebugOverlay *self) {
  return self->metaObject();
}

//  QString Qt3DRender::QDebugOverlay::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender13QDebugOverlay2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DRender::QDebugOverlay::tr(s, c, n));
}

//  QDebugOverlayPrivate *Qt3DRender::QDebugOverlay::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QDebugOverlayPrivate *ritual_ZN10Qt3DRender13QDebugOverlay6d_funcEv(
    Qt3DRender::QDebugOverlay *self) {
  return self->d_func();
}

//  const QDebugOverlayPrivate *Qt3DRender::QDebugOverlay::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QDebugOverlayPrivate *ritual_ZNK10Qt3DRender13QDebugOverlay6d_funcEv(
    const Qt3DRender::QDebugOverlay *self) {
  return self->d_func();
}
