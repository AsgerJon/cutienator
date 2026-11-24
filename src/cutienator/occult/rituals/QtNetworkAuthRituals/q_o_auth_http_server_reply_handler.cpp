//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetworkAuth/qoauthhttpserverreplyhandler.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtNetworkAuth/qoauthglobal.h>
#if !defined(QT_NO_HTTP)
#include <QtNetworkAuth/qoauthhttpserverreplyhandler.h>
#include <QtCore/qstring.h>
#include <QtNetwork/qhostaddress.h>
#include <QtNetwork/qsslconfiguration.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QOAuthHttpServerReplyHandler that Python can take functions over in. Every QOAuthHttpServerReplyHandler
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_HTTP)
typedef QString * (*CuteQOAuthHttpServerReplyHandlerCall0)(const void *, int *);
#endif  // !defined(QT_NO_HTTP)
#if !defined(QT_NO_HTTP)
typedef void (*CuteQOAuthHttpServerReplyHandlerCall1)(const void *, QNetworkReply *, int *);
#endif  // !defined(QT_NO_HTTP)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQOAuthHttpServerReplyHandlerCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQOAuthHttpServerReplyHandlerCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOAuthHttpServerReplyHandlerCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOAuthHttpServerReplyHandlerCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOAuthHttpServerReplyHandlerCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOAuthHttpServerReplyHandlerCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOAuthHttpServerReplyHandlerCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQOAuthHttpServerReplyHandler : public QOAuthHttpServerReplyHandler {
public:
  using QOAuthHttpServerReplyHandler::QOAuthHttpServerReplyHandler;
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
  //  QString QOAuthHttpServerReplyHandler::callback() const
  QString callback() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQOAuthHttpServerReplyHandlerCall0 call = reinterpret_cast<CuteQOAuthHttpServerReplyHandlerCall0>(taken[0]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QOAuthHttpServerReplyHandler::callback();
  }
#endif  // !defined(QT_NO_HTTP)

#if !defined(QT_NO_HTTP)
  //  void QOAuthOobReplyHandler::networkReplyFinished(QNetworkReply
  //      *reply)
  void networkReplyFinished(QNetworkReply *reply) override {
    if (taken[1]) {
      int handled = 0;
      CuteQOAuthHttpServerReplyHandlerCall1 call = reinterpret_cast<CuteQOAuthHttpServerReplyHandlerCall1>(taken[1]);
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
      CuteQOAuthHttpServerReplyHandlerCall2 call = reinterpret_cast<CuteQOAuthHttpServerReplyHandlerCall2>(taken[2]);
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
      CuteQOAuthHttpServerReplyHandlerCall3 call = reinterpret_cast<CuteQOAuthHttpServerReplyHandlerCall3>(taken[3]);
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
      CuteQOAuthHttpServerReplyHandlerCall4 call = reinterpret_cast<CuteQOAuthHttpServerReplyHandlerCall4>(taken[4]);
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
      CuteQOAuthHttpServerReplyHandlerCall5 call = reinterpret_cast<CuteQOAuthHttpServerReplyHandlerCall5>(taken[5]);
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
      CuteQOAuthHttpServerReplyHandlerCall6 call = reinterpret_cast<CuteQOAuthHttpServerReplyHandlerCall6>(taken[6]);
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
      CuteQOAuthHttpServerReplyHandlerCall7 call = reinterpret_cast<CuteQOAuthHttpServerReplyHandlerCall7>(taken[7]);
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
      CuteQOAuthHttpServerReplyHandlerCall8 call = reinterpret_cast<CuteQOAuthHttpServerReplyHandlerCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QOAuthHttpServerReplyHandler::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK28QOAuthHttpServerReplyHandler10metaObjectEv(
    const QOAuthHttpServerReplyHandler *self) {
  return self->metaObject();
}

//  QString QOAuthHttpServerReplyHandler::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN28QOAuthHttpServerReplyHandler2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QOAuthHttpServerReplyHandler::tr(s, c, n));
}

//  QOAuthHttpServerReplyHandler::QOAuthHttpServerReplyHandler(QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QOAuthHttpServerReplyHandler *ritual_ZN28QOAuthHttpServerReplyHandlerC1EP7QObject(
    QObject *parent) {
  return new CuteQOAuthHttpServerReplyHandler(parent);
}

//  QOAuthHttpServerReplyHandler::QOAuthHttpServerReplyHandler(quint16 port,
//      QObject *parent)
extern "C" Q_DECL_EXPORT
QOAuthHttpServerReplyHandler *ritual_ZN28QOAuthHttpServerReplyHandlerC1EtP7QObject(
    quint16 port,
    QObject *parent) {
  return new CuteQOAuthHttpServerReplyHandler(port, parent);
}

//  QOAuthHttpServerReplyHandler::QOAuthHttpServerReplyHandler(const
//      QHostAddress &address, quint16 port, QObject *parent)
extern "C" Q_DECL_EXPORT
QOAuthHttpServerReplyHandler *ritual_ZN28QOAuthHttpServerReplyHandlerC1ERK12QHostAddresstP7QObject(
    const QHostAddress *address,
    quint16 port,
    QObject *parent) {
  return new CuteQOAuthHttpServerReplyHandler(*address, port, parent);
}

