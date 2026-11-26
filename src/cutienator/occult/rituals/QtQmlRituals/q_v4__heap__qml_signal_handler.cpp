//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4qobjectwrapper_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4qobjectwrapper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4qobjectwrapper_p.h>
#include <QtQml/private/qjsvalue_p.h>
#include <QtQml/private/qjsmanagedvalue_p.h>
#include <QtQml/private/qqmlbinding_p.h>
#include <QtQml/private/qqmlbuiltinfunctions_p.h>
#include <QtQml/private/qqmlengine_p.h>
#include <QtQml/private/qqmlobjectorgadget_p.h>
#include <QtQml/private/qqmlpropertybinding_p.h>
#include <QtQml/private/qqmlscriptstring_p.h>
#include <QtQml/private/qqmlsignalnames_p.h>
#include <QtQml/private/qqmltypewrapper_p.h>
#include <QtQml/private/qqmlvaluetypewrapper_p.h>
#include <QtQml/private/qqmlvmemetaobject_p.h>
#include <QtQml/private/qv4arraybuffer_p.h>
#include <QtQml/private/qv4arrayobject_p.h>
#include <QtQml/private/qv4compileddata_p.h>
#include <QtQml/private/qv4dateobject_p.h>
#include <QtQml/private/qv4functionobject_p.h>
#include <QtQml/private/qv4identifiertable_p.h>
#include <QtQml/private/qv4jscall_p.h>
#include <QtQml/private/qv4jsonobject_p.h>
#include <QtQml/private/qv4lookup_p.h>
#include <QtQml/private/qv4mm_p.h>
#include <QtQml/private/qv4regexpobject_p.h>
#include <QtQml/private/qv4runtime_p.h>
#include <QtQml/private/qv4scopedvalue_p.h>
#include <QtQml/private/qv4sequenceobject_p.h>
#include <QtQml/private/qv4variantobject_p.h>
#include <QtCore/qjsonarray.h>
#include <QtCore/qjsonobject.h>
#include <QtCore/qjsonvalue.h>
#include <QtCore/qloggingcategory.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qqueue.h>
#include <QtCore/qtimer.h>
#include <QtCore/qtypes.h>
#include <QtCore/qvarlengtharray.h>
#include <vector>
#if QT_CONFIG(qml_itemmodel)
#include <QtCore/qabstractitemmodel.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from ../qtdeclarative/src/qml/jsruntime/qv4qobjectwrapper.cpp, line 2859, as _ZN3QV44Heap16QmlSignalHandler4initEP7QObjecti
namespace QV4 {
using namespace Qt::StringLiterals;
inline void Heap::QmlSignalHandler::init(QObject *object, int signalIndex)
{
    Object::init();
    this->signalIndex = signalIndex;
    setObject(object);
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::Heap::QmlSignalHandler::init(QObject *object, int signalIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap16QmlSignalHandler4initEP7QObjecti(
    QV4::Heap::QmlSignalHandler *self,
    QObject *object,
    int signalIndex) {
  self->init(object, signalIndex);
}

//  void QV4::Heap::QmlSignalHandler::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap16QmlSignalHandler7destroyEv(
    QV4::Heap::QmlSignalHandler *self) {
  self->destroy();
}

//  QObject *QV4::Heap::QmlSignalHandler::object() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK3QV44Heap16QmlSignalHandler6objectEv(
    const QV4::Heap::QmlSignalHandler *self) {
  return self->object();
}

//  void QV4::Heap::QmlSignalHandler::setObject(QObject *o)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap16QmlSignalHandler9setObjectEP7QObject(
    QV4::Heap::QmlSignalHandler *self,
    QObject *o) {
  self->setObject(o);
}
