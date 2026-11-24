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

//  void QDnsLookupReply::makeResolverSystemError(int code)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QDnsLookupReply23makeResolverSystemErrorEi(
    QDnsLookupReply *self,
    int code) {
  self->makeResolverSystemError(code);
}

//  void QDnsLookupReply::makeTimeoutError()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QDnsLookupReply16makeTimeoutErrorEv(QDnsLookupReply *self) {
  self->makeTimeoutError();
}

//  void QDnsLookupReply::makeDnsRcodeError(quint8 rcode)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QDnsLookupReply17makeDnsRcodeErrorEh(
    QDnsLookupReply *self,
    quint8 rcode) {
  self->makeDnsRcodeError(rcode);
}

//  bool QDnsLookupReply::allAreEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QDnsLookupReply11allAreEmptyEv(
    const QDnsLookupReply *self) {
  return self->allAreEmpty();
}

//  QDnsLookupReply::~QDnsLookupReply()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QDnsLookupReplyD1Ev(QDnsLookupReply *self) {
  delete self;
}

#endif  // QT_CONFIG(dnslookup)
#endif  // QT_CONFIG(dnslookup)
