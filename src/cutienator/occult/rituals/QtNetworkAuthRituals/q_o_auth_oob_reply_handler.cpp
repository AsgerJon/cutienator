//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetworkAuth/qoauthoobreplyhandler.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtNetworkAuth/qoauthglobal.h>
#if !defined(QT_NO_HTTP)
#include <QtNetworkAuth/qoauthoobreplyhandler.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>

//  Only a class built on QOAuthOobReplyHandler may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQOAuthOobReplyHandler : QOAuthOobReplyHandler {
  using QOAuthOobReplyHandler::networkReplyFinished;
};

//  A QOAuthOobReplyHandler that Python can take functions over in. Every QOAuthOobReplyHandler
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_HTTP)
typedef QString * (*CuteQOAuthOobReplyHandlerCall0)(const void *, int *);
#endif  // !defined(QT_NO_HTTP)
#if !defined(QT_NO_HTTP)
typedef void (*CuteQOAuthOobReplyHandlerCall1)(const void *, QNetworkReply *, int *);
#endif  // !defined(QT_NO_HTTP)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQOAuthOobReplyHandlerCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQOAuthOobReplyHandlerCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOAuthOobReplyHandlerCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOAuthOobReplyHandlerCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOAuthOobReplyHandlerCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOAuthOobReplyHandlerCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOAuthOobReplyHandlerCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQOAuthOobReplyHandler : public QOAuthOobReplyHandler {
public:
  using QOAuthOobReplyHandler::QOAuthOobReplyHandler;
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
  //  QString QOAuthOobReplyHandler::callback() const
  QString callback() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQOAuthOobReplyHandlerCall0 call = reinterpret_cast<CuteQOAuthOobReplyHandlerCall0>(taken[0]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QOAuthOobReplyHandler::callback();
  }
#endif  // !defined(QT_NO_HTTP)

#if !defined(QT_NO_HTTP)
  //  void QOAuthOobReplyHandler::networkReplyFinished(QNetworkReply
  //      *reply)
  void networkReplyFinished(QNetworkReply *reply) override {
    if (taken[1]) {
      int handled = 0;
      CuteQOAuthOobReplyHandlerCall1 call = reinterpret_cast<CuteQOAuthOobReplyHandlerCall1>(taken[1]);
      call(this, reply, &handled);
      if (handled) return;
    }
    QOAuthOobReplyHandler::networkReplyFinished(reply);
  }
#endif  // !defined(QT_NO_HTTP)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQOAuthOobReplyHandlerCall2 call = reinterpret_cast<CuteQOAuthOobReplyHandlerCall2>(taken[2]);
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
      CuteQOAuthOobReplyHandlerCall3 call = reinterpret_cast<CuteQOAuthOobReplyHandlerCall3>(taken[3]);
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
      CuteQOAuthOobReplyHandlerCall4 call = reinterpret_cast<CuteQOAuthOobReplyHandlerCall4>(taken[4]);
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
      CuteQOAuthOobReplyHandlerCall5 call = reinterpret_cast<CuteQOAuthOobReplyHandlerCall5>(taken[5]);
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
      CuteQOAuthOobReplyHandlerCall6 call = reinterpret_cast<CuteQOAuthOobReplyHandlerCall6>(taken[6]);
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
      CuteQOAuthOobReplyHandlerCall7 call = reinterpret_cast<CuteQOAuthOobReplyHandlerCall7>(taken[7]);
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
      CuteQOAuthOobReplyHandlerCall8 call = reinterpret_cast<CuteQOAuthOobReplyHandlerCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QOAuthOobReplyHandler::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QOAuthOobReplyHandler10metaObjectEv(
    const QOAuthOobReplyHandler *self) {
  return self->metaObject();
}

//  void *QOAuthOobReplyHandler::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN21QOAuthOobReplyHandler11qt_metacastEPKc(
    QOAuthOobReplyHandler *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QOAuthOobReplyHandler::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QOAuthOobReplyHandler11qt_metacallEN11QMetaObject4CallEiPPv(
    QOAuthOobReplyHandler *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QOAuthOobReplyHandler::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QOAuthOobReplyHandler2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QOAuthOobReplyHandler::tr(s, c, n));
}

//  QOAuthOobReplyHandler::QOAuthOobReplyHandler(QObject *parent)
extern "C" Q_DECL_EXPORT
QOAuthOobReplyHandler *ritual_ZN21QOAuthOobReplyHandlerC1EP7QObject(
    QObject *parent) {
  return new CuteQOAuthOobReplyHandler(parent);
}

//  QOAuthOobReplyHandler::~QOAuthOobReplyHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOAuthOobReplyHandlerD1Ev(QOAuthOobReplyHandler *self) {
  delete self;
}

//  QString QOAuthOobReplyHandler::callback() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QOAuthOobReplyHandler8callbackEv(
    const QOAuthOobReplyHandler *self) {
  return new QString(self->callback());
}

//  void QOAuthOobReplyHandler::networkReplyFinished(QNetworkReply *reply)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOAuthOobReplyHandler20networkReplyFinishedEP13QNetworkReply(
    QOAuthOobReplyHandler *self,
    QNetworkReply *reply) {
  self->networkReplyFinished(reply);
}

//  QOAuthOobReplyHandler::QOAuthOobReplyHandler(QOAuthOobReplyHandlerPrivate
//      &a0, QObject *parent)
extern "C" Q_DECL_EXPORT
QOAuthOobReplyHandler *ritual_ZN21QOAuthOobReplyHandlerC1ER28QOAuthOobReplyHandlerPrivateP7QObject(
    QOAuthOobReplyHandlerPrivate *a0,
    QObject *parent) {
  return new CuteQOAuthOobReplyHandler(*a0, parent);
}

//  QVariantMap QOAuthOobReplyHandler::parseResponse(const QByteArray
//      &response)
extern "C" Q_DECL_EXPORT
QMap<QString, QVariant> *ritual_ZN21QOAuthOobReplyHandler13parseResponseERK10QByteArray(
    QOAuthOobReplyHandler *self,
    const QByteArray *response) {
  return new QMap<QString, QVariant>(self->parseResponse(*response));
}

//  a Python function taken by a CuteQOAuthOobReplyHandler, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QOAuthOobReplyHandler(
    QOAuthOobReplyHandler *self,
    const char *key,
    void *call) {
  return static_cast<CuteQOAuthOobReplyHandler *>(self)->take(key, call);
}

//  QString QOAuthOobReplyHandler::callback() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK21QOAuthOobReplyHandler8callbackEv(
    const QOAuthOobReplyHandler *self) {
  return new QString(self->QOAuthOobReplyHandler::callback());
}

//  void QOAuthOobReplyHandler::networkReplyFinished(QNetworkReply *reply)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QOAuthOobReplyHandler20networkReplyFinishedEP13QNetworkReply(
    QOAuthOobReplyHandler *self,
    QNetworkReply *reply) {
  static_cast<OwnQOAuthOobReplyHandler *>(self)->OwnQOAuthOobReplyHandler::networkReplyFinished(
      reply);
}

#endif  // !defined(QT_NO_HTTP)
