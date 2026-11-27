//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebEngineCore/qwebengineprofile.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtWebEngineCore/qwebengineprofile.h>
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qbytearray.h>
#include <QtNetwork/qsslcertificate.h>
#include <QtWebEngineCore/qwebenginepermission.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#include <functional>
#include <memory>
#include <QtWebEngineCore/QWebEngineNotification>
#include <QtCore/QUrl>
#include <QtGui/QIcon>
#include <string>

//  A QWebEngineProfile that Python can take functions over in. Every QWebEngineProfile
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWebEngineProfileCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWebEngineProfileCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEngineProfileCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEngineProfileCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEngineProfileCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEngineProfileCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEngineProfileCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQWebEngineProfile : public QWebEngineProfile {
public:
  using QWebEngineProfile::QWebEngineProfile;
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
      CuteQWebEngineProfileCall0 call = reinterpret_cast<CuteQWebEngineProfileCall0>(taken[0]);
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
      CuteQWebEngineProfileCall1 call = reinterpret_cast<CuteQWebEngineProfileCall1>(taken[1]);
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
      CuteQWebEngineProfileCall2 call = reinterpret_cast<CuteQWebEngineProfileCall2>(taken[2]);
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
      CuteQWebEngineProfileCall3 call = reinterpret_cast<CuteQWebEngineProfileCall3>(taken[3]);
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
      CuteQWebEngineProfileCall4 call = reinterpret_cast<CuteQWebEngineProfileCall4>(taken[4]);
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
      CuteQWebEngineProfileCall5 call = reinterpret_cast<CuteQWebEngineProfileCall5>(taken[5]);
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
      CuteQWebEngineProfileCall6 call = reinterpret_cast<CuteQWebEngineProfileCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QWebEngineProfile::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QWebEngineProfile10metaObjectEv(
    const QWebEngineProfile *self) {
  return self->metaObject();
}

//  void *QWebEngineProfile::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17QWebEngineProfile11qt_metacastEPKc(
    QWebEngineProfile *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QWebEngineProfile::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QWebEngineProfile11qt_metacallEN11QMetaObject4CallEiPPv(
    QWebEngineProfile *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QWebEngineProfile::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QWebEngineProfile2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWebEngineProfile::tr(s, c, n));
}

//  QWebEngineProfile::QWebEngineProfile(QObject *parent)
extern "C" Q_DECL_EXPORT
QWebEngineProfile *ritual_ZN17QWebEngineProfileC1EP7QObject(
    QObject *parent) {
  return new CuteQWebEngineProfile(parent);
}

//  QWebEngineProfile::QWebEngineProfile(const QString &name, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QWebEngineProfile *ritual_ZN17QWebEngineProfileC1ERK7QStringP7QObject(
    const QString *name,
    QObject *parent) {
  return new CuteQWebEngineProfile(*name, parent);
}

//  QWebEngineProfile::~QWebEngineProfile()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWebEngineProfileD1Ev(QWebEngineProfile *self) {
  delete self;
}

//  QString QWebEngineProfile::storageName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QWebEngineProfile11storageNameEv(
    const QWebEngineProfile *self) {
  return new QString(self->storageName());
}

//  bool QWebEngineProfile::isOffTheRecord() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QWebEngineProfile14isOffTheRecordEv(
    const QWebEngineProfile *self) {
  return self->isOffTheRecord();
}

//  QString QWebEngineProfile::persistentStoragePath() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QWebEngineProfile21persistentStoragePathEv(
    const QWebEngineProfile *self) {
  return new QString(self->persistentStoragePath());
}

//  void QWebEngineProfile::setPersistentStoragePath(const QString &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWebEngineProfile24setPersistentStoragePathERK7QString(
    QWebEngineProfile *self,
    const QString *path) {
  self->setPersistentStoragePath(*path);
}

//  QString QWebEngineProfile::cachePath() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QWebEngineProfile9cachePathEv(
    const QWebEngineProfile *self) {
  return new QString(self->cachePath());
}

//  void QWebEngineProfile::setCachePath(const QString &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWebEngineProfile12setCachePathERK7QString(
    QWebEngineProfile *self,
    const QString *path) {
  self->setCachePath(*path);
}

//  QString QWebEngineProfile::httpUserAgent() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QWebEngineProfile13httpUserAgentEv(
    const QWebEngineProfile *self) {
  return new QString(self->httpUserAgent());
}

