//  Written by dev_tooling.RitualGenerator from the records of QtQuickParticl
//  es/6.12.0/QtQuickParticles/private/qquickangledirection_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuickParticles/6.12.0/QtQuickParticles/private/qtquickparticlesglobal_p.h>
#include <QtQuickParticles/QtQuickParticles>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickParticles/6.12.0/QtQuickParticles/private/qquickangledirection_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>

//  const QMetaObject *QQuickAngleDirection::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QQuickAngleDirection10metaObjectEv(
    const QQuickAngleDirection *self) {
  return self->metaObject();
}

//  QString QQuickAngleDirection::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QQuickAngleDirection2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickAngleDirection::tr(s, c, n));
}

//  QQuickAngleDirection::QQuickAngleDirection(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickAngleDirection *ritual_ZN20QQuickAngleDirectionC1EP7QObject(
    QObject *parent) {
  return new QQuickAngleDirection(parent);
}

//  QPointF QQuickAngleDirection::sample(const QPointF &from)
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZN20QQuickAngleDirection6sampleERK7QPointF(
    QQuickAngleDirection *self,
    const QPointF *from) {
  return new QPointF(self->sample(*from));
}

//  qreal QQuickAngleDirection::angle() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQuickAngleDirection5angleEv(
    const QQuickAngleDirection *self) {
  return self->angle();
}

//  qreal QQuickAngleDirection::magnitude() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQuickAngleDirection9magnitudeEv(
    const QQuickAngleDirection *self) {
  return self->magnitude();
}

//  qreal QQuickAngleDirection::angleVariation() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQuickAngleDirection14angleVariationEv(
    const QQuickAngleDirection *self) {
  return self->angleVariation();
}

//  qreal QQuickAngleDirection::magnitudeVariation() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQuickAngleDirection18magnitudeVariationEv(
    const QQuickAngleDirection *self) {
  return self->magnitudeVariation();
}

//  void QQuickAngleDirection::setAngle(qreal arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAngleDirection8setAngleEd(
    QQuickAngleDirection *self,
    qreal arg) {
  self->setAngle(arg);
}

//  void QQuickAngleDirection::setMagnitude(qreal arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAngleDirection12setMagnitudeEd(
    QQuickAngleDirection *self,
    qreal arg) {
  self->setMagnitude(arg);
}

//  void QQuickAngleDirection::setAngleVariation(qreal arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAngleDirection17setAngleVariationEd(
    QQuickAngleDirection *self,
    qreal arg) {
  self->setAngleVariation(arg);
}

//  void QQuickAngleDirection::setMagnitudeVariation(qreal arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAngleDirection21setMagnitudeVariationEd(
    QQuickAngleDirection *self,
    qreal arg) {
  self->setMagnitudeVariation(arg);
}

//  QPointF QQuickAngleDirection::sample(const QPointF &from)
extern "C" Q_DECL_EXPORT
QPointF *ritual_own_ZN20QQuickAngleDirection6sampleERK7QPointF(
    QQuickAngleDirection *self,
    const QPointF *from) {
  return new QPointF(self->QQuickAngleDirection::sample(*from));
}
