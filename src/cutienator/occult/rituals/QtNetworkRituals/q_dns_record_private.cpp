//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qdnslookup_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#if QT_CONFIG(dnslookup)
#if QT_CONFIG(dnslookup)
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qdnslookup_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QDnsRecordPrivate::QDnsRecordPrivate()
extern "C" Q_DECL_EXPORT
QDnsRecordPrivate *ritual_ZN17QDnsRecordPrivateC1Ev() {
  return new QDnsRecordPrivate();
}

//  QDnsRecordPrivate::~QDnsRecordPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDnsRecordPrivateD1Ev(QDnsRecordPrivate *self) {
  delete self;
}

#endif  // QT_CONFIG(dnslookup)
#endif  // QT_CONFIG(dnslookup)
