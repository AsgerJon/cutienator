//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4qmlcontext_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4qmlcontext_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4propertykey_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4qmlcontext_p.h>
#include <QtQml/private/qjsvalue_p.h>
#include <QtQml/private/qqmlcontext_p.h>
#include <QtQml/private/qqmlengine_p.h>
#include <QtQml/private/qqmlglobal_p.h>
#include <QtQml/private/qqmljavascriptexpression_p.h>
#include <QtQml/private/qqmllistwrapper_p.h>
#include <QtQml/private/qqmltypewrapper_p.h>
#include <QtQml/private/qv4compileddata_p.h>
#include <QtQml/private/qv4engine_p.h>
#include <QtQml/private/qv4function_p.h>
#include <QtQml/private/qv4identifiertable_p.h>
#include <QtQml/private/qv4lookup_p.h>
#include <QtQml/private/qv4mm_p.h>
#include <QtQml/private/qv4module_p.h>
#include <QtQml/private/qv4objectproto_p.h>
#include <QtQml/private/qv4qobjectwrapper_p.h>
#include <QtQml/private/qv4stackframe_p.h>
#include <QtQml/private/qv4value_p.h>
#include <QtCore/qloggingcategory.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4qmlcontext.cpp, line 44, as _ZN3QV44Heap18QQmlContextWrapper7destroyEv
namespace QV4 {
inline void Heap::QQmlContextWrapper::destroy()
{
    context->release();
    context = nullptr;
    scopeObject.destroy();
    Object::destroy();
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  const QV4::VTable *QV4::QQmlContextWrapper::staticVTable()
extern "C" Q_DECL_EXPORT
const QV4::VTable *ritual_ZN3QV418QQmlContextWrapper12staticVTableEv() {
  return QV4::QQmlContextWrapper::staticVTable();
}

//  void QV4::QQmlContextWrapper::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV418QQmlContextWrapper10__dataTestEv(
    QV4::QQmlContextWrapper *self) {
  self->__dataTest();
}

//  QV4::Heap::QQmlContextWrapper *QV4::QQmlContextWrapper::d_unchecked()
//      const
extern "C" Q_DECL_EXPORT
QV4::Heap::QQmlContextWrapper *ritual_ZNK3QV418QQmlContextWrapper11d_uncheckedEv(
    const QV4::QQmlContextWrapper *self) {
  return self->d_unchecked();
}

//  QV4::Heap::QQmlContextWrapper *QV4::QQmlContextWrapper::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::QQmlContextWrapper *ritual_ZNK3QV418QQmlContextWrapper1dEv(
    const QV4::QQmlContextWrapper *self) {
  return self->d();
}

//  void QV4::QQmlContextWrapper::virtualDestroy(QV4::Heap::Base *b)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV418QQmlContextWrapper14virtualDestroyEPNS_4Heap4BaseE(
    QV4::Heap::Base *b) {
  QV4::QQmlContextWrapper::virtualDestroy(b);
}

//  Heap::InternalClass
//      *QV4::QQmlContextWrapper::defaultInternalClass(QV4::EngineBase *e)
extern "C" Q_DECL_EXPORT
QV4::Heap::InternalClass *ritual_ZN3QV418QQmlContextWrapper20defaultInternalClassEPNS_10EngineBaseE(
    QV4::EngineBase *e) {
  return QV4::QQmlContextWrapper::defaultInternalClass(e);
}

//  QObject *QV4::QQmlContextWrapper::getScopeObject() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK3QV418QQmlContextWrapper14getScopeObjectEv(
    const QV4::QQmlContextWrapper *self) {
  return self->getScopeObject();
}

//  QQmlRefPointer<QQmlContextData> QV4::QQmlContextWrapper::getContext()
//      const
extern "C" Q_DECL_EXPORT
QQmlRefPointer<QQmlContextData> *ritual_ZNK3QV418QQmlContextWrapper10getContextEv(
    const QV4::QQmlContextWrapper *self) {
  return new QQmlRefPointer<QQmlContextData>(self->getContext());
}

//  ReturnedValue QV4::QQmlContextWrapper::getPropertyAndBase(const
//      QQmlContextWrapper *resource, PropertyKey id, const Value *receiver,
//      bool *hasProperty, Value *base, Lookup *lookup)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV418QQmlContextWrapper18getPropertyAndBaseEPKS0_NS_11PropertyKeyEPKNS_5ValueEPbPS4_PNS_6LookupE(
    const QV4::QQmlContextWrapper *resource,
    const QV4::PropertyKey *id,
    const QV4::Value *receiver,
    bool *hasProperty,
    QV4::Value *base,
    QV4::Lookup *lookup) {
  return QV4::QQmlContextWrapper::getPropertyAndBase(
      resource,
      *id,
      receiver,
      hasProperty,
      base,
      lookup);
}

