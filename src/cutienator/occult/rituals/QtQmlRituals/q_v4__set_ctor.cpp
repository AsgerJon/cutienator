//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4setobject_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4setobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4setobject_p.h>
#include <QtQml/private/qv4setiterator_p.h>
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

using namespace Qt::Literals::StringLiterals;

//  from ../qtdeclarative/src/qml/jsruntime/qv4setobject.cpp, line 28, as _ZN3QV411WeakSetCtor9constructEPKNS_14FunctionObjectEPKNS_5ValueEiS6_b
namespace QV4 {
using namespace Qt::Literals::StringLiterals;
inline ReturnedValue WeakSetCtor::construct(const FunctionObject *f, const Value *argv, int argc, const Value *newTarget, bool isWeak)
{
    Scope scope(f);
    Scoped<SetObject> a(scope, scope.engine->memoryManager->allocate<SetObject>());
    bool protoSet = false;
    if (newTarget)
        protoSet = a->setProtoFromNewTarget(newTarget);
    if (!protoSet && isWeak)
        a->setPrototypeOf(scope.engine->weakSetPrototype());
    a->d()->isWeakSet = isWeak;

    if (argc > 0) {
        ScopedValue iterable(scope, argv[0]);
        if (!iterable->isUndefined() && !iterable->isNull()) {
            ScopedFunctionObject adder(scope, a->get(ScopedString(scope, scope.engine->newString(u"add"_s))));
            if (!adder)
                return scope.engine->throwTypeError();
            ScopedObject iter(scope, Runtime::GetIterator::call(scope.engine, iterable, true));
            CHECK_EXCEPTION();
            if (!iter)
                return a.asReturnedValue();

            Value *nextValue = scope.constructUndefined(1);
            ScopedValue done(scope);
            forever {
                done = Runtime::IteratorNext::call(scope.engine, iter, nextValue);
                CHECK_EXCEPTION();
                if (done->toBoolean())
                    return a.asReturnedValue();

                adder->call(a, nextValue, 1);
                if (scope.hasException())
                    return Runtime::IteratorClose::call(scope.engine, iter);
            }
        }
    }

    return a.asReturnedValue();
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4setobject.cpp, line 171, as _ZN3QV44Heap9SetObject4initEv
namespace QV4 {
using namespace Qt::Literals::StringLiterals;
inline void Heap::SetObject::init()
{
    Object::init();
    esTable = new ESTable();
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::SetCtor::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV47SetCtor10__dataTestEv(QV4::SetCtor *self) {
  self->__dataTest();
}

//  QV4::Heap::SetCtor *QV4::SetCtor::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::SetCtor *ritual_ZNK3QV47SetCtor11d_uncheckedEv(
    const QV4::SetCtor *self) {
  return self->d_unchecked();
}

//  QV4::Heap::SetCtor *QV4::SetCtor::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::SetCtor *ritual_ZNK3QV47SetCtor1dEv(const QV4::SetCtor *self) {
  return self->d();
}
