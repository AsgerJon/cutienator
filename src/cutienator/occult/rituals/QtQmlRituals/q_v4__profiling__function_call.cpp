//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4profiling_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/qtqmlglobal.h>
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#if !(!QT_CONFIG(qml_debug))
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4profiling_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4profiling_p.h>
#include <QtQml/private/qv4mm_p.h>
#include <QtQml/private/qv4string_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4profiling.cpp, line 14, as _ZNK3QV49Profiling12FunctionCall15resolveLocationEv
namespace QV4::Profiling {
inline FunctionLocation FunctionCall::resolveLocation() const
{
    return FunctionLocation(m_function->name()->toQString(),
                            m_function->executableCompilationUnit()->fileName(),
                            m_function->compiledFunction->location.line(),
                            m_function->compiledFunction->location.column());
}
}  // namespace QV4::Profiling

//  from ../qtdeclarative/src/qml/jsruntime/qv4profiling.cpp, line 22, as _ZNK3QV49Profiling12FunctionCall10propertiesEv
namespace QV4::Profiling {
inline FunctionCallProperties FunctionCall::properties() const
{
    FunctionCallProperties props = {
        m_start,
        m_end,
        reinterpret_cast<quintptr>(m_function)
    };
    return props;
}
}  // namespace QV4::Profiling
//  -----------------------------------------------------------------------

//  QV4::Profiling::FunctionCall::FunctionCall()
extern "C" Q_DECL_EXPORT
QV4::Profiling::FunctionCall *ritual_ZN3QV49Profiling12FunctionCallC1Ev() {
  return new QV4::Profiling::FunctionCall();
}

//  QV4::Profiling::FunctionCall::FunctionCall(Function *function, qint64
//      start, qint64 end)
extern "C" Q_DECL_EXPORT
QV4::Profiling::FunctionCall *ritual_ZN3QV49Profiling12FunctionCallC1EPNS_8FunctionExx(
    QV4::Function *function,
    qint64 start,
    qint64 end) {
  return new QV4::Profiling::FunctionCall(function, start, end);
}

//  QV4::Profiling::FunctionCall::FunctionCall(const FunctionCall &other)
extern "C" Q_DECL_EXPORT
QV4::Profiling::FunctionCall *ritual_ZN3QV49Profiling12FunctionCallC1ERKS1_(
    const QV4::Profiling::FunctionCall *other) {
  return new QV4::Profiling::FunctionCall(*other);
}

//  QV4::Profiling::FunctionCall::FunctionCall(FunctionCall &&other)
extern "C" Q_DECL_EXPORT
QV4::Profiling::FunctionCall *ritual_ZN3QV49Profiling12FunctionCallC1EOS1_(
    QV4::Profiling::FunctionCall *other) {
  return new QV4::Profiling::FunctionCall(std::move(*other));
}

//  QV4::Profiling::FunctionCall::~FunctionCall()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV49Profiling12FunctionCallD1Ev(
    QV4::Profiling::FunctionCall *self) {
  delete self;
}

//  FunctionCall &QV4::Profiling::FunctionCall::operator=(const FunctionCall
//      &other)
extern "C" Q_DECL_EXPORT
QV4::Profiling::FunctionCall *ritual_ZN3QV49Profiling12FunctionCallaSERKS1_(
    QV4::Profiling::FunctionCall *self,
    const QV4::Profiling::FunctionCall *other) {
  return &(self->operator=(*other));
}

//  FunctionCall &QV4::Profiling::FunctionCall::operator=(FunctionCall
//      &&other)
extern "C" Q_DECL_EXPORT
QV4::Profiling::FunctionCall *ritual_ZN3QV49Profiling12FunctionCallaSEOS1_(
    QV4::Profiling::FunctionCall *self,
    QV4::Profiling::FunctionCall *other) {
  return &(self->operator=(std::move(*other)));
}

//  void QV4::Profiling::FunctionCall::swap(FunctionCall &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV49Profiling12FunctionCall4swapERS1_(
    QV4::Profiling::FunctionCall *self,
    QV4::Profiling::FunctionCall *other) {
  self->swap(*other);
}

//  Function *QV4::Profiling::FunctionCall::function() const
extern "C" Q_DECL_EXPORT
QV4::Function *ritual_ZNK3QV49Profiling12FunctionCall8functionEv(
    const QV4::Profiling::FunctionCall *self) {
  return self->function();
}

//  FunctionLocation QV4::Profiling::FunctionCall::resolveLocation() const
extern "C" Q_DECL_EXPORT
QV4::Profiling::FunctionLocation *ritual_ZNK3QV49Profiling12FunctionCall15resolveLocationEv(
    const QV4::Profiling::FunctionCall *self) {
  return new QV4::Profiling::FunctionLocation(self->resolveLocation());
}

//  FunctionCallProperties QV4::Profiling::FunctionCall::properties() const
extern "C" Q_DECL_EXPORT
QV4::Profiling::FunctionCallProperties *ritual_ZNK3QV49Profiling12FunctionCall10propertiesEv(
    const QV4::Profiling::FunctionCall *self) {
  return new QV4::Profiling::FunctionCallProperties(self->properties());
}

#endif  // !(!QT_CONFIG(qml_debug))
