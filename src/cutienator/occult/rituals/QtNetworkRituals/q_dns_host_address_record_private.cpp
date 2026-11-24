//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qdnslookup_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#if QT_CONFIG(dnslookup)
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qdnslookup_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QDnsHostAddressRecordPrivate::QDnsHostAddressRecordPrivate()
extern "C" Q_DECL_EXPORT
QDnsHostAddressRecordPrivate *ritual_ZN28QDnsHostAddressRecordPrivateC1Ev() {
  return new QDnsHostAddressRecordPrivate();
}

//  QDnsHostAddressRecordPrivate::~QDnsHostAddressRecordPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QDnsHostAddressRecordPrivateD1Ev(
    QDnsHostAddressRecordPrivate *self) {
  delete self;
}

#endif  // QT_CONFIG(dnslookup)
