//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/qqmlsa.h, Qt 6.12.0. Changes made here are lost.
#include <QtQmlCompiler/qqmlsa.h>

//  PropertyPrivate *QQmlSA::Property::d_func()
extern "C" Q_DECL_EXPORT
QQmlSA::PropertyPrivate *ritual_ZN6QQmlSA8Property6d_funcEv(
    QQmlSA::Property *self) {
  return self->d_func();
}

//  const PropertyPrivate *QQmlSA::Property::d_func() const
extern "C" Q_DECL_EXPORT
const QQmlSA::PropertyPrivate *ritual_ZNK6QQmlSA8Property6d_funcEv(
    const QQmlSA::Property *self) {
  return self->d_func();
}

//  bool operator==(const Property &lhs, const Property &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlSAeqERKNS_8PropertyES2_(
    const QQmlSA::Property *lhs,
    const QQmlSA::Property *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const Property &lhs, const Property &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlSAneERKNS_8PropertyES2_(
    const QQmlSA::Property *lhs,
    const QQmlSA::Property *rhs) {
  return operator!=(*lhs, *rhs);
}
