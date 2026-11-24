//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qpainter_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qpainter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QPainterPrivate::QPaintEngineDestructor::operator()(QPaintEngine
//      *pe) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK15QPainterPrivate22QPaintEngineDestructorclEP12QPaintEngine(
    const QPainterPrivate::QPaintEngineDestructor *self,
    QPaintEngine *pe) {
  self->operator()(pe);
}

//  QPainterPrivate::QPaintEngineDestructor::~QPaintEngineDestructor()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPainterPrivate22QPaintEngineDestructorD1Ev(
    QPainterPrivate::QPaintEngineDestructor *self) {
  delete self;
}
