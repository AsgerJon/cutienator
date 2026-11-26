//  Written by dev_tooling.RitualGenerator from the records of
//  QtGrpc/qgrpcstatus.h, Qt 6.12.0. Changes made here are lost.
#include <QtGrpc/qgrpcstatus.h>
#include <QtCore/qanystringview.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qdebug.h>

//  QGrpcStatus::QGrpcStatus(QtGrpc::StatusCode code, QAnyStringView message)
extern "C" Q_DECL_EXPORT
QGrpcStatus *ritual_ZN11QGrpcStatusC1EN6QtGrpc10StatusCodeE14QAnyStringView(
    QtGrpc::StatusCode code,
    const QString *message) {
  return new QGrpcStatus(code, QAnyStringView(*message));
}

//  QGrpcStatus::~QGrpcStatus()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGrpcStatusD1Ev(QGrpcStatus *self) {
  delete self;
}

//  QGrpcStatus::QGrpcStatus(const QGrpcStatus &other)
extern "C" Q_DECL_EXPORT
QGrpcStatus *ritual_ZN11QGrpcStatusC1ERKS_(const QGrpcStatus *other) {
  return new QGrpcStatus(*other);
}

//  QGrpcStatus &QGrpcStatus::operator=(const QGrpcStatus &other)
extern "C" Q_DECL_EXPORT
QGrpcStatus *ritual_ZN11QGrpcStatusaSERKS_(
    QGrpcStatus *self,
    const QGrpcStatus *other) {
  return &(self->operator=(*other));
}

//  QGrpcStatus::QGrpcStatus(QGrpcStatus &&other)
extern "C" Q_DECL_EXPORT
QGrpcStatus *ritual_ZN11QGrpcStatusC1EOS_(QGrpcStatus *other) {
  return new QGrpcStatus(std::move(*other));
}

//  QGrpcStatus &QGrpcStatus::operator=(QGrpcStatus &&other)
extern "C" Q_DECL_EXPORT
QGrpcStatus *ritual_ZN11QGrpcStatusaSEOS_(
    QGrpcStatus *self,
    QGrpcStatus *other) {
  return &(self->operator=(std::move(*other)));
}

//  QVariant QGrpcStatus::operator QVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK11QGrpcStatuscv8QVariantEv(const QGrpcStatus *self) {
  return new QVariant(self->operator QVariant());
}

//  void QGrpcStatus::swap(QGrpcStatus &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGrpcStatus4swapERS_(QGrpcStatus *self, QGrpcStatus *other) {
  self->swap(*other);
}

//  QtGrpc::StatusCode QGrpcStatus::code() const
extern "C" Q_DECL_EXPORT
QtGrpc::StatusCode ritual_ZNK11QGrpcStatus4codeEv(const QGrpcStatus *self) {
  return self->code();
}

//  bool QGrpcStatus::isOk() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QGrpcStatus4isOkEv(const QGrpcStatus *self) {
  return self->isOk();
}

//  const QString &QGrpcStatus::message() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNKR11QGrpcStatus7messageEv(const QGrpcStatus *self) {
  return new QString(self->message());
}

//  bool operator==(const QGrpcStatus &lhs, const QtGrpc::StatusCode &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK11QGrpcStatusRKN6QtGrpc10StatusCodeE(
    const QGrpcStatus *lhs,
    const QtGrpc::StatusCode *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QGrpcStatus &lhs, const QtGrpc::StatusCode &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK11QGrpcStatusRKN6QtGrpc10StatusCodeE(
    const QGrpcStatus *lhs,
    const QtGrpc::StatusCode *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator==(const QtGrpc::StatusCode &lhs, const QGrpcStatus &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRKN6QtGrpc10StatusCodeERK11QGrpcStatus(
    const QtGrpc::StatusCode *lhs,
    const QGrpcStatus *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QtGrpc::StatusCode &lhs, const QGrpcStatus &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRKN6QtGrpc10StatusCodeERK11QGrpcStatus(
    const QtGrpc::StatusCode *lhs,
    const QGrpcStatus *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator==(const QGrpcStatus &lhs, const QGrpcStatus &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK11QGrpcStatusS1_(
    const QGrpcStatus *lhs,
    const QGrpcStatus *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QGrpcStatus &lhs, const QGrpcStatus &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK11QGrpcStatusS1_(
    const QGrpcStatus *lhs,
    const QGrpcStatus *rhs) {
  return operator!=(*lhs, *rhs);
}

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug debug, const QGrpcStatus &status)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRK11QGrpcStatus(
    const QDebug *debug,
    const QGrpcStatus *status) {
  return new QDebug(operator<<(*debug, *status));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

#if !defined(QT_NO_DATASTREAM)
//  QDataStream &operator<<(QDataStream &out, const QGrpcStatus &status)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZlsR11QDataStreamRK11QGrpcStatus(
    QDataStream *out,
    const QGrpcStatus *status) {
  return &(operator<<(*out, *status));
}
#endif  // !defined(QT_NO_DATASTREAM)

#if !defined(QT_NO_DATASTREAM)
//  QDataStream &operator>>(QDataStream &in, QGrpcStatus &status)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZrsR11QDataStreamR11QGrpcStatus(
    QDataStream *in,
    QGrpcStatus *status) {
  return &(operator>>(*in, *status));
}
#endif  // !defined(QT_NO_DATASTREAM)
