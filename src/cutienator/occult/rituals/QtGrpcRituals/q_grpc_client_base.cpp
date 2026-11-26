//  Written by dev_tooling.RitualGenerator from the records of
//  QtGrpc/qgrpcclientbase.h, Qt 6.12.0. Changes made here are lost.
#include <QtGrpc/qgrpcclientbase.h>
#include <QtCore/qstring.h>
#include <QtCore/qlatin1stringview.h>
#include <QtGrpc/qgrpccalloptions.h>
#include <QtCore/qmetatype.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <memory>
#include <QtGrpc/QAbstractGrpcChannel>
#include <QtGrpc/QGrpcCallReply>
#include <QtCore/QLatin1String>
#include <QtGrpc/QGrpcCallOptions>
#include <QtGrpc/QGrpcServerStream>
#include <QtGrpc/QGrpcClientStream>
#include <QtGrpc/QGrpcBidiStream>

//  A QGrpcClientBase that Python can take functions over in. Every QGrpcClientBase
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGrpcClientBaseCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGrpcClientBaseCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGrpcClientBaseCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGrpcClientBaseCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGrpcClientBaseCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGrpcClientBaseCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGrpcClientBaseCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQGrpcClientBase : public QGrpcClientBase {
public:
  using QGrpcClientBase::QGrpcClientBase;
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
  //  bool QGrpcClientBase::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQGrpcClientBaseCall0 call = reinterpret_cast<CuteQGrpcClientBaseCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QGrpcClientBase::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQGrpcClientBaseCall1 call = reinterpret_cast<CuteQGrpcClientBaseCall1>(taken[1]);
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
      CuteQGrpcClientBaseCall2 call = reinterpret_cast<CuteQGrpcClientBaseCall2>(taken[2]);
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
      CuteQGrpcClientBaseCall3 call = reinterpret_cast<CuteQGrpcClientBaseCall3>(taken[3]);
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
      CuteQGrpcClientBaseCall4 call = reinterpret_cast<CuteQGrpcClientBaseCall4>(taken[4]);
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
      CuteQGrpcClientBaseCall5 call = reinterpret_cast<CuteQGrpcClientBaseCall5>(taken[5]);
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
      CuteQGrpcClientBaseCall6 call = reinterpret_cast<CuteQGrpcClientBaseCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QGrpcClientBase::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QGrpcClientBase10metaObjectEv(
    const QGrpcClientBase *self) {
  return self->metaObject();
}

//  void *QGrpcClientBase::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN15QGrpcClientBase11qt_metacastEPKc(
    QGrpcClientBase *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QGrpcClientBase::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QGrpcClientBase11qt_metacallEN11QMetaObject4CallEiPPv(
    QGrpcClientBase *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QGrpcClientBase::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QGrpcClientBase2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGrpcClientBase::tr(s, c, n));
}

//  QGrpcClientBase::~QGrpcClientBase()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGrpcClientBaseD1Ev(QGrpcClientBase *self) {
  delete self;
}

//  bool QGrpcClientBase::attachChannel(std::shared_ptr<QAbstractGrpcChannel>
//      channel)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QGrpcClientBase13attachChannelESt10shared_ptrI20QAbstractGrpcChannelE(
    QGrpcClientBase *self,
    const std::shared_ptr<QAbstractGrpcChannel> *channel) {
  return self->attachChannel(*channel);
}

//  std::shared_ptr<QAbstractGrpcChannel> QGrpcClientBase::channel() const
extern "C" Q_DECL_EXPORT
std::shared_ptr<QAbstractGrpcChannel> *ritual_ZNK15QGrpcClientBase7channelEv(
    const QGrpcClientBase *self) {
  return new std::shared_ptr<QAbstractGrpcChannel>(self->channel());
}

//  void QGrpcClientBase::channelChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGrpcClientBase14channelChangedEv(QGrpcClientBase *self) {
  self->channelChanged();
}

//  QGrpcClientBase::QGrpcClientBase(QLatin1StringView service, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QGrpcClientBase *ritual_ZN15QGrpcClientBaseC1E13QLatin1StringP7QObject(
    const QLatin1String *service,
    QObject *parent) {
  return new CuteQGrpcClientBase(*service, parent);
}

//  std::unique_ptr<QGrpcCallReply> QGrpcClientBase::call(QLatin1StringView
//      method, const QProtobufMessage &arg, const QGrpcCallOptions &options)
extern "C" Q_DECL_EXPORT
std::unique_ptr<QGrpcCallReply> *ritual_ZN15QGrpcClientBase4callE13QLatin1StringRK16QProtobufMessageRK16QGrpcCallOptions(
    QGrpcClientBase *self,
    const QLatin1String *method,
    const QProtobufMessage *arg,
    const QGrpcCallOptions *options) {
  return new std::unique_ptr<QGrpcCallReply>(
      self->call(
          *method,
          *arg,
          *options));
}

