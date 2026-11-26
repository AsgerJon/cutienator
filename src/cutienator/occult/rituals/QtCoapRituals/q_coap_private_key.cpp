//  Written by dev_tooling.RitualGenerator from the records of
//  QtCoap/qcoapsecurityconfiguration.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtCoap/qcoapsecurityconfiguration.h>
#include <QtCore/qbytearray.h>

//  QCoapPrivateKey::QCoapPrivateKey()
extern "C" Q_DECL_EXPORT
QCoapPrivateKey *ritual_ZN15QCoapPrivateKeyC1Ev() {
  return new QCoapPrivateKey();
}

//  QCoapPrivateKey::QCoapPrivateKey(const QByteArray &key,
//      QSsl::KeyAlgorithm algorithm, QSsl::EncodingFormat format, const
//      QByteArray &passPhrase)
extern "C" Q_DECL_EXPORT
QCoapPrivateKey *ritual_ZN15QCoapPrivateKeyC1ERK10QByteArrayN4QSsl12KeyAlgorithmENS3_14EncodingFormatES2_(
    const QByteArray *key,
    QSsl::KeyAlgorithm algorithm,
    QSsl::EncodingFormat format,
    const QByteArray *passPhrase) {
  return new QCoapPrivateKey(*key, algorithm, format, *passPhrase);
}

//  QCoapPrivateKey::QCoapPrivateKey(const Qt::HANDLE &handle)
extern "C" Q_DECL_EXPORT
QCoapPrivateKey *ritual_ZN15QCoapPrivateKeyC1ERKPv(
    const Qt::HANDLE *handle) {
  return new QCoapPrivateKey(*handle);
}

//  QCoapPrivateKey::QCoapPrivateKey(const QCoapPrivateKey &other)
extern "C" Q_DECL_EXPORT
QCoapPrivateKey *ritual_ZN15QCoapPrivateKeyC1ERKS_(
    const QCoapPrivateKey *other) {
  return new QCoapPrivateKey(*other);
}

//  QCoapPrivateKey::QCoapPrivateKey(QCoapPrivateKey &&other)
extern "C" Q_DECL_EXPORT
QCoapPrivateKey *ritual_ZN15QCoapPrivateKeyC1EOS_(QCoapPrivateKey *other) {
  return new QCoapPrivateKey(std::move(*other));
}

//  QCoapPrivateKey::~QCoapPrivateKey()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCoapPrivateKeyD1Ev(QCoapPrivateKey *self) {
  delete self;
}

//  QCoapPrivateKey &QCoapPrivateKey::operator=(QCoapPrivateKey &&other)
extern "C" Q_DECL_EXPORT
QCoapPrivateKey *ritual_ZN15QCoapPrivateKeyaSEOS_(
    QCoapPrivateKey *self,
    QCoapPrivateKey *other) {
  return &(self->operator=(std::move(*other)));
}

//  QCoapPrivateKey &QCoapPrivateKey::operator=(const QCoapPrivateKey &other)
extern "C" Q_DECL_EXPORT
QCoapPrivateKey *ritual_ZN15QCoapPrivateKeyaSERKS_(
    QCoapPrivateKey *self,
    const QCoapPrivateKey *other) {
  return &(self->operator=(*other));
}

//  void QCoapPrivateKey::swap(QCoapPrivateKey &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCoapPrivateKey4swapERS_(
    QCoapPrivateKey *self,
    QCoapPrivateKey *other) {
  self->swap(*other);
}

//  bool QCoapPrivateKey::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QCoapPrivateKey6isNullEv(const QCoapPrivateKey *self) {
  return self->isNull();
}

//  QByteArray QCoapPrivateKey::key() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK15QCoapPrivateKey3keyEv(const QCoapPrivateKey *self) {
  return new QByteArray(self->key());
}

//  Qt::HANDLE QCoapPrivateKey::handle() const
extern "C" Q_DECL_EXPORT
Qt::HANDLE ritual_ZNK15QCoapPrivateKey6handleEv(
    const QCoapPrivateKey *self) {
  return self->handle();
}

//  QSsl::KeyAlgorithm QCoapPrivateKey::algorithm() const
extern "C" Q_DECL_EXPORT
QSsl::KeyAlgorithm ritual_ZNK15QCoapPrivateKey9algorithmEv(
    const QCoapPrivateKey *self) {
  return self->algorithm();
}

//  QSsl::EncodingFormat QCoapPrivateKey::encodingFormat() const
extern "C" Q_DECL_EXPORT
QSsl::EncodingFormat ritual_ZNK15QCoapPrivateKey14encodingFormatEv(
    const QCoapPrivateKey *self) {
  return self->encodingFormat();
}

//  QByteArray QCoapPrivateKey::passPhrase() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK15QCoapPrivateKey10passPhraseEv(
    const QCoapPrivateKey *self) {
  return new QByteArray(self->passPhrase());
}
