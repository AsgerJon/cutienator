//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qrhi_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qrhi_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QRhiBufferData::QRhiBufferData()
extern "C" Q_DECL_EXPORT
QRhiBufferData *ritual_ZN14QRhiBufferDataC1Ev() {
  return new QRhiBufferData();
}

//  QRhiBufferData::~QRhiBufferData()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QRhiBufferDataD1Ev(QRhiBufferData *self) {
  delete self;
}

//  QRhiBufferData::QRhiBufferData(const QRhiBufferData &other)
extern "C" Q_DECL_EXPORT
QRhiBufferData *ritual_ZN14QRhiBufferDataC1ERKS_(
    const QRhiBufferData *other) {
  return new QRhiBufferData(*other);
}

//  const char *QRhiBufferData::constData() const
extern "C" Q_DECL_EXPORT
const char *ritual_ZNK14QRhiBufferData9constDataEv(
    const QRhiBufferData *self) {
  return self->constData();
}

//  quint32 QRhiBufferData::size() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK14QRhiBufferData4sizeEv(const QRhiBufferData *self) {
  return self->size();
}

//  quint32 QRhiBufferData::largeAlloc() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK14QRhiBufferData10largeAllocEv(
    const QRhiBufferData *self) {
  return self->largeAlloc();
}
