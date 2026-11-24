//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlNetwork/6.12.0/QtQmlNetwork/private/qqmlnetworkinformation_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlNetwork/QtQmlNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlNetwork/6.12.0/QtQmlNetwork/private/qqmlnetworkinformation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QQmlNetworkInformation::qt_qmlMarker_foreign()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQmlNetworkInformation20qt_qmlMarker_foreignEv(
    QQmlNetworkInformation *self) {
  self->qt_qmlMarker_foreign();
}

//  void QQmlNetworkInformation::qt_qmlMarker_singleton()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQmlNetworkInformation22qt_qmlMarker_singletonEv(
    QQmlNetworkInformation *self) {
  self->qt_qmlMarker_singleton();
}

//  QNetworkInformation *QQmlNetworkInformation::create(QQmlEngine *a0,
//      QJSEngine *a1)
extern "C" Q_DECL_EXPORT
QNetworkInformation *ritual_ZN22QQmlNetworkInformation6createEP10QQmlEngineP9QJSEngine(
    QQmlEngine *a0,
    QJSEngine *a1) {
  return QQmlNetworkInformation::create(a0, a1);
}

//  QQmlNetworkInformation::~QQmlNetworkInformation()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQmlNetworkInformationD1Ev(QQmlNetworkInformation *self) {
  delete self;
}
