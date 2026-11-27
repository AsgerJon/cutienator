//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebEngineQuick/qquickwebengineprofile.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtWebEngineQuick/QtWebEngineQuick>
#include <QtWebEngineQuick/qquickwebengineprofile.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qurl.h>
#include <QtWebEngineCore/qwebenginepermission.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QQuickWebEngineProfile that Python can take functions over in. Every QQuickWebEngineProfile
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickWebEngineProfileCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickWebEngineProfileCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebEngineProfileCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebEngineProfileCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebEngineProfileCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebEngineProfileCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebEngineProfileCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickWebEngineProfile : public QQuickWebEngineProfile {
public:
  using QQuickWebEngineProfile::QQuickWebEngineProfile;
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
      CuteQQuickWebEngineProfileCall0 call = reinterpret_cast<CuteQQuickWebEngineProfileCall0>(taken[0]);
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
      CuteQQuickWebEngineProfileCall1 call = reinterpret_cast<CuteQQuickWebEngineProfileCall1>(taken[1]);
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
      CuteQQuickWebEngineProfileCall2 call = reinterpret_cast<CuteQQuickWebEngineProfileCall2>(taken[2]);
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
      CuteQQuickWebEngineProfileCall3 call = reinterpret_cast<CuteQQuickWebEngineProfileCall3>(taken[3]);
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
      CuteQQuickWebEngineProfileCall4 call = reinterpret_cast<CuteQQuickWebEngineProfileCall4>(taken[4]);
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
      CuteQQuickWebEngineProfileCall5 call = reinterpret_cast<CuteQQuickWebEngineProfileCall5>(taken[5]);
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
      CuteQQuickWebEngineProfileCall6 call = reinterpret_cast<CuteQQuickWebEngineProfileCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickWebEngineProfile::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QQuickWebEngineProfile10metaObjectEv(
    const QQuickWebEngineProfile *self) {
  return self->metaObject();
}

//  void *QQuickWebEngineProfile::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN22QQuickWebEngineProfile11qt_metacastEPKc(
    QQuickWebEngineProfile *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickWebEngineProfile::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN22QQuickWebEngineProfile11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickWebEngineProfile *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickWebEngineProfile::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN22QQuickWebEngineProfile2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickWebEngineProfile::tr(s, c, n));
}

//  QQuickWebEngineProfile::QQuickWebEngineProfile(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickWebEngineProfile *ritual_ZN22QQuickWebEngineProfileC1EP7QObject(
    QObject *parent) {
  return new CuteQQuickWebEngineProfile(parent);
}

//  QQuickWebEngineProfile::QQuickWebEngineProfile(const QString
//      &storageName, QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickWebEngineProfile *ritual_ZN22QQuickWebEngineProfileC1ERK7QStringP7QObject(
    const QString *storageName,
    QObject *parent) {
  return new CuteQQuickWebEngineProfile(*storageName, parent);
}

//  QQuickWebEngineProfile::~QQuickWebEngineProfile()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickWebEngineProfileD1Ev(QQuickWebEngineProfile *self) {
  delete self;
}

//  QString QQuickWebEngineProfile::storageName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QQuickWebEngineProfile11storageNameEv(
    const QQuickWebEngineProfile *self) {
  return new QString(self->storageName());
}

//  void QQuickWebEngineProfile::setStorageName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickWebEngineProfile14setStorageNameERK7QString(
    QQuickWebEngineProfile *self,
    const QString *name) {
  self->setStorageName(*name);
}

//  bool QQuickWebEngineProfile::isOffTheRecord() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QQuickWebEngineProfile14isOffTheRecordEv(
    const QQuickWebEngineProfile *self) {
  return self->isOffTheRecord();
}

//  void QQuickWebEngineProfile::setOffTheRecord(bool offTheRecord)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickWebEngineProfile15setOffTheRecordEb(
    QQuickWebEngineProfile *self,
    bool offTheRecord) {
  self->setOffTheRecord(offTheRecord);
}

