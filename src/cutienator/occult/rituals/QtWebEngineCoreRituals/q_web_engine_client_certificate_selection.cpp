//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebEngineCore/qwebengineclientcertificateselection.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWebEngineCore/qwebengineclientcertificateselection.h>
#include <QtCore/qurl.h>
#include <QtNetwork/qsslcertificate.h>
#include <QtCore/qlist.h>
#include <QtCore/QSharedPointer>
#include <QtWebEngineCore/QtWebEngineCore>

//  QWebEngineClientCertificateSelection::QWebEngineClientCertificateSelectio
//      n(const QWebEngineClientCertificateSelection &a0)
extern "C" Q_DECL_EXPORT
QWebEngineClientCertificateSelection *ritual_ZN36QWebEngineClientCertificateSelectionC1ERKS_(
    const QWebEngineClientCertificateSelection *a0) {
  return new QWebEngineClientCertificateSelection(*a0);
}

//  QWebEngineClientCertificateSelection::~QWebEngineClientCertificateSelecti
//      on()
extern "C" Q_DECL_EXPORT
void ritual_ZN36QWebEngineClientCertificateSelectionD1Ev(
    QWebEngineClientCertificateSelection *self) {
  delete self;
}

//  QWebEngineClientCertificateSelection
//      &QWebEngineClientCertificateSelection::operator=(const
//      QWebEngineClientCertificateSelection &a0)
extern "C" Q_DECL_EXPORT
QWebEngineClientCertificateSelection *ritual_ZN36QWebEngineClientCertificateSelectionaSERKS_(
    QWebEngineClientCertificateSelection *self,
    const QWebEngineClientCertificateSelection *a0) {
  return &(self->operator=(*a0));
}

//  QUrl QWebEngineClientCertificateSelection::host() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK36QWebEngineClientCertificateSelection4hostEv(
    const QWebEngineClientCertificateSelection *self) {
  return new QUrl(self->host());
}

//  void QWebEngineClientCertificateSelection::select(const QSslCertificate
//      &certificate)
extern "C" Q_DECL_EXPORT
void ritual_ZN36QWebEngineClientCertificateSelection6selectERK15QSslCertificate(
    QWebEngineClientCertificateSelection *self,
    const QSslCertificate *certificate) {
  self->select(*certificate);
}

//  void QWebEngineClientCertificateSelection::selectNone()
extern "C" Q_DECL_EXPORT
void ritual_ZN36QWebEngineClientCertificateSelection10selectNoneEv(
    QWebEngineClientCertificateSelection *self) {
  self->selectNone();
}

//  QList<QSslCertificate>
//      QWebEngineClientCertificateSelection::certificates() const
extern "C" Q_DECL_EXPORT
QList<QSslCertificate> *ritual_ZNK36QWebEngineClientCertificateSelection12certificatesEv(
    const QWebEngineClientCertificateSelection *self) {
  return new QList<QSslCertificate>(self->certificates());
}

//  QWebEngineClientCertificateSelection::QWebEngineClientCertificateSelectio
//      n(QSharedPointer<QtWebEngineCore::ClientCertSelectController> a0)
extern "C" Q_DECL_EXPORT
QWebEngineClientCertificateSelection *ritual_ZN36QWebEngineClientCertificateSelectionC1E14QSharedPointerIN15QtWebEngineCore26ClientCertSelectControllerEE(
    const QSharedPointer<QtWebEngineCore::ClientCertSelectController> *a0) {
  return new QWebEngineClientCertificateSelection(*a0);
}
