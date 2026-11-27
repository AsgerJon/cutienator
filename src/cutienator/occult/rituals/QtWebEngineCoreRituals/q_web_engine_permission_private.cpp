//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebEngineCore/6.12.0/QtWebEngineCore/private/qwebenginepermission_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtWebEngineCore/6.12.0/QtWebEngineCore/private/qtwebenginecoreglobal_p.h>
#include <QtWebEngineCore/QtWebEngineCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebEngineCore/6.12.0/QtWebEngineCore/private/qwebenginepermission_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qurl.h>

//  QWebEnginePermissionPrivate::QWebEnginePermissionPrivate()
extern "C" Q_DECL_EXPORT
QWebEnginePermissionPrivate *ritual_ZN27QWebEnginePermissionPrivateC1Ev() {
  return new QWebEnginePermissionPrivate();
}

//  QWebEnginePermissionPrivate::QWebEnginePermissionPrivate(const QUrl &a0,
//      QWebEnginePermission::PermissionType a1,
//      QtWebEngineCore::ProfileAdapter *a2, int a3, const std::string &a4)
extern "C" Q_DECL_EXPORT
QWebEnginePermissionPrivate *ritual_ZN27QWebEnginePermissionPrivateC1ERK4QUrlN20QWebEnginePermission14PermissionTypeEPN15QtWebEngineCore14ProfileAdapterEiRKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEE(
    const QUrl *a0,
    QWebEnginePermission::PermissionType a1,
    QtWebEngineCore::ProfileAdapter *a2,
    int a3,
    const std::string *a4) {
  return new QWebEnginePermissionPrivate(*a0, a1, a2, a3, *a4);
}

//  QWebEnginePermissionPrivate::~QWebEnginePermissionPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QWebEnginePermissionPrivateD1Ev(
    QWebEnginePermissionPrivate *self) {
  delete self;
}
