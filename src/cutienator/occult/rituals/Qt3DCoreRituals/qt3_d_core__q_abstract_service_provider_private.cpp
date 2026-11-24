//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/6.12.0/Qt3DCore/private/qabstractserviceprovider_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DCore/6.12.0/Qt3DCore/private/qt3dcore_global_p.h>
#include <Qt3DCore/Qt3DCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/6.12.0/Qt3DCore/private/qabstractserviceprovider_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  Qt3DCore::QAbstractServiceProviderPrivate::QAbstractServiceProviderPrivat
//      e(int type, const QString &description)
extern "C" Q_DECL_EXPORT
Qt3DCore::QAbstractServiceProviderPrivate *ritual_ZN8Qt3DCore31QAbstractServiceProviderPrivateC1EiRK7QString(
    int type,
    const QString *description) {
  return new Qt3DCore::QAbstractServiceProviderPrivate(type, *description);
}

//  QAbstractServiceProvider
//      *Qt3DCore::QAbstractServiceProviderPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DCore::QAbstractServiceProvider *ritual_ZN8Qt3DCore31QAbstractServiceProviderPrivate6q_funcEv(
    Qt3DCore::QAbstractServiceProviderPrivate *self) {
  return self->q_func();
}

//  const QAbstractServiceProvider
//      *Qt3DCore::QAbstractServiceProviderPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DCore::QAbstractServiceProvider *ritual_ZNK8Qt3DCore31QAbstractServiceProviderPrivate6q_funcEv(
    const Qt3DCore::QAbstractServiceProviderPrivate *self) {
  return self->q_func();
}
