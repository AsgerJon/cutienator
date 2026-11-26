//  Written by dev_tooling.RitualGenerator from the records of
//  QtGrpc/qgrpcoperation.h, Qt 6.12.0. Changes made here are lost.
#include <QtGrpc/qgrpcoperation.h>
#include <QtCore/qstring.h>
#include <QtCore/qlatin1stringview.h>
#include <QtCore/qmetatype.h>
#include <QtGrpc/qgrpcstatus.h>
#include <QtGrpc/qtgrpcnamespace.h>
#include <QtGrpc/qgrpccalloptions.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QGrpcOperation that Python can take functions over in. Every QGrpcOperation
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGrpcOperationCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGrpcOperationCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGrpcOperationCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGrpcOperationCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGrpcOperationCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGrpcOperationCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGrpcOperationCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQGrpcOperation : public QGrpcOperation {
public:
  using QGrpcOperation::QGrpcOperation;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QGrpcOperation::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQGrpcOperationCall0 call = reinterpret_cast<CuteQGrpcOperationCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QGrpcOperation::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQGrpcOperationCall1 call = reinterpret_cast<CuteQGrpcOperationCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQGrpcOperationCall2 call = reinterpret_cast<CuteQGrpcOperationCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQGrpcOperationCall3 call = reinterpret_cast<CuteQGrpcOperationCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQGrpcOperationCall4 call = reinterpret_cast<CuteQGrpcOperationCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQGrpcOperationCall5 call = reinterpret_cast<CuteQGrpcOperationCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQGrpcOperationCall6 call = reinterpret_cast<CuteQGrpcOperationCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QGrpcOperation::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QGrpcOperation10metaObjectEv(
    const QGrpcOperation *self) {
  return self->metaObject();
}

//  void *QGrpcOperation::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN14QGrpcOperation11qt_metacastEPKc(
    QGrpcOperation *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QGrpcOperation::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QGrpcOperation11qt_metacallEN11QMetaObject4CallEiPPv(
    QGrpcOperation *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QGrpcOperation::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QGrpcOperation2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGrpcOperation::tr(s, c, n));
}

//  QGrpcOperation::~QGrpcOperation()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGrpcOperationD1Ev(QGrpcOperation *self) {
  delete self;
}

//  bool QGrpcOperation::read(QProtobufMessage *message) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QGrpcOperation4readEP16QProtobufMessage(
    const QGrpcOperation *self,
    QProtobufMessage *message) {
  return self->read(message);
}

#if QT_DEPRECATED_SINCE(6, 13)
//  const QHash<QByteArray, QByteArray> &QGrpcOperation::metadata() const
extern "C" Q_DECL_EXPORT
const QHash<QByteArray, QByteArray> *ritual_ZNKR14QGrpcOperation8metadataEv(
    const QGrpcOperation *self) {
  return &(self->metadata());
}
#endif  // QT_DEPRECATED_SINCE(6, 13)

//  const QMultiHash<QByteArray, QByteArray>
//      &QGrpcOperation::serverInitialMetadata() const
extern "C" Q_DECL_EXPORT
const QMultiHash<QByteArray, QByteArray> *ritual_ZNKR14QGrpcOperation21serverInitialMetadataEv(
    const QGrpcOperation *self) {
  return &(self->serverInitialMetadata());
}

//  const QMultiHash<QByteArray, QByteArray>
//      &QGrpcOperation::serverTrailingMetadata() const
extern "C" Q_DECL_EXPORT
const QMultiHash<QByteArray, QByteArray> *ritual_ZNKR14QGrpcOperation22serverTrailingMetadataEv(
    const QGrpcOperation *self) {
  return &(self->serverTrailingMetadata());
}

//  QLatin1StringView QGrpcOperation::method() const
extern "C" Q_DECL_EXPORT
QLatin1String *ritual_ZNK14QGrpcOperation6methodEv(
    const QGrpcOperation *self) {
  return new QLatin1String(self->method());
}

