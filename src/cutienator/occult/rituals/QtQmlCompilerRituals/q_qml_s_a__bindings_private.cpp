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
#include <utility>
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
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only WITH Qt-GPL-exception-1.0
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from ../qtdeclarative/src/qmlcompiler/qqmlsa.cpp, line 313, as _ZN6QQmlSA14BindingPrivate13createBindingERK25QQmlJSMetaPropertyBinding
namespace QQmlSA {
using namespace Qt::StringLiterals;
inline QQmlSA::Binding BindingPrivate::createBinding(const QQmlJSMetaPropertyBinding &binding)
{
    QQmlSA::Binding saBinding;
    saBinding.d_func()->m_binding = binding;
    return saBinding;
}
}  // namespace QQmlSA

//  from ../qtdeclarative/src/qmlcompiler/qqmlsa.cpp, line 174, as _ZN6QQmlSA15BindingsPrivateC1EPNS_7Binding8BindingsE
namespace QQmlSA {
using namespace Qt::StringLiterals;
inline BindingsPrivate::BindingsPrivate(QQmlSA::Binding::Bindings *iface) : q_ptr{ iface } { }
}  // namespace QQmlSA

//  from ../qtdeclarative/src/qmlcompiler/qqmlsa.cpp, line 189, as _ZN6QQmlSA15BindingsPrivateC1EPNS_7Binding8BindingsERKS0_
namespace QQmlSA {
using namespace Qt::StringLiterals;
inline BindingsPrivate::BindingsPrivate(QQmlSA::Binding::Bindings *iface, const BindingsPrivate &other)
    : m_bindings{ other.m_bindings.begin(), other.m_bindings.end() }, q_ptr{ iface }
{
}
}  // namespace QQmlSA

//  from ../qtdeclarative/src/qmlcompiler/qqmlsa.cpp, line 194, as _ZN6QQmlSA15BindingsPrivateC1EPNS_7Binding8BindingsEOS0_
namespace QQmlSA {
using namespace Qt::StringLiterals;
inline BindingsPrivate::BindingsPrivate(QQmlSA::Binding::Bindings *iface, BindingsPrivate &&other)
    : m_bindings{ std::move(other.m_bindings) }, q_ptr{ iface }
{
}
}  // namespace QQmlSA

//  from ../qtdeclarative/src/qmlcompiler/qqmlsa.cpp, line 213, as _ZNK6QQmlSA15BindingsPrivate10constBeginEv
namespace QQmlSA {
using namespace Qt::StringLiterals;
inline QMultiHash<QString, Binding>::const_iterator BindingsPrivate::constBegin() const
{
    return m_bindings.constBegin();
}
}  // namespace QQmlSA

//  from ../qtdeclarative/src/qmlcompiler/qqmlsa.cpp, line 232, as _ZNK6QQmlSA15BindingsPrivate8constEndEv
namespace QQmlSA {
using namespace Qt::StringLiterals;
inline QMultiHash<QString, Binding>::const_iterator BindingsPrivate::constEnd() const
{
    return m_bindings.constEnd();
}
}  // namespace QQmlSA

//  from ../qtdeclarative/src/qmlcompiler/qqmlsa.cpp, line 1150, as _ZN6QQmlSA15BindingsPrivate14createBindingsERK10QMultiHashI7QString25QQmlJSMetaPropertyBindingE
namespace QQmlSA {
using namespace Qt::StringLiterals;
inline QQmlSA::Binding::Bindings
BindingsPrivate::createBindings(const QMultiHash<QString, QQmlJSMetaPropertyBinding> &hash)
{
    QMultiHash<QString, QQmlSA::Binding> saBindings;
    for (const auto &[key, value] : hash.asKeyValueRange()) {
        saBindings.insert(key, BindingPrivate::createBinding(value));
    }

    QQmlSA::Binding::Bindings bindings;
    bindings.d_func()->m_bindings = std::move(saBindings);
    return bindings;
}
}  // namespace QQmlSA

//  from ../qtdeclarative/src/qmlcompiler/qqmlsa.cpp, line 1163, as _ZN6QQmlSA15BindingsPrivate14createBindingsESt4pairIN10QMultiHashI7QString25QQmlJSMetaPropertyBindingE14const_iteratorES6_E
namespace QQmlSA {
using namespace Qt::StringLiterals;
inline QQmlSA::Binding::Bindings BindingsPrivate::createBindings(
        std::pair<QMultiHash<QString, QQmlJSMetaPropertyBinding>::const_iterator,
              QMultiHash<QString, QQmlJSMetaPropertyBinding>::const_iterator> iterators)
{
    QMultiHash<QString, QQmlSA::Binding> saBindings;
    for (auto it = iterators.first; it != iterators.second; ++it) {
        saBindings.insert(it.key(), BindingPrivate::createBinding(it.value()));
    }

    QQmlSA::Binding::Bindings bindings;
    bindings.d_func()->m_bindings = std::move(saBindings);
    return bindings;
}
}  // namespace QQmlSA
//  -----------------------------------------------------------------------

