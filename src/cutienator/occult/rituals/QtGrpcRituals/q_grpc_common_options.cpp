//  Written by dev_tooling.RitualGenerator from the records of
//  QtGrpc/6.12.0/QtGrpc/private/qgrpccommonoptions_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtGrpc/QtGrpc>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGrpc/6.12.0/QtGrpc/private/qgrpccommonoptions_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGrpc/qtgrpcnamespace.h>
#include <QtCore/qbytearrayview.h>
#include <optional>
#include <chrono>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGrpc/private/qgrpccommonoptions_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtgrpc/src/grpc/qgrpccommonoptions.cpp, line 10, as _ZN13QtGrpcPrivate6toHashERK10QMultiHashI10QByteArrayS1_E
#if QT_DEPRECATED_SINCE(6, 13)
inline QHash<QByteArray, QByteArray>
QtGrpcPrivate::toHash(const QMultiHash<QByteArray, QByteArray> &multiHash)
{
    // Transform a QMultiHash into a QHash by keeping only the first value for each key.
    // The first value will be the newest one when iterating the multi-hash.
    QHash<QByteArray, QByteArray> out;
    out.reserve(multiHash.size());
    for (const auto &[k, v] : multiHash.asKeyValueRange())
        out.try_emplace(k, v);
    return out;
}
#endif  // QT_DEPRECATED_SINCE(6, 13)

//  from ../qtgrpc/src/grpc/qgrpccommonoptions.cpp, line 74, as _ZNK18QGrpcCommonOptions15deadlineTimeoutEv
inline std::optional<std::chrono::milliseconds> QGrpcCommonOptions::deadlineTimeout() const noexcept
{
    return m_timeout;
}

//  from ../qtgrpc/src/grpc/qgrpccommonoptions.cpp, line 92, as _ZN18QGrpcCommonOptions18setDeadlineTimeoutENSt6chrono8durationIlSt5ratioILl1ELl1000EEEE
inline void QGrpcCommonOptions::setDeadlineTimeout(std::chrono::milliseconds t)
{
    m_timeout = t;
}

//  from ../qtgrpc/src/grpc/qgrpccommonoptions.cpp, line 30, as _ZNKR18QGrpcCommonOptions8metadataEv
#if QT_DEPRECATED_SINCE(6, 13)
inline const QHash<QByteArray, QByteArray> &QGrpcCommonOptions::metadata() const & noexcept
{
    return m_deprecatedMetadata;
}
#endif  // QT_DEPRECATED_SINCE(6, 13)

//  from ../qtgrpc/src/grpc/qgrpccommonoptions.cpp, line 54, as _ZN18QGrpcCommonOptions11setMetadataERK5QHashI10QByteArrayS1_E
#if QT_DEPRECATED_SINCE(6, 13)
inline void QGrpcCommonOptions::setMetadata(const QHash<QByteArray, QByteArray> &md)
{
    m_deprecatedMetadata = md;
    m_metadata = QMultiHash<QByteArray, QByteArray>(md);
}
#endif  // QT_DEPRECATED_SINCE(6, 13)

//  from ../qtgrpc/src/grpc/qgrpccommonoptions.cpp, line 59, as _ZN18QGrpcCommonOptions11setMetadataEO5QHashI10QByteArrayS1_E
#if QT_DEPRECATED_SINCE(6, 13)
inline void QGrpcCommonOptions::setMetadata(QHash<QByteArray, QByteArray> &&md)
{
    m_deprecatedMetadata = std::move(md);
    m_metadata = QMultiHash<QByteArray, QByteArray>(m_deprecatedMetadata);
}
#endif  // QT_DEPRECATED_SINCE(6, 13)

//  from ../qtgrpc/src/grpc/qgrpccommonoptions.cpp, line 107, as _ZNKR18QGrpcCommonOptions8metadataEN6QtGrpc12MultiValue_tE
inline const QMultiHash<QByteArray, QByteArray> &
QGrpcCommonOptions::metadata(QtGrpc::MultiValue_t /*tag*/) const & noexcept
{
    return m_metadata;
}

