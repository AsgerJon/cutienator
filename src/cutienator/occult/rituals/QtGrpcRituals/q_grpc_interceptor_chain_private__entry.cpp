//  Written by dev_tooling.RitualGenerator from the records of
//  QtGrpc/6.12.0/QtGrpc/private/qgrpcinterceptorchain_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtGrpc/QtGrpc>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGrpc/6.12.0/QtGrpc/private/qgrpcinterceptorchain_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QGrpcInterceptorChainPrivate::Entry::Entry()
extern "C" Q_DECL_EXPORT
QGrpcInterceptorChainPrivate::Entry *ritual_ZN28QGrpcInterceptorChainPrivate5EntryC1Ev() {
  return new QGrpcInterceptorChainPrivate::Entry();
}

//  QGrpcInterceptorChainPrivate::Entry::~Entry()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QGrpcInterceptorChainPrivate5EntryD1Ev(
    QGrpcInterceptorChainPrivate::Entry *self) {
  delete self;
}
