//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qcryptographichash.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qcryptographichash.h>
#include <QtCore/qbytearrayview.h>
#include <QtCore/qbytearray.h>
#include <QtCore/QByteArrayView>
#include <QtCore/QSpan>
#include <cstddef>

//  QCryptographicHash::QCryptographicHash(Algorithm method)
extern "C" Q_DECL_EXPORT
QCryptographicHash *ritual_ZN18QCryptographicHashC1ENS_9AlgorithmE(
    QCryptographicHash::Algorithm method) {
  return new QCryptographicHash(method);
}

//  QCryptographicHash::QCryptographicHash(QCryptographicHash &&other)
extern "C" Q_DECL_EXPORT
QCryptographicHash *ritual_ZN18QCryptographicHashC1EOS_(
    QCryptographicHash *other) {
  return new QCryptographicHash(std::move(*other));
}

//  QCryptographicHash::~QCryptographicHash()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCryptographicHashD1Ev(QCryptographicHash *self) {
  delete self;
}

//  QCryptographicHash &QCryptographicHash::operator=(QCryptographicHash
//      &&other)
extern "C" Q_DECL_EXPORT
QCryptographicHash *ritual_ZN18QCryptographicHashaSEOS_(
    QCryptographicHash *self,
    QCryptographicHash *other) {
  return &(self->operator=(std::move(*other)));
}

//  void QCryptographicHash::swap(QCryptographicHash &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCryptographicHash4swapERS_(
    QCryptographicHash *self,
    QCryptographicHash *other) {
  self->swap(*other);
}

//  void QCryptographicHash::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCryptographicHash5resetEv(QCryptographicHash *self) {
  self->reset();
}

//  Algorithm QCryptographicHash::algorithm() const
extern "C" Q_DECL_EXPORT
QCryptographicHash::Algorithm ritual_ZNK18QCryptographicHash9algorithmEv(
    const QCryptographicHash *self) {
  return self->algorithm();
}

#if QT_DEPRECATED_SINCE(6, 4)
//  void QCryptographicHash::addData(const char *data, qsizetype length)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCryptographicHash7addDataEPKcx(
    QCryptographicHash *self,
    const char *data,
    qsizetype length) {
  self->addData(data, length);
}
#endif  // QT_DEPRECATED_SINCE(6, 4)

//  void QCryptographicHash::addData(QByteArrayView data)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCryptographicHash7addDataE14QByteArrayView(
    QCryptographicHash *self,
    const QByteArrayView *data) {
  self->addData(*data);
}

//  bool QCryptographicHash::addData(QIODevice *device)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QCryptographicHash7addDataEP9QIODevice(
    QCryptographicHash *self,
    QIODevice *device) {
  return self->addData(device);
}

//  QByteArray QCryptographicHash::result() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK18QCryptographicHash6resultEv(
    const QCryptographicHash *self) {
  return new QByteArray(self->result());
}

//  QByteArrayView QCryptographicHash::resultView() const
extern "C" Q_DECL_EXPORT
QByteArrayView *ritual_ZNK18QCryptographicHash10resultViewEv(
    const QCryptographicHash *self) {
  return new QByteArrayView(self->resultView());
}

//  QByteArray QCryptographicHash::hash(QByteArrayView data, Algorithm
//      method)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN18QCryptographicHash4hashE14QByteArrayViewNS_9AlgorithmE(
    const QByteArrayView *data,
    QCryptographicHash::Algorithm method) {
  return new QByteArray(QCryptographicHash::hash(*data, method));
}

//  QByteArrayView QCryptographicHash::hashInto(QSpan<char> buffer,
//      QByteArrayView data, Algorithm method)
extern "C" Q_DECL_EXPORT
QByteArrayView *ritual_ZN18QCryptographicHash8hashIntoE5QSpanIcLm18446744073709551615EE14QByteArrayViewNS_9AlgorithmE(
    const QSpan<char> *buffer,
    const QByteArrayView *data,
    QCryptographicHash::Algorithm method) {
  return new QByteArrayView(
      QCryptographicHash::hashInto(
          *buffer,
          *data,
          method));
}

