//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qplugin.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qplugin.h>

//  QPluginMetaData::Header::~Header()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPluginMetaData6HeaderD1Ev(QPluginMetaData::Header *self) {
  delete self;
}
