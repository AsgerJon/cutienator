//  Written by dev_tooling.RitualGenerator from the records of
//  QtGrpc/6.12.0/QtGrpc/private/qgrpcinterceptorchain_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtGrpc/QtGrpc>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGrpc/6.12.0/QtGrpc/private/qgrpcinterceptorchain_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGrpc/private/qgrpcinterceptorchain_p.h>
#include <QtGrpc/private/qtgrpclogging_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtgrpc/src/grpc/qgrpcinterceptorchain.cpp, line 10, as _ZN28QGrpcInterceptorChainPrivate5clearEv
inline void QGrpcInterceptorChainPrivate::clear()
{
    m_combinedCapabilities = {};
    m_interceptors.clear();
}
//  -----------------------------------------------------------------------

//  void QGrpcInterceptorChainPrivate::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QGrpcInterceptorChainPrivate5clearEv(
    QGrpcInterceptorChainPrivate *self) {
  self->clear();
}

//  bool
//      QGrpcInterceptorChainPrivate::hasHandlerFor(QtGrpc::InterceptorCapabi
//      lity cap) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QGrpcInterceptorChainPrivate13hasHandlerForEN6QtGrpc21InterceptorCapabilityE(
    const QGrpcInterceptorChainPrivate *self,
    QtGrpc::InterceptorCapability cap) {
  return self->hasHandlerFor(cap);
}

//  QGrpcInterceptorChainPrivate::~QGrpcInterceptorChainPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QGrpcInterceptorChainPrivateD1Ev(
    QGrpcInterceptorChainPrivate *self) {
  delete self;
}
