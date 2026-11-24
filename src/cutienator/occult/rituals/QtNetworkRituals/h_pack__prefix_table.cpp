//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/huffman_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/huffman_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  HPack::PrefixTable::PrefixTable()
extern "C" Q_DECL_EXPORT
HPack::PrefixTable *ritual_ZN5HPack11PrefixTableC1Ev() {
  return new HPack::PrefixTable();
}

//  HPack::PrefixTable::PrefixTable(quint32 prefix, quint32 index)
extern "C" Q_DECL_EXPORT
HPack::PrefixTable *ritual_ZN5HPack11PrefixTableC1Ejj(
    quint32 prefix,
    quint32 index) {
  return new HPack::PrefixTable(prefix, index);
}

//  quint32 HPack::PrefixTable::size() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK5HPack11PrefixTable4sizeEv(
    const HPack::PrefixTable *self) {
  return self->size();
}

//  HPack::PrefixTable::~PrefixTable()
extern "C" Q_DECL_EXPORT
void ritual_ZN5HPack11PrefixTableD1Ev(HPack::PrefixTable *self) {
  delete self;
}
