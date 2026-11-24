//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetworkAuth/qabstractoauthreplyhandler.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtNetworkAuth/qoauthglobal.h>
#if !defined(QT_NO_HTTP)
#include <QtNetworkAuth/qabstractoauthreplyhandler.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QAbstractOAuthReplyHandler that Python can take functions over in. Every QAbstractOAuthReplyHandler
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_HTTP)
typedef QString * (*CuteQAbstractOAuthReplyHandlerCall0)(const void *, int *);
#endif  // !defined(QT_NO_HTTP)
#if !defined(QT_NO_HTTP)
typedef void (*CuteQAbstractOAuthReplyHandlerCall1)(const void *, QNetworkReply *, int *);
#endif  // !defined(QT_NO_HTTP)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAbstractOAuthReplyHandlerCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAbstractOAuthReplyHandlerCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractOAuthReplyHandlerCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractOAuthReplyHandlerCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractOAuthReplyHandlerCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractOAuthReplyHandlerCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractOAuthReplyHandlerCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAbstractOAuthReplyHandler : public QAbstractOAuthReplyHandler {
public:
  using QAbstractOAuthReplyHandler::QAbstractOAuthReplyHandler;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_HTTP)
    if (!std::strcmp(key, "_ZNK26QAbstractOAuthReplyHandler8callbackEv")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_HTTP)
#if !defined(QT_NO_HTTP)
    if (!std::strcmp(key, "_ZN26QAbstractOAuthReplyHandler20networkReplyFinishedEP13QNetworkReply")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_HTTP)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_HTTP)
  //  QString QAbstractOAuthReplyHandler::callback() const
  QString callback() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAbstractOAuthReplyHandlerCall0 call = reinterpret_cast<CuteQAbstractOAuthReplyHandlerCall0>(taken[0]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }
#endif  // !defined(QT_NO_HTTP)

#if !defined(QT_NO_HTTP)
  //  void QAbstractOAuthReplyHandler::networkReplyFinished(QNetworkReply
  //      *reply)
  void networkReplyFinished(QNetworkReply *reply) override {
    if (taken[1]) {
      int handled = 0;
      CuteQAbstractOAuthReplyHandlerCall1 call = reinterpret_cast<CuteQAbstractOAuthReplyHandlerCall1>(taken[1]);
      call(this, reply, &handled);
      if (handled) return;
    }
  }
#endif  // !defined(QT_NO_HTTP)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQAbstractOAuthReplyHandlerCall2 call = reinterpret_cast<CuteQAbstractOAuthReplyHandlerCall2>(taken[2]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQAbstractOAuthReplyHandlerCall3 call = reinterpret_cast<CuteQAbstractOAuthReplyHandlerCall3>(taken[3]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQAbstractOAuthReplyHandlerCall4 call = reinterpret_cast<CuteQAbstractOAuthReplyHandlerCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQAbstractOAuthReplyHandlerCall5 call = reinterpret_cast<CuteQAbstractOAuthReplyHandlerCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQAbstractOAuthReplyHandlerCall6 call = reinterpret_cast<CuteQAbstractOAuthReplyHandlerCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQAbstractOAuthReplyHandlerCall7 call = reinterpret_cast<CuteQAbstractOAuthReplyHandlerCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQAbstractOAuthReplyHandlerCall8 call = reinterpret_cast<CuteQAbstractOAuthReplyHandlerCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QAbstractOAuthReplyHandler::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK26QAbstractOAuthReplyHandler10metaObjectEv(
    const QAbstractOAuthReplyHandler *self) {
  return self->metaObject();
}

//  QString QAbstractOAuthReplyHandler::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN26QAbstractOAuthReplyHandler2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAbstractOAuthReplyHandler::tr(s, c, n));
}

//  QAbstractOAuthReplyHandler::~QAbstractOAuthReplyHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QAbstractOAuthReplyHandlerD1Ev(
    QAbstractOAuthReplyHandler *self) {
  delete self;
}

//  QString QAbstractOAuthReplyHandler::callback() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QAbstractOAuthReplyHandler8callbackEv(
    const QAbstractOAuthReplyHandler *self) {
  return new QString(self->callback());
}

//  void QAbstractOAuthReplyHandler::networkReplyFinished(QNetworkReply
//      *reply)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QAbstractOAuthReplyHandler20networkReplyFinishedEP13QNetworkReply(
    QAbstractOAuthReplyHandler *self,
    QNetworkReply *reply) {
  self->networkReplyFinished(reply);
}

//  a Python function taken by a CuteQAbstractOAuthReplyHandler, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstractOAuthReplyHandler(
    QAbstractOAuthReplyHandler *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstractOAuthReplyHandler *>(self)->take(key, call);
}

#endif  // !defined(QT_NO_HTTP)