//  from ../qtgrpc/src/grpc/qgrpccommonoptions.cpp, line 123, as _ZN18QGrpcCommonOptions11setMetadataERK10QMultiHashI10QByteArrayS1_E
inline void QGrpcCommonOptions::setMetadata(const QMultiHash<QByteArray, QByteArray> &md)
{
    m_metadata = md;
#if QT_DEPRECATED_SINCE(6, 13)
    m_deprecatedMetadata = QtGrpcPrivate::toHash(m_metadata);
#endif
}

//  from ../qtgrpc/src/grpc/qgrpccommonoptions.cpp, line 131, as _ZN18QGrpcCommonOptions11setMetadataEO10QMultiHashI10QByteArrayS1_E
inline void QGrpcCommonOptions::setMetadata(QMultiHash<QByteArray, QByteArray> &&md)
{
    m_metadata = std::move(md);
#if QT_DEPRECATED_SINCE(6, 13)
    m_deprecatedMetadata = QtGrpcPrivate::toHash(m_metadata);
#endif
}

//  from ../qtgrpc/src/grpc/qgrpccommonoptions.cpp, line 152, as _ZN18QGrpcCommonOptions11addMetadataEO10QByteArrayS1_
inline void QGrpcCommonOptions::addMetadata(QByteArray &&key, QByteArray &&value)
{
#if QT_DEPRECATED_SINCE(6, 13)
    m_deprecatedMetadata.insertOrAssign(key, value);
#endif
    m_metadata.emplace(std::move(key), std::move(value));
}

//  from ../qtgrpc/src/grpc/qgrpccommonoptions.cpp, line 160, as _ZNK18QGrpcCommonOptions16containsMetadataE14QByteArrayViewS0_
inline bool QGrpcCommonOptions::containsMetadata(QByteArrayView key, QByteArrayView value) const
{
    const auto &md = metadata(QtGrpc::MultiValue);
    auto [f, l] = md.equal_range(key);
    return std::find(f, l, value) != l;
}

//  from ../qtgrpc/src/grpc/qgrpccommonoptions.cpp, line 179, as _ZNK18QGrpcCommonOptions20filterServerMetadataEv
inline std::optional<bool> QGrpcCommonOptions::filterServerMetadata() const noexcept
{
    return m_filterServerMetadata;
}

//  from ../qtgrpc/src/grpc/qgrpccommonoptions.cpp, line 195, as _ZN18QGrpcCommonOptions23setFilterServerMetadataEb
inline void QGrpcCommonOptions::setFilterServerMetadata(bool value)
{
    m_filterServerMetadata = value;
}

//  from ../qtgrpc/src/grpc/qgrpccommonoptions.cpp, line 217, as _ZNK18QGrpcCommonOptions25maximumReceiveMessageSizeEv
inline std::optional<quint64> QGrpcCommonOptions::maximumReceiveMessageSize() const noexcept
{
    return m_maximumReceiveMessageSize;
}

//  from ../qtgrpc/src/grpc/qgrpccommonoptions.cpp, line 243, as _ZN18QGrpcCommonOptions28setMaximumReceiveMessageSizeEy
inline void QGrpcCommonOptions::setMaximumReceiveMessageSize(quint64 size)
{
    m_maximumReceiveMessageSize = size;
}

//  from ../qtgrpc/src/grpc/qgrpccommonoptions.cpp, line 260, as _ZNK18QGrpcCommonOptions18requestCompressionEv
inline std::optional<QtGrpc::CompressionAlgorithm> QGrpcCommonOptions::requestCompression() const noexcept
{
    return m_requestCompression;
}

//  from ../qtgrpc/src/grpc/qgrpccommonoptions.cpp, line 286, as _ZN18QGrpcCommonOptions21setRequestCompressionEN6QtGrpc20CompressionAlgorithmE
inline void QGrpcCommonOptions::setRequestCompression(QtGrpc::CompressionAlgorithm algorithm)
{
    m_requestCompression = algorithm;
}
//  -----------------------------------------------------------------------

