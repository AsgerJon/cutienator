//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/qsslcertificate.h, Qt 6.12.0. Changes made here are lost.
#include <QtNetwork/qsslcertificate.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qstring.h>
#include <QtCore/qdatetime.h>
#include <QtNetwork/qsslkey.h>
#include <QtNetwork/qsslcertificateextension.h>
#include <QtNetwork/qsslerror.h>
#include <QtCore/qlist.h>
#include <QtCore/QMultiMap>
#include <QtNetwork/QSsl>
#include <QtCore/QString>

//  QSslCertificate::QSslCertificate(QIODevice *device, QSsl::EncodingFormat
//      format)
extern "C" Q_DECL_EXPORT
QSslCertificate *ritual_ZN15QSslCertificateC1EP9QIODeviceN4QSsl14EncodingFormatE(
    QIODevice *device,
    QSsl::EncodingFormat format) {
  return new QSslCertificate(device, format);
}

//  QSslCertificate::QSslCertificate(const QByteArray &data,
//      QSsl::EncodingFormat format)
extern "C" Q_DECL_EXPORT
QSslCertificate *ritual_ZN15QSslCertificateC1ERK10QByteArrayN4QSsl14EncodingFormatE(
    const QByteArray *data,
    QSsl::EncodingFormat format) {
  return new QSslCertificate(*data, format);
}

//  QSslCertificate::QSslCertificate(const QSslCertificate &other)
extern "C" Q_DECL_EXPORT
QSslCertificate *ritual_ZN15QSslCertificateC1ERKS_(
    const QSslCertificate *other) {
  return new QSslCertificate(*other);
}

//  QSslCertificate::QSslCertificate(QSslCertificate &&other)
extern "C" Q_DECL_EXPORT
QSslCertificate *ritual_ZN15QSslCertificateC1EOS_(QSslCertificate *other) {
  return new QSslCertificate(std::move(*other));
}

//  QSslCertificate::~QSslCertificate()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSslCertificateD1Ev(QSslCertificate *self) {
  delete self;
}

//  QSslCertificate &QSslCertificate::operator=(QSslCertificate &&other)
extern "C" Q_DECL_EXPORT
QSslCertificate *ritual_ZN15QSslCertificateaSEOS_(
    QSslCertificate *self,
    QSslCertificate *other) {
  return &(self->operator=(std::move(*other)));
}

//  QSslCertificate &QSslCertificate::operator=(const QSslCertificate &other)
extern "C" Q_DECL_EXPORT
QSslCertificate *ritual_ZN15QSslCertificateaSERKS_(
    QSslCertificate *self,
    const QSslCertificate *other) {
  return &(self->operator=(*other));
}

//  void QSslCertificate::swap(QSslCertificate &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSslCertificate4swapERS_(
    QSslCertificate *self,
    QSslCertificate *other) {
  self->swap(*other);
}

//  bool QSslCertificate::operator==(const QSslCertificate &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QSslCertificateeqERKS_(
    const QSslCertificate *self,
    const QSslCertificate *other) {
  return self->operator==(*other);
}

//  bool QSslCertificate::operator!=(const QSslCertificate &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QSslCertificateneERKS_(
    const QSslCertificate *self,
    const QSslCertificate *other) {
  return self->operator!=(*other);
}

//  bool QSslCertificate::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QSslCertificate6isNullEv(const QSslCertificate *self) {
  return self->isNull();
}

//  bool QSslCertificate::isBlacklisted() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QSslCertificate13isBlacklistedEv(
    const QSslCertificate *self) {
  return self->isBlacklisted();
}

//  bool QSslCertificate::isSelfSigned() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QSslCertificate12isSelfSignedEv(
    const QSslCertificate *self) {
  return self->isSelfSigned();
}

//  void QSslCertificate::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSslCertificate5clearEv(QSslCertificate *self) {
  self->clear();
}

//  QByteArray QSslCertificate::version() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK15QSslCertificate7versionEv(
    const QSslCertificate *self) {
  return new QByteArray(self->version());
}

//  QByteArray QSslCertificate::serialNumber() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK15QSslCertificate12serialNumberEv(
    const QSslCertificate *self) {
  return new QByteArray(self->serialNumber());
}

//  QByteArray QSslCertificate::digest(QCryptographicHash::Algorithm
//      algorithm) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK15QSslCertificate6digestEN18QCryptographicHash9AlgorithmE(
    const QSslCertificate *self,
    QCryptographicHash::Algorithm algorithm) {
  return new QByteArray(self->digest(algorithm));
}

