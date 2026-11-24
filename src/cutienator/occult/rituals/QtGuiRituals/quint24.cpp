//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qdrawhelper_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qdrawhelper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  quint24::quint24()
extern "C" Q_DECL_EXPORT
quint24 *ritual_ZN7quint24C1Ev() {
  return new quint24();
}

//  quint24::quint24(uint value)
extern "C" Q_DECL_EXPORT
quint24 *ritual_ZN7quint24C1Ej(uint value) {
  return new quint24(value);
}

//  uint quint24::operator unsigned int() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK7quint24cvjEv(const quint24 *self) {
  return self->operator uint();
}

//  quint24::~quint24()
extern "C" Q_DECL_EXPORT
void ritual_ZN7quint24D1Ev(quint24 *self) {
  delete self;
}
