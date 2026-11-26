//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4globalobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4globalobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4globalobject_p.h>
#include <QtQml/private/qv4alloca_p.h>
#include <QtQml/private/qv4codegen_p.h>
#include <QtQml/private/qv4context_p.h>
#include <QtQml/private/qv4function_p.h>
#include <QtQml/private/qv4mm_p.h>
#include <QtQml/private/qv4scopedvalue_p.h>
#include <QtQml/private/qv4script_p.h>
#include <QtQml/private/qv4stackframe_p.h>
#include <QtQml/private/qv4string_p.h>
#include <QtQml/private/qv4value_p.h>
#include <QtCore/private/qlocale_tools_p.h>
#include <QtCore/private/qtools_p.h>
#include <QtCore/qdebug.h>
#include <QtCore/qstring.h>
#include <iostream>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4globalobject.cpp, line 32, as local:qv4globalobject.cpp:escape
static QString escape(const QString &input)
{
    QString output;
    output.reserve(input.size() * 3);
    const int length = input.size();
    for (int i = 0; i < length; ++i) {
        ushort uc = input.at(i).unicode();
        if (uc < 0x100) {
            if (   (uc > 0x60 && uc < 0x7B)
                || (uc > 0x3F && uc < 0x5B)
                || (uc > 0x2C && uc < 0x3A)
                || (uc == 0x2A)
                || (uc == 0x2B)
                || (uc == 0x5F)) {
                output.append(QChar(uc));
            } else {
                output.append(u'%');
                output.append(QLatin1Char(toHexUpper(uc >> 4)));
                output.append(QLatin1Char(toHexUpper(uc)));
            }
        } else {
            output.append(u'%');
            output.append(u'u');
            output.append(QLatin1Char(toHexUpper(uc >> 12)));
            output.append(QLatin1Char(toHexUpper(uc >> 8)));
            output.append(QLatin1Char(toHexUpper(uc >> 4)));
            output.append(QLatin1Char(toHexUpper(uc)));
        }
    }
    return output;
}

//  from ../qtdeclarative/src/qml/jsruntime/qv4globalobject.cpp, line 64, as local:qv4globalobject.cpp:unescape
static QString unescape(const QString &input)
{
    QString result;
    result.reserve(input.size());
    int i = 0;
    const int length = input.size();
    while (i < length) {
        QChar c = input.at(i++);
        if ((c == u'%') && (i + 1 < length)) {
            QChar a = input.at(i);
            if ((a == u'u') && (i + 4 < length)) {
                int d3 = fromHex(input.at(i+1).unicode());
                int d2 = fromHex(input.at(i+2).unicode());
                int d1 = fromHex(input.at(i+3).unicode());
                int d0 = fromHex(input.at(i+4).unicode());
                if ((d3 != -1) && (d2 != -1) && (d1 != -1) && (d0 != -1)) {
                    ushort uc = ushort((d3 << 12) | (d2 << 8) | (d1 << 4) | d0);
                    result.append(QChar(uc));
                    i += 5;
                } else {
                    result.append(c);
                }
            } else {
                int d1 = fromHex(a.unicode());
                int d0 = fromHex(input.at(i+1).unicode());
                if ((d1 != -1) && (d0 != -1)) {
                    c = QChar((d1 << 4) | d0);
                    i += 2;
                }
                result.append(c);
            }
        } else {
            result.append(c);
        }
    }
    return result;
}

//  from ../qtdeclarative/src/qml/jsruntime/qv4globalobject.cpp, line 102, as local:qv4globalobject.cpp:uriReserved
static const char uriReserved[] = ";/?:@&=+$,#";

//  from ../qtdeclarative/src/qml/jsruntime/qv4globalobject.cpp, line 103, as local:qv4globalobject.cpp:uriUnescaped
static const char uriUnescaped[] = "-_.!~*'()";

//  from ../qtdeclarative/src/qml/jsruntime/qv4globalobject.cpp, line 104, as local:qv4globalobject.cpp:uriUnescapedReserved
static const char uriUnescapedReserved[] = "-_.!~*'();/?:@&=+$,#";

//  from ../qtdeclarative/src/qml/jsruntime/qv4globalobject.cpp, line 106, as local:qv4globalobject.cpp:addEscapeSequence
static void addEscapeSequence(QString &output, uchar ch)
{
    output.append(QLatin1Char('%'));
    output.append(QLatin1Char(toHexUpper(ch >> 4)));
    output.append(QLatin1Char(toHexUpper(ch & 0xf)));
}

//  from ../qtdeclarative/src/qml/jsruntime/qv4globalobject.cpp, line 182, as local:qv4globalobject.cpp:DecodeNonReserved
enum DecodeMode {
    DecodeAll,
    DecodeNonReserved
};

