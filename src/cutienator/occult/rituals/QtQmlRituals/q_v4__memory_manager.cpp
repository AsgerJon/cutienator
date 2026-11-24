//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4mm_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4mm_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::MemoryManager::changeUnmanagedHeapSizeUsage(qptrdiff delta)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV413MemoryManager28changeUnmanagedHeapSizeUsageEx(
    QV4::MemoryManager *self,
    qptrdiff delta) {
  self->changeUnmanagedHeapSizeUsage(delta);
}

//  MarkStack *QV4::MemoryManager::markStack()
extern "C" Q_DECL_EXPORT
QV4::MarkStack *ritual_ZN3QV413MemoryManager9markStackEv(
    QV4::MemoryManager *self) {
  return self->markStack();
}

//  bool QV4::MemoryManager::isAboveUnmanagedHeapLimit()
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV413MemoryManager25isAboveUnmanagedHeapLimitEv(
    QV4::MemoryManager *self) {
  return self->isAboveUnmanagedHeapLimit();
}
