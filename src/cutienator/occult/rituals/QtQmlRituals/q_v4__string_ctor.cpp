//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4stringobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4stringobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4symbol_p.h>
#include <QtQml/private/qv4functionobject_p.h>
#include <QtQml/private/qv4identifiertable_p.h>
#include <QtQml/private/qv4stringobject_p.h>
#include <QtQml/private/qv4regexpobject_p.h>
#include <QtQml/private/qv4mm_p.h>
#include <QtQml/private/qv4scopedvalue_p.h>
#include <QtQml/private/qv4symbol_p.h>
#include <QtQml/private/qv4alloca_p.h>
#include <QtQml/private/qv4jscall_p.h>
#include <QtQml/private/qv4stringiterator_p.h>
#include <QtCore/QDateTime>
#include <QtCore/QDebug>
#include <QtCore/QStringList>
#include <QtQml/private/qv4runtime_p.h>
#include <cassert>
#ifndef Q_OS_WIN
#  include <time.h>
#  ifndef Q_OS_VXWORKS
#    include <sys/time.h>
#  else
#    include "qplatformdefs.h"
#  endif
#else
#  include <QtCore/qt_windows.h>
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

using namespace Qt::Literals::StringLiterals;

//  from ../qtdeclarative/src/qml/jsruntime/qv4symbol.cpp, line 148, as _ZNK3QV46Symbol17descriptiveStringEv
namespace QV4 {
inline QString Symbol::descriptiveString() const
{
    return QLatin1String("Symbol(") + QStringView{toQString()}.mid(1) + QLatin1String(")");
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4stringobject.cpp, line 141, as _ZN3QV410StringCtor24virtualCallAsConstructorEPKNS_14FunctionObjectEPKNS_5ValueEiS6_
namespace QV4 {
using namespace Qt::Literals::StringLiterals;
inline ReturnedValue StringCtor::virtualCallAsConstructor(const FunctionObject *f, const Value *argv, int argc, const Value *newTarget)
{
    ExecutionEngine *v4 = static_cast<const Object *>(f)->engine();
    Scope scope(v4);
    ScopedString value(scope);
    if (argc)
        value = argv[0].toString(v4);
    else
        value = v4->newString();
    CHECK_EXCEPTION();
    ReturnedValue o = Encode(v4->newStringObject(value));

    if (!newTarget)
        return o;
    ScopedObject obj(scope, o);
    obj->setProtoFromNewTarget(newTarget);
    return obj->asReturnedValue();
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4stringobject.cpp, line 160, as _ZN3QV410StringCtor11virtualCallEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
using namespace Qt::Literals::StringLiterals;
inline ReturnedValue StringCtor::virtualCall(const FunctionObject *m, const Value *, const Value *argv, int argc)
{
    ExecutionEngine *v4 = m->engine();
    if (!argc)
        return v4->newString()->asReturnedValue();
    if (argv[0].isSymbol())
        return v4->newString(argv[0].symbolValue()->descriptiveString())->asReturnedValue();
    return argv[0].toString(v4)->asReturnedValue();
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4stringobject.cpp, line 170, as _ZN3QV410StringCtor19method_fromCharCodeEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
using namespace Qt::Literals::StringLiterals;
inline ReturnedValue StringCtor::method_fromCharCode(const FunctionObject *b, const Value *, const Value *argv, int argc)
{
    QString str(argc, Qt::Uninitialized);
    QChar *ch = str.data();
    for (int i = 0, ei = argc; i < ei; ++i) {
        *ch = QChar(argv[i].toUInt16());
        ++ch;
    }
    return Encode(b->engine()->newString(str));
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4stringobject.cpp, line 183, as _ZN3QV410StringCtor20method_fromCodePointEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
using namespace Qt::Literals::StringLiterals;
inline ReturnedValue StringCtor::method_fromCodePoint(const FunctionObject *f, const Value *, const Value *argv, int argc)
{
    ExecutionEngine *e = f->engine();
    QString result(argc*2, Qt::Uninitialized); // assume worst case
    QChar *ch = result.data();
    for (int i = 0; i < argc; ++i) {
        double num = argv[i].toNumber();
        if (e->hasException)
            return Encode::undefined();
        int cp = static_cast<int>(num);
        if (cp != num || cp < 0 || cp > 0x10ffff)
            return e->throwRangeError(QStringLiteral("String.fromCodePoint: argument out of range."));
        if (cp > 0xffff) {
            *ch = QChar::highSurrogate(cp);
            ++ch;
            *ch = QChar::lowSurrogate(cp);
        } else {
            *ch = QChar(cp);
        }
        ++ch;
    }
    result.truncate(ch - result.constData());
    return e->newString(result)->asReturnedValue();
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4stringobject.cpp, line 208, as _ZN3QV410StringCtor10method_rawEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
using namespace Qt::Literals::StringLiterals;
inline ReturnedValue StringCtor::method_raw(const FunctionObject *f, const Value *, const Value *argv, int argc)
{
    Scope scope(f);
    if (!argc)
        return scope.engine->throwTypeError();

    ScopedObject cooked(scope, argv[0].toObject(scope.engine));
    if (!cooked)
        return scope.engine->throwTypeError();
    ScopedString rawString(scope, scope.engine->newIdentifier(QStringLiteral("raw")));
    ScopedValue rawValue(scope, cooked->get(rawString));
    ScopedObject raw(scope, rawValue->toObject(scope.engine));
    if (scope.hasException())
        return Encode::undefined();

    ++argv;
    --argc;

    QString result;
    uint literalSegments = raw->getLength();
    if (!literalSegments)
        return scope.engine->id_empty()->asReturnedValue();

    uint nextIndex = 0;
    ScopedValue val(scope);
    while (1) {
        val = raw->get(nextIndex);
        result += val->toQString();
        if (scope.hasException())
            return Encode::undefined();
        if (nextIndex + 1 == literalSegments)
            return scope.engine->newString(result)->asReturnedValue();

        if (nextIndex < static_cast<uint>(argc))
            result += argv[nextIndex].toQString();
        if (scope.hasException())
            return Encode::undefined();
        ++nextIndex;
    }
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::StringCtor::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV410StringCtor10__dataTestEv(QV4::StringCtor *self) {
  self->__dataTest();
}

//  QV4::Heap::StringCtor *QV4::StringCtor::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::StringCtor *ritual_ZNK3QV410StringCtor11d_uncheckedEv(
    const QV4::StringCtor *self) {
  return self->d_unchecked();
}

//  QV4::Heap::StringCtor *QV4::StringCtor::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::StringCtor *ritual_ZNK3QV410StringCtor1dEv(
    const QV4::StringCtor *self) {
  return self->d();
}

//  ReturnedValue QV4::StringCtor::virtualCallAsConstructor(const
//      FunctionObject *f, const Value *argv, int argc, const Value *a3)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV410StringCtor24virtualCallAsConstructorEPKNS_14FunctionObjectEPKNS_5ValueEiS6_(
    const QV4::FunctionObject *f,
    const QV4::Value *argv,
    int argc,
    const QV4::Value *a3) {
  return QV4::StringCtor::virtualCallAsConstructor(f, argv, argc, a3);
}

//  ReturnedValue QV4::StringCtor::virtualCall(const FunctionObject *a0,
//      const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV410StringCtor11virtualCallEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::StringCtor::virtualCall(a0, thisObject, argv, argc);
}

//  ReturnedValue QV4::StringCtor::method_fromCharCode(const FunctionObject
//      *a0, const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV410StringCtor19method_fromCharCodeEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::StringCtor::method_fromCharCode(a0, thisObject, argv, argc);
}

//  ReturnedValue QV4::StringCtor::method_fromCodePoint(const FunctionObject
//      *a0, const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV410StringCtor20method_fromCodePointEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::StringCtor::method_fromCodePoint(a0, thisObject, argv, argc);
}

//  ReturnedValue QV4::StringCtor::method_raw(const FunctionObject *a0, const
//      Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV410StringCtor10method_rawEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::StringCtor::method_raw(a0, thisObject, argv, argc);
}