//  QGrpcCommonOptions::QGrpcCommonOptions()
extern "C" Q_DECL_EXPORT
QGrpcCommonOptions *ritual_ZN18QGrpcCommonOptionsC1Ev() {
  return new QGrpcCommonOptions();
}

//  QGrpcCommonOptions::~QGrpcCommonOptions()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QGrpcCommonOptionsD1Ev(QGrpcCommonOptions *self) {
  delete self;
}

//  std::optional<std::chrono::milliseconds>
//      QGrpcCommonOptions::deadlineTimeout() const
extern "C" Q_DECL_EXPORT
std::optional<std::chrono::milliseconds> *ritual_ZNK18QGrpcCommonOptions15deadlineTimeoutEv(
    const QGrpcCommonOptions *self) {
  return new std::optional<std::chrono::milliseconds>(
      self->deadlineTimeout());
}

//  void QGrpcCommonOptions::setDeadlineTimeout(std::chrono::milliseconds t)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QGrpcCommonOptions18setDeadlineTimeoutENSt6chrono8durationIlSt5ratioILl1ELl1000EEEE(
    QGrpcCommonOptions *self,
    long long t) {
  self->setDeadlineTimeout(std::chrono::milliseconds(t));
}

#if QT_DEPRECATED_SINCE(6, 13)
//  const QHash<QByteArray, QByteArray> &QGrpcCommonOptions::metadata() const
extern "C" Q_DECL_EXPORT
const QHash<QByteArray, QByteArray> *ritual_ZNKR18QGrpcCommonOptions8metadataEv(
    const QGrpcCommonOptions *self) {
  return &(self->metadata());
}
#endif  // QT_DEPRECATED_SINCE(6, 13)

#if QT_DEPRECATED_SINCE(6, 13)
//  void QGrpcCommonOptions::setMetadata(const QHash<QByteArray, QByteArray>
//      &md)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QGrpcCommonOptions11setMetadataERK5QHashI10QByteArrayS1_E(
    QGrpcCommonOptions *self,
    const QHash<QByteArray, QByteArray> *md) {
  self->setMetadata(*md);
}
#endif  // QT_DEPRECATED_SINCE(6, 13)

#if QT_DEPRECATED_SINCE(6, 13)
//  void QGrpcCommonOptions::setMetadata(QHash<QByteArray, QByteArray> &&md)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QGrpcCommonOptions11setMetadataEO5QHashI10QByteArrayS1_E(
    QGrpcCommonOptions *self,
    QHash<QByteArray, QByteArray> *md) {
  self->setMetadata(std::move(*md));
}
#endif  // QT_DEPRECATED_SINCE(6, 13)

//  const QMultiHash<QByteArray, QByteArray>
//      &QGrpcCommonOptions::metadata(QtGrpc::MultiValue_t a0) const
extern "C" Q_DECL_EXPORT
const QMultiHash<QByteArray, QByteArray> *ritual_ZNKR18QGrpcCommonOptions8metadataEN6QtGrpc12MultiValue_tE(
    const QGrpcCommonOptions *self,
    const QtGrpc::MultiValue_t *a0) {
  return &(self->metadata(*a0));
}

#if QT_DEPRECATED_SINCE(6, 13)
//  void QGrpcCommonOptions::setMetadata(const QMultiHash<QByteArray,
//      QByteArray> &md)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QGrpcCommonOptions11setMetadataERK10QMultiHashI10QByteArrayS1_E(
    QGrpcCommonOptions *self,
    const QMultiHash<QByteArray, QByteArray> *md) {
  self->setMetadata(*md);
}
#endif  // QT_DEPRECATED_SINCE(6, 13)

#if QT_DEPRECATED_SINCE(6, 13)
//  void QGrpcCommonOptions::setMetadata(QMultiHash<QByteArray, QByteArray>
//      &&md)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QGrpcCommonOptions11setMetadataEO10QMultiHashI10QByteArrayS1_E(
    QGrpcCommonOptions *self,
    QMultiHash<QByteArray, QByteArray> *md) {
  self->setMetadata(std::move(*md));
}
#endif  // QT_DEPRECATED_SINCE(6, 13)