//  void QWebEngineProfile::setHttpUserAgent(const QString &userAgent)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWebEngineProfile16setHttpUserAgentERK7QString(
    QWebEngineProfile *self,
    const QString *userAgent) {
  self->setHttpUserAgent(*userAgent);
}

//  HttpCacheType QWebEngineProfile::httpCacheType() const
extern "C" Q_DECL_EXPORT
QWebEngineProfile::HttpCacheType ritual_ZNK17QWebEngineProfile13httpCacheTypeEv(
    const QWebEngineProfile *self) {
  return self->httpCacheType();
}

//  void QWebEngineProfile::setHttpCacheType(QWebEngineProfile::HttpCacheType
//      a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWebEngineProfile16setHttpCacheTypeENS_13HttpCacheTypeE(
    QWebEngineProfile *self,
    QWebEngineProfile::HttpCacheType a0) {
  self->setHttpCacheType(a0);
}

//  void QWebEngineProfile::setHttpAcceptLanguage(const QString
//      &httpAcceptLanguage)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWebEngineProfile21setHttpAcceptLanguageERK7QString(
    QWebEngineProfile *self,
    const QString *httpAcceptLanguage) {
  self->setHttpAcceptLanguage(*httpAcceptLanguage);
}

//  QString QWebEngineProfile::httpAcceptLanguage() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QWebEngineProfile18httpAcceptLanguageEv(
    const QWebEngineProfile *self) {
  return new QString(self->httpAcceptLanguage());
}

//  PersistentCookiesPolicy QWebEngineProfile::persistentCookiesPolicy()
//      const
extern "C" Q_DECL_EXPORT
QWebEngineProfile::PersistentCookiesPolicy ritual_ZNK17QWebEngineProfile23persistentCookiesPolicyEv(
    const QWebEngineProfile *self) {
  return self->persistentCookiesPolicy();
}

//  void QWebEngineProfile::setPersistentCookiesPolicy(QWebEngineProfile::Per
//      sistentCookiesPolicy a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWebEngineProfile26setPersistentCookiesPolicyENS_23PersistentCookiesPolicyE(
    QWebEngineProfile *self,
    QWebEngineProfile::PersistentCookiesPolicy a0) {
  self->setPersistentCookiesPolicy(a0);
}

//  PersistentPermissionsPolicy
//      QWebEngineProfile::persistentPermissionsPolicy() const
extern "C" Q_DECL_EXPORT
QWebEngineProfile::PersistentPermissionsPolicy ritual_ZNK17QWebEngineProfile27persistentPermissionsPolicyEv(
    const QWebEngineProfile *self) {
  return self->persistentPermissionsPolicy();
}

//  void QWebEngineProfile::setPersistentPermissionsPolicy(QWebEngineProfile:
//      :PersistentPermissionsPolicy a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWebEngineProfile30setPersistentPermissionsPolicyENS_27PersistentPermissionsPolicyE(
    QWebEngineProfile *self,
    QWebEngineProfile::PersistentPermissionsPolicy a0) {
  self->setPersistentPermissionsPolicy(a0);
}

//  int QWebEngineProfile::httpCacheMaximumSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QWebEngineProfile20httpCacheMaximumSizeEv(
    const QWebEngineProfile *self) {
  return self->httpCacheMaximumSize();
}

//  void QWebEngineProfile::setHttpCacheMaximumSize(int maxSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWebEngineProfile23setHttpCacheMaximumSizeEi(
    QWebEngineProfile *self,
    int maxSize) {
  self->setHttpCacheMaximumSize(maxSize);
}

//  QWebEngineCookieStore *QWebEngineProfile::cookieStore()
extern "C" Q_DECL_EXPORT
QWebEngineCookieStore *ritual_ZN17QWebEngineProfile11cookieStoreEv(
    QWebEngineProfile *self) {
  return self->cookieStore();
}

//  void QWebEngineProfile::setUrlRequestInterceptor(QWebEngineUrlRequestInte
//      rceptor *interceptor)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWebEngineProfile24setUrlRequestInterceptorEP31QWebEngineUrlRequestInterceptor(
    QWebEngineProfile *self,
    QWebEngineUrlRequestInterceptor *interceptor) {
  self->setUrlRequestInterceptor(interceptor);
}

//  void QWebEngineProfile::clearAllVisitedLinks()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWebEngineProfile20clearAllVisitedLinksEv(
    QWebEngineProfile *self) {
  self->clearAllVisitedLinks();
}

