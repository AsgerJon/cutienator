//  Written by dev_tooling.RitualGenerator from the records of QtWebEngineQui
//  ck/6.12.0/QtWebEngineQuick/private/qquickwebengineprofileprototype_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qtwebenginequickglobal_p.h>
#include <QtWebEngineQuick/QtWebEngineQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qquickwebengineprofileprototype_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QQuickWebEngineProfilePrototype may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickWebEngineProfilePrototype : QQuickWebEngineProfilePrototype {
  using QQuickWebEngineProfilePrototype::componentComplete;
  using QQuickWebEngineProfilePrototype::classBegin;
};

//  A QQuickWebEngineProfilePrototype that Python can take functions over in. Every QQuickWebEngineProfilePrototype
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickWebEngineProfilePrototypeCall0)(const void *, int *);
typedef void (*CuteQQuickWebEngineProfilePrototypeCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickWebEngineProfilePrototypeCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickWebEngineProfilePrototypeCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebEngineProfilePrototypeCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebEngineProfilePrototypeCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebEngineProfilePrototypeCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebEngineProfilePrototypeCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebEngineProfilePrototypeCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickWebEngineProfilePrototype : public QQuickWebEngineProfilePrototype {
public:
  using QQuickWebEngineProfilePrototype::QQuickWebEngineProfilePrototype;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[1] = call;
      return true;
    }
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

  //  void QQuickWebEngineProfilePrototype::componentComplete()
  void componentComplete() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickWebEngineProfilePrototypeCall0 call = reinterpret_cast<CuteQQuickWebEngineProfilePrototypeCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickWebEngineProfilePrototype::componentComplete();
  }

  //  void QQuickWebEngineProfilePrototype::classBegin()
  void classBegin() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickWebEngineProfilePrototypeCall1 call = reinterpret_cast<CuteQQuickWebEngineProfilePrototypeCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickWebEngineProfilePrototype::classBegin();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickWebEngineProfilePrototypeCall2 call = reinterpret_cast<CuteQQuickWebEngineProfilePrototypeCall2>(taken[2]);
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
      CuteQQuickWebEngineProfilePrototypeCall3 call = reinterpret_cast<CuteQQuickWebEngineProfilePrototypeCall3>(taken[3]);
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
      CuteQQuickWebEngineProfilePrototypeCall4 call = reinterpret_cast<CuteQQuickWebEngineProfilePrototypeCall4>(taken[4]);
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
      CuteQQuickWebEngineProfilePrototypeCall5 call = reinterpret_cast<CuteQQuickWebEngineProfilePrototypeCall5>(taken[5]);
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
      CuteQQuickWebEngineProfilePrototypeCall6 call = reinterpret_cast<CuteQQuickWebEngineProfilePrototypeCall6>(taken[6]);
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
      CuteQQuickWebEngineProfilePrototypeCall7 call = reinterpret_cast<CuteQQuickWebEngineProfilePrototypeCall7>(taken[7]);
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
      CuteQQuickWebEngineProfilePrototypeCall8 call = reinterpret_cast<CuteQQuickWebEngineProfilePrototypeCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickWebEngineProfilePrototype::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK31QQuickWebEngineProfilePrototype10metaObjectEv(
    const QQuickWebEngineProfilePrototype *self) {
  return self->metaObject();
}

//  void *QQuickWebEngineProfilePrototype::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN31QQuickWebEngineProfilePrototype11qt_metacastEPKc(
    QQuickWebEngineProfilePrototype *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickWebEngineProfilePrototype::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN31QQuickWebEngineProfilePrototype11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickWebEngineProfilePrototype *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickWebEngineProfilePrototype::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN31QQuickWebEngineProfilePrototype2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickWebEngineProfilePrototype::tr(s, c, n));
}

//  QQuickWebEngineProfilePrototype::QQuickWebEngineProfilePrototype(QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QQuickWebEngineProfilePrototype *ritual_ZN31QQuickWebEngineProfilePrototypeC1EP7QObject(
    QObject *parent) {
  return new CuteQQuickWebEngineProfilePrototype(parent);
}

