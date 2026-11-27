//  Written by dev_tooling.RitualGenerator from the records of QtWebEngineQui
//  ck/6.12.0/QtWebEngineQuick/private/qquickwebenginedialogrequests_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qtwebenginequickglobal_p.h>
#include <QtWebEngineQuick/QtWebEngineQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qquickwebenginedialogrequests_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtCore/QSharedPointer>
#include <QtWebEngineCore/QtWebEngineCore>

//  A QQuickWebEngineAuthenticationDialogRequest that Python can take functions over in. Every QQuickWebEngineAuthenticationDialogRequest
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickWebEngineAuthenticationDialogRequestCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickWebEngineAuthenticationDialogRequestCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebEngineAuthenticationDialogRequestCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebEngineAuthenticationDialogRequestCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebEngineAuthenticationDialogRequestCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebEngineAuthenticationDialogRequestCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebEngineAuthenticationDialogRequestCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickWebEngineAuthenticationDialogRequest : public QQuickWebEngineAuthenticationDialogRequest {
public:
  using QQuickWebEngineAuthenticationDialogRequest::QQuickWebEngineAuthenticationDialogRequest;
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
      CuteQQuickWebEngineAuthenticationDialogRequestCall0 call = reinterpret_cast<CuteQQuickWebEngineAuthenticationDialogRequestCall0>(taken[0]);
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
      CuteQQuickWebEngineAuthenticationDialogRequestCall1 call = reinterpret_cast<CuteQQuickWebEngineAuthenticationDialogRequestCall1>(taken[1]);
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
      CuteQQuickWebEngineAuthenticationDialogRequestCall2 call = reinterpret_cast<CuteQQuickWebEngineAuthenticationDialogRequestCall2>(taken[2]);
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
      CuteQQuickWebEngineAuthenticationDialogRequestCall3 call = reinterpret_cast<CuteQQuickWebEngineAuthenticationDialogRequestCall3>(taken[3]);
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
      CuteQQuickWebEngineAuthenticationDialogRequestCall4 call = reinterpret_cast<CuteQQuickWebEngineAuthenticationDialogRequestCall4>(taken[4]);
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
      CuteQQuickWebEngineAuthenticationDialogRequestCall5 call = reinterpret_cast<CuteQQuickWebEngineAuthenticationDialogRequestCall5>(taken[5]);
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
      CuteQQuickWebEngineAuthenticationDialogRequestCall6 call = reinterpret_cast<CuteQQuickWebEngineAuthenticationDialogRequestCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject
//      *QQuickWebEngineAuthenticationDialogRequest::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK42QQuickWebEngineAuthenticationDialogRequest10metaObjectEv(
    const QQuickWebEngineAuthenticationDialogRequest *self) {
  return self->metaObject();
}

//  void *QQuickWebEngineAuthenticationDialogRequest::qt_metacast(const char
//      *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN42QQuickWebEngineAuthenticationDialogRequest11qt_metacastEPKc(
    QQuickWebEngineAuthenticationDialogRequest *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int
//      QQuickWebEngineAuthenticationDialogRequest::qt_metacall(QMetaObject::
//      Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN42QQuickWebEngineAuthenticationDialogRequest11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickWebEngineAuthenticationDialogRequest *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickWebEngineAuthenticationDialogRequest::tr(const char *s,
//      const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN42QQuickWebEngineAuthenticationDialogRequest2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(
      QQuickWebEngineAuthenticationDialogRequest::tr(
          s,
          c,
          n));
}

