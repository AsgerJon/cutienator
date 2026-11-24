//  Written by dev_tooling.RitualGenerator from the records of
//  QtNfc/6.12.0/QtNfc/private/qndefnfcsmartposterrecord_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtNfc/6.12.0/QtNfc/private/qtnfcglobal_p.h>
#include <QtNfc/QtNfc>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNfc/6.12.0/QtNfc/private/qndefnfcsmartposterrecord_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNfc/qndefrecord.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <qndefnfcsmartposterrecord.h>
#include "qndefnfcsmartposterrecord_p.h"
#include <qndefmessage.h>
#include <QtCore/QString>
#include <QtCore/QStringList>
#include <QtCore/QUrl>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtconnectivity/src/nfc/qndefnfcsmartposterrecord.cpp, line 759, as _ZN18QNdefNfcSizeRecord7setSizeEj
inline void QNdefNfcSizeRecord::setSize(quint32 size)
{
    QByteArray data(4, 0);

    data[0] = (int) ((size & 0xFF000000) >> 24);
    data[1] = (int) ((size & 0x00FF0000) >> 16);
    data[2] = (int) ((size & 0x0000FF00) >> 8);
    data[3] = (int) ((size & 0x000000FF));

    setPayload(data);
}

//  from ../qtconnectivity/src/nfc/qndefnfcsmartposterrecord.cpp, line 771, as _ZNK18QNdefNfcSizeRecord4sizeEv
inline quint32 QNdefNfcSizeRecord::size() const
{
    const QByteArray p = payload();

    if (p.isEmpty())
        return 0;

    return ((p[0] << 24) & 0xFF000000) + ((p[1] << 16) & 0x00FF0000)
            + ((p[2] << 8) & 0x0000FF00) + (p[3] & 0x000000FF);
}
//  -----------------------------------------------------------------------

//  QNdefNfcSizeRecord::QNdefNfcSizeRecord()
extern "C" Q_DECL_EXPORT
QNdefNfcSizeRecord *ritual_ZN18QNdefNfcSizeRecordC1Ev() {
  return new QNdefNfcSizeRecord();
}

//  QNdefNfcSizeRecord::QNdefNfcSizeRecord(const QNdefRecord &other)
extern "C" Q_DECL_EXPORT
QNdefNfcSizeRecord *ritual_ZN18QNdefNfcSizeRecordC1ERK11QNdefRecord(
    const QNdefRecord *other) {
  return new QNdefNfcSizeRecord(*other);
}

//  void QNdefNfcSizeRecord::setSize(quint32 size)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QNdefNfcSizeRecord7setSizeEj(
    QNdefNfcSizeRecord *self,
    quint32 size) {
  self->setSize(size);
}

//  quint32 QNdefNfcSizeRecord::size() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK18QNdefNfcSizeRecord4sizeEv(
    const QNdefNfcSizeRecord *self) {
  return self->size();
}

//  QNdefNfcSizeRecord::~QNdefNfcSizeRecord()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QNdefNfcSizeRecordD1Ev(QNdefNfcSizeRecord *self) {
  delete self;
}
