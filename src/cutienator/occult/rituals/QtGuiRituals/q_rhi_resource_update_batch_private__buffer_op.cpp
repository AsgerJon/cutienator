//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qrhi_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qrhi_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  BufferOp QRhiResourceUpdateBatchPrivate::BufferOp::read(QRhiBuffer *buf,
//      quint32 offset, quint32 size, QRhiReadbackResult *result)
extern "C" Q_DECL_EXPORT
QRhiResourceUpdateBatchPrivate::BufferOp *ritual_ZN30QRhiResourceUpdateBatchPrivate8BufferOp4readEP10QRhiBufferjjP18QRhiReadbackResult(
    QRhiBuffer *buf,
    quint32 offset,
    quint32 size,
    QRhiReadbackResult *result) {
  return new QRhiResourceUpdateBatchPrivate::BufferOp(
      QRhiResourceUpdateBatchPrivate::BufferOp::read(
          buf,
          offset,
          size,
          result));
}

//  QRhiResourceUpdateBatchPrivate::BufferOp::~BufferOp()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QRhiResourceUpdateBatchPrivate8BufferOpD1Ev(
    QRhiResourceUpdateBatchPrivate::BufferOp *self) {
  delete self;
}
