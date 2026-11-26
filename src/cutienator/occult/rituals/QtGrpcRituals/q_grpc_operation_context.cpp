//  Written by dev_tooling.RitualGenerator from the records of
//  QtGrpc/qgrpcoperationcontext.h, Qt 6.12.0. Changes made here are lost.
#include <QtGrpc/qgrpcoperationcontext.h>
#include <QtCore/qstring.h>
#include <QtGrpc/qtgrpcnamespace.h>
#include <QtGrpc/qgrpccalloptions.h>
#include <QtCore/qlatin1stringview.h>
#include <QtCore/qmetatype.h>
#include <QtGrpc/qgrpcstatus.h>
#include <QtCore/qbytearray.h>
#include <QtGrpc/QtGrpc>
#include <QtGrpc/QGrpcCallOptions>
#include <memory>
#include <QtProtobuf/QAbstractProtobufSerializer>
#include <QtGrpc/QGrpcOperationContext>

//  const QMetaObject *QGrpcOperationContext::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QGrpcOperationContext10metaObjectEv(
    const QGrpcOperationContext *self) {
  return self->metaObject();
}

//  void *QGrpcOperationContext::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN21QGrpcOperationContext11qt_metacastEPKc(
    QGrpcOperationContext *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QGrpcOperationContext::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QGrpcOperationContext11qt_metacallEN11QMetaObject4CallEiPPv(
    QGrpcOperationContext *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QGrpcOperationContext::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QGrpcOperationContext2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGrpcOperationContext::tr(s, c, n));
}

//  QGrpcOperationContext::QGrpcOperationContext(QtGrpc::RpcDescriptor
//      description, const QGrpcCallOptions &options,
//      std::shared_ptr<QAbstractProtobufSerializer> serializer,
//      QGrpcOperation *parent, PrivateConstructor a4)
extern "C" Q_DECL_EXPORT
QGrpcOperationContext *ritual_ZN21QGrpcOperationContextC1EN6QtGrpc13RpcDescriptorERK16QGrpcCallOptionsSt10shared_ptrI27QAbstractProtobufSerializerEP14QGrpcOperationNS_18PrivateConstructorE(
    const QtGrpc::RpcDescriptor *description,
    const QGrpcCallOptions *options,
    const std::shared_ptr<QAbstractProtobufSerializer> *serializer,
    QGrpcOperation *parent,
    const QGrpcOperationContext::PrivateConstructor *a4) {
  return new QGrpcOperationContext(
      *description,
      *options,
      *serializer,
      parent,
      *a4);
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

#if QT_DEPRECATED_SINCE(6, 13)
//  const QHash<QByteArray, QByteArray>
//      &QGrpcOperationContext::serverMetadata() const
extern "C" Q_DECL_EXPORT
const QHash<QByteArray, QByteArray> *ritual_ZNKR21QGrpcOperationContext14serverMetadataEv(
    const QGrpcOperationContext *self) {
  return &(self->serverMetadata());
}
#endif  // QT_DEPRECATED_SINCE(6, 13)

#if QT_DEPRECATED_SINCE(6, 13)
//  void QGrpcOperationContext::setServerMetadata(const QHash<QByteArray,
//      QByteArray> &metadata)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGrpcOperationContext17setServerMetadataERK5QHashI10QByteArrayS1_E(
    QGrpcOperationContext *self,
    const QHash<QByteArray, QByteArray> *metadata) {
  self->setServerMetadata(*metadata);
}
#endif  // QT_DEPRECATED_SINCE(6, 13)

#if QT_DEPRECATED_SINCE(6, 13)
//  void QGrpcOperationContext::setServerMetadata(QHash<QByteArray,
//      QByteArray> &&metadata)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGrpcOperationContext17setServerMetadataEO5QHashI10QByteArrayS1_E(
    QGrpcOperationContext *self,
    QHash<QByteArray, QByteArray> *metadata) {
  self->setServerMetadata(std::move(*metadata));
}
#endif  // QT_DEPRECATED_SINCE(6, 13)

//  const QMultiHash<QByteArray, QByteArray>
//      &QGrpcOperationContext::serverInitialMetadata() const
extern "C" Q_DECL_EXPORT
const QMultiHash<QByteArray, QByteArray> *ritual_ZNKR21QGrpcOperationContext21serverInitialMetadataEv(
    const QGrpcOperationContext *self) {
  return &(self->serverInitialMetadata());
}

