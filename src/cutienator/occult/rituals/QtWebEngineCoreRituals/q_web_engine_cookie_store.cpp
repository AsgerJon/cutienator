//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebEngineCore/qwebenginecookiestore.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtWebEngineCore/qwebenginecookiestore.h>
#include <QtCore/qstring.h>
#include <QtNetwork/qnetworkcookie.h>
#include <QtCore/qurl.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QWebEngineCookieStore that Python can take functions over in. Every QWebEngineCookieStore
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWebEngineCookieStoreCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWebEngineCookieStoreCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEngineCookieStoreCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEngineCookieStoreCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEngineCookieStoreCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEngineCookieStoreCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEngineCookieStoreCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQWebEngineCookieStore : public QWebEngineCookieStore {
public:
  using QWebEngineCookieStore::QWebEngineCookieStore;
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
      CuteQWebEngineCookieStoreCall0 call = reinterpret_cast<CuteQWebEngineCookieStoreCall0>(taken[0]);
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
      CuteQWebEngineCookieStoreCall1 call = reinterpret_cast<CuteQWebEngineCookieStoreCall1>(taken[1]);
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
      CuteQWebEngineCookieStoreCall2 call = reinterpret_cast<CuteQWebEngineCookieStoreCall2>(taken[2]);
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
      CuteQWebEngineCookieStoreCall3 call = reinterpret_cast<CuteQWebEngineCookieStoreCall3>(taken[3]);
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
      CuteQWebEngineCookieStoreCall4 call = reinterpret_cast<CuteQWebEngineCookieStoreCall4>(taken[4]);
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
      CuteQWebEngineCookieStoreCall5 call = reinterpret_cast<CuteQWebEngineCookieStoreCall5>(taken[5]);
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
      CuteQWebEngineCookieStoreCall6 call = reinterpret_cast<CuteQWebEngineCookieStoreCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QWebEngineCookieStore::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QWebEngineCookieStore10metaObjectEv(
    const QWebEngineCookieStore *self) {
  return self->metaObject();
}

//  void *QWebEngineCookieStore::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN21QWebEngineCookieStore11qt_metacastEPKc(
    QWebEngineCookieStore *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QWebEngineCookieStore::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QWebEngineCookieStore11qt_metacallEN11QMetaObject4CallEiPPv(
    QWebEngineCookieStore *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QWebEngineCookieStore::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QWebEngineCookieStore2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWebEngineCookieStore::tr(s, c, n));
}

//  QWebEngineCookieStore::~QWebEngineCookieStore()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QWebEngineCookieStoreD1Ev(QWebEngineCookieStore *self) {
  delete self;
}

//  void QWebEngineCookieStore::setCookieFilter(const std::function<bool
//      (const FilterRequest &)> &filterCallback)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QWebEngineCookieStore15setCookieFilterERKSt8functionIFbRKNS_13FilterRequestEEE(
    QWebEngineCookieStore *self,
    const std::function<bool (const QWebEngineCookieStore::FilterRequest &)> *filterCallback) {
  self->setCookieFilter(*filterCallback);
}

//  void QWebEngineCookieStore::setCookieFilter(std::function<bool (const
//      FilterRequest &)> &&filterCallback)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QWebEngineCookieStore15setCookieFilterEOSt8functionIFbRKNS_13FilterRequestEEE(
    QWebEngineCookieStore *self,
    std::function<bool (const QWebEngineCookieStore::FilterRequest &)> *filterCallback) {
  self->setCookieFilter(std::move(*filterCallback));
}

//  void QWebEngineCookieStore::setCookie(const QNetworkCookie &cookie, const
//      QUrl &origin)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QWebEngineCookieStore9setCookieERK14QNetworkCookieRK4QUrl(
    QWebEngineCookieStore *self,
    const QNetworkCookie *cookie,
    const QUrl *origin) {
  self->setCookie(*cookie, *origin);
}

//  void QWebEngineCookieStore::deleteCookie(const QNetworkCookie &cookie,
//      const QUrl &origin)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QWebEngineCookieStore12deleteCookieERK14QNetworkCookieRK4QUrl(
    QWebEngineCookieStore *self,
    const QNetworkCookie *cookie,
    const QUrl *origin) {
  self->deleteCookie(*cookie, *origin);
}

//  void QWebEngineCookieStore::deleteSessionCookies()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QWebEngineCookieStore20deleteSessionCookiesEv(
    QWebEngineCookieStore *self) {
  self->deleteSessionCookies();
}

//  void QWebEngineCookieStore::deleteAllCookies()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QWebEngineCookieStore16deleteAllCookiesEv(
    QWebEngineCookieStore *self) {
  self->deleteAllCookies();
}

//  void QWebEngineCookieStore::loadAllCookies()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QWebEngineCookieStore14loadAllCookiesEv(
    QWebEngineCookieStore *self) {
  self->loadAllCookies();
}

//  void QWebEngineCookieStore::cookieAdded(const QNetworkCookie &cookie)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QWebEngineCookieStore11cookieAddedERK14QNetworkCookie(
    QWebEngineCookieStore *self,
    const QNetworkCookie *cookie) {
  self->cookieAdded(*cookie);
}

//  void QWebEngineCookieStore::cookieRemoved(const QNetworkCookie &cookie)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QWebEngineCookieStore13cookieRemovedERK14QNetworkCookie(
    QWebEngineCookieStore *self,
    const QNetworkCookie *cookie) {
  self->cookieRemoved(*cookie);
}

//  QWebEngineCookieStore::QWebEngineCookieStore(QObject *parent)
extern "C" Q_DECL_EXPORT
QWebEngineCookieStore *ritual_ZN21QWebEngineCookieStoreC1EP7QObject(
    QObject *parent) {
  return new CuteQWebEngineCookieStore(parent);
}

//  QWebEngineCookieStorePrivate *QWebEngineCookieStore::d_func()
extern "C" Q_DECL_EXPORT
QWebEngineCookieStorePrivate *ritual_ZN21QWebEngineCookieStore6d_funcEv(
    QWebEngineCookieStore *self) {
  return self->d_func();
}

//  const QWebEngineCookieStorePrivate *QWebEngineCookieStore::d_func() const
extern "C" Q_DECL_EXPORT
const QWebEngineCookieStorePrivate *ritual_ZNK21QWebEngineCookieStore6d_funcEv(
    const QWebEngineCookieStore *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQWebEngineCookieStore, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWebEngineCookieStore(
    QWebEngineCookieStore *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWebEngineCookieStore *>(self)->take(key, call);
}
