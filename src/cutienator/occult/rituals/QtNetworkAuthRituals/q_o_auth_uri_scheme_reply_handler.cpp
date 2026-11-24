//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetworkAuth/qoauthurischemereplyhandler.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtNetworkAuth/qoauthurischemereplyhandler.h>
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QOAuthUriSchemeReplyHandler that Python can take functions over in. Every QOAuthUriSchemeReplyHandler
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_HTTP)
typedef QString * (*CuteQOAuthUriSchemeReplyHandlerCall0)(const void *, int *);
#endif  // !defined(QT_NO_HTTP)
#if !defined(QT_NO_HTTP)
typedef void (*CuteQOAuthUriSchemeReplyHandlerCall1)(const void *, QNetworkReply *, int *);
#endif  // !defined(QT_NO_HTTP)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQOAuthUriSchemeReplyHandlerCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQOAuthUriSchemeReplyHandlerCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOAuthUriSchemeReplyHandlerCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOAuthUriSchemeReplyHandlerCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOAuthUriSchemeReplyHandlerCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOAuthUriSchemeReplyHandlerCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOAuthUriSchemeReplyHandlerCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQOAuthUriSchemeReplyHandler : public QOAuthUriSchemeReplyHandler {
public:
  using QOAuthUriSchemeReplyHandler::QOAuthUriSchemeReplyHandler;
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
  //  QString QOAuthUriSchemeReplyHandler::callback() const
  QString callback() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQOAuthUriSchemeReplyHandlerCall0 call = reinterpret_cast<CuteQOAuthUriSchemeReplyHandlerCall0>(taken[0]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QOAuthUriSchemeReplyHandler::callback();
  }
#endif  // !defined(QT_NO_HTTP)

#if !defined(QT_NO_HTTP)
  //  void QOAuthOobReplyHandler::networkReplyFinished(QNetworkReply
  //      *reply)
  void networkReplyFinished(QNetworkReply *reply) override {
    if (taken[1]) {
      int handled = 0;
      CuteQOAuthUriSchemeReplyHandlerCall1 call = reinterpret_cast<CuteQOAuthUriSchemeReplyHandlerCall1>(taken[1]);
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
      CuteQOAuthUriSchemeReplyHandlerCall2 call = reinterpret_cast<CuteQOAuthUriSchemeReplyHandlerCall2>(taken[2]);
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
      CuteQOAuthUriSchemeReplyHandlerCall3 call = reinterpret_cast<CuteQOAuthUriSchemeReplyHandlerCall3>(taken[3]);
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
      CuteQOAuthUriSchemeReplyHandlerCall4 call = reinterpret_cast<CuteQOAuthUriSchemeReplyHandlerCall4>(taken[4]);
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
      CuteQOAuthUriSchemeReplyHandlerCall5 call = reinterpret_cast<CuteQOAuthUriSchemeReplyHandlerCall5>(taken[5]);
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
      CuteQOAuthUriSchemeReplyHandlerCall6 call = reinterpret_cast<CuteQOAuthUriSchemeReplyHandlerCall6>(taken[6]);
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
      CuteQOAuthUriSchemeReplyHandlerCall7 call = reinterpret_cast<CuteQOAuthUriSchemeReplyHandlerCall7>(taken[7]);
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
      CuteQOAuthUriSchemeReplyHandlerCall8 call = reinterpret_cast<CuteQOAuthUriSchemeReplyHandlerCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QOAuthUriSchemeReplyHandler::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK27QOAuthUriSchemeReplyHandler10metaObjectEv(
    const QOAuthUriSchemeReplyHandler *self) {
  return self->metaObject();
}

//  QString QOAuthUriSchemeReplyHandler::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN27QOAuthUriSchemeReplyHandler2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QOAuthUriSchemeReplyHandler::tr(s, c, n));
}

//  QOAuthUriSchemeReplyHandler::QOAuthUriSchemeReplyHandler()
extern "C" Q_DECL_EXPORT
QOAuthUriSchemeReplyHandler *ritual_ZN27QOAuthUriSchemeReplyHandlerC1Ev() {
  return new CuteQOAuthUriSchemeReplyHandler();
}

//  QOAuthUriSchemeReplyHandler::QOAuthUriSchemeReplyHandler(QObject *parent)
extern "C" Q_DECL_EXPORT
QOAuthUriSchemeReplyHandler *ritual_ZN27QOAuthUriSchemeReplyHandlerC1EP7QObject(
    QObject *parent) {
  return new CuteQOAuthUriSchemeReplyHandler(parent);
}

//  QOAuthUriSchemeReplyHandler::QOAuthUriSchemeReplyHandler(const QUrl
//      &redirectUrl, QObject *parent)
extern "C" Q_DECL_EXPORT
QOAuthUriSchemeReplyHandler *ritual_ZN27QOAuthUriSchemeReplyHandlerC1ERK4QUrlP7QObject(
    const QUrl *redirectUrl,
    QObject *parent) {
  return new CuteQOAuthUriSchemeReplyHandler(*redirectUrl, parent);
}

//  QOAuthUriSchemeReplyHandler::~QOAuthUriSchemeReplyHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QOAuthUriSchemeReplyHandlerD1Ev(
    QOAuthUriSchemeReplyHandler *self) {
  delete self;
}

