//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qmetacontainer.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qmetacontainer.h>

//  QtMetaContainerPrivate::QMetaAssociationInterface::QMetaAssociationInterf
//      ace()
extern "C" Q_DECL_EXPORT
QtMetaContainerPrivate::QMetaAssociationInterface *ritual_ZN22QtMetaContainerPrivate25QMetaAssociationInterfaceC1Ev() {
  return new QtMetaContainerPrivate::QMetaAssociationInterface();
}

//  QtMetaContainerPrivate::QMetaAssociationInterface::~QMetaAssociationInter
//      face()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QtMetaContainerPrivate25QMetaAssociationInterfaceD1Ev(
    QtMetaContainerPrivate::QMetaAssociationInterface *self) {
  delete self;
}