//  QString QQuickWebEngineProfile::persistentStoragePath() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QQuickWebEngineProfile21persistentStoragePathEv(
    const QQuickWebEngineProfile *self) {
  return new QString(self->persistentStoragePath());
}

//  void QQuickWebEngineProfile::setPersistentStoragePath(const QString
//      &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickWebEngineProfile24setPersistentStoragePathERK7QString(
    QQuickWebEngineProfile *self,
    const QString *path) {
  self->setPersistentStoragePath(*path);
}

//  QString QQuickWebEngineProfile::cachePath() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QQuickWebEngineProfile9cachePathEv(
    const QQuickWebEngineProfile *self) {
  return new QString(self->cachePath());
}

//  void QQuickWebEngineProfile::setCachePath(const QString &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickWebEngineProfile12setCachePathERK7QString(
    QQuickWebEngineProfile *self,
    const QString *path) {
  self->setCachePath(*path);
}

//  QString QQuickWebEngineProfile::httpUserAgent() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QQuickWebEngineProfile13httpUserAgentEv(
    const QQuickWebEngineProfile *self) {
  return new QString(self->httpUserAgent());
}

//  void QQuickWebEngineProfile::setHttpUserAgent(const QString &userAgent)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickWebEngineProfile16setHttpUserAgentERK7QString(
    QQuickWebEngineProfile *self,
    const QString *userAgent) {
  self->setHttpUserAgent(*userAgent);
}

//  HttpCacheType QQuickWebEngineProfile::httpCacheType() const
extern "C" Q_DECL_EXPORT
QQuickWebEngineProfile::HttpCacheType ritual_ZNK22QQuickWebEngineProfile13httpCacheTypeEv(
    const QQuickWebEngineProfile *self) {
  return self->httpCacheType();
}

//  void QQuickWebEngineProfile::setHttpCacheType(QQuickWebEngineProfile::Htt
//      pCacheType a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickWebEngineProfile16setHttpCacheTypeENS_13HttpCacheTypeE(
    QQuickWebEngineProfile *self,
    QQuickWebEngineProfile::HttpCacheType a0) {
  self->setHttpCacheType(a0);
}

//  PersistentCookiesPolicy QQuickWebEngineProfile::persistentCookiesPolicy()
//      const
extern "C" Q_DECL_EXPORT
QQuickWebEngineProfile::PersistentCookiesPolicy ritual_ZNK22QQuickWebEngineProfile23persistentCookiesPolicyEv(
    const QQuickWebEngineProfile *self) {
  return self->persistentCookiesPolicy();
}

//  void QQuickWebEngineProfile::setPersistentCookiesPolicy(QQuickWebEnginePr
//      ofile::PersistentCookiesPolicy a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickWebEngineProfile26setPersistentCookiesPolicyENS_23PersistentCookiesPolicyE(
    QQuickWebEngineProfile *self,
    QQuickWebEngineProfile::PersistentCookiesPolicy a0) {
  self->setPersistentCookiesPolicy(a0);
}

//  PersistentPermissionsPolicy
//      QQuickWebEngineProfile::persistentPermissionsPolicy() const
extern "C" Q_DECL_EXPORT
QQuickWebEngineProfile::PersistentPermissionsPolicy ritual_ZNK22QQuickWebEngineProfile27persistentPermissionsPolicyEv(
    const QQuickWebEngineProfile *self) {
  return self->persistentPermissionsPolicy();
}

//  void QQuickWebEngineProfile::setPersistentPermissionsPolicy(QQuickWebEngi
//      neProfile::PersistentPermissionsPolicy a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickWebEngineProfile30setPersistentPermissionsPolicyENS_27PersistentPermissionsPolicyE(
    QQuickWebEngineProfile *self,
    QQuickWebEngineProfile::PersistentPermissionsPolicy a0) {
  self->setPersistentPermissionsPolicy(a0);
}

