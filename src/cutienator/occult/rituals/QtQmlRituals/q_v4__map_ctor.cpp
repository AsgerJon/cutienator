//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4mapobject_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4mapobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4mapobject_p.h>
#include <QtQml/private/qv4mapiterator_p.h>
#include <QtQml/private/qv4estable_p.h>
#include <QtQml/private/qv4symbol_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4mapobject.cpp, line 26, as _ZN3QV411WeakMapCtor9constructEPKNS_14FunctionObjectEPKNS_5ValueEiS6_b
namespace QV4 {
inline ReturnedValue WeakMapCtor::construct(const FunctionObject *f, const Value *argv, int argc, const Value *newTarget, bool weakMap)
{
    Scope scope(f);
    Scoped<MapObject> a(scope, scope.engine->memoryManager->allocate<MapObject>());
    bool protoSet = false;
    if (newTarget)
        protoSet = a->setProtoFromNewTarget(newTarget);
    if (!protoSet && weakMap) {
        a->setPrototypeOf(scope.engine->weakMapPrototype());
        scope.engine->memoryManager->registerWeakMap(a->d());
    }
    a->d()->isWeakMap = weakMap;

    if (argc > 0) {
        ScopedValue iterable(scope, argv[0]);

        if (!iterable->isNullOrUndefined()) {
            ScopedFunctionObject adder(scope, a->get(ScopedString(scope, scope.engine->newString(QString::fromLatin1("set")))));
            if (!adder)
                return scope.engine->throwTypeError();

            ScopedObject iter(scope, Runtime::GetIterator::call(scope.engine, iterable, true));
            if (scope.hasException())
                return Encode::undefined();
            Q_ASSERT(iter);

            ScopedValue obj(scope);
            Value *arguments = scope.constructUndefined(2);
            ScopedValue done(scope);
            forever {
                done = Runtime::IteratorNext::call(scope.engine, iter, obj);
                if (scope.hasException())
                    break;
                if (done->toBoolean())
                    return a->asReturnedValue();
                const Object *o = obj->objectValue();
                if (!o) {
                    scope.engine->throwTypeError();
                    break;
                }

                arguments[0] = o->get(PropertyKey::fromArrayIndex(0));
                if (scope.hasException())
                    break;
                arguments[1] = o->get(PropertyKey::fromArrayIndex(1));
                if (scope.hasException())
                    break;

                adder->call(a, arguments, 2);
                if (scope.hasException())
                    break;
            }
            return Runtime::IteratorClose::call(scope.engine, iter);
        }
    }
    return a->asReturnedValue();

}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4mapobject.cpp, line 149, as _ZN3QV44Heap9MapObject4initEv
namespace QV4 {
inline void Heap::MapObject::init()
{
    Object::init();
    esTable = new ESTable();
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::MapCtor::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV47MapCtor10__dataTestEv(QV4::MapCtor *self) {
  self->__dataTest();
}

//  QV4::Heap::MapCtor *QV4::MapCtor::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::MapCtor *ritual_ZNK3QV47MapCtor11d_uncheckedEv(
    const QV4::MapCtor *self) {
  return self->d_unchecked();
}

//  QV4::Heap::MapCtor *QV4::MapCtor::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::MapCtor *ritual_ZNK3QV47MapCtor1dEv(const QV4::MapCtor *self) {
  return self->d();
}
