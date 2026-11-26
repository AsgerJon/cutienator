//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qrhi_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qrhi_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qloggingcategory.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/rhi/qrhi.cpp, line 35, as _Z12QRHI_LOG_RUBv
inline const QLoggingCategory &QRHI_LOG_RUB()
{
    static const QLoggingCategory category("qt.rhi.rub");
    return category;
}
//  -----------------------------------------------------------------------

//  BufferOp
//      QRhiResourceUpdateBatchPrivate::BufferOp::dynamicUpdate(QRhiBuffer
//      *buf, quint32 offset, quint32 size, const void *data)
extern "C" Q_DECL_EXPORT
QRhiResourceUpdateBatchPrivate::BufferOp *ritual_ZN30QRhiResourceUpdateBatchPrivate8BufferOp13dynamicUpdateEP10QRhiBufferjjPKv(
    QRhiBuffer *buf,
    quint32 offset,
    quint32 size,
    const void *data) {
  return new QRhiResourceUpdateBatchPrivate::BufferOp(
      QRhiResourceUpdateBatchPrivate::BufferOp::dynamicUpdate(
          buf,
          offset,
          size,
          data));
}

//  void
//      QRhiResourceUpdateBatchPrivate::BufferOp::changeToDynamicUpdate(Buffe
//      rOp *op, QRhiBuffer *buf, quint32 offset, quint32 size, const void
//      *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QRhiResourceUpdateBatchPrivate8BufferOp21changeToDynamicUpdateEPS0_P10QRhiBufferjjPKv(
    QRhiResourceUpdateBatchPrivate::BufferOp *op,
    QRhiBuffer *buf,
    quint32 offset,
    quint32 size,
    const void *data) {
  QRhiResourceUpdateBatchPrivate::BufferOp::changeToDynamicUpdate(
      op,
      buf,
      offset,
      size,
      data);
}

//  BufferOp
//      QRhiResourceUpdateBatchPrivate::BufferOp::dynamicUpdate(QRhiBuffer
//      *buf, quint32 offset, QByteArray data)
extern "C" Q_DECL_EXPORT
QRhiResourceUpdateBatchPrivate::BufferOp *ritual_ZN30QRhiResourceUpdateBatchPrivate8BufferOp13dynamicUpdateEP10QRhiBufferj10QByteArray(
    QRhiBuffer *buf,
    quint32 offset,
    const QByteArray *data) {
  return new QRhiResourceUpdateBatchPrivate::BufferOp(
      QRhiResourceUpdateBatchPrivate::BufferOp::dynamicUpdate(
          buf,
          offset,
          *data));
}

//  void
//      QRhiResourceUpdateBatchPrivate::BufferOp::changeToDynamicUpdate(Buffe
//      rOp *op, QRhiBuffer *buf, quint32 offset, QByteArray data)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QRhiResourceUpdateBatchPrivate8BufferOp21changeToDynamicUpdateEPS0_P10QRhiBufferj10QByteArray(
    QRhiResourceUpdateBatchPrivate::BufferOp *op,
    QRhiBuffer *buf,
    quint32 offset,
    const QByteArray *data) {
  QRhiResourceUpdateBatchPrivate::BufferOp::changeToDynamicUpdate(
      op,
      buf,
      offset,
      *data);
}

//  BufferOp
//      QRhiResourceUpdateBatchPrivate::BufferOp::staticUpload(QRhiBuffer
//      *buf, quint32 offset, quint32 size, const void *data)
extern "C" Q_DECL_EXPORT
QRhiResourceUpdateBatchPrivate::BufferOp *ritual_ZN30QRhiResourceUpdateBatchPrivate8BufferOp12staticUploadEP10QRhiBufferjjPKv(
    QRhiBuffer *buf,
    quint32 offset,
    quint32 size,
    const void *data) {
  return new QRhiResourceUpdateBatchPrivate::BufferOp(
      QRhiResourceUpdateBatchPrivate::BufferOp::staticUpload(
          buf,
          offset,
          size,
          data));
}

//  void
//      QRhiResourceUpdateBatchPrivate::BufferOp::changeToStaticUpload(Buffer
//      Op *op, QRhiBuffer *buf, quint32 offset, quint32 size, const void
//      *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QRhiResourceUpdateBatchPrivate8BufferOp20changeToStaticUploadEPS0_P10QRhiBufferjjPKv(
    QRhiResourceUpdateBatchPrivate::BufferOp *op,
    QRhiBuffer *buf,
    quint32 offset,
    quint32 size,
    const void *data) {
  QRhiResourceUpdateBatchPrivate::BufferOp::changeToStaticUpload(
      op,
      buf,
      offset,
      size,
      data);
}

//  BufferOp
//      QRhiResourceUpdateBatchPrivate::BufferOp::staticUpload(QRhiBuffer
//      *buf, quint32 offset, QByteArray data)
extern "C" Q_DECL_EXPORT
QRhiResourceUpdateBatchPrivate::BufferOp *ritual_ZN30QRhiResourceUpdateBatchPrivate8BufferOp12staticUploadEP10QRhiBufferj10QByteArray(
    QRhiBuffer *buf,
    quint32 offset,
    const QByteArray *data) {
  return new QRhiResourceUpdateBatchPrivate::BufferOp(
      QRhiResourceUpdateBatchPrivate::BufferOp::staticUpload(
          buf,
          offset,
          *data));
}

//  void
//      QRhiResourceUpdateBatchPrivate::BufferOp::changeToStaticUpload(Buffer
//      Op *op, QRhiBuffer *buf, quint32 offset, QByteArray data)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QRhiResourceUpdateBatchPrivate8BufferOp20changeToStaticUploadEPS0_P10QRhiBufferj10QByteArray(
    QRhiResourceUpdateBatchPrivate::BufferOp *op,
    QRhiBuffer *buf,
    quint32 offset,
    const QByteArray *data) {
  QRhiResourceUpdateBatchPrivate::BufferOp::changeToStaticUpload(
      op,
      buf,
      offset,
      *data);
}

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
