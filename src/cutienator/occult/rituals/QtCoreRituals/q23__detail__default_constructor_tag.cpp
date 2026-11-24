//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qexpected_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qexpected_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  q23::detail::default_constructor_tag::default_constructor_tag()
extern "C" Q_DECL_EXPORT
q23::detail::default_constructor_tag *ritual_ZN3q236detail23default_constructor_tagC1Ev() {
  return new q23::detail::default_constructor_tag();
}

//  q23::detail::default_constructor_tag::~default_constructor_tag()
extern "C" Q_DECL_EXPORT
void ritual_ZN3q236detail23default_constructor_tagD1Ev(
    q23::detail::default_constructor_tag *self) {
  delete self;
}
