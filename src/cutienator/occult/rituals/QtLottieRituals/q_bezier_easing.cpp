//  Written by dev_tooling.RitualGenerator from the records of
//  QtLottie/6.12.0/QtLottie/private/qbeziereasing_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtLottie/QtLottie>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLottie/6.12.0/QtLottie/private/qbeziereasing_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qbezier_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QBezierEasing::addCubicBezierSegment(const QPointF &c1, const
//      QPointF &c2, const QPointF &endPoint)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QBezierEasing21addCubicBezierSegmentERK7QPointFS2_S2_(
    QBezierEasing *self,
    const QPointF *c1,
    const QPointF *c2,
    const QPointF *endPoint) {
  self->addCubicBezierSegment(*c1, *c2, *endPoint);
}

//  qreal QBezierEasing::valueForProgress(qreal progress) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QBezierEasing16valueForProgressEd(
    const QBezierEasing *self,
    qreal progress) {
  return self->valueForProgress(progress);
}

//  QBezier QBezierEasing::bezier() const
extern "C" Q_DECL_EXPORT
QBezier *ritual_ZNK13QBezierEasing6bezierEv(const QBezierEasing *self) {
  return new QBezier(self->bezier());
}

//  qreal QBezierEasing::tForX(qreal x) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QBezierEasing5tForXEd(const QBezierEasing *self, qreal x) {
  return self->tForX(x);
}

//  QBezierEasing::~QBezierEasing()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QBezierEasingD1Ev(QBezierEasing *self) {
  delete self;
}
