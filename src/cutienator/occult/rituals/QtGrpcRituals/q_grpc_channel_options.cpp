//  Written by dev_tooling.RitualGenerator from the records of
//  QtGrpc/qgrpcchanneloptions.h, Qt 6.12.0. Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtGrpc/qgrpcchanneloptions.h>
#include <QtCore/qvariant.h>
#include <QtGrpc/qtgrpcnamespace.h>
#include <QtCore/qbytearrayview.h>
#include <QtGrpc/qgrpcserializationformat.h>
#include <QtNetwork/qsslconfiguration.h>
#include <QtCore/qdebug.h>
#include <optional>
#include <chrono>
#include <utility>
#include <QtCore/QByteArray>
#include <QtGrpc/QtGrpc>
#include <QtNetwork/QSslConfiguration>

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

//  QGrpcChannelOptions &QGrpcChannelOptions::operator=(const
//      QGrpcChannelOptions &other)
extern "C" Q_DECL_EXPORT
QGrpcChannelOptions *ritual_ZN19QGrpcChannelOptionsaSERKS_(
    QGrpcChannelOptions *self,
    const QGrpcChannelOptions *other) {
  return &(self->operator=(*other));
}

//  QGrpcChannelOptions::QGrpcChannelOptions(QGrpcChannelOptions &&other)
extern "C" Q_DECL_EXPORT
QGrpcChannelOptions *ritual_ZN19QGrpcChannelOptionsC1EOS_(
    QGrpcChannelOptions *other) {
  return new QGrpcChannelOptions(std::move(*other));
}

//  QGrpcChannelOptions &QGrpcChannelOptions::operator=(QGrpcChannelOptions
//      &&other)
extern "C" Q_DECL_EXPORT
QGrpcChannelOptions *ritual_ZN19QGrpcChannelOptionsaSEOS_(
    QGrpcChannelOptions *self,
    QGrpcChannelOptions *other) {
  return &(self->operator=(std::move(*other)));
}

//  QVariant QGrpcChannelOptions::operator QVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK19QGrpcChannelOptionscv8QVariantEv(
    const QGrpcChannelOptions *self) {
  return new QVariant(self->operator QVariant());
}

//  void QGrpcChannelOptions::swap(QGrpcChannelOptions &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGrpcChannelOptions4swapERS_(
    QGrpcChannelOptions *self,
    QGrpcChannelOptions *other) {
  self->swap(*other);
}

//  std::optional<std::chrono::milliseconds>
//      QGrpcChannelOptions::deadlineTimeout() const
extern "C" Q_DECL_EXPORT
std::optional<std::chrono::milliseconds> *ritual_ZNK19QGrpcChannelOptions15deadlineTimeoutEv(
    const QGrpcChannelOptions *self) {
  return new std::optional<std::chrono::milliseconds>(
      self->deadlineTimeout());
}

//  QGrpcChannelOptions
//      &QGrpcChannelOptions::setDeadlineTimeout(std::chrono::milliseconds
//      timeout)
extern "C" Q_DECL_EXPORT
QGrpcChannelOptions *ritual_ZN19QGrpcChannelOptions18setDeadlineTimeoutENSt6chrono8durationIlSt5ratioILl1ELl1000EEEE(
    QGrpcChannelOptions *self,
    long long timeout) {
  return &(self->setDeadlineTimeout(std::chrono::milliseconds(timeout)));
}

#if QT_DEPRECATED_SINCE(6, 13)
//  const QHash<QByteArray, QByteArray> &QGrpcChannelOptions::metadata()
//      const
extern "C" Q_DECL_EXPORT
const QHash<QByteArray, QByteArray> *ritual_ZNKR19QGrpcChannelOptions8metadataEv(
    const QGrpcChannelOptions *self) {
  return &(self->metadata());
}
#endif  // QT_DEPRECATED_SINCE(6, 13)

#if QT_DEPRECATED_SINCE(6, 13)
//  QGrpcChannelOptions &QGrpcChannelOptions::setMetadata(const
//      QHash<QByteArray, QByteArray> &metadata)
extern "C" Q_DECL_EXPORT
QGrpcChannelOptions *ritual_ZN19QGrpcChannelOptions11setMetadataERK5QHashI10QByteArrayS1_E(
    QGrpcChannelOptions *self,
    const QHash<QByteArray, QByteArray> *metadata) {
  return &(self->setMetadata(*metadata));
}
#endif  // QT_DEPRECATED_SINCE(6, 13)

#if QT_DEPRECATED_SINCE(6, 13)
//  QGrpcChannelOptions &QGrpcChannelOptions::setMetadata(QHash<QByteArray,
//      QByteArray> &&metadata)
extern "C" Q_DECL_EXPORT
QGrpcChannelOptions *ritual_ZN19QGrpcChannelOptions11setMetadataEO5QHashI10QByteArrayS1_E(
    QGrpcChannelOptions *self,
    QHash<QByteArray, QByteArray> *metadata) {
  return &(self->setMetadata(std::move(*metadata)));
}
#endif  // QT_DEPRECATED_SINCE(6, 13)