//  ReturnedValue QV4::QQmlContextWrapper::virtualGet(const Managed *m,
//      PropertyKey id, const Value *receiver, bool *hasProperty)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV418QQmlContextWrapper10virtualGetEPKNS_7ManagedENS_11PropertyKeyEPKNS_5ValueEPb(
    const QV4::Managed *m,
    const QV4::PropertyKey *id,
    const QV4::Value *receiver,
    bool *hasProperty) {
  return QV4::QQmlContextWrapper::virtualGet(m, *id, receiver, hasProperty);
}

//  bool QV4::QQmlContextWrapper::virtualPut(Managed *m, PropertyKey id,
//      const Value &value, Value *receiver)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV418QQmlContextWrapper10virtualPutEPNS_7ManagedENS_11PropertyKeyERKNS_5ValueEPS4_(
    QV4::Managed *m,
    const QV4::PropertyKey *id,
    const QV4::Value *value,
    QV4::Value *receiver) {
  return QV4::QQmlContextWrapper::virtualPut(m, *id, *value, receiver);
}

//  ReturnedValue
//      QV4::QQmlContextWrapper::resolveQmlContextPropertyLookupGetter(Lookup
//      *l, ExecutionEngine *engine, Value *base)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV418QQmlContextWrapper37resolveQmlContextPropertyLookupGetterEPNS_6LookupEPNS_15ExecutionEngineEPNS_5ValueE(
    QV4::Lookup *l,
    QV4::ExecutionEngine *engine,
    QV4::Value *base) {
  return QV4::QQmlContextWrapper::resolveQmlContextPropertyLookupGetter(
      l,
      engine,
      base);
}

//  ReturnedValue QV4::QQmlContextWrapper::lookupScript(Lookup *l,
//      ExecutionEngine *engine, Value *base)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV418QQmlContextWrapper12lookupScriptEPNS_6LookupEPNS_15ExecutionEngineEPNS_5ValueE(
    QV4::Lookup *l,
    QV4::ExecutionEngine *engine,
    QV4::Value *base) {
  return QV4::QQmlContextWrapper::lookupScript(l, engine, base);
}

//  ReturnedValue QV4::QQmlContextWrapper::lookupSingleton(Lookup *l,
//      ExecutionEngine *engine, Value *base)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV418QQmlContextWrapper15lookupSingletonEPNS_6LookupEPNS_15ExecutionEngineEPNS_5ValueE(
    QV4::Lookup *l,
    QV4::ExecutionEngine *engine,
    QV4::Value *base) {
  return QV4::QQmlContextWrapper::lookupSingleton(l, engine, base);
}

//  ReturnedValue QV4::QQmlContextWrapper::lookupValueSingleton(Lookup *l,
//      ExecutionEngine *engine, Value *base)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV418QQmlContextWrapper20lookupValueSingletonEPNS_6LookupEPNS_15ExecutionEngineEPNS_5ValueE(
    QV4::Lookup *l,
    QV4::ExecutionEngine *engine,
    QV4::Value *base) {
  return QV4::QQmlContextWrapper::lookupValueSingleton(l, engine, base);
}

//  ReturnedValue QV4::QQmlContextWrapper::lookupIdObject(Lookup *l,
//      ExecutionEngine *engine, Value *base)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV418QQmlContextWrapper14lookupIdObjectEPNS_6LookupEPNS_15ExecutionEngineEPNS_5ValueE(
    QV4::Lookup *l,
    QV4::ExecutionEngine *engine,
    QV4::Value *base) {
  return QV4::QQmlContextWrapper::lookupIdObject(l, engine, base);
}

//  ReturnedValue
//      QV4::QQmlContextWrapper::lookupIdObjectInParentContext(Lookup *l,
//      ExecutionEngine *engine, Value *base)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV418QQmlContextWrapper29lookupIdObjectInParentContextEPNS_6LookupEPNS_15ExecutionEngineEPNS_5ValueE(
    QV4::Lookup *l,
    QV4::ExecutionEngine *engine,
    QV4::Value *base) {
  return QV4::QQmlContextWrapper::lookupIdObjectInParentContext(
      l,
      engine,
      base);
}

