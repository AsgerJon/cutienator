//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qexpected_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qexpected_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  q23::unexpect_t::unexpect_t()
extern "C" Q_DECL_EXPORT
q23::unexpect_t *ritual_ZN3q2310unexpect_tC1Ev() {
  return new q23::unexpect_t();
}

//  q23::unexpect_t::~unexpect_t()
extern "C" Q_DECL_EXPORT
void ritual_ZN3q2310unexpect_tD1Ev(q23::unexpect_t *self) {
  delete self;
}