//  int QQuickWebEngineProfile::httpCacheMaximumSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QQuickWebEngineProfile20httpCacheMaximumSizeEv(
    const QQuickWebEngineProfile *self) {
  return self->httpCacheMaximumSize();
}

//  void QQuickWebEngineProfile::setHttpCacheMaximumSize(int maxSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickWebEngineProfile23setHttpCacheMaximumSizeEi(
    QQuickWebEngineProfile *self,
    int maxSize) {
  self->setHttpCacheMaximumSize(maxSize);
}

//  QString QQuickWebEngineProfile::httpAcceptLanguage() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QQuickWebEngineProfile18httpAcceptLanguageEv(
    const QQuickWebEngineProfile *self) {
  return new QString(self->httpAcceptLanguage());
}

//  void QQuickWebEngineProfile::setHttpAcceptLanguage(const QString
//      &httpAcceptLanguage)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickWebEngineProfile21setHttpAcceptLanguageERK7QString(
    QQuickWebEngineProfile *self,
    const QString *httpAcceptLanguage) {
  self->setHttpAcceptLanguage(*httpAcceptLanguage);
}

//  QWebEngineCookieStore *QQuickWebEngineProfile::cookieStore() const
extern "C" Q_DECL_EXPORT
QWebEngineCookieStore *ritual_ZNK22QQuickWebEngineProfile11cookieStoreEv(
    const QQuickWebEngineProfile *self) {
  return self->cookieStore();
}

//  void QQuickWebEngineProfile::setUrlRequestInterceptor(QWebEngineUrlReques
//      tInterceptor *interceptor)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickWebEngineProfile24setUrlRequestInterceptorEP31QWebEngineUrlRequestInterceptor(
    QQuickWebEngineProfile *self,
    QWebEngineUrlRequestInterceptor *interceptor) {
  self->setUrlRequestInterceptor(interceptor);
}

//  const QWebEngineUrlSchemeHandler
//      *QQuickWebEngineProfile::urlSchemeHandler(const QByteArray &a0) const
extern "C" Q_DECL_EXPORT
const QWebEngineUrlSchemeHandler *ritual_ZNK22QQuickWebEngineProfile16urlSchemeHandlerERK10QByteArray(
    const QQuickWebEngineProfile *self,
    const QByteArray *a0) {
  return self->urlSchemeHandler(*a0);
}

//  void QQuickWebEngineProfile::installUrlSchemeHandler(const QByteArray
//      &scheme, QWebEngineUrlSchemeHandler *a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickWebEngineProfile23installUrlSchemeHandlerERK10QByteArrayP26QWebEngineUrlSchemeHandler(
    QQuickWebEngineProfile *self,
    const QByteArray *scheme,
    QWebEngineUrlSchemeHandler *a1) {
  self->installUrlSchemeHandler(*scheme, a1);
}

//  void QQuickWebEngineProfile::removeUrlScheme(const QByteArray &scheme)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickWebEngineProfile15removeUrlSchemeERK10QByteArray(
    QQuickWebEngineProfile *self,
    const QByteArray *scheme) {
  self->removeUrlScheme(*scheme);
}

//  void
//      QQuickWebEngineProfile::removeUrlSchemeHandler(QWebEngineUrlSchemeHan
//      dler *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickWebEngineProfile22removeUrlSchemeHandlerEP26QWebEngineUrlSchemeHandler(
    QQuickWebEngineProfile *self,
    QWebEngineUrlSchemeHandler *a0) {
  self->removeUrlSchemeHandler(a0);
}

//  void QQuickWebEngineProfile::removeAllUrlSchemeHandlers()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickWebEngineProfile26removeAllUrlSchemeHandlersEv(
    QQuickWebEngineProfile *self) {
  self->removeAllUrlSchemeHandlers();
}

//  void QQuickWebEngineProfile::clearHttpCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickWebEngineProfile14clearHttpCacheEv(
    QQuickWebEngineProfile *self) {
  self->clearHttpCache();
}

