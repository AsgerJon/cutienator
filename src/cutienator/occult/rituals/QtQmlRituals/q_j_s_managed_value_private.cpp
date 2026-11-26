//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qjsmanagedvalue_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qjsmanagedvalue_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/QJSManagedValue>

//  QV4::Value *QJSManagedValuePrivate::member(const QJSManagedValue *jsmv)
extern "C" Q_DECL_EXPORT
QV4::Value *ritual_ZN22QJSManagedValuePrivate6memberEPK15QJSManagedValue(
    const QJSManagedValue *jsmv) {
  return QJSManagedValuePrivate::member(jsmv);
}

//  QJSManagedValue QJSManagedValuePrivate::create(QV4::ExecutionEngine
//      *engine, const QV4::Value &value)
extern "C" Q_DECL_EXPORT
QJSManagedValue *ritual_ZN22QJSManagedValuePrivate6createEPN3QV415ExecutionEngineERKNS0_5ValueE(
    QV4::ExecutionEngine *engine,
    const QV4::Value *value) {
  return new QJSManagedValue(QJSManagedValuePrivate::create(engine, *value));
}

//  QJSManagedValue QJSManagedValuePrivate::create(const QV4::Managed
//      &managed)
extern "C" Q_DECL_EXPORT
QJSManagedValue *ritual_ZN22QJSManagedValuePrivate6createERKN3QV47ManagedE(
    const QV4::Managed *managed) {
  return new QJSManagedValue(QJSManagedValuePrivate::create(*managed));
}

//  QJSManagedValuePrivate::~QJSManagedValuePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QJSManagedValuePrivateD1Ev(QJSManagedValuePrivate *self) {
  delete self;
}

//  a QJSManagedValue a ritual of QJSManagedValuePrivate gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QJSManagedValuePrivate__QJSManagedValue(
    QJSManagedValue *self) {
  delete self;
}
