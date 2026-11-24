//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qjsvalueiterator_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qjsvalueiterator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/qjsvalue.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/qjsvalueiterator.h>
#include <QtQml/private/qjsvalueiterator_p.h>
#include <QtQml/private/qjsvalue_p.h>
#include <QtQml/private/qv4string_p.h>
#include <QtQml/private/qv4object_p.h>
#include <QtQml/private/qv4context_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsapi/qjsvalueiterator.cpp, line 14, as _ZN23QJSValueIteratorPrivateC1ERK8QJSValue
inline QJSValueIteratorPrivate::QJSValueIteratorPrivate(const QJSValue &v)
{
    init(v);
}

//  from ../qtdeclarative/src/qml/jsapi/qjsvalueiterator.cpp, line 19, as _ZN23QJSValueIteratorPrivate4initERK8QJSValue
inline void QJSValueIteratorPrivate::init(const QJSValue &v)
{
    engine = nullptr;

    QV4::ExecutionEngine *e = QJSValuePrivate::engine(&v);
    if (!e)
        return;
    const QV4::Object *o = QJSValuePrivate::asManagedType<QV4::Object>(&v);
    if (!o)
        return;

    engine = e;
    object.set(e, o->asReturnedValue());
    iterator.reset(o->ownPropertyKeys(object.valueRef()));
    next();
}

//  from ../qtdeclarative/src/qml/jsapi/qjsvalueiterator.cpp, line 52, as _ZNK23QJSValueIteratorPrivate7isValidEv
inline bool QJSValueIteratorPrivate::isValid() const
{
    if (!engine || !iterator)
        return false;
    QV4::Value *val = object.valueRef();
    return (val && val->isObject());
}

//  from ../qtdeclarative/src/qml/jsapi/qjsvalueiterator.cpp, line 36, as _ZN23QJSValueIteratorPrivate4nextEv
inline void QJSValueIteratorPrivate::next()
{
    QV4::Object *o = object.as<QV4::Object>();
    if (!o || !iterator)
        return;

    QV4::PropertyKey key;
    while (1) {
        key = iterator->next(o);
        if (!key.isSymbol())
            break;
    }
    currentKey = nextKey;
    nextKey.set(engine, key.id());
}
//  -----------------------------------------------------------------------

//  QJSValueIteratorPrivate::QJSValueIteratorPrivate(const QJSValue &v)
extern "C" Q_DECL_EXPORT
QJSValueIteratorPrivate *ritual_ZN23QJSValueIteratorPrivateC1ERK8QJSValue(
    const QJSValue *v) {
  return new QJSValueIteratorPrivate(*v);
}

//  void QJSValueIteratorPrivate::init(const QJSValue &v)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QJSValueIteratorPrivate4initERK8QJSValue(
    QJSValueIteratorPrivate *self,
    const QJSValue *v) {
  self->init(*v);
}

//  bool QJSValueIteratorPrivate::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QJSValueIteratorPrivate7isValidEv(
    const QJSValueIteratorPrivate *self) {
  return self->isValid();
}

//  void QJSValueIteratorPrivate::next()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QJSValueIteratorPrivate4nextEv(
    QJSValueIteratorPrivate *self) {
  self->next();
}
