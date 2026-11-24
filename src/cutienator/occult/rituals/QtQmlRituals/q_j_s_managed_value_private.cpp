//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qjsmanagedvalue_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qjsmanagedvalue_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QV4::Value *QJSManagedValuePrivate::member(const QJSManagedValue *jsmv)
extern "C" Q_DECL_EXPORT
QV4::Value *ritual_ZN22QJSManagedValuePrivate6memberEPK15QJSManagedValue(
    const QJSManagedValue *jsmv) {
  return QJSManagedValuePrivate::member(jsmv);
}

//  QJSManagedValuePrivate::~QJSManagedValuePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QJSManagedValuePrivateD1Ev(QJSManagedValuePrivate *self) {
  delete self;
}