//  from ../qtdeclarative/src/qml/jsruntime/qv4globalobject.cpp, line 187, as local:qv4globalobject.cpp:decode
static QString decode(const QString &input, DecodeMode decodeMode, bool *ok)
{
    *ok = true;
    QString output;
    output.reserve(input.size());
    const int length = input.size();
    int i = 0;
    const QChar percent = QLatin1Char('%');
    while (i < length) {
        const QChar ch = input.at(i);
        if (ch == percent) {
            int start = i;
            if (i + 2 >= length)
                goto error;

            int d1 = fromHex(input.at(i+1).unicode());
            int d0 = fromHex(input.at(i+2).unicode());
            if ((d1 == -1) || (d0 == -1))
                goto error;

            int b = (d1 << 4) | d0;
            i += 2;
            if (b & 0x80) {
                int uc;
                int min_uc;
                int need;
                if ((b & 0xe0) == 0xc0) {
                    uc = b & 0x1f;
                    need = 1;
                    min_uc = 0x80;
                } else if ((b & 0xf0) == 0xe0) {
                    uc = b & 0x0f;
                    need = 2;
                    min_uc = 0x800;
                } else if ((b & 0xf8) == 0xf0) {
                    uc = b & 0x07;
                    need = 3;
                    min_uc = 0x10000;
                } else {
                    goto error;
                }

                if (i + (3 * need) >= length)
                    goto error;

                for (int j = 0; j < need; ++j) {
                    ++i;
                    if (input.at(i) != percent)
                        goto error;

                    d1 = fromHex(input.at(i+1).unicode());
                    d0 = fromHex(input.at(i+2).unicode());
                    if ((d1 == -1) || (d0 == -1))
                        goto error;

                    b = (d1 << 4) | d0;
                    if ((b & 0xC0) != 0x80)
                        goto error;

                    i += 2;
                    uc = (uc << 6) + (b & 0x3f);
                }
                if (uc < min_uc)
                    goto error;

                if (uc < 0x10000) {
                    output.append(QChar(uc));
                } else {
                    if (uc > 0x10FFFF)
                        goto error;

                    ushort l = ushort(((uc - 0x10000) & 0x3FF) + 0xDC00);
                    ushort h = ushort((((uc - 0x10000) >> 10) & 0x3FF) + 0xD800);
                    output.append(QChar(h));
                    output.append(QChar(l));
                }
            } else {
                if (decodeMode == DecodeNonReserved && b <= 0x40) {
                    const char *r = uriReserved;
                    while (*r) {
                        if (*r == b)
                            break;
                        ++r;
                    }
                    if (*r)
                        output.append(QStringView{input}.mid(start, i - start + 1));
                    else
                        output.append(QChar(b));
                } else {
                    output.append(QChar(b));
                }
            }
        } else {
            output.append(ch);
        }
        ++i;
    }
    if (i != length)
        *ok = false;
    return output;
  error:
    *ok = false;
    return QString();
}

//  from ../qtdeclarative/src/qml/jsruntime/qv4globalobject.cpp, line 366, as local:qv4globalobject.cpp:toInt
static inline int toInt(const QChar &qc, int R)
{
    ushort c = qc.unicode();
    int v = -1;
    if (c >= '0' && c <= '9')
        v = c - '0';
    else if (c >= 'A' && c <= 'Z')
        v = c - 'A' + 10;
    else if (c >= 'a' && c <= 'z')
        v = c - 'a' + 10;
    if (v >= 0 && v < R)
        return v;
    else
        return -1;
}

