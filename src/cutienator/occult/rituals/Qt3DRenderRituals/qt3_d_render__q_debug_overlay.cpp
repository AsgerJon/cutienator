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

//  void *Qt3DRender::QDebugOverlay::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender13QDebugOverlay11qt_metacastEPKc(
    Qt3DRender::QDebugOverlay *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DRender::QDebugOverlay::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender13QDebugOverlay11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DRender::QDebugOverlay *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
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

//  Qt3DRender::QDebugOverlay::QDebugOverlay(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QDebugOverlay *ritual_ZN10Qt3DRender13QDebugOverlayC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new Qt3DRender::QDebugOverlay(parent);
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
