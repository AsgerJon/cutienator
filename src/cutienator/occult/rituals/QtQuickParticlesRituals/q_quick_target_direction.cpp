//  Written by dev_tooling.RitualGenerator from the records of QtQuickParticl
//  es/6.12.0/QtQuickParticles/private/qquicktargetdirection_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuickParticles/6.12.0/QtQuickParticles/private/qtquickparticlesglobal_p.h>
#include <QtQuickParticles/QtQuickParticles>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickParticles/6.12.0/QtQuickParticles/private/qquicktargetdirection_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>

//  const QMetaObject *QQuickTargetDirection::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QQuickTargetDirection10metaObjectEv(
    const QQuickTargetDirection *self) {
  return self->metaObject();
}

//  QString QQuickTargetDirection::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QQuickTargetDirection2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickTargetDirection::tr(s, c, n));
}

//  QQuickTargetDirection::QQuickTargetDirection(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickTargetDirection *ritual_ZN21QQuickTargetDirectionC1EP7QObject(
    QObject *parent) {
  return new QQuickTargetDirection(parent);
}

//  QPointF QQuickTargetDirection::sample(const QPointF &from)
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZN21QQuickTargetDirection6sampleERK7QPointF(
    QQuickTargetDirection *self,
    const QPointF *from) {
  return new QPointF(self->sample(*from));
}

//  qreal QQuickTargetDirection::targetX() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QQuickTargetDirection7targetXEv(
    const QQuickTargetDirection *self) {
  return self->targetX();
}

//  qreal QQuickTargetDirection::targetY() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QQuickTargetDirection7targetYEv(
    const QQuickTargetDirection *self) {
  return self->targetY();
}

//  qreal QQuickTargetDirection::targetVariation() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QQuickTargetDirection15targetVariationEv(
    const QQuickTargetDirection *self) {
  return self->targetVariation();
}

//  qreal QQuickTargetDirection::magnitude() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QQuickTargetDirection9magnitudeEv(
    const QQuickTargetDirection *self) {
  return self->magnitude();
}

//  bool QQuickTargetDirection::proportionalMagnitude() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQuickTargetDirection21proportionalMagnitudeEv(
    const QQuickTargetDirection *self) {
  return self->proportionalMagnitude();
}

//  qreal QQuickTargetDirection::magnitudeVariation() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QQuickTargetDirection18magnitudeVariationEv(
    const QQuickTargetDirection *self) {
  return self->magnitudeVariation();
}

//  QQuickItem *QQuickTargetDirection::targetItem() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK21QQuickTargetDirection10targetItemEv(
    const QQuickTargetDirection *self) {
  return self->targetItem();
}

//  void QQuickTargetDirection::setTargetX(qreal arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickTargetDirection10setTargetXEd(
    QQuickTargetDirection *self,
    qreal arg) {
  self->setTargetX(arg);
}

//  void QQuickTargetDirection::setTargetY(qreal arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickTargetDirection10setTargetYEd(
    QQuickTargetDirection *self,
    qreal arg) {
  self->setTargetY(arg);
}

//  void QQuickTargetDirection::setTargetVariation(qreal arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickTargetDirection18setTargetVariationEd(
    QQuickTargetDirection *self,
    qreal arg) {
  self->setTargetVariation(arg);
}

//  void QQuickTargetDirection::setMagnitude(qreal arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickTargetDirection12setMagnitudeEd(
    QQuickTargetDirection *self,
    qreal arg) {
  self->setMagnitude(arg);
}

//  void QQuickTargetDirection::setProportionalMagnitude(bool arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickTargetDirection24setProportionalMagnitudeEb(
    QQuickTargetDirection *self,
    bool arg) {
  self->setProportionalMagnitude(arg);
}

//  void QQuickTargetDirection::setMagnitudeVariation(qreal arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickTargetDirection21setMagnitudeVariationEd(
    QQuickTargetDirection *self,
    qreal arg) {
  self->setMagnitudeVariation(arg);
}

//  void QQuickTargetDirection::setTargetItem(QQuickItem *arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickTargetDirection13setTargetItemEP10QQuickItem(
    QQuickTargetDirection *self,
    QQuickItem *arg) {
  self->setTargetItem(arg);
}

//  QPointF QQuickTargetDirection::sample(const QPointF &from)
extern "C" Q_DECL_EXPORT
QPointF *ritual_own_ZN21QQuickTargetDirection6sampleERK7QPointF(
    QQuickTargetDirection *self,
    const QPointF *from) {
  return new QPointF(self->QQuickTargetDirection::sample(*from));
}
