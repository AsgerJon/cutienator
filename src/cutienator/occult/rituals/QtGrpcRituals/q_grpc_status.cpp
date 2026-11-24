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

//  QVariant QGrpcStatus::operator QVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK11QGrpcStatuscv8QVariantEv(const QGrpcStatus *self) {
  return new QVariant(self->operator QVariant());
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