//  QByteArrayView QCryptographicHash::hashInto(QSpan<uchar> buffer,
//      QByteArrayView data, Algorithm method)
extern "C" Q_DECL_EXPORT
QByteArrayView *ritual_ZN18QCryptographicHash8hashIntoE5QSpanIhLm18446744073709551615EE14QByteArrayViewNS_9AlgorithmE(
    const QSpan<uchar> *buffer,
    const QByteArrayView *data,
    QCryptographicHash::Algorithm method) {
  return new QByteArrayView(
      QCryptographicHash::hashInto(
          *buffer,
          *data,
          method));
}

//  QByteArrayView QCryptographicHash::hashInto(QSpan<std::byte> buffer,
//      QByteArrayView data, Algorithm method)
extern "C" Q_DECL_EXPORT
QByteArrayView *ritual_ZN18QCryptographicHash8hashIntoE5QSpanISt4byteLm18446744073709551615EE14QByteArrayViewNS_9AlgorithmE(
    const QSpan<std::byte> *buffer,
    const QByteArrayView *data,
    QCryptographicHash::Algorithm method) {
  return new QByteArrayView(
      QCryptographicHash::hashInto(
          *buffer,
          *data,
          method));
}

//  QByteArrayView QCryptographicHash::hashInto(QSpan<char> buffer,
//      QSpan<const QByteArrayView> data, Algorithm method)
extern "C" Q_DECL_EXPORT
QByteArrayView *ritual_ZN18QCryptographicHash8hashIntoE5QSpanIcLm18446744073709551615EES0_IK14QByteArrayViewLm18446744073709551615EENS_9AlgorithmE(
    const QSpan<char> *buffer,
    const QSpan<const QByteArrayView> *data,
    QCryptographicHash::Algorithm method) {
  return new QByteArrayView(
      QCryptographicHash::hashInto(
          *buffer,
          *data,
          method));
}

//  QByteArrayView QCryptographicHash::hashInto(QSpan<uchar> buffer,
//      QSpan<const QByteArrayView> data, Algorithm method)
extern "C" Q_DECL_EXPORT
QByteArrayView *ritual_ZN18QCryptographicHash8hashIntoE5QSpanIhLm18446744073709551615EES0_IK14QByteArrayViewLm18446744073709551615EENS_9AlgorithmE(
    const QSpan<uchar> *buffer,
    const QSpan<const QByteArrayView> *data,
    QCryptographicHash::Algorithm method) {
  return new QByteArrayView(
      QCryptographicHash::hashInto(
          *buffer,
          *data,
          method));
}

//  QByteArrayView QCryptographicHash::hashInto(QSpan<std::byte> buffer,
//      QSpan<const QByteArrayView> data, Algorithm method)
extern "C" Q_DECL_EXPORT
QByteArrayView *ritual_ZN18QCryptographicHash8hashIntoE5QSpanISt4byteLm18446744073709551615EES0_IK14QByteArrayViewLm18446744073709551615EENS_9AlgorithmE(
    const QSpan<std::byte> *buffer,
    const QSpan<const QByteArrayView> *data,
    QCryptographicHash::Algorithm method) {
  return new QByteArrayView(
      QCryptographicHash::hashInto(
          *buffer,
          *data,
          method));
}

//  int QCryptographicHash::hashLength(Algorithm method)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QCryptographicHash10hashLengthENS_9AlgorithmE(
    QCryptographicHash::Algorithm method) {
  return QCryptographicHash::hashLength(method);
}

//  bool QCryptographicHash::supportsAlgorithm(Algorithm method)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QCryptographicHash17supportsAlgorithmENS_9AlgorithmE(
    QCryptographicHash::Algorithm method) {
  return QCryptographicHash::supportsAlgorithm(method);
}