//  from ../qtdeclarative/src/qml/jsruntime/qv4globalobject.cpp, line 464, as _ZN3QV415GlobalFunctions17method_parseFloatEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue GlobalFunctions::method_parseFloat(const FunctionObject *b, const Value *, const Value *argv, int argc)
{
    Scope scope(b);
    // [15.1.2.3] step by step:
    ScopedString inputString(scope, argc ? argv[0] : Value::undefinedValue(), ScopedString::Convert);
    CHECK_EXCEPTION();

    QString trimmed = inputString->toQString().trimmed(); // 2

    // 4:
    if (trimmed.startsWith(QLatin1String("Infinity"))
            || trimmed.startsWith(QLatin1String("+Infinity")))
        RETURN_RESULT(Encode(Q_INFINITY));
    if (trimmed.startsWith(QLatin1String("-Infinity")))
        RETURN_RESULT(Encode(-Q_INFINITY));
    QByteArray ba = trimmed.toLatin1();
    bool ok;
    const char *begin = ba.constData();
    const char *end = nullptr;
    double d = qstrtod(begin, &end, &ok);
    if (end - begin == 0)
        RETURN_RESULT(Encode(std::numeric_limits<double>::quiet_NaN())); // 3
    else
        RETURN_RESULT(Encode(d));
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4globalobject.cpp, line 491, as _ZN3QV415GlobalFunctions12method_isNaNEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue GlobalFunctions::method_isNaN(const FunctionObject *, const Value *, const Value *argv, int argc)
{
    if (!argc)
        // undefined gets converted to NaN
        RETURN_RESULT(Encode(true));

    if (argv[0].integerCompatible())
        RETURN_RESULT(Encode(false));

    double d = argv[0].toNumber();
    RETURN_RESULT(Encode((bool)std::isnan(d)));
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4globalobject.cpp, line 505, as _ZN3QV415GlobalFunctions15method_isFiniteEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue GlobalFunctions::method_isFinite(const FunctionObject *, const Value *, const Value *argv, int argc)
{
    if (!argc)
        // undefined gets converted to NaN
        RETURN_RESULT(Encode(false));

    if (argv[0].integerCompatible())
        RETURN_RESULT(Encode(true));

    double d = argv[0].toNumber();
    RETURN_RESULT(Encode((bool)std::isfinite(d)));
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4globalobject.cpp, line 519, as _ZN3QV415GlobalFunctions16method_decodeURIEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue GlobalFunctions::method_decodeURI(const FunctionObject *b, const Value *, const Value *argv, int argc)
{
    if (argc == 0)
        RETURN_UNDEFINED();

    ExecutionEngine *v4 = b->engine();
    QString uriString = argv[0].toQString();
    bool ok;
    QString out = decode(uriString, DecodeNonReserved, &ok);
    if (!ok) {
        Scope scope(v4);
        ScopedString s(scope, scope.engine->newString(QStringLiteral("malformed URI sequence")));
        RETURN_RESULT(scope.engine->throwURIError(s));
    }

    RETURN_RESULT(v4->newString(out));
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4globalobject.cpp, line 594, as _ZN3QV415GlobalFunctions13method_escapeEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue GlobalFunctions::method_escape(const FunctionObject *b, const Value *, const Value *argv, int argc)
{
    ExecutionEngine *v4 = b->engine();
    if (!argc)
        RETURN_RESULT(v4->newString(QStringLiteral("undefined")));

    QString str = argv[0].toQString();
    RETURN_RESULT(v4->newString(escape(str)));
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4globalobject.cpp, line 604, as _ZN3QV415GlobalFunctions15method_unescapeEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue GlobalFunctions::method_unescape(const FunctionObject *b, const Value *, const Value *argv, int argc)
{
    ExecutionEngine *v4 = b->engine();
    if (!argc)
        RETURN_RESULT(v4->newString(QStringLiteral("undefined")));

    QString str = argv[0].toQString();
    RETURN_RESULT(v4->newString(unescape(str)));
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  ReturnedValue QV4::GlobalFunctions::method_parseFloat(const
//      FunctionObject *a0, const Value *thisObject, const Value *argv, int
//      argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415GlobalFunctions17method_parseFloatEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::GlobalFunctions::method_parseFloat(a0, thisObject, argv, argc);
}

//  ReturnedValue QV4::GlobalFunctions::method_isNaN(const FunctionObject
//      *a0, const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415GlobalFunctions12method_isNaNEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::GlobalFunctions::method_isNaN(a0, thisObject, argv, argc);
}

//  ReturnedValue QV4::GlobalFunctions::method_isFinite(const FunctionObject
//      *a0, const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415GlobalFunctions15method_isFiniteEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::GlobalFunctions::method_isFinite(a0, thisObject, argv, argc);
}

//  ReturnedValue QV4::GlobalFunctions::method_decodeURI(const FunctionObject
//      *a0, const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415GlobalFunctions16method_decodeURIEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::GlobalFunctions::method_decodeURI(a0, thisObject, argv, argc);
}

//  ReturnedValue QV4::GlobalFunctions::method_escape(const FunctionObject
//      *a0, const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415GlobalFunctions13method_escapeEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::GlobalFunctions::method_escape(a0, thisObject, argv, argc);
}

//  ReturnedValue QV4::GlobalFunctions::method_unescape(const FunctionObject
//      *a0, const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415GlobalFunctions15method_unescapeEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::GlobalFunctions::method_unescape(a0, thisObject, argv, argc);
}

//  QV4::GlobalFunctions::~GlobalFunctions()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV415GlobalFunctionsD1Ev(QV4::GlobalFunctions *self) {
  delete self;
}
