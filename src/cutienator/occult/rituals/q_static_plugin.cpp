//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qplugin.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qplugin.h>
#include <QtCore/qjsonobject.h>

//  QJsonObject QStaticPlugin::metaData() const
extern "C" Q_DECL_EXPORT
QJsonObject *ritual_ZNK13QStaticPlugin8metaDataEv(
    const QStaticPlugin *self) {
  return new QJsonObject(self->metaData());
}

//  QStaticPlugin::~QStaticPlugin()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStaticPluginD1Ev(QStaticPlugin *self) {
  delete self;
}
