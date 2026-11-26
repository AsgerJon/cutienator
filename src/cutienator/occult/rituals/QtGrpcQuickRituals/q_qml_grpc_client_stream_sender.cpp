//  Written by dev_tooling.RitualGenerator from the records of
//  QtGrpcQuick/qtqmlgrpcstreamsender.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGrpcQuick/QtGrpcQuick>
#include <QtGrpcQuick/qtqmlgrpcstreamsender.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQmlGrpcClientStreamSender that Python can take functions over in. Every QQmlGrpcClientStreamSender
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlGrpcClientStreamSenderCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlGrpcClientStreamSenderCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlGrpcClientStreamSenderCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlGrpcClientStreamSenderCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlGrpcClientStreamSenderCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlGrpcClientStreamSenderCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlGrpcClientStreamSenderCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQmlGrpcClientStreamSender : public QQmlGrpcClientStreamSender {
public:
  using QQmlGrpcClientStreamSender::QQmlGrpcClientStreamSender;
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
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlGrpcClientStreamSenderCall0 call = reinterpret_cast<CuteQQmlGrpcClientStreamSenderCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlGrpcClientStreamSenderCall1 call = reinterpret_cast<CuteQQmlGrpcClientStreamSenderCall1>(taken[1]);
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
      CuteQQmlGrpcClientStreamSenderCall2 call = reinterpret_cast<CuteQQmlGrpcClientStreamSenderCall2>(taken[2]);
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
      CuteQQmlGrpcClientStreamSenderCall3 call = reinterpret_cast<CuteQQmlGrpcClientStreamSenderCall3>(taken[3]);
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
      CuteQQmlGrpcClientStreamSenderCall4 call = reinterpret_cast<CuteQQmlGrpcClientStreamSenderCall4>(taken[4]);
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
      CuteQQmlGrpcClientStreamSenderCall5 call = reinterpret_cast<CuteQQmlGrpcClientStreamSenderCall5>(taken[5]);
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
      CuteQQmlGrpcClientStreamSenderCall6 call = reinterpret_cast<CuteQQmlGrpcClientStreamSenderCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQmlGrpcClientStreamSender::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK26QQmlGrpcClientStreamSender10metaObjectEv(
    const QQmlGrpcClientStreamSender *self) {
  return self->metaObject();
}

//  void *QQmlGrpcClientStreamSender::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN26QQmlGrpcClientStreamSender11qt_metacastEPKc(
    QQmlGrpcClientStreamSender *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQmlGrpcClientStreamSender::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN26QQmlGrpcClientStreamSender11qt_metacallEN11QMetaObject4CallEiPPv(
    QQmlGrpcClientStreamSender *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQmlGrpcClientStreamSender::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN26QQmlGrpcClientStreamSender2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlGrpcClientStreamSender::tr(s, c, n));
}

//  QQmlGrpcClientStreamSender::~QQmlGrpcClientStreamSender()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQmlGrpcClientStreamSenderD1Ev(
    QQmlGrpcClientStreamSender *self) {
  delete self;
}

//  QQmlGrpcClientStreamSender::QQmlGrpcClientStreamSender(QGrpcClientStream
//      *stream, QObject *parent)
extern "C" Q_DECL_EXPORT
QQmlGrpcClientStreamSender *ritual_ZN26QQmlGrpcClientStreamSenderC1EP17QGrpcClientStreamP7QObject(
    QGrpcClientStream *stream,
    QObject *parent) {
  return new CuteQQmlGrpcClientStreamSender(stream, parent);
}

//  void QQmlGrpcClientStreamSender::writeMessageImpl(const QProtobufMessage
//      &message) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK26QQmlGrpcClientStreamSender16writeMessageImplERK16QProtobufMessage(
    const QQmlGrpcClientStreamSender *self,
    const QProtobufMessage *message) {
  self->writeMessageImpl(*message);
}

//  QQmlGrpcClientStreamSenderPrivate *QQmlGrpcClientStreamSender::d_func()
extern "C" Q_DECL_EXPORT
QQmlGrpcClientStreamSenderPrivate *ritual_ZN26QQmlGrpcClientStreamSender6d_funcEv(
    QQmlGrpcClientStreamSender *self) {
  return self->d_func();
}

//  const QQmlGrpcClientStreamSenderPrivate
//      *QQmlGrpcClientStreamSender::d_func() const
extern "C" Q_DECL_EXPORT
const QQmlGrpcClientStreamSenderPrivate *ritual_ZNK26QQmlGrpcClientStreamSender6d_funcEv(
    const QQmlGrpcClientStreamSender *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQmlGrpcClientStreamSender, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlGrpcClientStreamSender(
    QQmlGrpcClientStreamSender *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlGrpcClientStreamSender *>(self)->take(key, call);
}
