//  Written by dev_tooling.RitualGenerator from the records of
//  QtGrpc/qgrpccalloptions.h, Qt 6.12.0. Changes made here are lost.
#include <QtGrpc/qgrpccalloptions.h>
#include <QtCore/qvariant.h>
#include <QtGrpc/qtgrpcnamespace.h>
#include <QtCore/qbytearrayview.h>
#include <QtCore/qdebug.h>
#include <optional>
#include <chrono>
#include <utility>
#include <QtCore/QByteArray>
#include <QtGrpc/QtGrpc>

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

//  QGrpcCallOptions &QGrpcCallOptions::operator=(const QGrpcCallOptions
//      &other)
extern "C" Q_DECL_EXPORT
QGrpcCallOptions *ritual_ZN16QGrpcCallOptionsaSERKS_(
    QGrpcCallOptions *self,
    const QGrpcCallOptions *other) {
  return &(self->operator=(*other));
}

//  QGrpcCallOptions::QGrpcCallOptions(QGrpcCallOptions &&other)
extern "C" Q_DECL_EXPORT
QGrpcCallOptions *ritual_ZN16QGrpcCallOptionsC1EOS_(
    QGrpcCallOptions *other) {
  return new QGrpcCallOptions(std::move(*other));
}

//  QGrpcCallOptions &QGrpcCallOptions::operator=(QGrpcCallOptions &&other)
extern "C" Q_DECL_EXPORT
QGrpcCallOptions *ritual_ZN16QGrpcCallOptionsaSEOS_(
    QGrpcCallOptions *self,
    QGrpcCallOptions *other) {
  return &(self->operator=(std::move(*other)));
}

//  QVariant QGrpcCallOptions::operator QVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK16QGrpcCallOptionscv8QVariantEv(
    const QGrpcCallOptions *self) {
  return new QVariant(self->operator QVariant());
}

//  void QGrpcCallOptions::swap(QGrpcCallOptions &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QGrpcCallOptions4swapERS_(
    QGrpcCallOptions *self,
    QGrpcCallOptions *other) {
  self->swap(*other);
}

//  std::optional<std::chrono::milliseconds>
//      QGrpcCallOptions::deadlineTimeout() const
extern "C" Q_DECL_EXPORT
std::optional<std::chrono::milliseconds> *ritual_ZNK16QGrpcCallOptions15deadlineTimeoutEv(
    const QGrpcCallOptions *self) {
  return new std::optional<std::chrono::milliseconds>(
      self->deadlineTimeout());
}

//  QGrpcCallOptions
//      &QGrpcCallOptions::setDeadlineTimeout(std::chrono::milliseconds
//      timeout)
extern "C" Q_DECL_EXPORT
QGrpcCallOptions *ritual_ZN16QGrpcCallOptions18setDeadlineTimeoutENSt6chrono8durationIlSt5ratioILl1ELl1000EEEE(
    QGrpcCallOptions *self,
    long long timeout) {
  return &(self->setDeadlineTimeout(std::chrono::milliseconds(timeout)));
}

#if QT_DEPRECATED_SINCE(6, 13)
//  const QHash<QByteArray, QByteArray> &QGrpcCallOptions::metadata() const
extern "C" Q_DECL_EXPORT
const QHash<QByteArray, QByteArray> *ritual_ZNKR16QGrpcCallOptions8metadataEv(
    const QGrpcCallOptions *self) {
  return &(self->metadata());
}
#endif  // QT_DEPRECATED_SINCE(6, 13)

#if QT_DEPRECATED_SINCE(6, 13)
//  QGrpcCallOptions &QGrpcCallOptions::setMetadata(const QHash<QByteArray,
//      QByteArray> &metadata)
extern "C" Q_DECL_EXPORT
QGrpcCallOptions *ritual_ZN16QGrpcCallOptions11setMetadataERK5QHashI10QByteArrayS1_E(
    QGrpcCallOptions *self,
    const QHash<QByteArray, QByteArray> *metadata) {
  return &(self->setMetadata(*metadata));
}
#endif  // QT_DEPRECATED_SINCE(6, 13)

#if QT_DEPRECATED_SINCE(6, 13)
//  QGrpcCallOptions &QGrpcCallOptions::setMetadata(QHash<QByteArray,
//      QByteArray> &&metadata)
extern "C" Q_DECL_EXPORT
QGrpcCallOptions *ritual_ZN16QGrpcCallOptions11setMetadataEO5QHashI10QByteArrayS1_E(
    QGrpcCallOptions *self,
    QHash<QByteArray, QByteArray> *metadata) {
  return &(self->setMetadata(std::move(*metadata)));
}
#endif  // QT_DEPRECATED_SINCE(6, 13)

//  const QMultiHash<QByteArray, QByteArray>
//      &QGrpcCallOptions::metadata(QtGrpc::MultiValue_t a0) const
extern "C" Q_DECL_EXPORT
const QMultiHash<QByteArray, QByteArray> *ritual_ZNKR16QGrpcCallOptions8metadataEN6QtGrpc12MultiValue_tE(
    const QGrpcCallOptions *self,
    const QtGrpc::MultiValue_t *a0) {
  return &(self->metadata(*a0));
}

//  QGrpcCallOptions &QGrpcCallOptions::setMetadata(const
//      QMultiHash<QByteArray, QByteArray> &metadata)
extern "C" Q_DECL_EXPORT
QGrpcCallOptions *ritual_ZN16QGrpcCallOptions11setMetadataERK10QMultiHashI10QByteArrayS1_E(
    QGrpcCallOptions *self,
    const QMultiHash<QByteArray, QByteArray> *metadata) {
  return &(self->setMetadata(*metadata));
}

