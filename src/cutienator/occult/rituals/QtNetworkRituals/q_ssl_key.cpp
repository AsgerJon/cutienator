//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/qsslkey.h, Qt 6.12.0. Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#if !defined(QT_NO_SSL)
#include <QtNetwork/qsslkey.h>
#include <QtCore/qbytearray.h>

//  QSslKey::QSslKey()
extern "C" Q_DECL_EXPORT
QSslKey *ritual_ZN7QSslKeyC1Ev() {
  return new QSslKey();
}

//  QSslKey::QSslKey(const QByteArray &encoded, QSsl::KeyAlgorithm algorithm,
//      QSsl::EncodingFormat format, QSsl::KeyType type, const QByteArray
//      &passPhrase)
extern "C" Q_DECL_EXPORT
QSslKey *ritual_ZN7QSslKeyC1ERK10QByteArrayN4QSsl12KeyAlgorithmENS3_14EncodingFormatENS3_7KeyTypeES2_(
    const QByteArray *encoded,
    QSsl::KeyAlgorithm algorithm,
    QSsl::EncodingFormat format,
    QSsl::KeyType type,
    const QByteArray *passPhrase) {
  return new QSslKey(*encoded, algorithm, format, type, *passPhrase);
}

//  QSslKey::QSslKey(QIODevice *device, QSsl::KeyAlgorithm algorithm,
//      QSsl::EncodingFormat format, QSsl::KeyType type, const QByteArray
//      &passPhrase)
extern "C" Q_DECL_EXPORT
QSslKey *ritual_ZN7QSslKeyC1EP9QIODeviceN4QSsl12KeyAlgorithmENS2_14EncodingFormatENS2_7KeyTypeERK10QByteArray(
    QIODevice *device,
    QSsl::KeyAlgorithm algorithm,
    QSsl::EncodingFormat format,
    QSsl::KeyType type,
    const QByteArray *passPhrase) {
  return new QSslKey(device, algorithm, format, type, *passPhrase);
}

//  QSslKey::QSslKey(Qt::HANDLE handle, QSsl::KeyType type)
extern "C" Q_DECL_EXPORT
QSslKey *ritual_ZN7QSslKeyC1EPvN4QSsl7KeyTypeE(
    Qt::HANDLE handle,
    QSsl::KeyType type) {
  return new QSslKey(handle, type);
}

//  QSslKey::QSslKey(const QSslKey &other)
extern "C" Q_DECL_EXPORT
QSslKey *ritual_ZN7QSslKeyC1ERKS_(const QSslKey *other) {
  return new QSslKey(*other);
}

//  QSslKey::QSslKey(QSslKey &&other)
extern "C" Q_DECL_EXPORT
QSslKey *ritual_ZN7QSslKeyC1EOS_(QSslKey *other) {
  return new QSslKey(std::move(*other));
}

//  QSslKey &QSslKey::operator=(QSslKey &&other)
extern "C" Q_DECL_EXPORT
QSslKey *ritual_ZN7QSslKeyaSEOS_(QSslKey *self, QSslKey *other) {
  return &(self->operator=(std::move(*other)));
}

//  QSslKey &QSslKey::operator=(const QSslKey &other)
extern "C" Q_DECL_EXPORT
QSslKey *ritual_ZN7QSslKeyaSERKS_(QSslKey *self, const QSslKey *other) {
  return &(self->operator=(*other));
}

//  QSslKey::~QSslKey()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QSslKeyD1Ev(QSslKey *self) {
  delete self;
}

//  void QSslKey::swap(QSslKey &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QSslKey4swapERS_(QSslKey *self, QSslKey *other) {
  self->swap(*other);
}

//  bool QSslKey::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QSslKey6isNullEv(const QSslKey *self) {
  return self->isNull();
}

//  void QSslKey::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QSslKey5clearEv(QSslKey *self) {
  self->clear();
}

//  int QSslKey::length() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QSslKey6lengthEv(const QSslKey *self) {
  return self->length();
}

//  QSsl::KeyType QSslKey::type() const
extern "C" Q_DECL_EXPORT
QSsl::KeyType ritual_ZNK7QSslKey4typeEv(const QSslKey *self) {
  return self->type();
}

//  QSsl::KeyAlgorithm QSslKey::algorithm() const
extern "C" Q_DECL_EXPORT
QSsl::KeyAlgorithm ritual_ZNK7QSslKey9algorithmEv(const QSslKey *self) {
  return self->algorithm();
}

//  QByteArray QSslKey::toPem(const QByteArray &passPhrase) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK7QSslKey5toPemERK10QByteArray(
    const QSslKey *self,
    const QByteArray *passPhrase) {
  return new QByteArray(self->toPem(*passPhrase));
}

//  QByteArray QSslKey::toDer(const QByteArray &passPhrase) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK7QSslKey5toDerERK10QByteArray(
    const QSslKey *self,
    const QByteArray *passPhrase) {
  return new QByteArray(self->toDer(*passPhrase));
}

//  Qt::HANDLE QSslKey::handle() const
extern "C" Q_DECL_EXPORT
Qt::HANDLE ritual_ZNK7QSslKey6handleEv(const QSslKey *self) {
  return self->handle();
}

//  bool QSslKey::operator==(const QSslKey &key) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QSslKeyeqERKS_(const QSslKey *self, const QSslKey *key) {
  return self->operator==(*key);
}

//  bool QSslKey::operator!=(const QSslKey &key) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QSslKeyneERKS_(const QSslKey *self, const QSslKey *key) {
  return self->operator!=(*key);
}

#endif  // !defined(QT_NO_SSL)
