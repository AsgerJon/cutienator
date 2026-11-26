//  Written by dev_tooling.RitualGenerator from the records of
//  QtGrpc/qgrpcinterceptorchain.h, Qt 6.12.0. Edited by hand on 2026-11-25:
//  added by hand, rituals for functions the generator leaves out: 2. Kept as
//  it is when the generator runs again.
#include <QtGrpc/qgrpcinterceptorchain.h>
#include <QtCore/QSpan>

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

//  QGrpcInterceptorChain::QGrpcInterceptorChain(QGrpcInterceptorChain
//      &&other)
extern "C" Q_DECL_EXPORT
QGrpcInterceptorChain *ritual_ZN21QGrpcInterceptorChainC1EOS_(
    QGrpcInterceptorChain *other) {
  return new QGrpcInterceptorChain(std::move(*other));
}

//  QGrpcInterceptorChain
//      &QGrpcInterceptorChain::operator=(QGrpcInterceptorChain &&other)
extern "C" Q_DECL_EXPORT
QGrpcInterceptorChain *ritual_ZN21QGrpcInterceptorChainaSEOS_(
    QGrpcInterceptorChain *self,
    QGrpcInterceptorChain *other) {
  return &(self->operator=(std::move(*other)));
}

//  void QGrpcInterceptorChain::swap(QGrpcInterceptorChain &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGrpcInterceptorChain4swapERS_(
    QGrpcInterceptorChain *self,
    QGrpcInterceptorChain *other) {
  self->swap(*other);
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

//  bool QGrpcInterceptorChain::addImpl(void *interceptor, DeleterFn deleter,
//      QSpan<const QtGrpcPrivate::InterceptorCapabilityBinding> bindings)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QGrpcInterceptorChain7addImplEPvPFvS0_E5QSpanIKN13QtGrpcPrivate28InterceptorCapabilityBindingELm18446744073709551615EE(
    QGrpcInterceptorChain *self,
    void *interceptor,
    void *deleter,
    const QSpan<const QtGrpcPrivate::InterceptorCapabilityBinding> *bindings) {
  return self->addImpl(
      interceptor,
      reinterpret_cast<QGrpcInterceptorChain::DeleterFn>(deleter),
      *bindings);
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

//  QtGrpc::InterceptorCapabilities QGrpcInterceptorChain::capabilities()
//      const
extern "C" Q_DECL_EXPORT
unsigned long long ritual_ZNK21QGrpcInterceptorChain12capabilitiesEv(
    const QGrpcInterceptorChain *self) {
  return static_cast<unsigned long long>(self->capabilities().toInt());
}

//  QtGrpc::InterceptorCapabilities
//      QGrpcInterceptorChain::capabilitiesAt(qsizetype index) const
extern "C" Q_DECL_EXPORT
unsigned long long ritual_ZNK21QGrpcInterceptorChain14capabilitiesAtEx(
    const QGrpcInterceptorChain *self,
    qsizetype index) {
  return static_cast<unsigned long long>(
      self->capabilitiesAt(index).toInt());
}
