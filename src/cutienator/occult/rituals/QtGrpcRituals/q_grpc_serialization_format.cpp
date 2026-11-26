//  Written by dev_tooling.RitualGenerator from the records of
//  QtGrpc/qgrpcserializationformat.h, Qt 6.12.0. Changes made here are lost.
#include <QtGrpc/qgrpcserializationformat.h>
#include <QtCore/qbytearrayview.h>
#include <QtCore/qvariant.h>
#include <QtCore/qdebug.h>
#include <QtCore/QByteArrayView>
#include <memory>
#include <QtProtobuf/QAbstractProtobufSerializer>

//  QGrpcSerializationFormat::QGrpcSerializationFormat(QtGrpc::SerializationF
//      ormat format)
extern "C" Q_DECL_EXPORT
QGrpcSerializationFormat *ritual_ZN24QGrpcSerializationFormatC1EN6QtGrpc19SerializationFormatE(
    QtGrpc::SerializationFormat format) {
  return new QGrpcSerializationFormat(format);
}

//  QGrpcSerializationFormat::QGrpcSerializationFormat(QByteArrayView suffix,
//      std::shared_ptr<QAbstractProtobufSerializer> serializer)
extern "C" Q_DECL_EXPORT
QGrpcSerializationFormat *ritual_ZN24QGrpcSerializationFormatC1E14QByteArrayViewSt10shared_ptrI27QAbstractProtobufSerializerE(
    const QByteArrayView *suffix,
    const std::shared_ptr<QAbstractProtobufSerializer> *serializer) {
  return new QGrpcSerializationFormat(*suffix, *serializer);
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

//  QGrpcSerializationFormat &QGrpcSerializationFormat::operator=(const
//      QGrpcSerializationFormat &a0)
extern "C" Q_DECL_EXPORT
QGrpcSerializationFormat *ritual_ZN24QGrpcSerializationFormataSERKS_(
    QGrpcSerializationFormat *self,
    const QGrpcSerializationFormat *a0) {
  return &(self->operator=(*a0));
}

//  QGrpcSerializationFormat::QGrpcSerializationFormat(QGrpcSerializationForm
//      at &&other)
extern "C" Q_DECL_EXPORT
QGrpcSerializationFormat *ritual_ZN24QGrpcSerializationFormatC1EOS_(
    QGrpcSerializationFormat *other) {
  return new QGrpcSerializationFormat(std::move(*other));
}

//  QGrpcSerializationFormat
//      &QGrpcSerializationFormat::operator=(QGrpcSerializationFormat
//      &&other)
extern "C" Q_DECL_EXPORT
QGrpcSerializationFormat *ritual_ZN24QGrpcSerializationFormataSEOS_(
    QGrpcSerializationFormat *self,
    QGrpcSerializationFormat *other) {
  return &(self->operator=(std::move(*other)));
}

//  QVariant QGrpcSerializationFormat::operator QVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK24QGrpcSerializationFormatcv8QVariantEv(
    const QGrpcSerializationFormat *self) {
  return new QVariant(self->operator QVariant());
}

//  void QGrpcSerializationFormat::swap(QGrpcSerializationFormat &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGrpcSerializationFormat4swapERS_(
    QGrpcSerializationFormat *self,
    QGrpcSerializationFormat *other) {
  self->swap(*other);
}

//  QByteArrayView QGrpcSerializationFormat::suffix() const
extern "C" Q_DECL_EXPORT
QByteArrayView *ritual_ZNK24QGrpcSerializationFormat6suffixEv(
    const QGrpcSerializationFormat *self) {
  return new QByteArrayView(self->suffix());
}

//  std::shared_ptr<QAbstractProtobufSerializer>
//      QGrpcSerializationFormat::serializer() const
extern "C" Q_DECL_EXPORT
std::shared_ptr<QAbstractProtobufSerializer> *ritual_ZNK24QGrpcSerializationFormat10serializerEv(
    const QGrpcSerializationFormat *self) {
  return new std::shared_ptr<QAbstractProtobufSerializer>(
      self->serializer());
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

//  QGrpcSerializationFormatPrivate *QGrpcSerializationFormat::d_func()
extern "C" Q_DECL_EXPORT
QGrpcSerializationFormatPrivate *ritual_ZN24QGrpcSerializationFormat6d_funcEv(
    QGrpcSerializationFormat *self) {
  return self->d_func();
}

//  const QGrpcSerializationFormatPrivate *QGrpcSerializationFormat::d_func()
//      const
extern "C" Q_DECL_EXPORT
const QGrpcSerializationFormatPrivate *ritual_ZNK24QGrpcSerializationFormat6d_funcEv(
    const QGrpcSerializationFormat *self) {
  return self->d_func();
}

//  a std::shared_ptr<QAbstractProtobufSerializer> a ritual of
//      QGrpcSerializationFormat gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QGrpcSerializationFormat__std_shared_ptr_QAbstractProtobufSerializer(
    std::shared_ptr<QAbstractProtobufSerializer> *self) {
  delete self;
}
