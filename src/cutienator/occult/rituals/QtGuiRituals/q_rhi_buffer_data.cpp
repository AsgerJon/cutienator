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
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/rhi/qrhi.cpp, line 35, as _Z12QRHI_LOG_RUBv
inline const QLoggingCategory &QRHI_LOG_RUB()
{
    static const QLoggingCategory category("qt.rhi.rub");
    return category;
}
//  -----------------------------------------------------------------------

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

//  QRhiBufferData &QRhiBufferData::operator=(const QRhiBufferData &other)
extern "C" Q_DECL_EXPORT
QRhiBufferData *ritual_ZN14QRhiBufferDataaSERKS_(
    QRhiBufferData *self,
    const QRhiBufferData *other) {
  return &(self->operator=(*other));
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

//  void QRhiBufferData::assign(const char *s, quint32 size)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QRhiBufferData6assignEPKcj(
    QRhiBufferData *self,
    const char *s,
    quint32 size) {
  self->assign(s, size);
}

//  void QRhiBufferData::assign(QByteArray data)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QRhiBufferData6assignE10QByteArray(
    QRhiBufferData *self,
    const QByteArray *data) {
  self->assign(*data);
}
