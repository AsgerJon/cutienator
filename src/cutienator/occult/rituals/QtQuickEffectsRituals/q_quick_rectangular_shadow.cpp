//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickEffects/6.12.0/QtQuickEffects/private/qquickrectangularshadow_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuickEffects/qtquickeffectsexports.h>
#include <QtQuickEffects/6.12.0/QtQuickEffects/private/qtquickeffectsglobal_p.h>
#if QT_CONFIG(quick_shadereffect)
#include <QtQuickEffects/6.12.0/QtQuickEffects/private/qtquickeffectsglobal_p.h>
#include <QtQuickEffects/QtQuickEffects>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickEffects/6.12.0/QtQuickEffects/private/qquickrectangularshadow_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qvectornd.h>
#include <QtGui/qcolor.h>
#include <QtCore/qrect.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>

//  Only a class built on QQuickRectangularShadow may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickRectangularShadow : QQuickRectangularShadow {
  using QQuickRectangularShadow::componentComplete;
  using QQuickRectangularShadow::geometryChange;
  using QQuickRectangularShadow::itemChange;
};

//  const QMetaObject *QQuickRectangularShadow::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QQuickRectangularShadow10metaObjectEv(
    const QQuickRectangularShadow *self) {
  return self->metaObject();
}

//  QString QQuickRectangularShadow::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QQuickRectangularShadow2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickRectangularShadow::tr(s, c, n));
}

//  QQuickRectangularShadow::QQuickRectangularShadow(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickRectangularShadow *ritual_ZN23QQuickRectangularShadowC1EP10QQuickItem(
    QQuickItem *parent) {
  return new QQuickRectangularShadow(parent);
}

//  QVector2D QQuickRectangularShadow::offset() const
extern "C" Q_DECL_EXPORT
QVector2D *ritual_ZNK23QQuickRectangularShadow6offsetEv(
    const QQuickRectangularShadow *self) {
  return new QVector2D(self->offset());
}

//  void QQuickRectangularShadow::setOffset(const QVector2D &offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickRectangularShadow9setOffsetERK9QVector2D(
    QQuickRectangularShadow *self,
    const QVector2D *offset) {
  self->setOffset(*offset);
}

//  QColor QQuickRectangularShadow::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK23QQuickRectangularShadow5colorEv(
    const QQuickRectangularShadow *self) {
  return new QColor(self->color());
}

//  void QQuickRectangularShadow::setColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickRectangularShadow8setColorERK6QColor(
    QQuickRectangularShadow *self,
    const QColor *color) {
  self->setColor(*color);
}

//  qreal QQuickRectangularShadow::blur() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK23QQuickRectangularShadow4blurEv(
    const QQuickRectangularShadow *self) {
  return self->blur();
}

//  void QQuickRectangularShadow::setBlur(qreal blur)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickRectangularShadow7setBlurEd(
    QQuickRectangularShadow *self,
    qreal blur) {
  self->setBlur(blur);
}

//  qreal QQuickRectangularShadow::radius() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK23QQuickRectangularShadow6radiusEv(
    const QQuickRectangularShadow *self) {
  return self->radius();
}

//  void QQuickRectangularShadow::setRadius(qreal radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickRectangularShadow9setRadiusEd(
    QQuickRectangularShadow *self,
    qreal radius) {
  self->setRadius(radius);
}

//  qreal QQuickRectangularShadow::spread() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK23QQuickRectangularShadow6spreadEv(
    const QQuickRectangularShadow *self) {
  return self->spread();
}

//  void QQuickRectangularShadow::setSpread(qreal spread)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickRectangularShadow9setSpreadEd(
    QQuickRectangularShadow *self,
    qreal spread) {
  self->setSpread(spread);
}

//  bool QQuickRectangularShadow::isCached() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuickRectangularShadow8isCachedEv(
    const QQuickRectangularShadow *self) {
  return self->isCached();
}

//  void QQuickRectangularShadow::setCached(bool cached)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickRectangularShadow9setCachedEb(
    QQuickRectangularShadow *self,
    bool cached) {
  self->setCached(cached);
}

//  QQuickItem *QQuickRectangularShadow::material() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK23QQuickRectangularShadow8materialEv(
    const QQuickRectangularShadow *self) {
  return self->material();
}

//  void QQuickRectangularShadow::setMaterial(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickRectangularShadow11setMaterialEP10QQuickItem(
    QQuickRectangularShadow *self,
    QQuickItem *item) {
  self->setMaterial(item);
}

//  qreal QQuickRectangularShadow::topLeftRadius() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK23QQuickRectangularShadow13topLeftRadiusEv(
    const QQuickRectangularShadow *self) {
  return self->topLeftRadius();
}

