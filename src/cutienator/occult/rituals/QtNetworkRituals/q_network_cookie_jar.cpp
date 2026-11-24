//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/qnetworkcookiejar.h, Qt 6.12.0. Changes made here are lost.
#include <QtNetwork/qnetworkcookiejar.h>
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtNetwork/qnetworkcookie.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QNetworkCookieJar may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQNetworkCookieJar : QNetworkCookieJar {
  using QNetworkCookieJar::validateCookie;
};

//  A QNetworkCookieJar that Python can take functions over in. Every QNetworkCookieJar
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQNetworkCookieJarCall0)(const void *, const QNetworkCookie *, int *);
typedef bool (*CuteQNetworkCookieJarCall1)(const void *, const QNetworkCookie *, int *);
typedef bool (*CuteQNetworkCookieJarCall2)(const void *, const QNetworkCookie *, int *);
typedef bool (*CuteQNetworkCookieJarCall3)(const void *, const QNetworkCookie *, const QUrl *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQNetworkCookieJarCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQNetworkCookieJarCall5)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkCookieJarCall6)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkCookieJarCall7)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkCookieJarCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkCookieJarCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkCookieJarCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQNetworkCookieJar : public QNetworkCookieJar {
public:
  using QNetworkCookieJar::QNetworkCookieJar;
  void *taken[11] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN17QNetworkCookieJar12insertCookieERK14QNetworkCookie")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QNetworkCookieJar12updateCookieERK14QNetworkCookie")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QNetworkCookieJar12deleteCookieERK14QNetworkCookie")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QNetworkCookieJar14validateCookieERK14QNetworkCookieRK4QUrl")) {
      taken[3] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  bool QNetworkCookieJar::insertCookie(const QNetworkCookie &cookie)
  bool insertCookie(const QNetworkCookie &cookie) override {
    if (taken[0]) {
      int handled = 0;
      CuteQNetworkCookieJarCall0 call = reinterpret_cast<CuteQNetworkCookieJarCall0>(taken[0]);
      bool given = call(this, &cookie, &handled);
      if (handled) return given;
    }
    return QNetworkCookieJar::insertCookie(cookie);
  }

  //  bool QNetworkCookieJar::updateCookie(const QNetworkCookie &cookie)
  bool updateCookie(const QNetworkCookie &cookie) override {
    if (taken[1]) {
      int handled = 0;
      CuteQNetworkCookieJarCall1 call = reinterpret_cast<CuteQNetworkCookieJarCall1>(taken[1]);
      bool given = call(this, &cookie, &handled);
      if (handled) return given;
    }
    return QNetworkCookieJar::updateCookie(cookie);
  }

  //  bool QNetworkCookieJar::deleteCookie(const QNetworkCookie &cookie)
  bool deleteCookie(const QNetworkCookie &cookie) override {
    if (taken[2]) {
      int handled = 0;
      CuteQNetworkCookieJarCall2 call = reinterpret_cast<CuteQNetworkCookieJarCall2>(taken[2]);
      bool given = call(this, &cookie, &handled);
      if (handled) return given;
    }
    return QNetworkCookieJar::deleteCookie(cookie);
  }

  //  bool QNetworkCookieJar::validateCookie(const QNetworkCookie &cookie,
  //      const QUrl &url) const
  bool validateCookie(
      const QNetworkCookie &cookie,
      const QUrl &url) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQNetworkCookieJarCall3 call = reinterpret_cast<CuteQNetworkCookieJarCall3>(taken[3]);
      bool given = call(this, &cookie, &url, &handled);
      if (handled) return given;
    }
    return QNetworkCookieJar::validateCookie(cookie, url);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQNetworkCookieJarCall4 call = reinterpret_cast<CuteQNetworkCookieJarCall4>(taken[4]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQNetworkCookieJarCall5 call = reinterpret_cast<CuteQNetworkCookieJarCall5>(taken[5]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQNetworkCookieJarCall6 call = reinterpret_cast<CuteQNetworkCookieJarCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQNetworkCookieJarCall7 call = reinterpret_cast<CuteQNetworkCookieJarCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQNetworkCookieJarCall8 call = reinterpret_cast<CuteQNetworkCookieJarCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[9]) {
      int handled = 0;
      CuteQNetworkCookieJarCall9 call = reinterpret_cast<CuteQNetworkCookieJarCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[10]) {
      int handled = 0;
      CuteQNetworkCookieJarCall10 call = reinterpret_cast<CuteQNetworkCookieJarCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QNetworkCookieJar::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QNetworkCookieJar10metaObjectEv(
    const QNetworkCookieJar *self) {
  return self->metaObject();
}

//  QString QNetworkCookieJar::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QNetworkCookieJar2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QNetworkCookieJar::tr(s, c, n));
}

//  QNetworkCookieJar::QNetworkCookieJar(QObject *parent)
extern "C" Q_DECL_EXPORT
QNetworkCookieJar *ritual_ZN17QNetworkCookieJarC1EP7QObject(
    QObject *parent) {
  return new CuteQNetworkCookieJar(parent);
}

//  QNetworkCookieJar::~QNetworkCookieJar()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QNetworkCookieJarD1Ev(QNetworkCookieJar *self) {
  delete self;
}

