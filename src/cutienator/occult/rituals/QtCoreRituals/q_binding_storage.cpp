//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qbindingstorage.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qbindingstorage.h>

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

//  void QBindingStorage::registerDependency(const QUntypedPropertyData
//      *data) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK15QBindingStorage18registerDependencyEPK20QUntypedPropertyData(
    const QBindingStorage *self,
    const QUntypedPropertyData *data) {
  self->registerDependency(data);
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
