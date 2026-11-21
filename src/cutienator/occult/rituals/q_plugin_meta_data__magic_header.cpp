//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qplugin.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qplugin.h>

//  QPluginMetaData::MagicHeader::MagicHeader()
extern "C" Q_DECL_EXPORT
QPluginMetaData::MagicHeader *ritual_ZN15QPluginMetaData11MagicHeaderC1Ev() {
  return new QPluginMetaData::MagicHeader();
}

//  QPluginMetaData::MagicHeader::~MagicHeader()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPluginMetaData11MagicHeaderD1Ev(
    QPluginMetaData::MagicHeader *self) {
  delete self;
}