//  QStringList QSslCertificate::issuerInfo(SubjectInfo info) const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK15QSslCertificate10issuerInfoENS_11SubjectInfoE(
    const QSslCertificate *self,
    QSslCertificate::SubjectInfo info) {
  return new QList<QString>(self->issuerInfo(info));
}

//  QStringList QSslCertificate::issuerInfo(const QByteArray &attribute)
//      const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK15QSslCertificate10issuerInfoERK10QByteArray(
    const QSslCertificate *self,
    const QByteArray *attribute) {
  return new QList<QString>(self->issuerInfo(*attribute));
}

//  QStringList QSslCertificate::subjectInfo(SubjectInfo info) const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK15QSslCertificate11subjectInfoENS_11SubjectInfoE(
    const QSslCertificate *self,
    QSslCertificate::SubjectInfo info) {
  return new QList<QString>(self->subjectInfo(info));
}

//  QStringList QSslCertificate::subjectInfo(const QByteArray &attribute)
//      const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK15QSslCertificate11subjectInfoERK10QByteArray(
    const QSslCertificate *self,
    const QByteArray *attribute) {
  return new QList<QString>(self->subjectInfo(*attribute));
}

//  QString QSslCertificate::issuerDisplayName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QSslCertificate17issuerDisplayNameEv(
    const QSslCertificate *self) {
  return new QString(self->issuerDisplayName());
}

//  QString QSslCertificate::subjectDisplayName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QSslCertificate18subjectDisplayNameEv(
    const QSslCertificate *self) {
  return new QString(self->subjectDisplayName());
}

//  QList<QByteArray> QSslCertificate::subjectInfoAttributes() const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK15QSslCertificate21subjectInfoAttributesEv(
    const QSslCertificate *self) {
  return new QList<QByteArray>(self->subjectInfoAttributes());
}

//  QList<QByteArray> QSslCertificate::issuerInfoAttributes() const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK15QSslCertificate20issuerInfoAttributesEv(
    const QSslCertificate *self) {
  return new QList<QByteArray>(self->issuerInfoAttributes());
}

//  QMultiMap<QSsl::AlternativeNameEntryType, QString>
//      QSslCertificate::subjectAlternativeNames() const
extern "C" Q_DECL_EXPORT
QMultiMap<QSsl::AlternativeNameEntryType, QString> *ritual_ZNK15QSslCertificate23subjectAlternativeNamesEv(
    const QSslCertificate *self) {
  return new QMultiMap<QSsl::AlternativeNameEntryType, QString>(
      self->subjectAlternativeNames());
}

//  QDateTime QSslCertificate::effectiveDate() const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK15QSslCertificate13effectiveDateEv(
    const QSslCertificate *self) {
  return new QDateTime(self->effectiveDate());
}

//  QDateTime QSslCertificate::expiryDate() const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK15QSslCertificate10expiryDateEv(
    const QSslCertificate *self) {
  return new QDateTime(self->expiryDate());
}

#if !defined(QT_NO_SSL)
//  QSslKey QSslCertificate::publicKey() const
extern "C" Q_DECL_EXPORT
QSslKey *ritual_ZNK15QSslCertificate9publicKeyEv(
    const QSslCertificate *self) {
  return new QSslKey(self->publicKey());
}
#endif  // !defined(QT_NO_SSL)

//  QList<QSslCertificateExtension> QSslCertificate::extensions() const
extern "C" Q_DECL_EXPORT
QList<QSslCertificateExtension> *ritual_ZNK15QSslCertificate10extensionsEv(
    const QSslCertificate *self) {
  return new QList<QSslCertificateExtension>(self->extensions());
}

//  QByteArray QSslCertificate::toPem() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK15QSslCertificate5toPemEv(
    const QSslCertificate *self) {
  return new QByteArray(self->toPem());
}

//  QByteArray QSslCertificate::toDer() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK15QSslCertificate5toDerEv(
    const QSslCertificate *self) {
  return new QByteArray(self->toDer());
}

//  QString QSslCertificate::toText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QSslCertificate6toTextEv(const QSslCertificate *self) {
  return new QString(self->toText());
}

//  QList<QSslCertificate> QSslCertificate::fromPath(const QString &path,
//      QSsl::EncodingFormat format, PatternSyntax syntax)
extern "C" Q_DECL_EXPORT
QList<QSslCertificate> *ritual_ZN15QSslCertificate8fromPathERK7QStringN4QSsl14EncodingFormatENS_13PatternSyntaxE(
    const QString *path,
    QSsl::EncodingFormat format,
    QSslCertificate::PatternSyntax syntax) {
  return new QList<QSslCertificate>(
      QSslCertificate::fromPath(
          *path,
          format,
          syntax));
}

