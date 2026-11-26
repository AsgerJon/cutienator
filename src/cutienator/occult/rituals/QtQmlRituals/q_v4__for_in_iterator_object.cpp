//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4objectiterator_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4objectiterator_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4propertykey_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4objectiterator_p.h>
#include <QtQml/private/qv4object_p.h>
#include <QtQml/private/qv4iterator_p.h>
#include <QtQml/private/qv4propertykey_p.h>
#include <QtQml/private/qv4functionobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4objectiterator.cpp, line 105, as _ZN3QV44Heap19ForInIteratorObject7destroyEv
namespace QV4 {
inline void Heap::ForInIteratorObject::destroy()
{
    delete iterator;
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
//  -----------------------------------------------------------------------

//  void QV4::ForInIteratorObject::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV419ForInIteratorObject10__dataTestEv(
    QV4::ForInIteratorObject *self) {
  self->__dataTest();
}

//  QV4::Heap::ForInIteratorObject *QV4::ForInIteratorObject::d_unchecked()
//      const
extern "C" Q_DECL_EXPORT
QV4::Heap::ForInIteratorObject *ritual_ZNK3QV419ForInIteratorObject11d_uncheckedEv(
    const QV4::ForInIteratorObject *self) {
  return self->d_unchecked();
}

//  QV4::Heap::ForInIteratorObject *QV4::ForInIteratorObject::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::ForInIteratorObject *ritual_ZNK3QV419ForInIteratorObject1dEv(
    const QV4::ForInIteratorObject *self) {
  return self->d();
}

//  QV4::Object
//      *QV4::ForInIteratorObject::defaultPrototype(QV4::ExecutionEngine *e)
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZN3QV419ForInIteratorObject16defaultPrototypeEPNS_15ExecutionEngineE(
    QV4::ExecutionEngine *e) {
  return QV4::ForInIteratorObject::defaultPrototype(e);
}

//  void QV4::ForInIteratorObject::virtualDestroy(QV4::Heap::Base *b)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV419ForInIteratorObject14virtualDestroyEPNS_4Heap4BaseE(
    QV4::Heap::Base *b) {
  QV4::ForInIteratorObject::virtualDestroy(b);
}

//  PropertyKey QV4::ForInIteratorObject::nextProperty() const
extern "C" Q_DECL_EXPORT
QV4::PropertyKey *ritual_ZNK3QV419ForInIteratorObject12nextPropertyEv(
    const QV4::ForInIteratorObject *self) {
  return new QV4::PropertyKey(self->nextProperty());
}
