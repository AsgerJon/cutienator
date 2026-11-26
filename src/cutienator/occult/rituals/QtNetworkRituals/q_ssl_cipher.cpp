//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/qsslcipher.h, Qt 6.12.0. Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#if !defined(QT_NO_SSL)
#include <QtNetwork/qsslcipher.h>
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  QSslCipher::QSslCipher()
extern "C" Q_DECL_EXPORT
QSslCipher *ritual_ZN10QSslCipherC1Ev() {
  return new QSslCipher();
}

//  QSslCipher::QSslCipher(const QString &name)
extern "C" Q_DECL_EXPORT
QSslCipher *ritual_ZN10QSslCipherC1ERK7QString(const QString *name) {
  return new QSslCipher(*name);
}

//  QSslCipher::QSslCipher(const QString &name, QSsl::SslProtocol protocol)
extern "C" Q_DECL_EXPORT
QSslCipher *ritual_ZN10QSslCipherC1ERK7QStringN4QSsl11SslProtocolE(
    const QString *name,
    QSsl::SslProtocol protocol) {
  return new QSslCipher(*name, protocol);
}

//  QSslCipher::QSslCipher(const QSslCipher &other)
extern "C" Q_DECL_EXPORT
QSslCipher *ritual_ZN10QSslCipherC1ERKS_(const QSslCipher *other) {
  return new QSslCipher(*other);
}

//  QSslCipher &QSslCipher::operator=(QSslCipher &&other)
extern "C" Q_DECL_EXPORT
QSslCipher *ritual_ZN10QSslCipheraSEOS_(
    QSslCipher *self,
    QSslCipher *other) {
  return &(self->operator=(std::move(*other)));
}

//  QSslCipher &QSslCipher::operator=(const QSslCipher &other)
extern "C" Q_DECL_EXPORT
QSslCipher *ritual_ZN10QSslCipheraSERKS_(
    QSslCipher *self,
    const QSslCipher *other) {
  return &(self->operator=(*other));
}

//  QSslCipher::~QSslCipher()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSslCipherD1Ev(QSslCipher *self) {
  delete self;
}

//  void QSslCipher::swap(QSslCipher &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSslCipher4swapERS_(QSslCipher *self, QSslCipher *other) {
  self->swap(*other);
}

//  bool QSslCipher::operator==(const QSslCipher &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QSslCiphereqERKS_(
    const QSslCipher *self,
    const QSslCipher *other) {
  return self->operator==(*other);
}

//  bool QSslCipher::operator!=(const QSslCipher &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QSslCipherneERKS_(
    const QSslCipher *self,
    const QSslCipher *other) {
  return self->operator!=(*other);
}

//  bool QSslCipher::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QSslCipher6isNullEv(const QSslCipher *self) {
  return self->isNull();
}

//  QString QSslCipher::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QSslCipher4nameEv(const QSslCipher *self) {
  return new QString(self->name());
}

//  int QSslCipher::supportedBits() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QSslCipher13supportedBitsEv(const QSslCipher *self) {
  return self->supportedBits();
}

//  int QSslCipher::usedBits() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QSslCipher8usedBitsEv(const QSslCipher *self) {
  return self->usedBits();
}

//  QString QSslCipher::keyExchangeMethod() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QSslCipher17keyExchangeMethodEv(
    const QSslCipher *self) {
  return new QString(self->keyExchangeMethod());
}

//  QString QSslCipher::authenticationMethod() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QSslCipher20authenticationMethodEv(
    const QSslCipher *self) {
  return new QString(self->authenticationMethod());
}

//  QString QSslCipher::encryptionMethod() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QSslCipher16encryptionMethodEv(const QSslCipher *self) {
  return new QString(self->encryptionMethod());
}

//  QString QSslCipher::protocolString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QSslCipher14protocolStringEv(const QSslCipher *self) {
  return new QString(self->protocolString());
}

//  QSsl::SslProtocol QSslCipher::protocol() const
extern "C" Q_DECL_EXPORT
QSsl::SslProtocol ritual_ZNK10QSslCipher8protocolEv(const QSslCipher *self) {
  return self->protocol();
}

//  QList<QSslCipher>::QList()
extern "C" Q_DECL_EXPORT
QList<QSslCipher> *ritual_list_make_QSslCipher() {
  return new QList<QSslCipher>();
}

//  void QList<QSslCipher>::append(const QSslCipher &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QSslCipher(
    QList<QSslCipher> *self,
    const QSslCipher *element) {
  self->append(*element);
}

//  qsizetype QList<QSslCipher>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QSslCipher(const QList<QSslCipher> *self) {
  return self->size();
}

//  const QSslCipher &QList<QSslCipher>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QSslCipher *ritual_list_at_QSslCipher(
    const QList<QSslCipher> *self,
    long long index) {
  return new QSslCipher(self->at(index));
}

//  QList<QSslCipher>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QSslCipher(QList<QSslCipher> *self) {
  delete self;
}

#endif  // !defined(QT_NO_SSL)
