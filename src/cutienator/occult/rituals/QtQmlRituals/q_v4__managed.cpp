//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4managed_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4managed_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  const QV4::VTable *QV4::Managed::staticVTable()
extern "C" Q_DECL_EXPORT
const QV4::VTable *ritual_ZN3QV47Managed12staticVTableEv() {
  return QV4::Managed::staticVTable();
}

//  void QV4::Managed::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV47Managed10__dataTestEv(QV4::Managed *self) {
  self->__dataTest();
}

//  QV4::Heap::Base *QV4::Managed::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::Base *ritual_ZNK3QV47Managed11d_uncheckedEv(
    const QV4::Managed *self) {
  return self->d_unchecked();
}

//  QV4::Heap::Base *QV4::Managed::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::Base *ritual_ZNK3QV47Managed1dEv(const QV4::Managed *self) {
  return self->d();
}

//  Heap::InternalClass *QV4::Managed::internalClass() const
extern "C" Q_DECL_EXPORT
QV4::Heap::InternalClass *ritual_ZNK3QV47Managed13internalClassEv(
    const QV4::Managed *self) {
  return self->internalClass();
}

//  const VTable *QV4::Managed::vtable() const
extern "C" Q_DECL_EXPORT
const QV4::VTable *ritual_ZNK3QV47Managed6vtableEv(
    const QV4::Managed *self) {
  return self->vtable();
}

//  ExecutionEngine *QV4::Managed::engine() const
extern "C" Q_DECL_EXPORT
QV4::ExecutionEngine *ritual_ZNK3QV47Managed6engineEv(
    const QV4::Managed *self) {
  return self->engine();
}

//  bool QV4::Managed::isV4SequenceType() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV47Managed16isV4SequenceTypeEv(const QV4::Managed *self) {
  return self->isV4SequenceType();
}

//  bool QV4::Managed::isV4QObjectWrapper() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV47Managed18isV4QObjectWrapperEv(const QV4::Managed *self) {
  return self->isV4QObjectWrapper();
}

//  bool QV4::Managed::isQmlListPropertyType() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV47Managed21isQmlListPropertyTypeEv(
    const QV4::Managed *self) {
  return self->isQmlListPropertyType();
}

//  bool QV4::Managed::isArrayLike() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV47Managed11isArrayLikeEv(const QV4::Managed *self) {
  return self->isArrayLike();
}

//  bool QV4::Managed::isArrayObject() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV47Managed13isArrayObjectEv(const QV4::Managed *self) {
  return self->isArrayObject();
}

//  bool QV4::Managed::isStringObject() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV47Managed14isStringObjectEv(const QV4::Managed *self) {
  return self->isStringObject();
}

//  bool QV4::Managed::isSymbolObject() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV47Managed14isSymbolObjectEv(const QV4::Managed *self) {
  return self->isSymbolObject();
}

//  bool QV4::Managed::isEqualTo(const Managed *other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV47Managed9isEqualToEPKS0_(
    const QV4::Managed *self,
    const QV4::Managed *other) {
  return self->isEqualTo(other);
}

//  bool QV4::Managed::inUse() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV47Managed5inUseEv(const QV4::Managed *self) {
  return self->inUse();
}

//  bool QV4::Managed::markBit() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV47Managed7markBitEv(const QV4::Managed *self) {
  return self->markBit();
}

//  void QV4::Managed::mark(MarkStack *markStack)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV47Managed4markEPNS_9MarkStackE(
    QV4::Managed *self,
    QV4::MarkStack *markStack) {
  self->mark(markStack);
}

//  Heap::Base *QV4::Managed::heapObject() const
extern "C" Q_DECL_EXPORT
QV4::Heap::Base *ritual_ZNK3QV47Managed10heapObjectEv(
    const QV4::Managed *self) {
  return self->heapObject();
}

//  QV4::Managed as the QV4::VTableBase it is built on
extern "C" Q_DECL_EXPORT
QV4::VTableBase *ritual_cast_QV4_Managed_QV4_VTableBase(QV4::Managed *self) {
  return static_cast<QV4::VTableBase *>(self);
}
