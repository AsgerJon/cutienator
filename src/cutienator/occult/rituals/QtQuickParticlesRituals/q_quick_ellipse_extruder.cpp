//  Written by dev_tooling.RitualGenerator from the records of QtQuickParticl
//  es/6.12.0/QtQuickParticles/private/qquickellipseextruder_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuickParticles/6.12.0/QtQuickParticles/private/qtquickparticlesglobal_p.h>
#include <QtQuickParticles/QtQuickParticles>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickParticles/6.12.0/QtQuickParticles/private/qquickellipseextruder_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>

//  const QMetaObject *QQuickEllipseExtruder::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QQuickEllipseExtruder10metaObjectEv(
    const QQuickEllipseExtruder *self) {
  return self->metaObject();
}

//  QString QQuickEllipseExtruder::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QQuickEllipseExtruder2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickEllipseExtruder::tr(s, c, n));
}

//  QQuickEllipseExtruder::QQuickEllipseExtruder(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickEllipseExtruder *ritual_ZN21QQuickEllipseExtruderC1EP7QObject(
    QObject *parent) {
  return new QQuickEllipseExtruder(parent);
}

//  QPointF QQuickEllipseExtruder::extrude(const QRectF &a0)
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZN21QQuickEllipseExtruder7extrudeERK6QRectF(
    QQuickEllipseExtruder *self,
    const QRectF *a0) {
  return new QPointF(self->extrude(*a0));
}

//  bool QQuickEllipseExtruder::contains(const QRectF &bounds, const QPointF
//      &point)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QQuickEllipseExtruder8containsERK6QRectFRK7QPointF(
    QQuickEllipseExtruder *self,
    const QRectF *bounds,
    const QPointF *point) {
  return self->contains(*bounds, *point);
}

//  bool QQuickEllipseExtruder::fill() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQuickEllipseExtruder4fillEv(
    const QQuickEllipseExtruder *self) {
  return self->fill();
}

//  void QQuickEllipseExtruder::setFill(bool arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickEllipseExtruder7setFillEb(
    QQuickEllipseExtruder *self,
    bool arg) {
  self->setFill(arg);
}

//  QPointF QQuickEllipseExtruder::extrude(const QRectF &a0)
extern "C" Q_DECL_EXPORT
QPointF *ritual_own_ZN21QQuickEllipseExtruder7extrudeERK6QRectF(
    QQuickEllipseExtruder *self,
    const QRectF *a0) {
  return new QPointF(self->QQuickEllipseExtruder::extrude(*a0));
}

//  bool QQuickEllipseExtruder::contains(const QRectF &bounds, const QPointF
//      &point)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN21QQuickEllipseExtruder8containsERK6QRectFRK7QPointF(
    QQuickEllipseExtruder *self,
    const QRectF *bounds,
    const QPointF *point) {
  return self->QQuickEllipseExtruder::contains(*bounds, *point);
}
