//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/qssldiffiehellmanparameters.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtNetwork/qtnetworkglobal.h>
#if !defined(QT_NO_SSL)
#include <QtNetwork/qssldiffiehellmanparameters.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qstring.h>
#include <QtCore/qdebug.h>

//  QSslDiffieHellmanParameters
//      QSslDiffieHellmanParameters::defaultParameters()
extern "C" Q_DECL_EXPORT
QSslDiffieHellmanParameters *ritual_ZN27QSslDiffieHellmanParameters17defaultParametersEv() {
  return new QSslDiffieHellmanParameters(
      QSslDiffieHellmanParameters::defaultParameters());
}

//  QSslDiffieHellmanParameters::QSslDiffieHellmanParameters()
extern "C" Q_DECL_EXPORT
QSslDiffieHellmanParameters *ritual_ZN27QSslDiffieHellmanParametersC1Ev() {
  return new QSslDiffieHellmanParameters();
}

//  QSslDiffieHellmanParameters::QSslDiffieHellmanParameters(const
//      QSslDiffieHellmanParameters &other)
extern "C" Q_DECL_EXPORT
QSslDiffieHellmanParameters *ritual_ZN27QSslDiffieHellmanParametersC1ERKS_(
    const QSslDiffieHellmanParameters *other) {
  return new QSslDiffieHellmanParameters(*other);
}

//  QSslDiffieHellmanParameters::~QSslDiffieHellmanParameters()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QSslDiffieHellmanParametersD1Ev(
    QSslDiffieHellmanParameters *self) {
  delete self;
}

//  QSslDiffieHellmanParameters
//      QSslDiffieHellmanParameters::fromEncoded(const QByteArray &encoded,
//      QSsl::EncodingFormat format)
extern "C" Q_DECL_EXPORT
QSslDiffieHellmanParameters *ritual_ZN27QSslDiffieHellmanParameters11fromEncodedERK10QByteArrayN4QSsl14EncodingFormatE(
    const QByteArray *encoded,
    QSsl::EncodingFormat format) {
  return new QSslDiffieHellmanParameters(
      QSslDiffieHellmanParameters::fromEncoded(
          *encoded,
          format));
}

//  QSslDiffieHellmanParameters
//      QSslDiffieHellmanParameters::fromEncoded(QIODevice *device,
//      QSsl::EncodingFormat format)
extern "C" Q_DECL_EXPORT
QSslDiffieHellmanParameters *ritual_ZN27QSslDiffieHellmanParameters11fromEncodedEP9QIODeviceN4QSsl14EncodingFormatE(
    QIODevice *device,
    QSsl::EncodingFormat format) {
  return new QSslDiffieHellmanParameters(
      QSslDiffieHellmanParameters::fromEncoded(
          device,
          format));
}

//  bool QSslDiffieHellmanParameters::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QSslDiffieHellmanParameters7isEmptyEv(
    const QSslDiffieHellmanParameters *self) {
  return self->isEmpty();
}

//  bool QSslDiffieHellmanParameters::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QSslDiffieHellmanParameters7isValidEv(
    const QSslDiffieHellmanParameters *self) {
  return self->isValid();
}

//  Error QSslDiffieHellmanParameters::error() const
extern "C" Q_DECL_EXPORT
QSslDiffieHellmanParameters::Error ritual_ZNK27QSslDiffieHellmanParameters5errorEv(
    const QSslDiffieHellmanParameters *self) {
  return self->error();
}

//  QString QSslDiffieHellmanParameters::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK27QSslDiffieHellmanParameters11errorStringEv(
    const QSslDiffieHellmanParameters *self) {
  return new QString(self->errorString());
}

//  bool QSslDiffieHellmanParameters::isEqual(const
//      QSslDiffieHellmanParameters &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QSslDiffieHellmanParameters7isEqualERKS_(
    const QSslDiffieHellmanParameters *self,
    const QSslDiffieHellmanParameters *other) {
  return self->isEqual(*other);
}

//  bool operator==(const QSslDiffieHellmanParameters &lhs, const
//      QSslDiffieHellmanParameters &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK27QSslDiffieHellmanParametersS1_(
    const QSslDiffieHellmanParameters *lhs,
    const QSslDiffieHellmanParameters *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QSslDiffieHellmanParameters &lhs, const
//      QSslDiffieHellmanParameters &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK27QSslDiffieHellmanParametersS1_(
    const QSslDiffieHellmanParameters *lhs,
    const QSslDiffieHellmanParameters *rhs) {
  return operator!=(*lhs, *rhs);
}

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug debug, const QSslDiffieHellmanParameters
//      &dhparam)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRK27QSslDiffieHellmanParameters(
    const QDebug *debug,
    const QSslDiffieHellmanParameters *dhparam) {
  return new QDebug(operator<<(*debug, *dhparam));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

#endif  // !defined(QT_NO_SSL)
