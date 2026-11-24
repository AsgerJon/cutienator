//  Written by dev_tooling.RitualGenerator from the records of
//  QtNfc/6.12.0/QtNfc/private/qndefnfcsmartposterrecord_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtNfc/6.12.0/QtNfc/private/qtnfcglobal_p.h>
#include <QtNfc/QtNfc>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNfc/6.12.0/QtNfc/private/qndefnfcsmartposterrecord_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNfc/qndefnfcsmartposterrecord.h>
#include <QtNfc/private/qndefnfcsmartposterrecord_p.h>
#include <QtNfc/qndefmessage.h>
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

//  from ../qtconnectivity/src/nfc/qndefnfcsmartposterrecord.cpp, line 62, as _ZN32QNdefNfcSmartPosterRecordPrivateD1Ev
inline QNdefNfcSmartPosterRecordPrivate::~QNdefNfcSmartPosterRecordPrivate()
{
    cleanup();
}

//  from ../qtconnectivity/src/nfc/qndefnfcsmartposterrecord.cpp, line 67, as _ZN32QNdefNfcSmartPosterRecordPrivate7cleanupEv
inline void QNdefNfcSmartPosterRecordPrivate::cleanup()
{
    // Clean-up existing internal structure
    m_titleList.clear();
    delete m_uri;
    delete m_action;
    m_iconList.clear();
    delete m_size;
    delete m_type;
}
//  -----------------------------------------------------------------------

//  QNdefNfcSmartPosterRecordPrivate::QNdefNfcSmartPosterRecordPrivate()
extern "C" Q_DECL_EXPORT
QNdefNfcSmartPosterRecordPrivate *ritual_ZN32QNdefNfcSmartPosterRecordPrivateC1Ev() {
  return new QNdefNfcSmartPosterRecordPrivate();
}

//  QNdefNfcSmartPosterRecordPrivate::~QNdefNfcSmartPosterRecordPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QNdefNfcSmartPosterRecordPrivateD1Ev(
    QNdefNfcSmartPosterRecordPrivate *self) {
  delete self;
}

//  void QNdefNfcSmartPosterRecordPrivate::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QNdefNfcSmartPosterRecordPrivate7cleanupEv(
    QNdefNfcSmartPosterRecordPrivate *self) {
  self->cleanup();
}
