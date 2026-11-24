//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickgraphicsconfiguration_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickgraphicsconfiguration_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QQuickGraphicsConfigurationPrivate
//      *QQuickGraphicsConfigurationPrivate::get(QQuickGraphicsConfiguration
//      *p)
extern "C" Q_DECL_EXPORT
QQuickGraphicsConfigurationPrivate *ritual_ZN34QQuickGraphicsConfigurationPrivate3getEP27QQuickGraphicsConfiguration(
    QQuickGraphicsConfiguration *p) {
  return QQuickGraphicsConfigurationPrivate::get(p);
}

//  const QQuickGraphicsConfigurationPrivate
//      *QQuickGraphicsConfigurationPrivate::get(const
//      QQuickGraphicsConfiguration *p)
extern "C" Q_DECL_EXPORT
const QQuickGraphicsConfigurationPrivate *ritual_ZN34QQuickGraphicsConfigurationPrivate3getEPK27QQuickGraphicsConfiguration(
    const QQuickGraphicsConfiguration *p) {
  return QQuickGraphicsConfigurationPrivate::get(p);
}

//  QQuickGraphicsConfigurationPrivate::QQuickGraphicsConfigurationPrivate()
extern "C" Q_DECL_EXPORT
QQuickGraphicsConfigurationPrivate *ritual_ZN34QQuickGraphicsConfigurationPrivateC1Ev() {
  return new QQuickGraphicsConfigurationPrivate();
}

//  QQuickGraphicsConfigurationPrivate::QQuickGraphicsConfigurationPrivate(co
//      nst QQuickGraphicsConfigurationPrivate &other)
extern "C" Q_DECL_EXPORT
QQuickGraphicsConfigurationPrivate *ritual_ZN34QQuickGraphicsConfigurationPrivateC1ERKS_(
    const QQuickGraphicsConfigurationPrivate *other) {
  return new QQuickGraphicsConfigurationPrivate(*other);
}

//  QQuickGraphicsConfigurationPrivate::~QQuickGraphicsConfigurationPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QQuickGraphicsConfigurationPrivateD1Ev(
    QQuickGraphicsConfigurationPrivate *self) {
  delete self;
}
