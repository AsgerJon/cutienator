//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmlsa_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlCompiler/qqmlsa.h>
#include <QtQmlCompiler/QtQmlCompiler>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmlsa_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/QMultiHash>
#include <QtCore/QString>
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

//  from ../qtdeclarative/src/qmlcompiler/qqmlsa.cpp, line 549, as _ZN6QQmlSA14MethodsPrivateC1EPNS_6Method7MethodsE
namespace QQmlSA {
using namespace Qt::StringLiterals;
inline MethodsPrivate::MethodsPrivate(QQmlSA::Method::Methods *iface) : q_ptr{ iface } { }
}  // namespace QQmlSA

//  from ../qtdeclarative/src/qmlcompiler/qqmlsa.cpp, line 551, as _ZN6QQmlSA14MethodsPrivateC1EPNS_6Method7MethodsERKS0_
namespace QQmlSA {
using namespace Qt::StringLiterals;
inline MethodsPrivate::MethodsPrivate(QQmlSA::Method::Methods *iface, const MethodsPrivate &other)
    : m_methods{ other.m_methods }, q_ptr{ iface }
{
}
}  // namespace QQmlSA

//  from ../qtdeclarative/src/qmlcompiler/qqmlsa.cpp, line 556, as _ZN6QQmlSA14MethodsPrivateC1EPNS_6Method7MethodsEOS0_
namespace QQmlSA {
using namespace Qt::StringLiterals;
inline MethodsPrivate::MethodsPrivate(QQmlSA::Method::Methods *iface, MethodsPrivate &&other)
    : m_methods{ std::move(other.m_methods) }, q_ptr{ iface }
{
}
}  // namespace QQmlSA

//  from ../qtdeclarative/src/qmlcompiler/qqmlsa.cpp, line 525, as _ZNK6QQmlSA14MethodsPrivate10constBeginEv
namespace QQmlSA {
using namespace Qt::StringLiterals;
inline QMultiHash<QString, Method>::const_iterator MethodsPrivate::constBegin() const
{
    return m_methods.constBegin();
}
}  // namespace QQmlSA

//  from ../qtdeclarative/src/qmlcompiler/qqmlsa.cpp, line 544, as _ZNK6QQmlSA14MethodsPrivate8constEndEv
namespace QQmlSA {
using namespace Qt::StringLiterals;
inline QMultiHash<QString, Method>::const_iterator MethodsPrivate::constEnd() const
{
    return m_methods.constEnd();
}
}  // namespace QQmlSA

//  from ../qtdeclarative/src/qmlcompiler/qqmlsa.cpp, line 688, as _ZN6QQmlSA14MethodsPrivate13createMethodsERK10QMultiHashI7QString16QQmlJSMetaMethodE
namespace QQmlSA {
using namespace Qt::StringLiterals;
inline QQmlSA::Method::Methods
MethodsPrivate::createMethods(const QMultiHash<QString, QQmlJSMetaMethod> &hash)
{
    QMultiHash<QString, QQmlSA::Method> saMethods;
    for (const auto &[key, value] : hash.asKeyValueRange()) {
        saMethods.insert(key, MethodPrivate::createMethod(value));
    }

    QQmlSA::Method::Methods methods;
    methods.d_func()->m_methods = std::move(saMethods);
    return methods;
}
}  // namespace QQmlSA
//  -----------------------------------------------------------------------

//  QQmlSA::Method::Methods *QQmlSA::MethodsPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQmlSA::Method::Methods *ritual_ZN6QQmlSA14MethodsPrivate6q_funcEv(
    QQmlSA::MethodsPrivate *self) {
  return self->q_func();
}

//  const QQmlSA::Method::Methods *QQmlSA::MethodsPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQmlSA::Method::Methods *ritual_ZNK6QQmlSA14MethodsPrivate6q_funcEv(
    const QQmlSA::MethodsPrivate *self) {
  return self->q_func();
}

//  QQmlSA::MethodsPrivate::MethodsPrivate(QQmlSA::Method::Methods *a0)
extern "C" Q_DECL_EXPORT
QQmlSA::MethodsPrivate *ritual_ZN6QQmlSA14MethodsPrivateC1EPNS_6Method7MethodsE(
    QQmlSA::Method::Methods *a0) {
  return new QQmlSA::MethodsPrivate(a0);
}

//  QQmlSA::MethodsPrivate::MethodsPrivate(QQmlSA::Method::Methods *a0, const
//      MethodsPrivate &a1)
extern "C" Q_DECL_EXPORT
QQmlSA::MethodsPrivate *ritual_ZN6QQmlSA14MethodsPrivateC1EPNS_6Method7MethodsERKS0_(
    QQmlSA::Method::Methods *a0,
    const QQmlSA::MethodsPrivate *a1) {
  return new QQmlSA::MethodsPrivate(a0, *a1);
}

//  QQmlSA::MethodsPrivate::MethodsPrivate(QQmlSA::Method::Methods *a0,
//      MethodsPrivate &&a1)
extern "C" Q_DECL_EXPORT
QQmlSA::MethodsPrivate *ritual_ZN6QQmlSA14MethodsPrivateC1EPNS_6Method7MethodsEOS0_(
    QQmlSA::Method::Methods *a0,
    QQmlSA::MethodsPrivate *a1) {
  return new QQmlSA::MethodsPrivate(a0, std::move(*a1));
}

//  QQmlSA::MethodsPrivate::~MethodsPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlSA14MethodsPrivateD1Ev(QQmlSA::MethodsPrivate *self) {
  delete self;
}

//  QMultiHash<QString, Method>::const_iterator
//      QQmlSA::MethodsPrivate::constBegin() const
extern "C" Q_DECL_EXPORT
QMultiHash<QString, QQmlSA::Method>::const_iterator *ritual_ZNK6QQmlSA14MethodsPrivate10constBeginEv(
    const QQmlSA::MethodsPrivate *self) {
  return new QMultiHash<QString, QQmlSA::Method>::const_iterator(
      self->constBegin());
}

//  QMultiHash<QString, Method>::const_iterator
//      QQmlSA::MethodsPrivate::constEnd() const
extern "C" Q_DECL_EXPORT
QMultiHash<QString, QQmlSA::Method>::const_iterator *ritual_ZNK6QQmlSA14MethodsPrivate8constEndEv(
    const QQmlSA::MethodsPrivate *self) {
  return new QMultiHash<QString, QQmlSA::Method>::const_iterator(
      self->constEnd());
}

//  QQmlSA::Method::Methods QQmlSA::MethodsPrivate::createMethods(const
//      QMultiHash<QString, QQmlJSMetaMethod> &a0)
extern "C" Q_DECL_EXPORT
QQmlSA::Method::Methods *ritual_ZN6QQmlSA14MethodsPrivate13createMethodsERK10QMultiHashI7QString16QQmlJSMetaMethodE(
    const QMultiHash<QString, QQmlJSMetaMethod> *a0) {
  return new QQmlSA::Method::Methods(
      QQmlSA::MethodsPrivate::createMethods(
          *a0));
}

//  a QMultiHash<QString, QQmlSA::Method>::const_iterator a ritual of
//      QQmlSA::MethodsPrivate gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlSA_MethodsPrivate__QMultiHash_QString_QQmlSA_Method_const_iterator(
    QMultiHash<QString, QQmlSA::Method>::const_iterator *self) {
  delete self;
}