//  QQuickWebEngineProfilePrototype::~QQuickWebEngineProfilePrototype()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickWebEngineProfilePrototypeD1Ev(
    QQuickWebEngineProfilePrototype *self) {
  delete self;
}

//  QString QQuickWebEngineProfilePrototype::storageName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK31QQuickWebEngineProfilePrototype11storageNameEv(
    const QQuickWebEngineProfilePrototype *self) {
  return new QString(self->storageName());
}

//  void QQuickWebEngineProfilePrototype::setStorageName(const QString
//      &storageName)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickWebEngineProfilePrototype14setStorageNameERK7QString(
    QQuickWebEngineProfilePrototype *self,
    const QString *storageName) {
  self->setStorageName(*storageName);
}

//  QString QQuickWebEngineProfilePrototype::persistentStoragePath() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK31QQuickWebEngineProfilePrototype21persistentStoragePathEv(
    const QQuickWebEngineProfilePrototype *self) {
  return new QString(self->persistentStoragePath());
}

//  void QQuickWebEngineProfilePrototype::setPersistentStoragePath(const
//      QString &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickWebEngineProfilePrototype24setPersistentStoragePathERK7QString(
    QQuickWebEngineProfilePrototype *self,
    const QString *path) {
  self->setPersistentStoragePath(*path);
}

//  QString QQuickWebEngineProfilePrototype::cachePath() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK31QQuickWebEngineProfilePrototype9cachePathEv(
    const QQuickWebEngineProfilePrototype *self) {
  return new QString(self->cachePath());
}

//  void QQuickWebEngineProfilePrototype::setCachePath(const QString &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickWebEngineProfilePrototype12setCachePathERK7QString(
    QQuickWebEngineProfilePrototype *self,
    const QString *path) {
  self->setCachePath(*path);
}

//  QQuickWebEngineProfile::HttpCacheType
//      QQuickWebEngineProfilePrototype::httpCacheType() const
extern "C" Q_DECL_EXPORT
QQuickWebEngineProfile::HttpCacheType ritual_ZNK31QQuickWebEngineProfilePrototype13httpCacheTypeEv(
    const QQuickWebEngineProfilePrototype *self) {
  return self->httpCacheType();
}

//  void QQuickWebEngineProfilePrototype::setHttpCacheType(QQuickWebEnginePro
//      file::HttpCacheType httpCacheType)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickWebEngineProfilePrototype16setHttpCacheTypeEN22QQuickWebEngineProfile13HttpCacheTypeE(
    QQuickWebEngineProfilePrototype *self,
    QQuickWebEngineProfile::HttpCacheType httpCacheType) {
  self->setHttpCacheType(httpCacheType);
}

//  QQuickWebEngineProfile::PersistentCookiesPolicy
//      QQuickWebEngineProfilePrototype::persistentCookiesPolicy() const
extern "C" Q_DECL_EXPORT
QQuickWebEngineProfile::PersistentCookiesPolicy ritual_ZNK31QQuickWebEngineProfilePrototype23persistentCookiesPolicyEv(
    const QQuickWebEngineProfilePrototype *self) {
  return self->persistentCookiesPolicy();
}

//  void QQuickWebEngineProfilePrototype::setPersistentCookiesPolicy(QQuickWe
//      bEngineProfile::PersistentCookiesPolicy persistentCookiesPolicy)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickWebEngineProfilePrototype26setPersistentCookiesPolicyEN22QQuickWebEngineProfile23PersistentCookiesPolicyE(
    QQuickWebEngineProfilePrototype *self,
    QQuickWebEngineProfile::PersistentCookiesPolicy persistentCookiesPolicy) {
  self->setPersistentCookiesPolicy(persistentCookiesPolicy);
}

//  void QQuickWebEngineProfilePrototype::setHttpCacheMaximumSize(int
//      maxSizeInBytes)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickWebEngineProfilePrototype23setHttpCacheMaximumSizeEi(
    QQuickWebEngineProfilePrototype *self,
    int maxSizeInBytes) {
  self->setHttpCacheMaximumSize(maxSizeInBytes);
}

