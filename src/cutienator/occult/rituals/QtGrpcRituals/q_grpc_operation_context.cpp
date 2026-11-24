//  Written by dev_tooling.RitualGenerator from the records of
//  QtGrpc/qgrpcoperationcontext.h, Qt 6.12.0. Changes made here are lost.
#include <QtGrpc/qgrpcoperationcontext.h>
#include <QtCore/qstring.h>
#include <QtCore/qlatin1stringview.h>
#include <QtGrpc/qtgrpcnamespace.h>
#include <QtGrpc/qgrpccalloptions.h>
#include <QtCore/qmetatype.h>

//  const QMetaObject *QGrpcOperationContext::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QGrpcOperationContext10metaObjectEv(
    const QGrpcOperationContext *self) {
  return self->metaObject();
}

//  QString QGrpcOperationContext::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QGrpcOperationContext2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGrpcOperationContext::tr(s, c, n));
}

//  QGrpcOperationContext::~QGrpcOperationContext()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGrpcOperationContextD1Ev(QGrpcOperationContext *self) {
  delete self;
}

//  QLatin1StringView QGrpcOperationContext::method() const
extern "C" Q_DECL_EXPORT
QLatin1String *ritual_ZNK21QGrpcOperationContext6methodEv(
    const QGrpcOperationContext *self) {
  return new QLatin1String(self->method());
}

//  QLatin1StringView QGrpcOperationContext::service() const
extern "C" Q_DECL_EXPORT
QLatin1String *ritual_ZNK21QGrpcOperationContext7serviceEv(
    const QGrpcOperationContext *self) {
  return new QLatin1String(self->service());
}

//  QtGrpc::RpcDescriptor QGrpcOperationContext::descriptor() const
extern "C" Q_DECL_EXPORT
QtGrpc::RpcDescriptor *ritual_ZNK21QGrpcOperationContext10descriptorEv(
    const QGrpcOperationContext *self) {
  return new QtGrpc::RpcDescriptor(self->descriptor());
}

//  const QGrpcCallOptions &QGrpcOperationContext::callOptions() const
extern "C" Q_DECL_EXPORT
QGrpcCallOptions *ritual_ZNKR21QGrpcOperationContext11callOptionsEv(
    const QGrpcOperationContext *self) {
  return new QGrpcCallOptions(self->callOptions());
}

//  QMetaType QGrpcOperationContext::responseMetaType() const
extern "C" Q_DECL_EXPORT
QMetaType *ritual_ZNK21QGrpcOperationContext16responseMetaTypeEv(
    const QGrpcOperationContext *self) {
  return new QMetaType(self->responseMetaType());
}

//  void QGrpcOperationContext::setResponseMetaType(QMetaType metaType)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGrpcOperationContext19setResponseMetaTypeE9QMetaType(
    QGrpcOperationContext *self,
    const QMetaType *metaType) {
  self->setResponseMetaType(*metaType);
}

//  quint64 QGrpcOperationContext::operationId() const
extern "C" Q_DECL_EXPORT
quint64 ritual_ZNK21QGrpcOperationContext11operationIdEv(
    const QGrpcOperationContext *self) {
  return self->operationId();
}

//  QGrpcOperationContextPrivate *QGrpcOperationContext::d_func()
extern "C" Q_DECL_EXPORT
QGrpcOperationContextPrivate *ritual_ZN21QGrpcOperationContext6d_funcEv(
    QGrpcOperationContext *self) {
  return self->d_func();
}

//  const QGrpcOperationContextPrivate *QGrpcOperationContext::d_func() const
extern "C" Q_DECL_EXPORT
const QGrpcOperationContextPrivate *ritual_ZNK21QGrpcOperationContext6d_funcEv(
    const QGrpcOperationContext *self) {
  return self->d_func();
}

//  bool QGrpcOperationContext::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QGrpcOperationContext5eventEP6QEvent(
    QGrpcOperationContext *self,
    QEvent *event) {
  return self->event(event);
}
