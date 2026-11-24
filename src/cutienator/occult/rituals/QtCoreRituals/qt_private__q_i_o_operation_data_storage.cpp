//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qiooperation_p_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qiooperation_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>

//  QtPrivate::QIOOperationDataStorage::QIOOperationDataStorage()
extern "C" Q_DECL_EXPORT
QtPrivate::QIOOperationDataStorage *ritual_ZN9QtPrivate23QIOOperationDataStorageC1Ev() {
  return new QtPrivate::QIOOperationDataStorage();
}

//  QtPrivate::QIOOperationDataStorage::QIOOperationDataStorage(const
//      QByteArray &a)
extern "C" Q_DECL_EXPORT
QtPrivate::QIOOperationDataStorage *ritual_ZN9QtPrivate23QIOOperationDataStorageC1ERK10QByteArray(
    const QByteArray *a) {
  return new QtPrivate::QIOOperationDataStorage(*a);
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
