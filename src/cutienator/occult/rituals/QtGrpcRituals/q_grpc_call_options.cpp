//  Written by dev_tooling.RitualGenerator from the records of
//  QtGrpc/qgrpccalloptions.h, Qt 6.12.0. Changes made here are lost.
#include <QtGrpc/qgrpccalloptions.h>
#include <QtCore/qvariant.h>
#include <QtCore/qdebug.h>

//  QGrpcCallOptions::QGrpcCallOptions()
extern "C" Q_DECL_EXPORT
QGrpcCallOptions *ritual_ZN16QGrpcCallOptionsC1Ev() {
  return new QGrpcCallOptions();
}

//  QGrpcCallOptions::~QGrpcCallOptions()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QGrpcCallOptionsD1Ev(QGrpcCallOptions *self) {
  delete self;
}

//  QGrpcCallOptions::QGrpcCallOptions(const QGrpcCallOptions &other)
extern "C" Q_DECL_EXPORT
QGrpcCallOptions *ritual_ZN16QGrpcCallOptionsC1ERKS_(
    const QGrpcCallOptions *other) {
  return new QGrpcCallOptions(*other);
}

//  QVariant QGrpcCallOptions::operator QVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK16QGrpcCallOptionscv8QVariantEv(
    const QGrpcCallOptions *self) {
  return new QVariant(self->operator QVariant());
}

//  bool operator==(const QGrpcCallOptions &lhs, const QGrpcCallOptions &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK16QGrpcCallOptionsS1_(
    const QGrpcCallOptions *lhs,
    const QGrpcCallOptions *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QGrpcCallOptions &lhs, const QGrpcCallOptions &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK16QGrpcCallOptionsS1_(
    const QGrpcCallOptions *lhs,
    const QGrpcCallOptions *rhs) {
  return operator!=(*lhs, *rhs);
}

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug debug, const QGrpcCallOptions &callOpts)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRK16QGrpcCallOptions(
    const QDebug *debug,
    const QGrpcCallOptions *callOpts) {
  return new QDebug(operator<<(*debug, *callOpts));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)
