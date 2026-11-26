//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcuax509certificatesigningrequest.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: the include of
//  <QtOpcUa/qtopcua-config.h> before the #if, as it defines
//  QT_CONFIG(gds); the long #if line split in two.
//  Kept as it is when the generator runs again.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtOpcUa/qopcuaglobal.h>
#include <QtOpcUa/qtopcua-config.h>
#if QT_CONFIG(gds) && QT_CONFIG(openssl) \
    && !defined(Q_OS_DARWIN) && !defined(Q_OS_WINRT)
#include <QtOpcUa/QtOpcUa>
#include <QtOpcUa/qopcuax509certificatesigningrequest.h>
#include <QtOpcUa/qopcuax509distinguishedname.h>
#include <QtCore/qbytearray.h>

//  QOpcUaX509CertificateSigningRequestPrivate
//      *QOpcUaX509CertificateSigningRequest::d_func()
extern "C" Q_DECL_EXPORT
QOpcUaX509CertificateSigningRequestPrivate *ritual_ZN35QOpcUaX509CertificateSigningRequest6d_funcEv(
    QOpcUaX509CertificateSigningRequest *self) {
  return self->d_func();
}

//  const QOpcUaX509CertificateSigningRequestPrivate
//      *QOpcUaX509CertificateSigningRequest::d_func() const
extern "C" Q_DECL_EXPORT
const QOpcUaX509CertificateSigningRequestPrivate *ritual_ZNK35QOpcUaX509CertificateSigningRequest6d_funcEv(
    const QOpcUaX509CertificateSigningRequest *self) {
  return self->d_func();
}

//  QOpcUaX509CertificateSigningRequest::QOpcUaX509CertificateSigningRequest(
//      )
extern "C" Q_DECL_EXPORT
QOpcUaX509CertificateSigningRequest *ritual_ZN35QOpcUaX509CertificateSigningRequestC1Ev() {
  return new QOpcUaX509CertificateSigningRequest();
}

//  QOpcUaX509CertificateSigningRequest::~QOpcUaX509CertificateSigningRequest
//      ()
extern "C" Q_DECL_EXPORT
void ritual_ZN35QOpcUaX509CertificateSigningRequestD1Ev(
    QOpcUaX509CertificateSigningRequest *self) {
  delete self;
}

//  void QOpcUaX509CertificateSigningRequest::setMessageDigest(MessageDigest
//      digest)
extern "C" Q_DECL_EXPORT
void ritual_ZN35QOpcUaX509CertificateSigningRequest16setMessageDigestENS_13MessageDigestE(
    QOpcUaX509CertificateSigningRequest *self,
    QOpcUaX509CertificateSigningRequest::MessageDigest digest) {
  self->setMessageDigest(digest);
}

//  MessageDigest QOpcUaX509CertificateSigningRequest::messageDigest() const
extern "C" Q_DECL_EXPORT
QOpcUaX509CertificateSigningRequest::MessageDigest ritual_ZNK35QOpcUaX509CertificateSigningRequest13messageDigestEv(
    const QOpcUaX509CertificateSigningRequest *self) {
  return self->messageDigest();
}

//  void QOpcUaX509CertificateSigningRequest::setEncoding(Encoding encoding)
extern "C" Q_DECL_EXPORT
void ritual_ZN35QOpcUaX509CertificateSigningRequest11setEncodingENS_8EncodingE(
    QOpcUaX509CertificateSigningRequest *self,
    QOpcUaX509CertificateSigningRequest::Encoding encoding) {
  self->setEncoding(encoding);
}

//  Encoding QOpcUaX509CertificateSigningRequest::encoding() const
extern "C" Q_DECL_EXPORT
QOpcUaX509CertificateSigningRequest::Encoding ritual_ZNK35QOpcUaX509CertificateSigningRequest8encodingEv(
    const QOpcUaX509CertificateSigningRequest *self) {
  return self->encoding();
}

//  void QOpcUaX509CertificateSigningRequest::setSubject(const
//      QOpcUaX509DistinguishedName &subject)
extern "C" Q_DECL_EXPORT
void ritual_ZN35QOpcUaX509CertificateSigningRequest10setSubjectERK27QOpcUaX509DistinguishedName(
    QOpcUaX509CertificateSigningRequest *self,
    const QOpcUaX509DistinguishedName *subject) {
  self->setSubject(*subject);
}

//  const QOpcUaX509DistinguishedName
//      &QOpcUaX509CertificateSigningRequest::subject() const
extern "C" Q_DECL_EXPORT
QOpcUaX509DistinguishedName *ritual_ZNK35QOpcUaX509CertificateSigningRequest7subjectEv(
    const QOpcUaX509CertificateSigningRequest *self) {
  return new QOpcUaX509DistinguishedName(self->subject());
}

//  void
//      QOpcUaX509CertificateSigningRequest::addExtension(QOpcUaX509Extension
//      *extension)
extern "C" Q_DECL_EXPORT
void ritual_ZN35QOpcUaX509CertificateSigningRequest12addExtensionEP19QOpcUaX509Extension(
    QOpcUaX509CertificateSigningRequest *self,
    QOpcUaX509Extension *extension) {
  self->addExtension(extension);
}

//  QByteArray QOpcUaX509CertificateSigningRequest::createRequest(const
//      QOpcUaKeyPair &privateKey)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN35QOpcUaX509CertificateSigningRequest13createRequestERK13QOpcUaKeyPair(
    QOpcUaX509CertificateSigningRequest *self,
    const QOpcUaKeyPair *privateKey) {
  return new QByteArray(self->createRequest(*privateKey));
}

//  QByteArray
//      QOpcUaX509CertificateSigningRequest::createSelfSignedCertificate(cons
//      t QOpcUaKeyPair &privateKey, int validityInDays)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN35QOpcUaX509CertificateSigningRequest27createSelfSignedCertificateERK13QOpcUaKeyPairi(
    QOpcUaX509CertificateSigningRequest *self,
    const QOpcUaKeyPair *privateKey,
    int validityInDays) {
  return new QByteArray(
      self->createSelfSignedCertificate(
          *privateKey,
          validityInDays));
}

#endif  // QT_CONFIG(gds) && QT_CONFIG(openssl) && !defined(Q_OS_DARWIN) && !defined(Q_OS_WINRT)
