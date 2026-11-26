//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4numberobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4numberobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4numberobject_p.h>
#include <QtQml/private/qv4runtime_p.h>
#include <QtCore/qnumeric.h>
#include <QtCore/qmath.h>
#include <QtCore/QDebug>
#include <cassert>
#include <limits>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4numberobject.cpp, line 125, as _ZN3QV415NumberPrototype15method_isFiniteEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue NumberPrototype::method_isFinite(const FunctionObject *, const Value *, const Value *argv, int argc)
{
    if (!argc || !argv[0].isNumber())
        return Encode(false);

    double v = argv[0].toNumber();
    return Encode(!std::isnan(v) && !qt_is_inf(v));
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4numberobject.cpp, line 134, as _ZN3QV415NumberPrototype16method_isIntegerEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue NumberPrototype::method_isInteger(const FunctionObject *, const Value *, const Value *argv, int argc)
{
    if (!argc)
        return Encode(false);

    const Value &v = argv[0];
    if (!v.isNumber())
        return Encode(false);

    double dv = v.toNumber();
    if (std::isnan(dv) || qt_is_inf(dv))
        return Encode(false);

    double iv = v.toInteger();
    return Encode(dv == iv);
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4numberobject.cpp, line 151, as _ZN3QV415NumberPrototype20method_isSafeIntegerEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue NumberPrototype::method_isSafeInteger(const FunctionObject *, const Value *, const Value *argv, int argc)
{
    if (!argc)
        return Encode(false);

    const Value &v = argv[0];
    if (!v.isNumber())
        return Encode(false);

    double dv = v.toNumber();
    if (std::isnan(dv) || qt_is_inf(dv))
        return Encode(false);

    double iv = v.toInteger();
    return Encode(dv == iv && std::fabs(iv) <= (1LL << 53) - 1);
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4numberobject.cpp, line 168, as _ZN3QV415NumberPrototype12method_isNaNEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue NumberPrototype::method_isNaN(const FunctionObject *, const Value *, const Value *argv, int argc)
{
    if (!argc || !argv[0].isNumber())
        return Encode(false);

    double v = argv[0].toNumber();
    // cast to bool explicitly as std::isnan() may give us ::isnan(), which
    // sometimes returns an int and we don't want the Encode(int) overload.
    return Encode(bool(std::isnan(v)));
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  QV4::Object *QV4::NumberPrototype::defaultPrototype(QV4::ExecutionEngine
//      *e)
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZN3QV415NumberPrototype16defaultPrototypeEPNS_15ExecutionEngineE(
    QV4::ExecutionEngine *e) {
  return QV4::NumberPrototype::defaultPrototype(e);
}

//  ReturnedValue QV4::NumberPrototype::method_isFinite(const FunctionObject
//      *a0, const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415NumberPrototype15method_isFiniteEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::NumberPrototype::method_isFinite(a0, thisObject, argv, argc);
}

//  ReturnedValue QV4::NumberPrototype::method_isInteger(const FunctionObject
//      *a0, const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415NumberPrototype16method_isIntegerEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::NumberPrototype::method_isInteger(a0, thisObject, argv, argc);
}

//  ReturnedValue QV4::NumberPrototype::method_isSafeInteger(const
//      FunctionObject *a0, const Value *thisObject, const Value *argv, int
//      argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415NumberPrototype20method_isSafeIntegerEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::NumberPrototype::method_isSafeInteger(
      a0,
      thisObject,
      argv,
      argc);
}

//  ReturnedValue QV4::NumberPrototype::method_isNaN(const FunctionObject
//      *a0, const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415NumberPrototype12method_isNaNEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::NumberPrototype::method_isNaN(a0, thisObject, argv, argc);
}