//  void
//      QQuickWebEngineAuthenticationDialogRequest::qt_qmlMarker_uncreatable(
//      )
extern "C" Q_DECL_EXPORT
void ritual_ZN42QQuickWebEngineAuthenticationDialogRequest24qt_qmlMarker_uncreatableEv(
    QQuickWebEngineAuthenticationDialogRequest *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QQuickWebEngineAuthenticationDialogRequest::~QQuickWebEngineAuthenticatio
//      nDialogRequest()
extern "C" Q_DECL_EXPORT
void ritual_ZN42QQuickWebEngineAuthenticationDialogRequestD1Ev(
    QQuickWebEngineAuthenticationDialogRequest *self) {
  delete self;
}

//  QUrl QQuickWebEngineAuthenticationDialogRequest::url() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK42QQuickWebEngineAuthenticationDialogRequest3urlEv(
    const QQuickWebEngineAuthenticationDialogRequest *self) {
  return new QUrl(self->url());
}

//  QString QQuickWebEngineAuthenticationDialogRequest::realm() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK42QQuickWebEngineAuthenticationDialogRequest5realmEv(
    const QQuickWebEngineAuthenticationDialogRequest *self) {
  return new QString(self->realm());
}

//  QString QQuickWebEngineAuthenticationDialogRequest::proxyHost() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK42QQuickWebEngineAuthenticationDialogRequest9proxyHostEv(
    const QQuickWebEngineAuthenticationDialogRequest *self) {
  return new QString(self->proxyHost());
}

//  AuthenticationType QQuickWebEngineAuthenticationDialogRequest::type()
//      const
extern "C" Q_DECL_EXPORT
QQuickWebEngineAuthenticationDialogRequest::AuthenticationType ritual_ZNK42QQuickWebEngineAuthenticationDialogRequest4typeEv(
    const QQuickWebEngineAuthenticationDialogRequest *self) {
  return self->type();
}

//  bool QQuickWebEngineAuthenticationDialogRequest::isAccepted() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK42QQuickWebEngineAuthenticationDialogRequest10isAcceptedEv(
    const QQuickWebEngineAuthenticationDialogRequest *self) {
  return self->isAccepted();
}

//  void QQuickWebEngineAuthenticationDialogRequest::setAccepted(bool
//      accepted)
extern "C" Q_DECL_EXPORT
void ritual_ZN42QQuickWebEngineAuthenticationDialogRequest11setAcceptedEb(
    QQuickWebEngineAuthenticationDialogRequest *self,
    bool accepted) {
  self->setAccepted(accepted);
}

//  void QQuickWebEngineAuthenticationDialogRequest::dialogAccept(const
//      QString &user, const QString &password)
extern "C" Q_DECL_EXPORT
void ritual_ZN42QQuickWebEngineAuthenticationDialogRequest12dialogAcceptERK7QStringS2_(
    QQuickWebEngineAuthenticationDialogRequest *self,
    const QString *user,
    const QString *password) {
  self->dialogAccept(*user, *password);
}

//  void QQuickWebEngineAuthenticationDialogRequest::dialogReject()
extern "C" Q_DECL_EXPORT
void ritual_ZN42QQuickWebEngineAuthenticationDialogRequest12dialogRejectEv(
    QQuickWebEngineAuthenticationDialogRequest *self) {
  self->dialogReject();
}

//  QQuickWebEngineAuthenticationDialogRequest::QQuickWebEngineAuthentication
//      DialogRequest(QSharedPointer<QtWebEngineCore::AuthenticationDialogCon
//      troller> controller, QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickWebEngineAuthenticationDialogRequest *ritual_ZN42QQuickWebEngineAuthenticationDialogRequestC1E14QSharedPointerIN15QtWebEngineCore30AuthenticationDialogControllerEEP7QObject(
    const QSharedPointer<QtWebEngineCore::AuthenticationDialogController> *controller,
    QObject *parent) {
  return new CuteQQuickWebEngineAuthenticationDialogRequest(
      *controller,
      parent);
}

//  a Python function taken by a
//      CuteQQuickWebEngineAuthenticationDialogRequest, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickWebEngineAuthenticationDialogRequest(
    QQuickWebEngineAuthenticationDialogRequest *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickWebEngineAuthenticationDialogRequest *>(self)->take(key, call);
}
