//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlboundsignal_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlboundsignal_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qqmlboundsignal_p.h>
#include <QtCore/private/qmetaobject_p.h>
#include <QtCore/private/qmetaobjectbuilder_p.h>
#include <QtQml/private/qqmlengine_p.h>
#include <QtQml/private/qqmlglobal_p.h>
#include <QtQml/private/qqmlprofiler_p.h>
#include <QtQml/private/qqmldebugconnector_p.h>
#include <QtQml/private/qqmldebugserviceinterfaces_p.h>
#include <QtQml/qqmlinfo.h>
#include <QtQml/private/qjsvalue_p.h>
#include <QtQml/private/qv4value_p.h>
#include <QtQml/private/qv4jscall_p.h>
#include <QtQml/private/qv4qobjectwrapper_p.h>
#include <QtQml/private/qv4qmlcontext_p.h>
#include <QtCore/qdebug.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/qml/qqmlboundsignal.cpp, line 331, as _ZN20QQmlPropertyObserverC1EP25QQmlBoundSignalExpression
inline QQmlPropertyObserver::QQmlPropertyObserver(QQmlBoundSignalExpression *expr)
    : QPropertyObserver([](QPropertyObserver *self, QUntypedPropertyData *) {
                           auto This = static_cast<QQmlPropertyObserver*>(self);
                           This->expression->evaluate(nullptr);
                       })
{
    expression.adopt(expr);
}
//  -----------------------------------------------------------------------

//  QQmlPropertyObserver::QQmlPropertyObserver(QQmlBoundSignalExpression
//      *expr)
extern "C" Q_DECL_EXPORT
QQmlPropertyObserver *ritual_ZN20QQmlPropertyObserverC1EP25QQmlBoundSignalExpression(
    QQmlBoundSignalExpression *expr) {
  return new QQmlPropertyObserver(expr);
}
