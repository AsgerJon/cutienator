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

//  const QMetaObject *QDnsLookupRunnable::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QDnsLookupRunnable10metaObjectEv(
    const QDnsLookupRunnable *self) {
  return self->metaObject();
}

//  QDnsLookupRunnable as the QRunnable it is built on
extern "C" Q_DECL_EXPORT
QRunnable *ritual_cast_QDnsLookupRunnable_QRunnable(
    QDnsLookupRunnable *self) {
  return static_cast<QRunnable *>(self);
}

#endif  // QT_CONFIG(dnslookup)
#endif  // QT_CONFIG(dnslookup)
