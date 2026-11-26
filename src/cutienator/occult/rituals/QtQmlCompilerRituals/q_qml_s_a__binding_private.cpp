//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmlsa_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlCompiler/QtQmlCompiler>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmlsa_p.h>
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsmetatypes_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/qqmlsa.h>
#include <QtCore/qstring.h>
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

//  from ../qtdeclarative/src/qmlcompiler/qqmlsa.cpp, line 249, as _ZN6QQmlSA14BindingPrivateC1EPNS_7BindingE
namespace QQmlSA {
using namespace Qt::StringLiterals;
inline BindingPrivate::BindingPrivate(Binding *iface) : q_ptr{ iface } { }
}  // namespace QQmlSA

//  from ../qtdeclarative/src/qmlcompiler/qqmlsa.cpp, line 307, as _ZN6QQmlSA14BindingPrivateC1EPNS_7BindingERKS0_
namespace QQmlSA {
using namespace Qt::StringLiterals;
inline BindingPrivate::BindingPrivate(Binding *iface, const BindingPrivate &other)
    : m_binding{ other.m_binding }, m_bindingScope{ other.m_bindingScope }, q_ptr{ iface },
      m_isAttached{ other.m_isAttached }
{
}
}  // namespace QQmlSA

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
//  -----------------------------------------------------------------------

//  Binding *QQmlSA::BindingPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQmlSA::Binding *ritual_ZN6QQmlSA14BindingPrivate6q_funcEv(
    QQmlSA::BindingPrivate *self) {
  return self->q_func();
}

//  const Binding *QQmlSA::BindingPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQmlSA::Binding *ritual_ZNK6QQmlSA14BindingPrivate6q_funcEv(
    const QQmlSA::BindingPrivate *self) {
  return self->q_func();
}

//  QQmlSA::BindingPrivate::BindingPrivate(Binding *a0)
extern "C" Q_DECL_EXPORT
QQmlSA::BindingPrivate *ritual_ZN6QQmlSA14BindingPrivateC1EPNS_7BindingE(
    QQmlSA::Binding *a0) {
  return new QQmlSA::BindingPrivate(a0);
}

//  QQmlSA::BindingPrivate::BindingPrivate(Binding *a0, const BindingPrivate
//      &a1)
extern "C" Q_DECL_EXPORT
QQmlSA::BindingPrivate *ritual_ZN6QQmlSA14BindingPrivateC1EPNS_7BindingERKS0_(
    QQmlSA::Binding *a0,
    const QQmlSA::BindingPrivate *a1) {
  return new QQmlSA::BindingPrivate(a0, *a1);
}

//  BindingPrivate *QQmlSA::BindingPrivate::get(Binding *binding)
extern "C" Q_DECL_EXPORT
QQmlSA::BindingPrivate *ritual_ZN6QQmlSA14BindingPrivate3getEPNS_7BindingE(
    QQmlSA::Binding *binding) {
  return QQmlSA::BindingPrivate::get(binding);
}

//  const BindingPrivate *QQmlSA::BindingPrivate::get(const Binding *binding)
extern "C" Q_DECL_EXPORT
const QQmlSA::BindingPrivate *ritual_ZN6QQmlSA14BindingPrivate3getEPKNS_7BindingE(
    const QQmlSA::Binding *binding) {
  return QQmlSA::BindingPrivate::get(binding);
}

//  QQmlSA::Binding QQmlSA::BindingPrivate::createBinding(const
//      QQmlJSMetaPropertyBinding &a0)
extern "C" Q_DECL_EXPORT
QQmlSA::Binding *ritual_ZN6QQmlSA14BindingPrivate13createBindingERK25QQmlJSMetaPropertyBinding(
    const QQmlJSMetaPropertyBinding *a0) {
  return new QQmlSA::Binding(QQmlSA::BindingPrivate::createBinding(*a0));
}

//  void QQmlSA::BindingPrivate::setPropertyName(QString name)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlSA14BindingPrivate15setPropertyNameE7QString(
    QQmlSA::BindingPrivate *self,
    const QString *name) {
  self->setPropertyName(*name);
}

//  Element QQmlSA::BindingPrivate::bindingScope() const
extern "C" Q_DECL_EXPORT
QQmlSA::Element *ritual_ZNK6QQmlSA14BindingPrivate12bindingScopeEv(
    const QQmlSA::BindingPrivate *self) {
  return new QQmlSA::Element(self->bindingScope());
}

//  void QQmlSA::BindingPrivate::setBindingScope(Element bindingScope)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlSA14BindingPrivate15setBindingScopeENS_7ElementE(
    QQmlSA::BindingPrivate *self,
    const QQmlSA::Element *bindingScope) {
  self->setBindingScope(*bindingScope);
}

//  bool QQmlSA::BindingPrivate::isAttached() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QQmlSA14BindingPrivate10isAttachedEv(
    const QQmlSA::BindingPrivate *self) {
  return self->isAttached();
}

//  void QQmlSA::BindingPrivate::setIsAttached(bool isAttached)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlSA14BindingPrivate13setIsAttachedEb(
    QQmlSA::BindingPrivate *self,
    bool isAttached) {
  self->setIsAttached(isAttached);
}

//  QQmlSA::BindingPrivate::~BindingPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlSA14BindingPrivateD1Ev(QQmlSA::BindingPrivate *self) {
  delete self;
}
