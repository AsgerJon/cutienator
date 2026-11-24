//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4internalclass_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4internalclass_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  bool QV4::InternalClassTransition::operator==(const
//      InternalClassTransition &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV423InternalClassTransitioneqERKS0_(
    const QV4::InternalClassTransition *self,
    const QV4::InternalClassTransition *other) {
  return self->operator==(*other);
}

//  bool QV4::InternalClassTransition::operator<(const
//      InternalClassTransition &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV423InternalClassTransitionltERKS0_(
    const QV4::InternalClassTransition *self,
    const QV4::InternalClassTransition *other) {
  return self->operator<(*other);
}

//  QV4::InternalClassTransition::~InternalClassTransition()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV423InternalClassTransitionD1Ev(
    QV4::InternalClassTransition *self) {
  delete self;
}
