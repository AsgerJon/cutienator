//  Written by dev_tooling.RitualGenerator from the records of
//  QtGrpcQuick/qtqmlgrpcstreamsender.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGrpcQuick/QtGrpcQuick>
#include <QtGrpcQuick/qtqmlgrpcstreamsender.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQmlGrpcBidiStreamSender that Python can take functions over in. Every QQmlGrpcBidiStreamSender
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlGrpcBidiStreamSenderCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlGrpcBidiStreamSenderCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlGrpcBidiStreamSenderCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlGrpcBidiStreamSenderCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlGrpcBidiStreamSenderCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlGrpcBidiStreamSenderCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlGrpcBidiStreamSenderCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQmlGrpcBidiStreamSender : public QQmlGrpcBidiStreamSender {
public:
  using QQmlGrpcBidiStreamSender::QQmlGrpcBidiStreamSender;
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
      CuteQQmlGrpcBidiStreamSenderCall0 call = reinterpret_cast<CuteQQmlGrpcBidiStreamSenderCall0>(taken[0]);
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
      CuteQQmlGrpcBidiStreamSenderCall1 call = reinterpret_cast<CuteQQmlGrpcBidiStreamSenderCall1>(taken[1]);
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
      CuteQQmlGrpcBidiStreamSenderCall2 call = reinterpret_cast<CuteQQmlGrpcBidiStreamSenderCall2>(taken[2]);
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
      CuteQQmlGrpcBidiStreamSenderCall3 call = reinterpret_cast<CuteQQmlGrpcBidiStreamSenderCall3>(taken[3]);
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
      CuteQQmlGrpcBidiStreamSenderCall4 call = reinterpret_cast<CuteQQmlGrpcBidiStreamSenderCall4>(taken[4]);
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
      CuteQQmlGrpcBidiStreamSenderCall5 call = reinterpret_cast<CuteQQmlGrpcBidiStreamSenderCall5>(taken[5]);
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
      CuteQQmlGrpcBidiStreamSenderCall6 call = reinterpret_cast<CuteQQmlGrpcBidiStreamSenderCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQmlGrpcBidiStreamSender::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QQmlGrpcBidiStreamSender10metaObjectEv(
    const QQmlGrpcBidiStreamSender *self) {
  return self->metaObject();
}

//  void *QQmlGrpcBidiStreamSender::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN24QQmlGrpcBidiStreamSender11qt_metacastEPKc(
    QQmlGrpcBidiStreamSender *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQmlGrpcBidiStreamSender::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN24QQmlGrpcBidiStreamSender11qt_metacallEN11QMetaObject4CallEiPPv(
    QQmlGrpcBidiStreamSender *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQmlGrpcBidiStreamSender::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24QQmlGrpcBidiStreamSender2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlGrpcBidiStreamSender::tr(s, c, n));
}

//  QQmlGrpcBidiStreamSender::~QQmlGrpcBidiStreamSender()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlGrpcBidiStreamSenderD1Ev(
    QQmlGrpcBidiStreamSender *self) {
  delete self;
}

//  QQmlGrpcBidiStreamSender::QQmlGrpcBidiStreamSender(QGrpcBidiStream
//      *stream, QObject *parent)
extern "C" Q_DECL_EXPORT
QQmlGrpcBidiStreamSender *ritual_ZN24QQmlGrpcBidiStreamSenderC1EP15QGrpcBidiStreamP7QObject(
    QGrpcBidiStream *stream,
    QObject *parent) {
  return new CuteQQmlGrpcBidiStreamSender(stream, parent);
}

//  void QQmlGrpcBidiStreamSender::writeMessageImpl(const QProtobufMessage
//      &message) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK24QQmlGrpcBidiStreamSender16writeMessageImplERK16QProtobufMessage(
    const QQmlGrpcBidiStreamSender *self,
    const QProtobufMessage *message) {
  self->writeMessageImpl(*message);
}

//  QQmlGrpcBidiStreamSenderPrivate *QQmlGrpcBidiStreamSender::d_func()
extern "C" Q_DECL_EXPORT
QQmlGrpcBidiStreamSenderPrivate *ritual_ZN24QQmlGrpcBidiStreamSender6d_funcEv(
    QQmlGrpcBidiStreamSender *self) {
  return self->d_func();
}

//  const QQmlGrpcBidiStreamSenderPrivate *QQmlGrpcBidiStreamSender::d_func()
//      const
extern "C" Q_DECL_EXPORT
const QQmlGrpcBidiStreamSenderPrivate *ritual_ZNK24QQmlGrpcBidiStreamSender6d_funcEv(
    const QQmlGrpcBidiStreamSender *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQmlGrpcBidiStreamSender, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlGrpcBidiStreamSender(
    QQmlGrpcBidiStreamSender *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlGrpcBidiStreamSender *>(self)->take(key, call);
}
