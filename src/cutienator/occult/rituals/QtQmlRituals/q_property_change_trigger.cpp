//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlengine_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qqmljavascriptexpression_p.h>
#include <QtQml/private/qqmljavascriptexpression_p.h>
#include <QtQml/private/qqmlexpression_p.h>
#include <QtQml/private/qv4context_p.h>
#include <QtQml/private/qv4value_p.h>
#include <QtQml/private/qv4functionobject_p.h>
#include <QtQml/private/qv4script_p.h>
#include <QtQml/private/qv4errorobject_p.h>
#include <QtQml/private/qv4scopedvalue_p.h>
#include <QtQml/private/qv4jscall_p.h>
#include <QtQml/private/qqmlglobal_p.h>
#include <QtQml/private/qv4qobjectwrapper_p.h>
#include <QtQml/private/qqmlbuiltinfunctions_p.h>
#include <QtQml/private/qqmlsourcecoordinate_p.h>
#include <QtQml/private/qqmlabstractbinding_p.h>
#include <QtQml/private/qqmlpropertybinding_p.h>
#include <QtCore/private/qproperty_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/qml/qqmljavascriptexpression.cpp, line 532, as _ZN22QPropertyChangeTrigger7triggerEP17QPropertyObserverP20QUntypedPropertyData
inline void QPropertyChangeTrigger::trigger(QPropertyObserver *observer, QUntypedPropertyData *) {
    auto This = static_cast<QPropertyChangeTrigger *>(observer);
    This->m_expression->expressionChanged();
}

//  from ../qtdeclarative/src/qml/qml/qqmljavascriptexpression.cpp, line 537, as _ZNK22QPropertyChangeTrigger8propertyEv
inline QMetaProperty QPropertyChangeTrigger::property() const
{
    if (!target)
        return {};
    auto const mo = target->metaObject();
    if (!mo)
        return {};
    return mo->property(propertyIndex);
}
//  -----------------------------------------------------------------------

//  QPropertyChangeTrigger::QPropertyChangeTrigger(QQmlJavaScriptExpression
//      *expression)
extern "C" Q_DECL_EXPORT
QPropertyChangeTrigger *ritual_ZN22QPropertyChangeTriggerC1EP24QQmlJavaScriptExpression(
    QQmlJavaScriptExpression *expression) {
  return new QPropertyChangeTrigger(expression);
}

//  void QPropertyChangeTrigger::trigger(QPropertyObserver *a0,
//      QUntypedPropertyData *a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QPropertyChangeTrigger7triggerEP17QPropertyObserverP20QUntypedPropertyData(
    QPropertyObserver *a0,
    QUntypedPropertyData *a1) {
  QPropertyChangeTrigger::trigger(a0, a1);
}

//  QMetaProperty QPropertyChangeTrigger::property() const
extern "C" Q_DECL_EXPORT
QMetaProperty *ritual_ZNK22QPropertyChangeTrigger8propertyEv(
    const QPropertyChangeTrigger *self) {
  return new QMetaProperty(self->property());
}
