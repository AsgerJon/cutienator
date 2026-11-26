//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4persistent_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4persistent_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QV4::PersistentValueStorage::PersistentValueStorage(ExecutionEngine
//      *engine)
extern "C" Q_DECL_EXPORT
QV4::PersistentValueStorage *ritual_ZN3QV422PersistentValueStorageC1EPNS_15ExecutionEngineE(
    QV4::ExecutionEngine *engine) {
  return new QV4::PersistentValueStorage(engine);
}

//  QV4::PersistentValueStorage::~PersistentValueStorage()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV422PersistentValueStorageD1Ev(
    QV4::PersistentValueStorage *self) {
  delete self;
}

//  Value *QV4::PersistentValueStorage::allocate()
extern "C" Q_DECL_EXPORT
QV4::Value *ritual_ZN3QV422PersistentValueStorage8allocateEv(
    QV4::PersistentValueStorage *self) {
  return self->allocate();
}

//  void QV4::PersistentValueStorage::free(Value *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV422PersistentValueStorage4freeEPNS_5ValueE(QV4::Value *v) {
  QV4::PersistentValueStorage::free(v);
}

//  void QV4::PersistentValueStorage::mark(MarkStack *markStack)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV422PersistentValueStorage4markEPNS_9MarkStackE(
    QV4::PersistentValueStorage *self,
    QV4::MarkStack *markStack) {
  self->mark(markStack);
}

//  void QV4::PersistentValueStorage::clearFreePageHint()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV422PersistentValueStorage17clearFreePageHintEv(
    QV4::PersistentValueStorage *self) {
  self->clearFreePageHint();
}

//  ExecutionEngine *QV4::PersistentValueStorage::getEngine(const Value *v)
extern "C" Q_DECL_EXPORT
QV4::ExecutionEngine *ritual_ZN3QV422PersistentValueStorage9getEngineEPKNS_5ValueE(
    const QV4::Value *v) {
  return QV4::PersistentValueStorage::getEngine(v);
}

//  void QV4::PersistentValueStorage::freeUnchecked(Value *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV422PersistentValueStorage13freeUncheckedEPNS_5ValueE(
    QV4::Value *v) {
  QV4::PersistentValueStorage::freeUnchecked(v);
}

//  void QV4::PersistentValueStorage::freePage(void *page)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV422PersistentValueStorage8freePageEPv(void *page) {
  QV4::PersistentValueStorage::freePage(page);
}