//  QString QOAuthUriSchemeReplyHandler::callback() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK27QOAuthUriSchemeReplyHandler8callbackEv(
    const QOAuthUriSchemeReplyHandler *self) {
  return new QString(self->callback());
}

//  void QOAuthUriSchemeReplyHandler::setRedirectUrl(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QOAuthUriSchemeReplyHandler14setRedirectUrlERK4QUrl(
    QOAuthUriSchemeReplyHandler *self,
    const QUrl *url) {
  self->setRedirectUrl(*url);
}

//  QUrl QOAuthUriSchemeReplyHandler::redirectUrl() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK27QOAuthUriSchemeReplyHandler11redirectUrlEv(
    const QOAuthUriSchemeReplyHandler *self) {
  return new QUrl(self->redirectUrl());
}

//  bool QOAuthUriSchemeReplyHandler::handleAuthorizationRedirect(const QUrl
//      &url)
extern "C" Q_DECL_EXPORT
bool ritual_ZN27QOAuthUriSchemeReplyHandler27handleAuthorizationRedirectERK4QUrl(
    QOAuthUriSchemeReplyHandler *self,
    const QUrl *url) {
  return self->handleAuthorizationRedirect(*url);
}

//  bool QOAuthUriSchemeReplyHandler::listen()
extern "C" Q_DECL_EXPORT
bool ritual_ZN27QOAuthUriSchemeReplyHandler6listenEv(
    QOAuthUriSchemeReplyHandler *self) {
  return self->listen();
}

//  void QOAuthUriSchemeReplyHandler::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QOAuthUriSchemeReplyHandler5closeEv(
    QOAuthUriSchemeReplyHandler *self) {
  self->close();
}

//  bool QOAuthUriSchemeReplyHandler::isListening() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QOAuthUriSchemeReplyHandler11isListeningEv(
    const QOAuthUriSchemeReplyHandler *self) {
  return self->isListening();
}

//  QOAuthUriSchemeReplyHandlerPrivate *QOAuthUriSchemeReplyHandler::d_func()
extern "C" Q_DECL_EXPORT
QOAuthUriSchemeReplyHandlerPrivate *ritual_ZN27QOAuthUriSchemeReplyHandler6d_funcEv(
    QOAuthUriSchemeReplyHandler *self) {
  return self->d_func();
}

//  const QOAuthUriSchemeReplyHandlerPrivate
//      *QOAuthUriSchemeReplyHandler::d_func() const
extern "C" Q_DECL_EXPORT
const QOAuthUriSchemeReplyHandlerPrivate *ritual_ZNK27QOAuthUriSchemeReplyHandler6d_funcEv(
    const QOAuthUriSchemeReplyHandler *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQOAuthUriSchemeReplyHandler, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QOAuthUriSchemeReplyHandler(
    QOAuthUriSchemeReplyHandler *self,
    const char *key,
    void *call) {
  return static_cast<CuteQOAuthUriSchemeReplyHandler *>(self)->take(key, call);
}

//  QString QOAuthUriSchemeReplyHandler::callback() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK27QOAuthUriSchemeReplyHandler8callbackEv(
    const QOAuthUriSchemeReplyHandler *self) {
  return new QString(self->QOAuthUriSchemeReplyHandler::callback());
}
