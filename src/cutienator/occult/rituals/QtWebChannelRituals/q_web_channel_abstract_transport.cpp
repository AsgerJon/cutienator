//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebChannel/qwebchannelabstracttransport.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtWebChannel/qwebchannelabstracttransport.h>
#include <QtCore/qstring.h>
#include <QtCore/qjsonobject.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QWebChannelAbstractTransport that Python can take functions over in. Every QWebChannelAbstractTransport
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQWebChannelAbstractTransportCall0)(const void *, const QJsonObject *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWebChannelAbstractTransportCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWebChannelAbstractTransportCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebChannelAbstractTransportCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebChannelAbstractTransportCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebChannelAbstractTransportCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebChannelAbstractTransportCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebChannelAbstractTransportCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQWebChannelAbstractTransport : public QWebChannelAbstractTransport {
public:
  using QWebChannelAbstractTransport::QWebChannelAbstractTransport;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN28QWebChannelAbstractTransport11sendMessageERK11QJsonObject")) {
      taken[0] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QWebChannelAbstractTransport::sendMessage(const QJsonObject
  //      &message)
  void sendMessage(const QJsonObject &message) override {
    if (taken[0]) {
      int handled = 0;
      CuteQWebChannelAbstractTransportCall0 call = reinterpret_cast<CuteQWebChannelAbstractTransportCall0>(taken[0]);
      call(this, &message, &handled);
      if (handled) return;
    }
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQWebChannelAbstractTransportCall1 call = reinterpret_cast<CuteQWebChannelAbstractTransportCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQWebChannelAbstractTransportCall2 call = reinterpret_cast<CuteQWebChannelAbstractTransportCall2>(taken[2]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQWebChannelAbstractTransportCall3 call = reinterpret_cast<CuteQWebChannelAbstractTransportCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQWebChannelAbstractTransportCall4 call = reinterpret_cast<CuteQWebChannelAbstractTransportCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQWebChannelAbstractTransportCall5 call = reinterpret_cast<CuteQWebChannelAbstractTransportCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQWebChannelAbstractTransportCall6 call = reinterpret_cast<CuteQWebChannelAbstractTransportCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQWebChannelAbstractTransportCall7 call = reinterpret_cast<CuteQWebChannelAbstractTransportCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QWebChannelAbstractTransport::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK28QWebChannelAbstractTransport10metaObjectEv(
    const QWebChannelAbstractTransport *self) {
  return self->metaObject();
}

//  QString QWebChannelAbstractTransport::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN28QWebChannelAbstractTransport2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWebChannelAbstractTransport::tr(s, c, n));
}

//  QWebChannelAbstractTransport::~QWebChannelAbstractTransport()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QWebChannelAbstractTransportD1Ev(
    QWebChannelAbstractTransport *self) {
  delete self;
}

//  void QWebChannelAbstractTransport::sendMessage(const QJsonObject
//      &message)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QWebChannelAbstractTransport11sendMessageERK11QJsonObject(
    QWebChannelAbstractTransport *self,
    const QJsonObject *message) {
  self->sendMessage(*message);
}

//  a Python function taken by a CuteQWebChannelAbstractTransport, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWebChannelAbstractTransport(
    QWebChannelAbstractTransport *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWebChannelAbstractTransport *>(self)->take(key, call);
}
