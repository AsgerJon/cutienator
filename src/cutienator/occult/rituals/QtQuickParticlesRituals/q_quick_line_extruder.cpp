//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickParticles/6.12.0/QtQuickParticles/private/qquicklineextruder_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuickParticles/6.12.0/QtQuickParticles/private/qtquickparticlesglobal_p.h>
#include <QtQuickParticles/QtQuickParticles>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickParticles/6.12.0/QtQuickParticles/private/qquicklineextruder_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>

//  const QMetaObject *QQuickLineExtruder::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QQuickLineExtruder10metaObjectEv(
    const QQuickLineExtruder *self) {
  return self->metaObject();
}

//  QString QQuickLineExtruder::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QQuickLineExtruder2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickLineExtruder::tr(s, c, n));
}

//  QQuickLineExtruder::QQuickLineExtruder(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickLineExtruder *ritual_ZN18QQuickLineExtruderC1EP7QObject(
    QObject *parent) {
  return new QQuickLineExtruder(parent);
}

//  QPointF QQuickLineExtruder::extrude(const QRectF &a0)
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZN18QQuickLineExtruder7extrudeERK6QRectF(
    QQuickLineExtruder *self,
    const QRectF *a0) {
  return new QPointF(self->extrude(*a0));
}

//  bool QQuickLineExtruder::mirrored() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQuickLineExtruder8mirroredEv(
    const QQuickLineExtruder *self) {
  return self->mirrored();
}

//  void QQuickLineExtruder::setMirrored(bool arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickLineExtruder11setMirroredEb(
    QQuickLineExtruder *self,
    bool arg) {
  self->setMirrored(arg);
}

//  QPointF QQuickLineExtruder::extrude(const QRectF &a0)
extern "C" Q_DECL_EXPORT
QPointF *ritual_own_ZN18QQuickLineExtruder7extrudeERK6QRectF(
    QQuickLineExtruder *self,
    const QRectF *a0) {
  return new QPointF(self->QQuickLineExtruder::extrude(*a0));
}
