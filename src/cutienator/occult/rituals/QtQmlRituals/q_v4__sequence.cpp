//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4sequenceobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4sequenceobject_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4propertykey_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetasequence.h>
#include <QtQml/private/qv4sequenceobject_p.h>
#include <QtQml/private/qv4functionobject_p.h>
#include <QtQml/private/qv4arrayobject_p.h>
#include <QtQml/private/qqmlengine_p.h>
#include <QtQml/private/qv4scopedvalue_p.h>
#include <QtQml/private/qv4jscall_p.h>
#include <QtQml/private/qqmlmetatype_p.h>
#include <QtQml/private/qqmltype_p_p.h>
#include <QtQml/private/qqmlvaluetypewrapper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4sequenceobject.cpp, line 289, as _ZN3QV44Heap8Sequence7destroyEv
namespace QV4 {
inline void Heap::Sequence::destroy()
{
    if (isStoredInline() && m_container)
        listType().destroy(m_container);
    ReferenceObject::destroy();
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  const QV4::VTable *QV4::Sequence::staticVTable()
extern "C" Q_DECL_EXPORT
const QV4::VTable *ritual_ZN3QV48Sequence12staticVTableEv() {
  return QV4::Sequence::staticVTable();
}

//  void QV4::Sequence::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Sequence10__dataTestEv(QV4::Sequence *self) {
  self->__dataTest();
}

//  QV4::Heap::Sequence *QV4::Sequence::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::Sequence *ritual_ZNK3QV48Sequence11d_uncheckedEv(
    const QV4::Sequence *self) {
  return self->d_unchecked();
}

//  QV4::Heap::Sequence *QV4::Sequence::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::Sequence *ritual_ZNK3QV48Sequence1dEv(const QV4::Sequence *self) {
  return self->d();
}

//  QV4::Object *QV4::Sequence::defaultPrototype(QV4::ExecutionEngine *e)
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZN3QV48Sequence16defaultPrototypeEPNS_15ExecutionEngineE(
    QV4::ExecutionEngine *e) {
  return QV4::Sequence::defaultPrototype(e);
}

//  void QV4::Sequence::virtualDestroy(QV4::Heap::Base *b)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Sequence14virtualDestroyEPNS_4Heap4BaseE(
    QV4::Heap::Base *b) {
  QV4::Sequence::virtualDestroy(b);
}

//  QV4::ReturnedValue QV4::Sequence::virtualGet(const QV4::Managed *that,
//      PropertyKey id, const Value *receiver, bool *hasProperty)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV48Sequence10virtualGetEPKNS_7ManagedENS_11PropertyKeyEPKNS_5ValueEPb(
    const QV4::Managed *that,
    const QV4::PropertyKey *id,
    const QV4::Value *receiver,
    bool *hasProperty) {
  return QV4::Sequence::virtualGet(that, *id, receiver, hasProperty);
}

//  qint64 QV4::Sequence::virtualGetLength(const Managed *m)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN3QV48Sequence16virtualGetLengthEPKNS_7ManagedE(
    const QV4::Managed *m) {
  return QV4::Sequence::virtualGetLength(m);
}

//  bool QV4::Sequence::virtualPut(Managed *that, PropertyKey id, const
//      QV4::Value &value, Value *receiver)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Sequence10virtualPutEPNS_7ManagedENS_11PropertyKeyERKNS_5ValueEPS4_(
    QV4::Managed *that,
    const QV4::PropertyKey *id,
    const QV4::Value *value,
    QV4::Value *receiver) {
  return QV4::Sequence::virtualPut(that, *id, *value, receiver);
}

//  bool QV4::Sequence::virtualDeleteProperty(QV4::Managed *that, PropertyKey
//      id)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Sequence21virtualDeletePropertyEPNS_7ManagedENS_11PropertyKeyE(
    QV4::Managed *that,
    const QV4::PropertyKey *id) {
  return QV4::Sequence::virtualDeleteProperty(that, *id);
}

//  bool QV4::Sequence::virtualIsEqualTo(Managed *that, Managed *other)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Sequence16virtualIsEqualToEPNS_7ManagedES2_(
    QV4::Managed *that,
    QV4::Managed *other) {
  return QV4::Sequence::virtualIsEqualTo(that, other);
}

//  QV4::OwnPropertyKeyIterator *QV4::Sequence::virtualOwnPropertyKeys(const
//      Object *m, Value *target)
extern "C" Q_DECL_EXPORT
QV4::OwnPropertyKeyIterator *ritual_ZN3QV48Sequence22virtualOwnPropertyKeysEPKNS_6ObjectEPNS_5ValueE(
    const QV4::Object *m,
    QV4::Value *target) {
  return QV4::Sequence::virtualOwnPropertyKeys(m, target);
}

//  int QV4::Sequence::virtualMetacall(Object *object, QMetaObject::Call
//      call, int index, void **a)
extern "C" Q_DECL_EXPORT
int ritual_ZN3QV48Sequence15virtualMetacallEPNS_6ObjectEN11QMetaObject4CallEiPPv(
    QV4::Object *object,
    QMetaObject::Call call,
    int index,
    void **a) {
  return QV4::Sequence::virtualMetacall(object, call, index, a);
}