//  void QWebEngineProfile::clearVisitedLinks(const QList<QUrl> &urls)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWebEngineProfile17clearVisitedLinksERK5QListI4QUrlE(
    QWebEngineProfile *self,
    const QList<QUrl> *urls) {
  self->clearVisitedLinks(*urls);
}

//  bool QWebEngineProfile::visitedLinksContainsUrl(const QUrl &url) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QWebEngineProfile23visitedLinksContainsUrlERK4QUrl(
    const QWebEngineProfile *self,
    const QUrl *url) {
  return self->visitedLinksContainsUrl(*url);
}

//  QWebEngineSettings *QWebEngineProfile::settings() const
extern "C" Q_DECL_EXPORT
QWebEngineSettings *ritual_ZNK17QWebEngineProfile8settingsEv(
    const QWebEngineProfile *self) {
  return self->settings();
}

//  QWebEngineScriptCollection *QWebEngineProfile::scripts() const
extern "C" Q_DECL_EXPORT
QWebEngineScriptCollection *ritual_ZNK17QWebEngineProfile7scriptsEv(
    const QWebEngineProfile *self) {
  return self->scripts();
}

//  QWebEngineClientHints *QWebEngineProfile::clientHints() const
extern "C" Q_DECL_EXPORT
QWebEngineClientHints *ritual_ZNK17QWebEngineProfile11clientHintsEv(
    const QWebEngineProfile *self) {
  return self->clientHints();
}

//  const QWebEngineUrlSchemeHandler
//      *QWebEngineProfile::urlSchemeHandler(const QByteArray &a0) const
extern "C" Q_DECL_EXPORT
const QWebEngineUrlSchemeHandler *ritual_ZNK17QWebEngineProfile16urlSchemeHandlerERK10QByteArray(
    const QWebEngineProfile *self,
    const QByteArray *a0) {
  return self->urlSchemeHandler(*a0);
}

//  void QWebEngineProfile::installUrlSchemeHandler(const QByteArray &scheme,
//      QWebEngineUrlSchemeHandler *a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWebEngineProfile23installUrlSchemeHandlerERK10QByteArrayP26QWebEngineUrlSchemeHandler(
    QWebEngineProfile *self,
    const QByteArray *scheme,
    QWebEngineUrlSchemeHandler *a1) {
  self->installUrlSchemeHandler(*scheme, a1);
}

//  void QWebEngineProfile::removeUrlScheme(const QByteArray &scheme)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWebEngineProfile15removeUrlSchemeERK10QByteArray(
    QWebEngineProfile *self,
    const QByteArray *scheme) {
  self->removeUrlScheme(*scheme);
}

//  void QWebEngineProfile::removeUrlSchemeHandler(QWebEngineUrlSchemeHandler
//      *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWebEngineProfile22removeUrlSchemeHandlerEP26QWebEngineUrlSchemeHandler(
    QWebEngineProfile *self,
    QWebEngineUrlSchemeHandler *a0) {
  self->removeUrlSchemeHandler(a0);
}

//  void QWebEngineProfile::removeAllUrlSchemeHandlers()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWebEngineProfile26removeAllUrlSchemeHandlersEv(
    QWebEngineProfile *self) {
  self->removeAllUrlSchemeHandlers();
}

//  void QWebEngineProfile::clearHttpCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWebEngineProfile14clearHttpCacheEv(
    QWebEngineProfile *self) {
  self->clearHttpCache();
}

//  void QWebEngineProfile::setSpellCheckLanguages(const QStringList
//      &languages)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWebEngineProfile22setSpellCheckLanguagesERK5QListI7QStringE(
    QWebEngineProfile *self,
    const QList<QString> *languages) {
  self->setSpellCheckLanguages(*languages);
}

//  QStringList QWebEngineProfile::spellCheckLanguages() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK17QWebEngineProfile19spellCheckLanguagesEv(
    const QWebEngineProfile *self) {
  return new QList<QString>(self->spellCheckLanguages());
}

//  void QWebEngineProfile::setSpellCheckEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWebEngineProfile20setSpellCheckEnabledEb(
    QWebEngineProfile *self,
    bool enabled) {
  self->setSpellCheckEnabled(enabled);
}

//  bool QWebEngineProfile::isSpellCheckEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QWebEngineProfile19isSpellCheckEnabledEv(
    const QWebEngineProfile *self) {
  return self->isSpellCheckEnabled();
}

//  QString QWebEngineProfile::downloadPath() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QWebEngineProfile12downloadPathEv(
    const QWebEngineProfile *self) {
  return new QString(self->downloadPath());
}

