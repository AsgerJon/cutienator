//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qmessageauthenticationcode.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtCore/qmessageauthenticationcode.h>
#include <QtCore/qbytearrayview.h>
#include <QtCore/qbytearray.h>
#include <QtCore/QByteArrayView>
#include <QtCore/QSpan>
#include <cstddef>

//  QMessageAuthenticationCode::QMessageAuthenticationCode(QCryptographicHash
//      ::Algorithm method, QByteArrayView key)
extern "C" Q_DECL_EXPORT
QMessageAuthenticationCode *ritual_ZN26QMessageAuthenticationCodeC1EN18QCryptographicHash9AlgorithmE14QByteArrayView(
    QCryptographicHash::Algorithm method,
    const QByteArrayView *key) {
  return new QMessageAuthenticationCode(method, *key);
}

//  QMessageAuthenticationCode::QMessageAuthenticationCode(QMessageAuthentica
//      tionCode &&other)
extern "C" Q_DECL_EXPORT
QMessageAuthenticationCode *ritual_ZN26QMessageAuthenticationCodeC1EOS_(
    QMessageAuthenticationCode *other) {
  return new QMessageAuthenticationCode(std::move(*other));
}

//  QMessageAuthenticationCode::~QMessageAuthenticationCode()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QMessageAuthenticationCodeD1Ev(
    QMessageAuthenticationCode *self) {
  delete self;
}

//  QMessageAuthenticationCode
//      &QMessageAuthenticationCode::operator=(QMessageAuthenticationCode
//      &&other)
extern "C" Q_DECL_EXPORT
QMessageAuthenticationCode *ritual_ZN26QMessageAuthenticationCodeaSEOS_(
    QMessageAuthenticationCode *self,
    QMessageAuthenticationCode *other) {
  return &(self->operator=(std::move(*other)));
}

//  void QMessageAuthenticationCode::swap(QMessageAuthenticationCode &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QMessageAuthenticationCode4swapERS_(
    QMessageAuthenticationCode *self,
    QMessageAuthenticationCode *other) {
  self->swap(*other);
}

//  void QMessageAuthenticationCode::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QMessageAuthenticationCode5resetEv(
    QMessageAuthenticationCode *self) {
  self->reset();
}

//  void QMessageAuthenticationCode::setKey(QByteArrayView key)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QMessageAuthenticationCode6setKeyE14QByteArrayView(
    QMessageAuthenticationCode *self,
    const QByteArrayView *key) {
  self->setKey(*key);
}

//  void QMessageAuthenticationCode::addData(const char *data, qsizetype
//      length)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QMessageAuthenticationCode7addDataEPKcx(
    QMessageAuthenticationCode *self,
    const char *data,
    qsizetype length) {
  self->addData(data, length);
}

//  void QMessageAuthenticationCode::addData(QByteArrayView data)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QMessageAuthenticationCode7addDataE14QByteArrayView(
    QMessageAuthenticationCode *self,
    const QByteArrayView *data) {
  self->addData(*data);
}

//  bool QMessageAuthenticationCode::addData(QIODevice *device)
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QMessageAuthenticationCode7addDataEP9QIODevice(
    QMessageAuthenticationCode *self,
    QIODevice *device) {
  return self->addData(device);
}

//  QByteArrayView QMessageAuthenticationCode::resultView() const
extern "C" Q_DECL_EXPORT
QByteArrayView *ritual_ZNK26QMessageAuthenticationCode10resultViewEv(
    const QMessageAuthenticationCode *self) {
  return new QByteArrayView(self->resultView());
}

//  QByteArray QMessageAuthenticationCode::result() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK26QMessageAuthenticationCode6resultEv(
    const QMessageAuthenticationCode *self) {
  return new QByteArray(self->result());
}

//  QByteArray QMessageAuthenticationCode::hash(QByteArrayView message,
//      QByteArrayView key, QCryptographicHash::Algorithm method)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN26QMessageAuthenticationCode4hashE14QByteArrayViewS0_N18QCryptographicHash9AlgorithmE(
    const QByteArrayView *message,
    const QByteArrayView *key,
    QCryptographicHash::Algorithm method) {
  return new QByteArray(
      QMessageAuthenticationCode::hash(
          *message,
          *key,
          method));
}

