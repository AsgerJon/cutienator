//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebEngineCore/qwebengineclientcertificatestore.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtWebEngineCore/qtwebenginecoreglobal.h>
#if QT_CONFIG(ssl)
#include <QtWebEngineCore/qwebengineclientcertificatestore.h>
#include <QtNetwork/qsslcertificate.h>
#include <QtNetwork/qsslkey.h>
#include <QtCore/qlist.h>

//  void QWebEngineClientCertificateStore::add(const QSslCertificate
//      &certificate, const QSslKey &privateKey)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QWebEngineClientCertificateStore3addERK15QSslCertificateRK7QSslKey(
    QWebEngineClientCertificateStore *self,
    const QSslCertificate *certificate,
    const QSslKey *privateKey) {
  self->add(*certificate, *privateKey);
}

//  QList<QSslCertificate> QWebEngineClientCertificateStore::certificates()
//      const
extern "C" Q_DECL_EXPORT
QList<QSslCertificate> *ritual_ZNK32QWebEngineClientCertificateStore12certificatesEv(
    const QWebEngineClientCertificateStore *self) {
  return new QList<QSslCertificate>(self->certificates());
}

//  void QWebEngineClientCertificateStore::remove(const QSslCertificate
//      &certificate)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QWebEngineClientCertificateStore6removeERK15QSslCertificate(
    QWebEngineClientCertificateStore *self,
    const QSslCertificate *certificate) {
  self->remove(*certificate);
}

//  void QWebEngineClientCertificateStore::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QWebEngineClientCertificateStore5clearEv(
    QWebEngineClientCertificateStore *self) {
  self->clear();
}

//  QWebEngineClientCertificateStore::QWebEngineClientCertificateStore(QtWebE
//      ngineCore::ClientCertificateStoreData *storeData)
extern "C" Q_DECL_EXPORT
QWebEngineClientCertificateStore *ritual_ZN32QWebEngineClientCertificateStoreC1EPN15QtWebEngineCore26ClientCertificateStoreDataE(
    QtWebEngineCore::ClientCertificateStoreData *storeData) {
  return new QWebEngineClientCertificateStore(storeData);
}

//  QWebEngineClientCertificateStore::~QWebEngineClientCertificateStore()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QWebEngineClientCertificateStoreD1Ev(
    QWebEngineClientCertificateStore *self) {
  delete self;
}

#endif  // QT_CONFIG(ssl)
