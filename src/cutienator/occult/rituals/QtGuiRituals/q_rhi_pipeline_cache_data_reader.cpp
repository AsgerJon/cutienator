//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qrhi_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qrhi_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QRhiPipelineCacheDataReader::QRhiPipelineCacheDataReader(const char
//      *data, quint32 size)
extern "C" Q_DECL_EXPORT
QRhiPipelineCacheDataReader *ritual_ZN27QRhiPipelineCacheDataReaderC1EPKcj(
    const char *data,
    quint32 size) {
  return new QRhiPipelineCacheDataReader(data, size);
}

//  bool QRhiPipelineCacheDataReader::readUInt32(quint32 *dst)
extern "C" Q_DECL_EXPORT
bool ritual_ZN27QRhiPipelineCacheDataReader10readUInt32EPj(
    QRhiPipelineCacheDataReader *self,
    quint32 *dst) {
  return self->readUInt32(dst);
}

//  bool QRhiPipelineCacheDataReader::readByteArray(QByteArray *dst)
extern "C" Q_DECL_EXPORT
bool ritual_ZN27QRhiPipelineCacheDataReader13readByteArrayEP10QByteArray(
    QRhiPipelineCacheDataReader *self,
    QByteArray *dst) {
  return self->readByteArray(dst);
}

//  QRhiPipelineCacheDataReader::~QRhiPipelineCacheDataReader()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QRhiPipelineCacheDataReaderD1Ev(
    QRhiPipelineCacheDataReader *self) {
  delete self;
}