//  void QWebEngineProfile::setDownloadPath(const QString &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWebEngineProfile15setDownloadPathERK7QString(
    QWebEngineProfile *self,
    const QString *path) {
  self->setDownloadPath(*path);
}

//  bool QWebEngineProfile::isPushServiceEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QWebEngineProfile20isPushServiceEnabledEv(
    const QWebEngineProfile *self) {
  return self->isPushServiceEnabled();
}

//  void QWebEngineProfile::setPushServiceEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWebEngineProfile21setPushServiceEnabledEb(
    QWebEngineProfile *self,
    bool enabled) {
  self->setPushServiceEnabled(enabled);
}

//  void QWebEngineProfile::setNotificationPresenter(std::function<void
//      (std::unique_ptr<QWebEngineNotification>)> notificationPresenter)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWebEngineProfile24setNotificationPresenterESt8functionIFvSt10unique_ptrI22QWebEngineNotificationSt14default_deleteIS2_EEEE(
    QWebEngineProfile *self,
    const std::function<void (std::unique_ptr<QWebEngineNotification>)> *notificationPresenter) {
  self->setNotificationPresenter(*notificationPresenter);
}

//  QWebEngineClientCertificateStore
//      *QWebEngineProfile::clientCertificateStore()
extern "C" Q_DECL_EXPORT
QWebEngineClientCertificateStore *ritual_ZN17QWebEngineProfile22clientCertificateStoreEv(
    QWebEngineProfile *self) {
  return self->clientCertificateStore();
}

//  QList<QSslCertificate> QWebEngineProfile::additionalTrustedCertificates()
//      const
extern "C" Q_DECL_EXPORT
QList<QSslCertificate> *ritual_ZNK17QWebEngineProfile29additionalTrustedCertificatesEv(
    const QWebEngineProfile *self) {
  return new QList<QSslCertificate>(self->additionalTrustedCertificates());
}

//  void QWebEngineProfile::requestIconForPageURL(const QUrl &url, int
//      desiredSizeInPixel, std::function<void (const QIcon &, const QUrl &,
//      const QUrl &)> iconAvailableCallback) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK17QWebEngineProfile21requestIconForPageURLERK4QUrliSt8functionIFvRK5QIconS2_S2_EE(
    const QWebEngineProfile *self,
    const QUrl *url,
    int desiredSizeInPixel,
    const std::function<void (const QIcon &, const QUrl &, const QUrl &)> *iconAvailableCallback) {
  self->requestIconForPageURL(
      *url,
      desiredSizeInPixel,
      *iconAvailableCallback);
}

//  void QWebEngineProfile::requestIconForIconURL(const QUrl &url, int
//      desiredSizeInPixel, std::function<void (const QIcon &, const QUrl &)>
//      iconAvailableCallback) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK17QWebEngineProfile21requestIconForIconURLERK4QUrliSt8functionIFvRK5QIconS2_EE(
    const QWebEngineProfile *self,
    const QUrl *url,
    int desiredSizeInPixel,
    const std::function<void (const QIcon &, const QUrl &)> *iconAvailableCallback) {
  self->requestIconForIconURL(
      *url,
      desiredSizeInPixel,
      *iconAvailableCallback);
}

//  QWebEnginePermission QWebEngineProfile::queryPermission(const QUrl
//      &securityOrigin, QWebEnginePermission::PermissionType permissionType)
//      const
extern "C" Q_DECL_EXPORT
QWebEnginePermission *ritual_ZNK17QWebEngineProfile15queryPermissionERK4QUrlN20QWebEnginePermission14PermissionTypeE(
    const QWebEngineProfile *self,
    const QUrl *securityOrigin,
    QWebEnginePermission::PermissionType permissionType) {
  return new QWebEnginePermission(
      self->queryPermission(
          *securityOrigin,
          permissionType));
}

//  QList<QWebEnginePermission> QWebEngineProfile::listAllPermissions() const
extern "C" Q_DECL_EXPORT
QList<QWebEnginePermission> *ritual_ZNK17QWebEngineProfile18listAllPermissionsEv(
    const QWebEngineProfile *self) {
  return new QList<QWebEnginePermission>(self->listAllPermissions());
}

