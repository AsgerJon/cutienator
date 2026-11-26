//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmllistwrapper_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmllistwrapper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtQml/qqmlproperty.h>
#include <QtCore/qvariant.h>
#include <QtQml/qqmllist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4propertykey_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qqmllistwrapper_p.h>
#include <QtQml/qqmlinfo.h>
#include <QtQml/private/qqmlproperty_p.h>
#include <QtQml/private/qqmllist_p.h>
#include <QtQml/private/qv4arrayiterator_p.h>
#include <QtQml/private/qv4arrayobject_p.h>
#include <QtQml/private/qv4functionobject_p.h>
#include <QtQml/private/qv4objectiterator_p.h>
#include <QtQml/private/qv4objectproto_p.h>
#include <QtQml/private/qv4qobjectwrapper_p.h>
#include <QtQml/private/qv4symbol_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from ../qtdeclarative/src/qml/qml/qqmllistwrapper.cpp, line 140, as _ZN3QV44Heap14QmlListWrapper7destroyEv
namespace QV4 {
using namespace Qt::StringLiterals;
inline void Heap::QmlListWrapper::destroy()
{
    m_object.destroy();
    Object::destroy();
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  const QV4::VTable *QV4::QmlListWrapper::staticVTable()
extern "C" Q_DECL_EXPORT
const QV4::VTable *ritual_ZN3QV414QmlListWrapper12staticVTableEv() {
  return QV4::QmlListWrapper::staticVTable();
}

//  void QV4::QmlListWrapper::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV414QmlListWrapper10__dataTestEv(QV4::QmlListWrapper *self) {
  self->__dataTest();
}

//  QV4::Heap::QmlListWrapper *QV4::QmlListWrapper::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::QmlListWrapper *ritual_ZNK3QV414QmlListWrapper11d_uncheckedEv(
    const QV4::QmlListWrapper *self) {
  return self->d_unchecked();
}

//  QV4::Heap::QmlListWrapper *QV4::QmlListWrapper::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::QmlListWrapper *ritual_ZNK3QV414QmlListWrapper1dEv(
    const QV4::QmlListWrapper *self) {
  return self->d();
}

//  void QV4::QmlListWrapper::virtualDestroy(QV4::Heap::Base *b)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV414QmlListWrapper14virtualDestroyEPNS_4Heap4BaseE(
    QV4::Heap::Base *b) {
  QV4::QmlListWrapper::virtualDestroy(b);
}

//  QV4::Object *QV4::QmlListWrapper::defaultPrototype(QV4::ExecutionEngine
//      *e)
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZN3QV414QmlListWrapper16defaultPrototypeEPNS_15ExecutionEngineE(
    QV4::ExecutionEngine *e) {
  return QV4::QmlListWrapper::defaultPrototype(e);
}

//  ReturnedValue QV4::QmlListWrapper::create(ExecutionEngine *engine,
//      QObject *object, int propId, QMetaType propType)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV414QmlListWrapper6createEPNS_15ExecutionEngineEP7QObjecti9QMetaType(
    QV4::ExecutionEngine *engine,
    QObject *object,
    int propId,
    const QMetaType *propType) {
  return QV4::QmlListWrapper::create(engine, object, propId, *propType);
}

//  ReturnedValue QV4::QmlListWrapper::create(ExecutionEngine *engine, const
//      QQmlListProperty<QObject> &prop, QMetaType propType)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV414QmlListWrapper6createEPNS_15ExecutionEngineERK16QQmlListPropertyI7QObjectE9QMetaType(
    QV4::ExecutionEngine *engine,
    const QQmlListProperty<QObject> *prop,
    const QMetaType *propType) {
  return QV4::QmlListWrapper::create(engine, *prop, *propType);
}

//  ReturnedValue QV4::QmlListWrapper::create(ExecutionEngine *engine,
//      QMetaType propType)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV414QmlListWrapper6createEPNS_15ExecutionEngineE9QMetaType(
    QV4::ExecutionEngine *engine,
    const QMetaType *propType) {
  return QV4::QmlListWrapper::create(engine, *propType);
}

//  ReturnedValue QV4::QmlListWrapper::createOwned(ExecutionEngine *engine,
//      const QQmlProperty &prop)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV414QmlListWrapper11createOwnedEPNS_15ExecutionEngineERK12QQmlProperty(
    QV4::ExecutionEngine *engine,
    const QQmlProperty *prop) {
  return QV4::QmlListWrapper::createOwned(engine, *prop);
}

//  QVariant QV4::QmlListWrapper::toVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK3QV414QmlListWrapper9toVariantEv(
    const QV4::QmlListWrapper *self) {
  return new QVariant(self->toVariant());
}

//  QQmlListReference QV4::QmlListWrapper::toListReference() const
extern "C" Q_DECL_EXPORT
QQmlListReference *ritual_ZNK3QV414QmlListWrapper15toListReferenceEv(
    const QV4::QmlListWrapper *self) {
  return new QQmlListReference(self->toListReference());
}

//  ReturnedValue QV4::QmlListWrapper::virtualGet(const Managed *m,
//      PropertyKey id, const Value *receiver, bool *hasProperty)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV414QmlListWrapper10virtualGetEPKNS_7ManagedENS_11PropertyKeyEPKNS_5ValueEPb(
    const QV4::Managed *m,
    const QV4::PropertyKey *id,
    const QV4::Value *receiver,
    bool *hasProperty) {
  return QV4::QmlListWrapper::virtualGet(m, *id, receiver, hasProperty);
}

//  qint64 QV4::QmlListWrapper::virtualGetLength(const Managed *m)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN3QV414QmlListWrapper16virtualGetLengthEPKNS_7ManagedE(
    const QV4::Managed *m) {
  return QV4::QmlListWrapper::virtualGetLength(m);
}

//  bool QV4::QmlListWrapper::virtualPut(Managed *m, PropertyKey id, const
//      Value &value, Value *receiver)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV414QmlListWrapper10virtualPutEPNS_7ManagedENS_11PropertyKeyERKNS_5ValueEPS4_(
    QV4::Managed *m,
    const QV4::PropertyKey *id,
    const QV4::Value *value,
    QV4::Value *receiver) {
  return QV4::QmlListWrapper::virtualPut(m, *id, *value, receiver);
}

//  OwnPropertyKeyIterator *QV4::QmlListWrapper::virtualOwnPropertyKeys(const
//      Object *m, Value *target)
extern "C" Q_DECL_EXPORT
QV4::OwnPropertyKeyIterator *ritual_ZN3QV414QmlListWrapper22virtualOwnPropertyKeysEPKNS_6ObjectEPNS_5ValueE(
    const QV4::Object *m,
    QV4::Value *target) {
  return QV4::QmlListWrapper::virtualOwnPropertyKeys(m, target);
}