//  const QMultiHash<QByteArray, QByteArray>
//      &QGrpcChannelOptions::metadata(QtGrpc::MultiValue_t a0) const
extern "C" Q_DECL_EXPORT
const QMultiHash<QByteArray, QByteArray> *ritual_ZNKR19QGrpcChannelOptions8metadataEN6QtGrpc12MultiValue_tE(
    const QGrpcChannelOptions *self,
    const QtGrpc::MultiValue_t *a0) {
  return &(self->metadata(*a0));
}

//  QGrpcChannelOptions &QGrpcChannelOptions::setMetadata(const
//      QMultiHash<QByteArray, QByteArray> &metadata)
extern "C" Q_DECL_EXPORT
QGrpcChannelOptions *ritual_ZN19QGrpcChannelOptions11setMetadataERK10QMultiHashI10QByteArrayS1_E(
    QGrpcChannelOptions *self,
    const QMultiHash<QByteArray, QByteArray> *metadata) {
  return &(self->setMetadata(*metadata));
}

//  QGrpcChannelOptions
//      &QGrpcChannelOptions::setMetadata(QMultiHash<QByteArray, QByteArray>
//      &&metadata)
extern "C" Q_DECL_EXPORT
QGrpcChannelOptions *ritual_ZN19QGrpcChannelOptions11setMetadataEO10QMultiHashI10QByteArrayS1_E(
    QGrpcChannelOptions *self,
    QMultiHash<QByteArray, QByteArray> *metadata) {
  return &(self->setMetadata(std::move(*metadata)));
}

//  QGrpcChannelOptions &QGrpcChannelOptions::setMetadata(std::initializer_li
//      st<std::pair<QByteArray, QByteArray>> list)
extern "C" Q_DECL_EXPORT
QGrpcChannelOptions *ritual_ZN19QGrpcChannelOptions11setMetadataESt16initializer_listISt4pairI10QByteArrayS2_EE(
    QGrpcChannelOptions *self,
    const std::initializer_list<std::pair<QByteArray, QByteArray>> *list) {
  return &(self->setMetadata(*list));
}

//  QGrpcChannelOptions &QGrpcChannelOptions::addMetadata(QByteArrayView key,
//      QByteArrayView value)
extern "C" Q_DECL_EXPORT
QGrpcChannelOptions *ritual_ZN19QGrpcChannelOptions11addMetadataE14QByteArrayViewS0_(
    QGrpcChannelOptions *self,
    const QByteArrayView *key,
    const QByteArrayView *value) {
  return &(self->addMetadata(*key, *value));
}

//  std::optional<bool> QGrpcChannelOptions::filterServerMetadata() const
extern "C" Q_DECL_EXPORT
std::optional<bool> *ritual_ZNK19QGrpcChannelOptions20filterServerMetadataEv(
    const QGrpcChannelOptions *self) {
  return new std::optional<bool>(self->filterServerMetadata());
}

//  QGrpcChannelOptions &QGrpcChannelOptions::setFilterServerMetadata(bool
//      value)
extern "C" Q_DECL_EXPORT
QGrpcChannelOptions *ritual_ZN19QGrpcChannelOptions23setFilterServerMetadataEb(
    QGrpcChannelOptions *self,
    bool value) {
  return &(self->setFilterServerMetadata(value));
}

//  std::optional<quint64> QGrpcChannelOptions::maximumReceiveMessageSize()
//      const
extern "C" Q_DECL_EXPORT
std::optional<quint64> *ritual_ZNK19QGrpcChannelOptions25maximumReceiveMessageSizeEv(
    const QGrpcChannelOptions *self) {
  return new std::optional<quint64>(self->maximumReceiveMessageSize());
}

//  QGrpcChannelOptions
//      &QGrpcChannelOptions::setMaximumReceiveMessageSize(quint64 size)
extern "C" Q_DECL_EXPORT
QGrpcChannelOptions *ritual_ZN19QGrpcChannelOptions28setMaximumReceiveMessageSizeEy(
    QGrpcChannelOptions *self,
    quint64 size) {
  return &(self->setMaximumReceiveMessageSize(size));
}

//  std::optional<QtGrpc::CompressionAlgorithm>
//      QGrpcChannelOptions::requestCompression() const
extern "C" Q_DECL_EXPORT
std::optional<QtGrpc::CompressionAlgorithm> *ritual_ZNK19QGrpcChannelOptions18requestCompressionEv(
    const QGrpcChannelOptions *self) {
  return new std::optional<QtGrpc::CompressionAlgorithm>(
      self->requestCompression());
}

