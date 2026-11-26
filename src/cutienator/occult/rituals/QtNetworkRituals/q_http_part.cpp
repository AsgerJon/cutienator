//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/qhttpmultipart.h, Qt 6.12.0. Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#if (defined(Q_OS_WASM)) || (QT_CONFIG(http))
#if QT_CONFIG(http)
#include <QtNetwork/qhttpmultipart.h>
#include <QtCore/qvariant.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qdebug.h>

//  QHttpPart::QHttpPart()
extern "C" Q_DECL_EXPORT
QHttpPart *ritual_ZN9QHttpPartC1Ev() {
  return new QHttpPart();
}

//  QHttpPart::QHttpPart(const QHttpPart &other)
extern "C" Q_DECL_EXPORT
QHttpPart *ritual_ZN9QHttpPartC1ERKS_(const QHttpPart *other) {
  return new QHttpPart(*other);
}

//  QHttpPart::~QHttpPart()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QHttpPartD1Ev(QHttpPart *self) {
  delete self;
}

//  QHttpPart &QHttpPart::operator=(QHttpPart &&other)
extern "C" Q_DECL_EXPORT
QHttpPart *ritual_ZN9QHttpPartaSEOS_(QHttpPart *self, QHttpPart *other) {
  return &(self->operator=(std::move(*other)));
}

//  QHttpPart &QHttpPart::operator=(const QHttpPart &other)
extern "C" Q_DECL_EXPORT
QHttpPart *ritual_ZN9QHttpPartaSERKS_(
    QHttpPart *self,
    const QHttpPart *other) {
  return &(self->operator=(*other));
}

//  void QHttpPart::swap(QHttpPart &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QHttpPart4swapERS_(QHttpPart *self, QHttpPart *other) {
  self->swap(*other);
}

//  bool QHttpPart::operator==(const QHttpPart &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QHttpParteqERKS_(
    const QHttpPart *self,
    const QHttpPart *other) {
  return self->operator==(*other);
}

//  bool QHttpPart::operator!=(const QHttpPart &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QHttpPartneERKS_(
    const QHttpPart *self,
    const QHttpPart *other) {
  return self->operator!=(*other);
}

//  void QHttpPart::setHeader(QNetworkRequest::KnownHeaders header, const
//      QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QHttpPart9setHeaderEN15QNetworkRequest12KnownHeadersERK8QVariant(
    QHttpPart *self,
    QNetworkRequest::KnownHeaders header,
    const QVariant *value) {
  self->setHeader(header, *value);
}

//  void QHttpPart::setRawHeader(const QByteArray &headerName, const
//      QByteArray &headerValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QHttpPart12setRawHeaderERK10QByteArrayS2_(
    QHttpPart *self,
    const QByteArray *headerName,
    const QByteArray *headerValue) {
  self->setRawHeader(*headerName, *headerValue);
}

//  void QHttpPart::setBody(const QByteArray &body)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QHttpPart7setBodyERK10QByteArray(
    QHttpPart *self,
    const QByteArray *body) {
  self->setBody(*body);
}

//  void QHttpPart::setBodyDevice(QIODevice *device)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QHttpPart13setBodyDeviceEP9QIODevice(
    QHttpPart *self,
    QIODevice *device) {
  self->setBodyDevice(device);
}

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug debug, const QHttpPart &httpPart)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRK9QHttpPart(
    const QDebug *debug,
    const QHttpPart *httpPart) {
  return new QDebug(operator<<(*debug, *httpPart));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

#endif  // QT_CONFIG(http)
#endif  // (defined(Q_OS_WASM)) || (QT_CONFIG(http))
