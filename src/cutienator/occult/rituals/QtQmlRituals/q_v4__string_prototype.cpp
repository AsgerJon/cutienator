//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4stringobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4stringobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
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
//  -----------------------------------------------------------------------

//  QV4::Object *QV4::StringPrototype::defaultPrototype(QV4::ExecutionEngine
//      *e)
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZN3QV415StringPrototype16defaultPrototypeEPNS_15ExecutionEngineE(
    QV4::ExecutionEngine *e) {
  return QV4::StringPrototype::defaultPrototype(e);
}