//  ReturnedValue QV4::QQmlContextWrapper::lookupScopeObjectProperty(Lookup
//      *l, ExecutionEngine *engine, Value *base)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV418QQmlContextWrapper25lookupScopeObjectPropertyEPNS_6LookupEPNS_15ExecutionEngineEPNS_5ValueE(
    QV4::Lookup *l,
    QV4::ExecutionEngine *engine,
    QV4::Value *base) {
  return QV4::QQmlContextWrapper::lookupScopeObjectProperty(l, engine, base);
}

//  ReturnedValue QV4::QQmlContextWrapper::lookupScopeObjectMethod(Lookup *l,
//      ExecutionEngine *engine, Value *base)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV418QQmlContextWrapper23lookupScopeObjectMethodEPNS_6LookupEPNS_15ExecutionEngineEPNS_5ValueE(
    QV4::Lookup *l,
    QV4::ExecutionEngine *engine,
    QV4::Value *base) {
  return QV4::QQmlContextWrapper::lookupScopeObjectMethod(l, engine, base);
}

//  ReturnedValue QV4::QQmlContextWrapper::lookupScopeFallbackProperty(Lookup
//      *l, ExecutionEngine *engine, Value *base)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV418QQmlContextWrapper27lookupScopeFallbackPropertyEPNS_6LookupEPNS_15ExecutionEngineEPNS_5ValueE(
    QV4::Lookup *l,
    QV4::ExecutionEngine *engine,
    QV4::Value *base) {
  return QV4::QQmlContextWrapper::lookupScopeFallbackProperty(
      l,
      engine,
      base);
}

//  ReturnedValue QV4::QQmlContextWrapper::lookupContextObjectProperty(Lookup
//      *l, ExecutionEngine *engine, Value *base)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV418QQmlContextWrapper27lookupContextObjectPropertyEPNS_6LookupEPNS_15ExecutionEngineEPNS_5ValueE(
    QV4::Lookup *l,
    QV4::ExecutionEngine *engine,
    QV4::Value *base) {
  return QV4::QQmlContextWrapper::lookupContextObjectProperty(
      l,
      engine,
      base);
}

//  ReturnedValue QV4::QQmlContextWrapper::lookupContextObjectMethod(Lookup
//      *l, ExecutionEngine *engine, Value *base)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV418QQmlContextWrapper25lookupContextObjectMethodEPNS_6LookupEPNS_15ExecutionEngineEPNS_5ValueE(
    QV4::Lookup *l,
    QV4::ExecutionEngine *engine,
    QV4::Value *base) {
  return QV4::QQmlContextWrapper::lookupContextObjectMethod(l, engine, base);
}

//  ReturnedValue QV4::QQmlContextWrapper::lookupInGlobalObject(Lookup *l,
//      ExecutionEngine *engine, Value *base)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV418QQmlContextWrapper20lookupInGlobalObjectEPNS_6LookupEPNS_15ExecutionEngineEPNS_5ValueE(
    QV4::Lookup *l,
    QV4::ExecutionEngine *engine,
    QV4::Value *base) {
  return QV4::QQmlContextWrapper::lookupInGlobalObject(l, engine, base);
}

//  ReturnedValue
//      QV4::QQmlContextWrapper::lookupInParentContextHierarchy(Lookup *l,
//      ExecutionEngine *engine, Value *base)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV418QQmlContextWrapper30lookupInParentContextHierarchyEPNS_6LookupEPNS_15ExecutionEngineEPNS_5ValueE(
    QV4::Lookup *l,
    QV4::ExecutionEngine *engine,
    QV4::Value *base) {
  return QV4::QQmlContextWrapper::lookupInParentContextHierarchy(
      l,
      engine,
      base);
}

//  ReturnedValue QV4::QQmlContextWrapper::lookupType(Lookup *l,
//      ExecutionEngine *engine, Value *base)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV418QQmlContextWrapper10lookupTypeEPNS_6LookupEPNS_15ExecutionEngineEPNS_5ValueE(
    QV4::Lookup *l,
    QV4::ExecutionEngine *engine,
    QV4::Value *base) {
  return QV4::QQmlContextWrapper::lookupType(l, engine, base);
}

//  a QQmlRefPointer<QQmlContextData> a ritual of QV4::QQmlContextWrapper
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QV4_QQmlContextWrapper__QQmlRefPointer_QQmlContextData(
    QQmlRefPointer<QQmlContextData> *self) {
  delete self;
}
