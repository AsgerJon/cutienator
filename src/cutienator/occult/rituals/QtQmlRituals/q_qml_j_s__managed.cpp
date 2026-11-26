//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmljsmemorypool_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmljsmemorypool_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QQmlJS::Managed::Managed()
extern "C" Q_DECL_EXPORT
QQmlJS::Managed *ritual_ZN6QQmlJS7ManagedC1Ev(QQmlJS::MemoryPool *pool) {
  return new (pool) QQmlJS::Managed();
}

//  QQmlJS::Managed::~Managed()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS7ManagedD1Ev(QQmlJS::Managed *self) {
  delete self;
}

//  void *QQmlJS::Managed::operator new(size_t size, MemoryPool *pool)
extern "C" Q_DECL_EXPORT
void *ritual_ZN6QQmlJS7ManagednwEmPNS_10MemoryPoolE(
    QQmlJS::Managed *self,
    size_t size,
    QQmlJS::MemoryPool *pool) {
  return self->operator new(size, pool);
}

//  void QQmlJS::Managed::operator delete(void *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS7ManageddlEPv(QQmlJS::Managed *self, void *a0) {
  self->operator delete(a0);
}

//  void QQmlJS::Managed::operator delete(void *a0, MemoryPool *a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS7ManageddlEPvPNS_10MemoryPoolE(
    QQmlJS::Managed *self,
    void *a0,
    QQmlJS::MemoryPool *a1) {
  self->operator delete(a0, a1);
}
