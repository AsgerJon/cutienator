//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/qqmlextensioninterface.h, Qt 6.12.0. Changes made here are lost.
#include <QtQml/QtQml>
#include <QtQml/qqmlextensioninterface.h>

//  QQmlEngineExtensionInterface::~QQmlEngineExtensionInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQmlEngineExtensionInterfaceD1Ev(
    QQmlEngineExtensionInterface *self) {
  delete self;
}

//  void QQmlEngineExtensionInterface::initializeEngine(QQmlEngine *engine,
//      const char *uri)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQmlEngineExtensionInterface16initializeEngineEP10QQmlEnginePKc(
    QQmlEngineExtensionInterface *self,
    QQmlEngine *engine,
    const char *uri) {
  self->initializeEngine(engine, uri);
}
