//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qstroker_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if (!(defined QFIXED_IS_26_6)) && (!(defined QFIXED_IS_32_32)) && (!(defined QFIXED_IS_16_16))
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qstroker_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  bool qfixed2d::isFinite()
extern "C" Q_DECL_EXPORT
bool ritual_ZN8qfixed2d8isFiniteEv(qfixed2d *self) {
  return self->isFinite();
}

//  bool qfixed2d::operator==(const qfixed2d &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8qfixed2deqERKS_(
    const qfixed2d *self,
    const qfixed2d *other) {
  return self->operator==(*other);
}

//  qfixed2d::~qfixed2d()
extern "C" Q_DECL_EXPORT
void ritual_ZN8qfixed2dD1Ev(qfixed2d *self) {
  delete self;
}

#endif  // (!(defined QFIXED_IS_26_6)) && (!(defined QFIXED_IS_32_32)) && (!(defined QFIXED_IS_16_16))
