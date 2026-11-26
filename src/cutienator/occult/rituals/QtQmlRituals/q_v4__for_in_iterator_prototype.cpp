//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4objectiterator_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4objectiterator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4propertykey_p.h>
#include <QtCore/qstring.h>
#include <QtQml/private/qv4string_p.h>
#include <QtQml/private/qv4engine_p.h>
#include <QtQml/private/qv4scopedvalue_p.h>
#include <QtQml/private/qv4mm_p.h>
#include <QtQml/private/qv4iterator_p.h>
#include <QtQml/private/qv4symbol_p.h>
#include <QtQml/private/qv4engine_p.h>
#include <QtQml/private/qv4objectiterator_p.h>
#include <QtQml/private/qv4object_p.h>
#include <QtQml/private/qv4iterator_p.h>
#include <QtQml/private/qv4propertykey_p.h>
#include <QtQml/private/qv4functionobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::Literals::StringLiterals;

//  from ../qtdeclarative/src/qml/jsruntime/qv4propertykey.cpp, line 15, as _ZN3QV411PropertyKey16toStringOrSymbolEPNS_15ExecutionEngineE
inline QV4::Heap::StringOrSymbol *QV4::PropertyKey::toStringOrSymbol(QV4::ExecutionEngine *e)
{
    if (isArrayIndex())
        return Value::fromUInt32(asArrayIndex()).toString(e);
    return asStringOrSymbol();
}

//  from ../qtdeclarative/src/qml/jsruntime/qv4iterator.cpp, line 21, as _ZN3QV417IteratorPrototype22createIterResultObjectEPNS_15ExecutionEngineERKNS_5ValueEb
namespace QV4 {
inline ReturnedValue IteratorPrototype::createIterResultObject(ExecutionEngine *engine, const Value &value, bool done)
{
    Scope scope(engine);
    ScopedObject obj(scope, engine->newObject());
    obj->set(ScopedString(scope, engine->newString(QStringLiteral("value"))), value, Object::DoNotThrow);
    obj->set(ScopedString(scope, engine->newString(QStringLiteral("done"))), Value::fromBoolean(done), Object::DoNotThrow);
    return obj->asReturnedValue();
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4objectiterator.cpp, line 125, as _ZNK3QV419ForInIteratorObject12nextPropertyEv
namespace QV4 {
inline PropertyKey ForInIteratorObject::nextProperty() const
{
    if (!d()->current)
        return PropertyKey::invalid();

    Scope scope(this);
    ScopedObject c(scope, d()->current);
    ScopedObject t(scope, d()->target);
    ScopedObject o(scope);
    ScopedProperty p(scope);
    ScopedPropertyKey key(scope);
    PropertyAttributes attrs;

    while (1) {
        while (1) {
            key = d()->iterator->next(t, p, &attrs);
            if (!key->isValid())
                break;
            if (!attrs.isEnumerable() || key->isSymbol())
                continue;
            // check the property is not already defined earlier in the proto chain
            if (d()->current != d()->object) {
                o = d()->object;
                bool shadowed = false;
                while (o && o->d() != c->heapObject()) {
                    if (o->getOwnProperty(key) != Attr_Invalid) {
                        shadowed = true;
                        break;
                    }
                    o = o->getPrototypeOf();
                }
                if (shadowed)
                    continue;
            }
            return key;
        }

        c = c->getPrototypeOf();
        d()->current.set(scope.engine, c ? c->d() : nullptr);
        if (!c)
            break;
        delete d()->iterator;
        d()->iterator = c->ownPropertyKeys(t.getRef());
        d()->target.set(scope.engine, t->d());
        if (!d()->iterator) {
            scope.engine->throwTypeError();
            return PropertyKey::invalid();
        }
    }
    return PropertyKey::invalid();
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4objectiterator.cpp, line 12, as _ZN3QV422ForInIteratorPrototype4initEPNS_15ExecutionEngineE
namespace QV4 {
inline void ForInIteratorPrototype::init(ExecutionEngine *)
{
    defineDefaultProperty(QStringLiteral("next"), method_next, 0);
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4objectiterator.cpp, line 110, as _ZN3QV422ForInIteratorPrototype11method_nextEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue ForInIteratorPrototype::method_next(const FunctionObject *b, const Value *thisObject, const Value *, int)
{
    const ForInIteratorObject *forIn = static_cast<const ForInIteratorObject *>(thisObject);
    Q_ASSERT(forIn);
    Scope scope(b);

    ScopedPropertyKey key(scope, forIn->nextProperty());
    bool done = false;
    if (!key->isValid())
        done = true;
    ScopedStringOrSymbol s(scope, key->toStringOrSymbol(scope.engine));
    return IteratorPrototype::createIterResultObject(scope.engine, s, done);
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  QV4::Object
//      *QV4::ForInIteratorPrototype::defaultPrototype(QV4::ExecutionEngine
//      *e)
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZN3QV422ForInIteratorPrototype16defaultPrototypeEPNS_15ExecutionEngineE(
    QV4::ExecutionEngine *e) {
  return QV4::ForInIteratorPrototype::defaultPrototype(e);
}

//  void QV4::ForInIteratorPrototype::init(ExecutionEngine *engine)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV422ForInIteratorPrototype4initEPNS_15ExecutionEngineE(
    QV4::ForInIteratorPrototype *self,
    QV4::ExecutionEngine *engine) {
  self->init(engine);
}

//  ReturnedValue QV4::ForInIteratorPrototype::method_next(const
//      FunctionObject *b, const Value *thisObject, const Value *argv, int
//      argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV422ForInIteratorPrototype11method_nextEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *b,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::ForInIteratorPrototype::method_next(b, thisObject, argv, argc);
}
