//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qmetaobjectbuilder_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qmetaobjectbuilder_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>

//  QMetaStringTable::QMetaStringTable(const QByteArray &className)
extern "C" Q_DECL_EXPORT
QMetaStringTable *ritual_ZN16QMetaStringTableC1ERK10QByteArray(
    const QByteArray *className) {
  return new QMetaStringTable(*className);
}

//  int QMetaStringTable::enter(const QByteArray &value)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QMetaStringTable5enterERK10QByteArray(
    QMetaStringTable *self,
    const QByteArray *value) {
  return self->enter(*value);
}

//  int QMetaStringTable::preferredAlignment()
extern "C" Q_DECL_EXPORT
int ritual_ZN16QMetaStringTable18preferredAlignmentEv() {
  return QMetaStringTable::preferredAlignment();
}

//  int QMetaStringTable::blobSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QMetaStringTable8blobSizeEv(const QMetaStringTable *self) {
  return self->blobSize();
}

//  void QMetaStringTable::writeBlob(char *out) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK16QMetaStringTable9writeBlobEPc(
    const QMetaStringTable *self,
    char *out) {
  self->writeBlob(out);
}