//  int QQuickWebEngineProfilePrototype::httpCacheMaximumSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK31QQuickWebEngineProfilePrototype20httpCacheMaximumSizeEv(
    const QQuickWebEngineProfilePrototype *self) {
  return self->httpCacheMaximumSize();
}

//  QQuickWebEngineProfile::PersistentPermissionsPolicy
//      QQuickWebEngineProfilePrototype::persistentPermissionsPolicy() const
extern "C" Q_DECL_EXPORT
QQuickWebEngineProfile::PersistentPermissionsPolicy ritual_ZNK31QQuickWebEngineProfilePrototype27persistentPermissionsPolicyEv(
    const QQuickWebEngineProfilePrototype *self) {
  return self->persistentPermissionsPolicy();
}

//  void QQuickWebEngineProfilePrototype::setPersistentPermissionsPolicy(QQui
//      ckWebEngineProfile::PersistentPermissionsPolicy
//      persistentPermissionsPolicy)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickWebEngineProfilePrototype30setPersistentPermissionsPolicyEN22QQuickWebEngineProfile27PersistentPermissionsPolicyE(
    QQuickWebEngineProfilePrototype *self,
    QQuickWebEngineProfile::PersistentPermissionsPolicy persistentPermissionsPolicy) {
  self->setPersistentPermissionsPolicy(persistentPermissionsPolicy);
}

//  QStringList
//      QQuickWebEngineProfilePrototype::additionalTrustedCertificateFiles()
//      const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK31QQuickWebEngineProfilePrototype33additionalTrustedCertificateFilesEv(
    const QQuickWebEngineProfilePrototype *self) {
  return new QList<QString>(self->additionalTrustedCertificateFiles());
}

//  void QQuickWebEngineProfilePrototype::setAdditionalTrustedCertificateFile
//      s(const QStringList &paths)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickWebEngineProfilePrototype36setAdditionalTrustedCertificateFilesERK5QListI7QStringE(
    QQuickWebEngineProfilePrototype *self,
    const QList<QString> *paths) {
  self->setAdditionalTrustedCertificateFiles(*paths);
}

//  QQuickWebEngineProfile *QQuickWebEngineProfilePrototype::instance()
extern "C" Q_DECL_EXPORT
QQuickWebEngineProfile *ritual_ZN31QQuickWebEngineProfilePrototype8instanceEv(
    QQuickWebEngineProfilePrototype *self) {
  return self->instance();
}

//  void QQuickWebEngineProfilePrototype::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickWebEngineProfilePrototype17componentCompleteEv(
    QQuickWebEngineProfilePrototype *self) {
  self->componentComplete();
}

//  void QQuickWebEngineProfilePrototype::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickWebEngineProfilePrototype10classBeginEv(
    QQuickWebEngineProfilePrototype *self) {
  self->classBegin();
}

//  QQuickWebEngineProfilePrototype as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QQuickWebEngineProfilePrototype_QQmlParserStatus(
    QQuickWebEngineProfilePrototype *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  a Python function taken by a CuteQQuickWebEngineProfilePrototype, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickWebEngineProfilePrototype(
    QQuickWebEngineProfilePrototype *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickWebEngineProfilePrototype *>(self)->take(key, call);
}

//  void QQuickWebEngineProfilePrototype::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN31QQuickWebEngineProfilePrototype17componentCompleteEv(
    QQuickWebEngineProfilePrototype *self) {
  static_cast<OwnQQuickWebEngineProfilePrototype *>(self)->OwnQQuickWebEngineProfilePrototype::componentComplete();
}

//  void QQuickWebEngineProfilePrototype::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN31QQuickWebEngineProfilePrototype10classBeginEv(
    QQuickWebEngineProfilePrototype *self) {
  static_cast<OwnQQuickWebEngineProfilePrototype *>(self)->OwnQQuickWebEngineProfilePrototype::classBegin();
}
