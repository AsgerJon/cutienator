//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/rhi/qrhi.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/rhi/qrhi.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QRhiTextureUploadDescription::QRhiTextureUploadDescription()
extern "C" Q_DECL_EXPORT
QRhiTextureUploadDescription *ritual_ZN28QRhiTextureUploadDescriptionC1Ev() {
  return new QRhiTextureUploadDescription();
}

//  QRhiTextureUploadDescription::QRhiTextureUploadDescription(const
//      QRhiTextureUploadEntry &entry)
extern "C" Q_DECL_EXPORT
QRhiTextureUploadDescription *ritual_ZN28QRhiTextureUploadDescriptionC1ERK22QRhiTextureUploadEntry(
    const QRhiTextureUploadEntry *entry) {
  return new QRhiTextureUploadDescription(*entry);
}

//  const QRhiTextureUploadEntry
//      *QRhiTextureUploadDescription::cbeginEntries() const
extern "C" Q_DECL_EXPORT
const QRhiTextureUploadEntry *ritual_ZNK28QRhiTextureUploadDescription13cbeginEntriesEv(
    const QRhiTextureUploadDescription *self) {
  return self->cbeginEntries();
}

//  const QRhiTextureUploadEntry *QRhiTextureUploadDescription::cendEntries()
//      const
extern "C" Q_DECL_EXPORT
const QRhiTextureUploadEntry *ritual_ZNK28QRhiTextureUploadDescription11cendEntriesEv(
    const QRhiTextureUploadDescription *self) {
  return self->cendEntries();
}

//  const QRhiTextureUploadEntry
//      *QRhiTextureUploadDescription::entryAt(qsizetype index) const
extern "C" Q_DECL_EXPORT
const QRhiTextureUploadEntry *ritual_ZNK28QRhiTextureUploadDescription7entryAtEx(
    const QRhiTextureUploadDescription *self,
    qsizetype index) {
  return self->entryAt(index);
}

//  qsizetype QRhiTextureUploadDescription::entryCount() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK28QRhiTextureUploadDescription10entryCountEv(
    const QRhiTextureUploadDescription *self) {
  return self->entryCount();
}

//  QRhiTextureUploadDescription::~QRhiTextureUploadDescription()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QRhiTextureUploadDescriptionD1Ev(
    QRhiTextureUploadDescription *self) {
  delete self;
}
