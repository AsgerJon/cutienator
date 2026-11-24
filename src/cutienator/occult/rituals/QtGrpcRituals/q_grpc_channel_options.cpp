//  Written by dev_tooling.RitualGenerator from the records of
//  QtGrpc/qgrpcchanneloptions.h, Qt 6.12.0. Changes made here are lost.
#include <QtGrpc/qgrpcchanneloptions.h>
#include <QtCore/qvariant.h>
#include <QtGrpc/qgrpcserializationformat.h>
#include <QtCore/qdebug.h>

//  QGrpcChannelOptions::QGrpcChannelOptions()
extern "C" Q_DECL_EXPORT
QGrpcChannelOptions *ritual_ZN19QGrpcChannelOptionsC1Ev() {
  return new QGrpcChannelOptions();
}

//  QGrpcChannelOptions::~QGrpcChannelOptions()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGrpcChannelOptionsD1Ev(QGrpcChannelOptions *self) {
  delete self;
}

//  QGrpcChannelOptions::QGrpcChannelOptions(const QGrpcChannelOptions
//      &other)
extern "C" Q_DECL_EXPORT
QGrpcChannelOptions *ritual_ZN19QGrpcChannelOptionsC1ERKS_(
    const QGrpcChannelOptions *other) {
  return new QGrpcChannelOptions(*other);
}

//  QVariant QGrpcChannelOptions::operator QVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK19QGrpcChannelOptionscv8QVariantEv(
    const QGrpcChannelOptions *self) {
  return new QVariant(self->operator QVariant());
}

//  QtGrpc::CompressionAlgorithms
//      QGrpcChannelOptions::supportedCompressionAlgorithms()
extern "C" Q_DECL_EXPORT
int ritual_ZN19QGrpcChannelOptions30supportedCompressionAlgorithmsEv() {
  return static_cast<int>(
      QGrpcChannelOptions::supportedCompressionAlgorithms().toInt());
}

//  QtGrpc::CompressionAlgorithms
//      QGrpcChannelOptions::acceptedCompressionAlgorithms() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QGrpcChannelOptions29acceptedCompressionAlgorithmsEv(
    const QGrpcChannelOptions *self) {
  return static_cast<int>(self->acceptedCompressionAlgorithms().toInt());
}

//  QGrpcSerializationFormat QGrpcChannelOptions::serializationFormat() const
extern "C" Q_DECL_EXPORT
QGrpcSerializationFormat *ritual_ZNK19QGrpcChannelOptions19serializationFormatEv(
    const QGrpcChannelOptions *self) {
  return new QGrpcSerializationFormat(self->serializationFormat());
}

//  bool operator==(const QGrpcChannelOptions &lhs, const QGrpcChannelOptions
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK19QGrpcChannelOptionsS1_(
    const QGrpcChannelOptions *lhs,
    const QGrpcChannelOptions *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QGrpcChannelOptions &lhs, const QGrpcChannelOptions
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK19QGrpcChannelOptionsS1_(
    const QGrpcChannelOptions *lhs,
    const QGrpcChannelOptions *rhs) {
  return operator!=(*lhs, *rhs);
}

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug debug, const QGrpcChannelOptions &chOpts)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRK19QGrpcChannelOptions(
    const QDebug *debug,
    const QGrpcChannelOptions *chOpts) {
  return new QDebug(operator<<(*debug, *chOpts));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)
