//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/qqmlsa.h, Qt 6.12.0. Changes made here are lost.
#include <QtQmlCompiler/qqmlsa.h>

//  MethodPrivate *QQmlSA::Method::d_func()
extern "C" Q_DECL_EXPORT
QQmlSA::MethodPrivate *ritual_ZN6QQmlSA6Method6d_funcEv(
    QQmlSA::Method *self) {
  return self->d_func();
}

//  const MethodPrivate *QQmlSA::Method::d_func() const
extern "C" Q_DECL_EXPORT
const QQmlSA::MethodPrivate *ritual_ZNK6QQmlSA6Method6d_funcEv(
    const QQmlSA::Method *self) {
  return self->d_func();
}

//  bool operator==(const Method &lhs, const Method &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlSAeqERKNS_6MethodES2_(
    const QQmlSA::Method *lhs,
    const QQmlSA::Method *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const Method &lhs, const Method &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlSAneERKNS_6MethodES2_(
    const QQmlSA::Method *lhs,
    const QQmlSA::Method *rhs) {
  return operator!=(*lhs, *rhs);
}
