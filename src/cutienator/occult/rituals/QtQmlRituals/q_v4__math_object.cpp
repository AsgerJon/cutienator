//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4mathobject_p.h, Qt 6.12.0. Edited by hand
//  on 2026-11-27: code taken from Qt's source no longer stands under
//  defined(Q_OS_LINUX), which Qt does not write there; its rituals no longer
//  stand under defined(Q_OS_LINUX), as the code taken from Qt they call no
//  longer does. Kept as it is when the generator runs again.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4mathobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4mathobject_p.h>
#include <QtQml/private/qv4symbol_p.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qmath.h>
#include <QtCore/qrandom.h>
#include <QtCore/private/qnumeric_p.h>
#include <QtCore/qthreadstorage.h>
#include <cmath>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4mathobject.cpp, line 75, as local:qv4mathobject.cpp:copySign
static Q_ALWAYS_INLINE double copySign(double x, double y)
{
    return ::copysign(x, y);
}

//  from ../qtdeclarative/src/qml/jsruntime/qv4mathobject.cpp, line 80, as _ZN3QV410MathObject10method_absEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue MathObject::method_abs(const FunctionObject *, const Value *, const Value *argv, int argc)
{
    if (!argc)
        RETURN_RESULT(Encode(qt_qnan()));

    if (argv[0].isInteger()) {
        int i = argv[0].integerValue();
        RETURN_RESULT(Encode(i < 0 ? - i : i));
    }

    double v = argv[0].toNumber();
    if (v == 0) // 0 | -0
        RETURN_RESULT(Encode(0));

    RETURN_RESULT(Encode(v < 0 ? -v : v));
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4mathobject.cpp, line 97, as _ZN3QV410MathObject11method_acosEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue MathObject::method_acos(const FunctionObject *, const Value *, const Value *argv, int argc)
{
    double v = argc ? argv[0].toNumber() : 2;
    if (v > 1)
        RETURN_RESULT(Encode(qt_qnan()));

    RETURN_RESULT(Encode(std::acos(v)));
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4mathobject.cpp, line 106, as _ZN3QV410MathObject12method_acoshEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue MathObject::method_acosh(const FunctionObject *, const Value *, const Value *argv, int argc)
{
    double v = argc ? argv[0].toNumber() : 2;
    if (v < 1)
        RETURN_RESULT(Encode(qt_qnan()));

#ifdef Q_CC_MINGW
    // Mingw has a broken std::acosh(). It returns NaN when passed Infinity.
    if (std::isinf(v))
        RETURN_RESULT(Encode(v));
#endif
    RETURN_RESULT(Encode(std::acosh(v)));
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4mathobject.cpp, line 120, as _ZN3QV410MathObject11method_asinEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue MathObject::method_asin(const FunctionObject *, const Value *, const Value *argv, int argc)
{
    double v = argc ? argv[0].toNumber() : 2;
    if (v > 1)
        RETURN_RESULT(Encode(qt_qnan()));
    else
        RETURN_RESULT(Encode(std::asin(v)));
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4mathobject.cpp, line 129, as _ZN3QV410MathObject12method_asinhEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue MathObject::method_asinh(const FunctionObject *, const Value *, const Value *argv, int argc)
{
    double v = argc ? argv[0].toNumber() : 2;
    if (v == 0.0)
        RETURN_RESULT(Encode(v));
    RETURN_RESULT(Encode(std::asinh(v)));
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4mathobject.cpp, line 137, as _ZN3QV410MathObject11method_atanEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue MathObject::method_atan(const FunctionObject *, const Value *, const Value *argv, int argc)
{
    double v = argc ? argv[0].toNumber() : qt_qnan();
    if (v == 0.0)
        RETURN_RESULT(Encode(v));
    else
        RETURN_RESULT(Encode(std::atan(v)));
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4mathobject.cpp, line 146, as _ZN3QV410MathObject12method_atanhEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue MathObject::method_atanh(const FunctionObject *, const Value *, const Value *argv, int argc)
{
    double v = argc ? argv[0].toNumber() : qt_qnan();
    if (v == 0.0)
        RETURN_RESULT(Encode(v));

    RETURN_RESULT(Encode(std::atanh(v)));
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4mathobject.cpp, line 173, as _ZN3QV410MathObject11method_cbrtEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue MathObject::method_cbrt(const FunctionObject *, const Value *, const Value *argv, int argc)
{
    double v = argc ? argv[0].toNumber() : qt_qnan();
    RETURN_RESULT(Encode(std::cbrt(v))); // cube root
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4mathobject.cpp, line 188, as _ZN3QV410MathObject12method_clz32EPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue MathObject::method_clz32(const FunctionObject *, const Value *, const Value *argv, int argc)
{
    quint32 v = argc ? argv[0].toUInt32() : 0;
    RETURN_RESULT(Encode(qint32(qCountLeadingZeroBits(v))));
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4mathobject.cpp, line 194, as _ZN3QV410MathObject10method_cosEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue MathObject::method_cos(const FunctionObject *, const Value *, const Value *argv, int argc)
{
    double v = argc ? argv[0].toNumber() : qt_qnan();
    RETURN_RESULT(Encode(std::cos(v)));
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4mathobject.cpp, line 200, as _ZN3QV410MathObject11method_coshEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue MathObject::method_cosh(const FunctionObject *, const Value *, const Value *argv, int argc)
{
    double v = argc ? argv[0].toNumber() : qt_qnan();
    RETURN_RESULT(Encode(std::cosh(v)));
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4mathobject.cpp, line 234, as _ZN3QV410MathObject12method_floorEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue MathObject::method_floor(const FunctionObject *, const Value *, const Value *argv, int argc)
{
    double v = argc ? argv[0].toNumber() : qt_qnan();
    Value result = Value::fromDouble(std::floor(v));
    result.isInt32();
    RETURN_RESULT(result);
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4mathobject.cpp, line 242, as _ZN3QV410MathObject13method_froundEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue MathObject::method_fround(const FunctionObject *, const Value *, const Value *argv, int argc)
{
    double v = argc ? argv[0].toNumber() : qt_qnan();
    if (std::isnan(v) || qt_is_inf(v) || qIsNull(v))
        RETURN_RESULT(Encode(v));
    else // convert to 32-bit float using roundTiesToEven, then convert back to 64-bit double
        RETURN_RESULT(Encode(double(float(v))));
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4mathobject.cpp, line 251, as _ZN3QV410MathObject12method_hypotEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue MathObject::method_hypot(const FunctionObject *, const Value *, const Value *argv, int argc)
{
    // ES6 Math.hypot(v1, ..., vn) -> sqrt(sum(vi**2)) but "should take care to
    // avoid the loss of precision from overflows and underflows" (as std::hypot does).
    double v = 0;
    // Spec mandates +0 on no args; and says nothing about what to do if toNumber() signals ...
    if (argc > 0) {
        QtPrivate::QHypotHelper<double> h(argv[0].toNumber());
        for (int i = 1; i < argc; i++)
            h = h.add(argv[i].toNumber());
        v = h.result();
    }
    RETURN_RESULT(Value::fromDouble(v));
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4mathobject.cpp, line 266, as _ZN3QV410MathObject11method_imulEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue MathObject::method_imul(const FunctionObject *, const Value *, const Value *argv, int argc)
{
    quint32 a = argc ? argv[0].toUInt32() : 0;
    quint32 b = argc > 0 ? argv[1].toUInt32() : 0;
    qint32 product = a * b;
    RETURN_RESULT(Encode(product));
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4mathobject.cpp, line 274, as _ZN3QV410MathObject10method_logEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue MathObject::method_log(const FunctionObject *, const Value *, const Value *argv, int argc)
{
    double v = argc ? argv[0].toNumber() : qt_qnan();
    if (v < 0)
        RETURN_RESULT(Encode(qt_qnan()));
    else
        RETURN_RESULT(Encode(std::log(v)));
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4mathobject.cpp, line 283, as _ZN3QV410MathObject12method_log10EPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue MathObject::method_log10(const FunctionObject *, const Value *, const Value *argv, int argc)
{
    double v = argc ? argv[0].toNumber() : qt_qnan();
    if (v < 0)
        RETURN_RESULT(Encode(qt_qnan()));
    else
        RETURN_RESULT(Encode(std::log10(v)));
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4mathobject.cpp, line 292, as _ZN3QV410MathObject12method_log1pEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue MathObject::method_log1p(const FunctionObject *, const Value *, const Value *argv, int argc)
{
#if !defined(__ANDROID__)
    using std::log1p;
#endif
    double v = argc ? argv[0].toNumber() : qt_qnan();
    if (v < -1)
        RETURN_RESULT(Encode(qt_qnan()));
    else
        RETURN_RESULT(Encode(log1p(v)));
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4mathobject.cpp, line 304, as _ZN3QV410MathObject11method_log2EPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue MathObject::method_log2(const FunctionObject *, const Value *, const Value *argv, int argc)
{
    double v = argc ? argv[0].toNumber() : qt_qnan();
    if (v < 0) {
        RETURN_RESULT(Encode(qt_qnan()));
    } else {
        RETURN_RESULT(Encode(std::log2(v)));
    }
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4mathobject.cpp, line 340, as _ZN3QV410MathObject10method_powEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue MathObject::method_pow(const FunctionObject *, const Value *, const Value *argv, int argc)
{
    double x = argc > 0 ? argv[0].toNumber() : qt_qnan();
    double y = argc > 1 ? argv[1].toNumber() : qt_qnan();

    RETURN_RESULT(Encode(QQmlPrivate::jsExponentiate(x, y)));
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4mathobject.cpp, line 348, as _ZN3QV410MathObject13method_randomEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue MathObject::method_random(const FunctionObject *, const Value *, const Value *, int)
{
    RETURN_RESULT(Encode(QRandomGenerator::global()->generateDouble()));
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4mathobject.cpp, line 353, as _ZN3QV410MathObject12method_roundEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue MathObject::method_round(const FunctionObject *, const Value *, const Value *argv, int argc)
{
    double v = argc ? argv[0].toNumber() : qt_qnan();
    if (!std::isfinite(v))
        RETURN_RESULT(Encode(v));

    if (v < 0.5 && v >= -0.5)
        v = std::copysign(0.0, v);
    else
        v = std::floor(v + 0.5);
    RETURN_RESULT(Encode(v));
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4mathobject.cpp, line 366, as _ZN3QV410MathObject11method_signEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue MathObject::method_sign(const FunctionObject *, const Value *, const Value *argv, int argc)
{
    double v = argc ? argv[0].toNumber() : qt_qnan();

    if (std::isnan(v))
        RETURN_RESULT(Encode(qt_qnan()));

    if (qIsNull(v))
        RETURN_RESULT(Encode(v));

    RETURN_RESULT(Encode(std::signbit(v) ? -1 : 1));
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4mathobject.cpp, line 379, as _ZN3QV410MathObject10method_sinEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue MathObject::method_sin(const FunctionObject *, const Value *, const Value *argv, int argc)
{
    double v = argc ? argv[0].toNumber() : qt_qnan();
    if (v == 0.0)
        RETURN_RESULT(Encode(v));
    else
        RETURN_RESULT(Encode(std::sin(v)));
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4mathobject.cpp, line 388, as _ZN3QV410MathObject11method_sinhEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue MathObject::method_sinh(const FunctionObject *, const Value *, const Value *argv, int argc)
{
    double v = argc ? argv[0].toNumber() : qt_qnan();
    if (v == 0.0)
        RETURN_RESULT(Encode(v));
    else
        RETURN_RESULT(Encode(std::sinh(v)));
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4mathobject.cpp, line 397, as _ZN3QV410MathObject11method_sqrtEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue MathObject::method_sqrt(const FunctionObject *, const Value *, const Value *argv, int argc)
{
    double v = argc ? argv[0].toNumber() : qt_qnan();
    RETURN_RESULT(Encode(std::sqrt(v)));
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4mathobject.cpp, line 403, as _ZN3QV410MathObject10method_tanEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue MathObject::method_tan(const FunctionObject *, const Value *, const Value *argv, int argc)
{
    double v = argc ? argv[0].toNumber() : qt_qnan();
    if (v == 0.0)
        RETURN_RESULT(Encode(v));
    else
        RETURN_RESULT(Encode(std::tan(v)));
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4mathobject.cpp, line 412, as _ZN3QV410MathObject11method_tanhEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue MathObject::method_tanh(const FunctionObject *, const Value *, const Value *argv, int argc)
{
    double v = argc ? argv[0].toNumber() : qt_qnan();
    if (v == 0.0)
        RETURN_RESULT(Encode(v));
    else
        RETURN_RESULT(Encode(std::tanh(v)));
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4mathobject.cpp, line 421, as _ZN3QV410MathObject12method_truncEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue MathObject::method_trunc(const FunctionObject *, const Value *, const Value *argv, int argc)
{
    double v = argc ? argv[0].toNumber() : qt_qnan();
    RETURN_RESULT(Encode(std::trunc(v)));
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::MathObject::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV410MathObject10__dataTestEv(QV4::MathObject *self) {
  self->__dataTest();
}

//  QV4::Heap::MathObject *QV4::MathObject::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::MathObject *ritual_ZNK3QV410MathObject11d_uncheckedEv(
    const QV4::MathObject *self) {
  return self->d_unchecked();
}

//  QV4::Heap::MathObject *QV4::MathObject::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::MathObject *ritual_ZNK3QV410MathObject1dEv(
    const QV4::MathObject *self) {
  return self->d();
}

//  ReturnedValue QV4::MathObject::method_abs(const FunctionObject *a0, const
//      Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV410MathObject10method_absEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::MathObject::method_abs(a0, thisObject, argv, argc);
}

//  ReturnedValue QV4::MathObject::method_acos(const FunctionObject *a0,
//      const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV410MathObject11method_acosEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::MathObject::method_acos(a0, thisObject, argv, argc);
}

//  ReturnedValue QV4::MathObject::method_acosh(const FunctionObject *a0,
//      const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV410MathObject12method_acoshEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::MathObject::method_acosh(a0, thisObject, argv, argc);
}

//  ReturnedValue QV4::MathObject::method_asin(const FunctionObject *a0,
//      const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV410MathObject11method_asinEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::MathObject::method_asin(a0, thisObject, argv, argc);
}

//  ReturnedValue QV4::MathObject::method_asinh(const FunctionObject *a0,
//      const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV410MathObject12method_asinhEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::MathObject::method_asinh(a0, thisObject, argv, argc);
}

//  ReturnedValue QV4::MathObject::method_atan(const FunctionObject *a0,
//      const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV410MathObject11method_atanEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::MathObject::method_atan(a0, thisObject, argv, argc);
}

//  ReturnedValue QV4::MathObject::method_atanh(const FunctionObject *a0,
//      const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV410MathObject12method_atanhEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::MathObject::method_atanh(a0, thisObject, argv, argc);
}

//  ReturnedValue QV4::MathObject::method_cbrt(const FunctionObject *a0,
//      const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV410MathObject11method_cbrtEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::MathObject::method_cbrt(a0, thisObject, argv, argc);
}

//  ReturnedValue QV4::MathObject::method_clz32(const FunctionObject *a0,
//      const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV410MathObject12method_clz32EPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::MathObject::method_clz32(a0, thisObject, argv, argc);
}

//  ReturnedValue QV4::MathObject::method_cos(const FunctionObject *a0, const
//      Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV410MathObject10method_cosEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::MathObject::method_cos(a0, thisObject, argv, argc);
}

//  ReturnedValue QV4::MathObject::method_cosh(const FunctionObject *a0,
//      const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV410MathObject11method_coshEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::MathObject::method_cosh(a0, thisObject, argv, argc);
}

//  ReturnedValue QV4::MathObject::method_floor(const FunctionObject *a0,
//      const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV410MathObject12method_floorEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::MathObject::method_floor(a0, thisObject, argv, argc);
}

//  ReturnedValue QV4::MathObject::method_fround(const FunctionObject *a0,
//      const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV410MathObject13method_froundEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::MathObject::method_fround(a0, thisObject, argv, argc);
}

//  ReturnedValue QV4::MathObject::method_hypot(const FunctionObject *a0,
//      const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV410MathObject12method_hypotEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::MathObject::method_hypot(a0, thisObject, argv, argc);
}

//  ReturnedValue QV4::MathObject::method_imul(const FunctionObject *a0,
//      const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV410MathObject11method_imulEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::MathObject::method_imul(a0, thisObject, argv, argc);
}

//  ReturnedValue QV4::MathObject::method_log(const FunctionObject *a0, const
//      Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV410MathObject10method_logEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::MathObject::method_log(a0, thisObject, argv, argc);
}

//  ReturnedValue QV4::MathObject::method_log10(const FunctionObject *a0,
//      const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV410MathObject12method_log10EPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::MathObject::method_log10(a0, thisObject, argv, argc);
}

//  ReturnedValue QV4::MathObject::method_log1p(const FunctionObject *a0,
//      const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV410MathObject12method_log1pEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::MathObject::method_log1p(a0, thisObject, argv, argc);
}

//  ReturnedValue QV4::MathObject::method_log2(const FunctionObject *a0,
//      const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV410MathObject11method_log2EPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::MathObject::method_log2(a0, thisObject, argv, argc);
}

//  ReturnedValue QV4::MathObject::method_pow(const FunctionObject *a0, const
//      Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV410MathObject10method_powEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::MathObject::method_pow(a0, thisObject, argv, argc);
}

//  ReturnedValue QV4::MathObject::method_random(const FunctionObject *a0,
//      const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV410MathObject13method_randomEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::MathObject::method_random(a0, thisObject, argv, argc);
}

//  ReturnedValue QV4::MathObject::method_round(const FunctionObject *a0,
//      const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV410MathObject12method_roundEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::MathObject::method_round(a0, thisObject, argv, argc);
}

//  ReturnedValue QV4::MathObject::method_sign(const FunctionObject *a0,
//      const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV410MathObject11method_signEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::MathObject::method_sign(a0, thisObject, argv, argc);
}

//  ReturnedValue QV4::MathObject::method_sin(const FunctionObject *a0, const
//      Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV410MathObject10method_sinEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::MathObject::method_sin(a0, thisObject, argv, argc);
}

//  ReturnedValue QV4::MathObject::method_sinh(const FunctionObject *a0,
//      const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV410MathObject11method_sinhEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::MathObject::method_sinh(a0, thisObject, argv, argc);
}

//  ReturnedValue QV4::MathObject::method_sqrt(const FunctionObject *a0,
//      const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV410MathObject11method_sqrtEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::MathObject::method_sqrt(a0, thisObject, argv, argc);
}

//  ReturnedValue QV4::MathObject::method_tan(const FunctionObject *a0, const
//      Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV410MathObject10method_tanEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::MathObject::method_tan(a0, thisObject, argv, argc);
}

//  ReturnedValue QV4::MathObject::method_tanh(const FunctionObject *a0,
//      const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV410MathObject11method_tanhEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::MathObject::method_tanh(a0, thisObject, argv, argc);
}

//  ReturnedValue QV4::MathObject::method_trunc(const FunctionObject *a0,
//      const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV410MathObject12method_truncEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::MathObject::method_trunc(a0, thisObject, argv, argc);
}
