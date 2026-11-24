//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qdnslookup_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#if QT_CONFIG(dnslookup)
#if QT_CONFIG(dnslookup)
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/qdnslookup.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qdnslookup_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QDnsLookupPrivate::QDnsLookupPrivate()
extern "C" Q_DECL_EXPORT
QDnsLookupPrivate *ritual_ZN17QDnsLookupPrivateC1Ev() {
  return new QDnsLookupPrivate();
}

//  void QDnsLookupPrivate::nameChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDnsLookupPrivate11nameChangedEv(QDnsLookupPrivate *self) {
  self->nameChanged();
}

//  void QDnsLookupPrivate::nameserverChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDnsLookupPrivate17nameserverChangedEv(
    QDnsLookupPrivate *self) {
  self->nameserverChanged();
}

//  void QDnsLookupPrivate::typeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDnsLookupPrivate11typeChangedEv(QDnsLookupPrivate *self) {
  self->typeChanged();
}

//  void QDnsLookupPrivate::nameserverPortChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDnsLookupPrivate21nameserverPortChangedEv(
    QDnsLookupPrivate *self) {
  self->nameserverPortChanged();
}

//  void QDnsLookupPrivate::nameserverProtocolChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDnsLookupPrivate25nameserverProtocolChangedEv(
    QDnsLookupPrivate *self) {
  self->nameserverProtocolChanged();
}

//  QDnsLookup *QDnsLookupPrivate::q_func()
extern "C" Q_DECL_EXPORT
QDnsLookup *ritual_ZN17QDnsLookupPrivate6q_funcEv(QDnsLookupPrivate *self) {
  return self->q_func();
}

//  const QDnsLookup *QDnsLookupPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QDnsLookup *ritual_ZNK17QDnsLookupPrivate6q_funcEv(
    const QDnsLookupPrivate *self) {
  return self->q_func();
}

#endif  // QT_CONFIG(dnslookup)
#endif  // QT_CONFIG(dnslookup)