//  void QQuickRectangularShadow::setTopLeftRadius(qreal radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickRectangularShadow16setTopLeftRadiusEd(
    QQuickRectangularShadow *self,
    qreal radius) {
  self->setTopLeftRadius(radius);
}

//  void QQuickRectangularShadow::resetTopLeftRadius()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickRectangularShadow18resetTopLeftRadiusEv(
    QQuickRectangularShadow *self) {
  self->resetTopLeftRadius();
}

//  qreal QQuickRectangularShadow::topRightRadius() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK23QQuickRectangularShadow14topRightRadiusEv(
    const QQuickRectangularShadow *self) {
  return self->topRightRadius();
}

//  void QQuickRectangularShadow::setTopRightRadius(qreal radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickRectangularShadow17setTopRightRadiusEd(
    QQuickRectangularShadow *self,
    qreal radius) {
  self->setTopRightRadius(radius);
}

//  void QQuickRectangularShadow::resetTopRightRadius()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickRectangularShadow19resetTopRightRadiusEv(
    QQuickRectangularShadow *self) {
  self->resetTopRightRadius();
}

//  qreal QQuickRectangularShadow::bottomLeftRadius() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK23QQuickRectangularShadow16bottomLeftRadiusEv(
    const QQuickRectangularShadow *self) {
  return self->bottomLeftRadius();
}

//  void QQuickRectangularShadow::setBottomLeftRadius(qreal radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickRectangularShadow19setBottomLeftRadiusEd(
    QQuickRectangularShadow *self,
    qreal radius) {
  self->setBottomLeftRadius(radius);
}

//  void QQuickRectangularShadow::resetBottomLeftRadius()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickRectangularShadow21resetBottomLeftRadiusEv(
    QQuickRectangularShadow *self) {
  self->resetBottomLeftRadius();
}

//  qreal QQuickRectangularShadow::bottomRightRadius() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK23QQuickRectangularShadow17bottomRightRadiusEv(
    const QQuickRectangularShadow *self) {
  return self->bottomRightRadius();
}

//  void QQuickRectangularShadow::setBottomRightRadius(qreal radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickRectangularShadow20setBottomRightRadiusEd(
    QQuickRectangularShadow *self,
    qreal radius) {
  self->setBottomRightRadius(radius);
}

//  void QQuickRectangularShadow::resetBottomRightRadius()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickRectangularShadow22resetBottomRightRadiusEv(
    QQuickRectangularShadow *self) {
  self->resetBottomRightRadius();
}

//  void QQuickRectangularShadow::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickRectangularShadow17componentCompleteEv(
    QQuickRectangularShadow *self) {
  self->componentComplete();
}

//  void QQuickRectangularShadow::geometryChange(const QRectF &newGeometry,
//      const QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickRectangularShadow14geometryChangeERK6QRectFS2_(
    QQuickRectangularShadow *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  self->geometryChange(*newGeometry, *oldGeometry);
}

//  void QQuickRectangularShadow::itemChange(ItemChange change, const
//      ItemChangeData &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickRectangularShadow10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickRectangularShadow *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *value) {
  self->itemChange(change, *value);
}

//  QQuickRectangularShadowPrivate *QQuickRectangularShadow::d_func()
extern "C" Q_DECL_EXPORT
QQuickRectangularShadowPrivate *ritual_ZN23QQuickRectangularShadow6d_funcEv(
    QQuickRectangularShadow *self) {
  return self->d_func();
}

//  const QQuickRectangularShadowPrivate *QQuickRectangularShadow::d_func()
//      const
extern "C" Q_DECL_EXPORT
const QQuickRectangularShadowPrivate *ritual_ZNK23QQuickRectangularShadow6d_funcEv(
    const QQuickRectangularShadow *self) {
  return self->d_func();
}

//  void QQuickRectangularShadow::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QQuickRectangularShadow17componentCompleteEv(
    QQuickRectangularShadow *self) {
  static_cast<OwnQQuickRectangularShadow *>(self)->OwnQQuickRectangularShadow::componentComplete();
}

//  void QQuickRectangularShadow::geometryChange(const QRectF &newGeometry,
//      const QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QQuickRectangularShadow14geometryChangeERK6QRectFS2_(
    QQuickRectangularShadow *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  static_cast<OwnQQuickRectangularShadow *>(self)->OwnQQuickRectangularShadow::geometryChange(
      *newGeometry,
      *oldGeometry);
}

//  void QQuickRectangularShadow::itemChange(ItemChange change, const
//      ItemChangeData &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QQuickRectangularShadow10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickRectangularShadow *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *value) {
  static_cast<OwnQQuickRectangularShadow *>(self)->OwnQQuickRectangularShadow::itemChange(
      change,
      *value);
}

#endif  // QT_CONFIG(quick_shadereffect)
