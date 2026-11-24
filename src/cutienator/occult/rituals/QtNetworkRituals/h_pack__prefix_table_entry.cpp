//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/huffman_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#if QT_CONFIG(http)
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/huffman_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  HPack::PrefixTableEntry::PrefixTableEntry()
extern "C" Q_DECL_EXPORT
HPack::PrefixTableEntry *ritual_ZN5HPack16PrefixTableEntryC1Ev() {
  return new HPack::PrefixTableEntry();
}

//  HPack::PrefixTableEntry::~PrefixTableEntry()
extern "C" Q_DECL_EXPORT
void ritual_ZN5HPack16PrefixTableEntryD1Ev(HPack::PrefixTableEntry *self) {
  delete self;
}

#endif  // QT_CONFIG(http)
