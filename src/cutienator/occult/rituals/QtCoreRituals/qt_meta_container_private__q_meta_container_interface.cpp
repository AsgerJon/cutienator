//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qmetacontainer.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qmetacontainer.h>

//  QtMetaContainerPrivate::QMetaContainerInterface::QMetaContainerInterface(
//      )
extern "C" Q_DECL_EXPORT
QtMetaContainerPrivate::QMetaContainerInterface *ritual_ZN22QtMetaContainerPrivate23QMetaContainerInterfaceC1Ev() {
  return new QtMetaContainerPrivate::QMetaContainerInterface();
}

//  QtMetaContainerPrivate::QMetaContainerInterface::~QMetaContainerInterface
//      ()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QtMetaContainerPrivate23QMetaContainerInterfaceD1Ev(
    QtMetaContainerPrivate::QMetaContainerInterface *self) {
  delete self;
}
