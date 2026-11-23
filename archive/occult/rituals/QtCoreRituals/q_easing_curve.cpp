//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qeasingcurve.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qeasingcurve.h>
#include <QtCore/qpoint.h>
#include <QtCore/qdebug.h>
#include <QtCore/qlist.h>

//  QEasingCurve::QEasingCurve(Type type)
extern "C" Q_DECL_EXPORT
QEasingCurve *ritual_ZN12QEasingCurveC1ENS_4TypeE(QEasingCurve::Type type) {
  return new QEasingCurve(type);
}

//  QEasingCurve::QEasingCurve(const QEasingCurve &other)
extern "C" Q_DECL_EXPORT
QEasingCurve *ritual_ZN12QEasingCurveC1ERKS_(const QEasingCurve *other) {
  return new QEasingCurve(*other);
}

//  QEasingCurve::~QEasingCurve()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QEasingCurveD1Ev(QEasingCurve *self) {
  delete self;
}

//  qreal QEasingCurve::amplitude() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK12QEasingCurve9amplitudeEv(const QEasingCurve *self) {
  return self->amplitude();
}

//  void QEasingCurve::setAmplitude(qreal amplitude)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QEasingCurve12setAmplitudeEd(
    QEasingCurve *self,
    qreal amplitude) {
  self->setAmplitude(amplitude);
}

//  qreal QEasingCurve::period() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK12QEasingCurve6periodEv(const QEasingCurve *self) {
  return self->period();
}

//  void QEasingCurve::setPeriod(qreal period)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QEasingCurve9setPeriodEd(QEasingCurve *self, qreal period) {
  self->setPeriod(period);
}

//  qreal QEasingCurve::overshoot() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK12QEasingCurve9overshootEv(const QEasingCurve *self) {
  return self->overshoot();
}

//  void QEasingCurve::setOvershoot(qreal overshoot)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QEasingCurve12setOvershootEd(
    QEasingCurve *self,
    qreal overshoot) {
  self->setOvershoot(overshoot);
}

//  void QEasingCurve::addCubicBezierSegment(const QPointF &c1, const QPointF
//      &c2, const QPointF &endPoint)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QEasingCurve21addCubicBezierSegmentERK7QPointFS2_S2_(
    QEasingCurve *self,
    const QPointF *c1,
    const QPointF *c2,
    const QPointF *endPoint) {
  self->addCubicBezierSegment(*c1, *c2, *endPoint);
}

//  void QEasingCurve::addTCBSegment(const QPointF &nextPoint, qreal t, qreal
//      c, qreal b)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QEasingCurve13addTCBSegmentERK7QPointFddd(
    QEasingCurve *self,
    const QPointF *nextPoint,
    qreal t,
    qreal c,
    qreal b) {
  self->addTCBSegment(*nextPoint, t, c, b);
}

//  QList<QPointF> QEasingCurve::toCubicSpline() const
extern "C" Q_DECL_EXPORT
QList<QPointF> *ritual_ZNK12QEasingCurve13toCubicSplineEv(
    const QEasingCurve *self) {
  return new QList<QPointF>(self->toCubicSpline());
}

//  Type QEasingCurve::type() const
extern "C" Q_DECL_EXPORT
QEasingCurve::Type ritual_ZNK12QEasingCurve4typeEv(
    const QEasingCurve *self) {
  return self->type();
}

//  void QEasingCurve::setType(Type type)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QEasingCurve7setTypeENS_4TypeE(
    QEasingCurve *self,
    QEasingCurve::Type type) {
  self->setType(type);
}

//  qreal QEasingCurve::valueForProgress(qreal progress) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK12QEasingCurve16valueForProgressEd(
    const QEasingCurve *self,
    qreal progress) {
  return self->valueForProgress(progress);
}

//  QEasingCurve QEasingCurve::fromCubicBezier(QPointF c1, QPointF c2)
extern "C" Q_DECL_EXPORT
QEasingCurve *ritual_ZN12QEasingCurve15fromCubicBezierE7QPointFS0_(
    const QPointF *c1,
    const QPointF *c2) {
  return new QEasingCurve(QEasingCurve::fromCubicBezier(*c1, *c2));
}

//  QDebug operator<<(QDebug debug, const QEasingCurve &item)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRK12QEasingCurve(
    const QDebug *debug,
    const QEasingCurve *item) {
  return new QDebug(operator<<(*debug, *item));
}

//  bool operator==(const QEasingCurve &lhs, const QEasingCurve &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK12QEasingCurveS1_(
    const QEasingCurve *lhs,
    const QEasingCurve *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QEasingCurve &lhs, const QEasingCurve &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK12QEasingCurveS1_(
    const QEasingCurve *lhs,
    const QEasingCurve *rhs) {
  return operator!=(*lhs, *rhs);
}