//  void QQuickWebEngineProfile::setSpellCheckLanguages(const QStringList
//      &languages)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickWebEngineProfile22setSpellCheckLanguagesERK5QListI7QStringE(
    QQuickWebEngineProfile *self,
    const QList<QString> *languages) {
  self->setSpellCheckLanguages(*languages);
}

//  QStringList QQuickWebEngineProfile::spellCheckLanguages() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK22QQuickWebEngineProfile19spellCheckLanguagesEv(
    const QQuickWebEngineProfile *self) {
  return new QList<QString>(self->spellCheckLanguages());
}

//  void QQuickWebEngineProfile::setSpellCheckEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickWebEngineProfile20setSpellCheckEnabledEb(
    QQuickWebEngineProfile *self,
    bool enabled) {
  self->setSpellCheckEnabled(enabled);
}

//  bool QQuickWebEngineProfile::isSpellCheckEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QQuickWebEngineProfile19isSpellCheckEnabledEv(
    const QQuickWebEngineProfile *self) {
  return self->isSpellCheckEnabled();
}

//  QQuickWebEngineScriptCollection *QQuickWebEngineProfile::userScripts()
//      const
extern "C" Q_DECL_EXPORT
QQuickWebEngineScriptCollection *ritual_ZNK22QQuickWebEngineProfile11userScriptsEv(
    const QQuickWebEngineProfile *self) {
  return self->userScripts();
}

//  QString QQuickWebEngineProfile::downloadPath() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QQuickWebEngineProfile12downloadPathEv(
    const QQuickWebEngineProfile *self) {
  return new QString(self->downloadPath());
}

//  void QQuickWebEngineProfile::setDownloadPath(const QString &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickWebEngineProfile15setDownloadPathERK7QString(
    QQuickWebEngineProfile *self,
    const QString *path) {
  self->setDownloadPath(*path);
}

//  bool QQuickWebEngineProfile::isPushServiceEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QQuickWebEngineProfile20isPushServiceEnabledEv(
    const QQuickWebEngineProfile *self) {
  return self->isPushServiceEnabled();
}

//  void QQuickWebEngineProfile::setPushServiceEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickWebEngineProfile21setPushServiceEnabledEb(
    QQuickWebEngineProfile *self,
    bool enable) {
  self->setPushServiceEnabled(enable);
}

//  QWebEngineClientCertificateStore
//      *QQuickWebEngineProfile::clientCertificateStore()
extern "C" Q_DECL_EXPORT
QWebEngineClientCertificateStore *ritual_ZN22QQuickWebEngineProfile22clientCertificateStoreEv(
    QQuickWebEngineProfile *self) {
  return self->clientCertificateStore();
}

//  QWebEngineClientHints *QQuickWebEngineProfile::clientHints() const
extern "C" Q_DECL_EXPORT
QWebEngineClientHints *ritual_ZNK22QQuickWebEngineProfile11clientHintsEv(
    const QQuickWebEngineProfile *self) {
  return self->clientHints();
}

//  QWebEngineExtensionManager *QQuickWebEngineProfile::extensionManager()
extern "C" Q_DECL_EXPORT
QWebEngineExtensionManager *ritual_ZN22QQuickWebEngineProfile16extensionManagerEv(
    QQuickWebEngineProfile *self) {
  return self->extensionManager();
}

//  QWebEnginePermission QQuickWebEngineProfile::queryPermission(const QUrl
//      &securityOrigin, QWebEnginePermission::PermissionType permissionType)
//      const
extern "C" Q_DECL_EXPORT
QWebEnginePermission *ritual_ZNK22QQuickWebEngineProfile15queryPermissionERK4QUrlN20QWebEnginePermission14PermissionTypeE(
    const QQuickWebEngineProfile *self,
    const QUrl *securityOrigin,
    QWebEnginePermission::PermissionType permissionType) {
  return new QWebEnginePermission(
      self->queryPermission(
          *securityOrigin,
          permissionType));
}

