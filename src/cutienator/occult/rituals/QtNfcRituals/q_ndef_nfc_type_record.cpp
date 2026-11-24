//  Written by dev_tooling.RitualGenerator from the records of
//  QtNfc/6.12.0/QtNfc/private/qndefnfcsmartposterrecord_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtNfc/6.12.0/QtNfc/private/qtnfcglobal_p.h>
#include <QtNfc/QtNfc>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNfc/6.12.0/QtNfc/private/qndefnfcsmartposterrecord_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNfc/qndefrecord.h>
#include <QtCore/qstring.h>
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

//  from ../qtconnectivity/src/nfc/qndefnfcsmartposterrecord.cpp, line 782, as _ZN18QNdefNfcTypeRecord11setTypeInfoERK7QString
inline void QNdefNfcTypeRecord::setTypeInfo(const QString &type)
{
    setPayload(type.toUtf8());
}

//  from ../qtconnectivity/src/nfc/qndefnfcsmartposterrecord.cpp, line 787, as _ZNK18QNdefNfcTypeRecord8typeInfoEv
inline QString QNdefNfcTypeRecord::typeInfo() const
{
    return QString::fromUtf8(payload());
}
//  -----------------------------------------------------------------------

//  QNdefNfcTypeRecord::QNdefNfcTypeRecord()
extern "C" Q_DECL_EXPORT
QNdefNfcTypeRecord *ritual_ZN18QNdefNfcTypeRecordC1Ev() {
  return new QNdefNfcTypeRecord();
}

//  QNdefNfcTypeRecord::QNdefNfcTypeRecord(const QNdefRecord &other)
extern "C" Q_DECL_EXPORT
QNdefNfcTypeRecord *ritual_ZN18QNdefNfcTypeRecordC1ERK11QNdefRecord(
    const QNdefRecord *other) {
  return new QNdefNfcTypeRecord(*other);
}

//  void QNdefNfcTypeRecord::setTypeInfo(const QString &type)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QNdefNfcTypeRecord11setTypeInfoERK7QString(
    QNdefNfcTypeRecord *self,
    const QString *type) {
  self->setTypeInfo(*type);
}

//  QString QNdefNfcTypeRecord::typeInfo() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QNdefNfcTypeRecord8typeInfoEv(
    const QNdefNfcTypeRecord *self) {
  return new QString(self->typeInfo());
}

//  QNdefNfcTypeRecord::~QNdefNfcTypeRecord()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QNdefNfcTypeRecordD1Ev(QNdefNfcTypeRecord *self) {
  delete self;
}