//  QQmlSA::Binding::Bindings *QQmlSA::BindingsPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQmlSA::Binding::Bindings *ritual_ZN6QQmlSA15BindingsPrivate6q_funcEv(
    QQmlSA::BindingsPrivate *self) {
  return self->q_func();
}

//  const QQmlSA::Binding::Bindings *QQmlSA::BindingsPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQmlSA::Binding::Bindings *ritual_ZNK6QQmlSA15BindingsPrivate6q_funcEv(
    const QQmlSA::BindingsPrivate *self) {
  return self->q_func();
}

//  QQmlSA::BindingsPrivate::BindingsPrivate(QQmlSA::Binding::Bindings *a0)
extern "C" Q_DECL_EXPORT
QQmlSA::BindingsPrivate *ritual_ZN6QQmlSA15BindingsPrivateC1EPNS_7Binding8BindingsE(
    QQmlSA::Binding::Bindings *a0) {
  return new QQmlSA::BindingsPrivate(a0);
}

//  QQmlSA::BindingsPrivate::BindingsPrivate(QQmlSA::Binding::Bindings *a0,
//      const BindingsPrivate &a1)
extern "C" Q_DECL_EXPORT
QQmlSA::BindingsPrivate *ritual_ZN6QQmlSA15BindingsPrivateC1EPNS_7Binding8BindingsERKS0_(
    QQmlSA::Binding::Bindings *a0,
    const QQmlSA::BindingsPrivate *a1) {
  return new QQmlSA::BindingsPrivate(a0, *a1);
}

//  QQmlSA::BindingsPrivate::BindingsPrivate(QQmlSA::Binding::Bindings *a0,
//      BindingsPrivate &&a1)
extern "C" Q_DECL_EXPORT
QQmlSA::BindingsPrivate *ritual_ZN6QQmlSA15BindingsPrivateC1EPNS_7Binding8BindingsEOS0_(
    QQmlSA::Binding::Bindings *a0,
    QQmlSA::BindingsPrivate *a1) {
  return new QQmlSA::BindingsPrivate(a0, std::move(*a1));
}

//  QQmlSA::BindingsPrivate::~BindingsPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlSA15BindingsPrivateD1Ev(QQmlSA::BindingsPrivate *self) {
  delete self;
}

//  QMultiHash<QString, Binding>::const_iterator
//      QQmlSA::BindingsPrivate::constBegin() const
extern "C" Q_DECL_EXPORT
QMultiHash<QString, QQmlSA::Binding>::const_iterator *ritual_ZNK6QQmlSA15BindingsPrivate10constBeginEv(
    const QQmlSA::BindingsPrivate *self) {
  return new QMultiHash<QString, QQmlSA::Binding>::const_iterator(
      self->constBegin());
}

//  QMultiHash<QString, Binding>::const_iterator
//      QQmlSA::BindingsPrivate::constEnd() const
extern "C" Q_DECL_EXPORT
QMultiHash<QString, QQmlSA::Binding>::const_iterator *ritual_ZNK6QQmlSA15BindingsPrivate8constEndEv(
    const QQmlSA::BindingsPrivate *self) {
  return new QMultiHash<QString, QQmlSA::Binding>::const_iterator(
      self->constEnd());
}

//  QQmlSA::Binding::Bindings QQmlSA::BindingsPrivate::createBindings(const
//      QMultiHash<QString, QQmlJSMetaPropertyBinding> &a0)
extern "C" Q_DECL_EXPORT
QQmlSA::Binding::Bindings *ritual_ZN6QQmlSA15BindingsPrivate14createBindingsERK10QMultiHashI7QString25QQmlJSMetaPropertyBindingE(
    const QMultiHash<QString, QQmlJSMetaPropertyBinding> *a0) {
  return new QQmlSA::Binding::Bindings(
      QQmlSA::BindingsPrivate::createBindings(
          *a0));
}

//  QQmlSA::Binding::Bindings
//      QQmlSA::BindingsPrivate::createBindings(std::pair<QMultiHash<QString,
//      QQmlJSMetaPropertyBinding>::const_iterator, QMultiHash<QString,
//      QQmlJSMetaPropertyBinding>::const_iterator> a0)
extern "C" Q_DECL_EXPORT
QQmlSA::Binding::Bindings *ritual_ZN6QQmlSA15BindingsPrivate14createBindingsESt4pairIN10QMultiHashI7QString25QQmlJSMetaPropertyBindingE14const_iteratorES6_E(
    const std::pair<QMultiHash<QString, QQmlJSMetaPropertyBinding>::const_iterator, QMultiHash<QString, QQmlJSMetaPropertyBinding>::const_iterator> *a0) {
  return new QQmlSA::Binding::Bindings(
      QQmlSA::BindingsPrivate::createBindings(
          *a0));
}

//  a QMultiHash<QString, QQmlSA::Binding>::const_iterator a ritual of
//      QQmlSA::BindingsPrivate gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlSA_BindingsPrivate__QMultiHash_QString_QQmlSA_Binding_const_iterator(
    QMultiHash<QString, QQmlSA::Binding>::const_iterator *self) {
  delete self;
}
