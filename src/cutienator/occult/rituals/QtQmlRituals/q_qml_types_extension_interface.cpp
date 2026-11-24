//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/qqmlextensioninterface.h, Qt 6.12.0. Changes made here are lost.
#include <QtQml/QtQml>
#include <QtQml/qqmlextensioninterface.h>

//  QQmlTypesExtensionInterface::~QQmlTypesExtensionInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQmlTypesExtensionInterfaceD1Ev(
    QQmlTypesExtensionInterface *self) {
  delete self;
}

//  void QQmlTypesExtensionInterface::registerTypes(const char *uri)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQmlTypesExtensionInterface13registerTypesEPKc(
    QQmlTypesExtensionInterface *self,
    const char *uri) {
  self->registerTypes(uri);
}
