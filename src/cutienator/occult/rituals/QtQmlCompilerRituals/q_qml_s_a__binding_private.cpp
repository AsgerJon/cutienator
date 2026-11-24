//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmlsa_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlCompiler/QtQmlCompiler>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmlsa_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQmlCompiler/qqmlsa.h>

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