//  QList<QWebEnginePermission>
//      QWebEngineProfile::listPermissionsForOrigin(const QUrl
//      &securityOrigin) const
extern "C" Q_DECL_EXPORT
QList<QWebEnginePermission> *ritual_ZNK17QWebEngineProfile24listPermissionsForOriginERK4QUrl(
    const QWebEngineProfile *self,
    const QUrl *securityOrigin) {
  return new QList<QWebEnginePermission>(
      self->listPermissionsForOrigin(
          *securityOrigin));
}

//  QList<QWebEnginePermission> QWebEngineProfile::listPermissionsForPermissi
//      onType(QWebEnginePermission::PermissionType permissionType) const
extern "C" Q_DECL_EXPORT
QList<QWebEnginePermission> *ritual_ZNK17QWebEngineProfile32listPermissionsForPermissionTypeEN20QWebEnginePermission14PermissionTypeE(
    const QWebEngineProfile *self,
    QWebEnginePermission::PermissionType permissionType) {
  return new QList<QWebEnginePermission>(
      self->listPermissionsForPermissionType(
          permissionType));
}

//  QWebEngineExtensionManager *QWebEngineProfile::extensionManager() const
extern "C" Q_DECL_EXPORT
QWebEngineExtensionManager *ritual_ZNK17QWebEngineProfile16extensionManagerEv(
    const QWebEngineProfile *self) {
  return self->extensionManager();
}

//  void QWebEngineProfile::setCryptoModulePasswordFunction(std::function<std
//      ::string (std::string, std::string, bool)> passwordFunction)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWebEngineProfile31setCryptoModulePasswordFunctionESt8functionIFNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEES6_S6_bEE(
    QWebEngineProfile *self,
    const std::function<std::string (std::string, std::string, bool)> *passwordFunction) {
  self->setCryptoModulePasswordFunction(*passwordFunction);
}

//  QWebEngineProfile *QWebEngineProfile::defaultProfile()
extern "C" Q_DECL_EXPORT
QWebEngineProfile *ritual_ZN17QWebEngineProfile14defaultProfileEv() {
  return QWebEngineProfile::defaultProfile();
}

//  void QWebEngineProfile::downloadRequested(QWebEngineDownloadRequest
//      *download)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWebEngineProfile17downloadRequestedEP25QWebEngineDownloadRequest(
    QWebEngineProfile *self,
    QWebEngineDownloadRequest *download) {
  self->downloadRequested(download);
}

//  void QWebEngineProfile::clearHttpCacheCompleted()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWebEngineProfile23clearHttpCacheCompletedEv(
    QWebEngineProfile *self) {
  self->clearHttpCacheCompleted();
}

//  QWebEngineProfilePrivate *QWebEngineProfile::d_func()
extern "C" Q_DECL_EXPORT
QWebEngineProfilePrivate *ritual_ZN17QWebEngineProfile6d_funcEv(
    QWebEngineProfile *self) {
  return self->d_func();
}

//  const QWebEngineProfilePrivate *QWebEngineProfile::d_func() const
extern "C" Q_DECL_EXPORT
const QWebEngineProfilePrivate *ritual_ZNK17QWebEngineProfile6d_funcEv(
    const QWebEngineProfile *self) {
  return self->d_func();
}

//  QWebEngineProfile::QWebEngineProfile(QWebEngineProfilePrivate *a0,
//      QObject *parent)
extern "C" Q_DECL_EXPORT
QWebEngineProfile *ritual_ZN17QWebEngineProfileC1EP24QWebEngineProfilePrivateP7QObject(
    QWebEngineProfilePrivate *a0,
    QObject *parent) {
  return new CuteQWebEngineProfile(a0, parent);
}

//  std::function<void (std::unique_ptr<QWebEngineNotification>)>
//      QWebEngineProfile::notificationPresenter()
extern "C" Q_DECL_EXPORT
std::function<void (std::unique_ptr<QWebEngineNotification>)> *ritual_ZN17QWebEngineProfile21notificationPresenterEv(
    QWebEngineProfile *self) {
  return new std::function<void (std::unique_ptr<QWebEngineNotification>)>(
      self->notificationPresenter());
}

//  a Python function taken by a CuteQWebEngineProfile, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWebEngineProfile(
    QWebEngineProfile *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWebEngineProfile *>(self)->take(key, call);
}

//  a std::function<void (std::unique_ptr<QWebEngineNotification>)> a ritual
//      of QWebEngineProfile gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QWebEngineProfile__std_function_void_std_unique_ptr_QWebEngineNotification(
    std::function<void (std::unique_ptr<QWebEngineNotification>)> *self) {
  delete self;
}