//  QOAuthHttpServerReplyHandler::~QOAuthHttpServerReplyHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QOAuthHttpServerReplyHandlerD1Ev(
    QOAuthHttpServerReplyHandler *self) {
  delete self;
}

//  QString QOAuthHttpServerReplyHandler::callback() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK28QOAuthHttpServerReplyHandler8callbackEv(
    const QOAuthHttpServerReplyHandler *self) {
  return new QString(self->callback());
}

//  QString QOAuthHttpServerReplyHandler::callbackPath() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK28QOAuthHttpServerReplyHandler12callbackPathEv(
    const QOAuthHttpServerReplyHandler *self) {
  return new QString(self->callbackPath());
}

//  void QOAuthHttpServerReplyHandler::setCallbackPath(const QString &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QOAuthHttpServerReplyHandler15setCallbackPathERK7QString(
    QOAuthHttpServerReplyHandler *self,
    const QString *path) {
  self->setCallbackPath(*path);
}

//  QString QOAuthHttpServerReplyHandler::callbackHost() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK28QOAuthHttpServerReplyHandler12callbackHostEv(
    const QOAuthHttpServerReplyHandler *self) {
  return new QString(self->callbackHost());
}

//  void QOAuthHttpServerReplyHandler::setCallbackHost(const QString &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QOAuthHttpServerReplyHandler15setCallbackHostERK7QString(
    QOAuthHttpServerReplyHandler *self,
    const QString *path) {
  self->setCallbackHost(*path);
}

//  QString QOAuthHttpServerReplyHandler::callbackText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK28QOAuthHttpServerReplyHandler12callbackTextEv(
    const QOAuthHttpServerReplyHandler *self) {
  return new QString(self->callbackText());
}

//  void QOAuthHttpServerReplyHandler::setCallbackText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QOAuthHttpServerReplyHandler15setCallbackTextERK7QString(
    QOAuthHttpServerReplyHandler *self,
    const QString *text) {
  self->setCallbackText(*text);
}

//  quint16 QOAuthHttpServerReplyHandler::port() const
extern "C" Q_DECL_EXPORT
quint16 ritual_ZNK28QOAuthHttpServerReplyHandler4portEv(
    const QOAuthHttpServerReplyHandler *self) {
  return self->port();
}

//  bool QOAuthHttpServerReplyHandler::listen(const QHostAddress &address,
//      quint16 port)
extern "C" Q_DECL_EXPORT
bool ritual_ZN28QOAuthHttpServerReplyHandler6listenERK12QHostAddresst(
    QOAuthHttpServerReplyHandler *self,
    const QHostAddress *address,
    quint16 port) {
  return self->listen(*address, port);
}

#if !defined(QT_NO_SSL)
//  bool QOAuthHttpServerReplyHandler::listen(const QSslConfiguration
//      &configuration, const QHostAddress &address, quint16 port)
extern "C" Q_DECL_EXPORT
bool ritual_ZN28QOAuthHttpServerReplyHandler6listenERK17QSslConfigurationRK12QHostAddresst(
    QOAuthHttpServerReplyHandler *self,
    const QSslConfiguration *configuration,
    const QHostAddress *address,
    quint16 port) {
  return self->listen(*configuration, *address, port);
}
#endif  // !defined(QT_NO_SSL)

//  void QOAuthHttpServerReplyHandler::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QOAuthHttpServerReplyHandler5closeEv(
    QOAuthHttpServerReplyHandler *self) {
  self->close();
}

//  bool QOAuthHttpServerReplyHandler::isListening() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QOAuthHttpServerReplyHandler11isListeningEv(
    const QOAuthHttpServerReplyHandler *self) {
  return self->isListening();
}

//  QOAuthHttpServerReplyHandlerPrivate
//      *QOAuthHttpServerReplyHandler::d_func()
extern "C" Q_DECL_EXPORT
QOAuthHttpServerReplyHandlerPrivate *ritual_ZN28QOAuthHttpServerReplyHandler6d_funcEv(
    QOAuthHttpServerReplyHandler *self) {
  return self->d_func();
}

//  const QOAuthHttpServerReplyHandlerPrivate
//      *QOAuthHttpServerReplyHandler::d_func() const
extern "C" Q_DECL_EXPORT
const QOAuthHttpServerReplyHandlerPrivate *ritual_ZNK28QOAuthHttpServerReplyHandler6d_funcEv(
    const QOAuthHttpServerReplyHandler *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQOAuthHttpServerReplyHandler, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QOAuthHttpServerReplyHandler(
    QOAuthHttpServerReplyHandler *self,
    const char *key,
    void *call) {
  return static_cast<CuteQOAuthHttpServerReplyHandler *>(self)->take(key, call);
}

//  QString QOAuthHttpServerReplyHandler::callback() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK28QOAuthHttpServerReplyHandler8callbackEv(
    const QOAuthHttpServerReplyHandler *self) {
  return new QString(self->QOAuthHttpServerReplyHandler::callback());
}

#endif  // !defined(QT_NO_HTTP)
