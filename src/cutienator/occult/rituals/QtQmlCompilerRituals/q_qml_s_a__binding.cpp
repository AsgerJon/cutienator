//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/qqmlsa.h, Qt 6.12.0. Changes made here are lost.
#include <QtQmlCompiler/qqmlsa.h>

//  BindingPrivate *QQmlSA::Binding::d_func()
extern "C" Q_DECL_EXPORT
QQmlSA::BindingPrivate *ritual_ZN6QQmlSA7Binding6d_funcEv(
    QQmlSA::Binding *self) {
  return self->d_func();
}

//  const BindingPrivate *QQmlSA::Binding::d_func() const
extern "C" Q_DECL_EXPORT
const QQmlSA::BindingPrivate *ritual_ZNK6QQmlSA7Binding6d_funcEv(
    const QQmlSA::Binding *self) {
  return self->d_func();
}

//  bool operator==(const Binding &lhs, const Binding &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlSAeqERKNS_7BindingES2_(
    const QQmlSA::Binding *lhs,
    const QQmlSA::Binding *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const Binding &lhs, const Binding &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlSAneERKNS_7BindingES2_(
    const QQmlSA::Binding *lhs,
    const QQmlSA::Binding *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool QQmlSA::Binding::isLiteralBinding(BindingType a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlSA7Binding16isLiteralBindingENS_11BindingTypeE(
    QQmlSA::BindingType a0) {
  return QQmlSA::Binding::isLiteralBinding(a0);
}
