//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebEngineCore/qwebenginecertificateerror.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtWebEngineCore/qwebenginecertificateerror.h>
#include <QtCore/qurl.h>
#include <QtCore/qstring.h>
#include <QtNetwork/qsslcertificate.h>
#include <QtCore/qlist.h>

//  QWebEngineCertificateError::QWebEngineCertificateError()
extern "C" Q_DECL_EXPORT
QWebEngineCertificateError *ritual_ZN26QWebEngineCertificateErrorC1Ev() {
  return new QWebEngineCertificateError();
}

//  QWebEngineCertificateError::QWebEngineCertificateError(const
//      QWebEngineCertificateError &other)
extern "C" Q_DECL_EXPORT
QWebEngineCertificateError *ritual_ZN26QWebEngineCertificateErrorC1ERKS_(
    const QWebEngineCertificateError *other) {
  return new QWebEngineCertificateError(*other);
}

//  QWebEngineCertificateError &QWebEngineCertificateError::operator=(const
//      QWebEngineCertificateError &other)
extern "C" Q_DECL_EXPORT
QWebEngineCertificateError *ritual_ZN26QWebEngineCertificateErroraSERKS_(
    QWebEngineCertificateError *self,
    const QWebEngineCertificateError *other) {
  return &(self->operator=(*other));
}

//  QWebEngineCertificateError::~QWebEngineCertificateError()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QWebEngineCertificateErrorD1Ev(
    QWebEngineCertificateError *self) {
  delete self;
}

//  Type QWebEngineCertificateError::type() const
extern "C" Q_DECL_EXPORT
QWebEngineCertificateError::Type ritual_ZNK26QWebEngineCertificateError4typeEv(
    const QWebEngineCertificateError *self) {
  return self->type();
}

//  QUrl QWebEngineCertificateError::url() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK26QWebEngineCertificateError3urlEv(
    const QWebEngineCertificateError *self) {
  return new QUrl(self->url());
}

//  bool QWebEngineCertificateError::isOverridable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QWebEngineCertificateError13isOverridableEv(
    const QWebEngineCertificateError *self) {
  return self->isOverridable();
}

//  QString QWebEngineCertificateError::description() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QWebEngineCertificateError11descriptionEv(
    const QWebEngineCertificateError *self) {
  return new QString(self->description());
}

//  bool QWebEngineCertificateError::isMainFrame() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QWebEngineCertificateError11isMainFrameEv(
    const QWebEngineCertificateError *self) {
  return self->isMainFrame();
}

//  void QWebEngineCertificateError::defer()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QWebEngineCertificateError5deferEv(
    QWebEngineCertificateError *self) {
  self->defer();
}

//  void QWebEngineCertificateError::rejectCertificate()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QWebEngineCertificateError17rejectCertificateEv(
    QWebEngineCertificateError *self) {
  self->rejectCertificate();
}

//  void QWebEngineCertificateError::acceptCertificate()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QWebEngineCertificateError17acceptCertificateEv(
    QWebEngineCertificateError *self) {
  self->acceptCertificate();
}

//  QList<QSslCertificate> QWebEngineCertificateError::certificateChain()
//      const
extern "C" Q_DECL_EXPORT
QList<QSslCertificate> *ritual_ZNK26QWebEngineCertificateError16certificateChainEv(
    const QWebEngineCertificateError *self) {
  return new QList<QSslCertificate>(self->certificateChain());
}

//  QWebEngineCertificateError::QWebEngineCertificateError(const
//      QSharedPointer<QtWebEngineCore::CertificateErrorController>
//      &controller)
extern "C" Q_DECL_EXPORT
QWebEngineCertificateError *ritual_ZN26QWebEngineCertificateErrorC1ERK14QSharedPointerIN15QtWebEngineCore26CertificateErrorControllerEE(
    const QSharedPointer<QtWebEngineCore::CertificateErrorController> *controller) {
  return new QWebEngineCertificateError(*controller);
}
