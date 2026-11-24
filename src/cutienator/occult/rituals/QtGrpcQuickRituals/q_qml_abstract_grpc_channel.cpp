//  Written by dev_tooling.RitualGenerator from the records of
//  QtGrpcQuick/qqmlabstractgrpcchannel.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGrpcQuick/QtGrpcQuick>
#include <QtGrpcQuick/qqmlabstractgrpcchannel.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQmlAbstractGrpcChannel that Python can take functions over in. Every QQmlAbstractGrpcChannel
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlAbstractGrpcChannelCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlAbstractGrpcChannelCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlAbstractGrpcChannelCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlAbstractGrpcChannelCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlAbstractGrpcChannelCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlAbstractGrpcChannelCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlAbstractGrpcChannelCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQmlAbstractGrpcChannel : public QQmlAbstractGrpcChannel {
public:
  using QQmlAbstractGrpcChannel::QQmlAbstractGrpcChannel;
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
      CuteQQmlAbstractGrpcChannelCall0 call = reinterpret_cast<CuteQQmlAbstractGrpcChannelCall0>(taken[0]);
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
      CuteQQmlAbstractGrpcChannelCall1 call = reinterpret_cast<CuteQQmlAbstractGrpcChannelCall1>(taken[1]);
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
      CuteQQmlAbstractGrpcChannelCall2 call = reinterpret_cast<CuteQQmlAbstractGrpcChannelCall2>(taken[2]);
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
      CuteQQmlAbstractGrpcChannelCall3 call = reinterpret_cast<CuteQQmlAbstractGrpcChannelCall3>(taken[3]);
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
      CuteQQmlAbstractGrpcChannelCall4 call = reinterpret_cast<CuteQQmlAbstractGrpcChannelCall4>(taken[4]);
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
      CuteQQmlAbstractGrpcChannelCall5 call = reinterpret_cast<CuteQQmlAbstractGrpcChannelCall5>(taken[5]);
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
      CuteQQmlAbstractGrpcChannelCall6 call = reinterpret_cast<CuteQQmlAbstractGrpcChannelCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQmlAbstractGrpcChannel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QQmlAbstractGrpcChannel10metaObjectEv(
    const QQmlAbstractGrpcChannel *self) {
  return self->metaObject();
}

//  QString QQmlAbstractGrpcChannel::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QQmlAbstractGrpcChannel2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlAbstractGrpcChannel::tr(s, c, n));
}

//  QQmlAbstractGrpcChannel::~QQmlAbstractGrpcChannel()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQmlAbstractGrpcChannelD1Ev(QQmlAbstractGrpcChannel *self) {
  delete self;
}

//  QQmlAbstractGrpcChannelPrivate *QQmlAbstractGrpcChannel::d_func()
extern "C" Q_DECL_EXPORT
QQmlAbstractGrpcChannelPrivate *ritual_ZN23QQmlAbstractGrpcChannel6d_funcEv(
    QQmlAbstractGrpcChannel *self) {
  return self->d_func();
}

//  const QQmlAbstractGrpcChannelPrivate *QQmlAbstractGrpcChannel::d_func()
//      const
extern "C" Q_DECL_EXPORT
const QQmlAbstractGrpcChannelPrivate *ritual_ZNK23QQmlAbstractGrpcChannel6d_funcEv(
    const QQmlAbstractGrpcChannel *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQmlAbstractGrpcChannel, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlAbstractGrpcChannel(
    QQmlAbstractGrpcChannel *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlAbstractGrpcChannel *>(self)->take(key, call);
}
