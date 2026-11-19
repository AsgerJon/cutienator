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
