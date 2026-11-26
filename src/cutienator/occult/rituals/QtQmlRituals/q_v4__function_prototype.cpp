//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4functionobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4functionobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4memberdata_p.h>
#include <QtQml/private/qv4mm_p.h>
#include <QtQml/private/qv4value_p.h>
#include <QtQml/private/qv4object_p.h>
#include <QtQml/private/qv4function_p.h>
#include <QtQml/private/qv4symbol_p.h>
#include <QtQml/private/qv4mm_p.h>
#include <QtQml/private/qv4scopedvalue_p.h>
#include <QtQml/private/qv4argumentsobject_p.h>
#include <QtQml/private/qqmljsengine_p.h>
#include <QtQml/private/qqmljsast_p.h>
#include <QtQml/private/qqmljavascriptexpression_p.h>
#include <QtQml/private/qqmlengine_p.h>
#include <QtQml/private/qv4runtimecodegen_p.h>
#include <QtCore/private/qlocale_tools_p.h>
#include <QtQml/private/qqmlbuiltinfunctions_p.h>
#include <QtQml/private/qv4jscall_p.h>
#include <QtQml/private/qv4vme_moth_p.h>
#include <QtQml/private/qv4alloca_p.h>
#include <QtCore/QDebug>
#include <algorithm>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4memberdata.cpp, line 13, as local:qv4memberdata.cpp:nextPowerOfTwo
static size_t nextPowerOfTwo(size_t s)
{
    --s;
    s |= s >> 1;
    s |= s >> 2;
    s |= s >> 4;
    s |= s >> 8;
    s |= s >> 16;
#if (QT_POINTER_SIZE == 8)
        s |= s >> 32;
#endif
    ++s;
    return s;
}

//  from ../qtdeclarative/src/qml/jsruntime/qv4memberdata.cpp, line 28, as _ZN3QV410MemberData8allocateEPNS_15ExecutionEngineEjPNS_4Heap10MemberDataE
namespace QV4 {
inline Heap::MemberData *MemberData::allocate(ExecutionEngine *e, uint n, Heap::MemberData *old)
{
    Q_ASSERT(!old || old->values.size <= n);
    if (!n)
        n = 4;

    size_t alloc = MemoryManager::align(sizeof(Heap::MemberData) + (n - 1)*sizeof(Value));
    // round up to next power of two to avoid quadratic behaviour for very large objects
    alloc = nextPowerOfTwo(alloc);

    // The above code can overflow in a number of interesting ways. All of those are unsigned,
    // and therefore defined behavior. Still, apply some sane bounds.
    const size_t intMax = std::numeric_limits<int>::max();
    if (alloc > intMax)
        alloc = intMax;

    Heap::MemberData *m;
    if (old) {
        const size_t oldSize = sizeof(Heap::MemberData) + (old->values.size - 1) * sizeof(Value);
        if (oldSize > alloc)
            alloc = oldSize;
        m = e->memoryManager->allocManaged<MemberData>(alloc);
        // no write barrier required here, as m gets marked later when member data is set
        memcpy(m, old, oldSize);
    } else {
        m = e->memoryManager->allocManaged<MemberData>(alloc);
        m->init();
    }

    m->values.alloc = static_cast<uint>((alloc - sizeof(Heap::MemberData) + sizeof(Value))/sizeof(Value));
    m->values.size = m->values.alloc;
    return m;
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4functionobject.cpp, line 304, as _ZN3QV417FunctionPrototype11virtualCallEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue FunctionPrototype::virtualCall(
        const FunctionObject *, const Value *, const Value *, int)
{
    return Encode::undefined();
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4functionobject.cpp, line 310, as _ZN3QV417FunctionPrototype15method_toStringEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue FunctionPrototype::method_toString(const FunctionObject *b, const Value *thisObject, const Value *, int)
{
    ExecutionEngine *v4 = b->engine();
    const FunctionObject *fun = thisObject->as<FunctionObject>();
    if (!fun)
        return v4->throwTypeError();

    const Scope scope(fun->engine());
    const ScopedString scopedFunctionName(scope, fun->name());
    const QString functionName(scopedFunctionName ? scopedFunctionName->toQString() : QString());
    QString functionAsString = QStringLiteral("function");

    // If fun->name() is empty, then there is no function name
    // to append because the function is anonymous.
    if (!functionName.isEmpty())
        functionAsString.append(QLatin1Char(' ') + functionName);

    functionAsString.append(QStringLiteral("() { [native code] }"));

    return Encode(v4->newString(functionAsString));
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4functionobject.cpp, line 378, as _ZN3QV417FunctionPrototype11method_callEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue FunctionPrototype::method_call(const QV4::FunctionObject *b, const Value *thisObject, const Value *argv, int argc)
{
    QV4::ExecutionEngine *v4 = b->engine();
    if (!thisObject->isFunctionObject())
        return v4->throwTypeError();

    const FunctionObject *f = static_cast<const FunctionObject *>(thisObject);

    thisObject = argc ? argv : nullptr;
    if (argc) {
        ++argv;
        --argc;
    }
    return checkedResult(v4, f->call(thisObject, argv, argc));
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4functionobject.cpp, line 435, as _ZN3QV417FunctionPrototype18method_hasInstanceEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue FunctionPrototype::method_hasInstance(const FunctionObject *, const Value *thisObject, const Value *argv, int argc)
{
    if (!argc)
        return Encode(false);
    const Object *o = thisObject->as<Object>();
    if (!o)
        return Encode(false);

    return Object::virtualInstanceOf(o, argv[0]);
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::FunctionPrototype::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV417FunctionPrototype10__dataTestEv(
    QV4::FunctionPrototype *self) {
  self->__dataTest();
}

//  QV4::Heap::FunctionPrototype *QV4::FunctionPrototype::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::FunctionPrototype *ritual_ZNK3QV417FunctionPrototype11d_uncheckedEv(
    const QV4::FunctionPrototype *self) {
  return self->d_unchecked();
}

//  QV4::Heap::FunctionPrototype *QV4::FunctionPrototype::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::FunctionPrototype *ritual_ZNK3QV417FunctionPrototype1dEv(
    const QV4::FunctionPrototype *self) {
  return self->d();
}

//  ReturnedValue QV4::FunctionPrototype::virtualCall(const FunctionObject
//      *f, const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV417FunctionPrototype11virtualCallEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *f,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::FunctionPrototype::virtualCall(f, thisObject, argv, argc);
}

//  ReturnedValue QV4::FunctionPrototype::method_toString(const
//      FunctionObject *a0, const Value *thisObject, const Value *argv, int
//      argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV417FunctionPrototype15method_toStringEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::FunctionPrototype::method_toString(a0, thisObject, argv, argc);
}

//  ReturnedValue QV4::FunctionPrototype::method_call(const FunctionObject
//      *a0, const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV417FunctionPrototype11method_callEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::FunctionPrototype::method_call(a0, thisObject, argv, argc);
}

//  ReturnedValue QV4::FunctionPrototype::method_hasInstance(const
//      FunctionObject *a0, const Value *thisObject, const Value *argv, int
//      argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV417FunctionPrototype18method_hasInstanceEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::FunctionPrototype::method_hasInstance(
      a0,
      thisObject,
      argv,
      argc);
}