//  QGrpcChannelOptions
//      &QGrpcChannelOptions::setRequestCompression(QtGrpc::CompressionAlgori
//      thm algorithm)
extern "C" Q_DECL_EXPORT
QGrpcChannelOptions *ritual_ZN19QGrpcChannelOptions21setRequestCompressionEN6QtGrpc20CompressionAlgorithmE(
    QGrpcChannelOptions *self,
    QtGrpc::CompressionAlgorithm algorithm) {
  return &(self->setRequestCompression(algorithm));
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

//  QGrpcChannelOptions &QGrpcChannelOptions::setAcceptedCompressionAlgorithm
//      s(QtGrpc::CompressionAlgorithms algorithms)
extern "C" Q_DECL_EXPORT
QGrpcChannelOptions *ritual_ZN19QGrpcChannelOptions32setAcceptedCompressionAlgorithmsE6QFlagsIN6QtGrpc20CompressionAlgorithmEE(
    QGrpcChannelOptions *self,
    int algorithms) {
  return &(
      self->setAcceptedCompressionAlgorithms(
          QFlags<QtGrpc::CompressionAlgorithm>::fromInt(algorithms)));
}

//  QGrpcSerializationFormat QGrpcChannelOptions::serializationFormat() const
extern "C" Q_DECL_EXPORT
QGrpcSerializationFormat *ritual_ZNK19QGrpcChannelOptions19serializationFormatEv(
    const QGrpcChannelOptions *self) {
  return new QGrpcSerializationFormat(self->serializationFormat());
}

//  QGrpcChannelOptions &QGrpcChannelOptions::setSerializationFormat(const
//      QGrpcSerializationFormat &format)
extern "C" Q_DECL_EXPORT
QGrpcChannelOptions *ritual_ZN19QGrpcChannelOptions22setSerializationFormatERK24QGrpcSerializationFormat(
    QGrpcChannelOptions *self,
    const QGrpcSerializationFormat *format) {
  return &(self->setSerializationFormat(*format));
}

#if QT_CONFIG(ssl)
//  std::optional<QSslConfiguration> QGrpcChannelOptions::sslConfiguration()
//      const
extern "C" Q_DECL_EXPORT
std::optional<QSslConfiguration> *ritual_ZNK19QGrpcChannelOptions16sslConfigurationEv(
    const QGrpcChannelOptions *self) {
  return new std::optional<QSslConfiguration>(self->sslConfiguration());
}
#endif  // QT_CONFIG(ssl)

#if QT_CONFIG(ssl)
//  QGrpcChannelOptions &QGrpcChannelOptions::setSslConfiguration(const
//      QSslConfiguration &sslConfiguration)
extern "C" Q_DECL_EXPORT
QGrpcChannelOptions *ritual_ZN19QGrpcChannelOptions19setSslConfigurationERK17QSslConfiguration(
    QGrpcChannelOptions *self,
    const QSslConfiguration *sslConfiguration) {
  return &(self->setSslConfiguration(*sslConfiguration));
}
#endif  // QT_CONFIG(ssl)

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

//  QGrpcChannelOptionsPrivate *QGrpcChannelOptions::d_func()
extern "C" Q_DECL_EXPORT
QGrpcChannelOptionsPrivate *ritual_ZN19QGrpcChannelOptions6d_funcEv(
    QGrpcChannelOptions *self) {
  return self->d_func();
}

//  const QGrpcChannelOptionsPrivate *QGrpcChannelOptions::d_func() const
extern "C" Q_DECL_EXPORT
const QGrpcChannelOptionsPrivate *ritual_ZNK19QGrpcChannelOptions6d_funcEv(
    const QGrpcChannelOptions *self) {
  return self->d_func();
}

//  a std::optional<std::chrono::milliseconds> a ritual of
//      QGrpcChannelOptions gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QGrpcChannelOptions__std_optional_std_chrono_milliseconds(
    std::optional<std::chrono::milliseconds> *self) {
  delete self;
}

//  a std::optional<bool> a ritual of QGrpcChannelOptions gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QGrpcChannelOptions__std_optional_bool(
    std::optional<bool> *self) {
  delete self;
}

//  a std::optional<quint64> a ritual of QGrpcChannelOptions gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QGrpcChannelOptions__std_optional_quint64(
    std::optional<quint64> *self) {
  delete self;
}

//  a std::optional<QtGrpc::CompressionAlgorithm> a ritual of
//      QGrpcChannelOptions gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QGrpcChannelOptions__std_optional_QtGrpc_CompressionAlgorithm(
    std::optional<QtGrpc::CompressionAlgorithm> *self) {
  delete self;
}

//  a std::optional<QSslConfiguration> a ritual of QGrpcChannelOptions gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QGrpcChannelOptions__std_optional_QSslConfiguration(
    std::optional<QSslConfiguration> *self) {
  delete self;
}
