//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4managed_p.h, Qt 6.12.0. Edited by hand on
//  2026-11-25: added by hand, instances of templates of the class: 8. Kept
//  as it is when the generator runs again.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4managed_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

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

//  QString QV4::Managed::typeToString(Type a0)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN3QV47Managed12typeToStringENS0_4TypeE(
    QV4::Managed::Type a0) {
  return new QString(QV4::Managed::typeToString(a0));
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

//  QString QV4::Managed::className() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK3QV47Managed9classNameEv(const QV4::Managed *self) {
  return new QString(self->className());
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

//  bool QV4::Managed::virtualIsEqualTo(Managed *m, Managed *other)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV47Managed16virtualIsEqualToEPS0_S1_(
    QV4::Managed *m,
    QV4::Managed *other) {
  return QV4::Managed::virtualIsEqualTo(m, other);
}

//  QV4::Managed as the QV4::VTableBase it is built on
extern "C" Q_DECL_EXPORT
QV4::VTableBase *ritual_cast_QV4_Managed_QV4_VTableBase(QV4::Managed *self) {
  return static_cast<QV4::VTableBase *>(self);
}

#include <QtQml/6.12.0/QtQml/private/qv4object_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4string_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4functionobject_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4arrayobject_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4errorobject_p.h>

//  QV4::Object *QV4::Managed::cast<QV4::Object>()
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZN3QV47Managed4castINS_6ObjectEEEPT_v(
    QV4::Managed *self) {
  return self->cast<QV4::Object>();
}

//  QV4::FunctionObject *QV4::Managed::cast<QV4::FunctionObject>()
extern "C" Q_DECL_EXPORT
QV4::FunctionObject *ritual_ZN3QV47Managed4castINS_14FunctionObjectEEEPT_v(
    QV4::Managed *self) {
  return self->cast<QV4::FunctionObject>();
}

//  QV4::String *QV4::Managed::cast<QV4::String>()
extern "C" Q_DECL_EXPORT
QV4::String *ritual_ZN3QV47Managed4castINS_6StringEEEPT_v(
    QV4::Managed *self) {
  return self->cast<QV4::String>();
}

//  QV4::ArrayObject *QV4::Managed::cast<QV4::ArrayObject>()
extern "C" Q_DECL_EXPORT
QV4::ArrayObject *ritual_ZN3QV47Managed4castINS_11ArrayObjectEEEPT_v(
    QV4::Managed *self) {
  return self->cast<QV4::ArrayObject>();
}

//  QV4::ErrorObject *QV4::Managed::cast<QV4::ErrorObject>()
extern "C" Q_DECL_EXPORT
QV4::ErrorObject *ritual_ZN3QV47Managed4castINS_11ErrorObjectEEEPT_v(
    QV4::Managed *self) {
  return self->cast<QV4::ErrorObject>();
}

//  const QV4::Object *QV4::Managed::cast<QV4::Object>() const
extern "C" Q_DECL_EXPORT
const QV4::Object *ritual_ZNK3QV47Managed4castINS_6ObjectEEEPKT_v(
    const QV4::Managed *self) {
  return self->cast<QV4::Object>();
}

//  const QV4::FunctionObject *QV4::Managed::cast<QV4::FunctionObject>()
//      const
extern "C" Q_DECL_EXPORT
const QV4::FunctionObject *ritual_ZNK3QV47Managed4castINS_14FunctionObjectEEEPKT_v(
    const QV4::Managed *self) {
  return self->cast<QV4::FunctionObject>();
}

//  const QV4::String *QV4::Managed::cast<QV4::String>() const
extern "C" Q_DECL_EXPORT
const QV4::String *ritual_ZNK3QV47Managed4castINS_6StringEEEPKT_v(
    const QV4::Managed *self) {
  return self->cast<QV4::String>();
}
