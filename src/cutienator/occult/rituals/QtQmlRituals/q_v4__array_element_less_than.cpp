//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4arraydata_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4arraydata_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4arraydata_p.h>
#include <QtQml/private/qv4object_p.h>
#include <QtQml/private/qv4functionobject_p.h>
#include <QtQml/private/qv4mm_p.h>
#include <QtQml/private/qv4runtime_p.h>
#include <QtQml/private/qv4argumentsobject_p.h>
#include <QtQml/private/qv4string_p.h>
#include <QtQml/private/qv4jscall_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4arraydata.cpp, line 596, as _ZNK3QV420ArrayElementLessThanclENS_5ValueES1_
namespace QV4 {
inline bool ArrayElementLessThan::operator()(Value v1, Value v2) const
{
    Scope scope(m_engine);

    if (v1.isUndefined() || v1.isEmpty())
        return false;
    if (v2.isUndefined() || v2.isEmpty())
        return true;
    ScopedFunctionObject o(scope, m_comparefn);
    if (o) {
        Scope scope(o->engine());
        ScopedValue result(scope);
        JSCallArguments jsCallData(scope, 2);
        jsCallData.args[0] = v1;
        jsCallData.args[1] = v2;
        result = o->call(jsCallData);
        if (scope.hasException())
            return false;

        return result->toNumber() < 0;
    }
    ScopedString p1s(scope, v1.toString(scope.engine));
    ScopedString p2s(scope, v2.toString(scope.engine));

    if (!p1s)
        return false;
    if (!p2s)
        return true;

    return p1s->toQString() < p2s->toQString();
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  QV4::ArrayElementLessThan::ArrayElementLessThan(ExecutionEngine *engine,
//      const Value &comparefn)
extern "C" Q_DECL_EXPORT
QV4::ArrayElementLessThan *ritual_ZN3QV420ArrayElementLessThanC1EPNS_15ExecutionEngineERKNS_5ValueE(
    QV4::ExecutionEngine *engine,
    const QV4::Value *comparefn) {
  return new QV4::ArrayElementLessThan(engine, *comparefn);
}

//  bool QV4::ArrayElementLessThan::operator()(Value v1, Value v2) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV420ArrayElementLessThanclENS_5ValueES1_(
    const QV4::ArrayElementLessThan *self,
    const QV4::Value *v1,
    const QV4::Value *v2) {
  return self->operator()(*v1, *v2);
}

//  QV4::ArrayElementLessThan::~ArrayElementLessThan()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV420ArrayElementLessThanD1Ev(
    QV4::ArrayElementLessThan *self) {
  delete self;
}
