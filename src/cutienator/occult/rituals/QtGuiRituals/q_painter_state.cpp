//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qpainter_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qpainter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QPainterState::QPainterState()
extern "C" Q_DECL_EXPORT
QPainterState *ritual_ZN13QPainterStateC1Ev() {
  return new QPainterState();
}

//  QPainterState::QPainterState(const QPainterState *s)
extern "C" Q_DECL_EXPORT
QPainterState *ritual_ZN13QPainterStateC1EPKS_(const QPainterState *s) {
  return new QPainterState(s);
}

//  QPainterState::~QPainterState()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPainterStateD1Ev(QPainterState *self) {
  delete self;
}

//  void QPainterState::init(QPainter *p)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPainterState4initEP8QPainter(
    QPainterState *self,
    QPainter *p) {
  self->init(p);
}
