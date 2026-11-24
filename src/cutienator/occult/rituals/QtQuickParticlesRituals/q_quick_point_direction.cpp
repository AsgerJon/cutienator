//  Written by dev_tooling.RitualGenerator from the records of QtQuickParticl
//  es/6.12.0/QtQuickParticles/private/qquickpointdirection_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuickParticles/6.12.0/QtQuickParticles/private/qtquickparticlesglobal_p.h>
#include <QtQuickParticles/QtQuickParticles>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickParticles/6.12.0/QtQuickParticles/private/qquickpointdirection_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>

//  const QMetaObject *QQuickPointDirection::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QQuickPointDirection10metaObjectEv(
    const QQuickPointDirection *self) {
  return self->metaObject();
}

//  QString QQuickPointDirection::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QQuickPointDirection2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickPointDirection::tr(s, c, n));
}

//  QQuickPointDirection::QQuickPointDirection(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickPointDirection *ritual_ZN20QQuickPointDirectionC1EP7QObject(
    QObject *parent) {
  return new QQuickPointDirection(parent);
}

//  QPointF QQuickPointDirection::sample(const QPointF &from)
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZN20QQuickPointDirection6sampleERK7QPointF(
    QQuickPointDirection *self,
    const QPointF *from) {
  return new QPointF(self->sample(*from));
}

//  qreal QQuickPointDirection::x() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQuickPointDirection1xEv(
    const QQuickPointDirection *self) {
  return self->x();
}

//  qreal QQuickPointDirection::y() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQuickPointDirection1yEv(
    const QQuickPointDirection *self) {
  return self->y();
}

//  qreal QQuickPointDirection::xVariation() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQuickPointDirection10xVariationEv(
    const QQuickPointDirection *self) {
  return self->xVariation();
}

//  qreal QQuickPointDirection::yVariation() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQuickPointDirection10yVariationEv(
    const QQuickPointDirection *self) {
  return self->yVariation();
}

//  void QQuickPointDirection::setX(qreal arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickPointDirection4setXEd(
    QQuickPointDirection *self,
    qreal arg) {
  self->setX(arg);
}

//  void QQuickPointDirection::setY(qreal arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickPointDirection4setYEd(
    QQuickPointDirection *self,
    qreal arg) {
  self->setY(arg);
}

//  void QQuickPointDirection::setXVariation(qreal arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickPointDirection13setXVariationEd(
    QQuickPointDirection *self,
    qreal arg) {
  self->setXVariation(arg);
}

//  void QQuickPointDirection::setYVariation(qreal arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickPointDirection13setYVariationEd(
    QQuickPointDirection *self,
    qreal arg) {
  self->setYVariation(arg);
}

//  QPointF QQuickPointDirection::sample(const QPointF &from)
extern "C" Q_DECL_EXPORT
QPointF *ritual_own_ZN20QQuickPointDirection6sampleERK7QPointF(
    QQuickPointDirection *self,
    const QPointF *from) {
  return new QPointF(self->QQuickPointDirection::sample(*from));
}