//  QList<QSslCertificate> QSslCertificate::fromDevice(QIODevice *device,
//      QSsl::EncodingFormat format)
extern "C" Q_DECL_EXPORT
QList<QSslCertificate> *ritual_ZN15QSslCertificate10fromDeviceEP9QIODeviceN4QSsl14EncodingFormatE(
    QIODevice *device,
    QSsl::EncodingFormat format) {
  return new QList<QSslCertificate>(
      QSslCertificate::fromDevice(
          device,
          format));
}

//  QList<QSslCertificate> QSslCertificate::fromData(const QByteArray &data,
//      QSsl::EncodingFormat format)
extern "C" Q_DECL_EXPORT
QList<QSslCertificate> *ritual_ZN15QSslCertificate8fromDataERK10QByteArrayN4QSsl14EncodingFormatE(
    const QByteArray *data,
    QSsl::EncodingFormat format) {
  return new QList<QSslCertificate>(
      QSslCertificate::fromData(
          *data,
          format));
}

//  QList<QSslCertificate> QSslCertificate::fromFile(const QString &filePath,
//      QSsl::EncodingFormat format)
extern "C" Q_DECL_EXPORT
QList<QSslCertificate> *ritual_ZN15QSslCertificate8fromFileERK7QStringN4QSsl14EncodingFormatE(
    const QString *filePath,
    QSsl::EncodingFormat format) {
  return new QList<QSslCertificate>(
      QSslCertificate::fromFile(
          *filePath,
          format));
}

#if !defined(QT_NO_SSL)
//  QList<QSslError> QSslCertificate::verify(const QList<QSslCertificate>
//      &certificateChain, const QString &hostName)
extern "C" Q_DECL_EXPORT
QList<QSslError> *ritual_ZN15QSslCertificate6verifyERK5QListIS_ERK7QString(
    const QList<QSslCertificate> *certificateChain,
    const QString *hostName) {
  return new QList<QSslError>(
      QSslCertificate::verify(
          *certificateChain,
          *hostName));
}
#endif  // !defined(QT_NO_SSL)

#if !defined(QT_NO_SSL)
//  bool QSslCertificate::importPkcs12(QIODevice *device, QSslKey *key,
//      QSslCertificate *cert, QList<QSslCertificate> *caCertificates, const
//      QByteArray &passPhrase)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QSslCertificate12importPkcs12EP9QIODeviceP7QSslKeyPS_P5QListIS_ERK10QByteArray(
    QIODevice *device,
    QSslKey *key,
    QSslCertificate *cert,
    QList<QSslCertificate> *caCertificates,
    const QByteArray *passPhrase) {
  return QSslCertificate::importPkcs12(
      device,
      key,
      cert,
      caCertificates,
      *passPhrase);
}
#endif  // !defined(QT_NO_SSL)

//  Qt::HANDLE QSslCertificate::handle() const
extern "C" Q_DECL_EXPORT
Qt::HANDLE ritual_ZNK15QSslCertificate6handleEv(
    const QSslCertificate *self) {
  return self->handle();
}

//  QList<QSslCertificate>::QList()
extern "C" Q_DECL_EXPORT
QList<QSslCertificate> *ritual_list_make_QSslCertificate() {
  return new QList<QSslCertificate>();
}

//  void QList<QSslCertificate>::append(const QSslCertificate &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QSslCertificate(
    QList<QSslCertificate> *self,
    const QSslCertificate *element) {
  self->append(*element);
}

//  qsizetype QList<QSslCertificate>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QSslCertificate(
    const QList<QSslCertificate> *self) {
  return self->size();
}

//  const QSslCertificate &QList<QSslCertificate>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QSslCertificate *ritual_list_at_QSslCertificate(
    const QList<QSslCertificate> *self,
    long long index) {
  return new QSslCertificate(self->at(index));
}

//  QList<QSslCertificate>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QSslCertificate(QList<QSslCertificate> *self) {
  delete self;
}

//  a QMultiMap<QSsl::AlternativeNameEntryType, QString> a ritual of
//      QSslCertificate gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QSslCertificate__QMultiMap_QSsl_AlternativeNameEntryType_QString(
    QMultiMap<QSsl::AlternativeNameEntryType, QString> *self) {
  delete self;
}
