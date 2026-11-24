//  Written by dev_tooling.RitualGenerator from the records of
//  QtGrpc/qgrpcinterceptorchain.h, Qt 6.12.0. Changes made here are lost.
#include <QtGrpc/qgrpcinterceptorchain.h>

//  QGrpcInterceptorChain::QGrpcInterceptorChain()
extern "C" Q_DECL_EXPORT
QGrpcInterceptorChain *ritual_ZN21QGrpcInterceptorChainC1Ev() {
  return new QGrpcInterceptorChain();
}

//  QGrpcInterceptorChain::~QGrpcInterceptorChain()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGrpcInterceptorChainD1Ev(QGrpcInterceptorChain *self) {
  delete self;
}

//  void QGrpcInterceptorChain::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGrpcInterceptorChain5clearEv(QGrpcInterceptorChain *self) {
  self->clear();
}

//  qsizetype QGrpcInterceptorChain::size() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK21QGrpcInterceptorChain4sizeEv(
    const QGrpcInterceptorChain *self) {
  return self->size();
}

//  bool QGrpcInterceptorChain::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QGrpcInterceptorChain7isEmptyEv(
    const QGrpcInterceptorChain *self) {
  return self->isEmpty();
}

//  bool QGrpcInterceptorChain::empty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QGrpcInterceptorChain5emptyEv(
    const QGrpcInterceptorChain *self) {
  return self->empty();
}

//  bool QGrpcInterceptorChain::hasHandlerFor(QtGrpc::InterceptorCapability
//      cap) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QGrpcInterceptorChain13hasHandlerForEN6QtGrpc21InterceptorCapabilityE(
    const QGrpcInterceptorChain *self,
    QtGrpc::InterceptorCapability cap) {
  return self->hasHandlerFor(cap);
}

//  void QGrpcInterceptorChain::warnNullInterceptor(qsizetype index,
//      qsizetype total) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK21QGrpcInterceptorChain19warnNullInterceptorExx(
    const QGrpcInterceptorChain *self,
    qsizetype index,
    qsizetype total) {
  self->warnNullInterceptor(index, total);
}

//  QGrpcInterceptorChainPrivate *QGrpcInterceptorChain::d_func()
extern "C" Q_DECL_EXPORT
QGrpcInterceptorChainPrivate *ritual_ZN21QGrpcInterceptorChain6d_funcEv(
    QGrpcInterceptorChain *self) {
  return self->d_func();
}

//  const QGrpcInterceptorChainPrivate *QGrpcInterceptorChain::d_func() const
extern "C" Q_DECL_EXPORT
const QGrpcInterceptorChainPrivate *ritual_ZNK21QGrpcInterceptorChain6d_funcEv(
    const QGrpcInterceptorChain *self) {
  return self->d_func();
}
