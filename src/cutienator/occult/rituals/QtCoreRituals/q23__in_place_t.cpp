//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qexpected_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qexpected_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  q23::in_place_t::in_place_t()
extern "C" Q_DECL_EXPORT
q23::in_place_t *ritual_ZN3q2310in_place_tC1Ev() {
  return new q23::in_place_t();
}

//  q23::in_place_t::~in_place_t()
extern "C" Q_DECL_EXPORT
void ritual_ZN3q2310in_place_tD1Ev(q23::in_place_t *self) {
  delete self;
}
