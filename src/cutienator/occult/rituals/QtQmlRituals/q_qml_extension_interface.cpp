//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/qqmlextensioninterface.h, Qt 6.12.0. Changes made here are lost.
#include <QtQml/QtQml>
#include <QtQml/qqmlextensioninterface.h>

//  QQmlExtensionInterface::~QQmlExtensionInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQmlExtensionInterfaceD1Ev(QQmlExtensionInterface *self) {
  delete self;
}

//  void QQmlExtensionInterface::initializeEngine(QQmlEngine *engine, const
//      char *uri)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQmlExtensionInterface16initializeEngineEP10QQmlEnginePKc(
    QQmlExtensionInterface *self,
    QQmlEngine *engine,
    const char *uri) {
  self->initializeEngine(engine, uri);
}
