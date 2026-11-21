//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qmessageauthenticationcode.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtCore/qmessageauthenticationcode.h>
#include <QtCore/qbytearrayview.h>
#include <QtCore/qbytearray.h>

//  QMessageAuthenticationCode::QMessageAuthenticationCode(QCryptographicHash
//      ::Algorithm method, QByteArrayView key)
extern "C" Q_DECL_EXPORT
QMessageAuthenticationCode *ritual_ZN26QMessageAuthenticationCodeC1EN18QCryptographicHash9AlgorithmE14QByteArrayView(
    QCryptographicHash::Algorithm method,
    const QByteArrayView *key) {
  return new QMessageAuthenticationCode(method, *key);
}

//  QMessageAuthenticationCode::~QMessageAuthenticationCode()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QMessageAuthenticationCodeD1Ev(
    QMessageAuthenticationCode *self) {
  delete self;
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