//  QList<QNetworkCookie> QNetworkCookieJar::cookiesForUrl(const QUrl &url)
//      const
extern "C" Q_DECL_EXPORT
QList<QNetworkCookie> *ritual_ZNK17QNetworkCookieJar13cookiesForUrlERK4QUrl(
    const QNetworkCookieJar *self,
    const QUrl *url) {
  return new QList<QNetworkCookie>(self->cookiesForUrl(*url));
}

//  bool QNetworkCookieJar::setCookiesFromUrl(const QList<QNetworkCookie>
//      &cookieList, const QUrl &url)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QNetworkCookieJar17setCookiesFromUrlERK5QListI14QNetworkCookieERK4QUrl(
    QNetworkCookieJar *self,
    const QList<QNetworkCookie> *cookieList,
    const QUrl *url) {
  return self->setCookiesFromUrl(*cookieList, *url);
}

//  bool QNetworkCookieJar::insertCookie(const QNetworkCookie &cookie)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QNetworkCookieJar12insertCookieERK14QNetworkCookie(
    QNetworkCookieJar *self,
    const QNetworkCookie *cookie) {
  return self->insertCookie(*cookie);
}

//  bool QNetworkCookieJar::updateCookie(const QNetworkCookie &cookie)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QNetworkCookieJar12updateCookieERK14QNetworkCookie(
    QNetworkCookieJar *self,
    const QNetworkCookie *cookie) {
  return self->updateCookie(*cookie);
}

//  bool QNetworkCookieJar::deleteCookie(const QNetworkCookie &cookie)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QNetworkCookieJar12deleteCookieERK14QNetworkCookie(
    QNetworkCookieJar *self,
    const QNetworkCookie *cookie) {
  return self->deleteCookie(*cookie);
}

//  QList<QNetworkCookie> QNetworkCookieJar::allCookies() const
extern "C" Q_DECL_EXPORT
QList<QNetworkCookie> *ritual_ZNK17QNetworkCookieJar10allCookiesEv(
    const QNetworkCookieJar *self) {
  return new QList<QNetworkCookie>(self->allCookies());
}

//  void QNetworkCookieJar::setAllCookies(const QList<QNetworkCookie>
//      &cookieList)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QNetworkCookieJar13setAllCookiesERK5QListI14QNetworkCookieE(
    QNetworkCookieJar *self,
    const QList<QNetworkCookie> *cookieList) {
  self->setAllCookies(*cookieList);
}

//  bool QNetworkCookieJar::validateCookie(const QNetworkCookie &cookie,
//      const QUrl &url) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QNetworkCookieJar14validateCookieERK14QNetworkCookieRK4QUrl(
    const QNetworkCookieJar *self,
    const QNetworkCookie *cookie,
    const QUrl *url) {
  return self->validateCookie(*cookie, *url);
}

//  QNetworkCookieJarPrivate *QNetworkCookieJar::d_func()
extern "C" Q_DECL_EXPORT
QNetworkCookieJarPrivate *ritual_ZN17QNetworkCookieJar6d_funcEv(
    QNetworkCookieJar *self) {
  return self->d_func();
}

//  const QNetworkCookieJarPrivate *QNetworkCookieJar::d_func() const
extern "C" Q_DECL_EXPORT
const QNetworkCookieJarPrivate *ritual_ZNK17QNetworkCookieJar6d_funcEv(
    const QNetworkCookieJar *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQNetworkCookieJar, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QNetworkCookieJar(
    QNetworkCookieJar *self,
    const char *key,
    void *call) {
  return static_cast<CuteQNetworkCookieJar *>(self)->take(key, call);
}

//  bool QNetworkCookieJar::insertCookie(const QNetworkCookie &cookie)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QNetworkCookieJar12insertCookieERK14QNetworkCookie(
    QNetworkCookieJar *self,
    const QNetworkCookie *cookie) {
  return self->QNetworkCookieJar::insertCookie(*cookie);
}

//  bool QNetworkCookieJar::updateCookie(const QNetworkCookie &cookie)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QNetworkCookieJar12updateCookieERK14QNetworkCookie(
    QNetworkCookieJar *self,
    const QNetworkCookie *cookie) {
  return self->QNetworkCookieJar::updateCookie(*cookie);
}

//  bool QNetworkCookieJar::deleteCookie(const QNetworkCookie &cookie)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QNetworkCookieJar12deleteCookieERK14QNetworkCookie(
    QNetworkCookieJar *self,
    const QNetworkCookie *cookie) {
  return self->QNetworkCookieJar::deleteCookie(*cookie);
}

//  bool QNetworkCookieJar::validateCookie(const QNetworkCookie &cookie,
//      const QUrl &url) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK17QNetworkCookieJar14validateCookieERK14QNetworkCookieRK4QUrl(
    const QNetworkCookieJar *self,
    const QNetworkCookie *cookie,
    const QUrl *url) {
  return static_cast<const OwnQNetworkCookieJar *>(self)->OwnQNetworkCookieJar::validateCookie(
      *cookie,
      *url);
}
