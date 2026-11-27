//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebEngineCore/qwebengineprofilebuilder.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtWebEngineCore/qwebengineprofilebuilder.h>
#include <QtCore/qstring.h>
#include <QtNetwork/qsslcertificate.h>
#include <QtCore/qlist.h>

//  QWebEngineProfileBuilder::QWebEngineProfileBuilder()
extern "C" Q_DECL_EXPORT
QWebEngineProfileBuilder *ritual_ZN24QWebEngineProfileBuilderC1Ev() {
  return new QWebEngineProfileBuilder();
}

//  QWebEngineProfileBuilder::~QWebEngineProfileBuilder()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QWebEngineProfileBuilderD1Ev(
    QWebEngineProfileBuilder *self) {
  delete self;
}

//  QWebEngineProfile *QWebEngineProfileBuilder::createProfile(const QString
//      &storageName, QObject *parent) const
extern "C" Q_DECL_EXPORT
QWebEngineProfile *ritual_ZNK24QWebEngineProfileBuilder13createProfileERK7QStringP7QObject(
    const QWebEngineProfileBuilder *self,
    const QString *storageName,
    QObject *parent) {
  return self->createProfile(*storageName, parent);
}

//  QWebEngineProfile
//      *QWebEngineProfileBuilder::createOffTheRecordProfile(QObject *parent)
extern "C" Q_DECL_EXPORT
QWebEngineProfile *ritual_ZN24QWebEngineProfileBuilder25createOffTheRecordProfileEP7QObject(
    QObject *parent) {
  return QWebEngineProfileBuilder::createOffTheRecordProfile(parent);
}

//  QWebEngineProfileBuilder
//      &QWebEngineProfileBuilder::setPersistentStoragePath(const QString
//      &path)
extern "C" Q_DECL_EXPORT
QWebEngineProfileBuilder *ritual_ZN24QWebEngineProfileBuilder24setPersistentStoragePathERK7QString(
    QWebEngineProfileBuilder *self,
    const QString *path) {
  return &(self->setPersistentStoragePath(*path));
}

//  QWebEngineProfileBuilder &QWebEngineProfileBuilder::setCachePath(const
//      QString &path)
extern "C" Q_DECL_EXPORT
QWebEngineProfileBuilder *ritual_ZN24QWebEngineProfileBuilder12setCachePathERK7QString(
    QWebEngineProfileBuilder *self,
    const QString *path) {
  return &(self->setCachePath(*path));
}

//  QWebEngineProfileBuilder &QWebEngineProfileBuilder::setHttpCacheType(QWeb
//      EngineProfile::HttpCacheType httpCacheType)
extern "C" Q_DECL_EXPORT
QWebEngineProfileBuilder *ritual_ZN24QWebEngineProfileBuilder16setHttpCacheTypeEN17QWebEngineProfile13HttpCacheTypeE(
    QWebEngineProfileBuilder *self,
    QWebEngineProfile::HttpCacheType httpCacheType) {
  return &(self->setHttpCacheType(httpCacheType));
}

//  QWebEngineProfileBuilder &QWebEngineProfileBuilder::setPersistentCookiesP
//      olicy(QWebEngineProfile::PersistentCookiesPolicy
//      persistentCookiesPolicy)
extern "C" Q_DECL_EXPORT
QWebEngineProfileBuilder *ritual_ZN24QWebEngineProfileBuilder26setPersistentCookiesPolicyEN17QWebEngineProfile23PersistentCookiesPolicyE(
    QWebEngineProfileBuilder *self,
    QWebEngineProfile::PersistentCookiesPolicy persistentCookiesPolicy) {
  return &(self->setPersistentCookiesPolicy(persistentCookiesPolicy));
}

//  QWebEngineProfileBuilder
//      &QWebEngineProfileBuilder::setHttpCacheMaximumSize(int
//      maxSizeInBytes)
extern "C" Q_DECL_EXPORT
QWebEngineProfileBuilder *ritual_ZN24QWebEngineProfileBuilder23setHttpCacheMaximumSizeEi(
    QWebEngineProfileBuilder *self,
    int maxSizeInBytes) {
  return &(self->setHttpCacheMaximumSize(maxSizeInBytes));
}

//  QWebEngineProfileBuilder &QWebEngineProfileBuilder::setPersistentPermissi
//      onsPolicy(QWebEngineProfile::PersistentPermissionsPolicy
//      persistentPermissionPolicy)
extern "C" Q_DECL_EXPORT
QWebEngineProfileBuilder *ritual_ZN24QWebEngineProfileBuilder30setPersistentPermissionsPolicyEN17QWebEngineProfile27PersistentPermissionsPolicyE(
    QWebEngineProfileBuilder *self,
    QWebEngineProfile::PersistentPermissionsPolicy persistentPermissionPolicy) {
  return &(self->setPersistentPermissionsPolicy(persistentPermissionPolicy));
}

//  QWebEngineProfileBuilder
//      &QWebEngineProfileBuilder::setAdditionalTrustedCertificates(const
//      QList<QSslCertificate> &additionalTrustedCertificates)
extern "C" Q_DECL_EXPORT
QWebEngineProfileBuilder *ritual_ZN24QWebEngineProfileBuilder32setAdditionalTrustedCertificatesERK5QListI15QSslCertificateE(
    QWebEngineProfileBuilder *self,
    const QList<QSslCertificate> *additionalTrustedCertificates) {
  return &(
      self->setAdditionalTrustedCertificates(
          *additionalTrustedCertificates));
}
