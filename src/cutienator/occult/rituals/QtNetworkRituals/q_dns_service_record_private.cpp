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

//  QDnsServiceRecordPrivate::QDnsServiceRecordPrivate()
extern "C" Q_DECL_EXPORT
QDnsServiceRecordPrivate *ritual_ZN24QDnsServiceRecordPrivateC1Ev() {
  return new QDnsServiceRecordPrivate();
}

//  QDnsServiceRecordPrivate::~QDnsServiceRecordPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QDnsServiceRecordPrivateD1Ev(
    QDnsServiceRecordPrivate *self) {
  delete self;
}

#endif  // QT_CONFIG(dnslookup)
#endif  // QT_CONFIG(dnslookup)
