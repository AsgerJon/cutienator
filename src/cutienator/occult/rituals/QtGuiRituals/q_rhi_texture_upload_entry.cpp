//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/rhi/qrhi.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/rhi/qrhi.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QRhiTextureUploadEntry::QRhiTextureUploadEntry()
extern "C" Q_DECL_EXPORT
QRhiTextureUploadEntry *ritual_ZN22QRhiTextureUploadEntryC1Ev() {
  return new QRhiTextureUploadEntry();
}

//  QRhiTextureUploadEntry::QRhiTextureUploadEntry(int layer, int level,
//      const QRhiTextureSubresourceUploadDescription &desc)
extern "C" Q_DECL_EXPORT
QRhiTextureUploadEntry *ritual_ZN22QRhiTextureUploadEntryC1EiiRK39QRhiTextureSubresourceUploadDescription(
    int layer,
    int level,
    const QRhiTextureSubresourceUploadDescription *desc) {
  return new QRhiTextureUploadEntry(layer, level, *desc);
}

//  int QRhiTextureUploadEntry::layer() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QRhiTextureUploadEntry5layerEv(
    const QRhiTextureUploadEntry *self) {
  return self->layer();
}

//  void QRhiTextureUploadEntry::setLayer(int layer)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QRhiTextureUploadEntry8setLayerEi(
    QRhiTextureUploadEntry *self,
    int layer) {
  self->setLayer(layer);
}

//  int QRhiTextureUploadEntry::level() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QRhiTextureUploadEntry5levelEv(
    const QRhiTextureUploadEntry *self) {
  return self->level();
}

//  void QRhiTextureUploadEntry::setLevel(int level)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QRhiTextureUploadEntry8setLevelEi(
    QRhiTextureUploadEntry *self,
    int level) {
  self->setLevel(level);
}

//  QRhiTextureSubresourceUploadDescription
//      QRhiTextureUploadEntry::description() const
extern "C" Q_DECL_EXPORT
QRhiTextureSubresourceUploadDescription *ritual_ZNK22QRhiTextureUploadEntry11descriptionEv(
    const QRhiTextureUploadEntry *self) {
  return new QRhiTextureSubresourceUploadDescription(self->description());
}

//  void QRhiTextureUploadEntry::setDescription(const
//      QRhiTextureSubresourceUploadDescription &desc)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QRhiTextureUploadEntry14setDescriptionERK39QRhiTextureSubresourceUploadDescription(
    QRhiTextureUploadEntry *self,
    const QRhiTextureSubresourceUploadDescription *desc) {
  self->setDescription(*desc);
}

//  QRhiTextureUploadEntry::~QRhiTextureUploadEntry()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QRhiTextureUploadEntryD1Ev(QRhiTextureUploadEntry *self) {
  delete self;
}
