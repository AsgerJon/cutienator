//  Written by dev_tooling.RitualGenerator from the records of
//  QtGrpc/6.12.0/QtGrpc/private/qgrpcinterceptorchain_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtGrpc/QtGrpc>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGrpc/6.12.0/QtGrpc/private/qgrpcinterceptorchain_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <vector>

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

//  QGrpcInterceptorChainPrivate::Entry::Entry(void *s, DeleterFn d,
//      std::vector<QtGrpcPrivate::InterceptorCapabilityBinding> b)
extern "C" Q_DECL_EXPORT
QGrpcInterceptorChainPrivate::Entry *ritual_ZN28QGrpcInterceptorChainPrivate5EntryC1EPvPFvS1_ESt6vectorIN13QtGrpcPrivate28InterceptorCapabilityBindingESaIS6_EE(
    void *s,
    void *d,
    const std::vector<QtGrpcPrivate::InterceptorCapabilityBinding> *b) {
  return new QGrpcInterceptorChainPrivate::Entry(
      s,
      reinterpret_cast<QGrpcInterceptorChainPrivate::DeleterFn>(d),
      *b);
}

//  QGrpcInterceptorChainPrivate::Entry::Entry(Entry &&other)
extern "C" Q_DECL_EXPORT
QGrpcInterceptorChainPrivate::Entry *ritual_ZN28QGrpcInterceptorChainPrivate5EntryC1EOS0_(
    QGrpcInterceptorChainPrivate::Entry *other) {
  return new QGrpcInterceptorChainPrivate::Entry(std::move(*other));
}

//  Entry &QGrpcInterceptorChainPrivate::Entry::operator=(Entry &&other)
extern "C" Q_DECL_EXPORT
QGrpcInterceptorChainPrivate::Entry *ritual_ZN28QGrpcInterceptorChainPrivate5EntryaSEOS0_(
    QGrpcInterceptorChainPrivate::Entry *self,
    QGrpcInterceptorChainPrivate::Entry *other) {
  return &(self->operator=(std::move(*other)));
}

//  void QGrpcInterceptorChainPrivate::Entry::swap(Entry &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QGrpcInterceptorChainPrivate5Entry4swapERS0_(
    QGrpcInterceptorChainPrivate::Entry *self,
    QGrpcInterceptorChainPrivate::Entry *other) {
  self->swap(*other);
}
