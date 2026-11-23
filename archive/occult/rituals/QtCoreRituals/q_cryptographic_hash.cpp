//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qcryptographichash.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qcryptographichash.h>
#include <QtCore/qbytearrayview.h>
#include <QtCore/qbytearray.h>

//  QCryptographicHash::QCryptographicHash(Algorithm method)
extern "C" Q_DECL_EXPORT
QCryptographicHash *ritual_ZN18QCryptographicHashC1ENS_9AlgorithmE(
    QCryptographicHash::Algorithm method) {
  return new QCryptographicHash(method);
}

//  QCryptographicHash::~QCryptographicHash()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCryptographicHashD1Ev(QCryptographicHash *self) {
  delete self;
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

//  void QCryptographicHash::addData(const char *data, qsizetype length)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCryptographicHash7addDataEPKcx(
    QCryptographicHash *self,
    const char *data,
    qsizetype length) {
  self->addData(data, length);
}

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