//  QByteArrayView QMessageAuthenticationCode::hashInto(QSpan<char> buffer,
//      QByteArrayView message, QByteArrayView key,
//      QCryptographicHash::Algorithm method)
extern "C" Q_DECL_EXPORT
QByteArrayView *ritual_ZN26QMessageAuthenticationCode8hashIntoE5QSpanIcLm18446744073709551615EE14QByteArrayViewS2_N18QCryptographicHash9AlgorithmE(
    const QSpan<char> *buffer,
    const QByteArrayView *message,
    const QByteArrayView *key,
    QCryptographicHash::Algorithm method) {
  return new QByteArrayView(
      QMessageAuthenticationCode::hashInto(
          *buffer,
          *message,
          *key,
          method));
}

//  QByteArrayView QMessageAuthenticationCode::hashInto(QSpan<uchar> buffer,
//      QByteArrayView message, QByteArrayView key,
//      QCryptographicHash::Algorithm method)
extern "C" Q_DECL_EXPORT
QByteArrayView *ritual_ZN26QMessageAuthenticationCode8hashIntoE5QSpanIhLm18446744073709551615EE14QByteArrayViewS2_N18QCryptographicHash9AlgorithmE(
    const QSpan<uchar> *buffer,
    const QByteArrayView *message,
    const QByteArrayView *key,
    QCryptographicHash::Algorithm method) {
  return new QByteArrayView(
      QMessageAuthenticationCode::hashInto(
          *buffer,
          *message,
          *key,
          method));
}

//  QByteArrayView QMessageAuthenticationCode::hashInto(QSpan<std::byte>
//      buffer, QByteArrayView message, QByteArrayView key,
//      QCryptographicHash::Algorithm method)
extern "C" Q_DECL_EXPORT
QByteArrayView *ritual_ZN26QMessageAuthenticationCode8hashIntoE5QSpanISt4byteLm18446744073709551615EE14QByteArrayViewS3_N18QCryptographicHash9AlgorithmE(
    const QSpan<std::byte> *buffer,
    const QByteArrayView *message,
    const QByteArrayView *key,
    QCryptographicHash::Algorithm method) {
  return new QByteArrayView(
      QMessageAuthenticationCode::hashInto(
          *buffer,
          *message,
          *key,
          method));
}

//  QByteArrayView QMessageAuthenticationCode::hashInto(QSpan<char> buffer,
//      QSpan<const QByteArrayView> messageParts, QByteArrayView key,
//      QCryptographicHash::Algorithm method)
extern "C" Q_DECL_EXPORT
QByteArrayView *ritual_ZN26QMessageAuthenticationCode8hashIntoE5QSpanIcLm18446744073709551615EES0_IK14QByteArrayViewLm18446744073709551615EES2_N18QCryptographicHash9AlgorithmE(
    const QSpan<char> *buffer,
    const QSpan<const QByteArrayView> *messageParts,
    const QByteArrayView *key,
    QCryptographicHash::Algorithm method) {
  return new QByteArrayView(
      QMessageAuthenticationCode::hashInto(
          *buffer,
          *messageParts,
          *key,
          method));
}

//  QByteArrayView QMessageAuthenticationCode::hashInto(QSpan<uchar> buffer,
//      QSpan<const QByteArrayView> messageParts, QByteArrayView key,
//      QCryptographicHash::Algorithm method)
extern "C" Q_DECL_EXPORT
QByteArrayView *ritual_ZN26QMessageAuthenticationCode8hashIntoE5QSpanIhLm18446744073709551615EES0_IK14QByteArrayViewLm18446744073709551615EES2_N18QCryptographicHash9AlgorithmE(
    const QSpan<uchar> *buffer,
    const QSpan<const QByteArrayView> *messageParts,
    const QByteArrayView *key,
    QCryptographicHash::Algorithm method) {
  return new QByteArrayView(
      QMessageAuthenticationCode::hashInto(
          *buffer,
          *messageParts,
          *key,
          method));
}

//  QByteArrayView QMessageAuthenticationCode::hashInto(QSpan<std::byte>
//      buffer, QSpan<const QByteArrayView> message, QByteArrayView key,
//      QCryptographicHash::Algorithm method)
extern "C" Q_DECL_EXPORT
QByteArrayView *ritual_ZN26QMessageAuthenticationCode8hashIntoE5QSpanISt4byteLm18446744073709551615EES0_IK14QByteArrayViewLm18446744073709551615EES3_N18QCryptographicHash9AlgorithmE(
    const QSpan<std::byte> *buffer,
    const QSpan<const QByteArrayView> *message,
    const QByteArrayView *key,
    QCryptographicHash::Algorithm method) {
  return new QByteArrayView(
      QMessageAuthenticationCode::hashInto(
          *buffer,
          *message,
          *key,
          method));
}