//  std::unique_ptr<QGrpcServerStream>
//      QGrpcClientBase::serverStream(QLatin1StringView method, const
//      QProtobufMessage &arg, const QGrpcCallOptions &options)
extern "C" Q_DECL_EXPORT
std::unique_ptr<QGrpcServerStream> *ritual_ZN15QGrpcClientBase12serverStreamE13QLatin1StringRK16QProtobufMessageRK16QGrpcCallOptions(
    QGrpcClientBase *self,
    const QLatin1String *method,
    const QProtobufMessage *arg,
    const QGrpcCallOptions *options) {
  return new std::unique_ptr<QGrpcServerStream>(
      self->serverStream(
          *method,
          *arg,
          *options));
}

//  std::unique_ptr<QGrpcClientStream>
//      QGrpcClientBase::clientStream(QLatin1StringView method, const
//      QProtobufMessage &arg, const QGrpcCallOptions &options)
extern "C" Q_DECL_EXPORT
std::unique_ptr<QGrpcClientStream> *ritual_ZN15QGrpcClientBase12clientStreamE13QLatin1StringRK16QProtobufMessageRK16QGrpcCallOptions(
    QGrpcClientBase *self,
    const QLatin1String *method,
    const QProtobufMessage *arg,
    const QGrpcCallOptions *options) {
  return new std::unique_ptr<QGrpcClientStream>(
      self->clientStream(
          *method,
          *arg,
          *options));
}

//  std::unique_ptr<QGrpcBidiStream>
//      QGrpcClientBase::bidiStream(QLatin1StringView method, const
//      QProtobufMessage &arg, const QGrpcCallOptions &options)
extern "C" Q_DECL_EXPORT
std::unique_ptr<QGrpcBidiStream> *ritual_ZN15QGrpcClientBase10bidiStreamE13QLatin1StringRK16QProtobufMessageRK16QGrpcCallOptions(
    QGrpcClientBase *self,
    const QLatin1String *method,
    const QProtobufMessage *arg,
    const QGrpcCallOptions *options) {
  return new std::unique_ptr<QGrpcBidiStream>(
      self->bidiStream(
          *method,
          *arg,
          *options));
}

//  void QGrpcClientBase::setOperationResponseMetaType(QGrpcOperation
//      *operation, QMetaType responseMetaType)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGrpcClientBase28setOperationResponseMetaTypeEP14QGrpcOperation9QMetaType(
    QGrpcOperation *operation,
    const QMetaType *responseMetaType) {
  QGrpcClientBase::setOperationResponseMetaType(
      operation,
      *responseMetaType);
}

//  QGrpcClientBasePrivate *QGrpcClientBase::d_func()
extern "C" Q_DECL_EXPORT
QGrpcClientBasePrivate *ritual_ZN15QGrpcClientBase6d_funcEv(
    QGrpcClientBase *self) {
  return self->d_func();
}

//  const QGrpcClientBasePrivate *QGrpcClientBase::d_func() const
extern "C" Q_DECL_EXPORT
const QGrpcClientBasePrivate *ritual_ZNK15QGrpcClientBase6d_funcEv(
    const QGrpcClientBase *self) {
  return self->d_func();
}

//  bool QGrpcClientBase::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QGrpcClientBase5eventEP6QEvent(
    QGrpcClientBase *self,
    QEvent *event) {
  return self->event(event);
}

//  a Python function taken by a CuteQGrpcClientBase, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGrpcClientBase(
    QGrpcClientBase *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGrpcClientBase *>(self)->take(key, call);
}

//  bool QGrpcClientBase::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN15QGrpcClientBase5eventEP6QEvent(
    QGrpcClientBase *self,
    QEvent *event) {
  return self->QGrpcClientBase::event(event);
}

//  a std::shared_ptr<QAbstractGrpcChannel> a ritual of QGrpcClientBase gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QGrpcClientBase__std_shared_ptr_QAbstractGrpcChannel(
    std::shared_ptr<QAbstractGrpcChannel> *self) {
  delete self;
}

//  a std::unique_ptr<QGrpcCallReply> a ritual of QGrpcClientBase gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QGrpcClientBase__std_unique_ptr_QGrpcCallReply(
    std::unique_ptr<QGrpcCallReply> *self) {
  delete self;
}

//  a std::unique_ptr<QGrpcServerStream> a ritual of QGrpcClientBase gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QGrpcClientBase__std_unique_ptr_QGrpcServerStream(
    std::unique_ptr<QGrpcServerStream> *self) {
  delete self;
}

//  a std::unique_ptr<QGrpcClientStream> a ritual of QGrpcClientBase gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QGrpcClientBase__std_unique_ptr_QGrpcClientStream(
    std::unique_ptr<QGrpcClientStream> *self) {
  delete self;
}

//  a std::unique_ptr<QGrpcBidiStream> a ritual of QGrpcClientBase gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QGrpcClientBase__std_unique_ptr_QGrpcBidiStream(
    std::unique_ptr<QGrpcBidiStream> *self) {
  delete self;
}
