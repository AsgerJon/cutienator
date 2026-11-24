//  Written by dev_tooling.RitualGenerator from the records of QtQuickParticl
//  es/6.12.0/QtQuickParticles/private/qquickcumulativedirection_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuickParticles/6.12.0/QtQuickParticles/private/qtquickparticlesglobal_p.h>
#include <QtQuickParticles/QtQuickParticles>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickParticles/6.12.0/QtQuickParticles/private/qquickcumulativedirection_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>

//  const QMetaObject *QQuickCumulativeDirection::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK25QQuickCumulativeDirection10metaObjectEv(
    const QQuickCumulativeDirection *self) {
  return self->metaObject();
}

//  QString QQuickCumulativeDirection::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN25QQuickCumulativeDirection2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickCumulativeDirection::tr(s, c, n));
}

//  QQuickCumulativeDirection::QQuickCumulativeDirection(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickCumulativeDirection *ritual_ZN25QQuickCumulativeDirectionC1EP7QObject(
    QObject *parent) {
  return new QQuickCumulativeDirection(parent);
}

//  QPointF QQuickCumulativeDirection::sample(const QPointF &from)
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZN25QQuickCumulativeDirection6sampleERK7QPointF(
    QQuickCumulativeDirection *self,
    const QPointF *from) {
  return new QPointF(self->sample(*from));
}

//  QPointF QQuickCumulativeDirection::sample(const QPointF &from)
extern "C" Q_DECL_EXPORT
QPointF *ritual_own_ZN25QQuickCumulativeDirection6sampleERK7QPointF(
    QQuickCumulativeDirection *self,
    const QPointF *from) {
  return new QPointF(self->QQuickCumulativeDirection::sample(*from));
}