//  QList<QWebEnginePermission> QQuickWebEngineProfile::listAllPermissions()
//      const
extern "C" Q_DECL_EXPORT
QList<QWebEnginePermission> *ritual_ZNK22QQuickWebEngineProfile18listAllPermissionsEv(
    const QQuickWebEngineProfile *self) {
  return new QList<QWebEnginePermission>(self->listAllPermissions());
}

//  QList<QWebEnginePermission>
//      QQuickWebEngineProfile::listPermissionsForOrigin(const QUrl
//      &securityOrigin) const
extern "C" Q_DECL_EXPORT
QList<QWebEnginePermission> *ritual_ZNK22QQuickWebEngineProfile24listPermissionsForOriginERK4QUrl(
    const QQuickWebEngineProfile *self,
    const QUrl *securityOrigin) {
  return new QList<QWebEnginePermission>(
      self->listPermissionsForOrigin(
          *securityOrigin));
}

//  QList<QWebEnginePermission> QQuickWebEngineProfile::listPermissionsForPer
//      missionType(QWebEnginePermission::PermissionType permissionType)
//      const
extern "C" Q_DECL_EXPORT
QList<QWebEnginePermission> *ritual_ZNK22QQuickWebEngineProfile32listPermissionsForPermissionTypeEN20QWebEnginePermission14PermissionTypeE(
    const QQuickWebEngineProfile *self,
    QWebEnginePermission::PermissionType permissionType) {
  return new QList<QWebEnginePermission>(
      self->listPermissionsForPermissionType(
          permissionType));
}

//  QQuickWebEngineProfile *QQuickWebEngineProfile::defaultProfile()
extern "C" Q_DECL_EXPORT
QQuickWebEngineProfile *ritual_ZN22QQuickWebEngineProfile14defaultProfileEv() {
  return QQuickWebEngineProfile::defaultProfile();
}

//  void QQuickWebEngineProfile::storageNameChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickWebEngineProfile18storageNameChangedEv(
    QQuickWebEngineProfile *self) {
  self->storageNameChanged();
}

//  void QQuickWebEngineProfile::offTheRecordChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickWebEngineProfile19offTheRecordChangedEv(
    QQuickWebEngineProfile *self) {
  self->offTheRecordChanged();
}

//  void QQuickWebEngineProfile::persistentStoragePathChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickWebEngineProfile28persistentStoragePathChangedEv(
    QQuickWebEngineProfile *self) {
  self->persistentStoragePathChanged();
}

//  void QQuickWebEngineProfile::cachePathChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickWebEngineProfile16cachePathChangedEv(
    QQuickWebEngineProfile *self) {
  self->cachePathChanged();
}

//  void QQuickWebEngineProfile::httpUserAgentChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickWebEngineProfile20httpUserAgentChangedEv(
    QQuickWebEngineProfile *self) {
  self->httpUserAgentChanged();
}

//  void QQuickWebEngineProfile::httpCacheTypeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickWebEngineProfile20httpCacheTypeChangedEv(
    QQuickWebEngineProfile *self) {
  self->httpCacheTypeChanged();
}

//  void QQuickWebEngineProfile::persistentCookiesPolicyChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickWebEngineProfile30persistentCookiesPolicyChangedEv(
    QQuickWebEngineProfile *self) {
  self->persistentCookiesPolicyChanged();
}

//  void QQuickWebEngineProfile::httpCacheMaximumSizeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickWebEngineProfile27httpCacheMaximumSizeChangedEv(
    QQuickWebEngineProfile *self) {
  self->httpCacheMaximumSizeChanged();
}

//  void QQuickWebEngineProfile::httpAcceptLanguageChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickWebEngineProfile25httpAcceptLanguageChangedEv(
    QQuickWebEngineProfile *self) {
  self->httpAcceptLanguageChanged();
}

