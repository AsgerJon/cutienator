//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickgraphicsdevice_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickgraphicsdevice_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QQuickGraphicsDevicePrivate
//      *QQuickGraphicsDevicePrivate::get(QQuickGraphicsDevice *p)
extern "C" Q_DECL_EXPORT
QQuickGraphicsDevicePrivate *ritual_ZN27QQuickGraphicsDevicePrivate3getEP20QQuickGraphicsDevice(
    QQuickGraphicsDevice *p) {
  return QQuickGraphicsDevicePrivate::get(p);
}

//  const QQuickGraphicsDevicePrivate *QQuickGraphicsDevicePrivate::get(const
//      QQuickGraphicsDevice *p)
extern "C" Q_DECL_EXPORT
const QQuickGraphicsDevicePrivate *ritual_ZN27QQuickGraphicsDevicePrivate3getEPK20QQuickGraphicsDevice(
    const QQuickGraphicsDevice *p) {
  return QQuickGraphicsDevicePrivate::get(p);
}

//  QQuickGraphicsDevicePrivate::QQuickGraphicsDevicePrivate()
extern "C" Q_DECL_EXPORT
QQuickGraphicsDevicePrivate *ritual_ZN27QQuickGraphicsDevicePrivateC1Ev() {
  return new QQuickGraphicsDevicePrivate();
}

//  QQuickGraphicsDevicePrivate::QQuickGraphicsDevicePrivate(const
//      QQuickGraphicsDevicePrivate &other)
extern "C" Q_DECL_EXPORT
QQuickGraphicsDevicePrivate *ritual_ZN27QQuickGraphicsDevicePrivateC1ERKS_(
    const QQuickGraphicsDevicePrivate *other) {
  return new QQuickGraphicsDevicePrivate(*other);
}

//  QQuickGraphicsDevicePrivate::~QQuickGraphicsDevicePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickGraphicsDevicePrivateD1Ev(
    QQuickGraphicsDevicePrivate *self) {
  delete self;
}
