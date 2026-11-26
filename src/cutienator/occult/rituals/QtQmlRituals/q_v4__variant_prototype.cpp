//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4variantobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4variantobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4variantobject_p.h>
#include <QtQml/private/qv4functionobject_p.h>
#include <QtQml/private/qqmlvaluetypewrapper_p.h>
#include <QtQml/private/qv4qobjectwrapper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4variantobject.cpp, line 98, as _ZN3QV416VariantPrototype15method_toStringEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue VariantPrototype::method_toString(const FunctionObject *b, const Value *thisObject, const Value *, int)
{
    ExecutionEngine *v4 = b->engine();
    const VariantObject *o = thisObject->as<QV4::VariantObject>();
    if (!o)
        RETURN_UNDEFINED();
    const QVariant variant = o->d()->data();
    QString result = variant.toString();
    if (result.isEmpty() && !variant.canConvert(QMetaType(QMetaType::QString))) {
        QDebug dbg(&result);
        dbg << variant;
        // QDebug appends a space, we're not interested in continuing the stream so we chop it off.
        // Can't use nospace() because it would affect the debug-stream operator of the variant.
        result.chop(1);
    }
    return Encode(v4->newString(result));
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4variantobject.cpp, line 116, as _ZN3QV416VariantPrototype14method_valueOfEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue VariantPrototype::method_valueOf(const FunctionObject *b, const Value *thisObject, const Value *, int)
{
    const VariantObject *o = thisObject->as<QV4::VariantObject>();
    if (o) {
        QVariant v = o->d()->data();
        switch (v.userType()) {
        case QMetaType::UnknownType:
            return Encode::undefined();
        case QMetaType::QString:
            return Encode(b->engine()->newString(v.toString()));
        case QMetaType::Int:
            return Encode(v.toInt());
        case QMetaType::Double:
        case QMetaType::UInt:
            return Encode(v.toDouble());
        case QMetaType::Bool:
            return Encode(v.toBool());
        default:
            if (QMetaType(v.metaType()).flags() & QMetaType::IsEnumeration)
                if (v.metaType().sizeOf() <= qsizetype(sizeof(int)))
                    return Encode(v.toInt());
            if (v.canConvert<double>())
                return Encode(v.toDouble());
            if (v.canConvert<int>())
                return Encode(v.toInt());
            if (v.canConvert<uint>())
                return Encode(v.toUInt());
            if (v.canConvert<bool>())
                return Encode(v.toBool());
            if (v.canConvert<QString>())
                return Encode(b->engine()->newString(v.toString()));
            break;
        }
    }
    return thisObject->asReturnedValue();
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  QV4::Object *QV4::VariantPrototype::defaultPrototype(QV4::ExecutionEngine
//      *e)
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZN3QV416VariantPrototype16defaultPrototypeEPNS_15ExecutionEngineE(
    QV4::ExecutionEngine *e) {
  return QV4::VariantPrototype::defaultPrototype(e);
}

//  ReturnedValue QV4::VariantPrototype::method_toString(const FunctionObject
//      *a0, const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV416VariantPrototype15method_toStringEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::VariantPrototype::method_toString(a0, thisObject, argv, argc);
}

//  ReturnedValue QV4::VariantPrototype::method_valueOf(const FunctionObject
//      *a0, const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV416VariantPrototype14method_valueOfEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::VariantPrototype::method_valueOf(a0, thisObject, argv, argc);
}
