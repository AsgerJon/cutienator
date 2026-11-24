//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickrendertarget_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickrendertarget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QQuickRenderTargetPrivate
//      *QQuickRenderTargetPrivate::get(QQuickRenderTarget *rt)
extern "C" Q_DECL_EXPORT
QQuickRenderTargetPrivate *ritual_ZN25QQuickRenderTargetPrivate3getEP18QQuickRenderTarget(
    QQuickRenderTarget *rt) {
  return QQuickRenderTargetPrivate::get(rt);
}

//  const QQuickRenderTargetPrivate *QQuickRenderTargetPrivate::get(const
//      QQuickRenderTarget *rt)
extern "C" Q_DECL_EXPORT
const QQuickRenderTargetPrivate *ritual_ZN25QQuickRenderTargetPrivate3getEPK18QQuickRenderTarget(
    const QQuickRenderTarget *rt) {
  return QQuickRenderTargetPrivate::get(rt);
}

//  QQuickRenderTargetPrivate::QQuickRenderTargetPrivate()
extern "C" Q_DECL_EXPORT
QQuickRenderTargetPrivate *ritual_ZN25QQuickRenderTargetPrivateC1Ev() {
  return new QQuickRenderTargetPrivate();
}

//  QQuickRenderTargetPrivate::QQuickRenderTargetPrivate(const
//      QQuickRenderTargetPrivate &other)
extern "C" Q_DECL_EXPORT
QQuickRenderTargetPrivate *ritual_ZN25QQuickRenderTargetPrivateC1ERKS_(
    const QQuickRenderTargetPrivate *other) {
  return new QQuickRenderTargetPrivate(*other);
}

//  bool QQuickRenderTargetPrivate::resolve(QRhi *rhi,
//      QQuickWindowRenderTarget *dst)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QQuickRenderTargetPrivate7resolveEP4QRhiP24QQuickWindowRenderTarget(
    QQuickRenderTargetPrivate *self,
    QRhi *rhi,
    QQuickWindowRenderTarget *dst) {
  return self->resolve(rhi, dst);
}

//  QQuickRenderTargetPrivate::~QQuickRenderTargetPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickRenderTargetPrivateD1Ev(
    QQuickRenderTargetPrivate *self) {
  delete self;
}