//  void
//      QGrpcOperationContext::setServerInitialMetadata(QMultiHash<QByteArray
//      , QByteArray> &&metadata)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGrpcOperationContext24setServerInitialMetadataEO10QMultiHashI10QByteArrayS1_E(
    QGrpcOperationContext *self,
    QMultiHash<QByteArray, QByteArray> *metadata) {
  self->setServerInitialMetadata(std::move(*metadata));
}

//  const QMultiHash<QByteArray, QByteArray>
//      &QGrpcOperationContext::serverTrailingMetadata() const
extern "C" Q_DECL_EXPORT
const QMultiHash<QByteArray, QByteArray> *ritual_ZNKR21QGrpcOperationContext22serverTrailingMetadataEv(
    const QGrpcOperationContext *self) {
  return &(self->serverTrailingMetadata());
}

//  void
//      QGrpcOperationContext::setServerTrailingMetadata(QMultiHash<QByteArra
//      y, QByteArray> &&metadata)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGrpcOperationContext25setServerTrailingMetadataEO10QMultiHashI10QByteArrayS1_E(
    QGrpcOperationContext *self,
    QMultiHash<QByteArray, QByteArray> *metadata) {
  self->setServerTrailingMetadata(std::move(*metadata));
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

//  std::shared_ptr<const QAbstractProtobufSerializer>
//      QGrpcOperationContext::serializer() const
extern "C" Q_DECL_EXPORT
std::shared_ptr<const QAbstractProtobufSerializer> *ritual_ZNK21QGrpcOperationContext10serializerEv(
    const QGrpcOperationContext *self) {
  return new std::shared_ptr<const QAbstractProtobufSerializer>(
      self->serializer());
}

//  quint64 QGrpcOperationContext::operationId() const
extern "C" Q_DECL_EXPORT
quint64 ritual_ZNK21QGrpcOperationContext11operationIdEv(
    const QGrpcOperationContext *self) {
  return self->operationId();
}

//  void QGrpcOperationContext::finished(const QGrpcStatus &status)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGrpcOperationContext8finishedERK11QGrpcStatus(
    QGrpcOperationContext *self,
    const QGrpcStatus *status) {
  self->finished(*status);
}

//  void QGrpcOperationContext::messageReceived(const QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGrpcOperationContext15messageReceivedERK10QByteArray(
    QGrpcOperationContext *self,
    const QByteArray *data) {
  self->messageReceived(*data);
}

//  void QGrpcOperationContext::cancelRequested()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGrpcOperationContext15cancelRequestedEv(
    QGrpcOperationContext *self) {
  self->cancelRequested();
}

//  void QGrpcOperationContext::writeMessageRequested(const QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGrpcOperationContext21writeMessageRequestedERK10QByteArray(
    QGrpcOperationContext *self,
    const QByteArray *data) {
  self->writeMessageRequested(*data);
}

//  void QGrpcOperationContext::writesDoneRequested()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGrpcOperationContext19writesDoneRequestedEv(
    QGrpcOperationContext *self) {
  self->writesDoneRequested();
}

//  void QGrpcOperationContext::serverInitialMetadataReceived(const
//      QMultiHash<QByteArray, QByteArray> &metadata, QPrivateSignal a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGrpcOperationContext29serverInitialMetadataReceivedERK10QMultiHashI10QByteArrayS1_ENS_14QPrivateSignalE(
    QGrpcOperationContext *self,
    const QMultiHash<QByteArray, QByteArray> *metadata) {
  self->serverInitialMetadataReceived(
      *metadata,
      QGrpcOperationContext::QPrivateSignal());
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

//  const QGrpcOperation &QGrpcOperationContext::operation() const
extern "C" Q_DECL_EXPORT
const QGrpcOperation *ritual_ZNKR21QGrpcOperationContext9operationEv(
    const QGrpcOperationContext *self) {
  return &(self->operation());
}

//  QGrpcOperation &QGrpcOperationContext::operation()
extern "C" Q_DECL_EXPORT
QGrpcOperation *ritual_ZNR21QGrpcOperationContext9operationEv(
    QGrpcOperationContext *self) {
  return &(self->operation());
}

//  bool QGrpcOperationContext::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QGrpcOperationContext5eventEP6QEvent(
    QGrpcOperationContext *self,
    QEvent *event) {
  return self->event(event);
}

//  a std::shared_ptr<const QAbstractProtobufSerializer> a ritual of
//      QGrpcOperationContext gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QGrpcOperationContext__std_shared_ptr_const_QAbstractProtobufSerializer(
    std::shared_ptr<const QAbstractProtobufSerializer> *self) {
  delete self;
}
