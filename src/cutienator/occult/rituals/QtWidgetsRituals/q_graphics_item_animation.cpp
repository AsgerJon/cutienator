//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgraphicsitemanimation.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtWidgets/qgraphicsitemanimation.h>
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>
#include <QtGui/qtransform.h>

//  const QMetaObject *QGraphicsItemAnimation::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QGraphicsItemAnimation10metaObjectEv(
    const QGraphicsItemAnimation *self) {
  return self->metaObject();
}

//  QString QGraphicsItemAnimation::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN22QGraphicsItemAnimation2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGraphicsItemAnimation::tr(s, c, n));
}

//  QGraphicsItemAnimation::QGraphicsItemAnimation(QObject *parent)
extern "C" Q_DECL_EXPORT
QGraphicsItemAnimation *ritual_ZN22QGraphicsItemAnimationC1EP7QObject(
    QObject *parent) {
  return new QGraphicsItemAnimation(parent);
}

//  QGraphicsItemAnimation::~QGraphicsItemAnimation()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGraphicsItemAnimationD1Ev(QGraphicsItemAnimation *self) {
  delete self;
}

//  QGraphicsItem *QGraphicsItemAnimation::item() const
extern "C" Q_DECL_EXPORT
QGraphicsItem *ritual_ZNK22QGraphicsItemAnimation4itemEv(
    const QGraphicsItemAnimation *self) {
  return self->item();
}

//  void QGraphicsItemAnimation::setItem(QGraphicsItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGraphicsItemAnimation7setItemEP13QGraphicsItem(
    QGraphicsItemAnimation *self,
    QGraphicsItem *item) {
  self->setItem(item);
}

//  QTimeLine *QGraphicsItemAnimation::timeLine() const
extern "C" Q_DECL_EXPORT
QTimeLine *ritual_ZNK22QGraphicsItemAnimation8timeLineEv(
    const QGraphicsItemAnimation *self) {
  return self->timeLine();
}

//  void QGraphicsItemAnimation::setTimeLine(QTimeLine *timeLine)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGraphicsItemAnimation11setTimeLineEP9QTimeLine(
    QGraphicsItemAnimation *self,
    QTimeLine *timeLine) {
  self->setTimeLine(timeLine);
}

//  QPointF QGraphicsItemAnimation::posAt(qreal step) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK22QGraphicsItemAnimation5posAtEd(
    const QGraphicsItemAnimation *self,
    qreal step) {
  return new QPointF(self->posAt(step));
}

//  void QGraphicsItemAnimation::setPosAt(qreal step, const QPointF &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGraphicsItemAnimation8setPosAtEdRK7QPointF(
    QGraphicsItemAnimation *self,
    qreal step,
    const QPointF *pos) {
  self->setPosAt(step, *pos);
}

//  QTransform QGraphicsItemAnimation::transformAt(qreal step) const
extern "C" Q_DECL_EXPORT
QTransform *ritual_ZNK22QGraphicsItemAnimation11transformAtEd(
    const QGraphicsItemAnimation *self,
    qreal step) {
  return new QTransform(self->transformAt(step));
}

//  qreal QGraphicsItemAnimation::rotationAt(qreal step) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK22QGraphicsItemAnimation10rotationAtEd(
    const QGraphicsItemAnimation *self,
    qreal step) {
  return self->rotationAt(step);
}

//  void QGraphicsItemAnimation::setRotationAt(qreal step, qreal angle)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGraphicsItemAnimation13setRotationAtEdd(
    QGraphicsItemAnimation *self,
    qreal step,
    qreal angle) {
  self->setRotationAt(step, angle);
}

//  qreal QGraphicsItemAnimation::xTranslationAt(qreal step) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK22QGraphicsItemAnimation14xTranslationAtEd(
    const QGraphicsItemAnimation *self,
    qreal step) {
  return self->xTranslationAt(step);
}

//  qreal QGraphicsItemAnimation::yTranslationAt(qreal step) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK22QGraphicsItemAnimation14yTranslationAtEd(
    const QGraphicsItemAnimation *self,
    qreal step) {
  return self->yTranslationAt(step);
}

//  void QGraphicsItemAnimation::setTranslationAt(qreal step, qreal dx, qreal
//      dy)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGraphicsItemAnimation16setTranslationAtEddd(
    QGraphicsItemAnimation *self,
    qreal step,
    qreal dx,
    qreal dy) {
  self->setTranslationAt(step, dx, dy);
}

//  qreal QGraphicsItemAnimation::verticalScaleAt(qreal step) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK22QGraphicsItemAnimation15verticalScaleAtEd(
    const QGraphicsItemAnimation *self,
    qreal step) {
  return self->verticalScaleAt(step);
}

//  qreal QGraphicsItemAnimation::horizontalScaleAt(qreal step) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK22QGraphicsItemAnimation17horizontalScaleAtEd(
    const QGraphicsItemAnimation *self,
    qreal step) {
  return self->horizontalScaleAt(step);
}

//  void QGraphicsItemAnimation::setScaleAt(qreal step, qreal sx, qreal sy)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGraphicsItemAnimation10setScaleAtEddd(
    QGraphicsItemAnimation *self,
    qreal step,
    qreal sx,
    qreal sy) {
  self->setScaleAt(step, sx, sy);
}

//  qreal QGraphicsItemAnimation::verticalShearAt(qreal step) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK22QGraphicsItemAnimation15verticalShearAtEd(
    const QGraphicsItemAnimation *self,
    qreal step) {
  return self->verticalShearAt(step);
}

//  qreal QGraphicsItemAnimation::horizontalShearAt(qreal step) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK22QGraphicsItemAnimation17horizontalShearAtEd(
    const QGraphicsItemAnimation *self,
    qreal step) {
  return self->horizontalShearAt(step);
}

//  void QGraphicsItemAnimation::setShearAt(qreal step, qreal sh, qreal sv)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGraphicsItemAnimation10setShearAtEddd(
    QGraphicsItemAnimation *self,
    qreal step,
    qreal sh,
    qreal sv) {
  self->setShearAt(step, sh, sv);
}

//  void QGraphicsItemAnimation::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGraphicsItemAnimation5clearEv(
    QGraphicsItemAnimation *self) {
  self->clear();
}

//  void QGraphicsItemAnimation::setStep(qreal x)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGraphicsItemAnimation7setStepEd(
    QGraphicsItemAnimation *self,
    qreal x) {
  self->setStep(x);
}
