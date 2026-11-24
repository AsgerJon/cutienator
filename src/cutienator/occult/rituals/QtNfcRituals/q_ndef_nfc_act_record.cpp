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

//  from ../qtconnectivity/src/nfc/qndefnfcsmartposterrecord.cpp, line 721, as _ZN17QNdefNfcActRecord9setActionEN25QNdefNfcSmartPosterRecord6ActionE
inline void QNdefNfcActRecord::setAction(QNdefNfcSmartPosterRecord::Action action)
{
    QByteArray data(1, action);

    setPayload(data);
}

//  from ../qtconnectivity/src/nfc/qndefnfcsmartposterrecord.cpp, line 728, as _ZNK17QNdefNfcActRecord6actionEv
inline QNdefNfcSmartPosterRecord::Action QNdefNfcActRecord::action() const
{
    const QByteArray p = payload();
    QNdefNfcSmartPosterRecord::Action value =
            QNdefNfcSmartPosterRecord::UnspecifiedAction;

    if (!p.isEmpty())
        value = QNdefNfcSmartPosterRecord::Action(static_cast<signed char>(p[0]));

    return value;
}
//  -----------------------------------------------------------------------

//  QNdefNfcActRecord::QNdefNfcActRecord()
extern "C" Q_DECL_EXPORT
QNdefNfcActRecord *ritual_ZN17QNdefNfcActRecordC1Ev() {
  return new QNdefNfcActRecord();
}

//  QNdefNfcActRecord::QNdefNfcActRecord(const QNdefRecord &other)
extern "C" Q_DECL_EXPORT
QNdefNfcActRecord *ritual_ZN17QNdefNfcActRecordC1ERK11QNdefRecord(
    const QNdefRecord *other) {
  return new QNdefNfcActRecord(*other);
}

//  void QNdefNfcActRecord::setAction(QNdefNfcSmartPosterRecord::Action
//      action)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QNdefNfcActRecord9setActionEN25QNdefNfcSmartPosterRecord6ActionE(
    QNdefNfcActRecord *self,
    QNdefNfcSmartPosterRecord::Action action) {
  self->setAction(action);
}

//  QNdefNfcSmartPosterRecord::Action QNdefNfcActRecord::action() const
extern "C" Q_DECL_EXPORT
QNdefNfcSmartPosterRecord::Action ritual_ZNK17QNdefNfcActRecord6actionEv(
    const QNdefNfcActRecord *self) {
  return self->action();
}

//  QNdefNfcActRecord::~QNdefNfcActRecord()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QNdefNfcActRecordD1Ev(QNdefNfcActRecord *self) {
  delete self;
}