//  bool QGrpcOperation::isFinished() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QGrpcOperation10isFinishedEv(const QGrpcOperation *self) {
  return self->isFinished();
}

//  QMetaType QGrpcOperation::responseMetaType() const
extern "C" Q_DECL_EXPORT
QMetaType *ritual_ZNK14QGrpcOperation16responseMetaTypeEv(
    const QGrpcOperation *self) {
  return new QMetaType(self->responseMetaType());
}

//  void QGrpcOperation::finished(const QGrpcStatus &status)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGrpcOperation8finishedERK11QGrpcStatus(
    QGrpcOperation *self,
    const QGrpcStatus *status) {
  self->finished(*status);
}

//  void QGrpcOperation::serverInitialMetadataReceived(const
//      QMultiHash<QByteArray, QByteArray> &metadata)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGrpcOperation29serverInitialMetadataReceivedERK10QMultiHashI10QByteArrayS1_E(
    QGrpcOperation *self,
    const QMultiHash<QByteArray, QByteArray> *metadata) {
  self->serverInitialMetadataReceived(*metadata);
}

//  void QGrpcOperation::cancel()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGrpcOperation6cancelEv(QGrpcOperation *self) {
  self->cancel();
}

//  QGrpcOperation::QGrpcOperation(QtGrpc::RpcDescriptor descriptor, const
//      QGrpcCallOptions &options, std::weak_ptr<QAbstractGrpcChannel>
//      &&channel)
extern "C" Q_DECL_EXPORT
QGrpcOperation *ritual_ZN14QGrpcOperationC1EN6QtGrpc13RpcDescriptorERK16QGrpcCallOptionsOSt8weak_ptrI20QAbstractGrpcChannelE(
    const QtGrpc::RpcDescriptor *descriptor,
    const QGrpcCallOptions *options,
    std::weak_ptr<QAbstractGrpcChannel> *channel) {
  return new CuteQGrpcOperation(*descriptor, *options, std::move(*channel));
}

//  const QGrpcOperationContext &QGrpcOperation::context() const
extern "C" Q_DECL_EXPORT
const QGrpcOperationContext *ritual_ZNKR14QGrpcOperation7contextEv(
    const QGrpcOperation *self) {
  return &(self->context());
}

//  QGrpcOperationContext &QGrpcOperation::context()
extern "C" Q_DECL_EXPORT
QGrpcOperationContext *ritual_ZNR14QGrpcOperation7contextEv(
    QGrpcOperation *self) {
  return &(self->context());
}

//  void QGrpcOperation::writeMessage(const QProtobufMessage &message)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGrpcOperation12writeMessageERK16QProtobufMessage(
    QGrpcOperation *self,
    const QProtobufMessage *message) {
  self->writeMessage(*message);
}

//  void QGrpcOperation::writesDone()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGrpcOperation10writesDoneEv(QGrpcOperation *self) {
  self->writesDone();
}

//  QGrpcOperationPrivate *QGrpcOperation::d_func()
extern "C" Q_DECL_EXPORT
QGrpcOperationPrivate *ritual_ZN14QGrpcOperation6d_funcEv(
    QGrpcOperation *self) {
  return self->d_func();
}

//  const QGrpcOperationPrivate *QGrpcOperation::d_func() const
extern "C" Q_DECL_EXPORT
const QGrpcOperationPrivate *ritual_ZNK14QGrpcOperation6d_funcEv(
    const QGrpcOperation *self) {
  return self->d_func();
}

//  bool QGrpcOperation::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QGrpcOperation5eventEP6QEvent(
    QGrpcOperation *self,
    QEvent *event) {
  return self->event(event);
}

//  a Python function taken by a CuteQGrpcOperation, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGrpcOperation(
    QGrpcOperation *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGrpcOperation *>(self)->take(key, call);
}

//  bool QGrpcOperation::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN14QGrpcOperation5eventEP6QEvent(
    QGrpcOperation *self,
    QEvent *event) {
  return self->QGrpcOperation::event(event);
}
