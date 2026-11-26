//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmlsa_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlCompiler/QtQmlCompiler>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmlsa_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQmlCompiler/qqmlsasourcelocation.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsmetatypes_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/qqmlsa.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/qqmlsa.h>
#include <QtQmlCompiler/private/qqmlsa_p.h>
#include <QtQmlCompiler/qqmlsasourcelocation.h>
#include <QtQmlCompiler/private/qqmljsscope_p.h>
#include <QtQmlCompiler/private/qqmljslogger_p.h>
#include <QtQmlCompiler/private/qqmljstyperesolver_p.h>
#include <QtQmlCompiler/private/qqmljsimportvisitor_p.h>
#include <QtQmlCompiler/private/qqmljsutils_p.h>
#include <QtQmlCompiler/private/qdeferredpointer_p.h>
#include <QtQmlCompiler/private/qqmlsasourcelocation_p.h>
#include <memory>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from ../qtdeclarative/src/qmlcompiler/qqmlsa.cpp, line 561, as _ZN6QQmlSA13MethodPrivateC1EPNS_6MethodE
namespace QQmlSA {
using namespace Qt::StringLiterals;
inline MethodPrivate::MethodPrivate(Method *iface) : q_ptr{ iface } { }
}  // namespace QQmlSA

//  from ../qtdeclarative/src/qmlcompiler/qqmlsa.cpp, line 563, as _ZN6QQmlSA13MethodPrivateC1EPNS_6MethodERKS0_
namespace QQmlSA {
using namespace Qt::StringLiterals;
inline MethodPrivate::MethodPrivate(Method *iface, const MethodPrivate &other)
    : m_method{ other.m_method }, q_ptr{ iface }
{
}
}  // namespace QQmlSA

//  from ../qtdeclarative/src/qmlcompiler/qqmlsa.cpp, line 568, as _ZNK6QQmlSA13MethodPrivate10methodNameEv
namespace QQmlSA {
using namespace Qt::StringLiterals;
inline QString MethodPrivate::methodName() const
{
    return m_method.methodName();
}
}  // namespace QQmlSA

//  from ../qtdeclarative/src/qmlcompiler/qqmlsa.cpp, line 573, as _ZNK6QQmlSA13MethodPrivate14sourceLocationEv
namespace QQmlSA {
using namespace Qt::StringLiterals;
inline QQmlSA::SourceLocation MethodPrivate::sourceLocation() const
{
    return QQmlSA::SourceLocationPrivate::createQQmlSASourceLocation(m_method.sourceLocation());
}
}  // namespace QQmlSA

//  from ../qtdeclarative/src/qmlcompiler/qqmlsa.cpp, line 578, as _ZNK6QQmlSA13MethodPrivate10methodTypeEv
namespace QQmlSA {
using namespace Qt::StringLiterals;
inline MethodType MethodPrivate::methodType() const
{
    return m_method.methodType();
}
}  // namespace QQmlSA

//  from ../qtdeclarative/src/qmlcompiler/qqmlsa.cpp, line 680, as _ZN6QQmlSA13MethodPrivate12createMethodERK16QQmlJSMetaMethod
namespace QQmlSA {
using namespace Qt::StringLiterals;
inline QQmlSA::Method MethodPrivate::createMethod(const QQmlJSMetaMethod &jsMethod)
{
    QQmlSA::Method saMethod;
    auto &wrappedMethod = saMethod.d_func()->m_method;
    wrappedMethod = jsMethod;
    return saMethod;
}
}  // namespace QQmlSA

//  from ../qtdeclarative/src/qmlcompiler/qqmlsa.cpp, line 701, as _ZN6QQmlSA13MethodPrivate6methodERKNS_6MethodE
namespace QQmlSA {
using namespace Qt::StringLiterals;
inline QQmlJSMetaMethod MethodPrivate::method(const QQmlSA::Method &method)
{
    return method.d_func()->m_method;
}
}  // namespace QQmlSA
//  -----------------------------------------------------------------------

//  Method *QQmlSA::MethodPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQmlSA::Method *ritual_ZN6QQmlSA13MethodPrivate6q_funcEv(
    QQmlSA::MethodPrivate *self) {
  return self->q_func();
}

//  const Method *QQmlSA::MethodPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQmlSA::Method *ritual_ZNK6QQmlSA13MethodPrivate6q_funcEv(
    const QQmlSA::MethodPrivate *self) {
  return self->q_func();
}

//  QQmlSA::MethodPrivate::MethodPrivate(Method *a0)
extern "C" Q_DECL_EXPORT
QQmlSA::MethodPrivate *ritual_ZN6QQmlSA13MethodPrivateC1EPNS_6MethodE(
    QQmlSA::Method *a0) {
  return new QQmlSA::MethodPrivate(a0);
}

//  QQmlSA::MethodPrivate::MethodPrivate(Method *a0, const MethodPrivate &a1)
extern "C" Q_DECL_EXPORT
QQmlSA::MethodPrivate *ritual_ZN6QQmlSA13MethodPrivateC1EPNS_6MethodERKS0_(
    QQmlSA::Method *a0,
    const QQmlSA::MethodPrivate *a1) {
  return new QQmlSA::MethodPrivate(a0, *a1);
}

//  QString QQmlSA::MethodPrivate::methodName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK6QQmlSA13MethodPrivate10methodNameEv(
    const QQmlSA::MethodPrivate *self) {
  return new QString(self->methodName());
}

//  QQmlSA::SourceLocation QQmlSA::MethodPrivate::sourceLocation() const
extern "C" Q_DECL_EXPORT
QQmlSA::SourceLocation *ritual_ZNK6QQmlSA13MethodPrivate14sourceLocationEv(
    const QQmlSA::MethodPrivate *self) {
  return new QQmlSA::SourceLocation(self->sourceLocation());
}

//  MethodType QQmlSA::MethodPrivate::methodType() const
extern "C" Q_DECL_EXPORT
QQmlSA::MethodType ritual_ZNK6QQmlSA13MethodPrivate10methodTypeEv(
    const QQmlSA::MethodPrivate *self) {
  return self->methodType();
}

//  QQmlSA::Method QQmlSA::MethodPrivate::createMethod(const QQmlJSMetaMethod
//      &a0)
extern "C" Q_DECL_EXPORT
QQmlSA::Method *ritual_ZN6QQmlSA13MethodPrivate12createMethodERK16QQmlJSMetaMethod(
    const QQmlJSMetaMethod *a0) {
  return new QQmlSA::Method(QQmlSA::MethodPrivate::createMethod(*a0));
}

//  QQmlJSMetaMethod QQmlSA::MethodPrivate::method(const QQmlSA::Method &a0)
extern "C" Q_DECL_EXPORT
QQmlJSMetaMethod *ritual_ZN6QQmlSA13MethodPrivate6methodERKNS_6MethodE(
    const QQmlSA::Method *a0) {
  return new QQmlJSMetaMethod(QQmlSA::MethodPrivate::method(*a0));
}

//  QQmlSA::MethodPrivate::~MethodPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlSA13MethodPrivateD1Ev(QQmlSA::MethodPrivate *self) {
  delete self;
}
