//  Written by dev_tooling.RitualGenerator from the records of
//  QtGrpc/qgrpcserializationformat.h, Qt 6.12.0. Changes made here are lost.
#include <QtGrpc/qgrpcserializationformat.h>
#include <QtCore/qvariant.h>
#include <QtCore/qbytearrayview.h>
#include <QtCore/qdebug.h>

//  QGrpcSerializationFormat::QGrpcSerializationFormat(QtGrpc::SerializationF
//      ormat format)
extern "C" Q_DECL_EXPORT
QGrpcSerializationFormat *ritual_ZN24QGrpcSerializationFormatC1EN6QtGrpc19SerializationFormatE(
    QtGrpc::SerializationFormat format) {
  return new QGrpcSerializationFormat(format);
}

//  QGrpcSerializationFormat::~QGrpcSerializationFormat()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGrpcSerializationFormatD1Ev(
    QGrpcSerializationFormat *self) {
  delete self;
}

//  QGrpcSerializationFormat::QGrpcSerializationFormat(const
//      QGrpcSerializationFormat &a0)
extern "C" Q_DECL_EXPORT
QGrpcSerializationFormat *ritual_ZN24QGrpcSerializationFormatC1ERKS_(
    const QGrpcSerializationFormat *a0) {
  return new QGrpcSerializationFormat(*a0);
}

//  QVariant QGrpcSerializationFormat::operator QVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK24QGrpcSerializationFormatcv8QVariantEv(
    const QGrpcSerializationFormat *self) {
  return new QVariant(self->operator QVariant());
}

//  QByteArrayView QGrpcSerializationFormat::suffix() const
extern "C" Q_DECL_EXPORT
QByteArrayView *ritual_ZNK24QGrpcSerializationFormat6suffixEv(
    const QGrpcSerializationFormat *self) {
  return new QByteArrayView(self->suffix());
}

//  bool operator==(const QGrpcSerializationFormat &lhs, const
//      QGrpcSerializationFormat &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK24QGrpcSerializationFormatS1_(
    const QGrpcSerializationFormat *lhs,
    const QGrpcSerializationFormat *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QGrpcSerializationFormat &lhs, const
//      QGrpcSerializationFormat &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK24QGrpcSerializationFormatS1_(
    const QGrpcSerializationFormat *lhs,
    const QGrpcSerializationFormat *rhs) {
  return operator!=(*lhs, *rhs);
}

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug debug, const QGrpcSerializationFormat &sfmt)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRK24QGrpcSerializationFormat(
    const QDebug *debug,
    const QGrpcSerializationFormat *sfmt) {
  return new QDebug(operator<<(*debug, *sfmt));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)