//  void QQuickWebEngineProfile::spellCheckLanguagesChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickWebEngineProfile26spellCheckLanguagesChangedEv(
    QQuickWebEngineProfile *self) {
  self->spellCheckLanguagesChanged();
}

//  void QQuickWebEngineProfile::spellCheckEnabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickWebEngineProfile24spellCheckEnabledChangedEv(
    QQuickWebEngineProfile *self) {
  self->spellCheckEnabledChanged();
}

//  void QQuickWebEngineProfile::downloadPathChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickWebEngineProfile19downloadPathChangedEv(
    QQuickWebEngineProfile *self) {
  self->downloadPathChanged();
}

//  void QQuickWebEngineProfile::pushServiceEnabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickWebEngineProfile25pushServiceEnabledChangedEv(
    QQuickWebEngineProfile *self) {
  self->pushServiceEnabledChanged();
}

//  void QQuickWebEngineProfile::clearHttpCacheCompleted()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickWebEngineProfile23clearHttpCacheCompletedEv(
    QQuickWebEngineProfile *self) {
  self->clearHttpCacheCompleted();
}

//  void QQuickWebEngineProfile::persistentPermissionsPolicyChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickWebEngineProfile34persistentPermissionsPolicyChangedEv(
    QQuickWebEngineProfile *self) {
  self->persistentPermissionsPolicyChanged();
}

//  void
//      QQuickWebEngineProfile::downloadRequested(QQuickWebEngineDownloadRequ
//      est *download)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickWebEngineProfile17downloadRequestedEP30QQuickWebEngineDownloadRequest(
    QQuickWebEngineProfile *self,
    QQuickWebEngineDownloadRequest *download) {
  self->downloadRequested(download);
}

//  void
//      QQuickWebEngineProfile::downloadFinished(QQuickWebEngineDownloadReque
//      st *download)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickWebEngineProfile16downloadFinishedEP30QQuickWebEngineDownloadRequest(
    QQuickWebEngineProfile *self,
    QQuickWebEngineDownloadRequest *download) {
  self->downloadFinished(download);
}

//  void QQuickWebEngineProfile::presentNotification(QWebEngineNotification
//      *notification)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickWebEngineProfile19presentNotificationEP22QWebEngineNotification(
    QQuickWebEngineProfile *self,
    QWebEngineNotification *notification) {
  self->presentNotification(notification);
}

//  QQuickWebEngineProfilePrivate *QQuickWebEngineProfile::d_func()
extern "C" Q_DECL_EXPORT
QQuickWebEngineProfilePrivate *ritual_ZN22QQuickWebEngineProfile6d_funcEv(
    QQuickWebEngineProfile *self) {
  return self->d_func();
}

//  const QQuickWebEngineProfilePrivate *QQuickWebEngineProfile::d_func()
//      const
extern "C" Q_DECL_EXPORT
const QQuickWebEngineProfilePrivate *ritual_ZNK22QQuickWebEngineProfile6d_funcEv(
    const QQuickWebEngineProfile *self) {
  return self->d_func();
}

//  QQuickWebEngineProfile::QQuickWebEngineProfile(QQuickWebEngineProfilePriv
//      ate *a0, QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickWebEngineProfile *ritual_ZN22QQuickWebEngineProfileC1EP29QQuickWebEngineProfilePrivateP7QObject(
    QQuickWebEngineProfilePrivate *a0,
    QObject *parent) {
  return new CuteQQuickWebEngineProfile(a0, parent);
}

//  QQuickWebEngineSettings *QQuickWebEngineProfile::settings() const
extern "C" Q_DECL_EXPORT
QQuickWebEngineSettings *ritual_ZNK22QQuickWebEngineProfile8settingsEv(
    const QQuickWebEngineProfile *self) {
  return self->settings();
}

//  a Python function taken by a CuteQQuickWebEngineProfile, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickWebEngineProfile(
    QQuickWebEngineProfile *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickWebEngineProfile *>(self)->take(key, call);
}
