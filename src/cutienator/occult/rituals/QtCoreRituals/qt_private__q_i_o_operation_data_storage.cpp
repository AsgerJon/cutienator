//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qiooperation_p_p.h, Qt 6.12.0. Edited by
//  hand on 2026-11-25: added by hand, instances of templates of the class:
//  1. Kept as it is when the generator runs again.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(async_io)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qiooperation_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/QSpan>
#include <cstddef>

//  QtPrivate::QIOOperationDataStorage::QIOOperationDataStorage()
extern "C" Q_DECL_EXPORT
QtPrivate::QIOOperationDataStorage *ritual_ZN9QtPrivate23QIOOperationDataStorageC1Ev() {
  return new QtPrivate::QIOOperationDataStorage();
}

//  QtPrivate::QIOOperationDataStorage::QIOOperationDataStorage(QSpan<const
//      QSpan<std::byte>> s)
extern "C" Q_DECL_EXPORT
QtPrivate::QIOOperationDataStorage *ritual_ZN9QtPrivate23QIOOperationDataStorageC1E5QSpanIKS1_ISt4byteLm18446744073709551615EELm18446744073709551615EE(
    const QSpan<const QSpan<std::byte>> *s) {
  return new QtPrivate::QIOOperationDataStorage(*s);
}

//  QtPrivate::QIOOperationDataStorage::QIOOperationDataStorage(QSpan<const
//      QSpan<const std::byte>> s)
extern "C" Q_DECL_EXPORT
QtPrivate::QIOOperationDataStorage *ritual_ZN9QtPrivate23QIOOperationDataStorageC1E5QSpanIKS1_IKSt4byteLm18446744073709551615EELm18446744073709551615EE(
    const QSpan<const QSpan<const std::byte>> *s) {
  return new QtPrivate::QIOOperationDataStorage(*s);
}

//  QtPrivate::QIOOperationDataStorage::QIOOperationDataStorage(const
//      QByteArray &a)
extern "C" Q_DECL_EXPORT
QtPrivate::QIOOperationDataStorage *ritual_ZN9QtPrivate23QIOOperationDataStorageC1ERK10QByteArray(
    const QByteArray *a) {
  return new QtPrivate::QIOOperationDataStorage(*a);
}

//  QtPrivate::QIOOperationDataStorage::QIOOperationDataStorage(QByteArray
//      &&a)
extern "C" Q_DECL_EXPORT
QtPrivate::QIOOperationDataStorage *ritual_ZN9QtPrivate23QIOOperationDataStorageC1EO10QByteArray(
    QByteArray *a) {
  return new QtPrivate::QIOOperationDataStorage(std::move(*a));
}

//  bool QtPrivate::QIOOperationDataStorage::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QtPrivate23QIOOperationDataStorage7isEmptyEv(
    const QtPrivate::QIOOperationDataStorage *self) {
  return self->isEmpty();
}

//  bool QtPrivate::QIOOperationDataStorage::containsReadSpans() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QtPrivate23QIOOperationDataStorage17containsReadSpansEv(
    const QtPrivate::QIOOperationDataStorage *self) {
  return self->containsReadSpans();
}

//  bool QtPrivate::QIOOperationDataStorage::containsWriteSpans() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QtPrivate23QIOOperationDataStorage18containsWriteSpansEv(
    const QtPrivate::QIOOperationDataStorage *self) {
  return self->containsWriteSpans();
}

//  bool QtPrivate::QIOOperationDataStorage::containsByteArray() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QtPrivate23QIOOperationDataStorage17containsByteArrayEv(
    const QtPrivate::QIOOperationDataStorage *self) {
  return self->containsByteArray();
}

//  ReadSpans &QtPrivate::QIOOperationDataStorage::getReadSpans()
extern "C" Q_DECL_EXPORT
QtPrivate::QIOOperationDataStorage::ReadSpans *ritual_ZN9QtPrivate23QIOOperationDataStorage12getReadSpansEv(
    QtPrivate::QIOOperationDataStorage *self) {
  return &(self->getReadSpans());
}

//  const ReadSpans &QtPrivate::QIOOperationDataStorage::getReadSpans() const
extern "C" Q_DECL_EXPORT
const QtPrivate::QIOOperationDataStorage::ReadSpans *ritual_ZNK9QtPrivate23QIOOperationDataStorage12getReadSpansEv(
    const QtPrivate::QIOOperationDataStorage *self) {
  return &(self->getReadSpans());
}

//  WriteSpans &QtPrivate::QIOOperationDataStorage::getWriteSpans()
extern "C" Q_DECL_EXPORT
QtPrivate::QIOOperationDataStorage::WriteSpans *ritual_ZN9QtPrivate23QIOOperationDataStorage13getWriteSpansEv(
    QtPrivate::QIOOperationDataStorage *self) {
  return &(self->getWriteSpans());
}

//  const WriteSpans &QtPrivate::QIOOperationDataStorage::getWriteSpans()
//      const
extern "C" Q_DECL_EXPORT
const QtPrivate::QIOOperationDataStorage::WriteSpans *ritual_ZNK9QtPrivate23QIOOperationDataStorage13getWriteSpansEv(
    const QtPrivate::QIOOperationDataStorage *self) {
  return &(self->getWriteSpans());
}

//  QByteArray &QtPrivate::QIOOperationDataStorage::getByteArray()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN9QtPrivate23QIOOperationDataStorage12getByteArrayEv(
    QtPrivate::QIOOperationDataStorage *self) {
  return &(self->getByteArray());
}

//  const QByteArray &QtPrivate::QIOOperationDataStorage::getByteArray()
//      const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK9QtPrivate23QIOOperationDataStorage12getByteArrayEv(
    const QtPrivate::QIOOperationDataStorage *self) {
  return new QByteArray(self->getByteArray());
}

//  QtPrivate::QIOOperationDataStorage::~QIOOperationDataStorage()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate23QIOOperationDataStorageD1Ev(
    QtPrivate::QIOOperationDataStorage *self) {
  delete self;
}

//  QByteArray QtPrivate::QIOOperationDataStorage::getValue<QByteArray>()
//      const
extern "C" Q_DECL_EXPORT
QByteArray * ritual_ZNK9QtPrivate23QIOOperationDataStorage8getValueI10QByteArrayEET_v(
    const QtPrivate::QIOOperationDataStorage *self) {
  return new QByteArray(self->getValue<QByteArray>());
}

#endif  // QT_CONFIG(async_io)