//  void QGrpcCommonOptions::addMetadata(QByteArray &&key, QByteArray
//      &&value)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QGrpcCommonOptions11addMetadataEO10QByteArrayS1_(
    QGrpcCommonOptions *self,
    QByteArray *key,
    QByteArray *value) {
  self->addMetadata(std::move(*key), std::move(*value));
}

//  bool QGrpcCommonOptions::containsMetadata(QByteArrayView key,
//      QByteArrayView value) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QGrpcCommonOptions16containsMetadataE14QByteArrayViewS0_(
    const QGrpcCommonOptions *self,
    const QByteArrayView *key,
    const QByteArrayView *value) {
  return self->containsMetadata(*key, *value);
}

//  std::optional<bool> QGrpcCommonOptions::filterServerMetadata() const
extern "C" Q_DECL_EXPORT
std::optional<bool> *ritual_ZNK18QGrpcCommonOptions20filterServerMetadataEv(
    const QGrpcCommonOptions *self) {
  return new std::optional<bool>(self->filterServerMetadata());
}

//  void QGrpcCommonOptions::setFilterServerMetadata(bool value)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QGrpcCommonOptions23setFilterServerMetadataEb(
    QGrpcCommonOptions *self,
    bool value) {
  self->setFilterServerMetadata(value);
}

//  std::optional<quint64> QGrpcCommonOptions::maximumReceiveMessageSize()
//      const
extern "C" Q_DECL_EXPORT
std::optional<quint64> *ritual_ZNK18QGrpcCommonOptions25maximumReceiveMessageSizeEv(
    const QGrpcCommonOptions *self) {
  return new std::optional<quint64>(self->maximumReceiveMessageSize());
}

//  void QGrpcCommonOptions::setMaximumReceiveMessageSize(quint64 size)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QGrpcCommonOptions28setMaximumReceiveMessageSizeEy(
    QGrpcCommonOptions *self,
    quint64 size) {
  self->setMaximumReceiveMessageSize(size);
}

//  std::optional<QtGrpc::CompressionAlgorithm>
//      QGrpcCommonOptions::requestCompression() const
extern "C" Q_DECL_EXPORT
std::optional<QtGrpc::CompressionAlgorithm> *ritual_ZNK18QGrpcCommonOptions18requestCompressionEv(
    const QGrpcCommonOptions *self) {
  return new std::optional<QtGrpc::CompressionAlgorithm>(
      self->requestCompression());
}

//  void
//      QGrpcCommonOptions::setRequestCompression(QtGrpc::CompressionAlgorith
//      m algorithm)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QGrpcCommonOptions21setRequestCompressionEN6QtGrpc20CompressionAlgorithmE(
    QGrpcCommonOptions *self,
    QtGrpc::CompressionAlgorithm algorithm) {
  self->setRequestCompression(algorithm);
}

//  a std::optional<std::chrono::milliseconds> a ritual of QGrpcCommonOptions
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QGrpcCommonOptions__std_optional_std_chrono_milliseconds(
    std::optional<std::chrono::milliseconds> *self) {
  delete self;
}

//  a std::optional<bool> a ritual of QGrpcCommonOptions gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QGrpcCommonOptions__std_optional_bool(
    std::optional<bool> *self) {
  delete self;
}

//  a std::optional<quint64> a ritual of QGrpcCommonOptions gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QGrpcCommonOptions__std_optional_quint64(
    std::optional<quint64> *self) {
  delete self;
}

//  a std::optional<QtGrpc::CompressionAlgorithm> a ritual of
//      QGrpcCommonOptions gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QGrpcCommonOptions__std_optional_QtGrpc_CompressionAlgorithm(
    std::optional<QtGrpc::CompressionAlgorithm> *self) {
  delete self;
}
