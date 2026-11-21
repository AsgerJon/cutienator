//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgraphicseffect.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qgraphicseffect.h>
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtGui/qcolor.h>

//  const QMetaObject *QGraphicsDropShadowEffect::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK25QGraphicsDropShadowEffect10metaObjectEv(
    const QGraphicsDropShadowEffect *self) {
  return self->metaObject();
}

//  QString QGraphicsDropShadowEffect::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN25QGraphicsDropShadowEffect2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGraphicsDropShadowEffect::tr(s, c, n));
}

//  QGraphicsDropShadowEffect::QGraphicsDropShadowEffect(QObject *parent)
extern "C" Q_DECL_EXPORT
QGraphicsDropShadowEffect *ritual_ZN25QGraphicsDropShadowEffectC1EP7QObject(
    QObject *parent) {
  return new QGraphicsDropShadowEffect(parent);
}

//  QGraphicsDropShadowEffect::~QGraphicsDropShadowEffect()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QGraphicsDropShadowEffectD1Ev(
    QGraphicsDropShadowEffect *self) {
  delete self;
}

//  QRectF QGraphicsDropShadowEffect::boundingRectFor(const QRectF &rect)
//      const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK25QGraphicsDropShadowEffect15boundingRectForERK6QRectF(
    const QGraphicsDropShadowEffect *self,
    const QRectF *rect) {
  return new QRectF(self->boundingRectFor(*rect));
}

//  QPointF QGraphicsDropShadowEffect::offset() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK25QGraphicsDropShadowEffect6offsetEv(
    const QGraphicsDropShadowEffect *self) {
  return new QPointF(self->offset());
}

//  qreal QGraphicsDropShadowEffect::xOffset() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK25QGraphicsDropShadowEffect7xOffsetEv(
    const QGraphicsDropShadowEffect *self) {
  return self->xOffset();
}

//  qreal QGraphicsDropShadowEffect::yOffset() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK25QGraphicsDropShadowEffect7yOffsetEv(
    const QGraphicsDropShadowEffect *self) {
  return self->yOffset();
}

//  qreal QGraphicsDropShadowEffect::blurRadius() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK25QGraphicsDropShadowEffect10blurRadiusEv(
    const QGraphicsDropShadowEffect *self) {
  return self->blurRadius();
}

//  QColor QGraphicsDropShadowEffect::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK25QGraphicsDropShadowEffect5colorEv(
    const QGraphicsDropShadowEffect *self) {
  return new QColor(self->color());
}

//  void QGraphicsDropShadowEffect::setOffset(const QPointF &ofs)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QGraphicsDropShadowEffect9setOffsetERK7QPointF(
    QGraphicsDropShadowEffect *self,
    const QPointF *ofs) {
  self->setOffset(*ofs);
}

//  void QGraphicsDropShadowEffect::setOffset(qreal dx, qreal dy)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QGraphicsDropShadowEffect9setOffsetEdd(
    QGraphicsDropShadowEffect *self,
    qreal dx,
    qreal dy) {
  self->setOffset(dx, dy);
}

//  void QGraphicsDropShadowEffect::setOffset(qreal d)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QGraphicsDropShadowEffect9setOffsetEd(
    QGraphicsDropShadowEffect *self,
    qreal d) {
  self->setOffset(d);
}

//  void QGraphicsDropShadowEffect::setXOffset(qreal dx)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QGraphicsDropShadowEffect10setXOffsetEd(
    QGraphicsDropShadowEffect *self,
    qreal dx) {
  self->setXOffset(dx);
}

//  void QGraphicsDropShadowEffect::setYOffset(qreal dy)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QGraphicsDropShadowEffect10setYOffsetEd(
    QGraphicsDropShadowEffect *self,
    qreal dy) {
  self->setYOffset(dy);
}

//  void QGraphicsDropShadowEffect::setBlurRadius(qreal blurRadius)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QGraphicsDropShadowEffect13setBlurRadiusEd(
    QGraphicsDropShadowEffect *self,
    qreal blurRadius) {
  self->setBlurRadius(blurRadius);
}

//  void QGraphicsDropShadowEffect::setColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QGraphicsDropShadowEffect8setColorERK6QColor(
    QGraphicsDropShadowEffect *self,
    const QColor *color) {
  self->setColor(*color);
}
