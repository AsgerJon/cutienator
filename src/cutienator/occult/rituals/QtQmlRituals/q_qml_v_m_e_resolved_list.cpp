//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlvmemetaobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlvmemetaobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qqmlvmemetaobject_p.h>
#include <QtQml/private/qqmlrefcount_p.h>
#include <QtQml/private/qqmlpropertyvalueinterceptor_p.h>
#include <QtQml/qqmlinfo.h>
#include <QtQml/private/qqmlglobal_p.h>
#include <QtQml/private/qqmlpropertycachecreator_p.h>
#include <QtQml/private/qqmlpropertycachemethodarguments_p.h>
#include <QtQml/private/qqmlvaluetypewrapper_p.h>
#include <QtQml/private/qv4functionobject_p.h>
#include <QtQml/private/qv4jscall_p.h>
#include <QtQml/private/qv4object_p.h>
#include <QtQml/private/qv4qobjectwrapper_p.h>
#include <QtQml/private/qv4runtime_p.h>
#include <QtQml/private/qv4scopedvalue_p.h>
#include <QtQml/private/qv4sequenceobject_p.h>
#include <QtQml/private/qv4variantassociationobject_p.h>
#include <QtQml/private/qv4variantobject_p.h>
#include <QtCore/qmetasequence.h>
#include <climits> // for CHAR_BIT
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/qml/qqmlvmemetaobject.cpp, line 69, as _ZNK19QQmlVMEResolvedList6appendEP7QObject
inline void QQmlVMEResolvedList::append(QObject *o) const
{
    Q_ASSERT(isValid());

    QV4::Scope scope(m_list->internalClass->engine);
    QV4::Heap::ArrayData *arrayData = m_list->arrayData;

    const uint length = arrayData->length();
    if (Q_UNLIKELY(length == std::numeric_limits<uint>::max())) {
        scope.engine->throwRangeError(QLatin1String("Too many elements."));
        return;
    }

    QV4::ScopedObject object(scope, m_list);
    QV4::ArrayData::realloc(object, QV4::Heap::ArrayData::Simple, length + 1, false);
    QV4::ScopedValue wrappedObject(scope, QV4::QObjectWrapper::wrap(scope.engine, o));
    arrayData->vtable()->put(
            object, length, wrappedObject);
}

//  from ../qtdeclarative/src/qml/qml/qqmlvmemetaobject.cpp, line 98, as _ZNK19QQmlVMEResolvedList7replaceExP7QObject
inline void QQmlVMEResolvedList::replace(qsizetype i, QObject *o) const
{
    Q_ASSERT(isValid());

    QV4::Scope scope(m_list->internalClass->engine);
    QV4::ScopedObject object(scope, m_list);
    QV4::ScopedValue wrappedObject(scope, QV4::QObjectWrapper::wrap(scope.engine, o));
    m_list->arrayData->vtable()->put(object, i, wrappedObject);
}

//  from ../qtdeclarative/src/qml/qml/qqmlvmemetaobject.cpp, line 89, as _ZNK19QQmlVMEResolvedList2atEx
inline QObject *QQmlVMEResolvedList::at(qsizetype i) const
{
    Q_ASSERT(isValid());

    QV4::Scope scope(m_list->internalClass->engine);
    QV4::Scoped<QV4::QObjectWrapper> result(scope, m_list->arrayData->get(i));
    return result ? result->object() : nullptr;
}

//  from ../qtdeclarative/src/qml/qml/qqmlvmemetaobject.cpp, line 110, as _ZNK19QQmlVMEResolvedList14activateSignalEv
inline void QQmlVMEResolvedList::activateSignal() const
{
    m_metaObject->activate(m_metaObject->object.data(), int(m_id), nullptr);
}
//  -----------------------------------------------------------------------

//  QQmlVMEMetaObject *QQmlVMEResolvedList::metaObject() const
extern "C" Q_DECL_EXPORT
QQmlVMEMetaObject *ritual_ZNK19QQmlVMEResolvedList10metaObjectEv(
    const QQmlVMEResolvedList *self) {
  return self->metaObject();
}

//  QV4::Heap::Object *QQmlVMEResolvedList::list() const
extern "C" Q_DECL_EXPORT
QV4::Heap::Object *ritual_ZNK19QQmlVMEResolvedList4listEv(
    const QQmlVMEResolvedList *self) {
  return self->list();
}

//  quintptr QQmlVMEResolvedList::id() const
extern "C" Q_DECL_EXPORT
quintptr ritual_ZNK19QQmlVMEResolvedList2idEv(
    const QQmlVMEResolvedList *self) {
  return self->id();
}

//  bool QQmlVMEResolvedList::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQmlVMEResolvedList7isValidEv(
    const QQmlVMEResolvedList *self) {
  return self->isValid();
}

//  void QQmlVMEResolvedList::append(QObject *o) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK19QQmlVMEResolvedList6appendEP7QObject(
    const QQmlVMEResolvedList *self,
    QObject *o) {
  self->append(o);
}

//  void QQmlVMEResolvedList::replace(qsizetype i, QObject *o) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK19QQmlVMEResolvedList7replaceExP7QObject(
    const QQmlVMEResolvedList *self,
    qsizetype i,
    QObject *o) {
  self->replace(i, o);
}

//  QObject *QQmlVMEResolvedList::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK19QQmlVMEResolvedList2atEx(
    const QQmlVMEResolvedList *self,
    qsizetype i) {
  return self->at(i);
}

//  qsizetype QQmlVMEResolvedList::size() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK19QQmlVMEResolvedList4sizeEv(
    const QQmlVMEResolvedList *self) {
  return self->size();
}

//  void QQmlVMEResolvedList::clear() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK19QQmlVMEResolvedList5clearEv(
    const QQmlVMEResolvedList *self) {
  self->clear();
}

//  void QQmlVMEResolvedList::removeLast() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK19QQmlVMEResolvedList10removeLastEv(
    const QQmlVMEResolvedList *self) {
  self->removeLast();
}

//  void QQmlVMEResolvedList::activateSignal() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK19QQmlVMEResolvedList14activateSignalEv(
    const QQmlVMEResolvedList *self) {
  self->activateSignal();
}
