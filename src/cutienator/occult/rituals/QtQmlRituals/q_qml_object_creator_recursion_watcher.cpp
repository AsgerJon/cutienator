//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlobjectcreator_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlobjectcreator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qqmlobjectcreator_p.h>
#include <QtQml/private/qjsvalue_p.h>
#include <QtQml/private/qqmlanybinding_p.h>
#include <QtQml/private/qqmlbinding_p.h>
#include <QtQml/private/qqmlboundsignal_p.h>
#include <QtQml/private/qqmlcomponent_p.h>
#include <QtQml/private/qqmlcomponentattached_p.h>
#include <QtQml/private/qqmlcustomparser_p.h>
#include <QtQml/private/qqmldebugconnector_p.h>
#include <QtQml/private/qqmldebugserviceinterfaces_p.h>
#include <QtQml/private/qqmlengine_p.h>
#include <QtQml/private/qqmlpropertybinding_p.h>
#include <QtQml/private/qqmlpropertyvalueinterceptor_p.h>
#include <QtQml/private/qqmlscriptdata_p.h>
#include <QtQml/private/qqmlscriptstring_p.h>
#include <QtQml/private/qqmlsourcecoordinate_p.h>
#include <QtQml/private/qqmlstringconverters_p.h>
#include <QtQml/private/qqmlvaluetypeproxybinding_p.h>
#include <QtQml/private/qqmlvme_p.h>
#include <QtQml/private/qqmlvmemetaobject_p.h>
#include <QtQml/private/qv4function_p.h>
#include <QtQml/private/qv4functionobject_p.h>
#include <QtQml/private/qv4generatorobject_p.h>
#include <QtQml/private/qv4qobjectwrapper_p.h>
#include <QtQml/private/qv4referenceobject_p.h>
#include <QtQml/private/qv4resolvedtypereference_p.h>
#include <QtCore/qscopedvaluerollback.h>
#include <QtCore/qloggingcategory.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/qml/qqmlobjectcreator.cpp, line 2189, as _ZN33QQmlObjectCreatorRecursionWatcherC1EP17QQmlObjectCreator
inline QQmlObjectCreatorRecursionWatcher::QQmlObjectCreatorRecursionWatcher(QQmlObjectCreator *creator)
    : sharedState(creator->sharedState)
    , watcher(creator->sharedState.data())
{
}
//  -----------------------------------------------------------------------

//  QQmlObjectCreatorRecursionWatcher::QQmlObjectCreatorRecursionWatcher(QQml
//      ObjectCreator *creator)
extern "C" Q_DECL_EXPORT
QQmlObjectCreatorRecursionWatcher *ritual_ZN33QQmlObjectCreatorRecursionWatcherC1EP17QQmlObjectCreator(
    QQmlObjectCreator *creator) {
  return new QQmlObjectCreatorRecursionWatcher(creator);
}

//  bool QQmlObjectCreatorRecursionWatcher::hasRecursed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK33QQmlObjectCreatorRecursionWatcher11hasRecursedEv(
    const QQmlObjectCreatorRecursionWatcher *self) {
  return self->hasRecursed();
}

//  QQmlObjectCreatorRecursionWatcher::~QQmlObjectCreatorRecursionWatcher()
extern "C" Q_DECL_EXPORT
void ritual_ZN33QQmlObjectCreatorRecursionWatcherD1Ev(
    QQmlObjectCreatorRecursionWatcher *self) {
  delete self;
}
