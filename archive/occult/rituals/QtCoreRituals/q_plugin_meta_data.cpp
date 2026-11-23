//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qplugin.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qplugin.h>

//  quint8 QPluginMetaData::archRequirements()
extern "C" Q_DECL_EXPORT
quint8 ritual_ZN15QPluginMetaData16archRequirementsEv() {
  return QPluginMetaData::archRequirements();
}

//  QPluginMetaData::~QPluginMetaData()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPluginMetaDataD1Ev(QPluginMetaData *self) {
  delete self;
}
