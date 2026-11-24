//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/qqmlsa.h, Qt 6.12.0. Changes made here are lost.
#include <QtQmlCompiler/qqmlsa.h>

//  bool QQmlSA::Element::isComposite() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QQmlSA7Element11isCompositeEv(const QQmlSA::Element *self) {
  return self->isComposite();
}

//  bool operator==(const QQmlSA::Element &lhs, const QQmlSA::Element &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlSAeqERKNS_7ElementES2_(
    const QQmlSA::Element *lhs,
    const QQmlSA::Element *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const Element &lhs, const Element &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlSAneERKNS_7ElementES2_(
    const QQmlSA::Element *lhs,
    const QQmlSA::Element *rhs) {
  return operator!=(*lhs, *rhs);
}
