//  Written by dev_tooling.RitualGenerator from the records of QtRemoteObject
//  s/6.12.0/QtRemoteObjects/private/qremoteobjectcontainers_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtRemoteObjects/QtRemoteObjects>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectcontainers_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaassociation.h>
#include <QtCore/qbytearray.h>

//  QtROAssociativeContainer::QtROAssociativeContainer()
extern "C" Q_DECL_EXPORT
QtROAssociativeContainer *ritual_ZN24QtROAssociativeContainerC1Ev() {
  return new QtROAssociativeContainer();
}

//  QtROAssociativeContainer::QtROAssociativeContainer(const
//      QMetaAssociation::Iterable &map)
extern "C" Q_DECL_EXPORT
QtROAssociativeContainer *ritual_ZN24QtROAssociativeContainerC1ERKN22QtMetaContainerPrivate11AssociationE(
    const QtMetaContainerPrivate::Association *map) {
  return new QtROAssociativeContainer(*map);
}

//  void QtROAssociativeContainer::setTypes(const QByteArray &keyTypeName,
//      const QByteArray &valueTypeName)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QtROAssociativeContainer8setTypesERK10QByteArrayS2_(
    QtROAssociativeContainer *self,
    const QByteArray *keyTypeName,
    const QByteArray *valueTypeName) {
  self->setTypes(*keyTypeName, *valueTypeName);
}

//  QtROAssociativeContainer::~QtROAssociativeContainer()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QtROAssociativeContainerD1Ev(
    QtROAssociativeContainer *self) {
  delete self;
}