//  QGrpcCallOptions &QGrpcCallOptions::setMetadata(QMultiHash<QByteArray,
//      QByteArray> &&metadata)
extern "C" Q_DECL_EXPORT
QGrpcCallOptions *ritual_ZN16QGrpcCallOptions11setMetadataEO10QMultiHashI10QByteArrayS1_E(
    QGrpcCallOptions *self,
    QMultiHash<QByteArray, QByteArray> *metadata) {
  return &(self->setMetadata(std::move(*metadata)));
}

//  QGrpcCallOptions &QGrpcCallOptions::setMetadata(std::initializer_list<std
//      ::pair<QByteArray, QByteArray>> list)
extern "C" Q_DECL_EXPORT
QGrpcCallOptions *ritual_ZN16QGrpcCallOptions11setMetadataESt16initializer_listISt4pairI10QByteArrayS2_EE(
    QGrpcCallOptions *self,
    const std::initializer_list<std::pair<QByteArray, QByteArray>> *list) {
  return &(self->setMetadata(*list));
}

//  QGrpcCallOptions &QGrpcCallOptions::addMetadata(QByteArrayView key,
//      QByteArrayView value)
extern "C" Q_DECL_EXPORT
QGrpcCallOptions *ritual_ZN16QGrpcCallOptions11addMetadataE14QByteArrayViewS0_(
    QGrpcCallOptions *self,
    const QByteArrayView *key,
    const QByteArrayView *value) {
  return &(self->addMetadata(*key, *value));
}

//  std::optional<bool> QGrpcCallOptions::filterServerMetadata() const
extern "C" Q_DECL_EXPORT
std::optional<bool> *ritual_ZNK16QGrpcCallOptions20filterServerMetadataEv(
    const QGrpcCallOptions *self) {
  return new std::optional<bool>(self->filterServerMetadata());
}

//  QGrpcCallOptions &QGrpcCallOptions::setFilterServerMetadata(bool value)
extern "C" Q_DECL_EXPORT
QGrpcCallOptions *ritual_ZN16QGrpcCallOptions23setFilterServerMetadataEb(
    QGrpcCallOptions *self,
    bool value) {
  return &(self->setFilterServerMetadata(value));
}

//  std::optional<quint64> QGrpcCallOptions::maximumReceiveMessageSize()
//      const
extern "C" Q_DECL_EXPORT
std::optional<quint64> *ritual_ZNK16QGrpcCallOptions25maximumReceiveMessageSizeEv(
    const QGrpcCallOptions *self) {
  return new std::optional<quint64>(self->maximumReceiveMessageSize());
}

//  QGrpcCallOptions &QGrpcCallOptions::setMaximumReceiveMessageSize(quint64
//      size)
extern "C" Q_DECL_EXPORT
QGrpcCallOptions *ritual_ZN16QGrpcCallOptions28setMaximumReceiveMessageSizeEy(
    QGrpcCallOptions *self,
    quint64 size) {
  return &(self->setMaximumReceiveMessageSize(size));
}

//  std::optional<QtGrpc::CompressionAlgorithm>
//      QGrpcCallOptions::requestCompression() const
extern "C" Q_DECL_EXPORT
std::optional<QtGrpc::CompressionAlgorithm> *ritual_ZNK16QGrpcCallOptions18requestCompressionEv(
    const QGrpcCallOptions *self) {
  return new std::optional<QtGrpc::CompressionAlgorithm>(
      self->requestCompression());
}

//  QGrpcCallOptions
//      &QGrpcCallOptions::setRequestCompression(QtGrpc::CompressionAlgorithm
//      algorithm)
extern "C" Q_DECL_EXPORT
QGrpcCallOptions *ritual_ZN16QGrpcCallOptions21setRequestCompressionEN6QtGrpc20CompressionAlgorithmE(
    QGrpcCallOptions *self,
    QtGrpc::CompressionAlgorithm algorithm) {
  return &(self->setRequestCompression(algorithm));
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

//  QGrpcCallOptionsPrivate *QGrpcCallOptions::d_func()
extern "C" Q_DECL_EXPORT
QGrpcCallOptionsPrivate *ritual_ZN16QGrpcCallOptions6d_funcEv(
    QGrpcCallOptions *self) {
  return self->d_func();
}

//  const QGrpcCallOptionsPrivate *QGrpcCallOptions::d_func() const
extern "C" Q_DECL_EXPORT
const QGrpcCallOptionsPrivate *ritual_ZNK16QGrpcCallOptions6d_funcEv(
    const QGrpcCallOptions *self) {
  return self->d_func();
}

//  a std::optional<std::chrono::milliseconds> a ritual of QGrpcCallOptions
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QGrpcCallOptions__std_optional_std_chrono_milliseconds(
    std::optional<std::chrono::milliseconds> *self) {
  delete self;
}

//  a std::optional<bool> a ritual of QGrpcCallOptions gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QGrpcCallOptions__std_optional_bool(
    std::optional<bool> *self) {
  delete self;
}

//  a std::optional<quint64> a ritual of QGrpcCallOptions gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QGrpcCallOptions__std_optional_quint64(
    std::optional<quint64> *self) {
  delete self;
}

//  a std::optional<QtGrpc::CompressionAlgorithm> a ritual of
//      QGrpcCallOptions gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QGrpcCallOptions__std_optional_QtGrpc_CompressionAlgorithm(
    std::optional<QtGrpc::CompressionAlgorithm> *self) {
  delete self;
}
