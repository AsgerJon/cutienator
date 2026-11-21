//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qplugin.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qplugin.h>

//  QPluginMetaData::ElfNoteHeader::ElfNoteHeader(quint32 payloadSize)
extern "C" Q_DECL_EXPORT
QPluginMetaData::ElfNoteHeader *ritual_ZN15QPluginMetaData13ElfNoteHeaderC1Ej(
    quint32 payloadSize) {
  return new QPluginMetaData::ElfNoteHeader(payloadSize);
}

//  QPluginMetaData::ElfNoteHeader::~ElfNoteHeader()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPluginMetaData13ElfNoteHeaderD1Ev(
    QPluginMetaData::ElfNoteHeader *self) {
  delete self;
}
