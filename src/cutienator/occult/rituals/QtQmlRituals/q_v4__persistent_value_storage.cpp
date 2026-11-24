//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4persistent_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4persistent_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::PersistentValueStorage::free(Value *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV422PersistentValueStorage4freeEPNS_5ValueE(QV4::Value *v) {
  QV4::PersistentValueStorage::free(v);
}

//  ExecutionEngine *QV4::PersistentValueStorage::getEngine(const Value *v)
extern "C" Q_DECL_EXPORT
QV4::ExecutionEngine *ritual_ZN3QV422PersistentValueStorage9getEngineEPKNS_5ValueE(
    const QV4::Value *v) {
  return QV4::PersistentValueStorage::getEngine(v);
}
