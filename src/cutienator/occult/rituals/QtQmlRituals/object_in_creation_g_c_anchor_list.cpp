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

//  from ../qtdeclarative/src/qml/qml/qqmlobjectcreator.cpp, line 2195, as _ZN28ObjectInCreationGCAnchorList11trackObjectEPN3QV415ExecutionEngineEP7QObject
inline void ObjectInCreationGCAnchorList::trackObject(QV4::ExecutionEngine *engine, QObject *instance)
{
    QV4::Value *wrapper = allocationScope->construct(1, QV4::QObjectWrapper::wrap(engine, instance));
    // we have to handle the case where the gc is already running, but the scope is discarded
    // before the collector runs again. In that case, rescanning won't help us. Thus, mark the
    // object.
    QV4::WriteBarrier::markCustom(engine, [wrapper](QV4::MarkStack *ms) {
        wrapper->heapObject()->mark(ms);
    });
}
//  -----------------------------------------------------------------------

//  ObjectInCreationGCAnchorList::ObjectInCreationGCAnchorList()
extern "C" Q_DECL_EXPORT
ObjectInCreationGCAnchorList *ritual_ZN28ObjectInCreationGCAnchorListC1Ev() {
  return new ObjectInCreationGCAnchorList();
}

//  void ObjectInCreationGCAnchorList::trackObject(QV4::ExecutionEngine
//      *engine, QObject *instance)
extern "C" Q_DECL_EXPORT
void ritual_ZN28ObjectInCreationGCAnchorList11trackObjectEPN3QV415ExecutionEngineEP7QObject(
    ObjectInCreationGCAnchorList *self,
    QV4::ExecutionEngine *engine,
    QObject *instance) {
  self->trackObject(engine, instance);
}

//  bool ObjectInCreationGCAnchorList::canTrack() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28ObjectInCreationGCAnchorList8canTrackEv(
    const ObjectInCreationGCAnchorList *self) {
  return self->canTrack();
}

//  ObjectInCreationGCAnchorList::~ObjectInCreationGCAnchorList()
extern "C" Q_DECL_EXPORT
void ritual_ZN28ObjectInCreationGCAnchorListD1Ev(
    ObjectInCreationGCAnchorList *self) {
  delete self;
}
