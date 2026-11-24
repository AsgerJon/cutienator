//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickrectangle_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickrectangle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qcolor.h>
#include <QtQml/QtQml>
#include <QtQml/qjsvalue.h>

//  Only a class built on QQuickRectangle may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickRectangle : QQuickRectangle {
  using QQuickRectangle::updatePaintNode;
};

//  const QMetaObject *QQuickRectangle::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QQuickRectangle10metaObjectEv(
    const QQuickRectangle *self) {
  return self->metaObject();
}

//  QString QQuickRectangle::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QQuickRectangle2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickRectangle::tr(s, c, n));
}

//  QQuickRectangle::QQuickRectangle(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickRectangle *ritual_ZN15QQuickRectangleC1EP10QQuickItem(
    QQuickItem *parent) {
  return new QQuickRectangle(parent);
}

//  QColor QQuickRectangle::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK15QQuickRectangle5colorEv(const QQuickRectangle *self) {
  return new QColor(self->color());
}

//  void QQuickRectangle::setColor(const QColor &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickRectangle8setColorERK6QColor(
    QQuickRectangle *self,
    const QColor *a0) {
  self->setColor(*a0);
}

//  void QQuickRectangle::resetColor()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickRectangle10resetColorEv(QQuickRectangle *self) {
  self->resetColor();
}

//  QQuickPen *QQuickRectangle::border()
extern "C" Q_DECL_EXPORT
QQuickPen *ritual_ZN15QQuickRectangle6borderEv(QQuickRectangle *self) {
  return self->border();
}

//  QJSValue QQuickRectangle::gradient() const
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZNK15QQuickRectangle8gradientEv(
    const QQuickRectangle *self) {
  return new QJSValue(self->gradient());
}

//  void QQuickRectangle::setGradient(const QJSValue &gradient)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickRectangle11setGradientERK8QJSValue(
    QQuickRectangle *self,
    const QJSValue *gradient) {
  self->setGradient(*gradient);
}

//  void QQuickRectangle::resetGradient()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickRectangle13resetGradientEv(QQuickRectangle *self) {
  self->resetGradient();
}

//  qreal QQuickRectangle::radius() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickRectangle6radiusEv(const QQuickRectangle *self) {
  return self->radius();
}

//  void QQuickRectangle::setRadius(qreal radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickRectangle9setRadiusEd(
    QQuickRectangle *self,
    qreal radius) {
  self->setRadius(radius);
}

//  qreal QQuickRectangle::topLeftRadius() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickRectangle13topLeftRadiusEv(
    const QQuickRectangle *self) {
  return self->topLeftRadius();
}

//  void QQuickRectangle::setTopLeftRadius(qreal radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickRectangle16setTopLeftRadiusEd(
    QQuickRectangle *self,
    qreal radius) {
  self->setTopLeftRadius(radius);
}

//  void QQuickRectangle::resetTopLeftRadius()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickRectangle18resetTopLeftRadiusEv(
    QQuickRectangle *self) {
  self->resetTopLeftRadius();
}

//  qreal QQuickRectangle::topRightRadius() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickRectangle14topRightRadiusEv(
    const QQuickRectangle *self) {
  return self->topRightRadius();
}

//  void QQuickRectangle::setTopRightRadius(qreal radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickRectangle17setTopRightRadiusEd(
    QQuickRectangle *self,
    qreal radius) {
  self->setTopRightRadius(radius);
}

//  void QQuickRectangle::resetTopRightRadius()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickRectangle19resetTopRightRadiusEv(
    QQuickRectangle *self) {
  self->resetTopRightRadius();
}

//  qreal QQuickRectangle::bottomLeftRadius() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickRectangle16bottomLeftRadiusEv(
    const QQuickRectangle *self) {
  return self->bottomLeftRadius();
}

//  void QQuickRectangle::setBottomLeftRadius(qreal radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickRectangle19setBottomLeftRadiusEd(
    QQuickRectangle *self,
    qreal radius) {
  self->setBottomLeftRadius(radius);
}

//  void QQuickRectangle::resetBottomLeftRadius()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickRectangle21resetBottomLeftRadiusEv(
    QQuickRectangle *self) {
  self->resetBottomLeftRadius();
}

//  qreal QQuickRectangle::bottomRightRadius() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickRectangle17bottomRightRadiusEv(
    const QQuickRectangle *self) {
  return self->bottomRightRadius();
}

//  void QQuickRectangle::setBottomRightRadius(qreal radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickRectangle20setBottomRightRadiusEd(
    QQuickRectangle *self,
    qreal radius) {
  self->setBottomRightRadius(radius);
}

//  void QQuickRectangle::resetBottomRightRadius()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickRectangle22resetBottomRightRadiusEv(
    QQuickRectangle *self) {
  self->resetBottomRightRadius();
}

//  QSGNode *QQuickRectangle::updatePaintNode(QSGNode *a0,
//      UpdatePaintNodeData *a1)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_ZN15QQuickRectangle15updatePaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QQuickRectangle *self,
    QSGNode *a0,
    QQuickItem::UpdatePaintNodeData *a1) {
  return self->updatePaintNode(a0, a1);
}

//  void QQuickRectangle::doUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickRectangle8doUpdateEv(QQuickRectangle *self) {
  self->doUpdate();
}

//  QQuickRectanglePrivate *QQuickRectangle::d_func()
extern "C" Q_DECL_EXPORT
QQuickRectanglePrivate *ritual_ZN15QQuickRectangle6d_funcEv(
    QQuickRectangle *self) {
  return self->d_func();
}

//  const QQuickRectanglePrivate *QQuickRectangle::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickRectanglePrivate *ritual_ZNK15QQuickRectangle6d_funcEv(
    const QQuickRectangle *self) {
  return self->d_func();
}

//  QSGNode *QQuickRectangle::updatePaintNode(QSGNode *a0,
//      UpdatePaintNodeData *a1)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_own_ZN15QQuickRectangle15updatePaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QQuickRectangle *self,
    QSGNode *a0,
    QQuickItem::UpdatePaintNodeData *a1) {
  return static_cast<OwnQQuickRectangle *>(self)->OwnQQuickRectangle::updatePaintNode(
      a0,
      a1);
}
