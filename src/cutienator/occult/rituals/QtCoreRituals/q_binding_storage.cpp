//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qbindingstorage.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qbindingstorage.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qproperty_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QBindingStorage::QBindingStorage()
extern "C" Q_DECL_EXPORT
QBindingStorage *ritual_ZN15QBindingStorageC1Ev() {
  return new QBindingStorage();
}

//  QBindingStorage::~QBindingStorage()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QBindingStorageD1Ev(QBindingStorage *self) {
  delete self;
}

//  bool QBindingStorage::isEmpty()
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QBindingStorage7isEmptyEv(QBindingStorage *self) {
  return self->isEmpty();
}

//  bool QBindingStorage::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QBindingStorage7isValidEv(const QBindingStorage *self) {
  return self->isValid();
}

//  const QBindingStatus
//      *QBindingStorage::status(QtPrivate::QBindingStatusAccessToken a0)
//      const
extern "C" Q_DECL_EXPORT
const QBindingStatus *ritual_ZNK15QBindingStorage6statusEN9QtPrivate25QBindingStatusAccessTokenE(
    const QBindingStorage *self,
    const QtPrivate::QBindingStatusAccessToken *a0) {
  return self->status(*a0);
}

//  void QBindingStorage::registerDependency(const QUntypedPropertyData
//      *data) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK15QBindingStorage18registerDependencyEPK20QUntypedPropertyData(
    const QBindingStorage *self,
    const QUntypedPropertyData *data) {
  self->registerDependency(data);
}

//  QtPrivate::QPropertyBindingData *QBindingStorage::bindingData(const
//      QUntypedPropertyData *data) const
extern "C" Q_DECL_EXPORT
QtPrivate::QPropertyBindingData *ritual_ZNK15QBindingStorage11bindingDataEPK20QUntypedPropertyData(
    const QBindingStorage *self,
    const QUntypedPropertyData *data) {
  return self->bindingData(data);
}

//  QtPrivate::QPropertyBindingData
//      *QBindingStorage::bindingData(QUntypedPropertyData *data, bool
//      create)
extern "C" Q_DECL_EXPORT
QtPrivate::QPropertyBindingData *ritual_ZN15QBindingStorage11bindingDataEP20QUntypedPropertyDatab(
    QBindingStorage *self,
    QUntypedPropertyData *data,
    bool create) {
  return self->bindingData(data, create);
}

//  void QBindingStorage::reinitAfterThreadMove()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QBindingStorage21reinitAfterThreadMoveEv(
    QBindingStorage *self) {
  self->reinitAfterThreadMove();
}

//  void QBindingStorage::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QBindingStorage5clearEv(QBindingStorage *self) {
  self->clear();
}

//  void QBindingStorage::registerDependency_helper(const
//      QUntypedPropertyData *data) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK15QBindingStorage25registerDependency_helperEPK20QUntypedPropertyData(
    const QBindingStorage *self,
    const QUntypedPropertyData *data) {
  self->registerDependency_helper(data);
}

//  QtPrivate::QPropertyBindingData
//      *QBindingStorage::bindingData_helper(const QUntypedPropertyData
//      *data) const
extern "C" Q_DECL_EXPORT
QtPrivate::QPropertyBindingData *ritual_ZNK15QBindingStorage18bindingData_helperEPK20QUntypedPropertyData(
    const QBindingStorage *self,
    const QUntypedPropertyData *data) {
  return self->bindingData_helper(data);
}

//  QtPrivate::QPropertyBindingData
//      *QBindingStorage::bindingData_helper(QUntypedPropertyData *data, bool
//      create)
extern "C" Q_DECL_EXPORT
QtPrivate::QPropertyBindingData *ritual_ZN15QBindingStorage18bindingData_helperEP20QUntypedPropertyDatab(
    QBindingStorage *self,
    QUntypedPropertyData *data,
    bool create) {
  return self->bindingData_helper(data, create);
}
